import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, CheckCircle2, Lock } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { getVocabSets } from "@/server/actions/student/vocab";

export const dynamic = "force-dynamic";

export default async function VocabCollectionSetsPage({ params }: { params: { collectionId: string } }) {
  const collection = await prisma.vocabCollection.findUnique({ where: { id: params.collectionId } });
  if (!collection) notFound();

  const sets = await getVocabSets(params.collectionId);

  return (
    <div className="space-y-8">
      <div>
        <Link
          href="/vocabulary/sets"
          className="inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground"
        >
          <ArrowLeft className="h-3.5 w-3.5" /> All books
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold tracking-tight">{collection.name}</h1>
        <p className="text-sm text-muted-foreground">
          25 words, a passage, and a quiz per set. Score 80% or higher to unlock the next set.
        </p>
      </div>

      <div className="grid gap-3 sm:grid-cols-2">
        {sets.map((set) => {
          const content = (
            <Card
              className={
                set.unlocked
                  ? "transition-shadow hover:shadow-md"
                  : "cursor-not-allowed opacity-60"
              }
            >
              <CardContent className="flex items-center justify-between gap-4 p-5">
                <div>
                  <p className="font-display text-lg font-semibold">{set.name}</p>
                  <p className="text-sm text-muted-foreground">
                    {set.wordCount} words{set.quizCount < 10 && ` · quiz incomplete (${set.quizCount}/10)`}
                  </p>
                  {set.attempts > 0 && (
                    <p className="mt-1 text-xs text-muted-foreground">
                      Best score: {set.bestScore}/{set.quizCount}
                    </p>
                  )}
                </div>
                {set.passed ? (
                  <Badge variant="success" className="gap-1 shrink-0">
                    <CheckCircle2 className="h-3.5 w-3.5" /> Completed
                  </Badge>
                ) : set.unlocked ? (
                  <Badge variant="outline" className="shrink-0">
                    Unlocked
                  </Badge>
                ) : (
                  <Badge variant="secondary" className="gap-1 shrink-0">
                    <Lock className="h-3.5 w-3.5" /> Locked
                  </Badge>
                )}
              </CardContent>
            </Card>
          );

          return set.unlocked ? (
            <Link key={set.id} href={`/vocabulary/sets/${params.collectionId}/${set.id}`}>
              {content}
            </Link>
          ) : (
            <div key={set.id}>{content}</div>
          );
        })}
      </div>
    </div>
  );
}
