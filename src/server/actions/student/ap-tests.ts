"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { courseForSubject, subjectByCode } from "@/lib/ap/catalog";
import { canFill, selectQuestions } from "@/lib/ap/test-selection";
import {
  AP_TESTS,
  findTest,
  sectionOffsets,
  testDurationMinutes,
  testQuestionCount,
  testUnits,
  testsForSubject,
  type ApPracticeTest,
} from "@/lib/ap/tests";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

/**
 * AP practice tests: listing, starting, saving, grading, and the result.
 *
 * Three rules hold everywhere in this file.
 *
 *  1. **Ownership is checked on every call.** An attempt id from the browser is
 *     a claim, never a credential — every read and write filters on the
 *     signed-in user's id, so a guessed id resolves to nothing.
 *  2. **The exam payload carries no answer key.** `getTestAttempt` selects the
 *     stem and the choices and deliberately not `correctIndex`; grading happens
 *     in `submitTest` against a fresh read of the bank.
 *  3. **The clock is server-issued.** `expiresAt` is computed here from the
 *     configured duration, so the countdown the browser renders is a display of
 *     a deadline it cannot move.
 */

// ---------------------------------------------------------------------------
// Listing
// ---------------------------------------------------------------------------

export interface ApTestSectionSummary {
  id: string;
  name: string;
  short: string;
  questionCount: number;
  timeLimitMinutes: number;
  calculator: string;
}

export interface ApTestSummary {
  slug: string;
  name: string;
  blurb: string;
  questionCount: number;
  minutes: number;
  calculatorNote: string;
  referenceNote: string | null;
  sections: ApTestSectionSummary[];
  /** Attempts this student has finished. */
  attemptCount: number;
  /** Set when a sitting is open — the card offers Resume rather than Start. */
  inProgressAttemptId: string | null;
  bestScore: { score: number; total: number; percent: number } | null;
  lastScore: { score: number; total: number; percent: number } | null;
  lastAttemptId: string | null;
  lastSubmittedAt: Date | null;
}

export interface ApSubjectTests {
  code: string;
  slug: string;
  name: string;
  short: string;
  gradient: string;
  tests: ApTestSummary[];
  /** Configured tests the bank cannot fill yet — shown honestly, not hidden. */
  notReadyCount: number;
  questionCount: number;
}

const pct = (a: number, b: number) => (b === 0 ? 0 : Math.round((a / b) * 100));

function summarize(
  test: ApPracticeTest,
  attempts: {
    id: string;
    testSlug: string;
    status: string;
    score: number | null;
    total: number | null;
    submittedAt: Date | null;
  }[],
): ApTestSummary {
  const mine = attempts.filter((a) => a.testSlug === test.slug);
  const open = mine.find((a) => a.status === "IN_PROGRESS") ?? null;
  const done = mine
    .filter((a) => a.status === "SUBMITTED" && a.score !== null && a.total !== null)
    .sort((a, b) => (a.submittedAt?.getTime() ?? 0) - (b.submittedAt?.getTime() ?? 0));

  const last = done.length ? done[done.length - 1] : null;
  const best = done.reduce<(typeof done)[number] | null>((acc, a) => {
    if (!acc) return a;
    return pct(a.score!, a.total!) > pct(acc.score!, acc.total!) ? a : acc;
  }, null);

  const asScore = (a: (typeof done)[number] | null) =>
    a ? { score: a.score!, total: a.total!, percent: pct(a.score!, a.total!) } : null;

  return {
    slug: test.slug,
    name: test.name,
    blurb: test.blurb,
    questionCount: testQuestionCount(test),
    minutes: testDurationMinutes(test),
    calculatorNote: test.calculatorNote,
    referenceNote: test.referenceNote ?? null,
    sections: test.sections.map((s) => ({
      id: s.id,
      name: s.name,
      short: s.short,
      questionCount: s.questionCount,
      timeLimitMinutes: s.timeLimitMinutes,
      calculator: s.calculator,
    })),
    attemptCount: done.length,
    inProgressAttemptId: open?.id ?? null,
    bestScore: asScore(best),
    lastScore: asScore(last),
    lastAttemptId: last?.id ?? null,
    lastSubmittedAt: last?.submittedAt ?? null,
  };
}

/**
 * The student's subjects, each with the tests their bank can actually support.
 *
 * One groupBy over the whole ApQuestion table rather than a count per test: the
 * catalog is growing towards thirty subjects and a query per card would be a
 * real N+1 on the first page of the feature.
 */
