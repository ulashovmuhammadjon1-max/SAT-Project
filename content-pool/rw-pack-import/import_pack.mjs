/**
 * Import a large batch of Reading & Writing questions into its own named
 * collection, kept distinguishable from everything already in the bank.
 *
 * Separation is structural, not cosmetic. Every row written here carries a
 * `collectionId` pointing at one `QuestionCollection`; nothing already in the
 * database has one. So "the original bank" is exactly `collectionId IS NULL`,
 * the admin bank filters on it, and the whole batch can be published, hidden
 * or deleted as a unit without touching a single pre-existing question.
 *
 * Everything lands UNPUBLISHED. A transcribed R&W batch has never once been
 * safe to trust on arrival -- see CLAUDE.md: 6 of 81 keys wrong in Test 5,
 * 44 wrong across Tests 3-4. Publishing is a separate, deliberate step after
 * the answer audit, and `--publish` is what does it.
 *
 *   node import_pack.mjs --slug rw-pack-2026            # validate + report
 *   node import_pack.mjs --slug rw-pack-2026 --apply    # write, unpublished
 *   node import_pack.mjs --slug rw-pack-2026 --publish  # flip the batch live
 *
 * Local dev reads DATABASE_URL. Production reads PROD_URL, over Neon's HTTP
 * driver, because this sandbox blocks raw Postgres on 5432.
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";
import { readFileSync, readdirSync, existsSync } from "fs";

const DIR = new URL(".", import.meta.url).pathname;
const argv = process.argv.slice(2);
const flag = (name, fallback = undefined) => {
  const i = argv.indexOf(`--${name}`);
  return i === -1 ? fallback : argv[i + 1];
};
const APPLY = argv.includes("--apply");
const PUBLISH = argv.includes("--publish");

const SLUG = flag("slug");
if (!SLUG) throw new Error("Usage: node import_pack.mjs --slug <collection-slug> [--apply|--publish]");

const url = process.env.PROD_URL ?? process.env.DATABASE_URL;
if (!url) throw new Error("Set PROD_URL (production) or DATABASE_URL (local dev).");

// Same dual-driver arrangement as `insert_test.mjs`: Neon's HTTP driver is the
// only thing that reaches production from this sandbox (raw 5432 is blocked),
// but it cannot talk to a local Postgres, so local dev goes over pg.
let sql, pgClient;
if (/localhost|127\.0\.0\.1/.test(url)) {
  pgClient = new pg.Client({ connectionString: url });
  await pgClient.connect();
  sql = async (strings, ...values) => {
    const text = strings.reduce((a, s, i) => a + s + (i < values.length ? `$${i + 1}` : ""), "");
    return (await pgClient.query(text, values)).rows;
  };
  console.log("driver: pg (local)");
} else {
  sql = neon(url);
  console.log("driver: neon HTTP (production)");
}
const finish = async (code = 0) => {
  if (pgClient) await pgClient.end();
  process.exit(code);
};

/* -------------------------------------------------------------------------- */
/* Collection                                                                  */
/* -------------------------------------------------------------------------- */

const metaPath = `${DIR}/${SLUG}/collection.json`;
if (!existsSync(metaPath)) throw new Error(`No collection.json at ${metaPath}`);
const meta = JSON.parse(readFileSync(metaPath, "utf8"));

/* -------------------------------------------------------------------------- */
/* Load and validate                                                           */
/* -------------------------------------------------------------------------- */

const batchDir = `${DIR}/${SLUG}/batches`;
const files = existsSync(batchDir)
  ? readdirSync(batchDir).filter((f) => f.endsWith(".json")).sort()
  : [];
const items = files.flatMap((f) => {
  const parsed = JSON.parse(readFileSync(`${batchDir}/${f}`, "utf8"));
  if (!Array.isArray(parsed)) throw new Error(`${f}: expected a top-level array`);
  return parsed.map((q) => ({ ...q, _file: f }));
});

// Domain and skill are looked up by `code`, never by `name` -- name is a
// display string and a phrasing drift would silently create a mismatch.
const domains = Object.fromEntries(
  (await sql`SELECT id, code FROM "Domain"`).map((d) => [d.code, d.id])
);
const skills = Object.fromEntries(
  (await sql`SELECT id, code, "domainId" FROM "Skill"`).map((s) => [s.code, s])
);

const problems = [];
const seenRefs = new Set();
const seenKeys = new Map();

