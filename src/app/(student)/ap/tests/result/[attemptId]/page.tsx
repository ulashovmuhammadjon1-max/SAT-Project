import Link from "next/link";
import { notFound } from "next/navigation";
import {
  ArrowRight,
  BookOpen,
  Check,
  CircleMinus,
  Clock,
  Target,
  TrendingDown,
  X,
} from "lucide-react";

import { formatDuration } from "@/lib/ap/tests";
import {
  getTestResult,
  type ApResultBreakdown,
  type ApResultQuestion,
} from "@/server/actions/student/ap-tests";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "AP Test Result" };
export const dynamic = "force-dynamic";

const LETTERS = ["A", "B", "C", "D", "E"];

/**
 * The result of one practice test: the score, where it came from, and every
 * question with its explanation.
 *
 * The weakest-areas list links into the existing topic practice at
 * /ap/practice/<subject>/<topic>, so a test ends by pointing at the question
 * bank rather than at a number. That link is only rendered for topics the
 * practice route can actually serve — `getTestResult` checks each topic against
 * the course outline instead of assuming every topic code has a page.
 */
export default async function ApTestResultPage({ params }: { params: { attemptId: string } }) {
  await requireUser();
  const result = await getTestResult(params.attemptId);
  if (!result) notFound();

  const minutesSpent = Math.round(result.timeSpentSeconds / 60);

  return (
    <div className="space-y-8">
      <div>
        <Link
          href={`/ap/tests/${result.subjectSlug}`}
          className="text-sm text-muted-foreground hover:text-foreground"
        >
          {result.subjectName} practice tests
        </Link>
        <h1 className="mt-2 font-display text-3xl font-semibold tracking-tight">
          {result.testName}
        </h1>
        <p className="mt-1 text-sm text-muted-foreground">
          Submitted{" "}
          {result.submittedAt
            ? result.submittedAt.toLocaleString(undefined, {
                dateStyle: "medium",
                timeStyle: "short",
              })
            : "just now"}
        </p>
      </div>

      {/* Score */}
      <div className="grid gap-4 sm:grid-cols-4">
        <div className="rounded-2xl border border-border/70 bg-card p-5 shadow-soft sm:col-span-2">
          <p className="text-xs uppercase tracking-wide text-muted-foreground">Raw score</p>
          <p className="mt-1 text-4xl font-semibold tabular-nums leading-none">
            {result.score}
            <span className="text-2xl text-muted-foreground">/{result.total}</span>
          </p>
          <div className="mt-3 h-2 overflow-hidden rounded-full bg-secondary">
            <div className="h-full rounded-full bg-primary" style={{ width: `${result.percent}%` }} />
          </div>
          <p className="mt-2 text-sm text-muted-foreground">
            {result.percent}% of the multiple-choice section
          </p>
        </div>

        <Stat icon={Check} label="Correct" value={result.correct} tone="success" />
        <div className="grid gap-4">
          <Stat icon={X} label="Incorrect" value={result.incorrect} tone="danger" />
          <Stat icon={CircleMinus} label="Skipped" value={result.skipped} tone="muted" />
        </div>
      </div>

      <div className="flex flex-wrap items-center gap-x-6 gap-y-2 text-sm text-muted-foreground">
        <span className="flex items-center gap-1.5">
          <Clock className="h-4 w-4" />
          {minutesSpent < 1 ? "Under a minute" : formatDuration(minutesSpent)} spent of{" "}
          {formatDuration(result.allowedMinutes)} allowed
        </span>
        <span className="flex items-center gap-1.5">
          <Target className="h-4 w-4" />
          {result.topics.length} topics examined across {result.units.length} units
        </span>
      </div>

      {/* Weakest areas */}
      {result.weakest.length > 0 && (
        <section className="rounded-2xl border border-border/70 bg-card p-5 shadow-soft">
          <div className="flex items-center gap-2">
            <TrendingDown className="h-5 w-5 text-warning" />
            <h2 className="font-display text-lg font-semibold">Where to work next</h2>
          </div>
          <p className="mt-1 text-sm text-muted-foreground">
            The topics this test found weakest, worst first. Each one opens its full question set.
          </p>
          <ul className="mt-4 divide-y divide-border/60">
            {result.weakest.map((t) => (
              <li key={t.key} className="flex flex-wrap items-center gap-3 py-3">
                <span className="min-w-[200px] flex-1">
                  <span className="block text-sm font-medium leading-snug">{t.label}</span>
                  <span className="text-xs text-muted-foreground">{t.sublabel}</span>
                </span>
                <span className="text-sm tabular-nums text-muted-foreground">
                  {t.correct}/{t.total} correct
                </span>
                <span
                  className={cn(
                    "rounded-full px-2.5 py-0.5 text-xs font-medium tabular-nums",
                    t.percent >= 50 ? "bg-warning/15 text-warning" : "bg-destructive/10 text-destructive",
                  )}
                >
                  {t.percent}%
                </span>
                {t.practiceHref && (
                  <Link
                    href={t.practiceHref}
                    className="inline-flex items-center gap-1.5 rounded-lg border border-border px-3 py-1.5 text-sm font-medium transition-colors hover:border-primary/50 hover:text-primary"
                  >
                    <BookOpen className="h-3.5 w-3.5" /> Practise
                    <ArrowRight className="h-3.5 w-3.5" />
                  </Link>
                )}
              </li>
            ))}
          </ul>
        </section>
      )}

      {/* Breakdowns */}
      {result.sections.length > 1 && (
        <Breakdown title="By section" rows={result.sections} />
      )}
      <Breakdown title="By unit" rows={result.units} />
      <Breakdown title="By topic" rows={result.topics} collapsible />

      {/* Question review */}
      <section className="space-y-4">
        <h2 className="font-display text-lg font-semibold">Every question</h2>
        {result.questions.map((q) => (
          <QuestionReview key={q.id} q={q} />
        ))}
      </section>

      <div className="flex flex-wrap gap-3">
        <Link
          href={`/ap/tests/${result.subjectSlug}`}
          className="inline-flex items-center gap-1.5 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-primary/90"
        >
          Back to {result.subjectName} tests
          <ArrowRight className="h-4 w-4" />
        </Link>
        <Link
          href={`/ap/${result.subjectSlug}`}
          className="inline-flex items-center gap-1.5 rounded-lg border border-border px-4 py-2 text-sm font-medium transition-colors hover:border-primary/50 hover:text-primary"
        >
          <BookOpen className="h-4 w-4" /> Course topics
        </Link>
      </div>
    </div>
  );
}

