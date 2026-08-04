"use client";

import { Flag } from "lucide-react";

import { Sheet, SheetContent, SheetHeader, SheetTitle } from "@/components/ui/sheet";
import { cn } from "@/lib/utils";
import type { QuestionState } from "@/types/exam";

export function QuestionPalette({
  open,
  onOpenChange,
  count,
  currentIndex,
  states,
  onJump,
}: {
  open: boolean;
  onOpenChange: (v: boolean) => void;
  count: number;
  currentIndex: number;
  states: QuestionState[];
  onJump: (index: number) => void;
}) {
  return (
    <Sheet open={open} onOpenChange={onOpenChange}>
      <SheetContent side="bottom" className="max-h-[70vh] overflow-y-auto rounded-t-2xl bg-examCream">
        <SheetHeader>
          <SheetTitle className="text-navy-950">Question navigator</SheetTitle>
        </SheetHeader>
        <div className="mt-4 grid grid-cols-6 gap-2 sm:grid-cols-10">
          {Array.from({ length: count }).map((_, i) => {
            const state = states[i];
            const answered = !!(state?.selectedChoiceId || state?.freeResponseAnswer);
            // A question with recorded time (or an answer) has been visited;
            // there's no separate persisted flag, this is a reliable proxy.
            const visited = answered || (state?.timeSpentSeconds ?? 0) > 0;
            return (
              <button
                key={i}
                onClick={() => {
                  onJump(i);
                  onOpenChange(false);
                }}
                className={cn(
                  "relative flex h-11 w-11 items-center justify-center rounded border text-sm font-semibold transition-colors",
                  answered
                    ? "border-navy-950 bg-navy-950 text-white"
                    : visited
                      ? "border-navy-300 bg-navy-100 text-navy-950"
                      : "border-navy-300 bg-white text-navy-950",
                  i === currentIndex && "ring-2 ring-navy-500 ring-offset-1 ring-offset-examCream"
                )}
              >
                {i + 1}
                {state?.flagged && (
                  <Flag className="absolute -right-1.5 -top-1.5 h-3.5 w-3.5 fill-warning text-warning" />
                )}
              </button>
            );
          })}
        </div>
        <div className="mt-4 flex flex-wrap gap-4 text-xs text-navy-700">
          <span className="flex items-center gap-1.5">
            <span className="h-3 w-3 rounded-sm border border-navy-950 bg-navy-950" /> Answered
          </span>
          <span className="flex items-center gap-1.5">
            <span className="h-3 w-3 rounded-sm border border-navy-300 bg-navy-100" /> Visited
          </span>
          <span className="flex items-center gap-1.5">
            <span className="h-3 w-3 rounded-sm border border-navy-300 bg-white" /> Not visited
          </span>
          <span className="flex items-center gap-1.5">
            <Flag className="h-3.5 w-3.5 fill-warning text-warning" /> Flagged for review
          </span>
        </div>
      </SheetContent>
    </Sheet>
  );
}
