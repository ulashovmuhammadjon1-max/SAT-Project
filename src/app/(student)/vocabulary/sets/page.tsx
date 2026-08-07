import Link from "next/link";
import { CheckCircle2, Lock } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { getVocabSets } from "@/server/actions/student/vocab";
import { VOCAB_SET_PASS_THRESHOLD } from "@/lib/vocab-constants";

export const metadata = { title: "Vocab Sets" };
export const dynamic = "force-dynamic";

export default async function VocabSetsPage() {
  const sets = await getVocabSets();

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Vocab Sets</h1>
        <p className="text-sm text-muted-foreground">
          25 words, a passage, and a 10-question quiz per set. Score {VOCAB_SET_PASS_THRESHOLD}/10 or higher to
          unlock the next set.
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
                  <p className="text-sm text-muted-foreground">{set.wordCount} words</p>
                  {set.attempts > 0 && (
                    <p className="mt-1 text-xs text-muted-foreground">
                      Best score: {set.bestScore}/10
                    </p>
                  )}
                </div>
                {set.passed ? (
                  <Badge variant="success" className="gap-1">
                    <CheckCircle2 className="h-3.5 w-3.5" /> Completed
                  </Badge>
                ) : set.unlocked ? (
                  <Badge variant="outline">Unlocked</Badge>
                ) : (
                  <Badge variant="secondary" className="gap-1">
                    <Lock className="h-3.5 w-3.5" /> Locked
                  </Badge>
                )}
              </CardContent>
            </Card>
          );

          return set.unlocked ? (
            <Link key={set.id} href={`/vocabulary/sets/${set.id}`}>
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
