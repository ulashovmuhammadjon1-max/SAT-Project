const BULLET_LINE = /^[ \t]*[•\-*][ \t]+/;
const TEXT_LABEL = /^Text ?\d+$/i;

function escapeHtml(s: string): string {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

/**
 * Passage content is stored as HTML, but content that came from plain-text
 * PDF extraction (the no-API-key heuristic parser, or a plain paste into the
 * admin's raw textarea) has no markup at all -- just newlines, which HTML
 * collapses into one run-on block instead of separate list items. This
 * turns plain text into real paragraphs/lists so bulleted notes render as
 * an actual list. Content that already contains HTML tags is left as-is.
 */
export function toPassageHtml(raw: string): string {
  if (!raw) return raw;
  if (/<[a-z][\s\S]*>/i.test(raw)) return raw;

  const lines = raw
    .split("\n")
    .map((l) => l.trim())
    .filter((l) => l.length > 0);

  const blocks: string[] = [];
  let paragraphBuffer: string[] = [];
  let listBuffer: string[] = [];

  function flushParagraph() {
    if (paragraphBuffer.length) {
      blocks.push(`<p>${escapeHtml(paragraphBuffer.join(" "))}</p>`);
      paragraphBuffer = [];
    }
  }
  function flushList() {
    if (listBuffer.length) {
      const items = listBuffer.map((l) => `<li>${escapeHtml(l.replace(BULLET_LINE, ""))}</li>`).join("");
      blocks.push(`<ul>${items}</ul>`);
      listBuffer = [];
    }
  }

  for (const line of lines) {
    if (BULLET_LINE.test(line)) {
      flushParagraph();
      listBuffer.push(line);
    } else if (TEXT_LABEL.test(line)) {
      flushParagraph();
      flushList();
      blocks.push(`<p><strong>${escapeHtml(line)}</strong></p>`);
    } else {
      flushList();
      paragraphBuffer.push(line);
    }
  }
  flushParagraph();
  flushList();

  return blocks.join("");
}
