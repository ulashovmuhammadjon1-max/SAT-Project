import { prisma } from "@/lib/prisma";

/**
 * Everything known about one student, for the admin profile page.
 *
 * The list view answers "who should I look at"; this answers "what is going on
 * with this person" — the onboarding profile they filled in, every test they
 * have taken and scored, where their accuracy is weak by domain, when they
 * actually study, and what they have booked.
 *
 * Two conventions carried over from `statistics.ts`: counting happens in SQL
 * rather than by pulling rows into memory, and a section with no data returns
 * an empty array so the page can say "none yet" instead of rendering a zero
 * that reads like a measurement.
 */

export interface ProfileIdentity {
  id: string;
  name: string | null;
  email: string;
  image: string | null;
  emailVerified: Date | null;
  joinedAt: Date;
  /**
   * Last day this student actually studied.
   *
   * Taken from `StudyActivity`, the same source the student list uses — not
   * `User.lastActiveDate`, which is maintained by the streak logic and can sit
   * null on an account that has study rows. The two disagreeing made this page
   * say "never studied" beside a count of thirteen questions answered.
   */
  lastActiveDate: Date | null;
  currentStreak: number;
  longestStreak: number;
  coinBalance: number;
  termsAcceptedAt: Date | null;
  termsVersion: string | null;
}

export interface ProfileOnboarding {
  onboardedAt: Date | null;
  goal: string | null;
  gradeLevel: string | null;
  countryCode: string | null;
  currentScore: number | null;
  targetScore: number | null;
  satDate: Date | null;
  dreamUniversities: string[];
  strongestSection: string | null;
  weakestArea: string | null;
  studyMinutesPerDay: number | null;
  dailyGoalType: string | null;
  dailyGoalValue: number | null;
}

export interface ProfileTotals {
  questionsAnswered: number;
  daysActive: number;
  minutesStudied: number;
  testsStarted: number;
  testsCompleted: number;
  /** Submitted attempts that actually carry a total — see `bestScore`. */
  scoredCount: number;
  bestScore: number | null;
  latestScore: number | null;
  firstScore: number | null;
  qbAnswered: number;
  qbAccuracyPct: number | null;
}

export interface ProfileAttempt {
  id: string;
  testTitle: string;
  status: string;
  startedAt: Date;
  submittedAt: Date | null;
  totalScaledScore: number | null;
  rwScaledScore: number | null;
  mathScaledScore: number | null;
  /** Answered out of total, so an abandoned attempt is visibly partial. */
  answered: number;
  questionCount: number;
}

export interface ProfileScorePoint {
  label: string;
  total: number;
  rw: number | null;
  math: number | null;
}

export interface ProfileDomainRow {
  code: string;
  name: string;
  subject: string;
  attempted: number;
  correct: number;
  accuracyPct: number;
}

export interface ProfileActivityPoint {
  label: string;
  value: number;
}

export interface ProfileBooking {
  id: string;
  status: string;
  sessionType: string;
  startsAt: Date | null;
  coinCost: number;
  notes: string | null;
}

export interface ProfileReferrals {
  code: string | null;
  referredByName: string | null;
  referredByEmail: string | null;
  referredCount: number;
}

export interface ProfileVocab {
  wordsStarted: number;
  wordsMastered: number;
  setsPassed: number;
  setsAttempted: number;
}

export interface StudentProfile {
  identity: ProfileIdentity;
  onboarding: ProfileOnboarding;
  totals: ProfileTotals;
  attempts: ProfileAttempt[];
  scoreTrend: ProfileScorePoint[];
  domains: ProfileDomainRow[];
  activity: ProfileActivityPoint[];
  bookings: ProfileBooking[];
  referrals: ProfileReferrals;
  vocab: ProfileVocab;
}

const asNumber = (v: unknown): number => (v == null ? 0 : Number(v));

/** ISO date key in UTC, matching how `StudyActivity.date` is stored. */
function dayKey(d: Date): string {
  return d.toISOString().slice(0, 10);
}

/**
 * Accuracy by domain, pooling test answers and Question Bank answers.
 *
 * `Response.isCorrect` is nullable and null means *not graded* — an unanswered
 * question in a module the student walked away from. Those rows are excluded
 * rather than counted as wrong, which is the same reason the student list
 * shows Question Bank accuracy only. Here both sources can be pooled safely
 * because the null filter does the work explicitly.
 */
