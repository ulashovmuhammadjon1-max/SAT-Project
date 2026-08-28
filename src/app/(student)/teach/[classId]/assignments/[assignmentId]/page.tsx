import Link from "next/link";
import { notFound } from "next/navigation";
import { Download, Paperclip } from "lucide-react";

import { StatusBadge } from "@/components/classroom/status-badge";
import { DeleteAssignmentButton } from "@/components/teacher/assignment-form";
import { QuestionList } from "@/components/teacher/question-list";
import { formatBytes, formatDue } from "@/lib/classroom/status";
import { getAssignmentTracking } from "@/server/actions/teacher/classes";
import { getAssignmentQuestions } from "@/server/actions/teacher/question-sets";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Assignment" };
export const dynamic = "force-dynamic";

/**
 * One assignment, every student: who submitted, who is missing, what they
 * handed in. The counts at the top are the register; the rows below are the
 * marking pile — each uploaded file opens in a tab.
 */
export default async function TeachAssignmentPage({
  params,
}: {
  params: { classId: string; assignmentId: string };
}) {
  await requireUser();
  const tracking = await getAssignmentTracking(params.assignmentId);
  if (!tracking || tracking.assignment.classId !== params.classId) notFound();
  const { assignment: a, students } = tracking;

  // The exact questions in a Question Bank set — a teacher re-reading what
  // they assigned should never have to re-run the picker to see them.
  const questions =
    a.kind === "QUESTIONS" ? await getAssignmentQuestions(params.assignmentId) : [];

  const count = (statuses: string[]) => students.filter((s) => statuses.includes(s.status)).length;
  const stats = [
    { label: "Submitted", value: count(["SUBMITTED", "LATE"]), className: "text-success" },
    { label: "In progress", value: count(["IN_PROGRESS", "DRAFT"]), className: "text-primary" },
    { label: "Missing", value: count(["MISSING"]), className: "text-destructive" },
    { label: "Not started", value: count(["NOT_STARTED"]), className: "text-muted-foreground" },
  ];

  return (
    <div className="space-y-6">
      <nav className="flex flex-wrap items-center gap-1.5 text-sm text-muted-foreground">
        <Link href={`/teach/${params.classId}`} className="font-medium hover:text-foreground">
          {tracking.className}
        </Link>
        <span>/</span>
        <Link href={`/teach/${params.classId}`} className="hover:text-foreground">
          Assignments
        </Link>
        <span>/</span>
        <span className="truncate text-foreground">{a.title}</span>
      </nav>

      <div className="flex flex-wrap items-start justify-between gap-3">
        <div className="min-w-0">
          <h1 className="font-display text-3xl font-semibold tracking-tight">{a.title}</h1>
          <p className="mt-1.5 text-sm text-muted-foreground">
            {a.kind === "TEST" && <>{a.testTitle} · </>}
            {a.kind === "QUESTIONS" && <>{a.questionCount} Question Bank questions · </>}
            {a.dueAt ? formatDue(a.dueAt) : "No due date"} · {students.length} student
            {students.length === 1 ? "" : "s"} assigned
          </p>
          {a.instructions && (
            <p className="mt-2 max-w-2xl whitespace-pre-line text-sm leading-relaxed text-muted-foreground">
              {a.instructions}
            </p>
          )}
          {a.attachmentHref && (
            <a
              href={a.attachmentHref}
              target="_blank"
              rel="noreferrer"
              className="mt-2 inline-flex items-center gap-1.5 text-sm font-medium text-primary underline-offset-4 hover:underline"
            >
              <Paperclip className="h-3.5 w-3.5" /> {a.attachmentName}
            </a>
          )}
        </div>
        <DeleteAssignmentButton assignmentId={a.id} redirectTo={`/teach/${params.classId}`} />
      </div>

      <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
        {stats.map((s) => (
          <div key={s.label} className="rounded-2xl border border-border/70 bg-card px-4 py-3.5 shadow-soft">
            <p className={`text-2xl font-semibold tabular-nums ${s.className}`}>{s.value}</p>
            <p className="text-xs text-muted-foreground">{s.label}</p>
          </div>
        ))}
      </div>

      <div className="rounded-2xl border border-border/70 bg-card shadow-soft">
        <div className="divide-y divide-border/60">
          {students.map((s) => (
            <div key={s.userId} className="flex flex-wrap items-start gap-3 px-4 py-3.5 sm:px-5">
              <div className="min-w-[200px] flex-1">
                <Link
                  href={`/teach/student/${s.userId}`}
                  className="font-medium text-primary underline-offset-4 hover:underline"
                >
                  {s.name ?? s.email}
                </Link>
                <p className="mt-0.5 text-xs text-muted-foreground">
                  {a.kind === "QUESTIONS" && (
                    <>
                      {s.answered}/{a.questionCount} answered
                      {s.score != null && <> · {s.score}% correct</>}
                    </>
                  )}
                  {a.kind === "TEST" && s.score != null && <>Score {s.score}</>}
                  {a.kind === "TASK" && s.submittedAt && (
                    <>
                      Submitted{" "}
                      {s.submittedAt.toLocaleDateString(undefined, {
                        month: "short",
                        day: "numeric",
                      })}{" "}
                      at{" "}
                      {s.submittedAt.toLocaleTimeString(undefined, {
                        hour: "numeric",
                        minute: "2-digit",
                      })}
                    </>
                  )}
                </p>
                {s.note && (
                  <p className="mt-1.5 rounded-lg bg-secondary/60 px-3 py-2 text-sm leading-relaxed">
                    {s.note}
                  </p>
                )}
                {s.files.length > 0 && (
                  <div className="mt-1.5 flex flex-wrap gap-2">
                    {s.files.map((f) => (
                      <a
                        key={f.id}
                        href={`/api/submission-file/${f.id}`}
                        target="_blank"
                        rel="noreferrer"
                        className="inline-flex items-center gap-1.5 rounded-lg border border-border px-2.5 py-1.5 text-xs font-medium transition-colors hover:border-primary/50 hover:text-primary"
                      >
                        <Download className="h-3 w-3" />
                        {f.name}
                        <span className="text-muted-foreground">{formatBytes(f.size)}</span>
                      </a>
                    ))}
                  </div>
                )}
              </div>
              <StatusBadge status={s.status} />
            </div>
          ))}
          {students.length === 0 && (
            <p className="px-5 py-10 text-center text-sm text-muted-foreground">
              Nobody has joined this class yet.
            </p>
          )}
        </div>
      </div>

      {questions.length > 0 && (
        <section>
          <h2 className="font-display text-lg font-semibold tracking-tight">
            The questions in this set
          </h2>
          <p className="mt-0.5 text-sm text-muted-foreground">
            Exactly what your students see, with the answers marked.
          </p>
          <div className="mt-3 rounded-2xl border border-border/70 bg-card shadow-soft">
            <QuestionList questions={questions} />
          </div>
        </section>
      )}
    </div>
  );
}
