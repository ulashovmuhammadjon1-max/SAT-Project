/**
 * Render a range of an agent's slice for reading, with the answer key withheld.
 *
 *     node dump_slice.mjs sat-01 0 10        # questions 0-9
 *     node dump_slice.mjs sat-01 --todo 10   # next 10 not yet in the .jsonl
 *
 * Shared by every authoring agent so nobody writes their own dumper — on the
 * first batch two agents wrote a `dump.mjs` each and one clobbered the other,
 * and an agent briefly worked a sibling's questions.
 *
 * `isCorrect` is deliberately not printed. The brief's central rule is that the
 * author derives the answer before seeing the key; leaving the key out of the
 * only tool an agent uses to read a question turns that rule from an
 * instruction into a property of the workflow. `verify.mjs` still compares the
 * two afterwards, so a disagreement surfaces rather than being papered over.
 */
import { readFileSync } from "fs";
import { readJsonl } from "./status.mjs";

const DIR = new URL(".", import.meta.url).pathname;
const name = process.argv[2];
if (!name) throw new Error("Usage: node dump_slice.mjs <agent> [start count | --todo count]");

const slice = JSON.parse(readFileSync(`${DIR}/out/${name}.slice.json`, "utf8"));

let picked;
if (process.argv[3] === "--todo") {
  const done = new Set(readJsonl(`${DIR}/out/${name}.jsonl`).map((e) => e.questionId));
  picked = slice.filter((q) => !done.has(q.id)).slice(0, Number(process.argv[4] || 10));
  console.log(`# ${done.size}/${slice.length} done — showing the next ${picked.length}\n`);
} else {
  const start = Number(process.argv[3] || 0);
  picked = slice.slice(start, start + Number(process.argv[4] || 10));
  console.log(`# ${name} questions ${start}..${start + picked.length - 1} of ${slice.length}\n`);
}

for (const q of picked) {
  const i = slice.indexOf(q);
  console.log(`════ #${i}  ${q.id}`);
  console.log(`${q.test} · Module ${q.m_order} ${q.m_difficulty} · q${q.q_order} · ${q.skill_name} · ${q.difficulty}`);
  if (q.passage) console.log(`\nPASSAGE\n${q.passage}`);
  console.log(`\nSTEM\n${q.stem}`);
  console.log("\nCHOICES");
  for (const c of q.choices) console.log(`  ${c.label}. ${c.content}`);
  console.log();
}
