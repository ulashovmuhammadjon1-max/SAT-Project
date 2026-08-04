export const CONFIDENCE_PUBLISH_THRESHOLD = 0.75;

export const DOMAIN_TAXONOMY: {
  subject: "READING_WRITING" | "MATH";
  code: string;
  name: string;
  skills: { code: string; name: string }[];
}[] = [
  {
    subject: "READING_WRITING",
    code: "INI",
    name: "Information and Ideas",
    skills: [
      { code: "INI-CI", name: "Central Ideas and Details" },
      { code: "INI-IE", name: "Inferences" },
      { code: "INI-CE", name: "Command of Evidence" },
    ],
  },
  {
    subject: "READING_WRITING",
    code: "CAS",
    name: "Craft and Structure",
    skills: [
      { code: "CAS-WV", name: "Words in Context" },
      { code: "CAS-TS", name: "Text Structure and Purpose" },
      { code: "CAS-CT", name: "Cross-Text Connections" },
    ],
  },
  {
    subject: "READING_WRITING",
    code: "EOI",
    name: "Expression of Ideas",
    skills: [
      { code: "EOI-RS", name: "Rhetorical Synthesis" },
      { code: "EOI-TR", name: "Transitions" },
    ],
  },
  {
    subject: "READING_WRITING",
    code: "SEC",
    name: "Standard English Conventions",
    skills: [
      { code: "SEC-BS", name: "Boundaries" },
      { code: "SEC-FS", name: "Form, Structure, and Sense" },
    ],
  },
  {
    subject: "MATH",
    code: "ALG",
    name: "Algebra",
    skills: [
      { code: "ALG-LE", name: "Linear Equations and Systems" },
      { code: "ALG-LF", name: "Linear Functions" },
      { code: "ALG-LI", name: "Linear Inequalities" },
    ],
  },
  {
    subject: "MATH",
    code: "ADV",
    name: "Advanced Math",
    skills: [
      { code: "ADV-NF", name: "Nonlinear Functions" },
      { code: "ADV-EQ", name: "Equivalent Expressions" },
      { code: "ADV-NE", name: "Nonlinear Equations and Systems" },
    ],
  },
  {
    subject: "MATH",
    code: "PSDA",
    name: "Problem-Solving and Data Analysis",
    skills: [
      { code: "PSDA-RP", name: "Ratios, Rates, and Proportions" },
      { code: "PSDA-ST", name: "Statistics and Probability" },
      { code: "PSDA-DI", name: "Data Interpretation" },
    ],
  },
  {
    subject: "MATH",
    code: "GT",
    name: "Geometry and Trigonometry",
    skills: [
      { code: "GT-AV", name: "Area and Volume" },
      { code: "GT-LA", name: "Lines, Angles, and Triangles" },
      { code: "GT-TR", name: "Trigonometry" },
    ],
  },
];
