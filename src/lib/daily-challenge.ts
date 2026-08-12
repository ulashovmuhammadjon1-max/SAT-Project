import { prisma } from "@/lib/prisma";

/**
 * The Daily Challenge — one question, the same one for every student, changing
 * at midnight UTC.
 *
 * It is deliberately *global*: the social hook is that everyone is arguing
 * about the same question today. Personalising it would make "did you get
 * today's one?" a meaningless question to ask a friend.
 *
 * ## Why there is no separate daily streak
 *
 * A daily-challenge streak would need to know which question was featured on
 * each past day. That mapping is derived from the current question pool, so
 * publishing a new test would silently renumber history and rewrite streaks
 * that students had already earned. Rather than store the mapping (a schema
 * change) or accept the corruption, completing the daily challenge feeds the
 * platform's existing study streak — answering it records a `QuestionAttempt`
 * and a `StudyActivity` row exactly like any other practice answer.
 *
 * So nothing here reads further back than today, and the "last 7 days" strip
 * comes from `StudyActivity`, which is immune to the pool changing.
 */

/** The UTC day key a challenge belongs to. */
export function challengeDay(now = new Date()): string {
  return now.toISOString().slice(0, 10);
}

/**
 * A small deterministic hash of the day key.
 *
 * FNV-1a: stable across processes and deploys, which a JS `hashCode`-style
 * accumulator using bit shifts on values above 2^31 is not guaranteed to be.
 * `>>> 0` keeps it unsigned so the modulo below can never come out negative —
 * a negative offset would throw at the query.
 */
export function dayHash(key: string): number {
  let h = 0x811c9dc5;
  for (let i = 0; i < key.length; i++) {
    h ^= key.charCodeAt(i);
    h = Math.imul(h, 0x01000193);
  }
  return h >>> 0;
}

export interface DailyChallenge {
  day: string;
  questionId: string;
  domain: string;
  skill: string;
  subject: "MATH" | "READING_WRITING";
  difficulty: string;
  /** Whether this student has already answered it today. */
  answeredToday: boolean;
  answeredCorrectly: boolean | null;
  /** Students who have answered today's question today. */
  solvedBy: number;
  /** Their accuracy on it, or null below the sample floor. */
  crowdAccuracyPct: number | null;
  /** Trailing seven days, oldest first: did they study that day? */
  week: { label: string; studied: boolean; isToday: boolean }[];
}

/** Below this, a crowd percentage is noise rather than information. */
const CROWD_FLOOR = 5;

/** Midnight UTC of the given day key. */
function dayStart(day: string): Date {
  return new Date(`${day}T00:00:00.000Z`);
}

export async function getDailyChallenge(userId: string): Promise<DailyChallenge | null> {
  const day = challengeDay();

  // Multiple choice only. A free-response question with no keypad context and
  // no partial credit is a poor single-question format, and the whole point of
  // a daily is that it is quick.
  const where = { isPublished: true, type: "MULTIPLE_CHOICE" as const };

  const total = await prisma.question.count({ where });
  if (total === 0) return null;

  const [question] = await prisma.question.findMany({
    where,
    // A stable sort key is essential: without one Postgres may return rows in
    // any order and the "question of the day" would change between requests.
    orderBy: { id: "asc" },
    skip: dayHash(day) % total,
    take: 1,
    select: {
      id: true,
      difficulty: true,
      domain: { select: { name: true, subject: true } },
      skill: { select: { name: true } },
    },
  });
  if (!question) return null;

  const since = dayStart(day);

  const [mine, crowd] = await Promise.all([
    prisma.questionAttempt.findFirst({
      where: { userId, questionId: question.id, createdAt: { gte: since } },
      orderBy: { createdAt: "asc" },
      select: { isCorrect: true },
    }),
    prisma.questionAttempt.groupBy({
      by: ["isCorrect"],
      where: { questionId: question.id, createdAt: { gte: since } },
      _count: { _all: true },
    }),
  ]);

  const solvedBy = crowd.reduce((sum, g) => sum + g._count._all, 0);
  const correct = crowd.find((g) => g.isCorrect)?._count._all ?? 0;

  return {
    day,
    questionId: question.id,
    domain: question.domain.name,
    subject: question.domain.subject,
    skill: question.skill.name,
    difficulty: question.difficulty,
    answeredToday: !!mine,
    answeredCorrectly: mine?.isCorrect ?? null,
    solvedBy,
    crowdAccuracyPct: solvedBy >= CROWD_FLOOR ? Math.round((correct / solvedBy) * 100) : null,
    week: await weekStrip(userId),
  };
}

/** Did they study on each of the last seven days? Oldest first. */
async function weekStrip(userId: string) {
  const start = new Date();
  start.setUTCHours(0, 0, 0, 0);
  start.setUTCDate(start.getUTCDate() - 6);

  const rows = await prisma.studyActivity.findMany({
    where: { userId, date: { gte: start }, questionsAnswered: { gt: 0 } },
    select: { date: true },
  });
  const studied = new Set(rows.map((r) => r.date.toISOString().slice(0, 10)));
  const todayKey = challengeDay();

  return Array.from({ length: 7 }, (_, i) => {
    const d = new Date(start);
    d.setUTCDate(start.getUTCDate() + i);
    const key = d.toISOString().slice(0, 10);
    return {
      label: d.toLocaleDateString(undefined, { weekday: "narrow", timeZone: "UTC" }),
      studied: studied.has(key),
      isToday: key === todayKey,
    };
  });
}
