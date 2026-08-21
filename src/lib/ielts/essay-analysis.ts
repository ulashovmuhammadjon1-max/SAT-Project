import Anthropic from "@anthropic-ai/sdk";
import { createHash } from "crypto";
import { z } from "zod";

import { zodToJsonSchema } from "@/lib/ai/providers/claude-provider";

/**
 * Deconstructing a Band 8+ Task 2 essay into teaching material.
 *
 * The model is an assistant here, never the author: everything it returns lands
 * in an admin review queue and cannot reach a student until a human has kept
 * it. That is a product rule, and it is also the only honest way to ship
 * language teaching — a confident wrong annotation teaches the error.
 *
 * Same provider, model and structured-output shape as the PDF ingestion
 * pipeline (`lib/ai/providers/claude-provider.ts`); this is a second caller of
 * that infrastructure, not a second copy of it.
 */

const MODEL = "claude-opus-5";

export const ANNOTATION_CATEGORIES = ["GRAMMAR", "VOCABULARY", "COHESION", "COLLOCATION"] as const;
export type AnnotationCategory = (typeof ANNOTATION_CATEGORIES)[number];

/**
 * What the model returns for one highlight.
 *
 * Note what is **not** here: character offsets. Asking a language model to
 * count characters is asking it to do the one thing it is worst at, and a
 * plausible-but-wrong offset silently highlights the wrong words. Instead it
 * returns the exact quote plus which occurrence of that quote it means, and
 * this file computes the offsets deterministically — which also answers the
 * repeated-phrase problem properly, rather than by taking the first match.
 */
const annotationSchema = z.object({
  category: z.enum(ANNOTATION_CATEGORIES),
  subtype: z.string(),
  quote: z.string(),
  /** 1-based: which occurrence of `quote` in the essay this refers to. */
  occurrence: z.number(),
  explanation: z.string(),
  ieltsValue: z.string(),
  pattern: z.string().nullable(),
  confidence: z.number(),
});

const ideaSchema = z.object({
  claim: z.string(),
  explanation: z.string(),
  consequence: z.string().nullable(),
  example: z.string().nullable(),
  /** Where the idea surfaces, so the student can jump to it. Optional. */
  anchorQuote: z.string().nullable(),
});

const analysisSchema = z.object({
  annotations: z.array(annotationSchema),
  ideas: z.array(ideaSchema),
});

export interface LocatedAnnotation {
  category: AnnotationCategory;
  subtype: string;
  quote: string;
  startOffset: number;
  endOffset: number;
  explanation: string;
  ieltsValue: string | null;
  pattern: string | null;
  confidence: number;
}

export interface LocatedIdea {
  claim: string;
  explanation: string;
  consequence: string | null;
  example: string | null;
  startOffset: number | null;
  endOffset: number | null;
}

export interface EssayAnalysis {
  annotations: LocatedAnnotation[];
  ideas: LocatedIdea[];
  /** Anything dropped, and why. Shown to the admin, never to a student. */
  warnings: string[];
}

/** Identifies the exact text the annotations were computed against. */
export function hashEssayText(text: string): string {
  return createHash("sha256").update(text, "utf8").digest("hex");
}

export function countWords(text: string): number {
  return text.trim().split(/\s+/).filter(Boolean).length;
}

/**
 * Find the character span of the `occurrence`-th instance of `quote`.
 *
 * Exact match first. Falling back to a whitespace-insensitive scan matters more
 * than it sounds: a model reliably reproduces the words of a quote and quite
 * unreliably reproduces a line break in the middle of it, and losing a correct
 * annotation to a newline would be a silly way to make the feature worse.
 *
 * Returns null when the quote is not in the essay at all, or when the requested
 * occurrence does not exist — both of which mean the annotation is describing
 * text that is not there, and it is dropped rather than guessed at.
 */
