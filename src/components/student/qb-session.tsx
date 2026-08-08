"use client";

import { useState, useTransition } from "react";
import Link from "next/link";
import { Bookmark, Check, Loader2, X } from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Progress } from "@/components/ui/progress";
import { MathContent } from "@/components/shared/math-content";
import { cn } from "@/lib/utils";
import { toggleBookmark } from "@/server/actions/student/bookmarks";
import {
  submitQuestionAnswer,
  type SubmitAnswerResult,
} from "@/server/actions/student/question-bank";

export interface SessionQuestion {
  id: string;
  ref: string;
  type: "MULTIPLE_CHOICE" | "FREE_RESPONSE";
  difficulty: "EASY" | "MEDIUM" | "HARD";
  domainName: string;
  skillName: string;
  stem: string;
  imageUrl: string | null;
  passage: { title: string | null; content: string; imageUrl: string | null } | null;
  /** No `isCorrect` — the answer key never reaches the client before submission. */
  choices: { id: string; label: string; content: string }[];
  saved: boolean;
}

export function PracticeSession({
  questions,
  backHref,
}: {
  questions: SessionQuestion[];
  backHref: string;
}) {
  const [index, setIndex] = useState(0);
  const [selected, setSelected] = useState<string | null>(null);
  const [freeResponse, setFreeResponse] = useState("");
  const [result, setResult] = useState<SubmitAnswerResult | null>(null);
  const [startedAt, setStartedAt] = useState(() => Date.now());
  const [saved, setSaved] = useState(questions[0]?.saved ?? false);
  const [score, setScore] = useState({ correct: 0, answered: 0 });
  const [isPending, startTransition] = useTransition();
  const [isSaving, startSaving] = useTransition();

  const q = questions[index];
  const isLast = index === questions.length - 1;
  const finished = index >= questions.length;

  function submit() {
    if (!q || result) return;
    const answered = q.type === "FREE_RESPONSE" ? freeResponse.trim() : selected;
    if (!answered) return;

    startTransition(async () => {
      try {
        const res = await submitQuestionAnswer({
          questionId: q.id,
          selectedChoiceId: q.type === "MULTIPLE_CHOICE" ? selected : null,
          freeResponseAnswer: q.type === "FREE_RESPONSE" ? freeResponse.trim() : null,
          timeSpentSeconds: Math.round((Date.now() - startedAt) / 1000),
        });
        setResult(res);
        setScore((s) => ({ correct: s.correct + (res.isCorrect ? 1 : 0), answered: s.answered + 1 }));
      } catch {
        toast.error("Couldn't save that answer. Please try again.");
      }
    });
  }

  function next() {
    const nextIndex = index + 1;
    setIndex(nextIndex);
    setSelected(null);
    setFreeResponse("");
    setResult(null);
    setStartedAt(Date.now());
    setSaved(questions[nextIndex]?.saved ?? false);
  }

  function onToggleSave() {
    if (!q) return;
    const optimistic = !saved;
    setSaved(optimistic);
    startSaving(async () => {
      try {
        await toggleBookmark(q.id);
      } catch {
        setSaved(!optimistic);
        toast.error("Couldn't update saved questions.");
      }
    });
  }

  if (finished) {
    const pct = score.answered ? Math.round((score.correct / score.answered) * 100) : 0;
    return (
      <div className="flex flex-col items-center gap-4 py-20 text-center">
        <p className="font-display text-3xl font-semibold">
          {score.correct} / {score.answered}
        </p>
        <p className="text-sm text-muted-foreground">{pct}% correct in this session.</p>
        <div className="flex flex-wrap justify-center gap-2">
          <Button asChild variant="outline">
            <Link href={backHref}>Back to Question Bank</Link>
          </Button>
          <Button asChild>
            <Link href="/practice/start">Practice more</Link>
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-5">
      <div className="space-y-2">
        <div className="flex items-center justify-between text-sm text-muted-foreground">
          <span>
            Question {index + 1} of {questions.length}
          </span>
          <span className="tabular-nums">
            {score.correct}/{score.answered} correct
          </span>
        </div>
        <Progress value={(index / questions.length) * 100} />
      </div>

      <div className="flex flex-wrap items-center gap-2">
        <Badge variant="outline">{q.ref}</Badge>
        <Badge variant="secondary">{q.skillName}</Badge>
        <Badge variant={q.difficulty === "HARD" ? "destructive" : q.difficulty === "EASY" ? "success" : "warning"}>
          {q.difficulty[0] + q.difficulty.slice(1).toLowerCase()}
        </Badge>
        <Button
          variant="ghost"
          size="sm"
          onClick={onToggleSave}
          disabled={isSaving}
          aria-pressed={saved}
          className="ml-auto"
        >
          <Bookmark className={cn("h-4 w-4", saved && "fill-current text-primary")} />
          {saved ? "Saved" : "Save"}
        </Button>
      </div>

      <div className={cn("grid gap-5", q.passage && "lg:grid-cols-2")}>
        {q.passage && (
          <Card>
            <CardContent className="p-5">
              {q.passage.title && <h2 className="mb-2 font-display font-semibold">{q.passage.title}</h2>}
              <MathContent html={q.passage.content} className="prose-sm max-w-none text-[15px] leading-relaxed" />
              {q.passage.imageUrl && (
                // eslint-disable-next-line @next/next/no-img-element
                <img src={q.passage.imageUrl} alt="" className="mt-3 max-w-full rounded-lg" />
              )}
            </CardContent>
          </Card>
        )}

        <Card>
          <CardContent className="space-y-4 p-5">
            <MathContent html={q.stem} className="text-[15px] leading-relaxed" />
            {q.imageUrl && (
              // eslint-disable-next-line @next/next/no-img-element
              <img src={q.imageUrl} alt="" className="max-w-full rounded-lg" />
            )}

            {q.type === "FREE_RESPONSE" ? (
              <div className="space-y-1.5">
                <Label htmlFor="fr-answer">Your answer</Label>
                <Input
                  id="fr-answer"
                  value={freeResponse}
                  onChange={(e) => setFreeResponse(e.target.value)}
                  disabled={!!result}
                  placeholder="Enter your answer"
                  className="max-w-xs"
                />
              </div>
            ) : (
              <div className="space-y-2" role="radiogroup" aria-label="Answer choices">
                {q.choices.map((c) => {
                  const isPicked = selected === c.id;
                  const isKey = result?.correctChoiceId === c.id;
                  const isWrongPick = !!result && isPicked && !result.isCorrect;
                  return (
                    <button
                      key={c.id}
                      type="button"
                      role="radio"
                      aria-checked={isPicked}
                      disabled={!!result}
                      onClick={() => setSelected(c.id)}
                      className={cn(
                        "flex w-full items-start gap-3 rounded-lg border p-3 text-left text-sm transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
                        result && isKey && "border-success bg-success/5",
                        isWrongPick && "border-destructive bg-destructive/5",
                        !result && isPicked && "border-primary bg-primary/5",
                        !result && !isPicked && "hover:bg-secondary"
                      )}
                    >
                      <span
                        className={cn(
                          "flex h-5 w-5 shrink-0 items-center justify-center rounded-full border text-xs font-medium",
                          isPicked && !result && "border-primary bg-primary text-primary-foreground",
                          result && isKey && "border-success bg-success text-white",
                          isWrongPick && "border-destructive bg-destructive text-white"
                        )}
                      >
                        {c.label}
                      </span>
                      <MathContent html={c.content} className="flex-1" />
                      {result && isKey && <Check className="h-4 w-4 shrink-0 text-success" />}
                      {isWrongPick && <X className="h-4 w-4 shrink-0 text-destructive" />}
                    </button>
                  );
                })}
              </div>
            )}

            {result && (
              <div
                className={cn(
                  "rounded-lg border p-4",
                  result.isCorrect ? "border-success/40 bg-success/5" : "border-destructive/40 bg-destructive/5"
                )}
              >
                <p className={cn("font-medium", result.isCorrect ? "text-success" : "text-destructive")}>
                  {result.isCorrect ? "Correct" : "Incorrect"}
                </p>
                {!result.isCorrect && result.correctAnswerFR && result.correctAnswerFR.length > 0 && (
                  <p className="mt-1 text-sm">
                    Correct answer: <span className="font-medium">{result.correctAnswerFR.join(" or ")}</span>
                  </p>
                )}
                {result.explanationHtml ? (
                  <MathContent html={result.explanationHtml} className="mt-2 text-sm leading-relaxed" />
                ) : (
                  <p className="mt-1 text-sm text-muted-foreground">
                    No written explanation for this question yet.
                  </p>
                )}
              </div>
            )}

            <div className="flex justify-end gap-2">
              {!result ? (
                <Button
                  onClick={submit}
                  disabled={isPending || (q.type === "FREE_RESPONSE" ? !freeResponse.trim() : !selected)}
                >
                  {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
                  Check answer
                </Button>
              ) : (
                <Button onClick={next}>{isLast ? "Finish session" : "Next question"}</Button>
              )}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
