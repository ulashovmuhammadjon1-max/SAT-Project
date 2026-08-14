/**
 * Reshape the SAToplam export into the slice format the existing pipeline
 * expects, and split it across N authoring agents.
 *
 *     node satoplam_slices.mjs 12
 *
 * The export written by the Tests 16-31 rebuild carries its own short field
 * names (`mo`, `branch`, `qo`, `diff`). `verify.mjs` and `insert.mjs` read
 * `type`, `domain`, `q_order`, `test` — so the mapping happens once here
 * rather than being duplicated into every agent's brief, where a single agent
 * misreading it would silently fail the gate on every line it wrote.
 *
 * Slices are contiguous, not round-robin, so each agent owns a describable
 * range of tests and a restart lands on exactly the same work.
 */
import { readFileSync, writeFileSync, mkdirSync } from "fs";

const DIR = new URL(".", import.meta.url).pathname;
const N = Number(process.argv[2] || 12);

const SKILL_NAMES = {
  "INI-CI": "Central Ideas and Details",
  "INI-IE": "Inferences",
  "INI-CE": "Command of Evidence",
  "CAS-WV": "Words in Context",
  "CAS-TS": "Text Structure and Purpose",
  "CAS-CT": "Cross-Text Connections",
  "EOI-RS": "Rhetorical Synthesis",
  "EOI-TR": "Transitions",
  "SEC-BS": "Boundaries",
  "SEC-FS": "Form, Structure, and Sense",
};

const all = [];
for (let i = 1; i <= 8; i++) {
  for (const q of JSON.parse(readFileSync(`${DIR}/satoplam/slice${i}.json`, "utf8"))) {
    all.push({
      id: q.id,
      source: q.source,
      test: q.test,
      stem: q.stem,
      passage: q.passage,
      choices: q.choices,
      type: "MULTIPLE_CHOICE",
      correctAnswerFR: null,
      subject: "READING_WRITING",
      domain: q.skill.split("-")[0],
      skill: q.skill,
      skill_name: SKILL_NAMES[q.skill] ?? q.skill,
      difficulty: q.diff,
      m_subject: "READING_WRITING",
      m_order: q.mo,
      m_difficulty: q.branch,
      q_order: q.qo,
    });
  }
}

// Keep test order stable so a slice covers a contiguous run of tests.
const rank = (t) => Number(String(t).replace(/\D+/g, ""));
all.sort((a, b) =>
  rank(a.test) - rank(b.test) || a.m_order - b.m_order ||
  a.m_difficulty.localeCompare(b.m_difficulty) || a.q_order - b.q_order
);

const ids = new Set(all.map((q) => q.id));
if (ids.size !== all.length) throw new Error(`duplicate question ids: ${all.length - ids.size}`);
for (const q of all) {
  if (!q.choices?.length) throw new Error(`${q.id} has no choices`);
  if (!q.choices.some((c) => c.isCorrect)) throw new Error(`${q.id} has no correct choice`);
}

mkdirSync(`${DIR}/out`, { recursive: true });
const size = Math.ceil(all.length / N);
for (let i = 0; i < N; i++) {
  const qs = all.slice(i * size, (i + 1) * size);
  if (!qs.length) continue;
  const name = `sat-${String(i + 1).padStart(2, "0")}`;
  writeFileSync(`${DIR}/out/${name}.slice.json`, JSON.stringify(qs, null, 1));
  const tests = [...new Set(qs.map((q) => q.test))];
  console.log(
    `${name}  ${String(qs.length).padStart(4)} questions   ${tests[0]}${tests.length > 1 ? ` – ${tests[tests.length - 1]}` : ""}`
  );
}
console.log(`\ntotal ${all.length} R&W questions across ${N} agents`);
