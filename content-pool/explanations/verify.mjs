/**
 * Gate every authored explanation before it reaches a student.
 *
 * The one failure that matters is an explanation that confidently argues for
 * the wrong answer — a student believes it and learns the error, which is
 * strictly worse than having no explanation at all. So the central check is
 * not "is the prose nice" but "does the explanation name the same answer the
 * database has marked correct".
 */
import { readFileSync } from "fs";
import { readJsonl, agentNames } from "./status.mjs";

const DIR = new URL(".", import.meta.url).pathname;

const strip = (html) => (html || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();

export function checkOne(q, e) {
  const problems = [];

  if (!e.whyCorrect || strip(e.whyCorrect).length < 40)
    problems.push("whyCorrect missing or too short");

  if (q.type === "MULTIPLE_CHOICE") {
    const key = (q.choices || []).find((c) => c.isCorrect);
    if (!key) {
      problems.push("question has no correct choice");
    } else {
      // The author must state which letter is right, and it must match.
      if (!e.answerLabel) problems.push("answerLabel missing");
      else if (e.answerLabel !== key.label)
        problems.push(`ANSWER MISMATCH: explanation says ${e.answerLabel}, key is ${key.label}`);

      // Every distractor needs a reason. A list of three plausible options
      // with no comment is where students actually get stuck.
      const others = q.choices.filter((c) => !c.isCorrect).map((c) => c.label);
      const covered = Object.keys(e.whyWrong || {});
      const missing = others.filter((l) => !covered.includes(l));
      if (missing.length) problems.push(`no reason given for ${missing.join(", ")}`);
    }
  } else {
    // Free response: the stated answer must be one the grader accepts.
    let accepted = [];
    try {
      accepted = JSON.parse(q.correctAnswerFR || "[]").map(String);
    } catch {
      problems.push("correctAnswerFR is not JSON");
    }
    if (!e.answerValue) problems.push("answerValue missing");
    else if (accepted.length && !accepted.some((a) => a.trim() === String(e.answerValue).trim()))
      problems.push(`ANSWER MISMATCH: explanation says ${e.answerValue}, key accepts ${accepted.join("/")}`);
  }

  // House style, same rules the question content follows.
  const text = [e.whyCorrect, ...Object.values(e.whyWrong || {}), e.tips].join(" ");
  if (/\*[^*\n]+\*/.test(text)) problems.push("markdown asterisks — use <em>");
  if (/\$[^$\n]+\$/.test(text)) problems.push("$…$ math — use \\( \\)");
  // A LaTeX macro loose in prose renders as a literal backslash.
  const outside = text.replace(/\\\((.|\n)*?\\\)/g, "");
  if (/\\(frac|sqrt|pi|cdot|times|le|ge|ne)\b/.test(outside))
    problems.push("LaTeX macro outside a math span");

  return problems;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  let checked = 0, bad = 0, mismatches = 0;
  for (const name of agentNames()) {
    const slice = JSON.parse(readFileSync(`${DIR}/out/${name}.slice.json`, "utf8"));
    const byId = new Map(slice.map((q) => [q.id, q]));
    for (const e of readJsonl(`${DIR}/out/${name}.jsonl`)) {
      const q = byId.get(e.questionId);
      if (!q) { console.log(`  ! ${name}: ${e.questionId} not in slice`); bad++; continue; }
      const problems = checkOne(q, e);
      checked++;
      if (problems.length) {
        bad++;
        if (problems.some((p) => p.startsWith("ANSWER MISMATCH"))) mismatches++;
        console.log(`  ! ${name} ${q.test} ${q.domain} q${q.q_order}: ${problems.join("; ")}`);
      }
    }
  }
  console.log(`\nchecked ${checked}, failed ${bad}, of which answer mismatches: ${mismatches}`);
  process.exit(bad ? 1 : 0);
}