// Exact-text collision against the existing bank. A pack of this size WILL
// overlap material already shipped, and a student meeting the same question
// twice under two different collections is the failure this catches.
//
// Keyed on PASSAGE + stem, never the stem alone. R&W stems are boilerplate --
// "Which choice completes the text with the most logical and precise word or
// phrase?" is shared by every Words-in-Context question in the database -- so a
// stem-only key flags all ~1,800 as duplicates and the check becomes noise you
// learn to ignore. The passage is what actually identifies the question.
//
// This collection's own rows are excluded. Without that, a resumed run sees the
// questions it wrote on the first pass, calls them duplicates, and refuses to
// write the rest -- which would destroy the resumability that is the whole
// reason this is idempotent at 1,800 questions.
const bankKeys = new Set(
  (
    await sql`SELECT q.stem, p.content AS passage
                FROM "Question" q
                LEFT JOIN "Passage" p ON p.id = q."passageId"
                WHERE q."collectionId" IS NULL
                   OR q."collectionId" <> COALESCE(
                        (SELECT id FROM "QuestionCollection" WHERE slug = ${SLUG}), '')`
  ).map((r) => dupeKey(r.passage, r.stem))
);

function dupeKey(passage, stem) {
  return `${normalise(passage ?? "")}||${normalise(stem ?? "")}`;
}

