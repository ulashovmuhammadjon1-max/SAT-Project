/**
 * Refresh the answer keys inside the agent slice files from the live database.
 *
 * `insert.mjs` runs its gate against the slice, not against production — the
 * slice is the snapshot the agent actually worked from. That is the right
 * default (it makes a run reproducible), but it means correcting a key in the
 * database does NOT release the explanation that was held back for disagreeing
 * with the old key: the stale slice still carries the old key and the gate
 * still rejects. This resyncs the `choices` and `correctAnswerFR` of every
 * question in every slice, so a key fix takes effect on the next insert.
 *
 * It only ever rewrites the key fields. Stems, passages and ids are left alone,
 * so a slice cannot silently acquire different content than the agent read.
 *
 *   PROD_URL=… node resync_slices.mjs           # report only
 *   PROD_URL=… node resync_slices.mjs --apply
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync, writeFileSync } from "fs";
import { agentNames } from "./status.mjs";

const DIR = new URL(".", import.meta.url).pathname;
const APPLY = process.argv.includes("--apply");
const sql = neon(process.env.PROD_URL);

let changed = 0;
for (const name of agentNames()) {
  const path = `${DIR}/out/${name}.slice.json`;
  const slice = JSON.parse(readFileSync(path, "utf8"));
  let touched = 0;

  // One query per slice rather than per question — these are large files.
  const live = await sql.query(
    `SELECT q.id, q."correctAnswerFR",
            (SELECT json_agg(json_build_object('id', c.id, 'label', c.label,
                                               'content', c.content, 'isCorrect', c."isCorrect")
                             ORDER BY c."order")
               FROM "AnswerChoice" c WHERE c."questionId" = q.id) AS choices
       FROM "Question" q WHERE q.id = ANY($1)`,
    [slice.map((q) => q.id)]
  );
  const byId = new Map(live.map((r) => [r.id, r]));

  for (const q of slice) {
    const l = byId.get(q.id);
    if (!l) continue;
    const before = JSON.stringify([q.choices, q.correctAnswerFR]);
    const after = JSON.stringify([l.choices, l.correctAnswerFR]);
    if (before === after) continue;
    const oldKey = (q.choices ?? []).find((c) => c.isCorrect)?.label;
    const newKey = (l.choices ?? []).find((c) => c.isCorrect)?.label;
    console.log(`  ${name} ${q.id.slice(0, 8)} ${oldKey ?? q.correctAnswerFR} -> ${newKey ?? l.correctAnswerFR}`);
    q.choices = l.choices;
    q.correctAnswerFR = l.correctAnswerFR;
    touched++;
  }

  if (touched) {
    changed += touched;
    if (APPLY) writeFileSync(path, JSON.stringify(slice, null, 1));
  }
}

console.log(`${changed} question keys out of date`);
if (!APPLY && changed) console.log("Report only. Re-run with --apply.");
