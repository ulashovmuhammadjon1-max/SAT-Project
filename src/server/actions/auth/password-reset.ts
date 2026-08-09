"use server";

import { createHash, randomBytes } from "crypto";
import { headers } from "next/headers";
import bcrypt from "bcryptjs";
import { z } from "zod";

import { button, layout, para, sendEmail } from "@/lib/email";
import { prisma } from "@/lib/prisma";

/**
 * Password reset.
 *
 * Reuses the `VerificationToken` table Auth.js already defines rather than
 * adding a model — the shape (identifier, token, expires) is exactly right,
 * and the identifier is namespaced so reset tokens can never be confused with
 * anything else stored there.
 *
 * Three security properties, none of which are optional:
 *
 *  1. **Tokens are stored hashed.** A database read must not yield a working
 *     reset link for every account. The raw token exists only in the email.
 *  2. **Requesting a reset never reveals whether an account exists.** The
 *     response is identical either way, otherwise this becomes an endpoint for
 *     enumerating which emails have signed up.
 *  3. **Tokens are single-use and short-lived.** Consumed inside the same
 *     transaction that changes the password, so a leaked link cannot be
 *     replayed.
 */

const TOKEN_TTL_MS = 60 * 60 * 1000; // 1 hour
const PREFIX = "pwreset:";

const hash = (token: string) => createHash("sha256").update(token).digest("hex");

function origin(): string {
  const h = headers();
  const host = h.get("x-forwarded-host") ?? h.get("host") ?? "satforge.org";
  const proto = h.get("x-forwarded-proto") ?? (host.startsWith("localhost") ? "http" : "https");
  return `${proto}://${host}`;
}

export type RequestResult = { ok: true } | { ok: false; error: string };

export async function requestPasswordReset(rawEmail: string): Promise<RequestResult> {
  const parsed = z.string().trim().toLowerCase().email().safeParse(rawEmail);
  if (!parsed.success) return { ok: false, error: "Enter a valid email address." };
  const email = parsed.data;

  const user = await prisma.user.findUnique({
    where: { email },
    select: { id: true, name: true },
  });

  // Deliberately identical response whether or not the account exists.
  if (user) {
    const token = randomBytes(32).toString("hex");
    const identifier = `${PREFIX}${email}`;

    // One live token per address: requesting again invalidates the last link.
    await prisma.verificationToken.deleteMany({ where: { identifier } });
    await prisma.verificationToken.create({
      data: { identifier, token: hash(token), expires: new Date(Date.now() + TOKEN_TTL_MS) },
    });

    const link = `${origin()}/reset-password?token=${token}&email=${encodeURIComponent(email)}`;
    const firstName = user.name?.trim().split(/\s+/)[0] ?? "there";

    await sendEmail({
      to: email,
      subject: "Reset your SATForge password",
      text:
        `Hi ${firstName},\n\n` +
        `Use this link to set a new SATForge password. It expires in one hour ` +
        `and can only be used once.\n\n${link}\n\n` +
        `If you didn't ask for this, you can ignore this email — your password ` +
        `has not changed.`,
      html: layout(
        para(`Hi ${firstName},`) +
          para("Use the button below to set a new password. The link expires in one hour and can only be used once.") +
          button(link, "Set a new password") +
          para(
            `<span style="color:#8a97b1;font-size:13px;">If you didn't ask for this, ignore this email — your password has not changed.</span>`,
          ),
      ),
    });
  }

  return { ok: true };
}

const resetSchema = z.object({
  email: z.string().trim().toLowerCase().email(),
  token: z.string().min(32),
  password: z
    .string()
    .min(8, "Use at least 8 characters")
    .regex(/[A-Z]/, "Include one uppercase letter")
    .regex(/[0-9]/, "Include one number"),
});

export type ResetResult = { ok: true } | { ok: false; error: string };

export async function resetPassword(input: unknown): Promise<ResetResult> {
  const parsed = resetSchema.safeParse(input);
  if (!parsed.success) {
    return { ok: false, error: parsed.error.issues[0]?.message ?? "Check your details." };
  }
  const { email, token, password } = parsed.data;
  const identifier = `${PREFIX}${email}`;

  const record = await prisma.verificationToken.findUnique({
    where: { identifier_token: { identifier, token: hash(token) } },
  });
  // Same message for wrong, used and expired: a precise one would let someone
  // probe which tokens had existed.
  const invalid = { ok: false as const, error: "That reset link is invalid or has expired." };
  if (!record) return invalid;
  if (record.expires < new Date()) {
    await prisma.verificationToken.deleteMany({ where: { identifier } });
    return invalid;
  }

  const user = await prisma.user.findUnique({ where: { email }, select: { id: true } });
  if (!user) return invalid;

  const passwordHash = await bcrypt.hash(password, 12);

  // Consume the token and change the password together, so a token can never
  // survive a successful reset.
  await prisma.$transaction([
    prisma.user.update({ where: { id: user.id }, data: { passwordHash } }),
    prisma.verificationToken.deleteMany({ where: { identifier } }),
    // Any session issued against the old password is no longer trustworthy.
    prisma.session.deleteMany({ where: { userId: user.id } }),
  ]);

  return { ok: true };
}
