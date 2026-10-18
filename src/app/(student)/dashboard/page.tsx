import Link from "next/link";
import {
  ArrowRight,
  Award,
  CalendarRange,
  FlaskConical,
  Flame,
  Languages,
  MessagesSquare,
  UserRound,
  BookOpen,
} from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";
import { ScenicHeader } from "@/components/shared/scenic-header";
import {
  DashboardCoinsCard,
  DashboardSessionCard,
} from "@/components/student/dashboard-plan-card";
import {
  DashboardAchievementsCard,
  DashboardLeaderboardCard,
} from "@/components/student/dashboard-engagement";
import { getAchievements } from "@/lib/achievements/service";
import { getLeaderboard } from "@/lib/leaderboard";
import { ACTIVE_STATUSES } from "@/lib/booking/status";
import { getExamContext } from "@/lib/exam/mode";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { getSettings } from "@/lib/settings";
import { cn } from "@/lib/utils";

export const metadata = { title: "Home" };
export const dynamic = "force-dynamic";

/**
 * Home — the first page a signed-in student sees.
 *
 * Scholarly is several programmes, so Home is a hub across all of them: the
 * research programme, AP courses, mentorship, IELTS, events and community,
 * each showing where this student stands. SAT practice has its own home at
 * /sat and appears here last, as one card among the rest.
 *
 * Every query selects explicit columns (see CLAUDE.md on whole-row fetches).
 */
