import { prisma } from "@/lib/prisma";

/**
 * Operating statistics for the admin panel.
 *
 * Everything here is computed with SQL aggregates rather than by pulling rows
 * into memory. The existing analytics page loads 5,000 `Response` rows to
 * bucket them by domain, which is fine at 20 students and is not fine later;
 * these queries stay flat as the platform grows because the database does the
 * counting.
 *
 * Every figure is derived from real rows. Where there is no data yet a section
 * returns an empty array and the page says so, rather than rendering a zero
 * that reads like a measurement.
 */

export interface FunnelStep {
  label: string;
  count: number;
  /** Share of the first step, so the drop-off is visible without arithmetic. */
  pctOfTop: number;
  note: string;
}

export interface TrendPoint {
  label: string;
  value: number;
}

export interface TestUsageRow {
  title: string;
  started: number;
  completed: number;
  completionPct: number;
  averageScore: number | null;
}

export interface QuestionOutlier {
  questionId: string;
  ref: string;
  testTitle: string;
  moduleLabel: string;
  order: number;
  domain: string;
  skill: string;
  difficulty: string;
  attempts: number;
  correct: number;
  accuracyPct: number;
}

export interface ScoreBucket {
  label: string;
  value: number;
}

export interface AdminStatistics {
  funnel: FunnelStep[];
  signupsByWeek: TrendPoint[];
  activityByDay: TrendPoint[];
  scoreDistribution: ScoreBucket[];
  averageTotalScore: number | null;
  testUsage: TestUsageRow[];
  hardest: QuestionOutlier[];
  easiest: QuestionOutlier[];
  activeLast7: number;
  activeLast30: number;
  questionsAnsweredAllTime: number;
}

const asNumber = (v: unknown): number => (v == null ? 0 : Number(v));

/**
 * Students who have got as far as each stage.
 *
 * Deliberately counts distinct students, not events: one person who took six
 * tests is one student who reached "completed a test". Counting events here is
 * the classic way a funnel ends up widening at the bottom.
 */
async function buildFunnel(): Promise<FunnelStep[]> {
  const [signedUp, onboarded, verified, started, completed] = await Promise.all([
    prisma.user.count({ where: { role: "STUDENT" } }),
    prisma.user.count({ where: { role: "STUDENT", onboardedAt: { not: null } } }),
    prisma.user.count({ where: { role: "STUDENT", emailVerified: { not: null } } }),
    prisma.attempt
      .findMany({ where: {}, select: { userId: true }, distinct: ["userId"] })
      .then((rows) => rows.length),
    prisma.attempt
      .findMany({ where: { status: "SUBMITTED" }, select: { userId: true }, distinct: ["userId"] })
      .then((rows) => rows.length),
  ]);

  const top = signedUp || 1;
  const step = (label: string, count: number, note: string): FunnelStep => ({
    label,
    count,
    pctOfTop: Math.round((count / top) * 100),
    note,
  });

  return [
    step("Signed up", signedUp, "student accounts created"),
    step("Finished onboarding", onboarded, "answered the plan questions"),
    step("Confirmed email", verified, "clicked the confirmation link"),
    step("Started a test", started, "opened at least one practice test"),
    step("Completed a test", completed, "submitted a full test"),
  ];
}

/** Signups per ISO week for the last 12 weeks, oldest first. */
async function signupsByWeek(): Promise<TrendPoint[]> {
  const rows = await prisma.$queryRaw<{ week: Date; n: bigint }[]>`
    SELECT date_trunc('week', "createdAt") AS week, COUNT(*)::bigint AS n
      FROM "User"
     WHERE role = 'STUDENT'
       AND "createdAt" >= now() - interval '12 weeks'
     GROUP BY 1
     ORDER BY 1
  `;
  return rows.map((r) => ({
    label: new Date(r.week).toLocaleDateString(undefined, { day: "numeric", month: "short" }),
    value: asNumber(r.n),
  }));
}

