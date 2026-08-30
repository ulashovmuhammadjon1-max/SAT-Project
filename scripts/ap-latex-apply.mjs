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

let written = 0;
for (const p of patch) {
  if (!apply) {
    // A dry run reads the guard, it does not execute the write.
    const [row] = await sql.query(
      `SELECT "correctIndex", jsonb_array_length("choicesJson"::jsonb) AS n
         FROM "ApQuestion" WHERE id = $1`,
      [p.id],
    );
    if (!row) console.error(`MISSING: ${p.id}`);
    else if (row.correctIndex !== p.correctIndex || row.n !== p.choices.length)
      console.error(`GUARD WOULD FAIL: ${p.id}`);
    continue;
  }
  const res = await sql.query(
    `UPDATE "ApQuestion"
        SET stem = $2, "choicesJson" = $3, explanation = $4, "tableJson" = $5
      WHERE id = $1
        AND "correctIndex" = $6
        AND jsonb_array_length("choicesJson"::jsonb) = $7
      RETURNING id`,
    [
      p.id, p.stem, JSON.stringify(p.choices), p.explanation,
      p.table ? JSON.stringify(p.table) : null,
      p.correctIndex, p.choices.length,
    ],
  );
  if (res.length === 1) written++;
  else {
    console.error(`GUARD FAILED, not updated: ${p.id}`);
    process.exit(1);
  }
}

if (!apply) {
  console.log(`dry run: ${patch.length} questions would be updated (pass --apply)`);
  process.exit(0);
}
console.log(`updated ${written} of ${patch.length} questions`);
