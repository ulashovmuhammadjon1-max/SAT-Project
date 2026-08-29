"use client";

import Link from "next/link";
import { useMemo, useState, useTransition } from "react";
import { ArrowRight, CheckCircle2, Loader2, RotateCcw, XCircle } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { answerApQuestion, type ApSessionQuestion } from "@/server/actions/student/ap";
import { cn } from "@/lib/utils";

const LETTERS = ["A", "B", "C", "D", "E"];

/**
 * The AP topic runner: one question at a time, five choices, graded on the
 * server when the student commits. The correct answer is not in the payload —
 * it arrives only with the graded result, alongside the explanation.
 */
export function TopicRunner({
  questions,
  backHref,
  topicLabel,
}: {
  questions: ApSessionQuestion[];
  backHref: string;
  topicLabel: string;
}) {
  // Start where the student left off: the first never-answered question.
  const firstFresh = useMemo(() => {
    const i = questions.findIndex((q) => q.priorChoice === null);
    return i === -1 ? 0 : i;
  }, [questions]);

  const [index, setIndex] = useState(firstFresh);
  const [selected, setSelected] = useState<number | null>(null);
  const [result, setResult] = useState<{ correctIndex: number; isCorrect: boolean; explanation: string | null } | null>(null);
  const [sessionCorrect, setSessionCorrect] = useState(0);
  const [sessionAnswered, setSessionAnswered] = useState(0);
  const [finished, setFinished] = useState(false);
  const [pending, start] = useTransition();

  const q = questions[index];

  function check() {
    if (selected === null || result) return;
    start(async () => {
      const res = await answerApQuestion({ questionId: q.id, chosenIndex: selected });
      if (res.error || res.correctIndex === undefined) {
        toast.error(res.error ?? "Something went wrong — try again.");
        return;
      }
      setResult({
        correctIndex: res.correctIndex,
        isCorrect: Boolean(res.isCorrect),
        explanation: res.explanation ?? null,
      });
      setSessionAnswered((n) => n + 1);
      if (res.isCorrect) setSessionCorrect((n) => n + 1);
    });
  }

  function next() {
    if (index + 1 >= questions.length) {
      setFinished(true);
      return;
    }
    setIndex(index + 1);
    setSelected(null);
    setResult(null);
  }

  if (finished) {
    return (
      <div className="mx-auto max-w-lg rounded-2xl border border-border/70 bg-card p-8 text-center shadow-soft">
        <CheckCircle2 className="mx-auto h-10 w-10 text-success" />
        <h2 className="mt-3 font-display text-2xl font-semibold tracking-tight">
          Topic {topicLabel} finished
        </h2>
        <p className="mt-2 text-sm text-muted-foreground">
          This session: {sessionCorrect}/{sessionAnswered} correct
          {sessionAnswered > 0 && <> ({Math.round((sessionCorrect / sessionAnswered) * 100)}%)</>}.
          Every answer is saved — your topic progress updates on the course page.
        </p>
        <div className="mt-6 flex justify-center gap-2">
          <Button asChild>
            <Link href={backHref}>Back to the course</Link>
          </Button>
          <Button
            variant="outline"
            className="gap-2"
            onClick={() => {
              setIndex(0);
              setSelected(null);
              setResult(null);
              setFinished(false);
            }}
          >
            <RotateCcw className="h-4 w-4" /> Go through again
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-3xl space-y-5">
      <div className="flex items-center justify-between text-sm text-muted-foreground">
        <span>
          Question <span className="font-medium text-foreground">{index + 1}</span> of{" "}
          {questions.length}
        </span>
        <span className="tabular-nums">
          This session: {sessionCorrect}/{sessionAnswered} correct
        </span>
      </div>
      <div className="h-1.5 overflow-hidden rounded-full bg-secondary">
        <div
          className="h-full rounded-full bg-primary transition-all"
          style={{ width: `${((index + (result ? 1 : 0)) / questions.length) * 100}%` }}
        />
      </div>

      <div className="rounded-2xl border border-border/70 bg-card p-6 shadow-soft">
        {q.table && (
          <div className="mb-4 overflow-x-auto">
            <table className="text-sm">
              <thead>
                <tr>
                  {q.table.headers.map((h, i) => (
                    <th
                      key={i}
                      className="border border-border bg-secondary/60 px-3 py-1.5 text-left font-semibold"
                    >
                      {h}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {q.table.rows.map((row, i) => (
                  <tr key={i}>
                    {row.map((cell, j) => (
                      <td key={j} className="border border-border px-3 py-1.5">
                        {cell}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        <p className="text-[15px] font-medium leading-relaxed">{q.stem}</p>

        <div className="mt-4 space-y-2">
          {q.choices.map((choice, i) => {
            const isChosen = selected === i;
            const showCorrect = result && i === result.correctIndex;
            const showWrong = result && isChosen && i !== result.correctIndex;
            return (
              <button
                key={i}
                type="button"
                disabled={Boolean(result) || pending}
                onClick={() => setSelected(i)}
                className={cn(
                  "flex w-full items-start gap-3 rounded-xl border px-4 py-3 text-left text-sm transition-colors",
                  showCorrect
                    ? "border-success bg-success/10"
                    : showWrong
                      ? "border-destructive bg-destructive/10"
                      : isChosen
                        ? "border-primary bg-primary/5"
                        : "border-border hover:border-primary/40",
                  result && "cursor-default",
                )}
              >
                <span
                  className={cn(
                    "flex h-6 w-6 shrink-0 items-center justify-center rounded-full border text-xs font-semibold",
                    showCorrect
                      ? "border-success bg-success text-white"
                      : showWrong
                        ? "border-destructive bg-destructive text-white"
                        : isChosen
                          ? "border-primary bg-primary text-white"
                          : "border-border text-muted-foreground",
                  )}
                >
                  {LETTERS[i]}
                </span>
                <span className="leading-relaxed">{choice}</span>
                {showCorrect && <CheckCircle2 className="ml-auto h-5 w-5 shrink-0 text-success" />}
                {showWrong && <XCircle className="ml-auto h-5 w-5 shrink-0 text-destructive" />}
              </button>
            );
          })}
        </div>

        {result && (
          <div
            className={cn(
              "mt-4 rounded-xl p-4 text-sm leading-relaxed",
              result.isCorrect ? "bg-success/10" : "bg-secondary/70",
            )}
          >
            <p className={cn("font-semibold", result.isCorrect ? "text-success" : "text-foreground")}>
              {result.isCorrect
                ? "Correct."
                : `Not quite — the answer is ${LETTERS[result.correctIndex]}.`}
            </p>
            {result.explanation && <p className="mt-1 text-muted-foreground">{result.explanation}</p>}
          </div>
        )}

        <div className="mt-5 flex items-center justify-between">
          <Button variant="ghost" asChild>
            <Link href={backHref}>Save & exit</Link>
          </Button>
          {result ? (
            <Button onClick={next} className="gap-2">
              {index + 1 >= questions.length ? "Finish" : "Next question"}
              <ArrowRight className="h-4 w-4" />
            </Button>
          ) : (
            <Button onClick={check} disabled={selected === null || pending} className="gap-2">
              {pending && <Loader2 className="h-4 w-4 animate-spin" />}
              Check answer
            </Button>
          )}
        </div>
      </div>
    </div>
  );
}
