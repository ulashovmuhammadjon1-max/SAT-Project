/**
 * The AP subject catalog — every subject Scholarly lists, whether or not its
 * questions are written yet.
 *
 * This file is the single source of truth the AP UI renders from. Adding a
 * subject means adding an entry here (and its content), not editing the hub,
 * the sidebar, the practice-test picker and the subject page one by one. That
 * matters because the catalog is expected to grow to thirty-odd subjects.
 *
 * Course outlines for the subjects that HAVE content live in ./courses.ts and
 * are joined on here by code, so the two never disagree about a unit list.
 */

import { AP_COURSES, type ApCourse, type ApSubjectCode } from "./courses";

export type ApCategory = "STEM" | "SOCIAL" | "HISTORY" | "ENGLISH" | "ARTS";

export const AP_CATEGORIES: { id: ApCategory; label: string; blurb: string }[] = [
  { id: "STEM", label: "Math & Science", blurb: "Calculus, statistics, and the lab sciences." },
  { id: "SOCIAL", label: "Social Sciences", blurb: "How people, markets, and governments behave." },
  { id: "HISTORY", label: "History", blurb: "Long-run change across regions and periods." },
  { id: "ENGLISH", label: "English", blurb: "Argument, rhetoric, and literary analysis." },
  { id: "ARTS", label: "Arts & Research", blurb: "Art history and the Capstone courses." },
];

/** LIVE means questions exist and the subject can be practised today. */
export type ApStatus = "LIVE" | "COMING_SOON";

export interface ApCatalogEntry {
  /** Matches ApQuestion.subject and ApSubjectEnrollment.subject. */
  code: string;
  slug: string;
  /** The College Board's official course title. */
  name: string;
  /** For chips and the sidebar, where the full name does not fit. */
  short: string;
  category: ApCategory;
  status: ApStatus;
  /** What the course actually covers — never a generic placeholder. */
  blurb: string;
  /** Tailwind gradient for the subject card. */
  gradient: string;
}

/**
 * Subjects with content. Their outlines come from AP_COURSES, so a unit list
 * cannot drift between the catalog and the course page.
 */
const LIVE: Omit<ApCatalogEntry, "status">[] = [
  {
    code: "MACRO",
    slug: "macroeconomics",
    name: "AP Macroeconomics",
    short: "Macro",
    category: "SOCIAL",
    gradient: "from-amber-500 to-orange-600",
    blurb:
      "The economy as a whole: output and growth, unemployment and inflation, and how fiscal and monetary policy move them.",
  },
  {
    code: "MICRO",
    slug: "microeconomics",
    name: "AP Microeconomics",
    short: "Micro",
    category: "SOCIAL",
    gradient: "from-emerald-500 to-teal-600",
    blurb:
      "How consumers and firms decide under scarcity, how markets set prices, and where markets fail.",
  },
  {
    code: "CALC_AB",
    slug: "calculus-ab",
    name: "AP Calculus AB",
    short: "Calc AB",
    category: "STEM",
    gradient: "from-rose-500 to-pink-600",
    blurb:
      "Limits, derivatives, integrals, and the Fundamental Theorem — a first course in single-variable calculus.",
  },
  {
    code: "CALC_BC",
    slug: "calculus-bc",
    name: "AP Calculus BC",
    short: "Calc BC",
    category: "STEM",
    gradient: "from-indigo-500 to-violet-600",
    blurb:
      "Everything in AB, plus parametric and polar calculus, vector-valued functions, and infinite series.",
  },
  {
    code: "STATISTICS",
    slug: "statistics",
    name: "AP Statistics",
    short: "Statistics",
    category: "STEM",
    gradient: "from-sky-500 to-cyan-600",
    blurb:
      "Exploring data, designing studies, probability and random variables, and drawing inferences with confidence intervals and significance tests.",
  },
  {
    code: "PSYCHOLOGY",
    slug: "psychology",
    name: "AP Psychology",
    short: "Psychology",
    category: "SOCIAL",
    gradient: "from-fuchsia-500 to-purple-600",
    blurb:
      "The scientific study of behavior and mental processes: biological bases, cognition, development and learning, social psychology and personality, and mental and physical health.",
  },
  {
    code: "HUMAN_GEO",
    slug: "human-geography",
    name: "AP Human Geography",
    short: "Human Geography",
    category: "SOCIAL",
    gradient: "from-lime-500 to-green-600",
    blurb:
      "Population, migration, culture, political geography, agriculture, cities, and development.",
  },
  {
    code: "US_GOV",
    slug: "united-states-government-and-politics",
    name: "AP United States Government and Politics",
    short: "US Gov",
    category: "SOCIAL",
    gradient: "from-blue-500 to-indigo-600",
    blurb:
      "Constitutional foundations, the branches, civil liberties and rights, political behavior, and institutions.",
  },
  {
    code: "COMP_GOV",
    slug: "comparative-government-and-politics",
    name: "AP Comparative Government and Politics",
    short: "Comparative Gov",
    category: "SOCIAL",
    gradient: "from-red-500 to-rose-600",
    blurb:
      "Six course countries compared across political systems, institutions, participation, and policy.",
  },
  {
    code: "BIOLOGY",
    slug: "biology",
    name: "AP Biology",
    short: "Biology",
    category: "STEM",
    gradient: "from-green-500 to-emerald-600",
    blurb:
      "Evolution, energetics, information storage, and systems interactions.",
  },
];