async function domainAccuracy(userId: string): Promise<ProfileDomainRow[]> {
  const rows = await prisma.$queryRaw<
    { code: string; name: string; subject: string; attempted: bigint; correct: bigint }[]
  >`
    WITH answers AS (
      SELECT q."domainId" AS domain_id, r."isCorrect" AS is_correct
        FROM "Response" r
        JOIN "Attempt" a  ON a.id = r."attemptId"
        JOIN "Question" q ON q.id = r."questionId"
       WHERE a."userId" = ${userId} AND r."isCorrect" IS NOT NULL
      UNION ALL
      SELECT q."domainId", qa."isCorrect"
        FROM "QuestionAttempt" qa
        JOIN "Question" q ON q.id = qa."questionId"
       WHERE qa."userId" = ${userId}
    )
    SELECT d.code                                        AS code,
           d.name                                        AS name,
           d.subject::text                                AS subject,
           COUNT(*)::bigint                              AS attempted,
           COUNT(*) FILTER (WHERE answers.is_correct)::bigint AS correct
      FROM answers
      JOIN "Domain" d ON d.id = answers.domain_id
     GROUP BY d.code, d.name, d.subject
     ORDER BY d.subject, d.code
  `;

  return rows.map((r) => {
    const attempted = asNumber(r.attempted);
    return {
      code: r.code,
      name: r.name,
      subject: r.subject,
      attempted,
      correct: asNumber(r.correct),
      accuracyPct: attempted ? Math.round((asNumber(r.correct) / attempted) * 100) : 0,
    };
  });
}

/**
 * Questions answered per day over the trailing window.
 *
 * Days with no row are filled with zero. Without that the chart silently
 * closes the gaps and a student who studied twice a month looks continuous.
 */
async function activitySeries(userId: string, days: number): Promise<ProfileActivityPoint[]> {
  const since = new Date();
  since.setUTCHours(0, 0, 0, 0);
  since.setUTCDate(since.getUTCDate() - (days - 1));

  const rows = await prisma.studyActivity.findMany({
    where: { userId, date: { gte: since } },
    select: { date: true, questionsAnswered: true },
  });
  const byDay = new Map(rows.map((r) => [dayKey(r.date), r.questionsAnswered]));

  const out: ProfileActivityPoint[] = [];
  for (let i = 0; i < days; i++) {
    const d = new Date(since);
    d.setUTCDate(since.getUTCDate() + i);
    const key = dayKey(d);
    out.push({
      label: d.toLocaleDateString(undefined, { day: "numeric", month: "short", timeZone: "UTC" }),
      value: byDay.get(key) ?? 0,
    });
  }
  return out;
}

/**
 * One student's full profile, or null when the id matches no student.
 *
 * Returns null for a non-STUDENT account too: this page is for looking at
 * learners, and an admin row here would show nothing but empty sections.
 */
