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

export interface SessionStats {
  /** Distinct students who have ever booked, whatever the outcome. */
  uniqueStudentsBooked: number;
  /** Distinct students with at least one booking marked COMPLETED. */
  uniqueStudentsAttended: number;
  /** Bookings, not people — the gap between the two is the repeat rate. */
  totalBookings: number;
  completedBookings: number;
  cancelledBookings: number;
  upcomingBookings: number;
  /** Bookings per attending student, which says whether people come back. */
  repeatRate: number | null;
  byType: { type: string; bookings: number; uniqueStudents: number }[];
}

export interface StudentActivityRow {
  userId: string;
  name: string | null;
  email: string | null;
  joinedAt: Date;
  lastActiveAt: Date | null;
  questionsAnswered: number;
  daysActive: number;
  testsCompleted: number;
  bestScore: number | null;
  accuracyPct: number | null;
  sessionsBooked: number;
  sessionsAttended: number;
}

/**
 * This week's signups against last week's.
 *
 * Weeks are Postgres `date_trunc('week', …)` buckets, which start on Monday.
 * The current week is deliberately *partial* — it is however far into the week
 * we are — so `partialWeek` is exposed and the page says so. Comparing three
 * days against a full seven and calling it a fall would be misleading.
 */
export interface SignupComparison {
  thisWeek: number;
  lastWeek: number;
  /** Signed difference; null when there is no prior week to compare against. */
  change: number | null;
  changePct: number | null;
  /** Days elapsed in the current week, 1–7. */
  daysIntoWeek: number;
}

