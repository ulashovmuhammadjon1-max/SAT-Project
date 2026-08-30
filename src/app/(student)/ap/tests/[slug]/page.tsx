import Link from "next/link";
import { notFound } from "next/navigation";
import { Calculator, CircleCheck, Clock, FileText, ListChecks, Timer } from "lucide-react";

import { StartTestButton } from "@/components/ap/start-test-button";
import { subjectBySlug } from "@/lib/ap/catalog";
import { CALCULATOR_LABEL, formatDuration, type ApCalculatorPolicy } from "@/lib/ap/tests";
import { listTestsForSubject } from "@/server/actions/student/ap-tests";
import { requireUser } from "@/lib/session";

export const metadata = { title: "AP Practice Tests" };
export const dynamic = "force-dynamic";

/**
 * Step two: the tests available for one subject.
 *
 * Every test here is one the live bank can actually fill — `listTestsForSubject`
 * drops any whose blueprint the question bank cannot meet, so a card that is
 * visible is a test that will start. Tests still waiting on content are counted
 * honestly at the foot of the page rather than shown as dead buttons.
 */
export default async function ApSubjectTestsPage({ params }: { params: { slug: string } }) {
  await requireUser();
  const entry = subjectBySlug(params.slug);
  if (!entry) notFound();

  const subject = await listTestsForSubject(params.slug);
  // Not enrolled: the tests are real, they are just not this student's yet.
  if (!subject) {
    return (
      <div className="space-y-6">
        <Link href="/ap/tests" className="text-sm text-muted-foreground hover:text-foreground">
          AP Practice Tests
        </Link>
        <div className="rounded-2xl border border-dashed border-border bg-card px-6 py-12 text-center shadow-soft">
          <p className="font-medium">{entry.name} isn&apos;t on your list</p>
          <p className="mx-auto mt-1 max-w-md text-sm text-muted-foreground">
            Add it from the AP hub and its practice tests appear here.
          </p>
          <Link
            href="/ap"
            className="mt-5 inline-flex items-center gap-1.5 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-white hover:bg-primary/90"
          >
            Browse AP subjects
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      <div>
        <Link href="/ap/tests" className="text-sm text-muted-foreground hover:text-foreground">
          AP Practice Tests
        </Link>
        <div
          className={`mt-2 rounded-2xl bg-gradient-to-br ${subject.gradient} p-6 text-white shadow-soft`}
        >
          <h1 className="font-display text-3xl font-semibold tracking-tight">{subject.name}</h1>
          <p className="mt-1 text-sm text-white/85">
            {subject.tests.length} {subject.tests.length === 1 ? "test" : "tests"} built from{" "}
            {subject.questionCount.toLocaleString()} questions. Each form is fixed, so a score you
            beat is a score you really beat.
          </p>
        </div>
      </div>

      {subject.tests.length === 0 ? (
        <div className="rounded-2xl border border-dashed border-border bg-card px-6 py-12 text-center shadow-soft">
          <p className="font-medium">No test is ready for {subject.short} yet</p>
          <p className="mx-auto mt-1 max-w-md text-sm text-muted-foreground">
            The question bank is still being written. Topic practice is open in the meantime.
          </p>
          <Link
            href={`/ap/${subject.slug}`}
            className="mt-5 inline-flex items-center gap-1.5 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-white hover:bg-primary/90"
          >
            Practise {subject.short} by topic
          </Link>
        </div>
      ) : (
        <div className="space-y-4">
          {subject.tests.map((test) => (
            <div
              key={test.slug}
              className="rounded-2xl border border-border/70 bg-card p-5 shadow-soft"
            >
              <div className="flex flex-wrap items-start justify-between gap-4">
                <div className="min-w-0 flex-1">
                  <div className="flex flex-wrap items-center gap-2">
                    <h2 className="font-display text-lg font-semibold">{test.name}</h2>
                    {test.inProgressAttemptId ? (
                      <span className="rounded-full bg-warning/15 px-2.5 py-0.5 text-xs font-medium text-warning">
                        In progress
                      </span>
                    ) : test.attemptCount > 0 ? (
                      <span className="flex items-center gap-1 rounded-full bg-success/15 px-2.5 py-0.5 text-xs font-medium text-success">
                        <CircleCheck className="h-3 w-3" />
                        {test.attemptCount === 1 ? "Taken once" : `Taken ${test.attemptCount}×`}
                      </span>
                    ) : (
                      <span className="rounded-full bg-secondary px-2.5 py-0.5 text-xs text-muted-foreground">
                        Not started
                      </span>
                    )}
                  </div>
                  <p className="mt-1 max-w-2xl text-sm leading-relaxed text-muted-foreground">
                    {test.blurb}
                  </p>

                  <div className="mt-3 flex flex-wrap items-center gap-x-5 gap-y-1.5 text-sm text-muted-foreground">
                    <span className="flex items-center gap-1.5">
                      <ListChecks className="h-4 w-4" />
                      {test.questionCount} questions
                    </span>
                    <span className="flex items-center gap-1.5">
                      <Clock className="h-4 w-4" />
                      {formatDuration(test.minutes)}
                    </span>
                    <span className="flex items-center gap-1.5">
                      <Calculator className="h-4 w-4" />
                      {test.sections.length === 1
                        ? (CALCULATOR_LABEL[test.sections[0].calculator as ApCalculatorPolicy] ??
                          test.sections[0].calculator)
                        : "Calculator varies by part"}
                    </span>
                  </div>

                  {test.sections.length > 1 && (
                    <ul className="mt-3 space-y-1 border-l-2 border-border/70 pl-3 text-sm text-muted-foreground">
                      {test.sections.map((s) => (
                        <li key={s.id}>
                          <span className="font-medium text-foreground">{s.short}</span> —{" "}
                          {s.questionCount} questions, {s.timeLimitMinutes} min,{" "}
                          {(
                            CALCULATOR_LABEL[s.calculator as ApCalculatorPolicy] ?? s.calculator
                          ).toLowerCase()}
                        </li>
                      ))}
                    </ul>
                  )}

                  {test.referenceNote && (
                    <p className="mt-3 flex items-start gap-1.5 text-xs text-muted-foreground">
                      <FileText className="mt-0.5 h-3.5 w-3.5 shrink-0" />
                      {test.referenceNote} {test.calculatorNote}
                    </p>
                  )}
                </div>

                <div className="flex w-full flex-col items-start gap-3 sm:w-auto sm:items-end">
                  {(test.bestScore || test.lastScore) && (
                    <div className="flex gap-5 text-right">
                      {test.bestScore && (
                        <div>
                          <p className="text-xs uppercase tracking-wide text-muted-foreground">
                            Best
                          </p>
                          <p className="text-xl font-semibold tabular-nums">
                            {test.bestScore.percent}%
                          </p>
                          <p className="text-xs tabular-nums text-muted-foreground">
                            {test.bestScore.score}/{test.bestScore.total}
                          </p>
                        </div>
                      )}
                      {test.lastScore && (
                        <div>
                          <p className="text-xs uppercase tracking-wide text-muted-foreground">
                            Last
                          </p>
                          <p className="text-xl font-semibold tabular-nums">
                            {test.lastScore.percent}%
                          </p>
                          <p className="text-xs tabular-nums text-muted-foreground">
                            {test.lastScore.score}/{test.lastScore.total}
                          </p>
                        </div>
                      )}
                    </div>
                  )}

                  <div className="flex flex-wrap items-center gap-2">
                    {test.lastAttemptId && (
                      <Link
                        href={`/ap/tests/result/${test.lastAttemptId}`}
                        className="inline-flex items-center gap-1.5 rounded-lg border border-border px-3 py-2 text-sm font-medium transition-colors hover:border-primary/50 hover:text-primary"
                      >
                        <Timer className="h-3.5 w-3.5" /> Last result
                      </Link>
                    )}
                    <StartTestButton
                      subject={subject.code}
                      testSlug={test.slug}
                      resume={Boolean(test.inProgressAttemptId)}
                      label={
                        test.inProgressAttemptId
                          ? "Resume test"
                          : test.attemptCount > 0
                            ? "Retake test"
                            : "Start test"
                      }
                    />
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {subject.notReadyCount > 0 && (
        <p className="text-sm text-muted-foreground">
          {subject.notReadyCount} further{" "}
          {subject.notReadyCount === 1 ? "test is" : "tests are"} configured for {subject.short} and
          will appear here once enough questions are written for {" "}
          {subject.notReadyCount === 1 ? "it" : "them"}.
        </p>
      )}
    </div>
  );
}
