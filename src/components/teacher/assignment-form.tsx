"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { ClipboardPlus, Loader2, Trash2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { createAssignment, deleteAssignment } from "@/server/actions/teacher/assignments";

const NO_TEST = "none";

export function AssignmentForm({
  classId,
  tests,
}: {
  classId: string;
  tests: { id: string; title: string }[];
}) {
  const router = useRouter();
  const [pending, start] = useTransition();
  const [title, setTitle] = useState("");
  const [instructions, setInstructions] = useState("");
  const [testId, setTestId] = useState<string>(NO_TEST);
  const [dueAt, setDueAt] = useState("");

  function submit() {
    start(async () => {
      const res = await createAssignment({
        classId,
        title,
        instructions,
        testId: testId === NO_TEST ? "" : testId,
        dueAt: dueAt || null,
      });
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success("Assignment posted — your class sees it now.");
      setTitle(""); setInstructions(""); setTestId(NO_TEST); setDueAt("");
      router.refresh();
    });
  }

  return (
    <div className="space-y-3 rounded-xl border border-dashed border-border p-4">
      <div className="grid gap-3 sm:grid-cols-2">
        <div className="space-y-1">
          <Label>Task</Label>
          <Input
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Finish Test 12 by Friday"
          />
        </div>
        <div className="space-y-1">
          <Label>Link a practice test (optional)</Label>
          <Select value={testId} onValueChange={setTestId}>
            <SelectTrigger>
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value={NO_TEST}>No test — free-form task</SelectItem>
              {tests.map((t) => (
                <SelectItem key={t.id} value={t.id}>{t.title}</SelectItem>
              ))}
            </SelectContent>
          </Select>
          <p className="text-[11px] text-muted-foreground">
            Linked tests mark themselves complete when a student submits — with their score.
          </p>
        </div>
      </div>
      <div className="grid gap-3 sm:grid-cols-[1fr_220px]">
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
          <Label>Due (optional)</Label>
          <Input type="datetime-local" value={dueAt} onChange={(e) => setDueAt(e.target.value)} />
        </div>
      </div>
      <Button onClick={submit} disabled={pending || title.trim().length < 3} className="gap-2">
        {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <ClipboardPlus className="h-4 w-4" />}
        Post assignment
      </Button>
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
