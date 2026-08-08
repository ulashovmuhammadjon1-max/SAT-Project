/**
 * Insert Test 5 into the database.
 *
 * Modelled on ../test-3-4-build/insert.mjs and idempotent the same way: it
 * skips any Test/Module that already exists rather than duplicating it, so a
 * failed run can simply be re-run.
 *
 * The sandbox blocks raw Postgres (5432) and only allows outbound HTTPS, so
 * this goes over Neon's HTTP query API. Never put the connection string in a
 * file -- pass it in the environment:
 *
 *   DATABASE_URL='postgresql://...' node insert_test6.mjs [--publish]
 *
 * Without --publish the test lands as DRAFT.
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";
import { readFileSync, existsSync } from "fs";
import { randomUUID } from "crypto";
import path from "path";
import { fileURLToPath } from "url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PUBLISH = process.argv.includes("--publish");
const TITLE = "Test 6";

if (!process.env.DATABASE_URL) {
  console.error("Set DATABASE_URL.");
  process.exit(1);
}
/**
 * Neon's HTTP driver for production (the sandbox blocks port 5432), a normal
 * pg client for a local dry run. Both are used as the same tagged-template
 * function so the rest of the script does not care which is in play.
 */
const isLocal = /localhost|127\.0\.0\.1/.test(process.env.DATABASE_URL);
let sql, pgClient;
if (isLocal) {
  pgClient = new pg.Client({ connectionString: process.env.DATABASE_URL });
  await pgClient.connect();
  sql = async (strings, ...values) => {
    const text = strings.reduce((acc, s, i) => acc + s + (i < values.length ? `$${i + 1}` : ""), "");
    const res = await pgClient.query(text, values);
    return res.rows;
  };
  console.log("driver: pg (local dry run)");
} else {
  sql = neon(process.env.DATABASE_URL);
  console.log("driver: neon HTTP (production)");
}

const math = JSON.parse(readFileSync(path.join(HERE, "test6_math.json"), "utf8"));
const rw = JSON.parse(readFileSync(path.join(HERE, "test6_rw.json"), "utf8"));

const domainId = Object.fromEntries(
  (await sql`SELECT id, code FROM "Domain"`).map((d) => [d.code, d.id])
);
const skillId = Object.fromEntries(
  (await sql`SELECT id, code FROM "Skill"`).map((s) => [s.code, s.id])
);

const MODULE_CONFIG = {
  RW_M1:    { subject: "READING_WRITING", order: 1, difficulty: "STANDARD", title: "Module 1",        timeLimitMinutes: 32, adaptiveThresholdPct: 70 },
  RW_M2E:   { subject: "READING_WRITING", order: 2, difficulty: "EASY",     title: "Module 2 (Easy)", timeLimitMinutes: 32, adaptiveThresholdPct: null },
  RW_M2H:   { subject: "READING_WRITING", order: 2, difficulty: "HARD",     title: "Module 2 (Hard)", timeLimitMinutes: 32, adaptiveThresholdPct: null },
  MATH_M1:  { subject: "MATH", order: 1, difficulty: "STANDARD", title: "Module 1",        timeLimitMinutes: 35, adaptiveThresholdPct: 70 },
  MATH_M2E: { subject: "MATH", order: 2, difficulty: "EASY",     title: "Module 2 (Easy)", timeLimitMinutes: 35, adaptiveThresholdPct: null },
  MATH_M2H: { subject: "MATH", order: 2, difficulty: "HARD",     title: "Module 2 (Hard)", timeLimitMinutes: 35, adaptiveThresholdPct: null },
};

const TABLE_OPEN = '<table style="border-collapse:collapse;margin:0.75rem 0;">';
const TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">';
const TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">';

/** Render a Math question's `table` field into the standard HTML table. */
function tableHtml(t) {
  return (
    TABLE_OPEN +
    "<thead><tr>" + t.headers.map((h) => `${TH}${h}</th>`).join("") + "</tr></thead><tbody>" +
    t.rows.map((r) => "<tr>" + r.map((c) => `${TD}${c}</td>`).join("") + "</tr>").join("") +
    "</tbody></table>"
  );
}

/** Read a cropped source figure and inline it as a data URI. */
function figureDataUri(rel) {
  const p = path.join(HERE, rel);
  if (!existsSync(p)) throw new Error(`figure missing: ${rel}`);
  return "data:image/png;base64," + readFileSync(p).toString("base64");
}

async function ensureTest() {
  const existing = await sql`SELECT id, status FROM "Test" WHERE title=${TITLE}`;
  if (existing.length) {
    console.log(`Test "${TITLE}" already exists (${existing[0].id}, ${existing[0].status})`);
    return existing[0].id;
  }
  const id = randomUUID();
  await sql`
    INSERT INTO "Test" (id, title, description, type, status, "isAdaptive", "createdAt", "updatedAt")
    VALUES (${id}, ${TITLE}, ${"Full-length adaptive Digital SAT practice test."},
            'FULL_LENGTH', 'DRAFT', true, now(), now())`;
  console.log(`Created Test "${TITLE}" (${id}) as DRAFT`);
  return id;
}

