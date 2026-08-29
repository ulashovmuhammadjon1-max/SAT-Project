/**
 * The AP course catalog — static on purpose. Units, topics and exam weights
 * come from the College Board Course and Exam Descriptions and change once a
 * year at most; a database table for four courses would be ceremony. Question
 * CONTENT lives in the ApQuestion table, joined onto this by (subject, topic).
 *
 * A topic listed here only becomes visible once questions exist for it, so the
 * full official outline can sit here while the banks are still being written.
 */

export type ApSubjectCode = "MACRO" | "MICRO" | "CALC_AB" | "CALC_BC";

export interface ApUnit {
  number: number;
  title: string;
  /** Exam weighting from the CED, e.g. "12–15%". */
  weight?: string;
  /** One line on what the unit covers. */
  blurb?: string;
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

// ---------------------------------------------------------------------------
// AP Microeconomics
// ---------------------------------------------------------------------------

const MICRO_UNITS: ApUnit[] = [
  {
    number: 1,
    title: "Basic Economic Concepts",
    weight: "12–15%",
    blurb: "Scarcity, opportunity cost, the PPC, comparative advantage, and marginal analysis.",
    topics: [
      { code: "1.1", title: "Scarcity" },
      { code: "1.2", title: "Resource Allocation and Economic Systems" },
      { code: "1.3", title: "Production Possibilities Curve" },
      { code: "1.4", title: "Comparative Advantage and Trade" },
      { code: "1.5", title: "Cost-Benefit Analysis" },
      { code: "1.6", title: "Marginal Analysis and Consumer Choice" },
    ],
  },
  {
    number: 2,
    title: "Supply and Demand",
    weight: "20–25%",
    blurb: "Demand, supply, elasticity, equilibrium, surplus, and government intervention.",
    topics: [
      { code: "2.1", title: "Demand" },
      { code: "2.2", title: "Supply" },
      { code: "2.3", title: "Price Elasticity of Demand" },
      { code: "2.4", title: "Price Elasticity of Supply" },
      { code: "2.5", title: "Other Elasticities" },
      { code: "2.6", title: "Market Equilibrium and Consumer and Producer Surplus" },
      { code: "2.7", title: "Market Disequilibrium and Changes in Equilibrium" },
      { code: "2.8", title: "The Effects of Government Intervention in Markets" },
      { code: "2.9", title: "International Trade and Public Policy" },
    ],
  },
  {
    number: 3,
    title: "Production, Cost, and the Perfect Competition Model",
    weight: "22–25%",
    blurb: "Production functions, cost curves, profit, and the perfectly competitive firm.",
    topics: [
      { code: "3.1", title: "The Production Function" },
      { code: "3.2", title: "Short-Run Production Costs" },
      { code: "3.3", title: "Long-Run Production Costs" },
      { code: "3.4", title: "Types of Profit" },
      { code: "3.5", title: "Profit Maximization" },
      { code: "3.6", title: "Firms' Entry and Exit Decisions" },
      { code: "3.7", title: "Perfect Competition" },
    ],
  },
  {
    number: 4,
    title: "Imperfect Competition",
    weight: "15–22%",
    blurb: "Monopoly, price discrimination, monopolistic competition, oligopoly and game theory.",
    topics: [
      { code: "4.1", title: "Introduction to Imperfectly Competitive Markets" },
      { code: "4.2", title: "Monopoly" },
      { code: "4.3", title: "Price Discrimination" },
      { code: "4.4", title: "Monopolistic Competition" },
      { code: "4.5", title: "Oligopoly and Game Theory" },
    ],
  },
  {
    number: 5,
    title: "Factor Markets",
    weight: "10–13%",
    blurb: "Derived demand for resources, marginal revenue product, and monopsony.",
    topics: [
      { code: "5.1", title: "Introduction to Factor Markets" },
      { code: "5.2", title: "Changes in Factor Demand and Factor Supply" },
      { code: "5.3", title: "Profit-Maximizing Behavior in Perfectly Competitive Factor Markets" },
      { code: "5.4", title: "Monopsonistic Markets" },
    ],
  },
  {
    number: 6,
    title: "Market Failure and the Role of Government",
    weight: "8–13%",
    blurb: "Efficiency, externalities, public goods, regulation, and inequality.",
    topics: [
      { code: "6.1", title: "Socially Efficient and Inefficient Market Outcomes" },
      { code: "6.2", title: "Externalities" },
      { code: "6.3", title: "Public and Private Goods" },
      { code: "6.4", title: "Effects of Government Intervention in Different Market Structures" },
      { code: "6.5", title: "Income and Wealth Inequality" },
    ],
  },
];

// ---------------------------------------------------------------------------
// AP Macroeconomics
// ---------------------------------------------------------------------------

const MACRO_UNITS: ApUnit[] = [
  {
    number: 1,
    title: "Basic Economic Concepts",
    weight: "5–10%",
    blurb: "Scarcity, the PPC, comparative advantage, and the supply-and-demand model.",
    topics: [
      { code: "1.1", title: "Scarcity" },
      { code: "1.2", title: "Opportunity Cost and the Production Possibilities Curve" },
      { code: "1.3", title: "Comparative Advantage and Gains from Trade" },
      { code: "1.4", title: "Demand" },
      { code: "1.5", title: "Supply" },
      { code: "1.6", title: "Market Equilibrium, Disequilibrium, and Changes in Equilibrium" },
    ],
  },
  {
    number: 2,
    title: "Economic Indicators and the Business Cycle",
    weight: "12–17%",
    blurb: "GDP, unemployment, inflation and price indices, and the business cycle.",
    topics: [
      { code: "2.1", title: "The Circular Flow and GDP" },
      { code: "2.2", title: "Limitations of GDP" },
      { code: "2.3", title: "Unemployment" },
      { code: "2.4", title: "Price Indices and Inflation" },
      { code: "2.5", title: "Costs of Inflation" },
      { code: "2.6", title: "Real vs. Nominal GDP" },
      { code: "2.7", title: "Business Cycles" },
    ],
  },
  {
    number: 3,
    title: "National Income and Price Determination",
    weight: "17–27%",
    blurb: "Aggregate demand and supply, multipliers, equilibrium, and fiscal policy.",
    topics: [
      { code: "3.1", title: "Aggregate Demand" },
      { code: "3.2", title: "Multipliers" },
      { code: "3.3", title: "Short-Run Aggregate Supply" },
      { code: "3.4", title: "Long-Run Aggregate Supply" },
      { code: "3.5", title: "Equilibrium in the AD-AS Model" },
      { code: "3.6", title: "Changes in the AD-AS Model in the Short Run" },
      { code: "3.7", title: "Long-Run Self-Adjustment" },
      { code: "3.8", title: "Fiscal Policy" },
      { code: "3.9", title: "Automatic Stabilizers" },
    ],
  },
  {
    number: 4,
    title: "Financial Sector",
    weight: "18–23%",
    blurb: "Money, banking, the money market, loanable funds, and monetary policy.",
    topics: [
      { code: "4.1", title: "Financial Assets" },
      { code: "4.2", title: "Nominal vs. Real Interest Rates" },
      { code: "4.3", title: "Definition, Measurement, and Functions of Money" },
      { code: "4.4", title: "Banking and the Expansion of the Money Supply" },
      { code: "4.5", title: "The Money Market" },
      { code: "4.6", title: "Monetary Policy" },
      { code: "4.7", title: "The Loanable Funds Market" },
    ],
  },
  {
    number: 5,
    title: "Long-Run Consequences of Stabilization Policies",
    weight: "20–30%",
    blurb: "The Phillips curve, inflation, deficits and debt, crowding out, and growth.",
    topics: [
      { code: "5.1", title: "Fiscal and Monetary Policy Actions in the Short Run" },
      { code: "5.2", title: "The Phillips Curve" },
      { code: "5.3", title: "Money Growth and Inflation" },
      { code: "5.4", title: "Government Deficits and the National Debt" },
      { code: "5.5", title: "Crowding Out" },
      { code: "5.6", title: "Economic Growth" },
      { code: "5.7", title: "Public Policy and Economic Growth" },
    ],
  },
  {
    number: 6,
    title: "Open Economy — International Trade and Finance",
    weight: "10–13%",
    blurb: "Balance of payments, exchange rates, and international capital flows.",
    topics: [
      { code: "6.1", title: "Balance of Payments Accounts" },
      { code: "6.2", title: "Exchange Rates" },
      { code: "6.3", title: "The Foreign Exchange Market" },
      { code: "6.4", title: "Policy and Economic Conditions in the Foreign Exchange Market" },
      { code: "6.5", title: "Changes in the Foreign Exchange Market and Net Exports" },
      { code: "6.6", title: "Real Interest Rates and International Capital Flows" },
    ],
  },
];

// ---------------------------------------------------------------------------
// AP Calculus AB and BC — BC is AB's ten units, the last two BC-only.
// ---------------------------------------------------------------------------

const CALC_UNITS: ApUnit[] = [
  { number: 1, title: "Limits and Continuity", blurb: "Limits, asymptotes, continuity, and the squeeze theorem." },
  { number: 2, title: "Differentiation: Definition and Fundamental Properties", blurb: "The derivative, power/product/quotient rules." },
  { number: 3, title: "Differentiation: Composite, Implicit, and Inverse Functions", blurb: "The chain rule, implicit differentiation, inverses." },
  { number: 4, title: "Contextual Applications of Differentiation", blurb: "Rates of change, related rates, linearization, L'Hospital." },
  { number: 5, title: "Analytical Applications of Differentiation", blurb: "Extrema, concavity, curve sketching, optimization." },
  { number: 6, title: "Integration and Accumulation of Change", blurb: "Riemann sums, antiderivatives, the fundamental theorem." },
  { number: 7, title: "Differential Equations", blurb: "Slope fields, separation of variables, exponential models." },
  { number: 8, title: "Applications of Integration", blurb: "Average value, area, volume, and arc length." },
];

const CALC_BC_ONLY: ApUnit[] = [
  { number: 9, title: "Parametric Equations, Polar Coordinates, and Vector-Valued Functions", blurb: "BC only — calculus beyond y = f(x)." },
  { number: 10, title: "Infinite Sequences and Series", blurb: "BC only — convergence tests, Taylor and Maclaurin series." },
];

export const AP_COURSES: ApCourse[] = [
  {
    code: "MACRO",
    slug: "macroeconomics",
    name: "AP Macroeconomics",
    short: "Macro",
    blurb: "The economy as a whole — output, inflation, unemployment, and policy.",
    gradient: "from-amber-500 to-orange-600",
    units: MACRO_UNITS,
  },
  {
    code: "MICRO",
    slug: "microeconomics",
    name: "AP Microeconomics",
    short: "Micro",
    blurb: "How consumers, firms, and markets make decisions under scarcity.",
    gradient: "from-emerald-500 to-teal-600",
    units: MICRO_UNITS,
  },
  {
    code: "CALC_AB",
    slug: "calculus-ab",
    name: "AP Calculus AB",
    short: "Calc AB",
    blurb: "Limits, derivatives, integrals, and the fundamental theorem.",
    gradient: "from-rose-500 to-pink-600",
    units: CALC_UNITS,
  },
  {
    code: "CALC_BC",
    slug: "calculus-bc",
    name: "AP Calculus BC",
    short: "Calc BC",
    blurb: "Everything in AB plus series, parametrics, polars, and vectors.",
    gradient: "from-indigo-500 to-violet-600",
    units: [...CALC_UNITS, ...CALC_BC_ONLY],
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
