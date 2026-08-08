/**
 * Text annotations (highlights + notes) for the exam's readable regions —
 * the passage panel and the question stem.
 *
 * Annotations are stored as character offsets into the *plain text* of the
 * region rather than as DOM mutations. That matters because the region is
 * rendered with `dangerouslySetInnerHTML` and gets re-created whenever the
 * student navigates between questions — anything written directly into the
 * DOM would be wiped. Offsets survive, so we re-apply them after every render.
 */

export const HIGHLIGHT_COLORS = ["yellow", "pink", "blue"] as const;
export type HighlightColor = (typeof HIGHLIGHT_COLORS)[number];

export interface Annotation {
  id: string;
  /**
   * Which readable region this belongs to: a `Passage.id` for the reading
   * panel, or `stem:<questionId>` for a question stem. Offsets are only ever
   * meaningful within one region, so this scopes them.
   */
  regionId: string;
  start: number;
  end: number;
  /** The highlighted text itself, kept for the Highlights & Notes list. */
  text: string;
  color: HighlightColor;
  note: string | null;
  /**
   * A highlight the student is composing but has not saved yet. Painted like a
   * real one so they can see exactly which words they picked — the native
   * selection disappears the moment focus moves into the note field, which
   * otherwise leaves them choosing a colour for text they can no longer see.
   */
  pending?: boolean;
}

/** Region key for a question stem, kept in one place so both sides agree. */
export function stemRegionId(questionId: string): string {
  return `stem:${questionId}`;
}

/**
 * Text nodes of `container`, in document order, **excluding anything inside
 * KaTeX output**. A rendered formula is a dense tree of positioned spans whose
 * text nodes carry no meaning on their own ("x", "2", "+"), and splitting one
 * to insert a `<mark>` visibly breaks the typesetting. Skipping the whole
 * subtree means math simply isn't selectable for highlighting — and because
 * the same filter runs when *measuring* a selection and when *painting* it,
 * offsets stay consistent on both sides.
 */
function textNodes(container: Node): Text[] {
  const walker = document.createTreeWalker(container, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      if (node.nodeType === Node.ELEMENT_NODE) {
        return (node as Element).classList?.contains("katex")
          ? NodeFilter.FILTER_REJECT // skips the element *and* its descendants
          : NodeFilter.FILTER_SKIP; // keep walking into it, but don't collect it
      }
      return NodeFilter.FILTER_ACCEPT;
    },
  });
  const out: Text[] = [];
  let node: Node | null;
  while ((node = walker.nextNode())) out.push(node as Text);
  return out;
}

/** Character offset of (node, offset) measured from the start of `container`. */
function offsetOf(container: Node, node: Node, nodeOffset: number): number | null {
  let total = 0;
  for (const text of textNodes(container)) {
    if (text === node) return total + nodeOffset;
    total += text.data.length;
  }
  // The boundary may sit on an element rather than a text node (e.g. the user
  // dragged past the end of a paragraph). Fall back to the containing element.
  if (node.nodeType === Node.ELEMENT_NODE) {
    const child = node.childNodes[nodeOffset] ?? null;
    if (child) return offsetOf(container, child, 0);
  }
  return null;
}

/**
 * Convert the current window selection into offsets relative to `container`.
 * Returns null when there is no usable selection inside the container.
 */
export function selectionToRange(container: HTMLElement): { start: number; end: number; text: string } | null {
  const selection = window.getSelection();
  if (!selection || selection.isCollapsed || selection.rangeCount === 0) return null;

  const range = selection.getRangeAt(0);
  if (!container.contains(range.commonAncestorContainer)) return null;

  const start = offsetOf(container, range.startContainer, range.startOffset);
  const end = offsetOf(container, range.endContainer, range.endOffset);
  if (start === null || end === null || start >= end) return null;

  // Read the label back out of the offsets rather than using
  // `range.toString()`: the range may cross a KaTeX formula, which the offsets
  // deliberately exclude, and the stored label should describe what actually
  // gets painted.
  const text = plainText(container).slice(start, end).trim();
  if (!text) return null;

  return { start, end, text };
}

/** The annotatable text of `container`, i.e. everything offsets are measured against. */
function plainText(container: HTMLElement): string {
  return textNodes(container)
    .map((t) => t.data)
    .join("");
}

/**
 * Screen position of the current selection, relative to `container`. Both
 * edges are returned (not just the top) so the popup can flip below the
 * selection when it's too close to the top of the passage for the popup to
 * fit above it without being clipped off-screen.
 */
export function selectionAnchor(container: HTMLElement): { x: number; top: number; bottom: number } | null {
  const selection = window.getSelection();
  if (!selection || selection.rangeCount === 0) return null;
  const rect = selection.getRangeAt(0).getBoundingClientRect();
  const base = container.getBoundingClientRect();
  return { x: rect.left - base.left + rect.width / 2, top: rect.top - base.top, bottom: rect.bottom - base.top };
}

/** Wrap one offset range in `<mark>` elements, splitting text nodes as needed. */
function wrap(container: HTMLElement, annotation: Annotation) {
  const { start, end } = annotation;
  const targets: { node: Text; from: number; to: number }[] = [];

  let pos = 0;
  for (const text of textNodes(container)) {
    const nodeStart = pos;
    const nodeEnd = pos + text.data.length;
    pos = nodeEnd;
    if (nodeEnd <= start || nodeStart >= end) continue;
    targets.push({
      node: text,
      from: Math.max(0, start - nodeStart),
      to: Math.min(text.data.length, end - nodeStart),
    });
  }

  for (const target of targets) {
    if (target.to <= target.from) continue;
    // splitText leaves `node` holding [0, from) and returns the remainder;
    // splitting the remainder again isolates exactly the annotated slice.
    const middle = target.node.splitText(target.from);
    middle.splitText(target.to - target.from);

    const mark = document.createElement("mark");
    mark.className = "sat-highlight";
    mark.dataset.annId = annotation.id;
    mark.dataset.color = annotation.color;
    if (annotation.pending) mark.dataset.pending = "1";
    if (annotation.note) {
      mark.dataset.note = "1";
      mark.title = annotation.note;
    }
    middle.parentNode?.insertBefore(mark, middle);
    mark.appendChild(middle);
  }
}

/**
 * Re-render `container` from `html` and paint every annotation onto it.
 * Called after each render, so the DOM is always rebuilt from source first —
 * which keeps offsets stable no matter how many times this runs.
 */
export function paintAnnotations(container: HTMLElement, html: string, annotations: Annotation[]) {
  container.innerHTML = html;
  // Applied one at a time, re-walking between each: wrapping never changes
  // the container's textContent, so earlier offsets stay valid for later ones.
  for (const annotation of annotations) wrap(container, annotation);
}
