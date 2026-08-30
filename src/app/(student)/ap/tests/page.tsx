import Link from "next/link";
import { ArrowRight, ClipboardList, Plus, Timer } from "lucide-react";

import { listTestsForMySubjects } from "@/server/actions/student/ap-tests";
import { requireUser } from "@/lib/session";

export const metadata = { title: "AP Practice Tests" };
export const dynamic = "force-dynamic";

/**
 * Step one of taking a practice test: choose a subject.
 *
 * Only the student's own subjects appear. The catalog is heading for thirty
 * entries, and a picker that listed all of them would be a wall of courses the
 * student is not taking — adding a subject is a deliberate act on /ap, and this
 * page respects it.
 */
export default async function ApTestsPage() {
  await requireUser();
  const subjects = await listTestsForMySubjects();
  const withTests = subjects.filter((s) => s.tests.length > 0);

  return (
    <div className="space-y-8">
      <div>
        <Link href="/ap" className="text-sm text-muted-foreground hover:text-foreground">
          AP Prep
        </Link>
        <h1 className="mt-2 font-display text-3xl font-semibold tracking-tight">
          AP Practice Tests
        </h1>
        <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
          Full timed sittings in the shape of the real exam — the same countdown, question palette
          and mark-for-review you get on a Scholarly SAT test. Everything you answer counts towards
          your topic progress.
        </p>
      </div>

      {subjects.length === 0 ? (
        <EmptyState
          title="You haven't added any AP subjects yet"
          body="Practice tests are built from your own subjects. Add the courses you are taking and their tests appear here."
          href="/ap"
          cta="Browse AP subjects"
        />
      ) : withTests.length === 0 ? (
        <EmptyState
          title="No test is ready for your subjects yet"
          body="Your subjects are on the platform, but their question banks are not deep enough for a full practice form yet. Topic practice is available in the meantime, and tests appear here on their own once the banks fill."
          href="/ap"
          cta="Practise by topic"
        />
      ) : (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {withTests.map((subject) => {
            const openSitting = subject.tests.find((t) => t.inProgressAttemptId);
            const taken = subject.tests.reduce((n, t) => n + t.attemptCount, 0);
            return (
              <Link
                key={subject.code}
                href={`/ap/tests/${subject.slug}`}
                className="group flex flex-col overflow-hidden rounded-2xl border border-border/70 bg-card shadow-soft transition-shadow hover:shadow-md"
              >
                <div className={`bg-gradient-to-br ${subject.gradient} px-5 py-4 text-white`}>
                  <p className="font-display text-lg font-semibold leading-snug">{subject.name}</p>
                  <p className="mt-0.5 text-xs text-white/85">
                    {subject.tests.length} {subject.tests.length === 1 ? "test" : "tests"} ready
                    {subject.notReadyCount > 0 && <> · {subject.notReadyCount} in preparation</>}
                  </p>
                </div>
                <div className="flex flex-1 flex-col gap-2 px-5 py-4">
                  <p className="flex items-center gap-1.5 text-sm text-muted-foreground">
                    <ClipboardList className="h-4 w-4" />
                    {subject.questionCount.toLocaleString()} questions in the bank
                  </p>
                  <p className="flex items-center gap-1.5 text-sm text-muted-foreground">
                    <Timer className="h-4 w-4" />
                    {taken === 0 ? "No sittings yet" : `${taken} completed`}
                    {openSitting && <span className="text-warning"> · one in progress</span>}
                  </p>
                  <span className="mt-auto inline-flex items-center gap-1.5 pt-2 text-sm font-medium text-primary">
                    See tests
                    <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                  </span>
                </div>
              </Link>
            );
          })}
        </div>
      )}

      {subjects.length > 0 && (
        <Link
          href="/ap"
          className="inline-flex items-center gap-1.5 text-sm font-medium text-primary hover:underline"
        >
          <Plus className="h-4 w-4" /> Add another subject
        </Link>
      )}
    </div>
  );
}

function EmptyState({
  title,
  body,
  href,
  cta,
}: {
  title: string;
  body: string;
  href: string;
  cta: string;
}) {
  return (
    <div className="rounded-2xl border border-dashed border-border bg-card px-6 py-12 text-center shadow-soft">
      <ClipboardList className="mx-auto h-8 w-8 text-muted-foreground" />
      <p className="mt-3 font-medium">{title}</p>
      <p className="mx-auto mt-1 max-w-md text-sm text-muted-foreground">{body}</p>
      <Link
        href={href}
        className="mt-5 inline-flex items-center gap-1.5 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-primary/90"
      >
        {cta}
        <ArrowRight className="h-4 w-4" />
      </Link>
    </div>
  );
}
