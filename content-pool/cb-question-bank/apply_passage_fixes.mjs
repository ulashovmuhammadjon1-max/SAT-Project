/**
 * Apply corrected passage HTML to questions already in the database.
 *
 *   DATABASE_URL=… node apply_passage_fixes.mjs <fixes.json> [--apply]
 *
 * The file is either {"fixed": {cb_id: html}} or an array of
 * {cb_id, passage} — both shapes are accepted so the passage-structure fix and
 * the rebuilt-table output can share this applier.
 *
 * Every write is gated on finding exactly ONE question with that College Board
 * id, per the project rule that a positional or id-based fix must be checked
 * against the row before it is written. A mismatch is reported, never guessed
 * past.
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";
import { readFileSync } from "fs";

const file = process.argv[2];
const APPLY = process.argv.includes("--apply");
const url = process.env.DATABASE_URL;
if (!file || !url) throw new Error("Usage: DATABASE_URL=… node apply_passage_fixes.mjs <fixes.json> [--apply]");

let sql, pgc;
if (/localhost|127\.0\.0\.1/.test(url)) {
  pgc = new pg.Client({ connectionString: url }); await pgc.connect();
  sql = async (s, ...v) => (await pgc.query(s.reduce((a, x, i) => a + x + (i < v.length ? `$${i + 1}` : ""), ""), v)).rows;
} else sql = neon(url);

const raw = JSON.parse(readFileSync(file, "utf8"));
const entries = Array.isArray(raw)
  ? raw.map((r) => [r.cb_id, r.passage])
  : Object.entries(raw.fixed ?? raw);

let updated = 0, notFound = 0, unchanged = 0;
for (const [cbId, html] of entries) {
  const rows = await sql`
    SELECT q.id, q."passageId", p.content
      FROM "Question" q LEFT JOIN "Passage" p ON p.id = q."passageId"
     WHERE q.source = ${"CB:" + cbId} AND q."moduleId" IS NOT NULL`;
  if (rows.length !== 1) { notFound++; console.log(`  ${cbId}: ${rows.length} matching questions, skipped`); continue; }
  const row = rows[0];
  if (!row.passageId) { notFound++; console.log(`  ${cbId}: no passage row, skipped`); continue; }
  if (row.content === html) { unchanged++; continue; }
  if (APPLY) {
    await sql`UPDATE "Passage" SET content = ${html} WHERE id = ${row.passageId}`;
  }
  updated++;
}
console.log(APPLY
  ? `updated ${updated}, already correct ${unchanged}, skipped ${notFound}`
  : `would update ${updated}, already correct ${unchanged}, skipped ${notFound} (dry run)`);
if (pgc) await pgc.end();
