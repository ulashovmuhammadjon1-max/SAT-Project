"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { CornerUpLeft, FileText, Loader2, Shield, Trash2 } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Composer, type ReplyTarget } from "@/components/community/composer";
import { MessageText } from "@/components/community/message-text";
import { deleteMessage, listMessages, markChannelRead } from "@/server/actions/student/community";
import type { CommunityMessageView } from "@/lib/community/types";
import { cn } from "@/lib/utils";

/** How often to pull new messages while the tab is visible. */
const POLL_MS = 8000;

function initials(name: string): string {
  return name
    .split(/\s+/)
    .slice(0, 2)
    .map((p) => p[0])
    .join("")
    .toUpperCase();
}

function timeLabel(iso: string): string {
  const d = new Date(iso);
  const today = new Date();
  const sameDay = d.toDateString() === today.toDateString();
  return sameDay
    ? d.toLocaleTimeString(undefined, { hour: "2-digit", minute: "2-digit" })
    : d.toLocaleDateString(undefined, { day: "numeric", month: "short" }) +
        " " +
        d.toLocaleTimeString(undefined, { hour: "2-digit", minute: "2-digit" });
}

function fileSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${Math.round(bytes / 1024)} KB`;
  return `${(bytes / 1024 / 1024).toFixed(1)} MB`;
}

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
      const sameEdits =
        sameTail && prev.every((m, i) => m.deleted === fresh[i].deleted);
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

  function onScroll() {
    const el = scroller.current;
    if (!el) return;
    pinnedToBottom.current = el.scrollHeight - el.scrollTop - el.clientHeight < 80;
  }

  return (
    <div className="flex h-[calc(100vh-8rem)] flex-col overflow-hidden rounded-xl border bg-card">
      <div className="border-b px-4 py-3">
        <h2 className="font-display text-base font-semibold"># {channelName}</h2>
        {description && <p className="text-xs text-muted-foreground">{description}</p>}
      </div>

      <div ref={scroller} onScroll={onScroll} className="flex-1 space-y-1 overflow-y-auto px-2 py-3">
        {hasMore && (
          <div className="flex justify-center pb-2">
            <Button variant="ghost" size="sm" onClick={() => void loadOlder()} disabled={loadingMore}>
              {loadingMore ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : null}
              Load earlier messages
            </Button>
          </div>
        )}

        {messages.length === 0 ? (
          <p className="py-16 text-center text-sm text-muted-foreground">
            No messages yet. Say hello.
          </p>
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

function MessageRow({
  message: m,
  grouped,
  onReply,
  onDelete,
}: {
  message: CommunityMessageView;
  grouped: boolean;
  onReply: () => void;
  onDelete: () => void;
}) {
  return (
    <div
      className={cn(
        "group relative rounded-lg px-2 py-1 hover:bg-secondary/40",
        m.mentionedMe && "bg-primary/5 ring-1 ring-primary/20",
        grouped ? "mt-0" : "mt-3"
      )}
    >
      {m.replyTo && (
        <div className="mb-1 flex items-center gap-1.5 pl-10 text-xs text-muted-foreground">
          <CornerUpLeft className="h-3 w-3 shrink-0" />
          <span className="font-medium text-foreground/80">{m.replyTo.authorName}</span>
          <span className={cn("truncate", m.replyTo.deleted && "italic")}>{m.replyTo.excerpt}</span>
        </div>
      )}

      <div className="flex gap-2.5">
        <div className="w-8 shrink-0">
          {!grouped && (
            <span
              className={cn(
                "flex h-8 w-8 items-center justify-center rounded-full text-[11px] font-semibold",
                m.author.isAdmin ? "bg-navy-900 text-white" : "bg-primary/15 text-primary"
              )}
            >
              {initials(m.author.name)}
            </span>
          )}
        </div>

        <div className="min-w-0 flex-1">
          {!grouped && (
            <div className="flex items-baseline gap-2">
              <span className="text-sm font-medium">{m.author.name}</span>
              {m.author.isAdmin && (
                <span className="flex items-center gap-0.5 rounded bg-navy-900 px-1.5 py-px text-[10px] font-medium text-white">
                  <Shield className="h-2.5 w-2.5" /> Team
                </span>
              )}
              <span className="text-[11px] text-muted-foreground">{timeLabel(m.createdAt)}</span>
            </div>
          )}

          {m.deleted ? (
            <p className="text-sm italic text-muted-foreground">This message was deleted.</p>
          ) : (
            <>
              {m.body && (
                <MessageText body={m.body} className="whitespace-pre-wrap break-words text-sm" />
              )}
              {m.attachments.length > 0 && (
                <div className="mt-1.5 flex flex-wrap gap-2">
                  {m.attachments.map((a) =>
                    a.kind === "IMAGE" ? (
                      <a key={a.id} href={a.url} target="_blank" rel="noopener noreferrer">
                        {/* eslint-disable-next-line @next/next/no-img-element */}
                        <img
                          src={a.url}
                          alt={a.fileName}
                          className="max-h-64 max-w-full rounded-lg border object-contain"
                        />
                      </a>
                    ) : (
                      <a
                        key={a.id}
                        href={a.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="flex items-center gap-2 rounded-lg border bg-secondary/40 px-3 py-2 text-xs hover:bg-secondary"
                      >
                        <FileText className="h-4 w-4 shrink-0 text-muted-foreground" />
                        <span className="max-w-[14rem] truncate font-medium">{a.fileName}</span>
                        <span className="text-muted-foreground">{fileSize(a.sizeBytes)}</span>
                      </a>
                    )
                  )}
                </div>
              )}
            </>
          )}
        </div>

        {!m.deleted && (
          <div className="absolute right-2 top-1 hidden gap-1 group-hover:flex">
            <button
              onClick={onReply}
              className="rounded border bg-card p-1.5 text-muted-foreground shadow-sm hover:text-foreground"
              aria-label="Reply"
            >
              <CornerUpLeft className="h-3.5 w-3.5" />
            </button>
            {m.canDelete && (
              <button
                onClick={onDelete}
                className="rounded border bg-card p-1.5 text-muted-foreground shadow-sm hover:text-destructive"
                aria-label="Delete message"
              >
                <Trash2 className="h-3.5 w-3.5" />
              </button>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
