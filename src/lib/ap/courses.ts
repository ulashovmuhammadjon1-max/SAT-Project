/**
 * The AP course catalog — static on purpose. Units, topics and exam weights
 * come from the College Board Course and Exam Descriptions and change once a
 * year at most; a database table for four courses would be ceremony. Question
 * CONTENT lives in the ApQuestion table, joined onto this by (subject, topic).
 *
 * A topic listed here only becomes visible once questions exist for it, so the
 * full official outline can sit here while the banks are still being written.
 */

export type ApSubjectCode =
  | "MACRO"
  | "MICRO"
  | "CALC_AB"
  | "CALC_BC"
  | "STATISTICS"
  | "PSYCHOLOGY"
  | "HUMAN_GEO"
  | "US_GOV"
  | "COMP_GOV"
  | "BIOLOGY"
  | "CHEMISTRY"
  | "ENV_SCI";

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


// ---------------------------------------------------------------------------
// AP Statistics — CED effective Fall 2026 (five units). Verified against the
// official CED PDF; see content-pool/ap-banks/AP_STATS_CED.md for the source
// and for how the retired nine-unit framework maps onto these units.
// ---------------------------------------------------------------------------

const STATS_UNITS: ApUnit[] = [
  {
    number: 1,
    title: "Exploring One-Variable Data and Collecting Data",
    blurb: "Describing distributions, summary statistics, and how data are collected.",
    topics: [
      { code: "1.1", title: "Introducing Statistics: What Can We Learn from Data?" },
      { code: "1.2", title: "Variables" },
      { code: "1.3", title: "Tabular Representation and Summary Statistics for One Categorical Variable" },
      { code: "1.4", title: "Graphical Representations for One Categorical Variable" },
      { code: "1.5", title: "Graphical Representations for One Quantitative Variable" },
      { code: "1.6", title: "Descriptions for One Quantitative Variable Distributions" },
      { code: "1.7", title: "Summary Statistics for One Quantitative Variable" },
      { code: "1.8", title: "Graphical Representations of Summary Statistics for One Quantitative Variable" },
      { code: "1.9", title: "Comparisons of the Distributions for One Quantitative Variable" },
      { code: "1.10", title: "The Investigative Question Revisited and Data Collection" },
      { code: "1.11", title: "Random Sampling" },
      { code: "1.12", title: "Potential Problems with Sampling" },
      { code: "1.13", title: "Experimental Design" },
    ],
  },
  {
    number: 2,
    title: "Probability, Random Variables, and Probability Distributions",
    blurb: "Randomness, probability rules, random variables, and probability distributions.",
    topics: [
      { code: "2.1", title: "Tabular and Graphical Representations for the Distributions of Two Categorical Variables" },
      { code: "2.2", title: "Summary Statistics for Two Categorical Variables" },
      { code: "2.3", title: "Estimating Probabilities Using Simulation" },
      { code: "2.4", title: "Introduction to Probability" },
      { code: "2.5", title: "Mutually Exclusive Events" },
      { code: "2.6", title: "Conditional Probability" },
      { code: "2.7", title: "Independent Events and Unions of Events" },
      { code: "2.8", title: "Introduction to Random Variables and Probability Distributions" },
      { code: "2.9", title: "Parameters of Random Variables" },
      { code: "2.10", title: "The Binomial Distribution" },
      { code: "2.11", title: "The Normal Distribution" },
      { code: "2.12", title: "Sampling Distributions and the Central Limit Theorem" },
    ],
  },
  {
    number: 3,
    title: "Inference for Categorical Data: Proportions",
    blurb: "Confidence intervals and significance tests for proportions, including chi-square.",
    topics: [
      { code: "3.1", title: "Estimators" },
      { code: "3.2", title: "Sampling Distributions for Sample Proportions" },
      { code: "3.3", title: "Constructing a Confidence Interval for a Population Proportion" },
      { code: "3.4", title: "Justifying a Claim Based on a Confidence Interval for a Population Proportion" },
      { code: "3.5", title: "Setting Up a Test for a Population Proportion" },
      { code: "3.6", title: "p-Values" },
      { code: "3.7", title: "Carrying Out a Test for a Population Proportion" },
      { code: "3.8", title: "Potential Errors When Performing Tests" },
      { code: "3.9", title: "Sampling Distributions for the Difference Between Sample Proportions" },
      { code: "3.10", title: "Constructing a Confidence Interval for the Difference Between Two Population Proportions" },
      { code: "3.11", title: "Justifying a Claim Based on a Confidence Interval for the Difference Between Two Population Proportions" },
      { code: "3.12", title: "Setting Up a Test for the Difference Between Two Population Proportions" },
      { code: "3.13", title: "Carrying Out a Test for the Difference Between Two Population Proportions" },
      { code: "3.14", title: "Setting Up a Chi-Square Test for Homogeneity or Independence" },
      { code: "3.15", title: "Carrying Out a Chi-Square Test for Homogeneity or Independence" },
    ],
  },
  {
    number: 4,
    title: "Inference for Quantitative Data: Means",
    blurb: "Confidence intervals and significance tests for means, one-sample and two-sample.",
    topics: [
      { code: "4.1", title: "Sampling Distributions for Sample Means" },
      { code: "4.2", title: "Constructing a Confidence Interval for a Population Mean or Population Mean Difference" },
      { code: "4.3", title: "Justifying a Claim Based on a Confidence Interval for a Population Mean or Population Mean Difference" },
      { code: "4.4", title: "Setting Up a Test for a Population Mean or Population Mean Difference" },
      { code: "4.5", title: "Carrying Out a Test for a Population Mean or Population Mean Difference" },
      { code: "4.6", title: "Sampling Distributions for the Difference Between Two Sample Means" },
      { code: "4.7", title: "Constructing a Confidence Interval for the Difference Between Two Population Means" },
      { code: "4.8", title: "Justifying a Claim Based on a Confidence Interval for the Difference Between Two Population Means" },
      { code: "4.9", title: "Setting Up a Test for the Difference Between Two Population Means" },
      { code: "4.10", title: "Carrying Out a Test for the Difference Between Two Population Means" },
    ],
  },
  {
    number: 5,
    title: "Regression Analysis",
    blurb: "Scatterplots, correlation, least-squares regression, and residual analysis.",
    topics: [
      { code: "5.1", title: "Graphical Representations Between Two Quantitative Variables" },
      { code: "5.2", title: "Correlation" },
      { code: "5.3", title: "Linear Regression Models" },
      { code: "5.4", title: "Residuals" },
      { code: "5.5", title: "Least-Squares Regression" },
    ],
  },
];

