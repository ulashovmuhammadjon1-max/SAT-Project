"use client";

import { useState, useTransition } from "react";
import Link from "next/link";
import { CheckCircle2, PartyPopper, RotateCcw, XCircle } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { cn } from "@/lib/utils";
import { submitVocabSetQuiz } from "@/server/actions/student/vocab";

interface QuizQuestion {
  id: string;
  order: number;
  stem: string;
  choices: { A: string; B: string; C: string; D: string };
}

export function VocabSetQuiz({
  deckId,
  nextSetId,
  questions,
  passThreshold,
}: {
  deckId: string;
  nextSetId: string | null;
  questions: QuizQuestion[];
  passThreshold: number;
}) {
  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, "A" | "B" | "C" | "D">>({});
  const [result, setResult] = useState<Awaited<ReturnType<typeof submitVocabSetQuiz>> | null>(null);
  const [isPending, startTransition] = useTransition();

  const question = questions[index];
  const CHOICE_KEYS = ["A", "B", "C", "D"] as const;

  function choose(letter: "A" | "B" | "C" | "D") {
    setAnswers((a) => ({ ...a, [question.id]: letter }));
  }

  function next() {
    if (index < questions.length - 1) {
      setIndex((i) => i + 1);
      return;
    }
    startTransition(async () => {
      const res = await submitVocabSetQuiz(deckId, answers);
      setResult(res);
    });
  }

  function retry() {
    setResult(null);
    setAnswers({});
    setIndex(0);
  }

  if (result) {
    return (
      <div className="flex flex-col items-center gap-4 py-16 text-center">
        {result.passed ? (
          <PartyPopper className="h-10 w-10 text-primary" />
        ) : (
          <XCircle className="h-10 w-10 text-muted-foreground" />
        )}
        <p className="font-display text-2xl font-semibold">
          {result.score} / {result.total} correct
        </p>
        <p className="text-sm text-muted-foreground">
          {result.passed
            ? "Passed! The next set is now unlocked."
            : `You need ${result.passThreshold}/${result.total} to unlock the next set.`}
        </p>
        <div className="flex gap-2">
          {!result.passed && (
            <Button variant="outline" onClick={retry} className="gap-1.5">
              <RotateCcw className="h-4 w-4" /> Try again
            </Button>
          )}
          {result.passed && nextSetId ? (
            <Button asChild>
              <Link href={`/vocabulary/sets/${nextSetId}`}>Next set</Link>
            </Button>
          ) : (
            <Button asChild variant={result.passed ? "default" : "outline"}>
              <Link href="/vocabulary/sets">Back to sets</Link>
            </Button>
          )}
        </div>
      </div>
    );
  }

  const selected = answers[question.id];

  return (
    <div className="mx-auto max-w-xl space-y-6">
      <div className="space-y-2">
        <div className="flex items-center justify-between text-sm text-muted-foreground">
          <span>
            Question {index + 1} / {questions.length}
          </span>
        </div>
        <Progress value={(index / questions.length) * 100} />
      </div>

      <Card>
        <CardContent className="space-y-5 p-8">
          <p className="text-base leading-relaxed">{question.stem}</p>
          <div className="space-y-2">
            {CHOICE_KEYS.map((key) => {
              const isSelected = selected === key;
              return (
                <button
                  key={key}
                  onClick={() => choose(key)}
                  className={cn(
                    "flex w-full items-center gap-3 rounded-lg border p-3 text-left text-sm transition-colors",
                    isSelected ? "border-primary bg-primary/5" : "hover:bg-secondary"
                  )}
                >
                  <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full border text-xs">
                    {key}
                  </span>
                  <span>{question.choices[key]}</span>
                  {isSelected && <CheckCircle2 className="ml-auto h-4 w-4 shrink-0 text-primary" />}
                </button>
              );
            })}
          </div>
          <Button className="w-full" disabled={!selected || isPending} onClick={next}>
            {isPending ? "Submitting..." : index === questions.length - 1 ? "Submit quiz" : "Next question"}
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}
