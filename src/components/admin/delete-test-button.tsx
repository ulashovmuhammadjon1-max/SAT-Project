"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Trash2 } from "lucide-react";

import { Button } from "@/components/ui/button";
import { deleteTest } from "@/server/actions/admin/tests";

export function DeleteTestButton({ testId, title }: { testId: string; title: string }) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  function remove() {
    if (!confirm(`Delete "${title}" entirely, including every module and question in it? This can't be undone.`)) return;
    startTransition(async () => {
      await deleteTest(testId);
      router.refresh();
    });
  }

  return (
    <Button variant="ghost" size="icon" onClick={remove} disabled={isPending} title="Delete test">
      {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Trash2 className="h-4 w-4 text-destructive" />}
    </Button>
  );
}
