import { notFound, redirect } from "next/navigation";

import { ExamShell } from "@/components/exam/exam-shell";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

export const dynamic = "force-dynamic";

export default async function ExamPage({ params }: { params: { attemptId: string } }) {
  const user = await requireUser();

  const attempt = await prisma.attempt.findUnique({
    where: { id: params.attemptId },
  });

  if (!attempt || attempt.userId !== user.id) notFound();
  if (attempt.status === "SUBMITTED") redirect(`/review/${attempt.id}`);
  if (!attempt.currentModuleId) redirect(`/review/${attempt.id}`);

  let moduleAttempt = await prisma.moduleAttempt.findFirst({
    where: { attemptId: attempt.id, moduleId: attempt.currentModuleId, submittedAt: null },
    include: {
      module: {
        include: {
          questions: { orderBy: { order: "asc" }, include: { choices: { orderBy: { order: "asc" } }, passage: true } },
        },
      },
    },
  });

  if (!moduleAttempt) {
    moduleAttempt = await prisma.moduleAttempt.create({
      data: { attemptId: attempt.id, moduleId: attempt.currentModuleId },
      include: {
        module: {
          include: {
            questions: {
              orderBy: { order: "asc" },
              include: { choices: { orderBy: { order: "asc" } }, passage: true },
            },
          },
        },
      },
    });
  }

  const existingResponses = await prisma.response.findMany({ where: { moduleAttemptId: moduleAttempt.id } });

  // Never send `isCorrect` / `correctAnswerFR` to the client during a live attempt —
  // that would leak answers. Review mode (after submission) is the only place
  // that data is shown.
  const safeModule = {
    id: moduleAttempt.module.id,
    subject: moduleAttempt.module.subject,
    order: moduleAttempt.module.order,
    difficulty: moduleAttempt.module.difficulty,
    timeLimitMinutes: moduleAttempt.module.timeLimitMinutes,
    questions: moduleAttempt.module.questions.map((q) => ({
      id: q.id,
      type: q.type,
      stem: q.stem,
      imageUrl: q.imageUrl,
      order: q.order,
      passage: q.passage ? { id: q.passage.id, title: q.passage.title, content: q.passage.content } : null,
      choices: q.choices.map((c) => ({ id: c.id, label: c.label, content: c.content, order: c.order })),
    })),
  };

  // A fresh attempt: nothing answered anywhere yet, and this is the opening
  // module. Only then does the student see the "preparing your test" curtain.
  const priorModuleAttempts = await prisma.moduleAttempt.count({
    where: { attemptId: attempt.id, id: { not: moduleAttempt.id } },
  });
  const showPreparing = priorModuleAttempts === 0 && existingResponses.length === 0;

  return (
    // Keyed by the module attempt so that advancing to the next module
    // *remounts* the shell. Without this the client component survives the
    // server refetch and carries its old state across: the review page stays
    // open, `currentIndex` points into the previous module, and the per-question
    // state array is still sized for it — which is what forced the student to
    // pick a question by hand after ending a module.
    <ExamShell
      key={moduleAttempt.id}
      attemptId={attempt.id}
      showPreparing={showPreparing}
      studentName={user.name ?? "Student"}
      moduleAttemptId={moduleAttempt.id}
      startedAt={moduleAttempt.startedAt}
      module={safeModule}
      existingResponses={existingResponses.map((r) => ({
        questionId: r.questionId,
        selectedChoiceId: r.selectedChoiceId,
        freeResponseAnswer: r.freeResponseAnswer,
        flagged: r.flagged,
        timeSpentSeconds: r.timeSpentSeconds,
        changedAnswerCount: r.changedAnswerCount,
        eliminatedChoiceIds: (r.eliminatedChoiceIds as string[] | null) ?? [],
      }))}
    />
  );
}
