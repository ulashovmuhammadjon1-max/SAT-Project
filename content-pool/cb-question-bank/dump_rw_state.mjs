/**
 * Snapshot every Tests 16-31 R&W question for the duplicate planner.
 *
 *     PROD_URL=… node dump_rw_state.mjs > rw_state.json
 *
 * The planner scores candidate replacements against what is actually live, not
 * against the allocation file that produced it — the two have since diverged
 * through the quote, stem-spill and splice repairs.
 *
 * The test-number filter is applied in JS rather than as a `regexp_replace(…,
 * '\D', …)::int` in SQL: a `\D` inside a JS template literal is just `D`, so
 * the pattern silently became "strip the letter D" and Postgres was handed
 * "Test 20" to cast to an integer. Same family as every other escape bug in
 * this project — it looked right and quietly did something else.
 */
import { neon } from "@neondatabase/serverless";
const sql = neon(process.env.PROD_URL);

const rows = await sql`
  SELECT q.id, q.source, q.stem, q.difficulty, q."order" AS q_order,
         p.content AS passage, s.code AS skill_code, s.name AS skill_name,
         t.title AS test, m.id AS module_id, m."order" AS m_order,
         m.difficulty AS branch
  FROM "Question" q
  JOIN "Module" m ON m.id = q."moduleId"
  JOIN "Test" t ON t.id = m."testId"
  LEFT JOIN "Passage" p ON p.id = q."passageId"
  LEFT JOIN "Skill" s ON s.id = q."skillId"
  WHERE m.subject = 'READING_WRITING'
  ORDER BY m."order", m.difficulty, q."order"`;

const num = (t) => Number(String(t).replace(/[^0-9]/g, ""));
const kept = rows.filter((r) => num(r.test) >= 16 && num(r.test) <= 31);
process.stdout.write(JSON.stringify(kept, null, 1));
