"use client";

import {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
  useTransition,
  type CSSProperties,
  type KeyboardEvent as ReactKeyboardEvent,
  type MouseEvent as ReactMouseEvent,
} from "react";
import { useRouter } from "next/navigation";
import {
  Bookmark,
  Calculator as CalculatorIcon,
  Check,
  ChevronUp,
  CircleHelp,
  Highlighter,
  Loader2,
  Maximize2,
  Minimize2,
  Sigma,
  X,
} from "lucide-react";
import { toast } from "sonner";

import { MathContent, renderMathContent } from "@/components/shared/math-content";
import { CalculatorPanel } from "@/components/exam/calculator-panel";
import { HighlightableContent } from "@/components/exam/highlightable-content";
import { QuestionPalette, type QuestionOutcome } from "@/components/exam/question-palette";
import { ReferenceSheetDialog } from "@/components/exam/reference-sheet-dialog";
import { AnswerChoiceList, FreeResponseInput } from "@/components/testing/answer-choices";
import {
  FOCUS_RING,
  NavButton,
  QuestionNumberChip,
  TestingBanner,
  ToolButton,
} from "@/components/testing/primitives";
import { stemRegionId, type Annotation } from "@/lib/exam/annotations";
import { toPassageHtml } from "@/lib/exam/passage-html";
import {
  clearQbSession,
  readQbSession,
  sessionSignature,
  writeQbSession,
} from "@/lib/practice/qb-session-storage";
import { cn } from "@/lib/utils";
import { toggleBookmark } from "@/server/actions/student/bookmarks";
import { submitQuestionAnswer, type SubmitAnswerResult } from "@/server/actions/student/question-bank";
import type { QuestionState } from "@/types/exam";

export interface SessionQuestion {
  id: string;
  ref: string;
  subject: "READING_WRITING" | "MATH";
  type: "MULTIPLE_CHOICE" | "FREE_RESPONSE";
  difficulty: "EASY" | "MEDIUM" | "HARD";
  domainName: string;
  skillName: string;
  stem: string;
  imageUrl: string | null;
  passage: { id: string; title: string | null; content: string; imageUrl: string | null } | null;
  /** No `isCorrect` — the answer key never reaches the client before submission. */
  choices: { id: string; label: string; content: string }[];
  saved: boolean;
}

/** Everything the student has done to one question in this session. */
interface QbState {
  selectedChoiceId: string | null;
  freeResponseAnswer: string;
  eliminated: string[];
  marked: boolean;
  result: SubmitAnswerResult | null;
  secondsSpent: number;
}

const blank = (saved: boolean): QbState => ({
  selectedChoiceId: null,
  freeResponseAnswer: "",
  eliminated: [],
  marked: saved,
  result: null,
  secondsSpent: 0,
});

/**
 * Question Bank practice, running on the same testing chrome as a full practice
 * test: identical header, banner, split layout, answer choices, footer and
 * question navigator. The differences are the ones that make it *practice* --
 * no countdown, grading on submit, and an explanation panel.
 *
 * The rule that shapes the whole flow: submitting never moves the student on.
 * The question stays put, the outcome and explanation appear beneath it, and
 * only "Next Question" advances.
 *
 * The session also survives leaving: everything below is mirrored into
 * `localStorage` under the pinned question set, so reopening `sessionHref`
 * puts the student back on the question they were on with their answers,
 * eliminations and revealed explanations intact.
 */
