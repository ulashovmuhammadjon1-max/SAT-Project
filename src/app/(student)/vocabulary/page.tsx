import Link from "next/link";
import { Brain, ListChecks, Sparkles } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { AddWordDialog } from "@/components/vocabulary/add-word-dialog";
import { MyWordsList } from "@/components/vocabulary/my-words-list";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Vocabulary" };
export const dynamic = "force-dynamic";

export default async function VocabularyPage() {
  const user = await requireUser();

  const [totalWords, progress, dueCount, myWords] = await Promise.all([
    prisma.vocabWord.count({ where: { OR: [{ visibility: "PUBLIC" }, { createdById: user.id }] } }),
    prisma.vocabProgress.findMany({ where: { userId: user.id } }),
    prisma.vocabProgress.count({ where: { userId: user.id, nextReviewAt: { lte: new Date() } } }),
    prisma.vocabWord.findMany({
      where: { createdById: user.id, visibility: "PRIVATE" },
      orderBy: { createdAt: "desc" },
      select: { id: true, term: true, definition: true },
    }),
  ]);

  const mastered = progress.filter((p) => p.status === "MASTERED").length;
  const learning = progress.filter((p) => p.status === "LEARNING").length;
  const notStarted = totalWords - progress.length;

  return (
    <div className="space-y-8">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">Vocabulary</h1>
          <p className="text-sm text-muted-foreground">Build your word bank with spaced repetition.</p>
        </div>
        <AddWordDialog />
      </div>

      <div className="grid gap-4 sm:grid-cols-4">
        <Card>
          <CardContent className="p-5">
            <p className="font-display text-2xl font-semibold">{totalWords}</p>
            <p className="text-xs text-muted-foreground">Total words</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-5">
            <p className="font-display text-2xl font-semibold text-success">{mastered}</p>
            <p className="text-xs text-muted-foreground">Mastered</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-5">
            <p className="font-display text-2xl font-semibold text-primary">{learning}</p>
            <p className="text-xs text-muted-foreground">Learning</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-5">
            <p className="font-display text-2xl font-semibold">{notStarted}</p>
            <p className="text-xs text-muted-foreground">Not started</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-4 sm:grid-cols-3">
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base">
              <Brain className="h-4 w-4" /> Learn
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <p className="text-sm text-muted-foreground">
              Flashcards with spaced repetition. {dueCount} words due today.
            </p>
            <Button asChild className="w-full">
              <Link href="/vocabulary/learn">Start learning</Link>
            </Button>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base">
              <ListChecks className="h-4 w-4" /> Quiz mode
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <p className="text-sm text-muted-foreground">Multiple-choice quiz to test recall under pressure.</p>
            <Button asChild variant="outline" className="w-full">
              <Link href="/vocabulary/quiz">Start quiz</Link>
            </Button>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base">
              <Sparkles className="h-4 w-4" /> Practice mode
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <p className="text-sm text-muted-foreground">Untimed review of every word, no scoring pressure.</p>
            <Button asChild variant="outline" className="w-full">
              <Link href="/vocabulary/learn?mode=practice">Browse all words</Link>
            </Button>
          </CardContent>
        </Card>
      </div>

      {myWords.length > 0 && (
        <div className="space-y-3">
          <h2 className="font-display text-lg font-semibold">Your words</h2>
          <p className="-mt-2 text-sm text-muted-foreground">
            Words you added yourself — only visible to you, already in your flashcard and quiz rotation.
          </p>
          <MyWordsList words={myWords} />
        </div>
      )}
    </div>
  );
}
