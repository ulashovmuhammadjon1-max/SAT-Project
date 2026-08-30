/**
 * A check on the AP practice-test configuration and the question selector.
 *
 *   npx tsx scripts/check-ap-tests.ts
 *
 * It needs no database: the point is to exercise the selector against a
 * synthetic bank whose shape can be varied on purpose — a bank that is exactly
 * big enough, one that is one question short, one that is smaller than a form's
 * starting offset — because those are the cases the real bank will only reach
 * months apart as content lands.
 *
 * Exit code is non-zero on any failure, so it can gate a build.
 */

import {
  AP_TESTS,
  FORM_STRIDE,
  formatDuration,
  sectionOffsets,
  testDemandByUnit,
  testDurationMinutes,
  testQuestionCount,
  testUnits,
  type ApPracticeTest,
} from "../src/lib/ap/tests";
import { canFill, selectQuestions, type BankQuestion } from "../src/lib/ap/test-selection";

let failures = 0;

function check(condition: boolean, message: string) {
  if (!condition) {
    failures++;
    console.error(`  FAIL  ${message}`);
  }
}

/** A bank holding `perUnit` questions in each unit the test draws on. */
function bankFor(test: ApPracticeTest, perUnit: number): BankQuestion[] {
  const out: BankQuestion[] = [];
  for (const unit of testUnits(test)) {
    for (let i = 0; i < perUnit; i++) {
      out.push({ id: `${test.subject}-u${unit}-q${i}`, unit, topic: `${unit}.${(i % 9) + 1}` });
    }
  }
  return out;
}

console.log(`Checking ${AP_TESTS.length} configured tests\n`);

// --- The configuration itself ---------------------------------------------
const seen = new Set<string>();
for (const test of AP_TESTS) {
  const key = `${test.subject}/${test.slug}`;
  check(!seen.has(key), `${key}: duplicate subject+slug — ApTestAttempt could not tell them apart`);
  seen.add(key);

  const total = testQuestionCount(test);
  check(total > 0, `${key}: no questions`);
  check(testDurationMinutes(test) > 0, `${key}: no time limit`);

  for (const s of test.sections) {
    const blueprintTotal = s.blueprint.reduce((n, q) => n + q.count, 0);
    check(
      s.questionCount === blueprintTotal,
      `${key}/${s.id}: questionCount ${s.questionCount} does not match blueprint ${blueprintTotal}`,
    );
    check(s.timeLimitMinutes > 0, `${key}/${s.id}: no time limit`);
    for (const q of s.blueprint) {
      check(q.count > 0, `${key}/${s.id}: unit ${q.unit} has a zero quota`);
      check(
        q.count < FORM_STRIDE,
        `${key}/${s.id}: unit ${q.unit} wants ${q.count}, which is not below FORM_STRIDE ${FORM_STRIDE} — two forms would overlap`,
      );
    }
  }

  // Sections are laid out back to back, so the offsets must tile the list.
  const offsets = sectionOffsets(test);
  check(offsets[0] === 0, `${key}: first section does not start at 0`);
  check(
    offsets[offsets.length - 1] + test.sections[test.sections.length - 1].questionCount === total,
    `${key}: section offsets do not cover the question list`,
  );

  // Within one test, one unit's demand across all sections must still fit
  // inside a form's stride, or the second section would run into the next
  // form's questions.
  for (const [unit, demand] of testDemandByUnit(test)) {
    check(
      demand <= FORM_STRIDE,
      `${key}: unit ${unit} demands ${demand} across sections, above FORM_STRIDE ${FORM_STRIDE}`,
    );
  }
}

