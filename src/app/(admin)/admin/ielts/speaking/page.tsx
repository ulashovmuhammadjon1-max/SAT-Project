import Link from "next/link";
import { Mic } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import { formatBand } from "@/lib/ielts/bands";

export const metadata = { title: "Speaking Reviews" };
export const dynamic = "force-dynamic";

export default async function SpeakingQueuePage() {
  await requireAdmin();

  const submissions = await prisma.ieltsSpeakingSubmission.findMany({
    // A draft the student is still writing is not review work.
    where: { status: { not: "PENDING" } },
    orderBy: [{ status: "asc" }, { submittedAt: "asc" }],
    include: {
      user: { select: { name: true, email: true } },
      review: { select: { overallBand: true } },
      attempt: { select: { test: { select: { title: true } } } },
      _count: { select: { recordings: true } },
    },
  });


  const waiting = submissions.filter((s) => s.status !== "COMPLETE");
  const done = submissions.filter((s) => s.status === "COMPLETE");

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Speaking Reviews</h1>
        <p className="text-sm text-muted-foreground">
          {waiting.length} waiting &middot; {done.length} completed
        </p>
      </div>

      {[["Waiting for review", waiting], ["Completed", done]].map(([title, rows]) => (
        <section key={title as string} className="space-y-2">
          <h2 className="text-sm font-semibold uppercase tracking-wide text-muted-foreground">
            {title as string}
          </h2>
          {(rows as typeof submissions).length === 0 ? (
            <Card><CardContent className="py-8 text-center text-sm text-muted-foreground">
              Nothing here.
            </CardContent></Card>
          ) : (
            <div className="space-y-2">
              {(rows as typeof submissions).map((s) => {
                return (
                  <Link key={s.id} href={`/admin/ielts/speaking/${s.id}`} className="block">
                    <Card className="transition-colors hover:border-navy-900/30">
                      <CardContent className="flex flex-wrap items-center justify-between gap-3 py-4">
                        <div className="space-y-1">
                          <p className="flex items-center gap-2 text-sm font-semibold">
                            <Mic className="h-4 w-4 text-muted-foreground" />
                            {s.user.name ?? s.user.email}
                          </p>
                          <p className="text-xs text-muted-foreground">
                            {s.attempt.test.title} &middot;{" "}
                            {s._count.recordings} recordings &middot;{" "}
                            {new Date(s.submittedAt).toLocaleDateString()}
                          </p>
                        </div>
                        <Badge variant={s.status === "COMPLETE" ? "navy" : "outline"}>
                          {s.review?.overallBand != null
                            ? `Band ${formatBand(s.review.overallBand)}`
                            : s.status}
                        </Badge>
                      </CardContent>
                    </Card>
                  </Link>
                );
              })}
            </div>
          )}
        </section>
      ))}
    </div>
  );
}
