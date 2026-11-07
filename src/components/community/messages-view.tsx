"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { upload } from "@vercel/blob/client";
import {
  ArrowLeft,
  Bell,
  BellOff,
  Check,
  CheckCheck,
  CornerDownRight,
  Flag,
  Loader2,
  Mail,
  MoreHorizontal,
  Paperclip,
  SendHorizontal,
  ShieldAlert,
  SmilePlus,
  Trash2,
  X,
} from "lucide-react";
import { toast } from "sonner";

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { broadcastRead, useLive, useLiveScope } from "@/components/live/live-provider";
import { ATTACHMENT_TYPES, MAX_ATTACHMENT_BYTES, MAX_BODY, type NewAttachment } from "@/lib/community/types";
import { cn } from "@/lib/utils";
import {
  deleteDirectMessage,
  getConversation,
  listConversations,
  markConversationRead,
  sendDirectMessage,
  setConversationMuted,
  type ConversationSummary,
} from "@/server/actions/student/community-dm";

import { Attachments } from "./attachments";
import { LocalStamp, MemberAvatar, RoleBadge, dayLabel, useMounted } from "./bits";
import { EmojiPicker } from "./emoji-picker";
import { MemberPopover, ReportDialog } from "./member-card";
import { NavToggle } from "./community-shell";
import { RichText } from "./rich-text";

type Conversation = NonNullable<Awaited<ReturnType<typeof getConversation>>>;

export function MessagesView({ initialList, conversation }: { initialList: ConversationSummary[]; conversation: Conversation | null }) {
  const pathname = usePathname();
  const { data } = useLive();
  const [list, setList] = useState(initialList);
  const last = useRef<string | null>(null);

  const refreshList = useCallback(async () => setList(await listConversations()), []);
  useEffect(() => {
    const v = `${data?.dmUnread ?? ""}|${data?.conversationVersion ?? ""}`;
    if (last.current && v !== last.current) void refreshList();
    last.current = v;
  }, [data?.dmUnread, data?.conversationVersion, refreshList]);

  return (
    <div className="flex min-h-0 min-w-0 flex-1">
      <aside className={cn("flex min-h-0 w-full flex-col border-r border-border md:w-80 md:shrink-0", conversation && "hidden md:flex")}>
        <header className="flex h-14 shrink-0 items-center gap-2 border-b border-border px-3 sm:px-4">
          <NavToggle />
          <Mail className="h-4 w-4 text-primary" />
          <h1 className="font-display text-[15px] font-semibold">Messages</h1>
        </header>
        <div className="min-h-0 flex-1 overflow-y-auto p-2">
          {list.length === 0 ? (
            <div className="px-4 py-12 text-center">
              <span className="mx-auto flex h-12 w-12 items-center justify-center rounded-2xl bg-primary/10 text-primary">
                <Mail className="h-5 w-5" />
              </span>
              <p className="mt-3 font-serif text-lg">No conversations yet</p>
              <p className="mt-1 text-sm text-muted-foreground">Open a student&apos;s profile card from any channel and choose Message.</p>
            </div>
          ) : (
            list.map((c) => {
              const href = `/community/messages/${c.id}`;
              const active = pathname === href;
              return (
                <Link
                  key={c.id}
                  href={href}
                  className={cn("flex items-center gap-3 rounded-xl px-2.5 py-2.5 transition-colors", active ? "bg-primary/10" : "hover:bg-secondary/70")}
                >
                  <MemberAvatar id={c.other.id} name={c.other.name} image={c.other.image} size={42} online={c.other.activeNow} />
                  <span className="min-w-0 flex-1">
                    <span className="flex items-baseline gap-2">
                      <span className={cn("truncate text-sm", c.unread ? "font-bold" : "font-medium")}>{c.other.name}</span>
                      {c.lastMessage && <LocalStamp iso={c.lastMessage.at} mode="relative" className="ml-auto shrink-0 text-[11px] text-muted-foreground" />}
                    </span>
                    <span className={cn("block truncate text-xs", c.unread ? "font-medium text-foreground" : "text-muted-foreground")}>
                      {c.muted && <BellOff className="mr-1 inline h-3 w-3" />}
                      {c.lastMessage?.mine ? "You: " : ""}
                      {c.lastMessage?.body}
                    </span>
                  </span>
                  {c.unread > 0 && <span className="flex h-5 min-w-5 items-center justify-center rounded-full bg-primary px-1.5 text-[10px] font-bold text-primary-foreground">{c.unread}</span>}
                </Link>
              );
            })
          )}
        </div>
      </aside>

      {conversation ? (
        <ConversationPane key={conversation.id} initial={conversation} onActivity={() => void refreshList()} />
      ) : (
        <div className="hidden flex-1 items-center justify-center md:flex">
          <div className="text-center">
            <p className="font-serif text-2xl">Your private conversations</p>
            <p className="mt-1 text-sm text-muted-foreground">Choose one on the left. Only you and the other student can see them.</p>
          </div>
        </div>
      )}
    </div>
  );
}

