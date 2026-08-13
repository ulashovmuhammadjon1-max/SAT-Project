/**
 * Insert authored Cross-Text Connections questions into the Question Bank.
 *
 * These are standalone bank questions, not part of any test: `moduleId` is
 * null, which the schema allows and which the Question Bank's own filters
 * accommodate (they gate on `isPublished` alone, never on module membership).
 * That keeps a practice-only skill top-up from disturbing the 31 assembled
 * tests.
 *
 * Idempotent by `ref`: every question carries its ref in `source`, and a run
 * skips any ref already present, so re-running after an interruption inserts
 * only what is missing.
 *
 *   PROD_URL=… node insert_ct.mjs batch1.json            # report only
 *   PROD_URL=… node insert_ct.mjs batch1.json --apply
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync } from "fs";

const DIR = new URL(".", import.meta.url).pathname;
const APPLY = process.argv.includes("--apply");
const files = process.argv.slice(2).filter((a) => a.endsWith(".json"));
if (!files.length) throw new Error("Usage: node insert_ct.mjs <batch.json…> [--apply]");

const sql = neon(process.env.PROD_URL);

const [{ id: domainId }] = await sql`SELECT id FROM "Domain" WHERE code = 'CAS'`;
const [{ id: skillId }] = await sql`SELECT id FROM "Skill" WHERE code = 'CAS-CT'`;

const items = files.flatMap((f) => JSON.parse(readFileSync(`${DIR}/${f}`, "utf8")));

/* Guard rails, all cheap and all worth having: a malformed batch should fail
   here rather than land half-built rows in a live bank. */
const problems = [];
const seen = new Set();
for (const q of items) {
  const at = `${q.ref}`;
  if (seen.has(q.ref)) problems.push(`${at}: duplicate ref within the batch`);
  seen.add(q.ref);
  if (!/Text 1/.test(q.passage) || !/Text 2/.test(q.passage))
    problems.push(`${at}: passage must carry both Text 1 and Text 2`);
  const correct = q.choices.filter((c) => c.isCorrect);
  if (correct.length !== 1) problems.push(`${at}: ${correct.length} correct choices, expected 1`);
  if (q.choices.length !== 4) problems.push(`${at}: ${q.choices.length} choices, expected 4`);
  if (new Set(q.choices.map((c) => c.content.trim())).size !== q.choices.length)
    problems.push(`${at}: duplicate choice text`);
  // Every distractor needs its own reason — the whole point of the rewrite the
  // user asked for after seeing bare "this is incorrect" explanations.
  for (const c of q.choices) {
    if (c.isCorrect) continue;
    if (!q.whyWrong?.[c.label]?.trim()) problems.push(`${at}: no whyWrong for ${c.label}`);
  }
  if (!["EASY", "MEDIUM", "HARD"].includes(q.difficulty)) problems.push(`${at}: bad difficulty`);
  // A LaTeX macro outside a math span renders as a literal backslash. R&W
  // prose should not contain one at all.
  const prose = [q.stem, q.passage, ...q.choices.map((c) => c.content)].join(" ");
  if (/\\[A-Za-z]+/.test(prose)) problems.push(`${at}: LaTeX macro in prose`);
  if (/\*[^*\n]+\*/.test(prose)) problems.push(`${at}: markdown asterisks — use <em>`);
}
if (problems.length) {
  console.error(problems.join("\n"));
  throw new Error(`${problems.length} problems; nothing written`);
}

const existing = new Set(
  (await sql`SELECT source FROM "Question" WHERE source LIKE 'CT-AUTHORED:%'`).map((r) =>
    r.source.replace("CT-AUTHORED:", "")
  )
);
const todo = items.filter((q) => !existing.has(q.ref));
console.log(`${items.length} authored, ${items.length - todo.length} already present, ${todo.length} to insert`);

if (!APPLY) {
  console.log("Report only. Re-run with --apply to write them.");
  process.exit(0);
}

function html(q) {
  const bits = [`<p>${q.whyCorrect}</p>`, "<p><strong>Why the others are wrong</strong></p><ul>"];
  for (const [label, why] of Object.entries(q.whyWrong)) bits.push(`<li><strong>${label}.</strong> ${why}</li>`);
  bits.push("</ul>");
  return bits.join("");
}

let n = 0;
for (const q of todo) {
  const [{ id: passageId }] = await sql`
    INSERT INTO "Passage" (id, content, source)
    VALUES (gen_random_uuid()::text, ${q.passage}, ${"CT-AUTHORED:" + q.ref}) RETURNING id`;

  const [{ id: questionId }] = await sql`
    INSERT INTO "Question" (id, "passageId", "domainId", "skillId", type, difficulty, stem,
                            "order", points, "isPublished", source, "createdAt", "updatedAt")
    VALUES (gen_random_uuid()::text, ${passageId}, ${domainId}, ${skillId}, 'MULTIPLE_CHOICE',
            ${q.difficulty}::"QuestionDifficulty", ${q.stem}, 0, 1, true,
            ${"CT-AUTHORED:" + q.ref}, NOW(), NOW()) RETURNING id`;

  for (const [i, c] of q.choices.entries()) {
    await sql`
      INSERT INTO "AnswerChoice" (id, "questionId", label, content, "isCorrect", "order")
      VALUES (gen_random_uuid()::text, ${questionId}, ${c.label}, ${c.content}, ${c.isCorrect}, ${i})`;
  }

  await sql`
    INSERT INTO "Explanation" (id, "questionId", content, "whyCorrect", "whyWrongJson",
                               "commonMistakes", tips, source, "generatedAt")
    VALUES (gen_random_uuid()::text, ${questionId}, ${html(q)}, ${q.whyCorrect},
            ${JSON.stringify(q.whyWrong)}::jsonb, ${q.commonMistakes ?? null}, ${q.tips ?? null},
            'MANUAL', NOW())`;

  n++;
  console.log(`  ${q.ref}`);
}
console.log(`inserted ${n}`);
