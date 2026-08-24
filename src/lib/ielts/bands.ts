/**
 * IELTS band arithmetic.
 *
 * Every number a student sees in the IELTS section passes through this file,
 * so it is deliberately free of database and React imports and is unit-testable
 * on its own.
 *
 * Nothing here produces an official IELTS score. Scholarly reports a practice
 * estimate; `PRACTICE_DISCLAIMER` is the wording that must accompany it.
 */

export const IELTS_BAND_MIN = 0;
export const IELTS_BAND_MAX = 9;

export const PRACTICE_DISCLAIMER =
  "Scholarly IELTS scores are practice estimates and are not official IELTS results. " +
  "Scholarly is independent of IELTS, British Council, IDP and Cambridge.";

/** Every band a student can be given, 0.0 to 9.0 in half steps. */
export const BAND_STEPS: readonly number[] = Array.from(
  { length: 19 },
  (_, i) => i / 2
);

/**
 * Round to the nearest half band, which is how each of the four skills is
 * reported.
 */
export function toHalfBand(value: number): number {
  const clamped = Math.min(IELTS_BAND_MAX, Math.max(IELTS_BAND_MIN, value));
  return Math.round(clamped * 2) / 2;
}

/**
 * The overall band from the four skill bands.
 *
 * IELTS rounds the mean to the nearest whole or half band, and it rounds the
 * midpoint UP rather than to even: a mean of 6.25 is reported as 6.5 and 6.75
 * as 7.0. `Math.round` alone gets 6.25 right by luck and 6.75 wrong, so the
 * two thresholds are written out rather than inferred.
 *
 * Returns null unless all four skills are present — an overall band computed
 * from three of them is not an overall band, and showing one would tell a
 * student they had finished when they had not.
 */
export function overallBand(skills: {
  listening?: number | null;
  reading?: number | null;
  writing?: number | null;
  speaking?: number | null;
}): number | null {
  const values = [skills.listening, skills.reading, skills.writing, skills.speaking];
  if (values.some((v) => v === null || v === undefined || Number.isNaN(v))) return null;

  const mean = (values as number[]).reduce((a, b) => a + b, 0) / 4;
  const whole = Math.floor(mean);
  const frac = mean - whole;
  if (frac < 0.25) return whole;
  if (frac < 0.75) return whole + 0.5;
  return whole + 1;
}

/**
 * The Writing band from the two tasks.
 *
 * Task 2 carries twice the weight of Task 1. This is the single rule most
 * easily got wrong by averaging, and averaging would flatter a student who
 * wrote a strong Task 1 and a weak essay.
 */
export function writingBandFromTasks(
  task1: number | null | undefined,
  task2: number | null | undefined
): number | null {
  if (task1 === null || task1 === undefined) return null;
  if (task2 === null || task2 === undefined) return null;
  return toHalfBand((task1 + task2 * 2) / 3);
}

/** The four criteria of one Writing task, averaged to a half band. */
export function writingTaskBand(c: {
  task: number;
  coherence: number;
  lexical: number;
  grammar: number;
}): number {
  return toHalfBand((c.task + c.coherence + c.lexical + c.grammar) / 4);
}

/** The four criteria of Speaking, averaged to a half band. */
export function speakingBand(c: {
  fluency: number;
  lexical: number;
  grammar: number;
  pronunciation: number;
}): number {
  return toHalfBand((c.fluency + c.lexical + c.grammar + c.pronunciation) / 4);
}

export interface BandDescriptor {
  band: number;
  title: string;
  summary: string;
}

/** The publicly documented band scale, used in the Resources area. */
export const BAND_DESCRIPTORS: readonly BandDescriptor[] = [
  { band: 9, title: "Expert user", summary: "Full operational command of the language: appropriate, accurate and fluent with complete understanding." },
  { band: 8, title: "Very good user", summary: "Fully operational command with only occasional unsystematic inaccuracies and inappropriate usage." },
  { band: 7, title: "Good user", summary: "Operational command, though with occasional inaccuracies and misunderstandings in some situations." },
  { band: 6, title: "Competent user", summary: "Generally effective command despite some inaccuracies and misunderstandings." },
  { band: 5, title: "Modest user", summary: "Partial command, coping with overall meaning in most situations though likely to make many mistakes." },
  { band: 4, title: "Limited user", summary: "Basic competence limited to familiar situations; frequent problems in understanding and expression." },
  { band: 3, title: "Extremely limited user", summary: "Conveys and understands only general meaning in very familiar situations." },
  { band: 2, title: "Intermittent user", summary: "Great difficulty understanding spoken and written English." },
  { band: 1, title: "Non-user", summary: "No ability to use the language beyond a few isolated words." },
  { band: 0, title: "Did not attempt", summary: "No assessable information provided." },
];

export function describeBand(band: number): BandDescriptor {
  const whole = Math.floor(band);
  return (
    BAND_DESCRIPTORS.find((d) => d.band === whole) ??
    BAND_DESCRIPTORS[BAND_DESCRIPTORS.length - 1]
  );
}

/** "7.5", "8", "—" — bands are written with at most one decimal place. */
export function formatBand(band: number | null | undefined): string {
  if (band === null || band === undefined || Number.isNaN(band)) return "—";
  return Number.isInteger(band) ? String(band) : band.toFixed(1);
}
