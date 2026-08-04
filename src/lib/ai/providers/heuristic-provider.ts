import type {
  AIExtractionProvider,
  ExplanationDraft,
  ExtractedChoice,
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
const CHOICE_LINE = /(?:^|\n)\s*\(?([A-D])\)[.)]?\s+(.+?)(?=\n\s*\(?[A-D]\)?[.)]|\n\s*\d{1,3}[.)]|\n\n|$)/gs;

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

function extractChoices(block: string): { choices: ExtractedChoice[]; stem: string } {
  const choices: ExtractedChoice[] = [];
  let firstChoiceIndex = block.length;

  for (const match of block.matchAll(CHOICE_LINE)) {
    const label = match[1];
    const content = match[2].trim();
    if (!content) continue;
    firstChoiceIndex = Math.min(firstChoiceIndex, match.index ?? block.length);
    choices.push({ label, content, isCorrect: false });
  }

  const stem = block.slice(0, firstChoiceIndex).trim();
  return { choices, stem };
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

    const questions: ExtractedQuestion[] = blocks.map(({ number, block }) => {
      const { choices, stem } = extractChoices(block);
      const hasFourChoices = choices.length === 4;
      const hasImageHint = /\b(figure|graph|diagram|chart|see image)\b/i.test(block);
      const hasTableHint = /\btable\b/i.test(block) && /\|/.test(block);

      // Heuristic confidence: a clean 4-choice MCQ with a non-trivial stem
      // scores well; anything irregular is pushed down for manual review.
      let confidence = 0.4;
      if (hasFourChoices) confidence += 0.35;
      if (stem.length > 20) confidence += 0.15;
      if (choices.every((c) => c.content.length > 1)) confidence += 0.1;
      confidence = Math.min(confidence, hasFourChoices ? 0.85 : 0.55);

      return {
        number,
        stem: stem || block.slice(0, 200),
        type: "MULTIPLE_CHOICE",
        choices,
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

    return { passages: [], questions, overallConfidence, warnings };
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
