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
  const back = question.module
    ? { href: `/admin/tests/${question.module.testId}`, label: `Back to ${question.module.test.title}` }
    : { href: "/admin/questions", label: "Back to Question Bank" };

  return <QuestionEditor question={question} domains={domains} back={back} />;
}
