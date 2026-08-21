"use client";

import { useMemo, useState } from "react";

import { Badge } from "@/components/ui/badge";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import {
  buildSegments,
  CATEGORY_STYLES,
  type Category,
  type SegmentAnnotation,
} from "@/lib/ielts/essay-segments";
import { CATEGORY_LABELS } from "@/lib/validations/ielts-essay";
import { cn } from "@/lib/utils";

const ORDER: Category[] = ["GRAMMAR", "VOCABULARY", "COHESION", "COLLOCATION"];

/**
 * The essay, with its annotations drawn over it.
 *
 * Shared by the student's reading page and the admin's review screen on
 * purpose: an admin approving highlights should be looking at exactly what the
 * student will see, not at a different rendering of the same rows.
 *
 * The essay text is rendered from the stored string and never rewritten — the
 * highlights are a layer of spans over it, which is why every offset is
 * verified rather than trusted.
 */
export function EssayReader({
  essayText,
  annotations,
  className,
  onSelectText,
}: {
  essayText: string;
  annotations: SegmentAnnotation[];
  className?: string;
  /** Admin-only: called with the character span the user selected. */
  onSelectText?: (start: number, end: number) => void;
}) {
  const [active, setActive] = useState<Set<Category>>(() => new Set(ORDER));

  const counts = useMemo(() => {
    const c = {} as Record<Category, number>;
    for (const k of ORDER) c[k] = 0;
    for (const a of annotations) c[a.category] = (c[a.category] ?? 0) + 1;
    return c;
  }, [annotations]);

  const segments = useMemo(
    () => buildSegments(essayText, annotations, active),
    [essayText, annotations, active]
  );

  const toggle = (c: Category) =>
    setActive((prev) => {
      const next = new Set(prev);
      // Toggling is local state only — no navigation, no refetch, so a student
      // can flick between categories while reading without losing their place.
      next.has(c) ? next.delete(c) : next.add(c);
      return next;
    });

  /**
   * Map a DOM selection back to character offsets in the original essay.
   *
   * Walks the rendered segments rather than reading `selectionStart`, because
   * the text is split across many spans — the offset the browser reports is
   * relative to one span, not to the essay.
   */
  function handleMouseUp() {
    if (!onSelectText) return;
    const sel = window.getSelection();
    if (!sel || sel.isCollapsed || sel.rangeCount === 0) return;
    const range = sel.getRangeAt(0);

    const offsetOf = (node: Node, offsetInNode: number): number | null => {
      const el = (node.nodeType === Node.TEXT_NODE ? node.parentElement : (node as Element)) as
        | HTMLElement
        | null;
      const holder = el?.closest<HTMLElement>("[data-seg-start]");
      if (!holder) return null;
      return Number(holder.dataset.segStart) + offsetInNode;
    };

    const start = offsetOf(range.startContainer, range.startOffset);
    const end = offsetOf(range.endContainer, range.endOffset);
    if (start == null || end == null || end <= start) return;
    onSelectText(start, end);
  }

  return (
    <div className={cn("space-y-5", className)}>
      {/* Legend — each category toggles its own highlights. */}
      <div className="flex flex-wrap gap-2">
        {ORDER.map((c) => {
          const on = active.has(c);
          const style = CATEGORY_STYLES[c];
          return (
            <button
              key={c}
              type="button"
              onClick={() => toggle(c)}
              aria-pressed={on}
              className={cn(
                "flex items-center gap-2 rounded-full border px-3 py-1.5 text-xs font-medium transition-colors",
                on ? style.chip : "border-border bg-transparent text-muted-foreground hover:bg-secondary"
              )}
            >
              <span className={cn("h-2 w-2 rounded-full", on ? style.dot : "bg-muted-foreground/40")} />
              {CATEGORY_LABELS[c]}
              <span className="tabular-nums opacity-70">{counts[c] ?? 0}</span>
            </button>
          );
        })}
      </div>

      {/* The essay. `whitespace-pre-wrap` preserves the admin's paragraphing
          without turning the text into HTML we would then have to sanitise. */}
      <div
        onMouseUp={handleMouseUp}
        className="whitespace-pre-wrap text-[15px] leading-[1.9] text-foreground sm:text-base"
      >
        {segments.map((seg, i) => {
          if (seg.annotations.length === 0) {
            return (
              <span key={i} data-seg-start={seg.start}>
                {seg.text}
              </span>
            );
          }
          const top = seg.annotations[0];
          const style = CATEGORY_STYLES[top.category];
          return (
            <Popover key={i}>
              <PopoverTrigger asChild>
                <mark
                  data-seg-start={seg.start}
                  tabIndex={0}
                  role="button"
                  className={cn(
                    "cursor-pointer rounded-[3px] bg-transparent px-0.5 text-foreground underline decoration-2 underline-offset-4 transition-colors",
                    style.mark,
                    // More than one category here — a second, offset underline
                    // says so without stacking backgrounds into mud.
                    seg.annotations.length > 1 && "decoration-dotted"
                  )}
                >
                  {seg.text}
                </mark>
              </PopoverTrigger>
              <PopoverContent align="start" className="w-[min(22rem,calc(100vw-2rem))] p-0">
                <div className="max-h-[60vh] divide-y divide-border overflow-y-auto">
                  {seg.annotations.map((a) => (
                    <AnnotationDetail key={a.id} annotation={a} essayText={essayText} />
                  ))}
                </div>
              </PopoverContent>
            </Popover>
          );
        })}
      </div>
    </div>
  );
}

