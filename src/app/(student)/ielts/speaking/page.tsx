import Link from "next/link";
import { Mic } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { REVIEWER_CLAIM, SPEAKING_PRODUCT_NAME } from "@/lib/ielts/constants";
import { formatBand } from "@/lib/ielts/bands";

export const metadata = { title: "IELTS Speaking" };
export const dynamic = "force-dynamic";

const STATUS_LABEL: Record<string, string> = {
  PENDING: "In progress",
  ASSIGNED: "Waiting for reviewer",
  IN_REVIEW: "Under review",
  COMPLETE: "Reviewed",
  RETURNED: "Returned",
};

export default async function IeltsSpeakingPage() {
  const user = await requireUser();

  const [papers, submissions] = await Promise.all([
    prisma.ieltsTest.findMany({
      where: { status: "PUBLISHED", sections: { some: { skill: "SPEAKING" } } },
      orderBy: { title: "asc" },
      include: {
        sections: {
          where: { skill: "SPEAKING" },
          include: { parts: { orderBy: { partNumber: "asc" } } },
        },
      },
    }),
    prisma.ieltsSpeakingSubmission.findMany({
      where: { userId: user.id },
      orderBy: { submittedAt: "desc" },
      include: {
        review: { select: { overallBand: true } },
        attempt: { select: { testId: true } },
        _count: { select: { recordings: true } },
      },
    }),
  ]);

  const byTest = new Map<string, (typeof submissions)[number]>();
  for (const s of submissions) {
    if (!byTest.has(s.attempt.testId)) byTest.set(s.attempt.testId, s);
  }

  return (
    <div className="space-y-8">
      <div className="space-y-2">
        <h1 className="font-display text-2xl font-semibold tracking-tight">
          {SPEAKING_PRODUCT_NAME}
        </h1>
        <p className="max-w-2xl text-sm text-muted-foreground">
          Three parts, recorded in your browser. A human reviewer listens to your answers and
          scores them against the four official criteria.
        </p>
        <Badge variant="outline" className="border-emerald-600/40 text-emerald-700">
          Free &middot; {REVIEWER_CLAIM.SPEAKING}
        </Badge>
      </div>

      <div className="grid gap-3 sm:grid-cols-2">
        {papers.map((paper) => {
          const parts = paper.sections.flatMap((s) => s.parts);
          const sub = byTest.get(paper.id);
          const band = sub?.review?.overallBand;
          return (
            <Card key={paper.id} className="flex flex-col">
              <CardHeader className="flex flex-row items-center justify-between space-y-0">
                <CardTitle className="flex items-center gap-2 text-base">
                  <Mic className="h-4 w-4 text-muted-foreground" />
                  {paper.title}
                </CardTitle>
                {sub && (
                  <Badge variant={sub.status === "COMPLETE" ? "navy" : "outline"}>
                    {band != null ? `Band ${formatBand(band)}` : STATUS_LABEL[sub.status]}
                  </Badge>
                )}
              </CardHeader>
              <CardContent className="flex flex-1 flex-col justify-between gap-3">
                <div className="flex flex-wrap gap-2 text-xs text-muted-foreground">
                  <Badge variant="outline">{parts.length} parts</Badge>
                  <Badge variant="outline">11&ndash;14 min</Badge>
                  {sub && <Badge variant="outline">{sub._count.recordings} answers recorded</Badge>}
                </div>
                <Button asChild variant={sub ? "outline" : "default"}>
                  <Link href={`/ielts/speaking/${paper.id}`}>
                    {!sub ? "Start speaking test"
                      : sub.status === "PENDING" ? "Continue"
                      : "View submission"}
                  </Link>
                </Button>
              </CardContent>
            </Card>
          );
        })}
      </div>

      {papers.length === 0 && (
        <Card>
          <CardContent className="py-10 text-center text-sm text-muted-foreground">
            No Speaking papers are published yet.
          </CardContent>
        </Card>
      )}
    </div>
  );
}
