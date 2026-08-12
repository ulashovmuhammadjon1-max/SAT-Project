import Link from "next/link";
import { CalendarDays, CheckCircle2, Circle, Users, XCircle } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { PracticeQuestion } from "@/components/student/practice-question";
import { getDailyChallenge } from "@/lib/daily-challenge";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "Daily Challenge" };
export const dynamic = "force-dynamic";

export default async function DailyChallengePage() {
  const user = await requireUser();
  const daily = await getDailyChallenge(user.id);

  if (!daily) {
    return (
      <Card>
        <CardContent className="p-10 text-center text-sm text-muted-foreground">
          No published questions yet, so there is no challenge today.
        </CardContent>
      </Card>
    );
  }

  const [question, bookmark] = await Promise.all([
    prisma.question.findUnique({
      where: { id: daily.questionId },
      include: {
        choices: { orderBy: { order: "asc" } },
        passage: true,
        domain: true,
        skill: true,
        explanation: true,
      },
    }),
    prisma.bookmark.findUnique({
      where: { userId_questionId: { userId: user.id, questionId: daily.questionId } },
    }),
  ]);

  if (!question) {
    return (
      <Card>
        <CardContent className="p-10 text-center text-sm text-muted-foreground">
          Today&apos;s question could not be loaded. Try again shortly.
        </CardContent>
      </Card>
    );
  }

  const today = new Date(`${daily.day}T00:00:00.000Z`);

  return (
    <div className="space-y-6">
      {/* No domain/skill/difficulty badges here — PracticeQuestion renders its
          own set directly above the question, and two identical rows a few
          hundred pixels apart just reads as a bug. */}
      <div>
        <h1 className="flex items-center gap-2 font-display text-2xl font-semibold tracking-tight">
          <CalendarDays className="h-5 w-5" /> Daily Challenge
        </h1>
        <p className="text-sm text-muted-foreground">
          {today.toLocaleDateString(undefined, {
            weekday: "long",
            day: "numeric",
            month: "long",
            timeZone: "UTC",
          })}{" "}
          · everyone gets the same question today.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-3">
        <Card className={cn(daily.answeredToday && "border-emerald-500/40")}>
          <CardContent className="flex items-center gap-3 p-5">
            {daily.answeredToday ? (
              daily.answeredCorrectly ? (
                <CheckCircle2 className="h-8 w-8 shrink-0 text-emerald-500" />
              ) : (
                <XCircle className="h-8 w-8 shrink-0 text-amber-500" />
              )
            ) : (
              <Circle className="h-8 w-8 shrink-0 text-muted-foreground" />
            )}
            <div>
              <p className="font-medium">
                {daily.answeredToday
                  ? daily.answeredCorrectly
                    ? "Solved today"
                    : "Attempted today"
                  : "Not answered yet"}
              </p>
              <p className="text-xs text-muted-foreground">
                {daily.answeredToday
                  ? "Comes back tomorrow with a new one."
                  : "It counts toward your streak."}
              </p>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="flex items-center gap-3 p-5">
            <Users className="h-8 w-8 shrink-0 text-muted-foreground" />
            <div>
              <p className="font-medium tabular-nums">
                {daily.solvedBy} {daily.solvedBy === 1 ? "student" : "students"}
              </p>
              <p className="text-xs text-muted-foreground">
                {daily.crowdAccuracyPct == null
                  ? "answered it today"
                  : `answered today · ${daily.crowdAccuracyPct}% got it right`}
              </p>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-5">
            <p className="text-xs uppercase tracking-wide text-muted-foreground">Last 7 days</p>
            <div className="mt-2 flex gap-1.5">
              {daily.week.map((d, i) => (
                <div key={i} className="flex flex-1 flex-col items-center gap-1">
                  <span
                    className={cn(
                      "h-7 w-full rounded-md",
                      d.studied ? "bg-primary" : "bg-muted-foreground/25",
                      d.isToday && "ring-2 ring-primary ring-offset-2 ring-offset-background"
                    )}
                    title={d.studied ? "studied" : "no activity"}
                  />
                  <span className="text-[10px] text-muted-foreground">{d.label}</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>

      <PracticeQuestion
        question={{
          id: question.id,
          stem: question.stem,
          imageUrl: question.imageUrl,
          type: question.type,
          difficulty: question.difficulty,
          domain: question.domain.name,
          skill: question.skill.name,
          passage: question.passage
            ? { title: question.passage.title, content: question.passage.content }
            : null,
          choices: question.choices.map((c) => ({
            id: c.id,
            label: c.label,
            content: c.content,
            isCorrect: c.isCorrect,
          })),
          correctAnswerFR: question.correctAnswerFR
            ? (JSON.parse(question.correctAnswerFR)[0] ?? null)
            : null,
          explanation: question.explanation
            ? {
                content: question.explanation.content,
                tips: question.explanation.tips,
                commonMistakes: question.explanation.commonMistakes,
              }
            : null,
        }}
        // There is exactly one daily question, so "next" would contradict the
        // premise. Practice continues in the Question Bank instead.
        nextQuestionId={null}
        initiallyBookmarked={!!bookmark}
      />

      <div className="flex justify-center">
        <Button variant="outline" asChild>
          <Link href="/practice">Keep practising in the Question Bank</Link>
        </Button>
      </div>
    </div>
  );
}
