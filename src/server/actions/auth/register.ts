"use server";

import bcrypt from "bcryptjs";

import { credit } from "@/lib/coins";
import { prisma } from "@/lib/prisma";
import { attributeReferral } from "@/lib/referrals";
import { TERMS_VERSION } from "@/lib/legal";
import { getSettings } from "@/lib/settings";
import { registerSchema } from "@/lib/validations/auth";

export interface RegisterResult {
  error?: string;
  /** Field the error belongs to, so the form can focus the right input. */
  field?: "username" | "password";
  success?: boolean;
}

/**
 * Create an account from a username and a password. Nothing else is collected.
 *
 * WHAT THIS REPLACED, and why the old path is still in the tree: signup used
 * to sit at the end of the onboarding wizard, which asked for an exam track,
 * a target score, a grade, a test month, strengths and weaknesses, a daily
 * goal and an email, then created the account with all of it in one insert.
 * Those questions are not deleted -- `onboardingProfileSchema`,
 * `registerWithOnboarding` and the wizard component are all still here, and
 * every profile column still exists on User -- they are simply no longer in
 * the way of getting an account. They can be asked again later, from Settings
 * or a prompt after the first session, and written to the same columns.
 *
 * Everything after the insert is additive and failure there is swallowed: a
 * student must never be told their signup failed because a welcome bonus or a
 * referral attribution could not be written.
 */
export async function registerWithUsername(input: {
  username: string;
  password: string;
  referralCode?: string | null;
}): Promise<RegisterResult> {
  const parsed = registerSchema.safeParse(input);
  if (!parsed.success) {
    const issue = parsed.error.issues[0];
    const path = issue?.path[0];
    return {
      error: issue?.message ?? "Please check your details and try again.",
      field: path === "username" || path === "password" ? path : undefined,
    };
  }

  const { username, password } = parsed.data;

  let existing: { id: string } | null;
  try {
    existing = await prisma.user.findUnique({ where: { username }, select: { id: true } });
  } catch (error) {
    console.error("[register] Could not check for an existing username", error);
    return { error: "We couldn't reach the server. Please try again in a moment." };
  }
  if (existing) {
    return { error: "That username is taken. Try another.", field: "username" };
  }

  const passwordHash = await bcrypt.hash(password, 12);

  let createdUserId: string;
  try {
    const created = await prisma.user.create({
      data: {
        username,
        // `name` is what the UI greets the student with. Seeded from the
        // username so no screen has to render an empty string, and editable
        // from Settings.
        name: username,
        passwordHash,
        role: "STUDENT" as const,
        // Recorded rather than asked. The signup screen states that creating
        // an account accepts the Terms and Privacy Policy, which is the
        // consent; a checkbox would be a field, and the brief was that there
        // be none.
        termsAcceptedAt: new Date(),
        termsVersion: TERMS_VERSION,
      },
      select: { id: true },
    });
    createdUserId = created.id;
  } catch (error) {
    // A unique-constraint violation here means someone took the username
    // between the check above and this insert. Report it as the taken-name
    // error rather than as a server failure, which is what it looks like to
    // the person typing.
    if (typeof error === "object" && error !== null && "code" in error &&
        (error as { code?: string }).code === "P2002") {
      return { error: "That username is taken. Try another.", field: "username" };
    }
    console.error("[register] Failed to create user", error);
    return { error: "We couldn't create your account. Please try again in a moment." };
  }

  if (input.referralCode) {
    try {
      await attributeReferral(createdUserId, input.referralCode);
    } catch (error) {
      console.error("[register] Referral attribution failed", error);
    }
  }

  try {
    const settings = await getSettings();
    if (settings.signupBonusCoins > 0) {
      await credit({
        userId: createdUserId,
        amount: settings.signupBonusCoins,
        type: "SIGNUP_BONUS",
        description: "Welcome to Scholarly",
        // Same key shape the onboarding path used, so a student who somehow
        // reaches both is credited once.
        idempotencyKey: `signup:${createdUserId}`,
      });
    }
  } catch (error) {
    console.error("[register] Welcome bonus failed", error);
  }

  return { success: true };
}
