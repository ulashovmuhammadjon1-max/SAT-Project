/**
 * Text annotations (highlights + notes) for the exam passage panel.
 *
 * Annotations are stored as character offsets into the *plain text* of the
 * passage rather than as DOM mutations. That matters because the passage is
 * rendered with `dangerouslySetInnerHTML` and gets re-created whenever the
 * student navigates between questions — anything written directly into the
 * DOM would be wiped. Offsets survive, so we re-apply them after every render.
 */

export const HIGHLIGHT_COLORS = ["yellow", "pink", "blue"] as const;
export type HighlightColor = (typeof HIGHLIGHT_COLORS)[number];

export interface Annotation {
  id: string;
  passageId: string;
  start: number;
  end: number;
  /** The highlighted text itself, kept for the Highlights & Notes list. */
  text: string;
  color: HighlightColor;
  note: string | null;
}

function textNodes(container: Node): Text[] {
  const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT);
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

  const text = range.toString().trim();
  if (!text) return null;

  return { start, end, text };
}

/** Screen position of the current selection, relative to `container`. */
export function selectionAnchor(container: HTMLElement): { x: number; y: number } | null {
  const selection = window.getSelection();
  if (!selection || selection.rangeCount === 0) return null;
  const rect = selection.getRangeAt(0).getBoundingClientRect();
  const base = container.getBoundingClientRect();
  return { x: rect.left - base.left + rect.width / 2, y: rect.top - base.top };
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
