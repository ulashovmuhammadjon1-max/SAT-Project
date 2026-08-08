/**
 * Insert a test built by assemble_test7.py (or any later test in the same
 * shape) and optionally publish it.
 *
 * Idempotent: an existing Test/Module is skipped rather than duplicated, so a
 * failed run can simply be re-run.
 *
 * Differs from insert_test6.mjs in one important way: the question's own
 * `difficulty` is written through instead of being hardcoded to 'MEDIUM'.
 * Hardcoding it is why every question in Tests 3-6 reads MEDIUM in the
 * Question Bank regardless of which module it sits in.
 *
 * The sandbox blocks raw Postgres (5432) and allows only outbound HTTPS, so
 * production goes over Neon's HTTP API. Never put the connection string in a
 * file — pass it in the environment:
 *
 *   DATABASE_URL='postgresql://...' node insert_test.mjs test7.json "Test 7" [--publish]
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";
import { readFileSync } from "fs";
import { randomUUID } from "crypto";
import path from "path";
import { fileURLToPath } from "url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2).filter((a) => !a.startsWith("--"));
const PUBLISH = process.argv.includes("--publish");
const [jsonFile = "test7.json", TITLE = "Test 7"] = args;

if (!process.env.DATABASE_URL) {
  console.error("Set DATABASE_URL.");
  process.exit(1);
}

const isLocal = /localhost|127\.0\.0\.1/.test(process.env.DATABASE_URL);
let sql, pgClient;
if (isLocal) {
  pgClient = new pg.Client({ connectionString: process.env.DATABASE_URL });
  await pgClient.connect();
  sql = async (strings, ...values) => {
    const text = strings.reduce((a, s, i) => a + s + (i < values.length ? `$${i + 1}` : ""), "");
    return (await pgClient.query(text, values)).rows;
  };
  console.log("driver: pg (local)");
} else {
  sql = neon(process.env.DATABASE_URL);
  console.log("driver: neon HTTP (production)");
}

const test = JSON.parse(readFileSync(path.join(HERE, jsonFile), "utf8"));

const domainId = Object.fromEntries((await sql`SELECT id, code FROM "Domain"`).map((d) => [d.code, d.id]));
const skillId = Object.fromEntries((await sql`SELECT id, code FROM "Skill"`).map((s) => [s.code, s.id]));

const MODULE_CONFIG = {
  RW_M1:    { subject: "READING_WRITING", order: 1, difficulty: "STANDARD", title: "Module 1",        timeLimitMinutes: 32, adaptiveThresholdPct: 70 },
  RW_M2E:   { subject: "READING_WRITING", order: 2, difficulty: "EASY",     title: "Module 2 (Easy)", timeLimitMinutes: 32, adaptiveThresholdPct: null },
  RW_M2H:   { subject: "READING_WRITING", order: 2, difficulty: "HARD",     title: "Module 2 (Hard)", timeLimitMinutes: 32, adaptiveThresholdPct: null },
  MATH_M1:  { subject: "MATH", order: 1, difficulty: "STANDARD", title: "Module 1",        timeLimitMinutes: 35, adaptiveThresholdPct: 70 },
  MATH_M2E: { subject: "MATH", order: 2, difficulty: "EASY",     title: "Module 2 (Easy)", timeLimitMinutes: 35, adaptiveThresholdPct: null },
  MATH_M2H: { subject: "MATH", order: 2, difficulty: "HARD",     title: "Module 2 (Hard)", timeLimitMinutes: 35, adaptiveThresholdPct: null },
};
const ORDER = ["RW_M1", "RW_M2E", "RW_M2H", "MATH_M1", "MATH_M2E", "MATH_M2H"];

const TABLE_OPEN = '<table style="border-collapse:collapse;margin:0.75rem 0;">';
const TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">';
const TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">';

/** [caption, headers, rows] -> the house table markup. */
function tableHtml(t) {
  if (typeof t === "string") return t;
  const [caption, headers, rows] = t;
  const cap = caption
    ? `<caption style="caption-side:top;text-align:left;font-weight:600;padding-bottom:0.35rem;">${caption}</caption>`
    : "";
  return (
    TABLE_OPEN + cap +
    "<thead><tr>" + headers.map((h) => `${TH}${h}</th>`).join("") + "</tr></thead><tbody>" +
    rows.map((r) => "<tr>" + r.map((c) => `${TD}${c}</td>`).join("") + "</tr>").join("") +
    "</tbody></table>"
  );
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
  console.log(`Created "${TITLE}" (${id}) as DRAFT`);
  return id;
}

