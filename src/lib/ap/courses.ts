/**
 * The AP course catalog — static on purpose. Units and topic lists come from
 * the College Board Course and Exam Descriptions and change once a year at
 * most; a database table for four courses would be ceremony. Question CONTENT
 * lives in the ApQuestion table and is joined onto this by (subject, topic).
 */

export type ApSubjectCode = "MACRO" | "MICRO" | "CALC_AB" | "CALC_BC";

export interface ApUnit {
  number: number;
  title: string;
  /** Topics with authored question content, e.g. [{code:"1.1", title:"…"}]. */
  topics?: { code: string; title: string }[];
}

export interface ApCourse {
  code: ApSubjectCode;
  slug: string;
  name: string;
  short: string;
  blurb: string;
  /** Tailwind gradient classes for the subject card. */
  gradient: string;
  units: ApUnit[];
}

/** AP Micro Unit 1's topics — the unit that ships with a live question bank. */
const MICRO_UNIT1_TOPICS = [
  { code: "1.1", title: "Scarcity" },
  { code: "1.2", title: "Resource Allocation and Economic Systems" },
  { code: "1.3", title: "Production Possibilities Curve" },
  { code: "1.4", title: "Comparative Advantage and Trade" },
  { code: "1.5", title: "Cost-Benefit Analysis" },
  { code: "1.6", title: "Marginal Analysis and Consumer Choice" },
];

export const AP_COURSES: ApCourse[] = [
  {
    code: "MACRO",
    slug: "macroeconomics",
    name: "AP Macroeconomics",
    short: "Macro",
    blurb: "The economy as a whole — output, inflation, unemployment, and policy.",
    gradient: "from-amber-500 to-orange-600",
    units: [
      { number: 1, title: "Basic Economic Concepts" },
      { number: 2, title: "Economic Indicators and the Business Cycle" },
      { number: 3, title: "National Income and Price Determination" },
      { number: 4, title: "Financial Sector" },
      { number: 5, title: "Long-Run Consequences of Stabilization Policies" },
      { number: 6, title: "Open Economy — International Trade and Finance" },
    ],
  },
  {
    code: "MICRO",
    slug: "microeconomics",
    name: "AP Microeconomics",
    short: "Micro",
    blurb: "How consumers, firms, and markets make decisions under scarcity.",
    gradient: "from-emerald-500 to-teal-600",
    units: [
      { number: 1, title: "Basic Economic Concepts", topics: MICRO_UNIT1_TOPICS },
      { number: 2, title: "Supply and Demand" },
      { number: 3, title: "Production, Cost, and the Perfect Competition Model" },
      { number: 4, title: "Imperfect Competition" },
      { number: 5, title: "Factor Markets" },
      { number: 6, title: "Market Failure and the Role of Government" },
    ],
  },
  {
    code: "CALC_AB",
    slug: "calculus-ab",
    name: "AP Calculus AB",
    short: "Calc AB",
    blurb: "Limits, derivatives, integrals, and the fundamental theorem.",
    gradient: "from-rose-500 to-pink-600",
    units: [
      { number: 1, title: "Limits and Continuity" },
      { number: 2, title: "Differentiation: Definition and Fundamental Properties" },
      { number: 3, title: "Differentiation: Composite, Implicit, and Inverse Functions" },
      { number: 4, title: "Contextual Applications of Differentiation" },
      { number: 5, title: "Analytical Applications of Differentiation" },
      { number: 6, title: "Integration and Accumulation of Change" },
      { number: 7, title: "Differential Equations" },
      { number: 8, title: "Applications of Integration" },
    ],
  },
  {
    code: "CALC_BC",
    slug: "calculus-bc",
    name: "AP Calculus BC",
    short: "Calc BC",
    blurb: "Everything in AB plus series, parametrics, polars, and vectors.",
    gradient: "from-indigo-500 to-violet-600",
    units: [
      { number: 1, title: "Limits and Continuity" },
      { number: 2, title: "Differentiation: Definition and Fundamental Properties" },
      { number: 3, title: "Differentiation: Composite, Implicit, and Inverse Functions" },
      { number: 4, title: "Contextual Applications of Differentiation" },
      { number: 5, title: "Analytical Applications of Differentiation" },
      { number: 6, title: "Integration and Accumulation of Change" },
      { number: 7, title: "Differential Equations" },
      { number: 8, title: "Applications of Integration" },
      { number: 9, title: "Parametric Equations, Polar Coordinates, and Vector-Valued Functions" },
      { number: 10, title: "Infinite Sequences and Series" },
    ],
  },
];

export function courseBySlug(slug: string): ApCourse | undefined {
  return AP_COURSES.find((c) => c.slug === slug);
}

/** The next AP exam season's opening day. */
export const AP_EXAM_START = new Date("2027-05-03T00:00:00Z");

export function daysUntilExams(now = new Date()): number {
  return Math.max(0, Math.ceil((AP_EXAM_START.getTime() - now.getTime()) / 86_400_000));
}
