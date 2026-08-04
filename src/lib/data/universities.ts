export interface University {
  name: string;
  country: string;
  /** Extra search terms so "Penn", "UCLA" or "LSE" find the right school. */
  aliases?: string[];
}

/**
 * Universities offered in the onboarding picker. Deliberately weighted toward
 * the schools SAT takers actually target — US selectives plus the English- and
 * Italian-taught European programmes popular with Central Asian applicants,
 * who make up a large share of this platform's audience.
 *
 * The picker also accepts free text, so this list is a convenience, not a limit.
 */
export const UNIVERSITIES: University[] = [
  // ---- US: Ivy League + peers -------------------------------------------
  { name: "Harvard University", country: "United States" },
  { name: "Yale University", country: "United States" },
  { name: "Princeton University", country: "United States" },
  { name: "Columbia University", country: "United States" },
  { name: "Brown University", country: "United States" },
  { name: "Cornell University", country: "United States" },
  { name: "Dartmouth College", country: "United States" },
  { name: "University of Pennsylvania", country: "United States", aliases: ["Penn", "UPenn", "Wharton"] },
  { name: "Massachusetts Institute of Technology", country: "United States", aliases: ["MIT"] },
  { name: "Stanford University", country: "United States" },
  { name: "California Institute of Technology", country: "United States", aliases: ["Caltech"] },
  { name: "Duke University", country: "United States" },
  { name: "Johns Hopkins University", country: "United States", aliases: ["JHU"] },
  { name: "Northwestern University", country: "United States" },
  { name: "University of Chicago", country: "United States", aliases: ["UChicago"] },
  { name: "Vanderbilt University", country: "United States" },
  { name: "Rice University", country: "United States" },
  { name: "Washington University in St. Louis", country: "United States", aliases: ["WashU"] },
  { name: "Georgetown University", country: "United States" },
  { name: "University of Notre Dame", country: "United States" },
  { name: "Carnegie Mellon University", country: "United States", aliases: ["CMU"] },
  { name: "Emory University", country: "United States" },
  { name: "Tufts University", country: "United States" },
  { name: "New York University", country: "United States", aliases: ["NYU"] },
  { name: "Boston University", country: "United States", aliases: ["BU"] },
  { name: "Northeastern University", country: "United States" },
  { name: "University of Southern California", country: "United States", aliases: ["USC"] },

  // ---- US: liberal arts --------------------------------------------------
  { name: "Williams College", country: "United States" },
  { name: "Amherst College", country: "United States" },
  { name: "Swarthmore College", country: "United States" },
  { name: "Pomona College", country: "United States" },
  { name: "Wellesley College", country: "United States" },
  { name: "Bowdoin College", country: "United States" },
  { name: "Middlebury College", country: "United States" },
  { name: "Colby College", country: "United States" },
  { name: "Hamilton College", country: "United States" },
  { name: "Grinnell College", country: "United States" },
  { name: "Bard College", country: "United States" },

  // ---- US: public flagships ---------------------------------------------
  { name: "University of California, Berkeley", country: "United States", aliases: ["UC Berkeley", "Cal"] },
  { name: "University of California, Los Angeles", country: "United States", aliases: ["UCLA"] },
  { name: "University of California, San Diego", country: "United States", aliases: ["UCSD"] },
  { name: "University of Michigan", country: "United States", aliases: ["UMich"] },
  { name: "University of Virginia", country: "United States", aliases: ["UVA"] },
  { name: "University of North Carolina at Chapel Hill", country: "United States", aliases: ["UNC"] },
  { name: "University of Texas at Austin", country: "United States", aliases: ["UT Austin"] },
  { name: "Georgia Institute of Technology", country: "United States", aliases: ["Georgia Tech"] },
  { name: "University of Illinois Urbana-Champaign", country: "United States", aliases: ["UIUC"] },
  { name: "University of Wisconsin–Madison", country: "United States" },
  { name: "University of Washington", country: "United States", aliases: ["UW"] },
  { name: "University of Florida", country: "United States", aliases: ["UF"] },
  { name: "Purdue University", country: "United States" },
  { name: "Pennsylvania State University", country: "United States", aliases: ["Penn State"] },
  { name: "Arizona State University", country: "United States", aliases: ["ASU"] },

  // ---- United Kingdom ----------------------------------------------------
  { name: "University of Oxford", country: "United Kingdom" },
  { name: "University of Cambridge", country: "United Kingdom" },
  { name: "Imperial College London", country: "United Kingdom" },
  { name: "London School of Economics", country: "United Kingdom", aliases: ["LSE"] },
  { name: "University College London", country: "United Kingdom", aliases: ["UCL"] },
  { name: "King's College London", country: "United Kingdom", aliases: ["KCL"] },
  { name: "University of Edinburgh", country: "United Kingdom" },
  { name: "University of Manchester", country: "United Kingdom" },
  { name: "University of Warwick", country: "United Kingdom" },
  { name: "University of St Andrews", country: "United Kingdom" },

  // ---- Europe ------------------------------------------------------------
  { name: "Bocconi University", country: "Italy", aliases: ["Universita Bocconi"] },
  { name: "Politecnico di Milano", country: "Italy" },
  { name: "Sapienza University of Rome", country: "Italy" },
  { name: "University of Bologna", country: "Italy" },
  { name: "ETH Zurich", country: "Switzerland" },
  { name: "EPFL", country: "Switzerland", aliases: ["Ecole Polytechnique Federale de Lausanne"] },
  { name: "University of Amsterdam", country: "Netherlands" },
  { name: "Delft University of Technology", country: "Netherlands", aliases: ["TU Delft"] },
  { name: "Erasmus University Rotterdam", country: "Netherlands" },
  { name: "Technical University of Munich", country: "Germany", aliases: ["TUM"] },
  { name: "Ludwig Maximilian University of Munich", country: "Germany", aliases: ["LMU"] },
  { name: "Heidelberg University", country: "Germany" },
  { name: "Jacobs University Bremen", country: "Germany", aliases: ["Constructor University"] },
  { name: "Sciences Po", country: "France" },
  { name: "HEC Paris", country: "France" },
  { name: "Sorbonne University", country: "France" },
  { name: "IE University", country: "Spain" },
  { name: "Trinity College Dublin", country: "Ireland" },
  { name: "Central European University", country: "Austria", aliases: ["CEU"] },
  { name: "Charles University", country: "Czechia" },

  // ---- Asia & Middle East -------------------------------------------------
  { name: "National University of Singapore", country: "Singapore", aliases: ["NUS"] },
  { name: "Nanyang Technological University", country: "Singapore", aliases: ["NTU"] },
  { name: "University of Hong Kong", country: "Hong Kong", aliases: ["HKU"] },
  { name: "Hong Kong University of Science and Technology", country: "Hong Kong", aliases: ["HKUST"] },
  { name: "Tsinghua University", country: "China" },
  { name: "Peking University", country: "China" },
  { name: "NYU Shanghai", country: "China" },
  { name: "University of Tokyo", country: "Japan" },
  { name: "Waseda University", country: "Japan" },
  { name: "Seoul National University", country: "South Korea" },
  { name: "KAIST", country: "South Korea" },
  { name: "Indian Institute of Technology Bombay", country: "India", aliases: ["IIT Bombay"] },
  { name: "Indian Institute of Technology Delhi", country: "India", aliases: ["IIT Delhi"] },
  { name: "Ashoka University", country: "India" },
  { name: "New York University Abu Dhabi", country: "United Arab Emirates", aliases: ["NYUAD"] },
  { name: "American University of Sharjah", country: "United Arab Emirates", aliases: ["AUS"] },
  { name: "Khalifa University", country: "United Arab Emirates" },
  { name: "Koç University", country: "Türkiye", aliases: ["Koc University"] },
  { name: "Sabancı University", country: "Türkiye", aliases: ["Sabanci University"] },
  { name: "Boğaziçi University", country: "Türkiye", aliases: ["Bogazici University"] },
  { name: "Bilkent University", country: "Türkiye" },
  { name: "Middle East Technical University", country: "Türkiye", aliases: ["METU", "ODTU"] },
  { name: "American University of Central Asia", country: "Kyrgyzstan", aliases: ["AUCA"] },
  { name: "Nazarbayev University", country: "Kazakhstan" },
  { name: "KIMEP University", country: "Kazakhstan" },
  { name: "Westminster International University in Tashkent", country: "Uzbekistan", aliases: ["WIUT"] },
  { name: "Webster University in Tashkent", country: "Uzbekistan" },
  { name: "Inha University in Tashkent", country: "Uzbekistan" },
  { name: "New Uzbekistan University", country: "Uzbekistan" },

  // ---- Canada & Oceania ---------------------------------------------------
  { name: "University of Toronto", country: "Canada", aliases: ["UofT"] },
  { name: "University of British Columbia", country: "Canada", aliases: ["UBC"] },
  { name: "McGill University", country: "Canada" },
  { name: "University of Waterloo", country: "Canada" },
  { name: "University of Melbourne", country: "Australia" },
  { name: "University of Sydney", country: "Australia" },
  { name: "Australian National University", country: "Australia", aliases: ["ANU"] },
];

