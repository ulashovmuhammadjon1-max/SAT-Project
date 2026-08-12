/**
 * Export Tests 1–5 for explanation authoring.
 *
 * Runs once. Agents read these files instead of each hitting the database,
 * which keeps the work reproducible and lets a stopped agent resume from disk
 * without needing credentials.
 */
import { neon } from "@neondatabase/serverless";
import { writeFileSync, mkdirSync } from "fs";

const sql = neon(process.env.PROD_URL);
const OUT = new URL(".", import.meta.url).pathname;
mkdirSync(`${OUT}/input`, { recursive: true });

const tests = await sql.query(
  `SELECT id, title FROM "Test" WHERE title = ANY($1) ORDER BY title`,
  [["Test 1", "Test 2", "Test 3", "Test 4", "Test 5"]]
);

let grand = 0;
for (const t of tests) {
  const rows = await sql.query(
    `SELECT q.id, q.stem, q.type::text AS type, q.difficulty::text AS difficulty,
            q."correctAnswerFR", q."order" AS q_order, q."imageUrl",
            d.code AS domain, d.subject::text AS subject, s.code AS skill, s.name AS skill_name,
            m.subject::text AS m_subject, m."order" AS m_order, m.difficulty::text AS m_difficulty,
            p.content AS passage,
            (SELECT json_agg(json_build_object('id', c.id, 'label', c.label,
                                               'content', c.content, 'isCorrect', c."isCorrect")
                             ORDER BY c."order")
               FROM "AnswerChoice" c WHERE c."questionId" = q.id) AS choices,
            (SELECT count(*)::int FROM "Explanation" e WHERE e."questionId" = q.id) AS has_explanation
       FROM "Question" q
       JOIN "Module" m ON m.id = q."moduleId"
       JOIN "Domain" d ON d.id = q."domainId"
       JOIN "Skill"  s ON s.id = q."skillId"
       LEFT JOIN "Passage" p ON p.id = q."passageId"
      WHERE m."testId" = $1
      ORDER BY m.subject, m."order", m.difficulty, q."order"`,
    [t.id]
  );
  const slug = t.title.toLowerCase().replace(/\s+/g, "-");
  writeFileSync(`${OUT}/input/${slug}.json`, JSON.stringify({ test: t.title, testId: t.id, questions: rows }, null, 1));
  grand += rows.length;
  const math = rows.filter((r) => r.subject === "MATH").length;
  console.log(`${t.title}: ${rows.length} questions (${math} Math, ${rows.length - math} R&W), ${rows.filter(r=>r.has_explanation).length} already explained`);
}
console.log(`\ntotal: ${grand}`);
