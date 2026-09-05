/**
 * AP practice-test configuration — data, not code paths.
 *
 * Every AP exam has a genuinely different shape. Microeconomics is one
 * 60-question multiple-choice section with a four-function calculator;
 * Calculus is two parts, one of which forbids a calculator and one of which
 * requires a graphing one; Statistics expects a graphing calculator and hands
 * out tables; Psychology's redesigned exam is 75 four-choice questions. None of
 * that can be hard-coded into a runner, so it lives here and the runner reads
 * it.
 *
 * What this file does NOT do is pick questions. It states, per section, how
 * many questions come from which units — the blueprint — and the server action
 * in `server/actions/student/ap-tests.ts` resolves that against the live
 * `ApQuestion` bank. A test whose blueprint the bank cannot fill is skipped by
 * the picker rather than started and found empty, which is what lets a config
 * for a subject still being authored (Statistics, Psychology) sit here today
 * and light up on its own the day the questions land.
 *
 * Unit weightings come from each course's CED; the per-unit counts below are
 * that weighting rounded to the section's question count, so a practice form
 * has the real exam's balance rather than an even split.
 */

/** What a student may use on a section. Wording differs per exam on purpose. */
export type ApCalculatorPolicy =
  | "NONE"
  | "FOUR_FUNCTION"
  | "GRAPHING_REQUIRED"
  | "GRAPHING_EXPECTED";

export const CALCULATOR_LABEL: Record<ApCalculatorPolicy, string> = {
  NONE: "No calculator",
  FOUR_FUNCTION: "Four-function calculator",
  GRAPHING_REQUIRED: "Graphing calculator required",
  GRAPHING_EXPECTED: "Graphing calculator expected",
};

/** How many questions this section takes from one CED unit. */
export interface ApSectionQuota {
  unit: number;
  count: number;
}

export interface ApTestSection {
  /** Stable within its test; used for section navigation and the result page. */
  id: string;
  name: string;
  /** For the section switcher, where the full name will not fit. */
  short: string;
  /** Always the sum of the blueprint — see `section()` below. */
  questionCount: number;
  timeLimitMinutes: number;
  calculator: ApCalculatorPolicy;
  /** Per-unit question counts, in the order the units are examined. */
  blueprint: ApSectionQuota[];
  /**
   * Narrows a section to particular CED topic codes. Unused today — every
   * section here is unit-scoped — but a "Series and Polar" checkpoint would
   * need it, and the selector already honours it.
   */
  topics?: string[];
  directions: string;
}

export interface ApPracticeTest {
  /** Matches ApQuestion.subject and ApTestAttempt.subject. */
  subject: string;
  /** Identifies the test within its subject: ApTestAttempt.testSlug. */
  slug: string;
  name: string;
  blurb: string;
  sections: ApTestSection[];
  /** One line naming the real exam's calculator rule, shown before starting. */
  calculatorNote: string;
  /** Formula sheets, tables — whatever the real exam supplies, or does not. */
  referenceNote?: string;
  /**
   * Which slice of the bank this form takes. Two tests on one subject must
   * differ here or they would present the same questions: the selector orders
   * each unit's questions deterministically and this form starts
   * `variant * FORM_STRIDE` into that order. Deterministic on purpose — a
   * fixed form is what makes "best score" and "last score" comparable.
   */
  variant: number;
}

/**
 * The gap between two forms' starting points in a unit's ordered pool. Any
 * value above the largest per-unit quota keeps two forms disjoint; 25 is
 * comfortably above the largest quota here (15) and still small enough that a
 * three-form subject only needs 75 questions in its heaviest unit.
 */
export const FORM_STRIDE = 25;

/** Builds a section with its question count derived from the blueprint, so the
 *  two can never disagree. */
function section(s: Omit<ApTestSection, "questionCount">): ApTestSection {
  return { ...s, questionCount: s.blueprint.reduce((n, q) => n + q.count, 0) };
}

// ---------------------------------------------------------------------------
// Economics — one 60-question multiple-choice section, 70 minutes, A-E.
// A four-function calculator has been permitted on both economics exams since
// 2017. Unit quotas follow the CED weightings in lib/ap/courses.ts.
// ---------------------------------------------------------------------------

const MICRO_BLUEPRINT: ApSectionQuota[] = [
  { unit: 1, count: 8 }, // 12-15%
  { unit: 2, count: 14 }, // 20-25%
  { unit: 3, count: 14 }, // 22-25%
  { unit: 4, count: 11 }, // 15-22%
  { unit: 5, count: 7 }, // 10-13%
  { unit: 6, count: 6 }, // 8-13%
];

