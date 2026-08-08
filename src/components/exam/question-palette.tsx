"use client";

import { useEffect } from "react";
import { Bookmark, MapPin, X } from "lucide-react";

import { cn } from "@/lib/utils";
import type { QuestionState } from "@/types/exam";

/** Per-question outcome, once an answer has been graded. Practice tests never
 *  grade mid-module, so this stays null there; the Question Bank sets it. */
export type QuestionOutcome = "correct" | "incorrect" | null;

/** Legend shown above the grid, in the Question Menu and the Review Page. */
export function QuestionLegend({ showOutcomes = false }: { showOutcomes?: boolean }) {
  return (
    <div className="flex flex-wrap items-center justify-center gap-x-6 gap-y-1.5 text-[12px] text-exam-muted">
      <span className="flex items-center gap-1.5">
        <MapPin className="h-3.5 w-3.5 fill-exam-blue text-exam-blue" /> Current
      </span>
      <span className="flex items-center gap-1.5">
        <span className="h-3.5 w-3.5 rounded-[2px] border border-dashed border-exam-disabled" /> Unanswered
      </span>
      <span className="flex items-center gap-1.5">
        <Bookmark className="h-3.5 w-3.5 fill-exam-flag text-exam-flag" /> For Review
      </span>
      {showOutcomes && (
        <>
          <span className="flex items-center gap-1.5">
            <span className="h-3.5 w-3.5 rounded-[2px] bg-exam-correct" /> Correct
          </span>
          <span className="flex items-center gap-1.5">
            <span className="h-3.5 w-3.5 rounded-[2px] bg-exam-incorrect" /> Incorrect
          </span>
        </>
      )}
    </div>
  );
}

/**
 * The numbered question grid. Unanswered is the state the legend calls out
 * (dashed outline); answered questions read as filled.
 */
export function QuestionGrid({
  count,
  currentIndex,
  states,
  onJump,
  outcomes,
}: {
  count: number;
  currentIndex: number;
  states: QuestionState[];
  onJump: (index: number) => void;
  /** Graded results, when the surface grades as it goes (Question Bank). */
  outcomes?: QuestionOutcome[];
}) {
  return (
    <div className="grid grid-cols-[repeat(auto-fill,minmax(38px,1fr))] gap-x-2 gap-y-3">
      {Array.from({ length: count }).map((_, i) => {
        const state = states[i];
        const answered = !!(state?.selectedChoiceId || state?.freeResponseAnswer);
        const current = i === currentIndex;
        const outcome = outcomes?.[i] ?? null;
        return (
          <div key={i} className="relative flex justify-center pt-3">
            {current && (
              <MapPin className="absolute left-1/2 top-0 h-3.5 w-3.5 -translate-x-1/2 fill-exam-blue text-exam-blue" />
            )}
            <button
              type="button"
              onClick={() => onJump(i)}
              aria-current={current ? "true" : undefined}
              // Spell the whole state out: the visual cues (fill, dashed
              // outline, pin, bookmark) mean nothing to a screen reader.
              aria-label={[
                `Question ${i + 1}`,
                outcome ?? (answered ? "answered" : "unanswered"),
                state?.flagged ? "marked for review" : null,
                current ? "current" : null,
              ]
                .filter(Boolean)
                .join(", ")}
              className={cn(
                "relative flex h-[38px] w-[38px] items-center justify-center rounded-[3px] text-[13px] font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-exam-blue focus-visible:ring-offset-1",
                outcome === "correct" && "bg-exam-correct text-white hover:opacity-90",
                outcome === "incorrect" && "bg-exam-incorrect text-white hover:opacity-90",
                !outcome && answered && "bg-exam-blue text-white hover:bg-exam-blueHover",
                !outcome &&
                  !answered &&
                  "border border-dashed border-exam-disabled bg-white text-exam-text hover:bg-exam-hover",
                // The pin alone is easy to miss in a grid of 27 — ring the
                // current cell as well so it reads at a glance.
                current && "ring-2 ring-exam-strip ring-offset-2"
              )}
            >
              {i + 1}
              {state?.flagged && (
                <Bookmark className="absolute -right-1 -top-1.5 h-3.5 w-3.5 fill-exam-flag text-exam-flag" />
              )}
            </button>
          </div>
        );
      })}
    </div>
  );
}

/**
 * Bluebook's "Question Menu" — a popup anchored above the bottom navigation
 * bar rather than a slide-up sheet. Its parent must be positioned.
 */
export function QuestionPalette({
  open,
  onOpenChange,
  title,
  count,
  currentIndex,
  states,
  onJump,
  onGoToReview,
  outcomes,
  reviewLabel = "Go to Review Page",
}: {
  open: boolean;
  onOpenChange: (v: boolean) => void;
  title: string;
  count: number;
  currentIndex: number;
  states: QuestionState[];
  onJump: (index: number) => void;
  /** Omitted by surfaces with no end-of-module review page. */
  onGoToReview?: () => void;
  outcomes?: QuestionOutcome[];
  reviewLabel?: string;
}) {
  useEffect(() => {
    if (!open) return;
    function onKeyDown(e: KeyboardEvent) {
      if (e.key === "Escape") onOpenChange(false);
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [open, onOpenChange]);

  if (!open) return null;

  return (
    <>
      <div className="fixed inset-0 z-40" onMouseDown={() => onOpenChange(false)} />
      <div
        role="dialog"
        aria-label="Question Menu"
        className="absolute bottom-full left-1/2 z-50 mb-2 w-[min(620px,calc(100vw-1.5rem))] -translate-x-1/2 rounded-md border border-exam-border bg-white shadow-examPopup"
      >
        <div className="relative px-5 pb-3 pt-4">
          <p className="text-center text-[13px] font-semibold text-exam-text">{title}</p>
          <button
            type="button"
            onClick={() => onOpenChange(false)}
            aria-label="Close Question Menu"
            className="absolute right-3 top-3 flex h-6 w-6 items-center justify-center rounded text-exam-muted hover:bg-exam-hover hover:text-exam-text focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-exam-blue"
          >
            <X className="h-4 w-4" />
          </button>
          <div className="mt-2.5">
            <QuestionLegend showOutcomes={!!outcomes} />
          </div>
        </div>

        <div className="max-h-[46vh] overflow-y-auto exam-scroll border-t border-exam-divider px-5 py-4">
          <QuestionGrid
            count={count}
            currentIndex={currentIndex}
            states={states}
            outcomes={outcomes}
            onJump={(i) => {
              onJump(i);
              onOpenChange(false);
            }}
          />
        </div>

        {onGoToReview && (
        <div className="flex justify-center border-t border-exam-divider px-5 py-3">
          <button
            type="button"
            onClick={() => {
              onOpenChange(false);
              onGoToReview();
            }}
            className="rounded-full border border-exam-blue px-5 py-1.5 text-[13px] font-medium text-exam-blue transition-colors hover:bg-exam-hover focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-exam-blue focus-visible:ring-offset-1"
          >
            {reviewLabel}
          </button>
        </div>
        )}
      </div>
    </>
  );
}