// ---------------------------------------------------------------------------
// AP Psychology — current CED (five units). Verified against the official CED;
// see content-pool/ap-banks/AP_PSYCH_CED.md. This is the redesigned framework,
// not the retired nine-unit one that most third-party material still describes.
// ---------------------------------------------------------------------------

const PSYCH_UNITS: ApUnit[] = [
  {
    number: 1,
    title: "Biological Bases of Behavior",
    weight: "15-25%",
    blurb: "Genetics, the nervous and endocrine systems, sensation, and consciousness.",
    topics: [
      { code: "1.1", title: "Interaction of Heredity and Environment" },
      { code: "1.2", title: "Overview of the Nervous System" },
      { code: "1.3", title: "The Neuron and Neural Firing" },
      { code: "1.4", title: "The Brain" },
      { code: "1.5", title: "Sleep" },
      { code: "1.6", title: "Sensation" },
    ],
  },
  {
    number: 2,
    title: "Cognition",
    weight: "15-25%",
    blurb: "Perception, memory, thinking, problem solving, and intelligence.",
    topics: [
      { code: "2.1", title: "Perception" },
      { code: "2.2", title: "Thinking, Problem-Solving, Judgments, and Decision-Making" },
      { code: "2.3", title: "Introduction to Memory" },
      { code: "2.4", title: "Encoding Memories" },
      { code: "2.5", title: "Storing Memories" },
      { code: "2.6", title: "Retrieving Memories" },
      { code: "2.7", title: "Forgetting and Other Memory Challenges" },
      { code: "2.8", title: "Intelligence and Achievement" },
    ],
  },
  {
    number: 3,
    title: "Development and Learning",
    weight: "15-25%",
    blurb: "Lifespan development, classical and operant conditioning, and observational learning.",
    topics: [
      { code: "3.1", title: "Themes and Methods in Developmental Psychology" },
      { code: "3.2", title: "Physical Development Across the Lifespan" },
      { code: "3.3", title: "Gender and Sexual Orientation" },
      { code: "3.4", title: "Cognitive Development Across the Lifespan" },
      { code: "3.5", title: "Communication and Language Development" },
      { code: "3.6", title: "Social-Emotional Development Across the Lifespan" },
      { code: "3.7", title: "Classical Conditioning" },
      { code: "3.8", title: "Operant Conditioning" },
      { code: "3.9", title: "Social, Cognitive, and Neurological Factors in Learning" },
    ],
  },
  {
    number: 4,
    title: "Social Psychology and Personality",
    weight: "15-25%",
    blurb: "Attribution, social influence, group behavior, and theories of personality.",
    topics: [
      { code: "4.1", title: "Attribution Theory and Person Perception" },
      { code: "4.2", title: "Attitude Formation and Attitude Change" },
      { code: "4.3", title: "Psychology of Social Situations" },
      { code: "4.4", title: "Psychodynamic and Humanistic Theories of Personality" },
      { code: "4.5", title: "Social-Cognitive and Trait Theories of Personality" },
      { code: "4.6", title: "Motivation" },
      { code: "4.7", title: "Emotion" },
    ],
  },
  {
    number: 5,
    title: "Mental and Physical Health",
    weight: "15-25%",
    blurb: "Psychological disorders, treatment, health psychology, and positive psychology.",
    topics: [
      { code: "5.1", title: "Introduction to Health Psychology" },
      { code: "5.2", title: "Positive Psychology" },
      { code: "5.3", title: "Explaining and Classifying Psychological Disorders" },
      { code: "5.4", title: "Selection of Categories of Psychological Disorders" },
      { code: "5.5", title: "Treatment of Psychological Disorders" },
    ],
  },
];

// ---------------------------------------------------------------------------
// AP Human Geography, US Government, Comparative Government
//
// Generated by content-pool/ap-banks/gen_course_units.py from the
// *_topics.json files, which were read out of the official Course and Exam
// Descriptions. Regenerate rather than hand-editing: scripts/check-ap-coverage.ts
// asserts these codes match the question bank exactly, and that check is only
// meaningful while both sides come from the same source.
// ---------------------------------------------------------------------------

