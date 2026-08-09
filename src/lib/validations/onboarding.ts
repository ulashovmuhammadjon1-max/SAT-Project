import { z } from "zod";

export const ONBOARDING_GOALS = ["IMPROVE_SCORE", "FIRST_SAT", "RETAKING", "COLLEGE_ADMISSIONS"] as const;
export const GRADE_LEVELS = [
  "GRADE_9",
  "GRADE_10",
  "GRADE_11",
  "GRADE_12",
  "GAP_YEAR",
  "COLLEGE",
  "OTHER",
] as const;
export const DAILY_GOAL_TYPES = ["QUESTIONS", "MINUTES"] as const;
export const SECTIONS = ["READING", "WRITING", "MATH"] as const;
export const WEAK_AREAS = ["READING", "WRITING", "MATH", "VOCABULARY", "TIME_MANAGEMENT"] as const;

/** SAT scores are reported in 10-point increments from 400 to 1600. */
const satScore = z
  .number()
  .int()
  .min(400)
  .max(1600)
  .refine((n) => n % 10 === 0, "Scores move in steps of 10");

/**
 * Everything the wizard collects. All fields are optional because a student can
 * skip any question — only the account credentials at the end are required.
 */
export const onboardingProfileSchema = z.object({
  goal: z.enum(ONBOARDING_GOALS).nullable().default(null),
  currentScore: satScore.nullable().default(null),
  targetScore: satScore.nullable().default(null),
  dreamUniversities: z.array(z.string().min(1).max(120)).max(12).default([]),
  countryCode: z
    .string()
    .regex(/^[A-Z]{2}$/, "Expected an ISO country code")
    .nullable()
    .default(null),
  gradeLevel: z.enum(GRADE_LEVELS).nullable().default(null),
  /** Month precision, stored as the first day of that month (YYYY-MM). */
  satMonth: z
    .string()
    .regex(/^\d{4}-(0[1-9]|1[0-2])$/, "Expected YYYY-MM")
    .nullable()
    .default(null),
  strongestSection: z.enum(SECTIONS).nullable().default(null),
  weakestArea: z.enum(WEAK_AREAS).nullable().default(null),
  studyMinutesPerDay: z.number().int().min(5).max(600).nullable().default(null),
  dailyGoalType: z.enum(DAILY_GOAL_TYPES).nullable().default(null),
  dailyGoalValue: z.number().int().min(1).max(500).nullable().default(null),
});

export type OnboardingProfile = z.infer<typeof onboardingProfileSchema>;

export const EMPTY_PROFILE: OnboardingProfile = {
  goal: null,
  currentScore: null,
  targetScore: null,
  dreamUniversities: [],
  countryCode: null,
  gradeLevel: null,
  satMonth: null,
  strongestSection: null,
  weakestArea: null,
  studyMinutesPerDay: null,
  dailyGoalType: null,
  dailyGoalValue: null,
};

export const onboardingSignupSchema = z.object({
  name: z.string().trim().min(2, "Please enter your name").max(80),
  email: z.string().trim().toLowerCase().email("Enter a valid email address"),
  password: z
    .string()
    .min(8, "Use at least 8 characters")
    .regex(/[A-Z]/, "Include one uppercase letter")
    .regex(/[0-9]/, "Include one number"),
  profile: onboardingProfileSchema,
  /**
   * Referral code carried in from `?ref=`. Optional and never trusted: an
   * unknown, malformed or self-referring code is ignored at attribution time
   * rather than failing the signup.
   */
  referralCode: z.string().trim().max(16).optional().nullable(),
  /**
   * Terms + Privacy acceptance. `literal(true)` rather than a boolean: the
   * request is rejected outright if it is missing or false, so the disabled
   * button is a courtesy rather than the actual enforcement.
   */
  acceptedTerms: z.literal(true, {
    errorMap: () => ({ message: "Please accept the Terms and Privacy Policy to continue." }),
  }),
});

export type OnboardingSignup = z.infer<typeof onboardingSignupSchema>;

/* ---------------------------------------------------------------------------
 * Display helpers, shared by the dashboard and the admin analytics page.
 * ------------------------------------------------------------------------- */

export const GRADE_LABELS: Record<(typeof GRADE_LEVELS)[number], string> = {
  GRADE_9: "9th grade",
  GRADE_10: "10th grade",
  GRADE_11: "11th grade",
  GRADE_12: "12th grade",
  GAP_YEAR: "Gap year",
  COLLEGE: "College",
  OTHER: "Other",
};

export const GOAL_LABELS: Record<(typeof ONBOARDING_GOALS)[number], string> = {
  IMPROVE_SCORE: "Improve my SAT score",
  FIRST_SAT: "Preparing for my first SAT",
  RETAKING: "Retaking the SAT",
  COLLEGE_ADMISSIONS: "College admissions",
};

export const SECTION_LABELS: Record<(typeof WEAK_AREAS)[number], string> = {
  READING: "Reading",
  WRITING: "Writing",
  MATH: "Math",
  VOCABULARY: "Vocabulary",
  TIME_MANAGEMENT: "Time management",
};

/**
 * `strongestSection` and `weakestArea` are plain columns, so values read back
 * from the database are only typed as `string`. This narrows them safely rather
 * than asserting, so an unexpected value degrades to `null` instead of crashing
 * a label lookup.
 */
export function asWeakArea(value: string | null | undefined): (typeof WEAK_AREAS)[number] | null {
  return value && (WEAK_AREAS as readonly string[]).includes(value)
    ? (value as (typeof WEAK_AREAS)[number])
    : null;
}

export function asSection(value: string | null | undefined): (typeof SECTIONS)[number] | null {
  return value && (SECTIONS as readonly string[]).includes(value) ? (value as (typeof SECTIONS)[number]) : null;
}
