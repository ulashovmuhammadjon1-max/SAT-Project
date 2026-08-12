/**
 * Achievements.
 *
 * Every one is *derived* from data the platform already records — streaks,
 * answers, attempts, vocabulary, referrals. Nothing is stored, so a student
 * who has been here for months unlocks their full history the moment this
 * ships, rather than starting from zero like a new account. That also means
 * there is no way for the badge list and the underlying numbers to drift
 * apart, which is the usual failure of a separate achievements table.
 *
 * Each definition carries a `target` and reads its `current` value off the
 * same stats bundle, so a locked badge can always show how far away it is.
 * A badge you cannot see progress toward is just a locked door.
 */

export type AchievementTier = "BRONZE" | "SILVER" | "GOLD" | "PLATINUM";

export type AchievementCategory =
  | "CONSISTENCY"
  | "VOLUME"
  | "TESTS"
  | "SCORE"
  | "ACCURACY"
  | "VOCABULARY"
  | "COMMUNITY";

export interface AchievementStats {
  currentStreak: number;
  longestStreak: number;
  daysActive: number;
  questionsAnswered: number;
  testsCompleted: number;
  bestScore: number;
  bestRw: number;
  bestMath: number;
  /** Question Bank accuracy, 0–100. Only meaningful past a sample floor. */
  accuracyPct: number;
  accuracySample: number;
  vocabMastered: number;
  vocabSetsPassed: number;
  referralsCompleted: number;
  sessionsAttended: number;
}

export interface AchievementDef {
  id: string;
  title: string;
  /** What to do to earn it — written as an instruction, not a riddle. */
  description: string;
  category: AchievementCategory;
  tier: AchievementTier;
  target: number;
  /** Where this badge's progress is read from. */
  current: (s: AchievementStats) => number;
  /**
   * Extra condition beyond `current >= target`. Used by the accuracy badges,
   * which must not unlock off three lucky answers.
   */
  eligible?: (s: AchievementStats) => boolean;
  /** Shown on a locked badge when `eligible` is what's blocking it. */
  requirement?: string;
  /**
   * Appended to both numbers in the progress readout. Without it the accuracy
   * badges render "63 / 70", which reads as sixty-three questions out of
   * seventy rather than sixty-three percent against a seventy percent target.
   */
  unit?: string;
}

/** Minimum answers before an accuracy badge can be earned. */
const ACCURACY_SAMPLE_FLOOR = 50;

