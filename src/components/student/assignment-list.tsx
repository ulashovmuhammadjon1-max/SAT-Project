"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { CheckCircle2, Circle, ListChecks, Loader2, Paperclip, Upload } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { FileDrop, type PickedFile } from "@/components/shared/file-drop";
import type { MyAssignment } from "@/server/actions/student/school-class";
import { markAssignmentDone } from "@/server/actions/teacher/assignments";

/**
 * A student's assignment list.
 *
 * Only a free-form task has a button to press. A practice test or a question
 * set completes itself from real answers — offering a "mark done" there would
 * let a student report work they had not done, and the teacher's tick column
 * would stop meaning one thing.
 */
export function AssignmentList({ assignments }: { assignments: MyAssignment[] }) {
  return (
    <ul className="divide-y divide-border">
      {assignments.map((a) => (
        <AssignmentRow key={a.id} assignment={a} />
      ))}
    </ul>
  );
}

function AssignmentRow({ assignment: a }: { assignment: MyAssignment }) {
  const router = useRouter();
  const [pending, start] = useTransition();
  const [open, setOpen] = useState(false);
  const [note, setNote] = useState(a.submittedNote ?? "");
  const [file, setFile] = useState<PickedFile | null>(null);

  const isSet = a.questionCount > 0;
  const isFreeForm = !a.testId && !isSet;

  function submit() {
    start(async () => {
      const res = await markAssignmentDone({ assignmentId: a.id, note, file });
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success("Handed in — your teacher can see it.");
      setOpen(false);
      setFile(null);
      router.refresh();
    });
  }

  return (
    <li className="py-3">
      <div className="flex flex-wrap items-start gap-3">
        {a.done ? (
          <CheckCircle2 className="mt-0.5 h-5 w-5 shrink-0 text-success" />
        ) : (
          <Circle className="mt-0.5 h-5 w-5 shrink-0 text-muted-foreground" />
        )}

        <div className="min-w-[200px] flex-1">
          <p className={a.done ? "text-sm font-medium text-muted-foreground line-through" : "text-sm font-medium"}>
            {a.title}
          </p>
          <p className="text-xs text-muted-foreground">
            {a.className}
            {a.dueAt &&
              ` · due ${a.dueAt.toLocaleDateString(undefined, { month: "short", day: "numeric" })}`}
            {isSet && ` · ${a.questionsAnswered}/${a.questionCount} answered`}
          </p>

          {a.instructions && !a.done && (
            <p className="mt-0.5 text-xs leading-relaxed text-muted-foreground">{a.instructions}</p>
          )}

          {a.attachmentName && (
            <a
              href={`/api/assignments/${a.id}/attachment`}
              target="_blank"
              rel="noreferrer"
              className="mt-1 inline-flex items-center gap-1 text-xs font-medium text-primary underline-offset-4 hover:underline"
            >
              <Paperclip className="h-3 w-3" />
              {a.attachmentName}
            </a>
          )}

          {a.submissionHref && (
            <p className="mt-1 text-xs text-muted-foreground">
              You handed in{" "}
              <a
                href={a.submissionHref}
                target="_blank"
                rel="noreferrer"
                className="font-medium text-primary underline-offset-4 hover:underline"
              >
                {a.submittedFileName}
              </a>
            </p>
          )}
        </div>

        {/* One action, decided by what kind of assignment this is. */}
        {isSet ? (
          !a.done &&
          a.practiceHref && (
            <Button size="sm" variant="outline" asChild>
              <Link href={a.practiceHref} className="gap-1.5">
                <ListChecks className="h-3.5 w-3.5" />
                {a.questionsAnswered > 0 ? "Keep going" : "Start the questions"}
              </Link>
            </Button>
          )
        ) : a.testId ? (
          !a.done && (
            <Button size="sm" variant="outline" asChild>
              <Link href="/tests">Take {a.testTitle ?? "the test"}</Link>
            </Button>
          )
        ) : (
          <Button size="sm" variant={a.done ? "ghost" : "outline"} onClick={() => setOpen(!open)}>
            {a.done ? "Update" : "Hand in"}
          </Button>
        )}
      </div>

      {isFreeForm && open && (
        <div className="mt-3 space-y-3 rounded-xl border border-dashed border-border p-3">
          <Textarea
            value={note}
            onChange={(e) => setNote(e.target.value)}
            rows={2}
            placeholder="Anything you want your teacher to know (optional)."
          />
          <FileDrop
            value={file}
            onChange={setFile}
            label="Upload your work"
            hint="A PDF or a screenshot of what you did — up to 4MB. Optional."
          />
          <div className="flex gap-2">
            <Button size="sm" className="gap-2" disabled={pending} onClick={submit}>
              {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Upload className="h-4 w-4" />}
              {a.done ? "Update what I handed in" : "Mark done"}
            </Button>
            <Button size="sm" variant="ghost" onClick={() => setOpen(false)}>
              Cancel
            </Button>
          </div>
        </div>
      )}
    </li>
  );
}
