"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { CheckCircle2, Loader2, Trash2, XCircle } from "lucide-react";

import { Button } from "@/components/ui/button";
import { deleteTest, setTestStatus } from "@/server/actions/admin/tests";

export function TestActions({ testId, status }: { testId: string; status: string }) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();
  const [isDeleting, startDelete] = useTransition();

  function change(next: "PUBLISHED" | "DRAFT" | "ARCHIVED") {
    startTransition(async () => {
      await setTestStatus(testId, next);
      router.refresh();
    });
  }

  function remove() {
    if (!confirm("Delete this test entirely, including every module and question in it? This can't be undone.")) return;
    startDelete(async () => {
      await deleteTest(testId);
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
      <Button variant="outline" className="text-destructive" onClick={remove} disabled={isDeleting}>
        {isDeleting ? <Loader2 className="h-4 w-4 animate-spin" /> : <Trash2 className="h-4 w-4" />}
        Delete
      </Button>
    </div>
  );
}
