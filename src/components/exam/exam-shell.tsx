"use client";

import { useCallback, useEffect, useMemo, useRef, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import {
  Calculator,
  ChevronLeft,
  ChevronRight,
  Flag,
  GraduationCap,
  Grid3x3,
  Ruler,
  X,
} from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
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
  testTitle,
  moduleAttemptId,
  module,
  startedAt,
  existingResponses,
}: {
  attemptId: string;
  testTitle: string;
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
      <div className="flex min-h-screen flex-col bg-secondary/30">
        <ExamHeader
          testTitle={testTitle}
          module={module}
          secondsRemaining={secondsRemaining}
          onToggleCalculator={() => setCalculatorOpen((v) => !v)}
          onOpenReference={() => setReferenceOpen(true)}
        />
        <div className="mx-auto w-full max-w-3xl flex-1 space-y-6 p-6">
          <div>
            <h1 className="font-display text-xl font-semibold">Review your answers</h1>
            <p className="text-sm text-muted-foreground">
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
                    "relative flex h-12 w-12 items-center justify-center rounded-lg border text-sm font-semibold",
                    answered ? "border-success/40 bg-success/10 text-success" : "border-border bg-background"
                  )}
                >
                  {i + 1}
                  {s.flagged && <Flag className="absolute -right-1 -top-1 h-3.5 w-3.5 fill-warning text-warning" />}
                </button>
              );
            })}
          </div>
          <div className="flex justify-between">
            <Button variant="outline" onClick={() => setReviewScreen(false)}>
              <ChevronLeft className="h-4 w-4" /> Back to questions
            </Button>
            <Button onClick={handleSubmitModule} disabled={isSubmitting}>
              Submit module <ChevronRight className="h-4 w-4" />
            </Button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen flex-col bg-background">
      <ExamHeader
        testTitle={testTitle}
        module={module}
        secondsRemaining={secondsRemaining}
        onToggleCalculator={() => setCalculatorOpen((v) => !v)}
        onOpenReference={() => setReferenceOpen(true)}
      />

      <div className="flex-1 overflow-y-auto pb-24">
        {module.subject === "READING_WRITING" ? (
          <div className="mx-auto grid max-w-6xl gap-0 lg:grid-cols-2">
            <div className="border-b border-border p-6 lg:border-b-0 lg:border-r">
              {question.passage ? (
                <HighlightablePassage content={question.passage.content} />
              ) : (
                <p className="text-sm text-muted-foreground">No passage for this question.</p>
              )}
            </div>
            <div className="p-6">
              <QuestionBody
                question={question}
                index={currentIndex}
                state={states[currentIndex]}
                onSelect={selectChoice}
                onToggleEliminate={toggleEliminated}
                onFreeResponseChange={(v) => updateCurrent({ freeResponseAnswer: v })}
              />
            </div>
          </div>
        ) : (
          <div className="mx-auto max-w-2xl p-6">
            <QuestionBody
              question={question}
              index={currentIndex}
              state={states[currentIndex]}
              onSelect={selectChoice}
              onToggleEliminate={toggleEliminated}
              onFreeResponseChange={(v) => updateCurrent({ freeResponseAnswer: v })}
            />
          </div>
        )}
      </div>

      {/* Bottom toolbar */}
      <div className="fixed inset-x-0 bottom-0 z-30 border-t border-border bg-background/95 backdrop-blur">
        <div className="mx-auto flex max-w-6xl items-center justify-between gap-2 px-4 py-3">
          <Button
            variant={states[currentIndex]?.flagged ? "default" : "outline"}
            size="sm"
            onClick={toggleFlag}
          >
            <Flag className="h-4 w-4" /> {states[currentIndex]?.flagged ? "Flagged" : "Mark for review"}
          </Button>

          <div className="flex items-center gap-2">
            <Button variant="outline" size="sm" onClick={() => goTo(currentIndex - 1)} disabled={currentIndex === 0}>
              <ChevronLeft className="h-4 w-4" /> Back
            </Button>
            <Button variant="outline" size="sm" onClick={() => setPaletteOpen(true)}>
              <Grid3x3 className="h-4 w-4" />
              {currentIndex + 1} / {module.questions.length}
            </Button>
            {currentIndex < module.questions.length - 1 ? (
              <Button size="sm" onClick={() => goTo(currentIndex + 1)}>
                Next <ChevronRight className="h-4 w-4" />
              </Button>
            ) : (
              <Button size="sm" onClick={() => setReviewScreen(true)}>
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
  testTitle,
  module,
  secondsRemaining,
  onToggleCalculator,
  onOpenReference,
}: {
  testTitle: string;
  module: ExamModule;
  secondsRemaining: number;
  onToggleCalculator: () => void;
  onOpenReference: () => void;
}) {
  return (
    <header className="sticky top-0 z-20 border-b border-border bg-navy-950 text-white">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3">
        <div className="flex items-center gap-2">
          <span className="flex h-7 w-7 items-center justify-center rounded-md bg-white/10">
            <GraduationCap className="h-4 w-4" />
          </span>
          <div>
            <p className="text-sm font-medium leading-tight">{testTitle}</p>
            <p className="text-xs text-navy-300">
              {module.subject === "READING_WRITING" ? "Reading & Writing" : "Math"} · Module {module.order}
            </p>
          </div>
        </div>

        <div
          className={cn(
            "rounded-full px-4 py-1.5 font-mono text-sm font-semibold",
            secondsRemaining < 300 ? "bg-destructive/20 text-red-200" : "bg-white/10"
          )}
        >
          {formatDuration(secondsRemaining)}
        </div>

        <div className="flex items-center gap-2">
          {module.subject === "MATH" && (
            <>
              <Button
                variant="ghost"
                size="sm"
                className="text-white hover:bg-white/10 hover:text-white"
                onClick={onToggleCalculator}
              >
                <Calculator className="h-4 w-4" /> Calculator
              </Button>
              <Button
                variant="ghost"
                size="sm"
                className="text-white hover:bg-white/10 hover:text-white"
                onClick={onOpenReference}
              >
                <Ruler className="h-4 w-4" /> Reference
              </Button>
            </>
          )}
        </div>
      </div>
    </header>
  );
}

