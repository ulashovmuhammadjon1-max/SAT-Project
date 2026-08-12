"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { upload } from "@vercel/blob/client";
import { FileText, ImageIcon, Loader2, Paperclip, Send, X } from "lucide-react";

import { Button } from "@/components/ui/button";
import { postMessage, searchMembers } from "@/server/actions/student/community";
import { MAX_ATTACHMENTS, MAX_BODY, type NewAttachment } from "@/lib/community/types";
import { cn } from "@/lib/utils";

interface Member {
  id: string;
  name: string;
  handle: string;
}

export interface ReplyTarget {
  id: string;
  authorName: string;
  excerpt: string;
}

/** Which attachment bucket a MIME type belongs to. */
function kindOf(contentType: string): NewAttachment["kind"] {
  if (contentType.startsWith("image/")) return "IMAGE";
  if (contentType === "application/pdf") return "PDF";
  return "FILE";
}

export function Composer({
  channelSlug,
  disabled,
  replyTo,
  onCancelReply,
  onPosted,
}: {
  channelSlug: string;
  disabled?: boolean;
  replyTo: ReplyTarget | null;
  onCancelReply: () => void;
  onPosted: () => void;
}) {
  const [body, setBody] = useState("");
  const [pending, setPending] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [files, setFiles] = useState<NewAttachment[]>([]);
  const [uploading, setUploading] = useState(0);

  // Mentions typed into the body resolve to ids here. The body keeps the text
  // token for display; the ids are what actually get stored, so two students
  // with the same first name never collide.
  const [mentioned, setMentioned] = useState<Member[]>([]);
  const [suggestions, setSuggestions] = useState<Member[]>([]);
  const [mentionQuery, setMentionQuery] = useState<string | null>(null);
  const [activeSuggestion, setActiveSuggestion] = useState(0);

  const textarea = useRef<HTMLTextAreaElement>(null);
  const fileInput = useRef<HTMLInputElement>(null);

  // Focus the box when a reply is started, so answering is one click.
  useEffect(() => {
    if (replyTo) textarea.current?.focus();
  }, [replyTo]);

  /** The @word immediately before the caret, if the caret sits inside one. */
  const detectMention = useCallback((value: string, caret: number) => {
    const upToCaret = value.slice(0, caret);
    const m = /@([A-Za-z0-9_-]*)$/.exec(upToCaret);
    return m ? m[1] : null;
  }, []);

  useEffect(() => {
    if (mentionQuery == null) {
      setSuggestions([]);
      return;
    }
    let cancelled = false;
    // Debounced: a query per keystroke would fire a server action on every
    // letter of a name.
    const t = setTimeout(async () => {
      const found = await searchMembers(mentionQuery);
      if (!cancelled) {
        setSuggestions(found);
        setActiveSuggestion(0);
      }
    }, 180);
    return () => {
      cancelled = true;
      clearTimeout(t);
    };
  }, [mentionQuery]);

  function onChange(e: React.ChangeEvent<HTMLTextAreaElement>) {
    const value = e.target.value;
    setBody(value);
    setMentionQuery(detectMention(value, e.target.selectionStart ?? value.length));
  }

  function applySuggestion(member: Member) {
    const el = textarea.current;
    if (!el) return;
    const caret = el.selectionStart ?? body.length;
    const before = body.slice(0, caret).replace(/@([A-Za-z0-9_-]*)$/, `@${member.handle} `);
    const next = before + body.slice(caret);
    setBody(next);
    setMentioned((prev) => (prev.some((m) => m.id === member.id) ? prev : [...prev, member]));
    setMentionQuery(null);
    setSuggestions([]);
    requestAnimationFrame(() => {
      el.focus();
      el.setSelectionRange(before.length, before.length);
    });
  }

  async function addFiles(list: FileList | null) {
    if (!list?.length) return;
    setError(null);
    const room = MAX_ATTACHMENTS - files.length;
    const chosen = Array.from(list).slice(0, room);
    if (chosen.length < list.length) {
      setError(`Up to ${MAX_ATTACHMENTS} files per message.`);
    }

    for (const file of chosen) {
      setUploading((n) => n + 1);
      try {
        const blob = await upload(file.name, file, {
          access: "public",
          handleUploadUrl: "/api/community-upload",
        });
        setFiles((prev) => [
          ...prev,
          {
            kind: kindOf(file.type),
            url: blob.url,
            fileName: file.name,
            contentType: file.type || "application/octet-stream",
            sizeBytes: file.size,
          },
        ]);
      } catch (e) {
        setError(e instanceof Error ? e.message : "Upload failed.");
      } finally {
        setUploading((n) => n - 1);
      }
    }
  }

  /** Screenshots are usually pasted, not picked from a file dialog. */
  function onPaste(e: React.ClipboardEvent<HTMLTextAreaElement>) {
    const items = Array.from(e.clipboardData.files);
    if (items.length) {
      e.preventDefault();
      const dt = new DataTransfer();
      items.forEach((f) => dt.items.add(f));
      void addFiles(dt.files);
    }
  }

  async function send() {
    if (pending || uploading > 0) return;
    if (!body.trim() && files.length === 0) return;

    setPending(true);
    setError(null);
    const result = await postMessage({
      channelSlug,
      body,
      replyToId: replyTo?.id ?? null,
      // Only mentions whose token survives in the final text — deleting the
      // "@Name" after picking it should not still tag them.
      mentionUserIds: mentioned.filter((m) => body.includes(`@${m.handle}`)).map((m) => m.id),
      attachments: files,
    });
    setPending(false);

    if (!result.ok) {
      setError(result.error);
      return;
    }
    setBody("");
    setFiles([]);
    setMentioned([]);
    onCancelReply();
    onPosted();
  }

  function onKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (suggestions.length) {
      if (e.key === "ArrowDown") {
        e.preventDefault();
        setActiveSuggestion((i) => (i + 1) % suggestions.length);
        return;
      }
      if (e.key === "ArrowUp") {
        e.preventDefault();
        setActiveSuggestion((i) => (i - 1 + suggestions.length) % suggestions.length);
        return;
      }
      if (e.key === "Enter" || e.key === "Tab") {
        e.preventDefault();
        applySuggestion(suggestions[activeSuggestion]);
        return;
      }
      if (e.key === "Escape") {
        setSuggestions([]);
        setMentionQuery(null);
        return;
      }
    }
    // Enter sends, Shift+Enter breaks the line — the convention every chat
    // app uses, so nobody has to be told.
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      void send();
    }
    if (e.key === "Escape" && replyTo) onCancelReply();
  }

  if (disabled) {
    return (
      <div className="border-t bg-card px-4 py-3 text-center text-sm text-muted-foreground">
        This channel is read-only.
      </div>
    );
  }

  return (
    <div className="border-t bg-card">
      {replyTo && (
        <div className="flex items-center gap-2 border-b px-4 py-2 text-xs">
          <span className="text-muted-foreground">
            Replying to <strong className="text-foreground">{replyTo.authorName}</strong> ·{" "}
            {replyTo.excerpt}
          </span>
          <button
            onClick={onCancelReply}
            className="ml-auto rounded p-0.5 text-muted-foreground hover:text-foreground"
            aria-label="Cancel reply"
          >
            <X className="h-3.5 w-3.5" />
          </button>
        </div>
      )}

      {files.length > 0 && (
        <div className="flex flex-wrap gap-2 border-b px-4 py-2">
          {files.map((f, i) => (
            <span
              key={f.url}
              className="flex items-center gap-1.5 rounded-md border bg-secondary/50 px-2 py-1 text-xs"
            >
              {f.kind === "IMAGE" ? (
                <ImageIcon className="h-3.5 w-3.5" />
              ) : (
                <FileText className="h-3.5 w-3.5" />
              )}
              <span className="max-w-[12rem] truncate">{f.fileName}</span>
              <button
                onClick={() => setFiles((prev) => prev.filter((_, j) => j !== i))}
                className="text-muted-foreground hover:text-destructive"
                aria-label={`Remove ${f.fileName}`}
              >
                <X className="h-3 w-3" />
              </button>
            </span>
          ))}
        </div>
      )}

      <div className="relative">
        {suggestions.length > 0 && (
          <ul className="absolute bottom-full left-4 z-10 mb-2 w-64 overflow-hidden rounded-lg border bg-popover shadow-lg">
            {suggestions.map((s, i) => (
              <li key={s.id}>
                <button
                  onMouseDown={(e) => {
                    // mousedown, not click: the textarea blurring first would
                    // close the list before the click ever landed.
                    e.preventDefault();
                    applySuggestion(s);
                  }}
                  className={cn(
                    "flex w-full items-center gap-2 px-3 py-2 text-left text-sm",
                    i === activeSuggestion ? "bg-accent" : "hover:bg-accent/60"
                  )}
                >
                  <span className="flex h-6 w-6 items-center justify-center rounded-full bg-primary/15 text-[10px] font-semibold text-primary">
                    {s.name.slice(0, 2).toUpperCase()}
                  </span>
                  {s.name}
                </button>
              </li>
            ))}
          </ul>
        )}

        <div className="flex items-end gap-2 p-3">
          <input
            ref={fileInput}
            type="file"
            multiple
            accept="image/*,application/pdf"
            className="hidden"
            onChange={(e) => {
              void addFiles(e.target.files);
              e.target.value = "";
            }}
          />
          <Button
            variant="ghost"
            size="icon"
            className="shrink-0"
            onClick={() => fileInput.current?.click()}
            disabled={files.length >= MAX_ATTACHMENTS}
            aria-label="Attach a file"
          >
            <Paperclip className="h-4 w-4" />
          </Button>

          <textarea
            ref={textarea}
            value={body}
            onChange={onChange}
            onKeyDown={onKeyDown}
            onPaste={onPaste}
            rows={1}
            maxLength={MAX_BODY}
            placeholder="Message the community…  @ to mention, paste a screenshot"
            className="max-h-40 min-h-[2.5rem] flex-1 resize-y rounded-lg border bg-background px-3 py-2 text-sm outline-none focus:ring-2 focus:ring-ring"
          />

          <Button
            size="icon"
            className="shrink-0"
            onClick={() => void send()}
            disabled={pending || uploading > 0 || (!body.trim() && files.length === 0)}
            aria-label="Send"
          >
            {pending || uploading > 0 ? (
              <Loader2 className="h-4 w-4 animate-spin" />
            ) : (
              <Send className="h-4 w-4" />
            )}
          </Button>
        </div>

        {(error || uploading > 0) && (
          <p
            className={cn(
              "px-4 pb-2 text-xs",
              error ? "text-destructive" : "text-muted-foreground"
            )}
          >
            {error ?? `Uploading ${uploading} file${uploading === 1 ? "" : "s"}…`}
          </p>
        )}
      </div>
    </div>
  );
}
