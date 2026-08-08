"use server";

import { revalidatePath } from "next/cache";
import { Prisma, type QuestionDifficulty, type Subject } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

/* -------------------------------------------------------------------------- */
/* Filter contract                                                             */
/* -------------------------------------------------------------------------- */

export type AttemptStatus =
  | "ALL"
  | "NOT_ATTEMPTED"
  | "ATTEMPTED"
  | "CORRECT"
  | "INCORRECT"
  | "SAVED";

export interface QuestionBankFilters {
  subject?: Subject;
  domainId?: string;
  skillId?: string;
  difficulties?: QuestionDifficulty[];
  status?: AttemptStatus;
  /** Shorthand for status=NOT_ATTEMPTED; kept separate because the UI exposes it as its own toggle. */
  newOnly?: boolean;
}

/**
 * Per-question rollup of everything this student has ever done, from BOTH
 * sources: Question Bank practice (`QuestionAttempt`) and answers submitted
 * inside a real test (`Response`). A question answered in a mock therefore
 * counts as "attempted" here too, so "new questions only" never resurfaces it.
 *
 * Returned as plain id arrays because callers feed them straight into Prisma
 * `in` / `notIn` filters.
 */
interface UserQuestionState {
  attemptedIds: string[];
  /** Latest answer was correct. */
  correctIds: string[];
  /** Latest answer was wrong — this is what "mistakes" means. */
  incorrectIds: string[];
  savedIds: string[];
}

async function loadUserQuestionState(userId: string): Promise<UserQuestionState> {
  // One row per question the student has touched, carrying the correctness of
  // their most recent answer across both tables.
  const rows = await prisma.$queryRaw<{ questionId: string; isCorrect: boolean }[]>`
    SELECT DISTINCT ON ("questionId") "questionId", "isCorrect"
    FROM (
      SELECT "questionId", "isCorrect", "createdAt" AS at
        FROM "QuestionAttempt"
       WHERE "userId" = ${userId}
      UNION ALL
      SELECT r."questionId", r."isCorrect", COALESCE(r."answeredAt", r."updatedAt") AS at
        FROM "Response" r
        JOIN "Attempt" a ON a.id = r."attemptId"
       WHERE a."userId" = ${userId} AND r."isCorrect" IS NOT NULL
    ) merged
    ORDER BY "questionId", at DESC
  `;

  const saved = await prisma.bookmark.findMany({
    where: { userId },
    select: { questionId: true },
  });

  return {
    attemptedIds: rows.map((r) => r.questionId),
    correctIds: rows.filter((r) => r.isCorrect).map((r) => r.questionId),
    incorrectIds: rows.filter((r) => !r.isCorrect).map((r) => r.questionId),
    savedIds: saved.map((s) => s.questionId),
  };
}

/** Translates filters + this student's history into a Prisma `where` clause. */
function buildWhere(filters: QuestionBankFilters, state: UserQuestionState): Prisma.QuestionWhereInput {
  const where: Prisma.QuestionWhereInput = { isPublished: true };

  if (filters.skillId) where.skillId = filters.skillId;
  else if (filters.domainId) where.domainId = filters.domainId;
  else if (filters.subject) where.domain = { subject: filters.subject };

  if (filters.difficulties?.length) where.difficulty = { in: filters.difficulties };

  const status: AttemptStatus = filters.newOnly ? "NOT_ATTEMPTED" : filters.status ?? "ALL";
  switch (status) {
    case "NOT_ATTEMPTED":
      where.id = { notIn: state.attemptedIds };
      break;
    case "ATTEMPTED":
      where.id = { in: state.attemptedIds };
      break;
    case "CORRECT":
      where.id = { in: state.correctIds };
      break;
    case "INCORRECT":
      where.id = { in: state.incorrectIds };
      break;
    case "SAVED":
      where.id = { in: state.savedIds };
      break;
  }

  return where;
}

/* -------------------------------------------------------------------------- */
/* Progress                                                                    */
/* -------------------------------------------------------------------------- */

export interface QuestionBankOverview {
  totalQuestions: number;
  attempted: number;
  correct: number;
  incorrect: number;
  saved: number;
  /** Percentage of the published bank this student has attempted. */
  completionPct: number;
  /** Share of attempted questions whose latest answer was correct. */
  accuracyPct: number;
  hasData: boolean;
}

