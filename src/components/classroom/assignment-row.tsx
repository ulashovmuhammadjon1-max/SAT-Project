import Link from "next/link";
import { BookOpen, ChevronRight, FileText, ListChecks, Paperclip } from "lucide-react";

import { StatusBadge } from "@/components/classroom/status-badge";
import { formatDue } from "@/lib/classroom/status";
import type { StudentAssignment } from "@/server/actions/student/classroom";
import { cn } from "@/lib/utils";

/**
 * One assignment in a list — a row, not a card: the class page reads as a
 * list of work, and every row is one click from its workspace.
 */

const KIND_ICON = { TASK: FileText, TEST: BookOpen, QUESTIONS: ListChecks } as const;

export function AssignmentRow({
  assignment: a,
  showClass = false,
}: {
  assignment: StudentAssignment;
  showClass?: boolean;
}) {
  const Icon = KIND_ICON[a.kind];
  const overdue = a.status === "MISSING";

  const detail =
    a.kind === "TEST"
      ? a.testTitle
      : a.kind === "QUESTIONS"
        ? `${a.questionsAnswered}/${a.questionCount} questions`
        : null;

  return (
    <Link
      href={`/classes/${a.classId}/assignments/${a.id}`}
      className="group flex items-center gap-4 rounded-xl px-3 py-3.5 transition-colors hover:bg-secondary/60 sm:px-4"
    >
      <span
        className={cn(
          "flex h-10 w-10 shrink-0 items-center justify-center rounded-xl",
          overdue ? "bg-destructive/10 text-destructive" : "bg-primary/10 text-primary",
        )}
      >
        <Icon className="h-4.5 w-4.5 h-[18px] w-[18px]" />
      </span>

      <span className="min-w-0 flex-1">
        <span className="block truncate font-medium leading-snug group-hover:text-primary">
          {a.title}
        </span>
        <span className="mt-0.5 block truncate text-xs text-muted-foreground">
          {showClass && <>{a.className} · </>}
          {a.dueAt ? formatDue(a.dueAt) : "No due date"}
          {detail && <> · {detail}</>}
          {a.attachmentName && (
            <>
              {" "}
              · <Paperclip className="inline h-3 w-3 align-[-1.5px]" /> 1 file
            </>
          )}
        </span>
      </span>

      <StatusBadge status={a.status} className="hidden sm:inline-flex" />
      <ChevronRight className="h-4 w-4 shrink-0 text-muted-foreground/60 transition-transform group-hover:translate-x-0.5" />
    </Link>
  );
}
