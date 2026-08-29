import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowRight, BookOpen, CheckCircle2, Clock } from "lucide-react";

import { courseBySlug } from "@/lib/ap/courses";
import { getApProgress } from "@/server/actions/student/ap";
import { requireUser } from "@/lib/session";

export const metadata = { title: "AP Course" };
export const dynamic = "force-dynamic";

const pct = (a: number, b: number) => (b === 0 ? 0 : Math.round((a / b) * 100));

/**
 * One AP course: its units in CED order. Units with live questions expand
 * into topics with per-topic progress and a Practice button; the rest are
 * honestly labeled as coming soon rather than dressed up as content.
 */
export default async function ApSubjectPage({ params }: { params: { slug: string } }) {
  await requireUser();
  const course = courseBySlug(params.slug);
  if (!course) notFound();

  const progress = await getApProgress();
  const mine = progress.find((p) => p.subject === course.code);
  const topicProgress = new Map(mine?.topics.map((t) => [t.topic, t]) ?? []);

  return (
    <div className="space-y-8">
      <div>
        <Link href="/ap" className="text-sm text-muted-foreground hover:text-foreground">
          AP Prep
        </Link>
        <div className={`mt-2 rounded-2xl bg-gradient-to-br ${course.gradient} p-6 text-white shadow-soft`}>
          <h1 className="font-display text-3xl font-semibold tracking-tight">{course.name}</h1>
          <p className="mt-1 max-w-xl text-sm text-white/85">{course.blurb}</p>
          {mine && mine.total > 0 && (
            <p className="mt-4 text-sm text-white/90">
              {mine.answered}/{mine.total} questions answered
              {mine.answered > 0 && <> · {pct(mine.correct, mine.answered)}% correct</>}
            </p>
          )}
        </div>
      </div>

      <section className="space-y-4">
        {course.units.map((unit) => {
          const topics = unit.topics ?? [];
          const hasContent = topics.some((t) => (topicProgress.get(t.code)?.total ?? 0) > 0);
          return (
            <div key={unit.number} className="rounded-2xl border border-border/70 bg-card shadow-soft">
              <div className="flex items-center gap-3 px-5 py-4">
                <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-primary/10 text-sm font-semibold text-primary">
                  {unit.number}
                </span>
                <p className="min-w-0 flex-1 font-medium leading-snug">
                  Unit {unit.number} — {unit.title}
                </p>
                {!hasContent && (
                  <span className="flex shrink-0 items-center gap-1.5 rounded-full bg-secondary px-2.5 py-1 text-xs text-muted-foreground">
                    <Clock className="h-3 w-3" /> Coming soon
                  </span>
                )}
              </div>

              {hasContent && (
                <div className="divide-y divide-border/60 border-t border-border/60">
                  {topics.map((t) => {
                    const p = topicProgress.get(t.code);
                    if (!p || p.total === 0) return null;
                    const done = p.answered >= p.total;
                    return (
                      <div key={t.code} className="flex flex-wrap items-center gap-3 px-5 py-3">
                        <span className="w-8 shrink-0 text-sm font-semibold tabular-nums text-muted-foreground">
                          {t.code}
                        </span>
                        <span className="min-w-[180px] flex-1">
                          <span className="block text-sm font-medium leading-snug">{t.title}</span>
                          <span className="mt-1 flex items-center gap-2">
                            <span className="h-1.5 w-32 overflow-hidden rounded-full bg-secondary">
                              <span
                                className="block h-full rounded-full bg-primary"
                                style={{ width: `${pct(p.answered, p.total)}%` }}
                              />
                            </span>
                            <span className="text-xs tabular-nums text-muted-foreground">
                              {p.answered}/{p.total}
                              {p.answered > 0 && <> · {pct(p.correct, p.answered)}% correct</>}
                            </span>
                          </span>
                        </span>
                        {done ? (
                          <span className="flex items-center gap-1.5 text-sm font-medium text-success">
                            <CheckCircle2 className="h-4 w-4" /> Complete
                          </span>
                        ) : null}
                        <Link
                          href={`/ap/${course.slug}/practice/${t.code}`}
                          className="inline-flex items-center gap-1.5 rounded-lg border border-border px-3 py-1.5 text-sm font-medium transition-colors hover:border-primary/50 hover:text-primary"
                        >
                          <BookOpen className="h-3.5 w-3.5" />
                          {p.answered === 0 ? "Practice" : done ? "Review" : "Continue"}
                          <ArrowRight className="h-3.5 w-3.5" />
                        </Link>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          );
        })}
      </section>

      <p className="text-sm text-muted-foreground">
        More units are being written now — each one arrives with full explanations, the same way
        Unit 1 did.
      </p>
    </div>
  );
}
