/**
 * Replace duplicate questions a single student could meet twice in one sitting.
 *
 *     PROD_URL=… node apply_dupe_fix.mjs            # report only
 *     PROD_URL=… node apply_dupe_fix.mjs --apply
 *
 * Reads dupe_plan.json from plan_dupe_fix.py.
 *
 * Retire, never delete — students have already answered these questions and
 * `Response.questionId` has no onDelete rule, so a hard delete either fails on
 * the foreign key or destroys real attempt history. The old row keeps existing
 * with `moduleId = NULL, isPublished = false`: gone from the test, still
 * resolvable by every past Response, and reversible.
 *
 * Every replacement is gated on the row still being the row the plan was built
 * against — matched on id AND source AND slot. The project rule is to assert a
 * distinctive content match *before* writing, not after; the one time it was
 * checked afterwards an already-correct question had already been overwritten.
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync } from "fs";

const APPLY = process.argv.includes("--apply");
const sql = neon(process.env.PROD_URL);
const DIR = new URL(".", import.meta.url).pathname;
const plan = JSON.parse(readFileSync(`${DIR}/dupe_plan.json`, "utf8"));

const skills = Object.fromEntries(
  (await sql`SELECT id, code, "domainId" FROM "Skill"`).map((s) => [s.code, s])
);

let ready = [], skipped = 0;
for (const p of plan) {
  const [row] = await sql`
    SELECT q.id, q.source, q."order" AS q_order, q."moduleId", q.difficulty
    FROM "Question" q WHERE q.id = ${p.retire_id}`;
  const where = `${p.test} M${p.m_order}${p.branch} q${p.q_order}`;
  if (!row) { console.log(`  SKIP ${where} — question gone`); skipped++; continue; }
  if (row.source !== p.retire_source || row.q_order !== p.q_order ||
      row.moduleId !== p.module_id) {
    console.log(`  SKIP ${where} — row moved since the plan was built`); skipped++; continue;
  }
  const [clash] = await sql`
    SELECT id FROM "Question" WHERE "moduleId" = ${p.module_id} AND source = ${p.new_source}`;
  if (clash) { console.log(`  SKIP ${where} — replacement already in this module`); skipped++; continue; }
  if (!skills[p.skill_code]) { console.log(`  SKIP ${where} — unknown skill ${p.skill_code}`); skipped++; continue; }
  ready.push(p);
  console.log(`  ready ${where.padEnd(22)} ${p.skill_name.slice(0, 24).padEnd(24)} ` +
              `${p.was_difficulty}→${p.difficulty}  overlap ${p.overlap}` +
              (p.judge_difficulty ? "  [unlabelled]" : ""));
}

console.log(`\n${ready.length} ready, ${skipped} skipped`);
if (!APPLY || !ready.length) {
  if (!APPLY) console.log("Report only. Re-run with --apply to write them.");
  process.exit(0);
}

let done = 0;
for (const p of ready) {
  const skill = skills[p.skill_code];
  await sql`UPDATE "Question" SET "moduleId" = NULL, "isPublished" = false, "updatedAt" = NOW()
             WHERE id = ${p.retire_id}`;
  const [{ id: passageId }] = await sql`
    INSERT INTO "Passage" (id, "moduleId", content, source)
    VALUES (gen_random_uuid()::text, ${p.module_id}, ${p.passage}, ${p.new_source})
    RETURNING id`;
  const [{ id: questionId }] = await sql`
    INSERT INTO "Question" (id, "moduleId", "passageId", "domainId", "skillId", type,
                            difficulty, stem, "order", points, "isPublished", source,
                            "createdAt", "updatedAt")
    VALUES (gen_random_uuid()::text, ${p.module_id}, ${passageId}, ${skill.domainId},
            ${skill.id}, 'MULTIPLE_CHOICE', ${p.difficulty}::"QuestionDifficulty",
            ${p.stem}, ${p.q_order}, 1, true, ${p.new_source}, NOW(), NOW())
    RETURNING id`;
  for (const [i, c] of p.choices.entries()) {
    await sql`INSERT INTO "AnswerChoice" (id, "questionId", label, content, "isCorrect", "order")
              VALUES (gen_random_uuid()::text, ${questionId}, ${c.label}, ${c.content},
                      ${c.label === p.correct}, ${i})`;
  }
  // Only a real rationale ships. An empty Explanation row is worse than none:
  // it satisfies every "has an explanation" check while showing the student a
  // blank panel, and it hides the gap from the audit.
  if ((p.rationale ?? "").trim()) {
    await sql`INSERT INTO "Explanation" (id, "questionId", content, "whyCorrect", source, "generatedAt")
              VALUES (gen_random_uuid()::text, ${questionId}, ${`<p>${p.rationale}</p>`},
                      ${p.rationale}, 'MANUAL', NOW())`;
  }
  done++;
}
console.log(`retired ${done}, inserted ${done}`);
