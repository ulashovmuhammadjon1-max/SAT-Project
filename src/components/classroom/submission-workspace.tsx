"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { CheckCircle2, FileText, Loader2, Save, Send, Undo2 } from "lucide-react";
import { toast } from "sonner";

import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import {
  FileUploader,
  type ExistingFile,
  type NewFile,
} from "@/components/classroom/file-uploader";
import { formatBytes, type SubmissionStatus } from "@/lib/classroom/status";
import { saveWork, unsubmitWork } from "@/server/actions/student/classroom";

/**
 * The "Your work" panel on a free-form assignment.
 *
 * Two faces. While working: the drop zone, the note, Save draft and Submit —
 * nothing is lost by navigating away, because Save draft persists files
 * without handing anything in. Once handed in: a clear submitted state with
 * the files and time, and Unsubmit to pull it back for edits.
 */
export function SubmissionWorkspace({
  assignmentId,
  status,
  submittedAt,
  initialNote,
  initialFiles,
}: {
  assignmentId: string;
  status: SubmissionStatus;
  submittedAt: Date | null;
  initialNote: string | null;
  initialFiles: ExistingFile[];
}) {
  const router = useRouter();
  const [pending, start] = useTransition();
  const [note, setNote] = useState(initialNote ?? "");
  const [kept, setKept] = useState<ExistingFile[]>(initialFiles);
  const [added, setAdded] = useState<NewFile[]>([]);

  const submitted = status === "SUBMITTED" || status === "LATE";
  const totalFiles = kept.length + added.length;
  const dirty =
    added.length > 0 ||
    kept.length !== initialFiles.length ||
    note !== (initialNote ?? "");

  function persist(submit: boolean) {
    start(async () => {
      const res = await saveWork({
        assignmentId,
        note,
        keepFileIds: kept.map((f) => f.id),
        newFiles: added.map((f) => ({ name: f.name, dataUrl: f.dataUrl })),
        submit,
      });
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success(submit ? "Assignment submitted." : "Draft saved — nothing is handed in yet.");
      setAdded([]);
      router.refresh();
    });
  }

  function unsubmit() {
    start(async () => {
      const res = await unsubmitWork(assignmentId);
      if (res.error) toast.error(res.error);
      else {
        toast.success("Pulled back to a draft — edit and resubmit when ready.");
        router.refresh();
      }
    });
  }

  if (submitted) {
    return (
      <div className="space-y-4">
        <div className="flex items-start gap-3 rounded-2xl bg-success/10 p-4">
          <CheckCircle2 className="mt-0.5 h-5 w-5 shrink-0 text-success" />
          <div>
            <p className="font-medium text-success">
              {status === "LATE" ? "Submitted late" : "Assignment submitted"}
            </p>
            {submittedAt && (
              <p className="mt-0.5 text-sm text-muted-foreground">
                Submitted{" "}
                {submittedAt.toLocaleDateString(undefined, { month: "short", day: "numeric" })} at{" "}
                {submittedAt.toLocaleTimeString(undefined, { hour: "numeric", minute: "2-digit" })}
              </p>
            )}
          </div>
        </div>

        {initialFiles.length > 0 && (
          <div>
            <p className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">
              Your submission
            </p>
            <ul className="mt-2 space-y-2">
              {initialFiles.map((f) => (
                <li key={f.id}>
                  <a
                    href={`/api/submission-file/${f.id}`}
                    target="_blank"
                    rel="noreferrer"
                    className="flex items-center gap-3 rounded-xl border border-border bg-card px-3 py-2.5 transition-colors hover:border-primary/50"
                  >
                    <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-success/10 text-success">
                      <FileText className="h-4 w-4" />
                    </span>
                    <span className="min-w-0 flex-1">
                      <span className="block truncate text-sm font-medium">{f.name}</span>
                      <span className="text-xs text-muted-foreground">{formatBytes(f.size)}</span>
                    </span>
                  </a>
                </li>
              ))}
            </ul>
          </div>
        )}

        {initialNote && (
          <div>
            <p className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">
              Your note
            </p>
            <p className="mt-1.5 rounded-xl bg-secondary/50 px-3 py-2.5 text-sm leading-relaxed">
              {initialNote}
            </p>
          </div>
        )}

        <AlertDialog>
          <AlertDialogTrigger asChild>
            <Button variant="outline" size="sm" className="gap-2" disabled={pending}>
              <Undo2 className="h-4 w-4" /> Unsubmit and edit
            </Button>
          </AlertDialogTrigger>
          <AlertDialogContent>
            <AlertDialogHeader>
              <AlertDialogTitle>Unsubmit this assignment?</AlertDialogTitle>
              <AlertDialogDescription>
                It goes back to a draft your teacher sees as not handed in — submit again once you
                have made your changes.
              </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
              <AlertDialogCancel>Cancel</AlertDialogCancel>
              <AlertDialogAction onClick={unsubmit}>Unsubmit</AlertDialogAction>
            </AlertDialogFooter>
          </AlertDialogContent>
        </AlertDialog>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <FileUploader
        existing={kept}
        added={added}
        onAdd={(files) => setAdded((prev) => [...prev, ...files])}
        onRemoveExisting={(id) => setKept((prev) => prev.filter((f) => f.id !== id))}
        onRemoveAdded={(i) => setAdded((prev) => prev.filter((_, idx) => idx !== i))}
        disabled={pending}
      />

      <div>
        <label className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">
          Note to your teacher (optional)
        </label>
        <Textarea
          value={note}
          onChange={(e) => setNote(e.target.value)}
          rows={2}
          placeholder="Add a message…"
          className="mt-1.5"
        />
      </div>

      {status === "DRAFT" && !dirty && (
        <p className="text-xs text-muted-foreground">
          Draft saved — your files are safe here until you submit.
        </p>
      )}

      <div className="flex flex-wrap items-center gap-2">
        <AlertDialog>
          <AlertDialogTrigger asChild>
            <Button className="gap-2" disabled={pending || totalFiles + note.trim().length === 0}>
              {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Send className="h-4 w-4" />}
              Submit assignment
            </Button>
          </AlertDialogTrigger>
          <AlertDialogContent>
            <AlertDialogHeader>
              <AlertDialogTitle>Submit this assignment?</AlertDialogTitle>
              <AlertDialogDescription asChild>
                <div className="space-y-2 text-sm text-muted-foreground">
                  <p>Your teacher receives:</p>
                  <ul className="list-inside space-y-1">
                    {kept.map((f) => (
                      <li key={f.id} className="flex items-center gap-1.5">
                        <CheckCircle2 className="h-3.5 w-3.5 text-success" /> {f.name}
                      </li>
                    ))}
                    {added.map((f, i) => (
                      <li key={i} className="flex items-center gap-1.5">
                        <CheckCircle2 className="h-3.5 w-3.5 text-success" /> {f.name}
                      </li>
                    ))}
                    {totalFiles === 0 && <li>Just your note — no files attached.</li>}
                  </ul>
                  <p>You can unsubmit later if you need to make changes.</p>
                </div>
              </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
              <AlertDialogCancel>Cancel</AlertDialogCancel>
              <AlertDialogAction onClick={() => persist(true)}>Submit</AlertDialogAction>
            </AlertDialogFooter>
          </AlertDialogContent>
        </AlertDialog>

        <Button
          variant="outline"
          className="gap-2"
          disabled={pending || !dirty}
          onClick={() => persist(false)}
        >
          <Save className="h-4 w-4" /> Save draft
        </Button>
      </div>
    </div>
  );
}
