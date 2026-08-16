"use client";

import { useEffect, useRef, useState, type ReactNode } from "react";
import { ChevronDown, Clock, Maximize, Minimize, TriangleAlert, X } from "lucide-react";

import { cn } from "@/lib/utils";
import { FOCUS_RING, TestingBanner } from "@/components/testing/primitives";
import { useEscape } from "@/lib/exam/use-escape";

/**
 * The full-screen chrome the IELTS Writing and Speaking rooms sit inside.
 *
 * Deliberately the SAT testing chrome, not a second look: the same fixed
 * `exam-*` kiosk palette, the same 62px header with a centred clock and a
 * Hide/Show toggle, the same navy strip, the same 54px bottom bar. A student
 * who has sat a practice SAT here should recognise the room instantly, and the
 * shared `testing/primitives` mean a change to the testing look still lands in
 * one place.
 *
 * What it does NOT do is grade, autosave, or submit — the caller owns all of
 * that. This is chrome and a clock.
 */

function formatClock(total: number): string {
  const sign = total < 0 ? "-" : "";
  const s = Math.abs(total);
  return `${sign}${String(Math.floor(s / 60)).padStart(2, "0")}:${String(s % 60).padStart(2, "0")}`;
}

const WARNING_AT_SECONDS = 5 * 60;
const CRITICAL_AT_SECONDS = 60;

export interface IeltsShellProps {
  /** Shown top-left, e.g. "Academic Writing — Task 2". */
  title: string;
  /** Expanded by the Directions disclosure. */
  directions?: string[];
  /** Countdown length. Omit for a room with no clock (a reviewed, read-only view). */
  totalSeconds?: number | null;
  /** Seconds already spent, so a reload does not hand back the full allowance. */
  elapsedSeconds?: number;
  /** Called once when the clock first reaches zero. */
  onTimeUp?: () => void;
  bannerText?: string;
  /** Bottom-left, matching the SAT shell. */
  studentName: string;
  /** Bottom-centre pill, e.g. "Question 3 of 12". */
  centreLabel?: ReactNode;
  /** Bottom-right controls. */
  actions?: ReactNode;
  /** Top-left escape hatch. */
  exitHref: string;
  exitLabel?: string;
  children: ReactNode;
}

