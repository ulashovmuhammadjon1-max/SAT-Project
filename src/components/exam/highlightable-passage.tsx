"use client";

import { useCallback, useEffect, useRef, useState, type MouseEvent as ReactMouseEvent } from "react";
import { Trash2 } from "lucide-react";

import { cn } from "@/lib/utils";
import {
  HIGHLIGHT_COLORS,
  paintAnnotations,
  selectionAnchor,
  selectionToRange,
  type Annotation,
  type HighlightColor,
} from "@/lib/exam/annotations";
import { toPassageHtml } from "@/lib/exam/passage-html";

const SWATCH: Record<HighlightColor, string> = {
  yellow: "#FFE9A6",
  pink: "#FFD0DE",
  blue: "#BFDBFE",
};

type Popup =
  | { mode: "create"; x: number; y: number; start: number; end: number; text: string }
  | { mode: "edit"; x: number; y: number; id: string };

export function HighlightablePassage({
  passageId,
  content,
  annotations,
  onCreate,
  onUpdate,
  onRemove,
  className,
}: {
  passageId: string;
  content: string;
  annotations: Annotation[];
  onCreate: (a: Omit<Annotation, "id">) => void;
  onUpdate: (id: string, patch: Partial<Pick<Annotation, "color" | "note">>) => void;
  onRemove: (id: string) => void;
  className?: string;
}) {
  const bodyRef = useRef<HTMLDivElement>(null);
  const [popup, setPopup] = useState<Popup | null>(null);
  const [noteDraft, setNoteDraft] = useState("");

  // The passage subtree is owned by us, not React — repaint it from source
  // HTML on every change so annotation offsets are always applied to a clean
  // tree (see lib/exam/annotations.ts).
  useEffect(() => {
    if (bodyRef.current) paintAnnotations(bodyRef.current, toPassageHtml(content), annotations);
  }, [content, annotations]);

  // Close the popup when the student navigates to another passage.
  useEffect(() => {
    setPopup(null);
  }, [passageId]);

  const editing = popup?.mode === "edit" ? annotations.find((a) => a.id === popup.id) ?? null : null;

  const handleMouseUp = useCallback(() => {
    const container = bodyRef.current;
    if (!container) return;
    // A click that lands on an existing highlight is handled by onClick below.
    const range = selectionToRange(container);
    if (!range) return;
    const anchor = selectionAnchor(container);
    if (!anchor) return;
    setNoteDraft("");
    setPopup({ mode: "create", x: anchor.x, y: anchor.y, ...range });
  }, []);

  function handleClick(event: ReactMouseEvent) {
    const container = bodyRef.current;
    if (!container) return;
    const mark = (event.target as HTMLElement).closest<HTMLElement>("[data-ann-id]");
    if (!mark) return;
    const id = mark.dataset.annId;
    if (!id) return;
    const rect = mark.getBoundingClientRect();
    const base = container.getBoundingClientRect();
    setNoteDraft(annotations.find((a) => a.id === id)?.note ?? "");
    setPopup({ mode: "edit", x: rect.left - base.left + rect.width / 2, y: rect.top - base.top, id });
  }

  function createWith(color: HighlightColor, note: string | null) {
    if (popup?.mode !== "create") return;
    onCreate({ passageId, start: popup.start, end: popup.end, text: popup.text, color, note });
    window.getSelection()?.removeAllRanges();
    setPopup(null);
    setNoteDraft("");
  }

  function closePopup() {
    window.getSelection()?.removeAllRanges();
    setPopup(null);
    setNoteDraft("");
  }

  return (
    <div className="relative">
      <div
        ref={bodyRef}
        onMouseUp={handleMouseUp}
        onClick={handleClick}
        className={cn("exam-passage select-text text-[16px] leading-[1.7] text-exam-text", className)}
      />

      {popup && (
        <>
          {/* Click-away catcher; sits under the popup itself. */}
          <div className="fixed inset-0 z-20" onMouseDown={closePopup} />
          <div
            style={{ left: popup.x, top: Math.max(popup.y - 8, 4) }}
            className="absolute z-30 w-[248px] -translate-x-1/2 -translate-y-full rounded-md border border-exam-border bg-white p-2.5 shadow-examPopup"
          >
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-1.5">
                {HIGHLIGHT_COLORS.map((color) => {
                  const active = editing?.color === color;
                  return (
                    <button
                      key={color}
                      type="button"
                      title={`${color} highlight`}
                      onClick={() => (editing ? onUpdate(editing.id, { color }) : createWith(color, null))}
                      style={{ backgroundColor: SWATCH[color] }}
                      className={cn(
                        "h-5 w-5 rounded-full border transition-colors",
                        active ? "border-exam-blue ring-1 ring-exam-blue" : "border-exam-border hover:border-exam-muted"
                      )}
                    />
                  );
                })}
              </div>
              {editing && (
                <button
                  type="button"
                  onClick={() => {
                    onRemove(editing.id);
                    closePopup();
                  }}
                  title="Remove highlight"
                  className="flex h-6 w-6 items-center justify-center rounded text-exam-muted hover:bg-exam-hover hover:text-exam-text"
                >
                  <Trash2 className="h-3.5 w-3.5" />
                </button>
              )}
            </div>

            <textarea
              value={noteDraft}
              onChange={(e) => setNoteDraft(e.target.value)}
              placeholder="Add a note…"
              rows={2}
              className="mt-2 w-full resize-none rounded border border-exam-border bg-white px-2 py-1.5 text-[13px] leading-snug text-exam-text placeholder:text-exam-disabled focus:border-exam-blue focus:outline-none"
            />

            <div className="mt-1.5 flex justify-end gap-1.5">
              <button
                type="button"
                onClick={closePopup}
                className="rounded px-2 py-1 text-[13px] font-medium text-exam-muted hover:bg-exam-hover"
              >
                Cancel
              </button>
              <button
                type="button"
                onClick={() => {
                  const note = noteDraft.trim() || null;
                  if (editing) {
                    onUpdate(editing.id, { note });
                    closePopup();
                  } else {
                    createWith("yellow", note);
                  }
                }}
                className="rounded bg-exam-blue px-2.5 py-1 text-[13px] font-medium text-white hover:bg-exam-blueHover"
              >
                Save
              </button>
            </div>
          </div>
        </>
      )}
    </div>
  );
}
