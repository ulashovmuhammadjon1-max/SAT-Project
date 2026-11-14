/**
 * Insert SPECIAL TEST (special_test.json) as a DRAFT.
 *
 *   DATABASE_URL=<target> SOURCE_URL=<production> node insert_special.mjs [--publish]
 *
 * Differences from test-21-build/insert_test.mjs:
 *  - imageUrl is written (redrawn figures as data URIs);
 *  - Module 2 Easy items are COPIES of existing database questions, read from
 *    SOURCE_URL (production) so a local dry run copies the real content. The
 *    copy brings its passage, image, choices and explanation (whyWrongJson is
 *    re-keyed to the new choice ids) and applies the repairs in `fixes`, each of
 *    which must match exactly once or the run stops before writing anything;
 *  - routing cut-offs set by the user: R&W Module 1 below 20/27 -> Easy, so
 *    74% (20/27 = 74.1% goes Hard, 19/27 = 70.4% goes Easy); Math Module 1
 *    below 19/22 -> Easy, so 86% (19/22 = 86.4% Hard, 18/22 = 81.8% Easy).
 *
 * Idempotent like the original: an existing test or module is skipped.
 * Never put a connection string in a file; pass both in the environment.
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";
import { readFileSync } from "fs";
import { randomUUID } from "crypto";
import path from "path";
import { fileURLToPath } from "url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const TITLE = "SPECIAL TEST";
const PUBLISH = process.argv.includes("--publish");
if (!process.env.DATABASE_URL || !process.env.SOURCE_URL) {
  console.error("Set DATABASE_URL (target) and SOURCE_URL (production, read-only use).");
  process.exit(1);
}

function connect(url) {
  if (/localhost|127\.0\.0\.1/.test(url)) {
    const client = new pg.Client({ connectionString: url });
    const ready = client.connect();
    const q = async (strings, ...values) => {
      await ready;
      const text = strings.reduce((a, s, i) => a + s + (i < values.length ? `$${i + 1}` : ""), "");
      return (await client.query(text, values)).rows;
    };
    q.end = () => client.end();
    return q;
  }
  const q = neon(url);
  q.end = async () => {};
  return q;
}
const sql = connect(process.env.DATABASE_URL);
const src = connect(process.env.SOURCE_URL);
console.log("target:", /localhost/.test(process.env.DATABASE_URL) ? "local" : "PRODUCTION");

const test = JSON.parse(readFileSync(path.join(HERE, "special_test.json"), "utf8"));
const domainId = Object.fromEntries((await sql`SELECT id, code FROM "Domain"`).map((d) => [d.code, d.id]));
const skillId = Object.fromEntries((await sql`SELECT id, code FROM "Skill"`).map((s) => [s.code, s.id]));

const MODULES = {
  RW_M1:    { subject: "READING_WRITING", order: 1, difficulty: "STANDARD", title: "Module 1",        time: 32, threshold: 74 },
  RW_M2E:   { subject: "READING_WRITING", order: 2, difficulty: "EASY",     title: "Module 2 (Easy)", time: 32, threshold: null },
  RW_M2H:   { subject: "READING_WRITING", order: 2, difficulty: "HARD",     title: "Module 2 (Hard)", time: 32, threshold: null },
  MATH_M1:  { subject: "MATH", order: 1, difficulty: "STANDARD", title: "Module 1",        time: 35, threshold: 86 },
  MATH_M2E: { subject: "MATH", order: 2, difficulty: "EASY",     title: "Module 2 (Easy)", time: 35, threshold: null },
  MATH_M2H: { subject: "MATH", order: 2, difficulty: "HARD",     title: "Module 2 (Hard)", time: 35, threshold: null },
};
const ORDER = ["RW_M1", "RW_M2E", "RW_M2H", "MATH_M1", "MATH_M2E", "MATH_M2H"];

/** Resolve every copied question up front, so a bad fix stops the run before any write. */
function applyFix(text, oldStr, newStr, where) {
  const n = text.split(oldStr).length - 1;
  if (n !== 1) throw new Error(`fix for ${where} matched ${n} times: ${oldStr.slice(0, 60)}`);
  return text.replace(oldStr, newStr);
}
const copies = {};
for (const key of ["RW_M2E", "MATH_M2E"]) {
  for (const item of test[key]) {
    const id = item.copyFrom;
    const [q] = await src`
      SELECT q.*, d.code AS dcode, s.code AS scode FROM "Question" q
      JOIN "Domain" d ON d.id = q."domainId" JOIN "Skill" s ON s.id = q."skillId" WHERE q.id = ${id}`;
    if (!q) throw new Error(`source question ${id} not found`);
    const [p] = q.passageId ? await src`SELECT content, "imageUrl" FROM "Passage" WHERE id = ${q.passageId}` : [null];
    const choices = await src`SELECT id, label, content, "isCorrect", "order" FROM "AnswerChoice" WHERE "questionId" = ${id} ORDER BY "order"`;
    const [e] = await src`SELECT * FROM "Explanation" WHERE "questionId" = ${id}`;
    const copy = { q, passage: p ? { ...p } : null, choices: choices.map((c) => ({ ...c })), expl: e ?? null };
    for (const [field, oldStr, newStr] of test.fixes[id] ?? []) {
      if (field === "passage") copy.passage.content = applyFix(copy.passage.content, oldStr, newStr, `${id} passage`);
      else if (field === "stem") copy.q.stem = applyFix(copy.q.stem, oldStr, newStr, `${id} stem`);
      else if (field.startsWith("choice:")) {
        const c = copy.choices.find((x) => x.label === field.slice(7));
        c.content = applyFix(c.content, oldStr, newStr, `${id} ${field}`);
      } else throw new Error(`unknown fix field ${field}`);
    }
    copies[id] = copy;
  }
}
console.log(`resolved ${Object.keys(copies).length} copied questions, ${Object.keys(test.fixes).length} with repairs`);