/** Suggestions shown before the student types anything. */
export const FEATURED_UNIVERSITIES = [
  "Harvard University",
  "Massachusetts Institute of Technology",
  "Stanford University",
  "Princeton University",
  "Yale University",
  "Columbia University",
  "Cornell University",
  "New York University",
  "Georgetown University",
  "Bocconi University",
];

export function searchUniversities(query: string, limit = 40): University[] {
  const q = query.trim().toLowerCase();
  if (!q) {
    const featured = new Set(FEATURED_UNIVERSITIES);
    return UNIVERSITIES.filter((u) => featured.has(u.name));
  }
  const scored: { u: University; score: number }[] = [];
  for (const u of UNIVERSITIES) {
    const haystacks = [u.name, ...(u.aliases ?? [])].map((h) => h.toLowerCase());
    let best = -1;
    for (const h of haystacks) {
      const idx = h.indexOf(q);
      if (idx === -1) continue;
      // Prefix matches rank above matches buried mid-name.
      const score = idx === 0 ? 0 : 1;
      if (best === -1 || score < best) best = score;
    }
    if (best === -1 && u.country.toLowerCase().includes(q)) best = 2;
    if (best !== -1) scored.push({ u, score: best });
  }
  return scored
    .sort((a, b) => a.score - b.score || a.u.name.localeCompare(b.u.name))
    .slice(0, limit)
    .map((s) => s.u);
}
