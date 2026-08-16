/**
 * Insert a parsed IELTS test as a DRAFT.
 *
 *   PROD_URL='postgresql://...' node insert_ielts_test.mjs listening-1.json [--apply]
 *
 * DRAFT, always. This script has no publish flag on purpose: imported content
 * reaches students only when a human flips it in the admin panel, which is the
 * same rule the SAT pipeline follows and the reason the importer's findings are
 * worth generating at all. Re-running replaces the draft's content rather than
 * creating a second copy, so a corrected parse can simply be re-imported.
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync } from "fs";
import { randomUUID } from "crypto";

const file = process.argv[2];
const APPLY = process.argv.includes("--apply");
if (!file) {
  console.error("usage: insert_ielts_test.mjs <parsed.json> [--apply]");
  process.exit(1);
}
const sql = neon(process.env.PROD_URL);
const test = JSON.parse(readFileSync(file, "utf8"));

const nq = test.parts.reduce(
  (n, p) => n + p.groups.reduce((m, g) => m + g.questions.length, 0), 0);
console.log(`${test.title} — ${test.parts.length} parts, ${nq} questions, status DRAFT`);
if (test.findings?.length) {
  console.log(`\n${test.findings.length} finding(s) carried in as notes:`);
  for (const f of test.findings) console.log("  ! " + f);
}
if (!APPLY) { console.log("\nDRY RUN — re-run with --apply"); process.exit(0); }

const existing = await sql.query(`SELECT id FROM "IeltsTest" WHERE slug = $1`, [test.slug]);
let testId;
if (existing.length) {
  testId = existing[0].id;
  const st = await sql.query(`SELECT status FROM "IeltsTest" WHERE id = $1`, [testId]);
  if (st[0].status === "PUBLISHED") {
    // Never rewrite a paper students may be sitting right now.
    console.error("This slug is PUBLISHED. Unpublish it before re-importing.");
    process.exit(1);
  }
  // Sections cascade to parts, groups and questions, so clearing the section
  // clears the whole tree beneath it.
  await sql.query(`DELETE FROM "IeltsSection" WHERE "testId" = $1`, [testId]);
  console.log("replacing the existing draft");
} else {
  testId = randomUUID();
  await sql.query(
    `INSERT INTO "IeltsTest" (id, title, slug, module, status, description, difficulty,
                              "createdAt", "updatedAt")
     VALUES ($1,$2,$3,$4::"IeltsModule",'DRAFT',$5,3,now(),now())`,
    [testId, test.title, test.slug, test.module,
     "Imported from an HTML export. Audio must be attached before publishing."]);
}

const sectionId = randomUUID();
await sql.query(
  `INSERT INTO "IeltsSection" (id, "testId", skill, "order", "durationMinutes", instructions)
   VALUES ($1,$2,$3::"IeltsSkill",1,$4,$5)`,
  [sectionId, testId, test.skill, test.durationMinutes,
   "You will hear each recording once."]);

let inserted = 0;
for (const part of test.parts) {
  const partId = randomUUID();
  await sql.query(
    `INSERT INTO "IeltsPart" (id, "sectionId", "partNumber", title, instructions,
                              "audioUrl", transcript)
     VALUES ($1,$2,$3,$4,$5,$6,$7)`,
    [partId, sectionId, part.partNumber, part.title, part.instructions,
     part.audioUrl, part.transcript ?? null]);

  let order = 0;
  for (const g of part.groups) {
    const groupId = randomUUID();
    await sql.query(
      `INSERT INTO "IeltsQuestionGroup" (id, "partId", "order", type, instructions,
                                         "wordLimit", "maxWords", "maxNumbers",
                                         "bodyHtml", "optionsJson")
       VALUES ($1,$2,$3,$4::"IeltsQuestionType",$5,$6,$7,$8,$9,$10::jsonb)`,
      [groupId, partId, order++, g.type, g.instructions, g.wordLimit,
       g.maxWords, g.maxNumbers, g.bodyHtml,
       g.optionsJson ? JSON.stringify(g.optionsJson) : null]);

    for (const q of g.questions) {
      // A finding about this question travels with it, so an admin opening the
      // draft sees the problem on the row rather than in a log they never read.
      const note = (test.findings ?? []).filter((f) => f.startsWith(`Q${q.number}:`));
      await sql.query(
        `INSERT INTO "IeltsQuestion" (id, "partId", "groupId", number, type,
                                      "promptHtml", "optionsJson", "correctAnswer",
                                      "acceptedAnswers", "caseSensitive", metadata)
         VALUES ($1,$2,$3,$4,$5::"IeltsQuestionType",$6,$7::jsonb,$8,$9::jsonb,false,$10::jsonb)`,
        [randomUUID(), partId, groupId, q.number, q.type, q.promptHtml,
         q.optionsJson ? JSON.stringify(q.optionsJson) : null,
         q.correctAnswer,
         q.acceptedAnswers ? JSON.stringify(q.acceptedAnswers) : null,
         JSON.stringify({ importedFrom: "html-export", findings: note })]);
      inserted++;
    }
  }
}

const check = await sql.query(
  `SELECT p."partNumber", COUNT(q.id)::int AS questions,
          COUNT(DISTINCT g.id)::int AS groups,
          BOOL_OR(p."audioUrl" IS NOT NULL) AS "hasAudio"
     FROM "IeltsPart" p
     LEFT JOIN "IeltsQuestionGroup" g ON g."partId" = p.id
     LEFT JOIN "IeltsQuestion" q ON q."partId" = p.id
    WHERE p."sectionId" = $1
    GROUP BY p."partNumber" ORDER BY p."partNumber"`, [sectionId]);
console.table(check);
console.log(`inserted ${inserted} questions as DRAFT (test id ${testId})`);
console.log("Audio is not attached — no part will play until a file is uploaded.");
