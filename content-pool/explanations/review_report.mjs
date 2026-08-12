/**
 * The adjudication list: every question where an authoring agent's independent
 * answer disagreed with the live key.
 *
 * None of these shipped — the gate holds them back. This file is what a human
 * needs to decide each one, so it carries the stem, both answers in full, and
 * the agent's reasoning, rather than a bare list of ids.
 */
import { readFileSync, writeFileSync } from "fs";
import { readJsonl, agentNames } from "./status.mjs";

const DIR = new URL(".", import.meta.url).pathname;
const strip = (h) => (h || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();

const rows = [];
for (const name of agentNames()) {
  const slice = JSON.parse(readFileSync(`${DIR}/out/${name}.slice.json`, "utf8"));
  const byId = new Map(slice.map((q) => [q.id, q]));
  for (const e of readJsonl(`${DIR}/out/${name}.jsonl`)) {
    const q = byId.get(e.questionId);
    if (!q) continue;
    if (q.type === "MULTIPLE_CHOICE") {
      const key = (q.choices || []).find((c) => c.isCorrect);
      if (key && e.answerLabel && e.answerLabel !== key.label) {
        const mine = (q.choices || []).find((c) => c.label === e.answerLabel);
        rows.push({ name, q, keyLabel: key.label, keyText: strip(key.content),
                    myLabel: e.answerLabel, myText: strip(mine?.content), why: e.whyCorrect });
      }
    }
  }
}

rows.sort((a, b) => a.q.test.localeCompare(b.q.test) || a.q.m_order - b.q.m_order || a.q.q_order - b.q.q_order);

const out = [`# Answer-key review list`, ``,
  `${rows.length} questions where an agent's independent answer disagreed with the live key.`,
  `**None of these were inserted** — the verifier holds a mismatch back rather than`,
  `shipping an explanation that argues against the stored answer.`, ``,
  `Three of these were independently confirmed against the database during the run:`,
  `Test 2 M2H q17 has byte-identical B and D choices, Test 3 M1 q9 and q10 are the`,
  `same question, and Test 4 M1 q16 is keyed to a sentence fragment.`, ``];

let test = "";
for (const r of rows) {
  if (r.q.test !== test) { test = r.q.test; out.push(`\n## ${test}\n`); }
  const mod = `M${r.q.m_order}${r.q.m_difficulty === "STANDARD" ? "" : r.q.m_difficulty === "EASY" ? " Easy" : " Hard"}`;
  out.push(`### ${mod} q${r.q.q_order} · ${r.q.skill_name} · \`${r.q.id.slice(0, 8)}\``);
  out.push(`- **key:** ${r.keyLabel}. ${r.keyText}`);
  out.push(`- **agent:** ${r.myLabel}. ${r.myText}`);
  out.push(`- ${strip(r.why)}`);
  out.push(``);
}
writeFileSync(`${DIR}/REVIEW.md`, out.join("\n"));
console.log(`${rows.length} mismatches written to REVIEW.md`);
const byTest = {};
for (const r of rows) byTest[r.q.test] = (byTest[r.q.test] || 0) + 1;
console.log(byTest);