async function ensureModule(testId, key) {
  const c = MODULE_CONFIG[key];
  const existing = await sql`
    SELECT id FROM "Module"
    WHERE "testId"=${testId} AND subject=${c.subject} AND "order"=${c.order} AND difficulty=${c.difficulty}`;
  if (existing.length) {
    console.log(`  ${key}: exists — skipping`);
    return { id: existing[0].id, isNew: false };
  }
  const id = randomUUID();
  await sql`
    INSERT INTO "Module" (id, "testId", subject, "order", difficulty, title, "timeLimitMinutes", "adaptiveThresholdPct")
    VALUES (${id}, ${testId}, ${c.subject}, ${c.order}, ${c.difficulty}, ${c.title},
            ${c.timeLimitMinutes}, ${c.adaptiveThresholdPct})`;
  return { id, isNew: true };
}

async function insertQuestion(moduleId, q, order) {
  let passageId = null;
  if (q.passage) {
    passageId = randomUUID();
    await sql`
      INSERT INTO "Passage" (id, "moduleId", title, content, "imageUrl", source)
      VALUES (${passageId}, ${moduleId}, ${null}, ${q.passage}, ${null}, ${q._ref ?? null})`;
  }

  let stem = q.stem;
  if (q.table) stem = `${stem}${tableHtml(q.table)}`;

  const dId = domainId[q.domain];
  const sId = skillId[q.skill];
  if (!dId || !sId) throw new Error(`no Domain/Skill for ${q.domain}/${q.skill}`);

  const id = randomUUID();
  const type = q.type === "FREE_RESPONSE" ? "FREE_RESPONSE" : "MULTIPLE_CHOICE";
  await sql`
    INSERT INTO "Question" (id, "moduleId", "passageId", "domainId", "skillId", type, difficulty,
                            stem, "imageUrl", "tableData", "order", points, "correctAnswerFR",
                            "isPublished", source, "sourceUploadId", "createdAt", "updatedAt")
    VALUES (${id}, ${moduleId}, ${passageId}, ${dId}, ${sId}, ${type}, ${q.difficulty ?? "MEDIUM"},
            ${stem}, ${null}, ${null}, ${order}, 1, ${type === "FREE_RESPONSE" ? q.correctAnswerFR : null},
            true, ${q._ref ?? "MANUAL"}, ${null}, now(), now())`;

  if (type === "MULTIPLE_CHOICE") {
    let i = 0;
    for (const c of q.choices) {
      await sql`
        INSERT INTO "AnswerChoice" (id, "questionId", label, content, "isCorrect", "order")
        VALUES (${randomUUID()}, ${id}, ${c.label}, ${c.content}, ${c.isCorrect}, ${i})`;
      i++;
    }
  }
}

const testId = await ensureTest();
let total = 0;
for (const key of ORDER) {
  const questions = test[key];
  if (!questions) throw new Error(`missing module ${key} in ${jsonFile}`);
  const { id: moduleId, isNew } = await ensureModule(testId, key);
  if (!isNew) continue;
  let order = 1;
  for (const q of questions) await insertQuestion(moduleId, q, order++);
  total += questions.length;
  console.log(`  ${key}: inserted ${questions.length}`);
}

if (PUBLISH) {
  await sql`UPDATE "Test" SET status='PUBLISHED', "updatedAt"=now() WHERE id=${testId}`;
  console.log(`\n"${TITLE}" -> PUBLISHED`);
}

const check = await sql`
  SELECT m.subject, m."order" AS mo, m.difficulty AS mdiff, COUNT(q.id) AS n,
         COUNT(DISTINCT q.difficulty) AS distinct_q_difficulty,
         MIN(q.difficulty) AS q_difficulty
  FROM "Module" m LEFT JOIN "Question" q ON q."moduleId"=m.id
  WHERE m."testId"=${testId}
  GROUP BY m.subject, m."order", m.difficulty
  ORDER BY m.subject DESC, m."order", m.difficulty`;
console.table(check);
console.log(`inserted this run: ${total}`);
if (pgClient) await pgClient.end();
