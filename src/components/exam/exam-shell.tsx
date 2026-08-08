"use client";

import {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
  useTransition,
  type CSSProperties,
  type ComponentType,
  type KeyboardEvent as ReactKeyboardEvent,
  type MouseEvent as ReactMouseEvent,
  type ReactNode,
} from "react";
import { useRouter } from "next/navigation";
import {
  Bookmark,
  Calculator,
  ChevronDown,
  ChevronUp,
  CircleHelp,
  Clock,
  Highlighter,
  LogOut,
  Maximize,
  Minimize,
  Minus,
  MoreHorizontal,
  Plus,
  Ruler,
  ScanLine,
  Trash2,
  TriangleAlert,
  X,
} from "lucide-react";
import { toast } from "sonner";

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { CalculatorPanel } from "@/components/exam/calculator-panel";
import { BreakScreen, ModuleOverScreen, PreparingScreen } from "@/components/exam/exam-interstitials";
import { HighlightableContent } from "@/components/exam/highlightable-content";
import { LineReader } from "@/components/exam/line-reader";
import { QuestionGrid, QuestionLegend, QuestionPalette } from "@/components/exam/question-palette";
import { ReferenceSheetDialog } from "@/components/exam/reference-sheet-dialog";
import { MathContent, renderMathContent } from "@/components/shared/math-content";
import { AnswerChoiceList, FreeResponseInput } from "@/components/testing/answer-choices";
import { FOCUS_RING, NavButton, QuestionNumberChip, TestingBanner, ToolButton } from "@/components/testing/primitives";
import { cn } from "@/lib/utils";
import { stemRegionId, type Annotation } from "@/lib/exam/annotations";
import { toPassageHtml } from "@/lib/exam/passage-html";
import { useEscape } from "@/lib/exam/use-escape";
import { autosaveResponses, submitModule } from "@/server/actions/student/attempts";
import type { ExamModule, ExistingResponse, QuestionState } from "@/types/exam";

const DIRECTIONS: Record<ExamModule["subject"], string[]> = {
  READING_WRITING: [
    "The questions in this section address a number of important reading and writing skills. Each question includes one or more passages, which may include a table or graph. Read each passage and question carefully, and then choose the best answer to the question based on the passage(s).",
    "All questions in this section are multiple-choice with four answer choices. Each question has a single best answer.",
  ],
  MATH: [
    "The questions in this section address a number of important math skills. Use of a calculator is permitted for all questions. A reference sheet, calculator, and these directions can be accessed throughout the test.",
    "Unless otherwise indicated: all variables and expressions represent real numbers, figures provided are drawn to scale, all figures lie in a plane, and the domain of a given function f is the set of all real numbers x for which f(x) is a real number.",
  ],
};

