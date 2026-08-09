"use server";

import { createHash, randomBytes } from "crypto";
import { headers } from "next/headers";
import { z } from "zod";

import { button, layout, para, sendEmail } from "@/lib/email";
import { prisma } from "@/lib/prisma";
import { qualifyReferral } from "@/lib/referrals";
import { getCurrentUser } from "@/lib/session";

/**
 * Email verification.
 *
 * Built on the same `VerificationToken` table and the same three rules as the
 * password reset: tokens are stored hashed, the response never reveals whether
 * an address has an account, and a token is single-use and short-lived.
 *
 * What it is actually for is stopping throwaway signups. The lever that makes
 * that work is not the gate on its own — it is that **the referral reward is
 * paid at verification, not at signup**. Inventing accounts to farm invite
 * coins now requires a working inbox per account, which is the whole point.
 */

/** A day. Long enough to survive a phone left at home, short enough to expire. */
const TOKEN_TTL_MS = 24 * 60 * 60 * 1000;
const PREFIX = "verify:";

/** Minimum gap between sends to one address, so the button can't be a mail cannon. */
const RESEND_COOLDOWN_MS = 60 * 1000;

const hash = (token: string) => createHash("sha256").update(token).digest("hex");

function origin(): string {
  const h = headers();
  const host = h.get("x-forwarded-host") ?? h.get("host") ?? "satforge.org";
  const proto = h.get("x-forwarded-proto") ?? (host.startsWith("localhost") ? "http" : "https");
  return `${proto}://${host}`;
}

/**
 * Issues a token and emails the link.
 *
 * Returns `false` only when the cooldown blocked it — a delivery failure is
 * reported as sent, because the token is real either way and the message is in
 * the server log for an admin to recover.
 */
export async function sendVerificationEmail(input: {
  email: string;
  name?: string | null;
}): Promise<boolean> {
  const email = input.email.trim().toLowerCase();
  const identifier = `${PREFIX}${email}`;

  const existing = await prisma.verificationToken.findFirst({ where: { identifier } });
  if (existing) {
    // `expires` is the only timestamp the table has, so the issue time is
    // derived from it rather than stored twice.
    const issuedAt = existing.expires.getTime() - TOKEN_TTL_MS;
    if (Date.now() - issuedAt < RESEND_COOLDOWN_MS) return false;
  }

  const token = randomBytes(32).toString("hex");

  // One live token per address: a new link invalidates the previous one.
  await prisma.verificationToken.deleteMany({ where: { identifier } });
  await prisma.verificationToken.create({
    data: { identifier, token: hash(token), expires: new Date(Date.now() + TOKEN_TTL_MS) },
  });

  const link = `${origin()}/verify-email?token=${token}&email=${encodeURIComponent(email)}`;
  const firstName = input.name?.trim().split(/\s+/)[0] ?? "there";

  await sendEmail({
    to: email,
    subject: "Confirm your email for SATForge",
    text:
      `Hi ${firstName},\n\n` +
      `Confirm this address to finish setting up your SATForge account. ` +
      `The link works once and expires in 24 hours.\n\n${link}\n\n` +
      `If you didn't sign up for SATForge, you can ignore this email.`,
    html: layout(
      para(`Hi ${firstName},`) +
        para(
          "Confirm this address to finish setting up your SATForge account. The link works once and expires in 24 hours.",
        ) +
        button(link, "Confirm my email") +
        para(
          `<span style="color:#8a97b1;font-size:13px;">If you didn't sign up for SATForge, ignore this email — no account will be used.</span>`,
        ),
    ),
  });

  return true;
}

export type VerifyResult =
  | { ok: true; alreadyVerified: boolean }
  | { ok: false; error: string };

const verifySchema = z.object({
  email: z.string().trim().toLowerCase().email(),
  token: z.string().min(32),
});

/**
 * Consumes a token and marks the address verified.
 *
 * An account that is already verified reports success: clicking the link twice,
 * or a mail client prefetching it, must not read as a failure.
 */
export async function verifyEmail(input: unknown): Promise<VerifyResult> {
  const parsed = verifySchema.safeParse(input);
  if (!parsed.success) return { ok: false, error: "That confirmation link is not valid." };
  const { email, token } = parsed.data;
  const identifier = `${PREFIX}${email}`;

  const user = await prisma.user.findUnique({
    where: { email },
    select: { id: true, emailVerified: true },
  });
  if (user?.emailVerified) {
    await prisma.verificationToken.deleteMany({ where: { identifier } });
    return { ok: true, alreadyVerified: true };
  }

  const record = await prisma.verificationToken.findUnique({
    where: { identifier_token: { identifier, token: hash(token) } },
  });
  // One message for wrong, used and expired alike — a precise one would let
  // someone probe which links had existed.
  const invalid = {
    ok: false as const,
    error: "That confirmation link is invalid or has expired. Send yourself a new one below.",
  };
  if (!record) return invalid;
  if (record.expires < new Date()) {
    await prisma.verificationToken.deleteMany({ where: { identifier } });
    return invalid;
  }
  if (!user) return invalid;

  await prisma.$transaction([
    prisma.user.update({ where: { id: user.id }, data: { emailVerified: new Date() } }),
    prisma.verificationToken.deleteMany({ where: { identifier } }),
  ]);

  // The referral pays out here rather than at signup. `qualifyReferral` is
  // idempotent, so a replayed verification cannot pay twice.
  try {
    const referral = await prisma.referral.findUnique({
      where: { referredUserId: user.id },
      select: { id: true },
    });
    if (referral) await qualifyReferral(referral.id);
  } catch (error) {
    // The account is verified either way; a reward that failed to write is a
    // support question, not a reason to reject a valid link.
    console.error("[verify-email] referral payout failed", error);
  }

  return { ok: true, alreadyVerified: false };
}

export type ResendResult = { ok: true } | { ok: false; error: string };

/** "Send it again", from the waiting screen. Session-scoped, so it can only ever
 *  target the signed-in account's own address. */
export async function resendVerificationEmail(): Promise<ResendResult> {
  const sessionUser = await getCurrentUser();
  if (!sessionUser?.email) return { ok: false, error: "Please sign in first." };

  const user = await prisma.user.findUnique({
    where: { email: sessionUser.email },
    select: { name: true, email: true, emailVerified: true },
  });
  if (!user) return { ok: false, error: "Please sign in first." };
  if (user.emailVerified) return { ok: true };

  const sent = await sendVerificationEmail({ email: user.email!, name: user.name });
  if (!sent) {
    return { ok: false, error: "We just sent one — give it a minute before trying again." };
  }
  return { ok: true };
}
