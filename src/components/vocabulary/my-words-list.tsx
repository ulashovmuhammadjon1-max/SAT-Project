"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Trash2 } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { deletePersonalWord } from "@/server/actions/student/vocab";

export function MyWordsList({ words }: { words: { id: string; term: string; definition: string }[] }) {
  const router = useRouter();

  return (
    <div className="space-y-2">
      {words.map((word) => (
        <WordRow key={word.id} word={word} onDeleted={() => router.refresh()} />
      ))}
    </div>
  );
}

function WordRow({
  word,
  onDeleted,
}: {
  word: { id: string; term: string; definition: string };
  onDeleted: () => void;
}) {
  const [isDeleting, startDelete] = useTransition();

  function remove() {
    startDelete(async () => {
      await deletePersonalWord(word.id);
      onDeleted();
    });
  }

  return (
    <Card>
      <CardContent className="flex items-center justify-between gap-3 p-3">
        <div className="min-w-0">
          <p className="flex items-center gap-2 text-sm font-medium">
            {word.term} <Badge variant="outline">Personal</Badge>
          </p>
          <p className="line-clamp-1 text-xs text-muted-foreground">{word.definition}</p>
        </div>
        <Button variant="ghost" size="icon" onClick={remove} disabled={isDeleting}>
          {isDeleting ? <Loader2 className="h-4 w-4 animate-spin" /> : <Trash2 className="h-4 w-4 text-destructive" />}
        </Button>
      </CardContent>
    </Card>
  );
}
