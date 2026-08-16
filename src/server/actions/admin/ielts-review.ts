"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { getReviewerCapabilities } from "@/lib/ielts/access";
import { speakingBand, toHalfBand, writingTaskBand } from "@/lib/ielts/bands";

export interface ReviewResult {
  ok?: boolean;
  error?: string;
}

/** Admins review; approved reviewers review what they are assigned. */
async function canReview(kind: "WRITING" | "SPEAKING") {
  const user = await requireUser();
  if (user.role === "ADMIN") return { userId: user.id, ok: true as const };
  const caps = await getReviewerCapabilities(user.id);
  const allowed =
    kind === "WRITING" ? caps?.canReviewWriting : caps?.canReviewSpeaking;
  if (!allowed) return { userId: user.id, ok: false as const };
  return { userId: user.id, ok: true as const };
}

/** Every criterion must be a real half band between 0 and 9. */
function validBands(values: number[]): string | null {
  for (const v of values) {
    if (!Number.isFinite(v)) return "Give a band for every criterion.";
    if (v < 0 || v > 9) return "Bands run from 0 to 9.";
    if (Math.round(v * 2) !== v * 2) return "Bands go in half steps: 6, 6.5, 7.";
  }
  return null;
}

export interface WritingReviewInput {
  submissionId: string;
  /** Task Achievement for Task 1, Task Response for Task 2. */
  taskBand: number;
  coherenceBand: number;
  lexicalBand: number;
  grammarBand: number;
  overallFeedback?: string;
  didWell?: string;
  toImprove?: string;
  taskResponseNotes?: string;
  coherenceNotes?: string;
  vocabularyNotes?: string;
  grammarNotes?: string;
  nextSteps?: string;
}

export async function submitWritingReview(input: WritingReviewInput): Promise<ReviewResult> {
  const auth = await canReview("WRITING");
  if (!auth.ok) return { error: "You are not approved to review Writing." };

  const bands = [input.taskBand, input.coherenceBand, input.lexicalBand, input.grammarBand];
  const bad = validBands(bands);
  if (bad) return { error: bad };

  const submission = await prisma.ieltsWritingSubmission.findUnique({
    where: { id: input.submissionId },
    select: { id: true, attemptId: true },
  });
  if (!submission) return { error: "Submission not found." };

  // The four criteria carry equal weight WITHIN a task; Task 2's double weight
  // applies when the two tasks are combined, not here.
  const overall = writingTaskBand({
    task: input.taskBand, coherence: input.coherenceBand,
    lexical: input.lexicalBand, grammar: input.grammarBand,
  });

  await prisma.$transaction(async (tx) => {
    await tx.ieltsWritingReview.upsert({
      where: { submissionId: submission.id },
      create: {
        submissionId: submission.id, reviewerId: auth.userId,
        taskBand: input.taskBand, coherenceBand: input.coherenceBand,
        lexicalBand: input.lexicalBand, grammarBand: input.grammarBand,
        overallBand: overall,
        overallFeedback: input.overallFeedback ?? null,
        didWell: input.didWell ?? null, toImprove: input.toImprove ?? null,
        taskResponseNotes: input.taskResponseNotes ?? null,
        coherenceNotes: input.coherenceNotes ?? null,
        vocabularyNotes: input.vocabularyNotes ?? null,
        grammarNotes: input.grammarNotes ?? null,
        nextSteps: input.nextSteps ?? null,
        completedAt: new Date(),
      },
      update: {
        reviewerId: auth.userId,
        taskBand: input.taskBand, coherenceBand: input.coherenceBand,
        lexicalBand: input.lexicalBand, grammarBand: input.grammarBand,
        overallBand: overall,
        overallFeedback: input.overallFeedback ?? null,
        didWell: input.didWell ?? null, toImprove: input.toImprove ?? null,
        taskResponseNotes: input.taskResponseNotes ?? null,
        coherenceNotes: input.coherenceNotes ?? null,
        vocabularyNotes: input.vocabularyNotes ?? null,
        grammarNotes: input.grammarNotes ?? null,
        nextSteps: input.nextSteps ?? null,
        completedAt: new Date(),
      },
    });
    await tx.ieltsWritingSubmission.update({
      where: { id: submission.id }, data: { status: "COMPLETE" },
    });
    await rollUpWriting(tx, submission.attemptId);
  });

  revalidatePath("/admin/ielts/writing");
  revalidatePath("/ielts/feedback");
  return { ok: true };
}

