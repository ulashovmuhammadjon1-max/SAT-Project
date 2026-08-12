import { prisma } from "@/lib/prisma";

import {
  evaluateAchievements,
  type AchievementStats,
  type EarnedAchievement,
} from "./definitions";

/** The raw numbers every badge is derived from. */
export async function getAchievementStats(userId: string): Promise<AchievementStats> {
  const [user, study, qb, attemptAgg, vocabMastered, setsPassed, referrals, sessions] =
    await Promise.all([
      prisma.user.findUnique({
        where: { id: userId },
        select: { currentStreak: true, longestStreak: true },
      }),
      prisma.studyActivity.aggregate({
        where: { userId },
        _sum: { questionsAnswered: true },
        _count: { _all: true },
      }),
      prisma.questionAttempt.groupBy({
        by: ["isCorrect"],
        where: { userId },
        _count: { _all: true },
      }),
      prisma.attempt.aggregate({
        where: { userId, status: "SUBMITTED" },
        _max: { totalScaledScore: true, rwScaledScore: true, mathScaledScore: true },
        _count: { _all: true },
      }),
      prisma.vocabProgress.count({ where: { userId, status: "MASTERED" } }),
      prisma.vocabDeckProgress.count({ where: { userId, passed: true } }),
      // Only rewarded referrals count. A PENDING row is an account that signed
      // up and has not verified, and paying a badge for it would reward
      // exactly the throwaway signups verification exists to stop.
      prisma.referral.count({ where: { referrerId: userId, status: "REWARDED" } }),
      prisma.booking.count({ where: { userId, status: "COMPLETED" } }),
    ]);

  const correct = qb.find((g) => g.isCorrect)?._count._all ?? 0;
  const sample = qb.reduce((sum, g) => sum + g._count._all, 0);

  return {
    currentStreak: user?.currentStreak ?? 0,
    longestStreak: user?.longestStreak ?? 0,
    daysActive: study._count._all,
    questionsAnswered: study._sum.questionsAnswered ?? 0,
    testsCompleted: attemptAgg._count._all,
    bestScore: attemptAgg._max.totalScaledScore ?? 0,
    bestRw: attemptAgg._max.rwScaledScore ?? 0,
    bestMath: attemptAgg._max.mathScaledScore ?? 0,
    accuracyPct: sample ? Math.round((correct / sample) * 100) : 0,
    accuracySample: sample,
    vocabMastered,
    vocabSetsPassed: setsPassed,
    referralsCompleted: referrals,
    sessionsAttended: sessions,
  };
}

export interface AchievementSummary {
  all: EarnedAchievement[];
  unlocked: EarnedAchievement[];
  /**
   * The locked badges closest to completion — what to show on the dashboard.
   * Badges with zero progress are excluded: "answer 5000 questions, 0%" is not
   * a nudge, it is noise.
   */
  nextUp: EarnedAchievement[];
  unlockedCount: number;
  totalCount: number;
}

export async function getAchievements(userId: string): Promise<AchievementSummary> {
  const all = evaluateAchievements(await getAchievementStats(userId));
  const unlocked = all.filter((a) => a.unlocked);

  const nextUp = all
    .filter((a) => !a.unlocked && a.progressPct > 0 && !a.blockedBy)
    .sort((a, b) => b.progressPct - a.progressPct)
    .slice(0, 3);

  return { all, unlocked, nextUp, unlockedCount: unlocked.length, totalCount: all.length };
}