/** Questions answered per day for the last 30 days, from the study log. */
async function activityByDay(): Promise<TrendPoint[]> {
  const rows = await prisma.$queryRaw<{ day: Date; n: bigint }[]>`
    SELECT date AS day, SUM("questionsAnswered")::bigint AS n
      FROM "StudyActivity"
     WHERE date >= (now() - interval '30 days')::date
     GROUP BY 1
     ORDER BY 1
  `;
  return rows.map((r) => ({
    label: new Date(r.day).toLocaleDateString(undefined, { day: "numeric", month: "short" }),
    value: asNumber(r.n),
  }));
}

/**
 * Submitted totals bucketed into 100-point bands.
 *
 * Buckets rather than a raw list because a score histogram is the thing an
 * operator actually reads: it answers "are people scoring where we'd expect".
 */
async function scoreDistribution(): Promise<{ buckets: ScoreBucket[]; average: number | null }> {
  const rows = await prisma.attempt.findMany({
    where: { status: "SUBMITTED", totalScaledScore: { not: null } },
    select: { totalScaledScore: true },
  });
  if (!rows.length) return { buckets: [], average: null };

  const counts = new Map<number, number>();
  let sum = 0;
  for (const r of rows) {
    const score = r.totalScaledScore!;
    sum += score;
    const band = Math.min(1500, Math.floor(score / 100) * 100);
    counts.set(band, (counts.get(band) ?? 0) + 1);
  }

  const buckets: ScoreBucket[] = [];
  for (let band = 400; band <= 1500; band += 100) {
    buckets.push({ label: `${band}–${band + 99}`, value: counts.get(band) ?? 0 });
  }
  return { buckets, average: Math.round(sum / rows.length / 10) * 10 };
}

/** Per-test uptake: how many started it, how many finished, how they scored. */
async function testUsage(): Promise<TestUsageRow[]> {
  const rows = await prisma.$queryRaw<
    { title: string; started: bigint; completed: bigint; avg: number | null }[]
  >`
    SELECT t.title                                             AS title,
           COUNT(a.id)::bigint                                 AS started,
           COUNT(a.id) FILTER (WHERE a.status = 'SUBMITTED')::bigint AS completed,
           AVG(a."totalScaledScore") FILTER (WHERE a."totalScaledScore" IS NOT NULL) AS avg
      FROM "Test" t
      LEFT JOIN "Attempt" a ON a."testId" = t.id
     GROUP BY t.id, t.title
    HAVING COUNT(a.id) > 0
     ORDER BY COUNT(a.id) DESC
  `;
  return rows.map((r) => {
    const started = asNumber(r.started);
    const completed = asNumber(r.completed);
    return {
      title: r.title,
      started,
      completed,
      completionPct: started ? Math.round((completed / started) * 100) : 0,
      // Scores are always multiples of ten, so an average is rounded back to
      // one rather than shown as 1043.
      averageScore: r.avg == null ? null : Math.round(Number(r.avg) / 10) * 10,
    };
  });
}

/**
 * Questions students get right or wrong far more often than expected.
 *
 * This is the content-QA view: a question nobody answers correctly is usually
 * broken — a wrong key, an ambiguous stem, a missing figure — rather than
 * genuinely hard, and one everybody gets right is not testing anything. Both
 * ends are worth an editor's eye.
 *
 * Answers from the Question Bank and from real tests are pooled, because a
 * defective question is defective in both places.
 */
