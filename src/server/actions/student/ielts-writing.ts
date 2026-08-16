"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { countWords } from "@/lib/ielts/answers";

export interface WritingResult {
  ok?: boolean;
  error?: string;
  submissionId?: string;
  wordCount?: number;
}

/**
 * The attempt a standalone Writing submission hangs off.
 *
 * `IeltsWritingSubmission.attemptId` is required, so practising a single task
 * outside a full test still needs one. Reusing the student's open attempt on
 * the same paper rather than opening a new one per task is what lets Task 1 and
 * Task 2 of the same paper end up in one place.
 */
async function attemptFor(userId: string, testId: string) {
  const open = await prisma.ieltsAttempt.findFirst({
    where: { userId, testId, status: { in: ["IN_PROGRESS", "AWAITING_REVIEW"] } },
    orderBy: { createdAt: "desc" },
  });
  if (open) return open;
  return prisma.ieltsAttempt.create({
    data: { userId, testId, mode: "PRACTICE", status: "IN_PROGRESS", skills: ["WRITING"] },
  });
}

/**
 * Save without submitting.
 *
 * Called on a timer while the student types. Deliberately tolerant: a draft
 * save must never throw a word-count error and interrupt someone mid-sentence.
 */
export async function saveWritingDraft(
  partId: string,
  text: string
): Promise<WritingResult> {
  const user = await requireUser();
  const part = await prisma.ieltsPart.findUnique({
    where: { id: partId },
    select: { id: true, section: { select: { testId: true, skill: true } } },
  });
  if (!part || part.section.skill !== "WRITING") return { error: "Task not found." };

  const attempt = await attemptFor(user.id, part.section.testId);
  const wordCount = countWords(text);

  const existing = await prisma.ieltsWritingSubmission.findUnique({
    where: { attemptId_partId: { attemptId: attempt.id, partId } },
    select: { id: true, status: true },
  });
  // Once a reviewer has it, the text is frozen. A draft save arriving after
  // submission would otherwise rewrite the essay under the reviewer's cursor.
  if (existing && existing.status !== "PENDING") {
    return { ok: true, submissionId: existing.id, wordCount };
  }

  const row = await prisma.ieltsWritingSubmission.upsert({
    where: { attemptId_partId: { attemptId: attempt.id, partId } },
    create: {
      attemptId: attempt.id, partId, userId: user.id,
      responseText: text, wordCount, status: "PENDING",
    },
    update: { responseText: text, wordCount },
    select: { id: true },
  });
  return { ok: true, submissionId: row.id, wordCount };
}

/**
 * Submit for human review.
 *
 * The word minimum is a warning in IELTS, not a bar — an under-length response
 * is penalised, not refused — so a short answer is accepted and the count is
 * recorded for the reviewer to judge. An empty one is refused, because there is
 * nothing to review.
 */
export async function submitWriting(partId: string, text: string): Promise<WritingResult> {
  const user = await requireUser();
  const trimmed = (text ?? "").trim();
  if (!trimmed) return { error: "Write your response before submitting." };

  const part = await prisma.ieltsPart.findUnique({
    where: { id: partId },
    select: { id: true, section: { select: { testId: true, skill: true } } },
  });
  if (!part || part.section.skill !== "WRITING") return { error: "Task not found." };

  const attempt = await attemptFor(user.id, part.section.testId);
  const wordCount = countWords(trimmed);

  const existing = await prisma.ieltsWritingSubmission.findUnique({
    where: { attemptId_partId: { attemptId: attempt.id, partId } },
    select: { id: true, status: true },
  });
  if (existing && existing.status !== "PENDING") {
    return { error: "This response has already been sent for review." };
  }

  const row = await prisma.ieltsWritingSubmission.upsert({
    where: { attemptId_partId: { attemptId: attempt.id, partId } },
    create: {
      attemptId: attempt.id, partId, userId: user.id,
      responseText: trimmed, wordCount, status: "ASSIGNED", submittedAt: new Date(),
    },
    update: {
      responseText: trimmed, wordCount, status: "ASSIGNED", submittedAt: new Date(),
    },
    select: { id: true },
  });

  await prisma.ieltsAttempt.update({
    where: { id: attempt.id },
    data: { status: "AWAITING_REVIEW" },
  });

  revalidatePath("/ielts/writing");
  revalidatePath("/ielts/feedback");
  return { ok: true, submissionId: row.id, wordCount };
}
