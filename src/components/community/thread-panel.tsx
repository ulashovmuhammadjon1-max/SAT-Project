"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { Bell, BellOff, Loader2, MessagesSquare, X } from "lucide-react";
import { toast } from "sonner";

import { useLive } from "@/components/live/live-provider";
import type { CommunityMessageView } from "@/lib/community/types";
import { cn } from "@/lib/utils";
import { getThread, setFollow } from "@/server/actions/student/community";
import { markNotificationsForMessage } from "@/server/actions/student/notifications";

import { Composer, type ReplyTarget } from "./composer";
import { MessageItem } from "./message-item";

/**
 * A discussion beside the channel (a full-screen sheet on phones). The root
 * post stays on top; replies stay together instead of scattering through the
 * main stream.
 */
export function ThreadPanel({
  rootId,
  focusId,
  isAdmin,
  disabledReason,
  onClose,
  onRootChanged,
}: {
  rootId: string;
  focusId?: string | null;
  isAdmin: boolean;
  disabledReason: string | null;
  onClose: () => void;
  onRootChanged: (root: CommunityMessageView) => void;
}) {
  const { data, pokeNow } = useLive();
  const [state, setState] = useState<Awaited<ReturnType<typeof getThread>> | undefined>(undefined);
  const [replyTo, setReplyTo] = useState<ReplyTarget | null>(null);
  const [highlight, setHighlight] = useState<string | null>(focusId ?? null);
  const scroller = useRef<HTMLDivElement>(null);
  const atBottom = useRef(true);
  const lastVersion = useRef<string | null>(null);

  const load = useCallback(async () => {
    const t = await getThread(rootId);
    setState(t);
    if (t) onRootChanged(t.root);
    return t;
  }, [rootId, onRootChanged]);

  useEffect(() => {
    setState(undefined);
    lastVersion.current = null;
    void load().then((t) => {
      requestAnimationFrame(() => {
        const target = focusId ? document.getElementById(`msg-${focusId}`) : null;
        if (target) target.scrollIntoView({ block: "center" });
        else if (scroller.current) scroller.current.scrollTop = scroller.current.scrollHeight;
      });
      if (t) void markNotificationsForMessage(rootId);
      if (focusId) void markNotificationsForMessage(focusId);
    });
  }, [rootId, focusId, load]);

  useEffect(() => {
    const v = data?.threadVersion ?? null;
    if (!v) return;
    if (lastVersion.current && v !== lastVersion.current) {
      void load().then(() => {
        if (atBottom.current) requestAnimationFrame(() => scroller.current?.scrollTo({ top: scroller.current.scrollHeight, behavior: "smooth" }));
      });
    }
    lastVersion.current = v;
  }, [data?.threadVersion, load]);

  useEffect(() => {
    const on = () => void load();
    window.addEventListener("community:refresh", on);
    return () => window.removeEventListener("community:refresh", on);
  }, [load]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [onClose]);

  const patch = (id: string, p: Partial<CommunityMessageView>) =>
    setState((s) =>
      s
        ? {
            ...s,
            root: s.root.id === id ? { ...s.root, ...p } : s.root,
            replies: s.replies.map((r) => (r.id === id ? { ...r, ...p } : r)),
          }
        : s,
    );

  const handlers = {
    onPatch: patch,
    onReply: (m: CommunityMessageView) => setReplyTo({ id: m.id, authorName: m.author.name, excerpt: m.title ?? (m.body.slice(0, 80) || "attachment") }),
    onJump: (id: string) => {
      const el = document.getElementById(`msg-${id}`);
      if (el) {
        el.scrollIntoView({ behavior: "smooth", block: "center" });
        setHighlight(null);
        requestAnimationFrame(() => setHighlight(id));
      }
    },
    onChanged: () => void load(),
  };

  const following = state?.root.following;

  return (
    <aside
      aria-label="Discussion"
      className="fixed inset-0 z-40 flex flex-col bg-background animate-slide-in-right lg:static lg:z-auto lg:w-[27rem] lg:shrink-0 lg:border-l lg:border-border lg:bg-card/40"
    >
      <header className="flex h-14 shrink-0 items-center gap-2 border-b border-border px-4">
        <MessagesSquare className="h-4 w-4 text-primary" />
        <div className="min-w-0 flex-1">
          <p className="truncate font-display text-sm font-semibold">{state?.root.kind === "QUESTION" ? "Question & answers" : "Discussion"}</p>
          {state && <p className="truncate text-xs text-muted-foreground">#{state.channel.name} · {state.replies.length} {state.replies.length === 1 ? "reply" : "replies"}</p>}
        </div>
        {state && (
          <button
            type="button"
            onClick={async () => {
              const next = following === "FOLLOWING" ? "MUTED" : "FOLLOWING";
              const r = await setFollow(rootId, next);
              if (!r.ok) return void toast.error(r.error);
              patch(rootId, { following: next });
              toast.success(next === "FOLLOWING" ? "Following — you'll be notified of replies." : "Muted — no more notifications from this discussion.");
            }}
            className={cn(
              "flex h-8 items-center gap-1.5 rounded-lg border px-2.5 text-xs font-medium transition-colors",
              following === "FOLLOWING" ? "border-primary/40 bg-primary/10 text-primary" : "border-border text-muted-foreground hover:text-foreground",
            )}
          >
            {following === "FOLLOWING" ? <Bell className="h-3.5 w-3.5" /> : <BellOff className="h-3.5 w-3.5" />}
            {following === "FOLLOWING" ? "Following" : following === "MUTED" ? "Muted" : "Follow"}
          </button>
        )}
        <button type="button" onClick={onClose} aria-label="Close discussion" className="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary hover:text-foreground">
          <X className="h-5 w-5" />
        </button>
      </header>

      <div
        ref={scroller}
        onScroll={() => {
          const el = scroller.current;
          if (el) atBottom.current = el.scrollHeight - el.scrollTop - el.clientHeight < 80;
        }}
        className="min-h-0 flex-1 overflow-y-auto pb-4"
      >
        {state === undefined ? (
          <div className="flex justify-center py-16">
            <Loader2 className="h-5 w-5 animate-spin text-muted-foreground" />
          </div>
        ) : state === null ? (
          <p className="px-6 py-16 text-center text-sm text-muted-foreground">This discussion is no longer available.</p>
        ) : (
          <>
            <div className="border-b border-border bg-background/60 pb-3">
              <MessageItem message={state.root} context="root" handlers={handlers} highlight={highlight === state.root.id} />
            </div>
            <div className="flex items-center gap-3 px-4 pt-4">
              <span className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                {state.replies.length} {state.replies.length === 1 ? "reply" : "replies"}
              </span>
              <span className="h-px flex-1 bg-border" />
            </div>
            {state.replies.length === 0 ? (
              <p className="px-6 py-10 text-center text-sm text-muted-foreground">
                {state.root.kind === "QUESTION" ? "No answers yet. Be the first to help." : "No replies yet. Start the discussion."}
              </p>
            ) : (
              state.replies.map((r, i) => (
                <MessageItem
                  key={r.id}
                  message={r}
                  context="thread"
                  handlers={handlers}
                  highlight={highlight === r.id}
                  grouped={i > 0 && state.replies[i - 1].author.id === r.author.id && !r.replyTo && new Date(r.createdAt).getTime() - new Date(state.replies[i - 1].createdAt).getTime() < 5 * 60_000}
                />
              ))
            )}
          </>
        )}
      </div>

      {state && (
        <Composer
          channelSlug={state.channel.slug}
          channelName={state.channel.name}
          threadRootId={rootId}
          disabled={Boolean(disabledReason) || (state.channel.isReadOnly && !isAdmin)}
          disabledReason={disabledReason ?? "Only the Scholarly team posts in this channel."}
          isAdmin={isAdmin}
          replyTo={replyTo}
          onCancelReply={() => setReplyTo(null)}
          placeholder={state.root.kind === "QUESTION" ? "Write an answer…" : "Reply to the discussion…"}
          onPosted={() => {
            atBottom.current = true;
            void load().then(() => requestAnimationFrame(() => scroller.current?.scrollTo({ top: scroller.current.scrollHeight, behavior: "smooth" })));
            pokeNow();
          }}
        />
      )}
    </aside>
  );
}
