/**
 * Settle the disputed answer keys, using two independent readings.
 *
 *     PROD_URL=… node apply_key_verdicts.mjs            # report only
 *     PROD_URL=… node apply_key_verdicts.mjs --apply
 *
 * Each of these questions was worked twice by agents who could not see the
 * stored key and could not see each other's answer:
 *
 *   round 1  the original authoring agent (sat-*.jsonl), which flagged the
 *            disagreement and had its explanation held back
 *   round 2  an adjudicator (adj-a / adj-b .jsonl), told nothing except the
 *            question
 *
 * Three outcomes, and only one of them touches a key:
 *
 *   AGREE-AGAINST-KEY   both rounds reached the same answer and it is not the
 *                       stored one. Two independent readings converging on a
 *                       third letter is the strongest evidence available that
 *                       the transcribed key is wrong. Flip the key and ship
 *                       the explanation.
 *
 *   ADJUDICATOR-BACKS-KEY  round 2 reached the stored key. The original agent
 *                       was the outlier. Leave the key alone and ship round
 *                       2's explanation, which argues for it.
 *
 *   SPLIT               the two rounds disagree with each other and neither
 *                       matches. Nothing is written. A question three readings
 *                       cannot settle is a question to look at by hand, not
 *                       one to guess at.
 *
 * Flipping a key rewrites what every future student is graded against, so it
 * happens only on convergence, never on a single opinion — and never on the
 * stored key's say-so either, which is the whole reason these were held back.
 * Past `Response` rows are left untouched: they record what the student chose,
 * and re-grading history is a separate decision from fixing the question.
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync, existsSync, readdirSync } from "fs";
import { readJsonl } from "./status.mjs";

const APPLY = process.argv.includes("--apply");
const sql = neon(process.env.PROD_URL);
const DIR = new URL(".", import.meta.url).pathname;

/** Every answer an agent recorded, keyed by question id. */
function answersFrom(prefix) {
  const out = new Map();
  for (const f of readdirSync(`${DIR}/out`)) {
    if (!f.startsWith(prefix) || !f.endsWith(".jsonl")) continue;
    for (const e of readJsonl(`${DIR}/out/${f}`)) out.set(e.questionId, e);
  }
  return out;
}

const round1 = answersFrom("sat-");
const round2 = new Map([...answersFrom("adj-a"), ...answersFrom("adj-b")]);

const slices = new Map();
for (const f of readdirSync(`${DIR}/out`)) {
  if (!f.startsWith("adj-") || !f.endsWith(".slice.json")) continue;
  for (const q of JSON.parse(readFileSync(`${DIR}/out/${f}`, "utf8"))) slices.set(q.id, q);
}

const buckets = { flip: [], keep: [], split: [], missing: [] };
for (const [id, q] of slices) {
  const a = round1.get(id), b = round2.get(id);
  if (!a || !b) { buckets.missing.push({ q }); continue; }
  const key = (q.choices.find((c) => c.isCorrect) || {}).label;
  const where = `${q.test} M${q.m_order}${q.m_difficulty} q${q.q_order}`;
  const row = { q, where, key, r1: a.answerLabel, r2: b.answerLabel, a, b };
  if (a.answerLabel === b.answerLabel && a.answerLabel !== key) buckets.flip.push(row);
  else if (b.answerLabel === key) buckets.keep.push(row);
  else buckets.split.push(row);
}

const show = (title, rows, extra = () => "") => {
  console.log(`\n${title}: ${rows.length}`);
  for (const r of rows)
    console.log(`  ${r.where.padEnd(22)} key ${r.key} · round1 ${r.r1} · round2 ${r.r2}` +
                ` ${r.b?.confidence ? `(${r.b.confidence})` : ""}${extra(r)}`);
};

show("KEY IS WRONG — both readings agree against it, flipping", buckets.flip);
show("KEY STANDS — adjudicator reached the stored answer", buckets.keep);
show("UNSETTLED — three readings, no majority; left for a human", buckets.split);
if (buckets.missing.length) console.log(`\nno adjudication yet: ${buckets.missing.length}`);

if (!APPLY) {
  console.log("\nReport only. Re-run with --apply to write.");
  process.exit(0);
}

let flipped = 0;
for (const r of buckets.flip) {
  // Gate on the stored key still being what we read, so a concurrent change
  // fails loudly instead of being silently overwritten.
  const rows = await sql`
    SELECT label, "isCorrect" FROM "AnswerChoice" WHERE "questionId" = ${r.q.id}`;
  const live = rows.find((c) => c.isCorrect)?.label;
  if (live !== r.key) { console.log(`  SKIP ${r.where} — key moved (${live})`); continue; }
  await sql`UPDATE "AnswerChoice" SET "isCorrect" = (label = ${r.r1})
             WHERE "questionId" = ${r.q.id}`;
  flipped++;
}
console.log(`\nflipped ${flipped} answer key(s)`);
console.log(`${buckets.keep.length} key(s) confirmed; their explanations ship from adj-*`);
console.log(`${buckets.split.length} left unsettled`);
