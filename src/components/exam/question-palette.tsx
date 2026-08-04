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
      <SheetContent side="bottom" className="max-h-[70vh] overflow-y-auto rounded-t-lg bg-exam-bg">
        <SheetHeader>
          <SheetTitle className="text-exam-text">Question navigator</SheetTitle>
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
                  "relative flex h-10 w-10 items-center justify-center rounded border text-sm font-semibold transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-exam-blue focus-visible:ring-offset-2 focus-visible:ring-offset-exam-bg",
                  answered
                    ? "border-exam-blue bg-exam-blue text-white"
                    : visited
                      ? "border-exam-border bg-gray-100 text-exam-text"
                      : "border-exam-border bg-exam-card text-exam-text",
                  i === currentIndex && "ring-2 ring-exam-blue ring-offset-1 ring-offset-exam-bg"
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
        <div className="mt-4 flex flex-wrap gap-4 text-xs text-exam-muted">
          <span className="flex items-center gap-1.5">
            <span className="h-3 w-3 rounded-sm border border-exam-blue bg-exam-blue" /> Answered
          </span>
          <span className="flex items-center gap-1.5">
            <span className="h-3 w-3 rounded-sm border border-exam-border bg-gray-100" /> Visited
          </span>
          <span className="flex items-center gap-1.5">
            <span className="h-3 w-3 rounded-sm border border-exam-border bg-exam-card" /> Not visited
          </span>
          <span className="flex items-center gap-1.5">
            <Flag className="h-3.5 w-3.5 fill-warning text-warning" /> Flagged for review
          </span>
        </div>
      </SheetContent>
    </Sheet>
  );
}
