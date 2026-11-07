"use client";

import { useEffect, useRef, useState } from "react";
import { upload } from "@vercel/blob/client";
import {
  BarChart3,
  Bold,
  CircleHelp,
  Code,
  Italic,
  Library,
  Link2,
  List,
  ListOrdered,
  Loader2,
  Lock,
  Megaphone,
  MessageSquare,
  Paperclip,
  Plus,
  SendHorizontal,
  SmilePlus,
  SquareCode,
  Trophy,
  Underline,
  X,
  FileText,
} from "lucide-react";
import { toast } from "sonner";

import {
  ATTACHMENT_TYPES,
  MAX_ATTACHMENTS,
  MAX_ATTACHMENT_BYTES,
  MAX_BODY,
  POLL_MAX_OPTIONS,
  type MessageKind,
  type NewAttachment,
} from "@/lib/community/types";
import { cn } from "@/lib/utils";
import { postMessage, searchMembers } from "@/server/actions/student/community";

import { EmojiPicker } from "./emoji-picker";
import { MemberAvatar, fileSize } from "./bits";

export interface ReplyTarget {
  id: string;
  authorName: string;
  excerpt: string;
}

interface Member {
  id: string;
  name: string;
  handle: string;
  image: string | null;
}

const KINDS: { id: MessageKind; label: string; icon: typeof MessageSquare; hint: string; admin?: boolean }[] = [
  { id: "MESSAGE", label: "Message", icon: MessageSquare, hint: "Just talk" },
  { id: "QUESTION", label: "Question", icon: CircleHelp, hint: "Ask, and accept the best answer" },
  { id: "RESOURCE", label: "Resource", icon: Library, hint: "Share a link, notes or a PDF" },
  { id: "ACHIEVEMENT", label: "Achievement", icon: Trophy, hint: "A score, an offer, a milestone" },
  { id: "POLL", label: "Poll", icon: BarChart3, hint: "Let everyone vote" },
  { id: "ANNOUNCEMENT", label: "Announcement", icon: Megaphone, hint: "Notifies everyone", admin: true },
];

function kindFor(type: string): NewAttachment["kind"] {
  if (type.startsWith("image/")) return "IMAGE";
  if (type === "application/pdf") return "PDF";
  return "FILE";
}

