"use client";

import { useState, useTransition } from "react";
import Link from "next/link";
import { Bookmark, Check, Clock, Flag, RotateCcw, X } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { MathContent } from "@/components/shared/math-content";
import { cn, formatDuration } from "@/lib/utils";
import { toPassageHtml } from "@/lib/exam/passage-html";
import { toggleBookmark } from "@/server/actions/student/bookmarks";

interface ReviewItem {
  responseId: string;
  questionId: string;
  subject: "READING_WRITING" | "MATH";
  stem: string;
  passage: { title: string | null; content: string } | null;
  imageUrl: string | null;
  type: "MULTIPLE_CHOICE" | "FREE_RESPONSE";
  difficulty: string;
  domain: string;
  skill: string;
  choices: { id: string; label: string; content: string; isCorrect: boolean }[];
  correctAnswerFR: string | null;
  selectedChoiceId: string | null;
  freeResponseAnswer: string | null;
  isCorrect: boolean | null;
  flagged: boolean;
  changedAnswerCount: number;
  timeSpentSeconds: number;
  explanation: {
    content: string;
    whyCorrect: string | null;
    commonMistakes: string | null;
    tips: string | null;
    relatedConcepts: string | null;
  } | null;
}

export function ReviewShell({
  testTitle,
  totalScaledScore,
  rwScaledScore,
  mathScaledScore,
  correctCount,
  totalCount,
  items,
}: {
  testTitle: string;
  totalScaledScore: number | null;
  rwScaledScore: number | null;
  mathScaledScore: number | null;
  correctCount: number;
  totalCount: number;
  items: ReviewItem[];
}) {
  const [index, setIndex] = useState(0);
  const item = items[index];

  return (
    <div className="min-h-screen bg-secondary/30">
      <header className="border-b border-border bg-navy-950 text-white">
        <div className="mx-auto flex max-w-7xl flex-wrap items-center justify-between gap-4 px-6 py-5">
          <div>
            <p className="text-sm text-navy-300">Review</p>
            <h1 className="font-display text-xl font-semibold">{testTitle}</h1>
          </div>
          <div className="flex items-center gap-6 text-center">
            <div>
              <p className="font-display text-2xl font-semibold">{totalScaledScore ?? "—"}</p>
              <p className="text-xs text-navy-300">Total</p>
            </div>
            <div>
              <p className="font-display text-lg font-semibold">{rwScaledScore ?? "—"}</p>
              <p className="text-xs text-navy-300">R&amp;W</p>
            </div>
            <div>
              <p className="font-display text-lg font-semibold">{mathScaledScore ?? "—"}</p>
              <p className="text-xs text-navy-300">Math</p>
            </div>
            <div>
              <p className="font-display text-lg font-semibold">
                {correctCount}/{totalCount}
              </p>
              <p className="text-xs text-navy-300">Correct</p>
            </div>
          </div>
          <div className="flex gap-2">
            <Button variant="outline" className="border-white/20 bg-white/5 text-white hover:bg-white/10" asChild>
              <Link href="/dashboard">Back to dashboard</Link>
            </Button>
          </div>
        </div>
      </header>

      <div className="mx-auto grid max-w-7xl gap-6 p-6 lg:grid-cols-[280px_1fr]">
        <div className="space-y-5 lg:sticky lg:top-6 lg:h-fit lg:max-h-[calc(100vh-3rem)] lg:overflow-y-auto">
          <QuestionNavGroup
            label="Reading & Writing"
            items={items}
            subject="READING_WRITING"
            activeIndex={index}
            onSelect={setIndex}
          />
          <QuestionNavGroup label="Math" items={items} subject="MATH" activeIndex={index} onSelect={setIndex} />
        </div>

        {item && <ReviewDetail item={item} />}
      </div>
    </div>
  );
}

function QuestionNavGroup({
  label,
  items,
  subject,
  activeIndex,
  onSelect,
}: {
  label: string;
  items: ReviewItem[];
  subject: "READING_WRITING" | "MATH";
  activeIndex: number;
  onSelect: (index: number) => void;
}) {
  // Indices into the flat `items` array, kept alongside a 1-based label
  // local to this subject -- students think in terms of "R&W Q12", not the
  // question's absolute position across the whole 98-question attempt.
  const entries = items
    .map((it, i) => ({ it, i }))
    .filter(({ it }) => it.subject === subject);

  if (entries.length === 0) return null;

  const correctInGroup = entries.filter(({ it }) => it.isCorrect).length;

  return (
    <div className="space-y-2">
      <div className="flex items-center justify-between px-1">
        <p className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">{label}</p>
        <p className="text-xs text-muted-foreground">
          {correctInGroup}/{entries.length}
        </p>
      </div>
      <div className="grid grid-cols-6 gap-1.5 lg:grid-cols-5">
        {entries.map(({ it, i }, localIndex) => (
          <button
            key={it.responseId}
            onClick={() => onSelect(i)}
            className={cn(
              "relative flex h-10 w-10 items-center justify-center rounded-lg border text-xs font-semibold",
              i === activeIndex && "ring-2 ring-primary ring-offset-1",
              it.isCorrect
                ? "border-success/40 bg-success/10 text-success"
                : "border-destructive/40 bg-destructive/10 text-destructive"
            )}
          >
            {localIndex + 1}
            {it.flagged && <Flag className="absolute -right-1 -top-1 h-3 w-3 fill-warning text-warning" />}
          </button>
        ))}
      </div>
    </div>
  );
}

