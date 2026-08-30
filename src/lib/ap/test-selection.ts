import { createHash } from "crypto";

import { FORM_STRIDE, testDemandByUnit, type ApPracticeTest } from "./tests";

/**
 * Turning a test's blueprint into an actual list of question ids.
 *
 * This is pure and lives outside the server action on purpose: it is the one
 * piece of the practice-test feature with real logic to get wrong (per-unit
 * quotas, two sections drawing on one unit, two forms of the same test needing
 * different questions), and a pure module can be exercised directly by
 * `scripts/check-ap-tests.ts` with a synthetic bank rather than only in
 * production against the real one.
 */

export interface BankQuestion {
  id: string;
  unit: number;
  topic: string;
}

/**
 * A stable ordering of one unit's questions.
 *
 * Hashing (seed, id) rather than shuffling with a PRNG means the order does not
 * shift when a question is added to the middle of the bank — only the new
 * question slots in. That is what keeps "Practice Exam 1" the same test in
 * March as it was in January, which is the whole basis for comparing a best
 * score against a last score.
 */
export function orderedPool(subject: string, unit: number, ids: string[]): string[] {
  const seed = `${subject}:${unit}`;
  return [...ids]
    .map((id) => ({ id, key: createHash("md5").update(`${seed}|${id}`).digest("hex") }))
    .sort((a, b) => (a.key < b.key ? -1 : a.key > b.key ? 1 : 0))
    .map((x) => x.id);
}

/**
 * Resolves a test's blueprint against the bank, returning the frozen question
 * ids in presentation order (section by section, in configuration order).
 *
 * Returns null when the bank cannot fill the blueprint, which is the same
 * condition the picker uses to hide a test — so a test that is visible is a
 * test that can be started.
 */
export function selectQuestions(test: ApPracticeTest, bank: BankQuestion[]): string[] | null {
  const byUnit = new Map<number, BankQuestion[]>();
  for (const q of bank) {
    const list = byUnit.get(q.unit);
    if (list) list.push(q);
    else byUnit.set(q.unit, [q]);
  }

  // One cursor per unit for the whole test, so two sections drawing on the same
  // unit (Calculus Part A and Part B both examine integration) cannot hand the
  // student the same question twice.
  const cursor = new Map<number, number>();
  const taken = new Set<string>();
  const picked: string[] = [];

  for (const s of test.sections) {
    for (const quota of s.blueprint) {
      let candidates = byUnit.get(quota.unit) ?? [];
      if (s.topics?.length) {
        const wanted = new Set(s.topics);
        candidates = candidates.filter((q) => wanted.has(q.topic));
      }
      if (candidates.length < quota.count) return null;

      const pool = orderedPool(
        test.subject,
        quota.unit,
        candidates.map((q) => q.id),
      );
      const start = cursor.get(quota.unit) ?? test.variant * FORM_STRIDE;

      let got = 0;
      // Walk the pool cyclically from this form's starting point. The wrap only
      // matters for a unit whose bank is smaller than variant * FORM_STRIDE — a
      // young bank, where two forms will legitimately share questions rather
      // than one of them failing to exist.
      for (let step = 0; step < pool.length && got < quota.count; step++) {
        const id = pool[(start + step) % pool.length];
        if (taken.has(id)) continue;
        taken.add(id);
        picked.push(id);
        got++;
      }
      if (got < quota.count) return null;
      cursor.set(quota.unit, start + quota.count);
    }
  }

  return picked;
}

/** Whether the live bank can fill this test's blueprint, unit by unit. */
export function canFill(test: ApPracticeTest, availableByUnit: Map<number, number>): boolean {
  for (const [unit, needed] of testDemandByUnit(test)) {
    if ((availableByUnit.get(unit) ?? 0) < needed) return false;
  }
  return true;
}
