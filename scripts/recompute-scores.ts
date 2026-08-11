/**
 * Rescore every submitted attempt with the current conversion table.
 *
 * Needed because scores are stored, not derived on read: attempts submitted
 * before the scoring fix carry values the SAT cannot award (a student reported
 * a 336) and section scores that were averaged across modules rather than
 * converted once from the combined raw score.
 *
 * Safe to re-run — it recomputes from the stored raw counts every time and
 * writes only where the result differs.
 *
 *   npx tsx scripts/recompute-scores.ts --dry-run   # report, change nothing
 *   npx tsx scripts/recompute-scores.ts             # apply
 *
 * Uses whatever `DATABASE_URL` is set, so point it at production deliberately,
 * and never write the connection string into a file:
 *
 *   DATABASE_URL='postgresql://...' npx tsx scripts/recompute-scores.ts --dry-run
 *
 * Works against both databases. The sandbox this runs in blocks raw Postgres
 * (5432) and allows only outbound HTTPS, so a remote host goes over Neon's HTTP
 * API while localhost uses a normal TCP client — the same split `insert_test.mjs`
 * makes, for the same reason.
 */

import { neon } from "@neondatabase/serverless";
import pg from "pg";

import { estimateScaledScore, estimateTotalScore, sectionScoreForRaw } from "../src/lib/scoring/estimate";

const dryRun = process.argv.includes("--dry-run");
const url = process.env.DATABASE_URL;

if (!url) {
  console.error("Set DATABASE_URL.");
  process.exit(1);
}

type Row = Record<string, unknown>;
type Query = (text: string, values?: unknown[]) => Promise<Row[]>;

/** Connecting happens inside a function because tsx compiles this to CommonJS,
 *  where top-level await is not available. */
async function connect(): Promise<{ query: Query; close: () => Promise<void> }> {
  if (/localhost|127\.0\.0\.1/.test(url!)) {
    const client = new pg.Client({ connectionString: url });
    await client.connect();
    console.log("driver: pg (local)");
    return {
      query: async (text, values = []) => (await client.query(text, values)).rows,
      close: async () => {
        await client.end();
      },
    };
  }
  const sql = neon(url!);
  console.log("driver: neon HTTP (production)");
  return {
    query: async (text, values = []) => (await sql.query(text, values)) as Row[],
    close: async () => {},
  };
}

interface ModuleRow {
  id: string;
  correctCount: number | null;
  totalCount: number | null;
  scaledScore: number | null;
  submittedAt: Date | null;
  subject: "READING_WRITING" | "MATH";
}

interface AttemptRow {
  id: string;
  rw: number | null;
  math: number | null;
  total: number | null;
  modules: ModuleRow[];
}

const num = (v: unknown): number | null => (v === null || v === undefined ? null : Number(v));

async function main() {
  const { query, close } = await connect();
  try {
  const rows = await query(`
    SELECT a.id            AS attempt_id,
           a."rwScaledScore"    AS rw,
           a."mathScaledScore"  AS math,
           a."totalScaledScore" AS total,
           ma.id           AS module_attempt_id,
           ma."correctCount"    AS correct_count,
           ma."totalCount"      AS total_count,
           ma."scaledScore"     AS module_scaled,
           ma."submittedAt"     AS module_submitted,
           m.subject       AS subject
      FROM "Attempt" a
      JOIN "ModuleAttempt" ma ON ma."attemptId" = a.id
      JOIN "Module" m         ON m.id = ma."moduleId"
     WHERE a.status = 'SUBMITTED'
     ORDER BY a.id
  `);

  const attempts = new Map<string, AttemptRow>();
  for (const r of rows) {
    const id = String(r.attempt_id);
    if (!attempts.has(id)) {
      attempts.set(id, { id, rw: num(r.rw), math: num(r.math), total: num(r.total), modules: [] });
    }
    attempts.get(id)!.modules.push({
      id: String(r.module_attempt_id),
      correctCount: num(r.correct_count),
      totalCount: num(r.total_count),
      scaledScore: num(r.module_scaled),
      submittedAt: r.module_submitted as Date | null,
      subject: r.subject as ModuleRow["subject"],
    });
  }

  console.log(`${attempts.size} submitted attempt${attempts.size === 1 ? "" : "s"} to check.`);

  let attemptsChanged = 0;
  let modulesChanged = 0;
  let illegalBefore = 0;

  for (const attempt of attempts.values()) {
    const taken = attempt.modules.filter((m) => m.submittedAt != null);

    const sectionScore = (subject: ModuleRow["subject"]): number | null => {
      const forSubject = taken.filter((m) => m.subject === subject);
      if (!forSubject.length) return null;
      const rawCorrect = forSubject.reduce((sum, m) => sum + (m.correctCount ?? 0), 0);
      const questionCount = forSubject.reduce((sum, m) => sum + (m.totalCount ?? 0), 0);
      if (questionCount <= 0) return null;
      return sectionScoreForRaw(subject, rawCorrect, questionCount);
    };

    const rw = sectionScore("READING_WRITING");
    const math = sectionScore("MATH");
    const total = estimateTotalScore(rw, math);

    for (const previous of [attempt.rw, attempt.math, attempt.total]) {
      if (previous != null && previous % 10 !== 0) illegalBefore += 1;
    }

    if (rw !== attempt.rw || math !== attempt.math || total !== attempt.total) {
      attemptsChanged += 1;
      console.log(
        `  attempt ${attempt.id}: ` +
          `R&W ${attempt.rw ?? "—"}→${rw ?? "—"}, ` +
          `Math ${attempt.math ?? "—"}→${math ?? "—"}, ` +
          `Total ${attempt.total ?? "—"}→${total ?? "—"}`,
      );
      if (!dryRun) {
        await query(
          `UPDATE "Attempt"
              SET "rwScaledScore" = $1, "mathScaledScore" = $2, "totalScaledScore" = $3, "updatedAt" = now()
            WHERE id = $4`,
          [rw, math, total, attempt.id],
        );
      }
    }

    // The per-module figure is indicative only and never summed into a section
    // score, but it is stored and shown, so it should be a legal score too.
    for (const moduleAttempt of taken) {
      const count = moduleAttempt.totalCount ?? 0;
      if (count <= 0) continue;
      const indicative = estimateScaledScore(
        ((moduleAttempt.correctCount ?? 0) / count) * 100,
        moduleAttempt.subject,
      );
      if (indicative !== moduleAttempt.scaledScore) {
        modulesChanged += 1;
        if (!dryRun) {
          await query(`UPDATE "ModuleAttempt" SET "scaledScore" = $1 WHERE id = $2`, [
            indicative,
            moduleAttempt.id,
          ]);
        }
      }
    }
  }

  console.log(
    `\n${dryRun ? "Would update" : "Updated"} ${attemptsChanged} attempt${attemptsChanged === 1 ? "" : "s"} ` +
      `and ${modulesChanged} module score${modulesChanged === 1 ? "" : "s"}.`,
  );
  if (illegalBefore) {
    console.log(
      `${illegalBefore} stored score${illegalBefore === 1 ? " was" : "s were"} not a multiple of 10 — ` +
        `the defect a student reported.`,
    );
  }
  } finally {
    await close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
