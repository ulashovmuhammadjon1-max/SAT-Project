import Link from "next/link";
import { PenLine } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { REVIEWER_CLAIM } from "@/lib/ielts/constants";
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

  const [papers, submissions] = await Promise.all([
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
  ]);

  // Latest submission per task, so a card shows where that task stands.
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
          Free · {REVIEWER_CLAIM.WRITING}
        </Badge>
      </div>

      {papers.map((paper) => (
        <section key={paper.id} className="space-y-3">
          <h2 className="font-display text-lg font-semibold">{paper.title}</h2>
          <div className="grid gap-3 sm:grid-cols-2">
            {paper.sections.flatMap((s) => s.parts).map((part) => {
              const sub = byPart.get(part.id);
              const band = sub?.review?.overallBand;
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
                      <Badge variant="outline">
                        minimum {part.minWords ?? (part.partNumber === 1 ? 150 : 250)} words
                      </Badge>
                      <Badge variant="outline">
                        about {part.partNumber === 1 ? 20 : 40} minutes
                      </Badge>
                    </div>
                    <Button asChild variant={sub ? "outline" : "default"}>
                      <Link href={`/ielts/writing/${part.id}`}>
                        {!sub ? "Start writing"
                          : sub.status === "PENDING" ? "Continue draft"
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
