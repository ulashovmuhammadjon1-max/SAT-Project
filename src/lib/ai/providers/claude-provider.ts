import Anthropic from "@anthropic-ai/sdk";
import { z } from "zod";

import type {
  AIExtractionProvider,
  ExplanationDraft,
  TestExtractionResult,
  VocabExtractionResult,
} from "@/lib/ai/types";

const MODEL = "claude-opus-5";

const choiceSchema = z.object({
  label: z.enum(["A", "B", "C", "D"]),
  content: z.string(),
  isCorrect: z.boolean(),
});

const questionSchema = z.object({
  number: z.number(),
  stem: z.string(),
  passageIndex: z.number().nullable(),
  type: z.enum(["MULTIPLE_CHOICE", "FREE_RESPONSE"]),
  choices: z.array(choiceSchema),
  correctAnswerFreeResponse: z.string().nullable(),
  explanation: z.string().nullable(),
  domainGuess: z.string(),
  skillGuess: z.string(),
  difficultyGuess: z.enum(["EASY", "MEDIUM", "HARD"]),
  hasImage: z.boolean(),
  hasTable: z.boolean(),
  confidence: z.number(),
});

const passageSchema = z.object({
  title: z.string().nullable(),
  content: z.string(),
});

const testExtractionSchema = z.object({
  passages: z.array(passageSchema),
  questions: z.array(questionSchema),
  overallConfidence: z.number(),
  warnings: z.array(z.string()),
});

const vocabWordSchema = z.object({
  term: z.string(),
  partOfSpeech: z.string().nullable(),
  definition: z.string(),
  exampleSentence: z.string().nullable(),
  synonyms: z.array(z.string()),
  antonyms: z.array(z.string()),
  difficultyGuess: z.enum(["EASY", "MEDIUM", "HARD"]),
  confidence: z.number(),
});

const vocabExtractionSchema = z.object({
  words: z.array(vocabWordSchema),
  overallConfidence: z.number(),
  warnings: z.array(z.string()),
});

const explanationSchema = z.object({
  content: z.string(),
  whyCorrect: z.string(),
  whyWrongJson: z.record(z.string()),
  commonMistakes: z.string(),
  tips: z.string(),
  relatedConcepts: z.string(),
});

export function zodToJsonSchema(schema: z.ZodTypeAny): Record<string, unknown> {
  // Minimal, hand-rolled conversion covering only the node types used above —
  // avoids adding a zod-to-json-schema dependency for a handful of shapes.
  if (schema instanceof z.ZodObject) {
    const shape = schema.shape as Record<string, z.ZodTypeAny>;
    const properties: Record<string, unknown> = {};
    for (const [key, value] of Object.entries(shape)) {
      properties[key] = zodToJsonSchema(value);
    }
    return {
      type: "object",
      properties,
      required: Object.keys(shape),
      additionalProperties: false,
    };
  }
  if (schema instanceof z.ZodArray) {
    return { type: "array", items: zodToJsonSchema(schema.element) };
  }
  if (schema instanceof z.ZodEnum) {
    return { type: "string", enum: schema.options };
  }
  if (schema instanceof z.ZodNullable) {
    const inner = zodToJsonSchema(schema.unwrap()) as { type: string };
    return { type: [inner.type, "null"], ...(inner as Record<string, unknown>) };
  }
  if (schema instanceof z.ZodString) return { type: "string" };
  if (schema instanceof z.ZodNumber) return { type: "number" };
  if (schema instanceof z.ZodBoolean) return { type: "boolean" };
  if (schema instanceof z.ZodRecord) {
    return { type: "object", additionalProperties: { type: "string" } };
  }
  return {};
}

async function extractStructured<T>(
  client: Anthropic,
  schema: z.ZodType<T>,
  schemaName: string,
  systemPrompt: string,
  userContent: string
): Promise<T> {
  const stream = client.messages.stream({
    model: MODEL,
    max_tokens: 16000,
    output_config: {
      effort: "medium",
      format: {
        type: "json_schema",
        schema: { name: schemaName, schema: zodToJsonSchema(schema) },
      },
    },
    system: systemPrompt,
    messages: [{ role: "user", content: userContent }],
  });

  const message = await stream.finalMessage();
  if (message.stop_reason === "refusal") {
    throw new Error("The model declined to process this document.");
  }

  const textBlock = message.content.find((b) => b.type === "text");
  if (!textBlock || textBlock.type !== "text") {
    throw new Error("No structured output returned by the model.");
  }

  const parsed = JSON.parse(textBlock.text);
  return schema.parse(parsed);
}

export class ClaudeExtractionProvider implements AIExtractionProvider {
  readonly name = "claude-opus-5";
  private client: Anthropic;

  constructor(apiKey: string) {
    this.client = new Anthropic({ apiKey });
  }

