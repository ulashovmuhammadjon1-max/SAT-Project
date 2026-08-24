import { Prisma } from "@prisma/client";
import { customAlphabet } from "nanoid";

import { credit } from "@/lib/coins";
import { prisma } from "@/lib/prisma";
import { getSettings } from "@/lib/settings";

/**
 * Referrals.
 *
 * A referral pays out only when the invited person actually creates an account,
 * and pays out exactly once. Three independent mechanisms enforce that, because
 * any one of them alone has a hole:
 *
 *   - `Referral.referredUserId` is unique, so one account can only ever be
 *     counted as one referral no matter how many codes it is replayed against.
 *   - The reward `credit` carries `idempotencyKey = referral:<id>`, so even a
 *     retried or concurrent qualification pays once.
 *   - `attributeReferral` rejects self-referral and any account that already
 *     has a referrer.
 *
 * Codes are unambiguous by construction: no O/0, no I/1/l. Students read these
 * off a screenshot in a Telegram group.
 */

const ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
const CODE_LENGTH = 7;
const makeCode = customAlphabet(ALPHABET, CODE_LENGTH);

/** Normalise anything a student might paste or type into a comparable code. */
export function normalizeCode(raw: string | null | undefined): string | null {
  if (!raw) return null;
  const cleaned = raw.trim().toUpperCase().replace(/[^A-Z0-9]/g, "");
  if (cleaned.length < 4 || cleaned.length > 16) return null;
  return cleaned;
}

/**
 * Get this user's referral code, creating one on first use.
 *
 * Assigned lazily rather than at signup so accounts created before the referral
 * system existed get a code the first time they open the invite page, with no
 * backfill migration.
 */
export async function ensureReferralCode(userId: string): Promise<string> {
  const user = await prisma.user.findUnique({
    where: { id: userId },
    select: { referralCode: true },
  });
  if (user?.referralCode) return user.referralCode;

  // Retry on the vanishingly unlikely collision rather than assuming.
  for (let attempt = 0; attempt < 5; attempt++) {
    const code = makeCode();
    try {
      const updated = await prisma.user.update({
        where: { id: userId },
        data: { referralCode: code },
        select: { referralCode: true },
      });
      return updated.referralCode!;
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === "P2002") {
        continue;
      }
      throw error;
    }
  }
  throw new Error("Could not allocate a referral code");
}

export type AttributionOutcome =
  | "attributed"
  | "no_code"
  | "unknown_code"
  | "self_referral"
  | "already_referred";

/**
 * Record that `newUserId` signed up through `rawCode`.
 *
 * Called from account creation, inside that transaction, so a failed signup
 * leaves no referral behind. Never throws for a bad code — an invalid or
 * abusive code must not stop a legitimate person from creating an account, so
 * every rejection is a return value the caller can log and move past.
 */
export async function attributeReferral(
  newUserId: string,
  rawCode: string | null | undefined,
  db: Prisma.TransactionClient | typeof prisma = prisma,
): Promise<{ outcome: AttributionOutcome; referralId?: string }> {
  const code = normalizeCode(rawCode);
  if (!code) return { outcome: "no_code" };

  const referrer = await db.user.findUnique({
    where: { referralCode: code },
    select: { id: true },
  });
  if (!referrer) return { outcome: "unknown_code" };
  if (referrer.id === newUserId) return { outcome: "self_referral" };

  const already = await db.referral.findUnique({
    where: { referredUserId: newUserId },
    select: { id: true },
  });
  if (already) return { outcome: "already_referred" };

  try {
    const referral = await db.referral.create({
      data: {
        referrerId: referrer.id,
        referredUserId: newUserId,
        code,
        status: "PENDING",
      },
      select: { id: true },
    });
    await db.user.update({
      where: { id: newUserId },
      data: { referredById: referrer.id },
    });
    return { outcome: "attributed", referralId: referral.id };
  } catch (error) {
    if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === "P2002") {
      return { outcome: "already_referred" };
    }
    throw error;
  }
}

