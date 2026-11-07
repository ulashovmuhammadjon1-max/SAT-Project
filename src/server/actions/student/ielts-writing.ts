"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { canSubmitForAttempt, outOfReviewsMessage } from "@/lib/ielts/economy";
import { countWords } from "@/lib/ielts/answers";
import { responseImageSrc, savePromptImage } from "@/lib/ielts/image-storage";

export interface WritingResult {
  ok?: boolean;
  error?: string;
  submissionId?: string;
  wordCount?: number;
  /** Where the attached Task 1 image can be fetched from, if there is one. */
  imageSrc?: string | null;
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

  const part = await prisma.ieltsPart.findUnique({
    where: { id: partId },
    select: { id: true, section: { select: { testId: true, skill: true } } },
  });
  if (!part || part.section.skill !== "WRITING") return { error: "Task not found." };

  const attempt = await attemptFor(user.id, part.section.testId);
  const wordCount = countWords(trimmed);

  const existing = await prisma.ieltsWritingSubmission.findUnique({
    where: { attemptId_partId: { attemptId: attempt.id, partId } },
    select: { id: true, status: true, responseImage: true },
  });
  if (existing && existing.status !== "PENDING") {
    return { error: "This response has already been sent for review." };
  }
  // An attached image is a response in its own right — a photo of an answer
  // written by hand — so text is required only when there is no image.
  if (!trimmed && !existing?.responseImage) {
    return { error: "Write your response, or attach an image of it, before submitting." };
  }

  // Checked here rather than in the editor: the button is hidden when the
  // allowance is spent, but a hidden button is a hint, not a rule. Adding a
  // second task to a sitting already paid for is free — see `economy.ts`.
  const gate = await canSubmitForAttempt(user.id, attempt.id);
  if (!gate.ok) return { error: outOfReviewsMessage(gate.allowance) };

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

/**
 * The part a Task 1 image may be attached to, or an error.
 *
 * Task 1 only: the figure-description task is the one students most often
 * draft on paper or want to annotate. Task 2 is an essay, and an image there
 * would only be a way round the word count.
 */
async function task1Part(partId: string) {
  const part = await prisma.ieltsPart.findUnique({
    where: { id: partId },
    select: { id: true, partNumber: true, section: { select: { testId: true, skill: true } } },
  });
  if (!part || part.section.skill !== "WRITING") return { error: "Task not found." } as const;
  if (part.partNumber !== 1) return { error: "Images can only be attached to Task 1." } as const;
  return { part } as const;
}

/**
 * Attach (or replace) the image on a Task 1 response.
 *
 * Uploaded as soon as it is chosen, onto the draft row, rather than with the
 * final submit: the draft already survives a closed tab, and the image should
 * too. Refused once the response has gone for review, for the same reason the
 * text freezes then.
 */
export async function attachWritingImage(form: FormData): Promise<WritingResult> {
  const user = await requireUser();
  const partId = String(form.get("partId") ?? "");
  const image = form.get("image");
  if (!(image instanceof File) || image.size === 0) return { error: "Choose an image to attach." };

  const found = await task1Part(partId);
  if ("error" in found) return { error: found.error };

  const attempt = await attemptFor(user.id, found.part.section.testId);
  const existing = await prisma.ieltsWritingSubmission.findUnique({
    where: { attemptId_partId: { attemptId: attempt.id, partId } },
    select: { id: true, status: true },
  });
  if (existing && existing.status !== "PENDING") {
    return { error: "This response has already been sent for review." };
  }

  let stored: string;
  try {
    stored = await savePromptImage(image, user.id);
  } catch (error) {
    return { error: error instanceof Error ? error.message : "That image could not be saved." };
  }

  const row = await prisma.ieltsWritingSubmission.upsert({
    where: { attemptId_partId: { attemptId: attempt.id, partId } },
    create: {
      attemptId: attempt.id, partId, userId: user.id,
      responseText: "", wordCount: 0, status: "PENDING", responseImage: stored,
    },
    update: { responseImage: stored },
    select: { id: true },
  });
  return { ok: true, submissionId: row.id, imageSrc: `${responseImageSrc(row.id)}?v=${Date.now()}` };
}

/** Take the image off a Task 1 response that has not been sent yet. */
export async function removeWritingImage(partId: string): Promise<WritingResult> {
  const user = await requireUser();
  const found = await task1Part(partId);
  if ("error" in found) return { error: found.error };

  const attempt = await attemptFor(user.id, found.part.section.testId);
  const existing = await prisma.ieltsWritingSubmission.findUnique({
    where: { attemptId_partId: { attemptId: attempt.id, partId } },
    select: { id: true, status: true },
  });
  if (!existing) return { ok: true, imageSrc: null };
  if (existing.status !== "PENDING") return { error: "This response has already been sent for review." };

  await prisma.ieltsWritingSubmission.update({
    where: { id: existing.id },
    data: { responseImage: null },
    select: { id: true },
  });
  return { ok: true, imageSrc: null };
}
