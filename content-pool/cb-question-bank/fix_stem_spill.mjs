/**
 * Move passage text that spilled into the stem field back into the passage.
 *
 *     PROD_URL=… node fix_stem_spill.mjs           # report only
 *     PROD_URL=… node fix_stem_spill.mjs --apply
 *
 * Eleven questions were stored with the passage's last sentence at the front of
 * the `stem` column, the paragraph's closing `</p>` still attached to it, and
 * the passage itself left with an unclosed `<p>`:
 *
 *     passage:  <p>…participants heard 18 pairs of laughs.
 *     stem:     Analysis of the participants' evaluations prompted the team to
 *               conclude that … is universal across cultures.</p> Which
 *               potential finding, if true, would most weaken …?
 *
 * The student sees a passage that stops mid-argument and a question that opens
 * mid-sentence — and the sentence that went missing is usually the study's
 * conclusion, which is exactly the sentence the question is about. Five
 * separate explanation agents reported it independently.
 *
 * The split point is unambiguous, so no guessing is involved: everything up to
 * and including the `</p>` belongs to the passage, everything after it is the
 * question. Each row is checked to have exactly that shape before it is
 * touched — one `</p>` in the stem, no other block tags, and a passage whose
 * `<p>` count is exactly one higher than its `</p>` count. Anything else is
 * reported and skipped rather than guessed at, and afterwards both halves must
 * come out with balanced tags and no text lost.
 */
import { neon } from "@neondatabase/serverless";

const APPLY = process.argv.includes("--apply");
const sql = neon(process.env.PROD_URL);

const count = (s, re) => (s.match(re) || []).length;
const text = (s) => (s || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();

const rows = await sql`
  SELECT q.id, q.stem, q."passageId", p.content AS passage,
         t.title AS test, m."order" AS mo, m.difficulty AS br, q."order" AS qo
  FROM "Question" q
  JOIN "Module" m ON m.id = q."moduleId"
  JOIN "Test" t ON t.id = m."testId"
  LEFT JOIN "Passage" p ON p.id = q."passageId"
  WHERE m.subject = 'READING_WRITING'
    AND (q.stem LIKE '%<p>%' OR q.stem LIKE '%</p>%' OR q.stem LIKE '%<li>%')`;

const ready = [];
for (const r of rows) {
  const where = `${r.test} M${r.mo} ${r.br} q${r.qo}`;
  const shape =
    r.passage &&
    count(r.stem, /<\/p>/g) === 1 &&
    count(r.stem, /<p>/g) === 0 &&
    count(r.stem, /<(?!\/?p>)[a-z]/gi) === 0 &&
    count(r.passage, /<p>/g) === count(r.passage, /<\/p>/g) + 1;
  if (!shape) { console.log(`  SKIP  ${where} — not the simple spill shape, needs a human`); continue; }

  const cut = r.stem.indexOf("</p>");
  const spilled = r.stem.slice(0, cut).trim();
  const stem = r.stem.slice(cut + 4).trim();
  const passage = `${r.passage.trim()} ${spilled}</p>`;

  // Nothing may be lost or invented: the two halves together must still hold
  // exactly the words they held before.
  if (text(passage) + " " + text(stem) !== text(r.passage) + " " + text(r.stem)) {
    console.log(`  SKIP  ${where} — text would change, refusing`);
    continue;
  }
  if (count(passage, /<p>/g) !== count(passage, /<\/p>/g) || /<[^>]+>/.test(stem)) {
    console.log(`  SKIP  ${where} — result not clean`);
    continue;
  }
  ready.push({ r, passage, stem });
  console.log(`  ready  ${where.padEnd(24)} moves ${text(spilled).length} chars back into the passage`);
}

console.log(`\n${ready.length} of ${rows.length} ready`);
if (!APPLY || !ready.length) {
  if (!APPLY) console.log("Report only. Re-run with --apply to write them.");
  process.exit(0);
}
for (const { r, passage, stem } of ready) {
  await sql`UPDATE "Passage" SET content = ${passage} WHERE id = ${r.passageId}`;
  await sql`UPDATE "Question" SET stem = ${stem} WHERE id = ${r.id}`;
}
console.log(`applied ${ready.length}`);