// --- The selector ----------------------------------------------------------
for (const test of AP_TESTS) {
  const key = `${test.subject}/${test.slug}`;
  const demand = testDemandByUnit(test);
  const perUnit = (test.variant + 1) * FORM_STRIDE + Math.max(...demand.values());

  const picked = selectQuestions(test, bankFor(test, perUnit));
  check(picked !== null, `${key}: could not be filled from a bank of ${perUnit} per unit`);
  if (!picked) continue;

  check(
    picked.length === testQuestionCount(test),
    `${key}: selected ${picked.length} questions, wanted ${testQuestionCount(test)}`,
  );
  check(new Set(picked).size === picked.length, `${key}: selected the same question twice`);

  // Every section's slice must hold exactly the units its blueprint names.
  const offsets = sectionOffsets(test);
  test.sections.forEach((s, i) => {
    const slice = picked.slice(offsets[i], offsets[i] + s.questionCount);
    for (const quota of s.blueprint) {
      const got = slice.filter((id) => id.includes(`-u${quota.unit}-`)).length;
      check(
        got === quota.count,
        `${key}/${s.id}: unit ${quota.unit} got ${got} questions, blueprint says ${quota.count}`,
      );
    }
  });

  // Determinism: the same test against the same bank twice.
  const again = selectQuestions(test, bankFor(test, perUnit));
  check(
    JSON.stringify(again) === JSON.stringify(picked),
    `${key}: selection is not deterministic — best and last scores would not be comparable`,
  );

  // A bank one question short in the heaviest unit must refuse, not improvise.
  const heaviest = [...demand.entries()].sort((a, b) => b[1] - a[1])[0][0];
  const short = bankFor(test, perUnit).filter((q) => {
    if (q.unit !== heaviest) return true;
    return q.id !== `${test.subject}-u${heaviest}-q0`;
  });
  const shortByOne = short.filter(
    (q) => q.unit !== heaviest || Number(q.id.split("q")[1]) < (demand.get(heaviest) ?? 0) - 1,
  );
  check(
    selectQuestions(test, shortByOne) === null,
    `${key}: filled a blueprint from a bank that was short in unit ${heaviest}`,
  );

  // canFill must agree with the selector about that same bank.
  const available = new Map<number, number>();
  for (const q of shortByOne) available.set(q.unit, (available.get(q.unit) ?? 0) + 1);
  check(
    !canFill(test, available),
    `${key}: canFill said yes to a bank the selector rejects — the picker would show a test that cannot start`,
  );
}

// --- Two forms of one test must not share questions ------------------------
const bySubject = new Map<string, ApPracticeTest[]>();
for (const t of AP_TESTS) bySubject.set(t.subject, [...(bySubject.get(t.subject) ?? []), t]);

for (const [subject, tests] of bySubject) {
  const variants = new Set(tests.map((t) => t.variant));
  check(
    variants.size === tests.length,
    `${subject}: two tests share a variant, so they would present the same questions`,
  );

  // A bank generous enough for every form: each form's questions must be
  // disjoint from every other's.
  const units = [...new Set(tests.flatMap((t) => testUnits(t)))];
  const maxVariant = Math.max(...tests.map((t) => t.variant));
  const bank: BankQuestion[] = [];
  for (const unit of units) {
    for (let i = 0; i < (maxVariant + 1) * FORM_STRIDE + FORM_STRIDE; i++) {
      bank.push({ id: `${subject}-u${unit}-q${i}`, unit, topic: `${unit}.${(i % 9) + 1}` });
    }
  }

  const picks = tests.map((t) => ({ t, ids: selectQuestions(t, bank) }));
  for (let i = 0; i < picks.length; i++) {
    for (let j = i + 1; j < picks.length; j++) {
      const a = picks[i];
      const b = picks[j];
      if (!a.ids || !b.ids) continue;
      const overlap = a.ids.filter((id) => b.ids!.includes(id));
      check(
        overlap.length === 0,
        `${subject}: ${a.t.slug} and ${b.t.slug} share ${overlap.length} questions`,
      );
    }
  }
}

// --- A summary worth reading even when everything passes -------------------
console.log("subject       test          questions  time        sections");
for (const t of AP_TESTS) {
  console.log(
    `${t.subject.padEnd(13)} ${t.slug.padEnd(13)} ${String(testQuestionCount(t)).padStart(
      9,
    )}  ${formatDuration(testDurationMinutes(t)).padEnd(11)} ${t.sections
      .map((s) => `${s.short} (${s.questionCount}/${s.timeLimitMinutes}m, ${s.calculator})`)
      .join(" + ")}`,
  );
}

console.log(
  failures === 0
    ? `\nAll checks passed across ${AP_TESTS.length} tests.`
    : `\n${failures} check(s) FAILED.`,
);
process.exit(failures === 0 ? 0 : 1);
