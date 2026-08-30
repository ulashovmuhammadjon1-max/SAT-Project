/**
 * Step 3 of 3: write the typeset AP questions back.
 *
 *   PROD_URL='postgresql://...' node scripts/ap-latex-apply.mjs patch.json [--apply]
 *
 * Without --apply it reports what would change and writes nothing.
 *
 * Every row is re-read inside the update and guarded: the update only fires
 * when the stored `correctIndex` still matches what the patch was built from,
 * and it never writes `correctIndex` itself. CLAUDE.md's rule from the SAT
 * fixes applies here too -- assert a distinctive property of the row you
 * fetched BEFORE writing to it, not after.
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync } from "fs";

const file = process.argv[2];
const apply = process.argv.includes("--apply");
if (!file) {
  console.error("usage: ap-latex-apply.mjs <patch.json> [--apply]");
  process.exit(1);
}
const sql = neon(process.env.PROD_URL || process.env.DATABASE_URL);
const patch = JSON.parse(readFileSync(file, "utf8"));

// Batched, because one HTTP round trip per question over 5,266 questions is
// slow enough that a half-finished run becomes the likely outcome, and a
// half-converted bank is the one state worse than an unconverted one.
const BATCH = 250;
let written = 0;
let bad = 0;

for (let i = 0; i < patch.length; i += BATCH) {
  const chunk = patch.slice(i, i + BATCH);
  const payload = JSON.stringify(
    chunk.map((p) => ({
      id: p.id,
      stem: p.stem,
      choices: JSON.stringify(p.choices),
      explanation: p.explanation,
      table: p.table ? JSON.stringify(p.table) : null,
      correctIndex: p.correctIndex,
      n: p.choices.length,
    })),
  );

  if (!apply) {
    // A dry run reads the guard; it does not execute the write.
    const rows = await sql.query(
      `SELECT p.id
         FROM jsonb_to_recordset($1::jsonb)
              AS p(id text, "correctIndex" int, n int)
         LEFT JOIN "ApQuestion" q ON q.id = p.id
        WHERE q.id IS NULL
           OR q."correctIndex" <> p."correctIndex"
           OR jsonb_array_length(q."choicesJson"::jsonb) <> p.n`,
      [payload],
    );
    for (const r of rows) console.error(`GUARD WOULD FAIL: ${r.id}`);
    bad += rows.length;
    continue;
  }

  const rows = await sql.query(
    `UPDATE "ApQuestion" q
        SET stem = p.stem,
            "choicesJson" = p.choices,
            explanation = p.explanation,
            "tableJson" = p."table"
       FROM jsonb_to_recordset($1::jsonb)
            AS p(id text, stem text, choices text, explanation text,
                 "table" text, "correctIndex" int, n int)
      WHERE q.id = p.id
        AND q."correctIndex" = p."correctIndex"
        AND jsonb_array_length(q."choicesJson"::jsonb) = p.n
      RETURNING q.id`,
    [payload],
  );
  written += rows.length;
  if (rows.length !== chunk.length) {
    console.error(
      `GUARD FAILED: batch at ${i} wrote ${rows.length} of ${chunk.length}`,
    );
    process.exit(1);
  }
  process.stdout.write(`\r${written}/${patch.length}`);
}

if (!apply) {
  console.log(
    `dry run: ${patch.length} questions would be updated, ${bad} would fail the guard`,
  );
  process.exit(bad ? 1 : 0);
}
console.log(`\nupdated ${written} of ${patch.length} questions`);
