"use server";

import bcrypt from "bcryptjs";

import { prisma } from "@/lib/prisma";
import { isMissingColumnError } from "@/lib/onboarding/profile";
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

  const base = { name, email, passwordHash, role: "STUDENT" as const };

  try {
    await prisma.user.create({
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
      },
    });
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
      await prisma.user.create({ data: base });
    } catch (fallbackError) {
      console.error("[onboarding] Fallback user creation failed", fallbackError);
      return { error: "We couldn't create your account. Please try again in a moment." };
    }
  }

  return { success: true };
}
