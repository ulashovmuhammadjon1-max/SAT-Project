import { notFound } from "next/navigation";

import { WritingWorkspace } from "@/components/ielts/writing-workspace";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { WRITING_SUGGESTED_MINUTES } from "@/lib/ielts/constants";

export const metadata = { title: "Writing Task" };
export const dynamic = "force-dynamic";

export default async function WritingTaskPage({ params }: { params: { partId: string } }) {
  const user = await requireUser();

  const part = await prisma.ieltsPart.findUnique({
    where: { id: params.partId },
    include: {
      section: {
        select: { skill: true, testId: true, test: { select: { title: true } } },
      },
    },
  });
  if (!part || part.section.skill !== "WRITING") notFound();

  // The student's own latest response to this task, and nobody else's — the
  // editor is seeded from it.
  const submission = await prisma.ieltsWritingSubmission.findFirst({
    where: { partId: part.id, userId: user.id },
    orderBy: { submittedAt: "desc" },
    select: { responseText: true, status: true },
  });
  const readOnly = Boolean(submission && submission.status !== "PENDING");
  const minWords = part.minWords ?? (part.partNumber === 1 ? 150 : 250);

  return (
    <WritingWorkspace
      partId={part.id}
      taskNumber={part.partNumber}
      taskTitle={part.title ?? `Task ${part.partNumber}`}
      paperTitle={part.section.test.title}
      promptHtml={part.promptHtml ?? ""}
      minWords={minWords}
      suggestedMinutes={WRITING_SUGGESTED_MINUTES[part.partNumber] ?? 40}
      initialText={submission?.responseText ?? ""}
      readOnly={readOnly}
      studentName={user.name ?? user.email ?? "Student"}
    />
  );
}