export function PracticeSession({
  questions,
  backHref,
  sessionHref,
  studentName,
}: {
  questions: SessionQuestion[];
  backHref: string;
  /** The pinned URL that reopens exactly this set of questions. */
  sessionHref: string;
  studentName: string;
}) {
  const router = useRouter();
  const rootRef = useRef<HTMLDivElement>(null);
  const splitPaneRef = useRef<HTMLDivElement>(null);

  const [index, setIndex] = useState(0);
  const [states, setStates] = useState<QbState[]>(() => questions.map((q) => blank(q.saved)));
  const [menuOpen, setMenuOpen] = useState(false);
  const [calculatorOpen, setCalculatorOpen] = useState(false);
  const [referenceOpen, setReferenceOpen] = useState(false);
  const [crossOutEnabled, setCrossOutEnabled] = useState(false);
  const [helpOpen, setHelpOpen] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [finished, setFinished] = useState(false);
  const [annotations, setAnnotations] = useState<Annotation[]>([]);
  const [passageWidthPct, setPassageWidthPct] = useState<number | null>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [restored, setRestored] = useState(false);
  const [isPending, startTransition] = useTransition();
  const [isSaving, startSaving] = useTransition();

  const q = questions[index];
  const state = states[index];
  const result = state?.result ?? null;
  const revealed = !!result;
  const isLast = index === questions.length - 1;

  const patch = useCallback((changes: Partial<QbState>) => {
    setStates((prev) => prev.map((s, i) => (i === index ? { ...s, ...changes } : s)));
  }, [index]);

  // ---- Saving and resuming -------------------------------------------------
  // The signature identifies this exact question set. Restoring is gated on it
  // so a stored session can never paint one student's answers onto a different
  // set of questions.
  const signature = useMemo(() => sessionSignature(questions.map((x) => x.id)), [questions]);

  // Restore runs exactly once, guarded by a ref rather than by effect
  // dependencies. Every server action re-renders this page, which hands down a
  // fresh `questions` array; a dependency-driven effect would re-read storage
  // at that moment and could overwrite the answer that had just come back with
  // the pre-submit snapshot.
  const restoredRef = useRef(false);
  useEffect(() => {
    if (restoredRef.current) return;
    restoredRef.current = true;

    const stored = readQbSession();
    if (stored && stored.signature === signature && stored.states.length === questions.length) {
      // `marked` comes from the server on every load (bookmarks are real rows),
      // so the freshly-fetched value wins over the stored one.
      setStates(stored.states.map((s, i) => ({ ...s, marked: questions[i]?.saved ?? s.marked })));
      setIndex(stored.index);
      setPassageWidthPct(stored.splitPct);
    }
    setRestored(true);
  }, [signature, questions]);

  useEffect(() => {
    if (!restored) return;
    if (finished) {
      clearQbSession(signature);
      return;
    }
    // Debounced: the per-second timer touches `states` every tick, and there is
    // no reason to serialise the whole session that often.
    const id = setTimeout(() => {
      writeQbSession({
        version: 1,
        signature,
        href: sessionHref,
        label: `${questions[0]?.subject === "MATH" ? "Math" : "Reading and Writing"} — ${
          questions[0]?.domainName ?? "Question Bank"
        }`,
        index,
        total: questions.length,
        answered: states.filter((s) => s.result).length,
        correct: states.filter((s) => s.result?.isCorrect).length,
        splitPct: passageWidthPct,
        savedAt: new Date().toISOString(),
        states,
      });
    }, 400);
    return () => clearTimeout(id);
  }, [restored, finished, signature, sessionHref, questions, index, states, passageWidthPct]);

  // ---- Split pane ----------------------------------------------------------
  const SPLIT_MIN = 30;
  const SPLIT_MAX = 70;
  const SPLIT_DEFAULT = 55;

  const startDragging = useCallback((startEvent: ReactMouseEvent) => {
    startEvent.preventDefault();
    setIsDragging(true);
    function onMove(e: MouseEvent) {
      const el = splitPaneRef.current;
      if (!el) return;
      const rect = el.getBoundingClientRect();
      const pct = ((e.clientX - rect.left) / rect.width) * 100;
      setPassageWidthPct(Math.min(SPLIT_MAX, Math.max(SPLIT_MIN, pct)));
    }
    function onUp() {
      setIsDragging(false);
      window.removeEventListener("mousemove", onMove);
      window.removeEventListener("mouseup", onUp);
    }
    window.addEventListener("mousemove", onMove);
    window.addEventListener("mouseup", onUp);
  }, []);

  /** Arrow keys nudge the split, Home/End jump to the extremes — a drag handle
   *  that only responds to a mouse is unusable for keyboard-only students. */
  const nudgeSplit = useCallback((event: ReactKeyboardEvent) => {
    const STEP = 2;
    const current = passageWidthPct ?? SPLIT_DEFAULT;
    let next: number | null = null;
    if (event.key === "ArrowLeft") next = current - STEP;
    else if (event.key === "ArrowRight") next = current + STEP;
    else if (event.key === "Home") next = SPLIT_MIN;
    else if (event.key === "End") next = SPLIT_MAX;
    else if (event.key === "Enter" || event.key === " ") next = SPLIT_DEFAULT;
    if (next === null) return;
    event.preventDefault();
    // Stop here rather than bubbling: ArrowLeft/ArrowRight are also the
    // previous/next-question shortcuts.
    event.stopPropagation();
    setPassageWidthPct(Math.min(SPLIT_MAX, Math.max(SPLIT_MIN, next)));
  }, [passageWidthPct]);

  // Time on the current question, used only to record how long each took.
  useEffect(() => {
    if (finished) return;
    const id = setInterval(() => {
      setStates((prev) => prev.map((s, i) => (i === index ? { ...s, secondsSpent: s.secondsSpent + 1 } : s)));
    }, 1000);
    return () => clearInterval(id);
  }, [index, finished]);

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
      // The rest of the interface is unaffected, so just say so.
      toast.error("Your browser wouldn't allow fullscreen here.");
    }
  }, []);

  // ---- Answering -----------------------------------------------------------
  function submit() {
    if (!q || revealed || isPending) return;
    const answer = q.type === "FREE_RESPONSE" ? state.freeResponseAnswer.trim() : state.selectedChoiceId;
    if (!answer) return;

    const at = index;
    startTransition(async () => {
      try {
        const res = await submitQuestionAnswer({
          questionId: q.id,
          selectedChoiceId: q.type === "MULTIPLE_CHOICE" ? state.selectedChoiceId : null,
          freeResponseAnswer: q.type === "FREE_RESPONSE" ? state.freeResponseAnswer.trim() : null,
          timeSpentSeconds: state.secondsSpent,
        });
        // Written by index rather than through `patch`: the student may have
        // navigated while the request was in flight.
        setStates((prev) => prev.map((s, i) => (i === at ? { ...s, result: res } : s)));
      } catch {
        toast.error("Couldn't save that answer. Check your connection and try again.");
      }
    });
  }

  function goTo(next: number) {
    if (next < 0 || next >= questions.length) return;
    setIndex(next);
    setMenuOpen(false);
  }

  function onToggleMark() {
    if (!q) return;
    const optimistic = !state.marked;
    patch({ marked: optimistic });
    startSaving(async () => {
      try {
        await toggleBookmark(q.id);
      } catch {
        patch({ marked: !optimistic });
        toast.error("Couldn't update saved questions.");
      }
    });
  }

  // ---- Highlighting --------------------------------------------------------
  const addAnnotation = useCallback((a: Omit<Annotation, "id">) => {
    setAnnotations((prev) => [...prev, { ...a, id: crypto.randomUUID() }]);
  }, []);
  const updateAnnotation = useCallback((id: string, p: Partial<Annotation>) => {
    setAnnotations((prev) => prev.map((a) => (a.id === id ? { ...a, ...p } : a)));
  }, []);
  const removeAnnotation = useCallback((id: string) => {
    setAnnotations((prev) => prev.filter((a) => a.id !== id));
  }, []);

  const passageId = q?.passage?.id ?? null;
  const passageHtml = useMemo(() => (q?.passage ? toPassageHtml(q.passage.content) : ""), [q?.passage]);
  const passageAnnotations = useMemo(
    () => annotations.filter((a) => a.regionId === passageId).sort((a, b) => a.start - b.start),
    [annotations, passageId]
  );
  const stemId = q ? stemRegionId(q.id) : "";
  const stemHtml = useMemo(() => (q ? renderMathContent(q.stem) : ""), [q]);
  const stemAnnotations = useMemo(
    () => annotations.filter((a) => a.regionId === stemId).sort((a, b) => a.start - b.start),
    [annotations, stemId]
  );

  // ---- Navigator + scoring -------------------------------------------------
  const paletteStates: QuestionState[] = useMemo(
    () =>
      states.map((s) => ({
        selectedChoiceId: s.selectedChoiceId,
        freeResponseAnswer: s.freeResponseAnswer,
        flagged: s.marked,
        eliminated: s.eliminated,
        timeSpentSeconds: s.secondsSpent,
        changedAnswerCount: 0,
      })),
    [states]
  );
  const outcomes: QuestionOutcome[] = useMemo(
    () => states.map((s) => (s.result ? (s.result.isCorrect ? "correct" : "incorrect") : null)),
    [states]
  );
  const score = useMemo(() => {
    const answered = states.filter((s) => s.result).length;
    const correct = states.filter((s) => s.result?.isCorrect).length;
    return { answered, correct };
  }, [states]);

  // Keyboard: the same shortcuts as the exam, plus Enter to submit.
  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      const target = e.target as HTMLElement | null;
      if (target && ["INPUT", "TEXTAREA"].includes(target.tagName)) return;
      if (menuOpen || helpOpen || finished) return;
      // The split divider owns Arrow keys while focused (it resizes the panes).
      if (target?.getAttribute("role") === "separator") return;
      if (e.key === "ArrowRight" && revealed) goTo(index + 1);
      else if (e.key === "ArrowLeft") goTo(index - 1);
      else if (e.key === "Enter" && !revealed) submit();
      else if (["1", "2", "3", "4"].includes(e.key) && q?.type === "MULTIPLE_CHOICE" && !revealed) {
        const choice = q.choices[Number(e.key) - 1];
        if (choice) patch({ selectedChoiceId: choice.id });
      }
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [index, revealed, q, menuOpen, helpOpen, finished, state]);

  if (finished || !q) {
    const pct = score.answered ? Math.round((score.correct / score.answered) * 100) : 0;
    return (
      <div className="flex h-screen flex-col items-center justify-center gap-4 bg-exam-bg px-6 text-center text-exam-text">
        <p className="text-[13px] font-medium uppercase tracking-[0.12em] text-exam-muted">Session complete</p>
        <p className="text-[44px] font-semibold tabular-nums leading-none">
          {score.correct} / {score.answered}
        </p>
        <p className="text-[15px] text-exam-muted">{pct}% correct in this session.</p>
        <div className="mt-3 flex flex-wrap justify-center gap-2">
          <NavButton variant="ghost" onClick={() => router.push(backHref)}>
            Back to Question Bank
          </NavButton>
          <NavButton onClick={() => router.push("/practice/start")}>Practice more</NavButton>
        </div>
      </div>
    );
  }

  const canSubmit =
    q.type === "FREE_RESPONSE" ? !!state.freeResponseAnswer.trim() : !!state.selectedChoiceId;

  const questionPanel = (
    <div className="flex h-full flex-col">
      {/* Question header band — same treatment as the practice test. */}
      <div className="shrink-0 border-b border-exam-border bg-exam-header px-6 py-1.5 lg:px-10">
        <div className="flex items-center gap-3">
          <QuestionNumberChip n={index + 1} />
          <span className="sr-only">
            Question {index + 1} of {questions.length}
          </span>
          <button
            type="button"
            onClick={onToggleMark}
            disabled={isSaving}
            aria-pressed={state.marked}
            className={cn(
              "flex items-center gap-1.5 rounded px-1 py-0.5 text-[13px] font-medium text-exam-text transition-colors hover:bg-exam-hover",
              FOCUS_RING
            )}
          >
            <Bookmark className={cn("h-4 w-4", state.marked ? "fill-exam-flag text-exam-flag" : "text-exam-muted")} />
            {state.marked ? "Marked for Review" : "Mark for Review"}
          </button>

          <span className="ml-auto flex items-center gap-2">
            <span className="hidden text-[12px] text-exam-muted sm:inline">{q.skillName}</span>
            <span className="rounded-[3px] border border-exam-border bg-white px-1.5 py-0.5 text-[11px] font-semibold uppercase tracking-wide text-exam-muted">
              {q.difficulty}
            </span>
            {q.type === "MULTIPLE_CHOICE" && !revealed && (
              <button
                type="button"
                onClick={() => setCrossOutEnabled((v) => !v)}
                aria-pressed={crossOutEnabled}
                title={crossOutEnabled ? "Hide answer eliminator" : "Show answer eliminator"}
                className={cn(
                  "flex h-[26px] items-center rounded-[3px] border px-2 text-[12px] font-semibold tracking-tight transition-colors",
                  FOCUS_RING,
                  crossOutEnabled
                    ? "border-exam-blue bg-exam-blue text-white"
                    : "border-exam-text bg-transparent text-exam-text hover:bg-exam-hover"
                )}
              >
                <span className="line-through">ABC</span>
              </button>
            )}
          </span>
        </div>
      </div>

      <div className="min-h-0 flex-1 overflow-y-auto exam-scroll px-6 pb-14 pt-6 lg:px-10">
        <div className={q.subject === "MATH" ? "mx-auto max-w-[46rem]" : undefined}>
          <HighlightableContent
            regionId={stemId}
            html={stemHtml}
            annotations={stemAnnotations}
            onCreate={addAnnotation}
            onUpdate={updateAnnotation}
            onRemove={removeAnnotation}
            ariaLabel="Question"
            className="exam-stem block text-[16px] leading-[1.6]"
          />

          {q.imageUrl && q.subject === "MATH" && (
            // eslint-disable-next-line @next/next/no-img-element
            <img
              src={q.imageUrl}
              alt="Question figure"
              className="mt-4 max-w-full rounded border border-exam-border bg-white"
            />
          )}

          <div className="mt-5">
            {q.type === "MULTIPLE_CHOICE" ? (
              <AnswerChoiceList
                choices={q.choices}
                selectedId={state.selectedChoiceId}
                eliminatedIds={state.eliminated}
                crossOutEnabled={crossOutEnabled}
                correctId={result?.correctChoiceId ?? null}
                revealed={revealed}
                onSelect={(id) => patch({ selectedChoiceId: id })}
                onToggleEliminate={(id) =>
                  patch({
                    eliminated: state.eliminated.includes(id)
                      ? state.eliminated.filter((x) => x !== id)
                      : [...state.eliminated, id],
                  })
                }
              />
            ) : (
              <FreeResponseInput
                value={state.freeResponseAnswer}
                disabled={revealed}
                onChange={(v) => patch({ freeResponseAnswer: v })}
              />
            )}
          </div>

          {result && <ExplanationPanel result={result} questionType={q.type} />}
        </div>
      </div>
    </div>
  );

  return (
    <div ref={rootRef} className="flex h-screen flex-col bg-exam-bg text-exam-text">
      <QbHeader
        domainName={q.domainName}
        subject={q.subject}
        answered={score.answered}
        correct={score.correct}
        calculatorOpen={calculatorOpen}
        onToggleCalculator={() => setCalculatorOpen((v) => !v)}
        onOpenReference={() => setReferenceOpen(true)}
        onOpenHelp={() => setHelpOpen(true)}
        isFullscreen={isFullscreen}
        onToggleFullscreen={toggleFullscreen}
        onExit={() => router.push(backHref)}
      />

      <TestingBanner>Question Bank practice</TestingBanner>

      <div className="flex-1 overflow-hidden">
        {q.subject === "READING_WRITING" && q.passage ? (
          <div
            ref={splitPaneRef}
            className="grid h-full grid-rows-[42vh_auto_1fr] overflow-hidden lg:grid-cols-[var(--passage-w,55%)_auto_1fr] lg:grid-rows-1"
            style={passageWidthPct ? ({ "--passage-w": `${passageWidthPct}%` } as CSSProperties) : undefined}
          >
            <div className="min-h-0 border-b border-exam-border bg-exam-passage lg:border-b-0">
              <div className="h-full overflow-y-auto exam-scroll px-6 pb-14 pt-8 lg:px-10">
                <div className="max-w-[44rem]">
                  {q.passage.imageUrl && (
                    // eslint-disable-next-line @next/next/no-img-element
                    <img
                      src={q.passage.imageUrl}
                      alt=""
                      className="mb-4 max-w-full rounded border border-exam-border bg-white"
                    />
                  )}
                  <HighlightableContent
                    regionId={q.passage.id}
                    html={passageHtml}
                    annotations={passageAnnotations}
                    onCreate={addAnnotation}
                    onUpdate={updateAnnotation}
                    onRemove={removeAnnotation}
                    ariaLabel="Passage"
                    className="exam-passage text-[16px] leading-[1.7]"
                  />
                </div>
              </div>
            </div>

            <div
              onMouseDown={startDragging}
              onKeyDown={nudgeSplit}
              onDoubleClick={() => setPassageWidthPct(SPLIT_DEFAULT)}
              role="separator"
              tabIndex={0}
              aria-orientation="vertical"
              aria-label="Resize the passage and question panels"
              aria-valuemin={SPLIT_MIN}
              aria-valuemax={SPLIT_MAX}
              aria-valuenow={Math.round(passageWidthPct ?? SPLIT_DEFAULT)}
              title="Drag to resize — double-click to reset"
              className={cn(
                "group relative hidden lg:flex lg:h-full lg:w-[9px] lg:cursor-col-resize lg:items-center lg:justify-center",
                "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-exam-blue",
                isDragging ? "bg-exam-blue/15" : "bg-transparent"
              )}
            >
              <span
                className={cn(
                  "absolute inset-y-0 left-1/2 w-px -translate-x-1/2",
                  isDragging ? "bg-exam-blue" : "bg-exam-divider group-hover:bg-exam-disabled"
                )}
              />
              <span
                className={cn(
                  "relative h-9 w-[5px] rounded-full transition-colors",
                  isDragging ? "bg-exam-blue" : "bg-exam-divider group-hover:bg-exam-disabled"
                )}
              />
            </div>

            <div className="min-h-0 bg-exam-question">{questionPanel}</div>
          </div>
        ) : (
          <div className="h-full bg-exam-question">{questionPanel}</div>
        )}
      </div>

      {/* Bottom navigation — same bar as the practice test. */}
      <div className="relative shrink-0 border-t border-exam-border bg-exam-header">
        <div className="flex h-[54px] items-center px-4">
          <p className="hidden truncate text-[14px] font-medium sm:block sm:w-[26%]">{studentName}</p>

          <div className="flex flex-1 justify-center">
            <button
              type="button"
              onClick={() => setMenuOpen((v) => !v)}
              aria-expanded={menuOpen}
              className={cn(
                "flex h-[34px] items-center gap-1.5 rounded-md bg-exam-strip px-4 text-[13px] font-medium text-white transition-colors hover:bg-exam-strip/90",
                FOCUS_RING
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
              <NavButton onClick={submit} disabled={!canSubmit || isPending}>
                {isPending ? (
                  <span className="flex items-center gap-1.5">
                    <Loader2 className="h-3.5 w-3.5 animate-spin" /> Checking
                  </span>
                ) : (
                  "Submit"
                )}
              </NavButton>
            ) : isLast ? (
              <NavButton onClick={() => setFinished(true)}>Finish session</NavButton>
            ) : (
              <NavButton onClick={() => goTo(index + 1)}>Next Question</NavButton>
            )}
          </div>
        </div>

        <QuestionPalette
          open={menuOpen}
          onOpenChange={setMenuOpen}
          title={`${q.domainName} — ${questions.length} questions`}
          count={questions.length}
          currentIndex={index}
          states={paletteStates}
          outcomes={outcomes}
          onJump={goTo}
          onGoToReview={() => setFinished(true)}
          reviewLabel="Finish session"
        />
      </div>

      {q.subject === "MATH" && (
        <>
          {calculatorOpen && <CalculatorPanel onClose={() => setCalculatorOpen(false)} />}
          <ReferenceSheetDialog open={referenceOpen} onOpenChange={setReferenceOpen} />
        </>
      )}

      {helpOpen && <QbHelpDialog onClose={() => setHelpOpen(false)} />}
    </div>
  );
}