async function questionOutliers(minAttempts: number): Promise<{
  hardest: QuestionOutlier[];
  easiest: QuestionOutlier[];
}> {
  const rows = await prisma.$queryRaw<
    {
      questionid: string;
      testtitle: string;
      subject: string;
      mo: number;
      mdiff: string;
      qorder: number;
      domain: string;
      skill: string;
      difficulty: string;
      attempts: bigint;
      correct: bigint;
    }[]
  >`
    WITH answers AS (
      SELECT r."questionId" AS question_id, r."isCorrect" AS is_correct
        FROM "Response" r
       WHERE r."isCorrect" IS NOT NULL
      UNION ALL
      SELECT qa."questionId", qa."isCorrect"
        FROM "QuestionAttempt" qa
    )
    SELECT q.id            AS questionid,
           t.title         AS testtitle,
           m.subject::text AS subject,
           m."order"       AS mo,
           m.difficulty::text AS mdiff,
           q."order"       AS qorder,
           d.name          AS domain,
           s.name          AS skill,
           q.difficulty::text AS difficulty,
           COUNT(*)::bigint AS attempts,
           COUNT(*) FILTER (WHERE a.is_correct)::bigint AS correct
      FROM answers a
      JOIN "Question" q ON q.id = a.question_id
      JOIN "Module"  m ON m.id = q."moduleId"
      JOIN "Test"    t ON t.id = m."testId"
      JOIN "Domain"  d ON d.id = q."domainId"
      JOIN "Skill"   s ON s.id = q."skillId"
     GROUP BY q.id, t.title, m.subject, m."order", m.difficulty, q."order", d.name, s.name, q.difficulty
    HAVING COUNT(*) >= ${minAttempts}
  `;

  const mapped: QuestionOutlier[] = rows.map((r) => {
    const attempts = asNumber(r.attempts);
    const correct = asNumber(r.correct);
    const branch = r.mdiff === "STANDARD" ? "" : ` ${r.mdiff === "EASY" ? "Easy" : "Hard"}`;
    return {
      questionId: r.questionid,
      ref: `Q-${r.questionid.slice(-6).toUpperCase()}`,
      testTitle: r.testtitle,
      moduleLabel: `${r.subject === "MATH" ? "Math" : "R&W"} M${r.mo}${branch}`,
      order: r.qorder,
      domain: r.domain,
      skill: r.skill,
      difficulty: r.difficulty,
      attempts,
      correct,
      accuracyPct: attempts ? Math.round((correct / attempts) * 100) : 0,
    };
  });

  const byAccuracy = [...mapped].sort(
    (a, b) => a.accuracyPct - b.accuracyPct || b.attempts - a.attempts
  );
  return {
    hardest: byAccuracy.slice(0, 10),
    easiest: [...byAccuracy].reverse().slice(0, 10),
  };
}

/**
 * Everything the statistics page needs, in one round of parallel queries.
 *
 * `minAttempts` guards the outlier tables: with two or three answers a question
 * sits at 0% or 100% by chance, and a table full of noise is worse than no
 * table because it gets ignored.
 */
export async function getAdminStatistics(minAttempts = 5): Promise<AdminStatistics> {
  const [
    funnel,
    weeks,
    days,
    scores,
    usage,
    outliers,
    activeLast7,
    activeLast30,
    answeredAgg,
  ] = await Promise.all([
    buildFunnel(),
    signupsByWeek(),
    activityByDay(),
    scoreDistribution(),
    testUsage(),
    questionOutliers(minAttempts),
    prisma.studyActivity
      .findMany({
        where: { date: { gte: new Date(Date.now() - 7 * 86_400_000) }, questionsAnswered: { gt: 0 } },
        select: { userId: true },
        distinct: ["userId"],
      })
      .then((r) => r.length),
    prisma.studyActivity
      .findMany({
        where: { date: { gte: new Date(Date.now() - 30 * 86_400_000) }, questionsAnswered: { gt: 0 } },
        select: { userId: true },
        distinct: ["userId"],
      })
      .then((r) => r.length),
    prisma.studyActivity.aggregate({ _sum: { questionsAnswered: true } }),
  ]);

  return {
    funnel,
    signupsByWeek: weeks,
    activityByDay: days,
    scoreDistribution: scores.buckets,
    averageTotalScore: scores.average,
    testUsage: usage,
    hardest: outliers.hardest,
    easiest: outliers.easiest,
    activeLast7,
    activeLast30,
    questionsAnsweredAllTime: answeredAgg._sum.questionsAnswered ?? 0,
  };
}
