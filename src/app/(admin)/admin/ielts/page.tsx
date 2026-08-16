import Link from "next/link";
import { Clock, Globe2, Mic, PenLine, UserPlus } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import { formatBand } from "@/lib/ielts/bands";
import { cn } from "@/lib/utils";

export const metadata = { title: "IELTS Admin" };
export const dynamic = "force-dynamic";

/**
 * The IELTS panel's front page.
 *
 * It opens on the work, not the content: what is waiting to be marked and how
 * long it has been waiting. The SAT overview leads with content because SAT
 * content is the work; here the content is four papers that rarely change and
 * the work is a queue that fills every day.
 */
export default async function AdminIeltsOverviewPage() {
  await requireAdmin();

  const [writingQueue, speakingQueue, writingDone, speakingDone, papers, oldest] =
    await Promise.all([
      prisma.ieltsWritingSubmission.count({ where: { status: { in: ["ASSIGNED", "IN_REVIEW"] } } }),
      prisma.ieltsSpeakingSubmission.count({ where: { status: { in: ["ASSIGNED", "IN_REVIEW"] } } }),
      prisma.ieltsWritingSubmission.count({ where: { status: "COMPLETE" } }),
      prisma.ieltsSpeakingSubmission.count({ where: { status: "COMPLETE" } }),
      prisma.ieltsTest.count({ where: { status: "PUBLISHED" } }),
      prisma.ieltsWritingSubmission.findFirst({
        where: { status: { in: ["ASSIGNED", "IN_REVIEW"] } },
        orderBy: { submittedAt: "asc" },
        select: { submittedAt: true },
      }),
    ]);

  const recent = await prisma.ieltsWritingReview.findMany({
    orderBy: { completedAt: "desc" },
    take: 8,
    select: {
      id: true, overallBand: true, completedAt: true,
      submission: { select: { user: { select: { name: true, email: true } } } },
    },
  });

  const waitingDays = oldest?.submittedAt
    ? Math.floor((Date.now() - new Date(oldest.submittedAt).getTime()) / 86_400_000)
    : null;

  const queue = writingQueue + speakingQueue;

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">IELTS</h1>
        <p className="text-sm text-muted-foreground">
          Writing and Speaking, marked by people. Everything else on this panel exists to
          keep that queue short.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <Link href="/admin/ielts/writing">
          <Card className={cn("lift h-full", writingQueue > 0 && "border-amber-500/40")}>
            <CardContent className="space-y-1 py-5">
              <PenLine className="h-4 w-4 text-muted-foreground" />
              <p className="font-display text-3xl font-semibold tabular-nums">{writingQueue}</p>
              <p className="text-sm text-muted-foreground">Writing tasks waiting</p>
            </CardContent>
          </Card>
        </Link>
        <Link href="/admin/ielts/speaking">
          <Card className={cn("lift h-full", speakingQueue > 0 && "border-amber-500/40")}>
            <CardContent className="space-y-1 py-5">
              <Mic className="h-4 w-4 text-muted-foreground" />
              <p className="font-display text-3xl font-semibold tabular-nums">{speakingQueue}</p>
              <p className="text-sm text-muted-foreground">Interviews waiting</p>
            </CardContent>
          </Card>
        </Link>
        <Card>
          <CardContent className="space-y-1 py-5">
            <Clock className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-3xl font-semibold tabular-nums">
              {waitingDays == null ? "—" : waitingDays}
            </p>
            <p className="text-sm text-muted-foreground">
              {waitingDays == null
                ? "nothing waiting"
                : `${waitingDays === 1 ? "day" : "days"} — oldest in the queue`}
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="space-y-1 py-5">
            <Globe2 className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-3xl font-semibold tabular-nums">
              {writingDone + speakingDone}
            </p>
            <p className="text-sm text-muted-foreground">reviews delivered</p>
          </CardContent>
        </Card>
      </div>

      {queue === 0 && (
        <Card>
          <CardContent className="py-8 text-center text-sm text-muted-foreground">
            Nothing is waiting to be marked. {papers} published{" "}
            {papers === 1 ? "paper" : "papers"} are live for students.
          </CardContent>
        </Card>
      )}

      <div className="grid gap-4 lg:grid-cols-2">
        <Card>
          <CardHeader className="pb-3">
            <CardTitle className="text-base">Recently marked</CardTitle>
          </CardHeader>
          <CardContent className="p-0">
            {recent.length ? (
              <ol>
                {recent.map((r) => (
                  <li
                    key={r.id}
                    className="flex items-center justify-between gap-3 border-b px-6 py-2.5 last:border-0"
                  >
                    <span className="truncate text-sm">
                      {r.submission.user.name ?? r.submission.user.email}
                    </span>
                    <span className="flex items-center gap-3">
                      <span className="hidden text-xs text-muted-foreground sm:inline">
                        {r.completedAt ? new Date(r.completedAt).toLocaleDateString() : ""}
                      </span>
                      <Badge variant="navy">Band {formatBand(r.overallBand)}</Badge>
                    </span>
                  </li>
                ))}
              </ol>
            ) : (
              <p className="p-8 text-center text-sm text-muted-foreground">
                No reviews have been delivered yet.
              </p>
            )}
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="pb-3">
            <CardTitle className="text-base">Where to go</CardTitle>
          </CardHeader>
          <CardContent className="space-y-2 text-sm">
            <Link href="/admin/ielts/writing" className="flex items-center gap-2 underline">
              <PenLine className="h-3.5 w-3.5" /> Mark Writing tasks
            </Link>
            <Link href="/admin/ielts/speaking" className="flex items-center gap-2 underline">
              <Mic className="h-3.5 w-3.5" /> Mark Speaking interviews
            </Link>
            <Link href="/admin/ielts/economy" className="flex items-center gap-2 underline">
              <UserPlus className="h-3.5 w-3.5" /> Reviews and invites
            </Link>
            <Link href="/admin/ielts/papers" className="flex items-center gap-2 underline">
              <Globe2 className="h-3.5 w-3.5" /> Papers and content
            </Link>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