export function locateQuote(
  essayText: string,
  quote: string,
  occurrence = 1
): { startOffset: number; endOffset: number } | null {
  const wanted = Math.max(1, Math.floor(occurrence));
  const needle = quote.trim();
  if (!needle) return null;

  // Exact. Collect every occurrence rather than stopping at the wanted one,
  // because whether a miscount is safe to correct depends on how many there are.
  const exact: number[] = [];
  for (let at = essayText.indexOf(needle); at !== -1; at = essayText.indexOf(needle, at + 1)) {
    exact.push(at);
  }
  if (exact.length > 0) {
    if (wanted <= exact.length) {
      const at = exact[wanted - 1];
      return { startOffset: at, endOffset: at + needle.length };
    }
    // The occurrence asked for does not exist. If the phrase appears exactly
    // once there is nothing to get wrong, so the miscount is safe to correct.
    //
    // If it appears several times, it is not: placing it on the first is a
    // guess, and a guess here highlights the wrong sentence while looking
    // entirely convincing. That is the failure this whole occurrence scheme
    // exists to prevent, so the annotation is dropped instead.
    if (exact.length === 1) {
      return { startOffset: exact[0], endOffset: exact[0] + needle.length };
    }
    return null;
  }

  // Whitespace-insensitive. Build a regex from the words so any run of
  // whitespace in the essay matches any run in the quote.
  const escaped = needle
    .split(/\s+/)
    .map((w) => w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"))
    .join("\\s+");
  const re = new RegExp(escaped, "g");
  const loose: { startOffset: number; endOffset: number }[] = [];
  for (let m = re.exec(essayText); m; m = re.exec(essayText)) {
    loose.push({ startOffset: m.index, endOffset: m.index + m[0].length });
  }
  if (loose.length === 0) return null;
  if (wanted <= loose.length) return loose[wanted - 1];
  // Same reasoning as above: correct a miscount only when it is unambiguous.
  return loose.length === 1 ? loose[0] : null;
}

const SYSTEM_PROMPT = [
  "You are an experienced IELTS examiner preparing teaching material from a Band 8+ Writing Task 2 essay.",
  "Your job is to point out the language a candidate could actually learn from and reuse.",
  "",
  "BE CONSERVATIVE. A wrong annotation is far worse than a missing one, because a student will",
  "believe it. If an essay contains only five genuinely useful vocabulary items, return five.",
  "Never pad the analysis to make it look thorough.",
  "",
  "Do NOT annotate:",
  "- a long sentence merely because it is long",
  "- an ordinary word because it happens to relate to the topic (e.g. 'pollution' in an environment essay)",
  "- 'and', 'but', 'because', or 'so' as cohesive devices",
  "- an ordinary adjective+noun pair as a collocation (e.g. 'very important issue')",
  "- anything a Band 6 candidate would already produce naturally",
  "",
  "The four categories:",
  "GRAMMAR — a genuinely advanced structure: relative/concessive/conditional clauses, participle",
  "  and reduced relative clauses, inversion, cleft structures, complex noun phrases, passives",
  "  used for a reason, sophisticated comparatives. Name the structure in `subtype`",
  "  (e.g. relative_clause, concessive_clause, cleft_structure).",
  "VOCABULARY — lexis that shows subject knowledge or precision. `subtype` is one of",
  "  topic_specific or sophisticated. Basic topic words do not qualify.",
  "COHESION — meaningful connection between ideas, including referencing, substitution and",
  "  lexical chains, not just linkers. `subtype` names the relationship",
  "  (e.g. contrast, concession, result, exemplification, reference).",
  "COLLOCATION — a natural, precise, high-value phrase worth memorising",
  "  (e.g. 'play a crucial role', 'pose a significant threat'). `subtype` is high_value_phrase.",
  "",
  "For every annotation:",
  "- `quote` must be copied EXACTLY from the essay, character for character.",
  "- `occurrence` says which instance of that quote you mean, counting from 1. If the same",
  "  wording appears three times and you mean the second, send 2. This is how the highlight",
  "  is placed, so it must be right.",
  "- `explanation` says what the feature is, in one or two sentences a student can follow.",
  "- `ieltsValue` says why it is worth learning for IELTS.",
  "- `pattern` is a reusable frame where one genuinely exists, otherwise null.",
  "- `confidence` is your own 0-1 judgement.",
  "",
  "IDEAS: extract the arguments the essay actually makes, so a student can reuse them on a",
  "different question. Each needs a `claim` and an `explanation`; add `consequence` where the",
  "essay draws one. Set `example` ONLY if the essay contains an actual example — never invent",
  "one. `anchorQuote` is an exact quote where the idea appears, or null.",
  "Do not summarise the essay paragraph by paragraph. Extract reusable arguments.",
].join("\n");

/** Thrown for conditions the admin can act on; the message is safe to show. */
export class EssayAnalysisError extends Error {}

/**
 * Analyse an essay. Never writes to the database — the caller decides what to
 * keep, which is what makes the admin the author of record.
 */
export async function analyzeEssay(params: {
  question: string;
  essayText: string;
  topic: string;
  band: number;
}): Promise<EssayAnalysis> {
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    // No heuristic fallback on purpose. A regex "analyser" would produce
    // exactly the false positives this feature exists to avoid, and a library
    // of confidently-wrong grammar notes is worse than an empty one. The admin
    // can still annotate by hand.
    throw new EssayAnalysisError(
      "AI analysis is not configured — ANTHROPIC_API_KEY is not set. Annotations can still be added by hand."
    );
  }

  const client = new Anthropic({ apiKey });
  const userContent = [
    `TOPIC: ${params.topic}`,
    `BAND: ${params.band}`,
    "",
    "TASK 2 QUESTION:",
    params.question,
    "",
    "ESSAY (annotate only this text):",
    params.essayText,
  ].join("\n");

  let message;
  try {
    const stream = client.messages.stream({
      model: MODEL,
      max_tokens: 32000,
      thinking: { type: "adaptive" },
      output_config: {
        effort: "high",
        format: {
          type: "json_schema",
          schema: { name: "ielts_essay_analysis", schema: zodToJsonSchema(analysisSchema) },
        },
      },
      system: SYSTEM_PROMPT,
      messages: [{ role: "user", content: userContent }],
    });
    message = await stream.finalMessage();
  } catch (err) {
    if (err instanceof Anthropic.RateLimitError) {
      throw new EssayAnalysisError("The AI service is rate limited right now. Try again shortly.");
    }
    if (err instanceof Anthropic.AuthenticationError) {
      throw new EssayAnalysisError("The AI API key was rejected. Check ANTHROPIC_API_KEY.");
    }
    if (err instanceof Anthropic.APIError) {
      throw new EssayAnalysisError(`The AI service returned an error (${err.status}).`);
    }
    throw new EssayAnalysisError("Could not reach the AI service. Try again.");
  }

  if (message.stop_reason === "refusal") {
    throw new EssayAnalysisError("The model declined to analyse this essay.");
  }

  const textBlock = message.content.find((b) => b.type === "text");
  if (!textBlock || textBlock.type !== "text") {
    throw new EssayAnalysisError("The AI returned no analysis. Try again.");
  }

  let raw: z.infer<typeof analysisSchema>;
  try {
    raw = analysisSchema.parse(JSON.parse(textBlock.text));
  } catch {
    throw new EssayAnalysisError("The AI returned malformed analysis. Try re-analysing.");
  }

  return resolveAnalysis(params.essayText, raw);
}

