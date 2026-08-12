/**
 * Deterministic work split for the authoring agents.
 *
 * Written to disk rather than computed in each agent's head, so a restarted
 * agent picks up exactly the slice it had before. Split by subject first —
 * Math and R&W explanations read differently, and an agent that stays in one
 * subject keeps one voice.
 */
import { readFileSync, writeFileSync, mkdirSync } from "fs";

const DIR = new URL(".", import.meta.url).pathname;
mkdirSync(`${DIR}/out`, { recursive: true });

// node slices.mjs <prefix> <test numbers…>   e.g. `node slices.mjs t6 6 7 8 9 10 11`
// The prefix namespaces this batch's agents so a new run cannot overwrite a
// previous batch's slice or output files.
const PREFIX = process.argv[2] ?? "";
const NUMS = process.argv.slice(3).map(Number).filter(Number.isFinite);
if (!PREFIX || !NUMS.length) throw new Error("Usage: node slices.mjs <prefix> <test numbers…>");
const TESTS = NUMS.map((n) => `test-${n}`);
const all = [];
for (const t of TESTS) {
  const { test, questions } = JSON.parse(readFileSync(`${DIR}/input/${t}.json`, "utf8"));
  for (const q of questions) all.push({ ...q, test });
}

const math = all.filter((q) => q.subject === "MATH");
const rw = all.filter((q) => q.subject === "READING_WRITING");

/** Contiguous slices — not round-robin, so one agent's range is describable. */
function chunk(arr, n) {
  const size = Math.ceil(arr.length / n);
  return Array.from({ length: n }, (_, i) => arr.slice(i * size, (i + 1) * size));
}

const agents = {};
chunk(math, 3).forEach((qs, i) => (agents[`${PREFIX}-math-${"abc"[i]}`] = qs));
chunk(rw, 3).forEach((qs, i) => (agents[`${PREFIX}-rw-${"abc"[i]}`] = qs));

for (const [name, qs] of Object.entries(agents)) {
  writeFileSync(`${DIR}/out/${name}.slice.json`, JSON.stringify(qs, null, 1));
  const tests = [...new Set(qs.map((q) => q.test))].join(", ");
  console.log(`${name.padEnd(7)} ${String(qs.length).padStart(4)} questions   ${tests}`);
}
console.log(`\ntotal ${math.length} Math + ${rw.length} R&W = ${all.length}`);
