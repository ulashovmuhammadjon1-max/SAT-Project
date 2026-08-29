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
  topics?: ApTopic[];
}

export interface ApTopic {
  code: string;
  title: string;
  /**
   * Calculus only. Units 1-8 are shared by AB and BC, but a handful of topics
   * inside them (integration by parts, Euler's method, arc length, ...) are
   * examined on BC alone. Flagging the topic rather than splitting the unit
   * keeps one outline as the single source of truth for both courses.
   */
  bcOnly?: boolean;
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
  {
    number: 1,
    title: "Limits and Continuity",
    weight: "10-12% (AB) / 4-7% (BC)",
    blurb: "Limits, asymptotes, continuity, and the squeeze theorem.",
    topics: [
      { code: "1.1", title: "Introducing Calculus: Can Change Occur at an Instant?" },
      { code: "1.2", title: "Defining Limits and Using Limit Notation" },
      { code: "1.3", title: "Estimating Limit Values from Graphs" },
      { code: "1.4", title: "Estimating Limit Values from Tables" },
      { code: "1.5", title: "Determining Limits Using Algebraic Properties of Limits" },
      { code: "1.6", title: "Determining Limits Using Algebraic Manipulation" },
      { code: "1.7", title: "Selecting Procedures for Determining Limits" },
      { code: "1.8", title: "Determining Limits Using the Squeeze Theorem" },
      { code: "1.9", title: "Connecting Multiple Representations of Limits" },
      { code: "1.10", title: "Exploring Types of Discontinuities" },
      { code: "1.11", title: "Defining Continuity at a Point" },
      { code: "1.12", title: "Confirming Continuity over an Interval" },
      { code: "1.13", title: "Removing Discontinuities" },
      { code: "1.14", title: "Connecting Infinite Limits and Vertical Asymptotes" },
      { code: "1.15", title: "Connecting Limits at Infinity and Horizontal Asymptotes" },
      { code: "1.16", title: "Working with the Intermediate Value Theorem" },
    ],
  },
  {
    number: 2,
    title: "Differentiation: Definition and Fundamental Properties",
    weight: "10-12% (AB) / 4-7% (BC)",
    blurb: "The derivative, and the power, product, and quotient rules.",
    topics: [
      { code: "2.1", title: "Defining Average and Instantaneous Rates of Change at a Point" },
      { code: "2.2", title: "Defining the Derivative of a Function and Using Derivative Notation" },
      { code: "2.3", title: "Estimating Derivatives of a Function at a Point" },
      { code: "2.4", title: "Connecting Differentiability and Continuity" },
      { code: "2.5", title: "Applying the Power Rule" },
      { code: "2.6", title: "Derivative Rules: Constant, Sum, Difference, and Constant Multiple" },
      { code: "2.7", title: "Derivatives of cos x, sin x, e^x, and ln x" },
      { code: "2.8", title: "The Product Rule" },
      { code: "2.9", title: "The Quotient Rule" },
      { code: "2.10", title: "Finding the Derivatives of Tangent, Cotangent, Secant, and Cosecant" },
    ],
  },
  {
    number: 3,
    title: "Differentiation: Composite, Implicit, and Inverse Functions",
    weight: "9-13% (AB) / 4-7% (BC)",
    blurb: "The chain rule, implicit differentiation, and inverses.",
    topics: [
      { code: "3.1", title: "The Chain Rule" },
      { code: "3.2", title: "Implicit Differentiation" },
      { code: "3.3", title: "Differentiating Inverse Functions" },
      { code: "3.4", title: "Differentiating Inverse Trigonometric Functions" },
      { code: "3.5", title: "Selecting Procedures for Calculating Derivatives" },
      { code: "3.6", title: "Calculating Higher-Order Derivatives" },
    ],
  },
  {
    number: 4,
    title: "Contextual Applications of Differentiation",
    weight: "10-15% (AB) / 6-9% (BC)",
    blurb: "Rates of change, related rates, linearization, L'Hospital's rule.",
    topics: [
      { code: "4.1", title: "Interpreting the Meaning of the Derivative in Context" },
      { code: "4.2", title: "Straight-Line Motion: Connecting Position, Velocity, and Acceleration" },
      { code: "4.3", title: "Rates of Change in Applied Contexts Other Than Motion" },
      { code: "4.4", title: "Introduction to Related Rates" },
      { code: "4.5", title: "Solving Related Rates Problems" },
      { code: "4.6", title: "Approximating Values of a Function Using Local Linearity and Linearization" },
      { code: "4.7", title: "Using L'Hospital's Rule for Determining Limits of Indeterminate Forms" },
    ],
  },
  {
    number: 5,
    title: "Analytical Applications of Differentiation",
    weight: "15-18% (AB) / 8-11% (BC)",
    blurb: "Extrema, concavity, curve sketching, and optimization.",
    topics: [
      { code: "5.1", title: "Using the Mean Value Theorem" },
      { code: "5.2", title: "Extreme Value Theorem, Global Versus Local Extrema, and Critical Points" },
      { code: "5.3", title: "Determining Intervals on Which a Function Is Increasing or Decreasing" },
      { code: "5.4", title: "Using the First Derivative Test to Determine Relative Extrema" },
      { code: "5.5", title: "Using the Candidates Test to Determine Absolute Extrema" },
      { code: "5.6", title: "Determining Concavity of Functions over Their Domains" },
      { code: "5.7", title: "Using the Second Derivative Test to Determine Extrema" },
      { code: "5.8", title: "Sketching Graphs of Functions and Their Derivatives" },
      { code: "5.9", title: "Connecting a Function, Its First Derivative, and Its Second Derivative" },
      { code: "5.10", title: "Introduction to Optimization Problems" },
      { code: "5.11", title: "Solving Optimization Problems" },
      { code: "5.12", title: "Exploring Behaviors of Implicit Relations" },
    ],
  },
  {
    number: 6,
    title: "Integration and Accumulation of Change",
    weight: "17-20% (AB) / 17-20% (BC)",
    blurb: "Riemann sums, antiderivatives, and the fundamental theorem.",
    topics: [
      { code: "6.1", title: "Exploring Accumulations of Change" },
      { code: "6.2", title: "Approximating Areas with Riemann Sums" },
      { code: "6.3", title: "Riemann Sums, Summation Notation, and Definite Integral Notation" },
      { code: "6.4", title: "The Fundamental Theorem of Calculus and Accumulation Functions" },
      { code: "6.5", title: "Interpreting the Behavior of Accumulation Functions Involving Area" },
      { code: "6.6", title: "Applying Properties of Definite Integrals" },
      { code: "6.7", title: "The Fundamental Theorem of Calculus and Definite Integrals" },
      { code: "6.8", title: "Finding Antiderivatives and Indefinite Integrals: Basic Rules and Notation" },
      { code: "6.9", title: "Integrating Using Substitution" },
      { code: "6.10", title: "Integrating Functions Using Long Division and Completing the Square" },
      { code: "6.11", title: "Integrating Using Integration by Parts", bcOnly: true },
      { code: "6.12", title: "Integrating Using Linear Partial Fractions", bcOnly: true },
      { code: "6.13", title: "Evaluating Improper Integrals", bcOnly: true },
      { code: "6.14", title: "Selecting Techniques for Antidifferentiation" },
    ],
  },
  {
    number: 7,
    title: "Differential Equations",
    weight: "6-12% (AB) / 6-9% (BC)",
    blurb: "Slope fields, separation of variables, exponential models.",
    topics: [
      { code: "7.1", title: "Modeling Situations with Differential Equations" },
      { code: "7.2", title: "Verifying Solutions for Differential Equations" },
      { code: "7.3", title: "Sketching Slope Fields" },
      { code: "7.4", title: "Reasoning Using Slope Fields" },
      { code: "7.5", title: "Approximating Solutions Using Euler's Method", bcOnly: true },
      { code: "7.6", title: "Finding General Solutions Using Separation of Variables" },
      { code: "7.7", title: "Finding Particular Solutions Using Initial Conditions and Separation of Variables" },
      { code: "7.8", title: "Exponential Models with Differential Equations" },
      { code: "7.9", title: "Logistic Models with Differential Equations", bcOnly: true },
    ],
  },
  {
    number: 8,
    title: "Applications of Integration",
    weight: "10-15% (AB) / 6-9% (BC)",
    blurb: "Average value, area between curves, volume, and arc length.",
    topics: [
      { code: "8.1", title: "Finding the Average Value of a Function on an Interval" },
      { code: "8.2", title: "Connecting Position, Velocity, and Acceleration Using Integrals" },
      { code: "8.3", title: "Using Accumulation Functions and Definite Integrals in Applied Contexts" },
      { code: "8.4", title: "Finding the Area Between Curves Expressed as Functions of x" },
      { code: "8.5", title: "Finding the Area Between Curves Expressed as Functions of y" },
      { code: "8.6", title: "Finding the Area Between Curves That Intersect at More Than Two Points" },
      { code: "8.7", title: "Volumes with Cross Sections: Squares and Rectangles" },
      { code: "8.8", title: "Volumes with Cross Sections: Triangles and Semicircles" },
      { code: "8.9", title: "Volume with Disc Method: Revolving Around the x- or y-Axis" },
      { code: "8.10", title: "Volume with Disc Method: Revolving Around Other Axes" },
      { code: "8.11", title: "Volume with Washer Method: Revolving Around the x- or y-Axis" },
      { code: "8.12", title: "Volume with Washer Method: Revolving Around Other Axes" },
      { code: "8.13", title: "The Arc Length of a Smooth, Planar Curve and Distance Traveled", bcOnly: true },
    ],
  },
];