export function IeltsShell({
  title,
  directions,
  totalSeconds,
  elapsedSeconds = 0,
  onTimeUp,
  bannerText = "This is a practice test",
  studentName,
  centreLabel,
  actions,
  exitHref,
  exitLabel = "Save and exit",
  children,
}: IeltsShellProps) {
  const rootRef = useRef<HTMLDivElement>(null);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [timerHidden, setTimerHidden] = useState(false);
  const [directionsOpen, setDirectionsOpen] = useState(false);
  const [remaining, setRemaining] = useState(
    totalSeconds == null ? null : totalSeconds - elapsedSeconds
  );
  const firedRef = useRef(false);

  // Wall-clock, not a counter: a backgrounded tab has its intervals throttled
  // to once a minute, and a counter would quietly run slow for exactly the
  // student who left the tab to look something up.
  useEffect(() => {
    if (totalSeconds == null) return;
    const deadline = Date.now() + (totalSeconds - elapsedSeconds) * 1000;
    const tick = () => {
      const left = Math.round((deadline - Date.now()) / 1000);
      setRemaining(left);
      if (left <= 0 && !firedRef.current) {
        firedRef.current = true;
        onTimeUp?.();
      }
    };
    tick();
    const id = setInterval(tick, 1000);
    return () => clearInterval(id);
    // onTimeUp is intentionally not a dependency: a caller passing an inline
    // arrow would otherwise restart the clock on every render.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [totalSeconds, elapsedSeconds]);

  useEffect(() => {
    const onChange = () => setIsFullscreen(Boolean(document.fullscreenElement));
    document.addEventListener("fullscreenchange", onChange);
    return () => document.removeEventListener("fullscreenchange", onChange);
  }, []);

  useEscape(directionsOpen, () => setDirectionsOpen(false));

  async function toggleFullscreen() {
    try {
      if (document.fullscreenElement) await document.exitFullscreen();
      else await rootRef.current?.requestFullscreen();
    } catch {
      // Safari refuses without a user gesture it recognises; the room works
      // maximised either way, so a failure here is not worth an error toast.
    }
  }

  const warning = remaining != null && remaining <= WARNING_AT_SECONDS;
  const critical = remaining != null && remaining <= CRITICAL_AT_SECONDS;

  return (
    // `theme-light-scope` pins the shadcn tokens light inside the room. The
    // `exam-*` palette is already fixed, but a shared component that reaches
    // for `bg-background` would otherwise follow the site theme and render a
    // dark control on a light kiosk for anyone using dark mode.
    <div ref={rootRef} className="theme-light-scope flex h-screen flex-col bg-exam-bg text-exam-text">
      <header className="relative z-20 shrink-0 border-b border-dashed border-exam-divider bg-exam-header">
        <div className="flex h-[62px] items-center px-4">
          <div className="flex min-w-0 flex-col gap-0.5">
            <p className="truncate text-[14px] font-semibold leading-tight">{title}</p>
            {directions && directions.length > 0 ? (
              <button
                type="button"
                onClick={() => setDirectionsOpen(true)}
                className={cn(
                  "flex w-fit items-center gap-1 rounded text-[13px] leading-tight text-exam-text hover:underline",
                  FOCUS_RING
                )}
              >
                Directions <ChevronDown className="h-3.5 w-3.5" />
              </button>
            ) : (
              <a href={exitHref} className={cn("w-fit rounded text-[13px] leading-tight hover:underline", FOCUS_RING)}>
                {exitLabel}
              </a>
            )}
          </div>

          {remaining != null && (
            <div className="pointer-events-none absolute left-1/2 flex -translate-x-1/2 flex-col items-center">
              <div className="flex h-[26px] items-center gap-1.5">
                {timerHidden ? (
                  <Clock className="h-5 w-5 text-exam-muted" aria-hidden="true" />
                ) : (
                  <>
                    {critical && <TriangleAlert className="h-4 w-4 text-exam-error" aria-hidden="true" />}
                    <span
                      suppressHydrationWarning
                      className={cn(
                        "text-[20px] font-semibold tabular-nums leading-none",
                        critical ? "text-exam-error" : warning ? "text-exam-warning" : "text-exam-text"
                      )}
                    >
                      {formatClock(remaining)}
                    </span>
                  </>
                )}
              </div>
              <button
                type="button"
                onClick={() => setTimerHidden((v) => !v)}
                aria-pressed={timerHidden}
                aria-label={timerHidden ? "Show the timer" : "Hide the timer"}
                className={cn(
                  "pointer-events-auto mt-1 rounded-full border border-exam-text px-2.5 py-[1px] text-[11px] font-medium leading-tight text-exam-text transition-colors hover:bg-exam-hover",
                  FOCUS_RING
                )}
              >
                {timerHidden ? "Show" : "Hide"}
              </button>
            </div>
          )}

          <div className="ml-auto flex items-center gap-1">
            <button
              type="button"
              onClick={toggleFullscreen}
              className={cn(
                "flex h-[46px] min-w-[54px] flex-col items-center justify-center gap-1 rounded px-2 text-[11px] font-medium leading-none text-exam-text transition-colors hover:bg-exam-hover",
                FOCUS_RING
              )}
            >
              {isFullscreen ? <Minimize className="h-[18px] w-[18px]" /> : <Maximize className="h-[18px] w-[18px]" />}
              <span className="whitespace-nowrap">{isFullscreen ? "Exit" : "Full Screen"}</span>
            </button>
            <a
              href={exitHref}
              className={cn(
                "flex h-[46px] min-w-[54px] flex-col items-center justify-center gap-1 rounded px-2 text-[11px] font-medium leading-none text-exam-text transition-colors hover:bg-exam-hover",
                FOCUS_RING
              )}
            >
              <X className="h-[18px] w-[18px]" />
              <span className="whitespace-nowrap">Exit</span>
            </a>
          </div>
        </div>
      </header>

      <TestingBanner>{bannerText}</TestingBanner>

      <div className="min-h-0 flex-1 overflow-hidden">{children}</div>

      <div className="relative shrink-0 border-t border-exam-border bg-exam-header">
        <div className="flex h-[54px] items-center gap-3 px-4">
          <p className="hidden truncate text-[14px] font-medium sm:block sm:w-[26%]">{studentName}</p>
          <div className="flex flex-1 justify-center">
            {centreLabel && (
              <span className="flex h-[34px] items-center rounded-md bg-exam-strip px-4 text-[13px] font-medium text-white">
                {centreLabel}
              </span>
            )}
          </div>
          <div className="flex items-center justify-end gap-2 sm:w-[26%]">{actions}</div>
        </div>
      </div>

      {directionsOpen && directions && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          <div
            className="absolute inset-0 bg-black/40"
            onClick={() => setDirectionsOpen(false)}
            aria-hidden="true"
          />
          <div
            role="dialog"
            aria-modal="true"
            aria-label="Directions"
            className="relative max-h-[80vh] w-full max-w-[42rem] overflow-y-auto rounded-md border border-exam-border bg-white p-6 text-exam-text shadow-xl"
          >
            <div className="mb-3 flex items-start justify-between gap-4">
              <h2 className="text-[18px] font-semibold">{title}</h2>
              <button
                type="button"
                onClick={() => setDirectionsOpen(false)}
                aria-label="Close directions"
                className={cn("rounded p-1 hover:bg-exam-hover", FOCUS_RING)}
              >
                <X className="h-4 w-4" />
              </button>
            </div>
            <div className="space-y-3 text-[14px] leading-[1.65]">
              {directions.map((p, i) => (
                <p key={i}>{p}</p>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
