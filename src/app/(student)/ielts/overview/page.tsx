import Link from "next/link";
import { ArrowRight, CheckCircle2, Mic, PenLine, UserCheck } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { formatBand, PRACTICE_DISCLAIMER } from "@/lib/ielts/bands";
import {
  REVIEWER_CLAIM, SPEAKING_PART2_PREP_SECONDS, WRITING_SUGGESTED_MINUTES,
} from "@/lib/ielts/constants";

export const metadata = { title: "IELTS Academic — Overview" };
export const dynamic = "force-dynamic";

/**
 * What a student sees before they have opened the IELTS side.
 *
 * It describes Writing and Speaking and nothing else. An earlier version
 * advertised all four components and linked to a test list, a resources page
 * and a progress page — none of which exist any more. A landing page promising
 * sections that 404 is worse than a short one, and it is the first thing a new
 * student reads.
 */
export default async function IeltsLandingPage() {
  const user = await requireUser();

  const [writingPapers, speakingPapers, latest] = await Promise.all([
    prisma.ieltsTest.count({
      where: { status: "PUBLISHED", sections: { some: { skill: "WRITING" } } },
    }),
    prisma.ieltsTest.count({
      where: { status: "PUBLISHED", sections: { some: { skill: "SPEAKING" } } },
    }),
    prisma.ieltsAttempt.findFirst({
      where: { userId: user.id },
      orderBy: { createdAt: "desc" },
      select: { id: true, writingBand: true, speakingBand: true, status: true },
    }),
  ]);

  // Whichever band came back most recently — there is no overall band here,
  // because an overall band needs all four components and this product has two.
  const recent = latest?.writingBand ?? latest?.speakingBand ?? null;

  return (
    <div className="space-y-10">
      <section className="space-y-5">
        <div className="flex flex-wrap items-center gap-2">
          <Badge variant="navy">IELTS Academic</Badge>
          <Badge variant="outline" className="border-emerald-600/40 text-emerald-700">
            100% free
          </Badge>
        </div>
        <div className="space-y-3">
          <h1 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">
            IELTS Writing and Speaking
          </h1>
          <p className="max-w-2xl text-base text-muted-foreground">
            Write a task or record an interview, send it, and a human reads or listens to it
            and scores you against the four official criteria. No subscription, no credits,
            no premium tier.
          </p>
        </div>
        <div className="flex flex-wrap gap-3">
          <Button asChild size="lg">
            <Link href="/ielts/writing">
              Start a Writing task <ArrowRight className="ml-1 h-4 w-4" />
            </Link>
          </Button>
          <Button asChild variant="outline" size="lg">
            <Link href="/ielts/speaking">Record a Speaking test</Link>
          </Button>
        </div>
      </section>

      {latest && (
        <Card className="border-navy-900/15 bg-secondary/40">
          <CardContent className="flex flex-wrap items-center justify-between gap-4 py-5">
            <div>
              <p className="text-xs uppercase tracking-wide text-muted-foreground">
                Your most recent practice
              </p>
              <p className="font-display text-2xl font-semibold">
                {recent != null ? `Band ${formatBand(recent)}` : "Waiting for your reviewer"}
              </p>
            </div>
            <Button asChild variant="outline">
              <Link href="/ielts/feedback">Open feedback</Link>
            </Button>
          </CardContent>
        </Card>
      )}

      <section className="space-y-4">
        <h2 className="font-display text-xl font-semibold">The two skills a human marks</h2>
        <div className="grid gap-4 sm:grid-cols-2">
          <Card className="lift">
            <CardHeader className="flex flex-row items-center gap-3 space-y-0">
              <span className="flex h-9 w-9 items-center justify-center rounded-lg bg-navy-900 text-white">
                <PenLine className="h-4 w-4" />
              </span>
              <CardTitle className="text-base">Writing</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3">
              <p className="text-sm text-muted-foreground">
                Task 1 describes visual information; Task 2 argues a position and counts twice
                towards the band. A full-screen room with the task beside your answer and a
                live word count.
              </p>
              <div className="flex flex-wrap gap-2 text-xs">
                <Badge variant="outline">2 tasks</Badge>
                <Badge variant="outline">
                  {(WRITING_SUGGESTED_MINUTES[1] ?? 20) + (WRITING_SUGGESTED_MINUTES[2] ?? 40)} min
                </Badge>
                <Badge variant="outline">150 + 250 words</Badge>
              </div>
            </CardContent>
          </Card>

          <Card className="lift">
            <CardHeader className="flex flex-row items-center gap-3 space-y-0">
              <span className="flex h-9 w-9 items-center justify-center rounded-lg bg-navy-900 text-white">
                <Mic className="h-4 w-4" />
              </span>
              <CardTitle className="text-base">Speaking</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3">
              <p className="text-sm text-muted-foreground">
                One question at a time, recorded in your browser. Part 2 gives you{" "}
                {SPEAKING_PART2_PREP_SECONDS} seconds with the cue card before recording starts.
                You do not see the next question until you have answered the one in front of you.
              </p>
              <div className="flex flex-wrap gap-2 text-xs">
                <Badge variant="outline">3 parts</Badge>
                <Badge variant="outline">11–14 min</Badge>
                <Badge variant="outline">recorded</Badge>
              </div>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* The differentiator. Deliberately describes the band the reviewer
          achieved rather than any examiner status, which Scholarly cannot
          verify and does not claim. */}
      <section className="space-y-4 rounded-2xl border border-emerald-600/25 bg-emerald-50/60 p-6 dark:bg-emerald-950/20">
        <div className="flex flex-wrap items-center gap-2">
          <UserCheck className="h-5 w-5 text-emerald-700" />
          <h2 className="font-display text-xl font-semibold">Free human feedback</h2>
          <Badge className="bg-emerald-600 text-white hover:bg-emerald-600">$0</Badge>
        </div>
        <p className="max-w-2xl text-sm text-muted-foreground">
          Every submission is scored by a person against the four official criteria, with a
          written note on each one saying what you did and what would move that band up.
        </p>
        <div className="grid gap-3 sm:grid-cols-2">
          <div className="rounded-xl border border-border bg-card p-4">
            <p className="text-sm font-semibold">Writing</p>
            <p className="text-sm text-muted-foreground">{REVIEWER_CLAIM.WRITING}.</p>
            <p className="mt-2 text-xs text-muted-foreground">
              Task Achievement / Response &middot; Coherence and Cohesion &middot; Lexical
              Resource &middot; Grammatical Range and Accuracy
            </p>
          </div>
          <div className="rounded-xl border border-border bg-card p-4">
            <p className="text-sm font-semibold">Speaking</p>
            <p className="text-sm text-muted-foreground">{REVIEWER_CLAIM.SPEAKING}.</p>
            <p className="mt-2 text-xs text-muted-foreground">
              Fluency and Coherence &middot; Lexical Resource &middot; Grammatical Range and
              Accuracy &middot; Pronunciation
            </p>
          </div>
        </div>
        <p className="text-xs text-muted-foreground">
          This is human IELTS practice feedback, not official IELTS scoring.
        </p>
      </section>

      <section className="space-y-4">
        <h2 className="font-display text-xl font-semibold">What you get</h2>
        <ul className="grid gap-2 sm:grid-cols-2">
          {[
            "A full-screen Writing room with the task beside your answer",
            "Autosaved drafts, so a closed tab is not a lost essay",
            "A live word count against the task minimum",
            "Speaking one cue card at a time, with no reading ahead",
            "Playback of every take before you send it",
            "A band on all four criteria, with a note on each",
            "A reviewer's overall band, not just an average",
            "A leaderboard across everyone practising",
          ].map((item) => (
            <li key={item} className="flex items-start gap-2 text-sm">
              <CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0 text-emerald-600" />
              <span>{item}</span>
            </li>
          ))}
        </ul>
      </section>

      <section className="grid gap-4 sm:grid-cols-3">
        <Card>
          <CardContent className="space-y-1 py-5">
            <PenLine className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-2xl font-semibold">{writingPapers}</p>
            <p className="text-sm text-muted-foreground">
              Writing {writingPapers === 1 ? "paper" : "papers"}
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="space-y-1 py-5">
            <Mic className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-2xl font-semibold">{speakingPapers}</p>
            <p className="text-sm text-muted-foreground">
              Speaking {speakingPapers === 1 ? "paper" : "papers"}
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="flex h-full flex-col justify-center gap-2 py-5">
            <p className="text-sm font-medium">Bands 0.0 to 9.0</p>
            <p className="text-sm text-muted-foreground">
              Each criterion is marked in whole bands; the halves appear when the four are
              combined.
            </p>
          </CardContent>
        </Card>
      </section>

      <p className="border-t border-border pt-4 text-xs text-muted-foreground">
        {PRACTICE_DISCLAIMER}
      </p>
    </div>
  );
}
