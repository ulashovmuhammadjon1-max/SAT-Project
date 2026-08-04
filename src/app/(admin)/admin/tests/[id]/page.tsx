import { notFound } from "next/navigation";
import Link from "next/link";
import { AlertTriangle, UploadCloud } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { TestActions } from "@/components/admin/test-actions";
import { EditTestDialog } from "@/components/admin/edit-test-dialog";
import { DeleteModuleButton } from "@/components/admin/module-actions";
import { prisma } from "@/lib/prisma";

export const dynamic = "force-dynamic";

const ALL_SLOTS = [
  { subject: "READING_WRITING" as const, order: 1, difficulty: "STANDARD" as const, slot: "1", label: "R&W Module 1" },
  { subject: "READING_WRITING" as const, order: 2, difficulty: "EASY" as const, slot: "2E", label: "R&W Module 2 — Easy" },
  { subject: "READING_WRITING" as const, order: 2, difficulty: "HARD" as const, slot: "2H", label: "R&W Module 2 — Hard" },
  { subject: "MATH" as const, order: 1, difficulty: "STANDARD" as const, slot: "1", label: "Math Module 1" },
  { subject: "MATH" as const, order: 2, difficulty: "EASY" as const, slot: "2E", label: "Math Module 2 — Easy" },
  { subject: "MATH" as const, order: 2, difficulty: "HARD" as const, slot: "2H", label: "Math Module 2 — Hard" },
];

export default async function AdminTestDetailPage({ params }: { params: { id: string } }) {
  const test = await prisma.test.findUnique({
    where: { id: params.id },
    include: {
      modules: {
        orderBy: [{ subject: "asc" }, { order: "asc" }],
        include: { questions: { orderBy: { order: "asc" }, include: { choices: true } }, passages: true },
      },
    },
  });

  if (!test) notFound();

  const adaptiveConfigs = await prisma.adaptiveConfig.findMany({
    orderBy: { name: "asc" },
    select: { id: true, name: true },
  });

  const missingSlots =
    test.type === "FULL_LENGTH"
      ? ALL_SLOTS.filter(
          (s) => !test.modules.some((m) => m.subject === s.subject && m.order === s.order && m.difficulty === s.difficulty)
        )
      : [];

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">{test.title}</h1>
          <div className="flex items-center gap-1.5 text-sm text-muted-foreground">
            <span>{test.type.replace("_", " ")}</span>
            <span>·</span>
            <Badge variant={test.status === "PUBLISHED" ? "success" : "secondary"}>{test.status}</Badge>
          </div>
        </div>
        <div className="flex gap-2">
          <EditTestDialog
            testId={test.id}
            title={test.title}
            description={test.description}
            adaptiveConfigId={test.adaptiveConfigId}
            modules={test.modules.map((m) => ({
              id: m.id,
              subject: m.subject,
              order: m.order,
              difficulty: m.difficulty,
              timeLimitMinutes: m.timeLimitMinutes,
            }))}
            adaptiveConfigs={adaptiveConfigs}
          />
          <TestActions testId={test.id} status={test.status} />
        </div>
      </div>

      {test.status !== "PUBLISHED" && (
        <Card className="border-warning/40 bg-warning/5">
          <CardContent className="flex items-center gap-3 p-4 text-sm">
            <AlertTriangle className="h-5 w-5 shrink-0 text-warning" />
            <p>
              This test is a <strong>{test.status}</strong> — students can&apos;t see or take it yet. Click{" "}
              <strong>Publish</strong> above once you&apos;re happy with its modules and questions.
            </p>
          </CardContent>
        </Card>
      )}

      {missingSlots.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-base">Missing modules</CardTitle>
          </CardHeader>
          <CardContent className="flex flex-wrap gap-2">
            {missingSlots.map((s) => (
              <Button key={s.slot + s.subject} variant="outline" size="sm" asChild>
                <Link
                  href={`/admin/uploads?targetTest=${test.id}&subject=${s.subject}&slot=${s.slot}`}
                >
                  <UploadCloud className="h-3.5 w-3.5" /> Upload {s.label}
                </Link>
              </Button>
            ))}
          </CardContent>
        </Card>
      )}

      <div className="space-y-4">
        {test.modules.map((mod) => (
          <Card key={mod.id}>
            <CardHeader>
              <CardTitle className="flex items-center justify-between text-base">
                <span>
                  {mod.subject.replace("_", " ")} · Module {mod.order} ({mod.difficulty})
                  {mod.order === 1 && mod.adaptiveThresholdPct != null && (
                    <span className="ml-2 text-xs font-normal text-muted-foreground">
                      threshold {mod.adaptiveThresholdPct}%
                    </span>
                  )}
                </span>
                <span className="flex items-center gap-2 text-sm font-normal text-muted-foreground">
                  {mod.questions.length} questions · {mod.timeLimitMinutes} min
                  <DeleteModuleButton moduleId={mod.id} />
                </span>
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-2">
              {mod.questions.map((q) => (
                <Link
                  key={q.id}
                  href={`/admin/questions/${q.id}`}
                  className="flex items-center justify-between rounded-lg border border-border p-3 text-sm hover:bg-accent"
                >
                  <span className="line-clamp-1 pr-4">
                    {q.order}. {q.stem.replace(/<[^>]+>/g, "")}
                  </span>
                  <span className="flex shrink-0 items-center gap-2">
                    <Badge variant="outline">{q.difficulty}</Badge>
                    {!q.isPublished && <Badge variant="warning">Draft</Badge>}
                  </span>
                </Link>
              ))}
              {mod.questions.length === 0 && (
                <p className="text-sm text-muted-foreground">No questions in this module yet.</p>
              )}
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
