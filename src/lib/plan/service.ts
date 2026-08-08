import { prisma } from "@/lib/prisma";
import { generatePlan } from "@/lib/plan/generate";
import type { StudyPlanData } from "@/lib/plan/types";
import { estimateScaledScore } from "@/lib/scoring/estimate";

/**
 * Reading and refreshing a student's plan.
 *
 * The plan is derived data, so the source of truth is always the raw evidence
 * and the snapshot in `StudyPlan` is a cache. The cache is invalidated by
 * **evidence count**, not by a clock: the plan is stale exactly when the
 * student has answered more questions than the snapshot was built from. That
 * makes "the plan evolves as you practise" literally true, and it means a
 * student who has not practised does not pay to regenerate an identical plan.
 *
 * A time-based floor sits alongside it so the countdown and the week
 * boundaries do not drift once a day has passed.
 */

const MAX_SNAPSHOT_AGE_MS = 12 * 60 * 60 * 1000;

async function countEvidence(userId: string): Promise<number> {
  const [qb, exam] = await Promise.all([
    prisma.questionAttempt.count({ where: { userId } }),
    prisma.response.count({
      where: { isCorrect: { not: null }, attempt: { userId } },
    }),
  ]);
  return qb + exam;
}

async function planInputsFor(userId: string) {
  const user = await prisma.user.findUniqueOrThrow({
    where: { id: userId },
    select: {
      currentScore: true,
      targetScore: true,
      satDate: true,
      studyMinutesPerDay: true,
      weakestArea: true,
    },
  });

  // Prefer a score the student actually produced over the one they reported at
  // signup — a real submitted attempt is better evidence than a memory. A
  // stored scaled score wins over an estimate; the estimate is the fallback for
  // attempts that were never fully scored, which mirrors what the dashboard
  // already does.
  const latest = await prisma.attempt.findFirst({
    where: { userId, status: "SUBMITTED" },
    orderBy: { submittedAt: "desc" },
    select: { id: true, totalScaledScore: true },
  });

  let estimatedScore: number | null = latest?.totalScaledScore ?? null;

  if (latest && estimatedScore === null) {
    const [total, correct] = await Promise.all([
      prisma.response.count({ where: { attemptId: latest.id, isCorrect: { not: null } } }),
      prisma.response.count({ where: { attemptId: latest.id, isCorrect: true } }),
    ]);
    if (total > 0) {
      // Both sections estimated off one overall accuracy: rough, but this only
      // fires for attempts that were never scored properly, and it is clearly
      // labelled as an estimate wherever it surfaces.
      const accuracy = Math.round((correct / total) * 100);
      estimatedScore = estimateScaledScore(accuracy) * 2;
    }
  }

  return {
    userId,
    currentScore: user.currentScore,
    targetScore: user.targetScore,
    testDate: user.satDate,
    studyMinutesPerDay: user.studyMinutesPerDay,
    weakestArea: user.weakestArea,
    estimatedScore,
  };
}

/**
 * The student's plan, regenerating it if the evidence has moved.
 *
 * `force` is for the "rebuild my plan" button and for the moment right after
 * onboarding, where a plan must exist even though nothing has been answered.
 */
export async function getOrCreatePlan(
  userId: string,
  opts: { force?: boolean } = {},
): Promise<StudyPlanData> {
  const [existing, evidenceCount] = await Promise.all([
    prisma.studyPlan.findUnique({ where: { userId } }),
    countEvidence(userId),
  ]);

  const fresh =
    existing &&
    !opts.force &&
    existing.evidenceCount === evidenceCount &&
    Date.now() - existing.generatedAt.getTime() < MAX_SNAPSHOT_AGE_MS;

  if (fresh) return existing.data as unknown as StudyPlanData;

  const inputs = await planInputsFor(userId);
  const data = await generatePlan(inputs);

  await prisma.studyPlan.upsert({
    where: { userId },
    create: {
      userId,
      data: data as unknown as object,
      targetScore: inputs.targetScore,
      currentScore: inputs.currentScore,
      testDate: inputs.testDate,
      evidenceCount,
      generatedAt: new Date(),
    },
    update: {
      data: data as unknown as object,
      targetScore: inputs.targetScore,
      currentScore: inputs.currentScore,
      testDate: inputs.testDate,
      evidenceCount,
      generatedAt: new Date(),
    },
  });

  return data;
}

/**
 * Cheap read for surfaces that only need the summary — the dashboard card, the
 * sidebar. Falls back to a full generation when no snapshot exists yet.
 */
export async function getPlanSummary(userId: string) {
  const plan = await getOrCreatePlan(userId);
  return {
    headline: plan.headline,
    currentScore: plan.currentScore,
    estimatedScore: plan.estimatedScore,
    targetScore: plan.targetScore,
    scoreGap: plan.scoreGap,
    daysUntilTest: plan.daysUntilTest,
    coldStart: plan.coldStart,
    thisWeek: plan.weeks[0] ?? null,
    topPriorities: plan.priorities.slice(0, 3),
    evidenceCount: plan.evidenceCount,
  };
}
