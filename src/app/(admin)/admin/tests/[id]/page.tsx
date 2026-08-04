import { notFound } from "next/navigation";
import Link from "next/link";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { TestActions } from "@/components/admin/test-actions";
import { prisma } from "@/lib/prisma";

export const dynamic = "force-dynamic";

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
        <TestActions testId={test.id} status={test.status} />
      </div>

      <div className="space-y-4">
        {test.modules.map((mod) => (
          <Card key={mod.id}>
            <CardHeader>
              <CardTitle className="flex items-center justify-between text-base">
                <span>
                  {mod.subject.replace("_", " ")} · Module {mod.order} ({mod.difficulty})
                </span>
                <span className="text-sm font-normal text-muted-foreground">
                  {mod.questions.length} questions · {mod.timeLimitMinutes} min
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
