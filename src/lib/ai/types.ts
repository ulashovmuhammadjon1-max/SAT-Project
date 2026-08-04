// Shared contract between the PDF ingestion pipeline and any AI extraction
// provider (heuristic fallback or a real LLM). Keeping this provider-agnostic
// is what lets the pipeline run with no API key configured and upgrade to a
// real model later by only swapping `getExtractionProvider()`.

export interface ExtractedChoice {
  label: string; // "A" | "B" | "C" | "D"
  content: string;
  isCorrect: boolean;
}

export interface ExtractedQuestion {
  number: number;
  stem: string;
  passageIndex?: number | null; // index into ExtractedPassage[] this question belongs to
  type: "MULTIPLE_CHOICE" | "FREE_RESPONSE";
  choices: ExtractedChoice[];
  correctAnswerFreeResponse?: string | null;
  explanation?: string;
  domainGuess?: string;
  skillGuess?: string;
  // Set once an admin confirms/overrides the taxonomy in the review UI; takes
  // priority over domainGuess/skillGuess text-matching at publish time.
  domainId?: string | null;
  skillId?: string | null;
  difficultyGuess: "EASY" | "MEDIUM" | "HARD";
  hasImage: boolean;
  hasTable: boolean;
  confidence: number; // 0-1
}

export interface ExtractedPassage {
  title?: string | null;
  content: string;
}

export interface TestExtractionResult {
  passages: ExtractedPassage[];
  questions: ExtractedQuestion[];
  overallConfidence: number;
  warnings: string[];
}

export interface ExtractedVocabWord {
  term: string;
  partOfSpeech?: string | null;
  definition: string;
  exampleSentence?: string | null;
  synonyms: string[];
  antonyms: string[];
  difficultyGuess: "EASY" | "MEDIUM" | "HARD";
  confidence: number;
}

export interface VocabExtractionResult {
  words: ExtractedVocabWord[];
  overallConfidence: number;
  warnings: string[];
}

export interface ExplanationDraft {
  content: string;
  whyCorrect: string;
  whyWrongJson: Record<string, string>;
  commonMistakes: string;
  tips: string;
  relatedConcepts: string;
}

export interface AIExtractionProvider {
  readonly name: string;
  extractTest(rawText: string): Promise<TestExtractionResult>;
  extractVocabulary(rawText: string): Promise<VocabExtractionResult>;
  generateExplanation(input: {
    stem: string;
    choices: { label: string; content: string; isCorrect: boolean }[];
    domain: string;
    skill: string;
  }): Promise<ExplanationDraft>;
}
