import { FlashcardDeck } from "@/components/vocabulary/flashcard-deck";
import { getDueWords } from "@/server/actions/student/vocab";

export const metadata = { title: "Learn Vocabulary" };
export const dynamic = "force-dynamic";

export default async function VocabularyLearnPage() {
  const words = await getDueWords(20);

  return (
    <FlashcardDeck
      words={words.map((w) => ({
        id: w.id,
        term: w.term,
        partOfSpeech: w.partOfSpeech,
        definition: w.definition,
        exampleSentence: w.exampleSentence,
        synonyms: (w.synonyms as string[] | null) ?? [],
        antonyms: (w.antonyms as string[] | null) ?? [],
      }))}
    />
  );
}
