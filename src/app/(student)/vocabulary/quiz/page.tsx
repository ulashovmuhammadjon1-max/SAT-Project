import { VocabQuiz } from "@/components/vocabulary/vocab-quiz";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "Vocabulary Quiz" };
export const dynamic = "force-dynamic";

export default async function VocabularyQuizPage() {
  const words = await prisma.vocabWord.findMany({ take: 60, orderBy: { createdAt: "asc" } });

  if (words.length < 4) {
    return (
      <div className="py-24 text-center text-sm text-muted-foreground">
        At least 4 vocabulary words are needed to generate a quiz. Ask an admin to publish more vocabulary.
      </div>
    );
  }

  const shuffled = [...words].sort(() => Math.random() - 0.5).slice(0, 10);

  const questions = shuffled.map((word) => {
    const distractors = words
      .filter((w) => w.id !== word.id)
      .sort(() => Math.random() - 0.5)
      .slice(0, 3);
    const options = [word, ...distractors].sort(() => Math.random() - 0.5).map((w) => ({ id: w.id, definition: w.definition }));
    return { id: word.id, term: word.term, correctId: word.id, options };
  });

  return <VocabQuiz questions={questions} />;
}
