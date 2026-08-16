import Link from "next/link";
import { AlertTriangle, Headphones, BookOpenText, PenLine, Mic } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Prisma } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "IELTS Content" };
export const dynamic = "force-dynamic";

const SKILL_ICON = {
  LISTENING: Headphones, READING: BookOpenText, WRITING: PenLine, SPEAKING: Mic,
} as const;

export default async function AdminIeltsPage() {
  await requireAdmin();

  const tests = await prisma.ieltsTest.findMany({
    orderBy: [{ status: "asc" }, { createdAt: "desc" }],
    include: {
      sections: {
        orderBy: { order: "asc" },
        include: {
          parts: {
            orderBy: { partNumber: "asc" },
            select: {
              id: true, partNumber: true, audioUrl: true,
              _count: { select: { questions: true } },
            },
          },
        },
      },
    },
  });

  // A question carries its importer findings in `metadata`, so the count of
  // papers needing attention is answerable without opening each one.
  //
  // Filtered in JS rather than with a Prisma JSON-path `where`. The path
  // filter is dialect-specific and, if it silently matched nothing, this
  // badge would simply never appear — a checker that fails by going quiet is
  // the failure mode this project keeps hitting. The row count here is the
  // number of IELTS questions on the platform, so reading them is cheap.
  const withMeta = await prisma.ieltsQuestion.findMany({
    where: { NOT: { metadata: { equals: Prisma.DbNull } } },
    select: { metadata: true, part: { select: { section: { select: { testId: true } } } } },
  });
  const flaggedByTest = new Map<string, number>();
  for (const q of withMeta) {
    const findings = (q.metadata as { findings?: unknown[] } | null)?.findings;
    if (!Array.isArray(findings) || findings.length === 0) continue;
    const id = q.part.section.testId;
    flaggedByTest.set(id, (flaggedByTest.get(id) ?? 0) + 1);
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">IELTS Content</h1>
        <p className="text-sm text-muted-foreground">
          Imported and authored IELTS papers. Nothing reaches a student until its status
          is PUBLISHED.
        </p>
      </div>

      {tests.length === 0 && (
        <Card>
          <CardContent className="py-10 text-center text-sm text-muted-foreground">
            No IELTS papers yet.
          </CardContent>
        </Card>
      )}

      <div className="space-y-3">
        {tests.map((test) => {
          const questionCount = test.sections.reduce(
            (n, s) => n + s.parts.reduce((m, p) => m + p._count.questions, 0), 0);
          const missingAudio = test.sections
            .filter((s) => s.skill === "LISTENING")
            .flatMap((s) => s.parts)
            .filter((p) => !p.audioUrl).length;
          const issues = flaggedByTest.get(test.id) ?? 0;

          return (
            <Link key={test.id} href={`/admin/ielts/${test.id}`} className="block">
              <Card className="transition-colors hover:border-navy-900/30">
                <CardContent className="flex flex-wrap items-center justify-between gap-4 py-5">
                  <div className="space-y-1.5">
                    <div className="flex flex-wrap items-center gap-2">
                      <span className="font-display text-base font-semibold">{test.title}</span>
                      <Badge variant={test.status === "PUBLISHED" ? "navy" : "outline"}>
                        {test.status}
                      </Badge>
                      <Badge variant="outline">{test.module.replace("_", " ")}</Badge>
                    </div>
                    <div className="flex flex-wrap items-center gap-3 text-xs text-muted-foreground">
                      {test.sections.map((s) => {
                        const Icon = SKILL_ICON[s.skill];
                        return (
                          <span key={s.id} className="inline-flex items-center gap-1">
                            <Icon className="h-3.5 w-3.5" />
                            {s.skill.charAt(0) + s.skill.slice(1).toLowerCase()} ·{" "}
                            {s.parts.length} parts
                          </span>
                        );
                      })}
                      <span>{questionCount} questions</span>
                    </div>
                  </div>
                  <div className="flex flex-wrap items-center gap-2">
                    {missingAudio > 0 && (
                      <Badge variant="outline" className="border-amber-500/40 text-amber-700">
                        <AlertTriangle className="h-3 w-3" /> {missingAudio} parts without audio
                      </Badge>
                    )}
                    {issues > 0 && (
                      <Badge variant="outline" className="border-red-500/40 text-red-700">
                        <AlertTriangle className="h-3 w-3" /> {issues} flagged
                      </Badge>
                    )}
                  </div>
                </CardContent>
              </Card>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