const MACRO_BLUEPRINT: ApSectionQuota[] = [
  { unit: 1, count: 5 }, // 5-10%
  { unit: 2, count: 9 }, // 12-17%
  { unit: 3, count: 13 }, // 17-27%
  { unit: 4, count: 12 }, // 18-23%
  { unit: 5, count: 15 }, // 20-30%
  { unit: 6, count: 6 }, // 10-13%
];

/** The same blueprint scaled to a 30-question half-length diagnostic. */
function halve(blueprint: ApSectionQuota[], target: number): ApSectionQuota[] {
  const total = blueprint.reduce((n, q) => n + q.count, 0);
  // Largest-remainder, so the halved form keeps the weighting and hits `target`
  // exactly instead of drifting by a question or two.
  const exact = blueprint.map((q) => ({ unit: q.unit, raw: (q.count * target) / total }));
  const out = exact.map((e) => ({ unit: e.unit, count: Math.floor(e.raw) }));
  let short = target - out.reduce((n, q) => n + q.count, 0);
  const byRemainder = exact
    .map((e, i) => ({ i, rem: e.raw - Math.floor(e.raw) }))
    .sort((a, b) => b.rem - a.rem);
  for (const { i } of byRemainder) {
    if (short <= 0) break;
    out[i].count += 1;
    short -= 1;
  }
  return out.filter((q) => q.count > 0);
}

const ECON_DIRECTIONS =
  "Each question is followed by five suggested answers. Choose the one that is best in each case. Diagrams are described in words; no figures are used.";

function econTest(opts: {
  subject: string;
  slug: string;
  name: string;
  blurb: string;
  variant: number;
  blueprint: ApSectionQuota[];
  minutes: number;
  sectionName: string;
}): ApPracticeTest {
  return {
    subject: opts.subject,
    slug: opts.slug,
    name: opts.name,
    blurb: opts.blurb,
    variant: opts.variant,
    calculatorNote: "A four-function calculator is permitted on the real exam.",
    referenceNote: "No formula sheet is provided.",
    sections: [
      section({
        id: "mcq",
        name: opts.sectionName,
        short: "Section I",
        timeLimitMinutes: opts.minutes,
        calculator: "FOUR_FUNCTION",
        blueprint: opts.blueprint,
        directions: ECON_DIRECTIONS,
      }),
    ],
  };
}

// ---------------------------------------------------------------------------
// Calculus — Section I in two parts: 30 questions in 60 minutes with no
// calculator, then 15 in 45 minutes with a graphing calculator required.
// Four choices (A-D), matching the real exam and the authored bank.
// ---------------------------------------------------------------------------

const CALC_NO_CALC_DIRECTIONS =
  "Solve each problem and choose the best of the given answers. No calculator is permitted for this part. Unless otherwise specified, the domain of a function f is the set of all real numbers x for which f(x) is a real number.";
const CALC_CALC_DIRECTIONS =
  "Solve each problem and choose the best of the given answers. A graphing calculator is required for some questions in this part. The exact numerical value of the correct answer does not always appear among the choices; choose the number that best approximates it.";

const AB_PART_A: ApSectionQuota[] = [
  { unit: 1, count: 4 }, // 10-12%
  { unit: 2, count: 4 }, // 10-12%
  { unit: 3, count: 4 }, // 9-13%
  { unit: 4, count: 3 }, // 10-15%
  { unit: 5, count: 5 }, // 15-18%
  { unit: 6, count: 6 }, // 17-20%
  { unit: 7, count: 2 }, // 6-12%
  { unit: 8, count: 2 }, // 10-15%
];

const AB_PART_B: ApSectionQuota[] = [
  { unit: 4, count: 3 },
  { unit: 5, count: 2 },
  { unit: 6, count: 3 },
  { unit: 7, count: 2 },
  { unit: 8, count: 5 },
];

const BC_PART_A: ApSectionQuota[] = [
  { unit: 1, count: 2 }, // 4-7%
  { unit: 2, count: 2 }, // 4-7%
  { unit: 3, count: 2 }, // 4-7%
  { unit: 4, count: 2 }, // 6-9%
  { unit: 5, count: 3 }, // 8-11%
  { unit: 6, count: 5 }, // 17-20%
  { unit: 7, count: 2 }, // 6-9%
  { unit: 8, count: 2 }, // 6-9%
  { unit: 9, count: 4 }, // 11-12%
  { unit: 10, count: 6 }, // 17-18%
];

const BC_PART_B: ApSectionQuota[] = [
  { unit: 4, count: 1 },
  { unit: 5, count: 2 },
  { unit: 6, count: 3 },
  { unit: 7, count: 1 },
  { unit: 8, count: 2 },
  { unit: 9, count: 2 },
  { unit: 10, count: 4 },
];

