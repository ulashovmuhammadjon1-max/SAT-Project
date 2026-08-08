/**
 * Backfill Question.difficulty from the module it sits in.
 *
 * Tests 1, 2 and 7-15 stamp each question to match its module — an EASY
 * module's questions are EASY, a HARD module's are HARD. Tests 3, 4, 5 and 6
 * were inserted by a script that hardcoded 'MEDIUM', so all of their Easy and
 * Hard module questions read MEDIUM. That is the field the Question Bank shows
 * as its difficulty badge and filters on, so those questions currently
 * misreport their level and cannot be found by a difficulty filter.
 *
 * Only rows that actually disagree with their module are touched, and only
 * where the module carries a real difficulty (EASY/HARD). A STANDARD module
 * legitimately holds MEDIUM questions and is left alone.
 *
 *   DATABASE_URL='postgresql://...' node backfill_difficulty.mjs [--apply]
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";

const APPLY = process.argv.includes("--apply");
const isLocal = /localhost|127\.0\.0\.1/.test(process.env.DATABASE_URL || "");
let sql, pgClient;
if (isLocal) {
  pgClient = new pg.Client({ connectionString: process.env.DATABASE_URL });
  await pgClient.connect();
  sql = async (strings, ...values) => {
    const text = strings.reduce((a, s, i) => a + s + (i < values.length ? `$${i + 1}` : ""), "");
    return (await pgClient.query(text, values)).rows;
  };
} else {
  sql = neon(process.env.DATABASE_URL);
}

// STANDARD modules map to MEDIUM questions; EASY and HARD map to themselves.
const before = await sql`
  SELECT t.title, m.difficulty AS module_difficulty, q.difficulty AS question_difficulty,
         COUNT(*)::int AS n
  FROM "Question" q
  JOIN "Module" m ON m.id = q."moduleId"
  JOIN "Test" t ON t.id = m."testId"
  WHERE m.difficulty IN ('EASY', 'HARD') AND q.difficulty <> m.difficulty::text::"QuestionDifficulty"
  GROUP BY t.title, m.difficulty, q.difficulty
  ORDER BY t.title, m.difficulty`;

if (!before.length) {
  console.log("nothing to backfill — every question already matches its module");
} else {
  console.table(before);
  const total = before.reduce((a, r) => a + r.n, 0);
  console.log(`${APPLY ? "updating" : "would update"} ${total} questions`);

  if (APPLY) {
    await sql`
      UPDATE "Question" q
      SET difficulty = m.difficulty::text::"QuestionDifficulty", "updatedAt" = now()
      FROM "Module" m
      WHERE m.id = q."moduleId"
        AND m.difficulty IN ('EASY', 'HARD')
        AND q.difficulty <> m.difficulty::text::"QuestionDifficulty"`;

    const after = await sql`
      SELECT COUNT(*)::int AS n FROM "Question" q
      JOIN "Module" m ON m.id = q."moduleId"
      WHERE m.difficulty IN ('EASY', 'HARD')
        AND q.difficulty <> m.difficulty::text::"QuestionDifficulty"`;
    console.log(`remaining mismatches: ${after[0].n}`);
  }
}

// Whole-bank picture, so the result is visible rather than asserted.
const summary = await sql`
  SELECT m.difficulty AS module, q.difficulty AS question, COUNT(*)::int AS n
  FROM "Question" q JOIN "Module" m ON m.id = q."moduleId"
  GROUP BY m.difficulty, q.difficulty ORDER BY m.difficulty, q.difficulty`;
console.table(summary);
if (pgClient) await pgClient.end();
