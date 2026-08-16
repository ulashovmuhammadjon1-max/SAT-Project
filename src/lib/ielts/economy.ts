import { prisma } from "@/lib/prisma";

/**
 * What a free human review costs.
 *
 * The first review is free — a student has to see what the feedback is worth
 * before being asked to bring anyone. Every review after that is paid for with
 * two friends who signed up and stuck around long enough for their referral to
 * qualify.
 *
 * ## Why this is computed and not stored
 *
 * There is no ledger table and no new column. The entitlement is derived from
 * rows that already exist — qualified referrals in, submitted reviews out — so
 * the balance cannot drift from reality, cannot be double-spent by two
 * concurrent submissions reading a stale counter, and needs no migration to
 * ship. (Adding a column to a model before its migration reaches production is
 * how this app went down twice; see CLAUDE.md.) The cost is one aggregate query
 * per check, which is nothing next to the work a review represents.
 *
 * ## One pool, both skills
 *
 * A Writing paper and a Speaking interview each consume one review. The user's
 * rule was "the first review costs nothing", not "the first of each kind", and
 * two separate allowances would let a student take two free reviews.
 *
 * ## One paper, one review — not one essay, one review
 *
 * The unit is the sitting (`IeltsAttempt`), not the submission. A full
 * practice is two essays and one paper band, so charging it two reviews would
 * put the thing this product is best at out of reach of a student's free one.
 * The same rule then means Task 1 and Task 2 of the same paper cost one review
 * whether they are written in a single sitting or a week apart, which is the
 * only version of the rule that does not punish someone for stopping halfway.
 */

/** Friends who must qualify to buy one review, after the free one. */
export const FRIENDS_PER_REVIEW = 2;

/** Reviews granted before any invitation is needed. */
export const FREE_REVIEWS = 1;

export interface ReviewAllowance {
  /** Reviews earned in total, free one included. */
  allowance: number;
  /** Reviews already sent for review. */
  used: number;
  /** How many more can be sent right now. */
  remaining: number;
  /** Qualified referrals to date. */
  qualifiedFriends: number;
  /** Referrals counted toward the next review, 0..FRIENDS_PER_REVIEW-1. */
  towardNext: number;
  /** Friends still needed to unlock one more review. */
  friendsNeeded: number;
  /** True while the student still has their free review in hand. */
  onFreeReview: boolean;
}

export async function getReviewAllowance(userId: string): Promise<ReviewAllowance> {
  const [qualifiedFriends, writingSittings, speakingUsed] = await Promise.all([
    prisma.referral.count({ where: { referrerId: userId, status: "REWARDED" } }),
    // Distinct sittings, so a full practice's two essays cost one review.
    // A submission counts the moment it leaves the student's hands: counting
    // only completed reviews would let one student queue twenty papers against
    // a single entitlement while the first is still being marked.
    prisma.ieltsWritingSubmission.findMany({
      where: { userId, status: { not: "PENDING" } },
      select: { attemptId: true },
      distinct: ["attemptId"],
    }),
    // `IeltsSpeakingSubmission.attemptId` is unique, so one row is one sitting.
    prisma.ieltsSpeakingSubmission.count({
      where: { userId, status: { not: "PENDING" } },
    }),
  ]);

  const used = writingSittings.length + speakingUsed;
  const earned = Math.floor(qualifiedFriends / FRIENDS_PER_REVIEW);
  const allowance = FREE_REVIEWS + earned;
  const remaining = Math.max(0, allowance - used);
  const towardNext = qualifiedFriends % FRIENDS_PER_REVIEW;

  return {
    allowance,
    used,
    remaining,
    qualifiedFriends,
    towardNext,
    friendsNeeded: FRIENDS_PER_REVIEW - towardNext,
    onFreeReview: used < FREE_REVIEWS,
  };
}

/**
 * May this student send work from this particular sitting?
 *
 * A sitting already paid for is free to add to — submitting Task 2 after Task 1
 * of the same paper must not be refused, and must not be charged twice.
 */
export async function canSubmitForAttempt(
  userId: string,
  attemptId: string
): Promise<{ ok: true } | { ok: false; allowance: ReviewAllowance }> {
  const alreadyPaid = await prisma.ieltsWritingSubmission.findFirst({
    where: { userId, attemptId, status: { not: "PENDING" } },
    select: { id: true },
  });
  if (alreadyPaid) return { ok: true };

  const allowance = await getReviewAllowance(userId);
  return allowance.remaining > 0 ? { ok: true } : { ok: false, allowance };
}

/**
 * The message a student sees when they are out of reviews.
 *
 * Written to say what to do next, not just what went wrong — "you have used
 * your reviews" leaves someone staring at an essay they cannot send.
 */
export function outOfReviewsMessage(a: ReviewAllowance): string {
  return (
    `You have used all ${a.allowance} of your reviews. ` +
    `Invite ${a.friendsNeeded} more ${a.friendsNeeded === 1 ? "friend" : "friends"} ` +
    "to unlock the next one — your draft is saved and will be waiting."
  );
}
