import Link from "next/link";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "Question Bank" };
export const dynamic = "force-dynamic";

export default async function PracticePage({ searchParams }: { searchParams: { domain?: string } }) {
  const domains = await prisma.domain.findMany({
    orderBy: { name: "asc" },
    include: { _count: { select: { questions: { where: { isPublished: true } } } } },
  });

  const questions = await prisma.question.findMany({
    where: { isPublished: true, domainId: searchParams.domain || undefined },
    take: 40,
    include: { domain: true, skill: true },
    orderBy: { createdAt: "desc" },
  });

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Question Bank</h1>
        <p className="text-sm text-muted-foreground">
          Practice by domain and skill, untimed, with instant explanations.
        </p>
      </div>

      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <Link href="/practice">
          <Card className={!searchParams.domain ? "border-primary" : undefined}>
            <CardContent className="p-4">
              <p className="text-sm font-medium">All domains</p>
            </CardContent>
          </Card>
        </Link>
        {domains.map((d) => (
          <Link key={d.id} href={`/practice?domain=${d.id}`}>
            <Card className={searchParams.domain === d.id ? "border-primary" : undefined}>
              <CardContent className="p-4">
                <p className="text-sm font-medium">{d.name}</p>
                <p className="text-xs text-muted-foreground">{d._count.questions} questions</p>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>

      <div className="space-y-2">
        {questions.map((q) => (
          <Link key={q.id} href={`/practice/${q.id}`}>
            <Card className="transition-colors hover:border-primary">
              <CardContent className="flex items-center justify-between gap-4 p-4">
                <p className="line-clamp-1 flex-1 text-sm" dangerouslySetInnerHTML={{ __html: q.stem }} />
                <div className="flex shrink-0 gap-2">
                  <Badge variant="outline">{q.skill.name}</Badge>
                  <Badge variant="outline">{q.difficulty}</Badge>
                </div>
              </CardContent>
            </Card>
          </Link>
        ))}
        {questions.length === 0 && (
          <p className="text-sm text-muted-foreground">No published questions in this domain yet.</p>
        )}
      </div>
    </div>
  );
}
