import Link from "next/link";
import {
  ArrowRight,
  CalendarDays,
  CheckCircle2,
  Circle,
  Flame,
  Target,
  TrendingUp,
} from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { RebuildPlanButton } from "@/components/student/rebuild-plan-button";
import { getOrCreatePlan } from "@/lib/plan/service";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "My SAT plan" };
export const dynamic = "force-dynamic";

export default async function PlanPage() {
  const user = await requireUser();
  const plan = await getOrCreatePlan(user.id);

  return (
    <div className="mx-auto max-w-4xl space-y-6">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">Your SAT plan</h1>
          <p className="text-sm text-muted-foreground">{plan.headline}</p>
        </div>
        <RebuildPlanButton />
      </div>

      {/* Score header. Only renders what the student actually gave us — an
          absent target must not become a fake "0". */}
      <Card className="overflow-hidden border-primary/30 bg-gradient-to-br from-primary/10 via-primary/5 to-transparent">
        <CardContent className="grid gap-6 p-6 sm:grid-cols-3 sm:p-8">
          <Metric
            icon={TrendingUp}
            label={plan.estimatedScore ? "Latest estimate" : "Starting score"}
            value={plan.estimatedScore ?? plan.currentScore}
            fallback="Take a test"
          />
          <Metric icon={Target} label="Target" value={plan.targetScore} fallback="Not set" />
          <Metric
            icon={CalendarDays}
            label="Test day"
            value={plan.daysUntilTest}
            suffix={plan.daysUntilTest === 1 ? " day" : " days"}
            fallback="No date set"
          />
        </CardContent>
        {plan.scoreGap !== null && plan.scoreGap > 0 && (
          <div className="border-t border-primary/20 bg-primary/5 px-6 py-3 text-sm sm:px-8">
            <span className="font-semibold text-primary">{plan.scoreGap} points</span>{" "}
            <span className="text-muted-foreground">between where you are and where you want to be.</span>
          </div>
        )}
      </Card>

      {plan.coldStart && (
        <Card className="border-warning/40 bg-warning/5">
          <CardContent className="flex gap-3 p-5">
            <Flame className="mt-0.5 h-5 w-5 shrink-0 text-warning" />
            <div className="text-sm">
              <p className="font-medium">This plan is a starting point, not a diagnosis.</p>
              <p className="mt-1 text-muted-foreground">
                You&apos;ve answered {plan.evidenceCount}{" "}
                {plan.evidenceCount === 1 ? "question" : "questions"} so far. Once you pass 15,
                Scholarly rebuilds this plan around the skills you actually miss.
              </p>
              <Button asChild size="sm" className="mt-3">
                <Link href="/practice">
                  Start practising <ArrowRight className="ml-1.5 h-3.5 w-3.5" />
                </Link>
              </Button>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Priorities */}
      <Card>
        <CardHeader>
          <CardTitle className="text-base">What to work on, weakest first</CardTitle>
        </CardHeader>
        <CardContent className="space-y-2">
          {plan.priorities.map((p, i) => (
            <div
              key={p.code}
              className="flex items-center gap-3 rounded-lg border border-border bg-card px-3 py-2.5"
            >
              <span className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-primary/10 text-xs font-semibold text-primary">
                {i + 1}
              </span>
              <div className="min-w-0 flex-1">
                <p className="truncate text-sm font-medium">{p.name}</p>
                <p className="truncate text-xs text-muted-foreground">
                  {p.domainName} · {p.reason}
                </p>
              </div>
              {p.accuracy !== null && (
                <span
                  className={cn(
                    "shrink-0 text-sm font-semibold tabular-nums",
                    p.accuracy < 60
                      ? "text-destructive"
                      : p.accuracy < 80
                        ? "text-warning"
                        : "text-success",
                  )}
                >
                  {p.accuracy}%
                </span>
              )}
            </div>
          ))}
        </CardContent>
      </Card>

      {plan.strengths.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-base">Keep these warm</CardTitle>
          </CardHeader>
          <CardContent className="flex flex-wrap gap-2">
            {plan.strengths.map((s) => (
              <Badge key={s.code} variant="secondary" className="gap-1.5">
                {s.name}
                <span className="font-semibold text-success">{s.accuracy}%</span>
              </Badge>
            ))}
          </CardContent>
        </Card>
      )}

      {/* Weeks */}
      <Card>
        <CardHeader>
          <CardTitle className="text-base">
            Your schedule · {plan.sessionsPerWeek} sessions a week, about{" "}
            {plan.minutesPerSession} minutes each
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          {plan.weeks.map((w) => (
            <div key={w.index} className="rounded-lg border border-border p-4">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <p className="font-display text-sm font-semibold">{w.label}</p>
                <div className="flex flex-wrap gap-1.5">
                  <Badge variant="outline" className="text-xs">
                    {w.targetedSessions} targeted
                  </Badge>
                  {w.timedModules > 0 && (
                    <Badge variant="outline" className="text-xs">
                      {w.timedModules} timed module
                    </Badge>
                  )}
                  {w.fullTests > 0 && (
                    <Badge className="bg-primary/15 text-xs text-primary hover:bg-primary/20">
                      {w.fullTests} full test
                    </Badge>
                  )}
                </div>
              </div>

              <ul className="mt-3 space-y-1">
                {w.focus.map((f) => (
                  <li key={f.domainName} className="text-sm">
                    <span className="text-muted-foreground">{f.domainName}:</span>{" "}
                    <span className="font-medium">{f.skillNames.join(", ")}</span>
                  </li>
                ))}
              </ul>

              <p className="mt-2 text-xs text-muted-foreground">{w.reviewFocus}</p>

              <Button asChild size="sm" variant="outline" className="mt-3">
                <Link href={w.practiceHref}>
                  Practise {w.label.toLowerCase()} <ArrowRight className="ml-1.5 h-3.5 w-3.5" />
                </Link>
              </Button>
            </div>
          ))}
        </CardContent>
      </Card>

      {/* Milestones */}
      <Card>
        <CardHeader>
          <CardTitle className="text-base">Milestones</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          {plan.milestones.map((m) => (
            <div key={m.id}>
              <div className="flex items-center gap-2">
                {m.done ? (
                  <CheckCircle2 className="h-4 w-4 shrink-0 text-success" />
                ) : (
                  <Circle className="h-4 w-4 shrink-0 text-muted-foreground" />
                )}
                <p className={cn("flex-1 text-sm font-medium", m.done && "text-muted-foreground line-through")}>
                  {m.label}
                </p>
                <span className="text-xs tabular-nums text-muted-foreground">
                  {m.current}/{m.target}
                </span>
              </div>
              <Progress
                value={Math.min(100, Math.round((m.current / m.target) * 100))}
                className="mt-2 h-1.5"
              />
              <p className="mt-1 pl-6 text-xs text-muted-foreground">{m.detail}</p>
            </div>
          ))}
        </CardContent>
      </Card>

      <p className="text-center text-xs text-muted-foreground">
        Built from {plan.evidenceCount} answered{" "}
        {plan.evidenceCount === 1 ? "question" : "questions"}. This plan rebuilds itself as you
        practise.
      </p>
    </div>
  );
}

function Metric({
  icon: Icon,
  label,
  value,
  suffix = "",
  fallback,
}: {
  icon: typeof Target;
  label: string;
  value: number | null;
  suffix?: string;
  fallback: string;
}) {
  return (
    <div className="flex items-start gap-3">
      <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
        <Icon className="h-4 w-4" />
      </span>
      <div className="min-w-0">
        <p className="text-xs font-medium text-muted-foreground">{label}</p>
        {value !== null ? (
          <p className="font-display text-2xl font-semibold tabular-nums">
            {value}
            <span className="text-base font-normal text-muted-foreground">{suffix}</span>
          </p>
        ) : (
          <p className="mt-1 text-sm text-muted-foreground">{fallback}</p>
        )}
      </div>
    </div>
  );
}
