"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import {
  Bell,
  BellOff,
  Bookmark,
  BookmarkCheck,
  CheckCircle2,
  CircleHelp,
  CornerDownRight,
  CornerUpLeft,
  Library,
  Link2,
  Lock,
  Megaphone,
  MessageSquareText,
  MoreHorizontal,
  Pencil,
  Pin,
  PinOff,
  SmilePlus,
  Trash2,
  Trophy,
  BarChart3,
  Flag,
} from "lucide-react";
import { toast } from "sonner";

import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from "@/components/ui/alert-dialog";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Button } from "@/components/ui/button";
import { REACTIONS, type CommunityMessageView } from "@/lib/community/types";
import { cn } from "@/lib/utils";
import {
  acceptAnswer,
  closePoll,
  deleteMessage,
  editMessage,
  setFollow,
  toggleBookmark,
  togglePin,
  toggleReaction,
  votePoll,
} from "@/server/actions/student/community";

import { Attachments, LinkCard, LinkPreviews } from "./attachments";
import { LocalStamp, MemberAvatar, RoleBadge, relativeTime } from "./bits";
import { MemberPopover, ReportDialog } from "./member-card";
import { RichText, linksIn } from "./rich-text";

export interface MessageHandlers {
  onPatch: (id: string, patch: Partial<CommunityMessageView>) => void;
  onReply?: (m: CommunityMessageView) => void;
  onOpenThread?: (m: CommunityMessageView) => void;
  onJump?: (id: string, threadRootId: string | null) => void;
  onChanged?: () => void;
}

const KIND_META = {
  QUESTION: { label: "Question", icon: CircleHelp, chip: "bg-primary/10 text-primary", ring: "border-primary/25" },
  RESOURCE: { label: "Resource", icon: Library, chip: "bg-success/15 text-success", ring: "border-success/25" },
  ACHIEVEMENT: { label: "Achievement", icon: Trophy, chip: "bg-warning/20 text-warning-foreground dark:text-warning", ring: "border-warning/40" },
  POLL: { label: "Poll", icon: BarChart3, chip: "bg-accent text-accent-foreground", ring: "border-accent-foreground/20" },
  ANNOUNCEMENT: { label: "Announcement", icon: Megaphone, chip: "bg-foreground text-background", ring: "border-foreground/20" },
} as const;

