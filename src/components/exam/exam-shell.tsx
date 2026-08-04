"use client";

import { useCallback, useEffect, useMemo, useRef, useState, useTransition } from "react";
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
  MoreVertical,
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
  const [isSubmitting, startSubmit] = useTransition();

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

  // Autosave every 5 seconds.
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

  const answeredCount = useMemo(
    () => states.filter((s) => s.selectedChoiceId || s.freeResponseAnswer).length,
    [states]
  );

  if (reviewScreen) {
    return (
      <div className="flex h-screen flex-col bg-examCream">
        <ExamHeader
          module={module}
          secondsRemaining={secondsRemaining}
          directionsOpen={directionsOpen}
          onToggleDirections={() => setDirectionsOpen((v) => !v)}
          onToggleCalculator={() => setCalculatorOpen((v) => !v)}
          onOpenReference={() => setReferenceOpen(true)}
          onSaveAndExit={async () => {
            await persist();
            router.push("/dashboard");
          }}
        />
        <div className="mx-auto w-full max-w-3xl flex-1 space-y-6 overflow-y-auto p-8">
          <div>
            <h1 className="text-xl font-semibold text-navy-950">Review your answers</h1>
            <p className="text-sm text-navy-700">
              {answeredCount} of {module.questions.length} questions answered. You can still change any answer before
              submitting the module.
            </p>
          </div>
          <div className="grid grid-cols-6 gap-2 sm:grid-cols-10">
            {module.questions.map((q, i) => {
              const s = states[i];
              const answered = !!(s.selectedChoiceId || s.freeResponseAnswer);
              return (
                <button
                  key={q.id}
                  onClick={() => {
                    setReviewScreen(false);
                    goTo(i);
                  }}
                  className={cn(
                    "relative flex h-12 w-12 items-center justify-center rounded border text-sm font-semibold",
                    answered ? "border-navy-950 bg-navy-950 text-white" : "border-navy-300 bg-white text-navy-950"
                  )}
                >
                  {i + 1}
                  {s.flagged && <Flag className="absolute -right-1 -top-1 h-3.5 w-3.5 fill-warning text-warning" />}
                </button>
              );
            })}
          </div>
          <div className="flex justify-between">
            <Button
              variant="outline"
              className="rounded-full border-navy-950 text-navy-950 hover:bg-navy-950/5"
              onClick={() => setReviewScreen(false)}
            >
              <ChevronLeft className="h-4 w-4" /> Back to questions
            </Button>
            <Button
              className="rounded-full bg-navy-950 text-white hover:bg-navy-900"
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
    <div className="flex h-screen flex-col bg-examCream">
      <ExamHeader
        module={module}
        secondsRemaining={secondsRemaining}
        directionsOpen={directionsOpen}
        onToggleDirections={() => setDirectionsOpen((v) => !v)}
        onToggleCalculator={() => setCalculatorOpen((v) => !v)}
        onOpenReference={() => setReferenceOpen(true)}
        onSaveAndExit={async () => {
          await persist();
          router.push("/dashboard");
        }}
      />

      <div className="shrink-0 bg-navy-950 py-1.5 text-center text-xs font-semibold tracking-wide text-white">
        THIS IS A PRACTICE TEST
      </div>

      <div className="flex-1 overflow-y-auto">
        {module.subject === "READING_WRITING" ? (
          <div className="relative grid h-full lg:grid-cols-2">
            <div className="border-b border-navy-200 bg-examCream p-8 lg:border-b-0 lg:p-10 xl:p-14">
              {question.passage ? (
                <HighlightablePassage content={question.passage.content} />
              ) : (
                <p className="font-serif text-sm text-navy-700">No passage for this question.</p>
              )}
            </div>
            <div className="hidden lg:absolute lg:inset-y-0 lg:left-1/2 lg:flex lg:w-px lg:-translate-x-1/2 lg:items-center lg:justify-center lg:bg-navy-300">
              <span className="flex h-6 w-4 items-center justify-center rounded-sm border border-navy-400 bg-white text-navy-500">
                <GripVertical className="h-3.5 w-3.5" />
              </span>
            </div>
            <div className="bg-examCream p-8 lg:p-10 xl:p-14">
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
          <div className="mx-auto h-full max-w-3xl bg-examCream p-8 lg:p-14">
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
      <div className="shrink-0 border-t border-navy-200 bg-white">
        <div className="flex items-center justify-between gap-2 px-6 py-3">
          <p className="text-sm font-medium text-navy-950">{studentName}</p>

          <div className="flex items-center gap-3">
            <Button
              variant="outline"
              size="sm"
              className="rounded-full border-navy-950 text-navy-950 hover:bg-navy-950/5 disabled:opacity-30"
              onClick={() => goTo(currentIndex - 1)}
              disabled={currentIndex === 0}
            >
              <ChevronLeft className="h-4 w-4" /> Back
            </Button>
            <Button
              size="sm"
              className="gap-1.5 rounded-full bg-navy-950 px-4 text-white hover:bg-navy-900"
              onClick={() => setPaletteOpen(true)}
            >
              <Grid3x3 className="h-3.5 w-3.5" />
              Question {currentIndex + 1} of {module.questions.length}
              <ChevronDown className="h-3.5 w-3.5" />
            </Button>
            {currentIndex < module.questions.length - 1 ? (
              <Button
                size="sm"
                className="rounded-full bg-navy-950 text-white hover:bg-navy-900"
                onClick={() => goTo(currentIndex + 1)}
              >
                Next <ChevronRight className="h-4 w-4" />
              </Button>
            ) : (
              <Button
                size="sm"
                className="rounded-full bg-navy-950 text-white hover:bg-navy-900"
                onClick={() => setReviewScreen(true)}
              >
                Review &amp; submit
              </Button>
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
  onSaveAndExit,
}: {
  module: ExamModule;
  secondsRemaining: number;
  directionsOpen: boolean;
  onToggleDirections: () => void;
  onToggleCalculator: () => void;
  onOpenReference: () => void;
  onSaveAndExit: () => void;
}) {
  const sectionNumber = module.subject === "READING_WRITING" ? 1 : 2;
  const subjectLabel = module.subject === "READING_WRITING" ? "Reading and Writing" : "Math";

  return (
    <header className="relative shrink-0 border-b border-navy-200 bg-examCream text-navy-950">
      <div className="flex items-center justify-between px-6 py-3">
        <div>
          <p className="text-sm font-semibold leading-tight">
            Section {sectionNumber}, Module {module.order}: {subjectLabel}
          </p>
          <button
            type="button"
            onClick={onToggleDirections}
            className="flex items-center gap-1 text-xs text-navy-700 hover:text-navy-950"
          >
            Directions <ChevronDown className={cn("h-3 w-3 transition-transform", directionsOpen && "rotate-180")} />
          </button>
        </div>

        <div
          className={cn(
            "font-mono text-lg font-semibold tabular-nums",
            secondsRemaining < 300 && "text-destructive"
          )}
        >
          {formatDuration(secondsRemaining)}
        </div>

        <div className="flex items-center gap-1">
          {module.subject === "MATH" && (
            <>
              <Button variant="ghost" size="sm" className="text-navy-950 hover:bg-navy-950/5" onClick={onToggleCalculator}>
                <Calculator className="h-4 w-4" /> Calculator
              </Button>
              <Button variant="ghost" size="sm" className="text-navy-950 hover:bg-navy-950/5" onClick={onOpenReference}>
                <Ruler className="h-4 w-4" /> Reference
              </Button>
            </>
          )}
          <span className="hidden items-center gap-1 px-2 text-xs text-navy-500 sm:flex">
            <Highlighter className="h-3.5 w-3.5" /> Highlights &amp; Notes
          </span>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" size="icon" className="text-navy-950 hover:bg-navy-950/5">
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
        <div className="absolute left-0 top-full z-30 m-3 w-[420px] max-w-[calc(100vw-1.5rem)] rounded-lg border border-navy-200 bg-white p-5 text-sm leading-relaxed text-navy-950 shadow-panel">
          <p>
            Read each passage and question carefully, then choose the best answer based on the passage(s) and any
            accompanying figures. Each question has a single best answer.
          </p>
          <p className="mt-2">
            You can flag a question to revisit later, cross out choices you&apos;ve ruled out, and move freely between
            questions in this module until you submit it.
          </p>
          <div className="mt-3 text-right">
            <Button size="sm" variant="outline" className="rounded-full" onClick={onToggleDirections}>
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
    <div className="space-y-5">
      <div className="flex items-center justify-between border-b border-navy-200 pb-3">
        <div className="flex items-center gap-3">
          <span className="flex h-7 w-7 shrink-0 items-center justify-center rounded bg-navy-950 text-sm font-semibold text-white">
            {index + 1}
          </span>
          <button
            type="button"
            onClick={onToggleFlag}
            className={cn(
              "flex items-center gap-1.5 text-sm font-medium",
              flagged ? "text-warning-foreground" : "text-navy-700 hover:text-navy-950"
            )}
          >
            <Flag className={cn("h-4 w-4", flagged && "fill-warning text-warning")} />
            {flagged ? "Marked for Review" : "Mark for Review"}
          </button>
          {question.imageUrl && <span className="text-xs text-navy-700">Includes a figure</span>}
        </div>
        {question.type === "MULTIPLE_CHOICE" && (
          <button
            type="button"
            onClick={onToggleCrossOutEnabled}
            title={crossOutEnabled ? "Hide answer eliminator" : "Show answer eliminator"}
            className={cn(
              "flex h-7 w-9 shrink-0 items-center justify-center rounded border text-xs font-bold",
              crossOutEnabled
                ? "border-navy-950 bg-navy-950 text-white"
                : "border-navy-300 bg-white text-navy-700 hover:bg-navy-50"
            )}
          >
            <Strikethrough className="h-3.5 w-3.5" />
          </button>
        )}
      </div>
      <div
        className="font-serif text-[16px] leading-relaxed text-navy-950"
        dangerouslySetInnerHTML={{ __html: question.stem }}
      />
      {question.imageUrl && (
        // eslint-disable-next-line @next/next/no-img-element
        <img src={question.imageUrl} alt="Question figure" className="max-w-full rounded-lg border border-navy-200" />
      )}

      {question.type === "MULTIPLE_CHOICE" ? (
        <div className="space-y-3">
          {question.choices.map((choice) => {
            const eliminated = state.eliminated.includes(choice.id);
            const selected = state.selectedChoiceId === choice.id;
            return (
              <div key={choice.id} className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={() => !eliminated && onSelect(choice.id)}
                  className={cn(
                    "flex flex-1 items-start gap-3 rounded-lg border p-3 text-left font-serif text-[15px] transition-colors",
                    selected ? "border-navy-950 bg-navy-50" : "border-navy-300 bg-white hover:bg-navy-50/50",
                    eliminated && "opacity-40"
                  )}
                >
                  <span
                    className={cn(
                      "flex h-6 w-6 shrink-0 items-center justify-center rounded-full border text-xs font-semibold",
                      selected ? "border-navy-950 bg-navy-950 text-white" : "border-navy-400 text-navy-950"
                    )}
                  >
                    {choice.label}
                  </span>
                  <span className={cn("text-navy-950", eliminated && "line-through")}>{choice.content}</span>
                </button>
                {crossOutEnabled && (
                  <button
                    type="button"
                    onClick={() => onToggleEliminate(choice.id)}
                    className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-navy-300 text-xs text-navy-700 hover:bg-navy-50"
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
            className="border-navy-300 bg-white"
          />
          <p className="text-xs text-navy-700">Enter a numeric answer (fraction or decimal accepted).</p>
        </div>
      )}
    </div>
  );
}
