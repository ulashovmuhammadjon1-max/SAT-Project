"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { saveAudioRecording } from "@/lib/ielts/audio-storage";

export interface SpeakingResult {
  ok?: boolean;
  error?: string;
  recordingId?: string;
  submissionId?: string;
}

async function attemptFor(userId: string, testId: string) {
  const open = await prisma.ieltsAttempt.findFirst({
    where: { userId, testId, status: { in: ["IN_PROGRESS", "AWAITING_REVIEW"] } },
    orderBy: { createdAt: "desc" },
  });
  if (open) return open;
  return prisma.ieltsAttempt.create({
    data: { userId, testId, mode: "PRACTICE", status: "IN_PROGRESS", skills: ["SPEAKING"] },
  });
}

/**
 * Store one answer.
 *
 * Called once per prompt as the student works through the three parts, so a
 * dropped connection costs the current answer rather than the whole sitting.
 * Re-recording the same prompt replaces the previous take: the student may
 * redo an answer up until they submit, and never afterwards.
 */
export async function saveSpeakingRecording(form: FormData): Promise<SpeakingResult> {
  const user = await requireUser();
  const partId = String(form.get("partId") ?? "");
  const questionIndex = Number(form.get("questionIndex") ?? 0);
  const promptText = String(form.get("promptText") ?? "");
  const durationSeconds = Math.max(0, Math.round(Number(form.get("durationSeconds") ?? 0)));
  const file = form.get("audio");

  if (!(file instanceof File) || file.size === 0) return { error: "No audio was recorded." };
  // A recorded answer is small; anything much larger is not a two-minute take.
  if (file.size > 25 * 1024 * 1024) return { error: "That recording is too large." };

  const part = await prisma.ieltsPart.findUnique({
    where: { id: partId },
    select: { id: true, section: { select: { skill: true, testId: true } } },
  });
  if (!part || part.section.skill !== "SPEAKING") return { error: "Prompt not found." };

  const attempt = await attemptFor(user.id, part.section.testId);
  const submission = await prisma.ieltsSpeakingSubmission.upsert({
    where: { attemptId: attempt.id },
    create: { attemptId: attempt.id, userId: user.id, status: "PENDING" },
    update: {},
    select: { id: true, status: true },
  });
  if (submission.status !== "PENDING") {
    return { error: "This test has already been sent for review." };
  }

  const stored = await saveAudioRecording(file, user.id);

  // Replace rather than accumulate: a re-take should not leave the reviewer
  // with two versions of the same answer and no way to tell which is current.
  await prisma.ieltsSpeakingRecording.deleteMany({
    where: { submissionId: submission.id, partId, questionIndex },
  });
  const row = await prisma.ieltsSpeakingRecording.create({
    data: {
      submissionId: submission.id, partId, questionIndex, promptText,
      audioUrl: stored.path, durationSeconds,
    },
    select: { id: true },
  });

  return { ok: true, recordingId: row.id, submissionId: submission.id };
}

/** Send the whole three-part sitting for review. */
export async function submitSpeaking(testId: string): Promise<SpeakingResult> {
  const user = await requireUser();
  const attempt = await prisma.ieltsAttempt.findFirst({
    where: { userId: user.id, testId, status: { in: ["IN_PROGRESS", "AWAITING_REVIEW"] } },
    orderBy: { createdAt: "desc" },
    select: { id: true },
  });
  if (!attempt) return { error: "Record at least one answer first." };

  const submission = await prisma.ieltsSpeakingSubmission.findUnique({
    where: { attemptId: attempt.id },
    select: { id: true, status: true, _count: { select: { recordings: true } } },
  });
  if (!submission || submission._count.recordings === 0) {
    return { error: "Record at least one answer first." };
  }
  if (submission.status !== "PENDING") {
    return { error: "This test has already been sent for review." };
  }

  await prisma.$transaction([
    prisma.ieltsSpeakingSubmission.update({
      where: { id: submission.id },
      data: { status: "ASSIGNED", submittedAt: new Date() },
    }),
    prisma.ieltsAttempt.update({
      where: { id: attempt.id }, data: { status: "AWAITING_REVIEW" },
    }),
  ]);

  revalidatePath("/ielts/speaking");
  revalidatePath("/ielts/feedback");
  return { ok: true, submissionId: submission.id };
}
