"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { CheckCircle2, Loader2, XCircle } from "lucide-react";

import { Button } from "@/components/ui/button";
import { setTestStatus } from "@/server/actions/admin/tests";

export function TestActions({ testId, status }: { testId: string; status: string }) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  function change(next: "PUBLISHED" | "DRAFT" | "ARCHIVED") {
    startTransition(async () => {
      await setTestStatus(testId, next);
      router.refresh();
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
    </div>
  );
}
