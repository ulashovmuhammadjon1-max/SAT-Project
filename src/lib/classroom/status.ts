/**
 * The one place submission status is decided.
 *
 * Student pages, teacher tracking and the badges all derive from here, so
 * "submitted" can never mean different things on different screens. The rules:
 *
 *  - A TEST assignment is submitted by submitting the linked practice test.
 *  - A QUESTIONS assignment is submitted by answering every assigned question;
 *    partway through is IN_PROGRESS.
 *  - A TASK (free-form) assignment is submitted by handing work in. Uploaded
 *    work that has not been handed in is a DRAFT.
 *  - Anything unsubmitted past its due date is MISSING; work handed in after
 *    the due date is LATE (still submitted — late is a fact, not a rejection).
 */

export type AssignmentKind = "TASK" | "TEST" | "QUESTIONS";

export type SubmissionStatus =
  | "NOT_STARTED"
  | "IN_PROGRESS"
  | "DRAFT"
  | "SUBMITTED"
  | "LATE"
  | "MISSING";

export function assignmentKind(a: { testId: string | null; questionIds: string[] }): AssignmentKind {
  if (a.testId) return "TEST";
  if (a.questionIds.length > 0) return "QUESTIONS";
  return "TASK";
}

export interface StatusInput {
  kind: AssignmentKind;
  dueAt: Date | null;
  /** TASK: when the student handed in; null while drafting or untouched. */
  submittedAt: Date | null;
  /** TASK: a completion row exists (some work is saved). */
  hasWork: boolean;
  /** QUESTIONS: progress through the assigned set. */
  answered: number;
  total: number;
  /** TEST: a submitted attempt of the linked test exists. */
  testSubmitted: boolean;
  now?: Date;
}

export function deriveStatus(s: StatusInput): SubmissionStatus {
  const now = s.now ?? new Date();
  const pastDue = s.dueAt !== null && s.dueAt.getTime() < now.getTime();

  if (s.kind === "TEST") {
    if (s.testSubmitted) return "SUBMITTED";
    return pastDue ? "MISSING" : "NOT_STARTED";
  }

  if (s.kind === "QUESTIONS") {
    if (s.total > 0 && s.answered >= s.total) return "SUBMITTED";
    if (s.answered > 0) return pastDue ? "MISSING" : "IN_PROGRESS";
    return pastDue ? "MISSING" : "NOT_STARTED";
  }

  // TASK
  if (s.submittedAt) {
    return s.dueAt && s.submittedAt.getTime() > s.dueAt.getTime() ? "LATE" : "SUBMITTED";
  }
  if (s.hasWork) return pastDue ? "MISSING" : "DRAFT";
  return pastDue ? "MISSING" : "NOT_STARTED";
}

/** Submitted in either flavour — the "this one is done" test. */
export function isDone(status: SubmissionStatus): boolean {
  return status === "SUBMITTED" || status === "LATE";
}

/** Human-readable file size for the upload lists. */
export function formatBytes(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(0)} KB`;
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
}

/** Due-date phrasing a student actually reads: "Due tomorrow · 11:59 PM". */
export function formatDue(dueAt: Date, now = new Date()): string {
  const time = dueAt.toLocaleTimeString(undefined, { hour: "numeric", minute: "2-digit" });
  const startOfDay = (d: Date) => new Date(d.getFullYear(), d.getMonth(), d.getDate()).getTime();
  const days = Math.round((startOfDay(dueAt) - startOfDay(now)) / 86_400_000);

  if (days === 0) return `Due today · ${time}`;
  if (days === 1) return `Due tomorrow · ${time}`;
  if (days === -1) return `Was due yesterday · ${time}`;
  const date = dueAt.toLocaleDateString(undefined, { month: "short", day: "numeric" });
  if (days < 0) return `Was due ${date}`;
  return `Due ${date} · ${time}`;
}
