import Link from "next/link";
import { notFound } from "next/navigation";
import { AlertTriangle, ArrowLeft, VolumeX } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import { QUESTION_TYPE_LABEL } from "@/lib/ielts/constants";

export const metadata = { title: "IELTS Paper" };
export const dynamic = "force-dynamic";

interface Option { key: string; text: string }

/**
 * Render a group body, turning `{{7}}` markers into visible numbered gaps.
 *
 * The body is trusted HTML built by the importer, not user input — but the gap
 * substitution happens on the STRING before it reaches the DOM, so a marker can
 * never be produced by content and interpreted as markup.
 */
function GroupBody({ html }: { html: string }) {
  const withGaps = html.replace(
    /\{\{(\d+)\}\}/g,
    (_, n) =>
      `<span class="inline-flex min-w-[104px] items-center gap-1 rounded border border-dashed ` +
      `border-navy-900/40 bg-secondary/60 px-2 py-0.5 align-middle text-xs font-semibold">` +
      `<span class="text-muted-foreground">${n}</span>` +
      `<span class="text-muted-foreground/60">answer</span></span>`
  );
  return (
    <div
      className="ielts-body space-y-1 text-sm leading-relaxed [&_h4]:mt-3 [&_h4]:font-semibold [&_li]:ml-4 [&_li]:list-disc [&_ul]:space-y-1"
      dangerouslySetInnerHTML={{ __html: withGaps }}
    />
  );
}

export default async function AdminIeltsTestPage({
  params,
}: {
  params: { testId: string };
}) {
  await requireAdmin();

  const test = await prisma.ieltsTest.findUnique({
    where: { id: params.testId },
    include: {
      sections: {
        orderBy: { order: "asc" },
        include: {
          parts: {
            orderBy: { partNumber: "asc" },
            include: {
              groups: {
                orderBy: { order: "asc" },
                include: { questions: { orderBy: { number: "asc" } } },
              },
            },
          },
        },
      },
    },
  });
  if (!test) notFound();

  return (
    <div className="space-y-6">
      <Link
        href="/admin/ielts/papers"
        className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground"
      >
        <ArrowLeft className="h-4 w-4" /> IELTS Papers
      </Link>

      <div className="flex flex-wrap items-center gap-3">
        <h1 className="font-display text-2xl font-semibold tracking-tight">{test.title}</h1>
        <Badge variant={test.status === "PUBLISHED" ? "navy" : "outline"}>{test.status}</Badge>
        <Badge variant="outline">{test.module.replace("_", " ")}</Badge>
      </div>
      {test.description && (
        <p className="text-sm text-muted-foreground">{test.description}</p>
      )}

      {test.sections.map((section) => (
        <div key={section.id} className="space-y-4">
          <div className="flex flex-wrap items-center gap-2 border-b border-border pb-2">
            <h2 className="font-display text-lg font-semibold">
              {section.skill.charAt(0) + section.skill.slice(1).toLowerCase()}
            </h2>
            <Badge variant="outline">{section.durationMinutes} min</Badge>
            {section.instructions && (
              <span className="text-xs text-muted-foreground">{section.instructions}</span>
            )}
          </div>

          {section.parts.map((part) => (
            <Card key={part.id}>
              <CardHeader className="flex flex-row flex-wrap items-center justify-between gap-2 space-y-0">
                <CardTitle className="text-base">
                  {part.title ?? `Part ${part.partNumber}`}
                </CardTitle>
                <div className="flex flex-wrap items-center gap-2">
                  {section.skill === "LISTENING" && !part.audioUrl && (
                    <Badge variant="outline" className="border-amber-500/40 text-amber-700">
                      <VolumeX className="h-3 w-3" /> no audio attached
                    </Badge>
                  )}
                  <Badge variant="outline">
                    {part.groups.reduce((n, g) => n + g.questions.length, 0)} questions
                  </Badge>
                </div>
              </CardHeader>
              <CardContent className="space-y-6">
                {part.instructions && (
                  <p className="text-sm text-muted-foreground">{part.instructions}</p>
                )}

                {part.groups.map((group) => {
                  const options = (group.optionsJson as Option[] | null) ?? null;
                  const first = group.questions[0]?.number;
                  const last = group.questions[group.questions.length - 1]?.number;
                  return (
                    <div key={group.id} className="space-y-3 rounded-lg border border-border p-4">
                      <div className="flex flex-wrap items-center gap-2">
                        <span className="text-sm font-semibold">
                          Questions {first}–{last}
                        </span>
                        <Badge variant="outline">
                          {QUESTION_TYPE_LABEL[group.type] ?? group.type}
                        </Badge>
                        {group.wordLimit && (
                          <Badge variant="outline" className="uppercase">
                            {group.wordLimit}
                          </Badge>
                        )}
                      </div>
                      {group.instructions && (
                        <p className="text-sm italic text-muted-foreground">
                          {group.instructions}
                        </p>
                      )}

                      {group.bodyHtml && (
                        <div className="rounded-md bg-secondary/40 p-3">
                          <GroupBody html={group.bodyHtml} />
                        </div>
                      )}

                      {options && (
                        <div className="rounded-md border border-border p-3">
                          <p className="mb-1.5 text-xs font-semibold uppercase tracking-wide text-muted-foreground">
                            Options
                          </p>
                          <ul className="grid gap-1 text-sm sm:grid-cols-2">
                            {options.map((o) => (
                              <li key={o.key}>
                                <span className="font-semibold">{o.key}</span> &nbsp;{o.text}
                              </li>
                            ))}
                          </ul>
                        </div>
                      )}

                      <div className="space-y-2">
                        {group.questions.map((q) => {
                          const perQ = (q.optionsJson as Option[] | null) ?? null;
                          const meta = q.metadata as { findings?: string[] } | null;
                          const findings = meta?.findings ?? [];
                          return (
                            <div
                              key={q.id}
                              className="flex gap-3 rounded-md border border-border/70 p-2.5 text-sm"
                            >
                              <span className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded bg-navy-900 text-xs font-semibold text-white">
                                {q.number}
                              </span>
                              <div className="min-w-0 flex-1 space-y-1.5">
                                {q.promptHtml && <p>{q.promptHtml}</p>}
                                {perQ && (
                                  <ul className="space-y-0.5 text-muted-foreground">
                                    {perQ.map((o) => (
                                      <li key={o.key}>
                                        <span className="font-semibold">{o.key}</span> {o.text}
                                      </li>
                                    ))}
                                  </ul>
                                )}
                                <p className="text-xs">
                                  <span className="text-muted-foreground">Answer: </span>
                                  <span className="font-semibold text-emerald-700 dark:text-emerald-400">
                                    {q.correctAnswer}
                                  </span>
                                  {Array.isArray(q.acceptedAnswers) &&
                                    (q.acceptedAnswers as string[]).length > 0 && (
                                      <span className="text-muted-foreground">
                                        {"  (also accepts "}
                                        {(q.acceptedAnswers as string[]).join(", ")})
                                      </span>
                                    )}
                                </p>
                                {findings.map((f) => (
                                  <p
                                    key={f}
                                    className="flex items-start gap-1.5 rounded border-l-2 border-red-500 bg-red-50 px-2 py-1 text-xs text-red-800 dark:bg-red-950/30 dark:text-red-300"
                                  >
                                    <AlertTriangle className="mt-0.5 h-3 w-3 shrink-0" />
                                    {f}
                                  </p>
                                ))}
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  );
                })}
              </CardContent>
            </Card>
          ))}
        </div>
      ))}
    </div>
  );
}