const HUMAN_GEO_UNITS: ApUnit[] = [
  {
    number: 1,
    title: "Thinking Geographically",
    topics: [
      { code: "1.1", title: "Introduction to Maps" },
      { code: "1.2", title: "Geographic Data" },
      { code: "1.3", title: "The Power of Geographic Data" },
      { code: "1.4", title: "Spatial Concepts" },
      { code: "1.5", title: "Human–Environmental Interaction" },
      { code: "1.6", title: "Scales of Analysis" },
      { code: "1.7", title: "Regional Analysis" },
    ],
  },
  {
    number: 2,
    title: "Population and Migration Patterns and Processes",
    topics: [
      { code: "2.1", title: "Population Distribution" },
      { code: "2.2", title: "Consequences of Population Distribution" },
      { code: "2.3", title: "Population Composition" },
      { code: "2.4", title: "Population Dynamics" },
      { code: "2.5", title: "The Demographic Transition Model" },
      { code: "2.6", title: "Malthusian Theory" },
      { code: "2.7", title: "Population Policies" },
      { code: "2.8", title: "Women and Demographic Change" },
      { code: "2.9", title: "Aging Populations" },
      { code: "2.10", title: "Causes of Migration" },
      { code: "2.11", title: "Forced and Voluntary Migration" },
      { code: "2.12", title: "Effects of Migration" },
    ],
  },
  {
    number: 3,
    title: "Cultural Patterns and Processes",
    topics: [
      { code: "3.1", title: "Introduction to Culture" },
      { code: "3.2", title: "Cultural Landscapes" },
      { code: "3.3", title: "Cultural Patterns" },
      { code: "3.4", title: "Types of Diffusion" },
      { code: "3.5", title: "Historical Causes of Diffusion" },
      { code: "3.6", title: "Contemporary Causes of Diffusion" },
      { code: "3.7", title: "Diffusion of Religion and Language" },
      { code: "3.8", title: "Effects of Diffusion" },
    ],
  },
  {
    number: 4,
    title: "Political Patterns and Processes",
    topics: [
      { code: "4.1", title: "Introduction to Political Geography" },
      { code: "4.2", title: "Political Processes" },
      { code: "4.3", title: "Political Power and Territoriality" },
      { code: "4.4", title: "Defining Political Boundaries" },
      { code: "4.5", title: "The Function of Political Boundaries" },
      { code: "4.6", title: "Internal Boundaries" },
      { code: "4.7", title: "Forms of Governance" },
      { code: "4.8", title: "Defining Devolutionary Factors" },
      { code: "4.9", title: "Challenges to Sovereignty" },
      { code: "4.10", title: "Consequences of Centrifugal and Centripetal Forces" },
    ],
  },
  {
    number: 5,
    title: "Agriculture and Rural Land-Use Patterns and Processes",
    topics: [
      { code: "5.1", title: "Introduction to Agriculture" },
      { code: "5.2", title: "Settlement Patterns and Survey Methods" },
      { code: "5.3", title: "Agricultural Origins and Diffusions" },
      { code: "5.4", title: "The Second Agricultural Revolution" },
      { code: "5.5", title: "The Green Revolution" },
      { code: "5.6", title: "Agricultural Production Regions" },
      { code: "5.7", title: "Spatial Organization of Agriculture" },
      { code: "5.8", title: "Von Thünen Model" },
      { code: "5.9", title: "The Global System of Agriculture" },
      { code: "5.10", title: "Consequences of Agricultural Practices" },
      { code: "5.11", title: "Challenges of Contemporary Agriculture" },
      { code: "5.12", title: "Women in Agriculture" },
    ],
  },
  {
    number: 6,
    title: "Cities and Urban Land-Use Patterns and Processes",
    topics: [
      { code: "6.1", title: "The Origin and Influences of Urbanization" },
      { code: "6.2", title: "Cities Across the World" },
      { code: "6.3", title: "Cities and Globalization" },
      { code: "6.4", title: "The Size and Distribution of Cities" },
      { code: "6.5", title: "The Internal Structure of Cities" },
      { code: "6.6", title: "Density and Land Use" },
      { code: "6.7", title: "Infrastructure" },
      { code: "6.8", title: "Urban Sustainability" },
      { code: "6.9", title: "Urban Data" },
      { code: "6.10", title: "Challenges of Urban Changes" },
      { code: "6.11", title: "Challenges of Urban Sustainability" },
    ],
  },
  {
    number: 7,
    title: "Industrial and Economic Development Patterns and Processes",
    topics: [
      { code: "7.1", title: "The Industrial Revolution" },
      { code: "7.2", title: "Economic Sectors and Patterns" },
      { code: "7.3", title: "Measures of Development" },
      { code: "7.4", title: "Women and Economic Development" },
      { code: "7.5", title: "Theories of Development" },
      { code: "7.6", title: "Trade and the World Economy" },
      { code: "7.7", title: "Changes as a Result of the World Economy" },
      { code: "7.8", title: "Sustainable Development" },
    ],
  },
];

