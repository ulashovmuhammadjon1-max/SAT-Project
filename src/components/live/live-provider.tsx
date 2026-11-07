"use client";

import { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import { toast } from "sonner";

import type { SyncPayload } from "@/lib/community/types";
import { listNotifications } from "@/server/actions/student/notifications";

/**
 * Live updates for the whole signed-in app.
 *
 * One poller per tab hits /api/community/sync, which returns version stamps,
 * not data. Components that care (the bell, an open channel, a thread, a
 * conversation) watch the stamp they need and fetch only when it moves.
 *
 * Pace adapts to what the student is doing:
 *   - looking at a channel/thread/conversation and recently active: every 3s
 *   - looking at one but idle: every 10s
 *   - anywhere else: every 15s (30s once idle)
 *   - hidden tab: stops — unless browser notifications are on, then once a
 *     minute so the alert can still fire
 * A visible tab polls immediately on focus and on reconnecting, and backs off
 * after errors. Counts are shared with other open tabs over BroadcastChannel,
 * so two tabs never disagree about the badge.
 *
 * The same request is the presence heartbeat (`beat`, every 30s) that the
 * email system uses to decide whether a student is here right now.
 */

export interface LiveScope {
  channel?: string | null;
  thread?: string | null;
  conversation?: string | null;
}

interface LiveContextValue {
  data: SyncPayload | null;
  setScope: (key: string, scope: LiveScope | null) => void;
  /** Poll now (after the student posts, for example). */
  pokeNow: () => void;
  browserNotify: boolean;
  setBrowserNotify: (on: boolean) => void;
}

const LiveContext = createContext<LiveContextValue | null>(null);

const BROWSER_KEY = "scholarly-browser-notify";
const SHOWN_KEY = "scholarly-last-alert";

export function useLive(): LiveContextValue {
  const ctx = useContext(LiveContext);
  if (!ctx) {
    return { data: null, setScope: () => {}, pokeNow: () => {}, browserNotify: false, setBrowserNotify: () => {} };
  }
  return ctx;
}

/** Register what this component is looking at for as long as it is mounted. */
export function useLiveScope(scope: LiveScope) {
  const { setScope } = useLive();
  const key = useRef(`s${Math.random().toString(36).slice(2)}`).current;
  const { channel, thread, conversation } = scope;
  useEffect(() => {
    setScope(key, { channel, thread, conversation });
    return () => setScope(key, null);
  }, [key, setScope, channel, thread, conversation]);
}

export function LiveProvider({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const pathname = usePathname();
  const [data, setData] = useState<SyncPayload | null>(null);
  const [browserNotify, setBrowserNotifyState] = useState(false);

  const scopes = useRef(new Map<string, LiveScope>());
  const lastInteraction = useRef(Date.now());
  const lastBeat = useRef(0);
  const failures = useRef(0);
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const inFlight = useRef(false);
  const prev = useRef<SyncPayload | null>(null);
  const channel = useRef<BroadcastChannel | null>(null);
  const pathRef = useRef(pathname);
  pathRef.current = pathname;

  useEffect(() => {
    try {
      setBrowserNotifyState(localStorage.getItem(BROWSER_KEY) === "1" && Notification.permission === "granted");
    } catch {
      /* no storage or no Notification API */
    }
  }, []);

  const setBrowserNotify = useCallback((on: boolean) => {
    setBrowserNotifyState(on);
    try {
      localStorage.setItem(BROWSER_KEY, on ? "1" : "0");
    } catch {
      /* ignore */
    }
  }, []);

  const merged = useCallback((): LiveScope => {
    const s: LiveScope = {};
    for (const v of scopes.current.values()) {
      s.channel = v.channel ?? s.channel;
      s.thread = v.thread ?? s.thread;
      s.conversation = v.conversation ?? s.conversation;
    }
    return s;
  }, []);

  /** React to a payload: toast or browser alert for something new. */
  const announce = useCallback(
    async (next: SyncPayload) => {
      const before = prev.current;
      prev.current = next;
      if (!before) return;
      const newer =
        next.latestNotificationAt &&
        (!before.latestNotificationAt || next.latestNotificationAt > before.latestNotificationAt) &&
        next.notificationsUnread > 0;
      if (!newer) return;

      const { items } = await listNotifications({ filter: "unread", take: 1 });
      const n = items[0];
      if (!n) return;
      let lastShown = "";
      try {
        lastShown = localStorage.getItem(SHOWN_KEY) ?? "";
      } catch {
        /* ignore */
      }
      if (lastShown === `${n.id}:${n.createdAt}`) return; // another tab showed it
      try {
        localStorage.setItem(SHOWN_KEY, `${n.id}:${n.createdAt}`);
      } catch {
        /* ignore */
      }
      // Already looking at it: no need to interrupt.
      const [targetPath, targetQuery = ""] = n.url.split("?");
      const targetThread = new URLSearchParams(targetQuery).get("thread");
      const openThread = new URLSearchParams(window.location.search).get("thread");
      const here =
        targetPath === pathRef.current &&
        (!targetThread || targetThread === openThread) &&
        document.visibilityState === "visible";
      if (document.visibilityState === "visible" && !here) {
        toast(n.title, {
          description: n.body,
          action: { label: "View", onClick: () => router.push(n.url) },
          duration: 7000,
        });
      } else if (document.visibilityState !== "visible" && browserNotify) {
        try {
          const alert = new Notification(n.title, { body: n.body, tag: n.id, icon: "/icon" });
          alert.onclick = () => {
            window.focus();
            router.push(n.url);
            alert.close();
          };
        } catch {
          /* blocked or unsupported */
        }
      }
    },
    [browserNotify, router],
  );

  const poll = useCallback(async () => {
    if (inFlight.current) return;
    inFlight.current = true;
    try {
      const visible = document.visibilityState === "visible";
      const s = merged();
      const q = new URLSearchParams();
      if (s.channel) q.set("c", s.channel);
      if (s.thread) q.set("t", s.thread);
      if (s.conversation) q.set("d", s.conversation);
      if (visible && Date.now() - lastBeat.current > 30_000) {
        q.set("beat", "1");
        if (Date.now() - lastInteraction.current < 60_000) q.set("active", "1");
        lastBeat.current = Date.now();
      }
      const res = await fetch(`/api/community/sync?${q}`, { cache: "no-store" });
      if (!res.ok) throw new Error(String(res.status));
      const body = (await res.json()) as SyncPayload;
      failures.current = 0;
      setData(body);
      channel.current?.postMessage({ type: "counts", notificationsUnread: body.notificationsUnread, dmUnread: body.dmUnread });
      void announce(body);
    } catch {
      failures.current = Math.min(failures.current + 1, 6);
    } finally {
      inFlight.current = false;
    }
  }, [announce, merged]);

  const schedule = useCallback(() => {
    if (timer.current) clearTimeout(timer.current);
    const visible = document.visibilityState === "visible";
    const s = merged();
    const focused = Boolean(s.channel || s.thread || s.conversation);
    const recent = Date.now() - lastInteraction.current < 120_000;
    let delay = focused ? (recent ? 3000 : 10_000) : recent ? 15_000 : 30_000;
    if (!visible) delay = browserNotify ? 60_000 : -1;
    if (failures.current > 0) delay = Math.max(delay, Math.min(60_000, 2000 * 2 ** failures.current));
    if (delay < 0) return; // paused until the tab is visible again
    timer.current = setTimeout(async () => {
      await poll();
      schedule();
    }, delay);
  }, [browserNotify, merged, poll]);

  const pokeNow = useCallback(() => {
    void poll().then(schedule);
  }, [poll, schedule]);

  const setScope = useCallback(
    (key: string, scope: LiveScope | null) => {
      if (scope) scopes.current.set(key, scope);
      else scopes.current.delete(key);
      pokeNow();
    },
    [pokeNow],
  );

  useEffect(() => {
    const mark = () => {
      lastInteraction.current = Date.now();
    };
    const onVisible = () => {
      if (document.visibilityState === "visible") {
        lastBeat.current = 0; // report presence straight away
        pokeNow();
      } else schedule();
    };
    const opts = { passive: true } as const;
    window.addEventListener("pointerdown", mark, opts);
    window.addEventListener("keydown", mark, opts);
    window.addEventListener("wheel", mark, opts);
    window.addEventListener("touchstart", mark, opts);
    window.addEventListener("focus", onVisible);
    window.addEventListener("online", pokeNow);
    document.addEventListener("visibilitychange", onVisible);

    try {
      channel.current = new BroadcastChannel("scholarly-live");
      channel.current.onmessage = (e: MessageEvent) => {
        if (e.data?.type === "counts") {
          setData((d) => (d ? { ...d, notificationsUnread: e.data.notificationsUnread, dmUnread: e.data.dmUnread } : d));
        }
        if (e.data?.type === "read") pokeNow();
      };
    } catch {
      /* old browser: each tab polls on its own */
    }

    pokeNow();
    return () => {
      if (timer.current) clearTimeout(timer.current);
      window.removeEventListener("pointerdown", mark);
      window.removeEventListener("keydown", mark);
      window.removeEventListener("wheel", mark);
      window.removeEventListener("touchstart", mark);
      window.removeEventListener("focus", onVisible);
      window.removeEventListener("online", pokeNow);
      document.removeEventListener("visibilitychange", onVisible);
      channel.current?.close();
    };
  }, [pokeNow, schedule]);

  const value = useMemo(
    () => ({ data, setScope, pokeNow, browserNotify, setBrowserNotify }),
    [data, setScope, pokeNow, browserNotify, setBrowserNotify],
  );
  return <LiveContext.Provider value={value}>{children}</LiveContext.Provider>;
}

/** Tell other tabs that something was read, so their badges drop too. */
export function broadcastRead() {
  try {
    const c = new BroadcastChannel("scholarly-live");
    c.postMessage({ type: "read" });
    c.close();
  } catch {
    /* ignore */
  }
}
