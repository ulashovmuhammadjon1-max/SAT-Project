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
  type MouseEvent as ReactMouseEvent,
  type ReactNode,
} from "react";
import { useRouter } from "next/navigation";
import {
  Bookmark,
  Calculator,
  ChevronDown,
  ChevronUp,
  Clock,
  Highlighter,
  LogOut,
  Minus,
  MoreHorizontal,
  Plus,
  Ruler,
  ScanLine,
  Search,
  Trash2,
  X,
} from "lucide-react";
import { toast } from "sonner";

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { CalculatorPanel } from "@/components/exam/calculator-panel";
import { HighlightablePassage } from "@/components/exam/highlightable-passage";
import { LineReader } from "@/components/exam/line-reader";
import { QuestionGrid, QuestionLegend, QuestionPalette } from "@/components/exam/question-palette";
import { ReferenceSheetDialog } from "@/components/exam/reference-sheet-dialog";
import { cn } from "@/lib/utils";
import type { Annotation } from "@/lib/exam/annotations";
import { autosaveResponses, submitModule } from "@/server/actions/student/attempts";
import type { ExamModule, ExistingResponse, QuestionState } from "@/types/exam";

const FOCUS_RING =
  "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-exam-blue focus-visible:ring-offset-1";

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

/** Bluebook pads the minutes, so 7:23 reads as 07:23. */
function formatClock(totalSeconds: number): string {
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  return `${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
}

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

export function ExamShell({
  attemptId,
  studentName,
  moduleAttemptId,
  module,
  startedAt,
  existingResponses,
}: {
  attemptId: string;
  studentName: string;
  moduleAttemptId: string;
  module: ExamModule;
  startedAt: Date;
  existingResponses: ExistingResponse[];
}) {
  const router = useRouter();
  const [states, setStates] = useState<QuestionState[]>(() => buildInitialStates(module, existingResponses));
  const [currentIndex, setCurrentIndex] = useState(0);
  const [menuOpen, setMenuOpen] = useState(false);
  const [calculatorOpen, setCalculatorOpen] = useState(false);
  const [referenceOpen, setReferenceOpen] = useState(false);
  const [reviewPage, setReviewPage] = useState(false);
  const [directionsOpen, setDirectionsOpen] = useState(false);
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
  // sitting, and Bluebook likewise discards them when the module ends.
  const storageKey = `summit-annotations:${moduleAttemptId}`;
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
  const startDragging = useCallback((startEvent: ReactMouseEvent) => {
    startEvent.preventDefault();
    setIsDragging(true);
    function onMove(e: MouseEvent) {
      const el = splitPaneRef.current;
      if (!el) return;
      const rect = el.getBoundingClientRect();
      const pct = ((e.clientX - rect.left) / rect.width) * 100;
      setPassageWidthPct(Math.min(70, Math.max(30, pct)));
    }
    function onUp() {
      setIsDragging(false);
      window.removeEventListener("mousemove", onMove);
      window.removeEventListener("mouseup", onUp);
    }
    window.addEventListener("mousemove", onMove);
    window.addEventListener("mouseup", onUp);
  }, []);

  const totalSeconds = module.timeLimitMinutes * 60;
  const elapsedAtLoad = Math.floor((Date.now() - new Date(startedAt).getTime()) / 1000);
  const [secondsRemaining, setSecondsRemaining] = useState(() => Math.max(totalSeconds - elapsedAtLoad, 0));

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

  // Module countdown.
  useEffect(() => {
    const interval = setInterval(() => {
      setSecondsRemaining((s) => Math.max(s - 1, 0));
    }, 1000);
    return () => clearInterval(interval);
  }, []);

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

  useEffect(() => {
    if (secondsRemaining === 0) {
      handleEndModule();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [secondsRemaining]);

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
  }

  function toggleFlag() {
    updateCurrent({ flagged: !states[currentIndex].flagged });
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
    if (isSubmitting) return;
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
        } else {
          toast.success("Module submitted. Starting the next module.");
          router.push(`/exam/${attemptId}`);
          router.refresh();
        }
      } catch (error) {
        console.error("Failed to submit module", error);
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
      if (menuOpen || directionsOpen) return;

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
  }, [currentIndex, reviewPage, question, menuOpen, directionsOpen]);

  const answeredCount = useMemo(
    () => states.filter((s) => s.selectedChoiceId || s.freeResponseAnswer).length,
    [states]
  );

  const passageId = question?.passage?.id ?? null;
  const passageAnnotations = useMemo(
    () => annotations.filter((a) => a.passageId === passageId).sort((a, b) => a.start - b.start),
    [annotations, passageId]
  );

  const header = (
    <ExamHeader
      sectionTitle={sectionTitle}
      subject={module.subject}
      secondsRemaining={secondsRemaining}
      timerHidden={timerHidden}
      onToggleTimer={() => setTimerHidden((v) => !v)}
      onOpenDirections={() => setDirectionsOpen(true)}
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
      onSaveAndExit={async () => {
        await persist();
        router.push("/dashboard");
      }}
    />
  );

  return (
    <div className="flex h-screen flex-col bg-exam-bg text-exam-text">
      <div className="shrink-0 bg-exam-strip py-[5px] text-center text-[11px] font-medium uppercase tracking-[0.08em] text-white">
        This is a practice test
      </div>

      {header}

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
                      <HighlightablePassage
                        passageId={question.passage.id}
                        content={question.passage.content}
                        annotations={passageAnnotations}
                        onCreate={addAnnotation}
                        onUpdate={updateAnnotation}
                        onRemove={removeAnnotation}
                      />
                    ) : !question.imageUrl ? (
                      <p className="text-[14px] text-exam-muted">No passage for this question.</p>
                    ) : null}
                  </div>
                </div>
              </div>

              <div
                onMouseDown={startDragging}
                role="separator"
                aria-orientation="vertical"
                className={cn(
                  "group relative hidden lg:flex lg:h-full lg:w-[9px] lg:cursor-col-resize lg:items-center lg:justify-center",
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
                  state={states[currentIndex]}
                  crossOutEnabled={crossOutEnabled}
                  onToggleCrossOutEnabled={() => setCrossOutEnabled((v) => !v)}
                  onSelect={selectChoice}
                  onToggleEliminate={toggleEliminated}
                  onFreeResponseChange={(v) => updateCurrent({ freeResponseAnswer: v })}
                  onToggleFlag={toggleFlag}
                  showImage={false}
                />
              </div>
            </div>
          ) : (
            <div className="h-full bg-exam-question">
              <QuestionBody
                question={question}
                index={currentIndex}
                state={states[currentIndex]}
                crossOutEnabled={crossOutEnabled}
                onToggleCrossOutEnabled={() => setCrossOutEnabled((v) => !v)}
                onSelect={selectChoice}
                onToggleEliminate={toggleEliminated}
                onFreeResponseChange={(v) => updateCurrent({ freeResponseAnswer: v })}
                onToggleFlag={toggleFlag}
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

/** Bluebook's Back/Next: matched blue pills, right-aligned on the bottom bar. */
function NavButton({
  children,
  onClick,
  disabled,
}: {
  children: ReactNode;
  onClick: () => void;
  disabled?: boolean;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className={cn(
        "h-[34px] rounded-full bg-exam-blue px-5 text-[13px] font-medium text-white transition-colors hover:bg-exam-blueHover disabled:pointer-events-none disabled:opacity-50",
        FOCUS_RING
      )}
    >
      {children}
    </button>
  );
}

function ToolButton({
  icon: Icon,
  label,
  onClick,
  active,
}: {
  icon: ComponentType<{ className?: string }>;
  label: string;
  onClick: () => void;
  active?: boolean;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={cn(
        "flex h-[46px] min-w-[54px] flex-col items-center justify-center gap-1 rounded px-2 text-[11px] font-medium leading-none transition-colors",
        active ? "bg-exam-hover text-exam-blue" : "text-exam-text hover:bg-exam-hover",
        FOCUS_RING
      )}
    >
      <Icon className="h-[18px] w-[18px]" />
      <span className="whitespace-nowrap">{label}</span>
    </button>
  );
}

function ExamHeader({
  sectionTitle,
  subject,
  secondsRemaining,
  timerHidden,
  onToggleTimer,
  onOpenDirections,
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
  onSaveAndExit,
}: {
  sectionTitle: string;
  subject: ExamModule["subject"];
  secondsRemaining: number;
  timerHidden: boolean;
  onToggleTimer: () => void;
  onOpenDirections: () => void;
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
  onSaveAndExit: () => void;
}) {
  const [zoomOpen, setZoomOpen] = useState(false);

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
          <div className="flex h-[26px] items-center">
            {timerHidden ? (
              <Clock className="h-5 w-5 text-exam-muted" />
            ) : (
              <span
                className={cn(
                  "text-[20px] font-semibold tabular-nums leading-none",
                  secondsRemaining < 300 && "text-destructive"
                )}
              >
                {formatClock(secondsRemaining)}
              </span>
            )}
          </div>
          <button
            type="button"
            onClick={onToggleTimer}
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

          <div className="relative">
            <ToolButton icon={Search} label="Zoom" onClick={() => setZoomOpen((v) => !v)} active={zoomOpen} />
            {zoomOpen && (
              <>
                <div className="fixed inset-0 z-30" onMouseDown={() => setZoomOpen(false)} />
                <div className="absolute right-0 top-full z-40 mt-1 flex items-center gap-1 rounded-md border border-exam-border bg-white p-1.5 shadow-examPopup">
                  <button
                    type="button"
                    onClick={() => onZoomChange(Math.max(80, zoomPct - 10))}
                    aria-label="Zoom out"
                    className={cn(
                      "flex h-6 w-6 items-center justify-center rounded text-exam-muted hover:bg-exam-hover hover:text-exam-text",
                      FOCUS_RING
                    )}
                  >
                    <Minus className="h-3.5 w-3.5" />
                  </button>
                  <span className="w-11 text-center text-[12px] font-medium tabular-nums">{zoomPct}%</span>
                  <button
                    type="button"
                    onClick={() => onZoomChange(Math.min(150, zoomPct + 10))}
                    aria-label="Zoom in"
                    className={cn(
                      "flex h-6 w-6 items-center justify-center rounded text-exam-muted hover:bg-exam-hover hover:text-exam-text",
                      FOCUS_RING
                    )}
                  >
                    <Plus className="h-3.5 w-3.5" />
                  </button>
                  <button
                    type="button"
                    onClick={() => onZoomChange(100)}
                    className={cn(
                      "ml-0.5 rounded border-l border-exam-divider pl-2 pr-1 text-[12px] font-medium text-exam-muted hover:text-exam-text",
                      FOCUS_RING
                    )}
                  >
                    Reset
                  </button>
                </div>
              </>
            )}
          </div>

          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <button
                type="button"
                className={cn(
                  "flex h-[46px] min-w-[54px] flex-col items-center justify-center gap-1 rounded px-2 text-[11px] font-medium leading-none text-exam-text transition-colors hover:bg-exam-hover",
                  FOCUS_RING
                )}
              >
                <MoreHorizontal className="h-[18px] w-[18px]" />
                <span>More</span>
              </button>
            </DropdownMenuTrigger>
            <DropdownMenuContent
              align="end"
              className="w-52 rounded-md border-exam-border bg-white p-1 text-exam-text shadow-examPopup"
            >
              <DropdownMenuItem className="text-[13px] focus:bg-exam-hover" onClick={onToggleLineReader}>
                <ScanLine className="mr-2 h-4 w-4" /> {lineReaderOpen ? "Hide Line Reader" : "Line Reader"}
              </DropdownMenuItem>
              <DropdownMenuItem className="text-[13px] focus:bg-exam-hover" onClick={onOpenDirections}>
                <Bookmark className="mr-2 h-4 w-4" /> Directions
              </DropdownMenuItem>
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

function DirectionsDialog({
  title,
  paragraphs,
  onClose,
}: {
  title: string;
  paragraphs: string[];
  onClose: () => void;
}) {
  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if (e.key === "Escape") onClose();
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [onClose]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div className="absolute inset-0 bg-exam-strip/40" onMouseDown={onClose} />
      <div
        role="dialog"
        aria-modal="true"
        aria-label="Directions"
        className="relative w-full max-w-[560px] rounded-md border border-exam-border bg-white shadow-examPopup"
      >
        <div className="flex items-center justify-between border-b border-exam-divider px-5 py-3">
          <p className="text-[14px] font-semibold">{title}</p>
          <button
            type="button"
            onClick={onClose}
            aria-label="Close Directions"
            className="flex h-7 w-7 items-center justify-center rounded text-exam-muted hover:bg-exam-hover hover:text-exam-text"
          >
            <X className="h-4 w-4" />
          </button>
        </div>
        <div className="space-y-3 px-5 py-4 text-[14px] leading-[1.65] text-exam-text">
          {paragraphs.map((p) => (
            <p key={p}>{p}</p>
          ))}
        </div>
        <div className="flex justify-center border-t border-exam-divider px-5 py-3">
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

function QuestionBody({
  question,
  index,
  state,
  crossOutEnabled,
  onToggleCrossOutEnabled,
  onSelect,
  onToggleEliminate,
  onFreeResponseChange,
  onToggleFlag,
  innerClassName,
  showImage = true,
}: {
  question: ExamModule["questions"][number];
  index: number;
  state: QuestionState;
  crossOutEnabled: boolean;
  onToggleCrossOutEnabled: () => void;
  onSelect: (choiceId: string) => void;
  onToggleEliminate: (choiceId: string) => void;
  onFreeResponseChange: (value: string) => void;
  onToggleFlag: () => void;
  innerClassName?: string;
  /** false when the caller already renders the question's image itself (e.g. above the passage panel). */
  showImage?: boolean;
}) {
  const flagged = state.flagged;

  return (
    <div className="flex h-full flex-col">
      {/* Question header band — spans the panel, as in Bluebook. */}
      <div className="shrink-0 border-b border-exam-border bg-exam-header px-6 py-1.5 lg:px-10">
        <div className={cn("flex items-center gap-3", innerClassName)}>
          <span className="flex h-[26px] w-[26px] shrink-0 items-center justify-center rounded-[3px] bg-exam-strip text-[13px] font-semibold text-white">
            {index + 1}
          </span>
          <button
            type="button"
            onClick={onToggleFlag}
            className={cn("flex items-center gap-1.5 rounded text-[13px] font-medium text-exam-text", FOCUS_RING)}
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
          <div
            className="exam-stem text-[16px] leading-[1.6] text-exam-text"
            dangerouslySetInnerHTML={{ __html: question.stem }}
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
            <div className="mt-5 space-y-3">
              {question.choices.map((choice) => {
                const eliminated = state.eliminated.includes(choice.id);
                const selected = state.selectedChoiceId === choice.id;
                return (
                  <div key={choice.id} className="flex items-center gap-2">
                    <button
                      type="button"
                      onClick={() => !eliminated && onSelect(choice.id)}
                      aria-pressed={selected}
                      className={cn(
                        "flex flex-1 items-start gap-3 rounded-lg border bg-white px-3.5 py-2.5 text-left text-[16px] leading-[1.5] transition-colors",
                        FOCUS_RING,
                        selected
                          ? "border-exam-blue ring-1 ring-inset ring-exam-blue"
                          : "border-exam-disabled hover:bg-exam-hover",
                        eliminated && "opacity-45"
                      )}
                    >
                      <span
                        className={cn(
                          "flex h-6 w-6 shrink-0 items-center justify-center rounded-full border text-[13px] font-medium leading-none",
                          selected ? "border-exam-blue bg-exam-blue text-white" : "border-exam-muted text-exam-text",
                          eliminated && "line-through"
                        )}
                      >
                        {choice.label}
                      </span>
                      <span className={cn("text-exam-text", eliminated && "line-through")}>{choice.content}</span>
                    </button>

                    {crossOutEnabled && (
                      <button
                        type="button"
                        onClick={() => onToggleEliminate(choice.id)}
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
          ) : (
            <div className="mt-5 max-w-xs space-y-1.5">
              <input
                type="text"
                value={state.freeResponseAnswer}
                onChange={(e) => onFreeResponseChange(e.target.value)}
                placeholder="Enter your answer"
                className={cn(
                  "w-full rounded border border-exam-disabled bg-white px-3 py-2 text-[16px] text-exam-text placeholder:text-exam-disabled focus:border-exam-blue",
                  FOCUS_RING
                )}
              />
              <p className="text-[12px] text-exam-muted">
                Enter a numeric answer (fraction or decimal accepted).
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