const US_GOV_UNITS: ApUnit[] = [
  {
    number: 1,
    title: "Foundations of American Democracy",
    topics: [
      { code: "1.1", title: "Ideals of Democracy" },
      { code: "1.2", title: "Types of Democracy" },
      { code: "1.3", title: "Government Power and Individual Rights" },
      { code: "1.4", title: "Challenges of the Articles of Confederation" },
      { code: "1.5", title: "Ratification of the U.S. Constitution" },
      { code: "1.6", title: "Principles of American Government" },
      { code: "1.7", title: "Relationship Between the States and National Government" },
      { code: "1.8", title: "Constitutional Interpretations of Federalism" },
      { code: "1.9", title: "Federalism in Action" },
    ],
  },
  {
    number: 2,
    title: "Interactions Among Branches of Government",
    topics: [
      { code: "2.1", title: "Congress: The Senate and the House of Representatives" },
      { code: "2.2", title: "Structures, Powers, and Functions of Congress" },
      { code: "2.3", title: "Congressional Behavior" },
      { code: "2.4", title: "Roles and Powers of the President" },
      { code: "2.5", title: "Checks on the Presidency" },
      { code: "2.6", title: "Expansion of Presidential Power" },
      { code: "2.7", title: "Presidential Communication" },
      { code: "2.8", title: "The Judicial Branch" },
      { code: "2.9", title: "The Role of the Judicial Branch" },
      { code: "2.10", title: "The Court in Action" },
      { code: "2.11", title: "Checks on the Judicial Branch" },
      { code: "2.12", title: "The Bureaucracy" },
      { code: "2.13", title: "Discretionary and Rulemaking Authority" },
      { code: "2.14", title: "Holding the Bureaucracy Accountable" },
      { code: "2.15", title: "Policy and the Branches of Government" },
    ],
  },
  {
    number: 3,
    title: "Civil Liberties and Civil Rights",
    topics: [
      { code: "3.1", title: "The Bill of Rights" },
      { code: "3.2", title: "First Amendment: Freedom of Religion" },
      { code: "3.3", title: "First Amendment: Freedom of Speech" },
      { code: "3.4", title: "First Amendment: Freedom of the Press" },
      { code: "3.5", title: "Second Amendment: Right to Bear Arms" },
      { code: "3.6", title: "Amendments: Balancing Individual Freedom with Public Order and Safety" },
      { code: "3.7", title: "Selective Incorporation" },
      { code: "3.8", title: "Amendments: Due Process and the Rights of the Accused" },
      { code: "3.9", title: "Amendments: Due Process and the Right to Privacy" },
      { code: "3.10", title: "Social Movements and Equal Protection" },
      { code: "3.11", title: "Government Responses to Social Movements" },
      { code: "3.12", title: "Balancing Minority and Majority Rights" },
      { code: "3.13", title: "Affirmative Action" },
    ],
  },
  {
    number: 4,
    title: "American Political Ideologies and Beliefs",
    topics: [
      { code: "4.1", title: "American Attitudes About Government and Politics" },
      { code: "4.2", title: "Political Socialization" },
      { code: "4.3", title: "Changes in Ideology" },
      { code: "4.4", title: "Influence of Political Events on Ideology" },
      { code: "4.5", title: "Measuring Public Opinion" },
      { code: "4.6", title: "Evaluating Public Opinion Data" },
      { code: "4.7", title: "Ideologies of Political Parties" },
      { code: "4.8", title: "Ideology and Policymaking" },
      { code: "4.9", title: "Ideology and Economic Policy" },
      { code: "4.10", title: "Ideology and Social Policy" },
    ],
  },
  {
    number: 5,
    title: "Political Participation",
    topics: [
      { code: "5.1", title: "Voting Rights and Models of Voting Behavior" },
      { code: "5.2", title: "Voter Turnout" },
      { code: "5.3", title: "Political Parties" },
      { code: "5.4", title: "How and Why Political Parties Change and Adapt" },
      { code: "5.5", title: "Third-Party Politics" },
      { code: "5.6", title: "Interest Groups Influencing Policymaking" },
      { code: "5.7", title: "Groups Influencing Policy Outcomes" },
      { code: "5.8", title: "Electing a President" },
      { code: "5.9", title: "Congressional Elections" },
      { code: "5.10", title: "Modern Campaigns" },
      { code: "5.11", title: "Campaign Finance" },
      { code: "5.12", title: "The Media" },
      { code: "5.13", title: "Changing Media" },
    ],
  },
];

const COMP_GOV_UNITS: ApUnit[] = [
  {
    number: 1,
    title: "Political Systems, Regimes, and Governments",
    topics: [
      { code: "1.1", title: "The Practice of Political Scientists" },
      { code: "1.2", title: "Defining Political Organizations" },
      { code: "1.3", title: "Democracy vs. Authoritarianism" },
      { code: "1.4", title: "Democratization" },
      { code: "1.5", title: "Sources of Power and Authority" },
      { code: "1.6", title: "Change in Power and Authority" },
      { code: "1.7", title: "Federal and Unitary Systems" },
      { code: "1.8", title: "Political Legitimacy" },
      { code: "1.9", title: "Sustaining Legitimacy" },
      { code: "1.10", title: "Political Stability" },
    ],
  },
  {
    number: 2,
    title: "Political Institutions",
    topics: [
      { code: "2.1", title: "Parliamentary, Presidential, and Semi-Presidential Systems" },
      { code: "2.2", title: "Comparing Parliamentary, Presidential, and Semi-Presidential Systems" },
      { code: "2.3", title: "Executive Systems" },
      { code: "2.4", title: "Executive Term Limits" },
      { code: "2.5", title: "Removal of Executives" },
      { code: "2.6", title: "Legislative Systems" },
      { code: "2.7", title: "Independent Legislatures" },
      { code: "2.8", title: "Judicial Systems" },
      { code: "2.9", title: "Independent Judiciaries" },
    ],
  },
  {
    number: 3,
    title: "Political Culture and Participation",
    topics: [
      { code: "3.1", title: "Civil Society" },
      { code: "3.2", title: "Political Culture" },
      { code: "3.3", title: "Political Ideologies" },
      { code: "3.4", title: "Political Values and Beliefs" },
      { code: "3.5", title: "Nature and Role of Political Participation" },
      { code: "3.6", title: "Forces that Impact Political Participation" },
      { code: "3.7", title: "Civil Rights and Civil Liberties" },
      { code: "3.8", title: "Political and Social Cleavages" },
      { code: "3.9", title: "Challenges from Political and Social Cleavages" },
    ],
  },
  {
    number: 4,
    title: "Party and Electoral Systems and Citizen Organizations",
    topics: [
      { code: "4.1", title: "Electoral Systems and Rules" },
      { code: "4.2", title: "Objectives of Election Rules" },
      { code: "4.3", title: "Political Party Systems" },
      { code: "4.4", title: "Role of Political Party Systems" },
      { code: "4.5", title: "Impact of Social Movements and Interest Groups" },
      { code: "4.6", title: "Pluralist and Corporatist Interests" },
    ],
  },
  {
    number: 5,
    title: "Political and Economic Changes and Development",
    topics: [
      { code: "5.1", title: "Impact of Global Economic and Technological Forces" },
      { code: "5.2", title: "Political Responses to Global Market Forces" },
      { code: "5.3", title: "Challenges from Globalization" },
      { code: "5.4", title: "Policies and Economic Liberalization" },
      { code: "5.5", title: "International and Supranational Organizations" },
      { code: "5.6", title: "Adaptation of Social Policies" },
      { code: "5.7", title: "Impact of Industrialization and Economic Development" },
      { code: "5.8", title: "Causes and Effects of Demographic Change" },
      { code: "5.9", title: "Impact of Natural Resources" },
    ],
  },
];