async function ensureTest() {
  const existing = await sql`SELECT id, status FROM "Test" WHERE title = ${TITLE}`;
  if (existing.length) {
    console.log(`"${TITLE}" already exists (${existing[0].id}, ${existing[0].status})`);
    return existing[0].id;
  }
  const id = randomUUID();
  await sql`
    INSERT INTO "Test" (id, title, description, type, status, "isAdaptive", "createdAt", "updatedAt")
    VALUES (${id}, ${TITLE}, ${"Full-length adaptive Digital SAT practice test."}, 'FULL_LENGTH', 'DRAFT', true, now(), now())`;
  console.log(`created "${TITLE}" (${id}) as DRAFT`);
  return id;
}

async function ensureModule(testId, key) {
  const c = MODULES[key];
  const existing = await sql`
    SELECT id FROM "Module" WHERE "testId" = ${testId} AND subject = ${c.subject} AND "order" = ${c.order} AND difficulty = ${c.difficulty}`;
  if (existing.length) return { id: existing[0].id, isNew: false };
  const id = randomUUID();
  await sql`
    INSERT INTO "Module" (id, "testId", subject, "order", difficulty, title, "timeLimitMinutes", "adaptiveThresholdPct")
    VALUES (${id}, ${testId}, ${c.subject}, ${c.order}, ${c.difficulty}, ${c.title}, ${c.time}, ${c.threshold})`;
  return { id, isNew: true };
}

async function insertNew(moduleId, q, order) {
  let passageId = null;
  if (q.passage) {
    passageId = randomUUID();
    await sql`INSERT INTO "Passage" (id, "moduleId", title, content, "imageUrl", source)
              VALUES (${passageId}, ${moduleId}, ${null}, ${q.passage}, ${null}, ${q._ref})`;
  }
  const dId = domainId[q.domain], sId = skillId[q.skill];
  if (!dId || !sId) throw new Error(`no Domain/Skill ${q.domain}/${q.skill}`);
  const id = randomUUID();
  await sql`
    INSERT INTO "Question" (id, "moduleId", "passageId", "domainId", "skillId", type, difficulty, stem, "imageUrl",
                            "tableData", "order", points, "correctAnswerFR", "isPublished", source, "sourceUploadId", "createdAt", "updatedAt")
    VALUES (${id}, ${moduleId}, ${passageId}, ${dId}, ${sId}, ${q.type}, ${q.difficulty}, ${q.stem}, ${q.imageUrl ?? null},
            ${null}, ${order}, 1, ${q.type === "FREE_RESPONSE" ? q.correctAnswerFR : null}, true, ${q._ref}, ${null}, now(), now())`;
  if (q.type === "MULTIPLE_CHOICE") {
    let i = 0;
    for (const c of q.choices) {
      await sql`INSERT INTO "AnswerChoice" (id, "questionId", label, content, "isCorrect", "order")
                VALUES (${randomUUID()}, ${id}, ${c.label}, ${c.content}, ${c.isCorrect}, ${i++})`;
    }
  }
}

