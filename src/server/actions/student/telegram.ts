"use server";

import { revalidatePath } from "next/cache";
import { Prisma } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import {
  checkChannelMembership,
  telegramConfigured,
  verifyLoginPayload,
  type TelegramLoginPayload,
} from "@/lib/telegram";

export interface TelegramLinkResult {
  ok: boolean;
  error?: string;
  isMember?: boolean;
  username?: string | null;
}

/**
 * Link a Telegram account and check channel membership in one step.
 *
 * The payload comes from Telegram's Login Widget and is signed with the bot
 * token, so it is verified server-side before anything is stored — the client
 * could otherwise post any id it liked and claim that person's membership.
 */
export async function linkTelegram(payload: TelegramLoginPayload): Promise<TelegramLinkResult> {
  const user = await requireUser();
  if (!telegramConfigured()) return { ok: false, error: "Telegram verification is not configured." };

  const verified = verifyLoginPayload(payload);
  if (!verified.ok) return { ok: false, error: verified.error };

  const membership = await checkChannelMembership(payload.id);
  if (membership.status === "unknown") {
    // Do not store a negative we are not sure about, and do not blame the
    // student for an outage on our side.
    console.error("[telegram] membership check failed", membership.error);
    return { ok: false, error: "Telegram didn't answer just now. Try again in a moment." };
  }

  try {
    await prisma.user.update({
      where: { id: user.id },
      data: {
        telegramUserId: payload.id,
        telegramUsername: payload.username ?? null,
        telegramLinkedAt: new Date(),
        telegramIsMember: membership.status === "member",
        telegramCheckedAt: new Date(),
      },
    });
  } catch (error) {
    // The unique index on telegramUserId is the guard that stops one Telegram
    // account vouching for several site accounts.
    if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === "P2002") {
      return { ok: false, error: "That Telegram account is already linked to another Scholarly account." };
    }
    throw error;
  }

  revalidatePath("/booking");
  return { ok: true, isMember: membership.status === "member", username: payload.username ?? null };
}

/**
 * Re-run the membership check for the signed-in student.
 *
 * The student joins the channel in a different app, so nothing tells us when it
 * happens — they come back and press the button.
 */
export async function recheckMyTelegram(): Promise<TelegramLinkResult> {
  const user = await requireUser();
  const row = await prisma.user.findUnique({
    where: { id: user.id },
    select: { telegramUserId: true },
  });
  if (!row?.telegramUserId) return { ok: false, error: "Connect your Telegram account first." };

  const membership = await checkChannelMembership(row.telegramUserId);
  if (membership.status === "unknown") {
    return { ok: false, error: "Telegram didn't answer just now. Try again in a moment." };
  }

  await prisma.user.update({
    where: { id: user.id },
    data: { telegramIsMember: membership.status === "member", telegramCheckedAt: new Date() },
  });

  revalidatePath("/booking");
  return { ok: true, isMember: membership.status === "member" };
}
