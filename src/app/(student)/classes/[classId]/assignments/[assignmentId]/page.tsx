import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowRight, BookOpen, FileText, ListChecks, Paperclip } from "lucide-react";

import { Button } from "@/components/ui/button";
import { StatusBadge } from "@/components/classroom/status-badge";
import { SubmissionWorkspace } from "@/components/classroom/submission-workspace";
import { formatDue, isDone } from "@/lib/classroom/status";
import { getAssignmentWorkspace } from "@/server/actions/student/classroom";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Assignment" };
export const dynamic = "force-dynamic";

/**
 * The assignment workspace. Instructions and teacher materials on the left,
 * the student's own work on the right — side by side on a desktop, stacked on
 * a phone. The class context is in the breadcrumb, the sidebar and the URL;
 * the submission can only ever land on this assignment in this class.
 */
export default async function AssignmentPage({
  params,
}: {
  params: { classId: string; assignmentId: string };
}) {
  await requireUser();
  const a = await getAssignmentWorkspace(params.assignmentId);
  // The assignment decides its class — a URL claiming another class is wrong.
  if (!a || a.classId !== params.classId) notFound();

  return (
    <div className="space-y-6">
      <nav className="flex flex-wrap items-center gap-1.5 text-sm text-muted-foreground">
        <Link href={`/classes/${a.classId}`} className="font-medium hover:text-foreground">
          {a.className}
        </Link>
        <span>/</span>
        <Link href={`/classes/${a.classId}`} className="hover:text-foreground">
          Assignments
        </Link>
        <span>/</span>
        <span className="truncate text-foreground">{a.title}</span>
      </nav>

      <div className="flex flex-wrap items-start justify-between gap-3">
        <div className="min-w-0">
          <h1 className="font-display text-3xl font-semibold tracking-tight">{a.title}</h1>
          <p className="mt-1.5 text-sm text-muted-foreground">
            {a.teacherName}
            {a.dueAt && <> · {formatDue(a.dueAt)}</>}
          </p>
        </div>
        <StatusBadge status={a.status} className="mt-1.5" />
      </div>

      <div className="grid gap-8 lg:grid-cols-[minmax(0,1fr)_minmax(360px,440px)]">
        {/* What the teacher set */}
        <div className="min-w-0 space-y-7">
          {a.instructions && (
            <section>
              <h2 className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">
                Instructions
              </h2>
              <p className="mt-2 whitespace-pre-line text-[15px] leading-relaxed">
                {a.instructions}
              </p>
            </section>
          )}

          {a.attachmentHref && (
            <section>
              <h2 className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">
                Teacher materials
              </h2>
              <a
                href={a.attachmentHref}
                target="_blank"
                rel="noreferrer"
                className="mt-2 flex items-center gap-3 rounded-xl border border-border bg-card px-4 py-3 shadow-soft transition-colors hover:border-primary/50"
              >
                <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-lg bg-navy-900/5 text-navy-900 dark:bg-secondary dark:text-foreground">
                  <Paperclip className="h-4 w-4" />
                </span>
                <span className="min-w-0 flex-1">
                  <span className="block truncate text-sm font-medium">{a.attachmentName}</span>
                  <span className="text-xs text-muted-foreground">Open in a new tab</span>
                </span>
                <ArrowRight className="h-4 w-4 shrink-0 text-muted-foreground" />
              </a>
            </section>
          )}

          {a.kind === "TEST" && (
            <section className="rounded-2xl border border-border bg-card p-5 shadow-soft">
              <div className="flex items-start gap-3">
                <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-primary/10 text-primary">
                  <BookOpen className="h-5 w-5" />
                </span>
                <div className="min-w-0 flex-1">
                  <p className="font-medium">{a.testTitle}</p>
                  <p className="mt-0.5 text-sm text-muted-foreground">
                    This assignment completes itself the moment you submit the test — your teacher
                    sees your score, and there is nothing to upload.
                  </p>
                  {!isDone(a.status) && (
                    <Button asChild className="mt-3 gap-2">
                      <Link href="/tests">
                        Take the test <ArrowRight className="h-4 w-4" />
                      </Link>
                    </Button>
                  )}
                </div>
              </div>
            </section>
          )}

          {a.kind === "QUESTIONS" && (
            <section className="rounded-2xl border border-border bg-card p-5 shadow-soft">
              <div className="flex items-start gap-3">
                <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-primary/10 text-primary">
                  <ListChecks className="h-5 w-5" />
                </span>
                <div className="min-w-0 flex-1">
                  <p className="font-medium">
                    {a.questionCount} question{a.questionCount === 1 ? "" : "s"} picked by your
                    teacher
                  </p>
                  <div className="mt-2.5 h-2 overflow-hidden rounded-full bg-secondary">
                    <div
                      className="h-full rounded-full bg-primary transition-all"
                      style={{
                        width: `${a.questionCount ? Math.round((a.questionsAnswered / a.questionCount) * 100) : 0}%`,
                      }}
                    />
                  </div>
                  <p className="mt-1.5 text-sm text-muted-foreground">
                    {a.questionsAnswered}/{a.questionCount} answered — it marks itself done when
                    every question is answered.
                  </p>
                  {!isDone(a.status) && a.practiceHref && (
                    <Button asChild className="mt-3 gap-2">
                      <Link href={a.practiceHref}>
                        {a.questionsAnswered > 0 ? "Keep going" : "Start the questions"}
                        <ArrowRight className="h-4 w-4" />
                      </Link>
                    </Button>
                  )}
                </div>
              </div>
            </section>
          )}

          {!a.instructions && !a.attachmentHref && a.kind === "TASK" && (
            <p className="text-sm text-muted-foreground">
              No written instructions — hand your work in on the right.
            </p>
          )}
        </div>

        {/* The student's own work */}
        {a.kind === "TASK" ? (
          <aside className="lg:sticky lg:top-6 lg:self-start">
            <div className="rounded-2xl border border-border bg-card p-5 shadow-soft">
              <h2 className="flex items-center gap-2 font-display text-lg font-semibold tracking-tight">
                <FileText className="h-4.5 w-4.5 h-[18px] w-[18px] text-primary" /> Your work
              </h2>
              <div className="mt-4">
                <SubmissionWorkspace
                  assignmentId={a.id}
                  status={a.status}
                  submittedAt={a.submittedAt}
                  initialNote={a.note}
                  initialFiles={a.files}
                />
              </div>
            </div>
          </aside>
        ) : (
          <aside className="lg:sticky lg:top-6 lg:self-start">
            <div className="rounded-2xl border border-border bg-card p-5 shadow-soft">
              <h2 className="font-display text-lg font-semibold tracking-tight">Status</h2>
              <div className="mt-3">
                <StatusBadge status={a.status} />
              </div>
              <p className="mt-3 text-sm leading-relaxed text-muted-foreground">
                {a.kind === "TEST"
                  ? "Submitting the linked practice test is the hand-in — no upload needed here."
                  : "Answering every assigned question is the hand-in — no upload needed here."}
              </p>
            </div>
          </aside>
        )}
      </div>
    </div>
  );
}
