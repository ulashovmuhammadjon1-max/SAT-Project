/**
 * Put every verified SATashkent question that no test uses into the Question
 * Bank.
 *
 *   DATABASE_URL='postgresql://...' node insert_bank.mjs [--apply]
 *
 * The Question Bank selects on `isPublished` alone and never joins Module
 * (see src/server/actions/student/question-bank.ts), so a question with
 * `moduleId = NULL` and `isPublished = true` is a bank-only question: drillable
 * and searchable, but not part of any mock test. That is exactly what the
 * leftovers should be — there is no room for them in a 22-question module, and
 * they are verified content that would otherwise sit in a JSON file.
 *
 * Retired questions are the same shape with `isPublished = false`, so the two
 * populations stay distinguishable.
 *
 * Idempotent on `source`: a question already present is skipped, so this can be
 * re-run as more figures land.
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";
import { readFileSync, existsSync, readdirSync } from "fs";
import { randomUUID } from "crypto";
import path from "path";
import { fileURLToPath } from "url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const APPLY = process.argv.includes("--apply");

if (!process.env.DATABASE_URL) {
  console.error("Set DATABASE_URL.");
  process.exit(1);
}
const isLocal = /localhost|127\.0\.0\.1/.test(process.env.DATABASE_URL);
let sql, pgClient;
if (isLocal) {
  pgClient = new pg.Client({ connectionString: process.env.DATABASE_URL });
  await pgClient.connect();
  sql = { query: async (t, v = []) => (await pgClient.query(t, v)).rows };
} else {
  const n = neon(process.env.DATABASE_URL);
  sql = { query: async (t, v = []) => await n.query(t, v) };
}

const pool = JSON.parse(readFileSync(path.join(HERE, "pool.json"), "utf8"));
const meta = new Map();
for (const f of ["math_parsed.json", "hard_parsed.json"]) {
  for (const q of JSON.parse(readFileSync(path.join(HERE, f), "utf8"))) meta.set(q.id, q);
}

// Everything a test already uses.
const allocated = new Set();
for (const f of ["allocation.json", "allocation2.json"]) {
  if (!existsSync(path.join(HERE, f))) continue;
  for (const t of JSON.parse(readFileSync(path.join(HERE, f), "utf8")))
    for (const m of Object.values(t.modules))
      for (const q of m.questions) allocated.add(q.id);
}

const candidates = pool.filter((q) => !allocated.has(q.id));
console.log(`pool ${pool.length}, in tests ${allocated.size}, bank candidates ${candidates.length}`);

const existing = new Set(
  (await sql.query(
    `SELECT source FROM "Question"
      WHERE source LIKE 'SATMATH:%' OR source LIKE 'SATHARD:%'`))
    .map((r) => r.source));

const domainId = Object.fromEntries(
  (await sql.query('SELECT id, code FROM "Domain"')).map((d) => [d.code, d.id]));
const skillId = Object.fromEntries(
  (await sql.query('SELECT id, code FROM "Skill"')).map((s) => [s.code, s.id]));

function explanationHtml(q) {
  const bits = [];
  if (q.whyCorrect) bits.push(`<p>${q.whyCorrect}</p>`);
  const wrong = Object.entries(q.whyWrong || {});
  if (wrong.length) {
    bits.push("<p><strong>Why the other choices are wrong</strong></p><ul>");
    for (const [label, why] of wrong) bits.push(`<li><strong>${label}.</strong> ${why}</li>`);
    bits.push("</ul>");
  }
  return bits.join("");
}

let written = 0, skipped = 0;
for (const q of candidates) {
  const source = (q.id.startsWith("sathard") ? "SATHARD:" : "SATMATH:") + q.id;
  if (existing.has(source)) { skipped++; continue; }
  if (!APPLY) { written++; continue; }

  const m = meta.get(q.id);
  const dId = domainId[m.domain], sId = skillId[m.skill];
  if (!dId || !sId) throw new Error(`no Domain/Skill for ${q.id}`);
  const type = q.choices && q.choices.length ? "MULTIPLE_CHOICE" : "FREE_RESPONSE";
  const qid = randomUUID();

  await sql.query(
    `INSERT INTO "Question" (id, "moduleId", "domainId", "skillId", type, difficulty,
                             stem, "imageUrl", "order", points, "correctAnswerFR",
                             "isPublished", source, "createdAt", "updatedAt")
     VALUES ($1, NULL, $2,$3,$4,$5,$6,$7,0,1,$8,true,$9,now(),now())`,
    [qid, dId, sId, type, q.difficulty, q.stem, q.imageUrl ?? null,
     type === "FREE_RESPONSE" ? JSON.stringify([String(q.answerValue)]) : null, source]);

  if (type === "MULTIPLE_CHOICE") {
    let i = 0;
    for (const c of q.choices) {
      await sql.query(
        `INSERT INTO "AnswerChoice" (id, "questionId", label, content, "isCorrect", "order")
         VALUES ($1,$2,$3,$4,$5,$6)`,
        [randomUUID(), qid, c.label, c.content, c.label === q.answerLabel, i++]);
    }
  }

  await sql.query(
    `INSERT INTO "Explanation" (id, "questionId", content, "whyCorrect", "whyWrongJson",
                                source, "generatedAt")
     VALUES (gen_random_uuid()::text, $1, $2, $3, $4::jsonb, 'AI_GENERATED', now())
     ON CONFLICT ("questionId") DO NOTHING`,
    [qid, explanationHtml(q), q.whyCorrect ?? null, JSON.stringify(q.whyWrong || {})]);

  written++;
}

console.log(`${APPLY ? "APPLIED" : "DRY RUN"}: ${written} to insert, ${skipped} already present`);

if (APPLY) {
  const t = await sql.query(
    `SELECT COUNT(*)::int AS bank
       FROM "Question"
      WHERE "moduleId" IS NULL AND "isPublished"
        AND (source LIKE 'SATMATH:%' OR source LIKE 'SATHARD:%')`);
  console.log(`bank-only SATashkent questions now live: ${t[0].bank}`);
}
if (pgClient) await pgClient.end();
