"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { adjust, reconcile } from "@/lib/coins";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import {
  DEFAULT_SETTINGS,
  getSettings,
  invalidateSettingsCache,
  type PlatformSettings,
} from "@/lib/settings";

/**
 * Admin control over the coin economy.
 *
 * Two rules hold throughout:
 *   - Every manual balance change writes a ledger row naming the admin who made
 *     it. There is no code path that edits `coinBalance` directly.
 *   - Settings changes are validated before they are stored, because a
 *     malformed booking cost would otherwise reach the pricing formula.
 */

const adjustSchema = z.object({
  userId: z.string().min(1),
  // Bounded so a slipped keypress cannot mint a fortune.
  amount: z.number().int().refine((n) => n !== 0, "Amount cannot be zero")
    .refine((n) => Math.abs(n) <= 10_000, "Adjustments are limited to 10,000 coins"),
  reason: z.string().trim().min(3, "Please record a reason").max(200),
});

export type AdjustResult = { ok: true; balance: number } | { ok: false; error: string };

export async function adjustUserCoins(input: unknown): Promise<AdjustResult> {
  const admin = await requireAdmin();

  const parsed = adjustSchema.safeParse(input);
  if (!parsed.success) {
    return { ok: false, error: parsed.error.issues[0]?.message ?? "Invalid adjustment." };
  }
  const { userId, amount, reason } = parsed.data;

  const target = await prisma.user.findUnique({
    where: { id: userId },
    select: { id: true, coinBalance: true },
  });
  if (!target) return { ok: false, error: "That student no longer exists." };

  if (amount < 0 && target.coinBalance + amount < 0) {
    return {
      ok: false,
      error: `That would take them below zero — they have ${target.coinBalance} coins.`,
    };
  }

  try {
    const result = await adjust({
      userId,
      amount,
      type: "ADMIN_ADJUSTMENT",
      description: reason,
      actorId: admin.id,
    });
    revalidatePath("/admin/students");
    revalidatePath("/wallet");
    return { ok: true, balance: result.balance };
  } catch (error) {
    console.error("[admin] coin adjustment failed", error);
    return { ok: false, error: "Couldn't apply that adjustment." };
  }
}

/** Ledger for one student, for the admin detail view. */
export async function getUserLedger(userId: string) {
  await requireAdmin();
  const [transactions, check] = await Promise.all([
    prisma.coinTransaction.findMany({
      where: { userId },
      orderBy: { createdAt: "desc" },
      take: 50,
      include: { actor: { select: { name: true, email: true } } },
    }),
    reconcile(userId),
  ]);
  return { transactions, reconciliation: check };
}

const settingsSchema = z.object({
  signupBonusCoins: z.coerce.number().int().min(0).max(1000),
  referralRewardCoins: z.coerce.number().int().min(0).max(1000),
  bookingBaseCost: z.coerce.number().int().min(0).max(1000),
  bookingCostIncrement: z.coerce.number().int().min(0).max(1000),
  eventCost: z.coerce.number().int().min(0).max(1000),
  contactEmail: z
    .string()
    .trim()
    .max(200)
    .refine((v) => v === "" || /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v), "Enter a valid email address")
    .default(""),
  operatorName: z.string().trim().min(1).max(120).default("SATForge"),
  bookingRefundHours: z.coerce.number().int().min(0).max(720).nullable(),
  instagramHandle: z.string().trim().min(1).max(64),
  telegramHandle: z.string().trim().min(1).max(64),
  meetingProvider: z.enum(["manual", "static", "google_meet"]),
  // Empty is valid (no room configured yet); anything else must be a real URL,
  // because a malformed link becomes a dead "Join session" button.
  staticMeetingUrl: z
    .string()
    .trim()
    .max(500)
    .refine((v) => v === "" || /^https?:\/\/\S+$/.test(v), "Enter a full https:// link")
    .default(""),
});

export type SettingsResult = { ok: true } | { ok: false; error: string };

export async function updatePlatformSettings(input: unknown): Promise<SettingsResult> {
  const admin = await requireAdmin();

  const parsed = settingsSchema.safeParse(input);
  if (!parsed.success) {
    return { ok: false, error: parsed.error.issues[0]?.message ?? "Invalid settings." };
  }

  const entries = Object.entries(parsed.data) as [keyof PlatformSettings, unknown][];
  await prisma.$transaction(
    entries.map(([key, value]) =>
      prisma.platformSetting.upsert({
        where: { key },
        create: { key, value: value as never, updatedById: admin.id },
        update: { value: value as never, updatedById: admin.id },
      }),
    ),
  );

  invalidateSettingsCache();
  revalidatePath("/admin/settings");
  revalidatePath("/booking");
  return { ok: true };
}

export async function readPlatformSettings() {
  await requireAdmin();
  return { current: await getSettings(), defaults: DEFAULT_SETTINGS };
}

/** Referral records, newest first, for the admin overview. */
export async function listReferrals(limit = 100) {
  await requireAdmin();
  return prisma.referral.findMany({
    orderBy: { createdAt: "desc" },
    take: limit,
    include: {
      referrer: { select: { id: true, name: true, email: true } },
      referredUser: { select: { id: true, name: true, email: true, createdAt: true } },
    },
  });
}

/**
 * Void a referral and claw the reward back.
 *
 * The clawback is a normal signed adjustment, so it appears in the student's
 * own history rather than the coins quietly vanishing.
 */
export async function voidReferral(referralId: string, reason: string): Promise<AdjustResult> {
  const admin = await requireAdmin();

  const referral = await prisma.referral.findUnique({
    where: { id: referralId },
    select: { id: true, referrerId: true, status: true },
  });
  if (!referral) return { ok: false, error: "Referral not found." };
  if (referral.status === "VOID") return { ok: false, error: "Already voided." };

  const settings = await getSettings();
  const wasPaid = referral.status === "REWARDED";

  await prisma.referral.update({
    where: { id: referralId },
    data: { status: "VOID", voidReason: reason.trim().slice(0, 200) || "Voided by admin" },
  });

  let balance = 0;
  if (wasPaid && settings.referralRewardCoins > 0) {
    const owner = await prisma.user.findUnique({
      where: { id: referral.referrerId },
      select: { coinBalance: true },
    });
    // Never drive a balance negative reversing a reward they have since spent.
    const clawback = Math.min(settings.referralRewardCoins, owner?.coinBalance ?? 0);
    if (clawback > 0) {
      const result = await adjust({
        userId: referral.referrerId,
        amount: -clawback,
        type: "ADMIN_ADJUSTMENT",
        description: "Referral reversed",
        referralId: referral.id,
        actorId: admin.id,
      });
      balance = result.balance;
    }
  }

  revalidatePath("/admin/referrals");
  return { ok: true, balance };
}