/**
 * One annotation's explanation. Deliberately compact — this is a note in the
 * margin, not a lesson page.
 */
function AnnotationDetail({
  annotation,
  essayText,
}: {
  annotation: SegmentAnnotation;
  essayText: string;
}) {
  const style = CATEGORY_STYLES[annotation.category];
  const sentence = useMemo(
    () => surroundingSentence(essayText, annotation.startOffset, annotation.endOffset),
    [essayText, annotation.startOffset, annotation.endOffset]
  );

  return (
    <div className="space-y-2.5 p-3.5">
      <div className="flex flex-wrap items-center gap-2">
        <span className={cn("h-2 w-2 shrink-0 rounded-full", style.dot)} />
        <span className="text-xs font-semibold">{CATEGORY_LABELS[annotation.category]}</span>
        <Badge variant="outline" className="text-[10px]">
          {annotation.subtype.replace(/_/g, " ")}
        </Badge>
      </div>

      <p className="text-sm font-semibold leading-snug">{annotation.quote}</p>
      <p className="text-sm leading-relaxed text-muted-foreground">{annotation.explanation}</p>

      {annotation.pattern && (
        <div>
          <p className="text-[11px] font-medium uppercase tracking-wide text-muted-foreground">Pattern</p>
          <p className="font-mono text-xs">{annotation.pattern}</p>
        </div>
      )}

      {annotation.ieltsValue && (
        <div>
          <p className="text-[11px] font-medium uppercase tracking-wide text-muted-foreground">
            Why it is useful
          </p>
          <p className="text-sm leading-relaxed text-muted-foreground">{annotation.ieltsValue}</p>
        </div>
      )}

      <div>
        <p className="text-[11px] font-medium uppercase tracking-wide text-muted-foreground">
          In the essay
        </p>
        <p className="text-xs italic leading-relaxed text-muted-foreground">“{sentence}”</p>
      </div>
    </div>
  );
}

/** The sentence the annotation sits in, for context in the popover. */
function surroundingSentence(text: string, start: number, end: number): string {
  const before = text.lastIndexOf(".", start - 1);
  const nl = text.lastIndexOf("\n", start - 1);
  const from = Math.max(before, nl) + 1;
  const dot = text.indexOf(".", end);
  const to = dot === -1 ? text.length : dot + 1;
  return text.slice(from, to).trim();
}
