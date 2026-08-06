"use client";

import { memo, useCallback, useMemo, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { AlertTriangle, Check, Loader2, Plus, Save, Trash2, Upload } from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { ImageUploadField } from "@/components/admin/image-upload-field";
import { RichTextField } from "@/components/admin/rich-text-field";
import { cn } from "@/lib/utils";
import { isNextRedirectError } from "@/lib/next-redirect";
import { publishTestUpload, publishVocabUpload, updateExtractedData } from "@/server/actions/admin/uploads";
import type {
  ExtractedPassage,
  ExtractedQuestion,
  ExtractedVocabWord,
  TestExtractionResult,
  VocabExtractionResult,
} from "@/lib/ai/types";
import { CONFIDENCE_PUBLISH_THRESHOLD } from "@/lib/constants";

function ConfidenceBadge({ value }: { value: number }) {
  const pct = Math.round(value * 100);
  const variant = value >= CONFIDENCE_PUBLISH_THRESHOLD ? "success" : value >= 0.5 ? "warning" : "destructive";
  return <Badge variant={variant as never}>{pct}% confidence</Badge>;
}

type Subject = "READING_WRITING" | "MATH";

interface DomainOption {
  id: string;
  name: string;
  subject: Subject;
  skills: { id: string; name: string }[];
}

interface ExistingTestOption {
  id: string;
  title: string;
  modules: { subject: Subject; order: number; difficulty: "STANDARD" | "EASY" | "HARD" }[];
}

export function ExtractionReview({
  uploadId,
  jobId,
  category,
  confidence,
  data,
  alreadyPublished,
  domains,
  existingTests,
  initialTargetTestId,
  initialSubject,
  initialModuleSlot,
}: {
  uploadId: string;
  jobId: string;
  category: "FULL_TEST" | "QUESTION_BANK" | "VOCABULARY";
  confidence: number;
  data: TestExtractionResult | VocabExtractionResult;
  alreadyPublished: boolean;
  domains: DomainOption[];
  existingTests: ExistingTestOption[];
  initialTargetTestId?: string;
  initialSubject?: "READING_WRITING" | "MATH";
  initialModuleSlot?: string;
}) {
  if (category === "VOCABULARY") {
    return (
      <VocabReview
        uploadId={uploadId}
        jobId={jobId}
        confidence={confidence}
        initial={data as VocabExtractionResult}
        alreadyPublished={alreadyPublished}
      />
    );
  }
  return (
    <TestReview
      uploadId={uploadId}
      jobId={jobId}
      category={category}
      confidence={confidence}
      initial={data as TestExtractionResult}
      alreadyPublished={alreadyPublished}
      domains={domains}
      existingTests={existingTests}
      initialTargetTestId={initialTargetTestId}
      initialSubject={initialSubject}
      initialModuleSlot={initialModuleSlot}
    />
  );
}

// ---------------------------------------------------------------------------
// Test / question bank review
// ---------------------------------------------------------------------------

function guessDomainId(domains: DomainOption[], subject: Subject, guess?: string | null) {
  const candidates = domains.filter((d) => d.subject === subject);
  if (!candidates.length) return "";
  if (guess) {
    const g = guess.toLowerCase();
    const found = candidates.find((d) => d.name.toLowerCase().includes(g) || g.includes(d.name.toLowerCase()));
    if (found) return found.id;
  }
  return candidates[0].id;
}

function guessSkillId(domain: DomainOption | undefined, guess?: string | null) {
  if (!domain) return "";
  if (guess) {
    const g = guess.toLowerCase();
    const found = domain.skills.find((s) => s.name.toLowerCase().includes(g) || g.includes(s.name.toLowerCase()));
    if (found) return found.id;
  }
  return domain.skills[0]?.id ?? "";
}

// Only fills in a guessed domain/skill when the question doesn't already carry
// an admin-confirmed one (e.g. loaded from a previously saved draft) or when
// the previous value belongs to a domain outside the newly selected subject.
//
// Question Bank uploads skip this guessing entirely (see `requireExplicitTaxonomy`
// below): those questions go straight into student-facing practice, standalone,
// with no test/module context to catch a wrong guess later, so the admin must
// pick the domain, subtopic, and difficulty explicitly rather than have an
// AI guess silently stand in for a real decision.
function withTaxonomyDefaults(
  questions: ExtractedQuestion[],
  domains: DomainOption[],
  subject: Subject,
  guess: boolean
): ExtractedQuestion[] {
  const subjectDomainIds = new Set(domains.filter((d) => d.subject === subject).map((d) => d.id));
  return questions.map((q) => {
    if (q.domainId && subjectDomainIds.has(q.domainId) && q.skillId) return q;
    if (!guess) return { ...q, domainId: null, skillId: null };
    const domainId = guessDomainId(domains, subject, q.domainGuess);
    const skillId = guessSkillId(
      domains.find((d) => d.id === domainId),
      q.skillGuess
    );
    return { ...q, domainId, skillId };
  });
}

const MODULE_SLOTS = [
  { value: "1", label: "Module 1", order: 1 as const, difficulty: "STANDARD" as const },
  { value: "2E", label: "Module 2 — Easy", order: 2 as const, difficulty: "EASY" as const },
  { value: "2H", label: "Module 2 — Hard", order: 2 as const, difficulty: "HARD" as const },
];

function TestReview({
  uploadId,
  jobId,
  category,
  confidence,
  initial,
  alreadyPublished,
  domains,
  existingTests,
  initialTargetTestId,
  initialSubject,
  initialModuleSlot,
}: {
  uploadId: string;
  jobId: string;
  category: "FULL_TEST" | "QUESTION_BANK" | "VOCABULARY";
  confidence: number;
  initial: TestExtractionResult;
  alreadyPublished: boolean;
  domains: DomainOption[];
  existingTests: ExistingTestOption[];
  initialTargetTestId?: string;
  initialSubject?: Subject;
  initialModuleSlot?: string;
}) {
  const router = useRouter();
  const requireExplicitTaxonomy = category === "QUESTION_BANK";
  const [subject, setSubject] = useState<Subject>(initialSubject ?? "READING_WRITING");
  const [questions, setQuestions] = useState<ExtractedQuestion[]>(() =>
    withTaxonomyDefaults(initial.questions, domains, initialSubject ?? "READING_WRITING", !requireExplicitTaxonomy)
  );
  const [passages, setPassages] = useState<ExtractedPassage[]>(initial.passages);
  const [moduleSlot, setModuleSlot] = useState(initialModuleSlot ?? "1");
  const [thresholdPct, setThresholdPct] = useState("");
  const [targetTestId, setTargetTestId] = useState(initialTargetTestId ?? "new");
  const [isSaving, startSave] = useTransition();
  const [isPublishing, startPublish] = useTransition();
  const [confirmOpen, setConfirmOpen] = useState(false);

  const isFullTest = category === "FULL_TEST";
  const slot = MODULE_SLOTS.find((s) => s.value === moduleSlot) ?? MODULE_SLOTS[0];
  const subjectDomains = useMemo(() => domains.filter((d) => d.subject === subject), [domains, subject]);

  const compatibleTests = useMemo(
    () =>
      existingTests.filter(
        (t) => !t.modules.some((m) => m.subject === subject && m.order === slot.order && m.difficulty === slot.difficulty)
      ),
    [existingTests, subject, slot]
  );

  const lowConfidenceCount = useMemo(
    () => questions.filter((q) => q.confidence < CONFIDENCE_PUBLISH_THRESHOLD).length,
    [questions]
  );

  const missingTaxonomyCount = useMemo(
    () => (requireExplicitTaxonomy ? questions.filter((q) => !q.domainId || !q.skillId).length : 0),
    [questions, requireExplicitTaxonomy]
  );

  // Domain -> subtopic -> difficulty breakdown shown in the pre-publish
  // confirmation dialog for Question Bank uploads, so the admin sees exactly
  // what they're about to commit before it becomes practiceable.
  const taxonomySummary = useMemo(() => {
    if (!requireExplicitTaxonomy) return [];
    const rows = new Map<string, { domain: string; skill: string; difficulty: string; count: number }>();
    for (const q of questions) {
      const domain = subjectDomains.find((d) => d.id === q.domainId);
      const skill = domain?.skills.find((s) => s.id === q.skillId);
      const key = `${domain?.name ?? "?"}__${skill?.name ?? "?"}__${q.difficultyGuess}`;
      const row = rows.get(key);
      if (row) row.count += 1;
      else rows.set(key, { domain: domain?.name ?? "?", skill: skill?.name ?? "?", difficulty: q.difficultyGuess, count: 1 });
    }
    return Array.from(rows.values());
  }, [questions, subjectDomains, requireExplicitTaxonomy]);

  // One continuous review order: each passage appears once, immediately
  // before the first question that references it, so a passage and its
  // questions can be reviewed together in a single pass instead of jumping
  // between a "Passages" section and a separate "Questions" section far
  // below it. Passages no question points to (extraction gaps, or a passage
  // meant for a question that got deleted) still show up, up front, rather
  // than silently vanishing.
  const reviewBlocks = useMemo(() => {
    const shown = new Set<number>();
    const blocks: ({ type: "passage"; pIndex: number } | { type: "question"; qIndex: number })[] = [];
    questions.forEach((q, qIndex) => {
      const pIndex = q.passageIndex;
      if (pIndex !== null && pIndex !== undefined && passages[pIndex] && !shown.has(pIndex)) {
        blocks.push({ type: "passage", pIndex });
        shown.add(pIndex);
      }
      blocks.push({ type: "question", qIndex });
    });
    const orphanPassages = passages
      .map((_, pIndex) => pIndex)
      .filter((pIndex) => !shown.has(pIndex))
      .map((pIndex) => ({ type: "passage" as const, pIndex }));
    return [...orphanPassages, ...blocks];
  }, [questions, passages]);

  function changeSubject(next: Subject) {
    setSubject(next);
    setQuestions((prev) => withTaxonomyDefaults(prev, domains, next, !requireExplicitTaxonomy));
    setTargetTestId("new");
  }

  // Stable (empty-dep) callbacks: each only reaches into state through the
  // functional-update form, so identity never needs to change across
  // renders. That stability is what lets QuestionCard/PassageCard below be
  // memoized — without it, every keystroke in any one card would re-render
  // all thirty, since a fresh `questions` array is created on every edit.
  const updateQuestion = useCallback((index: number, patch: Partial<ExtractedQuestion>) => {
    setQuestions((prev) => prev.map((q, i) => (i === index ? { ...q, ...patch } : q)));
  }, []);

  const updateChoice = useCallback(
    (qIndex: number, cIndex: number, patch: Partial<ExtractedQuestion["choices"][number]>) => {
      setQuestions((prev) =>
        prev.map((q, i) =>
          i === qIndex
            ? { ...q, choices: q.choices.map((c, j) => (j === cIndex ? { ...c, ...patch } : c)) }
            : q
        )
      );
    },
    []
  );

  const setCorrectChoice = useCallback((qIndex: number, label: string) => {
    setQuestions((prev) =>
      prev.map((q, i) =>
        i === qIndex ? { ...q, choices: q.choices.map((c) => ({ ...c, isCorrect: c.label === label })) } : q
      )
    );
  }, []);

  const removeQuestion = useCallback((index: number) => {
    setQuestions((prev) => prev.filter((_, i) => i !== index));
  }, []);

  const addChoice = useCallback((qIndex: number) => {
    setQuestions((prev) =>
      prev.map((q, i) =>
        i === qIndex
          ? { ...q, choices: [...q.choices, { label: "ABCD"[q.choices.length], content: "", isCorrect: false }] }
          : q
      )
    );
  }, []);

  const removeChoice = useCallback((qIndex: number, cIndex: number) => {
    setQuestions((prev) =>
      prev.map((q, i) =>
        i === qIndex
          ? {
              ...q,
              // Relabel remaining choices A, B, C... so labels stay contiguous after a removal.
              choices: q.choices.filter((_, j) => j !== cIndex).map((c, j) => ({ ...c, label: "ABCD"[j] })),
            }
          : q
      )
    );
  }, []);

  const updatePassage = useCallback((index: number, patch: Partial<ExtractedPassage>) => {
    setPassages((prev) => prev.map((p, i) => (i === index ? { ...p, ...patch } : p)));
  }, []);

  function saveDraft() {
    startSave(async () => {
      try {
        await updateExtractedData(jobId, { ...initial, questions, passages });
        toast.success("Draft saved.");
      } catch (error) {
        toast.error(error instanceof Error ? error.message : "Couldn't save the draft.");
      }
    });
  }

  function publish() {
    startPublish(async () => {
      try {
        await updateExtractedData(jobId, { ...initial, questions, passages });
        await publishTestUpload(uploadId, {
          subject,
          order: slot.order,
          difficulty: slot.difficulty,
          thresholdPct: thresholdPct.trim() ? Number(thresholdPct) : null,
          targetTestId: targetTestId === "new" ? null : targetTestId,
        });
        toast.success(
          requireExplicitTaxonomy
            ? "Published to the Question Bank."
            : targetTestId === "new"
              ? "Published as a new test."
              : "Module added to the test."
        );
        router.refresh();
      } catch (error) {
        // publishTestUpload redirects to the new test on success, which Next
        // implements by throwing — that must propagate, not be swallowed as
        // a failure toast (the mistake this whole fix exists to avoid).
        if (isNextRedirectError(error)) throw error;
        toast.error(
          error instanceof Error
            ? error.message
            : "Couldn't publish this module. Your edits above are still here — fix the issue and try again."
        );
      }
    });
  }

  return (
    <div className="space-y-6">
      <Card>
        <CardContent className="flex flex-wrap items-center justify-between gap-4 p-6">
          <div className="flex items-center gap-3">
            <ConfidenceBadge value={confidence} />
            <span className="text-sm text-muted-foreground">{questions.length} questions extracted</span>
            {lowConfidenceCount > 0 && (
              <span className="flex items-center gap-1 text-sm text-warning-foreground">
                <AlertTriangle className="h-3.5 w-3.5" /> {lowConfidenceCount} need review
              </span>
            )}
          </div>
          {!alreadyPublished && (
            <div className="flex flex-wrap items-center gap-2">
              <Select value={subject} onValueChange={(v) => changeSubject(v as Subject)}>
                <SelectTrigger className="w-44">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="READING_WRITING">Reading & Writing</SelectItem>
                  <SelectItem value="MATH">Math</SelectItem>
                </SelectContent>
              </Select>

              {isFullTest && (
                <Select value={moduleSlot} onValueChange={setModuleSlot}>
                  <SelectTrigger className="w-44">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    {MODULE_SLOTS.map((s) => (
                      <SelectItem key={s.value} value={s.value}>
                        {s.label}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              )}

              {isFullTest && slot.order === 1 && (
                <Input
                  type="number"
                  min={0}
                  max={100}
                  placeholder="Threshold % (default 70)"
                  value={thresholdPct}
                  onChange={(e) => setThresholdPct(e.target.value)}
                  className="w-44"
                />
              )}

              {isFullTest && (
                <Select value={targetTestId} onValueChange={setTargetTestId}>
                  <SelectTrigger className="w-56">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="new">Create new test</SelectItem>
                    {compatibleTests.map((t) => (
                      <SelectItem key={t.id} value={t.id}>
                        Add to: {t.title}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              )}

              <Button variant="outline" onClick={saveDraft} disabled={isSaving}>
                {isSaving ? <Loader2 className="h-4 w-4 animate-spin" /> : <Save className="h-4 w-4" />}
                Save draft
              </Button>
              <Button
                onClick={requireExplicitTaxonomy ? () => setConfirmOpen(true) : publish}
                disabled={isPublishing || questions.length === 0 || (requireExplicitTaxonomy && missingTaxonomyCount > 0)}
                title={
                  requireExplicitTaxonomy && missingTaxonomyCount > 0
                    ? `${missingTaxonomyCount} question${missingTaxonomyCount === 1 ? "" : "s"} still need a domain, subtopic, and difficulty`
                    : undefined
                }
              >
                {isPublishing ? <Loader2 className="h-4 w-4 animate-spin" /> : <Upload className="h-4 w-4" />}
                {requireExplicitTaxonomy
                  ? "Publish to Question Bank"
                  : targetTestId === "new"
                    ? "Publish as new test"
                    : "Add to test"}
              </Button>
            </div>
          )}
        </CardContent>
      </Card>

      {requireExplicitTaxonomy && missingTaxonomyCount > 0 && (
        <p className="-mt-3 flex items-center gap-1.5 text-xs text-warning-foreground">
          <AlertTriangle className="h-3.5 w-3.5 shrink-0" />
          {missingTaxonomyCount} question{missingTaxonomyCount === 1 ? "" : "s"} below still need a domain and
          subtopic chosen before this can go to the Question Bank — pick one from each question&apos;s Domain and
          Skill dropdowns.
        </p>
      )}

      {requireExplicitTaxonomy && (
        <Dialog open={confirmOpen} onOpenChange={setConfirmOpen}>
          <DialogContent>
            <DialogHeader>
              <DialogTitle>Confirm before publishing to the Question Bank</DialogTitle>
              <DialogDescription>
                These {questions.length} question{questions.length === 1 ? "" : "s"} will become individually
                practiceable by students immediately. Double-check the domain, subtopic, and difficulty breakdown
                below.
              </DialogDescription>
            </DialogHeader>
            <div className="max-h-80 space-y-1.5 overflow-y-auto">
              {taxonomySummary.map((row, i) => (
                <div
                  key={i}
                  className="flex items-center justify-between rounded-md border border-border px-3 py-2 text-sm"
                >
                  <span>
                    <span className="font-medium">{row.domain}</span>
                    <span className="text-muted-foreground"> · {row.skill}</span>
                  </span>
                  <span className="flex items-center gap-2">
                    <Badge variant="outline">{row.difficulty}</Badge>
                    <span className="text-xs text-muted-foreground">
                      {row.count} question{row.count === 1 ? "" : "s"}
                    </span>
                  </span>
                </div>
              ))}
            </div>
            <DialogFooter>
              <Button variant="outline" onClick={() => setConfirmOpen(false)}>
                Go back and edit
              </Button>
              <Button
                onClick={() => {
                  setConfirmOpen(false);
                  publish();
                }}
                disabled={isPublishing}
              >
                {isPublishing ? <Loader2 className="h-4 w-4 animate-spin" /> : <Upload className="h-4 w-4" />}
                Confirm & publish
              </Button>
            </DialogFooter>
          </DialogContent>
        </Dialog>
      )}

      {isFullTest && slot.order === 1 && (
        <p className="-mt-3 text-xs text-muted-foreground">
          Routing threshold: the % of Module 1 questions a student must answer correctly to be routed into the
          Hard Module 2 instead of Easy. Leave blank to use the test-wide adaptive default (70%).
        </p>
      )}

      {initial.warnings.length > 0 && (
        <Card className="border-warning/40 bg-warning/5">
          <CardContent className="space-y-1 p-4 text-sm">
            {initial.warnings.map((w, i) => (
              <p key={i} className="text-warning-foreground">
                {w}
              </p>
            ))}
          </CardContent>
        </Card>
      )}

      <div className="space-y-4">
        {reviewBlocks.map((block) =>
          block.type === "passage" ? (
            <PassageCard
              key={`p-${block.pIndex}`}
              passage={passages[block.pIndex]}
              pIndex={block.pIndex}
              onUpdate={updatePassage}
            />
          ) : (
            <QuestionCard
              key={`q-${block.qIndex}`}
              question={questions[block.qIndex]}
              qIndex={block.qIndex}
              subjectDomains={subjectDomains}
              onUpdateQuestion={updateQuestion}
              onUpdateChoice={updateChoice}
              onSetCorrectChoice={setCorrectChoice}
              onRemoveQuestion={removeQuestion}
              onAddChoice={addChoice}
              onRemoveChoice={removeChoice}
            />
          )
        )}
      </div>
    </div>
  );
}

// A card holds a real (rich text, image upload) child field per question, so
// re-rendering all thirty on every keystroke anywhere on the page is not
// free — memoized so only the card actually being edited re-renders. This
// depends on every callback prop below having stable identity (see the
// useCallback-wrapped updaters in TestReview).
const PassageCard = memo(function PassageCard({
  passage,
  pIndex,
  onUpdate,
}: {
  passage: ExtractedPassage;
  pIndex: number;
  onUpdate: (index: number, patch: Partial<ExtractedPassage>) => void;
}) {
  return (
    <Card className="border-primary/30 bg-primary/[0.02]">
      <CardHeader className="pb-2">
        <CardTitle className="text-sm font-semibold text-muted-foreground">Passage</CardTitle>
      </CardHeader>
      <CardContent className="space-y-2 p-4 pt-0">
        <Input
          value={passage.title ?? ""}
          onChange={(e) => onUpdate(pIndex, { title: e.target.value })}
          placeholder="Passage title (optional)"
          className="h-8 font-medium"
        />
        <RichTextField
          value={passage.content}
          onChange={(v) => onUpdate(pIndex, { content: v })}
          rows={6}
          placeholder="Passage text"
        />
        <p className="text-xs text-muted-foreground">
          Select the exact wording that&apos;s underlined in the source PDF and click &quot;Underline
          selection&quot; — plain text extraction can&apos;t recover that formatting automatically.
        </p>
      </CardContent>
    </Card>
  );
});

const QuestionCard = memo(function QuestionCard({
  question: q,
  qIndex,
  subjectDomains,
  onUpdateQuestion,
  onUpdateChoice,
  onSetCorrectChoice,
  onRemoveQuestion,
  onAddChoice,
  onRemoveChoice,
}: {
  question: ExtractedQuestion;
  qIndex: number;
  subjectDomains: DomainOption[];
  onUpdateQuestion: (index: number, patch: Partial<ExtractedQuestion>) => void;
  onUpdateChoice: (qIndex: number, cIndex: number, patch: Partial<ExtractedQuestion["choices"][number]>) => void;
  onSetCorrectChoice: (qIndex: number, label: string) => void;
  onRemoveQuestion: (index: number) => void;
  onAddChoice: (qIndex: number) => void;
  onRemoveChoice: (qIndex: number, cIndex: number) => void;
}) {
  // Collapsed unless extraction already found explanation text, so reviewing
  // a batch of questions doesn't mean scrolling past thirty empty boxes for
  // a field most PDFs don't even include.
  const [explanationOpen, setExplanationOpen] = useState(!!q.explanation?.trim());

  // A MULTIPLE_CHOICE question that publishes without exactly 4 real
  // choices and one marked correct is unanswerable for a student -- this
  // is checked here so the admin sees it before hitting Publish, where the
  // same rule is enforced server-side as a hard block (uploads.ts).
  const hasBadChoices =
    q.type === "MULTIPLE_CHOICE" &&
    (q.choices.length !== 4 ||
      q.choices.some((c) => !c.content.trim()) ||
      q.choices.filter((c) => c.isCorrect).length !== 1);
  // hasImage is only a guess from extraction (it can be a false positive),
  // so this is a warning the admin can judge and dismiss by attaching an
  // image below -- never a hard block.
  const needsDiagram = q.hasImage && !q.imageUrl;

  return (
    <Card
      className={cn(
        (q.confidence < CONFIDENCE_PUBLISH_THRESHOLD || hasBadChoices) && "border-warning/50",
        hasBadChoices && "border-destructive/60"
      )}
    >
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-3">
        <CardTitle className="text-sm font-semibold text-muted-foreground">Question {q.number}</CardTitle>
        <div className="flex items-center gap-2">
          {hasBadChoices && (
            <Badge variant="destructive">
              <AlertTriangle className="h-3.5 w-3.5" /> Missing choices
            </Badge>
          )}
          {needsDiagram && (
            <Badge variant="warning">
              <AlertTriangle className="h-3.5 w-3.5" /> Needs diagram
            </Badge>
          )}
          <ConfidenceBadge value={q.confidence} />
          <Button variant="ghost" size="icon" onClick={() => onRemoveQuestion(qIndex)}>
            <Trash2 className="h-4 w-4" />
          </Button>
        </div>
      </CardHeader>
      <CardContent className="space-y-3">
        <RichTextField
          value={q.stem}
          onChange={(v) => onUpdateQuestion(qIndex, { stem: v })}
          rows={3}
          className="font-medium"
        />
        {needsDiagram && (
          <p className="rounded-lg border border-warning/50 bg-warning/10 px-3 py-2 text-xs text-warning-foreground">
            This question looks like it references a figure, graph, or table that wasn&apos;t captured as text.
            Attach the diagram image below, or dismiss this if it doesn&apos;t actually need one.
          </p>
        )}
        <ImageUploadField imageUrl={q.imageUrl} onChange={(url) => onUpdateQuestion(qIndex, { imageUrl: url })} />
        <div className="grid gap-2 sm:grid-cols-2">
          {q.choices.map((choice, cIndex) => (
            <label
              key={choice.label}
              className={cn(
                "flex items-start gap-2 rounded-lg border border-border p-2.5 text-sm",
                choice.isCorrect && "border-success bg-success/5"
              )}
            >
              <input
                type="radio"
                name={`correct-${qIndex}`}
                checked={choice.isCorrect}
                onChange={() => onSetCorrectChoice(qIndex, choice.label)}
                className="mt-1"
              />
              <span className="font-semibold">{choice.label}</span>
              <Input
                value={choice.content}
                onChange={(e) => onUpdateChoice(qIndex, cIndex, { content: e.target.value })}
                className="h-8 flex-1 border-none bg-transparent p-0 shadow-none focus-visible:ring-0"
              />
              {choice.isCorrect && <Check className="h-4 w-4 shrink-0 text-success" />}
              <button
                type="button"
                onClick={() => onRemoveChoice(qIndex, cIndex)}
                className="shrink-0 text-muted-foreground hover:text-destructive"
              >
                <Trash2 className="h-3.5 w-3.5" />
              </button>
            </label>
          ))}
        </div>
        {q.choices.length < 4 && (
          <Button variant="outline" size="sm" onClick={() => onAddChoice(qIndex)}>
            <Plus className="h-3.5 w-3.5" /> Add choice {"ABCD"[q.choices.length]}
            {q.choices.length === 0 ? " — extraction found no choices here, check the PDF text" : ""}
          </Button>
        )}
        {explanationOpen ? (
          <div className="space-y-1">
            <Label className="text-xs text-muted-foreground">Explanation (optional)</Label>
            <Textarea
              value={q.explanation ?? ""}
              onChange={(e) => onUpdateQuestion(qIndex, { explanation: e.target.value })}
              rows={2}
              placeholder="No explanation text was detected for this question."
            />
          </div>
        ) : (
          <button
            type="button"
            onClick={() => setExplanationOpen(true)}
            className="text-xs font-medium text-muted-foreground underline-offset-2 hover:text-foreground hover:underline"
          >
            + Add explanation (optional)
          </button>
        )}
        <div className="grid gap-2 sm:grid-cols-2">
          <div className="space-y-1">
            <Label className="text-xs text-muted-foreground">Domain</Label>
            <Select
              value={q.domainId ?? ""}
              onValueChange={(v) => {
                const d = subjectDomains.find((x) => x.id === v);
                onUpdateQuestion(qIndex, { domainId: v, skillId: d?.skills[0]?.id ?? "" });
              }}
            >
              <SelectTrigger className="h-8 text-xs">
                <SelectValue placeholder="Choose a domain" />
              </SelectTrigger>
              <SelectContent>
                {subjectDomains.map((d) => (
                  <SelectItem key={d.id} value={d.id}>
                    {d.name}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
          <div className="space-y-1">
            <Label className="text-xs text-muted-foreground">Skill / topic</Label>
            <Select value={q.skillId ?? ""} onValueChange={(v) => onUpdateQuestion(qIndex, { skillId: v })}>
              <SelectTrigger className="h-8 text-xs">
                <SelectValue placeholder="Choose a skill" />
              </SelectTrigger>
              <SelectContent>
                {(subjectDomains.find((d) => d.id === q.domainId)?.skills ?? []).map((s) => (
                  <SelectItem key={s.id} value={s.id}>
                    {s.name}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
          <div className="space-y-1">
            <Label className="text-xs text-muted-foreground">Difficulty</Label>
            <Select
              value={q.difficultyGuess}
              onValueChange={(v) => onUpdateQuestion(qIndex, { difficultyGuess: v as ExtractedQuestion["difficultyGuess"] })}
            >
              <SelectTrigger className="h-8 text-xs">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="EASY">Easy</SelectItem>
                <SelectItem value="MEDIUM">Medium</SelectItem>
                <SelectItem value="HARD">Hard</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </div>
        <div className="flex flex-wrap gap-3 text-xs text-muted-foreground">{q.hasTable && <span>Contains table</span>}</div>
      </CardContent>
    </Card>
  );
});

// ---------------------------------------------------------------------------
// Vocabulary review
// ---------------------------------------------------------------------------

function VocabReview({
  uploadId,
  jobId,
  confidence,
  initial,
  alreadyPublished,
}: {
  uploadId: string;
  jobId: string;
  confidence: number;
  initial: VocabExtractionResult;
  alreadyPublished: boolean;
}) {
  const router = useRouter();
  const [words, setWords] = useState<ExtractedVocabWord[]>(initial.words);
  const [isSaving, startSave] = useTransition();
  const [isPublishing, startPublish] = useTransition();

  function updateWord(index: number, patch: Partial<ExtractedVocabWord>) {
    setWords((prev) => prev.map((w, i) => (i === index ? { ...w, ...patch } : w)));
  }

  function removeWord(index: number) {
    setWords((prev) => prev.filter((_, i) => i !== index));
  }

  function addWord() {
    setWords((prev) => [
      ...prev,
      { term: "", definition: "", synonyms: [], antonyms: [], difficultyGuess: "MEDIUM", confidence: 1 },
    ]);
  }

  function saveDraft() {
    startSave(async () => {
      try {
        await updateExtractedData(jobId, { ...initial, words });
        toast.success("Draft saved.");
      } catch (error) {
        toast.error(error instanceof Error ? error.message : "Couldn't save the draft.");
      }
    });
  }

  function publish() {
    startPublish(async () => {
      try {
        await updateExtractedData(jobId, { ...initial, words });
        await publishVocabUpload(uploadId);
        toast.success("Vocabulary deck published.");
        router.refresh();
      } catch (error) {
        // publishVocabUpload redirects on success, which Next implements by
        // throwing — that must propagate, not be swallowed as a failure toast.
        if (isNextRedirectError(error)) throw error;
        toast.error(
          error instanceof Error
            ? error.message
            : "Couldn't publish this deck. Your edits above are still here — fix the issue and try again."
        );
      }
    });
  }

  return (
    <div className="space-y-6">
      <Card>
        <CardContent className="flex flex-wrap items-center justify-between gap-4 p-6">
          <div className="flex items-center gap-3">
            <ConfidenceBadge value={confidence} />
            <span className="text-sm text-muted-foreground">{words.length} words extracted</span>
          </div>
          {!alreadyPublished && (
            <div className="flex items-center gap-2">
              <Button variant="outline" size="sm" onClick={addWord}>
                <Plus className="h-4 w-4" /> Add word
              </Button>
              <Button variant="outline" onClick={saveDraft} disabled={isSaving}>
                {isSaving ? <Loader2 className="h-4 w-4 animate-spin" /> : <Save className="h-4 w-4" />}
                Save draft
              </Button>
              <Button onClick={publish} disabled={isPublishing || words.length === 0}>
                {isPublishing ? <Loader2 className="h-4 w-4 animate-spin" /> : <Upload className="h-4 w-4" />}
                Publish deck
              </Button>
            </div>
          )}
        </CardContent>
      </Card>

      <div className="grid gap-3 sm:grid-cols-2">
        {words.map((word, index) => (
          <Card key={index}>
            <CardContent className="space-y-2 p-4">
              <div className="flex items-center justify-between">
                <Input
                  value={word.term}
                  onChange={(e) => updateWord(index, { term: e.target.value })}
                  placeholder="Term"
                  className="h-8 flex-1 border-none bg-transparent p-0 text-base font-semibold shadow-none focus-visible:ring-0"
                />
                <Button variant="ghost" size="icon" onClick={() => removeWord(index)}>
                  <Trash2 className="h-4 w-4" />
                </Button>
              </div>
              <Textarea
                value={word.definition}
                onChange={(e) => updateWord(index, { definition: e.target.value })}
                placeholder="Definition"
                rows={2}
              />
              <div className="grid grid-cols-2 gap-2">
                <div className="space-y-1">
                  <Label className="text-xs text-muted-foreground">Synonyms</Label>
                  <Input
                    value={word.synonyms.join(", ")}
                    onChange={(e) =>
                      updateWord(index, { synonyms: e.target.value.split(",").map((s) => s.trim()).filter(Boolean) })
                    }
                  />
                </div>
                <div className="space-y-1">
                  <Label className="text-xs text-muted-foreground">Antonyms</Label>
                  <Input
                    value={word.antonyms.join(", ")}
                    onChange={(e) =>
                      updateWord(index, { antonyms: e.target.value.split(",").map((s) => s.trim()).filter(Boolean) })
                    }
                  />
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
