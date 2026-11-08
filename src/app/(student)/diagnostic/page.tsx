import Link from "next/link";
import {
  ArrowRight,
  BookOpenCheck,
  Calculator,
  CheckCircle2,
  Clock,
  Feather,
  PauseCircle,
  Sparkles,
  Target,
  TrendingUp,
} from "lucide-react";

import { Button } from "@/components/ui/button";
import { EnableDiagnosticButton, StartDiagnosticButton } from "@/components/student/diagnostic-actions";
import { DIAGNOSTIC_MINUTES, DIAGNOSTIC_SIZE, type DiagnosticResult } from "@/lib/diagnostic";
import { prisma } from "@/lib/prisma";
import { requireVerifiedUser } from "@/lib/session";
import { getMyDiagnostics, type DiagnosticStatus } from "@/server/actions/student/diagnostic";

export const metadata = { title: "Free diagnostic" };
export const dynamic = "force-dynamic";

export default async function DiagnosticPage({ searchParams }: { searchParams: { done?: string } }) {
  const user = await requireVerifiedUser();
  const [diagnostics, account] = await Promise.all([
    getMyDiagnostics(),
    prisma.user.findUnique({ where: { id: user.id }, select: { preparationExams: true, name: true } }),
  ]);
  const exams = account?.preparationExams?.length ? account.preparationExams : ["SAT"];
  const sat = diagnostics.find((d) => d.kind === "SAT");
  const ielts = diagnostics.find((d) => d.kind === "IELTS");
  const firstName = (account?.name ?? "").trim().split(/\s+/)[0] || "there";

  return (
    <div className="mx-auto max-w-4xl space-y-8">
      <header>
        <p className="flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.18em] text-primary">
          <Sparkles className="h-3.5 w-3.5" /> Free diagnostic
        </p>
        <h1 className="mt-2 font-serif text-4xl font-medium tracking-tight">
          {searchParams.done && sat?.state === "DONE" ? `Nice work, ${firstName}.` : "Find out where you stand."}
        </h1>
        <p className="mt-2 max-w-2xl text-[15px] text-muted-foreground">
          {searchParams.done && sat?.state === "DONE"
            ? "Here is what your diagnostic says, and exactly what to work on first. Your study plan has already been updated with these answers."
            : "One short test tells us your starting level and your weakest skills, so every practice session after it is aimed at the right thing."}
        </p>
      </header>

      {(exams.includes("SAT") || sat) && <SatPanel status={sat} />}
      {(exams.includes("IELTS") || ielts) && <IeltsPanel status={ielts} />}
    </div>
  );
}

function SatPanel({ status }: { status: DiagnosticStatus | undefined }) {
  if (status?.state === "DONE" && status.result) return <SatResult result={status.result} completedAt={status.completedAt} />;
  return (
    <section className="overflow-hidden rounded-2xl border border-border bg-card shadow-sm">
      <div className="relative border-b border-border bg-gradient-to-br from-primary/[0.12] via-card to-card px-6 py-6 sm:px-8">
        <p className="text-xs font-semibold uppercase tracking-wider text-primary">SAT diagnostic</p>
        <h2 className="mt-1 font-display text-2xl font-semibold tracking-tight">
          {status?.state === "IN_PROGRESS" ? "Your diagnostic is in progress" : status ? "Your diagnostic is ready" : "Take a free SAT diagnostic"}
        </h2>
        <p className="mt-1 max-w-xl text-sm text-muted-foreground">
          Every domain of the Digital SAT, from easy to hard, in the same test screen you will use for full practice tests.
        </p>
      </div>
      <div className="grid gap-4 px-6 py-6 sm:grid-cols-2 sm:px-8">
        <Fact icon={BookOpenCheck} title={`${DIAGNOSTIC_SIZE} questions`} body="13 Reading and Writing, then 12 Math" />
        <Fact icon={Clock} title={`About ${DIAGNOSTIC_MINUTES} minutes`} body="No timer. Take the time you need" />
        <Fact icon={Calculator} title="Calculator and reference sheet" body="Available on every Math question" />
        <Fact icon={PauseCircle} title="Pause any time" body="Leave and come back; your answers are kept" />
      </div>
      <div className="flex flex-col gap-3 border-t border-border bg-secondary/30 px-6 py-5 sm:flex-row sm:items-center sm:justify-between sm:px-8">
        <p className="text-sm text-muted-foreground">Answers are not shown until the end, so the result reflects what you really know.</p>
        {status ? (
          <StartDiagnosticButton kind="SAT" size="lg" label={status.state === "IN_PROGRESS" ? "Continue diagnostic" : "Start diagnostic"} />
        ) : (
          <EnableDiagnosticButton kind="SAT" label="Enable my free diagnostic" />
        )}
      </div>
    </section>
  );
}