async function ensureModule(testId, key) {
  const c = MODULE_CONFIG[key];
  const existing = await sql`
    SELECT id FROM "Module"
    WHERE "testId"=${testId} AND subject=${c.subject} AND "order"=${c.order} AND difficulty=${c.difficulty}`;
  if (existing.length) {
    console.log(`  ${key}: already exists (${existing[0].id}) — skipping`);
    return { id: existing[0].id, isNew: false };
  }
  const id = randomUUID();
  await sql`
    INSERT INTO "Module" (id, "testId", subject, "order", difficulty, title, "timeLimitMinutes", "adaptiveThresholdPct")
    VALUES (${id}, ${testId}, ${c.subject}, ${c.order}, ${c.difficulty}, ${c.title},
            ${c.timeLimitMinutes}, ${c.adaptiveThresholdPct})`;
  console.log(`  ${key}: created (${id})`);
  return { id, isNew: true };
}

async function insertQuestion(moduleId, q, kind, order) {
  let passageId = null;
  if (kind === "RW") {
    passageId = randomUUID();
    await sql`
      INSERT INTO "Passage" (id, "moduleId", title, content, "imageUrl", source)
      VALUES (${passageId}, ${moduleId}, ${null}, ${q.passageHtml}, ${null}, ${q.source ?? null})`;
  }

  // Math: fold any table into the stem and any figure onto imageUrl.
  let stem = q.stem;
  let imageUrl = null;
  if (q.table) stem = `${stem.replace(/TABLE_\w+\s*/, "")}${tableHtml(q.table)}`;
  if (q.figureFile) imageUrl = figureDataUri(q.figureFile);

  const domainCode = kind === "RW" ? q.domainCode : q.domain;
  const skillCode = kind === "RW" ? q.skillCode : q.skill;
  const dId = domainId[domainCode];
  const sId = skillId[skillCode];
  if (!dId || !sId) throw new Error(`no Domain/Skill for ${domainCode}/${skillCode}`);

  const questionId = randomUUID();
  const type = q.type === "FREE_RESPONSE" ? "FREE_RESPONSE" : "MULTIPLE_CHOICE";
  const correctAnswerFR = type === "FREE_RESPONSE" ? q.correctAnswerFR : null;
  const source = q.sourceRef ?? q.source ?? "MANUAL";

  await sql`
    INSERT INTO "Question" (id, "moduleId", "passageId", "domainId", "skillId", type, difficulty,
                            stem, "imageUrl", "tableData", "order", points, "correctAnswerFR",
                            "isPublished", source, "sourceUploadId", "createdAt", "updatedAt")
    VALUES (${questionId}, ${moduleId}, ${passageId}, ${dId}, ${sId}, ${type}, 'MEDIUM',
            ${stem}, ${imageUrl}, ${null}, ${order}, 1, ${correctAnswerFR},
            true, ${source}, ${null}, now(), now())`;

  if (type === "MULTIPLE_CHOICE") {
    const labels = ["A", "B", "C", "D"];
    let i = 0;
    for (const c of q.choices) {
      const label = typeof c === "string" ? labels[i] : c.label;
      const content = typeof c === "string" ? c : c.content;
      await sql`
        INSERT INTO "AnswerChoice" (id, "questionId", label, content, "isCorrect", "order")
        VALUES (${randomUUID()}, ${questionId}, ${label}, ${content}, ${label === q.correct}, ${i})`;
      i++;
    }
  }
}

const PLAN = [
  ["RW_M1",    "RW",   rw["test6|RW_M1"]],
  ["RW_M2E",   "RW",   rw["test6|RW_M2_EASY"]],
  ["RW_M2H",   "RW",   rw["test6|RW_M2_HARD"]],
  ["MATH_M1",  "MATH", math["MATH_M1"]],
  ["MATH_M2E", "MATH", math["MATH_M2_EASY"]],
  ["MATH_M2H", "MATH", math["MATH_M2_HARD"]],
];

const testId = await ensureTest();
let total = 0;
for (const [key, kind, questions] of PLAN) {
  const { id: moduleId, isNew } = await ensureModule(testId, key);
  if (!isNew) continue;
  let order = 1;
  for (const q of questions) {
    await insertQuestion(moduleId, q, kind, order++);
  }
  total += questions.length;
  console.log(`    inserted ${questions.length} questions`);
}

if (PUBLISH) {
  await sql`UPDATE "Test" SET status='PUBLISHED', "updatedAt"=now() WHERE id=${testId}`;
  console.log(`\nTest 6 status -> PUBLISHED`);
}

const check = await sql`
  SELECT m.subject, m."order" AS mo, m.difficulty, count(q.id)::int AS n
  FROM "Module" m LEFT JOIN "Question" q ON q."moduleId"=m.id
  WHERE m."testId"=${testId}
  GROUP BY m.subject, m."order", m.difficulty
  ORDER BY m.subject, m."order", m.difficulty`;
console.log(`\nTest 6 (${testId}) — ${total} questions inserted this run`);
for (const r of check) console.log(`  ${r.subject} M${r.mo} ${r.difficulty}: ${r.n}`);

if (pgClient) await pgClient.end();