function ReviewDetail({ item }: { item: ReviewItem }) {
  const [isPending, startTransition] = useTransition();
  const [bookmarked, setBookmarked] = useState(false);

  const wasGuessed = item.changedAnswerCount === 0 && item.timeSpentSeconds < 15 && !item.isCorrect;

  return (
    <div className="space-y-4">
      <Card>
        <CardContent className="flex flex-wrap items-center gap-2 p-4">
          <Badge variant={item.isCorrect ? "success" : "destructive"}>
            {item.isCorrect ? <Check className="h-3 w-3" /> : <X className="h-3 w-3" />}
            {item.isCorrect ? "Correct" : "Incorrect"}
          </Badge>
          <Badge variant="outline">{item.difficulty}</Badge>
          <Badge variant="outline">{item.domain}</Badge>
          <Badge variant="outline">{item.skill}</Badge>
          <Badge variant="outline">
            <Clock className="h-3 w-3" /> {formatDuration(item.timeSpentSeconds)}
          </Badge>
          {item.flagged && (
            <Badge variant="warning">
              <Flag className="h-3 w-3" /> Flagged
            </Badge>
          )}
          {item.changedAnswerCount > 0 && (
            <Badge variant="outline">
              <RotateCcw className="h-3 w-3" /> Changed {item.changedAnswerCount}×
            </Badge>
          )}
          {wasGuessed && <Badge variant="outline">Possibly guessed</Badge>}
          <Button
            variant="ghost"
            size="sm"
            className="ml-auto"
            disabled={isPending}
            onClick={() =>
              startTransition(async () => {
                const result = await toggleBookmark(item.questionId);
                setBookmarked(result.bookmarked);
              })
            }
          >
            <Bookmark className={cn("h-4 w-4", bookmarked && "fill-current")} /> Bookmark
          </Button>
        </CardContent>
      </Card>

      <div className={cn("grid gap-4", (item.passage || item.imageUrl) && "lg:grid-cols-2")}>
        {(item.passage || item.imageUrl) && (
          <Card>
            <CardContent className="space-y-4 p-5 text-sm leading-relaxed">
              {item.imageUrl && (
                // eslint-disable-next-line @next/next/no-img-element
                <img src={item.imageUrl} alt="Question figure" className="max-w-full rounded-lg border border-border" />
              )}
              {item.passage && <MathContent html={toPassageHtml(item.passage.content)} className="block" />}
            </CardContent>
          </Card>
        )}

        <Card>
          <CardContent className="space-y-4 p-5">
            <MathContent html={item.stem} className="block text-[15px] leading-relaxed" />

            {item.type === "MULTIPLE_CHOICE" ? (
              <div className="space-y-2">
                {item.choices.map((choice) => {
                  const isSelected = choice.id === item.selectedChoiceId;
                  return (
                    <div
                      key={choice.id}
                      className={cn(
                        "flex items-start gap-3 rounded-lg border p-3 text-sm",
                        choice.isCorrect && "border-success bg-success/5",
                        isSelected && !choice.isCorrect && "border-destructive bg-destructive/5"
                      )}
                    >
                      <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full border border-current text-xs font-semibold">
                        {choice.label}
                      </span>
                      <MathContent html={choice.content} className="flex-1" />
                      {choice.isCorrect && <Badge variant="success">Correct answer</Badge>}
                      {isSelected && !choice.isCorrect && <Badge variant="destructive">Your answer</Badge>}
                    </div>
                  );
                })}
              </div>
            ) : (
              <div className="grid grid-cols-2 gap-3 text-sm">
                <div className="rounded-lg border border-border p-3">
                  <p className="text-xs text-muted-foreground">Your answer</p>
                  <p className="font-medium">{item.freeResponseAnswer || "—"}</p>
                </div>
                <div className="rounded-lg border border-success/40 bg-success/5 p-3">
                  <p className="text-xs text-muted-foreground">Correct answer</p>
                  <p className="font-medium">{item.correctAnswerFR ?? "—"}</p>
                </div>
              </div>
            )}
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardContent className="space-y-4 p-5">
          <h3 className="font-display text-base font-semibold">Explanation</h3>
          {item.explanation ? (
            <div className="space-y-3 text-sm">
              <p>{item.explanation.content}</p>
              {item.explanation.whyCorrect && (
                <div>
                  <p className="font-medium">Why it&apos;s correct</p>
                  <p className="text-muted-foreground">{item.explanation.whyCorrect}</p>
                </div>
              )}
              {item.explanation.commonMistakes && (
                <div>
                  <p className="font-medium">Common mistakes</p>
                  <p className="text-muted-foreground">{item.explanation.commonMistakes}</p>
                </div>
              )}
              {item.explanation.tips && (
                <div>
                  <p className="font-medium">Tip</p>
                  <p className="text-muted-foreground">{item.explanation.tips}</p>
                </div>
              )}
            </div>
          ) : (
            <p className="text-sm text-muted-foreground">No explanation has been published for this question yet.</p>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
