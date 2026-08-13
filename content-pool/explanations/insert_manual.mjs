/**
 * Insert hand-written explanations for questions the gate correctly held back.
 *
 * Two outcomes are possible when an agent's answer disagrees with the key.
 * Where adjudication finds the AGENT right, `fix_keys.mjs` corrects the key and
 * the agent's own explanation ships through the normal pipeline. Where it finds
 * the KEY right, the agent's explanation argues for the wrong answer and must
 * never ship — so the explanation is written by hand here instead.
 *
 * Guard: each entry names the answer letter it was written for, and the insert
 * is refused unless that letter is the live key. This is what stops a
 * hand-written explanation from being attached to a question whose key later
 * moved underneath it.
 *
 *   PROD_URL=… node insert_manual.mjs           # report only
 *   PROD_URL=… node insert_manual.mjs --apply
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync } from "fs";

const DIR = new URL(".", import.meta.url).pathname;
const APPLY = process.argv.includes("--apply");
const sql = neon(process.env.PROD_URL);
const items = JSON.parse(readFileSync(`${DIR}/manual.json`, "utf8"));

function toHtml(e) {
  const bits = [`<p>${e.whyCorrect}</p>`, "<p><strong>Why the others are wrong</strong></p><ul>"];
  for (const [label, why] of Object.entries(e.whyWrong)) bits.push(`<li><strong>${label}.</strong> ${why}</li>`);
  bits.push("</ul>");
  return bits.join("");
}

let ok = 0;
for (const e of items) {
  const choices = await sql`
    SELECT label, content, "isCorrect" FROM "AnswerChoice"
     WHERE "questionId" = ${e.questionId} ORDER BY "order"`;
  if (!choices.length) { console.error(`${e.where}: question not found`); continue; }

  const key = choices.find((c) => c.isCorrect);
  if (!key) { console.error(`${e.where}: no key set`); continue; }
  if (key.label !== e.answerLabel) {
    console.error(`${e.where}: written for ${e.answerLabel} but the live key is ${key.label} — refusing`);
    continue;
  }
  if (e.expect && !key.content.includes(e.expect)) {
    console.error(`${e.where}: key ${key.label} does not contain "${e.expect}" — refusing`);
    continue;
  }
  // Every distractor needs its own reason.
  const missing = choices.filter((c) => !c.isCorrect && !e.whyWrong?.[c.label]?.trim()).map((c) => c.label);
  if (missing.length) { console.error(`${e.where}: no whyWrong for ${missing.join(", ")}`); continue; }

  console.log(`${e.where}  key ${key.label} confirmed`);
  ok++;
  if (!APPLY) continue;

  await sql`
    INSERT INTO "Explanation" (id, "questionId", content, "whyCorrect", "whyWrongJson",
                               "commonMistakes", tips, source, "generatedAt")
    VALUES (gen_random_uuid()::text, ${e.questionId}, ${toHtml(e)}, ${e.whyCorrect},
            ${JSON.stringify(e.whyWrong)}::jsonb, ${e.commonMistakes ?? null}, ${e.tips ?? null},
            'MANUAL', NOW())
    ON CONFLICT ("questionId") DO UPDATE
      SET content = EXCLUDED.content, "whyCorrect" = EXCLUDED."whyCorrect",
          "whyWrongJson" = EXCLUDED."whyWrongJson", "commonMistakes" = EXCLUDED."commonMistakes",
          tips = EXCLUDED.tips, "generatedAt" = NOW()`;
}

console.log(`${ok}/${items.length} ready`);
if (!APPLY) console.log("Report only. Re-run with --apply.");
