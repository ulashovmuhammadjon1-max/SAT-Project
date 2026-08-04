"use client";

import { useMemo, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { AlertTriangle, Check, Loader2, Plus, Save, Trash2, Upload } from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { cn } from "@/lib/utils";
import { publishTestUpload, publishVocabUpload, updateExtractedData } from "@/server/actions/admin/uploads";
import type {
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
function withTaxonomyDefaults(
  questions: ExtractedQuestion[],
  domains: DomainOption[],
  subject: Subject
): ExtractedQuestion[] {
  const subjectDomainIds = new Set(domains.filter((d) => d.subject === subject).map((d) => d.id));
  return questions.map((q) => {
    if (q.domainId && subjectDomainIds.has(q.domainId) && q.skillId) return q;
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
  const [subject, setSubject] = useState<Subject>(initialSubject ?? "READING_WRITING");
  const [questions, setQuestions] = useState<ExtractedQuestion[]>(() =>
    withTaxonomyDefaults(initial.questions, domains, initialSubject ?? "READING_WRITING")
  );
  const [moduleSlot, setModuleSlot] = useState(initialModuleSlot ?? "1");
  const [thresholdPct, setThresholdPct] = useState("");
  const [targetTestId, setTargetTestId] = useState(initialTargetTestId ?? "new");
  const [isSaving, startSave] = useTransition();
  const [isPublishing, startPublish] = useTransition();

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

  function changeSubject(next: Subject) {
    setSubject(next);
    setQuestions((prev) => withTaxonomyDefaults(prev, domains, next));
    setTargetTestId("new");
  }

  function updateQuestion(index: number, patch: Partial<ExtractedQuestion>) {
    setQuestions((prev) => prev.map((q, i) => (i === index ? { ...q, ...patch } : q)));
  }

  function updateChoice(qIndex: number, cIndex: number, patch: Partial<ExtractedQuestion["choices"][number]>) {
    setQuestions((prev) =>
      prev.map((q, i) =>
        i === qIndex
          ? { ...q, choices: q.choices.map((c, j) => (j === cIndex ? { ...c, ...patch } : c)) }
          : q
      )
    );
  }

  function setCorrectChoice(qIndex: number, label: string) {
    setQuestions((prev) =>
      prev.map((q, i) =>
        i === qIndex ? { ...q, choices: q.choices.map((c) => ({ ...c, isCorrect: c.label === label })) } : q
      )
    );
  }

  function removeQuestion(index: number) {
    setQuestions((prev) => prev.filter((_, i) => i !== index));
  }

  function addChoice(qIndex: number) {
    setQuestions((prev) =>
      prev.map((q, i) =>
        i === qIndex
          ? { ...q, choices: [...q.choices, { label: "ABCD"[q.choices.length], content: "", isCorrect: false }] }
          : q
      )
    );
  }

  function removeChoice(qIndex: number, cIndex: number) {
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
  }

  function saveDraft() {
    startSave(async () => {
      await updateExtractedData(jobId, { ...initial, questions });
      toast.success("Draft saved.");
    });
  }

  function publish() {
    startPublish(async () => {
      await updateExtractedData(jobId, { ...initial, questions });
      await publishTestUpload(uploadId, {
        subject,
        order: slot.order,
        difficulty: slot.difficulty,
        thresholdPct: thresholdPct.trim() ? Number(thresholdPct) : null,
        targetTestId: targetTestId === "new" ? null : targetTestId,
      });
      toast.success(targetTestId === "new" ? "Published as a new test." : "Module added to the test.");
      router.refresh();
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
              <Button onClick={publish} disabled={isPublishing || questions.length === 0}>
                {isPublishing ? <Loader2 className="h-4 w-4 animate-spin" /> : <Upload className="h-4 w-4" />}
                {targetTestId === "new" ? "Publish as new test" : "Add to test"}
              </Button>
            </div>
          )}
        </CardContent>
      </Card>

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
        {questions.map((q, qIndex) => (
          <Card key={qIndex} className={cn(q.confidence < CONFIDENCE_PUBLISH_THRESHOLD && "border-warning/50")}>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-3">
              <CardTitle className="text-sm font-semibold text-muted-foreground">Question {q.number}</CardTitle>
              <div className="flex items-center gap-2">
                <ConfidenceBadge value={q.confidence} />
                <Button variant="ghost" size="icon" onClick={() => removeQuestion(qIndex)}>
                  <Trash2 className="h-4 w-4" />
                </Button>
              </div>
            </CardHeader>
            <CardContent className="space-y-3">
              <Textarea
                value={q.stem}
                onChange={(e) => updateQuestion(qIndex, { stem: e.target.value })}
                rows={3}
                className="font-medium"
              />
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
                      onChange={() => setCorrectChoice(qIndex, choice.label)}
                      className="mt-1"
                    />
                    <span className="font-semibold">{choice.label}</span>
                    <Input
                      value={choice.content}
                      onChange={(e) => updateChoice(qIndex, cIndex, { content: e.target.value })}
                      className="h-8 flex-1 border-none bg-transparent p-0 shadow-none focus-visible:ring-0"
                    />
                    {choice.isCorrect && <Check className="h-4 w-4 shrink-0 text-success" />}
                    <button
                      type="button"
                      onClick={() => removeChoice(qIndex, cIndex)}
                      className="shrink-0 text-muted-foreground hover:text-destructive"
                    >
                      <Trash2 className="h-3.5 w-3.5" />
                    </button>
                  </label>
                ))}
              </div>
              {q.choices.length < 4 && (
                <Button variant="outline" size="sm" onClick={() => addChoice(qIndex)}>
                  <Plus className="h-3.5 w-3.5" /> Add choice {"ABCD"[q.choices.length]}
                  {q.choices.length === 0 ? " — extraction found no choices here, check the PDF text" : ""}
                </Button>
              )}
              <div className="space-y-1">
                <Label className="text-xs text-muted-foreground">Explanation (from the PDF, if present)</Label>
                <Textarea
                  value={q.explanation ?? ""}
                  onChange={(e) => updateQuestion(qIndex, { explanation: e.target.value })}
                  rows={2}
                  placeholder="No explanation text was detected for this question."
                />
              </div>
              <div className="grid gap-2 sm:grid-cols-2">
                <div className="space-y-1">
                  <Label className="text-xs text-muted-foreground">Domain</Label>
                  <Select
                    value={q.domainId ?? ""}
                    onValueChange={(v) => {
                      const d = subjectDomains.find((x) => x.id === v);
                      updateQuestion(qIndex, { domainId: v, skillId: d?.skills[0]?.id ?? "" });
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
                  <Select
                    value={q.skillId ?? ""}
                    onValueChange={(v) => updateQuestion(qIndex, { skillId: v })}
                  >
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
              </div>
              <div className="flex flex-wrap gap-3 text-xs text-muted-foreground">
                <span>Difficulty: {q.difficultyGuess}</span>
                {q.hasImage && <span>Contains image</span>}
                {q.hasTable && <span>Contains table</span>}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}

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
      await updateExtractedData(jobId, { ...initial, words });
      toast.success("Draft saved.");
    });
  }

  function publish() {
    startPublish(async () => {
      await updateExtractedData(jobId, { ...initial, words });
      await publishVocabUpload(uploadId);
      toast.success("Vocabulary deck published.");
      router.refresh();
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
