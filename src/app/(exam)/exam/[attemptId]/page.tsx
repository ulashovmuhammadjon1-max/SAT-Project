import { notFound, redirect } from "next/navigation";

import { ExamShell } from "@/components/exam/exam-shell";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

export const dynamic = "force-dynamic";

/**
 * The columns a live module actually renders.
 *
 * `imageUrl` is deliberately absent. Most figures are stored as base64 `data:`
 * URIs, and including the column drags them through the render and into the
 * page payload — 898 KB on the heaviest module in the bank, rebuilt on every
 * open. Whether a question *has* a figure is fetched separately as a set of
 * ids, and the client is handed `/api/question-image/<id>` instead, which the
 * browser then caches.
 *
 * Answer columns (`correctAnswerFR`) stay out for a different reason: sending
 * them to a live attempt would hand the student the key.
 */
const LIVE_QUESTION_SELECT = {
  id: true,
  type: true,
  stem: true,
  order: true,
  choices: {
    select: { id: true, label: true, content: true, order: true },
    orderBy: { order: "asc" },
  },
  passage: { select: { id: true, title: true, content: true } },
} as const;

export default async function ExamPage({ params }: { params: { attemptId: string } }) {
  const user = await requireUser();

  const attempt = await prisma.attempt.findUnique({
    where: { id: params.attemptId },
  });

  if (!attempt || attempt.userId !== user.id) notFound();
  // A finished attempt goes to the result summary, not straight into the
  // per-question review — same destination the exam itself redirects to on
  // submit, so a refresh and a submit land in the same place.
  if (attempt.status === "SUBMITTED") redirect(`/results/${attempt.id}`);
  if (!attempt.currentModuleId) redirect(`/results/${attempt.id}`);

  let moduleAttempt = await prisma.moduleAttempt.findFirst({
    where: { attemptId: attempt.id, moduleId: attempt.currentModuleId, submittedAt: null },
    include: {
      module: {
        include: {
          questions: { orderBy: { order: "asc" }, select: LIVE_QUESTION_SELECT },
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
            questions: { orderBy: { order: "asc" }, select: LIVE_QUESTION_SELECT },
          },
        },
      },
    });
  }

  const existingResponses = await prisma.response.findMany({ where: { moduleAttemptId: moduleAttempt.id } });

  // Which questions have a figure, as ids only. Asking for `imageUrl` itself
  // would pull every base64 payload in the module back into the render.
  const withImage = new Set(
    (
      await prisma.question.findMany({
        where: { moduleId: moduleAttempt.module.id, imageUrl: { not: null } },
        select: { id: true },
      })
    ).map((q) => q.id)
  );

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
      imageUrl: withImage.has(q.id) ? `/api/question-image/${q.id}` : null,
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
