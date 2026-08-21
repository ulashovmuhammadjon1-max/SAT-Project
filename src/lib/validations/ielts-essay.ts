import { z } from "zod";

/**
 * Validation for the Band 8+ Task 2 essay library.
 *
 * The band floor and the Task-2-only rule are enforced in three places: here,
 * in the server action that calls this, and as CHECK constraints in
 * `014_ielts_essay_library.sql`. That is not redundancy for its own sake — the
 * library's entire promise to a student is that everything in it is a Band 8+
 * Task 2 answer, so a 7.5 must be impossible rather than merely discouraged.
 */

/** The only bands this library will hold. */
export const ALLOWED_BANDS = [8.0, 8.5, 9.0] as const;
export type AllowedBand = (typeof ALLOWED_BANDS)[number];

export const bandSchema = z
  .number()
  .refine((v): v is AllowedBand => (ALLOWED_BANDS as readonly number[]).includes(v), {
    message: "Only Band 8.0, 8.5 and 9.0 essays belong in this library.",
  });

/**
 * Starting topics, used only when the admin has not typed their own.
 *
 * There is no existing taxonomy for IELTS themes — Domain/Skill is the SAT
 * curriculum tree and means nothing here — so the field is free text with these
 * as suggestions, rather than a hard enum that would need a migration the first
 * time an essay is about tourism.
 */
export const SUGGESTED_TOPICS = [
  "Education", "Environment", "Technology", "Health", "Government", "Society",
  "Crime", "Work", "Economy", "Transport", "Globalization", "Media", "Family", "Culture",
] as const;

/** Under this, it is a paragraph, not a Task 2 answer. */
const MIN_ESSAY_WORDS = 150;

const wordCount = (s: string) => s.trim().split(/\s+/).filter(Boolean).length;

export const essayInputSchema = z.object({
  title: z.string().trim().min(3, "Give the essay a title.").max(200),
  question: z.string().trim().min(20, "Paste the full Task 2 question."),
  essayText: z
    .string()
    .trim()
    .min(1, "The essay is empty.")
    .refine((s) => wordCount(s) >= MIN_ESSAY_WORDS, {
      message: `A Task 2 answer is at least ${MIN_ESSAY_WORDS} words.`,
    }),
  band: bandSchema,
  topic: z.string().trim().min(2, "Choose or type a topic."),
  subtopic: z.string().trim().max(80).optional().or(z.literal("")),
  tags: z.array(z.string().trim().min(1)).max(12).default([]),
});

export type EssayInput = z.infer<typeof essayInputSchema>;

export const annotationInputSchema = z.object({
  category: z.enum(["GRAMMAR", "VOCABULARY", "COHESION", "COLLOCATION"]),
  subtype: z.string().trim().min(1).max(60),
  quote: z.string().min(1),
  startOffset: z.number().int().min(0),
  endOffset: z.number().int().min(1),
  explanation: z.string().trim().min(1, "Say what this is."),
  ieltsValue: z.string().trim().optional().or(z.literal("")),
  pattern: z.string().trim().max(160).optional().or(z.literal("")),
});

export type AnnotationInput = z.infer<typeof annotationInputSchema>;

export const ideaInputSchema = z.object({
  claim: z.string().trim().min(3),
  explanation: z.string().trim().min(3),
  consequence: z.string().trim().optional().or(z.literal("")),
  example: z.string().trim().optional().or(z.literal("")),
});

/** Human labels, shared by the admin queue and the student legend. */
export const CATEGORY_LABELS: Record<AnnotationInput["category"], string> = {
  GRAMMAR: "Advanced Grammar",
  VOCABULARY: "Topic Vocabulary",
  COHESION: "Cohesive Devices",
  COLLOCATION: "Strong Collocations",
};

export const STATUS_LABELS: Record<string, string> = {
  DRAFT: "Draft",
  ANALYZING: "Analyzing",
  NEEDS_REVIEW: "Needs review",
  READY: "Ready",
  PUBLISHED: "Published",
};