/**
 * The outcome and explanation, shown in place under the answers. Never a
 * separate page: the point is to read the explanation with the question and
 * the choices still in front of you.
 */
function ExplanationPanel({
  result,
  questionType,
}: {
  result: SubmitAnswerResult;
  questionType: SessionQuestion["type"];
}) {
  return (
    <section
      aria-label="Result and explanation"
      className={cn(
        "mt-6 rounded-lg border-2",
        result.isCorrect ? "border-exam-correct bg-exam-correctSoft" : "border-exam-incorrect bg-exam-incorrectSoft"
      )}
    >
      <div className="flex items-center gap-2 border-b border-exam-divider px-4 py-3">
        <span
          className={cn(
            "flex h-6 w-6 items-center justify-center rounded-full text-white",
            result.isCorrect ? "bg-exam-correct" : "bg-exam-incorrect"
          )}
        >
          {result.isCorrect ? <Check className="h-4 w-4" /> : <X className="h-4 w-4" />}
        </span>
        <p className={cn("text-[15px] font-semibold", result.isCorrect ? "text-exam-correct" : "text-exam-incorrect")}>
          {result.isCorrect ? "Correct" : "Incorrect"}
        </p>
      </div>

      <div className="space-y-3 bg-white px-4 py-4">
        {!result.isCorrect && questionType === "FREE_RESPONSE" && result.correctAnswerFR?.length ? (
          <p className="text-[14px]">
            <span className="text-exam-muted">Correct answer: </span>
            <span className="font-semibold">{result.correctAnswerFR.join(" or ")}</span>
          </p>
        ) : null}

        <div>
          <p className="text-[12px] font-semibold uppercase tracking-[0.08em] text-exam-muted">Explanation</p>
          {result.explanationHtml ? (
            <MathContent html={result.explanationHtml} className="mt-1.5 text-[15px] leading-[1.7] text-exam-text" />
          ) : (
            <p className="mt-1.5 text-[14px] text-exam-muted">
              This question doesn&apos;t have a written explanation yet.
            </p>
          )}
        </div>
      </div>
    </section>
  );
}

