"use client";

import { Check, X } from "lucide-react";

import { MathContent } from "@/components/shared/math-content";
import { FOCUS_RING } from "@/components/testing/primitives";
import { cn } from "@/lib/utils";

export interface TestingChoice {
  id: string;
  label: string;
  content: string;
}

/**
 * The answer list, shared by practice tests and Question Bank practice.
 *
 * Two modes live in one component so the two surfaces cannot drift apart:
 *  - answering: select, and optionally cross out with the ABC eliminator
 *  - reviewing: the key and the student's pick are marked, and nothing is
 *    clickable
 *
 * Every state is carried by shape as well as colour — border weight, the filled
 * letter badge, a check or cross glyph, and a text label for screen readers —
 * so none of it depends on telling green from red.
 */
export function AnswerChoiceList({
  choices,
  selectedId,
  eliminatedIds = [],
  crossOutEnabled = false,
  correctId = null,
  revealed = false,
  onSelect,
  onToggleEliminate,
}: {
  choices: TestingChoice[];
  selectedId: string | null;
  eliminatedIds?: string[];
  crossOutEnabled?: boolean;
  /** Only ever set once an answer has been submitted. */
  correctId?: string | null;
  /** Locks the list and shows the outcome. */
  revealed?: boolean;
  onSelect?: (choiceId: string) => void;
  onToggleEliminate?: (choiceId: string) => void;
}) {
  return (
    <div className="space-y-3" role="radiogroup" aria-label="Answer choices">
      {choices.map((choice) => {
        const selected = selectedId === choice.id;
        const eliminated = eliminatedIds.includes(choice.id);
        const isKey = revealed && correctId === choice.id;
        const isWrongPick = revealed && selected && correctId !== choice.id;

        return (
          <div key={choice.id} className="flex items-center gap-2">
            <button
              type="button"
              role="radio"
              aria-checked={selected}
              disabled={revealed}
              onClick={() => !eliminated && onSelect?.(choice.id)}
              className={cn(
                "flex flex-1 items-start gap-3 rounded-lg border-2 px-3.5 py-3 text-left text-[16px] leading-[1.5] transition-colors",
                FOCUS_RING,
                isKey && "border-exam-correct bg-exam-correctSoft",
                isWrongPick && "border-exam-incorrect bg-exam-incorrectSoft",
                !isKey && !isWrongPick && selected && "border-exam-blue bg-exam-selected",
                !isKey &&
                  !isWrongPick &&
                  !selected &&
                  "border-exam-border bg-white",
                !revealed &&
                  !selected &&
                  "hover:border-exam-disabled hover:bg-exam-hover",
                revealed && "cursor-default",
                eliminated && "opacity-50"
              )}
            >
              <span
                className={cn(
                  "flex h-[26px] w-[26px] shrink-0 items-center justify-center rounded-full border text-[13px] font-semibold leading-none transition-colors",
                  isKey && "border-exam-correct bg-exam-correct text-white",
                  isWrongPick && "border-exam-incorrect bg-exam-incorrect text-white",
                  !isKey && !isWrongPick && selected && "border-exam-blue bg-exam-blue text-white",
                  !isKey && !isWrongPick && !selected && "border-exam-muted bg-white text-exam-text",
                  eliminated && "line-through"
                )}
              >
                {choice.label}
              </span>

              <MathContent
                html={choice.content}
                className={cn("min-w-0 flex-1 text-exam-text", eliminated && "line-through")}
              />

              {isKey && (
                <span className="flex shrink-0 items-center gap-1 text-[12px] font-semibold text-exam-correct">
                  <Check className="h-4 w-4" aria-hidden="true" />
                  Correct answer
                </span>
              )}
              {isWrongPick && (
                <span className="flex shrink-0 items-center gap-1 text-[12px] font-semibold text-exam-incorrect">
                  <X className="h-4 w-4" aria-hidden="true" />
                  Your answer
                </span>
              )}
            </button>

            {crossOutEnabled && !revealed && (
              <button
                type="button"
                onClick={() => onToggleEliminate?.(choice.id)}
                aria-pressed={eliminated}
                aria-label={eliminated ? `Restore choice ${choice.label}` : `Cross out choice ${choice.label}`}
                title={eliminated ? "Undo cross out" : `Cross out ${choice.label}`}
                className={cn(
                  "flex h-7 min-w-[28px] shrink-0 items-center justify-center rounded-full border border-exam-muted px-1.5 text-[12px] font-medium text-exam-text transition-colors hover:bg-exam-hover",
                  FOCUS_RING
                )}
              >
                {eliminated ? "Undo" : <span className="line-through">{choice.label}</span>}
              </button>
            )}
          </div>
        );
      })}
    </div>
  );
}

/** The numeric entry used for student-produced responses. */
export function FreeResponseInput({
  value,
  onChange,
  disabled,
}: {
  value: string;
  onChange?: (value: string) => void;
  disabled?: boolean;
}) {
  return (
    <div className="max-w-xs space-y-1.5">
      <input
        type="text"
        value={value}
        disabled={disabled}
        onChange={(e) => onChange?.(e.target.value)}
        placeholder="Enter your answer"
        aria-label="Your answer"
        className={cn(
          "w-full rounded border border-exam-disabled bg-white px-3 py-2 text-[16px] text-exam-text placeholder:text-exam-disabled focus:border-exam-blue disabled:bg-exam-hover disabled:text-exam-muted",
          FOCUS_RING
        )}
      />
      <p className="text-[12px] text-exam-muted">Enter a numeric answer (fraction or decimal accepted).</p>
    </div>
  );
}
