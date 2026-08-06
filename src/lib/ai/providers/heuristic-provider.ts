import { splitPassageFromStem } from "@/lib/ai/passage-split";
import type {
  AIExtractionProvider,
  ExplanationDraft,
  ExtractedChoice,
  ExtractedPassage,
  ExtractedQuestion,
  TestExtractionResult,
  VocabExtractionResult,
} from "@/lib/ai/types";

// Regex-based extraction that requires no API key. It is intentionally
// conservative: anything it isn't confident about gets a low confidence
// score so the admin review queue catches it before publishing. This is
// the default provider until ANTHROPIC_API_KEY is configured, at which
// point `getExtractionProvider()` swaps in the Claude provider.

const QUESTION_START = /(?:^|\n)\s*(\d{1,3})[.)]\s+/g;
// Matches "(A)", "A)", or "A." as a choice marker — deliberately NOT anchored
// to a line start, since PDF text extraction frequently runs all four choices
// together on one wrapped line/paragraph instead of one-per-line.
const CHOICE_MARKER = /\(?([A-D])\)[.)]?\s+/g;

// Phrases that typically introduce an answer explanation in mock-test PDFs,
// so it can be split out of the last choice's text instead of being treated
// as part of the answer content. Not anchored to a word boundary at the
// start: PDF text extraction often drops the space between the last choice
// and the explanation sentence (e.g. "...imposingThe correct option is D").
const EXPLANATION_LEAD_IN =
  /(?:the\s+correct\s+(?:answer|option|choice)\s+is\s+([A-D])\b[^.]*?(?:because|since|as)?|correct\s+answer\s*:?\s*([A-D])\b|explanation\s*:)/i;

function splitIntoQuestionBlocks(text: string): { number: number; block: string }[] {
  const matches = [...text.matchAll(QUESTION_START)];
  const blocks: { number: number; block: string }[] = [];

  for (let i = 0; i < matches.length; i++) {
    const match = matches[i];
    const start = (match.index ?? 0) + match[0].length;
    const end = matches[i + 1]?.index ?? text.length;
    blocks.push({ number: Number(match[1]), block: text.slice(start, end).trim() });
  }

  return blocks;
}

function extractChoices(
  block: string
): { choices: ExtractedChoice[]; stem: string; explanation?: string } {
  // Find every (A)/(B)/(C)/(D) marker in document order, but only keep the
  // sequence while each next letter is exactly the one that should follow —
  // this rejects a stray "(A)" appearing again inside explanation prose
  // after the real four choices have already been found.
  const markers: { label: string; index: number; end: number }[] = [];
  let expected = 0; // index into "ABCD"
  for (const match of block.matchAll(CHOICE_MARKER)) {
    if (expected >= 4) break;
    const label = match[1];
    if (label !== "ABCD"[expected]) continue;
    markers.push({ label, index: match.index ?? 0, end: (match.index ?? 0) + match[0].length });
    expected += 1;
  }

  if (markers.length === 0) {
    return { choices: [], stem: block };
  }

  const stem = block.slice(0, markers[0].index).trim();
  const choices: ExtractedChoice[] = [];
  let explanation: string | undefined;

  for (let i = 0; i < markers.length; i++) {
    const contentStart = markers[i].end;
    const contentEnd = markers[i + 1]?.index ?? block.length;
    let content = block.slice(contentStart, contentEnd).trim();

    // Only the last choice can run into trailing explanation prose.
    if (i === markers.length - 1) {
      const leadIn = content.match(EXPLANATION_LEAD_IN);
      if (leadIn && leadIn.index !== undefined) {
        explanation = content.slice(leadIn.index).trim();
        content = content.slice(0, leadIn.index).trim();
      }
    }

    if (content) choices.push({ label: markers[i].label, content, isCorrect: false });
  }

  if (explanation) {
    const correctLetter = (explanation.match(EXPLANATION_LEAD_IN)?.[1] ?? explanation.match(EXPLANATION_LEAD_IN)?.[2])?.toUpperCase();
    if (correctLetter) {
      const correctChoice = choices.find((c) => c.label === correctLetter);
      if (correctChoice) correctChoice.isCorrect = true;
    }
  }

  return { choices, stem, explanation };
}

// Best-effort, conservative plain-text-math -> LaTeX conversion for the
// no-API-key fallback path. Only touches patterns that are unambiguous out
// of context (an exponent right after a variable/number, an explicit
// "sqrt(...)" call) — it deliberately leaves bare "/" alone, since a slash
// in freeform extracted text is just as likely to be a date or a ratio in
// prose as an actual fraction, and a wrong guess there is worse than no
// conversion. Extraction confidence already accounts for this path needing
// a human pass, so this is a partial improvement, not a full fix.
const EXPONENT = /([A-Za-z0-9)\]])\^(\(-?[^()]+\)|-?\d+(?:\.\d+)?|[A-Za-z])/g;
const SQRT_CALL = /\bsqrt\(([^()]+)\)/gi;

function mathify(text: string): string {
  if (!text) return text;
  let out = text.replace(SQRT_CALL, (_m, radicand: string) => `\\(\\sqrt{${radicand.trim()}}\\)`);
  out = out.replace(EXPONENT, (_m, base: string, exp: string) => {
    const cleanExp = exp.startsWith("(") && exp.endsWith(")") ? exp.slice(1, -1) : exp;
    return `\\(${base}^{${cleanExp}}\\)`;
  });
  return out;
}

