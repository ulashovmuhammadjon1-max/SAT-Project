import Link from "next/link";
import {
  ArrowRight,
  CalendarDays,
  ClipboardList,
  Compass,
  GraduationCap,
  Sparkles,
} from "lucide-react";

import { AP_EXAM_START, daysUntilExams } from "@/lib/ap/courses";
import { getApProgress, type ApSubjectProgress } from "@/server/actions/student/ap";
import { getCatalog } from "@/server/actions/student/ap-subjects";
import { SubjectCatalog } from "@/components/ap/subject-catalog";
import { requireUser } from "@/lib/session";

export const metadata = { title: "AP Prep" };
export const dynamic = "force-dynamic";

const pct = (a: number, b: number) => (b === 0 ? 0 : Math.round((a / b) * 100));

/**
 * The AP hub: the exam-season countdown, the subjects this student has
 * actually added, a way into the practice tests, and the full catalog.
 *
 * The catalog is handed to the client whole so search and filtering never
 * touch the network. Everything above it is server-rendered, because it is
 * personal data that should be right on first paint.
 */
export default async function ApHubPage() {
  const user = await requireUser();
  const [catalog, progress] = await Promise.all([getCatalog(), getApProgress()]);

  // Keyed by the plain code: the catalog is wider than the outlines in
  // courses.ts, so a subject may legitimately have no progress row yet.
  const byCode = new Map<string, ApSubjectProgress>(progress.map((p) => [p.subject, p]));
  const mine = catalog.filter((s) => s.added);
  const firstName = user.name?.trim().split(/\s+/)[0] ?? "there";
  const days = daysUntilExams();

  return (
    <div className="space-y-8">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div>
          <p className="text-xs font-semibold uppercase tracking-[0.14em] text-primary">
            <GraduationCap aria-hidden className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
            AP Prep
          </p>
          <h1 className="mt-1 font-display text-3xl font-semibold tracking-tight">
            Good to see you, {firstName}
          </h1>
          <p className="mt-1.5 max-w-xl text-sm text-muted-foreground">
            Build your own AP list — practice by unit and topic, with explanations on every
            question, and sit full practice tests when you are ready.
          </p>
        </div>

        <div className="rounded-2xl border border-border/70 bg-card px-5 py-4 shadow-soft">
          <p className="flex items-center gap-1.5 text-xs font-medium text-muted-foreground">
            <CalendarDays aria-hidden className="h-3.5 w-3.5" /> AP exam season
          </p>
          <p className="mt-1 font-display text-xl font-semibold tracking-tight">
            {AP_EXAM_START.getUTCFullYear()} exams start May {AP_EXAM_START.getUTCDate()}
          </p>
          <p className="mt-0.5 text-sm text-muted-foreground">
            {AP_EXAM_START.toLocaleDateString("en-US", {
              weekday: "long",
              month: "long",
              day: "numeric",
              year: "numeric",
              timeZone: "UTC",
            })}{" "}
            · {days} days away
          </p>
        </div>
      </div>

      <section aria-labelledby="ap-mine-heading">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <h2 id="ap-mine-heading" className="font-display text-lg font-semibold tracking-tight">
            Your subjects
          </h2>
          {mine.length > 0 && (
            <a
              href="#ap-explore-heading"
              className="inline-flex items-center gap-1.5 rounded-lg px-2 py-1 text-sm font-medium text-primary transition-colors hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
            >
              <Compass aria-hidden className="h-3.5 w-3.5" /> Add another subject
            </a>
          )}
        </div>

        {mine.length === 0 ? (
          <div className="mt-3 rounded-2xl border border-dashed border-border bg-card/60 px-6 py-10 text-center shadow-soft">
            <span className="mx-auto flex h-11 w-11 items-center justify-center rounded-2xl bg-primary/10 text-primary">
              <Compass aria-hidden className="h-5 w-5" />
            </span>
            <p className="mt-3 font-display text-base font-semibold tracking-tight">
              You haven&apos;t added any AP subjects yet
            </p>
            <p className="mx-auto mt-1 max-w-sm text-sm text-muted-foreground">
              Pick the courses you are sitting this year. They show up here and in your sidebar,
              and you can change the list whenever you like.
            </p>
            <a
              href="#ap-explore-heading"
              className="mt-4 inline-flex items-center gap-1.5 rounded-lg bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground shadow-soft transition-colors hover:bg-primary-600 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
            >
              Browse AP subjects <ArrowRight aria-hidden className="h-4 w-4" />
            </a>
          </div>
        ) : (
          <div className="mt-3 grid gap-5 sm:grid-cols-2">
            {mine.map((subject) => {
              const p = byCode.get(subject.code);
              const total = p?.total ?? subject.questionCount;
              const answered = p?.answered ?? 0;
              return (
                <Link
                  key={subject.code}
                  href={`/ap/${subject.slug}`}
                  className={`group relative overflow-hidden rounded-2xl bg-gradient-to-br ${subject.gradient} p-6 text-white shadow-soft transition-all hover:-translate-y-0.5 hover:shadow-lg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2`}
                >
                  <Sparkles
                    aria-hidden
                    className="absolute right-4 top-4 h-5 w-5 opacity-40 transition-opacity group-hover:opacity-70"
                  />
                  <p className="font-display text-2xl font-semibold tracking-tight">
                    {subject.name}
                  </p>
                  <p className="mt-1 max-w-sm text-sm text-white/85">{subject.blurb}</p>

                  {total > 0 && (
                    <div className="mt-5">
                      <span className="block h-1.5 w-full overflow-hidden rounded-full bg-white/25">
                        <span
                          className="block h-full rounded-full bg-white"
                          style={{ width: `${pct(answered, total)}%` }}
                        />
                      </span>
                    </div>
                  )}

                  <div className="mt-4 flex items-end justify-between gap-3">
                    <span className="text-sm text-white/85">
                      {total > 0 ? (
                        <>
                          {answered.toLocaleString()}/{total.toLocaleString()} answered
                          {answered > 0 && <> · {pct(p?.correct ?? 0, answered)}% correct</>}
                        </>
                      ) : (
                        <>Questions coming soon</>
                      )}
                    </span>
                    <span className="inline-flex items-center gap-1.5 rounded-full bg-white px-4 py-2 text-sm font-semibold text-navy-900 transition-transform group-hover:translate-x-0.5">
                      Open <ArrowRight aria-hidden className="h-4 w-4" />
                    </span>
                  </div>
                </Link>
              );
            })}
          </div>
        )}
      </section>

      {/* A deliberately compact entry point: full tests are a separate mode, not
          a fifth card competing with the subjects above. */}
      <Link
        href="/ap/tests"
        className="group flex flex-wrap items-center gap-4 rounded-2xl border border-border/70 bg-card p-5 shadow-soft transition-all hover:-translate-y-0.5 hover:shadow-lg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
      >
        <span className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-primary/10 text-primary">
          <ClipboardList aria-hidden className="h-5 w-5" />
        </span>
        <span className="min-w-0 flex-1">
          <span className="block font-display text-base font-semibold tracking-tight">
            Practice tests
          </span>
          <span className="mt-0.5 block text-sm text-muted-foreground">
            Full timed papers under real exam conditions, scored the way the College Board scores
            them.
          </span>
        </span>
        <span className="inline-flex items-center gap-1.5 rounded-lg border border-border px-3 py-2 text-sm font-semibold transition-colors group-hover:border-primary/50 group-hover:text-primary">
          Take a test <ArrowRight aria-hidden className="h-4 w-4" />
        </span>
      </Link>

      <SubjectCatalog subjects={catalog} />
    </div>
  );
}