/** Minutes are padded, so 7:23 reads as 07:23. */
function formatClock(totalSeconds: number): string {
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  return `${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
}

/** Spoken form for the screen-reader announcements the clock makes at each threshold. */
function spokenClock(totalSeconds: number): string {
  const minutes = Math.round(totalSeconds / 60);
  return minutes === 1 ? "1 minute remaining" : `${minutes} minutes remaining`;
}

const WARNING_AT_SECONDS = 5 * 60;
const CRITICAL_AT_SECONDS = 60;

/** Thresholds that get an audible/announced callout, longest first. */
const TIMER_ANNOUNCEMENTS = [WARNING_AT_SECONDS, CRITICAL_AT_SECONDS];

function buildInitialStates(module: ExamModule, existing: ExistingResponse[]): QuestionState[] {
  const byId = new Map(existing.map((r) => [r.questionId, r]));
  return module.questions.map((q) => {
    const r = byId.get(q.id);
    return {
      selectedChoiceId: r?.selectedChoiceId ?? null,
      freeResponseAnswer: r?.freeResponseAnswer ?? "",
      flagged: r?.flagged ?? false,
      eliminated: r?.eliminatedChoiceIds ?? [],
      timeSpentSeconds: r?.timeSpentSeconds ?? 0,
      changedAnswerCount: r?.changedAnswerCount ?? 0,
    };
  });
}

type Phase = "preparing" | "testing" | "module-over" | "break";

export function ExamShell({
  attemptId,
  studentName,
  moduleAttemptId,
  module,
  startedAt,
  existingResponses,
  showPreparing = false,
}: {
  attemptId: string;
  studentName: string;
  moduleAttemptId: string;
  module: ExamModule;
  startedAt: Date;
  existingResponses: ExistingResponse[];
  /** First module of a fresh attempt — show the "preparing your test" curtain. */
  showPreparing?: boolean;
}) {
  const router = useRouter();
  const rootRef = useRef<HTMLDivElement>(null);
  // Which whole-screen state the shell is in. Everything except "testing" is an
  // interstitial that replaces the module entirely -- see exam-interstitials.
  const [phase, setPhase] = useState<Phase>(showPreparing ? "preparing" : "testing");
  const [pendingBreak, setPendingBreak] = useState<string | null>(null);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [states, setStates] = useState<QuestionState[]>(() => buildInitialStates(module, existingResponses));
  const [currentIndex, setCurrentIndex] = useState(0);
  const [menuOpen, setMenuOpen] = useState(false);
  const [calculatorOpen, setCalculatorOpen] = useState(false);
  const [referenceOpen, setReferenceOpen] = useState(false);
  const [reviewPage, setReviewPage] = useState(false);
  const [directionsOpen, setDirectionsOpen] = useState(false);
  const [helpOpen, setHelpOpen] = useState(false);
  const [lineReaderOpen, setLineReaderOpen] = useState(false);
  const [timerHidden, setTimerHidden] = useState(false);
  const [crossOutEnabled, setCrossOutEnabled] = useState(false);
  const [zoomPct, setZoomPct] = useState(100);
  const [passageWidthPct, setPassageWidthPct] = useState<number | null>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [isSubmitting, startSubmit] = useTransition();
  const splitPaneRef = useRef<HTMLDivElement>(null);

  const sectionNumber = module.subject === "READING_WRITING" ? 1 : 2;
  const subjectLabel = module.subject === "READING_WRITING" ? "Reading and Writing" : "Math";
  const sectionTitle = `Section ${sectionNumber}, Module ${module.order}: ${subjectLabel}`;

  // ---- Annotations (Highlights & Notes) ------------------------------------
  // Kept in the browser rather than the database: they're scratch work for one
  // sitting, and the real test likewise discards them when the module ends.
  // They do survive a refresh, which is the case that actually matters.
  // `:2` because annotations are now keyed by region (passage *or* stem) —
  // entries written by the previous shape would land on the wrong offsets.
  const storageKey = `satforge-annotations:2:${moduleAttemptId}`;
  const [annotations, setAnnotations] = useState<Annotation[]>([]);
  const [annotationsHydrated, setAnnotationsHydrated] = useState(false);
  const [notesPanelOpen, setNotesPanelOpen] = useState(false);

  useEffect(() => {
    try {
      const raw = window.localStorage.getItem(storageKey);
      if (raw) setAnnotations(JSON.parse(raw) as Annotation[]);
    } catch {
      // Corrupt or unavailable storage just means starting with none.
    }
    setAnnotationsHydrated(true);
  }, [storageKey]);

  useEffect(() => {
    if (!annotationsHydrated) return;
    try {
      window.localStorage.setItem(storageKey, JSON.stringify(annotations));
    } catch {
      // Quota or private-mode failures are not worth interrupting a test for.
    }
  }, [annotations, annotationsHydrated, storageKey]);

  const addAnnotation = useCallback((a: Omit<Annotation, "id">) => {
    setAnnotations((prev) => [...prev, { ...a, id: crypto.randomUUID() }]);
  }, []);
  const updateAnnotation = useCallback((id: string, patch: Partial<Annotation>) => {
    setAnnotations((prev) => prev.map((a) => (a.id === id ? { ...a, ...patch } : a)));
  }, []);
  const removeAnnotation = useCallback((id: string) => {
    setAnnotations((prev) => prev.filter((a) => a.id !== id));
  }, []);

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

  // ---- Countdown -----------------------------------------------------------
  // Derived from the server-issued `startedAt` on every tick rather than
  // decremented, so the clock is correct after a refresh, after the tab is
  // backgrounded (browsers throttle intervals to once a minute there, which
  // would otherwise make the timer run slow), and after the machine sleeps.
  const deadlineMs = useMemo(
    () => new Date(startedAt).getTime() + module.timeLimitMinutes * 60_000,
    [startedAt, module.timeLimitMinutes]
  );
  const readClock = useCallback(
    () => Math.max(Math.ceil((deadlineMs - Date.now()) / 1000), 0),
    [deadlineMs]
  );
  const [secondsRemaining, setSecondsRemaining] = useState(readClock);

  const question = module.questions[currentIndex];
  const dirtyRef = useRef(false);
  const statesRef = useRef(states);
  statesRef.current = states;

  // Per-question elapsed time.
  useEffect(() => {
    if (reviewPage) return;
    const interval = setInterval(() => {
      setStates((prev) =>
        prev.map((s, i) => (i === currentIndex ? { ...s, timeSpentSeconds: s.timeSpentSeconds + 1 } : s))
      );
      dirtyRef.current = true;
    }, 1000);
    return () => clearInterval(interval);
  }, [currentIndex, reviewPage]);

  // Module countdown. Re-reads the wall clock each tick (see readClock) and
  // also on wake-up, so a throttled or suspended tab catches up immediately
  // instead of silently handing the student extra time.
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

  // Announce the low-time thresholds once each, for students who have the
  // timer hidden or are using a screen reader.
  const announcedRef = useRef<number[]>([]);
  const [timerAnnouncement, setTimerAnnouncement] = useState("");
  useEffect(() => {
    for (const threshold of TIMER_ANNOUNCEMENTS) {
      if (secondsRemaining <= threshold && !announcedRef.current.includes(threshold)) {
        announcedRef.current.push(threshold);
        setTimerAnnouncement(spokenClock(threshold));
      }
    }
  }, [secondsRemaining]);

  const persist = useCallback(async () => {
    if (!dirtyRef.current) return;
    dirtyRef.current = false;
    const payload = module.questions.map((q, i) => ({
      questionId: q.id,
      selectedChoiceId: statesRef.current[i].selectedChoiceId,
      freeResponseAnswer: statesRef.current[i].freeResponseAnswer || null,
      timeSpentSeconds: statesRef.current[i].timeSpentSeconds,
      flagged: statesRef.current[i].flagged,
      changedAnswerCount: statesRef.current[i].changedAnswerCount,
      eliminatedChoiceIds: statesRef.current[i].eliminated,
    }));
    await autosaveResponses(attemptId, moduleAttemptId, payload);
  }, [attemptId, moduleAttemptId, module.questions]);

  // Autosave every 5 seconds, plus immediately after any answer change.
  useEffect(() => {
    const interval = setInterval(persist, 5000);
    return () => clearInterval(interval);
  }, [persist]);

  // Flush the moment the tab is hidden or the page is being torn down. Without
  // this, up to 5 seconds of answers — and every flag/cross-out, which don't
  // trigger their own save — die with the tab.
  useEffect(() => {
    function flushIfHidden() {
      if (document.visibilityState === "hidden") void persist();
    }
    document.addEventListener("visibilitychange", flushIfHidden);
    window.addEventListener("pagehide", persist);
    return () => {
      document.removeEventListener("visibilitychange", flushIfHidden);
      window.removeEventListener("pagehide", persist);
    };
  }, [persist]);

  // Reloading or closing mid-module is recoverable (answers and the clock are
  // both server-side), but it is almost never what the student meant — make
  // the browser ask. Suppressed once the module is on its way out, so
  // submitting doesn't trip its own warning.
  const submittingRef = useRef(false);
  useEffect(() => {
    function onBeforeUnload(e: BeforeUnloadEvent) {
      if (submittingRef.current) return;
      void persist();
      e.preventDefault();
      e.returnValue = "";
    }
    window.addEventListener("beforeunload", onBeforeUnload);
    return () => window.removeEventListener("beforeunload", onBeforeUnload);
  }, [persist]);

  useEffect(() => {
    if (secondsRemaining === 0) {
      handleEndModule();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [secondsRemaining]);

  // Keep isFullscreen in sync when the student exits via Esc or browser chrome
  // instead of the toggle button.
  useEffect(() => {
    function onFullscreenChange() {
      setIsFullscreen(document.fullscreenElement === rootRef.current);
    }
    document.addEventListener("fullscreenchange", onFullscreenChange);
    return () => document.removeEventListener("fullscreenchange", onFullscreenChange);
  }, []);

  async function toggleFullscreen() {
    if (document.fullscreenElement) {
      await document.exitFullscreen();
    } else {
      await rootRef.current?.requestFullscreen();
    }
  }

  function updateCurrent(patch: Partial<QuestionState>) {
    setStates((prev) => prev.map((s, i) => (i === currentIndex ? { ...s, ...patch } : s)));
    dirtyRef.current = true;
  }

  function selectChoice(choiceId: string) {
    const current = states[currentIndex];
    const changed = current.selectedChoiceId && current.selectedChoiceId !== choiceId;
    updateCurrent({
      selectedChoiceId: choiceId,
      changedAnswerCount: changed ? current.changedAnswerCount + 1 : current.changedAnswerCount,
    });
    void persist();
  }

  function toggleEliminated(choiceId: string) {
    const current = states[currentIndex];
    const eliminated = current.eliminated.includes(choiceId)
      ? current.eliminated.filter((id) => id !== choiceId)
      : [...current.eliminated, choiceId];
    updateCurrent({ eliminated });
    void persist();
  }

  function toggleFlag() {
    updateCurrent({ flagged: !states[currentIndex].flagged });
    // Saved immediately, not on the 5s tick: "Mark for Review" is exactly the
    // state a student expects to survive a stray refresh.
    void persist();
  }

  function goTo(index: number) {
    if (index < 0 || index >= module.questions.length) return;
    setReviewPage(false);
    setCurrentIndex(index);
  }

  function goNext() {
    if (currentIndex < module.questions.length - 1) goTo(currentIndex + 1);
    else setReviewPage(true);
  }

  async function handleEndModule() {
    // The countdown timer below calls this unconditionally the instant it
    // hits zero, with no awareness of a manual "End Module" click already in
    // flight — guard here so that race can't submit the module twice.
    if (isSubmitting || submittingRef.current) return;
    submittingRef.current = true; // also silences the beforeunload guard
    // Take the module off screen *before* the round-trip. Submitting is slow
    // enough that leaving the questions up invites clicks on controls whose
    // answers are already sealed.
    setPhase("module-over");
    startSubmit(async () => {
      try {
        await persist();
        const result = await submitModule(attemptId, moduleAttemptId);
        try {
          window.localStorage.removeItem(storageKey);
        } catch {
          // Non-fatal.
        }
        if (result.finished) {
          router.push(`/review/${attemptId}`);
          return;
        }
        if (result.breakBefore) {
          // Crossing into a new section: hold at the break and let the student
          // start the next module's clock themselves.
          setPendingBreak(result.nextSubjectLabel ?? "The next section");
          setPhase("break");
          return;
        }
        // Same section — move straight on, no student action needed.
        router.refresh();
      } catch (error) {
        console.error("Failed to submit module", error);
        // Re-arm: the student is still in the module, so a stray reload should
        // warn again and a retry should be allowed.
        submittingRef.current = false;
        setPhase("testing");
        toast.error("Couldn't submit the module — check your connection and try again.");
      }
    });
  }

  // Keyboard shortcuts: arrows to move, digits to pick a choice, F to flag.
  // Suppressed while typing, and while a popup owns the screen.
  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      const target = e.target as HTMLElement | null;
      if (target && ["INPUT", "TEXTAREA"].includes(target.tagName)) return;
      if (menuOpen || directionsOpen || helpOpen) return;
      // The split divider owns Arrow keys while focused (it resizes the panes).
      if (target?.getAttribute("role") === "separator") return;

      if (e.key === "ArrowRight") {
        e.preventDefault();
        if (!reviewPage) goNext();
      } else if (e.key === "ArrowLeft") {
        e.preventDefault();
        if (reviewPage) setReviewPage(false);
        else goTo(currentIndex - 1);
      } else if (reviewPage) {
        return;
      } else if (e.key.toLowerCase() === "f") {
        toggleFlag();
      } else if (["1", "2", "3", "4"].includes(e.key) && question?.type === "MULTIPLE_CHOICE") {
        const choice = question.choices[Number(e.key) - 1];
        if (choice) selectChoice(choice.id);
      }
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [currentIndex, reviewPage, question, menuOpen, directionsOpen, helpOpen]);

  const answeredCount = useMemo(
    () => states.filter((s) => s.selectedChoiceId || s.freeResponseAnswer).length,
    [states]
  );

  // Each readable region gets its own annotation slice and its own final HTML.
  // The HTML is memoised because HighlightableContent repaints whenever the
  // string identity changes, and repainting drops any in-progress selection.
  const passageId = question?.passage?.id ?? null;
  const passageAnnotations = useMemo(
    () => annotations.filter((a) => a.regionId === passageId).sort((a, b) => a.start - b.start),
    [annotations, passageId]
  );
  const passageHtml = useMemo(
    () => (question?.passage ? toPassageHtml(question.passage.content) : ""),
    [question?.passage]
  );

  const stemId = question ? stemRegionId(question.id) : "";
  const stemAnnotations = useMemo(
    () => annotations.filter((a) => a.regionId === stemId).sort((a, b) => a.start - b.start),
    [annotations, stemId]
  );
  const stemHtml = useMemo(() => (question ? renderMathContent(question.stem) : ""), [question]);

  const header = (
    <ExamHeader
      sectionTitle={sectionTitle}
      subject={module.subject}
      secondsRemaining={secondsRemaining}
      timerHidden={timerHidden}
      onToggleTimer={() => setTimerHidden((v) => !v)}
      onOpenDirections={() => setDirectionsOpen(true)}
      onOpenHelp={() => setHelpOpen(true)}
      onToggleCalculator={() => setCalculatorOpen((v) => !v)}
      onOpenReference={() => setReferenceOpen(true)}
      calculatorOpen={calculatorOpen}
      zoomPct={zoomPct}
      onZoomChange={setZoomPct}
      annotations={annotations}
      notesPanelOpen={notesPanelOpen}
      onToggleNotesPanel={() => setNotesPanelOpen((v) => !v)}
      onUpdateAnnotation={updateAnnotation}
      onRemoveAnnotation={removeAnnotation}
      lineReaderOpen={lineReaderOpen}
      onToggleLineReader={() => setLineReaderOpen((v) => !v)}
      isFullscreen={isFullscreen}
      onToggleFullscreen={toggleFullscreen}
      onSaveAndExit={async () => {
        submittingRef.current = true; // a deliberate exit shouldn't warn
        await persist();
        router.push("/dashboard");
      }}
    />
  );

  // Interstitials own the whole screen: no header, no timer, no footer. They
  // sit ahead of the module render so none of the testing chrome mounts behind
  // them and keeps ticking.
  if (phase === "preparing") {
    return <PreparingScreen onDone={() => setPhase("testing")} />;
  }
  if (phase === "module-over") {
    return <ModuleOverScreen />;
  }
  if (phase === "break") {
    return (
      <BreakScreen
        studentName={studentName}
        nextSectionTitle={pendingBreak ?? "The next section"}
        onResume={() => {
          setPhase("module-over");
          router.refresh();
        }}
      />
    );
  }

  return (
    <div ref={rootRef} className="flex h-screen flex-col bg-exam-bg text-exam-text">
      {header}

      <TestingBanner>This is a practice test</TestingBanner>

      {/* Timer callouts, for hidden-timer and screen-reader users alike. */}
      <p aria-live="polite" className="sr-only">
        {timerAnnouncement}
      </p>

      {reviewPage ? (
        <div className="flex-1 overflow-y-auto exam-scroll bg-exam-bg px-4 py-10">
          <div className="mx-auto w-full max-w-[640px]">
            <h1 className="text-center text-[26px] font-semibold tracking-tight">Check Your Work</h1>
            <p className="mx-auto mt-2 max-w-[34rem] text-center text-[14px] leading-[1.6] text-exam-muted">
              On test day, you won&apos;t be able to move on to the next module until time expires. For these practice
              questions, you can end the module when you&apos;re ready to move on.
            </p>

            <div className="mt-7 rounded-md border border-exam-border bg-white">
              <div className="px-5 pb-3 pt-4">
                <p className="text-center text-[13px] font-semibold">{sectionTitle}</p>
                <div className="mt-2.5">
                  <QuestionLegend />
                </div>
              </div>
              <div className="border-t border-exam-divider px-5 py-4">
                <QuestionGrid
                  count={module.questions.length}
                  currentIndex={currentIndex}
                  states={states}
                  onJump={goTo}
                />
              </div>
            </div>

            <p className="mt-4 text-center text-[13px] text-exam-muted">
              {answeredCount} of {module.questions.length} questions answered.
            </p>
          </div>
        </div>
      ) : (
        <div className="flex-1 overflow-hidden" style={{ zoom: `${zoomPct}%` } as CSSProperties}>
          {module.subject === "READING_WRITING" ? (
            <div
              ref={splitPaneRef}
              className="grid h-full grid-rows-[42vh_auto_1fr] overflow-hidden lg:grid-cols-[var(--passage-w,55%)_auto_1fr] lg:grid-rows-1"
              style={passageWidthPct ? ({ "--passage-w": `${passageWidthPct}%` } as CSSProperties) : undefined}
            >
              <div className="min-h-0 border-b border-exam-border bg-exam-passage lg:border-b-0">
                <div className="h-full overflow-y-auto exam-scroll px-6 pb-14 pt-8 lg:px-10">
                  <div className="max-w-[44rem]">
                    {question.imageUrl && (
                      // eslint-disable-next-line @next/next/no-img-element
                      <img
                        src={question.imageUrl}
                        alt="Question figure"
                        className="mb-4 max-w-full rounded border border-exam-border bg-white"
                      />
                    )}
                    {question.passage ? (
                      <HighlightableContent
                        regionId={question.passage.id}
                        html={passageHtml}
                        annotations={passageAnnotations}
                        onCreate={addAnnotation}
                        onUpdate={updateAnnotation}
                        onRemove={removeAnnotation}
                        ariaLabel="Passage"
                        className="exam-passage text-[16px] leading-[1.7]"
                      />
                    ) : !question.imageUrl ? (
                      <p className="text-[14px] text-exam-muted">No passage for this question.</p>
                    ) : null}
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

              <div className="min-h-0 bg-exam-question">
                <QuestionBody
                  question={question}
                  index={currentIndex}
                  total={module.questions.length}
                  state={states[currentIndex]}
                  crossOutEnabled={crossOutEnabled}
                  onToggleCrossOutEnabled={() => setCrossOutEnabled((v) => !v)}
                  onSelect={selectChoice}
                  onToggleEliminate={toggleEliminated}
                  onFreeResponseChange={(v) => updateCurrent({ freeResponseAnswer: v })}
                  onToggleFlag={toggleFlag}
                  stemId={stemId}
                  stemHtml={stemHtml}
                  stemAnnotations={stemAnnotations}
                  onCreateAnnotation={addAnnotation}
                  onUpdateAnnotation={updateAnnotation}
                  onRemoveAnnotation={removeAnnotation}
                  showImage={false}
                />
              </div>
            </div>
          ) : (
            <div className="h-full bg-exam-question">
              <QuestionBody
                question={question}
                index={currentIndex}
                total={module.questions.length}
                state={states[currentIndex]}
                crossOutEnabled={crossOutEnabled}
                onToggleCrossOutEnabled={() => setCrossOutEnabled((v) => !v)}
                onSelect={selectChoice}
                onToggleEliminate={toggleEliminated}
                onFreeResponseChange={(v) => updateCurrent({ freeResponseAnswer: v })}
                onToggleFlag={toggleFlag}
                stemId={stemId}
                stemHtml={stemHtml}
                stemAnnotations={stemAnnotations}
                onCreateAnnotation={addAnnotation}
                onUpdateAnnotation={updateAnnotation}
                onRemoveAnnotation={removeAnnotation}
                innerClassName="mx-auto max-w-[46rem]"
              />
            </div>
          )}
        </div>
      )}

      {/* Bottom navigation */}
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
              Question {currentIndex + 1} of {module.questions.length}
              <ChevronUp className={cn("h-3.5 w-3.5 transition-transform", menuOpen && "rotate-180")} />
            </button>
          </div>

          <div className="flex items-center justify-end gap-2 sm:w-[26%]">
            {reviewPage ? (
              <>
                <NavButton onClick={() => setReviewPage(false)}>Back</NavButton>
                <NavButton onClick={handleEndModule} disabled={isSubmitting}>
                  End Module
                </NavButton>
              </>
            ) : (
              <>
                {currentIndex > 0 && <NavButton onClick={() => goTo(currentIndex - 1)}>Back</NavButton>}
                <NavButton onClick={goNext}>Next</NavButton>
              </>
            )}
          </div>
        </div>

        <QuestionPalette
          open={menuOpen}
          onOpenChange={setMenuOpen}
          title={sectionTitle}
          count={module.questions.length}
          currentIndex={currentIndex}
          states={states}
          onJump={goTo}
          onGoToReview={() => setReviewPage(true)}
        />
      </div>

      {directionsOpen && (
        <DirectionsDialog
          title={sectionTitle}
          paragraphs={DIRECTIONS[module.subject]}
          onClose={() => setDirectionsOpen(false)}
        />
      )}

      {helpOpen && <HelpDialog subject={module.subject} onClose={() => setHelpOpen(false)} />}

      {lineReaderOpen && <LineReader onClose={() => setLineReaderOpen(false)} />}

      {module.subject === "MATH" && (
        <>
          {calculatorOpen && <CalculatorPanel onClose={() => setCalculatorOpen(false)} />}
          <ReferenceSheetDialog open={referenceOpen} onOpenChange={setReferenceOpen} />
        </>
      )}
    </div>
  );
}

function ExamHeader({
  sectionTitle,
  subject,
  secondsRemaining,
  timerHidden,
  onToggleTimer,
  onOpenDirections,
  onOpenHelp,
  onToggleCalculator,
  onOpenReference,
  calculatorOpen,
  zoomPct,
  onZoomChange,
  annotations,
  notesPanelOpen,
  onToggleNotesPanel,
  onUpdateAnnotation,
  onRemoveAnnotation,
  lineReaderOpen,
  onToggleLineReader,
  isFullscreen,
  onToggleFullscreen,
  onSaveAndExit,
}: {
  sectionTitle: string;
  subject: ExamModule["subject"];
  secondsRemaining: number;
  timerHidden: boolean;
  onToggleTimer: () => void;
  onOpenDirections: () => void;
  onOpenHelp: () => void;
  onToggleCalculator: () => void;
  onOpenReference: () => void;
  calculatorOpen: boolean;
  zoomPct: number;
  onZoomChange: (pct: number) => void;
  annotations: Annotation[];
  notesPanelOpen: boolean;
  onToggleNotesPanel: () => void;
  onUpdateAnnotation: (id: string, patch: Partial<Annotation>) => void;
  onRemoveAnnotation: (id: string) => void;
  lineReaderOpen: boolean;
  onToggleLineReader: () => void;
  isFullscreen: boolean;
  onToggleFullscreen: () => void;
  onSaveAndExit: () => void;
}) {
  const warning = secondsRemaining <= WARNING_AT_SECONDS;
  const critical = secondsRemaining <= CRITICAL_AT_SECONDS;

  useEscape(notesPanelOpen, onToggleNotesPanel);

  return (
    <header className="relative z-20 shrink-0 border-b border-dashed border-exam-divider bg-exam-header">
      <div className="flex h-[62px] items-center px-4">
        <div className="flex min-w-0 flex-col gap-0.5">
          <p className="truncate text-[14px] font-semibold leading-tight">{sectionTitle}</p>
          <button
            type="button"
            onClick={onOpenDirections}
            className={cn(
              "flex w-fit items-center gap-1 rounded text-[13px] leading-tight text-exam-text hover:underline",
              FOCUS_RING
            )}
          >
            Directions <ChevronDown className="h-3.5 w-3.5" />
          </button>
        </div>

        <div className="pointer-events-none absolute left-1/2 flex -translate-x-1/2 flex-col items-center">
          <div className="flex h-[26px] items-center gap-1.5">
            {timerHidden ? (
              <Clock className="h-5 w-5 text-exam-muted" aria-hidden="true" />
            ) : (
              <>
                {/* The low-time cue is an icon as well as a color, so it still
                    reads for color-blind students and in high-contrast mode. */}
                {critical && <TriangleAlert className="h-4 w-4 text-exam-error" aria-hidden="true" />}
                <span
                  // The server renders the clock at request time and the
                  // browser hydrates a moment later, so the two readings
                  // legitimately differ by a second. Suppressing here is the
                  // sanctioned escape hatch for clocks; the first interval tick
                  // corrects the DOM within a second either way.
                  suppressHydrationWarning
                  className={cn(
                    "text-[20px] font-semibold tabular-nums leading-none",
                    critical ? "text-exam-error" : warning ? "text-exam-warning" : "text-exam-text"
                  )}
                >
                  {formatClock(secondsRemaining)}
                </span>
              </>
            )}
          </div>
          <button
            type="button"
            onClick={onToggleTimer}
            aria-pressed={timerHidden}
            aria-label={timerHidden ? "Show the countdown timer" : "Hide the countdown timer"}
            className={cn(
              "pointer-events-auto mt-1 rounded-full border border-exam-text px-2.5 py-[1px] text-[11px] font-medium leading-tight text-exam-text transition-colors hover:bg-exam-hover",
              FOCUS_RING
            )}
          >
            {timerHidden ? "Show" : "Hide"}
          </button>
        </div>

        <div className="ml-auto flex items-center gap-0.5">
          {subject === "MATH" && (
            <>
              <ToolButton icon={Calculator} label="Calculator" onClick={onToggleCalculator} active={calculatorOpen} />
              <ToolButton icon={Ruler} label="Reference" onClick={onOpenReference} />
            </>
          )}

          <ToolButton icon={CircleHelp} label="Question" onClick={onOpenHelp} />

          <div className="relative">
            <ToolButton
              icon={Highlighter}
              label="Highlights & Notes"
              onClick={onToggleNotesPanel}
              active={notesPanelOpen}
            />
            {notesPanelOpen && (
              <>
                <div className="fixed inset-0 z-30" onMouseDown={onToggleNotesPanel} />
                <div className="absolute right-0 top-full z-40 mt-1 w-[320px] rounded-md border border-exam-border bg-white shadow-examPopup">
                  <div className="flex items-center justify-between border-b border-exam-divider px-3.5 py-2.5">
                    <p className="text-[13px] font-semibold">Highlights &amp; Notes</p>
                    <button
                      type="button"
                      onClick={onToggleNotesPanel}
                      aria-label="Close Highlights & Notes"
                      className="flex h-6 w-6 items-center justify-center rounded text-exam-muted hover:bg-exam-hover hover:text-exam-text"
                    >
                      <X className="h-4 w-4" />
                    </button>
                  </div>
                  {annotations.length === 0 ? (
                    <p className="px-3.5 py-4 text-[13px] leading-[1.55] text-exam-muted">
                      Select text in a passage to highlight it. You can attach a note to any highlight.
                    </p>
                  ) : (
                    <ul className="max-h-[52vh] divide-y divide-exam-divider overflow-y-auto exam-scroll">
                      {annotations.map((a) => (
                        <li key={a.id} className="px-3.5 py-2.5">
                          <div className="flex items-start gap-2">
                            <span
                              className="mt-1 h-2.5 w-2.5 shrink-0 rounded-full"
                              style={{
                                backgroundColor:
                                  a.color === "pink" ? "#FFD0DE" : a.color === "blue" ? "#BFDBFE" : "#FFE9A6",
                              }}
                            />
                            <div className="min-w-0 flex-1">
                              <p className="line-clamp-2 text-[13px] leading-[1.5] text-exam-text">“{a.text}”</p>
                              <textarea
                                value={a.note ?? ""}
                                onChange={(e) => onUpdateAnnotation(a.id, { note: e.target.value || null })}
                                placeholder="Add a note…"
                                rows={2}
                                className="mt-1.5 w-full resize-none rounded border border-exam-border bg-white px-2 py-1 text-[12px] leading-snug text-exam-text placeholder:text-exam-disabled focus:border-exam-blue focus:outline-none"
                              />
                            </div>
                            <button
                              type="button"
                              onClick={() => onRemoveAnnotation(a.id)}
                              aria-label="Delete highlight"
                              className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded text-exam-muted hover:bg-exam-hover hover:text-exam-text"
                            >
                              <Trash2 className="h-3.5 w-3.5" />
                            </button>
                          </div>
                        </li>
                      ))}
                    </ul>
                  )}
                </div>
              </>
            )}
          </div>

          {/* Zoom and Full Screen live in More rather than on the bar: the
              reference keeps the header down to three controls, and these two
              are set-once preferences rather than per-question tools. */}
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <button
                type="button"
                aria-label="More test tools"
                className={cn(
                  "flex h-[46px] min-w-[54px] flex-col items-center justify-center gap-1 rounded px-2 text-[11px] font-medium leading-none text-exam-text transition-colors hover:bg-exam-hover",
                  FOCUS_RING
                )}
              >
                <MoreHorizontal className="h-[18px] w-[18px]" aria-hidden="true" />
                <span>More</span>
              </button>
            </DropdownMenuTrigger>
            <DropdownMenuContent
              align="end"
              className="w-60 rounded-md border-exam-border bg-white p-1 text-exam-text shadow-examPopup"
            >
              <DropdownMenuLabel className="px-2 py-1.5 text-[11px] font-semibold uppercase tracking-[0.06em] text-exam-muted">
                Text size
              </DropdownMenuLabel>
              <div
                className="flex items-center gap-1 px-2 pb-1.5"
                // Zoom is a stepper, not a menu item — keep arrow-key menu
                // navigation from stealing the button clicks.
                onKeyDown={(e) => e.stopPropagation()}
              >
                <button
                  type="button"
                  onClick={() => onZoomChange(Math.max(80, zoomPct - 10))}
                  disabled={zoomPct <= 80}
                  aria-label="Decrease text size"
                  className={cn(
                    "flex h-7 w-7 items-center justify-center rounded border border-exam-border text-exam-muted transition-colors hover:bg-exam-hover hover:text-exam-text disabled:pointer-events-none disabled:opacity-40",
                    FOCUS_RING
                  )}
                >
                  <Minus className="h-3.5 w-3.5" />
                </button>
                <span className="w-12 text-center text-[12px] font-medium tabular-nums" aria-live="polite">
                  {zoomPct}%
                </span>
                <button
                  type="button"
                  onClick={() => onZoomChange(Math.min(150, zoomPct + 10))}
                  disabled={zoomPct >= 150}
                  aria-label="Increase text size"
                  className={cn(
                    "flex h-7 w-7 items-center justify-center rounded border border-exam-border text-exam-muted transition-colors hover:bg-exam-hover hover:text-exam-text disabled:pointer-events-none disabled:opacity-40",
                    FOCUS_RING
                  )}
                >
                  <Plus className="h-3.5 w-3.5" />
                </button>
                <button
                  type="button"
                  onClick={() => onZoomChange(100)}
                  className={cn(
                    "ml-auto rounded px-1.5 py-1 text-[12px] font-medium text-exam-muted transition-colors hover:bg-exam-hover hover:text-exam-text",
                    FOCUS_RING
                  )}
                >
                  Reset
                </button>
              </div>

              <DropdownMenuSeparator className="bg-exam-divider" />

              <DropdownMenuItem className="text-[13px] focus:bg-exam-hover" onClick={onToggleLineReader}>
                <ScanLine className="mr-2 h-4 w-4" /> {lineReaderOpen ? "Hide Line Reader" : "Line Reader"}
              </DropdownMenuItem>
              <DropdownMenuItem className="text-[13px] focus:bg-exam-hover" onClick={onToggleFullscreen}>
                {isFullscreen ? <Minimize className="mr-2 h-4 w-4" /> : <Maximize className="mr-2 h-4 w-4" />}
                {isFullscreen ? "Exit Full Screen" : "Full Screen"}
              </DropdownMenuItem>
              <DropdownMenuItem className="text-[13px] focus:bg-exam-hover" onClick={onOpenDirections}>
                <Bookmark className="mr-2 h-4 w-4" /> Directions
              </DropdownMenuItem>

              <DropdownMenuSeparator className="bg-exam-divider" />

              <DropdownMenuItem className="text-[13px] focus:bg-exam-hover" onClick={onSaveAndExit}>
                <LogOut className="mr-2 h-4 w-4" /> Save &amp; Exit
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>
    </header>
  );
}

/** Shared modal chrome for the exam's in-test dialogs (Directions, Help). */
function ExamDialog({
  title,
  onClose,
  children,
  widthClassName = "max-w-[560px]",
}: {
  title: string;
  onClose: () => void;
  children: ReactNode;
  widthClassName?: string;
}) {
  const panelRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if (e.key === "Escape") {
        onClose();
        return;
      }
      // Keep Tab inside the dialog — an aria-modal that leaks focus back to
      // the question behind it isn't actually modal for keyboard users.
      if (e.key !== "Tab" || !panelRef.current) return;
      const focusable = panelRef.current.querySelectorAll<HTMLElement>(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      );
      if (focusable.length === 0) return;
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
    window.addEventListener("keydown", onKeyDown);
    // Move focus in on open so the dialog is immediately operable.
    panelRef.current?.querySelector<HTMLElement>("button")?.focus();
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [onClose]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div className="absolute inset-0 bg-exam-strip/40" onMouseDown={onClose} />
      <div
        ref={panelRef}
        role="dialog"
        aria-modal="true"
        aria-label={title}
        className={cn(
          "relative flex max-h-[85vh] w-full flex-col rounded-md border border-exam-border bg-white shadow-examPopup",
          widthClassName
        )}
      >
        <div className="flex shrink-0 items-center justify-between border-b border-exam-divider px-5 py-3">
          <p className="text-[14px] font-semibold">{title}</p>
          <button
            type="button"
            onClick={onClose}
            aria-label={`Close ${title}`}
            className={cn(
              "flex h-7 w-7 items-center justify-center rounded text-exam-muted hover:bg-exam-hover hover:text-exam-text",
              FOCUS_RING
            )}
          >
            <X className="h-4 w-4" />
          </button>
        </div>

        <div className="min-h-0 flex-1 overflow-y-auto exam-scroll px-5 py-4">{children}</div>

        <div className="flex shrink-0 justify-center border-t border-exam-divider px-5 py-3">
          <button
            type="button"
            onClick={onClose}
            className={cn(
              "rounded-full bg-exam-blue px-6 py-1.5 text-[13px] font-medium text-white transition-colors hover:bg-exam-blueHover",
              FOCUS_RING
            )}
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}

function DirectionsDialog({
  title,
  paragraphs,
  onClose,
}: {
  title: string;
  paragraphs: string[];
  onClose: () => void;
}) {
  return (
    <ExamDialog title={title} onClose={onClose}>
      <div className="space-y-3 text-[14px] leading-[1.65] text-exam-text">
        {paragraphs.map((p) => (
          <p key={p}>{p}</p>
        ))}
      </div>
    </ExamDialog>
  );
}

/**
 * The header's "Question" button. Everything listed here is a control that
 * actually exists on this screen — keep it that way when the toolbar changes.
 */
const SHORTCUTS: { keys: string; action: string }[] = [
  { keys: "→", action: "Next question" },
  { keys: "←", action: "Previous question" },
  { keys: "1 – 4", action: "Choose answer A through D" },
  { keys: "F", action: "Mark the current question for review" },
  { keys: "Esc", action: "Close an open menu or dialog" },
];

function HelpDialog({ subject, onClose }: { subject: ExamModule["subject"]; onClose: () => void }) {
  return (
    <ExamDialog title="Using this screen" onClose={onClose}>
      <div className="space-y-4 text-[14px] leading-[1.65] text-exam-text">
        <ul className="list-disc space-y-1.5 pl-5">
          <li>
            Select an answer by clicking anywhere on its row. Your answers save automatically and are restored if
            you reload the page.
          </li>
          <li>
            <strong>Mark for Review</strong> flags a question so you can find it again from the question menu at the
            bottom of the screen or on the review page.
          </li>
          <li>
            Select any text in the passage or the question to <strong>highlight</strong> it and attach a note.
            Highlights last for this module.
          </li>
          <li>
            The crossed-out <span className="font-semibold line-through">ABC</span> button turns on the answer
            eliminator, letting you cross off choices you have ruled out.
          </li>
          {subject === "READING_WRITING" ? (
            <li>Drag the divider between the two panels to give the passage more or less room.</li>
          ) : (
            <li>
              <strong>Calculator</strong> and <strong>Reference</strong> in the header are available for every
              question in this section.
            </li>
          )}
          <li>
            The timer runs on the clock, not on this tab — leaving the page does not pause it. Use{" "}
            <strong>Hide</strong> if it is distracting.
          </li>
        </ul>

        <div>
          <p className="mb-2 text-[13px] font-semibold uppercase tracking-[0.06em] text-exam-muted">
            Keyboard shortcuts
          </p>
          <dl className="divide-y divide-exam-divider rounded-md border border-exam-border">
            {SHORTCUTS.map((s) => (
              <div key={s.keys} className="flex items-center gap-4 px-3 py-2">
                <dt className="w-20 shrink-0">
                  <kbd className="rounded border border-exam-border bg-exam-header px-1.5 py-0.5 text-[12px] font-medium">
                    {s.keys}
                  </kbd>
                </dt>
                <dd className="text-[13px]">{s.action}</dd>
              </div>
            ))}
          </dl>
        </div>
      </div>
    </ExamDialog>
  );
}

function QuestionBody({
  question,
  index,
  total,
  state,
  crossOutEnabled,
  onToggleCrossOutEnabled,
  onSelect,
  onToggleEliminate,
  onFreeResponseChange,
  onToggleFlag,
  stemId,
  stemHtml,
  stemAnnotations,
  onCreateAnnotation,
  onUpdateAnnotation,
  onRemoveAnnotation,
  innerClassName,
  showImage = true,
}: {
  question: ExamModule["questions"][number];
  index: number;
  total: number;
  state: QuestionState;
  crossOutEnabled: boolean;
  onToggleCrossOutEnabled: () => void;
  onSelect: (choiceId: string) => void;
  onToggleEliminate: (choiceId: string) => void;
  onFreeResponseChange: (value: string) => void;
  onToggleFlag: () => void;
  stemId: string;
  stemHtml: string;
  stemAnnotations: Annotation[];
  onCreateAnnotation: (a: Omit<Annotation, "id">) => void;
  onUpdateAnnotation: (id: string, patch: Partial<Annotation>) => void;
  onRemoveAnnotation: (id: string) => void;
  innerClassName?: string;
  /** false when the caller already renders the question's image itself (e.g. above the passage panel). */
  showImage?: boolean;
}) {
  const flagged = state.flagged;

  return (
    <div className="flex h-full flex-col">
      {/* Question header band — spans the panel width. */}
      <div className="shrink-0 border-b border-exam-border bg-exam-header px-6 py-1.5 lg:px-10">
        <div className={cn("flex items-center gap-3", innerClassName)}>
          <QuestionNumberChip n={index + 1} />
          <span className="sr-only">
            Question {index + 1} of {total}
          </span>
          <button
            type="button"
            onClick={onToggleFlag}
            aria-pressed={flagged}
            className={cn(
              "flex items-center gap-1.5 rounded px-1 py-0.5 text-[13px] font-medium text-exam-text transition-colors hover:bg-exam-hover",
              FOCUS_RING
            )}
          >
            <Bookmark className={cn("h-4 w-4", flagged ? "fill-exam-flag text-exam-flag" : "text-exam-muted")} />
            {flagged ? "Marked for Review" : "Mark for Review"}
          </button>

          {question.type === "MULTIPLE_CHOICE" && (
            <button
              type="button"
              onClick={onToggleCrossOutEnabled}
              aria-pressed={crossOutEnabled}
              title={crossOutEnabled ? "Hide answer eliminator" : "Show answer eliminator"}
              className={cn(
                "ml-auto flex h-[26px] items-center rounded-[3px] border px-2 text-[12px] font-semibold tracking-tight transition-colors",
                FOCUS_RING,
                crossOutEnabled
                  ? "border-exam-blue bg-exam-blue text-white"
                  : "border-exam-text bg-transparent text-exam-text hover:bg-exam-hover"
              )}
            >
              <span className="line-through">ABC</span>
            </button>
          )}
        </div>
      </div>

      <div className="min-h-0 flex-1 overflow-y-auto exam-scroll px-6 pb-14 pt-6 lg:px-10">
        <div className={innerClassName}>
          {/* The stem is highlightable too — students annotate the question as
              often as the passage ("EXCEPT", "least likely", a units clue).
              Math inside it is skipped by the annotation walker, so KaTeX
              output is never split. */}
          <HighlightableContent
            regionId={stemId}
            html={stemHtml}
            annotations={stemAnnotations}
            onCreate={onCreateAnnotation}
            onUpdate={onUpdateAnnotation}
            onRemove={onRemoveAnnotation}
            ariaLabel="Question"
            className="exam-stem block text-[16px] leading-[1.6]"
          />

          {showImage && question.imageUrl && (
            // eslint-disable-next-line @next/next/no-img-element
            <img
              src={question.imageUrl}
              alt="Question figure"
              className="mt-4 max-w-full rounded border border-exam-border bg-white"
            />
          )}

          {question.type === "MULTIPLE_CHOICE" ? (
            <div className="mt-5">
              <AnswerChoiceList
                choices={question.choices}
                selectedId={state.selectedChoiceId}
                eliminatedIds={state.eliminated}
                crossOutEnabled={crossOutEnabled}
                onSelect={onSelect}
                onToggleEliminate={onToggleEliminate}
              />
            </div>
          ) : (
            <div className="mt-5">
              <FreeResponseInput value={state.freeResponseAnswer} onChange={onFreeResponseChange} />
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
