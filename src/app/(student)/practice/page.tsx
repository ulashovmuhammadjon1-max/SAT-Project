import Link from "next/link";
import { ArrowLeft, BookOpen, Calculator } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { cn } from "@/lib/utils";

export const metadata = { title: "Question Bank" };
export const dynamic = "force-dynamic";

type Subject = "READING_WRITING" | "MATH";

const SUBJECTS: { value: Subject; label: string; description: string; icon: typeof BookOpen }[] = [
  { value: "READING_WRITING", label: "Reading & Writing", description: "EBRW — every domain and subtopic", icon: BookOpen },
  { value: "MATH", label: "Math", description: "Every domain and subtopic", icon: Calculator },
];

export default async function PracticePage({
  searchParams,
}: {
  searchParams: { subject?: string; skill?: string };
}) {
  const subject = (searchParams.subject === "READING_WRITING" || searchParams.subject === "MATH"
    ? searchParams.subject
    : undefined) as Subject | undefined;

  if (!subject) {
    const [rwCount, mathCount] = await Promise.all([
      prisma.question.count({ where: { isPublished: true, domain: { subject: "READING_WRITING" } } }),
      prisma.question.count({ where: { isPublished: true, domain: { subject: "MATH" } } }),
    ]);
    const counts: Record<Subject, number> = { READING_WRITING: rwCount, MATH: mathCount };

    return (
      <div className="space-y-8">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">Question Bank</h1>
          <p className="text-sm text-muted-foreground">
            Practice by domain and subtopic, untimed, with instant explanations.
          </p>
        </div>

        <div className="grid gap-4 sm:grid-cols-2">
          {SUBJECTS.map((s) => (
            <Link key={s.value} href={`/practice?subject=${s.value}`}>
              <Card className="h-full transition-colors hover:border-primary">
                <CardContent className="flex items-start gap-4 p-6">
                  <span className="flex h-11 w-11 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
                    <s.icon className="h-5 w-5" />
                  </span>
                  <div>
                    <p className="font-display text-lg font-semibold">{s.label}</p>
                    <p className="text-sm text-muted-foreground">{s.description}</p>
                    <p className="mt-1 text-xs text-muted-foreground">{counts[s.value]} questions</p>
                  </div>
                </CardContent>
              </Card>
            </Link>
          ))}
        </div>
      </div>
    );
  }

  const domains = await prisma.domain.findMany({
    where: { subject },
    orderBy: { order: "asc" },
    include: {
      skills: {
        orderBy: { order: "asc" },
        include: { _count: { select: { questions: { where: { isPublished: true } } } } },
      },
    },
  });

  const selectedSkillId = searchParams.skill;
  const selectedSkill = selectedSkillId
    ? domains.flatMap((d) => d.skills.map((s) => ({ ...s, domainName: d.name }))).find((s) => s.id === selectedSkillId)
    : undefined;

  const questions = selectedSkillId
    ? await prisma.question.findMany({
        where: { isPublished: true, skillId: selectedSkillId },
        take: 40,
        include: { domain: true, skill: true },
        orderBy: { createdAt: "desc" },
      })
    : [];

  const subjectLabel = SUBJECTS.find((s) => s.value === subject)!.label;

  return (
    <div className="space-y-8">
      <div>
        <Link href="/practice" className="mb-2 inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground">
          <ArrowLeft className="h-3.5 w-3.5" /> All subjects
        </Link>
        <h1 className="font-display text-2xl font-semibold tracking-tight">{subjectLabel} Question Bank</h1>
        <p className="text-sm text-muted-foreground">
          Every domain and its subtopics are listed below — pick one to practice.
        </p>
      </div>

      <div className="space-y-4">
        {domains.map((domain) => (
          <Card key={domain.id} id={`domain-${domain.id}`}>
            <CardContent className="space-y-3 p-5">
              <p className="font-display text-base font-semibold">{domain.name}</p>
              <div className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
                {domain.skills.map((skill) => (
                  <Link key={skill.id} href={`/practice?subject=${subject}&skill=${skill.id}#domain-${domain.id}`}>
                    <div
                      className={cn(
                        "flex items-center justify-between gap-2 rounded-lg border border-border p-3 text-sm transition-colors hover:border-primary hover:bg-accent",
                        selectedSkillId === skill.id && "border-primary bg-accent"
                      )}
                    >
                      <span className="line-clamp-1">{skill.name}</span>
                      <Badge variant="outline" className="shrink-0">
                        {skill._count.questions}
                      </Badge>
                    </div>
                  </Link>
                ))}
                {domain.skills.length === 0 && (
                  <p className="text-sm text-muted-foreground">No subtopics defined for this domain yet.</p>
                )}
              </div>
            </CardContent>
          </Card>
        ))}
        {domains.length === 0 && <p className="text-sm text-muted-foreground">No domains defined for this subject yet.</p>}
      </div>

      {selectedSkillId && (
        <div className="space-y-3">
          <h2 className="font-display text-lg font-semibold">
            {selectedSkill ? `${selectedSkill.domainName} · ${selectedSkill.name}` : "Questions"}
          </h2>
          <div className="space-y-2">
            {questions.map((q) => (
              <Link key={q.id} href={`/practice/${q.id}`}>
                <Card className="transition-colors hover:border-primary">
                  <CardContent className="flex items-center justify-between gap-4 p-4">
                    <p className="line-clamp-1 flex-1 text-sm" dangerouslySetInnerHTML={{ __html: q.stem }} />
                    <div className="flex shrink-0 gap-2">
                      <Badge variant="outline">{q.difficulty}</Badge>
                    </div>
                  </CardContent>
                </Card>
              </Link>
            ))}
            {questions.length === 0 && (
              <p className="text-sm text-muted-foreground">No published questions in this subtopic yet.</p>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
