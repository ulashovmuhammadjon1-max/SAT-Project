"use client";

import type { ComponentType, ReactNode } from "react";

import { cn } from "@/lib/utils";

/**
 * The pieces every Scholarly testing surface is built from — practice tests,
 * Question Bank practice, and post-test review.
 *
 * These live outside `components/exam` on purpose: the exam shell used to own
 * them privately, which is how the Question Bank ended up looking like a
 * different product. Anything that appears in more than one testing surface
 * belongs here, so a change to the testing look lands everywhere at once.
 */

export const FOCUS_RING =
  "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-exam-blue";

/** The Back/Next pill on the bottom bar. */
export function NavButton({
  children,
  onClick,
  disabled,
  variant = "primary",
  type = "button",
  action,
}: {
  children: ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  /** "ghost" is for the secondary action sitting beside a primary one. */
  variant?: "primary" | "ghost";
  type?: "button" | "submit";
  /**
   * A stable name for this control, e.g. "next" or "submit". The bottom bar
   * reflows as its status text changes ("Saving…" becoming "Draft saved"
   * shifts every button left), so anything driving this UI needs a handle that
   * does not move with the label.
   */
  action?: string;
}) {
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      data-action={action}
      className={cn(
        "h-[34px] rounded-full px-5 text-[13px] font-medium transition-colors disabled:pointer-events-none disabled:opacity-50",
        variant === "primary"
          ? "bg-exam-blue text-white hover:bg-exam-blueHover"
          : "border border-exam-border bg-white text-exam-text hover:bg-exam-hover",
        FOCUS_RING
      )}
    >
      {children}
    </button>
  );
}

/** An icon-over-label control in the top-right tool cluster. */
export function ToolButton({
  icon: Icon,
  label,
  onClick,
  active,
  disabled,
}: {
  icon: ComponentType<{ className?: string }>;
  label: string;
  onClick: () => void;
  active?: boolean;
  disabled?: boolean;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      aria-pressed={active}
      className={cn(
        "flex h-[46px] min-w-[54px] flex-col items-center justify-center gap-1 rounded px-2 text-[11px] font-medium leading-none transition-colors",
        active ? "bg-exam-hover text-exam-blue" : "text-exam-text hover:bg-exam-hover",
        "disabled:pointer-events-none disabled:opacity-40",
        FOCUS_RING
      )}
    >
      <Icon className="h-[18px] w-[18px]" />
      <span className="whitespace-nowrap">{label}</span>
    </button>
  );
}

/**
 * The navy strip under the header. On a practice test it reads "This is a
 * practice test"; in the Question Bank it names the mode instead, so the
 * student always knows which surface they are on without it looking different.
 */
export function TestingBanner({ children }: { children: ReactNode }) {
  return (
    <div className="shrink-0 px-4 pb-1 pt-2">
      <p className="rounded-[3px] bg-exam-strip py-[5px] text-center text-[11px] font-semibold uppercase tracking-[0.09em] text-white">
        {children}
      </p>
    </div>
  );
}

/** The numbered chip that opens a question panel, matching the exam's. */
export function QuestionNumberChip({ n }: { n: number }) {
  return (
    <span
      className="flex h-[26px] w-[26px] shrink-0 items-center justify-center rounded-[3px] bg-exam-strip text-[13px] font-semibold text-white"
      aria-hidden="true"
    >
      {n}
    </span>
  );
}