/**
 * Combine the reviewed tasks into the attempt's Writing band.
 *
 * Task 2 counts twice. With only one task reviewed there is nothing to weight,
 * so that task's own band stands — reporting a half-finished paper as if both
 * tasks were in would understate a student who has written one good essay.
 */
async function rollUpWriting(
  tx: Parameters<Parameters<typeof prisma.$transaction>[0]>[0],
  attemptId: string
) {
  const rows = await tx.ieltsWritingSubmission.findMany({
    where: { attemptId },
    select: { partId: true, review: { select: { overallBand: true } } },
  });
  const parts = await tx.ieltsPart.findMany({
    where: { id: { in: rows.map((r) => r.partId) } },
    select: { id: true, partNumber: true },
  });
  const numberOf = new Map(parts.map((p) => [p.id, p.partNumber]));

  let t1: number | null = null, t2: number | null = null;
  for (const r of rows) {
    if (!r.review) continue;
    if (numberOf.get(r.partId) === 1) t1 = r.review.overallBand;
    if (numberOf.get(r.partId) === 2) t2 = r.review.overallBand;
  }
  const band =
    t1 != null && t2 != null ? toHalfBand((t1 + t2 * 2) / 3)
      : t2 ?? t1 ?? null;
  if (band == null) return;

  await tx.ieltsAttempt.update({
    where: { id: attemptId },
    data: { writingBand: band, status: "COMPLETE" },
  });
}

export interface SpeakingReviewInput {
  submissionId: string;
  fluencyBand: number;
  lexicalBand: number;
  grammarBand: number;
  pronunciationBand: number;
  overallFeedback?: string;
  fluencyNotes?: string;
  vocabularyNotes?: string;
  grammarNotes?: string;
  pronunciationNotes?: string;
  strongPoints?: string;
  weaknesses?: string;
  howToImprove?: string;
}

export async function submitSpeakingReview(input: SpeakingReviewInput): Promise<ReviewResult> {
  const auth = await canReview("SPEAKING");
  if (!auth.ok) return { error: "You are not approved to review Speaking." };

  const bands = [input.fluencyBand, input.lexicalBand, input.grammarBand, input.pronunciationBand];
  const bad = validBands(bands);
  if (bad) return { error: bad };

  const submission = await prisma.ieltsSpeakingSubmission.findUnique({
    where: { id: input.submissionId },
    select: { id: true, attemptId: true },
  });
  if (!submission) return { error: "Submission not found." };

  const overall = speakingBand({
    fluency: input.fluencyBand, lexical: input.lexicalBand,
    grammar: input.grammarBand, pronunciation: input.pronunciationBand,
  });

  await prisma.$transaction(async (tx) => {
    const data = {
      reviewerId: auth.userId,
      fluencyBand: input.fluencyBand, lexicalBand: input.lexicalBand,
      grammarBand: input.grammarBand, pronunciationBand: input.pronunciationBand,
      overallBand: overall,
      overallFeedback: input.overallFeedback ?? null,
      fluencyNotes: input.fluencyNotes ?? null,
      vocabularyNotes: input.vocabularyNotes ?? null,
      grammarNotes: input.grammarNotes ?? null,
      pronunciationNotes: input.pronunciationNotes ?? null,
      strongPoints: input.strongPoints ?? null,
      weaknesses: input.weaknesses ?? null,
      howToImprove: input.howToImprove ?? null,
      completedAt: new Date(),
    };
    await tx.ieltsSpeakingReview.upsert({
      where: { submissionId: submission.id },
      create: { submissionId: submission.id, ...data },
      update: data,
    });
    await tx.ieltsSpeakingSubmission.update({
      where: { id: submission.id }, data: { status: "COMPLETE" },
    });
    await tx.ieltsAttempt.update({
      where: { id: submission.attemptId },
      data: { speakingBand: overall, status: "COMPLETE" },
    });
  });

  revalidatePath("/admin/ielts/speaking");
  revalidatePath("/ielts/feedback");
  return { ok: true };
}

/** Move a submission back to the queue, e.g. after opening it by mistake. */
export async function reopenSubmission(
  kind: "WRITING" | "SPEAKING",
  submissionId: string
): Promise<ReviewResult> {
  const auth = await canReview(kind);
  if (!auth.ok) return { error: "Not permitted." };
  if (kind === "WRITING") {
    await prisma.ieltsWritingSubmission.update({
      where: { id: submissionId }, data: { status: "ASSIGNED" },
    });
  } else {
    await prisma.ieltsSpeakingSubmission.update({
      where: { id: submissionId }, data: { status: "ASSIGNED" },
    });
  }
  revalidatePath(`/admin/ielts/${kind.toLowerCase()}`);
  return { ok: true };
}