export async function getQuestionBankOverview(subject?: Subject): Promise<QuestionBankOverview> {
  const user = await requireUser();
  const state = await loadUserQuestionState(user.id);

  const scope: Prisma.QuestionWhereInput = {
    isPublished: true,
    ...(subject ? { domain: { subject } } : {}),
  };

  // Restrict the student's history to the subject in view so the numbers match
  // the tab they are actually looking at.
  const [totalQuestions, attempted, correct, saved] = await Promise.all([
    prisma.question.count({ where: scope }),
    prisma.question.count({ where: { ...scope, id: { in: state.attemptedIds } } }),
    prisma.question.count({ where: { ...scope, id: { in: state.correctIds } } }),
    prisma.question.count({ where: { ...scope, id: { in: state.savedIds } } }),
  ]);

  const incorrect = attempted - correct;

  return {
    totalQuestions,
    attempted,
    correct,
    incorrect,
    saved,
    completionPct: totalQuestions ? Math.round((attempted / totalQuestions) * 100) : 0,
    accuracyPct: attempted ? Math.round((correct / attempted) * 100) : 0,
    hasData: attempted > 0,
  };
}

export interface SkillProgress {
  skillId: string;
  skillCode: string;
  skillName: string;
  total: number;
  attempted: number;
  correct: number;
  accuracyPct: number;
}

export interface DomainProgress {
  domainId: string;
  domainCode: string;
  domainName: string;
  total: number;
  attempted: number;
  correct: number;
  accuracyPct: number;
  skills: SkillProgress[];
}

/** Domain → subtopic progress for one subject, all from this student's real attempts. */
export async function getDomainProgress(subject: Subject): Promise<DomainProgress[]> {
  const user = await requireUser();
  const state = await loadUserQuestionState(user.id);

  const domains = await prisma.domain.findMany({
    where: { subject },
    orderBy: { code: "asc" },
    include: { skills: { orderBy: { code: "asc" } } },
  });

  // Three grouped counts rather than per-skill queries: totals, attempted and
  // correct. Each returns at most one row per skill.
  const [totals, attemptedBy, correctBy] = await Promise.all([
    prisma.question.groupBy({
      by: ["skillId"],
      where: { isPublished: true, domain: { subject } },
      _count: { _all: true },
    }),
    state.attemptedIds.length
      ? prisma.question.groupBy({
          by: ["skillId"],
          where: { isPublished: true, domain: { subject }, id: { in: state.attemptedIds } },
          _count: { _all: true },
        })
      : Promise.resolve([]),
    state.correctIds.length
      ? prisma.question.groupBy({
          by: ["skillId"],
          where: { isPublished: true, domain: { subject }, id: { in: state.correctIds } },
          _count: { _all: true },
        })
      : Promise.resolve([]),
  ]);

  const totalMap = new Map(totals.map((t) => [t.skillId, t._count._all]));
  const attemptedMap = new Map(attemptedBy.map((t) => [t.skillId, t._count._all]));
  const correctMap = new Map(correctBy.map((t) => [t.skillId, t._count._all]));

  return domains.map((d) => {
    const skills: SkillProgress[] = d.skills.map((s) => {
      const total = totalMap.get(s.id) ?? 0;
      const attempted = attemptedMap.get(s.id) ?? 0;
      const correct = correctMap.get(s.id) ?? 0;
      return {
        skillId: s.id,
        skillCode: s.code,
        skillName: s.name,
        total,
        attempted,
        correct,
        accuracyPct: attempted ? Math.round((correct / attempted) * 100) : 0,
      };
    });

    const total = skills.reduce((n, s) => n + s.total, 0);
    const attempted = skills.reduce((n, s) => n + s.attempted, 0);
    const correct = skills.reduce((n, s) => n + s.correct, 0);

    return {
      domainId: d.id,
      domainCode: d.code,
      domainName: d.name,
      total,
      attempted,
      correct,
      accuracyPct: attempted ? Math.round((correct / attempted) * 100) : 0,
      // Skills with no questions in the bank would render as dead 0/0 rows.
      skills: skills.filter((s) => s.total > 0),
    };
  });
}

/* -------------------------------------------------------------------------- */
/* Browsing & session generation                                               */
/* -------------------------------------------------------------------------- */