function guessDifficulty(stem: string): "EASY" | "MEDIUM" | "HARD" {
  const words = stem.split(/\s+/).length;
  if (words < 25) return "EASY";
  if (words < 60) return "MEDIUM";
  return "HARD";
}

export class HeuristicExtractionProvider implements AIExtractionProvider {
  readonly name = "heuristic";

  async extractTest(rawText: string): Promise<TestExtractionResult> {
    const warnings: string[] = [];
    const blocks = splitIntoQuestionBlocks(rawText);

    if (blocks.length === 0) {
      warnings.push("No numbered questions were detected. Manual entry is required.");
    }

    const passages: ExtractedPassage[] = [];

    const questions: ExtractedQuestion[] = blocks.map(({ number, block }) => {
      const extracted = extractChoices(block);
      const choices = extracted.choices.map((c) => ({ ...c, content: mathify(c.content) }));
      const rawStem = mathify(extracted.stem);
      const explanation = extracted.explanation ? mathify(extracted.explanation) : extracted.explanation;
      const hasFourChoices = choices.length === 4;
      const hasKnownAnswer = choices.some((c) => c.isCorrect);
      const hasImageHint = /\b(figure|graph|diagram|chart|see image)\b/i.test(block);
      const hasTableHint = /\btable\b/i.test(block) && /\|/.test(block);

      // Real Digital SAT R&W questions always show a passage/stimulus
      // separately from the instructional question — never merged into one
      // block of text. Plain-text extraction loses that visual split, so
      // recover it here: if the stem looks like "<reading material> <actual
      // question>?", split off the reading material as its own passage.
      let stem = rawStem;
      let passageIndex: number | undefined;
      const split = splitPassageFromStem(rawStem);
      if (split) {
        passageIndex = passages.length;
        passages.push({ content: split.passage });
        stem = split.stem;
      }

      // Heuristic confidence: a clean 4-choice MCQ with a non-trivial stem
      // scores well; anything irregular is pushed down for manual review.
      let confidence = 0.4;
      if (hasFourChoices) confidence += 0.3;
      if (stem.length > 20) confidence += 0.15;
      if (choices.every((c) => c.content.length > 1)) confidence += 0.1;
      if (hasKnownAnswer) confidence += 0.1;
      confidence = Math.min(confidence, hasFourChoices ? (hasKnownAnswer ? 0.95 : 0.85) : 0.55);

      return {
        number,
        stem: stem || block.slice(0, 200),
        passageIndex,
        type: "MULTIPLE_CHOICE",
        choices,
        explanation,
        difficultyGuess: guessDifficulty(stem),
        hasImage: hasImageHint,
        hasTable: hasTableHint,
        confidence,
      };
    });

    const overallConfidence = questions.length
      ? questions.reduce((sum, q) => sum + q.confidence, 0) / questions.length
      : 0;

    if (overallConfidence < 0.7) {
      warnings.push(
        "Extraction confidence is low. Configure ANTHROPIC_API_KEY to enable AI-assisted extraction, or correct questions manually before publishing."
      );
    }

    return { passages, questions, overallConfidence, warnings };
  }

  async extractVocabulary(rawText: string): Promise<VocabExtractionResult> {
    const warnings: string[] = [];
    // Common vocab-list export shape: "term - definition" or "term: definition" per line.
    const lines = rawText
      .split("\n")
      .map((l) => l.trim())
      .filter(Boolean);

    const words = lines
      .map((line) => {
        const match = line.match(/^([A-Za-z][A-Za-z\-' ]{1,30})\s*[-:–]\s*(.+)$/);
        if (!match) return null;
        const term = match[1].trim();
        const definition = match[2].trim();
        if (term.split(" ").length > 3 || definition.length < 3) return null;
        return {
          term,
          definition,
          synonyms: [] as string[],
          antonyms: [] as string[],
          difficultyGuess: (definition.length > 60 ? "HARD" : "MEDIUM") as "EASY" | "MEDIUM" | "HARD",
          confidence: 0.55,
        };
      })
      .filter((w): w is NonNullable<typeof w> => w !== null);

    if (words.length === 0) {
      warnings.push("No 'term - definition' pairs were detected. Manual entry is required.");
    } else {
      warnings.push(
        "Parsed with plain-text heuristics only — synonyms, antonyms, and examples were not extracted. Configure ANTHROPIC_API_KEY for full extraction."
      );
    }

    return {
      words,
      overallConfidence: words.length ? 0.55 : 0,
      warnings,
    };
  }

  async generateExplanation(input: {
    stem: string;
    choices: { label: string; content: string; isCorrect: boolean }[];
    domain: string;
    skill: string;
  }): Promise<ExplanationDraft> {
    const correct = input.choices.find((c) => c.isCorrect);
    return {
      content: `Choice ${correct?.label ?? "?"} is correct. Configure ANTHROPIC_API_KEY to generate a full explanation automatically, or write one manually.`,
      whyCorrect: correct ? `${correct.label}: ${correct.content}` : "",
      whyWrongJson: Object.fromEntries(
        input.choices.filter((c) => !c.isCorrect).map((c) => [c.label, "Draft explanation pending."])
      ),
      commonMistakes: "",
      tips: "",
      relatedConcepts: `${input.domain} — ${input.skill}`,
    };
  }
}
