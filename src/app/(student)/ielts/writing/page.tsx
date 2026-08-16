import Link from "next/link";
import { PenLine, Sparkles, Timer } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { getReviewAllowance } from "@/lib/ielts/economy";
import { ReviewBalance } from "@/components/ielts/review-balance";
import { REVIEWER_CLAIM, WRITING_SUGGESTED_MINUTES } from "@/lib/ielts/constants";
import { formatBand } from "@/lib/ielts/bands";

export const metadata = { title: "IELTS Writing" };
export const dynamic = "force-dynamic";

const STATUS_LABEL: Record<string, string> = {
  PENDING: "Draft",
  ASSIGNED: "Waiting for reviewer",
  IN_REVIEW: "Under review",
  COMPLETE: "Reviewed",
  RETURNED: "Returned",
};

export default async function IeltsWritingPage() {
  const user = await requireUser();

  const [papers, submissions, allowance] = await Promise.all([
    prisma.ieltsTest.findMany({
      where: { status: "PUBLISHED", sections: { some: { skill: "WRITING" } } },
      orderBy: { title: "asc" },
      include: {
        sections: {
          where: { skill: "WRITING" },
          include: { parts: { orderBy: { partNumber: "asc" } } },
        },
      },
    }),
    prisma.ieltsWritingSubmission.findMany({
      where: { userId: user.id },
      orderBy: { submittedAt: "desc" },
      include: { review: { select: { overallBand: true } } },
    }),
    getReviewAllowance(user.id),
  ]);

  // The student's own topics. Unpublished, so they never reach the list above;
  // reachable here through the attempt that proves they created them.
  const mine = await prisma.ieltsTest.findMany({
    where: {
      status: { not: "PUBLISHED" },
      attempts: { some: { userId: user.id } },
      sections: { some: { skill: "WRITING" } },
    },
    orderBy: { createdAt: "desc" },
    include: {
      sections: {
        where: { skill: "WRITING" },
        include: { parts: { orderBy: { partNumber: "asc" } } },
      },
    },
  });

  // Latest submission per task, so each card shows where that task stands.
  const byPart = new Map<string, (typeof submissions)[number]>();
  for (const s of submissions) if (!byPart.has(s.partId)) byPart.set(s.partId, s);

  return (
    <div className="space-y-8">
      <div className="space-y-2">
        <h1 className="font-display text-2xl font-semibold tracking-tight">IELTS Writing</h1>
        <p className="max-w-2xl text-sm text-muted-foreground">
          Two tasks per paper. Write your response, submit it, and a human reviewer scores it
          against the four official criteria and writes you feedback.
        </p>
        <Badge variant="outline" className="border-emerald-600/40 text-emerald-700">
          Free &middot; {REVIEWER_CLAIM.WRITING}
        </Badge>
      </div>

      <ReviewBalance allowance={allowance} />

      {/* Bring your own question. Deliberately above the published papers: a
          student with a question from their teacher wants that one marked,
          not whichever two happen to be published here. */}
      <Card className="border-dashed">
        <CardContent className="flex flex-wrap items-center justify-between gap-4 py-5">
          <div className="flex items-start gap-3">
            <Sparkles className="mt-0.5 h-5 w-5 shrink-0 text-muted-foreground" />
            <div>
              <p className="text-sm font-semibold">Write on your own topic</p>
              <p className="text-sm text-muted-foreground">
                Bring the question your teacher set or one from a past paper. Task 1 needs its
                chart or diagram uploaded with it.
              </p>
            </div>
          </div>
          <Button asChild variant="outline">
            <Link href="/ielts/writing/custom">Choose a topic</Link>
          </Button>
        </CardContent>
      </Card>

      {mine.length > 0 && (
        <section className="space-y-3">
          <h2 className="font-display text-lg font-semibold">Your own topics</h2>
          <div className="grid gap-3 sm:grid-cols-2">
            {mine.map((paper) => {
              const parts = paper.sections.flatMap((s) => s.parts);
              const done = parts.filter((p) => {
                const sub = byPart.get(p.id);
                return sub && sub.status !== "PENDING";
              }).length;
              const band = parts
                .map((p) => byPart.get(p.id)?.review?.overallBand)
                .find((b) => b != null);
              return (
                <Card key={paper.id} className="flex flex-col">
                  <CardHeader className="flex flex-row items-center justify-between space-y-0">
                    <CardTitle className="flex items-center gap-2 text-base">
                      <Sparkles className="h-4 w-4 text-muted-foreground" />
                      {paper.title}
                    </CardTitle>
                    {band != null && <Badge variant="navy">Band {formatBand(band)}</Badge>}
                  </CardHeader>
                  <CardContent className="flex flex-1 flex-col justify-between gap-3">
                    <div className="flex flex-wrap gap-2 text-xs text-muted-foreground">
                      <Badge variant="outline">
                        {parts.length === 1 ? "1 task" : `${parts.length} tasks`}
                      </Badge>
                      {done > 0 && (
                        <Badge variant="outline">
                          {done} of {parts.length} sent
                        </Badge>
                      )}
                    </div>
                    <Button asChild variant={done > 0 ? "outline" : "default"}>
                      <Link
                        href={
                          parts.length > 1
                            ? `/ielts/writing/full/${paper.id}`
                            : `/ielts/writing/${parts[0]?.id}`
                        }
                      >
                        {done === parts.length ? "View response" : done > 0 ? "Continue" : "Start writing"}
                      </Link>
                    </Button>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </section>
      )}

      {papers.map((paper) => (
        <section key={paper.id} className="space-y-3">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <h2 className="font-display text-lg font-semibold">{paper.title}</h2>
            {/* One sitting, both tasks, one clock — the thing the separate
                task cards below cannot rehearse, which is budgeting sixty
                minutes across a short report and a longer essay. */}
            {paper.sections.flatMap((s) => s.parts).length > 1 && (
              <Button asChild size="sm">
                <Link href={`/ielts/writing/full/${paper.id}`}>
                  <Timer className="mr-1.5 h-3.5 w-3.5" />
                  Full practice &middot; 60 min
                </Link>
              </Button>
            )}
          </div>
          <div className="grid gap-3 sm:grid-cols-2">
            {paper.sections.flatMap((s) => s.parts).map((part) => {
              const sub = byPart.get(part.id);
              const band = sub?.review?.overallBand;
              const minWords = part.minWords ?? (part.partNumber === 1 ? 150 : 250);
              return (
                <Card key={part.id} className="flex flex-col">
                  <CardHeader className="flex flex-row items-center justify-between space-y-0">
                    <CardTitle className="flex items-center gap-2 text-base">
                      <PenLine className="h-4 w-4 text-muted-foreground" />
                      {part.title ?? `Task ${part.partNumber}`}
                    </CardTitle>
                    {sub && (
                      <Badge variant={sub.status === "COMPLETE" ? "navy" : "outline"}>
                        {band != null ? `Band ${formatBand(band)}` : STATUS_LABEL[sub.status]}
                      </Badge>
                    )}
                  </CardHeader>
                  <CardContent className="flex flex-1 flex-col justify-between gap-3">
                    <div className="flex flex-wrap gap-2 text-xs text-muted-foreground">
                      <Badge variant="outline">minimum {minWords} words</Badge>
                      <Badge variant="outline">
                        about {WRITING_SUGGESTED_MINUTES[part.partNumber] ?? 40} minutes
                      </Badge>
                    </div>
                    <Button asChild variant={sub ? "outline" : "default"}>
                      <Link href={`/ielts/writing/${part.id}`}>
                        {!sub
                          ? "Start writing"
                          : sub.status === "PENDING"
                            ? "Continue draft"
                            : "View response"}
                      </Link>
                    </Button>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </section>
      ))}

      {papers.length === 0 && (
        <Card>
          <CardContent className="py-10 text-center text-sm text-muted-foreground">
            No Writing papers are published yet.
          </CardContent>
        </Card>
      )}
    </div>
  );
}
