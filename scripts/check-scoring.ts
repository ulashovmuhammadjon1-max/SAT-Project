/**
 * Scoring invariants, checked exhaustively rather than spot-checked.
 *
 * Run with `npm run check:scoring`.
 *
 * This exists because the bug it guards against was invisible to inspection:
 * a linear `200 + accuracy * 600` looks perfectly reasonable in a diff and
 * silently produces scores like 336, which the SAT cannot award. The cheapest
 * way to make that class of mistake impossible is to enumerate every raw score
 * a student can actually get and assert the result is a legal SAT score.
 */

import {
  estimateScaledScore,
  estimateTotalScore,
  scoreBandForRaw,
  sectionScoreForRaw,
  type ScoredSubject,
} from "../src/lib/scoring/estimate";

/** Section lengths our tests actually use: R&W 27 + 27, Math 22 + 22. */
const SECTIONS: { subject: ScoredSubject; questions: number }[] = [
  { subject: "READING_WRITING", questions: 54 },
  { subject: "MATH", questions: 44 },
];

const failures: string[] = [];
const fail = (message: string) => failures.push(message);

function checkSectionScore(label: string, score: number) {
  if (!Number.isInteger(score)) fail(`${label}: ${score} is not a whole number`);
  if (score % 10 !== 0) fail(`${label}: ${score} is not a multiple of 10`);
  if (score < 200 || score > 800) fail(`${label}: ${score} is outside 200-800`);
}

for (const { subject, questions } of SECTIONS) {
  let previous = -1;

  for (let raw = 0; raw <= questions; raw++) {
    const score = sectionScoreForRaw(subject, raw, questions);
    checkSectionScore(`${subject} raw ${raw}/${questions}`, score);

    // Answering one more question right must never lower the score.
    if (score < previous) {
      fail(`${subject}: raw ${raw} scored ${score}, below raw ${raw - 1} at ${previous}`);
    }
    previous = score;

    const band = scoreBandForRaw(subject, raw, questions);
    checkSectionScore(`${subject} raw ${raw} band lower`, band.lower);
    checkSectionScore(`${subject} raw ${raw} band upper`, band.upper);
    if (band.lower > band.upper) fail(`${subject} raw ${raw}: band ${band.lower}-${band.upper} inverted`);
    if (score < band.lower || score > band.upper) {
      fail(`${subject} raw ${raw}: ${score} sits outside its own band ${band.lower}-${band.upper}`);
    }
  }

  // The endpoints are the whole point of moving off the averaging scheme: they
  // were previously unreachable.
  const blank = sectionScoreForRaw(subject, 0, questions);
  const perfect = sectionScoreForRaw(subject, questions, questions);
  if (blank !== 200) fail(`${subject}: a blank paper scored ${blank}, expected 200`);
  if (perfect !== 800) fail(`${subject}: a perfect paper scored ${perfect}, expected 800`);
}

// Every total a student can produce.
for (let rw = 0; rw <= 54; rw++) {
  for (let math = 0; math <= 44; math++) {
    const total = estimateTotalScore(
      sectionScoreForRaw("READING_WRITING", rw, 54),
      sectionScoreForRaw("MATH", math, 44),
    );
    if (total === null) {
      fail(`total ${rw}/${math}: unexpectedly null`);
      continue;
    }
    if (total % 10 !== 0) fail(`total ${rw}/${math}: ${total} is not a multiple of 10`);
    if (total < 400 || total > 1600) fail(`total ${rw}/${math}: ${total} is outside 400-1600`);
  }
}

// The accuracy-only estimate, which is where the reported 336 came from.
for (let pct = 0; pct <= 100; pct++) {
  for (const { subject } of SECTIONS) {
    checkSectionScore(`estimate ${pct}% ${subject}`, estimateScaledScore(pct, subject));
  }
}

if (failures.length) {
  console.error(`FAIL — ${failures.length} problem${failures.length === 1 ? "" : "s"}:`);
  for (const message of failures.slice(0, 25)) console.error(`  ${message}`);
  if (failures.length > 25) console.error(`  …and ${failures.length - 25} more`);
  process.exit(1);
}

console.log("PASS — every reachable score is a multiple of 10, in range, monotonic,");
console.log("       and a blank/perfect paper reaches 200/800 in both sections.");
for (const { subject, questions } of SECTIONS) {
  const marks = [0, Math.round(questions * 0.25), Math.round(questions * 0.5), Math.round(questions * 0.75), questions];
  const shown = marks.map((raw) => `${raw}/${questions}→${sectionScoreForRaw(subject, raw, questions)}`).join("  ");
  console.log(`       ${subject.padEnd(15)} ${shown}`);
}