export async function listTestsForMySubjects(): Promise<ApSubjectTests[]> {
  const user = await requireUser();

  const [enrollments, counts, attempts] = await Promise.all([
    prisma.apSubjectEnrollment.findMany({
      where: { userId: user.id },
      orderBy: { addedAt: "asc" },
      select: { subject: true },
    }),
    prisma.apQuestion.groupBy({ by: ["subject", "unit"], _count: { id: true } }),
    prisma.apTestAttempt.findMany({
      where: { userId: user.id },
      select: {
        id: true,
        subject: true,
        testSlug: true,
        status: true,
        score: true,
        total: true,
        submittedAt: true,
      },
    }),
  ]);

  const available = new Map<string, Map<number, number>>();
  for (const row of counts) {
    const forSubject = available.get(row.subject) ?? new Map<number, number>();
    forSubject.set(row.unit, row._count.id);
    available.set(row.subject, forSubject);
  }

  return enrollments.flatMap((e) => {
    const entry = subjectByCode(e.subject);
    if (!entry) return [];
    const units = available.get(e.subject) ?? new Map<number, number>();
    const configured = testsForSubject(e.subject);
    const ready = configured.filter((t) => canFill(t, units));
    const mine = attempts.filter((a) => a.subject === e.subject);

    return [
      {
        code: entry.code,
        slug: entry.slug,
        name: entry.name,
        short: entry.short,
        gradient: entry.gradient,
        tests: ready.map((t) => summarize(t, mine)),
        notReadyCount: configured.length - ready.length,
        questionCount: [...units.values()].reduce((n, c) => n + c, 0),
      },
    ];
  });
}

/** One subject's tests, for the step-two page. Null when not enrolled. */
export async function listTestsForSubject(subjectSlug: string): Promise<ApSubjectTests | null> {
  const all = await listTestsForMySubjects();
  return all.find((s) => s.slug === subjectSlug) ?? null;
}

// ---------------------------------------------------------------------------
// Starting
// ---------------------------------------------------------------------------

const startSchema = z.object({
  subject: z.string().min(1).max(64),
  testSlug: z.string().min(1).max(64),
});

export interface StartTestResult {
  attemptId?: string;
  /** True when an open sitting was picked up rather than a new one started. */
  resumed?: boolean;
  error?: string;
}

export async function startTest(input: {
  subject: string;
  testSlug: string;
}): Promise<StartTestResult> {
  const user = await requireUser();
  const parsed = startSchema.safeParse(input);
  if (!parsed.success) return { error: "That test does not exist." };

  const test = findTest(parsed.data.subject, parsed.data.testSlug);
  if (!test) return { error: "That test does not exist." };

  // Enrolled subjects only: the picker offers nothing else, so anything reaching
  // here for a subject the student has not added is a hand-built request.
  const enrolled = await prisma.apSubjectEnrollment.findFirst({
    where: { userId: user.id, subject: test.subject },
    select: { id: true },
  });
  if (!enrolled) return { error: "Add this subject to your list before taking its tests." };

  // Resume an open sitting rather than starting a second one. An open sitting
  // whose clock has already run out is finalised first, so a student who closed
  // the tab an hour ago gets their score rather than a dead attempt.
  const open = await prisma.apTestAttempt.findFirst({
    where: { userId: user.id, subject: test.subject, testSlug: test.slug, status: "IN_PROGRESS" },
    orderBy: { startedAt: "desc" },
    select: { id: true, expiresAt: true },
  });
  if (open) {
    if (!open.expiresAt || open.expiresAt.getTime() > Date.now()) {
      return { attemptId: open.id, resumed: true };
    }
    await gradeAndClose(open.id, user.id);
  }

  const bank = await prisma.apQuestion.findMany({
    where: { subject: test.subject, unit: { in: testUnits(test) } },
    select: { id: true, unit: true, topic: true },
  });
  const questionIds = selectQuestions(test, bank);
  if (!questionIds) {
    return { error: "This test isn't ready yet — its question bank is still being written." };
  }

  const attempt = await prisma.apTestAttempt.create({
    data: {
      userId: user.id,
      subject: test.subject,
      testSlug: test.slug,
      status: "IN_PROGRESS",
      questionIdsJson: JSON.stringify(questionIds),
      answersJson: "{}",
      markedJson: "[]",
      expiresAt: new Date(Date.now() + testDurationMinutes(test) * 60_000),
    },
    select: { id: true },
  });

  revalidatePath("/ap/tests");
  return { attemptId: attempt.id };
}

