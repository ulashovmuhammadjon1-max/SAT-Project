import Link from "next/link";
import { ArrowRight, CalendarCheck, Sparkles, Target, UserPlus, Video } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { CoinAmount } from "@/components/student/coin-badge";
import { LocalTime } from "@/components/shared/local-time";
import type { getPlanSummary } from "@/lib/plan/service";

type PlanSummary = Awaited<ReturnType<typeof getPlanSummary>>;

/**
 * "Your SAT plan" on the dashboard.
 *
 * Shows the single next action rather than the whole schedule — the plan page
 * is where the detail lives. A student opening the dashboard should be able to
 * start working without reading anything.
 */
export function DashboardPlanCard({ plan }: { plan: PlanSummary }) {
  const week = plan.thisWeek;

  return (
    <Card className="overflow-hidden border-primary/30 bg-gradient-to-br from-primary/10 via-primary/5 to-transparent">
      <CardContent className="p-6">
        <div className="flex flex-wrap items-start justify-between gap-4">
          <div className="min-w-0">
            <div className="flex items-center gap-2">
              <Target className="h-4 w-4 text-primary" />
              <p className="text-sm font-semibold text-primary">Your SAT plan</p>
            </div>
            <p className="mt-2 font-display text-lg font-semibold leading-snug">{plan.headline}</p>
          </div>

          <div className="flex shrink-0 gap-4 text-right">
            {(plan.estimatedScore ?? plan.currentScore) !== null && (
              <div>
                <p className="text-xs text-muted-foreground">Now</p>
                <p className="font-display text-xl font-semibold tabular-nums">
                  {plan.estimatedScore ?? plan.currentScore}
                </p>
              </div>
            )}
            {plan.targetScore !== null && (
              <div>
                <p className="text-xs text-muted-foreground">Target</p>
                <p className="font-display text-xl font-semibold tabular-nums text-primary">
                  {plan.targetScore}
                </p>
              </div>
            )}
            {plan.daysUntilTest !== null && (
              <div>
                <p className="text-xs text-muted-foreground">Test in</p>
                <p className="font-display text-xl font-semibold tabular-nums">
                  {plan.daysUntilTest}d
                </p>
              </div>
            )}
          </div>
        </div>

        {week && week.focus.length > 0 && (
          <div className="mt-4 rounded-lg border border-border bg-card/70 p-4">
            <p className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
              This week
            </p>
            <p className="mt-1 text-sm font-medium">
              {week.focus.flatMap((f) => f.skillNames).join(" · ")}
            </p>
            <div className="mt-2 flex flex-wrap gap-1.5">
              <Badge variant="outline" className="text-xs">
                {week.targetedSessions} targeted sessions
              </Badge>
              {week.fullTests > 0 && (
                <Badge variant="outline" className="text-xs">
                  {week.fullTests} full test
                </Badge>
              )}
            </div>
          </div>
        )}

        <div className="mt-4 flex flex-wrap gap-2">
          <Button asChild>
            <Link href={week?.practiceHref ?? "/practice"}>
              Continue today&apos;s plan <ArrowRight className="ml-1.5 h-4 w-4" />
            </Link>
          </Button>
          <Button asChild variant="outline">
            <Link href="/plan">See full plan</Link>
          </Button>
        </div>

        {plan.coldStart && (
          <p className="mt-3 flex items-start gap-1.5 text-xs text-muted-foreground">
            <Sparkles className="mt-0.5 h-3.5 w-3.5 shrink-0" />
            Based on {plan.evidenceCount} answered{" "}
            {plan.evidenceCount === 1 ? "question" : "questions"} — it sharpens as you practise.
          </p>
        )}
      </CardContent>
    </Card>
  );
}

/** Coins summary plus the two ways to act on them. */
export function DashboardCoinsCard({
  balance,
  referralReward,
}: {
  balance: number;
  referralReward: number;
}) {
  return (
    <Card>
      <CardContent className="p-5">
        <p className="text-sm font-medium text-muted-foreground">Scholarly Coins</p>
        <div className="mt-1">
          <CoinAmount value={balance} size="lg" />
        </div>
        <p className="mt-1 text-xs text-muted-foreground">
          +{referralReward} for every friend who joins
        </p>
        <div className="mt-3 flex flex-wrap gap-2">
          <Button asChild size="sm" variant="outline">
            <Link href="/invite">
              <UserPlus className="mr-1.5 h-3.5 w-3.5" />
              Invite
            </Link>
          </Button>
          <Button asChild size="sm" variant="outline">
            <Link href="/booking">
              <CalendarCheck className="mr-1.5 h-3.5 w-3.5" />
              Book 1-on-1
            </Link>
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}

export function DashboardSessionCard({
  startsAt,
  durationMinutes,
  meetingUrl,
}: {
  startsAt: Date;
  durationMinutes: number;
  meetingUrl: string | null;
}) {
  // "Join" only makes sense close to the start; outside that window a live
  // button invites a student to click into an empty room.
  const minutesAway = (startsAt.getTime() - Date.now()) / 60000;
  const joinable = minutesAway <= 10 && minutesAway > -durationMinutes;

  return (
    <Card className="border-success/40 bg-success/5">
      <CardContent className="p-5">
        <p className="text-sm font-medium text-success">Upcoming session</p>
        <p className="mt-1 font-display text-base font-semibold">
          <LocalTime iso={startsAt.toISOString()} format="full" />
        </p>
        <p className="text-xs text-muted-foreground">{durationMinutes} minutes · 1-on-1 guidance</p>
        <div className="mt-3 flex flex-wrap gap-2">
          {meetingUrl && joinable ? (
            <Button asChild size="sm">
              <a href={meetingUrl} target="_blank" rel="noopener noreferrer">
                <Video className="mr-1.5 h-3.5 w-3.5" />
                Join session
              </a>
            </Button>
          ) : null}
          <Button asChild size="sm" variant="outline">
            <Link href="/bookings">View details</Link>
          </Button>
        </div>
        {!meetingUrl && (
          <p className="mt-2 text-xs text-muted-foreground">
            Your join link will appear here before the session starts.
          </p>
        )}
      </CardContent>
    </Card>
  );
}
