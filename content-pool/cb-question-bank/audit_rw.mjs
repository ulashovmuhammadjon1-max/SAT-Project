/**
 * Audit every Reading & Writing question in a range of tests for rendering and
 * structural defects.
 *
 *   DATABASE_URL=… node audit_rw.mjs 1 15
 *
 * Checks what actually reaches a student, reading the live database rather
 * than any build file — a build file is a point-in-time snapshot and does not
 * reflect fixes applied directly to the DB afterwards.
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";

const [lo, hi] = [Number(process.argv[2] ?? 1), Number(process.argv[3] ?? 15)];
const url = process.env.DATABASE_URL;
if (!url) throw new Error("Set DATABASE_URL.");
let sql, pgc;
if (/localhost|127\.0\.0\.1/.test(url)) {
  pgc = new pg.Client({ connectionString: url }); await pgc.connect();
  sql = async (s, ...v) => (await pgc.query(s.reduce((a, x, i) => a + x + (i < v.length ? `$${i + 1}` : ""), ""), v)).rows;
} else sql = neon(url);

const titles = Array.from({ length: hi - lo + 1 }, (_, i) => `Test ${lo + i}`);
const rows = await sql`
  SELECT t.title, m."order" AS mo, m.difficulty::text AS branch, q.id, q."order" AS qorder,
         q.stem, q."imageUrl", s.code AS skill, p.content AS passage,
         (SELECT count(*) FROM "Explanation" e WHERE e."questionId" = q.id) AS expl,
         (SELECT count(*) FROM "AnswerChoice" c WHERE c."questionId" = q.id) AS nchoices,
         (SELECT count(*) FROM "AnswerChoice" c WHERE c."questionId" = q.id AND c."isCorrect") AS ncorrect,
         (SELECT count(DISTINCT lower(btrim(c.content))) FROM "AnswerChoice" c WHERE c."questionId" = q.id) AS ndistinct
    FROM "Test" t JOIN "Module" m ON m."testId" = t.id
    JOIN "Question" q ON q."moduleId" = m.id
    JOIN "Skill" s ON s.id = q."skillId"
    LEFT JOIN "Passage" p ON p.id = q."passageId"
   WHERE t.title = ANY(${titles}) AND m.subject = 'READING_WRITING'
   ORDER BY t.title, m."order", m.difficulty, q."order"`;

const findings = [];
const add = (r, kind, detail = "") =>
  findings.push({ test: r.title, mod: `M${r.mo}${r.branch[0]}`, q: Number(r.qorder), skill: r.skill, kind, detail });

const READING = new Set(["CAS-WV", "CAS-TS", "CAS-CT", "INI-CI", "INI-CE", "INI-IE"]);
const seenWriting = new Map();

for (const r of rows) {
  const text = `${r.passage ?? ""} ${r.stem ?? ""}`;

  if (Number(r.nchoices) !== 4) add(r, "choices≠4", `${r.nchoices}`);
  if (Number(r.ncorrect) !== 1) add(r, "correct≠1", `${r.ncorrect}`);
  if (Number(r.ndistinct) !== Number(r.nchoices)) add(r, "duplicate choice text");
  if (Number(r.expl) === 0) add(r, "no explanation");
  if (!r.stem?.trim()) add(r, "empty stem");
  if (!r.passage?.trim() && r.skill !== "EOI-RS") add(r, "empty passage");

  // Bulleted student notes must be real <ul><li>, never a run-on paragraph.
  if (/following notes/i.test(text) && !/<li>/i.test(text)) add(r, "notes not bulleted");

  // Any passage with no markup at all renders as one undifferentiated block;
  // multi-paragraph texts silently run together.
  if (r.passage && !/<[a-z]/i.test(r.passage)) add(r, "passage has no HTML markup");

  if (/underlined/i.test(r.stem ?? "") && !/<u>/i.test(text)) add(r, "underline stem, no <u>");
  if (/completes the text/i.test(r.stem ?? "") && !/_{3,}/.test(text)) add(r, "blank stem, no _____");
  if (r.skill === "CAS-CT" && !(/Text 1/.test(text) && /Text 2/.test(text))) add(r, "cross-text missing Text 1/2");
  // A figure counts whether it is a real <table>, an inline <img> embedded in
  // the passage, or an imageUrl on the question. The inline case is how the
  // regenerated charts ship — they are self-contained in the passage
  // deliberately, so that a chart is never rendered twice.
  if (/\b(graph|table|chart|figure)\b/i.test(r.stem ?? "") &&
      !/<table/i.test(text) && !/<img/i.test(text) && !r.imageUrl)
    add(r, "references a figure, none present");

  if (/\*[^*\n]{2,}\*/.test(text)) add(r, "markdown asterisks");
  if (/\\[A-Za-z]{2,}/.test(text)) add(r, "LaTeX macro in prose");
  for (const tag of ["u", "em", "strong", "p", "li", "ul", "table"]) {
    const o = (text.match(new RegExp(`<${tag}(?![a-z])[^>]*>`, "gi")) ?? []).length;
    const c = (text.match(new RegExp(`</${tag}>`, "gi")) ?? []).length;
    if (o !== c) add(r, `unbalanced <${tag}>`, `${o} open / ${c} close`);
  }

  // Domain-block order: no reading question after a writing question.
  const key = `${r.title}|${r.mo}|${r.branch}`;
  if (!READING.has(r.skill)) seenWriting.set(key, true);
  else if (seenWriting.get(key)) add(r, "reading question after writing block");
}

const byKind = {};
for (const f of findings) (byKind[f.kind] ??= []).push(f);
console.log(`audited ${rows.length} questions across ${titles.length} tests\n`);
if (!findings.length) console.log("no findings");
for (const [kind, list] of Object.entries(byKind).sort((a, b) => b[1].length - a[1].length)) {
  const tests = [...new Set(list.map((f) => f.test))].sort((a, b) => +a.split(" ")[1] - +b.split(" ")[1]);
  console.log(`${String(list.length).padStart(4)}  ${kind}`);
  console.log(`      tests: ${tests.join(", ")}`);
}
if (pgc) await pgc.end();
