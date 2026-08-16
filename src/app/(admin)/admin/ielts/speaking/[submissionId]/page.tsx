import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { IeltsReviewForm } from "@/components/admin/ielts-review-form";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "Review Speaking" };
export const dynamic = "force-dynamic";

function clock(s: number) {
  return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`;
}

export default async function ReviewSpeakingPage({
  params,
}: {
  params: { submissionId: string };
}) {
  await requireAdmin();

  const submission = await prisma.ieltsSpeakingSubmission.findUnique({
    where: { id: params.submissionId },
    include: {
      user: { select: { name: true, email: true } },
      review: true,
      attempt: { select: { test: { select: { title: true } } } },
      recordings: { orderBy: [{ partId: "asc" }, { questionIndex: "asc" }] },
    },
  });
  if (!submission) notFound();

  const parts = await prisma.ieltsPart.findMany({
    where: { id: { in: [...new Set(submission.recordings.map((r) => r.partId))] } },
    select: { id: true, partNumber: true, title: true },
  });
  const partOf = new Map(parts.map((p) => [p.id, p]));
  // Group by part so the reviewer hears Part 1, then 2, then 3 — the order the
  // interview was taken in, not the order rows came back.
  const grouped = [...partOf.values()]
    .sort((a, b) => a.partNumber - b.partNumber)
    .map((p) => ({
      part: p,
      items: submission.recordings
        .filter((r) => r.partId === p.id)
        .sort((a, b) => a.questionIndex - b.questionIndex),
    }));

  return (
    <div className="space-y-5">
      <Link href="/admin/ielts/speaking"
        className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground">
        <ArrowLeft className="h-4 w-4" /> Speaking Reviews
      </Link>

      <div className="flex flex-wrap items-center gap-2">
        <h1 className="font-display text-xl font-semibold tracking-tight">
          {submission.user.name ?? submission.user.email}
        </h1>
        <Badge variant="outline">{submission.attempt.test.title}</Badge>
        <Badge variant="outline">{submission.recordings.length} recordings</Badge>
        {submission.review && <Badge variant="navy">Already reviewed</Badge>}
      </div>

      <div className="grid gap-4 lg:grid-cols-[minmax(0,1fr)_minmax(0,1fr)]">
        <div className="space-y-4">
          {grouped.map(({ part, items }) => (
            <div key={part.id} className="rounded-lg border border-border bg-card p-4">
              <p className="mb-3 text-xs font-semibold uppercase tracking-wide text-muted-foreground">
                {part.title ?? `Part ${part.partNumber}`}
              </p>
              <div className="space-y-3">
                {items.map((r) => (
                  <div key={r.id} className="space-y-1.5">
                    <p className="text-sm">{r.promptText}</p>
                    {/* Served through the signed route, which checks the
                        listener against the submission before streaming. */}
                    <audio
                      controls
                      preload="none"
                      src={`/api/ielts/audio/${r.id}`}
                      className="w-full"
                    />
                    <p className="text-xs text-muted-foreground tabular-nums">
                      {clock(r.durationSeconds)}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          ))}
          {submission.recordings.length === 0 && (
            <div className="rounded-lg border border-border bg-card p-6 text-center text-sm text-muted-foreground">
              No recordings were submitted.
            </div>
          )}
        </div>

        <IeltsReviewForm
          kind="SPEAKING"
          submissionId={submission.id}
          initial={
            submission.review
              ? {
                  bands: {
                    fluency: submission.review.fluencyBand,
                    lexical: submission.review.lexicalBand,
                    grammar: submission.review.grammarBand,
                    pronunciation: submission.review.pronunciationBand,
                  },
                  notes: {
                    overall: submission.review.overallFeedback ?? "",
                    didWell: submission.review.strongPoints ?? "",
                    toImprove: submission.review.weaknesses ?? "",
                    fluencyNotes: submission.review.fluencyNotes ?? "",
                    lexicalNotes: submission.review.vocabularyNotes ?? "",
                    grammarNotes: submission.review.grammarNotes ?? "",
                    pronunciationNotes: submission.review.pronunciationNotes ?? "",
                    nextSteps: submission.review.howToImprove ?? "",
                  },
                }
              : undefined
          }
        />
      </div>
    </div>
  );
}