export function MessageItem({
  message: m,
  grouped = false,
  context = "stream",
  highlight = false,
  handlers,
}: {
  message: CommunityMessageView;
  grouped?: boolean;
  context?: "stream" | "thread" | "root" | "list";
  highlight?: boolean;
  handlers: MessageHandlers;
}) {
  const [editing, setEditing] = useState(false);
  const [draft, setDraft] = useState(m.body);
  const [saving, setSaving] = useState(false);
  const [pickerOpen, setPickerOpen] = useState(false);
  const [confirmDelete, setConfirmDelete] = useState(false);
  const [reporting, setReporting] = useState(false);
  const [revealBlocked, setRevealBlocked] = useState(false);
  const [touchActive, setTouchActive] = useState(false);
  const picker = useRef<HTMLDivElement>(null);
  const editBox = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    if (!pickerOpen) return;
    const onDown = (e: MouseEvent) => {
      if (picker.current && !picker.current.contains(e.target as Node)) setPickerOpen(false);
    };
    document.addEventListener("mousedown", onDown);
    return () => document.removeEventListener("mousedown", onDown);
  }, [pickerOpen]);

  useEffect(() => {
    if (editing) {
      const el = editBox.current;
      el?.focus();
      el?.setSelectionRange(el.value.length, el.value.length);
    }
  }, [editing]);

  if (m.authorBlocked && !revealBlocked && !m.deleted) {
    return (
      <div className={cn("px-4 py-1.5", grouped ? "mt-0" : "mt-3")}>
        <button
          type="button"
          onClick={() => setRevealBlocked(true)}
          className="rounded-lg border border-dashed border-border px-3 py-1.5 text-xs text-muted-foreground hover:bg-secondary/50"
        >
          Message from someone you blocked · Show
        </button>
      </div>
    );
  }

  /* ---------------------------- actions ---------------------------------- */

  function react(emoji: string) {
    setPickerOpen(false);
    const existing = m.reactions.find((r) => r.emoji === emoji);
    const reactions = !existing
      ? [...m.reactions, { emoji, count: 1, mine: true }]
      : m.reactions
          .map((r) => (r.emoji === emoji ? { ...r, count: r.count + (r.mine ? -1 : 1), mine: !r.mine } : r))
          .filter((r) => r.count > 0);
    handlers.onPatch(m.id, { reactions });
    void toggleReaction(m.id, emoji).then((r) => {
      if (!r.ok) {
        toast.error(r.error);
        handlers.onPatch(m.id, { reactions: m.reactions });
      }
    });
  }

  async function saveEdit() {
    const next = draft.trim();
    if (next === m.body) return setEditing(false);
    setSaving(true);
    const r = await editMessage(m.id, next);
    setSaving(false);
    if (!r.ok) return void toast.error(r.error);
    handlers.onPatch(m.id, { body: next, editedAt: new Date().toISOString() });
    setEditing(false);
  }

  async function remove() {
    const r = await deleteMessage(m.id);
    if (!r.ok) return void toast.error(r.error);
    handlers.onPatch(m.id, { deleted: true, body: "", title: null, attachments: [], reactions: [], canDelete: false, canEdit: false, poll: null });
    handlers.onChanged?.();
  }

  async function bookmark() {
    handlers.onPatch(m.id, { bookmarked: !m.bookmarked });
    const r = await toggleBookmark(m.id);
    if (!r.ok) {
      handlers.onPatch(m.id, { bookmarked: m.bookmarked });
      return void toast.error(r.error);
    }
    toast.success(r.bookmarked ? "Saved to your bookmarks." : "Removed from bookmarks.");
  }

  async function follow(state: "FOLLOWING" | "MUTED" | null) {
    const r = await setFollow(m.threadRootId ?? m.id, state);
    if (!r.ok) return void toast.error(r.error);
    handlers.onPatch(m.id, { following: state });
    toast.success(state === "FOLLOWING" ? "You'll be notified about new replies." : state === "MUTED" ? "Discussion muted." : "Stopped following.");
  }

  async function pin() {
    const r = await togglePin(m.id);
    if (!r.ok) return void toast.error(r.error);
    handlers.onPatch(m.id, { pinned: r.pinned });
    handlers.onChanged?.();
    toast.success(r.pinned ? "Pinned to the channel." : "Unpinned.");
  }

  function copyLink() {
    const url = `${window.location.origin}/community/${m.channelSlug}?${m.threadRootId ? `thread=${m.threadRootId}&` : ""}m=${m.id}`;
    void navigator.clipboard?.writeText(url).then(() => toast.success("Link copied."));
  }

  async function accept() {
    if (!m.threadRootId) return;
    const r = await acceptAnswer(m.threadRootId, m.isAcceptedAnswer ? null : m.id);
    if (!r.ok) return void toast.error(r.error);
    handlers.onChanged?.();
    toast.success(m.isAcceptedAnswer ? "Answer un-marked." : "Marked as the accepted answer.");
  }

  /* ---------------------------- pieces ----------------------------------- */

  const kind = m.kind !== "MESSAGE" ? KIND_META[m.kind] : null;
  const previews = !m.deleted && m.kind !== "RESOURCE" ? linksIn(m.body) : [];
  const isRootLike = context === "stream" || context === "root" || context === "list";

  const header = (
    <div className="flex flex-wrap items-baseline gap-x-2 gap-y-0.5">
      <MemberPopover userId={m.author.id}>
        <button type="button" className="font-semibold leading-tight text-foreground hover:underline focus-visible:underline focus-visible:outline-none">
          {m.author.name}
        </button>
      </MemberPopover>
      <RoleBadge isAdmin={m.author.isAdmin} isMentor={m.author.isMentor} />
      <LocalStamp iso={m.createdAt} mode={context === "list" ? "relative" : "clock"} className="text-xs text-muted-foreground" />
      {m.editedAt && !m.deleted && <span className="text-[11px] text-muted-foreground">(edited)</span>}
      {m.pinned && (
        <span className="inline-flex items-center gap-1 text-[11px] font-medium text-primary">
          <Pin className="h-3 w-3" /> Pinned
        </span>
      )}
      {m.isAcceptedAnswer && (
        <span className="inline-flex items-center gap-1 rounded-full bg-success/15 px-2 py-px text-[11px] font-semibold text-success">
          <CheckCircle2 className="h-3 w-3" /> Accepted answer
        </span>
      )}
    </div>
  );

  const body = m.deleted ? (
    <p className="text-sm italic text-muted-foreground">This message was deleted.</p>
  ) : editing ? (
    <div className="mt-1">
      <textarea
        ref={editBox}
        value={draft}
        onChange={(e) => setDraft(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            void saveEdit();
          }
          if (e.key === "Escape") {
            setEditing(false);
            setDraft(m.body);
          }
        }}
        rows={Math.min(10, Math.max(2, draft.split("\n").length))}
        className="w-full resize-none rounded-lg border border-input bg-background px-3 py-2 text-[15px] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
      />
      <p className="mt-1 text-xs text-muted-foreground">
        {saving ? "Saving…" : "Enter to save · Esc to cancel"}
      </p>
    </div>
  ) : m.body ? (
    <RichText body={m.body} />
  ) : null;

  const kindCard = kind && !m.deleted ? (
    <div
      className={cn(
        "mt-1.5 max-w-2xl overflow-hidden rounded-xl border bg-card shadow-sm",
        kind.ring,
        m.kind === "ACHIEVEMENT" && "bg-gradient-to-br from-warning/[0.12] via-card to-card",
        m.kind === "ANNOUNCEMENT" && "bg-gradient-to-br from-primary/[0.08] via-card to-card",
      )}
    >
      <div className="px-4 pb-3 pt-3.5">
        <div className="flex flex-wrap items-center gap-2">
          <span className={cn("inline-flex items-center gap-1 rounded-full px-2 py-0.5 text-[11px] font-semibold uppercase tracking-wide", kind.chip)}>
            <kind.icon className="h-3 w-3" /> {kind.label}
          </span>
          {m.subject && <span className="rounded-full border border-border px-2 py-0.5 text-[11px] text-muted-foreground">{m.subject}</span>}
          {m.kind === "QUESTION" && (
            <span
              className={cn(
                "ml-auto inline-flex items-center gap-1 text-[11px] font-semibold",
                m.acceptedAnswerId ? "text-success" : m.replyCount ? "text-primary" : "text-muted-foreground",
              )}
            >
              {m.acceptedAnswerId ? (
                <>
                  <CheckCircle2 className="h-3.5 w-3.5" /> Answered
                </>
              ) : m.replyCount ? (
                `${m.replyCount} ${m.replyCount === 1 ? "answer" : "answers"}`
              ) : (
                "Unanswered"
              )}
            </span>
          )}
        </div>
        {m.title && (
          <h3 className="mt-2 font-serif text-[1.35rem] font-medium leading-snug tracking-[-0.01em] text-foreground">
            {m.kind === "ACHIEVEMENT" && <span className="mr-1.5">🏆</span>}
            {m.title}
          </h3>
        )}
        {body && <div className="mt-1.5">{body}</div>}
        {m.kind === "RESOURCE" && m.linkUrl && (
          <div className="mt-3">
            <LinkCard url={m.linkUrl} title={m.title} />
          </div>
        )}
        {m.poll && <Poll message={m} onPatch={handlers.onPatch} />}
        <Attachments items={m.attachments} />
        {m.kind === "ACHIEVEMENT" && !m.author.isMe && (
          <Button
            type="button"
            size="sm"
            variant={m.reactions.find((r) => r.emoji === "🎉")?.mine ? "secondary" : "outline"}
            className="mt-3 h-8 rounded-full"
            onClick={() => react("🎉")}
          >
            🎉 {m.reactions.find((r) => r.emoji === "🎉")?.mine ? "Congratulated" : "Congratulate"}
          </Button>
        )}
      </div>
    </div>
  ) : null;

  const reactions =
    m.reactions.length > 0 && !m.deleted ? (
      <div className="mt-1.5 flex flex-wrap gap-1">
        {m.reactions.map((r) => (
          <button
            key={r.emoji}
            type="button"
            onClick={() => react(r.emoji)}
            aria-pressed={r.mine}
            aria-label={`${r.emoji} ${r.count}${r.mine ? ", you reacted" : ""}`}
            className={cn(
              "inline-flex h-7 items-center gap-1 rounded-full border px-2 text-xs font-medium tabular-nums transition-all hover:-translate-y-px active:scale-95",
              r.mine ? "border-primary/50 bg-primary/10 text-primary" : "border-border bg-background hover:border-foreground/25",
            )}
          >
            <span key={`${r.emoji}-${r.count}`} className="text-[15px] leading-none animate-pop">
              {r.emoji}
            </span>
            {r.count}
          </button>
        ))}
      </div>
    ) : null;

  const threadSummary =
    context === "stream" && !m.deleted && (m.replyCount > 0 || m.kind === "QUESTION") ? (
      <button
        type="button"
        onClick={() => handlers.onOpenThread?.(m)}
        className="group/thread mt-2 inline-flex items-center gap-2 rounded-lg border border-border bg-background px-3 py-1.5 text-xs font-medium transition-colors hover:border-primary/40 hover:bg-primary/[0.04]"
      >
        <MessageSquareText className="h-3.5 w-3.5 text-primary" />
        {m.replyCount > 0 ? (
          <>
            <span className="text-primary">
              {m.replyCount} {m.replyCount === 1 ? "reply" : "replies"}
            </span>
            {m.lastReplyAt && (
              <span className="text-muted-foreground" suppressHydrationWarning>
                · last {relativeTime(m.lastReplyAt)}
              </span>
            )}
          </>
        ) : (
          <span className="text-primary">Answer this question</span>
        )}
        <span className="text-muted-foreground transition-transform group-hover/thread:translate-x-0.5">→</span>
      </button>
    ) : null;

  /* ---------------------------- layout ----------------------------------- */

  return (
    <div
      id={`msg-${m.id}`}
      onClick={(e) => {
        // Touch screens have no hover: a tap on the message shows its actions.
        if (window.matchMedia("(hover: none)").matches && !(e.target as HTMLElement).closest("a,button,textarea,input")) {
          setTouchActive((v) => !v);
        }
      }}
      className={cn(
        "group/msg relative scroll-mt-24 px-4 transition-colors",
        context === "list" ? "rounded-xl py-3 hover:bg-secondary/40" : "py-1 hover:bg-secondary/40",
        !grouped && context !== "list" && "mt-3 pt-2",
        m.mentionedMe && !m.deleted && "bg-primary/[0.05] shadow-[inset_3px_0_0_hsl(var(--primary))]",
        m.isAcceptedAnswer && "bg-success/[0.05] shadow-[inset_3px_0_0_hsl(var(--success))]",
        highlight && "animate-highlight-fade",
      )}
    >
      {m.replyTo && (
        <button
          type="button"
          onClick={() => handlers.onJump?.(m.replyTo!.id, m.replyTo!.threadRootId)}
          className="group/reply mb-1 ml-[1.1rem] flex max-w-full items-center gap-1.5 text-xs text-muted-foreground"
        >
          <span className="h-3 w-6 shrink-0 rounded-tl-lg border-l-2 border-t-2 border-border" aria-hidden />
          <CornerUpLeft className="h-3 w-3 shrink-0 sm:hidden" />
          <span className="font-semibold text-foreground/80 group-hover/reply:text-primary">{m.replyTo.authorName}</span>
          <span className={cn("truncate group-hover/reply:text-foreground", m.replyTo.deleted && "italic")}>{m.replyTo.excerpt}</span>
        </button>
      )}

      <div className="flex gap-3">
        <div className="w-10 shrink-0">
          {!grouped || context === "list" ? (
            <MemberPopover userId={m.author.id}>
              <button type="button" className="rounded-full focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring" aria-label={`${m.author.name}'s profile`}>
                <MemberAvatar id={m.author.id} name={m.author.name} image={m.author.image} isAdmin={m.author.isAdmin} size={40} />
              </button>
            </MemberPopover>
          ) : (
            <LocalStamp iso={m.createdAt} className="invisible block pt-1 text-right text-[10px] text-muted-foreground group-hover/msg:visible" />
          )}
        </div>
        <div className="min-w-0 flex-1 pb-1">
          {(!grouped || context === "list") && header}
          {kindCard ?? body}
          {!kind && !m.deleted && <Attachments items={m.attachments} />}
          {previews.length > 0 && !editing && <LinkPreviews urls={previews} />}
          {reactions}
          {threadSummary}
          {context === "thread" && m.canAccept && !m.deleted && (
            <button
              type="button"
              onClick={() => void accept()}
              className={cn(
                "mt-1.5 inline-flex items-center gap-1 rounded-full px-2.5 py-1 text-xs font-medium transition-colors",
                m.isAcceptedAnswer ? "bg-success/15 text-success hover:bg-success/25" : "border border-border text-muted-foreground hover:border-success/50 hover:text-success",
              )}
            >
              <CheckCircle2 className="h-3.5 w-3.5" />
              {m.isAcceptedAnswer ? "Accepted · undo" : "Accept this answer"}
            </button>
          )}
        </div>
      </div>

      {/* Hover actions */}
      {!m.deleted && !editing && context !== "list" && (
        <div
          className={cn(
            "absolute -top-3 right-3 z-10 flex items-center gap-0.5 rounded-xl border border-border bg-popover p-0.5 shadow-lg transition-opacity",
            "opacity-0 group-hover/msg:opacity-100 focus-within:opacity-100",
            (touchActive || pickerOpen) && "opacity-100",
          )}
        >
          {["👍", "🎉", "✅"].map((e) => (
            <button key={e} type="button" onClick={() => react(e)} className="hidden h-8 w-8 items-center justify-center rounded-lg text-base transition-transform hover:scale-110 hover:bg-secondary sm:flex" aria-label={`React ${e}`}>
              {e}
            </button>
          ))}
          <div className="relative" ref={picker}>
            <ActionButton label="Add reaction" onClick={() => setPickerOpen((v) => !v)}>
              <SmilePlus className="h-4 w-4" />
            </ActionButton>
            {pickerOpen && (
              <div className="absolute right-0 top-9 z-20 flex gap-0.5 rounded-xl border border-border bg-popover p-1 shadow-xl animate-fade-in">
                {REACTIONS.map((e) => (
                  <button key={e} type="button" onClick={() => react(e)} className="flex h-9 w-9 items-center justify-center rounded-lg text-lg transition-transform hover:scale-125 hover:bg-secondary" aria-label={`React ${e}`}>
                    {e}
                  </button>
                ))}
              </div>
            )}
          </div>
          {handlers.onReply && (
            <ActionButton label="Reply" onClick={() => handlers.onReply?.(m)}>
              <CornerDownRight className="h-4 w-4" />
            </ActionButton>
          )}
          {context === "stream" && handlers.onOpenThread && (
            <ActionButton label="Reply in a discussion" onClick={() => handlers.onOpenThread?.(m)}>
              <MessageSquareText className="h-4 w-4" />
            </ActionButton>
          )}
          <ActionButton label={m.bookmarked ? "Remove bookmark" : "Save"} onClick={() => void bookmark()}>
            {m.bookmarked ? <BookmarkCheck className="h-4 w-4 text-primary" /> : <Bookmark className="h-4 w-4" />}
          </ActionButton>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <button type="button" aria-label="More actions" className="flex h-8 w-8 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary hover:text-foreground">
                <MoreHorizontal className="h-4 w-4" />
              </button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="w-52">
              <DropdownMenuItem onClick={copyLink}>
                <Link2 className="mr-2 h-4 w-4" /> Copy link
              </DropdownMenuItem>
              {isRootLike && !m.threadRootId && (
                m.following === "FOLLOWING" ? (
                  <DropdownMenuItem onClick={() => void follow("MUTED")}>
                    <BellOff className="mr-2 h-4 w-4" /> Mute discussion
                  </DropdownMenuItem>
                ) : (
                  <DropdownMenuItem onClick={() => void follow("FOLLOWING")}>
                    <Bell className="mr-2 h-4 w-4" /> {m.following === "MUTED" ? "Unmute & follow" : "Follow discussion"}
                  </DropdownMenuItem>
                )
              )}
              {m.canPin && (
                <DropdownMenuItem onClick={() => void pin()}>
                  {m.pinned ? <PinOff className="mr-2 h-4 w-4" /> : <Pin className="mr-2 h-4 w-4" />} {m.pinned ? "Unpin" : "Pin to channel"}
                </DropdownMenuItem>
              )}
              {m.poll && !m.poll.closed && (m.author.isMe || m.canPin) && (
                <DropdownMenuItem
                  onClick={() =>
                    void closePoll(m.id).then((r) => {
                      if (!r.ok) return void toast.error(r.error);
                      handlers.onPatch(m.id, { poll: { ...m.poll!, closed: true } });
                    })
                  }
                >
                  <Lock className="mr-2 h-4 w-4" /> Close poll
                </DropdownMenuItem>
              )}
              {m.canEdit && (
                <DropdownMenuItem
                  onClick={() => {
                    setDraft(m.body);
                    setEditing(true);
                  }}
                >
                  <Pencil className="mr-2 h-4 w-4" /> Edit
                </DropdownMenuItem>
              )}
              {!m.author.isMe && (
                <DropdownMenuItem onClick={() => setReporting(true)}>
                  <Flag className="mr-2 h-4 w-4" /> Report
                </DropdownMenuItem>
              )}
              {m.canDelete && (
                <>
                  <DropdownMenuSeparator />
                  <DropdownMenuItem onClick={() => setConfirmDelete(true)} className="text-destructive focus:text-destructive">
                    <Trash2 className="mr-2 h-4 w-4" /> Delete
                  </DropdownMenuItem>
                </>
              )}
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      )}

      {context === "list" && (
        <Link
          href={`/community/${m.channelSlug}?${m.threadRootId ? `thread=${m.threadRootId}&` : ""}m=${m.id}`}
          className="absolute inset-0 rounded-xl focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
          aria-label="Open in channel"
        />
      )}

      <AlertDialog open={confirmDelete} onOpenChange={setConfirmDelete}>
        <AlertDialogContent className="w-[calc(100vw-2rem)] max-w-md">
          <AlertDialogHeader>
            <AlertDialogTitle>Delete this message?</AlertDialogTitle>
            <AlertDialogDescription>
              {m.author.isMe
                ? "It will be replaced with “This message was deleted” for everyone. This cannot be undone."
                : "You are removing another student's message as a moderator. They will be told a moderator removed it, and the action is logged."}
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>Keep it</AlertDialogCancel>
            <AlertDialogAction onClick={() => void remove()} className="bg-destructive text-destructive-foreground hover:bg-destructive/90">
              Delete
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
      {reporting && <ReportDialog target={{ messageId: m.id }} open={reporting} onOpenChange={setReporting} />}
    </div>
  );
}

