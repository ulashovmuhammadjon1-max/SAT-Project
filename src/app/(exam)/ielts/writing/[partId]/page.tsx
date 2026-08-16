import { notFound } from "next/navigation";

import { WritingWorkspace } from "@/components/ielts/writing-workspace";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { WRITING_SUGGESTED_MINUTES } from "@/lib/ielts/constants";
import { promptImageSrc } from "@/lib/ielts/image-storage";

export const metadata = { title: "Writing Task" };
export const dynamic = "force-dynamic";

export default async function WritingTaskPage({ params }: { params: { partId: string } }) {
  const user = await requireUser();

  const part = await prisma.ieltsPart.findUnique({
    where: { id: params.partId },
    include: {
      section: {
        select: { skill: true, testId: true, test: { select: { title: true, status: true } } },
      },
    },
  });
  if (!part || part.section.skill !== "WRITING") notFound();

  // An unpublished paper is somebody's own custom topic. It is reachable only
  // by the student who created it — otherwise a guessed id would hand out
  // another student's prompt and their uploaded chart.
  if (part.section.test.status !== "PUBLISHED") {
    const mine = await prisma.ieltsAttempt.findFirst({
      where: { testId: part.section.testId, userId: user.id },
      select: { id: true },
    });
    if (!mine) notFound();
  }

  // The student's own latest response to this task, and nobody else's — the
  // editor is seeded from it.
  const submission = await prisma.ieltsWritingSubmission.findFirst({
    where: { partId: part.id, userId: user.id },
    orderBy: { submittedAt: "desc" },
    select: { responseText: true, status: true },
  });
  const minWords = part.minWords ?? (part.partNumber === 1 ? 150 : 250);

  return (
    <WritingWorkspace
      paperTitle={part.section.test.title}
      suggestedMinutes={WRITING_SUGGESTED_MINUTES[part.partNumber] ?? 40}
      studentName={user.name ?? user.email ?? "Student"}
      tasks={[
        {
          partId: part.id,
          taskNumber: part.partNumber,
          title: part.title ?? `Task ${part.partNumber}`,
          promptHtml: part.promptHtml ?? "",
          imageUrl: promptImageSrc(part.id, part.imageUrl),
          imageAlt: part.imageAlt,
          minWords,
          initialText: submission?.responseText ?? "",
          readOnly: Boolean(submission && submission.status !== "PENDING"),
        },
      ]}
    />
  );
}