export const ACHIEVEMENTS: AchievementDef[] = [
  // --- consistency --------------------------------------------------------
  {
    id: "streak-3",
    title: "Getting Started",
    description: "Study three days in a row.",
    category: "CONSISTENCY",
    tier: "BRONZE",
    target: 3,
    current: (s) => s.longestStreak,
  },
  {
    id: "streak-7",
    title: "Full Week",
    description: "Study seven days in a row.",
    category: "CONSISTENCY",
    tier: "SILVER",
    target: 7,
    current: (s) => s.longestStreak,
  },
  {
    id: "streak-30",
    title: "Iron Habit",
    description: "Study thirty days in a row.",
    category: "CONSISTENCY",
    tier: "GOLD",
    target: 30,
    current: (s) => s.longestStreak,
  },
  {
    id: "streak-100",
    title: "Unbreakable",
    description: "Study a hundred days in a row.",
    category: "CONSISTENCY",
    tier: "PLATINUM",
    target: 100,
    current: (s) => s.longestStreak,
  },
  {
    id: "days-25",
    title: "Regular",
    description: "Study on twenty-five separate days.",
    category: "CONSISTENCY",
    tier: "SILVER",
    target: 25,
    current: (s) => s.daysActive,
  },

  // --- volume -------------------------------------------------------------
  {
    id: "questions-50",
    title: "First Fifty",
    description: "Answer fifty questions.",
    category: "VOLUME",
    tier: "BRONZE",
    target: 50,
    current: (s) => s.questionsAnswered,
  },
  {
    id: "questions-250",
    title: "Warmed Up",
    description: "Answer 250 questions.",
    category: "VOLUME",
    tier: "BRONZE",
    target: 250,
    current: (s) => s.questionsAnswered,
  },
  {
    id: "questions-1000",
    title: "Four Figures",
    description: "Answer a thousand questions.",
    category: "VOLUME",
    tier: "SILVER",
    target: 1000,
    current: (s) => s.questionsAnswered,
  },
  {
    id: "questions-5000",
    title: "Marathon",
    description: "Answer five thousand questions.",
    category: "VOLUME",
    tier: "PLATINUM",
    target: 5000,
    current: (s) => s.questionsAnswered,
  },

  // --- tests --------------------------------------------------------------
  {
    id: "tests-1",
    title: "First Sitting",
    description: "Finish a full practice test.",
    category: "TESTS",
    tier: "BRONZE",
    target: 1,
    current: (s) => s.testsCompleted,
  },
  {
    id: "tests-5",
    title: "Five Down",
    description: "Finish five full practice tests.",
    category: "TESTS",
    tier: "SILVER",
    target: 5,
    current: (s) => s.testsCompleted,
  },
  {
    id: "tests-10",
    title: "Seasoned",
    description: "Finish ten full practice tests.",
    category: "TESTS",
    tier: "GOLD",
    target: 10,
    current: (s) => s.testsCompleted,
  },
  {
    id: "tests-25",
    title: "Test Veteran",
    description: "Finish twenty-five full practice tests.",
    category: "TESTS",
    tier: "PLATINUM",
    target: 25,
    current: (s) => s.testsCompleted,
  },

  // --- score --------------------------------------------------------------
  {
    id: "score-1000",
    title: "Four Digits",
    description: "Score 1000 or higher on a practice test.",
    category: "SCORE",
    tier: "BRONZE",
    target: 1000,
    current: (s) => s.bestScore,
  },
  {
    id: "score-1200",
    title: "Climbing",
    description: "Score 1200 or higher on a practice test.",
    category: "SCORE",
    tier: "SILVER",
    target: 1200,
    current: (s) => s.bestScore,
  },
  {
    id: "score-1400",
    title: "Top Tier",
    description: "Score 1400 or higher on a practice test.",
    category: "SCORE",
    tier: "GOLD",
    target: 1400,
    current: (s) => s.bestScore,
  },
  {
    id: "score-1500",
    title: "Elite",
    description: "Score 1500 or higher on a practice test.",
    category: "SCORE",
    tier: "PLATINUM",
    target: 1500,
    current: (s) => s.bestScore,
  },
  {
    id: "rw-700",
    title: "Word Master",
    description: "Score 700 or higher on Reading & Writing.",
    category: "SCORE",
    tier: "GOLD",
    target: 700,
    current: (s) => s.bestRw,
  },
  {
    id: "math-700",
    title: "Number Master",
    description: "Score 700 or higher on Math.",
    category: "SCORE",
    tier: "GOLD",
    target: 700,
    current: (s) => s.bestMath,
  },

  // --- accuracy -----------------------------------------------------------
  {
    id: "accuracy-70",
    title: "Sharp",
    description: "Reach 70% accuracy in the Question Bank.",
    category: "ACCURACY",
    tier: "BRONZE",
    target: 70,
    current: (s) => s.accuracyPct,
    eligible: (s) => s.accuracySample >= ACCURACY_SAMPLE_FLOOR,
    requirement: `needs ${ACCURACY_SAMPLE_FLOOR}+ answers`,
    unit: "%",
  },
  {
    id: "accuracy-80",
    title: "Precise",
    description: "Reach 80% accuracy in the Question Bank.",
    category: "ACCURACY",
    tier: "SILVER",
    target: 80,
    current: (s) => s.accuracyPct,
    eligible: (s) => s.accuracySample >= ACCURACY_SAMPLE_FLOOR,
    requirement: `needs ${ACCURACY_SAMPLE_FLOOR}+ answers`,
    unit: "%",
  },
  {
    id: "accuracy-90",
    title: "Deadly Accurate",
    description: "Reach 90% accuracy in the Question Bank.",
    category: "ACCURACY",
    tier: "PLATINUM",
    target: 90,
    current: (s) => s.accuracyPct,
    eligible: (s) => s.accuracySample >= ACCURACY_SAMPLE_FLOOR,
    requirement: `needs ${ACCURACY_SAMPLE_FLOOR}+ answers`,
    unit: "%",
  },

  // --- vocabulary ---------------------------------------------------------
  {
    id: "vocab-25",
    title: "Word Collector",
    description: "Master twenty-five vocabulary words.",
    category: "VOCABULARY",
    tier: "BRONZE",
    target: 25,
    current: (s) => s.vocabMastered,
  },
  {
    id: "vocab-100",
    title: "Lexicon",
    description: "Master a hundred vocabulary words.",
    category: "VOCABULARY",
    tier: "SILVER",
    target: 100,
    current: (s) => s.vocabMastered,
  },
  {
    id: "vocab-250",
    title: "Walking Dictionary",
    description: "Master 250 vocabulary words.",
    category: "VOCABULARY",
    tier: "GOLD",
    target: 250,
    current: (s) => s.vocabMastered,
  },
  {
    id: "sets-5",
    title: "Set Runner",
    description: "Pass five vocabulary set quizzes.",
    category: "VOCABULARY",
    tier: "SILVER",
    target: 5,
    current: (s) => s.vocabSetsPassed,
  },
  {
    id: "sets-16",
    title: "Every Set",
    description: "Pass all sixteen vocabulary set quizzes.",
    category: "VOCABULARY",
    tier: "PLATINUM",
    target: 16,
    current: (s) => s.vocabSetsPassed,
  },

  // --- community ----------------------------------------------------------
  {
    id: "referral-1",
    title: "Spread the Word",
    description: "Invite a friend who joins and verifies.",
    category: "COMMUNITY",
    tier: "BRONZE",
    target: 1,
    current: (s) => s.referralsCompleted,
  },
  {
    id: "referral-3",
    title: "Recruiter",
    description: "Invite three friends who join and verify.",
    category: "COMMUNITY",
    tier: "SILVER",
    target: 3,
    current: (s) => s.referralsCompleted,
  },
  {
    id: "referral-10",
    title: "Community Builder",
    description: "Invite ten friends who join and verify.",
    category: "COMMUNITY",
    tier: "GOLD",
    target: 10,
    current: (s) => s.referralsCompleted,
  },
  {
    id: "session-1",
    title: "Asked for Help",
    description: "Attend a mentorship session.",
    category: "COMMUNITY",
    tier: "BRONZE",
    target: 1,
    current: (s) => s.sessionsAttended,
  },
  {
    id: "session-5",
    title: "Regular Attendee",
    description: "Attend five mentorship sessions.",
    category: "COMMUNITY",
    tier: "GOLD",
    target: 5,
    current: (s) => s.sessionsAttended,
  },
];

