/**
 * Replace the Reading & Writing questions of one or more tests.
 *
 *   DATABASE_URL=…  node rebuild_rw.mjs rw_tests_6_10.json            # report only
 *   DATABASE_URL=…  node rebuild_rw.mjs rw_tests_6_10.json --apply
 *
 * RETIRES the old questions, it does not delete them. Students have already
 * answered these: tests 6-10's R&W carried 428 `Response` rows and 272
 * `QuestionAttempt` rows. `Response.questionId` has no `onDelete` rule, so a
 * hard delete either fails on the foreign key or — if the responses are
 * cleared first — destroys real attempt history and makes past results and
 * review pages wrong. Retiring means `moduleId = NULL, isPublished = false`:
 * the rows leave the test, every past Response still resolves, and the change
 * is reversible.
 *
 * Idempotent: a question already inserted for a module (matched on its
 * official College Board id in `Question.source`) is skipped, so an
 * interrupted run resumes instead of duplicating.
 */
import { neon } from "@neondatabase/serverless";
import pg from "pg";
import { readFileSync } from "fs";

const file = process.argv[2];
const APPLY = process.argv.includes("--apply");
if (!file) throw new Error("Usage: node rebuild_rw.mjs <tests.json> [--apply]");

const url = process.env.DATABASE_URL;
if (!url) throw new Error("Set DATABASE_URL.");

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
const done = async (code = 0) => { if (pgClient) await pgClient.end(); process.exit(code); };

const tests = JSON.parse(readFileSync(file, "utf8"));

// Domain and skill are looked up by `code`, never by display name.
const SKILL_CODE = {
  "Words in Context": "CAS-WV", "Text Structure and Purpose": "CAS-TS",
  "Cross-Text Connections": "CAS-CT", "Central Ideas and Details": "INI-CI",
  "Command of Evidence": "INI-CE", "Inferences": "INI-IE",
  "Boundaries": "SEC-BS", "Form, Structure, and Sense": "SEC-FS",
  "Transitions": "EOI-TR", "Rhetorical Synthesis": "EOI-RS",
};
const skills = Object.fromEntries(
  (await sql`SELECT id, code, "domainId" FROM "Skill"`).map((s) => [s.code, s])
);
for (const c of Object.values(SKILL_CODE)) {
  if (!skills[c]) throw new Error(`Skill code ${c} not found`);
}

let retired = 0, inserted = 0, skipped = 0;

for (const t of tests) {
  const title = `Test ${t.test}`;
  const [test] = await sql`SELECT id FROM "Test" WHERE title = ${title}`;
  if (!test) throw new Error(`${title} not found`);

  for (const m of t.modules) {
    const [mod] = await sql`
      SELECT id FROM "Module"
       WHERE "testId" = ${test.id} AND subject = 'READING_WRITING'
         AND "order" = ${m.order} AND difficulty = ${m.difficulty}::"ModuleDifficulty"`;
    if (!mod) throw new Error(`${title} module ${m.order}/${m.difficulty} not found`);

    const existing = await sql`
      SELECT id, source FROM "Question" WHERE "moduleId" = ${mod.id}`;
    const already = new Set(existing.map((r) => r.source).filter((s) => s?.startsWith("CB:")));
    const stale = existing.filter((r) => !r.source?.startsWith("CB:"));

    console.log(`${title} M${m.order}${m.difficulty[0]}: ${stale.length} to retire, ` +
                `${m.questions.filter((q) => !already.has(`CB:${q.cb_id}`)).length} to insert`);

    if (!APPLY) { retired += stale.length; continue; }

    if (stale.length) {
      // Detach and hide rather than delete — see the header.
      const ids = stale.map((r) => r.id);
      await sql`UPDATE "Question"
                   SET "moduleId" = NULL, "isPublished" = false, "updatedAt" = NOW()
                 WHERE id = ANY(${ids})`;
      retired += stale.length;
    }

    for (const q of m.questions) {
      const src = `CB:${q.cb_id}`;
      if (already.has(src)) { skipped++; continue; }
      const skill = skills[SKILL_CODE[q.skill]];

      const [{ id: passageId }] = await sql`
        INSERT INTO "Passage" (id, "moduleId", content, source)
        VALUES (gen_random_uuid()::text, ${mod.id}, ${q.passage}, ${src}) RETURNING id`;

      const [{ id: questionId }] = await sql`
        INSERT INTO "Question" (id, "moduleId", "passageId", "domainId", "skillId", type,
                                difficulty, stem, "order", points, "isPublished", source,
                                "createdAt", "updatedAt")
        VALUES (gen_random_uuid()::text, ${mod.id}, ${passageId}, ${skill.domainId}, ${skill.id},
                'MULTIPLE_CHOICE', ${q.difficulty}::"QuestionDifficulty", ${q.stem},
                ${q.order}, 1, true, ${src}, NOW(), NOW()) RETURNING id`;

      for (const [i, c] of q.choices.entries()) {
        await sql`
          INSERT INTO "AnswerChoice" (id, "questionId", label, content, "isCorrect", "order")
          VALUES (gen_random_uuid()::text, ${questionId}, ${c.label}, ${c.content},
                  ${c.label === q.correct}, ${i})`;
      }

      // The official rationale covers the credited answer and every distractor,
      // so it ships as the explanation rather than anything re-authored.
      await sql`
        INSERT INTO "Explanation" (id, "questionId", content, "whyCorrect", source, "generatedAt")
        VALUES (gen_random_uuid()::text, ${questionId}, ${`<p>${q.rationale}</p>`},
                ${q.rationale}, 'MANUAL', NOW())`;
      inserted++;
    }
  }
}

console.log(APPLY
  ? `\nretired ${retired}, inserted ${inserted}, skipped ${skipped} already present`
  : `\nReport only: ${retired} would be retired. Re-run with --apply.`);
await done();