export default async function HomePage() {
  const user = await requireUser();

  const [
    proposals,
    apEnrollments,
    exam,
    upcomingSession,
    coinUser,
    profile,
    satLatest,
    satInProgress,
    settings,
    achievements,
    weeklyBoard,
  ] = await Promise.all([
    prisma.researchProposal.findMany({
      where: { userId: user.id },
      orderBy: { createdAt: "desc" },
      select: { status: true },
      take: 1,
    }),
    prisma.apSubjectEnrollment.count({ where: { userId: user.id } }),
    getExamContext(),
    prisma.booking.findFirst({
      where: { userId: user.id, status: { in: ACTIVE_STATUSES } },
      orderBy: { slot: { startsAt: "asc" } },
      select: {
        meetingUrl: true,
        slot: { select: { startsAt: true, durationMinutes: true } },
      },
    }),
    prisma.user.findUnique({ where: { id: user.id }, select: { coinBalance: true } }),
    prisma.user.findUnique({ where: { id: user.id }, select: { currentStreak: true } }),
    prisma.attempt.findFirst({
      where: { userId: user.id, status: "SUBMITTED", totalScaledScore: { not: null } },
      orderBy: { submittedAt: "desc" },
      select: { totalScaledScore: true },
    }),
    prisma.attempt.findFirst({
      where: { userId: user.id, status: { in: ["IN_PROGRESS", "PAUSED"] } },
      orderBy: { updatedAt: "desc" },
      select: { id: true, test: { select: { title: true } } },
    }),
    getSettings(),
    getAchievements(user.id),
    getLeaderboard("weekly", user.id, 3),
  ]);

  const firstName = user.name ? user.name.split(" ")[0] : "";
  const streak = profile?.currentStreak ?? 0;
  const proposal = proposals[0]?.status ?? null;

  const paths: PathCard[] = [
    {
      key: "research",
      icon: FlaskConical,
      tint: "bg-[hsl(190_84%_42%)]/10 text-[hsl(190_84%_42%)]",
      title: "Research programme",
      status:
        proposal === "ACCEPTED"
          ? "Your project is accepted"
          : proposal === "PENDING"
            ? "Your proposal is under review"
            : proposal === "REJECTED"
              ? "Ready for a new proposal"
              : "Investigate a question you care about",
      cta: proposal === "ACCEPTED" ? "Open your project" : proposal === "PENDING" ? "View proposal" : "Propose a topic",
      href: "/research",
      highlight: proposal === "ACCEPTED",
    },
    {
      key: "ap",
      icon: Award,
      tint: "bg-success/10 text-success",
      title: "AP courses",
      status:
        apEnrollments > 0
          ? `${apEnrollments} subject${apEnrollments === 1 ? "" : "s"} on your list`
          : "Practise AP subjects unit by unit",
      cta: apEnrollments > 0 ? "Continue AP practice" : "Pick your subjects",
      href: "/ap",
    },
    {
      key: "mentorship",
      icon: UserRound,
      tint: "bg-primary/10 text-primary",
      title: "Mentorship",
      status: upcomingSession
        ? `Next session ${upcomingSession.slot.startsAt.toLocaleDateString("en-US", {
            weekday: "short",
            month: "short",
            day: "numeric",
            timeZone: "UTC",
          })}`
        : "Book a free 1-on-1 session",
      cta: upcomingSession ? "My sessions" : "Book a session",
      href: upcomingSession ? "/bookings" : "/booking",
    },
    {
      key: "ielts",
      icon: Languages,
      tint: "bg-[hsl(266_84%_60%)]/10 text-[hsl(266_84%_60%)]",
      title: "IELTS",
      status: exam?.hasIelts ? "Writing and Speaking practice" : "Add IELTS preparation any time",
      cta: exam?.hasIelts ? "Open IELTS" : "Explore IELTS",
      href: "/ielts",
    },
    {
      key: "events",
      icon: CalendarRange,
      tint: "bg-warning/15 text-warning",
      title: "Events & classes",
      status: "Financial literacy classes and lectures",
      cta: "See events",
      href: "/events",
    },
    {
      key: "community",
      icon: MessagesSquare,
      tint: "bg-[hsl(340_78%_56%)]/10 text-[hsl(340_78%_56%)]",
      title: "Community",
      status: "Talk with other students",
      cta: "Open community",
      href: "/community",
    },
  ];

  return (
    <div className="space-y-8">
      <ScenicHeader
        theme="dashboard"
        priority
        contentClassName="flex min-h-[176px] flex-col justify-end sm:min-h-[200px]"
      >
        <div className="flex flex-wrap items-end justify-between gap-3">
          <div>
            <h1 className="font-display text-2xl font-semibold tracking-tight drop-shadow-sm sm:text-3xl">
              Welcome back{firstName ? `, ${firstName}` : ""}
            </h1>
            <p className="mt-1 text-sm text-white/85 drop-shadow-sm">What would you like to work on today?</p>
          </div>
          {streak > 0 && (
            <span className="flex items-center gap-1.5 rounded-full bg-white/15 px-3 py-1.5 text-sm font-semibold text-white backdrop-blur-sm">
              <Flame className="h-4 w-4 text-amber-300" />
              {streak}-day streak
            </span>
          )}
        </div>
      </ScenicHeader>

      <section aria-labelledby="paths-heading" className="space-y-4">
        <h2 id="paths-heading" className="font-display text-lg font-semibold tracking-tight">
          Your programmes
        </h2>
        <div className="stagger grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {paths.map((p) => (
            <PathTile key={p.key} card={p} />
          ))}
        </div>
      </section>

      <div className="stagger grid gap-4 md:grid-cols-2">
        <DashboardAchievementsCard
          unlocked={achievements.unlocked}
          nextUp={achievements.nextUp}
          unlockedCount={achievements.unlockedCount}
          totalCount={achievements.totalCount}
        />
        <DashboardLeaderboardCard
          rows={weeklyBoard.rows}
          myRank={weeklyBoard.rows.find((r) => r.isMe)?.rank ?? weeklyBoard.me?.rank ?? null}
          participants={weeklyBoard.participants}
        />
      </div>

      <div className="stagger grid gap-4 md:grid-cols-2">
        <DashboardCoinsCard balance={coinUser?.coinBalance ?? 0} referralReward={settings.referralRewardCoins} />
        {upcomingSession && (
          <DashboardSessionCard
            startsAt={upcomingSession.slot.startsAt}
            durationMinutes={upcomingSession.slot.durationMinutes}
            meetingUrl={upcomingSession.meetingUrl}
          />
        )}
      </div>

      {/* SAT practice — one card among the programmes, last. */}
      <Card>
        <CardContent className="flex flex-wrap items-center justify-between gap-4 p-5">
          <div className="flex items-center gap-3">
            <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-secondary text-muted-foreground">
              <BookOpen className="h-5 w-5" />
            </span>
            <div>
              <p className="text-sm font-semibold">SAT practice</p>
              <p className="text-sm text-muted-foreground">
                {satInProgress
                  ? `In progress: ${satInProgress.test.title}`
                  : satLatest?.totalScaledScore != null
                    ? `Latest full-length score: ${satLatest.totalScaledScore}`
                    : "Full-length adaptive tests, a question bank and analytics"}
              </p>
            </div>
          </div>
          <Link
            href={satInProgress ? `/exam/${satInProgress.id}` : "/sat"}
            className="inline-flex items-center gap-1 text-sm font-medium text-primary hover:underline"
          >
            {satInProgress ? "Resume test" : "Open SAT practice"} <ArrowRight className="h-3.5 w-3.5" />
          </Link>
        </CardContent>
      </Card>
    </div>
  );
}

interface PathCard {
  key: string;
  icon: typeof FlaskConical;
  tint: string;
  title: string;
  status: string;
  cta: string;
  href: string;
  highlight?: boolean;
}

function PathTile({ card }: { card: PathCard }) {
  const Icon = card.icon;
  return (
    <Link
      href={card.href}
      className={cn(
        "lift group flex h-full flex-col rounded-2xl border bg-card p-5 shadow-soft transition-colors hover:border-foreground/20 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
        card.highlight ? "border-success/40" : "border-border",
      )}
    >
      <span className={cn("flex h-10 w-10 items-center justify-center rounded-xl", card.tint)}>
        <Icon className="h-5 w-5" />
      </span>
      <p className="mt-4 font-display text-base font-semibold tracking-tight">{card.title}</p>
      <p className="mt-1 flex-1 text-sm text-muted-foreground">{card.status}</p>
      <span className="mt-4 inline-flex items-center gap-1 text-sm font-medium text-primary">
        {card.cta}
        <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5" />
      </span>
    </Link>
  );
}
