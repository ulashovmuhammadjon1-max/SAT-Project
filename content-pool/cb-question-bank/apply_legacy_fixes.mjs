/**
 * Apply legacy_fixes.json — the last audit findings outstanding on Tests 3-5.
 *
 *     PROD_URL=… node apply_legacy_fixes.mjs           # report only
 *     PROD_URL=… node apply_legacy_fixes.mjs --apply
 *
 * Two defects, both left over from the EliteXSAT transcription:
 *
 *   underline  the stem asks about "the underlined portion" and the passage
 *              has no <u> anywhere, so the student is asked about something
 *              they cannot see. The transcript did record the span, as a
 *              trailing parenthetical note — a note is not markup.
 *   figure     the stem says "uses data from the table/graph" and there is no
 *              <table>, no <img> and no imageUrl.
 *
 * `build_legacy_fixes.py` already checks the fixes are internally well formed
 * (exactly one <u>, balanced tags, uniform table rows). What it cannot check
 * is that the row in the database is still the row the fix was written
 * against, so that check happens here, against the live value:
 *
 *   underline  stripping tags from the new passage must reproduce the current
 *              passage's text exactly — the fix adds markup and nothing else,
 *              so any difference means the passage moved on since the fix was
 *              built and the fix would silently overwrite that change;
 *   figure     the current passage's text must survive intact inside the new
 *              one, once the bracketed "[Graph/figure not available in this
 *              environment — described here for reference: …]" placeholder is
 *              removed. That placeholder is the defect: a prose summary of a
 *              chart standing in for the chart, which both describes what the
 *              student is supposed to read off the figure and sometimes leaks
 *              the answer outright. Supplying the real figure means deleting
 *              it, so the gate has to expect that one deletion — and only that
 *              one. Everything else must still survive verbatim.
 *
 * This is the project rule about matching on distinctive content rather than
 * position, applied per row and before the write rather than after — the one
 * time it was checked afterwards, an already-correct question had already been
 * overwritten.
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync } from "fs";

const APPLY = process.argv.includes("--apply");
const sql = neon(process.env.PROD_URL);
const DIR = new URL(".", import.meta.url).pathname;
const fixes = JSON.parse(readFileSync(`${DIR}/legacy_fixes.json`, "utf8"));

const text = (s) =>
  (s || "").replace(/<[^>]+>/g, "").replace(/&nbsp;/g, " ").replace(/\s+/g, " ").trim();

/** The prose stand-in a figure fix is expected to delete. */
const PLACEHOLDER = /\s*\[Graph\/figure not available in this environment[^\]]*\]/g;

let ok = [], skipped = 0;
for (const f of fixes) {
  const rows = await sql`
    SELECT q.id, q."passageId", p.content, t.title AS test, m."order" AS m_order,
           m.difficulty AS branch, q."order" AS q_order
    FROM "Question" q
    LEFT JOIN "Passage" p ON p.id = q."passageId"
    LEFT JOIN "Module" m ON m.id = q."moduleId"
    LEFT JOIN "Test" t ON t.id = m."testId"
    WHERE q.id = ${f.id}`;
  if (!rows.length) { console.log(`  MISSING  ${f.id} — no such question`); skipped++; continue; }
  const r = rows[0];
  if (!r.passageId) { console.log(`  NO PASSAGE  ${f.id}`); skipped++; continue; }

  const cur = text(r.content), next = text(f.passage);
  const curNoPlaceholder = text(r.content.replace(PLACEHOLDER, ""));
  const matches = f.kind === "underline" ? cur === next : next.includes(curNoPlaceholder);
  if (!matches) {
    console.log(`  CHANGED  ${f.id} (${r.test} M${r.m_order} ${r.branch} q${r.q_order}) — ` +
      `live passage no longer matches the fix; re-derive it before applying`);
    skipped++;
    continue;
  }
  if (r.content === f.passage) { console.log(`  already applied  ${f.id}`); skipped++; continue; }
  ok.push({ f, r });
  console.log(`  ready  ${f.kind.padEnd(9)} ${r.test} M${r.m_order} ${r.branch} q${r.q_order}`);
}

console.log(`\n${ok.length} ready, ${skipped} skipped`);
if (!APPLY || !ok.length) {
  if (!APPLY) console.log("Report only. Re-run with --apply to write them.");
  process.exit(0);
}
for (const { f, r } of ok) {
  await sql`UPDATE "Passage" SET content = ${f.passage} WHERE id = ${r.passageId}`;
}
console.log(`applied ${ok.length}`);
