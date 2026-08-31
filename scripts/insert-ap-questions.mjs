/**
 * Insert an authored AP question bank into the ApQuestion table.
 *
 *   PROD_URL='postgresql://...' node scripts/insert-ap-questions.mjs bank.json
 *   PROD_URL='postgresql://...' node scripts/insert-ap-questions.mjs bank.json --dry-run
 *
 * Ids are derived from (subject, topic, order), so re-running updates rows in
 * place rather than duplicating them. The sandbox blocks raw Postgres, so this
 * goes over Neon's HTTP driver like every other production script here.
 *
 * WHY THIS BATCHES. The first version issued one INSERT per question over HTTP.
 * That is fine for a 300-question economics unit and does not survive a social
 * science bank: Human Geography alone is 2,040 questions, and the same
 * one-row-per-round-trip shape already timed out at roughly 2,000 rows when the
 * LaTeX conversion script used it. Rows are sent in batches through
 * jsonb_to_recordset instead, which is one round trip per BATCH.
 *
 * A partial run is safe to repeat -- the id is a pure function of subject,
 * topic and order, and the statement upserts -- but it should not be relied on,
 * which is why validation happens over the WHOLE file before a single row is
 * written.
 */
import { neon } from "@neondatabase/serverless";
import { createHash } from "crypto";
import { readFileSync } from "fs";

const args = process.argv.slice(2);
const dryRun = args.includes("--dry-run");
const file = args.find((a) => !a.startsWith("--"));
if (!file) {
  console.error("usage: insert-ap-questions.mjs <bank.json> [--dry-run]");
  process.exit(1);
}
if (!dryRun && !process.env.PROD_URL) {
  console.error("PROD_URL is not set. Refusing to run.");
  process.exit(1);
}

const questions = JSON.parse(readFileSync(file, "utf8"));

const id = (q) =>
  "apq_" + createHash("md5").update(`${q.subject}|${q.topic}|${q.order}`).digest("hex").slice(0, 20);

// ---- validate the whole file first ------------------------------------------
// Every check that used to run inside the write loop runs here instead, so a
// bad question at index 3,000 is caught before row 1 is written rather than
// after row 2,999.
const problems = [];
const seen = new Map();
for (const q of questions) {
  const where = `${q.subject} ${q.topic} #${q.order}`;
  // Econ and the social sciences use five choices (A-E); Calculus uses four
  // (A-D), matching each exam's real format. Anything else is an authoring
  // mistake.
  if (!Array.isArray(q.choices) || (q.choices.length !== 4 && q.choices.length !== 5)) {
    problems.push(`${where}: must have four or five choices`);
  } else if (
    !Number.isInteger(q.correctIndex) ||
    q.correctIndex < 0 ||
    q.correctIndex >= q.choices.length
  ) {
    problems.push(`${where}: answer key out of range`);
  }
  if (!q.subject || !q.topic || !Number.isInteger(q.order)) {
    problems.push(`${where}: missing subject, topic or order`);
  }
  if (!q.stem || !String(q.stem).trim()) problems.push(`${where}: empty stem`);
  // The id is derived from these three fields, so a collision would make one
  // question silently overwrite another.
  const key = id(q);
  if (seen.has(key)) problems.push(`${where}: id collides with ${seen.get(key)}`);
  else seen.set(key, where);
}
if (problems.length) {
  console.error(`FAILED: ${problems.length} problem(s); nothing written.`);
  for (const p of problems.slice(0, 20)) console.error("  " + p);
  if (problems.length > 20) console.error(`  ... and ${problems.length - 20} more`);
  process.exit(1);
}

const subjects = [...new Set(questions.map((q) => q.subject))];
const topics = new Set(questions.map((q) => `${q.subject}|${q.topic}`));
console.log(
  `${questions.length} questions validated: ${subjects.join(", ")}, ${topics.size} topics, ` +
    `${seen.size} distinct ids`,
);

if (dryRun) {
  console.log("--dry-run: validated only, nothing written.");
  process.exit(0);
}

// ---- write ------------------------------------------------------------------
const sql = neon(process.env.PROD_URL);
const BATCH = 250;

const COLUMNS =
  'id text, subject text, unit int, topic text, "topicTitle" text, "order" int, ' +
  'stem text, "tableJson" text, "choicesJson" text, "correctIndex" int, explanation text';

let n = 0;
for (let i = 0; i < questions.length; i += BATCH) {
  const rows = questions.slice(i, i + BATCH).map((q) => ({
    id: id(q),
    subject: q.subject,
    unit: q.unit,
    topic: q.topic,
    topicTitle: q.topicTitle,
    order: q.order,
    stem: q.stem,
    tableJson: q.table ? JSON.stringify(q.table) : null,
    choicesJson: JSON.stringify(q.choices),
    correctIndex: q.correctIndex,
    explanation: q.explanation ?? null,
  }));
  await sql.query(
    `INSERT INTO "ApQuestion"
       (id, subject, unit, topic, "topicTitle", "order", stem, "tableJson",
        "choicesJson", "correctIndex", explanation)
     SELECT r.id, r.subject, r.unit, r.topic, r."topicTitle", r."order", r.stem,
            r."tableJson", r."choicesJson", r."correctIndex", r.explanation
     FROM jsonb_to_recordset($1::jsonb) AS r(${COLUMNS})
     ON CONFLICT (id) DO UPDATE SET
       unit = EXCLUDED.unit,
       "topicTitle" = EXCLUDED."topicTitle",
       stem = EXCLUDED.stem,
       "tableJson" = EXCLUDED."tableJson",
       "choicesJson" = EXCLUDED."choicesJson",
       "correctIndex" = EXCLUDED."correctIndex",
       explanation = EXCLUDED.explanation`,
    [JSON.stringify(rows)],
  );
  n += rows.length;
  console.log(`  ${n}/${questions.length}`);
}

// Read back only the subjects this file touched, so the summary of a 2,040-row
// Human Geography insert is not buried under every other bank in the table.
const summary = await sql.query(
  `SELECT subject, unit, topic, COUNT(*)::int AS n FROM "ApQuestion"
   WHERE subject = ANY($1) GROUP BY subject, unit, topic
   ORDER BY subject, unit, topic`,
  [subjects],
);
const total = summary.reduce((a, r) => a + r.n, 0);
console.log(`wrote ${n} questions; ${subjects.join(", ")} now holds ${total} across ${summary.length} topics`);
const short = summary.filter((r) => r.n !== 30);
if (short.length) {
  console.log(`topics not at 30 questions (${short.length}):`);
  console.log(short.map((r) => `  ${r.subject} U${r.unit} ${r.topic}: ${r.n}`).join("\n"));
}
