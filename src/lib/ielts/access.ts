/**
 * Who may see what in the IELTS section.
 *
 * Every one of these is a server-side check. The rule that matters most is the
 * one about reviewers: a reviewer is not a small admin. They may open exactly
 * the submissions assigned to them and nothing else — not another reviewer's
 * queue, not a student's other attempts, and nothing in the SAT admin surface.
 *
 * Students must never reach an answer key, a Listening transcript, a
 * reviewer's private notes, or anyone else's submission. Those are enforced by
 * the loaders in this directory selecting the safe columns explicitly rather
 * than by trusting a component not to render a field it was handed.
 */

import { redirect } from "next/navigation";

import { prisma } from "@/lib/prisma";
import { requireVerifiedUser } from "@/lib/session";

export interface ReviewerCapabilities {
  userId: string;
  canReviewWriting: boolean;
  canReviewSpeaking: boolean;
  writingBand: number | null;
  speakingBand: number | null;
}

/**
 * An approved reviewer, or null.
 *
 * `approved` is set by an admin. Nobody self-certifies: holding the REVIEWER
 * role is not enough on its own, because the role can be granted before the
 * credential is checked.
 */
export async function getReviewerCapabilities(
  userId: string
): Promise<ReviewerCapabilities | null> {
  const profile = await prisma.ieltsReviewerProfile.findUnique({
    where: { userId },
    select: {
      userId: true, approved: true,
      canReviewWriting: true, canReviewSpeaking: true,
      writingBand: true, speakingBand: true,
    },
  });
  if (!profile || !profile.approved) return null;
  return {
    userId: profile.userId,
    canReviewWriting: profile.canReviewWriting,
    canReviewSpeaking: profile.canReviewSpeaking,
    writingBand: profile.writingBand,
    speakingBand: profile.speakingBand,
  };
}

/** Gate a reviewer route. Admins pass, so support can see the queue. */
export async function requireReviewer(): Promise<{
  userId: string;
  isAdmin: boolean;
  caps: ReviewerCapabilities | null;
}> {
  const user = await requireVerifiedUser();
  const isAdmin = user.role === "ADMIN";
  const caps = await getReviewerCapabilities(user.id);
  if (!isAdmin && !caps) redirect("/dashboard");
  return { userId: user.id, isAdmin, caps };
}

/**
 * The attempt, only if it belongs to this student.
 *
 * Returns null rather than throwing so a caller can 404 instead of leaking
 * that the id exists at all.
 */
export async function ownedAttempt(attemptId: string, userId: string) {
  return prisma.ieltsAttempt.findFirst({
    where: { id: attemptId, userId },
  });
}

/** May this user open this Writing submission? */
export async function canOpenWritingSubmission(
  submissionId: string,
  userId: string,
  isAdmin: boolean
): Promise<boolean> {
  if (isAdmin) return true;
  const sub = await prisma.ieltsWritingSubmission.findUnique({
    where: { id: submissionId },
    select: { userId: true, review: { select: { reviewerId: true } } },
  });
  if (!sub) return false;
  // The student who wrote it, or the reviewer it is assigned to. An approved
  // reviewer with no assignment on this row gets nothing.
  return sub.userId === userId || sub.review?.reviewerId === userId;
}

/** May this user open this Speaking submission? */
export async function canOpenSpeakingSubmission(
  submissionId: string,
  userId: string,
  isAdmin: boolean
): Promise<boolean> {
  if (isAdmin) return true;
  const sub = await prisma.ieltsSpeakingSubmission.findUnique({
    where: { id: submissionId },
    select: { userId: true, review: { select: { reviewerId: true } } },
  });
  if (!sub) return false;
  return sub.userId === userId || sub.review?.reviewerId === userId;
}

/**
 * Fields a student may never receive.
 *
 * Used as the explicit `select` on student-facing question loads. Listing what
 * IS sent, rather than deleting fields afterwards, is the difference between a
 * leak being impossible and a leak being one forgotten line away — the audit
 * that found a transcript in a payload found it in a whole-row fetch.
 */
export const STUDENT_SAFE_QUESTION_SELECT = {
  id: true,
  number: true,
  type: true,
  promptHtml: true,
  optionsJson: true,
  groupId: true,
  partId: true,
} as const;

export const STUDENT_SAFE_PART_SELECT = {
  id: true,
  partNumber: true,
  title: true,
  instructions: true,
  passageHtml: true,
  promptHtml: true,
  imageUrl: true,
  imageAlt: true,
  audioDuration: true,
  prepSeconds: true,
  speakSeconds: true,
  minWords: true,
  // audioUrl and transcript are deliberately absent. Audio is fetched through
  // a signed route that checks the attempt's play state; the transcript is
  // never sent to a student at all.
} as const;
