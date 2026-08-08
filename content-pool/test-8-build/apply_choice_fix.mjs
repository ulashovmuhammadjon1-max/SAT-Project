/**
 * Push the repaired writing-domain choices into a published test.
 *
 * Test 8 shipped 12 Boundaries questions whose four options were bare
 * punctuation — ", " / "; " / ": " / " and " — so the student saw four
 * near-empty rows. This replaces them with the spliced versions produced by
 * fix_writing_choices.py, which repeat the words either side of the blank.
 *
 * Matched by passage content, never by row id (ids differ between
 * environments), and every question is checked to still have exactly one
 * correct choice after the write.
 *
 *   DATABASE_URL='postgresql://...' node apply_choice_fix.mjs rw_test8_repaired.json "Test 8" [--apply]
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";
import { readFileSync } from "fs";
import path from "path";
import { fileURLToPath } from "url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2).filter((a) => !a.startsWith("--"));
const APPLY = process.argv.includes("--apply");
const [jsonFile, TITLE] = args;

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

const repaired = JSON.parse(readFileSync(path.join(HERE, jsonFile), "utf8"));
// Only the questions the repair actually changed: a choice with no letters is
// what marked a question as broken in the first place.
const targets = repaired.filter((q) =>
  q.choices.every((c) => /[A-Za-z]/.test(c)) && q.skill === "Boundaries");

let changed = 0, skipped = 0;
for (const q of targets) {
  const rows = await sql`
    SELECT q.id, p.content AS passage FROM "Question" q
    JOIN "Passage" p ON p.id = q."passageId"
    JOIN "Module" m ON m.id = q."moduleId"
    JOIN "Test" t ON t.id = m."testId"
    WHERE t.title = ${TITLE} AND p.content = ${q.passage}`;
  if (rows.length !== 1) {
    console.log(`  .. ${q.num}: matched ${rows.length} questions by passage — skipping`);
    skipped++;
    continue;
  }
  const questionId = rows[0].id;

  const existing = await sql`
    SELECT id, label, content, "isCorrect" FROM "AnswerChoice"
    WHERE "questionId" = ${questionId} ORDER BY "order"`;
  if (existing.length !== 4) {
    console.log(`  !! ${q.num}: ${existing.length} choices in the database — skipping`);
    skipped++;
    continue;
  }
  // The stored options must still be the broken ones, or this row is not what
  // the repair was computed against. The signature of a broken row is an option
  // with no letters at all — testing for a long word instead gives a false
  // "already repaired" on choices like ", and " or "; also ".
  if (!existing.some((c) => !/[A-Za-z]/.test(c.content))) {
    console.log(`  .. ${q.num}: already repaired — skipping`);
    continue;
  }

  for (let i = 0; i < 4; i++) {
    if (APPLY) {
      await sql`UPDATE "AnswerChoice" SET content = ${q.choices[i]} WHERE id = ${existing[i].id}`;
    }
  }
  const keyIdx = "ABCD".indexOf(q.answer);
  if (!existing[keyIdx].isCorrect) {
    console.log(`  !! ${q.num}: the database key is at ${existing.findIndex((c) => c.isCorrect)}, `
      + `the source says ${keyIdx} — NOT touched`);
    skipped++;
    continue;
  }
  changed++;
}

console.log(`\n${APPLY ? "applied" : "dry run"}: ${changed} questions, ${skipped} skipped`);

if (APPLY) {
  const bad = await sql`
    SELECT COUNT(*)::int AS n FROM "Question" q
    JOIN "Module" m ON m.id = q."moduleId" JOIN "Test" t ON t.id = m."testId"
    WHERE t.title = ${TITLE} AND q.type = 'MULTIPLE_CHOICE'
      AND (SELECT COUNT(*) FROM "AnswerChoice" ac
           WHERE ac."questionId" = q.id AND ac."isCorrect") <> 1`;
  console.log(`questions without exactly one key: ${bad[0].n}`);
}
if (pgClient) await pgClient.end();
