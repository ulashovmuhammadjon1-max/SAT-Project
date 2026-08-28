import Link from "next/link";

import { AppReturnBar } from "@/components/marketing/app-return-bar";
import { SiteNav } from "@/components/marketing/site-nav";
import { getCurrentUser } from "@/lib/session";
import { countedStudentWhere } from "@/lib/counted-students";
import { prisma } from "@/lib/prisma";

export const metadata = {
  title: "Impact",
  description: "Live, verifiable numbers from the Scholarly platform — students, countries, tests, questions.",
};

/**
 * Public, self-updating proof of scale.
 *
 * Every number on this page is computed from the live database on render —
 * nothing is typed in, so nothing can quietly go stale or get inflated. That
 * is the whole point: a claim anyone can check is worth more than a bigger
 * claim nobody can. Rendered per request so a signed-in visitor gets the
 * in-app return bar instead of the marketing nav.
 */
export const dynamic = "force-dynamic";

async function getImpact() {
  try {
    return await queryImpact();
  } catch (error) {
    // A build environment without a database must not fail the build; the
    // first real request after deploy regenerates this page with live numbers.
    console.error("[impact] falling back to placeholders", error);
    return null;
  }
}

async function queryImpact() {
  const [students, countries, testsCompleted, activity, questionsLive, sessionsHeld] =
    await Promise.all([
      prisma.user.count({ where: countedStudentWhere }),
      prisma.user
        .findMany({
          where: { ...countedStudentWhere, countryCode: { not: null } },
          select: { countryCode: true },
          distinct: ["countryCode"],
        })
        .then((rows) => rows.length),
      prisma.attempt.count({ where: { status: "SUBMITTED" } }),
      prisma.studyActivity.aggregate({
        _sum: { questionsAnswered: true, minutesStudied: true },
      }),
      prisma.question.count({ where: { isPublished: true } }),
      prisma.booking.count({ where: { status: "COMPLETED" } }),
    ]);

  return {
    students,
    countries,
    testsCompleted,
    questionsAnswered: activity._sum.questionsAnswered ?? 0,
    hoursStudied: Math.round((activity._sum.minutesStudied ?? 0) / 60),
    questionsLive,
    sessionsHeld,
  };
}

const fmt = (n: number) => n.toLocaleString("en-US");

export default async function ImpactPage() {
  const [d, user] = await Promise.all([getImpact(), getCurrentUser()]);

  const STATS: { value: string; label: string; sub: string }[] = [
    { value: d ? fmt(d.students) : "—", label: "Students", sub: "registered accounts" },
    { value: d ? fmt(d.countries) : "—", label: "Countries", sub: "represented by students" },
    { value: d ? fmt(d.testsCompleted) : "—", label: "Practice tests completed", sub: "full adaptive sittings" },
    { value: d ? fmt(d.questionsAnswered) : "—", label: "Questions answered", sub: "across all practice" },
    { value: d ? fmt(d.questionsLive) : "—", label: "Questions in the bank", sub: "authored and verified" },
    { value: d ? fmt(d.sessionsHeld) : "—", label: "1-on-1 sessions held", sub: "free mentorship" },
  ];

  return (
    <div className="min-h-screen bg-background">
      {user ? <AppReturnBar backHref="/dashboard" backLabel="Back to dashboard" /> : <SiteNav />}
      <main className="mx-auto w-full max-w-5xl px-4 py-16 sm:px-6 lg:px-8">
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-primary">Impact</p>
        <h1 className="mt-2 font-display text-3xl font-semibold tracking-tight sm:text-4xl">
          Numbers you can check
        </h1>
        <p className="mt-3 max-w-2xl text-[15px] leading-relaxed text-muted-foreground">
          Everything below is computed live from the platform&apos;s own database each hour —
          nothing on this page is typed in by hand, so nothing can be inflated. This is what free,
          community-built preparation actually adds up to.
        </p>

        <div className="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {STATS.map((s) => (
            <div
              key={s.label}
              className="rounded-2xl border border-border/70 bg-card p-6 shadow-soft"
            >
              <p className="bg-gradient-to-br from-primary to-[hsl(266_84%_60%)] bg-clip-text font-display text-4xl font-semibold tabular-nums tracking-tight text-transparent">
                {s.value}
              </p>
              <p className="mt-2 font-medium">{s.label}</p>
              <p className="text-sm text-muted-foreground">{s.sub}</p>
            </div>
          ))}
        </div>

        {!user && (
        <p className="mt-10 text-sm text-muted-foreground">
          Want to be part of it?{" "}
          <Link href="/onboarding" className="font-medium text-primary underline-offset-4 hover:underline">
            Create a free account
          </Link>{" "}
          — or{" "}
          <Link href="/" className="font-medium text-primary underline-offset-4 hover:underline">
            see what Scholarly is
          </Link>
          .
        </p>
        )}
      </main>
    </div>
  );
}
