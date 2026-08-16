import Link from "next/link";
import {
  Headphones, BookOpenText, PenLine, Mic, ArrowRight,
  CheckCircle2, LineChart, UserCheck,
} from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { formatBand, PRACTICE_DISCLAIMER } from "@/lib/ielts/bands";
import { REVIEWER_CLAIM, SKILL_SHAPE } from "@/lib/ielts/constants";

export const metadata = { title: "IELTS Academic — Overview" };
export const dynamic = "force-dynamic";

const SKILL_ICON = {
  LISTENING: Headphones,
  READING: BookOpenText,
  WRITING: PenLine,
  SPEAKING: Mic,
} as const;

export default async function IeltsLandingPage() {
  const user = await requireUser();

  const [publishedCount, latest] = await Promise.all([
    prisma.ieltsTest.count({ where: { status: "PUBLISHED", module: "ACADEMIC" } }),
    prisma.ieltsAttempt.findFirst({
      where: { userId: user.id },
      orderBy: { createdAt: "desc" },
      select: {
        id: true, overallBand: true, listeningBand: true,
        readingBand: true, writingBand: true, speakingBand: true, status: true,
      },
    }),
  ]);

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
            IELTS Academic
          </h1>
          <p className="max-w-2xl text-base text-muted-foreground">
            Prepare for IELTS with realistic practice, full-length tests, and completely
            free human feedback.
          </p>
        </div>
        <div className="flex flex-wrap gap-3">
          <Button asChild size="lg">
            <Link href="/ielts/tests">
              Start practising <ArrowRight className="ml-1 h-4 w-4" />
            </Link>
          </Button>
          <Button asChild variant="outline" size="lg">
            <Link href="/ielts/resources">Test format and band descriptors</Link>
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
                {latest.overallBand != null
                  ? `Estimated overall band ${formatBand(latest.overallBand)}`
                  : "In progress"}
              </p>
            </div>
            <Button asChild variant="outline">
              <Link href="/ielts/progress">View progress</Link>
            </Button>
          </CardContent>
        </Card>
      )}

      <section className="space-y-4">
        <h2 className="font-display text-xl font-semibold">The four components</h2>
        <div className="grid gap-4 sm:grid-cols-2">
          {(["LISTENING", "READING", "WRITING", "SPEAKING"] as const).map((skill) => {
            const shape = SKILL_SHAPE[skill];
            const Icon = SKILL_ICON[skill];
            return (
              <Card key={skill} className="lift">
                <CardHeader className="flex flex-row items-center gap-3 space-y-0">
                  <span className="flex h-9 w-9 items-center justify-center rounded-lg bg-navy-900 text-white">
                    <Icon className="h-4 w-4" />
                  </span>
                  <CardTitle className="text-base">{shape.label}</CardTitle>
                </CardHeader>
                <CardContent className="space-y-3">
                  <p className="text-sm text-muted-foreground">{shape.blurb}</p>
                  <div className="flex flex-wrap gap-2 text-xs">
                    <Badge variant="outline">
                      {shape.parts} {shape.partNoun}
                    </Badge>
                    {shape.questions && (
                      <Badge variant="outline">{shape.questions} questions</Badge>
                    )}
                    <Badge variant="outline">
                      {skill === "SPEAKING" ? "11–14 min" : `${shape.minutes} min`}
                    </Badge>
                  </div>
                </CardContent>
              </Card>
            );
          })}
        </div>
      </section>

      {/* The differentiator. Deliberately describes the band the reviewer
          achieved rather than any examiner status, which SATForge cannot
          verify and does not claim. */}
      <section className="space-y-4 rounded-2xl border border-emerald-600/25 bg-emerald-50/60 p-6 dark:bg-emerald-950/20">
        <div className="flex flex-wrap items-center gap-2">
          <UserCheck className="h-5 w-5 text-emerald-700" />
          <h2 className="font-display text-xl font-semibold">Free human feedback</h2>
          <Badge className="bg-emerald-600 text-white hover:bg-emerald-600">$0</Badge>
        </div>
        <p className="max-w-2xl text-sm text-muted-foreground">
          Submit your Writing and Speaking practice and get feedback from experienced
          high-scoring reviewers. No subscription, no credits, no hidden fees, no
          premium tier.
        </p>
        <div className="grid gap-3 sm:grid-cols-2">
          <div className="rounded-xl border border-border bg-card p-4">
            <p className="text-sm font-semibold">Writing</p>
            <p className="text-sm text-muted-foreground">{REVIEWER_CLAIM.WRITING}.</p>
          </div>
          <div className="rounded-xl border border-border bg-card p-4">
            <p className="text-sm font-semibold">Speaking</p>
            <p className="text-sm text-muted-foreground">{REVIEWER_CLAIM.SPEAKING}.</p>
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
            "Full-length IELTS Academic practice tests",
            "Computer-style Listening with single-play audio",
            "Computer-style Reading with a split passage and question pane",
            "Timed Writing with a live word count",
            "Three-part Speaking practice you record and submit",
            "Human Writing feedback, free",
            "Human Speaking feedback, free",
            "Progress tracking and estimated band scores",
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
            <LineChart className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-2xl font-semibold">{publishedCount}</p>
            <p className="text-sm text-muted-foreground">
              published {publishedCount === 1 ? "paper" : "papers"}
            </p>
          </CardContent>
        </Card>
        <Card className="sm:col-span-2">
          <CardContent className="flex h-full flex-col justify-center gap-2 py-5">
            <p className="text-sm font-medium">Bands 0.0 to 9.0</p>
            <p className="text-sm text-muted-foreground">
              Listening and Reading are marked automatically. Writing and Speaking are
              scored by a human reviewer against the four official criteria.
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