function normalise(html) {
  return html
    .replace(/<[^>]+>/g, " ")
    .replace(/&nbsp;/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}

for (const q of items) {
  const at = `${q._file}:${q.ref ?? "<no ref>"}`;

  if (!q.ref) problems.push(`${at}: missing ref`);
  if (seenRefs.has(q.ref)) problems.push(`${at}: duplicate ref within the import`);
  seenRefs.add(q.ref);

  if (!q.stem?.trim()) problems.push(`${at}: empty stem`);
  if (!["EASY", "MEDIUM", "HARD"].includes(q.difficulty)) problems.push(`${at}: bad difficulty`);

  if (!skills[q.skillCode]) problems.push(`${at}: unknown skill code ${q.skillCode}`);
  else if (!domains[q.domainCode]) problems.push(`${at}: unknown domain code ${q.domainCode}`);
  else if (skills[q.skillCode].domainId !== domains[q.domainCode])
    problems.push(`${at}: skill ${q.skillCode} does not belong to domain ${q.domainCode}`);

  const choices = q.choices ?? [];
  if (choices.length !== 4) problems.push(`${at}: ${choices.length} choices, expected 4`);
  if (choices.filter((c) => c.isCorrect).length !== 1)
    problems.push(`${at}: expected exactly 1 correct choice`);
  if (new Set(choices.map((c) => normalise(c.content))).size !== choices.length)
    problems.push(`${at}: two choices with the same text`);
  if (choices.some((c) => !c.content?.trim())) problems.push(`${at}: empty choice text`);
  if (choices.map((c) => c.label).join("") !== "ABCD")
    problems.push(`${at}: choice labels must be A,B,C,D in order`);

  // A fill-in-the-blank stem needs its blank, or the question is unanswerable.
  if (/completes the text/i.test(q.stem) && !/_{3,}/.test(`${q.passage ?? ""}${q.stem}`))
    problems.push(`${at}: Words-in-Context question with no _____ blank`);

  // An "underlined portion" question needs real <u> markup, not a description.
  if (/underlined/i.test(q.stem) && !/<u>/.test(`${q.passage ?? ""}${q.stem}`))
    problems.push(`${at}: mentions an underlined portion but has no <u> markup`);

  // Cross-text items keep both texts in ONE passage row.
  if (q.skillCode === "CAS-CT" && !(/Text 1/.test(q.passage ?? "") && /Text 2/.test(q.passage ?? "")))
    problems.push(`${at}: cross-text question missing Text 1 / Text 2`);

  // If the stem points at a figure, one has to exist.
  if (/\b(graph|table|chart|figure)\b/i.test(q.stem) && !/<table/.test(q.passage ?? "") && !q.imageUrl)
    problems.push(`${at}: stem references a graph/table/figure with neither <table> nor imageUrl`);

  const prose = [q.stem, q.passage ?? "", ...choices.map((c) => c.content)].join(" ");
  // R&W is prose. A backslash macro here is a stray LaTeX escape and renders
  // as a literal backslash.
  if (/\\[A-Za-z]+/.test(prose)) problems.push(`${at}: LaTeX macro in R&W prose`);
  // Markdown asterisks render literally -- italics are <em>.
  if (/\*[^*\n]+\*/.test(prose)) problems.push(`${at}: markdown asterisks, use <em>`);
  // Unbalanced tags. Explicit lookahead on the letter so <ul> is not counted
  // as a <u> -- the exact substring bug CLAUDE.md warns about.
  for (const tag of ["u", "em", "strong", "p", "li", "ul", "table"]) {
    const open = (prose.match(new RegExp(`<${tag}(?![a-z])[^>]*>`, "gi")) ?? []).length;
    const close = (prose.match(new RegExp(`</${tag}>`, "gi")) ?? []).length;
    if (open !== close) problems.push(`${at}: ${open} <${tag}> vs ${close} </${tag}>`);
  }

  const key = dupeKey(q.passage, q.stem);
  if (bankKeys.has(key)) problems.push(`${at}: passage + stem already in the bank verbatim`);
  // Within the pack too: a 1,800-question source recycles its own material.
  if (seenKeys.has(key)) problems.push(`${at}: duplicates ${seenKeys.get(key)} inside this import`);
  else seenKeys.set(key, q.ref);
}

if (problems.length) {
  console.error(problems.slice(0, 200).join("\n"));
  if (problems.length > 200) console.error(`… and ${problems.length - 200} more`);
  throw new Error(`${problems.length} problems across ${items.length} questions; nothing written`);
}

console.log(`${items.length} questions validated across ${files.length} file(s).`);

/* -------------------------------------------------------------------------- */
/* Publish-only mode                                                           */
/* -------------------------------------------------------------------------- */

if (PUBLISH) {
  const rows = await sql`
    UPDATE "Question" SET "isPublished" = true, "updatedAt" = NOW()
     WHERE "collectionId" = (SELECT id FROM "QuestionCollection" WHERE slug = ${SLUG})
     RETURNING id`;
  console.log(`published ${rows.length} questions in ${SLUG}`);
  await finish();
}

if (!APPLY) {
  console.log("Report only. Re-run with --apply to write them (unpublished).");
  await finish();
}

/* -------------------------------------------------------------------------- */
/* Write                                                                       */
/* -------------------------------------------------------------------------- */

await sql`
  INSERT INTO "QuestionCollection" (id, name, slug, description, origin, "order", "createdAt", "updatedAt")
  VALUES (gen_random_uuid()::text, ${meta.name}, ${SLUG}, ${meta.description ?? null},
          ${meta.origin ?? null}, ${meta.order ?? 0}, NOW(), NOW())
  ON CONFLICT (slug) DO UPDATE
    SET name = EXCLUDED.name, description = EXCLUDED.description,
        origin = EXCLUDED.origin, "updatedAt" = NOW()`;

const [{ id: collectionId }] =
  await sql`SELECT id FROM "QuestionCollection" WHERE slug = ${SLUG}`;

// Idempotent by ref, so an interrupted run resumes instead of duplicating.
// 1,800 questions is far past the point where a single failure can be allowed
// to mean starting over.
const done = new Set(
  (await sql`SELECT source FROM "Question" WHERE "collectionId" = ${collectionId}`)
    .map((r) => r.source)
    .filter(Boolean)
);
const todo = items.filter((q) => !done.has(`${SLUG}:${q.ref}`));
console.log(`${done.size} already imported, ${todo.length} to write`);

let n = 0;
for (const q of todo) {
  let passageId = null;
  if (q.passage?.trim()) {
    [{ id: passageId }] = await sql`
      INSERT INTO "Passage" (id, title, content, "imageUrl", source)
      VALUES (gen_random_uuid()::text, ${q.passageTitle ?? null}, ${q.passage},
              ${q.passageImageUrl ?? null}, ${`${SLUG}:${q.ref}`})
      RETURNING id`;
  }

  const [{ id: questionId }] = await sql`
    INSERT INTO "Question" (id, "collectionId", "passageId", "domainId", "skillId", type,
                            difficulty, stem, "imageUrl", "order", points, "isPublished",
                            source, "createdAt", "updatedAt")
    VALUES (gen_random_uuid()::text, ${collectionId}, ${passageId}, ${domains[q.domainCode]},
            ${skills[q.skillCode].id}, 'MULTIPLE_CHOICE',
            ${q.difficulty}::"QuestionDifficulty", ${q.stem}, ${q.imageUrl ?? null},
            ${q.order ?? 0}, 1, false, ${`${SLUG}:${q.ref}`}, NOW(), NOW())
    RETURNING id`;

  for (const [i, c] of q.choices.entries()) {
    await sql`
      INSERT INTO "AnswerChoice" (id, "questionId", label, content, "isCorrect", "order")
      VALUES (gen_random_uuid()::text, ${questionId}, ${c.label}, ${c.content}, ${c.isCorrect}, ${i})`;
  }

  if (q.whyCorrect) {
    await sql`
      INSERT INTO "Explanation" (id, "questionId", content, "whyCorrect", "whyWrongJson",
                                 "commonMistakes", tips, source, "generatedAt")
      VALUES (gen_random_uuid()::text, ${questionId},
              ${`<p>${q.whyCorrect}</p>`}, ${q.whyCorrect},
              ${JSON.stringify(q.whyWrong ?? {})}::jsonb,
              ${q.commonMistakes ?? null}, ${q.tips ?? null}, 'MANUAL', NOW())`;
  }

  if (++n % 50 === 0) console.log(`  … ${n}/${todo.length}`);
}

console.log(`inserted ${n} questions into "${meta.name}" (${SLUG}), all unpublished.`);
console.log(`Review, run the answer audit, then: node import_pack.mjs --slug ${SLUG} --publish`);
await finish();
