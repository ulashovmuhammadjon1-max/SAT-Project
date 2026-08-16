/**
 * Marking a typed IELTS answer.
 *
 * Listening and Reading are mostly gap-fills, so almost every mark in the
 * objective sections is decided here rather than by a choice id. The rules are
 * deliberately conservative: a student is given the mark when the difference
 * from the key is one IELTS does not care about, and never otherwise.
 */

export interface MarkableQuestion {
  correctAnswer: string;
  /** Alternative spellings, contractions, with/without an article. */
  acceptedAnswers?: string[] | null;
  /** For multi-answer questions: the full set, order-insensitive. */
  correctAnswerSet?: string[] | null;
  caseSensitive?: boolean;
}

/**
 * Normalise for comparison.
 *
 * Curly quotes and non-breaking spaces come in from pasted content and from
 * phone keyboards, and a student who types the right word with a smart
 * apostrophe has not made a mistake. Hyphens are normalised the same way, but
 * NOT removed: "part-time" and "part time" are both accepted through the
 * accepted-answers list rather than by silently deleting punctuation, because
 * deleting it would also mark "co-operate" the same as "cooperate" in a
 * spelling-sensitive question.
 */
export function normalise(raw: string, caseSensitive = false): string {
  let s = (raw ?? "")
    .replace(/[‘’ʼ]/g, "'")
    .replace(/[“”]/g, '"')
    .replace(/[‐-―]/g, "-")
    .replace(/ /g, " ")
    .trim()
    .replace(/\s+/g, " ");
  if (!caseSensitive) s = s.toLowerCase();
  return s;
}

/** Words as IELTS counts them: a hyphenated compound is one word. */
export function countWords(raw: string): number {
  const s = normalise(raw);
  if (!s) return 0;
  return s.split(" ").filter(Boolean).length;
}

/** Numbers as IELTS counts them: "1,500" and "3.5" are each one number. */
export function countNumbers(raw: string): number {
  const matches = normalise(raw).match(/\d[\d.,]*/g);
  return matches ? matches.length : 0;
}

export interface WordLimit {
  maxWords?: number | null;
  maxNumbers?: number | null;
}

export interface LimitCheck {
  ok: boolean;
  words: number;
  numbers: number;
  message?: string;
}

/**
 * Check an answer against a group's word limit.
 *
 * A number written as a numeral does not count toward the word allowance under
 * "NO MORE THAN TWO WORDS AND/OR A NUMBER", so numerals are excluded from the
 * word count before it is compared. Counting "23 March" as two words is the
 * mistake that would reject a correct answer.
 */
export function checkLimit(raw: string, limit: WordLimit): LimitCheck {
  const s = normalise(raw);
  const tokens = s ? s.split(" ").filter(Boolean) : [];
  const numberTokens = tokens.filter((t) => /^\d[\d.,]*$/.test(t));
  const words = tokens.length - numberTokens.length;
  const numbers = numberTokens.length;

  if (limit.maxWords != null && words > limit.maxWords) {
    return {
      ok: false, words, numbers,
      message: `Use no more than ${limit.maxWords} word${limit.maxWords === 1 ? "" : "s"}.`,
    };
  }
  if (limit.maxNumbers != null && numbers > limit.maxNumbers) {
    return {
      ok: false, words, numbers,
      message: `Use no more than ${limit.maxNumbers} number${limit.maxNumbers === 1 ? "" : "s"}.`,
    };
  }
  return { ok: true, words, numbers };
}

/** Split a stored multi-answer value back into its parts. */
function asSet(value: string): string[] {
  const trimmed = value.trim();
  if (trimmed.startsWith("[")) {
    try {
      const parsed = JSON.parse(trimmed);
      if (Array.isArray(parsed)) return parsed.map(String);
    } catch {
      // fall through to the delimiter split
    }
  }
  return trimmed.split(/[,;|]/).map((s) => s.trim()).filter(Boolean);
}

/**
 * Is this answer correct?
 *
 * Returns false for an empty answer rather than throwing, because an unanswered
 * question is a wrong answer and not an error.
 */
export function isAnswerCorrect(
  submitted: string | null | undefined,
  q: MarkableQuestion
): boolean {
  if (submitted === null || submitted === undefined) return false;
  const cs = q.caseSensitive ?? false;
  const given = normalise(submitted, cs);
  if (!given) return false;

  // Multi-answer: compare as sets, so the order the student chose them in
  // cannot cost them the mark.
  if (q.correctAnswerSet && q.correctAnswerSet.length) {
    const want = new Set(q.correctAnswerSet.map((a) => normalise(a, cs)));
    const got = new Set(asSet(submitted).map((a) => normalise(a, cs)));
    if (want.size !== got.size) return false;
    for (const w of want) if (!got.has(w)) return false;
    return true;
  }

  const candidates = [q.correctAnswer, ...(q.acceptedAnswers ?? [])];
  return candidates.some((c) => normalise(c, cs) === given);
}

/** Every answer that would have been marked right, for the review screen. */
export function acceptedAnswerList(q: MarkableQuestion): string[] {
  if (q.correctAnswerSet && q.correctAnswerSet.length) return q.correctAnswerSet;
  return [q.correctAnswer, ...(q.acceptedAnswers ?? [])];
}
