"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Trash2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { deleteTest } from "@/server/actions/admin/tests";

export function DeleteTestButton({ testId, title }: { testId: string; title: string }) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  function remove() {
    if (
      !confirm(
        `Delete "${title}" entirely, including every module, question, and any student attempts on it? This can't be undone.`
      )
    )
      return;
    startTransition(async () => {
      const result = await deleteTest(testId);
      if (result.error) {
        toast.error(result.error);
        return;
      }
      toast.success(`"${title}" was deleted.`);
      router.refresh();
    });
  }

  return (
    <Button variant="ghost" size="icon" onClick={remove} disabled={isPending} title="Delete test">
      {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Trash2 className="h-4 w-4 text-destructive" />}
    </Button>
  );
}
