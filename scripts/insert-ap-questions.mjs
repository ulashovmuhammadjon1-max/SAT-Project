/**
 * Insert an authored AP question bank into the ApQuestion table.
 *
 *   PROD_URL='postgresql://...' node scripts/insert-ap-questions.mjs bank.json
 *
 * Ids are derived from (subject, topic, order), so re-running updates rows in
 * place rather than duplicating them. The sandbox blocks raw Postgres, so this
 * goes over Neon's HTTP driver like every other production script here.
 */
import { neon } from "@neondatabase/serverless";
import { createHash } from "crypto";
import { readFileSync } from "fs";

const file = process.argv[2];
if (!file) {
  console.error("usage: insert-ap-questions.mjs <bank.json>");
  process.exit(1);
}
const sql = neon(process.env.PROD_URL);
const questions = JSON.parse(readFileSync(file, "utf8"));

const id = (q) =>
  "apq_" + createHash("md5").update(`${q.subject}|${q.topic}|${q.order}`).digest("hex").slice(0, 20);

let n = 0;
for (const q of questions) {
  if (!Array.isArray(q.choices) || q.choices.length !== 5) {
    console.error(`FAILED: ${q.topic} #${q.order} does not have five choices`);
    process.exit(1);
  }
  await sql.query(
    `INSERT INTO "ApQuestion"
       (id, subject, unit, topic, "topicTitle", "order", stem, "tableJson", "choicesJson", "correctIndex", explanation)
     VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11)
     ON CONFLICT (id) DO UPDATE SET
       unit = $3, "topicTitle" = $5, stem = $7, "tableJson" = $8,
       "choicesJson" = $9, "correctIndex" = $10, explanation = $11`,
    [
      id(q), q.subject, q.unit, q.topic, q.topicTitle, q.order, q.stem,
      q.table ? JSON.stringify(q.table) : null, JSON.stringify(q.choices),
      q.correctIndex, q.explanation,
    ],
  );
  n++;
}

const rows = await sql.query(
  `SELECT subject, unit, topic, COUNT(*)::int AS n FROM "ApQuestion"
   GROUP BY subject, unit, topic ORDER BY subject, unit, topic`,
);
console.log(`wrote ${n} questions`);
console.log(rows.map((r) => `  ${r.subject} U${r.unit} ${r.topic}: ${r.n}`).join("\n"));