function QbHeader({
  domainName,
  subject,
  answered,
  correct,
  calculatorOpen,
  onToggleCalculator,
  onOpenReference,
  onOpenHelp,
  isFullscreen,
  onToggleFullscreen,
  onExit,
}: {
  domainName: string;
  subject: SessionQuestion["subject"];
  answered: number;
  correct: number;
  calculatorOpen: boolean;
  onToggleCalculator: () => void;
  onOpenReference: () => void;
  onOpenHelp: () => void;
  isFullscreen: boolean;
  onToggleFullscreen: () => void;
  onExit: () => void;
}) {
  return (
    <header className="shrink-0 border-b border-exam-border bg-exam-header">
      <div className="flex h-[62px] items-center gap-4 px-4">
        <div className="min-w-0 flex-1">
          <p className="truncate text-[15px] font-semibold leading-tight">
            Question Bank: {subject === "MATH" ? "Math" : "Reading and Writing"}
          </p>
          <p className="truncate text-[12px] leading-tight text-exam-muted">{domainName}</p>
        </div>

        <div className="hidden text-center sm:block">
          <p className="text-[15px] font-semibold tabular-nums leading-tight">
            {correct}/{answered}
          </p>
          <p className="text-[11px] leading-tight text-exam-muted">correct so far</p>
        </div>

        <div className="flex flex-1 items-center justify-end gap-0.5">
          {subject === "MATH" && (
            <>
              <ToolButton
                icon={CalculatorIcon}
                label="Calculator"
                active={calculatorOpen}
                onClick={onToggleCalculator}
              />
              <ToolButton icon={Sigma} label="Reference" onClick={onOpenReference} />
            </>
          )}
          <ToolButton icon={Highlighter} label="Highlights" onClick={onOpenHelp} />
          <ToolButton icon={CircleHelp} label="Help" onClick={onOpenHelp} />
          <ToolButton
            icon={isFullscreen ? Minimize2 : Maximize2}
            label={isFullscreen ? "Exit Full" : "Fullscreen"}
            active={isFullscreen}
            onClick={onToggleFullscreen}
          />
          <button
            type="button"
            onClick={onExit}
            title="Leave — your place in this session is kept"
            className={cn(
              "ml-1 rounded-full border border-exam-border bg-white px-3 py-1.5 text-[12px] font-medium text-exam-text transition-colors hover:bg-exam-hover",
              FOCUS_RING
            )}
          >
            Exit
          </button>
        </div>
      </div>
    </header>
  );
}

