import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { IeltsReviewForm } from "@/components/admin/ielts-review-form";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "Review Writing" };
export const dynamic = "force-dynamic";

export default async function ReviewWritingPage({
  params,
}: {
  params: { submissionId: string };
}) {
  await requireAdmin();

  const submission = await prisma.ieltsWritingSubmission.findUnique({
    where: { id: params.submissionId },
    include: {
      user: { select: { name: true, email: true } },
      review: true,
    },
  });
  if (!submission) notFound();

  const part = await prisma.ieltsPart.findUnique({
    where: { id: submission.partId },
    select: {
      partNumber: true, title: true, promptHtml: true, minWords: true,
      section: { select: { test: { select: { title: true } } } },
    },
  });

  const minWords = part?.minWords ?? (part?.partNumber === 1 ? 150 : 250);
  const short = submission.wordCount < minWords;

  return (
    <div className="space-y-5">
      <Link href="/admin/ielts/writing"
        className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground">
        <ArrowLeft className="h-4 w-4" /> Writing Reviews
      </Link>

      <div className="flex flex-wrap items-center gap-2">
        <h1 className="font-display text-xl font-semibold tracking-tight">
          {submission.user.name ?? submission.user.email}
        </h1>
        <Badge variant="outline">
          {part?.section.test.title} &middot; {part?.title ?? `Task ${part?.partNumber}`}
        </Badge>
        <Badge variant={short ? "outline" : "outline"}
          className={short ? "border-amber-500/40 text-amber-700" : undefined}>
          {submission.wordCount} words {short && `(under ${minWords})`}
        </Badge>
        {submission.review && <Badge variant="navy">Already reviewed</Badge>}
      </div>

      <div className="grid gap-4 lg:grid-cols-[minmax(0,1fr)_minmax(0,1fr)]">
        <div className="space-y-4">
          <div className="rounded-lg border border-border bg-card p-4">
            <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted-foreground">
              Task prompt
            </p>
            <div className="space-y-2 text-sm leading-relaxed [&_li]:ml-5 [&_li]:list-disc [&_table]:text-xs"
              dangerouslySetInnerHTML={{ __html: part?.promptHtml ?? "" }} />
          </div>

          <div className="rounded-lg border border-border bg-card p-4">
            <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted-foreground">
              Student response
            </p>
            {/* Rendered as plain text, never as HTML: this is student input and
                anything else would let one student's markup run in a
                reviewer's browser. whitespace-pre-wrap keeps their paragraphing. */}
            <p className="whitespace-pre-wrap text-[15px] leading-relaxed">
              {submission.responseText}
            </p>
          </div>
        </div>

        <IeltsReviewForm
          kind="WRITING"
          submissionId={submission.id}
          initial={
            submission.review
              ? {
                  bands: {
                    task: submission.review.taskBand,
                    coherence: submission.review.coherenceBand,
                    lexical: submission.review.lexicalBand,
                    grammar: submission.review.grammarBand,
                  },
                  notes: {
                    overall: submission.review.overallFeedback ?? "",
                    didWell: submission.review.didWell ?? "",
                    toImprove: submission.review.toImprove ?? "",
                    taskNotes: submission.review.taskResponseNotes ?? "",
                    coherenceNotes: submission.review.coherenceNotes ?? "",
                    lexicalNotes: submission.review.vocabularyNotes ?? "",
                    grammarNotes: submission.review.grammarNotes ?? "",
                    nextSteps: submission.review.nextSteps ?? "",
                  },
                }
              : undefined
          }
        />
      </div>
    </div>
  );
}
