"use client";

import { useCallback, useEffect, useMemo, useRef, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import {
  Bookmark,
  ChevronUp,
  CircleHelp,
  Loader2,
  Maximize2,
  Minimize2,
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
import { QuestionPalette, type QuestionOutcome } from "@/components/exam/question-palette";
import { answerApQuestion, type ApSessionQuestion } from "@/server/actions/student/ap";
import type { QuestionState } from "@/types/exam";
import { cn } from "@/lib/utils";

const LETTERS = ["A", "B", "C", "D", "E"];

interface Graded {
  correctIndex: number;
  isCorrect: boolean;
  explanation: string | null;
}

/**
 * The AP topic runner, built on the same testing shell as the practice test and
 * the Question Bank: full-viewport layout, the question-number bar that opens
 * the palette, mark for review, and a fullscreen toggle.
 *
 * Grading still happens on the server. The payload this component receives
 * carries no correct index — it arrives only with the graded result, alongside
 * the explanation.
 */
export function TopicRunner({
  questions,
  backHref,
  topicLabel,
  topicTitle,
  courseName,
}: {
  questions: ApSessionQuestion[];
  backHref: string;
  topicLabel: string;
  topicTitle: string;
  courseName: string;
}) {
  const router = useRouter();
  const rootRef = useRef<HTMLDivElement>(null);

  // Resume where the student left off: the first never-answered question.
  const firstFresh = useMemo(() => {
    const i = questions.findIndex((q) => q.priorChoice === null);
    return i === -1 ? 0 : i;
  }, [questions]);

  const [index, setIndex] = useState(firstFresh);
  const [selected, setSelected] = useState<number | null>(null);
  const [marked, setMarked] = useState<Set<string>>(new Set());
  const [graded, setGraded] = useState<Record<string, Graded>>({});
  const [answeredOrder, setAnsweredOrder] = useState<string[]>([]);
  const [menuOpen, setMenuOpen] = useState(false);
  const [helpOpen, setHelpOpen] = useState(false);
  const [finished, setFinished] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [pending, start] = useTransition();

  const q = questions[index];
  const result = q ? (graded[q.id] ?? null) : null;
  const revealed = Boolean(result);

  // Session score counts only what was answered in this sitting.
  const sessionAnswered = answeredOrder.length;
  const sessionCorrect = answeredOrder.filter((id) => graded[id]?.isCorrect).length;

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
      // Fullscreen can be refused (permissions policy, an embedded frame).
      toast.error("Your browser wouldn't allow fullscreen here.");
    }
  }, []);

  const goTo = useCallback(
    (next: number) => {
      if (next < 0 || next >= questions.length) return;
      setIndex(next);
      setMenuOpen(false);
      // Restore the pick for a question already graded this session, so
      // jumping back shows what was chosen rather than an empty list.
      const target = questions[next];
      const g = graded[target.id];
      setSelected(g ? target.priorChoice : null);
    },
    [questions, graded],
  );

  function submit() {
    if (selected === null || revealed || !q) return;
    start(async () => {
      const res = await answerApQuestion({ questionId: q.id, chosenIndex: selected });
      if (res.error || res.correctIndex === undefined) {
        toast.error(res.error ?? "Something went wrong — try again.");
        return;
      }
      setGraded((prev) => ({
        ...prev,
        [q.id]: {
          correctIndex: res.correctIndex!,
          isCorrect: Boolean(res.isCorrect),
          explanation: res.explanation ?? null,
        },
      }));
      setAnsweredOrder((prev) => (prev.includes(q.id) ? prev : [...prev, q.id]));
    });
  }

  function toggleMark() {
    if (!q) return;
    setMarked((prev) => {
      const next = new Set(prev);
      if (next.has(q.id)) next.delete(q.id);
      else next.add(q.id);
      return next;
    });
  }

  // ---- Keyboard ------------------------------------------------------------
  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if (finished) return;
      const el = document.activeElement;
      if (el instanceof HTMLInputElement || el instanceof HTMLTextAreaElement) return;
      if (e.key === "Escape") {
        setMenuOpen(false);
        setHelpOpen(false);
        return;
      }
      if (menuOpen || helpOpen) return;
      if (e.key === "ArrowRight" && revealed && index + 1 < questions.length) goTo(index + 1);
      if (e.key === "ArrowLeft" && index > 0) goTo(index - 1);
      if (e.key === "Enter" && !revealed && selected !== null) submit();
      // Letter keys pick a choice, as in the practice test.
      if (!revealed && q) {
        const i = LETTERS.indexOf(e.key.toUpperCase());
        if (i !== -1 && i < q.choices.length) setSelected(i);
      }
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [index, revealed, selected, menuOpen, helpOpen, finished, q, questions.length]);

  // ---- Palette state -------------------------------------------------------
  const paletteStates: QuestionState[] = useMemo(
    () =>
      questions.map((item) => ({
        selectedChoiceId: graded[item.id] ? String(item.priorChoice ?? "answered") : null,
        freeResponseAnswer: "",
        flagged: marked.has(item.id),
        eliminated: [],
        timeSpentSeconds: 0,
        changedAnswerCount: 0,
      })),
    [questions, graded, marked],
  );

  const outcomes: QuestionOutcome[] = useMemo(
    () => questions.map((item) => (graded[item.id] ? (graded[item.id].isCorrect ? "correct" : "incorrect") : null)),
    [questions, graded],
  );

  if (finished || !q) {
    const pct = sessionAnswered ? Math.round((sessionCorrect / sessionAnswered) * 100) : 0;
    return (
      <div className="flex h-full flex-col items-center justify-center gap-4 bg-exam-bg px-6 text-center text-exam-text">
        <p className="text-[13px] font-medium uppercase tracking-[0.12em] text-exam-muted">
          Topic {topicLabel} complete
        </p>
        <p className="text-[44px] font-semibold tabular-nums leading-none">
          {sessionCorrect} / {sessionAnswered}
        </p>
        <p className="text-[15px] text-exam-muted">
          {pct}% correct in this session. Every answer is saved — your topic progress updates on the
          course page.
        </p>
        <div className="mt-3 flex flex-wrap justify-center gap-2">
          <NavButton variant="ghost" onClick={() => router.push(backHref)}>
            Back to the course
          </NavButton>
          <NavButton
            onClick={() => {
              setIndex(0);
              setSelected(null);
              setFinished(false);
            }}
          >
            Go through again
          </NavButton>
        </div>
      </div>
    );
  }

  const choices: TestingChoice[] = q.choices.map((content, i) => ({
    id: String(i),
    label: LETTERS[i],
    content,
  }));
  const isLast = index + 1 >= questions.length;

  return (
    <div ref={rootRef} className="flex h-full flex-col bg-exam-bg text-exam-text">
      <header className="shrink-0 border-b border-exam-border bg-exam-header">
        <div className="flex h-[62px] items-center gap-4 px-4">
          <div className="min-w-0 flex-1">
            <p className="truncate text-[15px] font-semibold leading-tight">{courseName}</p>
            <p className="truncate text-[12px] leading-tight text-exam-muted">
              {topicLabel} {topicTitle}
            </p>
          </div>

          <div className="hidden text-center sm:block">
            <p className="text-[15px] font-semibold tabular-nums leading-tight">
              {sessionCorrect}/{sessionAnswered}
            </p>
            <p className="text-[11px] leading-tight text-exam-muted">correct so far</p>
          </div>

          <div className="flex flex-1 items-center justify-end gap-0.5">
            <ToolButton icon={CircleHelp} label="Help" onClick={() => setHelpOpen(true)} />
            <ToolButton
              icon={isFullscreen ? Minimize2 : Maximize2}
              label={isFullscreen ? "Exit Full" : "Fullscreen"}
              active={isFullscreen}
              onClick={toggleFullscreen}
            />
            <button
              type="button"
              onClick={() => router.push(backHref)}
              title="Leave — every answer you have submitted is already saved"
              className={cn(
                "ml-1 rounded-full border border-exam-border bg-white px-3 py-1.5 text-[12px] font-medium text-exam-text transition-colors hover:bg-exam-hover",
                FOCUS_RING,
              )}
            >
              Exit
            </button>
          </div>
        </div>
      </header>

      <TestingBanner>AP practice — answers are graded as you go</TestingBanner>

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
                            {h}
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {q.table.rows.map((row, i) => (
                        <tr key={i}>
                          {row.map((cell, j) => (
                            <td key={j} className="border border-exam-border px-3 py-1.5">
                              {cell}
                            </td>
                          ))}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}

              <p className="text-[17px] leading-relaxed">{q.stem}</p>

              <div className="mt-5">
                <AnswerChoiceList
                  choices={choices}
                  selectedId={selected === null ? null : String(selected)}
                  correctId={result ? String(result.correctIndex) : null}
                  revealed={revealed}
                  onSelect={(id) => !revealed && setSelected(Number(id))}
                />
              </div>

              {result && (
                <div
                  className={cn(
                    "mt-6 rounded-lg border p-4",
                    result.isCorrect
                      ? "border-exam-correct/40 bg-exam-correct/10"
                      : "border-exam-border bg-white",
                  )}
                >
                  <p className="text-[14px] font-semibold">
                    {result.isCorrect
                      ? "Correct."
                      : `Not quite — the answer is ${LETTERS[result.correctIndex]}.`}
                  </p>
                  {result.explanation && (
                    <p className="mt-1.5 text-[14px] leading-relaxed text-exam-muted">
                      {result.explanation}
                    </p>
                  )}
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      <div className="relative shrink-0 border-t border-exam-border bg-exam-header">
        <div className="flex h-[54px] items-center px-4">
          <p className="hidden truncate text-[14px] font-medium sm:block sm:w-[26%]">
            {topicLabel} {topicTitle}
          </p>

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

          <div className="flex items-center justify-end gap-2 sm:w-[26%]">
            {index > 0 && (
              <NavButton variant="ghost" onClick={() => goTo(index - 1)}>
                Back
              </NavButton>
            )}
            {!revealed ? (
              <NavButton onClick={submit} disabled={selected === null || pending}>
                {pending ? (
                  <span className="flex items-center gap-1.5">
                    <Loader2 className="h-3.5 w-3.5 animate-spin" /> Checking
                  </span>
                ) : (
                  "Submit"
                )}
              </NavButton>
            ) : isLast ? (
              <NavButton onClick={() => setFinished(true)}>Finish topic</NavButton>
            ) : (
              <NavButton onClick={() => goTo(index + 1)}>Next Question</NavButton>
            )}
          </div>
        </div>

        <QuestionPalette
          open={menuOpen}
          onOpenChange={setMenuOpen}
          title={`${topicLabel} ${topicTitle} — ${questions.length} questions`}
          count={questions.length}
          currentIndex={index}
          states={paletteStates}
          outcomes={outcomes}
          onJump={goTo}
          onGoToReview={() => setFinished(true)}
          reviewLabel="Finish topic"
        />
      </div>

      {helpOpen && <ApHelpDialog onClose={() => setHelpOpen(false)} />}
    </div>
  );
}

function ApHelpDialog({ onClose }: { onClose: () => void }) {
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
        aria-label="Practice help"
        className="w-full max-w-md rounded-lg border border-exam-border bg-white p-5 text-exam-text shadow-xl"
      >
        <div className="flex items-start justify-between gap-4">
          <h2 className="text-[16px] font-semibold">Practising this topic</h2>
          <button
            type="button"
            onClick={onClose}
            aria-label="Close"
            className={cn("rounded p-1 hover:bg-exam-hover", FOCUS_RING)}
          >
            <X className="h-4 w-4" />
          </button>
        </div>
        <ul className="mt-3 space-y-2 text-[14px] leading-relaxed text-exam-muted">
          <li>
            Pick an answer and choose <strong className="text-exam-text">Submit</strong>. The
            explanation appears with the question still in front of you.
          </li>
          <li>
            <strong className="text-exam-text">Question {"{n}"} of {"{n}"}</strong> at the bottom
            opens the full list, so you can jump anywhere and see what you have answered.
          </li>
          <li>
            <strong className="text-exam-text">Mark for Review</strong> flags a question in that
            list without affecting your answer.
          </li>
          <li>
            Press <kbd className="rounded border border-exam-border px-1">A</kbd>–
            <kbd className="rounded border border-exam-border px-1">E</kbd> to choose,{" "}
            <kbd className="rounded border border-exam-border px-1">Enter</kbd> to submit, and the
            arrow keys to move between questions.
          </li>
          <li>Every submitted answer is saved. You can leave and pick up where you left off.</li>
        </ul>
      </div>
    </div>
  );
}
