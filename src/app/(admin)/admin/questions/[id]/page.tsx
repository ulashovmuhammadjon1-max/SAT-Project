import { notFound } from "next/navigation";

import { QuestionEditor } from "@/components/admin/question-editor";
import { prisma } from "@/lib/prisma";

export const dynamic = "force-dynamic";

export default async function AdminQuestionEditorPage({ params }: { params: { id: string } }) {
  const [question, domains] = await Promise.all([
    prisma.question.findUnique({
      where: { id: params.id },
      include: {
        choices: { orderBy: { order: "asc" } },
        explanation: true,
        passage: true,
        module: { select: { testId: true, test: { select: { title: true } } } },
      },
    }),
    prisma.domain.findMany({ orderBy: { name: "asc" }, include: { skills: { orderBy: { name: "asc" } } } }),
  ]);

  if (!question) notFound();

  // Most questions are opened from their test's module list, so "back"
  // should return there rather than to the ungrouped Question Bank —
  // standalone bank questions (no module) fall back to that list instead.
  // The #q-{id} anchor lands back on this exact question's row instead of
  // resetting to the top of the test (Module 1, Question 1).
  const back = question.module
    ? {
        href: `/admin/tests/${question.module.testId}#q-${question.id}`,
        label: `Back to ${question.module.test.title}`,
      }
    : { href: "/admin/questions", label: "Back to Question Bank" };

  // Prev/Next within the same module, ordered the same way the module list
  // shows them, so the admin can step through every question without
  // returning to the list in between.
  let prevId: string | null = null;
  let nextId: string | null = null;
  if (question.moduleId) {
    const siblings = await prisma.question.findMany({
      where: { moduleId: question.moduleId },
      orderBy: { order: "asc" },
      select: { id: true },
    });
    const index = siblings.findIndex((s) => s.id === question.id);
    if (index > 0) prevId = siblings[index - 1].id;
    if (index >= 0 && index < siblings.length - 1) nextId = siblings[index + 1].id;
  }

  return <QuestionEditor question={question} domains={domains} back={back} prevId={prevId} nextId={nextId} />;
}
