"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { BookOpenCheck, CheckCircle2, Loader2, Trash2, XCircle } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { deleteTest, publishAllQuestionsInTest, setTestStatus } from "@/server/actions/admin/tests";

export function TestActions({ testId, status }: { testId: string; status: string }) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();
  const [isDeleting, startDelete] = useTransition();
  const [isPublishingQuestions, startPublishQuestions] = useTransition();

  function publishQuestions() {
    startPublishQuestions(async () => {
      const { count } = await publishAllQuestionsInTest(testId);
      toast.success(
        count > 0 ? `${count} question${count === 1 ? "" : "s"} added to the question bank.` : "Already up to date — nothing to publish."
      );
      router.refresh();
    });
  }

  function change(next: "PUBLISHED" | "DRAFT" | "ARCHIVED") {
    startTransition(async () => {
      await setTestStatus(testId, next);
      router.refresh();
    });
  }

  function remove() {
    if (
      !confirm(
        "Delete this test entirely, including every module, question, and any student attempts on it? This can't be undone."
      )
    )
      return;
    startDelete(async () => {
      const result = await deleteTest(testId);
      if (result.error) {
        toast.error(result.error);
        return;
      }
      toast.success("Test deleted.");
      router.push("/admin/tests");
    });
  }

  return (
    <div className="flex gap-2">
      {status !== "PUBLISHED" ? (
        <Button onClick={() => change("PUBLISHED")} disabled={isPending}>
          {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <CheckCircle2 className="h-4 w-4" />}
          Publish
        </Button>
      ) : (
        <Button variant="outline" onClick={() => change("ARCHIVED")} disabled={isPending}>
          {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <XCircle className="h-4 w-4" />}
          Archive
        </Button>
      )}
      <Button
        variant="outline"
        onClick={publishQuestions}
        disabled={isPublishingQuestions}
        title="Make every question in this test individually practiceable in the student Question Bank"
      >
        {isPublishingQuestions ? <Loader2 className="h-4 w-4 animate-spin" /> : <BookOpenCheck className="h-4 w-4" />}
        Add to question bank
      </Button>
      <Button variant="outline" className="text-destructive" onClick={remove} disabled={isDeleting}>
        {isDeleting ? <Loader2 className="h-4 w-4 animate-spin" /> : <Trash2 className="h-4 w-4" />}
        Delete
      </Button>
    </div>
  );
}