export interface QuestionListItem {
  id: string;
  ref: string;
  subject: Subject;
  domainName: string;
  skillName: string;
  difficulty: QuestionDifficulty;
  status: "NOT_ATTEMPTED" | "CORRECT" | "INCORRECT";
  saved: boolean;
}

/** Short human-facing reference, e.g. Q-3F9A2C. Ids are cuids, which read badly. */
function questionRef(id: string) {
  return `Q-${id.slice(-6).toUpperCase()}`;
}

export async function countMatchingQuestions(filters: QuestionBankFilters): Promise<number> {
  const user = await requireUser();
  const state = await loadUserQuestionState(user.id);
  return prisma.question.count({ where: buildWhere(filters, state) });
}

export async function listQuestions(
  filters: QuestionBankFilters,
  page = 1,
  pageSize = 20
): Promise<{ items: QuestionListItem[]; total: number }> {
  const user = await requireUser();
  const state = await loadUserQuestionState(user.id);
  const where = buildWhere(filters, state);

  const [total, rows] = await Promise.all([
    prisma.question.count({ where }),
    prisma.question.findMany({
      where,
      // Never select stem/choices here: the browse list must not leak answers.
      select: {
        id: true,
        difficulty: true,
        domain: { select: { name: true, subject: true } },
        skill: { select: { name: true } },
      },
      orderBy: [{ difficulty: "asc" }, { id: "asc" }],
      skip: (page - 1) * pageSize,
      take: pageSize,
    }),
  ]);

  const correct = new Set(state.correctIds);
  const incorrect = new Set(state.incorrectIds);
  const saved = new Set(state.savedIds);

  return {
    total,
    items: rows.map((q) => ({
      id: q.id,
      ref: questionRef(q.id),
      subject: q.domain.subject,
      domainName: q.domain.name,
      skillName: q.skill.name,
      difficulty: q.difficulty,
      status: correct.has(q.id) ? "CORRECT" : incorrect.has(q.id) ? "INCORRECT" : "NOT_ATTEMPTED",
      saved: saved.has(q.id),
    })),
  };
}

/**
 * Picks question ids for a practice session.
 *
 * Returns fewer than `size` when the filters simply don't match enough — the
 * caller surfaces that honestly rather than padding with unrelated questions.
 */
export async function generateSession(
  filters: QuestionBankFilters,
  size: number
): Promise<string[]> {
  const user = await requireUser();
  const state = await loadUserQuestionState(user.id);
  const where = buildWhere(filters, state);

  // Ids only, then shuffle in memory. The bank is small enough that this beats
  // ORDER BY random() and keeps the selection provably within the filters.
  const rows = await prisma.question.findMany({ where, select: { id: true } });

  for (let i = rows.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [rows[i], rows[j]] = [rows[j], rows[i]];
  }

  return rows.slice(0, Math.max(1, size)).map((r) => r.id);
}

/** "Practice my mistakes" — most recently missed first. */
export async function generateMistakeSession(size: number, subject?: Subject): Promise<string[]> {
  const user = await requireUser();
  const state = await loadUserQuestionState(user.id);
  if (!state.incorrectIds.length) return [];

  const rows = await prisma.question.findMany({
    where: {
      isPublished: true,
      id: { in: state.incorrectIds },
      ...(subject ? { domain: { subject } } : {}),
    },
    select: { id: true },
  });
  const eligible = new Set(rows.map((r) => r.id));

  // Order by when the miss happened, newest first.
  const recency = await prisma.$queryRaw<{ questionId: string }[]>`
    SELECT "questionId", MAX(at) AS at
    FROM (
      SELECT "questionId", "createdAt" AS at FROM "QuestionAttempt" WHERE "userId" = ${user.id}
      UNION ALL
      SELECT r."questionId", COALESCE(r."answeredAt", r."updatedAt")
        FROM "Response" r JOIN "Attempt" a ON a.id = r."attemptId"
       WHERE a."userId" = ${user.id}
    ) x
    GROUP BY "questionId"
    ORDER BY at DESC
  `;

  const ordered = recency.map((r) => r.questionId).filter((id) => eligible.has(id));
  return ordered.slice(0, Math.max(1, size));
}

/* -------------------------------------------------------------------------- */
/* Answering                                                                   */
/* -------------------------------------------------------------------------- */

export interface SubmitAnswerResult {
  isCorrect: boolean;
  correctChoiceId: string | null;
  correctAnswerFR: string[] | null;
  explanationHtml: string | null;
}