/**
 * Turn quotes into offsets and throw away anything that cannot be placed.
 *
 * Exported so it can be unit-tested without an API call — the locating logic is
 * where a highlight silently lands on the wrong words, so it is the part that
 * most needs testing.
 */
export function resolveAnalysis(
  essayText: string,
  raw: z.infer<typeof analysisSchema>
): EssayAnalysis {
  const warnings: string[] = [];
  const annotations: LocatedAnnotation[] = [];
  const seen = new Set<string>();

  for (const a of raw.annotations) {
    const span = locateQuote(essayText, a.quote, a.occurrence);
    if (!span) {
      const present = essayText.includes(a.quote.trim());
      warnings.push(
        present
          ? `Dropped ${a.category.toLowerCase()} "${a.quote.slice(0, 40)}" — it appears several times and occurrence ${a.occurrence} does not exist, so the highlight could not be placed safely.`
          : `Dropped ${a.category.toLowerCase()} "${a.quote.slice(0, 40)}" — not found in the essay.`
      );
      continue;
    }
    // The quote as it truly appears, so `quote` always equals the text at those
    // offsets. Any later drift is then detectable by comparison.
    const actual = essayText.slice(span.startOffset, span.endOffset);

    // Same category over the same span twice is noise, not two lessons.
    const key = `${a.category}:${span.startOffset}:${span.endOffset}`;
    if (seen.has(key)) continue;
    seen.add(key);

    annotations.push({
      category: a.category,
      subtype: a.subtype.trim() || "general",
      quote: actual,
      startOffset: span.startOffset,
      endOffset: span.endOffset,
      explanation: a.explanation.trim(),
      ieltsValue: a.ieltsValue.trim() || null,
      pattern: a.pattern?.trim() || null,
      confidence: Math.max(0, Math.min(1, a.confidence)),
    });
  }

  const ideas: LocatedIdea[] = raw.ideas.map((i) => {
    const span = i.anchorQuote ? locateQuote(essayText, i.anchorQuote, 1) : null;
    return {
      claim: i.claim.trim(),
      explanation: i.explanation.trim(),
      consequence: i.consequence?.trim() || null,
      example: i.example?.trim() || null,
      startOffset: span?.startOffset ?? null,
      endOffset: span?.endOffset ?? null,
    };
  });

  annotations.sort((a, b) => a.startOffset - b.startOffset);
  return { annotations, ideas, warnings };
}