function calcTest(opts: {
  subject: string;
  slug: string;
  name: string;
  blurb: string;
  variant: number;
  partA: ApSectionQuota[];
  partB: ApSectionQuota[];
}): ApPracticeTest {
  return {
    subject: opts.subject,
    slug: opts.slug,
    name: opts.name,
    blurb: opts.blurb,
    variant: opts.variant,
    calculatorNote:
      "Part A allows no calculator. Part B requires a graphing calculator — have one beside you before you start.",
    referenceNote: "No formula sheet is provided on the AP Calculus exams.",
    sections: [
      section({
        id: "part-a",
        name: "Section I, Part A — No calculator",
        short: "Part A",
        timeLimitMinutes: 60,
        calculator: "NONE",
        blueprint: opts.partA,
        directions: CALC_NO_CALC_DIRECTIONS,
      }),
      section({
        id: "part-b",
        name: "Section I, Part B — Graphing calculator required",
        short: "Part B",
        timeLimitMinutes: 45,
        calculator: "GRAPHING_REQUIRED",
        blueprint: opts.partB,
        directions: CALC_CALC_DIRECTIONS,
      }),
    ],
  };
}

// ---------------------------------------------------------------------------
// Statistics (CED effective Fall 2026) — 42 multiple-choice questions in 90
// minutes across five units, graphing calculator expected, tables supplied.
// Psychology (CED effective Fall 2024) — 75 four-choice questions in 90
// minutes across five evenly weighted units.
//
// Both banks are still being authored. The configs sit here so that the day
// the questions land the tests appear on their own; until then the picker's
// capacity check skips them.
// ---------------------------------------------------------------------------

const STATS_BLUEPRINT: ApSectionQuota[] = [
  { unit: 1, count: 11 }, // 20-30%
  { unit: 2, count: 8 }, // 15-25%
  { unit: 3, count: 9 }, // 15-25%
  { unit: 4, count: 7 }, // 10-20%
  { unit: 5, count: 7 }, // 10-20%
];

const PSYCH_BLUEPRINT: ApSectionQuota[] = [
  { unit: 1, count: 15 }, // 15-25%
  { unit: 2, count: 15 },
  { unit: 3, count: 15 },
  { unit: 4, count: 15 },
  { unit: 5, count: 15 },
];

// ---------------------------------------------------------------------------
// The tests themselves.
// ---------------------------------------------------------------------------


// ---------------------------------------------------------------------------
// The three social science exams. Each has a different Section I shape, and
// each blueprint is that course's CED unit weighting rounded to the section's
// question count, so a practice form carries the real exam's balance.
//
//   Human Geography   60 MC in 60 minutes, five choices
//   US Government     55 MC in 80 minutes, five choices
//   Comparative Gov   55 MC in 60 minutes, five choices
//
// None of the three permits a calculator. Timings and counts are taken from
// the CED records in content-pool/ap-banks/AP_*_CED.md, which were read out of
// the official Course and Exam Descriptions rather than recalled.
// ---------------------------------------------------------------------------

// CED: Unit 1 is 8-10%; Units 2-7 are 12-17% each. Rounded to 60.
const HUMAN_GEO_BLUEPRINT: ApSectionQuota[] = [
  { unit: 1, count: 6 }, // 8-10%
  { unit: 2, count: 9 }, // 12-17%
  { unit: 3, count: 9 }, // 12-17%
  { unit: 4, count: 9 }, // 12-17%
  { unit: 5, count: 9 }, // 12-17%
  { unit: 6, count: 9 }, // 12-17%
  { unit: 7, count: 9 }, // 12-17%
];

// CED: 15-22 / 25-36 / 13-18 / 10-15 / 20-27. Rounded to 55 at the midpoints.
const US_GOV_BLUEPRINT: ApSectionQuota[] = [
  { unit: 1, count: 10 }, // 15-22%
  { unit: 2, count: 17 }, // 25-36%
  { unit: 3, count: 9 },  // 13-18%
  { unit: 4, count: 6 },  // 10-15%
  { unit: 5, count: 13 }, // 20-27%
];

// CED: 18-27 / 22-33 / 11-18 / 13-18 / 16-24. Rounded to 55 at the midpoints.
/** AP Biology Section I is 60 questions in 90 minutes (CED p. 218). Counts are
 *  the midpoints of the CED's published unit weightings, which sum to 60. */
const BIOLOGY_BLUEPRINT: ApSectionQuota[] = [
  { unit: 1, count: 6 },  // 8-11%
  { unit: 2, count: 7 },  // 10-13%
  { unit: 3, count: 8 },  // 12-16%
  { unit: 4, count: 8 },  // 10-15%
  { unit: 5, count: 6 },  // 8-11%
  { unit: 6, count: 8 },  // 12-16%
  { unit: 7, count: 10 }, // 13-20%
  { unit: 8, count: 7 },  // 10-15%
];

