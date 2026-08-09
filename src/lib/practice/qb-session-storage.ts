/**
 * Local persistence for a Question Bank practice session.
 *
 * Every answer is already graded and recorded server-side the moment it is
 * submitted (`QuestionAttempt`), so progress statistics are never at risk. What
 * was missing is the *session*: which question you were on, what you had picked
 * but not yet submitted, which choices you had crossed out, and the explanations
 * you had already revealed. All of that lived only in React state, so a refresh,
 * a closed tab or a walk to the kitchen threw it away and dropped the student
 * back on question 1.
 *
 * The browser is the right home for it. It is scratch work for one sitting —
 * the same reasoning that keeps exam highlights in `localStorage` — and it needs
 * no round trip, so it can be written on every keystroke without cost.
 *
 * The stored result shape is declared here rather than imported from the server
 * action so this module never pulls server code into the client bundle. It is
 * structurally identical to `SubmitAnswerResult`; the compiler checks that at
 * both call sites.
 */

const STORAGE_KEY = "satforge-qb-session:1";

/** Bumped when the stored shape changes; older records are discarded on read. */
const VERSION = 1;

export interface StoredQbResult {
  isCorrect: boolean;
  correctChoiceId: string | null;
  correctAnswerFR: string[] | null;
  explanationHtml: string | null;
}

export interface StoredQbQuestionState {
  selectedChoiceId: string | null;
  freeResponseAnswer: string;
  eliminated: string[];
  marked: boolean;
  result: StoredQbResult | null;
  secondsSpent: number;
}

export interface StoredQbSession {
  version: number;
  /**
   * The exact question set this state belongs to. Restoring is only safe when
   * it matches the set currently on screen — the ids are pinned into the URL,
   * so the same link always yields the same signature.
   */
  signature: string;
  /** The link that reopens this session, used by the "continue" card. */
  href: string;
  /** Human label for that card, e.g. "Reading and Writing — Craft and Structure". */
  label: string;
  index: number;
  total: number;
  answered: number;
  correct: number;
  /** Passage/question split, so the layout the student chose comes back too. */
  splitPct: number | null;
  savedAt: string;
  states: StoredQbQuestionState[];
}

export function sessionSignature(questionIds: string[]): string {
  return questionIds.join(",");
}

function isStoredState(value: unknown): value is StoredQbQuestionState {
  if (typeof value !== "object" || value === null) return false;
  const s = value as Record<string, unknown>;
  return (
    (s.selectedChoiceId === null || typeof s.selectedChoiceId === "string") &&
    typeof s.freeResponseAnswer === "string" &&
    Array.isArray(s.eliminated) &&
    typeof s.marked === "boolean" &&
    typeof s.secondsSpent === "number"
  );
}

/**
 * Reads the saved session, or null when there isn't one.
 *
 * Anything unrecognisable — an older version, a truncated write, a hand-edited
 * value — is treated as "no session" rather than trusted, because a malformed
 * record would otherwise restore a student's answers onto the wrong questions.
 */
export function readQbSession(): StoredQbSession | null {
  if (typeof window === "undefined") return null;
  let raw: string | null = null;
  try {
    raw = window.localStorage.getItem(STORAGE_KEY);
  } catch {
    // Private mode / disabled storage. Sessions simply won't persist.
    return null;
  }
  if (!raw) return null;

  try {
    const parsed = JSON.parse(raw) as Partial<StoredQbSession>;
    if (parsed.version !== VERSION) return null;
    if (typeof parsed.signature !== "string" || !parsed.signature) return null;
    if (typeof parsed.href !== "string" || !parsed.href.startsWith("/")) return null;
    if (!Array.isArray(parsed.states) || !parsed.states.every(isStoredState)) return null;
    if (typeof parsed.total !== "number" || parsed.states.length !== parsed.total) return null;
    if (typeof parsed.index !== "number" || parsed.index < 0 || parsed.index >= parsed.total) return null;
    return parsed as StoredQbSession;
  } catch {
    return null;
  }
}

export function writeQbSession(session: StoredQbSession): void {
  if (typeof window === "undefined") return;
  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(session));
  } catch {
    // A quota failure must never interrupt practice.
  }
}

/**
 * Forgets the saved session.
 *
 * With a signature, only that session is cleared: finishing an old session in a
 * background tab must not wipe the one the student started since.
 */
export function clearQbSession(signature?: string): void {
  if (typeof window === "undefined") return;
  try {
    if (signature) {
      const current = readQbSession();
      if (current && current.signature !== signature) return;
    }
    window.localStorage.removeItem(STORAGE_KEY);
  } catch {
    // Nothing to do — the record is unreadable anyway.
  }
}
