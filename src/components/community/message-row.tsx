"use client";

import { useEffect, useRef, useState } from "react";
import { CornerUpLeft, FileText, Pencil, Shield, SmilePlus, Trash2 } from "lucide-react";

import { MessageText } from "@/components/community/message-text";
import { REACTIONS, type CommunityMessageView } from "@/lib/community/types";
import { cn } from "@/lib/utils";

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
  const sameDay = d.toDateString() === new Date().toDateString();
  return sameDay
    ? d.toLocaleTimeString(undefined, { hour: "2-digit", minute: "2-digit" })
    : `${d.toLocaleDateString(undefined, { day: "numeric", month: "short" })} ${d.toLocaleTimeString(
        undefined,
        { hour: "2-digit", minute: "2-digit" }
      )}`;
}

function fileSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${Math.round(bytes / 1024)} KB`;
  return `${(bytes / 1024 / 1024).toFixed(1)} MB`;
}

export function MessageRow({
  message: m,
  grouped,
  onReply,
  onDelete,
  onEdit,
  onReact,
}: {
  message: CommunityMessageView;
  grouped: boolean;
  onReply: () => void;
  onDelete: () => void;
  onEdit: (body: string) => Promise<void>;
  onReact: (emoji: string) => void;
}) {
  const [editing, setEditing] = useState(false);
  const [draft, setDraft] = useState(m.body);
  const [saving, setSaving] = useState(false);
  const [pickerOpen, setPickerOpen] = useState(false);
  const editBox = useRef<HTMLTextAreaElement>(null);
  const picker = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (editing) {
      const el = editBox.current;
      el?.focus();
      // Caret at the end, not the start — an edit is almost always an addition
      // or a fix near the end, never a rewrite from character zero.
      el?.setSelectionRange(el.value.length, el.value.length);
    }
  }, [editing]);

  // Close the emoji picker on an outside click, the way every popover should.
  useEffect(() => {
    if (!pickerOpen) return;
    function onDown(e: MouseEvent) {
      if (picker.current && !picker.current.contains(e.target as Node)) setPickerOpen(false);
    }
    document.addEventListener("mousedown", onDown);
    return () => document.removeEventListener("mousedown", onDown);
  }, [pickerOpen]);

  async function save() {
    const next = draft.trim();
    if (!next || next === m.body) {
      setEditing(false);
      setDraft(m.body);
      return;
    }
    setSaving(true);
    await onEdit(next);
    setSaving(false);
    setEditing(false);
  }

  return (
    <div
      className={cn(
        "group relative rounded-lg px-3 py-1.5 transition-colors hover:bg-secondary/50",
        m.mentionedMe && "bg-primary/5 ring-1 ring-primary/20",
        grouped ? "mt-0.5" : "mt-4"
      )}
    >
      {m.replyTo && (
        <div className="mb-1 flex items-center gap-1.5 pl-12 text-xs text-muted-foreground">
          <CornerUpLeft className="h-3.5 w-3.5 shrink-0" />
          <span className="font-medium text-foreground/80">{m.replyTo.authorName}</span>
          <span className={cn("truncate", m.replyTo.deleted && "italic")}>{m.replyTo.excerpt}</span>
        </div>
      )}

      <div className="flex gap-3">
        <div className="w-9 shrink-0">
          {!grouped && (
            <span
              className={cn(
                "flex h-9 w-9 items-center justify-center rounded-full text-xs font-semibold",
                m.author.isAdmin ? "bg-navy-900 text-white" : "bg-primary/15 text-primary"
              )}
            >
              {initials(m.author.name)}
            </span>
          )}
        </div>

        <div className="min-w-0 flex-1">
          {!grouped && (
            <div className="flex flex-wrap items-baseline gap-2">
              <span className="font-medium">{m.author.name}</span>
              {m.author.isAdmin && (
                <span className="flex items-center gap-0.5 rounded bg-navy-900 px-1.5 py-px text-[10px] font-medium text-white">
                  <Shield className="h-2.5 w-2.5" /> Team
                </span>
              )}
              <span className="text-xs text-muted-foreground">{timeLabel(m.createdAt)}</span>
            </div>
          )}

          {m.deleted ? (
            <p className="italic text-muted-foreground">This message was deleted.</p>
          ) : editing ? (
            <div className="mt-1 space-y-2">
              <textarea
                ref={editBox}
                value={draft}
                onChange={(e) => setDraft(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === "Enter" && !e.shiftKey) {
                    e.preventDefault();
                    void save();
                  }
                  if (e.key === "Escape") {
                    setEditing(false);
                    setDraft(m.body);
                  }
                }}
                rows={2}
                className="w-full resize-y rounded-lg border bg-background px-3 py-2 outline-none focus:ring-2 focus:ring-ring"
              />
              <p className="text-xs text-muted-foreground">
                <button
                  onClick={() => void save()}
                  disabled={saving}
                  className="font-medium text-primary hover:underline disabled:opacity-50"
                >
                  {saving ? "Saving…" : "Save"}
                </button>
                {" · "}
                <button
                  onClick={() => {
                    setEditing(false);
                    setDraft(m.body);
                  }}
                  className="hover:underline"
                >
                  Cancel
                </button>
                {" · Enter to save, Escape to cancel"}
              </p>
            </div>
          ) : (
            <>
              {m.body && (
                <MessageText
                  body={m.body}
                  className="whitespace-pre-wrap break-words leading-relaxed"
                />
              )}
              {m.editedAt && (
                <span className="ml-1 align-baseline text-[11px] text-muted-foreground">
                  (edited)
                </span>
              )}
              {m.attachments.length > 0 && (
                <div className="mt-2 flex flex-wrap gap-2">
                  {m.attachments.map((a) =>
                    a.kind === "IMAGE" ? (
                      <a key={a.id} href={a.url} target="_blank" rel="noopener noreferrer">
                        {/* eslint-disable-next-line @next/next/no-img-element */}
                        <img
                          src={a.url}
                          alt={a.fileName}
                          className="max-h-80 max-w-full rounded-lg border object-contain"
                        />
                      </a>
                    ) : (
                      <a
                        key={a.id}
                        href={a.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="flex items-center gap-2 rounded-lg border bg-secondary/40 px-3 py-2 text-sm hover:bg-secondary"
                      >
                        <FileText className="h-4 w-4 shrink-0 text-muted-foreground" />
                        <span className="max-w-[16rem] truncate font-medium">{a.fileName}</span>
                        <span className="text-xs text-muted-foreground">
                          {fileSize(a.sizeBytes)}
                        </span>
                      </a>
                    )
                  )}
                </div>
              )}
            </>
          )}

          {m.reactions.length > 0 && !editing && (
            <div className="mt-1.5 flex flex-wrap gap-1">
              {m.reactions.map((r) => (
                <button
                  key={r.emoji}
                  onClick={() => onReact(r.emoji)}
                  title={r.mine ? "Remove your reaction" : "React"}
                  className={cn(
                    "flex items-center gap-1 rounded-full border px-2 py-0.5 text-xs transition-colors",
                    r.mine
                      ? "border-primary/50 bg-primary/10 text-primary"
                      : "bg-secondary/60 hover:bg-secondary"
                  )}
                >
                  <span className="text-sm leading-none">{r.emoji}</span>
                  <span className="tabular-nums">{r.count}</span>
                </button>
              ))}
            </div>
          )}
        </div>

        {!m.deleted && !editing && (
          <div className="absolute right-2 top-0 hidden items-center gap-1 group-hover:flex group-focus-within:flex">
            <div className="relative" ref={picker}>
              <button
                onClick={() => setPickerOpen((v) => !v)}
                className="rounded border bg-card p-1.5 text-muted-foreground shadow-sm hover:text-foreground"
                aria-label="Add reaction"
              >
                <SmilePlus className="h-4 w-4" />
              </button>
              {pickerOpen && (
                <div className="absolute right-0 top-full z-20 mt-1 flex gap-0.5 rounded-lg border bg-popover p-1.5 shadow-lg">
                  {REACTIONS.map((e) => (
                    <button
                      key={e}
                      onClick={() => {
                        onReact(e);
                        setPickerOpen(false);
                      }}
                      className="rounded p-1 text-lg leading-none hover:bg-accent"
                      aria-label={`React with ${e}`}
                    >
                      {e}
                    </button>
                  ))}
                </div>
              )}
            </div>

            <button
              onClick={onReply}
              className="rounded border bg-card p-1.5 text-muted-foreground shadow-sm hover:text-foreground"
              aria-label="Reply"
            >
              <CornerUpLeft className="h-4 w-4" />
            </button>

            {m.canEdit && (
              <button
                onClick={() => {
                  setDraft(m.body);
                  setEditing(true);
                }}
                className="rounded border bg-card p-1.5 text-muted-foreground shadow-sm hover:text-foreground"
                aria-label="Edit message"
              >
                <Pencil className="h-4 w-4" />
              </button>
            )}

            {m.canDelete && (
              <button
                onClick={onDelete}
                className="rounded border bg-card p-1.5 text-muted-foreground shadow-sm hover:text-destructive"
                aria-label="Delete message"
              >
                <Trash2 className="h-4 w-4" />
              </button>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
