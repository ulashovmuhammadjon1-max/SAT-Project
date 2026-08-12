import { prisma } from "@/lib/prisma";

/**
 * Leaderboards, computed from existing activity rows.
 *
 * Three boards rather than one, because a single ranking always rewards the
 * same person. Questions-this-week is winnable by anyone who shows up;
 * best-score rewards the strongest test-taker; streak rewards the most
 * consistent. A student who cannot place on one can place on another, which
 * is the whole point of running more than one board.
 *
 * ## On names
 *
 * A board shows a display name, never an email address — an email is contact
 * information and a leaderboard is a public page inside the app. Names are
 * shortened to a first name plus a last initial, so a full legal name is not
 * broadcast to every other student.
 */

export type LeaderboardKind = "weekly" | "score" | "streak";

export interface LeaderboardRow {
  rank: number;
  userId: string;
  displayName: string;
  value: number;
  /** Secondary figure shown beside the value, already formatted. */
  detail: string | null;
  isMe: boolean;
}

export interface LeaderboardResult {
  kind: LeaderboardKind;
  rows: LeaderboardRow[];
  /** The signed-in student's row when they fall outside the visible top N. */
  me: LeaderboardRow | null;
  /** Students with a non-zero value on this board — the real field size. */
  participants: number;
}

/**
 * "Dilnoza Karimova" → "Dilnoza K." — enough to recognise yourself and your
 * friends, not enough to be a directory of everyone's full name.
 */
export function shortName(name: string | null, fallback = "Anonymous"): string {
  const trimmed = (name ?? "").trim();
  if (!trimmed) return fallback;
  const parts = trimmed.split(/\s+/);
  if (parts.length === 1) return parts[0];
  const last = parts[parts.length - 1];
  return `${parts.slice(0, -1).join(" ")} ${last[0].toUpperCase()}.`;
}

/** Monday 00:00 UTC of the current week. */
export function weekStart(now = new Date()): Date {
  const d = new Date(now);
  d.setUTCHours(0, 0, 0, 0);
  // getUTCDay() is 0 for Sunday, so Sunday must go back six days, not zero.
  const back = (d.getUTCDay() + 6) % 7;
  d.setUTCDate(d.getUTCDate() - back);
  return d;
}

const asNumber = (v: unknown): number => (v == null ? 0 : Number(v));

interface RawRow {
  id: string;
  name: string | null;
  value: bigint | number | null;
  detail: bigint | number | null;
}

/**
 * Rank rows densely: equal values share a rank, and the next distinct value
 * takes the position after the tie. Two students on 340 questions are both
 * 2nd and the next is 3rd — the alternative silently ranks one above the
 * other on row order, which looks like a bug to whoever comes second.
 */
function rank(rows: RawRow[], userId: string, format: (r: RawRow) => string | null) {
  let lastValue: number | null = null;
  let lastRank = 0;
  return rows.map((r, i) => {
    const value = asNumber(r.value);
    if (value !== lastValue) {
      lastRank = i + 1;
      lastValue = value;
    }
    return {
      rank: lastRank,
      userId: r.id,
      displayName: shortName(r.name),
      value,
      detail: format(r),
      isMe: r.id === userId,
    };
  });
}

/**
 * One board.
 *
 * `limit` bounds the visible table; the signed-in student's own row is looked
 * up separately and returned as `me` when they rank below it, so the page can
 * always show them where they stand. A board that hides you unless you are in
 * the top ten gives the people who most need motivating nothing to look at.
 */
export async function getLeaderboard(
  kind: LeaderboardKind,
  userId: string,
  limit = 25
): Promise<LeaderboardResult> {
  const since = weekStart();

  let rows: RawRow[];
  let format: (r: RawRow) => string | null;

  if (kind === "weekly") {
    rows = await prisma.$queryRaw<RawRow[]>`
      SELECT u.id, u.name,
             COALESCE(SUM(sa."questionsAnswered"), 0)::bigint AS value,
             COUNT(sa.id)::bigint                             AS detail
        FROM "User" u
        JOIN "StudyActivity" sa ON sa."userId" = u.id AND sa.date >= ${since}
       WHERE u.role = 'STUDENT'
       GROUP BY u.id, u.name
      HAVING COALESCE(SUM(sa."questionsAnswered"), 0) > 0
       ORDER BY value DESC, u."createdAt" ASC
    `;
    format = (r) => {
      const days = asNumber(r.detail);
      return `${days} ${days === 1 ? "day" : "days"}`;
    };
  } else if (kind === "score") {
    rows = await prisma.$queryRaw<RawRow[]>`
      SELECT u.id, u.name,
             MAX(a."totalScaledScore")                        AS value,
             COUNT(a.id) FILTER (WHERE a.status = 'SUBMITTED')::bigint AS detail
        FROM "User" u
        JOIN "Attempt" a ON a."userId" = u.id
       WHERE u.role = 'STUDENT'
         AND a.status = 'SUBMITTED'
         AND a."totalScaledScore" IS NOT NULL
       GROUP BY u.id, u.name
       ORDER BY value DESC, u."createdAt" ASC
    `;
    format = (r) => {
      const tests = asNumber(r.detail);
      return `${tests} ${tests === 1 ? "test" : "tests"}`;
    };
  } else {
    rows = await prisma.$queryRaw<RawRow[]>`
      SELECT u.id, u.name,
             u."currentStreak"::bigint AS value,
             u."longestStreak"::bigint AS detail
        FROM "User" u
       WHERE u.role = 'STUDENT' AND u."currentStreak" > 0
       ORDER BY value DESC, u."createdAt" ASC
    `;
    format = (r) => `best ${asNumber(r.detail)}d`;
  }

  const ranked = rank(rows, userId, format);
  const visible = ranked.slice(0, limit);
  const mine = ranked.find((r) => r.isMe) ?? null;

  return {
    kind,
    rows: visible,
    // Only when they are not already on screen — otherwise the page would
    // render the same student twice.
    me: mine && !visible.some((r) => r.isMe) ? mine : null,
    participants: ranked.length,
  };
}

export const LEADERBOARD_LABELS: Record<LeaderboardKind, { title: string; unit: string; blurb: string }> = {
  weekly: {
    title: "This week",
    unit: "questions",
    blurb: "Questions answered since Monday. Resets every week, so everyone starts level.",
  },
  score: {
    title: "Best score",
    unit: "points",
    blurb: "Highest score on any completed practice test.",
  },
  streak: {
    title: "Current streak",
    unit: "days",
    blurb: "Consecutive days studied, right now. Miss a day and it resets.",
  },
};