function ConversationPane({ initial, onActivity }: { initial: Conversation; onActivity: () => void }) {
  const { data, pokeNow } = useLive();
  const [c, setC] = useState(initial);
  const [body, setBody] = useState("");
  const [files, setFiles] = useState<NewAttachment[]>([]);
  const [uploading, setUploading] = useState(0);
  const [sending, setSending] = useState(false);
  const [replyTo, setReplyTo] = useState<{ id: string; excerpt: string } | null>(null);
  const [emoji, setEmoji] = useState(false);
  const [reporting, setReporting] = useState<string | null>(null);
  const scroller = useRef<HTMLDivElement>(null);
  const box = useRef<HTMLTextAreaElement>(null);
  const version = useRef<string | null>(null);

  useLiveScope({ conversation: c.id });
  const mounted = useMounted();

  const reload = useCallback(async () => {
    const next = await getConversation(c.id);
    if (next) setC(next);
  }, [c.id]);

  const toBottom = (smooth = false) => requestAnimationFrame(() => scroller.current?.scrollTo({ top: scroller.current.scrollHeight, behavior: smooth ? "smooth" : "auto" }));

  useEffect(() => {
    toBottom();
    void markConversationRead(c.id).then(() => {
      broadcastRead();
      pokeNow();
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [c.id]);

  useEffect(() => {
    const v = data?.conversationVersion ?? null;
    if (!v) return;
    if (version.current && v !== version.current) {
      void reload().then(() => {
        toBottom(true);
        if (document.visibilityState === "visible") void markConversationRead(c.id);
        onActivity();
      });
    }
    version.current = v;
  }, [data?.conversationVersion, reload, c.id, onActivity]);

  useEffect(() => {
    const el = box.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = `${Math.min(el.scrollHeight, 200)}px`;
  }, [body]);

  async function addFiles(list: FileList | File[]) {
    for (const file of Array.from(list).slice(0, 4 - files.length)) {
      if (!(ATTACHMENT_TYPES as readonly string[]).includes(file.type) || file.size > MAX_ATTACHMENT_BYTES) {
        toast.error(`${file.name}: images or PDFs under 10 MB only.`);
        continue;
      }
      setUploading((n) => n + 1);
      try {
        const blob = await upload(file.name, file, { access: "public", handleUploadUrl: "/api/community-upload" });
        setFiles((xs) => [...xs, { kind: file.type.startsWith("image/") ? "IMAGE" : "PDF", url: blob.url, fileName: file.name, contentType: file.type, sizeBytes: file.size }]);
      } catch {
        toast.error(`Could not upload ${file.name}.`);
      } finally {
        setUploading((n) => n - 1);
      }
    }
  }

  async function send() {
    if (sending || uploading || (!body.trim() && files.length === 0)) return;
    setSending(true);
    const r = await sendDirectMessage({ conversationId: c.id, body, replyToId: replyTo?.id ?? null, attachments: files });
    setSending(false);
    if (!r.ok) return void toast.error(r.error);
    setBody("");
    setFiles([]);
    setReplyTo(null);
    await reload();
    toBottom(true);
    onActivity();
    pokeNow();
  }

  const lastMine = [...c.messages].reverse().find((m) => m.mine && !m.deleted);
  const seen = lastMine && c.otherLastReadAt && new Date(c.otherLastReadAt) >= new Date(lastMine.createdAt);

  return (
    <section className="flex min-h-0 min-w-0 flex-1 flex-col">
      <header className="flex h-14 shrink-0 items-center gap-3 border-b border-border bg-background/70 px-3 backdrop-blur sm:px-4">
        <Link href="/community/messages" className="-ml-1 flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary md:hidden" aria-label="All conversations">
          <ArrowLeft className="h-5 w-5" />
        </Link>
        <MemberPopover userId={c.other.id}>
          <button type="button" className="flex min-w-0 items-center gap-2.5 rounded-lg pr-2 text-left hover:bg-secondary/60">
            <MemberAvatar id={c.other.id} name={c.other.name} image={c.other.image} size={34} isAdmin={c.other.isAdmin} online={c.other.activeNow} />
            <span className="min-w-0">
              <span className="flex items-center gap-1.5 truncate text-sm font-semibold">
                {c.other.name} <RoleBadge isAdmin={c.other.isAdmin} isMentor={c.other.isMentor} />
              </span>
              <span className="block text-xs text-muted-foreground">{c.other.activeNow ? "Active now" : "Private conversation"}</span>
            </span>
          </button>
        </MemberPopover>
        <button
          type="button"
          onClick={async () => {
            const r = await setConversationMuted(c.id, !c.muted);
            if (!r.ok) return void toast.error(r.error);
            setC({ ...c, muted: !c.muted });
            toast.success(c.muted ? "Notifications on." : "Conversation muted.");
          }}
          className="ml-auto flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary hover:text-foreground"
          aria-label={c.muted ? "Unmute conversation" : "Mute conversation"}
          title={c.muted ? "Unmute conversation" : "Mute conversation"}
        >
          {c.muted ? <BellOff className="h-4 w-4" /> : <Bell className="h-4 w-4" />}
        </button>
      </header>

      <div ref={scroller} className="min-h-0 flex-1 overflow-y-auto px-3 py-4 sm:px-6">
        <div className="mx-auto max-w-2xl space-y-1">
          <div className="mb-6 flex flex-col items-center text-center">
            <MemberAvatar id={c.other.id} name={c.other.name} image={c.other.image} size={64} isAdmin={c.other.isAdmin} />
            <p className="mt-2 font-serif text-xl">{c.other.name}</p>
            <p className="mt-1 flex items-center gap-1 text-xs text-muted-foreground">
              <ShieldAlert className="h-3.5 w-3.5" /> Be kind. Never share passwords or personal details. Report anything that makes you uncomfortable.
            </p>
          </div>
          {c.messages.map((m, i) => {
            const prev = c.messages[i - 1];
            const newDay = mounted && (!prev || new Date(prev.createdAt).toDateString() !== new Date(m.createdAt).toDateString());
            const tight = prev && !newDay && prev.mine === m.mine && new Date(m.createdAt).getTime() - new Date(prev.createdAt).getTime() < 3 * 60_000;
            return (
              <div key={m.id}>
                {newDay && <p className="py-3 text-center text-[11px] font-semibold uppercase tracking-wider text-muted-foreground">{dayLabel(m.createdAt)}</p>}
                <div id={`dm-${m.id}`} className={cn("group flex", m.mine ? "justify-end" : "justify-start", tight ? "mt-0.5" : "mt-3")}>
                  <div className={cn("relative max-w-[85%] sm:max-w-[75%]")}>
                    {m.replyTo && (
                      <p className={cn("mb-1 flex items-center gap-1 truncate text-[11px] text-muted-foreground", m.mine && "justify-end")}>
                        <CornerDownRight className="h-3 w-3" /> {m.replyTo.mine ? "You" : c.other.name}: {m.replyTo.excerpt}
                      </p>
                    )}
                    <div
                      className={cn(
                        "rounded-2xl px-3.5 py-2 shadow-sm",
                        m.mine ? "rounded-br-md bg-primary text-primary-foreground [&_a]:text-primary-foreground [&_*]:text-inherit" : "rounded-bl-md border border-border bg-card",
                        m.deleted && "bg-secondary text-muted-foreground italic shadow-none",
                      )}
                    >
                      {m.deleted ? <p className="text-sm">Message deleted</p> : m.body ? <RichText body={m.body} className="text-[15px] text-inherit" /> : null}
                      {!m.deleted && <Attachments items={m.attachments} compact />}
                      <p className={cn("mt-0.5 text-right text-[10px]", m.mine ? "text-primary-foreground/70" : "text-muted-foreground")}>
                        <LocalStamp iso={m.createdAt} />
                        {m.editedAt && " · edited"}
                      </p>
                    </div>
                    {!m.deleted && (
                      <div className={cn("absolute top-1 flex opacity-0 transition-opacity group-hover:opacity-100 focus-within:opacity-100", m.mine ? "-left-16" : "-right-16")}>
                        <button type="button" onClick={() => setReplyTo({ id: m.id, excerpt: m.body.slice(0, 80) || "attachment" })} className="rounded-lg p-1.5 text-muted-foreground hover:bg-secondary" aria-label="Reply">
                          <CornerDownRight className="h-4 w-4" />
                        </button>
                        <DropdownMenu>
                          <DropdownMenuTrigger asChild>
                            <button type="button" className="rounded-lg p-1.5 text-muted-foreground hover:bg-secondary" aria-label="More">
                              <MoreHorizontal className="h-4 w-4" />
                            </button>
                          </DropdownMenuTrigger>
                          <DropdownMenuContent align={m.mine ? "end" : "start"}>
                            {m.mine ? (
                              <DropdownMenuItem
                                className="text-destructive focus:text-destructive"
                                onClick={async () => {
                                  const r = await deleteDirectMessage(m.id);
                                  if (!r.ok) return void toast.error(r.error);
                                  await reload();
                                }}
                              >
                                <Trash2 className="mr-2 h-4 w-4" /> Delete
                              </DropdownMenuItem>
                            ) : (
                              <DropdownMenuItem onClick={() => setReporting(m.id)}>
                                <Flag className="mr-2 h-4 w-4" /> Report
                              </DropdownMenuItem>
                            )}
                          </DropdownMenuContent>
                        </DropdownMenu>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            );
          })}
          {lastMine && (
            <p className="flex items-center justify-end gap-1 pt-1 text-[11px] text-muted-foreground">
              {seen ? <CheckCheck className="h-3.5 w-3.5 text-primary" /> : <Check className="h-3.5 w-3.5" />}
              {seen ? "Seen" : "Sent"}
            </p>
          )}
        </div>
      </div>

      {c.canSend ? (
        <div className="border-t border-border bg-card/70 px-3 pb-3 pt-2 sm:px-4">
          <div className="mx-auto max-w-2xl">
            {replyTo && (
              <div className="mb-2 flex items-center gap-2 rounded-lg border-l-2 border-primary bg-primary/[0.06] px-3 py-1.5 text-xs">
                <span className="text-muted-foreground">Replying to</span>
                <span className="min-w-0 flex-1 truncate">{replyTo.excerpt}</span>
                <button type="button" onClick={() => setReplyTo(null)} aria-label="Cancel reply">
                  <X className="h-3.5 w-3.5" />
                </button>
              </div>
            )}
            {(files.length > 0 || uploading > 0) && (
              <div className="mb-2 flex flex-wrap gap-2">
                {files.map((f, i) => (
                  <span key={f.url} className="inline-flex items-center gap-1.5 rounded-lg border border-border bg-background px-2 py-1 text-xs">
                    {f.fileName}
                    <button type="button" onClick={() => setFiles((xs) => xs.filter((_, j) => j !== i))} aria-label={`Remove ${f.fileName}`}>
                      <X className="h-3 w-3" />
                    </button>
                  </span>
                ))}
                {uploading > 0 && <Loader2 className="h-4 w-4 animate-spin text-muted-foreground" />}
              </div>
            )}
            <div className="flex items-end gap-1.5 rounded-2xl border border-input bg-background p-1.5 focus-within:border-primary/50">
              <label className="flex h-9 w-9 shrink-0 cursor-pointer items-center justify-center rounded-xl text-muted-foreground hover:bg-secondary" aria-label="Attach">
                <Paperclip className="h-4 w-4" />
                <input type="file" multiple accept={ATTACHMENT_TYPES.join(",")} className="hidden" onChange={(e) => e.target.files && void addFiles(e.target.files)} />
              </label>
              <div className="relative">
                <button type="button" onClick={() => setEmoji((v) => !v)} className="flex h-9 w-9 items-center justify-center rounded-xl text-muted-foreground hover:bg-secondary" aria-label="Emoji">
                  <SmilePlus className="h-4 w-4" />
                </button>
                {emoji && (
                  <div className="absolute bottom-11 left-0 z-30">
                    <EmojiPicker
                      onPick={(e) => {
                        setBody((b) => b + e);
                        setEmoji(false);
                        box.current?.focus();
                      }}
                    />
                  </div>
                )}
              </div>
              <textarea
                ref={box}
                rows={1}
                value={body}
                maxLength={MAX_BODY}
                onChange={(e) => setBody(e.target.value)}
                onPaste={(e) => {
                  const pasted = Array.from(e.clipboardData.files);
                  if (pasted.length) {
                    e.preventDefault();
                    void addFiles(pasted);
                  }
                }}
                onKeyDown={(e) => {
                  if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
                    e.preventDefault();
                    void send();
                  }
                }}
                placeholder={`Message ${c.other.name}`}
                aria-label={`Message ${c.other.name}`}
                className="max-h-[200px] min-h-9 flex-1 resize-none bg-transparent px-1.5 py-2 text-[15px] focus:outline-none"
              />
              <button
                type="button"
                onClick={() => void send()}
                disabled={sending || uploading > 0 || (!body.trim() && files.length === 0)}
                className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-primary text-primary-foreground transition-opacity disabled:opacity-40"
                aria-label="Send"
              >
                {sending ? <Loader2 className="h-4 w-4 animate-spin" /> : <SendHorizontal className="h-4 w-4" />}
              </button>
            </div>
          </div>
        </div>
      ) : (
        <div className="border-t border-border px-4 py-4">
          <p className="mx-auto max-w-2xl rounded-xl bg-secondary/70 px-4 py-3 text-center text-sm text-muted-foreground">{c.blockReason}</p>
        </div>
      )}
      {reporting && <ReportDialog target={{ directMessageId: reporting }} open onOpenChange={(o) => !o && setReporting(null)} />}
    </section>
  );
}
