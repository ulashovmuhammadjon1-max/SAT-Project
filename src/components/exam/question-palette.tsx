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
      <SheetContent side="bottom" className="max-h-[70vh] overflow-y-auto rounded-t-2xl">
        <SheetHeader>
          <SheetTitle>Question navigator</SheetTitle>
        </SheetHeader>
        <div className="mt-4 grid grid-cols-6 gap-2 sm:grid-cols-10">
          {Array.from({ length: count }).map((_, i) => {
            const state = states[i];
            const answered = !!(state?.selectedChoiceId || state?.freeResponseAnswer);
            return (
              <button
                key={i}
                onClick={() => {
                  onJump(i);
                  onOpenChange(false);
                }}
                className={cn(
                  "relative flex h-11 w-11 items-center justify-center rounded-lg border text-sm font-semibold transition-colors",
                  i === currentIndex
                    ? "border-primary bg-primary text-primary-foreground"
                    : answered
                      ? "border-success/40 bg-success/10 text-success"
                      : "border-border bg-secondary text-muted-foreground"
                )}
              >
                {i + 1}
                {state?.flagged && (
                  <Flag className="absolute -right-1 -top-1 h-3.5 w-3.5 fill-warning text-warning" />
                )}
              </button>
            );
          })}
        </div>
        <div className="mt-4 flex flex-wrap gap-4 text-xs text-muted-foreground">
          <span className="flex items-center gap-1.5">
            <span className="h-3 w-3 rounded-sm bg-success/20" /> Answered
          </span>
          <span className="flex items-center gap-1.5">
            <span className="h-3 w-3 rounded-sm bg-secondary" /> Unanswered
          </span>
          <span className="flex items-center gap-1.5">
            <Flag className="h-3.5 w-3.5 fill-warning text-warning" /> Flagged for review
          </span>
        </div>
      </SheetContent>
    </Sheet>
  );
}
