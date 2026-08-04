"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { onboardingProfileSchema } from "@/lib/validations/onboarding";

export interface UpdateStudyPlanResult {
  error?: string;
  success?: boolean;
}

/**
 * Lets an existing student fill in (or change) the answers the onboarding
 * wizard collects. Accounts created before the wizard existed have none of
 * this, so the dashboard links here to complete it.
 */
export async function updateStudyPlan(input: unknown): Promise<UpdateStudyPlanResult> {
  const user = await requireUser();

  const parsed = onboardingProfileSchema.safeParse(input);
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Please check your answers." };
  }
  const p = parsed.data;

  const satDate = p.satMonth ? new Date(`${p.satMonth}-01T00:00:00.000Z`) : null;

  // The session user carries no profile columns, so read the existing
  // completion timestamp before deciding whether to stamp a new one.
  const existing = await prisma.user.findUnique({
    where: { id: user.id },
    select: { onboardedAt: true },
  });

  await prisma.user.update({
    where: { id: user.id },
    data: {
      onboardingGoal: p.goal,
      currentScore: p.currentScore,
      targetScore: p.targetScore,
      dreamUniversities: p.dreamUniversities,
      countryCode: p.countryCode,
      gradeLevel: p.gradeLevel,
      satDate,
      strongestSection: p.strongestSection,
      weakestArea: p.weakestArea,
      studyMinutesPerDay: p.studyMinutesPerDay,
      dailyGoalType: p.dailyGoalType,
      dailyGoalValue: p.dailyGoalValue,
      // Marks the profile complete the first time it's filled in; keeps the
      // original timestamp on later edits.
      onboardedAt: existing?.onboardedAt ?? new Date(),
    },
  });

  revalidatePath("/dashboard");
  revalidatePath("/settings");
  return { success: true };
}