/** AP Biology, CED effective Fall 2025. Generated by
 *  content-pool/ap-banks/gen_course_units.py from BIOLOGY_topics.json. */
const BIOLOGY_UNITS: ApUnit[] = [
  {
    number: 1,
    title: "Chemistry of Life",
    topics: [
      { code: "1.1", title: "Structure of Water and Hydrogen Bonding" },
      { code: "1.2", title: "Elements of Life" },
      { code: "1.3", title: "Introduction to Macromolecules" },
      { code: "1.4", title: "Carbohydrates" },
      { code: "1.5", title: "Lipids" },
      { code: "1.6", title: "Nucleic Acids" },
      { code: "1.7", title: "Proteins" },
    ],
  },
  {
    number: 2,
    title: "Cells",
    topics: [
      { code: "2.1", title: "Cell Structure and Function" },
      { code: "2.2", title: "Cell Size" },
      { code: "2.3", title: "Plasma Membrane" },
      { code: "2.4", title: "Membrane Permeability" },
      { code: "2.5", title: "Membrane Transport" },
      { code: "2.6", title: "Facilitated Diffusion" },
      { code: "2.7", title: "Tonicity and Osmoregulation" },
      { code: "2.8", title: "Mechanisms of Transport" },
      { code: "2.9", title: "Cell Compartmentalization" },
      { code: "2.10", title: "Origins of Cell Compartmentalization" },
    ],
  },
  {
    number: 3,
    title: "Cellular Energetics",
    topics: [
      { code: "3.1", title: "Enzymes" },
      { code: "3.2", title: "Environmental Impacts on Enzyme Function" },
      { code: "3.3", title: "Cellular Energy" },
      { code: "3.4", title: "Photosynthesis" },
      { code: "3.5", title: "Cellular Respiration" },
    ],
  },
  {
    number: 4,
    title: "Cell Communication and Cell Cycle",
    topics: [
      { code: "4.1", title: "Cell Communication" },
      { code: "4.2", title: "Introduction to Signal Transduction" },
      { code: "4.3", title: "Signal Transduction Pathways" },
      { code: "4.4", title: "Feedback" },
      { code: "4.5", title: "Cell Cycle" },
      { code: "4.6", title: "Regulation of Cell Cycle" },
    ],
  },
  {
    number: 5,
    title: "Heredity",
    topics: [
      { code: "5.1", title: "Meiosis" },
      { code: "5.2", title: "Meiosis and Genetic Diversity" },
      { code: "5.3", title: "Mendelian Genetics" },
      { code: "5.4", title: "Non-Mendelian Genetics" },
      { code: "5.5", title: "Environmental Effects on Phenotype" },
    ],
  },
  {
    number: 6,
    title: "Gene Expression and Regulation",
    topics: [
      { code: "6.1", title: "DNA and RNA Structure" },
      { code: "6.2", title: "DNA Replication" },
      { code: "6.3", title: "Transcription and RNA Processing" },
      { code: "6.4", title: "Translation" },
      { code: "6.5", title: "Regulation of Gene Expression" },
      { code: "6.6", title: "Gene Expression and Cell Specialization" },
      { code: "6.7", title: "Mutations" },
      { code: "6.8", title: "Biotechnology" },
    ],
  },
  {
    number: 7,
    title: "Natural Selection",
    topics: [
      { code: "7.1", title: "Introduction to Natural Selection" },
      { code: "7.2", title: "Natural Selection" },
      { code: "7.3", title: "Artificial Selection" },
      { code: "7.4", title: "Population Genetics" },
      { code: "7.5", title: "Hardy–Weinberg Equilibrium" },
      { code: "7.6", title: "Evidence of Evolution" },
      { code: "7.7", title: "Common Ancestry" },
      { code: "7.8", title: "Continuing Evolution" },
      { code: "7.9", title: "Phylogeny" },
      { code: "7.10", title: "Speciation" },
      { code: "7.11", title: "Variations in Populations" },
      { code: "7.12", title: "Origins of Life on Earth" },
    ],
  },
  {
    number: 8,
    title: "Ecology",
    topics: [
      { code: "8.1", title: "Responses to the Environment" },
      { code: "8.2", title: "Energy Flow Through Ecosystems" },
      { code: "8.3", title: "Population Ecology" },
      { code: "8.4", title: "Effect of Density on Populations" },
      { code: "8.5", title: "Community Ecology" },
      { code: "8.6", title: "Biodiversity" },
      { code: "8.7", title: "Disruptions in Ecosystems" },
    ],
  },
];

/** AP Chemistry, 9 units and 91 topics. Generated by
 *  content-pool/ap-banks/gen_course_units.py from CHEMISTRY_topics.json. */
