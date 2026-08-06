"use client";

import { useState, useTransition } from "react";
import Link from "next/link";
import { Bookmark, Check, X } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { MathContent } from "@/components/shared/math-content";
import { cn } from "@/lib/utils";
import { toggleBookmark } from "@/server/actions/student/bookmarks";

interface PracticeQuestionData {
  id: string;
  stem: string;
  imageUrl: string | null;
  type: "MULTIPLE_CHOICE" | "FREE_RESPONSE";
  difficulty: string;
  domain: string;
  skill: string;
  passage: { title: string | null; content: string } | null;
  choices: { id: string; label: string; content: string; isCorrect: boolean }[];
  correctAnswerFR: string | null;
  explanation: { content: string; tips: string | null; commonMistakes: string | null } | null;
}

export function PracticeQuestion({
  question,
  nextQuestionId,
  initiallyBookmarked,
}: {
  question: PracticeQuestionData;
  nextQuestionId: string | null;
  initiallyBookmarked: boolean;
}) {
  const [selected, setSelected] = useState<string | null>(null);
  const [freeResponse, setFreeResponse] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [bookmarked, setBookmarked] = useState(initiallyBookmarked);
  const [isPending, startTransition] = useTransition();

  const isCorrect =
    question.type === "MULTIPLE_CHOICE"
      ? question.choices.find((c) => c.id === selected)?.isCorrect ?? false
      : freeResponse.trim().toLowerCase() === (question.correctAnswerFR ?? "").trim().toLowerCase();

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="flex flex-wrap gap-2">
          <Badge variant="outline">{question.domain}</Badge>
          <Badge variant="outline">{question.skill}</Badge>
          <Badge variant="outline">{question.difficulty}</Badge>
        </div>
        <Button
          variant="outline"
          size="sm"
          disabled={isPending}
          onClick={() =>
            startTransition(async () => {
              const result = await toggleBookmark(question.id);
              setBookmarked(result.bookmarked);
            })
          }
        >
          <Bookmark className={cn("h-4 w-4", bookmarked && "fill-current")} /> Bookmark
        </Button>
      </div>

      <div className={cn("grid gap-4", question.passage && "lg:grid-cols-2")}>
        {question.passage && (
          <Card>
            <CardContent className="p-5 text-sm leading-relaxed">
              <MathContent html={question.passage.content} />
            </CardContent>
          </Card>
        )}

        <Card>
          <CardContent className="space-y-4 p-5">
            <MathContent html={question.stem} className="block text-[15px] leading-relaxed" />

            {question.type === "MULTIPLE_CHOICE" ? (
              <div className="space-y-2">
                {question.choices.map((choice) => {
                  const showResult = submitted;
                  const isSelected = selected === choice.id;
                  return (
                    <button
                      key={choice.id}
                      disabled={submitted}
                      onClick={() => setSelected(choice.id)}
                      className={cn(
                        "flex w-full items-start gap-3 rounded-lg border p-3 text-left text-sm transition-colors",
                        isSelected && !showResult && "border-primary bg-accent",
                        showResult && choice.isCorrect && "border-success bg-success/5",
                        showResult && isSelected && !choice.isCorrect && "border-destructive bg-destructive/5"
                      )}
                    >
                      <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full border border-current text-xs font-semibold">
                        {choice.label}
                      </span>
                      <MathContent html={choice.content} className="flex-1" />
                      {showResult && choice.isCorrect && <Check className="h-4 w-4 shrink-0 text-success" />}
                      {showResult && isSelected && !choice.isCorrect && <X className="h-4 w-4 shrink-0 text-destructive" />}
                    </button>
                  );
                })}
              </div>
            ) : (
              <Input
                value={freeResponse}
                onChange={(e) => setFreeResponse(e.target.value)}
                disabled={submitted}
                placeholder="Enter your answer"
                className="max-w-xs"
              />
            )}

            {!submitted ? (
              <Button
                onClick={() => setSubmitted(true)}
                disabled={question.type === "MULTIPLE_CHOICE" ? !selected : !freeResponse}
              >
                Check answer
              </Button>
            ) : (
              <div className="flex items-center gap-3">
                <Badge variant={isCorrect ? "success" : "destructive"}>{isCorrect ? "Correct" : "Incorrect"}</Badge>
                {nextQuestionId && (
                  <Button asChild size="sm">
                    <Link href={`/practice/${nextQuestionId}`}>Next question</Link>
                  </Button>
                )}
              </div>
            )}
          </CardContent>
        </Card>
      </div>

      {submitted && question.explanation && (
        <Card>
          <CardContent className="space-y-3 p-5 text-sm">
            <h3 className="font-display text-base font-semibold">Explanation</h3>
            <MathContent html={question.explanation.content} className="block" />
            {question.explanation.tips && <p className="text-muted-foreground">Tip: {question.explanation.tips}</p>}
          </CardContent>
        </Card>
      )}
    </div>
  );
}
