"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { credit } from "@/lib/coins";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

/**
 * Give Coins: any admin can add coins to any account, with a written reason.
 *
 * Every grant is an ADMIN_ADJUSTMENT row in the coin ledger naming the admin
 * who made it, so the student's wallet history shows it and the log on
 * /admin/coins can answer "who gave this, and why" later. Nothing edits a
 * balance directly.
 */

/** The reason must be at least this many words. */
const MIN_REASON_WORDS = 10;
const MAX_GRANT = 10_000;

const countWords = (text: string) => text.trim().split(/\s+/).filter(Boolean).length;

const grantSchema = z.object({
  userId: z.string().min(1, "Choose who receives the coins."),
  amount: z
    .number({ invalid_type_error: "Enter how many coins to give." })
    .int("Coins must be a whole number.")
    .min(1, "Give at least 1 coin.")
    .max(MAX_GRANT, `You can give at most ${MAX_GRANT.toLocaleString()} coins at once.`),
  reason: z
    .string()
    .trim()
    .max(500, "Keep the reason under 500 characters.")
    .refine((r) => countWords(r) >= MIN_REASON_WORDS, `Write a reason of at least ${MIN_REASON_WORDS} words.`),
});

export type GrantResult = { ok: true; balance: number; name: string } | { ok: false; error: string };

export async function grantCoins(input: { userId: string; amount: number; reason: string }): Promise<GrantResult> {
  const admin = await requireAdmin();

  const parsed = grantSchema.safeParse(input);
  if (!parsed.success) return { ok: false, error: parsed.error.issues[0]?.message ?? "Check the form and try again." };
  const { userId, amount, reason } = parsed.data;

  const target = await prisma.user.findUnique({
    where: { id: userId },
    select: { id: true, name: true, username: true, email: true },
  });
  if (!target) return { ok: false, error: "That account no longer exists." };

  try {
    const result = await credit({
      userId,
      amount,
      type: "ADMIN_ADJUSTMENT",
      description: reason,
      actorId: admin.id,
    });
    revalidatePath("/admin/coins");
    revalidatePath("/wallet");
    return {
      ok: true,
      balance: result.balance,
      name: target.name ?? (target.username ? `@${target.username}` : target.email ?? "the account"),
    };
  } catch (error) {
    console.error("[admin] coin grant failed", error);
    return { ok: false, error: "Couldn't add the coins. Nothing was changed." };
  }
}

export interface CoinRecipient {
  id: string;
  name: string | null;
  username: string | null;
  email: string | null;
  role: string;
  coinBalance: number;
}

/** Up to 8 accounts matching a username, email or name, for the picker. */
export async function searchCoinRecipients(query: string): Promise<CoinRecipient[]> {
  await requireAdmin();
  const q = query.trim().replace(/^@/, "");
  if (q.length < 2) return [];
  return prisma.user.findMany({
    where: {
      OR: [
        { username: { contains: q, mode: "insensitive" } },
        { email: { contains: q, mode: "insensitive" } },
        { name: { contains: q, mode: "insensitive" } },
      ],
    },
    orderBy: { createdAt: "desc" },
    take: 8,
    select: { id: true, name: true, username: true, email: true, role: true, coinBalance: true },
  });
}