export function Composer({
  channelSlug,
  channelName,
  threadRootId,
  disabled,
  disabledReason,
  isAdmin,
  slowModeSeconds = 0,
  replyTo,
  onCancelReply,
  onPosted,
  placeholder,
  initialKind,
}: {
  channelSlug: string;
  channelName: string;
  threadRootId?: string | null;
  disabled?: boolean;
  disabledReason?: string | null;
  isAdmin?: boolean;
  slowModeSeconds?: number;
  replyTo: ReplyTarget | null;
  onCancelReply: () => void;
  onPosted: (id: string) => void;
  placeholder?: string;
  initialKind?: MessageKind;
}) {
  const draftKey = `scholarly-draft:${channelSlug}:${threadRootId ?? "main"}`;
  const [kind, setKind] = useState<MessageKind>(initialKind ?? "MESSAGE");
  const [kindMenu, setKindMenu] = useState(false);
  const [body, setBody] = useState("");
  const [title, setTitle] = useState("");
  const [subject, setSubject] = useState("");
  const [link, setLink] = useState("");
  const [options, setOptions] = useState<string[]>(["", ""]);
  const [files, setFiles] = useState<(NewAttachment & { preview?: string })[]>([]);
  const [uploading, setUploading] = useState(0);
  const [sending, setSending] = useState(false);
  const [emojiOpen, setEmojiOpen] = useState(false);
  const [dragging, setDragging] = useState(false);

  const [mentionQuery, setMentionQuery] = useState<string | null>(null);
  const [suggestions, setSuggestions] = useState<Member[]>([]);
  const [highlighted, setHighlighted] = useState(0);
  const [mentioned, setMentioned] = useState<Member[]>([]);

  const box = useRef<HTMLTextAreaElement>(null);
  const fileInput = useRef<HTMLInputElement>(null);
  const emojiRef = useRef<HTMLDivElement>(null);
  const kindRef = useRef<HTMLDivElement>(null);

  // Drafts survive navigation and reloads, per channel and per thread.
  useEffect(() => {
    try {
      setBody(localStorage.getItem(draftKey) ?? "");
    } catch {
      /* ignore */
    }
  }, [draftKey]);
  useEffect(() => {
    const t = setTimeout(() => {
      try {
        if (body) localStorage.setItem(draftKey, body);
        else localStorage.removeItem(draftKey);
      } catch {
        /* ignore */
      }
    }, 400);
    return () => clearTimeout(t);
  }, [body, draftKey]);

  useEffect(() => {
    if (replyTo) box.current?.focus();
  }, [replyTo]);

  useEffect(() => {
    const el = box.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = `${Math.min(el.scrollHeight, 260)}px`;
  }, [body]);

  useEffect(() => {
    const onDown = (e: MouseEvent) => {
      if (emojiOpen && emojiRef.current && !emojiRef.current.contains(e.target as Node)) setEmojiOpen(false);
      if (kindMenu && kindRef.current && !kindRef.current.contains(e.target as Node)) setKindMenu(false);
    };
    document.addEventListener("mousedown", onDown);
    return () => document.removeEventListener("mousedown", onDown);
  }, [emojiOpen, kindMenu]);

  useEffect(() => {
    if (mentionQuery == null) {
      setSuggestions([]);
      return;
    }
    const t = setTimeout(async () => {
      setSuggestions(await searchMembers(mentionQuery || "a"));
      setHighlighted(0);
    }, 150);
    return () => clearTimeout(t);
  }, [mentionQuery]);

  function trackMention(value: string, caret: number) {
    const m = /(?:^|\s)@([A-Za-z0-9_-]{0,30})$/.exec(value.slice(0, caret));
    setMentionQuery(m ? m[1] : null);
  }

  function pickMention(member: Member) {
    const el = box.current;
    if (!el) return;
    const caret = el.selectionStart;
    const before = body.slice(0, caret).replace(/@([A-Za-z0-9_-]*)$/, `@${member.handle} `);
    const next = before + body.slice(caret);
    setBody(next);
    setMentioned((prev) => (prev.some((x) => x.id === member.id) ? prev : [...prev, member]));
    setMentionQuery(null);
    requestAnimationFrame(() => {
      el.focus();
      el.setSelectionRange(before.length, before.length);
    });
  }

  /** Wrap the selection in markers, or insert them around a placeholder. */
  function wrap(before: string, after = before, placeholderText = "text") {
    const el = box.current;
    if (!el) return;
    const { selectionStart: s, selectionEnd: e } = el;
    const selected = body.slice(s, e) || placeholderText;
    const next = body.slice(0, s) + before + selected + after + body.slice(e);
    setBody(next);
    requestAnimationFrame(() => {
      el.focus();
      el.setSelectionRange(s + before.length, s + before.length + selected.length);
    });
  }

  function prefixLines(prefix: (i: number) => string) {
    const el = box.current;
    if (!el) return;
    const { selectionStart: s, selectionEnd: e } = el;
    const lineStart = body.lastIndexOf("\n", s - 1) + 1;
    const block = body.slice(lineStart, e) || "";
    const lines = (block || "item").split("\n").map((l, i) => prefix(i) + l);
    const next = body.slice(0, lineStart) + lines.join("\n") + body.slice(e);
    setBody(next);
    requestAnimationFrame(() => el.focus());
  }

  function insert(text: string) {
    const el = box.current;
    const s = el?.selectionStart ?? body.length;
    const e = el?.selectionEnd ?? body.length;
    const next = body.slice(0, s) + text + body.slice(e);
    setBody(next);
    requestAnimationFrame(() => {
      el?.focus();
      el?.setSelectionRange(s + text.length, s + text.length);
    });
  }

  async function addFiles(list: FileList | File[]) {
    const chosen = Array.from(list).slice(0, MAX_ATTACHMENTS - files.length);
    for (const file of chosen) {
      if (!(ATTACHMENT_TYPES as readonly string[]).includes(file.type)) {
        toast.error(`${file.name}: attach images or PDFs only.`);
        continue;
      }
      if (file.size > MAX_ATTACHMENT_BYTES) {
        toast.error(`${file.name} is over 10 MB.`);
        continue;
      }
      setUploading((n) => n + 1);
      try {
        const blob = await upload(file.name, file, { access: "public", handleUploadUrl: "/api/community-upload" });
        setFiles((prev) => [
          ...prev,
          {
            kind: kindFor(file.type),
            url: blob.url,
            fileName: file.name,
            contentType: file.type,
            sizeBytes: file.size,
            preview: file.type.startsWith("image/") ? URL.createObjectURL(file) : undefined,
          },
        ]);
      } catch {
        toast.error(`Could not upload ${file.name}. Check your connection and try again.`);
      } finally {
        setUploading((n) => n - 1);
      }
    }
  }

  const needsTitle = kind === "QUESTION" || kind === "RESOURCE" || kind === "POLL";
  const canSend =
    !sending &&
    uploading === 0 &&
    !disabled &&
    (body.trim().length > 0 || files.length > 0 || (kind !== "MESSAGE" && title.trim().length > 0)) &&
    (!needsTitle || title.trim().length > 0) &&
    (kind !== "POLL" || options.filter((o) => o.trim()).length >= 2) &&
    (kind !== "RESOURCE" || link.trim().length > 0 || files.length > 0);

  async function send() {
    if (!canSend) return;
    setSending(true);
    const r = await postMessage({
      channelSlug,
      body,
      kind,
      title,
      subject,
      linkUrl: link,
      pollOptions: options,
      replyToId: replyTo?.id ?? null,
      threadRootId: threadRootId ?? null,
      mentionUserIds: mentioned.filter((m) => body.includes(`@${m.handle}`)).map((m) => m.id),
      attachments: files.map(({ preview: _p, ...a }) => a),
    });
    setSending(false);
    if (!r.ok) return void toast.error(r.error);
    files.forEach((f) => f.preview && URL.revokeObjectURL(f.preview));
    setBody("");
    setTitle("");
    setSubject("");
    setLink("");
    setOptions(["", ""]);
    setFiles([]);
    setMentioned([]);
    setKind("MESSAGE");
    onCancelReply();
    onPosted(r.id);
    requestAnimationFrame(() => box.current?.focus());
  }

  function onKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (suggestions.length > 0 && mentionQuery != null) {
      if (e.key === "ArrowDown") {
        e.preventDefault();
        return setHighlighted((h) => (h + 1) % suggestions.length);
      }
      if (e.key === "ArrowUp") {
        e.preventDefault();
        return setHighlighted((h) => (h - 1 + suggestions.length) % suggestions.length);
      }
      if (e.key === "Enter" || e.key === "Tab") {
        e.preventDefault();
        return pickMention(suggestions[highlighted]);
      }
      if (e.key === "Escape") return setMentionQuery(null);
    }
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "b") {
      e.preventDefault();
      return wrap("**");
    }
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "i") {
      e.preventDefault();
      return wrap("*");
    }
    // Enter sends, Shift+Enter breaks the line.
    if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
      e.preventDefault();
      void send();
    }
    if (e.key === "Escape" && replyTo) onCancelReply();
  }

  if (disabled) {
    return (
      <div className="border-t border-border bg-card/60 px-4 py-4">
        <p className="flex items-center justify-center gap-2 rounded-xl bg-secondary/70 px-4 py-3 text-center text-sm text-muted-foreground">
          <Lock className="h-4 w-4 shrink-0" /> {disabledReason ?? "Only the Scholarly team posts here."}
        </p>
      </div>
    );
  }

  const activeKind = KINDS.find((k) => k.id === kind)!;
  const tools: { icon: typeof Bold; label: string; run: () => void }[] = [
    { icon: Bold, label: "Bold (Ctrl+B)", run: () => wrap("**") },
    { icon: Italic, label: "Italic (Ctrl+I)", run: () => wrap("*") },
    { icon: Underline, label: "Underline", run: () => wrap("__") },
    { icon: Code, label: "Inline code", run: () => wrap("`", "`", "code") },
    { icon: SquareCode, label: "Code block", run: () => wrap("\n```\n", "\n```\n", "code") },
    { icon: List, label: "Bulleted list", run: () => prefixLines(() => "- ") },
    { icon: ListOrdered, label: "Numbered list", run: () => prefixLines((i) => `${i + 1}. `) },
    { icon: Link2, label: "Link", run: () => wrap("[", "](https://)", "label") },
  ];

  return (
    <div
      className={cn("relative border-t border-border bg-card/70 px-3 pb-3 pt-2 backdrop-blur sm:px-4", dragging && "ring-2 ring-inset ring-primary")}
      onDragOver={(e) => {
        if (e.dataTransfer.types.includes("Files")) {
          e.preventDefault();
          setDragging(true);
        }
      }}
      onDragLeave={() => setDragging(false)}
      onDrop={(e) => {
        e.preventDefault();
        setDragging(false);
        if (e.dataTransfer.files.length) void addFiles(e.dataTransfer.files);
      }}
    >
      {suggestions.length > 0 && mentionQuery != null && (
        <ul role="listbox" className="absolute bottom-full left-4 z-30 mb-2 w-72 overflow-hidden rounded-xl border border-border bg-popover p-1 shadow-xl animate-fade-in">
          <li className="px-2.5 pb-1 pt-1.5 text-[11px] font-semibold uppercase tracking-wide text-muted-foreground">Mention</li>
          {suggestions.map((s, i) => (
            <li key={s.id} role="option" aria-selected={i === highlighted}>
              <button
                type="button"
                onMouseDown={(e) => {
                  e.preventDefault();
                  pickMention(s);
                }}
                className={cn("flex w-full items-center gap-2.5 rounded-lg px-2.5 py-1.5 text-left text-sm", i === highlighted ? "bg-primary/10 text-primary" : "hover:bg-secondary")}
              >
                <MemberAvatar id={s.id} name={s.name} image={s.image} size={26} />
                <span className="font-medium">{s.name}</span>
                <span className="ml-auto text-xs text-muted-foreground">@{s.handle}</span>
              </button>
            </li>
          ))}
        </ul>
      )}

      {replyTo && (
        <div className="mb-2 flex items-center gap-2 rounded-lg border-l-2 border-primary bg-primary/[0.06] px-3 py-1.5 text-xs">
          <span className="text-muted-foreground">Replying to</span>
          <span className="font-semibold">{replyTo.authorName}</span>
          <span className="min-w-0 flex-1 truncate text-muted-foreground">{replyTo.excerpt}</span>
          <button type="button" onClick={onCancelReply} aria-label="Cancel reply" className="rounded p-0.5 hover:bg-secondary">
            <X className="h-3.5 w-3.5" />
          </button>
        </div>
      )}

      <div className="overflow-hidden rounded-2xl border border-input bg-background shadow-sm transition-shadow focus-within:border-primary/50 focus-within:shadow-[0_0_0_4px_hsl(var(--primary)/0.1)]">
        {kind !== "MESSAGE" && (
          <div className="space-y-2 border-b border-border/70 bg-secondary/30 px-3 py-2.5 animate-fade-in">
            <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wide text-primary">
              <activeKind.icon className="h-3.5 w-3.5" /> {activeKind.label}
              <button type="button" onClick={() => setKind("MESSAGE")} className="ml-auto rounded p-0.5 text-muted-foreground hover:bg-secondary" aria-label="Back to a plain message">
                <X className="h-3.5 w-3.5" />
              </button>
            </div>
            <input
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              maxLength={140}
              placeholder={
                kind === "QUESTION"
                  ? "What do you want to know? e.g. How do I solve systems with substitution?"
                  : kind === "RESOURCE"
                    ? "Name of the resource"
                    : kind === "POLL"
                      ? "Ask a question"
                      : kind === "ACHIEVEMENT"
                        ? "e.g. Scored 1500 on the October SAT"
                        : "Headline"
              }
              className="w-full bg-transparent font-serif text-lg font-medium placeholder:text-muted-foreground/70 focus:outline-none"
              aria-label="Title"
            />
            {(kind === "QUESTION" || kind === "RESOURCE") && (
              <input
                value={subject}
                onChange={(e) => setSubject(e.target.value)}
                maxLength={60}
                placeholder="Subject (optional) — Algebra, IELTS Writing, AP Biology…"
                className="w-full rounded-md bg-background/60 px-2 py-1 text-sm placeholder:text-muted-foreground/70 focus:outline-none focus:ring-1 focus:ring-ring"
                aria-label="Subject"
              />
            )}
            {kind === "RESOURCE" && (
              <input
                value={link}
                onChange={(e) => setLink(e.target.value)}
                inputMode="url"
                placeholder="https://… (or attach a PDF below)"
                className="w-full rounded-md bg-background/60 px-2 py-1 text-sm placeholder:text-muted-foreground/70 focus:outline-none focus:ring-1 focus:ring-ring"
                aria-label="Link"
              />
            )}
            {kind === "POLL" && (
              <div className="space-y-1.5">
                {options.map((o, i) => (
                  <div key={i} className="flex items-center gap-2">
                    <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-secondary text-xs font-semibold">{i + 1}</span>
                    <input
                      value={o}
                      maxLength={80}
                      onChange={(e) => setOptions((xs) => xs.map((x, j) => (j === i ? e.target.value : x)))}
                      placeholder={`Option ${i + 1}`}
                      className="min-w-0 flex-1 rounded-md bg-background/60 px-2 py-1 text-sm focus:outline-none focus:ring-1 focus:ring-ring"
                      aria-label={`Option ${i + 1}`}
                    />
                    {options.length > 2 && (
                      <button type="button" onClick={() => setOptions((xs) => xs.filter((_, j) => j !== i))} className="rounded p-1 text-muted-foreground hover:bg-secondary" aria-label={`Remove option ${i + 1}`}>
                        <X className="h-3.5 w-3.5" />
                      </button>
                    )}
                  </div>
                ))}
                {options.length < POLL_MAX_OPTIONS && (
                  <button type="button" onClick={() => setOptions((xs) => [...xs, ""])} className="ml-8 inline-flex items-center gap-1 text-xs font-medium text-primary hover:underline">
                    <Plus className="h-3.5 w-3.5" /> Add option
                  </button>
                )}
              </div>
            )}
          </div>
        )}

        {files.length > 0 && (
          <div className="flex gap-2 overflow-x-auto px-3 pt-3">
            {files.map((f, i) => (
              <div key={f.url} className="group relative shrink-0">
                {f.preview ? (
                  // eslint-disable-next-line @next/next/no-img-element
                  <img src={f.preview} alt={f.fileName} className="h-20 w-20 rounded-lg border border-border object-cover" />
                ) : (
                  <div className="flex h-20 w-40 items-center gap-2 rounded-lg border border-border bg-secondary/50 px-2.5">
                    <FileText className="h-6 w-6 shrink-0 text-destructive" />
                    <div className="min-w-0">
                      <p className="truncate text-xs font-medium">{f.fileName}</p>
                      <p className="text-[11px] text-muted-foreground">{fileSize(f.sizeBytes)}</p>
                    </div>
                  </div>
                )}
                <button
                  type="button"
                  onClick={() => setFiles((prev) => prev.filter((_, j) => j !== i))}
                  className="absolute -right-1.5 -top-1.5 flex h-6 w-6 items-center justify-center rounded-full border border-border bg-background shadow"
                  aria-label={`Remove ${f.fileName}`}
                >
                  <X className="h-3 w-3" />
                </button>
              </div>
            ))}
            {uploading > 0 && (
              <div className="flex h-20 w-20 shrink-0 items-center justify-center rounded-lg border border-dashed border-border">
                <Loader2 className="h-5 w-5 animate-spin text-muted-foreground" />
              </div>
            )}
          </div>
        )}

        <textarea
          ref={box}
          value={body}
          rows={1}
          maxLength={MAX_BODY}
          onChange={(e) => {
            setBody(e.target.value);
            trackMention(e.target.value, e.target.selectionStart);
          }}
          onKeyDown={onKeyDown}
          onClick={(e) => trackMention(body, (e.target as HTMLTextAreaElement).selectionStart)}
          onPaste={(e) => {
            const pasted = Array.from(e.clipboardData.files);
            if (pasted.length > 0) {
              e.preventDefault();
              void addFiles(pasted);
            }
          }}
          placeholder={
            placeholder ??
            (kind === "MESSAGE" ? `Message #${channelName}` : kind === "QUESTION" ? "Add details, what you tried, where you got stuck…" : "Add a description (optional)")
          }
          aria-label={placeholder ?? `Message ${channelName}`}
          className="block max-h-[260px] min-h-[2.75rem] w-full resize-none bg-transparent px-3.5 py-3 text-[15px] leading-relaxed placeholder:text-muted-foreground/70 focus:outline-none"
        />

        <div className="flex items-center gap-0.5 px-1.5 pb-1.5">
          {!threadRootId && (
            <div className="relative" ref={kindRef}>
              <button
                type="button"
                onClick={() => setKindMenu((v) => !v)}
                className="flex h-8 items-center gap-1 rounded-lg px-2 text-xs font-semibold text-primary hover:bg-primary/10"
                aria-haspopup="menu"
                aria-expanded={kindMenu}
              >
                <Plus className="h-4 w-4" /> <span className="hidden whitespace-nowrap sm:inline">Post type</span>
              </button>
              {kindMenu && (
                <div role="menu" className="absolute bottom-10 left-0 z-30 w-64 rounded-xl border border-border bg-popover p-1 shadow-xl animate-fade-in">
                  {KINDS.filter((k) => !k.admin || isAdmin).map((k) => (
                    <button
                      key={k.id}
                      type="button"
                      role="menuitem"
                      onClick={() => {
                        setKind(k.id);
                        setKindMenu(false);
                        requestAnimationFrame(() => box.current?.focus());
                      }}
                      className={cn("flex w-full items-center gap-3 rounded-lg px-2.5 py-2 text-left hover:bg-secondary", kind === k.id && "bg-primary/10")}
                    >
                      <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-secondary text-foreground">
                        <k.icon className="h-4 w-4" />
                      </span>
                      <span>
                        <span className="block text-sm font-medium">{k.label}</span>
                        <span className="block text-xs text-muted-foreground">{k.hint}</span>
                      </span>
                    </button>
                  ))}
                </div>
              )}
            </div>
          )}
          <span className={cn("mx-1 hidden h-5 w-px bg-border", threadRootId ? "2xl:block" : "sm:block")} />
          <div className={cn("hidden items-center", threadRootId ? "2xl:flex" : "sm:flex")}>
            {tools.map((t) => (
              <button key={t.label} type="button" title={t.label} aria-label={t.label} onClick={t.run} className="flex h-8 w-8 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary hover:text-foreground">
                <t.icon className="h-4 w-4" />
              </button>
            ))}
          </div>
          <div className="relative" ref={emojiRef}>
            <button type="button" title="Emoji" aria-label="Emoji" onClick={() => setEmojiOpen((v) => !v)} className="flex h-8 w-8 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary hover:text-foreground">
              <SmilePlus className="h-4 w-4" />
            </button>
            {emojiOpen && (
              <div className="absolute bottom-10 left-0 z-30 animate-fade-in sm:left-auto sm:right-0">
                <EmojiPicker onPick={(e) => insert(e)} />
              </div>
            )}
          </div>
          <button
            type="button"
            title="Attach images or PDFs"
            aria-label="Attach images or PDFs"
            onClick={() => fileInput.current?.click()}
            disabled={files.length >= MAX_ATTACHMENTS}
            className="flex h-8 w-8 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary hover:text-foreground disabled:opacity-40"
          >
            <Paperclip className="h-4 w-4" />
          </button>
          <input
            ref={fileInput}
            type="file"
            multiple
            accept={ATTACHMENT_TYPES.join(",")}
            className="hidden"
            onChange={(e) => {
              if (e.target.files) void addFiles(e.target.files);
              e.target.value = "";
            }}
          />
          <span className={cn("ml-auto hidden whitespace-nowrap pr-2 text-[11px] text-muted-foreground", !threadRootId && "2xl:inline")}>
            {slowModeSeconds > 0 && !isAdmin ? `Slow mode ${slowModeSeconds}s · ` : ""}
            <kbd className="font-sans">Enter</kbd> to send · <kbd className="font-sans">Shift+Enter</kbd> new line
          </span>
          <button
            type="button"
            onClick={() => void send()}
            disabled={!canSend}
            aria-label="Send"
            className={cn(
              "ml-auto flex h-9 shrink-0 items-center gap-1.5 rounded-xl px-3.5 text-sm font-semibold transition-all",
              canSend ? "bg-primary text-primary-foreground shadow-sm hover:brightness-110 active:scale-95" : "bg-secondary text-muted-foreground",
            )}
          >
            {sending ? <Loader2 className="h-4 w-4 animate-spin" /> : <SendHorizontal className="h-4 w-4" />}
            <span className="hidden sm:inline">{kind === "MESSAGE" ? "Send" : "Post"}</span>
          </button>
        </div>
      </div>
    </div>
  );
}
