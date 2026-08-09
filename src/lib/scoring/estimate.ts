/**
 * Digital SAT scaled scoring.
 *
 * Replaces a linear `200 + accuracy * 600` approximation that could return any
 * integer at all — a student reported seeing **336**. Real SAT scores only ever
 * come in steps of ten: 200-800 per section, 400-1600 in total. Nothing in this
 * file may return a value that is not a multiple of ten.
 *
 * Scores come from the raw-score conversion table below, not from a formula.
 * The table gives a *range* per raw score because the real curve varies by
 * form; we report the midpoint of that range, snapped to ten.
 *
 * ## The raw score is per SECTION, not per module
 *
 * This is the part the old code got wrong in a way no rounding fix would have
 * caught. It scored each module separately and then **averaged** the two. The
 * SAT does not work that way: a section's raw score is the number correct
 * across *both* of its modules combined, converted once. Averaging two
 * per-module estimates compresses everything toward the middle — it cannot
 * produce a 200 or an 800 even from a blank or perfect paper.
 */

export type ScoredSubject = "READING_WRITING" | "MATH";

export interface ScoreBand {
  lower: number;
  upper: number;
}

const band = (lower: number, upper: number): ScoreBand => ({ lower, upper });

/**
 * Reading and Writing, raw 0-66. Index is the raw score.
 */
const RW_BANDS: readonly ScoreBand[] = [
  band(200, 200), band(200, 200), band(200, 200), band(200, 200), band(200, 200),
  band(200, 210), band(200, 230), band(200, 240), band(200, 250), band(200, 260),
  band(220, 280), band(230, 290), band(240, 300), band(250, 310), band(260, 320),
  band(270, 330), band(290, 350), band(310, 370), band(330, 370), band(340, 380),
  band(350, 390), band(360, 400), band(360, 400), band(370, 410), band(380, 420),
  band(390, 430), band(390, 430), band(400, 440), band(410, 450), band(420, 460),
  band(430, 470), band(440, 480), band(450, 490), band(450, 490), band(460, 500),
  band(470, 510), band(480, 520), band(490, 530), band(500, 540), band(500, 540),
  band(510, 550), band(520, 560), band(530, 570), band(530, 590), band(540, 600),
  band(550, 610), band(560, 620), band(570, 630), band(580, 640), band(590, 650),
  band(600, 660), band(620, 660), band(630, 670), band(640, 680), band(650, 690),
  band(660, 700), band(680, 720), band(690, 730), band(700, 740), band(710, 750),
  band(720, 760), band(730, 770), band(750, 770), band(760, 780), band(770, 790),
  band(780, 800), band(790, 800),
];

/**
 * Math, raw 0-54. Index is the raw score.
 */
const MATH_BANDS: readonly ScoreBand[] = [
  band(200, 200), band(200, 200), band(200, 200), band(200, 210), band(200, 220),
  band(200, 240), band(210, 260), band(220, 270), band(230, 290), band(270, 330),
  band(290, 330), band(300, 340), band(310, 350), band(320, 360), band(330, 370),
  band(340, 380), band(340, 380), band(350, 390), band(350, 390), band(360, 400),
  band(370, 410), band(380, 420), band(380, 420), band(390, 430), band(400, 440),
  band(410, 450), band(420, 460), band(430, 470), band(440, 480), band(450, 510),
  band(460, 520), band(470, 530), band(480, 540), band(490, 550), band(510, 570),
  band(520, 580), band(530, 590), band(540, 600), band(550, 610), band(560, 620),
  band(570, 630), band(580, 640), band(600, 660), band(610, 670), band(630, 690),
  band(640, 700), band(660, 720), band(680, 740), band(700, 760), band(720, 780),
  band(750, 790), band(760, 800), band(780, 800), band(790, 800), band(790, 800),
];

function bandsFor(subject: ScoredSubject): readonly ScoreBand[] {
  return subject === "MATH" ? MATH_BANDS : RW_BANDS;
}

/** The raw score the table tops out at, i.e. a perfect paper on its scale. */
export function tableMaxRaw(subject: ScoredSubject): number {
  return bandsFor(subject).length - 1;
}

export const SECTION_MIN = 200;
export const SECTION_MAX = 800;

/**
 * Rounds to the nearest ten and clamps into the section range.
 *
 * Every public function here ends by calling this, so "always a multiple of
 * ten" is enforced in exactly one place rather than trusted at each call site.
 */
export function toSectionScore(value: number): number {
  const snapped = Math.round(value / 10) * 10;
  return Math.min(SECTION_MAX, Math.max(SECTION_MIN, snapped));
}

/**
 * Maps a raw score onto the conversion table's scale.
 *
 * Our tests are 54 questions of Reading and Writing (27 + 27) and 44 of Math
 * (22 + 22), while the table runs to 66 and 54. Rather than truncate — which
 * would cap a perfect Reading and Writing paper at 690 — the raw score is
 * scaled proportionally, so full marks reach the top of the table and a blank
 * paper sits at the bottom.
 *
 * When a test happens to match the table's own length this is the identity, so
 * swapping in a table cut for 54/44 later needs no other change.
 */
function rawOnTableScale(subject: ScoredSubject, rawCorrect: number, questionCount: number): number {
  const max = tableMaxRaw(subject);
  if (questionCount <= 0) return 0;
  const clamped = Math.min(questionCount, Math.max(0, rawCorrect));
  if (questionCount === max) return clamped;
  return Math.round((clamped / questionCount) * max);
}

/**
 * The published range for a raw score — useful for showing "620-660" rather
 * than implying a single number is exact.
 */
export function scoreBandForRaw(
  subject: ScoredSubject,
  rawCorrect: number,
  questionCount: number,
): ScoreBand {
  const bands = bandsFor(subject);
  const index = Math.min(bands.length - 1, Math.max(0, rawOnTableScale(subject, rawCorrect, questionCount)));
  const found = bands[index];
  return { lower: toSectionScore(found.lower), upper: toSectionScore(found.upper) };
}

/**
 * One section score, 200-800 in steps of ten.
 *
 * `rawCorrect` and `questionCount` are section totals across both modules.
 */
export function sectionScoreForRaw(
  subject: ScoredSubject,
  rawCorrect: number,
  questionCount: number,
): number {
  const { lower, upper } = scoreBandForRaw(subject, rawCorrect, questionCount);
  return toSectionScore((lower + upper) / 2);
}

/**
 * A directional estimate from accuracy alone, for surfaces that have no raw
 * score to work from — the study plan before any full test exists.
 *
 * Deliberately routed through the same table so a dashboard estimate and a real
 * result cannot disagree about what 70% is worth, and so it too lands on a
 * multiple of ten.
 */
export function estimateScaledScore(accuracyPct: number, subject: ScoredSubject = "READING_WRITING"): number {
  const clamped = Math.max(0, Math.min(100, accuracyPct));
  const max = tableMaxRaw(subject);
  return sectionScoreForRaw(subject, Math.round((clamped / 100) * max), max);
}

/** 400-1600, in steps of ten by construction. */
export function estimateTotalScore(rw: number | null, math: number | null): number | null {
  if (rw == null || math == null) return null;
  return toSectionScore(rw) + toSectionScore(math);
}
