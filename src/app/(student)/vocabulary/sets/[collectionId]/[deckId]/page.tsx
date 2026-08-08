import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { VocabSetQuiz } from "@/components/vocabulary/vocab-set-quiz";
import { getVocabSetDetail, getVocabSets } from "@/server/actions/student/vocab";
import { passThresholdFor } from "@/lib/vocab-constants";

export const dynamic = "force-dynamic";

export default async function VocabSetDetailPage({
  params,
}: {
  params: { collectionId: string; deckId: string };
}) {
  const [detail, sets] = await Promise.all([
    getVocabSetDetail(params.deckId).catch(() => null),
    getVocabSets(params.collectionId),
  ]);

  if (!detail) notFound();

  const currentIndex = sets.findIndex((s) => s.id === params.deckId);
  const nextSet = sets[currentIndex + 1] ?? null;

  return (
    <div className="space-y-6">
      <div>
        <Link
          href={`/vocabulary/sets/${params.collectionId}`}
          className="inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground"
        >
          <ArrowLeft className="h-3.5 w-3.5" /> All sets
        </Link>
        <div className="mt-2 flex items-center gap-3">
          <h1 className="font-display text-2xl font-semibold tracking-tight">{detail.name}</h1>
          {detail.passed && <Badge variant="success">Completed</Badge>}
        </div>
      </div>

      <Tabs defaultValue="learn">
        <TabsList>
          <TabsTrigger value="learn">Learn</TabsTrigger>
          <TabsTrigger value="read">Read</TabsTrigger>
          <TabsTrigger value="quiz">Quiz</TabsTrigger>
        </TabsList>

        <TabsContent value="learn" className="space-y-3 pt-4">
          {detail.words.map((w, i) => (
            <Card key={w.id}>
              <CardContent className="p-5">
                <div className="flex items-baseline gap-2">
                  <span className="text-xs text-muted-foreground">{i + 1}.</span>
                  <p className="font-display text-lg font-semibold">{w.term}</p>
                </div>
                <p className="mt-1 text-sm">{w.definition}</p>
                {w.example && <p className="mt-2 text-sm italic text-muted-foreground">&ldquo;{w.example}&rdquo;</p>}
                {w.antonym && (
                  <p className="mt-2 text-xs text-muted-foreground">
                    <span className="font-medium">Antonym:</span> {w.antonym}
                  </p>
                )}
              </CardContent>
            </Card>
          ))}
        </TabsContent>

        <TabsContent value="read" className="pt-4">
          <Card>
            <CardContent className="space-y-4 p-8">
              {detail.passageTitle && (
                <h2 className="font-display text-xl font-semibold">{detail.passageTitle}</h2>
              )}
              {detail.passage ? (
                <div className="space-y-4 text-sm leading-relaxed text-foreground">
                  {detail.passage.split("\n\n").map((para, i) => (
                    <p key={i}>{para}</p>
                  ))}
                </div>
              ) : (
                <p className="text-sm text-muted-foreground">No passage available for this set.</p>
              )}
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="quiz" className="pt-4">
          {detail.quiz.length === 0 ? (
            <p className="text-sm text-muted-foreground">
              This set&apos;s quiz isn&apos;t available yet.
            </p>
          ) : (
            <VocabSetQuiz
              deckId={detail.id}
              nextSetHref={nextSet ? `/vocabulary/sets/${params.collectionId}/${nextSet.id}` : null}
              setsListHref={`/vocabulary/sets/${params.collectionId}`}
              questions={detail.quiz}
              passThreshold={passThresholdFor(detail.quiz.length)}
            />
          )}
        </TabsContent>
      </Tabs>
    </div>
  );
}