// ---------------------------------------------------------------------------
// The exam payload — no answer key anywhere in it
// ---------------------------------------------------------------------------

export interface ApExamQuestion {
  id: string;
  stem: string;
  table: { headers: string[]; rows: string[][] } | null;
  choices: string[];
  unit: number;
  topic: string;
  topicTitle: string;
}

export interface ApExamPayload {
  attemptId: string;
  subject: string;
  subjectName: string;
  subjectSlug: string;
  testSlug: string;
  testName: string;
  status: string;
  startedAt: string;
  expiresAt: string;
  calculatorNote: string;
  referenceNote: string | null;
  sections: {
    id: string;
    name: string;
    short: string;
    calculator: string;
    directions: string;
    timeLimitMinutes: number;
    /** Index of this section's first question in the flat list. */
    offset: number;
    count: number;
  }[];
  questions: ApExamQuestion[];
  answers: Record<string, number>;
  marked: string[];
}

function parseJson<T>(raw: string, fallback: T): T {
  try {
    return JSON.parse(raw) as T;
  } catch {
    return fallback;
  }
}

/**
 * Everything the exam page needs, and nothing more.
 *
 * `correctIndex` and `explanation` are not selected. That is the reason grading
 * cannot be read out of the network tab, and it is why this is a separate query
 * from the one `getTestResult` runs.
 */
export async function getTestAttempt(attemptId: string): Promise<ApExamPayload | null> {
  const user = await requireUser();
  const attempt = await prisma.apTestAttempt.findFirst({
    where: { id: attemptId, userId: user.id },
    select: {
      id: true,
      subject: true,
      testSlug: true,
      status: true,
      questionIdsJson: true,
      answersJson: true,
      markedJson: true,
      startedAt: true,
      expiresAt: true,
    },
  });
  if (!attempt) return null;

  const test = findTest(attempt.subject, attempt.testSlug);
  const entry = subjectByCode(attempt.subject);
  if (!test || !entry) return null;

  const ids = parseJson<string[]>(attempt.questionIdsJson, []);
  const rows = await prisma.apQuestion.findMany({
    where: { id: { in: ids } },
    select: {
      id: true,
      stem: true,
      tableJson: true,
      choicesJson: true,
      unit: true,
      topic: true,
      topicTitle: true,
    },
  });
  const byId = new Map(rows.map((r) => [r.id, r]));

  // Order by the frozen list, and drop anything the bank no longer holds rather
  // than rendering a hole. Sections are re-derived below from what survived.
  const questions: ApExamQuestion[] = [];
  const kept: string[] = [];
  for (const id of ids) {
    const r = byId.get(id);
    if (!r) continue;
    kept.push(id);
    questions.push({
      id: r.id,
      stem: r.stem,
      table: r.tableJson ? parseJson(r.tableJson, null) : null,
      choices: parseJson<string[]>(r.choicesJson, []),
      unit: r.unit,
      topic: r.topic,
      topicTitle: r.topicTitle,
    });
  }

  // Section boundaries come from the configuration, clamped to what is actually
  // present — a config edited under a live attempt shortens the last section
  // instead of pointing past the end of the array.
  const offsets = sectionOffsets(test);
  const sections = test.sections.map((s, i) => {
    const offset = Math.min(offsets[i], questions.length);
    const count = Math.max(0, Math.min(s.questionCount, questions.length - offset));
    return {
      id: s.id,
      name: s.name,
      short: s.short,
      calculator: s.calculator,
      directions: s.directions,
      timeLimitMinutes: s.timeLimitMinutes,
      offset,
      count,
    };
  });

  const answers = parseJson<Record<string, number>>(attempt.answersJson, {});
  const marked = parseJson<string[]>(attempt.markedJson, []);
  const keptSet = new Set(kept);

  return {
    attemptId: attempt.id,
    subject: attempt.subject,
    subjectName: entry.name,
    subjectSlug: entry.slug,
    testSlug: attempt.testSlug,
    testName: test.name,
    status: attempt.status,
    startedAt: attempt.startedAt.toISOString(),
    expiresAt: (
      attempt.expiresAt ??
      new Date(attempt.startedAt.getTime() + testDurationMinutes(test) * 60_000)
    ).toISOString(),
    calculatorNote: test.calculatorNote,
    referenceNote: test.referenceNote ?? null,
    sections: sections.filter((s) => s.count > 0),
    questions,
    answers: Object.fromEntries(
      Object.entries(answers).filter(([id, v]) => keptSet.has(id) && Number.isInteger(v)),
    ),
    marked: marked.filter((id) => keptSet.has(id)),
  };
}