function SatResult({ result, completedAt }: { result: DiagnosticResult; completedAt: string | null }) {
  return (
    <section className="space-y-6">
      <div className="overflow-hidden rounded-2xl border border-border bg-card shadow-sm">
        <div className="grid gap-6 bg-gradient-to-br from-primary/[0.12] via-card to-card px-6 py-7 sm:grid-cols-[1.1fr_1fr] sm:px-8">
          <div>
            <p className="text-xs font-semibold uppercase tracking-wider text-primary">Estimated SAT score</p>
            <p className="mt-2 font-serif text-6xl font-medium tabular-nums tracking-tight">{result.total.estimate}</p>
            <p className="mt-1 text-sm text-muted-foreground">
              Likely range {result.total.low}–{result.total.high}. An estimate from {DIAGNOSTIC_SIZE} questions, not an
              official score.
            </p>
            {completedAt && (
              <p className="mt-1 text-xs text-muted-foreground">
                Taken {new Date(completedAt).toISOString().slice(0, 10)}
              </p>
            )}
          </div>
          <div className="space-y-4">
            {result.sections.map((s) => (
              <div key={s.subject}>
                <div className="flex items-baseline justify-between">
                  <p className="text-sm font-semibold">{s.label}</p>
                  <p className="font-display text-xl font-semibold tabular-nums">{s.estimate}</p>
                </div>
                <div className="mt-1.5 h-2 overflow-hidden rounded-full bg-secondary">
                  <div className="h-full rounded-full bg-primary" style={{ width: `${((s.estimate - 200) / 600) * 100}%` }} />
                </div>
                <p className="mt-1 text-xs text-muted-foreground">
                  {s.correct} of {s.questions} correct
                  {s.answered < s.questions ? ` · ${s.questions - s.answered} skipped` : ""} · range {s.low}–{s.high}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        <div className="rounded-2xl border border-border bg-card p-6 shadow-sm">
          <h3 className="flex items-center gap-2 font-display text-lg font-semibold">
            <Target className="h-5 w-5 text-primary" /> Work on these first
          </h3>
          {result.focus.length === 0 ? (
            <p className="mt-2 text-sm text-muted-foreground">You answered everything correctly. Try a full practice test next.</p>
          ) : (
            <ul className="mt-3 space-y-2">
              {result.focus.map((f) => (
                <li key={f.skillId}>
                  <Link
                    href={`/practice/start?subject=${f.subject}&skillId=${f.skillId}`}
                    className="group flex items-center justify-between gap-3 rounded-xl border border-border px-3.5 py-2.5 transition-colors hover:border-primary/40 hover:bg-primary/[0.04]"
                  >
                    <span>
                      <span className="block text-sm font-medium">{f.skillName}</span>
                      <span className="text-xs text-muted-foreground">{f.subject === "MATH" ? "Math" : "Reading and Writing"}</span>
                    </span>
                    <span className="flex items-center gap-1 text-sm font-semibold text-primary">
                      Practise <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                    </span>
                  </Link>
                </li>
              ))}
            </ul>
          )}
        </div>

        <div className="rounded-2xl border border-border bg-card p-6 shadow-sm">
          <h3 className="flex items-center gap-2 font-display text-lg font-semibold">
            <TrendingUp className="h-5 w-5 text-primary" /> By area
          </h3>
          <ul className="mt-3 space-y-3">
            {result.domains.map((d) => {
              const pct = d.questions ? Math.round((d.correct / d.questions) * 100) : 0;
              return (
                <li key={d.name}>
                  <div className="flex items-baseline justify-between text-sm">
                    <span>{d.name}</span>
                    <span className="tabular-nums text-muted-foreground">
                      {d.correct}/{d.questions}
                    </span>
                  </div>
                  <div className="mt-1 h-1.5 overflow-hidden rounded-full bg-secondary">
                    <div
                      className={pct >= 75 ? "h-full rounded-full bg-success" : pct >= 40 ? "h-full rounded-full bg-warning" : "h-full rounded-full bg-destructive"}
                      style={{ width: `${Math.max(pct, 4)}%` }}
                    />
                  </div>
                </li>
              );
            })}
          </ul>
          {result.strengths.length > 0 && (
            <p className="mt-4 flex items-start gap-1.5 text-sm text-muted-foreground">
              <CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0 text-success" /> Strong already: {result.strengths.join(", ")}.
            </p>
          )}
        </div>
      </div>

      <div className="flex flex-col gap-3 sm:flex-row">
        <Button asChild size="lg">
          <Link href="/plan">
            See my study plan <ArrowRight className="h-4 w-4" />
          </Link>
        </Button>
        <Button asChild size="lg" variant="outline">
          <Link href="/tests">Take a full practice test</Link>
        </Button>
      </div>
    </section>
  );
}

function IeltsPanel({ status }: { status: DiagnosticStatus | undefined }) {
  const done = status?.state === "DONE";
  return (
    <section className="overflow-hidden rounded-2xl border border-border bg-card shadow-sm">
      <div className="border-b border-border bg-gradient-to-br from-success/[0.12] via-card to-card px-6 py-6 sm:px-8">
        <p className="text-xs font-semibold uppercase tracking-wider text-success">IELTS diagnostic</p>
        <h2 className="mt-1 font-display text-2xl font-semibold tracking-tight">
          {done ? "Your essay is with a reviewer" : status?.state === "IN_PROGRESS" ? "Finish your diagnostic essay" : "One essay, marked by a person"}
        </h2>
        <p className="mt-1 max-w-xl text-sm text-muted-foreground">
          {done
            ? "A reviewer marks it on all four IELTS criteria and gives you a band and written feedback. You will be notified when it is ready."
            : "Write one Writing Task 2 essay: about 40 minutes, at least 250 words. A real reviewer gives you a band for each criterion and tells you what to fix first."}
        </p>
      </div>
      <div className="flex flex-col gap-3 px-6 py-5 sm:flex-row sm:items-center sm:justify-between sm:px-8">
        <p className="flex items-center gap-2 text-sm text-muted-foreground">
          <Feather className="h-4 w-4" /> Your draft saves itself as you type.
        </p>
        {done ? (
          <Button asChild variant="outline">
            <Link href="/ielts/feedback">Open IELTS feedback</Link>
          </Button>
        ) : status ? (
          <StartDiagnosticButton kind="IELTS" size="lg" label={status.state === "IN_PROGRESS" ? "Continue my essay" : "Start writing"} />
        ) : (
          <EnableDiagnosticButton kind="IELTS" label="Enable my free IELTS diagnostic" />
        )}
      </div>
    </section>
  );
}

function Fact({ icon: Icon, title, body }: { icon: typeof Clock; title: string; body: string }) {
  return (
    <div className="flex items-start gap-3">
      <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-primary/10 text-primary">
        <Icon className="h-[18px] w-[18px]" />
      </span>
      <div>
        <p className="text-sm font-semibold">{title}</p>
        <p className="text-sm text-muted-foreground">{body}</p>
      </div>
    </div>
  );
}