function Stat({
  icon: Icon,
  label,
  value,
  tone,
}: {
  icon: React.ComponentType<{ className?: string }>;
  label: string;
  value: number;
  tone: "success" | "danger" | "muted";
}) {
  return (
    <div className="rounded-2xl border border-border/70 bg-card p-5 shadow-soft">
      <p className="flex items-center gap-1.5 text-xs uppercase tracking-wide text-muted-foreground">
        <Icon
          className={cn(
            "h-3.5 w-3.5",
            tone === "success" && "text-success",
            tone === "danger" && "text-destructive",
          )}
        />
        {label}
      </p>
      <p className="mt-1 text-3xl font-semibold tabular-nums leading-none">{value}</p>
    </div>
  );
}

function Breakdown({
  title,
  rows,
  collapsible,
}: {
  title: string;
  rows: ApResultBreakdown[];
  collapsible?: boolean;
}) {
  if (rows.length === 0) return null;

  const body = (
    <ul className="divide-y divide-border/60">
      {rows.map((r) => (
        <li key={r.key} className="flex flex-wrap items-center gap-3 py-3">
          <span className="min-w-[200px] flex-1">
            <span className="block text-sm font-medium leading-snug">{r.label}</span>
            {r.sublabel && <span className="text-xs text-muted-foreground">{r.sublabel}</span>}
          </span>
          <span className="h-1.5 w-32 overflow-hidden rounded-full bg-secondary">
            <span
              className={cn(
                "block h-full rounded-full",
                r.percent >= 75 ? "bg-success" : r.percent >= 50 ? "bg-warning" : "bg-destructive",
              )}
              style={{ width: `${r.percent}%` }}
            />
          </span>
          <span className="w-28 text-right text-sm tabular-nums text-muted-foreground">
            {r.correct}/{r.total} · {r.percent}%
          </span>
        </li>
      ))}
    </ul>
  );

  if (collapsible) {
    return (
      <details className="rounded-2xl border border-border/70 bg-card p-5 shadow-soft">
        <summary className="cursor-pointer font-display text-lg font-semibold">
          {title}{" "}
          <span className="text-sm font-normal text-muted-foreground">({rows.length})</span>
        </summary>
        <div className="mt-3">{body}</div>
      </details>
    );
  }

  return (
    <section className="rounded-2xl border border-border/70 bg-card p-5 shadow-soft">
      <h2 className="font-display text-lg font-semibold">{title}</h2>
      <div className="mt-3">{body}</div>
    </section>
  );
}