const COMP_GOV_BLUEPRINT: ApSectionQuota[] = [
  { unit: 1, count: 12 }, // 18-27%
  { unit: 2, count: 15 }, // 22-33%
  { unit: 3, count: 8 },  // 11-18%
  { unit: 4, count: 9 },  // 13-18%
  { unit: 5, count: 11 }, // 16-24%
];

/** AP Chemistry Section I is 60 questions in 90 minutes (CED p. 205).
 *
 *  The CED's nine bands CANNOT all be met at 60 integer counts: taking the
 *  largest whole number inside each band sums to 57, three short. So three
 *  units have to sit one question above their band, and the choice was made
 *  by minimising the WORST distortion rather than the number of units touched
 *  -- spreading three 1.0-point overshoots beats concentrating a single
 *  2.7-point one, since no unit then misrepresents its share by more than the
 *  one question that is the smallest error available at n=60. The three
 *  extras go to the units with the most instructional time among those tied,
 *  which is the CED's own other measure of a unit's size. */
const CHEMISTRY_BLUEPRINT: ApSectionQuota[] = [
  { unit: 1, count: 5 },  // 7-9%,   8.3%
  { unit: 2, count: 5 },  // 7-9%,   8.3%
  { unit: 3, count: 13 }, // 18-22%, 21.7%
  { unit: 4, count: 6 },  // 7-9%,  10.0%  (+1 question, ~14-15 class periods)
  { unit: 5, count: 6 },  // 7-9%,  10.0%  (+1 question, ~13-14 class periods)
  { unit: 6, count: 5 },  // 7-9%,   8.3%
  { unit: 7, count: 6 },  // 7-9%,  10.0%  (+1 question, ~13-15 class periods)
  { unit: 8, count: 9 },  // 11-15%, 15.0%
  { unit: 9, count: 5 },  // 7-9%,   8.3%
];

/** AP Environmental Science Section I is 80 questions in 90 minutes
 *  (CED p. 191). Every count here falls inside its published band. */
const ENV_SCI_BLUEPRINT: ApSectionQuota[] = [
  { unit: 1, count: 6 },  // 6-8%,    7.5%
  { unit: 2, count: 6 },  // 6-8%,    7.5%
  { unit: 3, count: 10 }, // 10-15%, 12.5%
  { unit: 4, count: 10 }, // 10-15%, 12.5%
  { unit: 5, count: 10 }, // 10-15%, 12.5%
  { unit: 6, count: 10 }, // 10-15%, 12.5%
  { unit: 7, count: 7 },  // 7-10%,   8.8%
  { unit: 8, count: 7 },  // 7-10%,   8.8%
  { unit: 9, count: 14 }, // 15-20%, 17.5%
];

/** AP World History: Modern Section I Part A is 55 questions in 55 minutes
 *  (CED p. 202; the section is 40% of the exam).
 *
 *  Every unit lands INSIDE its published band, and the total is exactly 55 --
 *  unlike Chemistry, where the bands could not be met at 60 integer counts.
 *  Units 3 to 6 all sit at 12-15%, so two of the four must take 8 questions and
 *  two take 7; the CED's own class-period allocation breaks the tie, giving the
 *  extra question to units 4 (~22-25 periods) and 5 (~20-23) over units 3
 *  (~8-11) and 6 (~12-15). */
const WORLD_HISTORY_BLUEPRINT: ApSectionQuota[] = [
  { unit: 1, count: 5 }, // 8-10%,   9.1%
  { unit: 2, count: 5 }, // 8-10%,   9.1%
  { unit: 3, count: 7 }, // 12-15%, 12.7%
  { unit: 4, count: 8 }, // 12-15%, 14.5%
  { unit: 5, count: 8 }, // 12-15%, 14.5%
  { unit: 6, count: 7 }, // 12-15%, 12.7%
  { unit: 7, count: 5 }, // 8-10%,   9.1%
  { unit: 8, count: 5 }, // 8-10%,   9.1%
  { unit: 9, count: 5 }, // 8-10%,   9.1%
];