/**
 * Pay a pending referral.
 *
 * Separate from attribution so the qualifying bar can be raised later — right
 * now creating a real account qualifies, but this is the single place that
 * would change if it should instead require, say, finishing onboarding or
 * answering some questions.
 *
 * The status flip is a conditional write (`updateMany` on `status: PENDING`),
 * so two concurrent calls cannot both proceed to pay.
 */
export async function qualifyReferral(referralId: string): Promise<{ paid: boolean; reason?: string }> {
  const settings = await getSettings();

  const referral = await prisma.referral.findUnique({
    where: { id: referralId },
    select: { id: true, referrerId: true, referredUserId: true, status: true },
  });
  if (!referral) return { paid: false, reason: "not_found" };
  if (referral.status !== "PENDING") return { paid: false, reason: referral.status.toLowerCase() };
  if (referral.referrerId === referral.referredUserId) {
    await prisma.referral.update({
      where: { id: referralId },
      data: { status: "VOID", voidReason: "Self-referral" },
    });
    return { paid: false, reason: "self_referral" };
  }

  const claimed = await prisma.referral.updateMany({
    where: { id: referralId, status: "PENDING" },
    data: { status: "REWARDED", rewardedAt: new Date() },
  });
  if (claimed.count === 0) return { paid: false, reason: "already_claimed" };

  try {
    await credit({
      userId: referral.referrerId,
      amount: settings.referralRewardCoins,
      type: "REFERRAL_REWARD",
      description: "Friend joined Scholarly",
      referralId: referral.id,
      idempotencyKey: `referral:${referral.id}`,
    });
    return { paid: true };
  } catch (error) {
    // Put the referral back so it can be retried, rather than leaving it marked
    // rewarded with no coins behind it.
    await prisma.referral.updateMany({
      where: { id: referralId, status: "REWARDED" },
      data: { status: "PENDING", rewardedAt: null },
    });
    console.error("[referrals] reward failed, reverted to PENDING", error);
    return { paid: false, reason: "credit_failed" };
  }
}

export interface ReferralSummary {
  code: string;
  link: string;
  invited: number;
  rewarded: number;
  pending: number;
  coinsEarned: number;
  recent: {
    id: string;
    name: string;
    joinedAt: Date;
    status: "PENDING" | "REWARDED" | "VOID";
  }[];
}

/** Everything the invite page renders, in one round trip. */
export async function getReferralSummary(userId: string, origin: string): Promise<ReferralSummary> {
  const code = await ensureReferralCode(userId);

  const [rows, earned] = await Promise.all([
    prisma.referral.findMany({
      where: { referrerId: userId },
      orderBy: { createdAt: "desc" },
      take: 25,
      select: {
        id: true,
        status: true,
        createdAt: true,
        referredUser: { select: { name: true, email: true } },
      },
    }),
    prisma.coinTransaction.aggregate({
      where: { userId, type: "REFERRAL_REWARD" },
      _sum: { amount: true },
    }),
  ]);

  const counts = { REWARDED: 0, PENDING: 0, VOID: 0 } as Record<string, number>;
  for (const r of rows) counts[r.status] = (counts[r.status] ?? 0) + 1;

  return {
    code,
    link: `${origin.replace(/\/$/, "")}/onboarding?ref=${code}`,
    invited: rows.filter((r) => r.status !== "VOID").length,
    rewarded: counts.REWARDED ?? 0,
    pending: counts.PENDING ?? 0,
    coinsEarned: earned._sum.amount ?? 0,
    recent: rows.map((r) => ({
      id: r.id,
      // First name only — the referrer does not need a full identity, and the
      // email address is deliberately never exposed here.
      name: displayName(r.referredUser.name, r.referredUser.email),
      joinedAt: r.createdAt,
      status: r.status,
    })),
  };
}

function displayName(name: string | null, email: string): string {
  const first = name?.trim().split(/\s+/)[0];
  if (first) return first;
  const local = email.split("@")[0] ?? "Student";
  return local.slice(0, 2) + "•".repeat(Math.max(2, Math.min(6, local.length - 2)));
}
