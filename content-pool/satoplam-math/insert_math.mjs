/**
 * Replace the Math of Tests 6-19 with the allocated SATashkent questions.
 *
 *   DATABASE_URL='postgresql://...' node insert_math.mjs [--apply] [--publish]
 *   DATABASE_URL='...' node insert_math.mjs --apply --only "Test 6"
 *
 * Without --apply it reports what it would do and writes nothing.
 *
 * The old questions are RETIRED, never deleted: `moduleId = NULL,
 * isPublished = false`. `Response.questionId` carries no onDelete rule, so a
 * hard delete either fails on the foreign key or destroys real students'
 * attempt history and makes their past results and review pages wrong.
 * Retiring leaves every past Response resolvable and is reversible, which a
 * delete is not.
 *
 * The sandbox blocks raw Postgres (5432) and allows only outbound HTTPS, so
 * production goes over Neon's HTTP API. Never put the connection string in a
 * file — pass it in the environment.
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";
import { readFileSync } from "fs";
import { randomUUID } from "crypto";
import path from "path";
import { fileURLToPath } from "url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const APPLY = process.argv.includes("--apply");
const PUBLISH = process.argv.includes("--publish");
const ONLY = process.argv.includes("--only")
  ? process.argv[process.argv.indexOf("--only") + 1] : null;

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
  console.log("driver: pg (local)");
} else {
  const n = neon(process.env.DATABASE_URL);
  sql = { query: async (t, v = []) => await n.query(t, v) };
  console.log("driver: neon HTTP (production)");
}

const tests = JSON.parse(readFileSync(path.join(HERE, "allocation.json"), "utf8"));

const domainId = Object.fromEntries(
  (await sql.query('SELECT id, code FROM "Domain"')).map((d) => [d.code, d.id]));
const skillId = Object.fromEntries(
  (await sql.query('SELECT id, code FROM "Skill"')).map((s) => [s.code, s.id]));

// The module a pick belongs to, as (order, difficulty) — Module has no name
// column, and (testId, subject, order, difficulty) is its real key.
const MOD = { M1: [1, "STANDARD"], M2E: [2, "EASY"], M2H: [2, "HARD"] };

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

let retired = 0, inserted = 0, touchedTests = 0;

for (const t of tests) {
  if (ONLY && t.title !== ONLY) continue;
  const rows = await sql.query('SELECT id, status FROM "Test" WHERE title = $1', [t.title]);
  if (!rows.length) {
    console.log(`${t.title}: NOT FOUND — skipped`);
    continue;
  }
  const testId = rows[0].id;
  console.log(`\n${t.title} (${rows[0].status})`);
  touchedTests++;

  for (const [key, m] of Object.entries(t.modules)) {
    const [order, difficulty] = MOD[key];
    const mods = await sql.query(
      `SELECT id FROM "Module"
        WHERE "testId" = $1 AND subject = 'MATH' AND "order" = $2 AND difficulty = $3`,
      [testId, order, difficulty]);
    if (!mods.length) {
      console.log(`  ${key}: module missing — skipped`);
      continue;
    }
    const moduleId = mods[0].id;

    const old = await sql.query(
      'SELECT COUNT(*)::int AS n FROM "Question" WHERE "moduleId" = $1', [moduleId]);
    console.log(`  ${key}: retiring ${old[0].n}, inserting ${m.questions.length}`);
    if (!APPLY) continue;

    await sql.query(
      `UPDATE "Question" SET "moduleId" = NULL, "isPublished" = false, "updatedAt" = now()
        WHERE "moduleId" = $1`, [moduleId]);
    retired += old[0].n;

    let n = 1;
    for (const q of m.questions) {
      const type = q.choices && q.choices.length ? "MULTIPLE_CHOICE" : "FREE_RESPONSE";
      const dId = domainId[q.domain], sId = skillId[q.skill];
      if (!dId || !sId) throw new Error(`no Domain/Skill for ${q.domain}/${q.skill}`);
      const qid = randomUUID();
      await sql.query(
        `INSERT INTO "Question" (id, "moduleId", "domainId", "skillId", type, difficulty,
                                 stem, "imageUrl", "order", points, "correctAnswerFR",
                                 "isPublished", source, "createdAt", "updatedAt")
         VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,1,$10,true,$11,now(),now())`,
        [qid, moduleId, dId, sId, type, q.difficulty, q.stem, q.imageUrl ?? null, n,
         // correctAnswerFR is a JSON-encoded ARRAY string. A bare string parses
         // to a number at grading time and crashes .some().
         type === "FREE_RESPONSE" ? JSON.stringify([String(q.answerValue)]) : null,
         q.id.startsWith("sathard") ? `SATHARD:${q.id}` : `SATMATH:${q.id}`]);

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
        [qid, explanationHtml(q), q.whyCorrect ?? null,
         JSON.stringify(q.whyWrong || {})]);

      inserted++;
      n++;
    }
  }

  if (APPLY && PUBLISH) {
    await sql.query(`UPDATE "Test" SET status='PUBLISHED', "updatedAt"=now() WHERE id=$1`, [testId]);
  }
}

console.log(`\n${APPLY ? "APPLIED" : "DRY RUN"}: ${touchedTests} tests, `
  + `retired ${retired}, inserted ${inserted}`);

if (APPLY) {
  const check = await sql.query(
    `SELECT t.title, m."order" AS mo, m.difficulty AS branch,
            COUNT(q.id)::int AS n,
            COUNT(*) FILTER (WHERE q.type = 'FREE_RESPONSE')::int AS fr,
            COUNT(*) FILTER (WHERE e.id IS NOT NULL)::int AS expl
       FROM "Test" t
       JOIN "Module" m ON m."testId" = t.id AND m.subject = 'MATH'
       LEFT JOIN "Question" q ON q."moduleId" = m.id
       LEFT JOIN "Explanation" e ON e."questionId" = q.id
      WHERE t.title = ANY($1)
      GROUP BY t.title, m."order", m.difficulty
      ORDER BY t.title, m."order", m.difficulty`,
    [tests.map((t) => t.title)]);
  console.table(check);
}

if (pgClient) await pgClient.end();