export interface EarnedAchievement extends AchievementDef {
  currentValue: number;
  unlocked: boolean;
  /** 0–100, capped. Used for the progress bar on a locked badge. */
  progressPct: number;
  /** Set when `eligible` is false — the badge is gated, not merely short. */
  blockedBy: string | null;
}

export function evaluateAchievements(stats: AchievementStats): EarnedAchievement[] {
  return ACHIEVEMENTS.map((def) => {
    const currentValue = def.current(stats);
    const eligible = def.eligible ? def.eligible(stats) : true;
    return {
      ...def,
      currentValue,
      unlocked: eligible && currentValue >= def.target,
      progressPct: Math.min(100, Math.round((currentValue / def.target) * 100)),
      blockedBy: eligible ? null : (def.requirement ?? "not yet eligible"),
    };
  });
}

export const CATEGORY_LABELS: Record<AchievementCategory, string> = {
  CONSISTENCY: "Consistency",
  VOLUME: "Practice volume",
  TESTS: "Practice tests",
  SCORE: "Scores",
  ACCURACY: "Accuracy",
  VOCABULARY: "Vocabulary",
  COMMUNITY: "Community",
};

export const TIER_ORDER: AchievementTier[] = ["BRONZE", "SILVER", "GOLD", "PLATINUM"];
