"use server";

import { z } from "zod";

import { AP_COURSES, type ApSubjectCode } from "@/lib/ap/courses";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

/**
 * AP practice. Grading happens here, never in the browser: the questions a
 * page receives carry no correct index, and an answer comes back graded with
 * its explanation only after the student has committed to a choice.
 */

export interface ApTopicProgress {
  topic: string;
  total: number;
  answered: number;
  correct: number;
}

export interface ApSubjectProgress {
  subject: ApSubjectCode;
  total: number;
  answered: number;
  correct: number;
  topics: ApTopicProgress[];
}

/** Question counts and this student's progress, for the hub and subject pages. */
export async function getApProgress(): Promise<ApSubjectProgress[]> {
  const user = await requireUser();

  const [questions, attempts] = await Promise.all([
    prisma.apQuestion.groupBy({ by: ["subject", "topic"], _count: { id: true } }),
    prisma.apQuestionAttempt.findMany({
      where: { userId: user.id },
      select: { questionId: true, isCorrect: true, createdAt: true },
      orderBy: { createdAt: "asc" },
    }),
  ]);

  // Latest attempt per question decides its state.
  const latest = new Map<string, boolean>();
  for (const a of attempts) latest.set(a.questionId, a.isCorrect);

  // Attempted question ids need their (subject, topic) to bucket them.
  const attemptedIds = [...latest.keys()];
  const attemptedMeta = attemptedIds.length
    ? await prisma.apQuestion.findMany({
        where: { id: { in: attemptedIds } },
        select: { id: true, subject: true, topic: true },
      })
    : [];

  return AP_COURSES.map((course) => {
    const topicRows = questions.filter((q) => q.subject === course.code);
    const topics = topicRows.map((row) => {
      const mine = attemptedMeta.filter(
        (m) => m.subject === course.code && m.topic === row.topic,
      );
      return {
        topic: row.topic,
        total: row._count.id,
        answered: mine.length,
        correct: mine.filter((m) => latest.get(m.id)).length,
      };
    });
    return {
      subject: course.code,
      total: topics.reduce((s, t) => s + t.total, 0),
      answered: topics.reduce((s, t) => s + t.answered, 0),
      correct: topics.reduce((s, t) => s + t.correct, 0),
      topics,
    };
  });
}

export interface ApSessionQuestion {
  id: string;
  order: number;
  stem: string;
  table: { headers: string[]; rows: string[][] } | null;
  choices: string[];
  /** The student's latest recorded choice, so a revisit shows where they left off. */
  priorChoice: number | null;
  priorCorrect: boolean | null;
}

/** A topic's questions, correct answers withheld. */
export async function getTopicSession(
  subject: string,
  topic: string,
): Promise<ApSessionQuestion[]> {
  const user = await requireUser();
  const rows = await prisma.apQuestion.findMany({
    where: { subject, topic },
    orderBy: { order: "asc" },
    select: { id: true, order: true, stem: true, tableJson: true, choicesJson: true },
  });
  if (rows.length === 0) return [];

  const attempts = await prisma.apQuestionAttempt.findMany({
    where: { userId: user.id, questionId: { in: rows.map((r) => r.id) } },
    orderBy: { createdAt: "asc" },
    select: { questionId: true, chosenIndex: true, isCorrect: true },
  });
  const prior = new Map<string, { chosenIndex: number; isCorrect: boolean }>();
  for (const a of attempts) prior.set(a.questionId, a);

  return rows.map((r) => ({
    id: r.id,
    order: r.order,
    stem: r.stem,
    table: r.tableJson ? JSON.parse(r.tableJson) : null,
    choices: JSON.parse(r.choicesJson),
    priorChoice: prior.get(r.id)?.chosenIndex ?? null,
    priorCorrect: prior.get(r.id)?.isCorrect ?? null,
  }));
}

const answerSchema = z.object({
  questionId: z.string().min(1),
  // Econ questions carry five choices (A-E), Calculus four (A-D); the real
  // bound is the question's own choice count, checked after the lookup.
  chosenIndex: z.number().int().min(0).max(4),
});

export interface ApAnswerResult {
  ok?: boolean;
  error?: string;
  isCorrect?: boolean;
  correctIndex?: number;
  explanation?: string | null;
}

/** Grade one answer and record the attempt. */
export async function answerApQuestion(input: {
  questionId: string;
  chosenIndex: number;
}): Promise<ApAnswerResult> {
  const user = await requireUser();
  const parsed = answerSchema.safeParse(input);
  if (!parsed.success) return { error: "Pick one of the five choices." };

  const q = await prisma.apQuestion.findUnique({
    where: { id: parsed.data.questionId },
    select: { id: true, correctIndex: true, explanation: true, choicesJson: true },
  });
  if (!q) return { error: "That question no longer exists." };

  const choiceCount = (JSON.parse(q.choicesJson) as string[]).length;
  if (parsed.data.chosenIndex >= choiceCount) {
    return { error: "Pick one of the listed choices." };
  }

  const isCorrect = parsed.data.chosenIndex === q.correctIndex;
  await prisma.apQuestionAttempt.create({
    data: {
      userId: user.id,
      questionId: q.id,
      chosenIndex: parsed.data.chosenIndex,
      isCorrect,
    },
  });

  return { ok: true, isCorrect, correctIndex: q.correctIndex, explanation: q.explanation };
}
