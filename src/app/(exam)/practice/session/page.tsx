import Link from "next/link";
import { redirect } from "next/navigation";
import type { QuestionDifficulty, Subject } from "@prisma/client";
import { ArrowLeft } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { PracticeSession, type SessionQuestion } from "@/components/student/qb-session";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import {
  generateMistakeSession,
  generateSession,
  type AttemptStatus,
} from "@/server/actions/student/question-bank";

export const metadata = { title: "Practice" };
export const dynamic = "force-dynamic";

const VALID_DIFFICULTIES = new Set(["EASY", "MEDIUM", "HARD"]);
const VALID_STATUSES = new Set([
  "ALL",
  "NOT_ATTEMPTED",
  "ATTEMPTED",
  "CORRECT",
  "INCORRECT",
  "SAVED",
]);

export default async function PracticeSessionPage({
  searchParams,
}: {
  searchParams: {
    subject?: string;
    domainId?: string;
    skillId?: string;
    difficulties?: string;
    status?: string;
    size?: string;
    mistakes?: string;
    ids?: string;
  };
}) {
  const user = await requireUser();
  const subject: Subject = searchParams.subject === "MATH" ? "MATH" : "READING_WRITING";
  const backHref = `/practice?subject=${subject}`;

  const size = Math.min(100, Math.max(1, parseInt(searchParams.size ?? "10", 10) || 10));

  const difficulties = (searchParams.difficulties ?? "")
    .split(",")
    .filter((d) => VALID_DIFFICULTIES.has(d)) as QuestionDifficulty[];

  const status = (
    VALID_STATUSES.has(searchParams.status ?? "") ? searchParams.status : "ALL"
  ) as AttemptStatus;

  // The question set is pinned into the URL on first load.
  //
  // Calling any server action re-renders this page's server components, and
  // `generateSession` is randomized — so without pinning, submitting an answer
  // silently dealt a whole new set of questions underneath the running session
  // while the client kept its old state. Resolving the ids once and redirecting
  // makes every later re-render return the identical set.
  const pinned = (searchParams.ids ?? "")
    .split(",")
    .map((id) => id.trim())
    .filter(Boolean);

  const ids = pinned.length
    ? pinned
    : searchParams.mistakes === "1"
      ? await generateMistakeSession(size, subject)
      : await generateSession(
          {
            subject,
            domainId: searchParams.domainId,
            skillId: searchParams.skillId,
            difficulties,
            status,
          },
          size
        );

  // The canonical, fully-pinned link to this session. It is what the redirect
  // below navigates to, and what the runner stores so the student can come back
  // to this exact set of questions later.
  const params = new URLSearchParams();
  for (const [key, value] of Object.entries(searchParams)) {
    if (typeof value === "string" && value) params.set(key, value);
  }
  params.set("ids", ids.join(","));
  const sessionHref = `/practice/session?${params.toString()}`;

  if (!pinned.length && ids.length > 0) {
    redirect(sessionHref);
  }

  if (ids.length === 0) {
    return (
      <div className="space-y-6">
        <Link
          href={backHref}
          className="inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground"
        >
          <ArrowLeft className="h-3.5 w-3.5" /> Question Bank
        </Link>
        <Card>
          <CardContent className="space-y-3 p-8 text-center">
            <p className="font-medium">No questions match those filters.</p>
            <p className="text-sm text-muted-foreground">
              Try widening the difficulty or attempt-status filters.
            </p>
            <Button asChild>
              <Link href={`/practice/start?subject=${subject}`}>Change filters</Link>
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  const [rows, bookmarks] = await Promise.all([
    prisma.question.findMany({
      where: { id: { in: ids } },
      select: {
        id: true,
        type: true,
        difficulty: true,
        stem: true,
        imageUrl: true,
        // Subject lives on the domain, not the question.
        domain: { select: { name: true, subject: true } },
        skill: { select: { name: true } },
        // `id` is required: it is the region key highlights are anchored to.
        passage: { select: { id: true, title: true, content: true, imageUrl: true } },
        // isCorrect deliberately not selected — grading happens server-side.
        choices: { select: { id: true, label: true, content: true }, orderBy: { order: "asc" } },
      },
    }),
    prisma.bookmark.findMany({
      where: { userId: user.id, questionId: { in: ids } },
      select: { questionId: true },
    }),
  ]);

  const saved = new Set(bookmarks.map((b) => b.questionId));
  const byId = new Map(rows.map((r) => [r.id, r]));

  // Preserve the randomized order produced by the generator.
  const questions: SessionQuestion[] = ids.flatMap((id) => {
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
        imageUrl: q.imageUrl,
        passage: q.passage,
        choices: q.choices,
        saved: saved.has(q.id),
      },
    ];
  });

  // Rendered bare: PracticeSession owns the full viewport, the same way the
  // exam shell does. Wrapping it in dashboard chrome is what made Question Bank
  // practice read as a page with a quiz on it rather than a testing environment.
  return (
    <PracticeSession
      questions={questions}
      backHref={backHref}
      sessionHref={sessionHref}
      studentName={user.name ?? "Student"}
    />
  );
}