const CHEMISTRY_UNITS: ApUnit[] = [
  {
    number: 1,
    title: "Atomic Structure and Properties",
    topics: [
      { code: "1.1", title: "Moles and Molar Mass" },
      { code: "1.2", title: "Mass Spectra of Elements" },
      { code: "1.3", title: "Elemental Composition of Pure Substances" },
      { code: "1.4", title: "Composition of Mixtures" },
      { code: "1.5", title: "Atomic Structure and Electron Configuration" },
      { code: "1.6", title: "Photoelectron Spectroscopy" },
      { code: "1.7", title: "Periodic Trends" },
      { code: "1.8", title: "Valence Electrons and Ionic Compounds" },
    ],
  },
  {
    number: 2,
    title: "Compound Structure and Properties",
    topics: [
      { code: "2.1", title: "Types of Chemical Bonds" },
      { code: "2.2", title: "Intramolecular Force and Potential Energy" },
      { code: "2.3", title: "Structure of Ionic Solids" },
      { code: "2.4", title: "Structure of Metals and Alloys" },
      { code: "2.5", title: "Lewis Diagrams" },
      { code: "2.6", title: "Resonance and Formal Charge" },
      { code: "2.7", title: "VSEPR and Hybridization" },
    ],
  },
  {
    number: 3,
    title: "Properties of Substances and Mixtures",
    topics: [
      { code: "3.1", title: "Intermolecular and Interparticle Forces" },
      { code: "3.2", title: "Properties of Solids" },
      { code: "3.3", title: "Solids, Liquids, and Gases" },
      { code: "3.4", title: "Ideal Gas Law" },
      { code: "3.5", title: "Kinetic Molecular Theory" },
      { code: "3.6", title: "Deviation from Ideal Gas Law" },
      { code: "3.7", title: "Solutions and Mixtures" },
      { code: "3.8", title: "Representations of Solutions" },
      { code: "3.9", title: "Separation of Solutions and Mixtures" },
      { code: "3.10", title: "Solubility" },
      { code: "3.11", title: "Spectroscopy and the Electromagnetic Spectrum" },
      { code: "3.12", title: "Properties of Photons" },
      { code: "3.13", title: "Beer-Lambert Law" },
    ],
  },
  {
    number: 4,
    title: "Chemical Reactions",
    topics: [
      { code: "4.1", title: "Introduction for Reactions" },
      { code: "4.2", title: "Net Ionic Equations" },
      { code: "4.3", title: "Representations of Reactions" },
      { code: "4.4", title: "Physical and Chemical Changes" },
      { code: "4.5", title: "Stoichiometry" },
      { code: "4.6", title: "Introduction to Titration" },
      { code: "4.7", title: "Types of Chemical Reactions" },
      { code: "4.8", title: "Introduction to Acid-Base Reactions" },
      { code: "4.9", title: "Oxidation-Reduction (Redox) Reactions" },
    ],
  },
  {
    number: 5,
    title: "Kinetics",
    topics: [
      { code: "5.1", title: "Reaction Rates" },
      { code: "5.2", title: "Introduction to Rate Law" },
      { code: "5.3", title: "Concentration Changes Over Time" },
      { code: "5.4", title: "Elementary Reactions" },
      { code: "5.5", title: "Collision Model" },
      { code: "5.6", title: "Reaction Energy Profile" },
      { code: "5.7", title: "Introduction to Reaction Mechanisms" },
      { code: "5.8", title: "Reaction Mechanism and Rate Law" },
      { code: "5.9", title: "Pre-Equilibrium Approximation" },
      { code: "5.10", title: "Multistep Reaction Energy Profile" },
      { code: "5.11", title: "Catalysis" },
    ],
  },
  {
    number: 6,
    title: "Thermochemistry",
    topics: [
      { code: "6.1", title: "Endothermic and Exothermic Processes" },
      { code: "6.2", title: "Energy Diagrams" },
      { code: "6.3", title: "Heat Transfer and Thermal Equilibrium" },
      { code: "6.4", title: "Heat Capacity and Calorimetry" },
      { code: "6.5", title: "Energy of Phase Changes" },
      { code: "6.6", title: "Introduction to Enthalpy of Reaction" },
      { code: "6.7", title: "Bond Enthalpies" },
      { code: "6.8", title: "Enthalpy of Formation" },
      { code: "6.9", title: "Hess’s Law" },
    ],
  },
  {
    number: 7,
    title: "Principles of Equilibrium",
    topics: [
      { code: "7.1", title: "Introduction to Equilibrium" },
      { code: "7.2", title: "Direction of Reversible Reactions" },
      { code: "7.3", title: "Reaction Quotient and Equilibrium Constant" },
      { code: "7.4", title: "Calculating the Equilibrium Constant" },
      { code: "7.5", title: "Magnitude of the Equilibrium Constant" },
      { code: "7.6", title: "Properties of the Equilibrium Constant" },
      { code: "7.7", title: "Calculating Equilibrium Concentrations" },
      { code: "7.8", title: "Representations of Equilibrium" },
      { code: "7.9", title: "Introduction to Le Châtelier’s Principle" },
      { code: "7.10", title: "Reaction Quotient and Le Châtelier’s Principle" },
      { code: "7.11", title: "Introduction to Solubility Equilibria" },
      { code: "7.12", title: "Common-Ion Effect" },
    ],
  },
  {
    number: 8,
    title: "Acids and Bases",
    topics: [
      { code: "8.1", title: "Introduction to Acids and Bases" },
      { code: "8.2", title: "pH and pOH of Strong Acids and Bases" },
      { code: "8.3", title: "Weak Acid and Base Equilibria" },
      { code: "8.4", title: "Acid-Base Reactions and Buffers" },
      { code: "8.5", title: "Acid-Base Titrations" },
      { code: "8.6", title: "Molecular Structure of Acids and Bases" },
      { code: "8.7", title: "pH and pKa" },
      { code: "8.8", title: "Properties of Buffers" },
      { code: "8.9", title: "Henderson- Hasselbalch Equation" },
      { code: "8.10", title: "Buffer Capacity" },
      { code: "8.11", title: "pH and Solubility" },
    ],
  },
  {
    number: 9,
    title: "Thermodynamics and Electrochemistry",
    topics: [
      { code: "9.1", title: "Introduction to Entropy" },
      { code: "9.2", title: "Absolute Entropy and Entropy Change" },
      { code: "9.3", title: "Gibbs Free Energy and Thermodynamic Favorability" },
      { code: "9.4", title: "Thermodynamic and Kinetic Control" },
      { code: "9.5", title: "Free Energy and Equilibrium" },
      { code: "9.6", title: "Free Energy of Dissolution" },
      { code: "9.7", title: "Coupled Reactions" },
      { code: "9.8", title: "Galvanic (Voltaic) and Electrolytic Cells" },
      { code: "9.9", title: "Cell Potential and Free Energy" },
      { code: "9.10", title: "Cell Potential Under Nonstandard Conditions" },
      { code: "9.11", title: "Electrolysis and Faraday’s Law" },
    ],
  },
];

