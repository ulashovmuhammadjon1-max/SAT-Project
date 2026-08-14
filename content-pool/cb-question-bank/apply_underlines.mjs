/**
 * Wrap the recovered underlined spans in <u> tags.
 *
 *   DATABASE_URL=… node apply_underlines.mjs underlines.json [--apply]
 *
 * Questions asking about "the underlined portion" are unanswerable without
 * this: the underline in the source PDF is a drawn line, not a font property,
 * so text extraction loses it entirely and the student sees a question
 * referring to something that is not marked.
 *
 * Each span is re-checked against the LIVE passage rather than the build file,
 * because the passages were rebuilt into HTML after the spans were recovered.
 * A span that does not occur exactly once in the current content is reported
 * and skipped, never forced. One question legitimately carries two spans.
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";
import { readFileSync } from "fs";

const file = process.argv[2];
const APPLY = process.argv.includes("--apply");
const url = process.env.DATABASE_URL;
if (!file || !url) throw new Error("Usage: DATABASE_URL=… node apply_underlines.mjs <file> [--apply]");

let sql, pgc;
if (/localhost|127\.0\.0\.1/.test(url)) {
  pgc = new pg.Client({ connectionString: url }); await pgc.connect();
  sql = async (s, ...v) => (await pgc.query(s.reduce((a, x, i) => a + x + (i < v.length ? `$${i + 1}` : ""), ""), v)).rows;
} else sql = neon(url);

// Group spans by question — one question has two underlined portions.
const bySpan = new Map();
for (const e of JSON.parse(readFileSync(file, "utf8"))) {
  if (!bySpan.has(e.cb_id)) bySpan.set(e.cb_id, []);
  bySpan.get(e.cb_id).push(e.underlined);
}

let updated = 0, skipped = 0;
for (const [cbId, spans0] of bySpan) {
  let spans = spans0;
  const rows = await sql`
    SELECT q."passageId", p.content
      FROM "Question" q JOIN "Passage" p ON p.id = q."passageId"
     WHERE q.source = ${"CB:" + cbId} AND q."moduleId" IS NOT NULL`;
  if (rows.length !== 1) { skipped++; console.log(`  ${cbId}: ${rows.length} rows, skipped`); continue; }

  let content = rows[0].content;
  if (/<u>/.test(content)) { skipped++; continue; }        // already applied

  // The stored passage is HTML-escaped, so a span containing & < or > will not
  // match verbatim — "R&B" is stored as "R&amp;B". Try the raw span first,
  // then its escaped form, and use whichever occurs exactly once.
  const esc = (t) => t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const resolved = [];
  let ok = true;
  for (const s of spans) {
    const cand = [s, esc(s)].find((c) => content.split(c).length - 1 === 1);
    if (!cand) {
      console.log(`  ${cbId}: span not found exactly once in live passage, skipped`);
      ok = false;
      break;
    }
    resolved.push(cand);
  }
  if (!ok) { skipped++; continue; }
  spans = resolved;

  // Longest first, so a shorter span nested inside a longer one cannot break
  // the wrapping of the longer one.
  for (const s of [...spans].sort((a, b) => b.length - a.length)) {
    content = content.replace(s, `<u>${s}</u>`);
  }
  if (APPLY) await sql`UPDATE "Passage" SET content = ${content} WHERE id = ${rows[0].passageId}`;
  updated++;
}
console.log(APPLY ? `underlined ${updated}, skipped ${skipped}` : `would underline ${updated}, skip ${skipped} (dry run)`);
if (pgc) await pgc.end();
