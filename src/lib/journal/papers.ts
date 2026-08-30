/**
 * The Scholarly Journal's published papers.
 *
 * Metadata lives here; each paper's body is a component in
 * `src/components/journal/`, keyed by slug in the journal's [slug] route. A
 * registry rather than a database table because a published paper is
 * immutable once it is out — the version a reader cites should not be able to
 * change under them — and because the set is small enough that a code review
 * is a better editorial gate than an admin form.
 *
 * Work IN PROGRESS is different and does live in the database, as
 * `ResearchProposal` rows with status ACCEPTED; the journal index shows both.
 */

export interface JournalPaper {
  slug: string;
  title: string;
  /** The subtitle that carries the method, as an academic subtitle should. */
  subtitle?: string;
  author: string;
  /** Field label, matching the research programme's areas. */
  field: string;
  /** ISO date the paper was published here. */
  publishedAt: string;
  /** One paragraph, shown on the index and used as the page description. */
  abstract: string;
  /** Rough reading time in minutes, for the index card. */
  readingMinutes: number;
}

export const JOURNAL_PAPERS: JournalPaper[] = [
  {
    slug: "study-time-focus-and-sat-score-improvement",
    title: "Study Time, Focus, and Baseline Ability as Correlates of SAT Score Improvement",
    subtitle: "A descriptive survey of more than twenty test-takers",
    author: "Muhammadjon Ulashov",
    field: "Education",
    publishedAt: "2026-08-30",
    abstract:
      "Preparation for the SAT varies widely in intensity, duration, and quality of attention, " +
      "but students receive little evidence about which of those dimensions matters most, or " +
      "whether the answer depends on where they start. This study surveyed more than twenty " +
      "test-takers on their baseline score, months of preparation, daily study hours, " +
      "self-rated focus, and score improvement, and compared respondents who began below a " +
      "1100 cut point with those who began above it. Daily study intensity was more closely " +
      "associated with improvement than total preparation duration in both groups, and the " +
      "below-cut group improved more on average (320 points, against 220). Both findings are " +
      "reported as associations rather than effects: the design is observational, the sample " +
      "is small, and regression to the mean is a live rival explanation for the group " +
      "difference that this data cannot rule out.",
    readingMinutes: 12,
  },
];

export function paperBySlug(slug: string): JournalPaper | undefined {
  return JOURNAL_PAPERS.find((p) => p.slug === slug);
}
