import { prisma } from "@/lib/prisma";

/**
 * Where a score sits against everyone else who sat the same test.
 *
 * The number is only shown once enough people have taken the test. With four
 * other students, "you beat 75% of test-takers" is one person's bad afternoon,
 * not a percentile — and a rank presented with false confidence is worse than
 * no rank, because students plan around it.
 */

/** Below this many scored attempts, a percentile is not reported at all. */
export const PERCENTILE_MIN_SAMPLE = 15;

export interface PeerComparison {
  /** Scored attempts on this test by other students. */
  sample: number;
  /** 0–100, or null when the sample is too small to say. */
  percentile: number | null;
  /** Mean score across the cohort, or null below the floor. */
  cohortAverage: number | null;
  /** Best score anyone has posted on this test, or null below the floor. */
  cohortBest: number | null;
}

/**
 * Compare one attempt's total against the cohort for its test.
 *
 * Counts one attempt per student — their best — so a student who sits the same
 * test five times does not fill five slots in the distribution and drag the
 * percentile around. Their own attempts are excluded entirely: being told you
 * beat yourself is noise.
 */
export async function getPeerComparison(
  testId: string,
  userId: string,
  score: number | null
): Promise<PeerComparison> {
  const rows = await prisma.$queryRaw<{ best: number }[]>`
    SELECT MAX(a."totalScaledScore")::int AS best
      FROM "Attempt" a
      JOIN "User" u ON u.id = a."userId"
     WHERE a."testId" = ${testId}
       AND a.status = 'SUBMITTED'
       AND a."totalScaledScore" IS NOT NULL
       AND a."userId" <> ${userId}
       AND u.role = 'STUDENT'
     GROUP BY a."userId"
  `;

  const sample = rows.length;
  if (sample < PERCENTILE_MIN_SAMPLE || score == null) {
    return { sample, percentile: null, cohortAverage: null, cohortBest: null };
  }

  const scores = rows.map((r) => r.best);
  const below = scores.filter((s) => s < score).length;
  const equal = scores.filter((s) => s === score).length;

  return {
    sample,
    // Midpoint of the tied band, the standard convention. Using strictly-less
    // alone reports 0th percentile for everyone tied at the bottom, and
    // less-or-equal reports 100th for everyone tied at the top.
    percentile: Math.round(((below + equal / 2) / sample) * 100),
    cohortAverage: Math.round(scores.reduce((sum, s) => sum + s, 0) / sample / 10) * 10,
    cohortBest: Math.max(...scores),
  };
}