// ---------------------------------------------------------------------------
// Saving mid-exam
// ---------------------------------------------------------------------------

const saveSchema = z.object({
  attemptId: z.string().min(1).max(64),
  answers: z.record(z.number().int().min(0).max(9)),
  marked: z.array(z.string().min(1).max(64)).max(300),
});

export interface SaveProgressResult {
  ok?: boolean;
  /** The clock ran out — the client should submit rather than keep writing. */
  expired?: boolean;
  error?: string;
}

/**
 * Persists the answers and the review flags. Called on a debounce, so it has to
 * be cheap and it has to be safe to lose: the exam is still correct if the last
 * few seconds of typing never land, because every write is the whole state, not
 * a delta.
 */
export async function saveProgress(input: {
  attemptId: string;
  answers: Record<string, number>;
  marked: string[];
}): Promise<SaveProgressResult> {
  const user = await requireUser();
  const parsed = saveSchema.safeParse(input);
  if (!parsed.success) return { error: "Could not save that." };

  const attempt = await prisma.apTestAttempt.findFirst({
    where: { id: parsed.data.attemptId, userId: user.id },
    select: { id: true, status: true, questionIdsJson: true, expiresAt: true },
  });
  if (!attempt) return { error: "That test attempt does not exist." };
  if (attempt.status !== "IN_PROGRESS") return { error: "This test has already been submitted." };
  if (attempt.expiresAt && attempt.expiresAt.getTime() <= Date.now()) {
    // Writing after the deadline would let a student keep answering past time.
    return { expired: true };
  }

  // Only ids frozen into this attempt are storable, so a crafted payload cannot
  // pad the answer map with questions the test never contained.
  const allowed = new Set(parseJson<string[]>(attempt.questionIdsJson, []));
  const answers: Record<string, number> = {};
  for (const [id, choice] of Object.entries(parsed.data.answers)) {
    if (allowed.has(id)) answers[id] = choice;
  }
  const marked = parsed.data.marked.filter((id) => allowed.has(id));

  await prisma.apTestAttempt.update({
    where: { id: attempt.id },
    data: { answersJson: JSON.stringify(answers), markedJson: JSON.stringify(marked) },
  });

  return { ok: true };
}

// ---------------------------------------------------------------------------
// Submitting
// ---------------------------------------------------------------------------

/**
 * Grades an attempt and closes it. Shared by `submitTest` and by the
 * auto-finalisation of an abandoned sitting in `startTest`.
 *
 * Returns null when the attempt is not this user's or is already submitted —
 * both of which the caller reports rather than silently re-grading.
 */
async function gradeAndClose(
  attemptId: string,
  userId: string,
): Promise<{ score: number; total: number } | null> {
  const attempt = await prisma.apTestAttempt.findFirst({
    where: { id: attemptId, userId },
    select: { id: true, status: true, questionIdsJson: true, answersJson: true },
  });
  if (!attempt || attempt.status !== "IN_PROGRESS") return null;

  const ids = parseJson<string[]>(attempt.questionIdsJson, []);
  const answers = parseJson<Record<string, number>>(attempt.answersJson, {});

  const keys = await prisma.apQuestion.findMany({
    where: { id: { in: ids } },
    select: { id: true, correctIndex: true },
  });
  const keyById = new Map(keys.map((k) => [k.id, k.correctIndex]));

  let score = 0;
  const graded: { questionId: string; chosenIndex: number; isCorrect: boolean }[] = [];
  for (const id of ids) {
    const chosen = answers[id];
    if (!Number.isInteger(chosen)) continue; // skipped
    const key = keyById.get(id);
    if (key === undefined) continue;
    const isCorrect = chosen === key;
    if (isCorrect) score++;
    graded.push({ questionId: id, chosenIndex: chosen, isCorrect });
  }
  const total = ids.length;

  await prisma.$transaction(async (tx) => {
    // Guarded update: if a second submit raced this one, the where clause
    // matches nothing and the attempt is graded exactly once.
    const updated = await tx.apTestAttempt.updateMany({
      where: { id: attempt.id, userId, status: "IN_PROGRESS" },
      data: { status: "SUBMITTED", submittedAt: new Date(), score, total },
    });
    if (updated.count === 0) return;

    // Practice-test work feeds the same progress the Question Bank uses, so a
    // topic answered inside a test counts on the course page too.
    if (graded.length) {
      await tx.apQuestionAttempt.createMany({
        data: graded.map((g) => ({
          userId,
          questionId: g.questionId,
          chosenIndex: g.chosenIndex,
          isCorrect: g.isCorrect,
        })),
      });
    }
  });

  return { score, total };
}

