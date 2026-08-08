"use client";

import { useEffect, useRef, useState } from "react";

import { cn } from "@/lib/utils";

const FOCUS_RING =
  "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-exam-blue";

/**
 * The screen between clicking "End Module" and the next module appearing.
 *
 * The real test never drops the student straight from one module's last
 * question into the next module's first question -- it confirms the work was
 * saved and moves on by itself. Reproducing that matters for more than
 * fidelity: the submit round-trip plus a server refetch takes long enough that
 * without a screen of its own the student sees a frozen, still-interactive
 * module and clicks things that no longer mean anything.
 */
export function ModuleOverScreen() {
  return (
    <div className="flex h-screen flex-col items-center justify-center bg-exam-bg px-6 text-center">
      <h1 className="text-[26px] font-semibold tracking-tight text-exam-blue">This Module Is Over</h1>
      <p className="mt-4 text-[15px] leading-[1.7] text-exam-text">All your work has been saved.</p>
      <p className="text-[15px] leading-[1.7] text-exam-text">
        You&apos;ll move on automatically in just a moment.
      </p>
      <p className="text-[15px] leading-[1.7] text-exam-text">Do not refresh this page or close this tab.</p>
      <Spinner className="mt-8" />
      <p aria-live="polite" className="sr-only">
        This module is over. Your work has been saved and the next module is loading.
      </p>
    </div>
  );
}

/**
 * Shown once per attempt, immediately after the student starts the test.
 *
 * Purely a curtain over the first paint: the module underneath is already
 * loaded, so this is time the student spends reading rather than waiting.
 */
export function PreparingScreen({ onDone, ms = 2200 }: { onDone: () => void; ms?: number }) {
  // The callback lives in a ref so the timer is armed exactly once. The shell
  // re-renders every second while the module clock ticks, and depending on the
  // (inline, freshly-allocated) callback would clear and restart the timeout on
  // every one of those renders — the curtain would never lift.
  const onDoneRef = useRef(onDone);
  onDoneRef.current = onDone;

  useEffect(() => {
    const t = setTimeout(() => onDoneRef.current(), ms);
    return () => clearTimeout(t);
  }, [ms]);

  return (
    <div className="flex h-screen flex-col items-center justify-center bg-exam-bg px-6 text-center">
      <h1 className="text-[26px] font-semibold tracking-tight text-exam-text">
        We&apos;re Preparing Your Practice Test
      </h1>
      <div className="mt-8 w-full max-w-[380px] rounded-md border border-exam-border bg-white px-8 py-9">
        <Hourglass />
        <p className="mt-6 text-[14px] leading-[1.6] text-exam-muted">
          This may take up to a minute. Please don&apos;t refresh this page or close this tab.
        </p>
      </div>
    </div>
  );
}

/**
 * The break between sections.
 *
 * Dark, deliberately unlike the testing chrome, so nobody mistakes it for a
 * screen they are being timed on. The next module's clock does not start until
 * "Resume Testing" is pressed -- that is the whole point of the screen, so the
 * copy says so outright.
 */
export function BreakScreen({
  studentName,
  nextSectionTitle,
  onResume,
  minutes = 10,
}: {
  studentName: string;
  nextSectionTitle: string;
  onResume: () => void;
  minutes?: number;
}) {
  const [secondsLeft, setSecondsLeft] = useState(minutes * 60);

  useEffect(() => {
    const id = setInterval(() => setSecondsLeft((s) => Math.max(s - 1, 0)), 1000);
    return () => clearInterval(id);
  }, []);

  // Running out the break clock just resumes -- it never costs testing time.
  useEffect(() => {
    if (secondsLeft === 0) onResume();
  }, [secondsLeft, onResume]);

  const mm = String(Math.floor(secondsLeft / 60)).padStart(2, "0");
  const ss = String(secondsLeft % 60).padStart(2, "0");

  return (
    <div className="flex h-screen flex-col bg-[#1B1B1F] text-white">
      <div className="flex flex-1 flex-col items-center justify-center px-6 text-center">
        <p className="text-[13px] font-medium uppercase tracking-[0.14em] text-white/50">Section Break</p>
        <h1 className="mt-3 text-[30px] font-semibold tracking-tight">Take a Break</h1>
        <p className="mt-4 max-w-[34rem] text-[15px] leading-[1.7] text-white/70">
          Your work on the previous section has been saved. {nextSectionTitle} begins when you&apos;re ready — the
          timer for it has not started counting down yet.
        </p>

        <p className="mt-8 font-mono text-[44px] font-semibold tabular-nums tracking-tight" aria-live="off">
          {mm}:{ss}
        </p>
        <p className="mt-1 text-[13px] text-white/50">remaining in your break</p>

        <button
          type="button"
          onClick={onResume}
          className={cn(
            "mt-8 rounded-full bg-exam-gold px-7 py-2.5 text-[14px] font-semibold text-[#1B1B1F]",
            "transition-colors hover:bg-exam-gold/90 focus-visible:ring-offset-[#1B1B1F]",
            FOCUS_RING
          )}
        >
          Resume Testing
        </button>
      </div>

      <p className="px-8 pb-7 text-[15px] font-semibold text-white/90">{studentName}</p>
    </div>
  );
}

function Spinner({ className }: { className?: string }) {
  return (
    <span
      role="status"
      aria-label="Loading the next module"
      className={cn(
        "block h-8 w-8 animate-spin rounded-full border-[3px] border-exam-divider border-t-exam-blue",
        className
      )}
    />
  );
}

function Hourglass() {
  return (
    <svg viewBox="0 0 64 64" className="mx-auto h-16 w-16" role="presentation" aria-hidden="true">
      <path d="M18 6h28M18 58h28" stroke="#5B6474" strokeWidth="3.5" strokeLinecap="round" />
      <path
        d="M20 6v9c0 6 12 11 12 17s-12 11-12 17v9M44 6v9c0 6-12 11-12 17s12 11 12 17v9"
        fill="none"
        stroke="#5B6474"
        strokeWidth="3.5"
        strokeLinejoin="round"
      />
      <path d="M32 32c0-5 9-9 10.5-14h-21C23 23 32 27 32 32Z" fill="#E8613C" />
      <path d="M32 34c0 4 7 8 9 13H23c2-5 9-9 9-13Z" fill="#E8613C" opacity="0.55" />
    </svg>
  );
}
