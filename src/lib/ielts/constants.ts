/**
 * The shape of an IELTS Academic paper, and the wording rules that go with it.
 *
 * These are the publicly documented structural facts of the test — part counts,
 * question counts, durations, criteria names. They are collected here so a
 * screen never hardcodes "40" and then disagrees with the engine.
 */

import type { IeltsSkill } from "@prisma/client";

export const IELTS_SKILLS = ["LISTENING", "READING", "WRITING", "SPEAKING"] as const;

export interface SkillShape {
  skill: IeltsSkill;
  label: string;
  /** Parts for Listening/Speaking, passages for Reading, tasks for Writing. */
  parts: number;
  partNoun: string;
  questions: number | null;
  minutes: number;
  blurb: string;
}

export const SKILL_SHAPE: Record<IeltsSkill, SkillShape> = {
  LISTENING: {
    skill: "LISTENING", label: "Listening",
    parts: 4, partNoun: "parts", questions: 40, minutes: 30,
    blurb: "Four recorded parts, ten questions each. Each recording plays once.",
  },
  READING: {
    skill: "READING", label: "Reading",
    parts: 3, partNoun: "passages", questions: 40, minutes: 60,
    blurb: "Three academic passages and forty questions in sixty minutes.",
  },
  WRITING: {
    skill: "WRITING", label: "Writing",
    parts: 2, partNoun: "tasks", questions: null, minutes: 60,
    blurb: "Task 1 describes visual information; Task 2 is an essay.",
  },
  SPEAKING: {
    skill: "SPEAKING", label: "Speaking",
    parts: 3, partNoun: "parts", questions: null, minutes: 14,
    blurb: "Three parts, recorded and submitted for free human review.",
  },
};

/** Writing minimums, by task number. */
export const WRITING_MIN_WORDS: Record<number, number> = { 1: 150, 2: 250 };
/** Recommended split of the 60 minutes, by task number. */
export const WRITING_SUGGESTED_MINUTES: Record<number, number> = { 1: 20, 2: 40 };

/** Speaking timings, in seconds. */
export const SPEAKING_PART2_PREP_SECONDS = 60;
export const SPEAKING_PART2_SPEAK_SECONDS = 120;

/**
 * Listening pacing for the computer-delivered style.
 *
 * The computer test differs from paper: answers are typed straight in, so
 * there is no ten-minute transfer window. Instead each part gets time to read
 * the questions before the audio, a short check after it, and the whole
 * section closes with a final review.
 */
export const LISTENING_PART_READ_SECONDS = 30;
export const LISTENING_PART_REVIEW_SECONDS = 30;
export const LISTENING_FINAL_REVIEW_SECONDS = 120;

/** Where the timer changes appearance, in seconds remaining. */
export const TIMER_WARN_SECONDS = 10 * 60;
export const TIMER_URGENT_SECONDS = 5 * 60;

export const WRITING_CRITERIA = [
  { key: "task", label: "Task Achievement / Task Response" },
  { key: "coherence", label: "Coherence and Cohesion" },
  { key: "lexical", label: "Lexical Resource" },
  { key: "grammar", label: "Grammatical Range and Accuracy" },
] as const;

export const SPEAKING_CRITERIA = [
  { key: "fluency", label: "Fluency and Coherence" },
  { key: "lexical", label: "Lexical Resource" },
  { key: "grammar", label: "Grammatical Range and Accuracy" },
  { key: "pronunciation", label: "Pronunciation" },
] as const;

/**
 * How reviewers are described to students.
 *
 * Deliberately about the band the reviewer achieved, never about examiner
 * status, which Scholarly cannot verify and does not claim.
 */
export const REVIEWER_CLAIM = {
  WRITING: "Reviewed by a Band 8 IELTS writer",
  SPEAKING: "Reviewed by a Band 9 IELTS speaker",
} as const;

export const SPEAKING_PRODUCT_NAME = "Scholarly Speaking Practice";

/** Human-readable labels for every supported question type. */
export const QUESTION_TYPE_LABEL: Record<string, string> = {
  MULTIPLE_CHOICE_SINGLE: "Multiple choice",
  MULTIPLE_CHOICE_MULTI: "Multiple choice (more than one answer)",
  TRUE_FALSE_NOT_GIVEN: "True / False / Not Given",
  YES_NO_NOT_GIVEN: "Yes / No / Not Given",
  MATCHING_INFORMATION: "Matching information",
  MATCHING_HEADINGS: "Matching headings",
  MATCHING_FEATURES: "Matching features",
  MATCHING_SENTENCE_ENDINGS: "Matching sentence endings",
  MATCHING_GENERAL: "Matching",
  PLAN_MAP_DIAGRAM_LABEL: "Plan, map or diagram labelling",
  FORM_COMPLETION: "Form completion",
  NOTE_COMPLETION: "Note completion",
  TABLE_COMPLETION: "Table completion",
  FLOWCHART_COMPLETION: "Flow-chart completion",
  SUMMARY_COMPLETION: "Summary completion",
  SENTENCE_COMPLETION: "Sentence completion",
  SHORT_ANSWER: "Short-answer questions",
  DIAGRAM_LABEL_COMPLETION: "Diagram label completion",
};

/** Types whose answer is typed rather than selected. */
export const TYPED_ANSWER_TYPES = new Set([
  "PLAN_MAP_DIAGRAM_LABEL", "FORM_COMPLETION", "NOTE_COMPLETION",
  "TABLE_COMPLETION", "FLOWCHART_COMPLETION", "SUMMARY_COMPLETION",
  "SENTENCE_COMPLETION", "SHORT_ANSWER", "DIAGRAM_LABEL_COMPLETION",
]);
