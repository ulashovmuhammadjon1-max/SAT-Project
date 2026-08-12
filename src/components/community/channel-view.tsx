"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { Loader2 } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Composer, type ReplyTarget } from "@/components/community/composer";
import { MessageRow } from "@/components/community/message-row";
import {
  deleteMessage,
  editMessage,
  listMessages,
  markChannelRead,
  toggleReaction,
} from "@/server/actions/student/community";
import type { CommunityMessageView } from "@/lib/community/types";
import { cn } from "@/lib/utils";

/** How often to pull new messages while the tab is visible. */
const POLL_MS = 8000;




export function ChannelView({
  channelSlug,
  channelName,
  description,
  isReadOnly,
  initialMessages,
  initialHasMore,
}: {
  channelSlug: string;
  channelName: string;
  description: string | null;
  isReadOnly: boolean;
  initialMessages: CommunityMessageView[];
  initialHasMore: boolean;
}) {
  const [messages, setMessages] = useState(initialMessages);
  const [hasMore, setHasMore] = useState(initialHasMore);
  const [loadingMore, setLoadingMore] = useState(false);
  const [replyTo, setReplyTo] = useState<ReplyTarget | null>(null);

  const scroller = useRef<HTMLDivElement>(null);
  // Only auto-scroll when the reader is already at the bottom. Yanking someone
  // to the newest message while they are reading history is the single most
  // irritating thing a chat can do.
  const pinnedToBottom = useRef(true);

  const scrollToBottom = useCallback(() => {
    const el = scroller.current;
    if (el) el.scrollTop = el.scrollHeight;
  }, []);

  useEffect(() => {
    scrollToBottom();
    void markChannelRead(channelSlug);
  }, [channelSlug, scrollToBottom]);

  const refresh = useCallback(async () => {
    const { messages: fresh, hasMore: more } = await listMessages(channelSlug);
    setMessages((prev) => {
      // Nothing changed — return the same array so React skips the re-render
      // and the reader's scroll position is untouched.
      const sameLength = prev.length === fresh.length;
      const sameTail = sameLength && prev[prev.length - 1]?.id === fresh[fresh.length - 1]?.id;
      // Reactions and edits change nothing about length or tail id, so they
      // have to be compared explicitly or a new reaction would never appear.
      const sameEdits =
        sameTail &&
        prev.every(
          (m, i) =>
            m.deleted === fresh[i].deleted &&
            m.editedAt === fresh[i].editedAt &&
            m.reactions.length === fresh[i].reactions.length &&
            m.reactions.every(
              (r, j) =>
                r.emoji === fresh[i].reactions[j]?.emoji &&
                r.count === fresh[i].reactions[j]?.count &&
                r.mine === fresh[i].reactions[j]?.mine
            )
        );
      return sameEdits ? prev : fresh;
    });
    setHasMore(more);
    if (pinnedToBottom.current) requestAnimationFrame(scrollToBottom);
    void markChannelRead(channelSlug);
  }, [channelSlug, scrollToBottom]);

  useEffect(() => {
    const id = setInterval(() => {
      // Polling a hidden tab burns the database for nobody's benefit.
      if (document.visibilityState === "visible") void refresh();
    }, POLL_MS);
    return () => clearInterval(id);
  }, [refresh]);

  async function loadOlder() {
    const oldest = messages[0];
    if (!oldest || loadingMore) return;
    setLoadingMore(true);
    const el = scroller.current;
    const before = el?.scrollHeight ?? 0;

    const { messages: older, hasMore: more } = await listMessages(channelSlug, oldest.id);
    setMessages((prev) => [...older, ...prev]);
    setHasMore(more);
    setLoadingMore(false);

    // Keep the reader looking at the same message rather than jumping to the
    // top of the newly-prepended block.
    requestAnimationFrame(() => {
      if (el) el.scrollTop = el.scrollHeight - before;
    });
  }

  async function remove(id: string) {
    const result = await deleteMessage(id);
    if (result.ok) {
      setMessages((prev) => prev.map((m) => (m.id === id ? { ...m, deleted: true, body: "", attachments: [], canDelete: false } : m)));
    }
  }

  async function edit(id: string, body: string) {
    const result = await editMessage(id, body);
    if (result.ok) {
      setMessages((prev) =>
        prev.map((m) => (m.id === id ? { ...m, body, editedAt: new Date().toISOString() } : m))
      );
    }
  }

  /**
   * Toggle a reaction, updating the pill immediately.
   *
   * Optimistic because a reaction is the lowest-stakes action in the app and a
   * pill that waits for a round trip feels broken. A refresh follows so the
   * count settles to the truth if someone else reacted in the same moment.
   */
  function react(id: string, emoji: string) {
    setMessages((prev) =>
      prev.map((m) => {
        if (m.id !== id) return m;
        const existing = m.reactions.find((r) => r.emoji === emoji);
        if (!existing) return { ...m, reactions: [...m.reactions, { emoji, count: 1, mine: true }] };
        const count = existing.count + (existing.mine ? -1 : 1);
        return {
          ...m,
          reactions:
            count === 0
              ? m.reactions.filter((r) => r.emoji !== emoji)
              : m.reactions.map((r) =>
                  r.emoji === emoji ? { ...r, count, mine: !existing.mine } : r
                ),
        };
      })
    );
    void toggleReaction(id, emoji).then(() => refresh());
  }

  function onScroll() {
    const el = scroller.current;
    if (!el) return;
    pinnedToBottom.current = el.scrollHeight - el.scrollTop - el.clientHeight < 80;
  }

  return (
    <div className="flex min-h-0 flex-1 flex-col overflow-hidden rounded-xl border bg-card">
      <div className="shrink-0 border-b px-5 py-3">
        <h2 className="font-display text-lg font-semibold"># {channelName}</h2>
        {description && <p className="text-sm text-muted-foreground">{description}</p>}
      </div>

      <div ref={scroller} onScroll={onScroll} className="flex-1 overflow-y-auto px-3 py-4">
        {hasMore && (
          <div className="flex justify-center pb-2">
            <Button variant="ghost" size="sm" onClick={() => void loadOlder()} disabled={loadingMore}>
              {loadingMore ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : null}
              Load earlier messages
            </Button>
          </div>
        )}

        {messages.length === 0 ? (
          <p className="py-24 text-center text-muted-foreground">No messages yet. Say hello.</p>
        ) : (
          messages.map((m, i) => (
            <MessageRow
              key={m.id}
              message={m}
              // Consecutive messages from one person collapse into a block, so
              // a burst of three lines does not repeat the name three times.
              grouped={
                i > 0 &&
                messages[i - 1].author.id === m.author.id &&
                !m.replyTo &&
                new Date(m.createdAt).getTime() -
                  new Date(messages[i - 1].createdAt).getTime() <
                  5 * 60_000
              }
              onReply={() =>
                setReplyTo({
                  id: m.id,
                  authorName: m.author.name,
                  excerpt: m.body.slice(0, 60) || "attachment",
                })
              }
              onDelete={() => void remove(m.id)}
              onEdit={(body) => edit(m.id, body)}
              onReact={(emoji) => react(m.id, emoji)}
            />
          ))
        )}
      </div>

      <Composer
        channelSlug={channelSlug}
        disabled={isReadOnly}
        replyTo={replyTo}
        onCancelReply={() => setReplyTo(null)}
        onPosted={() => {
          pinnedToBottom.current = true;
          void refresh();
        }}
      />
    </div>
  );
}
