"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Trash2 } from "lucide-react";

import { Button } from "@/components/ui/button";
import { deleteModule } from "@/server/actions/admin/tests";

export function DeleteModuleButton({ moduleId }: { moduleId: string }) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  function remove() {
    if (!confirm("Delete this module and all of its questions? This can't be undone.")) return;
    startTransition(async () => {
      await deleteModule(moduleId);
      router.refresh();
    });
  }

  return (
    <Button variant="ghost" size="icon" onClick={remove} disabled={isPending} title="Delete this module">
      {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Trash2 className="h-4 w-4 text-destructive" />}
    </Button>
  );
}
