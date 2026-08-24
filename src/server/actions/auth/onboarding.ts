"use server";

import bcrypt from "bcryptjs";

import { credit } from "@/lib/coins";
import { prisma } from "@/lib/prisma";
import { isMissingColumnError } from "@/lib/onboarding/profile";
import { attributeReferral } from "@/lib/referrals";
import { sendVerificationEmail } from "@/server/actions/auth/email-verification";
import { TERMS_VERSION } from "@/lib/legal";
import { getSettings } from "@/lib/settings";
import { onboardingSignupSchema, type OnboardingSignup } from "@/lib/validations/onboarding";

export interface OnboardingSignupResult {
  error?: string;
  /** Field the error belongs to, so the wizard can focus the right input. */
  field?: "name" | "email" | "password";
  success?: boolean;
}

/**
 * Creates the account at the *end* of the onboarding wizard, writing every
 * answer collected along the way in the same insert. Until this runs, the
 * answers live only in the browser — no partial user rows are ever created.
 */
export async function registerWithOnboarding(input: OnboardingSignup): Promise<OnboardingSignupResult> {
  const parsed = onboardingSignupSchema.safeParse(input);
  if (!parsed.success) {
    const issue = parsed.error.issues[0];
    const path = issue?.path[0];
    return {
      error: issue?.message ?? "Please check your details and try again.",
      field: path === "name" || path === "email" || path === "password" ? path : undefined,
    };
  }

  const { name, email, password, profile } = parsed.data;
  const termsAcceptedAt = new Date();

  let existing: { id: string } | null;
  try {
    existing = await prisma.user.findUnique({ where: { email }, select: { id: true } });
  } catch (error) {
    console.error("[onboarding] Could not check for an existing account", error);
    return { error: "We couldn't reach the server. Please try again in a moment." };
  }
  if (existing) {
    return { error: "An account with this email already exists.", field: "email" };
  }

  const passwordHash = await bcrypt.hash(password, 12);

  // A month-precision answer is stored as midnight UTC on the 1st, so date
  // comparisons in the admin panel don't drift with the viewer's timezone.
  const satDate = profile.satMonth ? new Date(`${profile.satMonth}-01T00:00:00.000Z`) : null;
  const ieltsDate = profile.ielts.examMonth
    ? new Date(`${profile.ielts.examMonth}-01T00:00:00.000Z`)
    : null;

  // The track chosen on the first screen decides two different things, which
  // is why it lands in two columns. `preparationExams` is what the student is
  // working towards and governs what data exists; `activeExam` is what they
  // are looking at right now. Picking one exam never removes the other from
  // the switcher — it only decides which questions were worth asking.
  const track = profile.track ?? "SAT";
  const preparationExams =
    track === "BOTH" ? (["SAT", "IELTS"] as const) : ([track] as const);

  const base = {
    name,
    email,
    passwordHash,
    role: "STUDENT" as const,
    termsAcceptedAt,
    termsVersion: TERMS_VERSION,
  };

  let createdUserId: string | null = null;

  try {
    const created = await prisma.user.create({
      data: {
        ...base,
        onboardingGoal: profile.goal,
        currentScore: profile.currentScore,
        targetScore: profile.targetScore,
        dreamUniversities: profile.dreamUniversities,
        countryCode: profile.countryCode,
        gradeLevel: profile.gradeLevel,
        satDate,
        strongestSection: profile.strongestSection,
        weakestArea: profile.weakestArea,
        studyMinutesPerDay: profile.studyMinutesPerDay,
        dailyGoalType: profile.dailyGoalType,
        dailyGoalValue: profile.dailyGoalValue,
        onboardedAt: new Date(),
        preparationExams: [...preparationExams],
        activeExam: track,
      },
      select: { id: true },
    });
    createdUserId = created.id;
  } catch (error) {
    // If the deployed database predates the onboarding columns, still create
    // the account — being unable to save a target score is no reason to block
    // someone from signing up. They can fill the plan in from Settings once
    // the migration lands.
    if (!isMissingColumnError(error)) {
      console.error("[onboarding] Failed to create user", error);
      return { error: "We couldn't create your account. Please try again in a moment." };
    }

    console.warn("[onboarding] Profile columns missing — creating account without the study plan.");
    try {
      const created = await prisma.user.create({ data: base, select: { id: true } });
      createdUserId = created.id;
    } catch (fallbackError) {
      console.error("[onboarding] Fallback user creation failed", fallbackError);
      return { error: "We couldn't create your account. Please try again in a moment." };
    }
  }

  // The account exists from here on. Everything below is additive, so any
  // failure is logged and swallowed: a student must never be told their signup
  // failed because a welcome bonus could not be written.
  if (createdUserId) {
    // The IELTS answers, when they were asked for. Separate row, separate
    // failure: a student whose IELTS profile cannot be written still has an
    // account and can answer again from the IELTS side.
    if (track !== "SAT") {
      try {
        await prisma.ieltsStudentProfile.create({
          data: {
            userId: createdUserId,
            reason: profile.ielts.reason?.toLowerCase() ?? null,
            targetBand: profile.ielts.targetBand,
            examDate: ieltsDate,
            currentWriting: profile.ielts.currentWriting,
            currentSpeaking: profile.ielts.currentSpeaking,
            levelSource: profile.ielts.levelSource?.toLowerCase() ?? null,
            studyMinutesPerDay: profile.ielts.studyMinutesPerDay,
            focusSkill: profile.ielts.focusSkill,
            onboardedAt: new Date(),
          },
        });
      } catch (error) {
        console.error("[onboarding] Could not save the IELTS profile", error);
      }
    }

    await grantSignupRewards(createdUserId, input.referralCode ?? null);

    try {
      await sendVerificationEmail({ email, name });
    } catch (error) {
      // The account exists and the student can ask for the link again from the
      // waiting screen. Failing the signup over an undelivered email would be
      // the worse outcome by a distance.
      console.error("[onboarding] verification email failed", error);
    }
  }

  return { success: true };
}

/**
 * Welcome coins, and attribution of the referral if the account arrived through
 * an invite link.
 *
 * The referral is only *recorded* here. It pays out when the new account
 * confirms its email address (`verifyEmail`), which is what makes inventing
 * accounts to farm invite coins cost a working inbox each.
 *
 * The signup bonus is keyed on the user id and the referral reward on the
 * referral id, so a retried signup or a double-submitted form cannot mint extra
 * coins.
 */
async function grantSignupRewards(userId: string, rawReferralCode: string | null) {
  const settings = await getSettings();

  try {
    if (settings.signupBonusCoins > 0) {
      await credit({
        userId,
        amount: settings.signupBonusCoins,
        type: "SIGNUP_BONUS",
        description: "Welcome to Scholarly",
        idempotencyKey: `signup:${userId}`,
      });
    }
  } catch (error) {
    console.error("[onboarding] signup bonus failed", error);
  }

  try {
    const { outcome } = await attributeReferral(userId, rawReferralCode);
    if (outcome !== "attributed" && outcome !== "no_code") {
      console.info(`[onboarding] referral not attributed: ${outcome}`);
    }
  } catch (error) {
    console.error("[onboarding] referral attribution failed", error);
  }
}
