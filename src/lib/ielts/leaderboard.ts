import { prisma } from "@/lib/prisma";
import { shortName, weekStart } from "@/lib/leaderboard";

/**
 * IELTS leaderboards.
 *
 * Separate from `lib/leaderboard.ts` on purpose: the SAT boards rank on a 1600
 * scale and on questions answered, neither of which exists on this side. The
 * two share only `shortName` and `weekStart`, which is exactly the amount of
 * sharing that survives the two exams diverging.
 *
 * Three boards, for the same reason the SAT has three. A band board rewards the
 * strongest writer, who will be the same person every week; the effort board is
 * winnable by anyone who submits work. A student who cannot place on one can
 * place on another.
 *
 * ## On names and privacy
 *
 * A board shows a first name and last initial, never an email address, and
 * never the text of anyone's essay. Bands shown are reviewed bands only — an
 * unreviewed submission is not a score and ranking on it would be inventing one.
 */

export type IeltsBoardKind = "writing" | "speaking" | "effort";

export interface IeltsLeaderboardRow {
  rank: number;
  userId: string;
  displayName: string;
  /** A band for the band boards; a count for the effort board. */
  value: number;
  detail: string | null;
  isMe: boolean;
}

export interface IeltsLeaderboardResult {
  kind: IeltsBoardKind;
  rows: IeltsLeaderboardRow[];
  /** The signed-in student's row when they fall outside the visible top N. */
  me: IeltsLeaderboardRow | null;
  participants: number;
}

const asNumber = (v: unknown): number => (v == null ? 0 : Number(v));

interface RawRow {
  id: string;
  name: string | null;
  value: number | bigint | null;
  detail: number | bigint | null;
}

/**
 * Dense ranking: equal values share a rank and the next distinct value takes
 * the position after the tie. Two students on band 7 are both 2nd. Bands tie
 * far more often than SAT scores do — there are 19 possible values, not 1,001 —
 * so ranking on row order would look arbitrary to most of the board.
 */
function rank(
  rows: RawRow[],
  userId: string,
  format: (r: RawRow) => string | null
): IeltsLeaderboardRow[] {
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

export async function getIeltsLeaderboard(
  kind: IeltsBoardKind,
  userId: string,
  limit = 25
): Promise<IeltsLeaderboardResult> {
  let rows: RawRow[];
  let format: (r: RawRow) => string | null;

  if (kind === "writing") {
    // The best reviewed task band, and how many reviewed tasks it came from —
    // so a band 8 earned once reads differently from a band 8 earned five
    // times, without either being hidden.
    rows = await prisma.$queryRaw<RawRow[]>`
      SELECT u.id, u.name,
             MAX(r."overallBand")  AS value,
             COUNT(r.id)::bigint   AS detail
        FROM "User" u
        JOIN "IeltsWritingSubmission" s ON s."userId" = u.id
        JOIN "IeltsWritingReview" r     ON r."submissionId" = s.id
       WHERE u.role = 'STUDENT'
       GROUP BY u.id, u.name
       ORDER BY value DESC, u."createdAt" ASC
    `;
    format = (r) => {
      const n = asNumber(r.detail);
      return `${n} reviewed ${n === 1 ? "task" : "tasks"}`;
    };
  } else if (kind === "speaking") {
    rows = await prisma.$queryRaw<RawRow[]>`
      SELECT u.id, u.name,
             MAX(r."overallBand")  AS value,
             COUNT(r.id)::bigint   AS detail
        FROM "User" u
        JOIN "IeltsSpeakingSubmission" s ON s."userId" = u.id
        JOIN "IeltsSpeakingReview" r     ON r."submissionId" = s.id
       WHERE u.role = 'STUDENT'
       GROUP BY u.id, u.name
       ORDER BY value DESC, u."createdAt" ASC
    `;
    format = (r) => {
      const n = asNumber(r.detail);
      return `${n} reviewed ${n === 1 ? "interview" : "interviews"}`;
    };
  } else {
    // Work SENT this week, from both skills. A UNION rather than two joins:
    // joining both submission tables to User multiplies the rows and would
    // credit a student who wrote two essays and one interview with six.
    const since = weekStart();
    rows = await prisma.$queryRaw<RawRow[]>`
      WITH sent AS (
        SELECT "userId", "submittedAt" FROM "IeltsWritingSubmission"
         WHERE status <> 'PENDING' AND "submittedAt" >= ${since}
        UNION ALL
        SELECT "userId", "submittedAt" FROM "IeltsSpeakingSubmission"
         WHERE status <> 'PENDING' AND "submittedAt" >= ${since}
      )
      SELECT u.id, u.name,
             COUNT(sent."userId")::bigint AS value,
             NULL::bigint                 AS detail
        FROM "User" u
        JOIN sent ON sent."userId" = u.id
       WHERE u.role = 'STUDENT'
       GROUP BY u.id, u.name
      HAVING COUNT(sent."userId") > 0
       ORDER BY value DESC, u."createdAt" ASC
    `;
    format = () => null;
  }

  const ranked = rank(rows, userId, format);
  const visible = ranked.slice(0, limit);
  const mine = ranked.find((r) => r.isMe) ?? null;

  return {
    kind,
    rows: visible,
    // Only when they are not already on screen, or the page renders the same
    // student twice.
    me: mine && !visible.some((r) => r.isMe) ? mine : null,
    participants: ranked.length,
  };
}

export const IELTS_BOARD_LABELS: Record<
  IeltsBoardKind,
  { title: string; unit: string; blurb: string; empty: string }
> = {
  writing: {
    title: "Writing band",
    unit: "band",
    blurb: "Your highest reviewed Writing task band. Only reviewed work counts.",
    empty: "No Writing task has been reviewed yet. Submit one and the board is yours.",
  },
  speaking: {
    title: "Speaking band",
    unit: "band",
    blurb: "Your highest reviewed Speaking band. Only reviewed work counts.",
    empty: "No Speaking test has been reviewed yet. Record one and the board is yours.",
  },
  effort: {
    title: "This week",
    unit: "submitted",
    blurb: "Writing tasks and Speaking tests sent for review since Monday. Resets every week, so everyone starts level.",
    empty: "Nobody has submitted work yet this week. Send one and you are first.",
  },
};
