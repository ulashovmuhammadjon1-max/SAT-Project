import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { WritingEditor } from "@/components/ielts/writing-editor";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { PRACTICE_DISCLAIMER } from "@/lib/ielts/bands";
import { REVIEWER_CLAIM, WRITING_SUGGESTED_MINUTES } from "@/lib/ielts/constants";

export const metadata = { title: "Writing Task" };
export const dynamic = "force-dynamic";

export default async function WritingTaskPage({ params }: { params: { partId: string } }) {
  const user = await requireUser();

  const part = await prisma.ieltsPart.findUnique({
    where: { id: params.partId },
    include: { section: { select: { skill: true, testId: true, test: { select: { title: true } } } } },
  });
  if (!part || part.section.skill !== "WRITING") notFound();

  // The student's own latest response to this task, and nothing of anyone
  // else's — the editor is seeded from it.
  const submission = await prisma.ieltsWritingSubmission.findFirst({
    where: { partId: part.id, userId: user.id },
    orderBy: { submittedAt: "desc" },
    select: { responseText: true, status: true },
  });
  const readOnly = Boolean(submission && submission.status !== "PENDING");
  const minWords = part.minWords ?? (part.partNumber === 1 ? 150 : 250);

  return (
    <div className="space-y-5">
      <Link
        href="/ielts/writing"
        className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground"
      >
        <ArrowLeft className="h-4 w-4" /> Writing
      </Link>

      <div className="flex flex-wrap items-center gap-2">
        <h1 className="font-display text-xl font-semibold tracking-tight">
          {part.section.test.title} — {part.title ?? `Task ${part.partNumber}`}
        </h1>
        <Badge variant="outline">
          about {WRITING_SUGGESTED_MINUTES[part.partNumber] ?? 40} minutes
        </Badge>
        <Badge variant="outline">minimum {minWords} words</Badge>
      </div>

      {/* Prompt left, editor right — the computer-delivered Writing layout. */}
      <div className="grid gap-4 lg:grid-cols-2">
        <div className="rounded-lg border border-border bg-card p-5">
          <p className="mb-3 text-xs font-semibold uppercase tracking-wide text-muted-foreground">
            Task {part.partNumber}
          </p>
          <div
            className="ielts-prompt space-y-3 text-sm leading-relaxed [&_li]:ml-5 [&_li]:list-disc [&_table]:text-xs [&_ul]:space-y-1"
            dangerouslySetInnerHTML={{ __html: part.promptHtml ?? "" }}
          />
        </div>

        <WritingEditor
          partId={part.id}
          taskNumber={part.partNumber}
          minWords={minWords}
          initialText={submission?.responseText ?? ""}
          readOnly={readOnly}
        />
      </div>

      <p className="text-xs text-muted-foreground">
        {REVIEWER_CLAIM.WRITING}. {PRACTICE_DISCLAIMER}
      </p>
    </div>
  );
}