function QbHelpDialog({ onClose }: { onClose: () => void }) {
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if (e.key === "Escape") onClose();
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/30 px-4" onMouseDown={onClose}>
      <div
        role="dialog"
        aria-label="Question Bank help"
        onMouseDown={(e) => e.stopPropagation()}
        className="w-full max-w-[440px] rounded-md border border-exam-border bg-white p-5 shadow-examPopup"
      >
        <div className="flex items-start justify-between gap-4">
          <h2 className="text-[16px] font-semibold">Practising in the Question Bank</h2>
          <button
            type="button"
            onClick={onClose}
            aria-label="Close"
            className="flex h-6 w-6 items-center justify-center rounded text-exam-muted hover:bg-exam-hover"
          >
            <X className="h-4 w-4" />
          </button>
        </div>
        <ul className="mt-3 space-y-2 text-[14px] leading-[1.6] text-exam-text">
          <li>Answer, then press <strong>Submit</strong>. The question stays on screen with the explanation.</li>
          <li><strong>Next Question</strong> moves on — nothing advances by itself.</li>
          <li>Drag across the passage or the question to highlight it.</li>
          <li>Drag the divider between the two panels to resize them — double-click it to reset.</li>
          <li>
            Your place is saved as you go. Leaving and coming back to the Question Bank offers to{" "}
            <strong>continue this session</strong>.
          </li>
          <li>Math questions have <strong>Calculator</strong> (Desmos) and the <strong>Reference</strong> sheet.</li>
          <li>Keys: <strong>1–4</strong> pick a choice, <strong>Enter</strong> submits, <strong>←/→</strong> move.</li>
        </ul>
      </div>
    </div>
  );
}
