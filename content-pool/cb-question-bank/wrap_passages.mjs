/**
 * Wrap bare passage text in <p> for tests whose passages were authored rather
 * than extracted.
 *
 *   DATABASE_URL=… node wrap_passages.mjs <firstTest> <lastTest> [--apply]
 *
 * Tests 16-31 were authored directly, and most of their passages are a bare
 * prose string with no block markup at all. The Cross-Text passages and the
 * student-notes lists already carry correct structure, and some passages carry
 * an inline <u> without ever being wrapped in a paragraph.
 *
 * This ONLY adds paragraph tags around text that is not already inside a
 * block-level element. It never reflows, re-splits or rewrites the prose:
 * stripping the tags from the result must yield exactly the text that was
 * there before, and that is asserted per passage before anything is written.
 * Guessing at paragraph breaks is what split "Booker T." from "Whatley" in the
 * extracted tests, so this deliberately makes no such guess.
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";

const lo = Number(process.argv[2]), hi = Number(process.argv[3]);
const APPLY = process.argv.includes("--apply");
const url = process.env.DATABASE_URL;
if (!url || !lo || !hi) throw new Error("Usage: DATABASE_URL=… node wrap_passages.mjs <lo> <hi> [--apply]");

let sql, pgc;
if (/localhost|127\.0\.0\.1/.test(url)) {
  pgc = new pg.Client({ connectionString: url }); await pgc.connect();
  sql = async (s, ...v) => (await pgc.query(s.reduce((a, x, i) => a + x + (i < v.length ? `$${i + 1}` : ""), ""), v)).rows;
} else sql = neon(url);

const titles = Array.from({ length: hi - lo + 1 }, (_, i) => `Test ${lo + i}`);

/** Block-level elements whose content is already structured. */
const BLOCK = /<\/?(?:p|ul|ol|li|table|thead|tbody|tr|td|th|blockquote|h[1-6]|div|figure|img|br)\b[^>]*>/gi;

const strip = (s) => s.replace(/<[^>]+>/g, "").replace(/&nbsp;/g, " ").replace(/\s+/g, " ").trim();

function wrap(html) {
  // Walk the string, collecting runs of text that sit outside any block
  // element. Only those runs get a paragraph; everything already inside one is
  // copied through untouched.
  const out = [];
  let last = 0, depth = 0, buf = "";
  const flush = () => {
    const t = buf.trim();
    if (t && strip(t)) out.push(`<p>${t}</p>`);
    buf = "";
  };
  for (const m of html.matchAll(BLOCK)) {
    const tag = m[0];
    const name = tag.replace(/[<\/]/g, "").split(/[\s>]/)[0].toLowerCase();
    const closing = tag.startsWith("</");
    const between = html.slice(last, m.index);
    if (depth === 0) buf += between; else out.push(between);
    if (name === "br" || name === "img") {
      if (depth === 0) buf += tag; else out.push(tag);
      last = m.index + tag.length;
      continue;
    }
    if (!closing) {
      if (depth === 0) flush();
      out.push(tag);
      depth++;
    } else {
      depth = Math.max(0, depth - 1);
      out.push(tag);
    }
    last = m.index + tag.length;
  }
  const tail = html.slice(last);
  if (depth === 0) { buf += tail; flush(); } else out.push(tail);
  return out.join("");
}

const rows = await sql`
  SELECT p.id, p.content, t.title
    FROM "Question" q JOIN "Module" m ON m."testId" IS NOT NULL AND m.id = q."moduleId"
    JOIN "Test" t ON t.id = m."testId"
    JOIN "Passage" p ON p.id = q."passageId"
   WHERE t.title = ANY(${titles}) AND m.subject = 'READING_WRITING'`;

const seen = new Set();
let changed = 0, same = 0, refused = 0, wsOnly = 0;
for (const r of rows) {
  if (seen.has(r.id)) continue;
  seen.add(r.id);
  const next = wrap(r.content);
  if (next === r.content) { same++; continue; }
  // The only permitted difference is markup. Compared on non-whitespace
  // characters: wrapping a run of prose that sits immediately before a <table>
  // trims the single space between them, which HTML collapses anyway and no
  // reader can see. Any change to an actual character still fails here.
  const squash = (t) => strip(t).replace(/\s+/g, "");
  if (squash(next) !== squash(r.content)) {
    refused++;
    console.log(`  ${r.title} passage ${r.id}: text would change, refused`);
    continue;
  }
  if (strip(next) !== strip(r.content)) wsOnly++;
  if (APPLY) await sql`UPDATE "Passage" SET content = ${next} WHERE id = ${r.id}`;
  changed++;
}
console.log(`${seen.size} distinct passages | ${changed} ${APPLY ? "wrapped" : "would wrap"} | ${same} already fine | ${refused} refused` +
            (wsOnly ? ` | ${wsOnly} differ only by collapsible whitespace at a block boundary` : ""));
if (pgc) await pgc.end();
