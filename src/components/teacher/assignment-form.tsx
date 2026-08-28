"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { ClipboardPlus, FileText, ListChecks, Loader2, Trash2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { FileDrop, type PickedFile } from "@/components/shared/file-drop";
import { QuestionPicker } from "@/components/teacher/question-picker";
import { createAssignment, deleteAssignment } from "@/server/actions/teacher/assignments";
import type { PreviewQuestion } from "@/server/actions/teacher/question-sets";

const NO_TEST = "none";

/** What the assignment is built around. A task carries at most one of them. */
type Kind = "TASK" | "TEST" | "QUESTIONS";

const KINDS: { value: Kind; label: string; icon: typeof FileText; hint: string }[] = [
  {
    value: "TASK",
    label: "Task",
    icon: FileText,
    hint: "Anything you set yourself — attach a worksheet and students hand their work back.",
  },
  {
    value: "TEST",
    label: "Practice test",
    icon: ClipboardPlus,
    hint: "Completes itself when the student submits, and you see the score.",
  },
  {
    value: "QUESTIONS",
    label: "Question Bank set",
    icon: ListChecks,
    hint: "Pick the exact questions. Marks itself done when every one is answered.",
  },
];

export function AssignmentForm({
  classId,
  tests,
}: {
  classId: string;
  tests: { id: string; title: string }[];
}) {
  const router = useRouter();
  const [pending, start] = useTransition();
  const [kind, setKind] = useState<Kind>("TASK");
  const [title, setTitle] = useState("");
  const [instructions, setInstructions] = useState("");
  const [testId, setTestId] = useState<string>(NO_TEST);
  const [dueAt, setDueAt] = useState("");
  const [attachment, setAttachment] = useState<PickedFile | null>(null);
  const [questions, setQuestions] = useState<PreviewQuestion[]>([]);

  function reset() {
    setTitle("");
    setInstructions("");
    setTestId(NO_TEST);
    setDueAt("");
    setAttachment(null);
    setQuestions([]);
    setKind("TASK");
  }

  function submit() {
    if (kind === "TEST" && testId === NO_TEST) {
      toast.error("Choose which practice test to assign.");
      return;
    }
    if (kind === "QUESTIONS" && questions.length === 0) {
      toast.error("Preview a set of questions first — you should read them before assigning them.");
      return;
    }
    start(async () => {
      const res = await createAssignment({
        classId,
        title,
        instructions,
        testId: kind === "TEST" ? testId : "",
        dueAt: dueAt || null,
        attachment,
        questionIds: kind === "QUESTIONS" ? questions.map((q) => q.id) : [],
      });
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success(
        res.notified
          ? `Posted — ${res.notified} student${res.notified === 1 ? "" : "s"} emailed.`
          : "Assignment posted.",
      );
      reset();
      router.refresh();
    });
  }

  const active = KINDS.find((k) => k.value === kind)!;

  return (
    <div className="space-y-4 rounded-xl border border-dashed border-border p-4">
      {/* What kind of assignment */}
      <div className="flex flex-wrap gap-2">
        {KINDS.map((k) => {
          const Icon = k.icon;
          const on = kind === k.value;
          return (
            <button
              key={k.value}
              type="button"
              onClick={() => setKind(k.value)}
              className={`inline-flex items-center gap-1.5 rounded-full border px-3 py-1.5 text-sm font-medium transition-colors ${
                on
                  ? "border-primary bg-primary text-primary-foreground"
                  : "border-border text-muted-foreground hover:border-primary/50"
              }`}
            >
              <Icon className="h-3.5 w-3.5" />
              {k.label}
            </button>
          );
        })}
      </div>
      <p className="-mt-2 text-[11px] text-muted-foreground">{active.hint}</p>

      <div className="grid gap-3 sm:grid-cols-[1fr_220px]">
        <div className="space-y-1">
          <Label>Title</Label>
          <Input
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Finish Test 12 by Friday"
          />
        </div>
        <div className="space-y-1">
          <Label>Due (optional)</Label>
          <Input type="datetime-local" value={dueAt} onChange={(e) => setDueAt(e.target.value)} />
        </div>
      </div>

      {kind === "TEST" && (
        <div className="space-y-1">
          <Label>Which practice test</Label>
          <Select value={testId} onValueChange={setTestId}>
            <SelectTrigger><SelectValue placeholder="Choose a test" /></SelectTrigger>
            <SelectContent>
              <SelectItem value={NO_TEST}>Choose a test…</SelectItem>
              {tests.map((t) => (
                <SelectItem key={t.id} value={t.id}>{t.title}</SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>
      )}

      {kind === "QUESTIONS" && <QuestionPicker onChange={setQuestions} />}

      <div className="grid gap-3 sm:grid-cols-2">
        <div className="space-y-1">
          <Label>Instructions (optional)</Label>
          <Textarea
            value={instructions}
            onChange={(e) => setInstructions(e.target.value)}
            rows={2}
            placeholder="Anything the class should know."
          />
        </div>
        <div className="space-y-1">
          <Label>Attach a file (optional)</Label>
          <FileDrop
            value={attachment}
            onChange={setAttachment}
            label="Upload a worksheet"
            hint="PDF, PNG, JPG or WEBP — up to 4MB. Your class can open it from their assignment list."
          />
        </div>
      </div>

      <div className="flex flex-wrap items-center gap-3">
        <Button onClick={submit} disabled={pending || title.trim().length < 3} className="gap-2">
          {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <ClipboardPlus className="h-4 w-4" />}
          Post assignment
        </Button>
        <p className="text-xs text-muted-foreground">
          Everyone in the class is emailed when you post.
        </p>
      </div>
    </div>
  );
}

export function DeleteAssignmentButton({ assignmentId }: { assignmentId: string }) {
  const router = useRouter();
  const [pending, start] = useTransition();
  return (
    <Button
      size="sm"
      variant="ghost"
      className="text-destructive hover:text-destructive"
      disabled={pending}
      onClick={() => {
        if (!confirm("Delete this assignment for the whole class?")) return;
        start(async () => {
          const res = await deleteAssignment(assignmentId);
          if (res.error) toast.error(res.error);
          else {
            toast.success("Assignment removed.");
            router.refresh();
          }
        });
      }}
    >
      <Trash2 className="h-4 w-4" />
    </Button>
  );
}
