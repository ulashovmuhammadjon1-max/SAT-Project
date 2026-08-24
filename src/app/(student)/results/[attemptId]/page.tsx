import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import { ArrowRight, Target, TrendingDown, TrendingUp, Users } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { ScoreCard } from "@/components/student/score-card";
import { getPeerComparison } from "@/lib/scoring/percentile";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "Your result" };
export const dynamic = "force-dynamic";

/**
 * The page a student lands on after finishing a test.
 *
 * The review screen answers "which ones did I get wrong"; this answers "how
 * did I do" — the score, how it moved, where it sits against everyone else who
 * sat the same paper, which skills cost the most marks, and a card built to be
 * screenshotted into a group chat.
 */
export default async function ResultsPage({ params }: { params: { attemptId: string } }) {
  const user = await requireUser();

  const attempt = await prisma.attempt.findUnique({
    where: { id: params.attemptId },
    include: { test: { select: { id: true, title: true } } },
  });

  if (!attempt || attempt.userId !== user.id) notFound();
  if (attempt.status !== "SUBMITTED") redirect(`/exam/${attempt.id}`);

  const [responses, previous, peers] = await Promise.all([
    prisma.response.findMany({
      where: { attemptId: attempt.id, isCorrect: { not: null } },
      select: {
        isCorrect: true,
        timeSpentSeconds: true,
        question: {
          select: {
            skill: { select: { name: true } },
            domain: { select: { name: true, subject: true } },
          },
        },
      },
    }),
    // The attempt immediately before this one, to show movement. Ordered by
    // submission time, not creation: a student can start three tests and
    // finish them out of order.
    prisma.attempt.findFirst({
      where: {
        userId: user.id,
        status: "SUBMITTED",
        totalScaledScore: { not: null },
        submittedAt: { lt: attempt.submittedAt ?? new Date() },
      },
      orderBy: { submittedAt: "desc" },
      select: { totalScaledScore: true, test: { select: { title: true } } },
    }),
    getPeerComparison(attempt.test.id, user.id, attempt.totalScaledScore),
  ]);

  const correct = responses.filter((r) => r.isCorrect).length;
  const improvement =
    attempt.totalScaledScore != null && previous?.totalScaledScore != null
      ? attempt.totalScaledScore - previous.totalScaledScore
      : null;

  // Skill-level accuracy, weakest first — the actionable half of the page.
  const bySkill = new Map<string, { name: string; subject: string; correct: number; total: number }>();
  for (const r of responses) {
    const key = r.question.skill.name;
    const bucket =
      bySkill.get(key) ??
      { name: key, subject: r.question.domain.subject, correct: 0, total: 0 };
    bucket.total += 1;
    if (r.isCorrect) bucket.correct += 1;
    bySkill.set(key, bucket);
  }
  const skills = [...bySkill.values()]
    // Three questions is too thin a base to call a skill weak, so those sort
    // last rather than topping the list on a single unlucky answer.
    .map((s) => ({ ...s, pct: Math.round((s.correct / s.total) * 100), thin: s.total < 4 }))
    .sort((a, b) => Number(a.thin) - Number(b.thin) || a.pct - b.pct);

  const weakest = skills.filter((s) => !s.thin && s.pct < 70).slice(0, 5);

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-end justify-between gap-4">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">
            {attempt.test.title} · your result
          </h1>
          <p className="text-sm text-muted-foreground">
            Submitted{" "}
            {attempt.submittedAt?.toLocaleDateString(undefined, {
              day: "numeric",
              month: "long",
              year: "numeric",
            })}
          </p>
        </div>
        <Button asChild>
          <Link href={`/review/${attempt.id}`}>
            Review every question <ArrowRight className="h-4 w-4" />
          </Link>
        </Button>
      </div>

      <div className="grid gap-4 lg:grid-cols-[minmax(0,22rem)_1fr]">
        <ScoreCard
          data={{
            studentName: user.name ?? "Scholarly student",
            testTitle: attempt.test.title,
            total: attempt.totalScaledScore ?? 0,
            rw: attempt.rwScaledScore,
            math: attempt.mathScaledScore,
            correct,
            outOf: responses.length,
            dateLabel:
              attempt.submittedAt?.toLocaleDateString(undefined, {
                day: "numeric",
                month: "short",
                year: "numeric",
              }) ?? "",
            percentile: peers.percentile,
            improvement,
          }}
        />

        <div className="space-y-4">
          <div className="grid gap-4 sm:grid-cols-3">
            <Stat
              label="Change"
              value={
                improvement == null
                  ? "—"
                  : improvement > 0
                    ? `+${improvement}`
                    : String(improvement)
              }
              tone={improvement == null ? undefined : improvement > 0 ? "up" : improvement < 0 ? "down" : undefined}
              sub={
                previous
                  ? `vs ${previous.test.title} (${previous.totalScaledScore})`
                  : "your first scored test"
              }
            />
            <Stat
              label="Percentile"
              value={peers.percentile == null ? "—" : `${peers.percentile}th`}
              sub={
                peers.percentile == null
                  ? `needs more results on this test (${peers.sample} so far)`
                  : `of ${peers.sample} students on this test`
              }
            />
            <Stat
              label="Accuracy"
              value={responses.length ? `${Math.round((correct / responses.length) * 100)}%` : "—"}
              sub={`${correct} of ${responses.length} answered correctly`}
            />
          </div>

          {peers.cohortAverage != null && (
            <Card>
              <CardContent className="flex flex-wrap items-center gap-x-8 gap-y-3 p-5 text-sm">
                <span className="flex items-center gap-2 text-muted-foreground">
                  <Users className="h-4 w-4" /> How this test usually goes
                </span>
                <span>
                  Average <strong className="tabular-nums">{peers.cohortAverage}</strong>
                </span>
                <span>
                  Best <strong className="tabular-nums">{peers.cohortBest}</strong>
                </span>
                <span>
                  You <strong className="tabular-nums">{attempt.totalScaledScore}</strong>
                </span>
              </CardContent>
            </Card>
          )}

          <Card>
            <CardHeader className="pb-3">
              <CardTitle className="flex items-center gap-2 text-base">
                <Target className="h-4 w-4" /> What to work on next
              </CardTitle>
            </CardHeader>
            <CardContent>
              {weakest.length ? (
                <ul className="space-y-3">
                  {weakest.map((s) => (
                    <li key={s.name}>
                      <div className="mb-1 flex items-baseline justify-between gap-2 text-sm">
                        <div className="flex min-w-0 items-center gap-2">
                          <span className="truncate">{s.name}</span>
                          <Badge variant="outline" className="shrink-0">
                            {s.subject === "MATH" ? "Math" : "R&W"}
                          </Badge>
                        </div>
                        <span className="shrink-0 tabular-nums text-muted-foreground">
                          {s.correct}/{s.total}
                        </span>
                      </div>
                      <Progress value={s.pct} className="h-1.5" />
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="py-4 text-center text-sm text-muted-foreground">
                  Nothing under 70% with enough questions to judge — a strong sitting.
                </p>
              )}
              <Button variant="outline" size="sm" className="mt-4 w-full" asChild>
                <Link href="/practice/start">Drill these in the Question Bank</Link>
              </Button>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}

function Stat({
  label,
  value,
  sub,
  tone,
}: {
  label: string;
  value: string;
  sub: string;
  tone?: "up" | "down";
}) {
  const Icon = tone === "up" ? TrendingUp : tone === "down" ? TrendingDown : null;
  return (
    <Card>
      <CardContent className="p-5">
        <p className="text-xs uppercase tracking-wide text-muted-foreground">{label}</p>
        <p
          className={cn(
            "mt-1 flex items-center gap-1.5 font-display text-3xl font-semibold tabular-nums",
            tone === "up" && "text-emerald-500",
            tone === "down" && "text-amber-500"
          )}
        >
          {Icon && <Icon className="h-5 w-5" />}
          {value}
        </p>
        <p className="mt-1 text-xs text-muted-foreground">{sub}</p>
      </CardContent>
    </Card>
  );
}