function QuestionReview({ q }: { q: ApResultQuestion }) {
  const skipped = q.chosenIndex === null;
  return (
    <div
      className={cn(
        "rounded-2xl border bg-card p-5 shadow-soft",
        q.isCorrect ? "border-success/40" : skipped ? "border-border/70" : "border-destructive/40",
      )}
    >
      <div className="flex flex-wrap items-center gap-2">
        <span className="flex h-7 w-7 items-center justify-center rounded-lg bg-secondary text-sm font-semibold tabular-nums">
          {q.number}
        </span>
        <span
          className={cn(
            "rounded-full px-2.5 py-0.5 text-xs font-medium",
            q.isCorrect
              ? "bg-success/15 text-success"
              : skipped
                ? "bg-secondary text-muted-foreground"
                : "bg-destructive/10 text-destructive",
          )}
        >
          {q.isCorrect ? "Correct" : skipped ? "Skipped" : "Incorrect"}
        </span>
        <span className="text-xs text-muted-foreground">
          Unit {q.unit} · {q.topic} {q.topicTitle}
        </span>
      </div>

      {q.table && (
        <div className="mt-3 overflow-x-auto">
          <table className="border-collapse text-sm">
            <thead>
              <tr>
                {q.table.headers.map((h, i) => (
                  <th
                    key={i}
                    className="border border-border px-3 py-1.5 text-left font-semibold bg-secondary/60"
                  >
                    {h}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {q.table.rows.map((row, i) => (
                <tr key={i}>
                  {row.map((cell, j) => (
                    <td key={j} className="border border-border px-3 py-1.5">
                      {cell}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <p className="mt-3 text-[15px] leading-relaxed">{q.stem}</p>

      <ul className="mt-3 space-y-1.5">
        {q.choices.map((choice, i) => {
          const isKey = i === q.correctIndex;
          const isPick = i === q.chosenIndex;
          return (
            <li
              key={i}
              className={cn(
                "flex items-start gap-2.5 rounded-lg border px-3 py-2 text-sm",
                isKey && "border-success/50 bg-success/5",
                !isKey && isPick && "border-destructive/50 bg-destructive/5",
                !isKey && !isPick && "border-border/60",
              )}
            >
              <span
                className={cn(
                  "flex h-6 w-6 shrink-0 items-center justify-center rounded-full border text-xs font-semibold",
                  isKey && "border-success bg-success text-white",
                  !isKey && isPick && "border-destructive bg-destructive text-white",
                  !isKey && !isPick && "border-border text-muted-foreground",
                )}
              >
                {LETTERS[i]}
              </span>
              <span className="min-w-0 flex-1 leading-relaxed">{choice}</span>
              {isKey && <span className="shrink-0 text-xs font-medium text-success">Correct</span>}
              {!isKey && isPick && (
                <span className="shrink-0 text-xs font-medium text-destructive">Your answer</span>
              )}
            </li>
          );
        })}
      </ul>

      {q.explanation && (
        <p className="mt-3 rounded-lg bg-secondary/50 px-3 py-2.5 text-sm leading-relaxed text-muted-foreground">
          {q.explanation}
        </p>
      )}
    </div>
  );
}
