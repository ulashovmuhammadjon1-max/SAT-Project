import { Prisma } from "@prisma/client";
import { countedStudentWhere } from "@/lib/counted-students";

import { prisma } from "@/lib/prisma";

/**
 * Reads of the onboarding profile columns are guarded, because the schema and
 * the deployed database can legitimately be out of step for a short window:
 * Vercel builds a Prisma client from schema.prisma on every deploy, but the
 * migration is applied separately. Without this guard the whole dashboard
 * 500s on a column that only powers optional personalisation.
 *
 * Only P2022 ("column does not exist") is swallowed — every other database
 * error still propagates, so real faults stay loud.
 */
function isMissingColumn(error: unknown): boolean {
  return error instanceof Prisma.PrismaClientKnownRequestError && (error.code === "P2022" || error.code === "P2021");
}

let warned = false;
function warnOnce() {
  if (warned) return;
  warned = true;
  console.warn(
    "[onboarding] Profile columns are missing from the database. " +
      "Apply prisma/migrations/manual/001_onboarding_profile.sql (or run `prisma db push`). " +
      "Personalisation is disabled until then."
  );
}

const PROFILE_SELECT = {
  onboardingGoal: true,
  currentScore: true,
  targetScore: true,
  dreamUniversities: true,
  countryCode: true,
  gradeLevel: true,
  satDate: true,
  strongestSection: true,
  weakestArea: true,
  studyMinutesPerDay: true,
  dailyGoalType: true,
  dailyGoalValue: true,
  onboardedAt: true,
  currentStreak: true,
} satisfies Prisma.UserSelect;

export type StoredProfile = Prisma.UserGetPayload<{ select: typeof PROFILE_SELECT }>;

/** One student's onboarding profile, or null if the columns aren't there yet. */
export async function readProfile(userId: string): Promise<StoredProfile | null> {
  try {
    return await prisma.user.findUnique({ where: { id: userId }, select: PROFILE_SELECT });
  } catch (error) {
    if (isMissingColumn(error)) {
      warnOnce();
      return null;
    }
    throw error;
  }
}

const AUDIENCE_SELECT = {
  countryCode: true,
  gradeLevel: true,
  dreamUniversities: true,
  satDate: true,
  onboardedAt: true,
} satisfies Prisma.UserSelect;

export type AudienceRow = Prisma.UserGetPayload<{ select: typeof AUDIENCE_SELECT }>;

export interface AudienceData {
  students: AudienceRow[];
  avgTargetScore: number | null;
  avgCurrentScore: number | null;
  avgStudyMinutes: number | null;
  targetScoreCount: number;
  currentScoreCount: number;
  studyMinutesCount: number;
  /** False when the profile columns don't exist yet, so the UI can explain why. */
  available: boolean;
}

const EMPTY_AUDIENCE: AudienceData = {
  students: [],
  avgTargetScore: null,
  avgCurrentScore: null,
  avgStudyMinutes: null,
  targetScoreCount: 0,
  currentScoreCount: 0,
  studyMinutesCount: 0,
  available: false,
};

/** Aggregate audience data for the admin analytics page. */
export async function readAudience(): Promise<AudienceData> {
  try {
    const [students, scores, study] = await Promise.all([
      prisma.user.findMany({ where: countedStudentWhere, select: AUDIENCE_SELECT }),
      prisma.user.aggregate({
        where: countedStudentWhere,
        _avg: { targetScore: true, currentScore: true },
        _count: { targetScore: true, currentScore: true },
      }),
      prisma.user.aggregate({
        where: countedStudentWhere,
        _avg: { studyMinutesPerDay: true },
        _count: { studyMinutesPerDay: true },
      }),
    ]);

    return {
      students,
      avgTargetScore: scores._avg.targetScore,
      avgCurrentScore: scores._avg.currentScore,
      avgStudyMinutes: study._avg.studyMinutesPerDay,
      targetScoreCount: scores._count.targetScore,
      currentScoreCount: scores._count.currentScore,
      studyMinutesCount: study._count.studyMinutesPerDay,
      available: true,
    };
  } catch (error) {
    if (isMissingColumn(error)) {
      warnOnce();
      return EMPTY_AUDIENCE;
    }
    throw error;
  }
}

/** True when the write path can persist onboarding answers. */
export function isMissingColumnError(error: unknown): boolean {
  return isMissingColumn(error);
}