  async extractTest(rawText: string): Promise<TestExtractionResult> {
    return extractStructured(
      this.client,
      testExtractionSchema,
      "sat_test_extraction",
      `You convert raw text extracted from a Digital SAT-style practice test PDF into structured
data. On the real Digital SAT (Bluebook), Reading & Writing questions always show a passage or
stimulus — a paragraph, a student's bulleted research notes, a short sentence with a blank,
whatever the reading material is — separately from a short instructional question ("Which choice
completes the text...", "As used in the text, what does 'X' most nearly mean?", "The student wants
to...Which choice..."). Extracted PDF text usually runs these together as one block: split them.
Put the reading material into a "passages" entry and set the question's "passageIndex" to it; the
question's own "stem" should be ONLY the short instructional question, never the passage text
itself. Do this for every Reading & Writing question that has reading material to separate — most
of them will. Self-contained Math problems (no separate reading passage) don't need this: leave
"passageIndex" null and put the whole problem in "stem". Many source PDFs also print a written
explanation immediately after each question (e.g. "The correct answer is D because...") — when
present, put that explanation text (cleaned up, not the raw OCR line breaks)
into the question's "explanation" field, keep it OUT of the last answer choice's "content", and use
it to determine the correct choice (set that choice's isCorrect true). If no explanation is present,
determine the correct choice from any other source marking (e.g. an answer key) if available, and
leave "explanation" null. Passage "content" is rendered as raw HTML, not plain text — a bare string
with newlines collapses into one run-on block in a browser. When the reading material is a student's
bulleted research notes, emit real markup: an intro line as its own "<p>", each note as its own
"<li>" inside a single "<ul>". When it's a paired passage (a "Text 1" / "Text 2" comparison), label
each with its own "<p><strong>Text 1</strong></p>" before that text's paragraph(s). Otherwise use
plain "<p>" paragraphs — one per distinct paragraph in the source, not one per wrapped line.

Math notation: never write math as plain-text approximations like "x^2", "a/b", "sqrt(x)", or
"3.14...". Bluebook typesets math properly — stacked fractions, true superscript/subscript
exponents, radical signs — and "stem"/"choices[].content"/"problem" must match that. Wrap every
math expression in LaTeX delimiters: \\( ... \\) for anything inline (mixed into a sentence, e.g.
"the value of \\(x^2 + 3x\\)"), \\[ ... \\] for a standalone displayed equation on its own line
(e.g. a system of equations block). Inside the delimiters use standard LaTeX: \\frac{a}{b} for
fractions (never a bare "/"), ^{...} for exponents (x^{2}, not x^2 with no braces — braces matter
whenever the exponent is more than one character), _{...} for subscripts, \\sqrt{...} or
\\sqrt[n]{...} for radicals, \\pi, \\theta, \\times, \\cdot, \\leq, \\geq, \\neq as needed. This
applies to every displayed field: question "stem" (this is where the whole problem goes for
self-contained Math questions too) and every entry in "choices[].content". The one exception is
"correctAnswerFreeResponse" -- that value is compared directly against what a student types into a
grid-in box, so it must stay plain exam-entry format (e.g. "3/4" or "-2.5", never LaTeX). A question with
no math in it at all needs no delimiters — don't wrap plain prose. Guess
the College Board domain/skill category and difficulty if not explicit, and flag whether the
question references an image or table. Set a confidence score (0-1)
per question reflecting how certain you are the extraction is complete and correctly structured —
use lower scores for ambiguous OCR artifacts, missing choices, or unclear question boundaries so a
human can review them before publishing. Never invent question content that is not present in the
source text.`,
      rawText.slice(0, 100_000)
    );
  }

  async extractVocabulary(rawText: string): Promise<VocabExtractionResult> {
    return extractStructured(
      this.client,
      vocabExtractionSchema,
      "sat_vocab_extraction",
      `You convert raw text extracted from an SAT vocabulary list PDF into structured flashcard
data. For each word, extract or infer: part of speech, a clear definition, an example sentence
(write a natural one if the source doesn't include one), synonyms, antonyms, and a difficulty
level appropriate for SAT prep. Set a confidence score (0-1) per word reflecting extraction
certainty.`,
      rawText.slice(0, 100_000)
    );
  }

  async generateExplanation(input: {
    stem: string;
    choices: { label: string; content: string; isCorrect: boolean }[];
    domain: string;
    skill: string;
  }): Promise<ExplanationDraft> {
    return extractStructured(
      this.client,
      explanationSchema,
      "sat_explanation",
      `You write detailed, encouraging explanations for Digital SAT practice questions. Explain why
the correct answer is right, why each incorrect choice is wrong, common mistakes students make on
this type of question, a study tip, and related concepts. Be specific to the question, not generic.
Any math you write (equations, fractions, exponents) must use LaTeX delimiters -- \\( ... \\) inline,
\\[ ... \\] for a standalone equation -- with \\frac{a}{b} for fractions and ^{...} for exponents,
never plain-text "a/b" or "x^2".`,
      JSON.stringify(input)
    );
  }
}
