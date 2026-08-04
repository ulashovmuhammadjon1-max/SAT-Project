import { notFound } from "next/navigation";

import { QuestionEditor } from "@/components/admin/question-editor";
import { prisma } from "@/lib/prisma";

export const dynamic = "force-dynamic";

export default async function AdminQuestionEditorPage({ params }: { params: { id: string } }) {
  const [question, domains] = await Promise.all([
    prisma.question.findUnique({
      where: { id: params.id },
      include: { choices: { orderBy: { order: "asc" } }, explanation: true, passage: true },
    }),
    prisma.domain.findMany({ orderBy: { name: "asc" }, include: { skills: { orderBy: { name: "asc" } } } }),
  ]);

  if (!question) notFound();

  return <QuestionEditor question={question} domains={domains} />;
}
