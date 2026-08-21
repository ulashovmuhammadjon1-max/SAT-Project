import type { IeltsEssayAnnotationCategory } from "@prisma/client";

/**
 * Turning overlapping annotations into something renderable.
 *
 * A phrase can legitimately be three things at once — "Although public
 * transport plays a crucial role in reducing urban congestion" is a concessive
 * clause, a collocation and topic vocabulary. The data model has to allow that;
 * the reading experience must not become a stack of three background colours,
 * because the essay has to stay readable or the feature is pointless.
 *
 * The resolution: cut the essay at every annotation boundary, so each resulting
 * segment is covered by a fixed set of annotations. A segment is painted in one
 * category — the highest-priority one still switched on — and carries a marker
 * when more apply. Clicking it offers all of them.
 */

export type Category = IeltsEssayAnnotationCategory;

export interface SegmentAnnotation {
  id: string;
  category: Category;
  subtype: string;
  quote: string;
  startOffset: number;
  endOffset: number;
  explanation: string;
  ieltsValue: string | null;
  pattern: string | null;
}

export interface Segment {
  text: string;
  start: number;
  end: number;
  /** Every annotation covering this segment, highest priority first. */
  annotations: SegmentAnnotation[];
}

/**
 * Which colour wins when several cover the same words.
 *
 * Ordered by how specific the teaching point is rather than by importance:
 * a collocation is a particular phrase worth memorising, whereas topic
 * vocabulary is the broadest bucket and the one most likely to swallow a span
 * that is really about something else.
 */
const PRIORITY: Record<Category, number> = {
  COLLOCATION: 0,
  GRAMMAR: 1,
  COHESION: 2,
  VOCABULARY: 3,
};

/**
 * Split `text` into consecutive segments covering it exactly.
 *
 * Guarantees, because the essay must render byte-for-byte as the admin wrote it
 * (§13 — the annotations are a layer over the original, never a rewrite):
 *   - concatenating every segment's text reproduces `text` exactly
 *   - segments are contiguous and in order
 *   - an annotation whose offsets fall outside the text is ignored rather than
 *     throwing, so one bad row cannot blank the page
 */
export function buildSegments(
  text: string,
  annotations: SegmentAnnotation[],
  activeCategories?: Set<Category>
): Segment[] {
  const usable = annotations.filter(
    (a) =>
      a.startOffset >= 0 &&
      a.endOffset <= text.length &&
      a.endOffset > a.startOffset &&
      (!activeCategories || activeCategories.has(a.category))
  );

  if (usable.length === 0) {
    return text ? [{ text, start: 0, end: text.length, annotations: [] }] : [];
  }

  // Every boundary any annotation introduces, plus the ends of the essay.
  const cuts = new Set<number>([0, text.length]);
  for (const a of usable) {
    cuts.add(a.startOffset);
    cuts.add(a.endOffset);
  }
  const points = [...cuts].sort((x, y) => x - y);

  const segments: Segment[] = [];
  for (let i = 0; i < points.length - 1; i++) {
    const start = points[i];
    const end = points[i + 1];
    if (end <= start) continue;

    const covering = usable
      .filter((a) => a.startOffset <= start && a.endOffset >= end)
      .sort(
        (a, b) =>
          PRIORITY[a.category] - PRIORITY[b.category] ||
          a.endOffset - a.startOffset - (b.endOffset - b.startOffset)
      );

    segments.push({ text: text.slice(start, end), start, end, annotations: covering });
  }
  return segments;
}

/** True when the stored quote still matches the text at its own offsets. */
export function annotationIsIntact(text: string, a: SegmentAnnotation): boolean {
  return text.slice(a.startOffset, a.endOffset) === a.quote;
}

/**
 * Subtle, readable highlight styles — background tints rather than the neon
 * marker-pen look, so a paragraph carrying four categories still reads as
 * prose. Colours follow the semantic mapping in the brief (grammar blue,
 * vocabulary green, cohesion orange, collocations purple) and are defined for
 * both themes.
 */
export const CATEGORY_STYLES: Record<Category, { chip: string; mark: string; dot: string }> = {
  GRAMMAR: {
    chip: "border-sky-500/40 bg-sky-500/10 text-sky-700 dark:text-sky-300",
    mark: "bg-sky-500/15 hover:bg-sky-500/25 decoration-sky-500/50",
    dot: "bg-sky-500",
  },
  VOCABULARY: {
    chip: "border-emerald-500/40 bg-emerald-500/10 text-emerald-700 dark:text-emerald-300",
    mark: "bg-emerald-500/15 hover:bg-emerald-500/25 decoration-emerald-500/50",
    dot: "bg-emerald-500",
  },
  COHESION: {
    chip: "border-amber-500/40 bg-amber-500/10 text-amber-700 dark:text-amber-300",
    mark: "bg-amber-500/15 hover:bg-amber-500/25 decoration-amber-500/50",
    dot: "bg-amber-500",
  },
  COLLOCATION: {
    chip: "border-violet-500/40 bg-violet-500/10 text-violet-700 dark:text-violet-300",
    mark: "bg-violet-500/15 hover:bg-violet-500/25 decoration-violet-500/50",
    dot: "bg-violet-500",
  },
};