const CALC_BC_ONLY: ApUnit[] = [
  {
    number: 9,
    title: "Parametric Equations, Polar Coordinates, and Vector-Valued Functions",
    weight: "11-12% (BC)",
    blurb: "BC only - calculus beyond y = f(x).",
    topics: [
      { code: "9.1", title: "Defining and Differentiating Parametric Equations" },
      { code: "9.2", title: "Second Derivatives of Parametric Equations" },
      { code: "9.3", title: "Finding Arc Lengths of Curves Given by Parametric Equations" },
      { code: "9.4", title: "Defining and Differentiating Vector-Valued Functions" },
      { code: "9.5", title: "Integrating Vector-Valued Functions" },
      { code: "9.6", title: "Solving Motion Problems Using Parametric and Vector-Valued Functions" },
      { code: "9.7", title: "Defining Polar Coordinates and Differentiating in Polar Form" },
      { code: "9.8", title: "Finding the Area of a Region Bounded by a Single Polar Curve" },
      { code: "9.9", title: "Finding the Area of the Region Bounded by Two Polar Curves" },
    ],
  },
  {
    number: 10,
    title: "Infinite Sequences and Series",
    weight: "17-18% (BC)",
    blurb: "BC only - convergence tests, Taylor and Maclaurin series.",
    topics: [
      { code: "10.1", title: "Defining Convergent and Divergent Infinite Series" },
      { code: "10.2", title: "Working with Geometric Series" },
      { code: "10.3", title: "The nth Term Test for Divergence" },
      { code: "10.4", title: "Integral Test for Convergence" },
      { code: "10.5", title: "Harmonic Series and p-Series" },
      { code: "10.6", title: "Comparison Tests for Convergence" },
      { code: "10.7", title: "Alternating Series Test for Convergence" },
      { code: "10.8", title: "Ratio Test for Convergence" },
      { code: "10.9", title: "Determining Absolute or Conditional Convergence" },
      { code: "10.10", title: "Alternating Series Error Bound" },
      { code: "10.11", title: "Finding Taylor Polynomial Approximations of Functions" },
      { code: "10.12", title: "Lagrange Error Bound" },
      { code: "10.13", title: "Radius and Interval of Convergence of Power Series" },
      { code: "10.14", title: "Finding Taylor or Maclaurin Series for a Function" },
      { code: "10.15", title: "Representing Functions as Power Series" },
    ],
  },
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
    units: CALC_UNITS.map((u) => ({
      ...u,
      topics: u.topics?.filter((t) => !t.bcOnly),
    })),
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