/** AP Environmental Science, 9 units and 99 topics. Generated by
 *  content-pool/ap-banks/gen_course_units.py from ENV_SCI_topics.json. */
const ENV_SCI_UNITS: ApUnit[] = [
  {
    number: 1,
    title: "The Living World: Ecosystems",
    topics: [
      { code: "1.1", title: "Introduction to Ecosystems" },
      { code: "1.2", title: "Terrestrial Biomes" },
      { code: "1.3", title: "Aquatic Biomes" },
      { code: "1.4", title: "The Carbon Cycle" },
      { code: "1.5", title: "The Nitrogen Cycle" },
      { code: "1.6", title: "The Phosphorus Cycle" },
      { code: "1.7", title: "The Hydrologic (Water) Cycle" },
      { code: "1.8", title: "Primary Productivity" },
      { code: "1.9", title: "Trophic Levels" },
      { code: "1.10", title: "Energy Flow and the 10% Rule" },
      { code: "1.11", title: "Food Chains and Food Webs" },
    ],
  },
  {
    number: 2,
    title: "The Living World: Biodiversity",
    topics: [
      { code: "2.1", title: "Introduction to Biodiversity" },
      { code: "2.2", title: "Ecosystem Services" },
      { code: "2.3", title: "Island Biogeography" },
      { code: "2.4", title: "Ecological Tolerance" },
      { code: "2.5", title: "Natural Disruptions to Ecosystems" },
      { code: "2.6", title: "Adaptations" },
      { code: "2.7", title: "Ecological Succession" },
    ],
  },
  {
    number: 3,
    title: "Populations",
    topics: [
      { code: "3.1", title: "Generalist and Specialist Species" },
      { code: "3.2", title: "K-Selected r-Selected Species" },
      { code: "3.3", title: "Survivorship Curves" },
      { code: "3.4", title: "Carrying Capacity" },
      { code: "3.5", title: "Population Growth and Resource Availability" },
      { code: "3.6", title: "Age Structure Diagrams" },
      { code: "3.7", title: "Total Fertility Rate" },
      { code: "3.8", title: "Human Population Dynamics" },
      { code: "3.9", title: "Demographic Transition" },
    ],
  },
  {
    number: 4,
    title: "Earth Systems and Resources",
    topics: [
      { code: "4.1", title: "Plate Tectonics" },
      { code: "4.2", title: "Soil Formation and Erosion" },
      { code: "4.3", title: "Soil Composition and Properties" },
      { code: "4.4", title: "Earth’s Atmosphere" },
      { code: "4.5", title: "Global Wind Patterns" },
      { code: "4.6", title: "Watersheds" },
      { code: "4.7", title: "Solar Radiation and Earth’s Seasons" },
      { code: "4.8", title: "Earth’s Geography and Climate" },
      { code: "4.9", title: "El Niño and La Niña" },
    ],
  },
  {
    number: 5,
    title: "Land and Water Use",
    topics: [
      { code: "5.1", title: "The Tragedy of the Commons" },
      { code: "5.2", title: "Clearcutting" },
      { code: "5.3", title: "The Green Revolution" },
      { code: "5.4", title: "Impacts of Agricultural Practices" },
      { code: "5.5", title: "Irrigation Methods" },
      { code: "5.6", title: "Pest Control Methods" },
      { code: "5.7", title: "Meat Production Methods" },
      { code: "5.8", title: "Impacts of Overfishing" },
      { code: "5.9", title: "Impacts of Mining" },
      { code: "5.10", title: "Impacts of Urbanization" },
      { code: "5.11", title: "Ecological Footprints" },
      { code: "5.12", title: "Introduction to Sustainability" },
      { code: "5.13", title: "Methods to Reduce Urban Runoff" },
      { code: "5.14", title: "Integrated Pest Management" },
      { code: "5.15", title: "Sustainable Agriculture" },
      { code: "5.16", title: "Aquaculture" },
      { code: "5.17", title: "Sustainable Forestry" },
    ],
  },
  {
    number: 6,
    title: "Energy Resources and Consumption",
    topics: [
      { code: "6.1", title: "Renewable and Nonrenewable Resources" },
      { code: "6.2", title: "Global Energy Consumption" },
      { code: "6.3", title: "Fuel Types and Uses" },
      { code: "6.4", title: "Distribution of Natural Energy Resources" },
      { code: "6.5", title: "Fossil Fuels" },
      { code: "6.6", title: "Nuclear Power" },
      { code: "6.7", title: "Energy from Biomass" },
      { code: "6.8", title: "Solar Energy" },
      { code: "6.9", title: "Hydroelectric Power" },
      { code: "6.10", title: "Geothermal Energy" },
      { code: "6.11", title: "Hydrogen Fuel Cell" },
      { code: "6.12", title: "Wind Energy" },
      { code: "6.13", title: "Energy Conservation" },
    ],
  },
  {
    number: 7,
    title: "Atmospheric Pollution",
    topics: [
      { code: "7.1", title: "I ntroduction to Air Pollution" },
      { code: "7.2", title: "Photochemical Smog" },
      { code: "7.3", title: "Thermal Inversion" },
      { code: "7.4", title: "Atmospheric Particulates" },
      { code: "7.5", title: "Indoor Air Pollutants" },
      { code: "7.6", title: "Reduction of Air Pollutants" },
      { code: "7.7", title: "Acid Rain" },
      { code: "7.8", title: "Noise Pollution" },
    ],
  },
  {
    number: 8,
    title: "Aquatic and Terrestrial Pollution",
    topics: [
      { code: "8.1", title: "Sources of Pollution" },
      { code: "8.2", title: "Human Impacts on Ecosystems" },
      { code: "8.3", title: "Endocrine Disruptors" },
      { code: "8.4", title: "Human Impacts on Wetlands and Mangroves" },
      { code: "8.5", title: "Eutrophication" },
      { code: "8.6", title: "Thermal Pollution" },
      { code: "8.7", title: "Persistent Organic Pollutants (POPs)" },
      { code: "8.8", title: "Bioaccumulation and Biomagnification" },
      { code: "8.9", title: "Solid Waste Disposal" },
      { code: "8.10", title: "Waste Reduction Methods" },
      { code: "8.11", title: "Sewage Treatment" },
      { code: "8.12", title: "Lethal Dose 50% (LD50)" },
      { code: "8.13", title: "Dose Response Curve" },
      { code: "8.14", title: "Pollution and Human Health" },
      { code: "8.15", title: "Pathogens and Infectious Diseases" },
    ],
  },
  {
    number: 9,
    title: "Global Change",
    topics: [
      { code: "9.1", title: "Stratospheric Ozone Depletion" },
      { code: "9.2", title: "Reducing Ozone Depletion" },
      { code: "9.3", title: "The Greenhouse Effect" },
      { code: "9.4", title: "Increases in the Greenhouse Gases" },
      { code: "9.5", title: "Global Climate Change" },
      { code: "9.6", title: "Ocean Warming" },
      { code: "9.7", title: "Ocean Acidification" },
      { code: "9.8", title: "Invasive Species" },
      { code: "9.9", title: "Endangered Species" },
      { code: "9.10", title: "Human Impacts on Biodiversity" },
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
    code: "STATISTICS",
    slug: "statistics",
    name: "AP Statistics",
    short: "Statistics",
    blurb: "Exploring data, designing studies, probability, and statistical inference.",
    gradient: "from-sky-500 to-cyan-600",
    units: STATS_UNITS,
  },
  {
    code: "PSYCHOLOGY",
    slug: "psychology",
    name: "AP Psychology",
    short: "Psychology",
    blurb: "The scientific study of behavior and mental processes.",
    gradient: "from-fuchsia-500 to-purple-600",
    units: PSYCH_UNITS,
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
  {
    code: "HUMAN_GEO",
    slug: "human-geography",
    name: "AP Human Geography",
    short: "Human Geography",
    blurb: "Population, migration, culture, political geography, agriculture, cities, and development.",
    gradient: "from-emerald-500 to-teal-600",
    units: HUMAN_GEO_UNITS,
  },
  {
    code: "US_GOV",
    slug: "united-states-government-and-politics",
    name: "AP United States Government and Politics",
    short: "US Gov",
    blurb: "Constitutional foundations, the branches, civil liberties and rights, political behavior, and institutions.",
    gradient: "from-sky-500 to-indigo-600",
    units: US_GOV_UNITS,
  },
  {
    code: "COMP_GOV",
    slug: "comparative-government-and-politics",
    name: "AP Comparative Government and Politics",
    short: "Comparative Gov",
    blurb: "Six course countries compared across political systems, institutions, participation, and policy.",
    gradient: "from-rose-500 to-purple-600",
    units: COMP_GOV_UNITS,
  },
  {
    code: "BIOLOGY",
    slug: "biology",
    name: "AP Biology",
    short: "Biology",
    blurb: "Evolution, energetics, information storage, and systems interactions.",
    gradient: "from-lime-500 to-green-600",
    units: BIOLOGY_UNITS,
  },
  {
    code: "CHEMISTRY",
    slug: "chemistry",
    name: "AP Chemistry",
    short: "Chemistry",
    blurb: "Atomic structure, bonding, reactions, kinetics, thermodynamics, and equilibrium.",
    gradient: "from-orange-500 to-amber-600",
    units: CHEMISTRY_UNITS,
  },
  {
    code: "ENV_SCI",
    slug: "environmental-science",
    name: "AP Environmental Science",
    short: "Environmental Sci",
    blurb: "Ecosystems, biodiversity, populations, land and water use, energy, pollution, and global change.",
    gradient: "from-teal-500 to-emerald-600",
    units: ENV_SCI_UNITS,
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