function QuestionBody({
  question,
  index,
  state,
  onSelect,
  onToggleEliminate,
  onFreeResponseChange,
}: {
  question: ExamModule["questions"][number];
  index: number;
  state: QuestionState;
  onSelect: (choiceId: string) => void;
  onToggleEliminate: (choiceId: string) => void;
  onFreeResponseChange: (value: string) => void;
}) {
  return (
    <div className="space-y-5">
      <div className="flex items-center gap-2">
        <Badge variant="navy">{index + 1}</Badge>
        {question.imageUrl && <span className="text-xs text-muted-foreground">Includes a figure</span>}
      </div>
      <div className="text-[15px] leading-relaxed" dangerouslySetInnerHTML={{ __html: question.stem }} />
      {question.imageUrl && (
        // eslint-disable-next-line @next/next/no-img-element
        <img src={question.imageUrl} alt="Question figure" className="max-w-full rounded-lg border border-border" />
      )}

      {question.type === "MULTIPLE_CHOICE" ? (
        <div className="space-y-2.5">
          {question.choices.map((choice) => {
            const eliminated = state.eliminated.includes(choice.id);
            const selected = state.selectedChoiceId === choice.id;
            return (
              <div key={choice.id} className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={() => !eliminated && onSelect(choice.id)}
                  className={cn(
                    "flex flex-1 items-start gap-3 rounded-lg border p-3 text-left text-sm transition-colors",
                    selected ? "border-primary bg-accent" : "border-border hover:bg-secondary",
                    eliminated && "opacity-40"
                  )}
                >
                  <span
                    className={cn(
                      "flex h-6 w-6 shrink-0 items-center justify-center rounded-full border text-xs font-semibold",
                      selected ? "border-primary bg-primary text-primary-foreground" : "border-muted-foreground"
                    )}
                  >
                    {choice.label}
                  </span>
                  <span className={cn(eliminated && "line-through")}>{choice.content}</span>
                </button>
                <button
                  type="button"
                  onClick={() => onToggleEliminate(choice.id)}
                  className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-border text-xs text-muted-foreground hover:bg-secondary"
                  title="Cross out this choice"
                >
                  {eliminated ? <X className="h-3.5 w-3.5" /> : choice.label}
                </button>
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
          />
          <p className="text-xs text-muted-foreground">Enter a numeric answer (fraction or decimal accepted).</p>
        </div>
      )}
    </div>
  );
}