/**
 * Grades one Question Bank answer and records it.
 *
 * Grading happens here, server-side, from the stored answer key — the client
 * never receives the correct answer until after it submits.
 */
export async function submitQuestionAnswer(input: {
  questionId: string;
  selectedChoiceId?: string | null;
  freeResponseAnswer?: string | null;
  timeSpentSeconds?: number;
}): Promise<SubmitAnswerResult> {
  const user = await requireUser();

  const question = await prisma.question.findUnique({
    where: { id: input.questionId },
    include: { choices: true, explanation: true },
  });
  if (!question || !question.isPublished) throw new Error("Question not found.");

  let isCorrect = false;
  let correctAnswerFR: string[] | null = null;

  if (question.type === "FREE_RESPONSE") {
    // Stored as a JSON-encoded array of accepted answers.
    try {
      const accepted = JSON.parse(question.correctAnswerFR ?? "[]");
      correctAnswerFR = Array.isArray(accepted) ? accepted.map(String) : [];
    } catch {
      correctAnswerFR = [];
    }
    const given = (input.freeResponseAnswer ?? "").trim();
    isCorrect = correctAnswerFR.some((a) => a.trim() === given);
  } else {
    const correctChoice = question.choices.find((c) => c.isCorrect);
    isCorrect = !!correctChoice && correctChoice.id === input.selectedChoiceId;
  }

  await prisma.questionAttempt.create({
    data: {
      userId: user.id,
      questionId: question.id,
      selectedChoiceId: input.selectedChoiceId ?? null,
      freeResponseAnswer: input.freeResponseAnswer ?? null,
      isCorrect,
      timeSpentSeconds: Math.max(0, Math.round(input.timeSpentSeconds ?? 0)),
    },
  });

  const today = new Date();
  today.setHours(0, 0, 0, 0);
  await prisma.studyActivity.upsert({
    where: { userId_date: { userId: user.id, date: today } },
    create: { userId: user.id, date: today, questionsAnswered: 1 },
    update: { questionsAnswered: { increment: 1 } },
  });

  revalidatePath("/practice");

  return {
    isCorrect,
    correctChoiceId: question.choices.find((c) => c.isCorrect)?.id ?? null,
    correctAnswerFR,
    explanationHtml: question.explanation?.content ?? null,
  };
}

/* -------------------------------------------------------------------------- */
/* History                                                                     */
/* -------------------------------------------------------------------------- */

export interface HistoryItem {
  questionId: string;
  ref: string;
  subject: Subject;
  domainName: string;
  skillName: string;
  isCorrect: boolean;
  at: Date;
  source: "BANK" | "TEST";
}

export async function getRecentActivity(limit = 20): Promise<HistoryItem[]> {
  const user = await requireUser();

  const rows = await prisma.$queryRaw<
    { questionId: string; isCorrect: boolean; at: Date; source: string }[]
  >`
    SELECT "questionId", "isCorrect", at, source FROM (
      SELECT "questionId", "isCorrect", "createdAt" AS at, 'BANK' AS source
        FROM "QuestionAttempt" WHERE "userId" = ${user.id}
      UNION ALL
      SELECT r."questionId", r."isCorrect", COALESCE(r."answeredAt", r."updatedAt"), 'TEST'
        FROM "Response" r JOIN "Attempt" a ON a.id = r."attemptId"
       WHERE a."userId" = ${user.id} AND r."isCorrect" IS NOT NULL
    ) merged
    ORDER BY at DESC
    LIMIT ${limit}
  `;

  if (!rows.length) return [];

  const questions = await prisma.question.findMany({
    where: { id: { in: rows.map((r) => r.questionId) } },
    select: {
      id: true,
      domain: { select: { name: true, subject: true } },
      skill: { select: { name: true } },
    },
  });
  const meta = new Map(questions.map((q) => [q.id, q]));

  return rows.flatMap((r) => {
    const q = meta.get(r.questionId);
    if (!q) return [];
    return [
      {
        questionId: r.questionId,
        ref: questionRef(r.questionId),
        subject: q.domain.subject,
        domainName: q.domain.name,
        skillName: q.skill.name,
        isCorrect: r.isCorrect,
        at: r.at,
        source: r.source === "BANK" ? ("BANK" as const) : ("TEST" as const),
      },
    ];
  });
}
