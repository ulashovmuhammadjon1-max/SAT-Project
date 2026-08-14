/**
 * Fix long-standing defects in Tests 1-5 that predate the College Board rebuild.
 *
 *   DATABASE_URL=… node fix_legacy_defects.mjs [--apply]
 *
 * Every change asserts a distinctive substring of the CURRENT row before
 * writing, per the project rule that an id- or position-based fix must be
 * gated on content. A row that does not match is reported and skipped.
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

let done = 0, skipped = 0;

/* -------------------------------------------------------------------------- */
/* 1. Fill-in-the-blank passages whose blank is one or two underscores.        */
/*                                                                            */
/* The house convention is a five-underscore blank. A single "_" between two  */
/* spaces is almost invisible at body-text size, so the student cannot see    */
/* where the missing word goes. Matched by the exact surrounding words rather */
/* than by a bare underscore, because an underscore can legitimately appear   */
/* elsewhere in a passage.                                                    */
/* -------------------------------------------------------------------------- */
const BLANKS = [
  { id: "oklxnec5yogs7hqfvlxa00nb", from: "The organization _ this commitment",
    to: "The organization _____ this commitment" },
  { id: "tugrkcg3qniv7ut39qvx00bi", from: "being able to __ relatively small companies",
    to: "being able to _____ relatively small companies" },
  { id: "w14kh9is8rcbk9ucactyum8z", from: "an effort to _ what were regarded",
    to: "an effort to _____ what were regarded" },
];

for (const b of BLANKS) {
  const rows = await sql`
    SELECT p.id, p.content FROM "Question" q JOIN "Passage" p ON p.id = q."passageId"
     WHERE q.id = ${b.id}`;
  if (rows.length !== 1 || !rows[0].content.includes(b.from)) {
    console.log(`  blank ${b.id}: expected text not found, skipped`); skipped++; continue;
  }
  const next = rows[0].content.replace(b.from, b.to);
  if (APPLY) await sql`UPDATE "Passage" SET content = ${next} WHERE id = ${rows[0].id}`;
  console.log(`  blank ${b.id}: "${b.from}" -> five-underscore blank`);
  done++;
}

/* -------------------------------------------------------------------------- */
/* 2. Test 2 M2 Hard q17 — choices B and D are character-for-character the     */
/*    same, so the question has only three distinct options and two of them   */
/*    are indistinguishable.                                                  */
/*                                                                            */
/* The item tests comma placement around a restrictive appositive: the        */
/* credited answer C has no commas, because "lawyer and cycling advocate      */
/* Ernesto Hernandez-Lopez" is the subject and must not be cut off from its   */
/* verb "has identified". The natural four-way set is the four permutations   */
/* of the two comma positions, and D is the one missing: a comma after        */
/* "advocate" but none before the verb. Restoring that makes the choices      */
/* distinct and keeps C uniquely correct.                                     */
/* -------------------------------------------------------------------------- */
{
  const qid = "pti7yo2nzgxn44qe91212127";
  const choices = await sql`
    SELECT id, label, content, "isCorrect" FROM "AnswerChoice"
     WHERE "questionId" = ${qid} ORDER BY "order"`;
  const d = choices.find((c) => c.label === "D");
  const b = choices.find((c) => c.label === "B");
  const dup = d && b && d.content.trim() === b.content.trim();
  if (!dup) {
    console.log("  Test 2 q17: B and D no longer identical, skipped"); skipped++;
  } else if (d.isCorrect) {
    console.log("  Test 2 q17: D is marked correct — not safe to edit, skipped"); skipped++;
  } else {
    const next = "advocate, Ernesto Hernandez-Lopez";
    if (APPLY) await sql`UPDATE "AnswerChoice" SET content = ${next} WHERE id = ${d.id}`;
    console.log(`  Test 2 q17: choice D "${d.content}" -> "${next}"`);
    done++;
  }
}

console.log(APPLY ? `\napplied ${done}, skipped ${skipped}` : `\nwould apply ${done}, skip ${skipped} (dry run)`);
if (pgc) await pgc.end();
