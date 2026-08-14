/**
 * Repair quotation marks that arrived from the source PDFs as apostrophes.
 *
 *     PROD_URL=… node fix_quote_glyphs.mjs            # report only
 *     PROD_URL=… node fix_quote_glyphs.mjs --apply
 *
 * The SAToplam books typeset some quoted phrases with a glyph whose text-layer
 * mapping is U+2019, so a passage reads
 *
 *     praising the former as ’especially pointed’
 *
 * where the real text is a double-quoted phrase. It is the same class of
 * text-layer defect as the apostrophe problem documented for `pdftotext
 * -layout`, and it reaches the student — the quoted phrase is often the exact
 * word a Words-in-Context question turns on.
 *
 * The evidence that these are not real single quotes: a genuine typeset pair
 * opens with U+2018 and closes with U+2019, and U+2018 appears in only 4 of
 * 1,254 records while these both-ends-U+2019 pairs appear in 29. The books also
 * use real double quotes elsewhere (33 curly, 212 straight), so the pair is an
 * encoding artifact, not the author's punctuation.
 *
 * ── Why the pattern is this fussy ─────────────────────────────────────────
 * An apostrophe and a closing quote are the same character, so a loose pattern
 * eats possessives and elisions — the recurring own-goal this project keeps
 * relearning (`\bpi`, `LETTER_REF`, the "fen" inside "fence"). Three
 * constraints keep it honest:
 *
 *   - the opening mark must follow whitespace, `(` or `>` — a possessive never
 *     does, because it is always attached to the end of a word;
 *   - it must not be followed by a digit, which is what an elided year looks
 *     like ("the 1950s and ’60s");
 *   - the closing mark must be followed by punctuation, whitespace or `<`.
 *
 * Every one of the 36 spans this matched across the SAToplam set was checked by
 * eye and every one is a quotation. It is still gated: each row asserts that
 * the rewrite changed nothing but quote characters before it is written.
 */
import { neon } from "@neondatabase/serverless";

const APPLY = process.argv.includes("--apply");
const sql = neon(process.env.PROD_URL);

const QUOTED = /(?<=[\s(>])’(?!\d)([^’‘<>]{2,200})’(?=[\s.,;:)!?]|<|$)/g;

const fix = (s) => (s || "").replace(QUOTED, (_, inner) => `“${inner}”`);

/** A rewrite may only ever change quote characters. */
function safe(before, after) {
  const strip = (s) => s.replace(/[’“”]/g, "");
  return strip(before) === strip(after);
}

const rows = await sql`
  SELECT q.id AS qid, q.stem, q.source, q."passageId", p.content AS passage,
         t.title AS test
  FROM "Question" q
  LEFT JOIN "Passage" p ON p.id = q."passageId"
  LEFT JOIN "Module" m ON m.id = q."moduleId"
  LEFT JOIN "Test" t ON t.id = m."testId"
  WHERE q."moduleId" IS NOT NULL AND m.subject = 'READING_WRITING'
`;

const passageEdits = new Map(); // passageId -> new content
const stemEdits = [];
const choiceEdits = [];
const byTest = {};

for (const r of rows) {
  if (r.passage && r.passageId) {
    const next = fix(r.passage);
    if (next !== r.passage) {
      if (!safe(r.passage, next)) throw new Error(`unsafe passage rewrite on ${r.qid}`);
      passageEdits.set(r.passageId, next);
      byTest[r.test] = (byTest[r.test] || 0) + 1;
    }
  }
  const nextStem = fix(r.stem);
  if (nextStem !== r.stem) {
    if (!safe(r.stem, nextStem)) throw new Error(`unsafe stem rewrite on ${r.qid}`);
    stemEdits.push({ id: r.qid, stem: nextStem });
    byTest[r.test] = (byTest[r.test] || 0) + 1;
  }
}

const choices = await sql`
  SELECT c.id, c.content, t.title AS test
  FROM "AnswerChoice" c
  JOIN "Question" q ON q.id = c."questionId"
  JOIN "Module" m ON m.id = q."moduleId"
  JOIN "Test" t ON t.id = m."testId"
  WHERE m.subject = 'READING_WRITING'
`;
for (const c of choices) {
  const next = fix(c.content);
  if (next !== c.content) {
    if (!safe(c.content, next)) throw new Error(`unsafe choice rewrite on ${c.id}`);
    choiceEdits.push({ id: c.id, content: next });
    byTest[c.test] = (byTest[c.test] || 0) + 1;
  }
}

console.log(`${passageEdits.size} passages, ${stemEdits.length} stems, ${choiceEdits.length} choices to repair`);
for (const [test, n] of Object.entries(byTest).sort()) console.log(`  ${test.padEnd(10)} ${n}`);

if (!APPLY) {
  console.log("\nReport only. Re-run with --apply to write them.");
  process.exit(0);
}

for (const [id, content] of passageEdits) {
  await sql`UPDATE "Passage" SET content = ${content} WHERE id = ${id}`;
}
for (const e of stemEdits) {
  await sql`UPDATE "Question" SET stem = ${e.stem} WHERE id = ${e.id}`;
}
for (const e of choiceEdits) {
  await sql`UPDATE "AnswerChoice" SET content = ${e.content} WHERE id = ${e.id}`;
}
console.log(`applied ${passageEdits.size + stemEdits.length + choiceEdits.length} rewrites`);