export async function getStudentProfile(userId: string): Promise<StudentProfile | null> {
  const user = await prisma.user.findUnique({
    where: { id: userId },
    include: {
      referredBy: { select: { name: true, email: true } },
      _count: { select: { referredAccounts: true } },
    },
  });
  if (!user || user.role !== "STUDENT") return null;

  const [
    attemptRows,
    studyTotals,
    qbTotals,
    daysActive,
    domains,
    activity,
    bookings,
    vocabWords,
    vocabMastered,
    vocabSets,
    vocabSetsPassed,
  ] = await Promise.all([
    prisma.attempt.findMany({
      where: { userId },
      orderBy: { startedAt: "desc" },
      select: {
        id: true,
        status: true,
        startedAt: true,
        submittedAt: true,
        totalScaledScore: true,
        rwScaledScore: true,
        mathScaledScore: true,
        test: { select: { title: true, _count: { select: { modules: true } } } },
        _count: { select: { responses: true } },
        // Answered means a graded row exists; an abandoned module leaves
        // ungraded rows behind and they must not read as progress.
        responses: { where: { isCorrect: { not: null } }, select: { id: true } },
        moduleAttempts: { select: { module: { select: { _count: { select: { questions: true } } } } } },
      },
    }),
    prisma.studyActivity.aggregate({
      where: { userId },
      _sum: { questionsAnswered: true, minutesStudied: true },
      _max: { date: true },
      _count: { _all: true },
    }),
    prisma.questionAttempt.groupBy({
      by: ["isCorrect"],
      where: { userId },
      _count: { _all: true },
    }),
    // Days they actually answered something. A StudyActivity row can exist
    // with only vocabulary reviewed on it, and the student list counts days
    // the same way — the two figures have to agree.
    prisma.studyActivity.count({ where: { userId, questionsAnswered: { gt: 0 } } }),
    domainAccuracy(userId),
    activitySeries(userId, 60),
    prisma.booking.findMany({
      where: { userId },
      orderBy: { createdAt: "desc" },
      take: 25,
      select: {
        id: true,
        status: true,
        sessionType: true,
        coinCost: true,
        notes: true,
        slot: { select: { startsAt: true } },
      },
    }),
    prisma.vocabProgress.count({ where: { userId } }),
    prisma.vocabProgress.count({ where: { userId, status: "MASTERED" } }),
    prisma.vocabDeckProgress.count({ where: { userId } }),
    prisma.vocabDeckProgress.count({ where: { userId, passed: true } }),
  ]);

  const attempts: ProfileAttempt[] = attemptRows.map((a) => ({
    id: a.id,
    testTitle: a.test.title,
    status: a.status,
    startedAt: a.startedAt,
    submittedAt: a.submittedAt,
    totalScaledScore: a.totalScaledScore,
    rwScaledScore: a.rwScaledScore,
    mathScaledScore: a.mathScaledScore,
    answered: a.responses.length,
    // Only the modules actually reached, not the whole test: an adaptive test
    // has six modules on paper but a student sits four of them.
    questionCount: a.moduleAttempts.reduce((sum, ma) => sum + ma.module._count.questions, 0),
  }));

  const scored = attempts
    .filter((a) => a.totalScaledScore != null && a.submittedAt != null)
    .sort((x, y) => x.submittedAt!.getTime() - y.submittedAt!.getTime());

  const scoreTrend: ProfileScorePoint[] = scored.map((a) => ({
    label: a.testTitle,
    total: a.totalScaledScore!,
    rw: a.rwScaledScore,
    math: a.mathScaledScore,
  }));

  const qbCorrect = qbTotals.find((g) => g.isCorrect)?._count._all ?? 0;
  const qbAnswered = qbTotals.reduce((sum, g) => sum + g._count._all, 0);

  return {
    identity: {
      id: user.id,
      name: user.name,
      email: user.email,
      image: user.image,
      emailVerified: user.emailVerified,
      joinedAt: user.createdAt,
      lastActiveDate: studyTotals._max.date ?? user.lastActiveDate,
      currentStreak: user.currentStreak,
      longestStreak: user.longestStreak,
      coinBalance: user.coinBalance,
      termsAcceptedAt: user.termsAcceptedAt,
      termsVersion: user.termsVersion,
    },
    onboarding: {
      onboardedAt: user.onboardedAt,
      goal: user.onboardingGoal,
      gradeLevel: user.gradeLevel,
      countryCode: user.countryCode,
      currentScore: user.currentScore,
      targetScore: user.targetScore,
      satDate: user.satDate,
      dreamUniversities: user.dreamUniversities,
      strongestSection: user.strongestSection,
      weakestArea: user.weakestArea,
      studyMinutesPerDay: user.studyMinutesPerDay,
      dailyGoalType: user.dailyGoalType,
      dailyGoalValue: user.dailyGoalValue,
    },
    totals: {
      questionsAnswered: studyTotals._sum.questionsAnswered ?? 0,
      minutesStudied: studyTotals._sum.minutesStudied ?? 0,
      daysActive,
      testsStarted: attempts.length,
      testsCompleted: attempts.filter((a) => a.status === "SUBMITTED").length,
      scoredCount: scored.length,
      bestScore: scored.length ? Math.max(...scored.map((a) => a.totalScaledScore!)) : null,
      latestScore: scored.length ? scored[scored.length - 1].totalScaledScore : null,
      firstScore: scored.length ? scored[0].totalScaledScore : null,
      qbAnswered,
      qbAccuracyPct: qbAnswered ? Math.round((qbCorrect / qbAnswered) * 100) : null,
    },
    attempts,
    scoreTrend,
    domains,
    activity,
    bookings: bookings.map((b) => ({
      id: b.id,
      status: b.status,
      sessionType: b.sessionType,
      startsAt: b.slot?.startsAt ?? null,
      coinCost: b.coinCost,
      notes: b.notes,
    })),
    referrals: {
      code: user.referralCode,
      referredByName: user.referredBy?.name ?? null,
      referredByEmail: user.referredBy?.email ?? null,
      referredCount: user._count.referredAccounts,
    },
    vocab: {
      wordsStarted: vocabWords,
      wordsMastered: vocabMastered,
      setsAttempted: vocabSets,
      setsPassed: vocabSetsPassed,
    },
  };
}
