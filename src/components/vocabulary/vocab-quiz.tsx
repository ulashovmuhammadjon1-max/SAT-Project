"use client";

import { useState, useTransition } from "react";
import Link from "next/link";
import { Check, PartyPopper, X } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { cn } from "@/lib/utils";
import { reviewWord } from "@/server/actions/student/vocab";

interface QuizQuestion {
  id: string;
  term: string;
  correctId: string;
  options: { id: string; definition: string }[];
}

export function VocabQuiz({ questions }: { questions: QuizQuestion[] }) {
  const [index, setIndex] = useState(0);
  const [selected, setSelected] = useState<string | null>(null);
  const [score, setScore] = useState(0);
  const [isPending, startTransition] = useTransition();

  const question = questions[index];

  function choose(optionId: string) {
    if (selected) return;
    setSelected(optionId);
    const correct = optionId === question.correctId;
    if (correct) setScore((s) => s + 1);
    startTransition(() => reviewWord(question.id, correct ? 4 : 1));
  }

  function next() {
    setSelected(null);
    setIndex((i) => i + 1);
  }

  if (index >= questions.length) {
    const pct = Math.round((score / questions.length) * 100);
    return (
      <div className="flex flex-col items-center gap-4 py-24 text-center">
        <PartyPopper className="h-10 w-10 text-primary" />
        <p className="font-display text-2xl font-semibold">
          {score} / {questions.length} correct ({pct}%)
        </p>
        <Button asChild>
          <Link href="/vocabulary">Back to vocabulary</Link>
        </Button>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-xl space-y-6">
      <div className="space-y-2">
        <div className="flex items-center justify-between text-sm text-muted-foreground">
          <span>
            {index + 1} / {questions.length}
          </span>
          <span>Score: {score}</span>
        </div>
        <Progress value={(index / questions.length) * 100} />
      </div>

      <Card>
        <CardContent className="space-y-5 p-8">
          <p className="text-center font-display text-2xl font-semibold">{question.term}</p>
          <p className="text-center text-sm text-muted-foreground">Choose the correct definition</p>
          <div className="space-y-2">
            {question.options.map((opt) => {
              const isCorrectOpt = opt.id === question.correctId;
              const isSelected = selected === opt.id;
              return (
                <button
                  key={opt.id}
                  onClick={() => choose(opt.id)}
                  disabled={!!selected || isPending}
                  className={cn(
                    "flex w-full items-center justify-between gap-3 rounded-lg border p-3 text-left text-sm transition-colors",
                    selected && isCorrectOpt && "border-success bg-success/5",
                    selected && isSelected && !isCorrectOpt && "border-destructive bg-destructive/5",
                    !selected && "hover:bg-secondary"
                  )}
                >
                  <span>{opt.definition}</span>
                  {selected && isCorrectOpt && <Check className="h-4 w-4 shrink-0 text-success" />}
                  {selected && isSelected && !isCorrectOpt && <X className="h-4 w-4 shrink-0 text-destructive" />}
                </button>
              );
            })}
          </div>
          {selected && (
            <Button className="w-full" onClick={next}>
              {index === questions.length - 1 ? "See results" : "Next word"}
            </Button>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
