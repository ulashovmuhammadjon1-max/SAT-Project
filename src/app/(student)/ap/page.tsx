import Link from "next/link";
import { ArrowRight, CalendarDays, GraduationCap, Sparkles } from "lucide-react";

import { AP_COURSES, AP_EXAM_START, daysUntilExams } from "@/lib/ap/courses";
import { getApProgress } from "@/server/actions/student/ap";
import { requireUser } from "@/lib/session";

export const metadata = { title: "AP Prep" };
export const dynamic = "force-dynamic";

/**
 * The AP hub: one card per course, the exam-season countdown, and a progress
 * line wherever a course already has live questions.
 */
export default async function ApHubPage() {
  const user = await requireUser();
  const progress = await getApProgress();
  const byCode = new Map(progress.map((p) => [p.subject, p]));
  const firstName = user.name?.trim().split(/\s+/)[0] ?? "there";
  const days = daysUntilExams();

  return (
    <div className="space-y-8">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div>
          <p className="text-xs font-semibold uppercase tracking-[0.14em] text-primary">
            <GraduationCap className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
            AP Prep
          </p>
          <h1 className="mt-1 font-display text-3xl font-semibold tracking-tight">
            Good to see you, {firstName}
          </h1>
          <p className="mt-1.5 max-w-xl text-sm text-muted-foreground">
            Four courses to start — practice by unit and topic, with explanations on every
            question.
          </p>
        </div>

        <div className="rounded-2xl border border-border/70 bg-card px-5 py-4 shadow-soft">
          <p className="flex items-center gap-1.5 text-xs font-medium text-muted-foreground">
            <CalendarDays className="h-3.5 w-3.5" /> AP exam season
          </p>
          <p className="mt-1 font-display text-xl font-semibold tracking-tight">
            {AP_EXAM_START.getUTCFullYear()} exams start May {AP_EXAM_START.getUTCDate()}
          </p>
          <p className="mt-0.5 text-sm text-muted-foreground">
            {AP_EXAM_START.toLocaleDateString(undefined, {
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

      <section>
        <h2 className="font-display text-lg font-semibold tracking-tight">Your subjects</h2>
        <div className="mt-3 grid gap-5 sm:grid-cols-2">
          {AP_COURSES.map((course) => {
            const p = byCode.get(course.code);
            const hasContent = (p?.total ?? 0) > 0;
            return (
              <Link
                key={course.code}
                href={`/ap/${course.slug}`}
                className={`group relative overflow-hidden rounded-2xl bg-gradient-to-br ${course.gradient} p-6 text-white shadow-soft transition-all hover:-translate-y-0.5 hover:shadow-lg`}
              >
                <Sparkles className="absolute right-4 top-4 h-5 w-5 opacity-40 transition-opacity group-hover:opacity-70" />
                <p className="font-display text-2xl font-semibold tracking-tight">
                  {course.name}
                </p>
                <p className="mt-1 max-w-sm text-sm text-white/85">{course.blurb}</p>
                <div className="mt-6 flex items-end justify-between gap-3">
                  <span className="text-sm text-white/85">
                    {hasContent ? (
                      <>
                        {p!.total.toLocaleString()} questions
                        {p!.answered > 0 && <> · {p!.answered} answered</>}
                      </>
                    ) : (
                      <>{course.units.length} units · questions coming soon</>
                    )}
                  </span>
                  <span className="inline-flex items-center gap-1.5 rounded-full bg-white px-4 py-2 text-sm font-semibold text-navy-900 transition-transform group-hover:translate-x-0.5">
                    Open <ArrowRight className="h-4 w-4" />
                  </span>
                </div>
              </Link>
            );
          })}
        </div>
      </section>
    </div>
  );
}
