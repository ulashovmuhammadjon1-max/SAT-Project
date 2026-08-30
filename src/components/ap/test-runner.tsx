"use client";

import { useCallback, useEffect, useMemo, useRef, useState, useTransition } from "react";
import { MathContent } from "@/components/shared/math-content";
import { useRouter } from "next/navigation";
import {
  Bookmark,
  ChevronDown,
  ChevronUp,
  CircleHelp,
  Clock,
  Loader2,
  Maximize2,
  Minimize2,
  TriangleAlert,
  X,
} from "lucide-react";
import { toast } from "sonner";

import { AnswerChoiceList, type TestingChoice } from "@/components/testing/answer-choices";
import {
  FOCUS_RING,
  NavButton,
  QuestionNumberChip,
  TestingBanner,
  ToolButton,
} from "@/components/testing/primitives";
import { QuestionPalette } from "@/components/exam/question-palette";
import { CALCULATOR_LABEL, type ApCalculatorPolicy } from "@/lib/ap/tests";
import { saveProgress, submitTest, type ApExamPayload } from "@/server/actions/student/ap-tests";
import type { QuestionState } from "@/types/exam";
import { cn } from "@/lib/utils";

const LETTERS = ["A", "B", "C", "D", "E"];

const WARNING_AT_SECONDS = 5 * 60;
const CRITICAL_AT_SECONDS = 60;
/** How long after the last keystroke the answers go to the server. */
const SAVE_DEBOUNCE_MS = 1_200;
/** A backstop, so a student who stops interacting still has their work saved. */
const SAVE_INTERVAL_MS = 15_000;

function formatClock(totalSeconds: number): string {
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  const mm = minutes.toString().padStart(2, "0");
  const ss = seconds.toString().padStart(2, "0");
  return hours > 0 ? `${hours}:${mm}:${ss}` : `${mm}:${ss}`;
}

function spokenClock(totalSeconds: number): string {
  const minutes = Math.round(totalSeconds / 60);
  return minutes === 1 ? "1 minute remaining" : `${minutes} minutes remaining`;
}

/**
 * The AP practice-test runner — the exam sibling of `topic-runner.tsx`.
 *
 * Same shell, opposite posture: the topic runner grades as you go and shows the
 * explanation immediately; this one shows nothing until the whole test is
 * submitted, because that is what a real sitting does. It shares the header,
 * the navy banner, the question-number bar, the answer list and the question
 * palette with the SAT exam and the Question Bank, so a student who has taken
 * one has already learned this one.
 *
 * Three things are worth knowing about how it works:
 *
 *  - **The clock is the server's.** `expiresAt` came from the server at start;
 *    every tick re-reads the wall clock against it rather than decrementing, so
 *    a backgrounded tab (which browsers throttle to a tick a minute), a sleep,
 *    or a reload all resume on the correct second rather than handing out extra
 *    time. At zero it submits, once, whatever the student was doing.
 *  - **Answers survive a reload** because they are on the server, not in this
 *    component: a debounced write after each change, a 15-second backstop, and
 *    an immediate write when a question is marked for review.
 *  - **Sections share one countdown.** The configuration gives each section its
 *    own time limit and the header shows it, but the deadline enforced is the
 *    test's total. A real AP sitting locks Part A when its time is called; we
 *    deliberately do not, because a practice student who finishes Part A in
 *    forty minutes should be able to start Part B rather than sit and wait, and
 *    because there is nowhere in `ApTestAttempt` to record which section they
 *    are in without guessing at reload.
 */
