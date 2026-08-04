// Real Digital SAT Reading & Writing questions always show two things side
// by side: a passage/stimulus on the left (a paragraph, a student's notes,
// a short sentence with a blank — whatever the reading material is) and a
// short instructional question on the right ("Which choice...", "As used in
// the text, what does...", etc.), never both crammed together. Plain-text
// PDF extraction has no notion of that visual split, so the heuristic
// parser has to infer it after the fact.

const BULLET_LINE = /^[ \t]*(?:[•\-*]|\d+[.)])[ \t]+/;
const MIN_PASSAGE_WORDS = 12;

function splitSentences(text: string): string[] {
  // Keeps the terminating punctuation attached to each sentence.
  return (text.match(/[^.?!]+[.?!]+(?:\s|$)/g) ?? [text]).map((s) => s.trim()).filter(Boolean);
}

function wordCount(text: string): number {
  return text.split(/\s+/).filter(Boolean).length;
}

/**
 * Splits a raw extracted block into a passage/stimulus and a short stem, if
 * the block looks like it has one. Returns null when there's nothing worth
 * separating (e.g. a self-contained math problem, or a stem that's already
 * just the instructional question with no lead-in reading material) — the
 * caller should leave the original stem untouched in that case.
 */
export function splitPassageFromStem(raw: string): { passage: string; stem: string } | null {
  const text = raw.trim();
  if (!text) return null;

  const lines = text.split("\n");
  const lastBulletIndex = lines.reduce((last, line, i) => (BULLET_LINE.test(line) ? i : last), -1);

  if (lastBulletIndex !== -1 && lastBulletIndex < lines.length - 1) {
    // Rhetorical-synthesis style: "...following notes: • ... • ... The student
    // wants to X. Which choice...?" — everything through the last bullet is
    // the stimulus; the sentence(s) after it are the actual question.
    const passage = lines.slice(0, lastBulletIndex + 1).join("\n").trim();
    const stem = lines.slice(lastBulletIndex + 1).join("\n").trim();
    if (passage && stem && wordCount(passage) >= MIN_PASSAGE_WORDS) {
      return { passage, stem };
    }
  }

  const sentences = splitSentences(text);
  if (sentences.length < 2) return null;

  const last = sentences[sentences.length - 1];
  if (!last.trim().endsWith("?")) return null;

  const passage = sentences.slice(0, -1).join(" ").trim();
  if (wordCount(passage) < MIN_PASSAGE_WORDS) return null;

  return { passage, stem: last.trim() };
}
