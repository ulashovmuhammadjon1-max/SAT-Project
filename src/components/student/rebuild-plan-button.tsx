"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { RefreshCw } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { rebuildPlan } from "@/server/actions/student/wallet";

/**
 * Force a plan regeneration.
 *
 * The plan already rebuilds itself whenever the evidence count moves, so this
 * is for the case where the student changed their target score or test date and
 * wants to see it reflected now rather than on the next answer.
 */
export function RebuildPlanButton() {
  const [pending, startTransition] = useTransition();
  const router = useRouter();

  return (
    <Button
      variant="outline"
      size="sm"
      disabled={pending}
      onClick={() =>
        startTransition(async () => {
          try {
            await rebuildPlan();
            router.refresh();
            toast.success("Plan rebuilt from your latest results");
          } catch {
            toast.error("Couldn't rebuild your plan. Please try again.");
          }
        })
      }
    >
      <RefreshCw className={`mr-2 h-3.5 w-3.5 ${pending ? "animate-spin" : ""}`} />
      {pending ? "Rebuilding…" : "Rebuild plan"}
    </Button>
  );
}
