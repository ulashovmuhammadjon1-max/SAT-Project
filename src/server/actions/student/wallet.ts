"use server";

import { headers } from "next/headers";
import { revalidatePath } from "next/cache";

import { getBalance } from "@/lib/coins";
import { prisma } from "@/lib/prisma";
import { getReferralSummary } from "@/lib/referrals";
import { requireUser } from "@/lib/session";
import { getSettings } from "@/lib/settings";

export interface WalletTransaction {
  id: string;
  amount: number;
  type: string;
  description: string;
  balanceAfter: number;
  createdAt: Date;
}

export interface WalletPage {
  balance: number;
  transactions: WalletTransaction[];
  hasMore: boolean;
  totalEarned: number;
  totalSpent: number;
}

const PAGE_SIZE = 25;

/**
 * Wallet contents.
 *
 * Paginated from the start: a long-standing student accumulates a row per
 * reward and per booking, and the transaction list is exactly the kind of table
 * that is fine at ten rows and a problem at ten thousand.
 */
export async function getWallet(cursor?: string): Promise<WalletPage> {
  const user = await requireUser();

  const [balance, rows, earned, spent] = await Promise.all([
    getBalance(user.id),
    prisma.coinTransaction.findMany({
      where: { userId: user.id },
      orderBy: { createdAt: "desc" },
      // One extra row tells us whether another page exists without a count().
      take: PAGE_SIZE + 1,
      ...(cursor ? { cursor: { id: cursor }, skip: 1 } : {}),
      select: {
        id: true,
        amount: true,
        type: true,
        description: true,
        balanceAfter: true,
        createdAt: true,
      },
    }),
    prisma.coinTransaction.aggregate({
      where: { userId: user.id, amount: { gt: 0 } },
      _sum: { amount: true },
    }),
    prisma.coinTransaction.aggregate({
      where: { userId: user.id, amount: { lt: 0 } },
      _sum: { amount: true },
    }),
  ]);

  const hasMore = rows.length > PAGE_SIZE;
  return {
    balance,
    transactions: rows.slice(0, PAGE_SIZE),
    hasMore,
    totalEarned: earned._sum.amount ?? 0,
    totalSpent: Math.abs(spent._sum.amount ?? 0),
  };
}

/** Referral summary for the invite page, with an absolute share link. */
export async function getMyReferrals() {
  const user = await requireUser();

  // Build the link from the request host so it is correct in local dev,
  // preview deploys and production without a hard-coded domain.
  const h = headers();
  const host = h.get("x-forwarded-host") ?? h.get("host") ?? "satforge.org";
  const proto = h.get("x-forwarded-proto") ?? (host.startsWith("localhost") ? "http" : "https");

  const [summary, settings] = await Promise.all([
    getReferralSummary(user.id, `${proto}://${host}`),
    getSettings(),
  ]);

  return { ...summary, rewardPerReferral: settings.referralRewardCoins };
}

/** Force a plan rebuild from the student's current performance. */
export async function rebuildPlan() {
  const user = await requireUser();
  const { getOrCreatePlan } = await import("@/lib/plan/service");
  await getOrCreatePlan(user.id, { force: true });
  revalidatePath("/plan");
  revalidatePath("/dashboard");
  return { ok: true as const };
}
