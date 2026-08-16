import { notFound } from "next/navigation";

import { WritingWorkspace, type WritingTask } from "@/components/ielts/writing-workspace";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { WRITING_SUGGESTED_MINUTES } from "@/lib/ielts/constants";
import { promptImageSrc } from "@/lib/ielts/image-storage";

export const metadata = { title: "Full Writing Practice" };
export const dynamic = "force-dynamic";

/**
 * Both tasks, one sitting, one clock.
 *
 * The real Writing paper is not two exercises; it is sixty minutes in which a
 * candidate has to budget their own time across a short report and a longer
 * essay, and running out of time on Task 2 is one of the commonest ways to lose
 * a band. Practising the tasks separately never rehearses that, which is why
 * this route exists rather than only the per-task one.
 */
export default async function FullWritingPracticePage({
  params,
}: {
  params: { testId: string };
}) {
  const user = await requireUser();

  const test = await prisma.ieltsTest.findUnique({
    where: { id: params.testId },
    include: {
      sections: {
        where: { skill: "WRITING" },
        include: { parts: { orderBy: { partNumber: "asc" } } },
      },
    },
  });
  if (!test || !test.sections.length) notFound();

  // Same rule as the single-task room: an unpublished paper is a custom topic
  // and belongs to exactly one student.
  if (test.status !== "PUBLISHED") {
    const mine = await prisma.ieltsAttempt.findFirst({
      where: { testId: test.id, userId: user.id },
      select: { id: true },
    });
    if (!mine) notFound();
  }

  const parts = test.sections.flatMap((s) => s.parts);
  if (parts.length === 0) notFound();

  const submissions = await prisma.ieltsWritingSubmission.findMany({
    where: { userId: user.id, partId: { in: parts.map((p) => p.id) } },
    orderBy: { submittedAt: "desc" },
    select: { partId: true, responseText: true, status: true },
  });
  // Newest first, so the first hit per part is the current one.
  const byPart = new Map<string, (typeof submissions)[number]>();
  for (const s of submissions) if (!byPart.has(s.partId)) byPart.set(s.partId, s);

  const tasks: WritingTask[] = parts.map((p) => {
    const sub = byPart.get(p.id);
    return {
      partId: p.id,
      taskNumber: p.partNumber,
      title: p.title ?? `Task ${p.partNumber}`,
      promptHtml: p.promptHtml ?? "",
      imageUrl: promptImageSrc(p.id, p.imageUrl),
      imageAlt: p.imageAlt,
      minWords: p.minWords ?? (p.partNumber === 1 ? 150 : 250),
      initialText: sub?.responseText ?? "",
      readOnly: Boolean(sub && sub.status !== "PENDING"),
    };
  });

  // The clock covers whatever tasks this paper actually has, so a custom
  // single-task paper opened here still gets an honest allowance.
  const minutes = parts.reduce(
    (n, p) => n + (WRITING_SUGGESTED_MINUTES[p.partNumber] ?? 40),
    0
  );

  return (
    <WritingWorkspace
      full={parts.length > 1}
      tasks={tasks}
      paperTitle={test.title}
      suggestedMinutes={minutes}
      studentName={user.name ?? user.email ?? "Student"}
    />
  );
}
