"use server";

import bcrypt from "bcryptjs";

import { prisma } from "@/lib/prisma";
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

  const existing = await prisma.user.findUnique({ where: { email }, select: { id: true } });
  if (existing) {
    return { error: "An account with this email already exists.", field: "email" };
  }

  const passwordHash = await bcrypt.hash(password, 12);

  // A month-precision answer is stored as midnight UTC on the 1st, so date
  // comparisons in the admin panel don't drift with the viewer's timezone.
  const satDate = profile.satMonth ? new Date(`${profile.satMonth}-01T00:00:00.000Z`) : null;

  try {
    await prisma.user.create({
      data: {
        name,
        email,
        passwordHash,
        role: "STUDENT",
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
  } catch {
    return { error: "We couldn't create your account. Please try again in a moment." };
  }

  return { success: true };
}