async function insertCopy(moduleId, item, order) {
  const { q, passage, choices, expl } = copies[item.copyFrom];
  let passageId = null;
  if (passage) {
    passageId = randomUUID();
    await sql`INSERT INTO "Passage" (id, "moduleId", title, content, "imageUrl", source)
              VALUES (${passageId}, ${moduleId}, ${null}, ${passage.content}, ${passage.imageUrl}, ${"copy:" + q.id})`;
  }
  const id = randomUUID();
  await sql`
    INSERT INTO "Question" (id, "moduleId", "passageId", "domainId", "skillId", type, difficulty, stem, "imageUrl",
                            "tableData", "order", points, "correctAnswerFR", "isPublished", source, "sourceUploadId", "createdAt", "updatedAt")
    VALUES (${id}, ${moduleId}, ${passageId}, ${domainId[q.dcode]}, ${skillId[q.scode]}, ${q.type}, ${item.difficulty}, ${q.stem},
            ${q.imageUrl}, ${q.tableData ? JSON.stringify(q.tableData) : null}, ${order}, 1, ${q.correctAnswerFR}, true,
            ${"copy:" + q.id}, ${null}, now(), now())`;
  const newChoice = {};
  for (const c of choices) {
    const cid = randomUUID();
    newChoice[c.id] = cid;
    await sql`INSERT INTO "AnswerChoice" (id, "questionId", label, content, "isCorrect", "order")
              VALUES (${cid}, ${id}, ${c.label}, ${c.content}, ${c.isCorrect}, ${c.order})`;
  }
  if (expl) {
    let wrong = expl.whyWrongJson;
    if (wrong && typeof wrong === "object") {
      wrong = Object.fromEntries(Object.entries(wrong).map(([k, v]) => [newChoice[k] ?? k, v]));
    }
    await sql`
      INSERT INTO "Explanation" (id, "questionId", content, "whyCorrect", "whyWrongJson", "commonMistakes", tips, "relatedConcepts", source, "generatedAt")
      VALUES (${randomUUID()}, ${id}, ${expl.content}, ${expl.whyCorrect}, ${wrong ? JSON.stringify(wrong) : null},
              ${expl.commonMistakes}, ${expl.tips}, ${expl.relatedConcepts}, ${expl.source}, ${expl.generatedAt})`;
  }
}

const testId = await ensureTest();
for (const key of ORDER) {
  const { id: moduleId, isNew } = await ensureModule(testId, key);
  if (!isNew) { console.log(`  ${key}: exists, skipped`); continue; }
  let order = 1;
  for (const q of test[key]) {
    if (q.copyFrom) await insertCopy(moduleId, q, order++);
    else await insertNew(moduleId, q, order++);
  }
  console.log(`  ${key}: inserted ${test[key].length}`);
}
if (PUBLISH) {
  await sql`UPDATE "Test" SET status = 'PUBLISHED', "updatedAt" = now() WHERE id = ${testId}`;
  console.log(`"${TITLE}" -> PUBLISHED`);
}
const check = await sql`
  SELECT m.subject, m.difficulty, m."adaptiveThresholdPct" AS cutoff, COUNT(q.id)::int AS n,
         SUM(CASE WHEN q.type = 'FREE_RESPONSE' THEN 1 ELSE 0 END)::int AS fr,
         SUM(CASE WHEN q."imageUrl" IS NOT NULL THEN 1 ELSE 0 END)::int AS images,
         MIN(q."order")::int AS first, MAX(q."order")::int AS last
  FROM "Module" m LEFT JOIN "Question" q ON q."moduleId" = m.id
  WHERE m."testId" = ${testId} GROUP BY m.subject, m."order", m.difficulty, m."adaptiveThresholdPct"
  ORDER BY m.subject DESC, m."order", m.difficulty`;
console.table(check);
console.log("test id:", testId);
await sql.end(); await src.end();
