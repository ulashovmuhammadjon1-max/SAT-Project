import Link from "next/link";
import { ChevronRight } from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";
import { cn } from "@/lib/utils";
import type { DomainProgress, QuestionBankOverview } from "@/server/actions/student/question-bank";

/** Colour the accuracy bar by band so weak skills are visible at a glance. */
function accuracyTone(pct: number) {
  if (pct >= 80) return "bg-success";
  if (pct >= 60) return "bg-warning";
  return "bg-destructive";
}

export function OverviewStats({ overview }: { overview: QuestionBankOverview }) {
  if (!overview.hasData) {
    return (
      <Card>
        <CardContent className="flex flex-col items-start gap-1 p-6">
          <p className="font-medium">Start practicing to see your progress.</p>
          <p className="text-sm text-muted-foreground">
            {overview.totalQuestions.toLocaleString()} questions are available. Your accuracy, weak
            skills and mistakes appear here once you answer your first one.
          </p>
        </CardContent>
      </Card>
    );
  }

  const stats = [
    { label: "Attempted", value: overview.attempted.toLocaleString(), tone: "" },
    { label: "Accuracy", value: `${overview.accuracyPct}%`, tone: "text-success" },
    { label: "Completed", value: `${overview.completionPct}%`, tone: "" },
    { label: "Saved", value: overview.saved.toLocaleString(), tone: "" },
    { label: "Mistakes", value: overview.incorrect.toLocaleString(), tone: "text-destructive" },
  ];

  return (
    <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-5">
      {stats.map((s) => (
        <Card key={s.label}>
          <CardContent className="p-4">
            <p className={cn("font-display text-2xl font-semibold tabular-nums", s.tone)}>{s.value}</p>
            <p className="mt-0.5 text-xs text-muted-foreground">{s.label}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}

export function DomainProgressList({
  domains,
  subject,
}: {
  domains: DomainProgress[];
  subject: string;
}) {
  return (
    <div className="space-y-4">
      {domains.map((d) => (
        <Card key={d.domainId}>
          <CardContent className="p-5">
            <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
              <h3 className="font-display text-base font-semibold">{d.domainName}</h3>
              <p className="text-xs text-muted-foreground tabular-nums">
                {d.attempted} / {d.total} attempted
                {d.attempted > 0 && <> · {d.accuracyPct}% accuracy</>}
              </p>
            </div>

            <ul className="mt-4 space-y-3">
              {d.skills.map((s) => {
                const attemptedPct = s.total ? Math.round((s.attempted / s.total) * 100) : 0;
                return (
                  <li key={s.skillId}>
                    <Link
                      href={`/practice/start?subject=${subject}&skillId=${s.skillId}`}
                      className="group -mx-2 block rounded-lg px-2 py-1.5 transition-colors hover:bg-secondary/60 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
                    >
                      <div className="flex items-center justify-between gap-3">
                        <span className="text-sm font-medium">{s.skillName}</span>
                        <span className="flex shrink-0 items-center gap-1.5 text-xs text-muted-foreground tabular-nums">
                          {s.attempted} / {s.total}
                          {s.attempted > 0 && (
                            <span className={cn(s.accuracyPct >= 80 ? "text-success" : s.accuracyPct < 60 ? "text-destructive" : "")}>
                              · {s.accuracyPct}%
                            </span>
                          )}
                          <ChevronRight className="h-3.5 w-3.5 opacity-0 transition-opacity group-hover:opacity-100" />
                        </span>
                      </div>
                      <div className="mt-1.5 h-1.5 overflow-hidden rounded-full bg-secondary">
                        <div
                          className={cn(
                            "h-full rounded-full transition-all",
                            s.attempted ? accuracyTone(s.accuracyPct) : "bg-border"
                          )}
                          style={{ width: `${attemptedPct}%` }}
                        />
                      </div>
                    </Link>
                  </li>
                );
              })}
            </ul>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
