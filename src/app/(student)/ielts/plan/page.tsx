import Link from "next/link";
import { ArrowRight, CalendarDays, Check, Circle, Clock, Target } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { loadIeltsPlan, weeklyShape } from "@/lib/ielts/plan";
import { formatBand, PRACTICE_DISCLAIMER } from "@/lib/ielts/bands";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "My IELTS Plan" };
export const dynamic = "force-dynamic";

/**
 * The IELTS roadmap.
 *
 * Its own page and its own route, not a tab on the SAT plan: a student doing
 * both exams has two targets, two dates and two sets of work, and a single
 * merged plan would have to pick one of them to lead with.
 */
export default async function IeltsPlanPage() {
  const user = await requireUser();
  const plan = await loadIeltsPlan(user.id);
  const { minutesPerWeek, focusShare } = weeklyShape(plan);

  const focusLabel = plan.focus === "WRITING" ? "Writing" : "Speaking";
  const otherLabel = plan.focus === "WRITING" ? "Speaking" : "Writing";

  return (
    <div className="space-y-8">
      <div className="space-y-2">
        <h1 className="font-display text-2xl font-semibold tracking-tight">My IELTS Plan</h1>
        <p className="max-w-2xl text-sm text-muted-foreground">
          Built from your answers and from the bands your reviewers have actually given —
          so it changes on its own as your work comes back marked.
        </p>
      </div>

      {plan.needsOnboarding && (
        <Card className="border-dashed">
          <CardContent className="flex flex-wrap items-center justify-between gap-4 py-5">
            <div>
              <p className="text-sm font-semibold">We have not asked you about IELTS yet</p>
              <p className="text-sm text-muted-foreground">
                The roadmap below is the general one. Send a task for review and it starts
                using your real bands.
              </p>
            </div>
            <Button asChild variant="outline">
              <Link href="/ielts/writing">Start Writing</Link>
            </Button>
          </CardContent>
        </Card>
      )}

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardContent className="space-y-1 py-5">
            <Target className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-3xl font-semibold tabular-nums">
              {plan.targetBand != null ? formatBand(plan.targetBand) : "—"}
            </p>
            <p className="text-sm text-muted-foreground">target band</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="space-y-1 py-5">
            <ArrowRight className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-3xl font-semibold tabular-nums">
              {plan.estimatedBand != null ? formatBand(plan.estimatedBand) : "—"}
            </p>
            <p className="text-sm text-muted-foreground">
              {plan.reviewedWriting + plan.reviewedSpeaking > 0
                ? "where you are, reviewed"
                : "where you said you are"}
            </p>
          </CardContent>
        </Card>
        <Card className={cn(plan.gap != null && plan.gap > 0 && "border-amber-500/40")}>
          <CardContent className="space-y-1 py-5">
            <Circle className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-3xl font-semibold tabular-nums">
              {plan.gap != null ? (plan.gap === 0 ? "0" : `+${formatBand(plan.gap)}`) : "—"}
            </p>
            <p className="text-sm text-muted-foreground">
              {plan.gap === 0 ? "you are there" : "bands to climb"}
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="space-y-1 py-5">
            <CalendarDays className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-3xl font-semibold tabular-nums">
              {plan.weeksLeft ?? "—"}
            </p>
            <p className="text-sm text-muted-foreground">
              {plan.weeksLeft == null
                ? "no test date set"
                : plan.weeksLeft === 1
                  ? "week to your test"
                  : "weeks to your test"}
            </p>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader className="pb-3">
          <CardTitle className="text-base">Where your effort goes</CardTitle>
          <p className="text-sm text-muted-foreground">{plan.focusReason}</p>
        </CardHeader>
        <CardContent className="space-y-4">
          {/* Two thirds to the weaker skill, drawn rather than stated — a bar
              makes "most of it, not all of it" obvious at a glance. */}
          <div className="flex h-3 overflow-hidden rounded-full">
            <div
              className="bg-primary"
              style={{ width: `${Math.round(focusShare * 100)}%` }}
              aria-hidden
            />
            <div className="flex-1 bg-secondary" aria-hidden />
          </div>
          <div className="flex flex-wrap justify-between gap-2 text-sm">
            <span>
              <span className="font-semibold">{focusLabel}</span>
              <span className="text-muted-foreground"> · {Math.round(focusShare * 100)}%</span>
            </span>
            <span>
              <span className="font-semibold">{otherLabel}</span>
              <span className="text-muted-foreground">
                {" "}
                · {100 - Math.round(focusShare * 100)}%
              </span>
            </span>
          </div>
          {minutesPerWeek && (
            <p className="flex items-center gap-2 text-sm text-muted-foreground">
              <Clock className="h-3.5 w-3.5" />
              About {minutesPerWeek} minutes a week, at the pace you set. The weaker skill
              gets most of it — never all of it, because Speaking especially goes backwards
              if it is left alone.
            </p>
          )}
        </CardContent>
      </Card>

      <section className="space-y-3">
        <h2 className="font-display text-lg font-semibold">Your roadmap</h2>
        <ol className="space-y-3">
          {plan.stages.map((stage) => (
            <li key={stage.index}>
              <Card
                className={cn(
                  stage.current && "border-primary/50 bg-primary/5",
                  stage.done && "opacity-70"
                )}
              >
                <CardContent className="flex flex-wrap items-start gap-4 py-5">
                  <span
                    className={cn(
                      "flex h-8 w-8 shrink-0 items-center justify-center rounded-full text-sm font-semibold",
                      stage.done
                        ? "bg-emerald-600 text-white"
                        : stage.current
                          ? "bg-primary text-primary-foreground"
                          : "border border-border text-muted-foreground"
                    )}
                  >
                    {stage.done ? <Check className="h-4 w-4" /> : stage.index}
                  </span>
                  <div className="min-w-[240px] flex-1 space-y-1">
                    <div className="flex flex-wrap items-center gap-2">
                      <p className="text-sm font-semibold">{stage.title}</p>
                      {stage.current && <Badge variant="navy">You are here</Badge>}
                      {stage.done && <Badge variant="outline">Done</Badge>}
                    </div>
                    <p className="text-sm text-muted-foreground">{stage.blurb}</p>
                  </div>
                  {!stage.done && (
                    <div className="flex flex-wrap gap-2">
                      {stage.actions.map((a) => (
                        <Button
                          key={a.href + a.label}
                          asChild
                          size="sm"
                          variant={stage.current ? "default" : "outline"}
                        >
                          <Link href={a.href}>{a.label}</Link>
                        </Button>
                      ))}
                    </div>
                  )}
                </CardContent>
              </Card>
            </li>
          ))}
        </ol>
      </section>

      <p className="border-t border-border pt-4 text-xs text-muted-foreground">
        {PRACTICE_DISCLAIMER}
      </p>
    </div>
  );
}
