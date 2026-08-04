"use client";

import {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
  useTransition,
  type CSSProperties,
  type MouseEvent as ReactMouseEvent,
} from "react";
import { useRouter } from "next/navigation";
import {
  Calculator,
  ChevronDown,
  ChevronLeft,
  ChevronRight,
  Flag,
  GripVertical,
  Grid3x3,
  Highlighter,
  LogOut,
  Minus,
  MoreVertical,
  Plus,
  Ruler,
  Strikethrough,
  X,
} from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Textarea } from "@/components/ui/textarea";
import { CalculatorPanel } from "@/components/exam/calculator-panel";
import { HighlightablePassage } from "@/components/exam/highlightable-passage";
import { QuestionPalette } from "@/components/exam/question-palette";
import { ReferenceSheetDialog } from "@/components/exam/reference-sheet-dialog";
import { cn, formatDuration } from "@/lib/utils";
import { autosaveResponses, submitModule } from "@/server/actions/student/attempts";
import type { ExamModule, ExistingResponse, QuestionState } from "@/types/exam";

const FOCUS_RING = "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-exam-blue focus-visible:ring-offset-1";

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
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [calculatorOpen, setCalculatorOpen] = useState(false);
  const [referenceOpen, setReferenceOpen] = useState(false);
  const [reviewScreen, setReviewScreen] = useState(false);
  const [directionsOpen, setDirectionsOpen] = useState(false);
  const [crossOutEnabled, setCrossOutEnabled] = useState(false);
  const [zoomPct, setZoomPct] = useState(100);
  const [passageWidthPct, setPassageWidthPct] = useState<number | null>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [isSubmitting, startSubmit] = useTransition();
  const splitPaneRef = useRef<HTMLDivElement>(null);

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
    if (reviewScreen) return;
    const interval = setInterval(() => {
      setStates((prev) =>
        prev.map((s, i) => (i === currentIndex ? { ...s, timeSpentSeconds: s.timeSpentSeconds + 1 } : s))
      );
      dirtyRef.current = true;
    }, 1000);
    return () => clearInterval(interval);
  }, [currentIndex, reviewScreen]);

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

  // Autosave every 5 seconds, plus immediately after selecting an answer (below).
  useEffect(() => {
    const interval = setInterval(persist, 5000);
    return () => clearInterval(interval);
  }, [persist]);

  // Auto-submit when time runs out.
  useEffect(() => {
    if (secondsRemaining === 0) {
      handleSubmitModule();
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
    // Answer selections persist right away rather than waiting for the next
    // 5s tick — the choice that actually matters for not losing progress.
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
    setCurrentIndex(index);
  }

  async function handleSubmitModule() {
    startSubmit(async () => {
      await persist();
      const result = await submitModule(attemptId, moduleAttemptId);
      if (result.finished) {
        router.push(`/review/${attemptId}`);
      } else {
        toast.success("Module submitted. Starting the next module.");
        router.push(`/exam/${attemptId}`);
        router.refresh();
      }
    });
  }

  // Keyboard shortcuts: arrow keys to move, digits to pick a choice, F to
  // flag. Disabled while typing in the free-response box so digits/letters
  // still work as text input there.
  useEffect(() => {
    if (reviewScreen) return;
    function onKeyDown(e: KeyboardEvent) {
      const target = e.target as HTMLElement | null;
      if (target && ["INPUT", "TEXTAREA"].includes(target.tagName)) return;

      if (e.key === "ArrowRight") {
        e.preventDefault();
        if (currentIndex < module.questions.length - 1) goTo(currentIndex + 1);
        else setReviewScreen(true);
      } else if (e.key === "ArrowLeft") {
        e.preventDefault();
        goTo(currentIndex - 1);
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
  }, [currentIndex, reviewScreen, question]);

  const answeredCount = useMemo(
    () => states.filter((s) => s.selectedChoiceId || s.freeResponseAnswer).length,
    [states]
  );

  if (reviewScreen) {
    return (
      <div className="flex h-screen flex-col bg-exam-bg">
        <ExamHeader
          module={module}
          secondsRemaining={secondsRemaining}
          directionsOpen={directionsOpen}
          onToggleDirections={() => setDirectionsOpen((v) => !v)}
          onToggleCalculator={() => setCalculatorOpen((v) => !v)}
          onOpenReference={() => setReferenceOpen(true)}
          zoomPct={zoomPct}
          onZoomChange={setZoomPct}
          onSaveAndExit={async () => {
            await persist();
            router.push("/dashboard");
          }}
        />
        <div className="mx-auto w-full max-w-3xl flex-1 space-y-5 overflow-y-auto exam-scroll p-6">
          <div>
            <h1 className="text-lg font-semibold text-exam-text">Review your answers</h1>
            <p className="text-sm text-exam-muted">
              {answeredCount} of {module.questions.length} questions answered. You can still change any answer before
              submitting the module.
            </p>
          </div>
          <div className="grid grid-cols-6 gap-1.5 sm:grid-cols-10">
            {module.questions.map((q, i) => {
              const s = states[i];
              const answered = !!(s.selectedChoiceId || s.freeResponseAnswer);
              const visited = answered || s.timeSpentSeconds > 0;
              return (
                <button
                  key={q.id}
                  onClick={() => {
                    setReviewScreen(false);
                    goTo(i);
                  }}
                  className={cn(
                    "relative flex h-10 w-10 items-center justify-center rounded border text-sm font-medium",
                    FOCUS_RING,
                    answered
                      ? "border-exam-blue bg-exam-blue text-white"
                      : visited
                        ? "border-exam-border bg-gray-100 text-exam-text"
                        : "border-exam-border bg-exam-card text-exam-text"
                  )}
                >
                  {i + 1}
                  {s.flagged && <Flag className="absolute -right-1.5 -top-1.5 h-3.5 w-3.5 fill-warning text-warning" />}
                </button>
              );
            })}
          </div>
          <div className="flex justify-between pt-2">
            <Button
              variant="outline"
              className="rounded-md border-exam-border bg-exam-card text-exam-text hover:bg-gray-50"
              onClick={() => setReviewScreen(false)}
            >
              <ChevronLeft className="h-4 w-4" /> Back to questions
            </Button>
            <Button
              className="rounded-md bg-exam-blue text-white hover:bg-exam-blueHover"
              onClick={handleSubmitModule}
              disabled={isSubmitting}
            >
              Submit module <ChevronRight className="h-4 w-4" />
            </Button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="flex h-screen flex-col bg-exam-bg">
      <ExamHeader
        module={module}
        secondsRemaining={secondsRemaining}
        directionsOpen={directionsOpen}
        onToggleDirections={() => setDirectionsOpen((v) => !v)}
        onToggleCalculator={() => setCalculatorOpen((v) => !v)}
        onOpenReference={() => setReferenceOpen(true)}
        zoomPct={zoomPct}
        onZoomChange={setZoomPct}
        onSaveAndExit={async () => {
          await persist();
          router.push("/dashboard");
        }}
      />

      <div className="shrink-0 bg-navy-950 py-1 text-center text-[11px] font-semibold tracking-wide text-white">
        THIS IS A PRACTICE TEST
      </div>

      <div className="flex-1 overflow-hidden" style={{ zoom: `${zoomPct}%` } as CSSProperties}>
        {module.subject === "READING_WRITING" ? (
          <div
            ref={splitPaneRef}
            className="grid h-full overflow-y-auto exam-scroll lg:grid-cols-[var(--passage-w,55%)_auto_1fr] lg:overflow-hidden"
            style={passageWidthPct ? ({ "--passage-w": `${passageWidthPct}%` } as CSSProperties) : undefined}
          >
            <div className="border-b border-exam-border bg-exam-bg px-6 pb-6 pt-4 lg:h-full lg:overflow-y-auto lg:exam-scroll lg:border-b-0 lg:px-8 lg:pb-8">
              {question.passage ? (
                <HighlightablePassage content={question.passage.content} />
              ) : (
                <p className="font-sans text-sm text-exam-muted">No passage for this question.</p>
              )}
            </div>
            <div
              onMouseDown={startDragging}
              className={cn(
                "hidden lg:flex lg:h-full lg:w-2.5 lg:cursor-col-resize lg:items-center lg:justify-center",
                isDragging ? "bg-exam-blue/20" : "bg-transparent hover:bg-gray-100"
              )}
            >
              <span
                className={cn(
                  "flex h-8 w-3.5 items-center justify-center rounded-sm border text-gray-400",
                  isDragging ? "border-exam-blue bg-exam-blue text-white" : "border-exam-border bg-exam-card"
                )}
              >
                <GripVertical className="h-3 w-3" />
              </span>
            </div>
            <div className="bg-exam-card px-6 pb-6 pt-4 lg:h-full lg:overflow-y-auto lg:exam-scroll lg:px-8 lg:pb-8">
              <QuestionBody
                question={question}
                index={currentIndex}
                state={states[currentIndex]}
                flagged={!!states[currentIndex]?.flagged}
                crossOutEnabled={crossOutEnabled}
                onToggleCrossOutEnabled={() => setCrossOutEnabled((v) => !v)}
                onSelect={selectChoice}
                onToggleEliminate={toggleEliminated}
                onFreeResponseChange={(v) => updateCurrent({ freeResponseAnswer: v })}
                onToggleFlag={toggleFlag}
              />
            </div>
          </div>
        ) : (
          <div className="mx-auto h-full max-w-3xl overflow-y-auto exam-scroll bg-exam-card px-6 pb-8 pt-4 lg:px-10">
            <QuestionBody
              question={question}
              index={currentIndex}
              state={states[currentIndex]}
              flagged={!!states[currentIndex]?.flagged}
              crossOutEnabled={crossOutEnabled}
              onToggleCrossOutEnabled={() => setCrossOutEnabled((v) => !v)}
              onSelect={selectChoice}
              onToggleEliminate={toggleEliminated}
              onFreeResponseChange={(v) => updateCurrent({ freeResponseAnswer: v })}
              onToggleFlag={toggleFlag}
            />
          </div>
        )}
      </div>

      {/* Bottom toolbar */}
      <div className="shrink-0 border-t border-exam-border bg-exam-card">
        <div className="flex items-center justify-between gap-2 px-5 py-2">
          <p className="text-sm font-medium text-exam-text">{studentName}</p>

          <div className={cn("flex items-center divide-x rounded-md border border-exam-border divide-exam-border")}>
            <button
              type="button"
              onClick={() => goTo(currentIndex - 1)}
              disabled={currentIndex === 0}
              className={cn(
                "flex h-9 items-center gap-1 rounded-l-md px-3.5 text-sm font-medium text-exam-text hover:bg-gray-50 disabled:pointer-events-none disabled:opacity-30",
                FOCUS_RING
              )}
            >
              <ChevronLeft className="h-4 w-4" /> Back
            </button>
            <button
              type="button"
              onClick={() => setPaletteOpen(true)}
              className={cn(
                "flex h-9 items-center gap-1.5 px-3.5 text-sm font-medium text-exam-text hover:bg-gray-50",
                FOCUS_RING
              )}
            >
              <Grid3x3 className="h-3.5 w-3.5" />
              Question {currentIndex + 1} of {module.questions.length}
              <ChevronDown className="h-3.5 w-3.5" />
            </button>
            {currentIndex < module.questions.length - 1 ? (
              <button
                type="button"
                onClick={() => goTo(currentIndex + 1)}
                className={cn(
                  "flex h-9 items-center gap-1 rounded-r-md bg-exam-blue px-3.5 text-sm font-medium text-white hover:bg-exam-blueHover",
                  FOCUS_RING
                )}
              >
                Next <ChevronRight className="h-4 w-4" />
              </button>
            ) : (
              <button
                type="button"
                onClick={() => setReviewScreen(true)}
                className={cn(
                  "flex h-9 items-center rounded-r-md bg-exam-blue px-3.5 text-sm font-medium text-white hover:bg-exam-blueHover",
                  FOCUS_RING
                )}
              >
                Review &amp; submit
              </button>
            )}
          </div>
        </div>
      </div>

      <QuestionPalette
        open={paletteOpen}
        onOpenChange={setPaletteOpen}
        count={module.questions.length}
        currentIndex={currentIndex}
        states={states}
        onJump={goTo}
      />

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
  module,
  secondsRemaining,
  directionsOpen,
  onToggleDirections,
  onToggleCalculator,
  onOpenReference,
  zoomPct,
  onZoomChange,
  onSaveAndExit,
}: {
  module: ExamModule;
  secondsRemaining: number;
  directionsOpen: boolean;
  onToggleDirections: () => void;
  onToggleCalculator: () => void;
  onOpenReference: () => void;
  zoomPct: number;
  onZoomChange: (pct: number) => void;
  onSaveAndExit: () => void;
}) {
  const sectionNumber = module.subject === "READING_WRITING" ? 1 : 2;
  const subjectLabel = module.subject === "READING_WRITING" ? "Reading and Writing" : "Math";

  return (
    <header className="relative shrink-0 border-b border-exam-border bg-exam-bg text-exam-text">
      <div className="flex items-center justify-between px-4 py-1.5">
        <div className="leading-none">
          <p className="text-[13px] font-semibold leading-tight">
            Section {sectionNumber}, Module {module.order}: {subjectLabel}
          </p>
          <button
            type="button"
            onClick={onToggleDirections}
            className={cn("mt-0.5 flex items-center gap-0.5 text-xs text-exam-muted hover:text-exam-text", FOCUS_RING)}
          >
            Directions <ChevronDown className={cn("h-3 w-3 transition-transform", directionsOpen && "rotate-180")} />
          </button>
        </div>

        <div
          className={cn("font-mono text-base font-semibold tabular-nums", secondsRemaining < 300 && "text-destructive")}
        >
          {formatDuration(secondsRemaining)}
        </div>

        <div className="flex items-center gap-1">
          <div className="hidden items-center gap-0.5 rounded border border-exam-border bg-exam-card px-1 py-0.5 sm:flex">
            <button
              type="button"
              onClick={() => onZoomChange(Math.max(80, zoomPct - 10))}
              className={cn("flex h-5 w-5 items-center justify-center text-exam-muted hover:text-exam-text", FOCUS_RING)}
              title="Zoom out"
            >
              <Minus className="h-3 w-3" />
            </button>
            <span className="w-9 text-center text-xs font-medium tabular-nums text-exam-text">{zoomPct}%</span>
            <button
              type="button"
              onClick={() => onZoomChange(Math.min(150, zoomPct + 10))}
              className={cn("flex h-5 w-5 items-center justify-center text-exam-muted hover:text-exam-text", FOCUS_RING)}
              title="Zoom in"
            >
              <Plus className="h-3 w-3" />
            </button>
            {zoomPct !== 100 && (
              <button
                type="button"
                onClick={() => onZoomChange(100)}
                className={cn("ml-1 border-l border-exam-border pl-1.5 text-xs font-medium text-exam-muted hover:text-exam-text", FOCUS_RING)}
              >
                Reset
              </button>
            )}
          </div>
          {module.subject === "MATH" && (
            <>
              <Button variant="ghost" size="sm" className="h-7 px-2 text-exam-text hover:bg-gray-100" onClick={onToggleCalculator}>
                <Calculator className="h-3.5 w-3.5" /> Calculator
              </Button>
              <Button variant="ghost" size="sm" className="h-7 px-2 text-exam-text hover:bg-gray-100" onClick={onOpenReference}>
                <Ruler className="h-3.5 w-3.5" /> Reference
              </Button>
            </>
          )}
          <span className="hidden items-center gap-1 px-1.5 text-xs text-exam-muted sm:flex">
            <Highlighter className="h-3.5 w-3.5" /> Highlights &amp; Notes
          </span>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" size="icon" className="h-7 w-7 text-exam-text hover:bg-gray-100">
                <MoreVertical className="h-4 w-4" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
              <DropdownMenuItem onClick={onSaveAndExit}>
                <LogOut className="mr-2 h-4 w-4" /> Save &amp; exit
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>

      {directionsOpen && (
        <div className="absolute left-0 top-full z-30 m-2 w-[400px] max-w-[calc(100vw-1rem)] rounded-md border border-exam-border bg-exam-card p-4 text-sm leading-relaxed text-exam-text shadow-examFlat">
          <p>
            Read each passage and question carefully, then choose the best answer based on the passage(s) and any
            accompanying figures. Each question has a single best answer.
          </p>
          <p className="mt-2">
            You can flag a question to revisit later, cross out choices you&apos;ve ruled out, and move freely between
            questions in this module until you submit it.
          </p>
          <div className="mt-3 text-right">
            <Button size="sm" variant="outline" className="rounded-md" onClick={onToggleDirections}>
              Close
            </Button>
          </div>
        </div>
      )}
    </header>
  );
}

function QuestionBody({
  question,
  index,
  state,
  flagged,
  crossOutEnabled,
  onToggleCrossOutEnabled,
  onSelect,
  onToggleEliminate,
  onFreeResponseChange,
  onToggleFlag,
}: {
  question: ExamModule["questions"][number];
  index: number;
  state: QuestionState;
  flagged: boolean;
  crossOutEnabled: boolean;
  onToggleCrossOutEnabled: () => void;
  onSelect: (choiceId: string) => void;
  onToggleEliminate: (choiceId: string) => void;
  onFreeResponseChange: (value: string) => void;
  onToggleFlag: () => void;
}) {
  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between border-b border-exam-border pb-2">
        <div className="flex items-center gap-2.5">
          <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded bg-navy-950 text-xs font-semibold text-white">
            {index + 1}
          </span>
          <button
            type="button"
            onClick={onToggleFlag}
            className={cn(
              "flex items-center gap-1 text-sm font-medium",
              FOCUS_RING,
              flagged ? "text-warning-foreground" : "text-exam-muted hover:text-exam-text"
            )}
          >
            <Flag className={cn("h-3.5 w-3.5", flagged && "fill-warning text-warning")} />
            {flagged ? "Marked for Review" : "Mark for Review"}
          </button>
          {question.imageUrl && <span className="text-xs text-exam-muted">Includes a figure</span>}
        </div>
        {question.type === "MULTIPLE_CHOICE" && (
          <button
            type="button"
            onClick={onToggleCrossOutEnabled}
            title={crossOutEnabled ? "Hide answer eliminator" : "Show answer eliminator"}
            className={cn(
              "flex h-6 w-8 shrink-0 items-center justify-center rounded border text-xs font-bold",
              FOCUS_RING,
              crossOutEnabled
                ? "border-exam-blue bg-exam-blue text-white"
                : "border-exam-border bg-exam-card text-exam-muted hover:bg-gray-50"
            )}
          >
            <Strikethrough className="h-3.5 w-3.5" />
          </button>
        )}
      </div>
      <div
        className="font-sans text-[17px] leading-[1.6] text-exam-text"
        dangerouslySetInnerHTML={{ __html: question.stem }}
      />
      {question.imageUrl && (
        // eslint-disable-next-line @next/next/no-img-element
        <img src={question.imageUrl} alt="Question figure" className="max-w-full rounded border border-exam-border" />
      )}

      {question.type === "MULTIPLE_CHOICE" ? (
        <div className="space-y-2">
          {question.choices.map((choice) => {
            const eliminated = state.eliminated.includes(choice.id);
            const selected = state.selectedChoiceId === choice.id;
            return (
              <div key={choice.id} className="flex items-center gap-1.5">
                <button
                  type="button"
                  onClick={() => !eliminated && onSelect(choice.id)}
                  className={cn(
                    "flex flex-1 items-start gap-2.5 rounded-md border p-2.5 text-left font-sans text-[16px] leading-[1.5] transition-colors",
                    FOCUS_RING,
                    selected ? "border-exam-blue bg-white" : "border-exam-border bg-exam-card hover:bg-gray-50",
                    eliminated && "opacity-40"
                  )}
                >
                  <span
                    className={cn(
                      "flex h-5 w-5 shrink-0 items-center justify-center rounded-full border text-[11px] font-semibold",
                      selected ? "border-exam-blue bg-exam-blue text-white" : "border-gray-400 text-exam-text"
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
                    className={cn(
                      "flex h-7 w-7 shrink-0 items-center justify-center rounded-full border border-exam-border text-xs text-exam-muted hover:bg-gray-50",
                      FOCUS_RING
                    )}
                    title="Cross out this choice"
                  >
                    {eliminated ? <X className="h-3.5 w-3.5" /> : choice.label}
                  </button>
                )}
              </div>
            );
          })}
        </div>
      ) : (
        <div className="max-w-xs space-y-1.5">
          <Textarea
            value={state.freeResponseAnswer}
            onChange={(e) => onFreeResponseChange(e.target.value)}
            placeholder="Enter your answer"
            rows={1}
            className="rounded-md border-exam-border bg-exam-card"
          />
          <p className="text-xs text-exam-muted">Enter a numeric answer (fraction or decimal accepted).</p>
        </div>
      )}
    </div>
  );
}