export interface SubmitTestResult {
  ok?: boolean;
  score?: number;
  total?: number;
  error?: string;
}

export async function submitTest(attemptId: string): Promise<SubmitTestResult> {
  const user = await requireUser();
  if (typeof attemptId !== "string" || attemptId.length === 0 || attemptId.length > 64) {
    return { error: "That test attempt does not exist." };
  }

  const attempt = await prisma.apTestAttempt.findFirst({
    where: { id: attemptId, userId: user.id },
    select: { id: true, status: true, subject: true },
  });
  if (!attempt) return { error: "That test attempt does not exist." };
  if (attempt.status !== "IN_PROGRESS") return { error: "This test has already been submitted." };

  const result = await gradeAndClose(attempt.id, user.id);
  if (!result) return { error: "This test has already been submitted." };

  revalidatePath("/ap/tests");
  const entry = subjectByCode(attempt.subject);
  if (entry) {
    revalidatePath(`/ap/tests/${entry.slug}`);
    revalidatePath(`/ap/${entry.slug}`);
  }
  return { ok: true, score: result.score, total: result.total };
}

// ---------------------------------------------------------------------------
// The result
// ---------------------------------------------------------------------------

export interface ApResultQuestion {
  id: string;
  number: number;
  sectionId: string;
  unit: number;
  topic: string;
  topicTitle: string;
  stem: string;
  table: { headers: string[]; rows: string[][] } | null;
  choices: string[];
  correctIndex: number;
  chosenIndex: number | null;
  isCorrect: boolean;
  explanation: string | null;
}

export interface ApResultBreakdown {
  key: string;
  label: string;
  sublabel?: string;
  total: number;
  correct: number;
  incorrect: number;
  skipped: number;
  percent: number;
  /** Set only where the topic maps onto a live practice route. */
  practiceHref?: string;
}

export interface ApTestResult {
  attemptId: string;
  subject: string;
  subjectName: string;
  subjectSlug: string;
  testSlug: string;
  testName: string;
  score: number;
  total: number;
  percent: number;
  correct: number;
  incorrect: number;
  skipped: number;
  startedAt: Date;
  submittedAt: Date | null;
  timeSpentSeconds: number;
  allowedMinutes: number;
  sections: ApResultBreakdown[];
  units: ApResultBreakdown[];
  topics: ApResultBreakdown[];
  /** Weakest topics first, already filtered to ones worth practising. */
  weakest: ApResultBreakdown[];
  questions: ApResultQuestion[];
}

function tally(
  rows: ApResultQuestion[],
  key: string,
  label: string,
  extra: Partial<ApResultBreakdown> = {},
): ApResultBreakdown {
  const correct = rows.filter((r) => r.isCorrect).length;
  const skipped = rows.filter((r) => r.chosenIndex === null).length;
  return {
    key,
    label,
    total: rows.length,
    correct,
    incorrect: rows.length - correct - skipped,
    skipped,
    percent: pct(correct, rows.length),
    ...extra,
  };
}

