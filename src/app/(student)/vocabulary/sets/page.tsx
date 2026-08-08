import Link from "next/link";
import { BookOpen, CheckCircle2 } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { getVocabCollections } from "@/server/actions/student/vocab";

export const metadata = { title: "Vocab Sets" };
export const dynamic = "force-dynamic";

export default async function VocabCollectionsPage() {
  const collections = await getVocabCollections();

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Vocab Sets</h1>
        <p className="text-sm text-muted-foreground">
          Pick a book to start working through its sets in order.
        </p>
      </div>

      {collections.length === 0 ? (
        <p className="text-sm text-muted-foreground">No vocab collections yet.</p>
      ) : (
        <div className="grid gap-3 sm:grid-cols-2">
          {collections.map((c) => {
            const complete = c.setsCompleted === c.setCount && c.setCount > 0;
            return (
              <Link key={c.id} href={`/vocabulary/sets/${c.id}`}>
                <Card className="transition-shadow hover:shadow-md">
                  <CardContent className="flex items-center justify-between gap-4 p-5">
                    <div>
                      <div className="flex items-center gap-2">
                        <BookOpen className="h-4 w-4 text-muted-foreground" />
                        <p className="font-display text-lg font-semibold">{c.name}</p>
                      </div>
                      {c.description && (
                        <p className="mt-1 text-sm text-muted-foreground">{c.description}</p>
                      )}
                      <p className="mt-1 text-xs text-muted-foreground">
                        {c.setsCompleted} / {c.setCount} sets completed
                      </p>
                    </div>
                    {complete && (
                      <Badge variant="success" className="gap-1 shrink-0">
                        <CheckCircle2 className="h-3.5 w-3.5" /> Done
                      </Badge>
                    )}
                  </CardContent>
                </Card>
              </Link>
            );
          })}
        </div>
      )}
    </div>
  );
}