/**
 * Announced but not yet written. These render as Coming soon and cannot be
 * added or entered — a student must never land in an empty course.
 */
const PLANNED: Omit<ApCatalogEntry, "status" | "gradient">[] = [
  { code: "CHEMISTRY", slug: "chemistry", name: "AP Chemistry", short: "Chemistry", category: "STEM", blurb: "Atomic structure, bonding, reactions, kinetics, thermodynamics, and equilibrium." },
  { code: "PHYSICS_1", slug: "physics-1", name: "AP Physics 1: Algebra-Based", short: "Physics 1", category: "STEM", blurb: "Kinematics, forces, energy, momentum, rotation, and simple harmonic motion." },
  { code: "PHYSICS_2", slug: "physics-2", name: "AP Physics 2: Algebra-Based", short: "Physics 2", category: "STEM", blurb: "Fluids, thermodynamics, electromagnetism, optics, and modern physics." },
  { code: "PHYSICS_C_MECH", slug: "physics-c-mechanics", name: "AP Physics C: Mechanics", short: "Physics C: Mech", category: "STEM", blurb: "Calculus-based mechanics: kinematics, Newton's laws, work and energy, momentum, rotation, oscillations, and gravitation." },
  { code: "PHYSICS_C_EM", slug: "physics-c-electricity-and-magnetism", name: "AP Physics C: Electricity and Magnetism", short: "Physics C: E&M", category: "STEM", blurb: "Calculus-based electrostatics, conductors and capacitors, circuits, magnetic fields, and electromagnetism." },
  { code: "CSA", slug: "computer-science-a", name: "AP Computer Science A", short: "CS A", category: "STEM", blurb: "Object-oriented programming in Java: classes, arrays and lists, inheritance, and recursion." },
  { code: "CSP", slug: "computer-science-principles", name: "AP Computer Science Principles", short: "CS Principles", category: "STEM", blurb: "Computational thinking, data, algorithms, programming, and the impact of computing." },
  { code: "ENV_SCI", slug: "environmental-science", name: "AP Environmental Science", short: "Environmental Sci", category: "STEM", blurb: "Ecosystems, biodiversity, populations, land and water use, energy, pollution, and global change." },
  { code: "WORLD_HISTORY", slug: "world-history-modern", name: "AP World History: Modern", short: "World History", category: "HISTORY", blurb: "Global processes from about 1200 CE to the present." },
  { code: "US_HISTORY", slug: "united-states-history", name: "AP United States History", short: "US History", category: "HISTORY", blurb: "American history from about 1491 to the present, across nine periods." },
  { code: "EURO_HISTORY", slug: "european-history", name: "AP European History", short: "European History", category: "HISTORY", blurb: "European history from about 1450 to the present." },
  { code: "ENG_LANG", slug: "english-language-and-composition", name: "AP English Language and Composition", short: "English Lang", category: "ENGLISH", blurb: "Rhetorical analysis, argument, and synthesis in non-fiction prose." },
  { code: "ENG_LIT", slug: "english-literature-and-composition", name: "AP English Literature and Composition", short: "English Lit", category: "ENGLISH", blurb: "Close reading and analysis of poetry, prose fiction, and drama." },
  { code: "ART_HISTORY", slug: "art-history", name: "AP Art History", short: "Art History", category: "ARTS", blurb: "250 works across global artistic traditions, from prehistory to the present." },
  { code: "SEMINAR", slug: "seminar", name: "AP Seminar", short: "Seminar", category: "ARTS", blurb: "Capstone course in research, argument, collaboration, and presentation." },
  { code: "RESEARCH", slug: "research", name: "AP Research", short: "Research", category: "ARTS", blurb: "Capstone course: an independent, year-long research investigation and academic paper." },
];

export const AP_CATALOG: ApCatalogEntry[] = [
  ...LIVE.map((s) => ({ ...s, status: "LIVE" as const })),
  ...PLANNED.map((s) => ({
    ...s,
    status: "COMING_SOON" as const,
    // Planned subjects share one muted treatment, so colour reads as "ready".
    gradient: "from-slate-400 to-slate-500",
  })),
];

const BY_CODE = new Map(AP_CATALOG.map((s) => [s.code, s]));
const BY_SLUG = new Map(AP_CATALOG.map((s) => [s.slug, s]));

export function subjectByCode(code: string): ApCatalogEntry | undefined {
  return BY_CODE.get(code);
}

export function subjectBySlug(slug: string): ApCatalogEntry | undefined {
  return BY_SLUG.get(slug);
}

export function isLiveSubject(code: string): boolean {
  return BY_CODE.get(code)?.status === "LIVE";
}

/** The course outline for a subject, when it has one. */
export function courseForSubject(code: string): ApCourse | undefined {
  return AP_COURSES.find((c) => c.code === (code as ApSubjectCode));
}

/** Catalog entries grouped for display, skipping categories with no subjects. */
export function catalogByCategory(): {
  category: (typeof AP_CATEGORIES)[number];
  subjects: ApCatalogEntry[];
}[] {
  return AP_CATEGORIES.map((category) => ({
    category,
    subjects: AP_CATALOG.filter((s) => s.category === category.id),
  })).filter((g) => g.subjects.length > 0);
}
