/**
 * Apply adjudicated verdicts from `verdicts-test3.json` / `verdicts-test4.json`.
 *
 * Same discipline as `fix_keys.mjs`, driven from a file instead of a literal
 * list. The choice is always fetched BY LABEL and the content assertion checked
 * against that specific row — never by searching for the substring across the
 * choice set. That matters here: one Test 3 item has "struggle" as the correct
 * choice and "struggled" / "had struggled" / "were struggling" as the other
 * three, so a substring search would match the wrong row every time.
 *
 * KEY_WRONG   → move the key; the agent's held-back explanation then ships
 *               through the normal gate once the slices are resynced.
 * KEY_RIGHT   → leave the key; write the adjudicator's replacement explanation,
 *               because the agent's argues for the wrong answer.
 * DEFECTIVE   → never applied automatically. Reported for a human decision,
 *               since a broken item needs rewriting, not re-keying.
 *
 *   PROD_URL=… node apply_verdicts.mjs verdicts-test3.json
 *   PROD_URL=… node apply_verdicts.mjs verdicts-test3.json --apply
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync } from "fs";

const DIR = new URL(".", import.meta.url).pathname;
const APPLY = process.argv.includes("--apply");
const files = process.argv.slice(2).filter((a) => a.endsWith(".json"));
if (!files.length) throw new Error("Usage: node apply_verdicts.mjs <verdicts.json…> [--apply]");
const sql = neon(process.env.PROD_URL);

const items = files.flatMap((f) => JSON.parse(readFileSync(`${DIR}/${f}`, "utf8")));
const counts = { KEY_WRONG: 0, KEY_RIGHT: 0, DEFECTIVE: 0, refused: 0 };

for (const v of items) {
  const choices = await sql`
    SELECT c.id, c.label, c.content, c."isCorrect"
      FROM "AnswerChoice" c JOIN "Question" q ON q.id = c."questionId"
     WHERE q.id LIKE ${v.id + "%"} ORDER BY c."order"`;
  if (!choices.length) { console.error(`${v.id} ${v.where}: no choices found`); counts.refused++; continue; }
  const [{ questionId }] = await sql`SELECT id AS "questionId" FROM "Question" WHERE id LIKE ${v.id + "%"}`;

  if (v.verdict === "DEFECTIVE") {
    counts.DEFECTIVE++;
    console.log(`DEFECTIVE  ${v.where}\n  ${v.reasoning}`);
    continue;
  }

  const live = choices.find((c) => c.isCorrect);
  if (!live) { console.error(`${v.id} ${v.where}: no key set`); counts.refused++; continue; }

  if (v.verdict === "KEY_RIGHT") {
    if (live.label !== v.storedKey) {
      console.error(`${v.id} ${v.where}: verdict says the stored key ${v.storedKey} is right, but live key is ${live.label} — refusing`);
      counts.refused++;
      continue;
    }
    counts.KEY_RIGHT++;
    console.log(`KEY_RIGHT  ${v.where}  (key ${live.label} stands)`);
    if (!APPLY || !v.explanation) continue;
    await writeExplanation(questionId, v.explanation);
    continue;
  }

  // KEY_WRONG
  const target = choices.find((c) => c.label === v.correctKey);
  if (!target) { console.error(`${v.id} ${v.where}: label ${v.correctKey} not present`); counts.refused++; continue; }
  if (live.label === v.correctKey) {
    console.log(`already fixed  ${v.where}  (key is ${v.correctKey})`);
    continue;
  }
  if (live.label !== v.storedKey) {
    console.error(`${v.id} ${v.where}: expected stored key ${v.storedKey} but found ${live.label} — refusing`);
    counts.refused++;
    continue;
  }
  if (v.expect && !target.content.includes(v.expect)) {
    console.error(`${v.id} ${v.where}: choice ${v.correctKey} does not contain "${v.expect}" — refusing`);
    console.error(`  it reads: ${target.content.replace(/<[^>]+>/g, "").slice(0, 90)}`);
    counts.refused++;
    continue;
  }

  counts.KEY_WRONG++;
  console.log(`KEY_WRONG  ${v.where}  ${v.storedKey} -> ${v.correctKey}  ${target.content.replace(/<[^>]+>/g, "").slice(0, 60)}`);
  if (!APPLY) continue;

  await sql`UPDATE "AnswerChoice" SET "isCorrect" = false WHERE id = ${live.id}`;
  await sql`UPDATE "AnswerChoice" SET "isCorrect" = true  WHERE id = ${target.id}`;
  const after = await sql`
    SELECT label FROM "AnswerChoice" WHERE "questionId" = ${questionId} AND "isCorrect"`;
  if (after.length !== 1 || after[0].label !== v.correctKey) {
    throw new Error(`${v.id}: after update the key is ${JSON.stringify(after)} — expected ${v.correctKey}`);
  }
  if (v.explanation) await writeExplanation(questionId, v.explanation);
}

async function writeExplanation(questionId, e) {
  const bits = [`<p>${e.whyCorrect}</p>`];
  if (e.whyWrong && Object.keys(e.whyWrong).length) {
    bits.push("<p><strong>Why the others are wrong</strong></p><ul>");
    for (const [label, why] of Object.entries(e.whyWrong)) bits.push(`<li><strong>${label}.</strong> ${why}</li>`);
    bits.push("</ul>");
  }
  await sql`
    INSERT INTO "Explanation" (id, "questionId", content, "whyCorrect", "whyWrongJson",
                               "commonMistakes", tips, source, "generatedAt")
    VALUES (gen_random_uuid()::text, ${questionId}, ${bits.join("")}, ${e.whyCorrect},
            ${JSON.stringify(e.whyWrong ?? {})}::jsonb, ${e.commonMistakes ?? null}, ${e.tips ?? null},
            'MANUAL', NOW())
    ON CONFLICT ("questionId") DO UPDATE
      SET content = EXCLUDED.content, "whyCorrect" = EXCLUDED."whyCorrect",
          "whyWrongJson" = EXCLUDED."whyWrongJson", "commonMistakes" = EXCLUDED."commonMistakes",
          tips = EXCLUDED.tips, source = 'MANUAL', "generatedAt" = NOW()`;
}

console.log(
  `\n${items.length} verdicts: ${counts.KEY_WRONG} key moved, ${counts.KEY_RIGHT} key kept, ` +
    `${counts.DEFECTIVE} defective (not applied), ${counts.refused} refused`
);
if (!APPLY) console.log("Report only. Re-run with --apply.");
