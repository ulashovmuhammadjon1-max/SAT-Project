import { redirect } from "next/navigation";

import { PracticeSession, type SessionQuestion } from "@/components/student/qb-session";
import { prisma } from "@/lib/prisma";
import { questionImageSrc } from "@/lib/question-image";
import { requireVerifiedUser } from "@/lib/session";

export const metadata = { title: "Free diagnostic" };
export const dynamic = "force-dynamic";

/**
 * The SAT diagnostic runner: the practice-test screen in diagnostic mode, over
 * the question set pinned on the student's own DiagnosticTest row.
 */
export default async function SatDiagnosticRunPage() {
  const user = await requireVerifiedUser();
  const row = await prisma.diagnosticTest.findUnique({ where: { userId_kind: { userId: user.id, kind: "SAT" } } });
  if (!row || row.completedAt || row.questionIds.length === 0) redirect("/diagnostic");

  const [rows, bookmarks] = await Promise.all([
    prisma.question.findMany({
      where: { id: { in: row.questionIds } },
      select: {
        id: true,
        type: true,
        difficulty: true,
        stem: true,
        imageUrl: true,
        domain: { select: { name: true, subject: true } },
        skill: { select: { name: true } },
        passage: { select: { id: true, title: true, content: true, imageUrl: true } },
        // isCorrect deliberately not selected — grading happens server-side.
        choices: { select: { id: true, label: true, content: true }, orderBy: { order: "asc" } },
      },
    }),
    prisma.bookmark.findMany({ where: { userId: user.id, questionId: { in: row.questionIds } }, select: { questionId: true } }),
  ]);
  const saved = new Set(bookmarks.map((b) => b.questionId));
  const byId = new Map(rows.map((r) => [r.id, r]));
  const questions: SessionQuestion[] = row.questionIds.flatMap((id) => {
    const q = byId.get(id);
    if (!q) return [];
    return [
      {
        id: q.id,
        ref: `Q-${q.id.slice(-6).toUpperCase()}`,
        type: q.type,
        subject: q.domain.subject,
        difficulty: q.difficulty,
        domainName: q.domain.name,
        skillName: q.skill.name,
        stem: q.stem,
        imageUrl: questionImageSrc(q.id, q.imageUrl),
        passage: q.passage,
        choices: q.choices,
        saved: saved.has(q.id),
      },
    ];
  });

  return (
    <PracticeSession
      diagnostic
      questions={questions}
      backHref="/diagnostic"
      sessionHref="/diagnostic/sat"
      studentName={user.name ?? "Student"}
    />
  );
}