export interface AdminStatistics {
  funnel: FunnelStep[];
  signupsByWeek: TrendPoint[];
  signupComparison: SignupComparison;
  activityByDay: TrendPoint[];
  scoreDistribution: ScoreBucket[];
  averageTotalScore: number | null;
  testUsage: TestUsageRow[];
  hardest: QuestionOutlier[];
  easiest: QuestionOutlier[];
  activeLast7: number;
  activeLast30: number;
  questionsAnsweredAllTime: number;
  sessions: SessionStats;
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

/** This week's student signups against last week's. */
async function signupComparison(): Promise<SignupComparison> {
  const rows = await prisma.$queryRaw<{ bucket: string; n: bigint }[]>`
    SELECT CASE
             WHEN "createdAt" >= date_trunc('week', now()) THEN 'this'
             ELSE 'last'
           END AS bucket,
           COUNT(*)::bigint AS n
      FROM "User"
     WHERE role = 'STUDENT'
       AND "createdAt" >= date_trunc('week', now()) - interval '1 week'
     GROUP BY 1
  `;
  const thisWeek = asNumber(rows.find((r) => r.bucket === "this")?.n);
  const lastWeek = asNumber(rows.find((r) => r.bucket === "last")?.n);

  // Monday is day 1. getDay() calls Sunday 0, which would otherwise report the
  // last day of the week as the zeroth.
  const dow = new Date().getDay();
  const daysIntoWeek = dow === 0 ? 7 : dow;

  return {
    thisWeek,
    lastWeek,
    change: lastWeek === 0 && thisWeek === 0 ? null : thisWeek - lastWeek,
    // A percentage against a zero baseline is infinity, not growth.
    changePct: lastWeek === 0 ? null : Math.round(((thisWeek - lastWeek) / lastWeek) * 100),
    daysIntoWeek,
  };
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
 * Session uptake.
 *
 * The number that matters is **distinct students**, not bookings: ten bookings
 * could be ten people who each came once or one person who came ten times, and
 * those are opposite outcomes for a platform whose whole differentiator is the
 * 1-on-1. Both are reported, and the ratio between them is the repeat rate.
 *
 * "Attended" means a booking marked COMPLETED. That is an operator's judgement
 * recorded after the session, not automatic attendance — nothing here observes
 * whether anyone actually joined the call.
 */
async function sessionStats(): Promise<SessionStats> {
  const [rows, byTypeRows] = await Promise.all([
    prisma.$queryRaw<
      {
        unique_booked: bigint;
        unique_attended: bigint;
        total: bigint;
        completed: bigint;
        cancelled: bigint;
        upcoming: bigint;
      }[]
    >`
      SELECT COUNT(DISTINCT "userId")::bigint AS unique_booked,
             COUNT(DISTINCT "userId") FILTER (WHERE status = 'COMPLETED')::bigint AS unique_attended,
             COUNT(*)::bigint AS total,
             COUNT(*) FILTER (WHERE status = 'COMPLETED')::bigint AS completed,
             COUNT(*) FILTER (WHERE status = 'CANCELLED')::bigint AS cancelled,
             COUNT(*) FILTER (WHERE status = 'UPCOMING')::bigint  AS upcoming
        FROM "Booking"
    `,
    prisma.$queryRaw<{ type: string; bookings: bigint; students: bigint }[]>`
      SELECT "sessionType"::text AS type,
             COUNT(*)::bigint AS bookings,
             COUNT(DISTINCT "userId")::bigint AS students
        FROM "Booking"
       GROUP BY "sessionType"
       ORDER BY COUNT(*) DESC
    `,
  ]);

  const r = rows[0];
  const attended = asNumber(r?.unique_attended);
  const completed = asNumber(r?.completed);

  return {
    uniqueStudentsBooked: asNumber(r?.unique_booked),
    uniqueStudentsAttended: attended,
    totalBookings: asNumber(r?.total),
    completedBookings: completed,
    cancelledBookings: asNumber(r?.cancelled),
    upcomingBookings: asNumber(r?.upcoming),
    repeatRate: attended ? Math.round((completed / attended) * 10) / 10 : null,
    byType: byTypeRows.map((t) => ({
      type: t.type,
      bookings: asNumber(t.bookings),
      uniqueStudents: asNumber(t.students),
    })),
  };
}

/**
 * One row per student, so an operator can look at people rather than totals.
 *
 * Assembled from four sources in a single query — the study log, graded test
 * attempts, pooled answers, and bookings — because doing it per student would
 * be one query per row and this list is meant to be read at a glance.
 */
export async function getStudentActivity(limit = 200): Promise<StudentActivityRow[]> {
  const rows = await prisma.$queryRaw<
    {
      id: string;
      name: string | null;
      email: string | null;
      createdat: Date;
      lastactive: Date | null;
      answered: bigint;
      daysactive: bigint;
      testscompleted: bigint;
      bestscore: number | null;
      correct: bigint;
      attempted: bigint;
      booked: bigint;
      attended: bigint;
    }[]
  >`
    SELECT u.id, u.name, u.email, u."createdAt" AS createdat,
           (SELECT MAX(sa.date) FROM "StudyActivity" sa WHERE sa."userId" = u.id) AS lastactive,
           COALESCE((SELECT SUM(sa."questionsAnswered") FROM "StudyActivity" sa WHERE sa."userId" = u.id), 0)::bigint AS answered,
           (SELECT COUNT(*) FROM "StudyActivity" sa WHERE sa."userId" = u.id AND sa."questionsAnswered" > 0)::bigint AS daysactive,
           (SELECT COUNT(*) FROM "Attempt" a WHERE a."userId" = u.id AND a.status = 'SUBMITTED')::bigint AS testscompleted,
           (SELECT MAX(a."totalScaledScore") FROM "Attempt" a WHERE a."userId" = u.id) AS bestscore,
           (SELECT COUNT(*) FROM "QuestionAttempt" qa WHERE qa."userId" = u.id AND qa."isCorrect")::bigint AS correct,
           (SELECT COUNT(*) FROM "QuestionAttempt" qa WHERE qa."userId" = u.id)::bigint AS attempted,
           (SELECT COUNT(*) FROM "Booking" b WHERE b."userId" = u.id)::bigint AS booked,
           (SELECT COUNT(*) FROM "Booking" b WHERE b."userId" = u.id AND b.status = 'COMPLETED')::bigint AS attended
      FROM "User" u
     WHERE u.role = 'STUDENT'
     ORDER BY u."createdAt" DESC
     LIMIT ${limit}
  `;

  return rows.map((r) => {
    const attempted = asNumber(r.attempted);
    return {
      userId: r.id,
      name: r.name,
      email: r.email,
      joinedAt: r.createdat,
      lastActiveAt: r.lastactive,
      questionsAnswered: asNumber(r.answered),
      daysActive: asNumber(r.daysactive),
      testsCompleted: asNumber(r.testscompleted),
      bestScore: r.bestscore == null ? null : Number(r.bestscore),
      // Only from Question Bank answers, where a graded row always exists.
      accuracyPct: attempted ? Math.round((asNumber(r.correct) / attempted) * 100) : null,
      sessionsBooked: asNumber(r.booked),
      sessionsAttended: asNumber(r.attended),
    };
  });
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
    weekCompare,
    days,
    scores,
    usage,
    outliers,
    activeLast7,
    activeLast30,
    answeredAgg,
    sessions,
  ] = await Promise.all([
    buildFunnel(),
    signupsByWeek(),
    signupComparison(),
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
    sessionStats(),
  ]);

  return {
    funnel,
    signupsByWeek: weeks,
    signupComparison: weekCompare,
    activityByDay: days,
    scoreDistribution: scores.buckets,
    averageTotalScore: scores.average,
    testUsage: usage,
    hardest: outliers.hardest,
    easiest: outliers.easiest,
    activeLast7,
    activeLast30,
    questionsAnsweredAllTime: answeredAgg._sum.questionsAnswered ?? 0,
    sessions,
  };
}
