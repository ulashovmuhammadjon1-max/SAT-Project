/**
 * Dump every question already in the production database, so a new test's
 * content can be deduped against it before insertion.
 *
 * This is the input to the duplicate check required by CLAUDE.md's standing
 * rules — new questions must not repeat an existing problem *template* with
 * only the numbers changed, and that can only be judged against the whole
 * database, not just the test being built.
 *
 * Usage (the sandbox blocks raw Postgres, so this goes over Neon's HTTP API;
 * never write the connection string into a file — pass it in the environment):
 *
 *   PRODDB='postgresql://...' node dump_existing_questions.mjs [MATH|READING_WRITING] [outfile]
 */
import { neon } from "@neondatabase/serverless";
import fs from "fs";

const subject = process.argv[2] ?? "MATH";
const outfile = process.argv[3] ?? `existing_${subject.toLowerCase()}.json`;

if (!process.env.PRODDB) {
  console.error("Set PRODDB to the production connection string.");
  process.exit(1);
}

const sql = neon(process.env.PRODDB);

const rows = await sql`
  SELECT t.title, m.subject, m."order" AS mo, m.difficulty,
         q."order" AS qo, q.type, q.stem, q."correctAnswerFR",
         d.code AS domain, s.code AS skill
  FROM "Question" q
  JOIN "Module" m ON m.id = q."moduleId"
  JOIN "Test" t   ON t.id = m."testId"
  LEFT JOIN "Domain" d ON d.id = q."domainId"
  LEFT JOIN "Skill"  s ON s.id = q."skillId"
  WHERE m.subject = ${subject}
  ORDER BY t.title, m."order", m.difficulty, q."order"`;

fs.writeFileSync(outfile, JSON.stringify(rows, null, 1));

const byTest = {};
const bySkill = {};
for (const r of rows) {
  byTest[r.title] = (byTest[r.title] ?? 0) + 1;
  bySkill[r.skill ?? "unclassified"] = (bySkill[r.skill ?? "unclassified"] ?? 0) + 1;
}
console.log(`${rows.length} ${subject} questions -> ${outfile}`);
console.log("by test: ", byTest);
console.log("by skill:", bySkill);