function ActionButton({ label, onClick, children }: { label: string; onClick: () => void; children: React.ReactNode }) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label={label}
      title={label}
      className="flex h-8 w-8 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
    >
      {children}
    </button>
  );
}

function Poll({ message: m, onPatch }: { message: CommunityMessageView; onPatch: MessageHandlers["onPatch"] }) {
  const poll = m.poll!;
  const showResults = poll.closed || poll.myVote !== null;

  function vote(optionId: string) {
    if (poll.closed) return;
    const prevVote = poll.myVote;
    const options = poll.options.map((o) => ({
      ...o,
      votes: o.votes + (o.id === optionId ? 1 : 0) - (o.id === prevVote ? 1 : 0),
    }));
    onPatch(m.id, {
      poll: { ...poll, options, myVote: optionId, totalVotes: poll.totalVotes + (prevVote ? 0 : 1) },
    });
    void votePoll(m.id, optionId).then((r) => {
      if (!r.ok) {
        toast.error(r.error);
        onPatch(m.id, { poll });
      }
    });
  }

  const leader = Math.max(...poll.options.map((o) => o.votes));
  return (
    <div className="mt-3 space-y-2" role="group" aria-label="Poll options">
      {poll.options.map((o) => {
        const pct = poll.totalVotes ? Math.round((o.votes / poll.totalVotes) * 100) : 0;
        const mine = poll.myVote === o.id;
        return (
          <button
            key={o.id}
            type="button"
            disabled={poll.closed}
            onClick={() => vote(o.id)}
            aria-pressed={mine}
            className={cn(
              "relative flex w-full items-center justify-between gap-3 overflow-hidden rounded-lg border px-3 py-2.5 text-left text-sm transition-colors",
              mine ? "border-primary/60" : "border-border hover:border-foreground/30",
              poll.closed && "cursor-default",
            )}
          >
            {showResults && (
              <span
                aria-hidden
                className={cn("absolute inset-y-0 left-0 transition-[width] duration-500", mine ? "bg-primary/15" : o.votes === leader && leader > 0 ? "bg-accent" : "bg-secondary")}
                style={{ width: `${pct}%` }}
              />
            )}
            <span className="relative flex items-center gap-2 font-medium">
              <span className={cn("flex h-4 w-4 items-center justify-center rounded-full border-2", mine ? "border-primary bg-primary" : "border-muted-foreground/40")}>
                {mine && <span className="h-1.5 w-1.5 rounded-full bg-primary-foreground" />}
              </span>
              {o.label}
            </span>
            {showResults && <span className="relative text-xs font-semibold tabular-nums text-muted-foreground">{pct}%</span>}
          </button>
        );
      })}
      <p className="text-xs text-muted-foreground">
        {poll.totalVotes} {poll.totalVotes === 1 ? "vote" : "votes"}
        {poll.closed ? " · Final results" : poll.myVote ? " · You can change your vote" : " · Vote to see results"}
      </p>
    </div>
  );
}
