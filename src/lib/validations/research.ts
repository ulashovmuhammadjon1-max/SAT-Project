import { z } from "zod";

/**
 * The research proposal, shared by the form (live word counter) and the server
 * action (the real check), so the two can never disagree about the limits.
 */

export const INTRO_MAX_WORDS = 300;
export const INTRO_MIN_WORDS = 50;

/** Words as a reader would count them: runs of non-space characters. */
export function countWords(text: string): number {
  return text.trim().split(/\s+/).filter(Boolean).length;
}

export const proposalSchema = z.object({
  title: z.string().trim().min(8, "Give your project a real title (at least 8 characters).").max(160),
  field: z.string().trim().min(2, "What field is this in?").max(80),
  question: z
    .string()
    .trim()
    .min(30, "State the question you want to answer — a sentence or two.")
    .max(2000),
  priorWork: z
    .string()
    .trim()
    .min(30, "Tell us what you have already done on this question — reading, data, notes, anything.")
    .max(3000),
  motivation: z
    .string()
    .trim()
    .min(30, "Tell us why this question matters to you.")
    .max(4000),
  qualifications: z
    .string()
    .trim()
    .min(2, "List your exams and scores, or write “None yet”.")
    .max(1500),
  experience: z.string().trim().max(4000).optional().or(z.literal("")),
  introEssay: z
    .string()
    .trim()
    .refine((s) => countWords(s) >= INTRO_MIN_WORDS, {
      message: `Your introduction needs at least ${INTRO_MIN_WORDS} words.`,
    })
    .refine((s) => countWords(s) <= INTRO_MAX_WORDS, {
      message: `Your introduction is over ${INTRO_MAX_WORDS} words — please shorten it.`,
    }),
});
