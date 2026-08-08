import Link from "next/link";
import { redirect } from "next/navigation";
import type { Subject } from "@prisma/client";
import { ArrowLeft } from "lucide-react";

import { SessionBuilder } from "@/components/student/qb-session-builder";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { generateMistakeSession } from "@/server/actions/student/question-bank";

export const metadata = { title: "Start practice" };
export const dynamic = "force-dynamic";

export default async function StartPracticePage({
  searchParams,
}: {
  searchParams: { subject?: string; skillId?: string; newOnly?: string; mistakes?: string };
}) {
  await requireUser();
  const subject: Subject = searchParams.subject === "MATH" ? "MATH" : "READING_WRITING";

  // "Practice my mistakes" skips the builder entirely and goes straight in.
  if (searchParams.mistakes === "1") {
    const ids = await generateMistakeSession(10, subject);
    if (ids.length > 0) {
      redirect(`/practice/session?subject=${subject}&mistakes=1&size=${ids.length}`);
    }
  }

  const domains = await prisma.domain.findMany({
    where: { subject },
    orderBy: { code: "asc" },
    include: { skills: { orderBy: { code: "asc" } } },
  });

  return (
    <div className="space-y-6">
      <div>
        <Link
          href={`/practice?subject=${subject}`}
          className="inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground"
        >
          <ArrowLeft className="h-3.5 w-3.5" /> Question Bank
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold tracking-tight">Build a practice session</h1>
        <p className="text-sm text-muted-foreground">
          Choose what to practice. You&apos;ll only get questions that match every filter.
        </p>
      </div>

      <SessionBuilder
        subject={subject}
        domains={domains.map((d) => ({
          id: d.id,
          name: d.name,
          skills: d.skills.map((s) => ({ id: s.id, name: s.name })),
        }))}
        initialSkillId={searchParams.skillId}
        initialNewOnly={searchParams.newOnly === "1"}
      />
    </div>
  );
}