export async function getTestResult(attemptId: string): Promise<ApTestResult | null> {
  const user = await requireUser();
  const attempt = await prisma.apTestAttempt.findFirst({
    where: { id: attemptId, userId: user.id },
    select: {
      id: true,
      subject: true,
      testSlug: true,
      status: true,
      questionIdsJson: true,
      answersJson: true,
      startedAt: true,
      submittedAt: true,
      score: true,
      total: true,
    },
  });
  if (!attempt || attempt.status !== "SUBMITTED") return null;

  const test = findTest(attempt.subject, attempt.testSlug);
  const entry = subjectByCode(attempt.subject);
  if (!test || !entry) return null;

  const ids = parseJson<string[]>(attempt.questionIdsJson, []);
  const answers = parseJson<Record<string, number>>(attempt.answersJson, {});
  const rows = await prisma.apQuestion.findMany({
    where: { id: { in: ids } },
    select: {
      id: true,
      stem: true,
      tableJson: true,
      choicesJson: true,
      correctIndex: true,
      explanation: true,
      unit: true,
      topic: true,
      topicTitle: true,
    },
  });
  const byId = new Map(rows.map((r) => [r.id, r]));

  // Which section each position falls in, from the configuration.
  const offsets = sectionOffsets(test);
  const sectionAt = (position: number) => {
    for (let i = test.sections.length - 1; i >= 0; i--) {
      if (position >= offsets[i]) return test.sections[i];
    }
    return test.sections[0];
  };

  const questions: ApResultQuestion[] = [];
  ids.forEach((id, i) => {
    const r = byId.get(id);
    if (!r) return;
    const chosen = Number.isInteger(answers[id]) ? answers[id] : null;
    questions.push({
      id: r.id,
      number: i + 1,
      sectionId: sectionAt(i).id,
      unit: r.unit,
      topic: r.topic,
      topicTitle: r.topicTitle,
      stem: r.stem,
      table: r.tableJson ? parseJson(r.tableJson, null) : null,
      choices: parseJson<string[]>(r.choicesJson, []),
      correctIndex: r.correctIndex,
      chosenIndex: chosen,
      isCorrect: chosen !== null && chosen === r.correctIndex,
      explanation: r.explanation,
    });
  });

  const course = courseForSubject(attempt.subject);
  const unitTitle = (n: number) =>
    course?.units.find((u) => u.number === n)?.title ?? `Unit ${n}`;
  // Only link a topic that the practice route can actually serve.
  const practicableTopics = new Set(
    course?.units.flatMap((u) => u.topics?.map((t) => t.code) ?? []) ?? [],
  );

  const sections = test.sections.map((s) =>
    tally(
      questions.filter((q) => q.sectionId === s.id),
      s.id,
      s.name,
      { sublabel: `${s.timeLimitMinutes} min` },
    ),
  );

  const unitNumbers = [...new Set(questions.map((q) => q.unit))].sort((a, b) => a - b);
  const units = unitNumbers.map((n) =>
    tally(
      questions.filter((q) => q.unit === n),
      String(n),
      `Unit ${n} — ${unitTitle(n)}`,
    ),
  );

  const topicCodes = [...new Set(questions.map((q) => q.topic))].sort(
    (a, b) => Number(a) - Number(b) || a.localeCompare(b),
  );
  const topics = topicCodes.map((code) => {
    const forTopic = questions.filter((q) => q.topic === code);
    return tally(forTopic, code, `${code} ${forTopic[0].topicTitle}`, {
      sublabel: `Unit ${forTopic[0].unit}`,
      practiceHref: practicableTopics.has(code)
        ? `/ap/practice/${entry.slug}/${code}`
        : undefined,
    });
  });

  // Weakest areas: anything below three quarters, worst first, and only where
  // enough questions were asked for the number to mean something.
  const weakest = topics
    .filter((t) => t.total >= 2 && t.percent < 75)
    .sort((a, b) => a.percent - b.percent || b.total - a.total)
    .slice(0, 6);

  const correct = questions.filter((q) => q.isCorrect).length;
  const skipped = questions.filter((q) => q.chosenIndex === null).length;
  const submittedAt = attempt.submittedAt;

  return {
    attemptId: attempt.id,
    subject: attempt.subject,
    subjectName: entry.name,
    subjectSlug: entry.slug,
    testSlug: attempt.testSlug,
    testName: test.name,
    score: attempt.score ?? correct,
    total: attempt.total ?? questions.length,
    percent: pct(attempt.score ?? correct, attempt.total ?? questions.length),
    correct,
    incorrect: questions.length - correct - skipped,
    skipped,
    startedAt: attempt.startedAt,
    submittedAt,
    timeSpentSeconds: submittedAt
      ? Math.max(0, Math.round((submittedAt.getTime() - attempt.startedAt.getTime()) / 1000))
      : 0,
    allowedMinutes: testDurationMinutes(test),
    sections,
    units,
    topics,
    weakest,
    questions,
  };
}

/** Every configured test, for a health check or an admin view. */
export async function listAllConfiguredTests(): Promise<
  { subject: string; slug: string; name: string; questions: number; minutes: number }[]
> {
  return AP_TESTS.map((t) => ({
    subject: t.subject,
    slug: t.slug,
    name: t.name,
    questions: testQuestionCount(t),
    minutes: testDurationMinutes(t),
  }));
}
