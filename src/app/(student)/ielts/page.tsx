import Link from "next/link";
import { redirect } from "next/navigation";
import {
  ArrowRight, Headphones, BookOpenText, PenLine, Mic,
  MessageSquareText, Target, CalendarClock,
} from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { getExamContext } from "@/lib/exam/mode";
import { loadIeltsDashboard } from "@/lib/ielts/dashboard";
import { formatBand, PRACTICE_DISCLAIMER } from "@/lib/ielts/bands";

export const metadata = { title: "IELTS Dashboard" };
export const dynamic = "force-dynamic";

const SKILL_ICON = {
  LISTENING: Headphones, READING: BookOpenText, WRITING: PenLine, SPEAKING: Mic,
} as const;

const SKILL_HREF = {
  LISTENING: "/ielts/listening", READING: "/ielts/reading",
  WRITING: "/ielts/writing", SPEAKING: "/ielts/speaking",
} as const;

function greeting() {
  const h = new Date().getHours();
  if (h < 12) return "Good morning";
  if (h < 18) return "Good afternoon";
  return "Good evening";
}

export default async function IeltsDashboardPage() {
  const user = await requireUser();
  const exam = await getExamContext();

  // A student who has not added IELTS gets the public overview instead of an
  // empty dashboard — the page only means something with a profile behind it.
  if (!exam?.hasIelts) redirect("/ielts/overview");

  const [data, profile] = await Promise.all([
    loadIeltsDashboard(user.id),
    prisma.user.findUnique({ where: { id: user.id }, select: { name: true } }),
  ]);

  const firstName = profile?.name?.split(" ")[0] ?? "there";

  return (
    <div className="space-y-8">
      {/* Hero — the student's own numbers, not a marketing pitch. */}
      <section className="space-y-4">
        <p className="text-sm text-muted-foreground">
          {greeting()}, <span className="font-medium text-foreground">{firstName}</span>
        </p>
        <div className="flex flex-wrap items-end justify-between gap-4">
          <div className="space-y-1">
            <Badge variant="navy">IELTS Academic</Badge>
            <h1 className="font-display text-3xl font-semibold tracking-tight">
              {data.currentOverall != null
                ? `Band ${formatBand(data.currentOverall)}`
                : "Let's find your starting band"}
            </h1>
            <p className="text-sm text-muted-foreground">
              {data.profile.targetBand != null ? (
                <>Target <span className="font-medium text-foreground">Band {formatBand(data.profile.targetBand)}</span></>
              ) : (
                "No target band set yet"
              )}
              {data.focus && (
                <> · Next focus <span className="font-medium text-foreground">{data.focus.label}</span></>
              )}
            </p>
          </div>
          <div className="flex flex-wrap gap-2">
            <Button asChild>
              <Link href="/ielts/plan">
                Continue my IELTS plan <ArrowRight className="ml-1 h-4 w-4" />
              </Link>
            </Button>
            {!data.profile.onboarded && (
              // Optional, always. Nobody is asked anything to start using
              // IELTS — a target band only sharpens the plan, it does not
              // unlock it.
              <Button asChild variant="outline">
                <Link href="/ielts/plan">Set a target band</Link>
              </Button>
            )}
          </div>
        </div>

        <div className="flex flex-wrap gap-2 text-xs">
          {data.profile.daysToExam != null && (
            <Badge variant="outline">
              <CalendarClock className="h-3 w-3" />
              {data.profile.daysToExam > 0
                ? `${data.profile.daysToExam} days to your test`
                : "Test date passed"}
            </Badge>
          )}
          {data.profile.studyMinutesPerDay != null && (
            <Badge variant="outline">
              <Target className="h-3 w-3" /> {data.profile.studyMinutesPerDay} min/day
            </Badge>
          )}
        </div>
      </section>

      {/* Per-skill standing. Four cards, each a way in to that skill. */}
      <section className="space-y-3">
        <h2 className="font-display text-lg font-semibold">Your progress</h2>
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
          {data.standings.map((s) => {
            const Icon = SKILL_ICON[s.skill];
            return (
              <Link key={s.skill} href={SKILL_HREF[s.skill]} className="group">
                <Card className="h-full transition-colors group-hover:border-navy-900/30">
                  <CardContent className="space-y-2 py-5">
                    <div className="flex items-center gap-2 text-muted-foreground">
                      <Icon className="h-4 w-4" />
                      <span className="text-xs font-medium uppercase tracking-wide">
                        {s.label}
                      </span>
                    </div>
                    <p className="font-display text-3xl font-semibold tabular-nums">
                      {formatBand(s.band)}
                    </p>
                    <p className="text-xs text-muted-foreground">
                      {s.attempts === 0
                        ? "Not assessed yet"
                        : `${s.attempts} assessed ${s.attempts === 1 ? "attempt" : "attempts"}`}
                    </p>
                  </CardContent>
                </Card>
              </Link>
            );
          })}
        </div>
      </section>

      <div className="grid gap-4 lg:grid-cols-2">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0">
            <CardTitle className="text-base">Full practice tests</CardTitle>
            <Badge variant="outline">{data.publishedTests} available</Badge>
          </CardHeader>
          <CardContent className="space-y-3">
            <p className="text-sm text-muted-foreground">
              Listening, Reading, Writing and Speaking in one sitting, timed the way the
              computer-delivered test is.
            </p>
            <Button asChild variant={data.inProgressAttemptId ? "default" : "outline"}>
              <Link href="/ielts/tests">
                {data.inProgressAttemptId ? "Continue your test" : "Browse tests"}
              </Link>
            </Button>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0">
            <CardTitle className="text-base">Human feedback</CardTitle>
            <MessageSquareText className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent className="space-y-3">
            <div className="grid grid-cols-2 gap-3 text-sm">
              <div>
                <p className="font-display text-2xl font-semibold tabular-nums">
                  {data.readyWritingReviews}
                </p>
                <p className="text-xs text-muted-foreground">
                  Writing {data.readyWritingReviews === 1 ? "review" : "reviews"} ready
                  {data.pendingWritingReviews > 0 && ` · ${data.pendingWritingReviews} pending`}
                </p>
              </div>
              <div>
                <p className="font-display text-2xl font-semibold tabular-nums">
                  {data.readySpeakingReviews}
                </p>
                <p className="text-xs text-muted-foreground">
                  Speaking {data.readySpeakingReviews === 1 ? "review" : "reviews"} ready
                  {data.pendingSpeakingReviews > 0 && ` · ${data.pendingSpeakingReviews} pending`}
                </p>
              </div>
            </div>
            <Button asChild variant="outline">
              <Link href="/ielts/feedback">Open feedback</Link>
            </Button>
          </CardContent>
        </Card>
      </div>

      <p className="border-t border-border pt-4 text-xs text-muted-foreground">
        {PRACTICE_DISCLAIMER}
      </p>
    </div>
  );
}
