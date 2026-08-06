"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { ChevronDown, ChevronUp, Loader2 } from "lucide-react";
import { toast } from "sonner";

import { swapQuestionOrder } from "@/server/actions/admin/questions";

export function QuestionOrderButtons({
  questionId,
  isFirst,
  isLast,
}: {
  questionId: string;
  isFirst: boolean;
  isLast: boolean;
}) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  function move(direction: "up" | "down") {
    startTransition(async () => {
      const result = await swapQuestionOrder(questionId, direction);
      if (result.error) {
        toast.error(result.error);
        return;
      }
      router.refresh();
    });
  }

  return (
    <span className="flex shrink-0 flex-col">
      <button
        type="button"
        onClick={(e) => {
          e.preventDefault();
          e.stopPropagation();
          move("up");
        }}
        disabled={isFirst || isPending}
        title="Move up"
        className="rounded p-0.5 text-muted-foreground hover:bg-accent hover:text-foreground disabled:pointer-events-none disabled:opacity-30"
      >
        {isPending ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : <ChevronUp className="h-3.5 w-3.5" />}
      </button>
      <button
        type="button"
        onClick={(e) => {
          e.preventDefault();
          e.stopPropagation();
          move("down");
        }}
        disabled={isLast || isPending}
        title="Move down"
        className="rounded p-0.5 text-muted-foreground hover:bg-accent hover:text-foreground disabled:pointer-events-none disabled:opacity-30"
      >
        <ChevronDown className="h-3.5 w-3.5" />
      </button>
    </span>
  );
}
