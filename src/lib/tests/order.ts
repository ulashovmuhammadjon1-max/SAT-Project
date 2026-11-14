/**
 * Ordering for lists of tests.
 *
 * Titles are "Test 1".."Test 31", which neither of the two obvious orderings
 * gets right:
 *
 *   - `createdAt` is build order, so the newest test lands first and the list
 *     reads 31, 30, 29, … — and within a batch built by parallel agents the
 *     order is whatever finished first, which is not even monotonic.
 *   - `title` sorts lexically: "Test 10" precedes "Test 2" because "1" < "2"
 *     at the first differing character.
 *
 * So the number is pulled out of the title and compared numerically.
 */

/** The first run of digits in a title, or null when it has none. */
export function testNumber(title: string): number | null {
  const match = /\d+/.exec(title);
  if (!match) return null;
  const n = Number(match[0]);
  return Number.isSafeInteger(n) ? n : null;
}

/**
 * "SPECIAL TEST" is pinned to the top of every test list at the founder's
 * request. Matched by its title prefix so a later "SPECIAL TEST 2" joins it.
 */
export function isFeaturedTest(title: string): boolean {
  return /^special test\b/i.test(title.trim());
}

/**
 * Compare two tests: numbered titles ascending, then everything else.
 *
 * A title without a number (a themed or diagnostic test, say) sorts after all
 * the numbered ones rather than being forced to position zero, and ties break
 * on the title so the order is stable regardless of the input ordering.
 */
export function compareTests(
  a: { title: string },
  b: { title: string }
): number {
  // Featured tests come before everything else, whatever their title says.
  const fa = isFeaturedTest(a.title);
  const fb = isFeaturedTest(b.title);
  if (fa !== fb) return fa ? -1 : 1;
  const na = testNumber(a.title);
  const nb = testNumber(b.title);
  if (na !== null && nb !== null && na !== nb) return na - nb;
  if (na !== null && nb === null) return -1;
  if (na === null && nb !== null) return 1;
  return a.title.localeCompare(b.title, undefined, { numeric: true });
}

/** A copy of `tests` in display order. Does not mutate the input. */
export function sortTests<T extends { title: string }>(tests: T[]): T[] {
  return [...tests].sort(compareTests);
}