export function ApTestRunner({
  payload,
  exitHref,
}: {
  payload: ApExamPayload;
  exitHref: string;
}) {
  const router = useRouter();
  const rootRef = useRef<HTMLDivElement>(null);
  const { questions, sections } = payload;

  const [answers, setAnswers] = useState<Record<string, number>>(payload.answers);
  const [marked, setMarked] = useState<Set<string>>(new Set(payload.marked));
  const [index, setIndex] = useState(0);
  const [menuOpen, setMenuOpen] = useState(false);
  const [helpOpen, setHelpOpen] = useState(false);
  const [directionsOpen, setDirectionsOpen] = useState(false);
  const [confirmOpen, setConfirmOpen] = useState(false);
  const [timerHidden, setTimerHidden] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [submitting, startSubmit] = useTransition();
  const submittedRef = useRef(false);

  const q = questions[index];
  const section = useMemo(() => {
    for (let i = sections.length - 1; i >= 0; i--) {
      if (index >= sections[i].offset) return sections[i];
    }
    return sections[0];
  }, [sections, index]);

  const answeredCount = Object.keys(answers).length;
  const unanswered = questions.length - answeredCount;

  // ---- Persistence ---------------------------------------------------------
  // Kept in refs as well as state so the save functions never close over a
  // stale answer map — a debounced write firing with last-render's answers is
  // exactly how a student loses the choice they just made.
  const answersRef = useRef(answers);
  answersRef.current = answers;
  const markedRef = useRef(marked);
  markedRef.current = marked;
  const dirtyRef = useRef(false);
  const saveTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  const persist = useCallback(async () => {
    if (!dirtyRef.current || submittedRef.current) return;
    dirtyRef.current = false;
    const res = await saveProgress({
      attemptId: payload.attemptId,
      answers: answersRef.current,
      marked: [...markedRef.current],
    });
    if (res.expired) {
      // The deadline passed while this was in flight; the countdown below is
      // about to submit, so nothing to do but stop writing.
      dirtyRef.current = false;
    } else if (res.error) {
      // Left dirty on purpose: the next tick retries rather than dropping the
      // answers on the floor.
      dirtyRef.current = true;
    }
  }, [payload.attemptId]);

  const queueSave = useCallback(() => {
    dirtyRef.current = true;
    if (saveTimer.current) clearTimeout(saveTimer.current);
    saveTimer.current = setTimeout(() => void persist(), SAVE_DEBOUNCE_MS);
  }, [persist]);

  useEffect(() => {
    const interval = setInterval(() => void persist(), SAVE_INTERVAL_MS);
    const onHide = () => {
      if (document.visibilityState === "hidden") void persist();
    };
    document.addEventListener("visibilitychange", onHide);
    return () => {
      clearInterval(interval);
      document.removeEventListener("visibilitychange", onHide);
      if (saveTimer.current) clearTimeout(saveTimer.current);
      void persist();
    };
  }, [persist]);

  // ---- Submitting ----------------------------------------------------------
  const finish = useCallback(() => {
    if (submittedRef.current) return;
    submittedRef.current = true;
    setConfirmOpen(false);
    startSubmit(async () => {
      // Flush first: a choice made a second before the deadline must be in the
      // answers the server grades.
      dirtyRef.current = true;
      await persist();
      const res = await submitTest(payload.attemptId);
      if (res.error && !res.ok) {
        // Already submitted is not a failure worth trapping the student in —
        // the result page is where they wanted to go either way.
        toast.error(res.error);
      }
      router.replace(`/ap/tests/result/${payload.attemptId}`);
    });
  }, [payload.attemptId, persist, router]);

  // ---- Countdown -----------------------------------------------------------
  const deadlineMs = useMemo(() => new Date(payload.expiresAt).getTime(), [payload.expiresAt]);
  const readClock = useCallback(
    () => Math.max(Math.ceil((deadlineMs - Date.now()) / 1000), 0),
    [deadlineMs],
  );
  const [secondsRemaining, setSecondsRemaining] = useState(readClock);

  useEffect(() => {
    const tick = () => setSecondsRemaining(readClock());
    const interval = setInterval(tick, 1000);
    document.addEventListener("visibilitychange", tick);
    window.addEventListener("focus", tick);
    return () => {
      clearInterval(interval);
      document.removeEventListener("visibilitychange", tick);
      window.removeEventListener("focus", tick);
    };
  }, [readClock]);

  useEffect(() => {
    if (secondsRemaining <= 0) finish();
  }, [secondsRemaining, finish]);

  const announcedRef = useRef<number[]>([]);
  const [announcement, setAnnouncement] = useState("");
  useEffect(() => {
    for (const threshold of [WARNING_AT_SECONDS, CRITICAL_AT_SECONDS]) {
      if (secondsRemaining > 0 && secondsRemaining <= threshold && !announcedRef.current.includes(threshold)) {
        announcedRef.current.push(threshold);
        setAnnouncement(spokenClock(threshold));
      }
    }
  }, [secondsRemaining]);

  // ---- Fullscreen ----------------------------------------------------------
  useEffect(() => {
    function onChange() {
      setIsFullscreen(document.fullscreenElement === rootRef.current);
    }
    document.addEventListener("fullscreenchange", onChange);
    return () => document.removeEventListener("fullscreenchange", onChange);
  }, []);

  const toggleFullscreen = useCallback(async () => {
    try {
      if (document.fullscreenElement) await document.exitFullscreen();
      else await rootRef.current?.requestFullscreen();
    } catch {
      toast.error("Your browser wouldn't allow fullscreen here.");
    }
  }, []);

  // ---- Navigation and answering -------------------------------------------
  const goTo = useCallback(
    (next: number) => {
      if (next < 0 || next >= questions.length) return;
      setIndex(next);
      setMenuOpen(false);
    },
    [questions.length],
  );

  const choose = useCallback(
    (choiceIndex: number) => {
      if (!q) return;
      setAnswers((prev) => ({ ...prev, [q.id]: choiceIndex }));
      queueSave();
    },
    [q, queueSave],
  );

  const toggleMark = useCallback(() => {
    if (!q) return;
    setMarked((prev) => {
      const next = new Set(prev);
      if (next.has(q.id)) next.delete(q.id);
      else next.add(q.id);
      markedRef.current = next;
      return next;
    });
    // Immediately, not on the debounce: a review flag is exactly the state a
    // student expects to survive a stray refresh.
    dirtyRef.current = true;
    void persist();
  }, [q, persist]);

  // ---- Keyboard ------------------------------------------------------------
  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      const el = document.activeElement;
      if (el instanceof HTMLInputElement || el instanceof HTMLTextAreaElement) return;
      if (e.key === "Escape") {
        setMenuOpen(false);
        setHelpOpen(false);
        setDirectionsOpen(false);
        setConfirmOpen(false);
        return;
      }
      if (menuOpen || helpOpen || directionsOpen || confirmOpen) return;
      if (e.key === "ArrowRight") goTo(index + 1);
      if (e.key === "ArrowLeft") goTo(index - 1);
      if (q) {
        const i = LETTERS.indexOf(e.key.toUpperCase());
        if (i !== -1 && i < q.choices.length) choose(i);
      }
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [index, menuOpen, helpOpen, directionsOpen, confirmOpen, q, goTo, choose]);

  // ---- Palette -------------------------------------------------------------
  // Scoped to the current section, the way a real exam's question menu is.
  const paletteStates: QuestionState[] = useMemo(
    () =>
      questions
        .slice(section.offset, section.offset + section.count)
        .map((item) => ({
          selectedChoiceId:
            answers[item.id] === undefined ? null : String(answers[item.id]),
          freeResponseAnswer: "",
          flagged: marked.has(item.id),
          eliminated: [],
          timeSpentSeconds: 0,
          changedAnswerCount: 0,
        })),
    [questions, section, answers, marked],
  );

  if (!q) {
    return (
      <div className="flex h-full flex-col items-center justify-center gap-3 bg-exam-bg px-6 text-center text-exam-text">
        <p className="text-[15px]">This test has no questions left to show.</p>
        <NavButton onClick={() => router.push(exitHref)}>Back to practice tests</NavButton>
      </div>
    );
  }

  const choices: TestingChoice[] = q.choices.map((content, i) => ({
    id: String(i),
    label: LETTERS[i],
    content,
  }));
  const selected = answers[q.id];
  const isLast = index + 1 >= questions.length;
  const warning = secondsRemaining <= WARNING_AT_SECONDS;
  const critical = secondsRemaining <= CRITICAL_AT_SECONDS;

  return (
    <div ref={rootRef} className="flex h-full flex-col bg-exam-bg text-exam-text">
      <header className="shrink-0 border-b border-dashed border-exam-divider bg-exam-header">
        <div className="relative flex h-[62px] items-center px-4">
          <div className="flex min-w-0 flex-col gap-0.5">
            <p className="truncate text-[14px] font-semibold leading-tight">{payload.testName}</p>
            <button
              type="button"
              onClick={() => setDirectionsOpen(true)}
              className={cn(
                "flex w-fit items-center gap-1 rounded text-[13px] leading-tight text-exam-text hover:underline",
                FOCUS_RING,
              )}
            >
              <span className="truncate">{section.name}</span>
              <ChevronDown className="h-3.5 w-3.5 shrink-0" />
            </button>
          </div>

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
                      critical ? "text-exam-error" : warning ? "text-exam-warning" : "text-exam-text",
                    )}
                  >
                    {formatClock(secondsRemaining)}
                  </span>
                </>
              )}
            </div>
            <button
              type="button"
              onClick={() => setTimerHidden((v) => !v)}
              aria-pressed={timerHidden}
              aria-label={timerHidden ? "Show the countdown timer" : "Hide the countdown timer"}
              className={cn(
                "pointer-events-auto mt-1 rounded-full border border-exam-text px-2.5 py-[1px] text-[11px] font-medium leading-tight text-exam-text transition-colors hover:bg-exam-hover",
                FOCUS_RING,
              )}
            >
              {timerHidden ? "Show" : "Hide"}
            </button>
          </div>

          <div className="ml-auto flex items-center gap-0.5">
            <ToolButton icon={CircleHelp} label="Help" onClick={() => setHelpOpen(true)} />
            <ToolButton
              icon={isFullscreen ? Minimize2 : Maximize2}
              label={isFullscreen ? "Exit Full" : "Fullscreen"}
              active={isFullscreen}
              onClick={toggleFullscreen}
            />
            <button
              type="button"
              onClick={async () => {
                dirtyRef.current = true;
                await persist();
                router.push(exitHref);
              }}
              title="Leave — your answers are saved and the clock keeps running"
              className={cn(
                "ml-1 rounded-full border border-exam-border bg-white px-3 py-1.5 text-[12px] font-medium text-exam-text transition-colors hover:bg-exam-hover",
                FOCUS_RING,
              )}
            >
              Save &amp; Exit
            </button>
          </div>
        </div>
      </header>

      <TestingBanner>
        {payload.subjectName} practice test — {CALCULATOR_LABEL[section.calculator as ApCalculatorPolicy] ?? section.calculator}
      </TestingBanner>

      <div aria-live="polite" className="sr-only">
        {announcement}
      </div>

      <div className="flex-1 overflow-hidden">
        <div className="flex h-full flex-col">
          <div className="shrink-0 border-b border-exam-border bg-exam-header px-6 py-1.5 lg:px-10">
            <div className="flex items-center gap-3">
              <QuestionNumberChip n={index + 1} />
              <span className="sr-only">
                Question {index + 1} of {questions.length}
              </span>
              <button
                type="button"
                onClick={toggleMark}
                aria-pressed={marked.has(q.id)}
                className={cn(
                  "flex items-center gap-1.5 rounded px-1 py-0.5 text-[13px] font-medium text-exam-text transition-colors hover:bg-exam-hover",
                  FOCUS_RING,
                )}
              >
                <Bookmark
                  className={cn(
                    "h-4 w-4",
                    marked.has(q.id) ? "fill-exam-flag text-exam-flag" : "text-exam-muted",
                  )}
                />
                {marked.has(q.id) ? "Marked for Review" : "Mark for Review"}
              </button>

              <span className="ml-auto hidden text-[12px] text-exam-muted sm:block">
                Unit {q.unit} · {q.topic} {q.topicTitle}
              </span>
            </div>
          </div>

          <div className="min-h-0 flex-1 overflow-y-auto exam-scroll px-6 pb-16 pt-6 lg:px-10">
            <div className="mx-auto max-w-[46rem]">
              {q.table && (
                <div className="mb-5 overflow-x-auto">
                  <table className="border-collapse text-[15px]">
                    <thead>
                      <tr>
                        {q.table.headers.map((h, i) => (
                          <th
                            key={i}
                            className="border border-exam-border bg-exam-header px-3 py-1.5 text-left font-semibold"
                          >
                            <MathContent html={h} />
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {q.table.rows.map((row, i) => (
                        <tr key={i}>
                          {row.map((cell, j) => (
                            <td key={j} className="border border-exam-border px-3 py-1.5">
                              <MathContent html={cell} />
                            </td>
                          ))}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}

              <MathContent className="block text-[17px] leading-relaxed" html={q.stem} />

              <div className="mt-5">
                <AnswerChoiceList
                  choices={choices}
                  selectedId={selected === undefined ? null : String(selected)}
                  onSelect={(id) => choose(Number(id))}
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="relative shrink-0 border-t border-exam-border bg-exam-header">
        <div className="flex h-[54px] items-center gap-2 px-4">
          <div className="hidden min-w-0 items-center gap-1.5 sm:flex sm:w-[30%]">
            {sections.length > 1 ? (
              sections.map((s) => {
                const active = s.id === section.id;
                return (
                  <button
                    key={s.id}
                    type="button"
                    onClick={() => goTo(s.offset)}
                    aria-current={active ? "true" : undefined}
                    title={`${s.name} — ${s.count} questions, ${s.timeLimitMinutes} min suggested`}
                    className={cn(
                      "rounded-full border px-3 py-1 text-[12px] font-medium transition-colors",
                      active
                        ? "border-exam-blue bg-exam-selected text-exam-blue"
                        : "border-exam-border bg-white text-exam-text hover:bg-exam-hover",
                      FOCUS_RING,
                    )}
                  >
                    {s.short}
                  </button>
                );
              })
            ) : (
              <p className="truncate text-[13px] text-exam-muted">
                {answeredCount} of {questions.length} answered
              </p>
            )}
          </div>

          <div className="flex flex-1 justify-center">
            <button
              type="button"
              onClick={() => setMenuOpen((v) => !v)}
              aria-expanded={menuOpen}
              className={cn(
                "flex h-[34px] items-center gap-1.5 rounded-md bg-exam-strip px-4 text-[13px] font-medium text-white transition-colors hover:bg-exam-strip/90",
                FOCUS_RING,
              )}
            >
              Question {index + 1} of {questions.length}
              <ChevronUp className={cn("h-3.5 w-3.5 transition-transform", menuOpen && "rotate-180")} />
            </button>
          </div>

          <div className="flex items-center justify-end gap-2 sm:w-[30%]">
            <NavButton variant="ghost" onClick={() => goTo(index - 1)} disabled={index === 0}>
              Back
            </NavButton>
            {isLast ? (
              <NavButton onClick={() => setConfirmOpen(true)} disabled={submitting}>
                {submitting ? (
                  <span className="flex items-center gap-1.5">
                    <Loader2 className="h-3.5 w-3.5 animate-spin" /> Submitting
                  </span>
                ) : (
                  "Submit test"
                )}
              </NavButton>
            ) : (
              <NavButton onClick={() => goTo(index + 1)}>Next</NavButton>
            )}
          </div>
        </div>

        <QuestionPalette
          open={menuOpen}
          onOpenChange={setMenuOpen}
          title={`${section.name} — ${section.count} questions`}
          count={section.count}
          currentIndex={index - section.offset}
          states={paletteStates}
          onJump={(i) => goTo(section.offset + i)}
          onGoToReview={() => setConfirmOpen(true)}
          reviewLabel="Submit test"
        />
      </div>

      {directionsOpen && (
        <ExamDialog title={section.name} onClose={() => setDirectionsOpen(false)}>
          <p>{section.directions}</p>
          <p>
            <strong className="text-exam-text">
              {CALCULATOR_LABEL[section.calculator as ApCalculatorPolicy] ?? section.calculator}
            </strong>{" "}
            — {payload.calculatorNote}
          </p>
          {payload.referenceNote && <p>{payload.referenceNote}</p>}
          <p>
            This section is {section.count} questions and the real exam allows{" "}
            {section.timeLimitMinutes} minutes for it. The countdown above runs on the whole test,
            so spending longer here leaves less for the rest.
          </p>
        </ExamDialog>
      )}

      {helpOpen && (
        <ExamDialog title="Taking this test" onClose={() => setHelpOpen(false)}>
          <p>
            Nothing is graded until you submit — no answer is marked right or wrong while you work,
            exactly as in a real sitting.
          </p>
          <p>
            <strong className="text-exam-text">Question {"{n}"} of {"{n}"}</strong> at the bottom
            opens the full list, so you can jump anywhere and see what is still unanswered.{" "}
            <strong className="text-exam-text">Mark for Review</strong> flags a question there
            without changing your answer.
          </p>
          <p>
            Press <kbd className="rounded border border-exam-border px-1">A</kbd>–
            <kbd className="rounded border border-exam-border px-1">E</kbd> to choose and the arrow
            keys to move between questions.
          </p>
          <p>
            Your answers are saved to your account as you go, so a reload or a closed tab does not
            cost you the sitting. The clock keeps running either way, and the test submits itself
            when it reaches zero.
          </p>
        </ExamDialog>
      )}

      {confirmOpen && (
        <ExamDialog title="Submit this test?" onClose={() => setConfirmOpen(false)}>
          <p>
            {unanswered === 0 ? (
              <>All {questions.length} questions are answered.</>
            ) : (
              <>
                <strong className="text-exam-text">
                  {unanswered} of {questions.length} questions
                </strong>{" "}
                {unanswered === 1 ? "is" : "are"} still unanswered. Unanswered questions score
                nothing — there is no penalty for a guess.
              </>
            )}
          </p>
          <p>
            You cannot return to the questions after submitting. Your score and a full review with
            explanations come next.
          </p>
          <div className="mt-4 flex justify-end gap-2">
            <NavButton variant="ghost" onClick={() => setConfirmOpen(false)}>
              Keep working
            </NavButton>
            <NavButton onClick={finish} disabled={submitting}>
              {submitting ? (
                <span className="flex items-center gap-1.5">
                  <Loader2 className="h-3.5 w-3.5 animate-spin" /> Submitting
                </span>
              ) : (
                "Submit test"
              )}
            </NavButton>
          </div>
        </ExamDialog>
      )}
    </div>
  );
}

function ExamDialog({
  title,
  onClose,
  children,
}: {
  title: string;
  onClose: () => void;
  children: React.ReactNode;
}) {
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if (e.key === "Escape") onClose();
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 p-4">
      <div
        role="dialog"
        aria-modal="true"
        aria-label={title}
        className="w-full max-w-md rounded-lg border border-exam-border bg-white p-5 text-exam-text shadow-xl"
      >
        <div className="flex items-start justify-between gap-4">
          <h2 className="text-[16px] font-semibold">{title}</h2>
          <button
            type="button"
            onClick={onClose}
            aria-label="Close"
            className={cn("rounded p-1 hover:bg-exam-hover", FOCUS_RING)}
          >
            <X className="h-4 w-4" />
          </button>
        </div>
        <div className="mt-3 space-y-2.5 text-[14px] leading-relaxed text-exam-muted">{children}</div>
      </div>
    </div>
  );
}
