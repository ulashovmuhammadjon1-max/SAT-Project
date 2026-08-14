/**
 * Delete retired questions that carry no student history.
 *
 *   DATABASE_URL=… node purge_retired.mjs [--apply]
 *
 * "Retired" means detached from its test and unpublished — the state the R&W
 * rebuild left the replaced questions in. They are already invisible to
 * students, but they still count in the admin Question Bank's row total, which
 * is what made 5,415 look wrong.
 *
 * A retired question is deleted ONLY when nothing references it: no Response,
 * no QuestionAttempt, no Bookmark. Anything a student has actually answered or
 * saved stays, because `Response.questionId` has no onDelete rule and removing
 * the row would either fail on the foreign key or, if the responses were
 * cleared first, silently destroy that student's attempt history and make
 * their past results and review pages wrong.
 *
 * AnswerChoice, Explanation, Bookmark and QuestionAttempt all cascade from
 * Question. The Passage does not — it is referenced the other way — so an
 * orphaned passage is removed afterwards.
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";

const APPLY = process.argv.includes("--apply");
const url = process.env.DATABASE_URL;
if (!url) throw new Error("Set DATABASE_URL.");
let sql, pgc;
if (/localhost|127\.0\.0\.1/.test(url)) {
  pgc = new pg.Client({ connectionString: url }); await pgc.connect();
  sql = async (s, ...v) => (await pgc.query(s.reduce((a, x, i) => a + x + (i < v.length ? `$${i + 1}` : ""), ""), v)).rows;
} else sql = neon(url);

const targets = await sql`
  SELECT q.id, q."passageId"
    FROM "Question" q
   WHERE q."moduleId" IS NULL AND NOT q."isPublished"
     AND NOT EXISTS (SELECT 1 FROM "Response"        r WHERE r."questionId" = q.id)
     AND NOT EXISTS (SELECT 1 FROM "QuestionAttempt" a WHERE a."questionId" = q.id)
     AND NOT EXISTS (SELECT 1 FROM "Bookmark"        b WHERE b."questionId" = q.id)`;

const [{ kept }] = await sql`
  SELECT count(*) AS kept FROM "Question" q
   WHERE q."moduleId" IS NULL AND NOT q."isPublished"
     AND (EXISTS (SELECT 1 FROM "Response"        r WHERE r."questionId" = q.id)
       OR EXISTS (SELECT 1 FROM "QuestionAttempt" a WHERE a."questionId" = q.id)
       OR EXISTS (SELECT 1 FROM "Bookmark"        b WHERE b."questionId" = q.id))`;

console.log(`retired with no history : ${targets.length}  (deletable)`);
console.log(`retired with history    : ${Number(kept)}  (kept — deleting these would destroy attempt history)`);

if (!APPLY) {
  console.log("Report only. Re-run with --apply.");
  if (pgc) await pgc.end();
  process.exit(0);
}

const ids = targets.map((t) => t.id);
const passageIds = [...new Set(targets.map((t) => t.passageId).filter(Boolean))];

for (let i = 0; i < ids.length; i += 200) {
  const chunk = ids.slice(i, i + 200);
  await sql`DELETE FROM "Question" WHERE id = ANY(${chunk})`;
}
// Passages are referenced BY the question, so they only become orphans after
// the questions are gone. Only ever remove one nothing else still points at.
let orphans = 0;
for (let i = 0; i < passageIds.length; i += 200) {
  const chunk = passageIds.slice(i, i + 200);
  const r = await sql`
    DELETE FROM "Passage" p
     WHERE p.id = ANY(${chunk})
       AND NOT EXISTS (SELECT 1 FROM "Question" q WHERE q."passageId" = p.id)
     RETURNING p.id`;
  orphans += r.length;
}
console.log(`deleted ${ids.length} questions and ${orphans} orphaned passages`);
if (pgc) await pgc.end();