export const AP_TESTS: ApPracticeTest[] = [
  // --- Microeconomics ---
  econTest({
    subject: "MICRO",
    slug: "diagnostic",
    name: "Microeconomics Diagnostic",
    blurb:
      "Half a real Section I, weighted like the exam. The fastest way to find which of the six units is costing you the most.",
    variant: 0,
    blueprint: halve(MICRO_BLUEPRINT, 30),
    minutes: 35,
    sectionName: "Diagnostic — Multiple Choice",
  }),
  econTest({
    subject: "MICRO",
    slug: "practice-1",
    name: "Microeconomics Practice Exam 1",
    blurb: "A full Section I: 60 questions in 70 minutes, weighted to the CED.",
    variant: 1,
    blueprint: MICRO_BLUEPRINT,
    minutes: 70,
    sectionName: "Section I — Multiple Choice",
  }),
  econTest({
    subject: "MICRO",
    slug: "practice-2",
    name: "Microeconomics Practice Exam 2",
    blurb: "A second full form, drawing on different questions from the first.",
    variant: 2,
    blueprint: MICRO_BLUEPRINT,
    minutes: 70,
    sectionName: "Section I — Multiple Choice",
  }),

  // --- Macroeconomics ---
  econTest({
    subject: "MACRO",
    slug: "diagnostic",
    name: "Macroeconomics Diagnostic",
    blurb:
      "Half a real Section I, weighted like the exam — enough to place your weakest unit in about half an hour.",
    variant: 0,
    blueprint: halve(MACRO_BLUEPRINT, 30),
    minutes: 35,
    sectionName: "Diagnostic — Multiple Choice",
  }),
  econTest({
    subject: "MACRO",
    slug: "practice-1",
    name: "Macroeconomics Practice Exam 1",
    blurb: "A full Section I: 60 questions in 70 minutes, weighted to the CED.",
    variant: 1,
    blueprint: MACRO_BLUEPRINT,
    minutes: 70,
    sectionName: "Section I — Multiple Choice",
  }),
  econTest({
    subject: "MACRO",
    slug: "practice-2",
    name: "Macroeconomics Practice Exam 2",
    blurb: "A second full form, drawing on different questions from the first.",
    variant: 2,
    blueprint: MACRO_BLUEPRINT,
    minutes: 70,
    sectionName: "Section I — Multiple Choice",
  }),

  // --- Calculus AB ---
  {
    subject: "CALC_AB",
    slug: "diagnostic",
    name: "Calculus AB Diagnostic",
    blurb:
      "Twenty no-calculator questions across all eight units, in forty minutes. A placement check, not a full sitting.",
    variant: 0,
    calculatorNote: "No calculator — this diagnostic is drawn from Part A style questions only.",
    referenceNote: "No formula sheet is provided on the AP Calculus exams.",
    sections: [
      section({
        id: "diagnostic",
        name: "Diagnostic — No calculator",
        short: "Diagnostic",
        timeLimitMinutes: 40,
        calculator: "NONE",
        blueprint: [
          { unit: 1, count: 3 },
          { unit: 2, count: 3 },
          { unit: 3, count: 2 },
          { unit: 4, count: 2 },
          { unit: 5, count: 3 },
          { unit: 6, count: 4 },
          { unit: 7, count: 1 },
          { unit: 8, count: 2 },
        ],
        directions: CALC_NO_CALC_DIRECTIONS,
      }),
    ],
  },
  calcTest({
    subject: "CALC_AB",
    slug: "practice-1",
    name: "Calculus AB Practice Exam 1",
    blurb:
      "The real Section I: 30 questions in 60 minutes with no calculator, then 15 in 45 with a graphing calculator.",
    variant: 1,
    partA: AB_PART_A,
    partB: AB_PART_B,
  }),
  calcTest({
    subject: "CALC_AB",
    slug: "practice-2",
    name: "Calculus AB Practice Exam 2",
    blurb: "A second full Section I, on different questions from the first.",
    variant: 2,
    partA: AB_PART_A,
    partB: AB_PART_B,
  }),

  // --- Calculus BC ---
  {
    subject: "CALC_BC",
    slug: "diagnostic",
    name: "Calculus BC Diagnostic",
    blurb:
      "Twenty no-calculator questions weighted towards series, parametrics and polars — the BC-only material AB students never see.",
    variant: 0,
    calculatorNote: "No calculator — this diagnostic is drawn from Part A style questions only.",
    referenceNote: "No formula sheet is provided on the AP Calculus exams.",
    sections: [
      section({
        id: "diagnostic",
        name: "Diagnostic — No calculator",
        short: "Diagnostic",
        timeLimitMinutes: 40,
        calculator: "NONE",
        blueprint: [
          { unit: 1, count: 1 },
          { unit: 2, count: 1 },
          { unit: 3, count: 1 },
          { unit: 4, count: 2 },
          { unit: 5, count: 2 },
          { unit: 6, count: 3 },
          { unit: 7, count: 1 },
          { unit: 8, count: 2 },
          { unit: 9, count: 3 },
          { unit: 10, count: 4 },
        ],
        directions: CALC_NO_CALC_DIRECTIONS,
      }),
    ],
  },
  calcTest({
    subject: "CALC_BC",
    slug: "practice-1",
    name: "Calculus BC Practice Exam 1",
    blurb:
      "The real Section I: 30 questions in 60 minutes with no calculator, then 15 in 45 with a graphing calculator.",
    variant: 1,
    partA: BC_PART_A,
    partB: BC_PART_B,
  }),
  calcTest({
    subject: "CALC_BC",
    slug: "practice-2",
    name: "Calculus BC Practice Exam 2",
    blurb: "A second full Section I, on different questions from the first.",
    variant: 2,
    partA: BC_PART_A,
    partB: BC_PART_B,
  }),

  // --- Statistics (bank in progress) ---
  {
    subject: "STATISTICS",
    slug: "diagnostic",
    name: "Statistics Diagnostic",
    blurb: "Half a Section I across the five units of the redesigned course.",
    variant: 0,
    calculatorNote:
      "A graphing calculator with statistical capabilities is expected throughout the real exam.",
    referenceNote: "Formulas and the normal, t and chi-square tables are supplied on the exam.",
    sections: [
      section({
        id: "mcq",
        name: "Diagnostic — Multiple Choice",
        short: "Diagnostic",
        timeLimitMinutes: 45,
        calculator: "GRAPHING_EXPECTED",
        blueprint: halve(STATS_BLUEPRINT, 21),
        directions:
          "Choose the best answer to each question. A graphing calculator with statistical capabilities is expected.",
      }),
    ],
  },
  {
    subject: "STATISTICS",
    slug: "practice-1",
    name: "Statistics Practice Exam 1",
    blurb: "A full Section I: 42 multiple-choice questions in 90 minutes.",
    variant: 1,
    calculatorNote:
      "A graphing calculator with statistical capabilities is expected throughout the real exam.",
    referenceNote: "Formulas and the normal, t and chi-square tables are supplied on the exam.",
    sections: [
      section({
        id: "mcq",
        name: "Section I — Multiple Choice",
        short: "Section I",
        timeLimitMinutes: 90,
        calculator: "GRAPHING_EXPECTED",
        blueprint: STATS_BLUEPRINT,
        directions:
          "Choose the best answer to each question. Some questions share a common prompt. A graphing calculator with statistical capabilities is expected.",
      }),
    ],
  },

  // --- Psychology (bank in progress) ---
  {
    subject: "PSYCHOLOGY",
    slug: "diagnostic",
    name: "Psychology Diagnostic",
    blurb: "Half a Section I, spread evenly across the five units.",
    variant: 0,
    calculatorNote: "No calculator is used on the AP Psychology exam.",
    referenceNote: "Multiple-choice questions have four answer choices on the redesigned exam.",
    sections: [
      section({
        id: "mcq",
        name: "Diagnostic — Multiple Choice",
        short: "Diagnostic",
        timeLimitMinutes: 45,
        calculator: "NONE",
        blueprint: halve(PSYCH_BLUEPRINT, 40),
        directions:
          "Each question is followed by four suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "PSYCHOLOGY",
    slug: "practice-1",
    name: "Psychology Practice Exam 1",
    blurb: "A full Section I: 75 four-choice questions in 90 minutes.",
    variant: 1,
    calculatorNote: "No calculator is used on the AP Psychology exam.",
    referenceNote: "Multiple-choice questions have four answer choices on the redesigned exam.",
    sections: [
      section({
        id: "mcq",
        name: "Section I — Multiple Choice",
        short: "Section I",
        timeLimitMinutes: 90,
        calculator: "NONE",
        blueprint: PSYCH_BLUEPRINT,
        directions:
          "Each question is followed by four suggested answers. Choose the one that is best in each case. Section I contains both discrete and set-based questions.",
      }),
    ],
  },
  {
    subject: "HUMAN_GEO",
    slug: "diagnostic",
    name: "Human Geography Diagnostic",
    blurb: "Half a Section I, weighted across all seven units.",
    variant: 0,
    calculatorNote: "No calculator is used on the AP Human Geography exam.",
    referenceNote: "Multiple-choice questions have five answer choices.",
    sections: [
      section({
        id: "mcq",
        name: "Diagnostic — Multiple Choice",
        short: "Diagnostic",
        timeLimitMinutes: 30,
        calculator: "NONE",
        blueprint: halve(HUMAN_GEO_BLUEPRINT, 30),
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "HUMAN_GEO",
    slug: "practice-1",
    name: "Human Geography Practice Exam 1",
    blurb: "A full Section I: 60 questions in 60 minutes.",
    variant: 1,
    calculatorNote: "No calculator is used on the AP Human Geography exam.",
    referenceNote: "Multiple-choice questions have five answer choices.",
    sections: [
      section({
        id: "mcq",
        name: "Section I — Multiple Choice",
        short: "Section I",
        timeLimitMinutes: 60,
        calculator: "NONE",
        blueprint: HUMAN_GEO_BLUEPRINT,
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "US_GOV",
    slug: "diagnostic",
    name: "US Government Diagnostic",
    blurb: "Half a Section I, weighted across all five units.",
    variant: 0,
    calculatorNote: "No calculator is used on the AP U.S. Government and Politics exam.",
    referenceNote: "Multiple-choice questions have five answer choices.",
    sections: [
      section({
        id: "mcq",
        name: "Diagnostic — Multiple Choice",
        short: "Diagnostic",
        timeLimitMinutes: 40,
        calculator: "NONE",
        blueprint: halve(US_GOV_BLUEPRINT, 28),
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "US_GOV",
    slug: "practice-1",
    name: "US Government Practice Exam 1",
    blurb: "A full Section I: 55 questions in 80 minutes.",
    variant: 1,
    calculatorNote: "No calculator is used on the AP U.S. Government and Politics exam.",
    referenceNote: "Multiple-choice questions have five answer choices.",
    sections: [
      section({
        id: "mcq",
        name: "Section I — Multiple Choice",
        short: "Section I",
        timeLimitMinutes: 80,
        calculator: "NONE",
        blueprint: US_GOV_BLUEPRINT,
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "COMP_GOV",
    slug: "diagnostic",
    name: "Comparative Government Diagnostic",
    blurb: "Half a Section I, weighted across all five units.",
    variant: 0,
    calculatorNote: "No calculator is used on the AP Comparative Government and Politics exam.",
    referenceNote: "Multiple-choice questions have five answer choices.",
    sections: [
      section({
        id: "mcq",
        name: "Diagnostic — Multiple Choice",
        short: "Diagnostic",
        timeLimitMinutes: 30,
        calculator: "NONE",
        blueprint: halve(COMP_GOV_BLUEPRINT, 28),
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "COMP_GOV",
    slug: "practice-1",
    name: "Comparative Government Practice Exam 1",
    blurb: "A full Section I: 55 questions in 60 minutes.",
    variant: 1,
    calculatorNote: "No calculator is used on the AP Comparative Government and Politics exam.",
    referenceNote: "Multiple-choice questions have five answer choices.",
    sections: [
      section({
        id: "mcq",
        name: "Section I — Multiple Choice",
        short: "Section I",
        timeLimitMinutes: 60,
        calculator: "NONE",
        blueprint: COMP_GOV_BLUEPRINT,
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "BIOLOGY",
    slug: "diagnostic",
    name: "Biology Diagnostic",
    blurb: "Half a Section I, weighted across all eight units.",
    variant: 0,
    calculatorNote: "A four-function, scientific, or graphing calculator is allowed on the whole AP Biology exam.",
    referenceNote: "Multiple-choice questions have four answer choices on the real exam; this bank uses five.",
    sections: [
      section({
        id: "mcq",
        name: "Diagnostic — Multiple Choice",
        short: "Diagnostic",
        timeLimitMinutes: 45,
        calculator: "FOUR_FUNCTION",
        blueprint: halve(BIOLOGY_BLUEPRINT, 30),
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "BIOLOGY",
    slug: "practice-1",
    name: "Biology Practice Exam 1",
    blurb: "A full Section I: 60 questions in 90 minutes.",
    variant: 1,
    calculatorNote: "A four-function, scientific, or graphing calculator is allowed on the whole AP Biology exam.",
    referenceNote: "Multiple-choice questions have four answer choices on the real exam; this bank uses five.",
    sections: [
      section({
        id: "mcq",
        name: "Section I — Multiple Choice",
        short: "Section I",
        timeLimitMinutes: 90,
        calculator: "FOUR_FUNCTION",
        blueprint: BIOLOGY_BLUEPRINT,
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "CHEMISTRY",
    slug: "diagnostic",
    name: "Chemistry Diagnostic",
    blurb: "Half a Section I, weighted across all nine units.",
    variant: 0,
    calculatorNote: "A four-function, scientific, or graphing calculator is allowed on the whole AP Chemistry exam.",
    referenceNote: "Multiple-choice questions have four answer choices on the real exam; this bank uses five.",
    sections: [
      section({
        id: "mcq",
        name: "Diagnostic — Multiple Choice",
        short: "Diagnostic",
        timeLimitMinutes: 45,
        calculator: "FOUR_FUNCTION",
        blueprint: halve(CHEMISTRY_BLUEPRINT, 30),
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "CHEMISTRY",
    slug: "practice-1",
    name: "Chemistry Practice Exam 1",
    blurb: "A full Section I: 60 questions in 90 minutes.",
    variant: 1,
    calculatorNote: "A four-function, scientific, or graphing calculator is allowed on the whole AP Chemistry exam.",
    referenceNote: "Multiple-choice questions have four answer choices on the real exam; this bank uses five.",
    sections: [
      section({
        id: "mcq",
        name: "Section I — Multiple Choice",
        short: "Section I",
        timeLimitMinutes: 90,
        calculator: "FOUR_FUNCTION",
        blueprint: CHEMISTRY_BLUEPRINT,
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "ENV_SCI",
    slug: "diagnostic",
    name: "Environmental Science Diagnostic",
    blurb: "Half a Section I, weighted across all nine units.",
    variant: 0,
    calculatorNote: "A four-function, scientific, or graphing calculator is allowed on the whole AP Environmental Science exam.",
    referenceNote: "Multiple-choice questions have four answer choices on the real exam; this bank uses five.",
    sections: [
      section({
        id: "mcq",
        name: "Diagnostic — Multiple Choice",
        short: "Diagnostic",
        timeLimitMinutes: 45,
        calculator: "FOUR_FUNCTION",
        blueprint: halve(ENV_SCI_BLUEPRINT, 40),
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "ENV_SCI",
    slug: "practice-1",
    name: "Environmental Science Practice Exam 1",
    blurb: "A full Section I: 80 questions in 90 minutes.",
    variant: 1,
    calculatorNote: "A four-function, scientific, or graphing calculator is allowed on the whole AP Environmental Science exam.",
    referenceNote: "Multiple-choice questions have four answer choices on the real exam; this bank uses five.",
    sections: [
      section({
        id: "mcq",
        name: "Section I — Multiple Choice",
        short: "Section I",
        timeLimitMinutes: 90,
        calculator: "FOUR_FUNCTION",
        blueprint: ENV_SCI_BLUEPRINT,
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },

  {
    subject: "WORLD_HISTORY",
    slug: "diagnostic",
    name: "World History Diagnostic",
    blurb: "Half a Section I, weighted across all nine units.",
    variant: 0,
    calculatorNote: "No calculator is used on the AP World History: Modern exam.",
    referenceNote: "Multiple-choice questions have four answer choices on the real exam; this bank uses five.",
    sections: [
      section({
        id: "mcq",
        name: "Diagnostic — Multiple Choice",
        short: "Diagnostic",
        timeLimitMinutes: 28,
        calculator: "NONE",
        blueprint: halve(WORLD_HISTORY_BLUEPRINT, 28),
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
  {
    subject: "WORLD_HISTORY",
    slug: "practice-1",
    name: "World History Practice Exam 1",
    blurb: "A full Section I Part A: 55 questions in 55 minutes.",
    variant: 1,
    calculatorNote: "No calculator is used on the AP World History: Modern exam.",
    referenceNote: "Multiple-choice questions have four answer choices on the real exam; this bank uses five.",
    sections: [
      section({
        id: "mcq",
        name: "Section I, Part A — Multiple Choice",
        short: "Section I",
        timeLimitMinutes: 55,
        calculator: "NONE",
        blueprint: WORLD_HISTORY_BLUEPRINT,
        directions: "Each question is followed by five suggested answers. Choose the one that is best in each case.",
      }),
    ],
  },
];

// ---------------------------------------------------------------------------
// Lookups and derived facts
// ---------------------------------------------------------------------------

export function testsForSubject(subject: string): ApPracticeTest[] {
  return AP_TESTS.filter((t) => t.subject === subject);
}

export function findTest(subject: string, slug: string): ApPracticeTest | undefined {
  return AP_TESTS.find((t) => t.subject === subject && t.slug === slug);
}

export function testQuestionCount(test: ApPracticeTest): number {
  return test.sections.reduce((n, s) => n + s.questionCount, 0);
}

export function testDurationMinutes(test: ApPracticeTest): number {
  return test.sections.reduce((n, s) => n + s.timeLimitMinutes, 0);
}

/** Every unit any section of this test draws on, ascending. */
export function testUnits(test: ApPracticeTest): number[] {
  const units = new Set<number>();
  for (const s of test.sections) for (const q of s.blueprint) units.add(q.unit);
  return [...units].sort((a, b) => a - b);
}

/**
 * How many questions this test needs from each unit, across all its sections.
 * The capacity check compares this against the bank; the picker skips any test
 * the bank cannot fill.
 */
export function testDemandByUnit(test: ApPracticeTest): Map<number, number> {
  const demand = new Map<number, number>();
  for (const s of test.sections) {
    for (const q of s.blueprint) demand.set(q.unit, (demand.get(q.unit) ?? 0) + q.count);
  }
  return demand;
}

/**
 * Where each section starts in the attempt's frozen question list. Sections are
 * laid out back to back in configuration order, so a flat array of ids is all
 * the attempt has to store.
 */
export function sectionOffsets(test: ApPracticeTest): number[] {
  const offsets: number[] = [];
  let running = 0;
  for (const s of test.sections) {
    offsets.push(running);
    running += s.questionCount;
  }
  return offsets;
}

/** Human duration, e.g. "1 hr 45 min". */
export function formatDuration(minutes: number): string {
  const h = Math.floor(minutes / 60);
  const m = minutes % 60;
  if (h === 0) return `${m} min`;
  if (m === 0) return h === 1 ? "1 hr" : `${h} hr`;
  return `${h} hr ${m} min`;
}
