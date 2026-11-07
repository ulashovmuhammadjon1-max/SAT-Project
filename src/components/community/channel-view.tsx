"use client";

import { Fragment, useCallback, useEffect, useRef, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import Link from "next/link";
import { ArrowDown, Bell, BellOff, Loader2, Pin, Search, X } from "lucide-react";
import { toast } from "sonner";

import { useLive, useLiveScope } from "@/components/live/live-provider";
import type { ChannelView as Channel, CommunityMessageView } from "@/lib/community/types";
import { cn } from "@/lib/utils";
import {
  listMessages,
  listPinned,
  locateMessage,
  markChannelRead,
  setChannelMuted,
} from "@/server/actions/student/community";
import { markNotificationsForMessage } from "@/server/actions/student/notifications";

import { ChannelIcon, dayLabel, useMounted } from "./bits";
import { Composer, type ReplyTarget } from "./composer";
import { MessageItem } from "./message-item";
import { NavToggle } from "./community-shell";
import { ThreadPanel } from "./thread-panel";

const GROUP_GAP_MS = 5 * 60_000;

export function ChannelView({
  channel,
  initialMessages,
  initialHasMore,
  initialPinned,
  isAdmin,
  restriction,
  initialThread,
  focusMessage,
  initialKind,
}: {
  channel: Channel;
  initialMessages: CommunityMessageView[];
  initialHasMore: boolean;
  initialPinned: CommunityMessageView[];
  isAdmin: boolean;
  restriction: { until: string; reason: string } | null;
  initialThread: string | null;
  focusMessage: string | null;
  initialKind?: import("@/lib/community/types").MessageKind;
}) {
  const router = useRouter();
  const pathname = usePathname();
  const { data, pokeNow } = useLive();
  const [messages, setMessages] = useState(initialMessages);
  const [hasMore, setHasMore] = useState(initialHasMore);
  const [loadingMore, setLoadingMore] = useState(false);
  const [pinned, setPinned] = useState(initialPinned);
  const [showPinned, setShowPinned] = useState(false);
  const [replyTo, setReplyTo] = useState<ReplyTarget | null>(null);
  const [thread, setThread] = useState<{ id: string; focus: string | null } | null>(
    initialThread ? { id: initialThread, focus: focusMessage } : null,
  );
  const [highlight, setHighlight] = useState<string | null>(initialThread ? null : focusMessage);
  const [muted, setMuted] = useState(channel.muted);
  const [newBelow, setNewBelow] = useState(0);

  useLiveScope({ channel: channel.slug, thread: thread?.id ?? null });
  const mounted = useMounted();

  const scroller = useRef<HTMLDivElement>(null);
  const atBottom = useRef(true);
  const lastVersion = useRef<string | null>(null);

  const scrollToBottom = useCallback((smooth = false) => {
    const el = scroller.current;
    if (el) el.scrollTo({ top: el.scrollHeight, behavior: smooth ? "smooth" : "auto" });
    setNewBelow(0);
  }, []);

  // First paint: jump to a linked message, or to the newest one.
  useEffect(() => {
    if (focusMessage && !initialThread) {
      const go = () => {
        const el = document.getElementById(`msg-${focusMessage}`);
        if (el) {
          el.scrollIntoView({ block: "center" });
          atBottom.current = false;
        } else scrollToBottom();
      };
      if (!initialMessages.some((m) => m.id === focusMessage)) {
        void listMessages(channel.slug, { around: focusMessage }).then((r) => {
          setMessages(r.messages);
          setHasMore(r.hasMore);
          requestAnimationFrame(go);
        });
      } else requestAnimationFrame(go);
      void markNotificationsForMessage(focusMessage);
    } else {
      requestAnimationFrame(() => scrollToBottom());
    }
    void markChannelRead(channel.slug);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [channel.slug]);

  const refresh = useCallback(async () => {
    const r = await listMessages(channel.slug);
    setMessages((prev) => {
      // Keep any older history the reader already loaded.
      const firstNew = r.messages[0];
      const olderKept = firstNew ? prev.filter((m) => new Date(m.createdAt) < new Date(firstNew.createdAt)) : [];
      const added = r.messages.filter((m) => !prev.some((p) => p.id === m.id)).length;
      if (!atBottom.current && added > 0) setNewBelow((n) => n + added);
      return [...olderKept, ...r.messages];
    });
    if (atBottom.current) requestAnimationFrame(() => scrollToBottom(true));
    if (document.visibilityState === "visible") void markChannelRead(channel.slug);
    setPinned(await listPinned(channel.slug));
  }, [channel.slug, scrollToBottom]);

  useEffect(() => {
    const on = () => void refresh();
    window.addEventListener("community:refresh", on);
    return () => window.removeEventListener("community:refresh", on);
  }, [refresh]);

  // Live: refetch when the channel's version stamp moves.
  useEffect(() => {
    const v = data?.channelVersion ?? null;
    if (!v) return;
    if (lastVersion.current && v !== lastVersion.current) void refresh();
    lastVersion.current = v;
  }, [data?.channelVersion, refresh]);

  // Keep the URL in step with the open discussion, so it can be shared and
  // the back button closes it.
  const openThread = useCallback(
    (id: string | null, focus: string | null = null) => {
      setThread(id ? { id, focus } : null);
      // history.replaceState (not router.replace): the URL stays shareable and
      // in sync with useSearchParams, without a server round trip that would
      // remount the channel and lose its scroll position.
      const url = id ? `${pathname}?thread=${id}${focus ? `&m=${focus}` : ""}` : pathname;
      window.history.replaceState(window.history.state, "", url);
    },
    [pathname],
  );

  const onRootChanged = useCallback((root: CommunityMessageView) => {
    setMessages((prev) => prev.map((m) => (m.id === root.id ? { ...m, ...root } : m)));
  }, []);

  async function loadOlder() {
    const oldest = messages[0];
    if (!oldest || loadingMore) return;
    setLoadingMore(true);
    const el = scroller.current;
    const before = el?.scrollHeight ?? 0;
    const r = await listMessages(channel.slug, { before: oldest.id });
    setMessages((prev) => [...r.messages, ...prev]);
    setHasMore(r.hasMore);
    setLoadingMore(false);
    requestAnimationFrame(() => {
      if (el) el.scrollTop = el.scrollHeight - before;
    });
  }

  const patch = (id: string, p: Partial<CommunityMessageView>) => {
    setMessages((prev) => prev.map((m) => (m.id === id ? { ...m, ...p } : m)));
    if ("pinned" in p) void listPinned(channel.slug).then(setPinned);
  };

  async function jump(id: string, threadRootId: string | null) {
    if (threadRootId) return openThread(threadRootId, id);
    let el = document.getElementById(`msg-${id}`);
    if (!el) {
      const loc = await locateMessage(id);
      if (!loc) return void toast.error("That message is no longer available.");
      if (loc.channelSlug !== channel.slug) return router.push(`/community/${loc.channelSlug}?m=${id}`);
      const r = await listMessages(channel.slug, { around: id });
      setMessages(r.messages);
      setHasMore(r.hasMore);
      await new Promise((res) => requestAnimationFrame(res));
      el = document.getElementById(`msg-${id}`);
    }
    el?.scrollIntoView({ behavior: "smooth", block: "center" });
    setHighlight(null);
    requestAnimationFrame(() => setHighlight(id));
  }

  const handlers = {
    onPatch: patch,
    onReply: (m: CommunityMessageView) => setReplyTo({ id: m.id, authorName: m.author.name, excerpt: m.title ?? (m.body.slice(0, 80) || "attachment") }),
    onOpenThread: (m: CommunityMessageView) => openThread(m.id),
    onJump: (id: string, root: string | null) => void jump(id, root),
    onChanged: () => void refresh(),
  };

  const disabledReason = restriction
    ? `A moderator has paused your posting until ${mounted ? new Date(restriction.until).toLocaleString() : "later"}.`
    : channel.isReadOnly && !isAdmin
      ? "Only the Scholarly team posts in this channel. You'll be notified of new posts."
      : null;

  return (
    <div className="flex min-h-0 min-w-0 flex-1">
      <section className="flex min-h-0 min-w-0 flex-1 flex-col">
        <header className="flex h-14 shrink-0 items-center gap-2 border-b border-border bg-background/70 px-3 backdrop-blur sm:px-5">
          <NavToggle />
          <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
            <ChannelIcon icon={channel.icon} />
          </span>
          <div className="min-w-0 flex-1">
            <h1 className="truncate font-display text-[15px] font-semibold leading-tight">{channel.name}</h1>
            {channel.description && <p className="hidden truncate text-xs text-muted-foreground sm:block">{channel.description}</p>}
          </div>
          <div className="flex items-center gap-0.5">
            {pinned.length > 0 && (
              <button
                type="button"
                onClick={() => setShowPinned((v) => !v)}
                className={cn("flex h-9 items-center gap-1 rounded-lg px-2.5 text-xs font-medium", showPinned ? "bg-primary/10 text-primary" : "text-muted-foreground hover:bg-secondary hover:text-foreground")}
                aria-expanded={showPinned}
              >
                <Pin className="h-4 w-4" /> <span className="tabular-nums">{pinned.length}</span>
              </button>
            )}
            <button
              type="button"
              title={muted ? "Unmute channel" : "Mute channel"}
              aria-label={muted ? "Unmute channel" : "Mute channel"}
              onClick={async () => {
                const r = await setChannelMuted(channel.slug, !muted);
                if (!r.ok) return void toast.error(r.error);
                setMuted(!muted);
                toast.success(!muted ? `#${channel.name} muted. Direct replies and mentions still reach you.` : `#${channel.name} unmuted.`);
                pokeNow();
              }}
              className="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary hover:text-foreground"
            >
              {muted ? <BellOff className="h-4 w-4" /> : <Bell className="h-4 w-4" />}
            </button>
            <Link href={`/community/search?channel=${channel.slug}`} aria-label="Search this channel" className="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary hover:text-foreground">
              <Search className="h-4 w-4" />
            </Link>
          </div>
        </header>

        {showPinned && pinned.length > 0 && (
          <div className="max-h-72 shrink-0 overflow-y-auto border-b border-border bg-secondary/30 animate-fade-in">
            <div className="flex items-center justify-between px-5 pt-3">
              <p className="flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                <Pin className="h-3.5 w-3.5" /> Pinned
              </p>
              <button type="button" onClick={() => setShowPinned(false)} aria-label="Close pinned" className="rounded p-1 text-muted-foreground hover:bg-secondary">
                <X className="h-3.5 w-3.5" />
              </button>
            </div>
            {pinned.map((p) => (
              <button key={p.id} type="button" onClick={() => { setShowPinned(false); void jump(p.id, null); }} className="block w-full px-5 py-2 text-left hover:bg-secondary/60">
                <span className="text-xs font-semibold">{p.author.name}</span>
                <span className="ml-2 line-clamp-1 text-sm text-muted-foreground">{p.title ?? p.body}</span>
              </button>
            ))}
          </div>
        )}

        <div
          ref={scroller}
          onScroll={() => {
            const el = scroller.current;
            if (!el) return;
            atBottom.current = el.scrollHeight - el.scrollTop - el.clientHeight < 120;
            if (atBottom.current && newBelow) setNewBelow(0);
          }}
          className="relative min-h-0 flex-1 overflow-y-auto overflow-x-hidden pb-6"
        >
          {hasMore ? (
            <div className="flex justify-center py-3">
              <button
                type="button"
                onClick={() => void loadOlder()}
                disabled={loadingMore}
                className="inline-flex items-center gap-2 rounded-full border border-border bg-background px-4 py-1.5 text-xs font-medium text-muted-foreground hover:text-foreground"
              >
                {loadingMore && <Loader2 className="h-3.5 w-3.5 animate-spin" />} Load earlier messages
              </button>
            </div>
          ) : (
            <ChannelIntro channel={channel} empty={messages.length === 0} />
          )}

          {messages.map((m, i) => {
            const prev = messages[i - 1];
            // Day boundaries are the reader's local days, so they are drawn only
            // in the browser (the server does not know the reader's timezone).
            const newDay = mounted && (!prev || new Date(prev.createdAt).toDateString() !== new Date(m.createdAt).toDateString());
            const grouped =
              !newDay &&
              Boolean(prev) &&
              prev.author.id === m.author.id &&
              !m.replyTo &&
              m.kind === "MESSAGE" &&
              prev.kind === "MESSAGE" &&
              new Date(m.createdAt).getTime() - new Date(prev.createdAt).getTime() < GROUP_GAP_MS;
            return (
              <Fragment key={m.id}>
                {newDay && (
                  <div className="sticky top-0 z-[5] flex items-center gap-3 px-5 py-2">
                    <span className="h-px flex-1 bg-border" />
                    <span className="rounded-full border border-border bg-background/90 px-3 py-0.5 text-[11px] font-semibold uppercase tracking-wider text-muted-foreground backdrop-blur">
                      {dayLabel(m.createdAt)}
                    </span>
                    <span className="h-px flex-1 bg-border" />
                  </div>
                )}
                <MessageItem message={m} grouped={grouped} handlers={handlers} highlight={highlight === m.id} />
              </Fragment>
            );
          })}
        </div>

        {newBelow > 0 && (
          <div className="pointer-events-none relative">
            <button
              type="button"
              onClick={() => scrollToBottom(true)}
              className="pointer-events-auto absolute -top-12 left-1/2 flex -translate-x-1/2 items-center gap-1.5 rounded-full bg-primary px-4 py-1.5 text-xs font-semibold text-primary-foreground shadow-lg animate-badge-bump"
            >
              <ArrowDown className="h-3.5 w-3.5" /> {newBelow} new {newBelow === 1 ? "message" : "messages"}
            </button>
          </div>
        )}

        <Composer
          channelSlug={channel.slug}
          channelName={channel.name}
          disabled={Boolean(disabledReason)}
          disabledReason={disabledReason}
          isAdmin={isAdmin}
          slowModeSeconds={channel.slowModeSeconds}
          initialKind={initialKind}
          replyTo={replyTo}
          onCancelReply={() => setReplyTo(null)}
          onPosted={() => {
            atBottom.current = true;
            void refresh();
            pokeNow();
          }}
        />
      </section>

      {thread && (
        <ThreadPanel
          key={thread.id}
          rootId={thread.id}
          focusId={thread.focus}
          isAdmin={isAdmin}
          disabledReason={restriction ? disabledReason : null}
          onClose={() => openThread(null)}
          onRootChanged={onRootChanged}
        />
      )}
    </div>
  );
}

function ChannelIntro({ channel, empty }: { channel: Channel; empty: boolean }) {
  return (
    <div className="px-5 pb-4 pt-10 sm:px-8">
      <span className="flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-primary/20 to-accent text-primary shadow-sm">
        <ChannelIcon icon={channel.icon} className="h-7 w-7" />
      </span>
      <h2 className="mt-4 font-serif text-3xl font-medium tracking-tight">Welcome to #{channel.name}</h2>
      <p className="mt-1.5 max-w-xl text-[15px] text-muted-foreground">
        {channel.description ?? "This is the very beginning of the channel."}
        {empty && " Nothing has been posted yet — start the first conversation."}
      </p>
    </div>
  );
}
