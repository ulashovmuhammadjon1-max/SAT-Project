/**
 * Insert verified explanations into the database.
 *
 * A hand-written explanation always wins. The upsert refuses to overwrite a row
 * whose `source` is `MANUAL`, because those rows exist precisely where an
 * agent's line must not ship — a question that was rewritten after the agent
 * read it, or one where adjudication found the agent's answer wrong. Without
 * that guard the agent's line silently replaced a rewritten question's
 * explanation while leaving `source = 'MANUAL'` in place, since the DO UPDATE
 * never touched `source`.
 *
 * Idempotent and re-runnable: it upserts on `Explanation.questionId`, which is
 * unique, and it can be run repeatedly while agents are still working — each
 * run picks up whatever has landed on disk since the last one. That is the
 * point of running it as work arrives rather than once at the end: if the
 * session stops, everything already written is already live.
 *
 *   PROD_URL=… node insert.mjs           # report only
 *   PROD_URL=… node insert.mjs --apply
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync } from "fs";
import { readJsonl, agentNames } from "./status.mjs";
import { checkOne } from "./verify.mjs";

const DIR = new URL(".", import.meta.url).pathname;
const APPLY = process.argv.includes("--apply");
// `--only <prefix>` limits the run to one batch's agents. Without it every
// batch is re-upserted, which is harmless but needlessly slow once several
// batches exist.
const onlyIdx = process.argv.indexOf("--only");
const ONLY = onlyIdx === -1 ? null : process.argv[onlyIdx + 1];
const sql = neon(process.env.PROD_URL);

/** Assemble the student-facing HTML from the authored parts. */
function toHtml(q, e) {
  const bits = [`<p>${e.whyCorrect}</p>`];
  const wrong = Object.entries(e.whyWrong || {});
  if (wrong.length) {
    bits.push("<p><strong>Why the others are wrong</strong></p><ul>");
    for (const [label, why] of wrong) bits.push(`<li><strong>${label}.</strong> ${why}</li>`);
    bits.push("</ul>");
  }
  return bits.join("");
}

let ready = [], rejected = 0;
for (const name of agentNames()) {
  if (ONLY && !name.startsWith(ONLY)) continue;
  const slice = JSON.parse(readFileSync(`${DIR}/out/${name}.slice.json`, "utf8"));
  const byId = new Map(slice.map((q) => [q.id, q]));
  for (const e of readJsonl(`${DIR}/out/${name}.jsonl`)) {
    const q = byId.get(e.questionId);
    if (!q) { rejected++; continue; }
    // Nothing that fails the gate is ever written — a wrong explanation on a
    // live question is the failure this whole pipeline exists to prevent.
    if (checkOne(q, e).length) { rejected++; continue; }
    ready.push({ q, e });
  }
}

console.log(`${ready.length} explanations pass the gate, ${rejected} rejected`);
if (!APPLY) {
  console.log("Report only. Re-run with --apply to write them.");
  process.exit(0);
}

let written = 0;
for (const { q, e } of ready) {
  await sql.query(
    `INSERT INTO "Explanation" (id, "questionId", content, "whyCorrect", "whyWrongJson",
                                "commonMistakes", tips, source, "generatedAt")
     VALUES (gen_random_uuid()::text, $1, $2, $3, $4::jsonb, $5, $6, 'AI_GENERATED', NOW())
     ON CONFLICT ("questionId") DO UPDATE
       SET content = EXCLUDED.content, "whyCorrect" = EXCLUDED."whyCorrect",
           "whyWrongJson" = EXCLUDED."whyWrongJson", "commonMistakes" = EXCLUDED."commonMistakes",
           tips = EXCLUDED.tips, "generatedAt" = NOW()
     WHERE "Explanation".source <> 'MANUAL'`,
    [q.id, toHtml(q, e), e.whyCorrect, JSON.stringify(e.whyWrong || {}),
     e.commonMistakes ?? null, e.tips ?? null]
  );
  written++;
  if (written % 50 === 0) console.log(`  …${written}`);
}
console.log(`wrote ${written}`);
