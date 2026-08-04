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

export function ExtractionReview({
  uploadId,
  jobId,
  category,
  confidence,
  data,
  alreadyPublished,
}: {
  uploadId: string;
  jobId: string;
  category: "FULL_TEST" | "QUESTION_BANK" | "VOCABULARY";
  confidence: number;
  data: TestExtractionResult | VocabExtractionResult;
  alreadyPublished: boolean;
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
      confidence={confidence}
      initial={data as TestExtractionResult}
      alreadyPublished={alreadyPublished}
    />
  );
}

// ---------------------------------------------------------------------------
// Test / question bank review
// ---------------------------------------------------------------------------

function TestReview({
  uploadId,
  jobId,
  confidence,
  initial,
  alreadyPublished,
}: {
  uploadId: string;
  jobId: string;
  confidence: number;
  initial: TestExtractionResult;
  alreadyPublished: boolean;
}) {
  const router = useRouter();
  const [questions, setQuestions] = useState<ExtractedQuestion[]>(initial.questions);
  const [subject, setSubject] = useState<"READING_WRITING" | "MATH">("READING_WRITING");
  const [isSaving, startSave] = useTransition();
  const [isPublishing, startPublish] = useTransition();

  const lowConfidenceCount = useMemo(
    () => questions.filter((q) => q.confidence < CONFIDENCE_PUBLISH_THRESHOLD).length,
    [questions]
  );

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

  function saveDraft() {
    startSave(async () => {
      await updateExtractedData(jobId, { ...initial, questions });
      toast.success("Draft saved.");
    });
  }

  function publish() {
    startPublish(async () => {
      await updateExtractedData(jobId, { ...initial, questions });
      await publishTestUpload(uploadId, subject);
      toast.success("Published to the question bank.");
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
            <div className="flex items-center gap-2">
              <Select value={subject} onValueChange={(v) => setSubject(v as typeof subject)}>
                <SelectTrigger className="w-48">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="READING_WRITING">Reading & Writing</SelectItem>
                  <SelectItem value="MATH">Math</SelectItem>
                </SelectContent>
              </Select>
              <Button variant="outline" onClick={saveDraft} disabled={isSaving}>
                {isSaving ? <Loader2 className="h-4 w-4 animate-spin" /> : <Save className="h-4 w-4" />}
                Save draft
              </Button>
              <Button onClick={publish} disabled={isPublishing || questions.length === 0}>
                {isPublishing ? <Loader2 className="h-4 w-4 animate-spin" /> : <Upload className="h-4 w-4" />}
                Publish as new test
              </Button>
            </div>
          )}
        </CardContent>
      </Card>

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
                  </label>
                ))}
              </div>
              <div className="flex flex-wrap gap-3 text-xs text-muted-foreground">
                <span>Domain: {q.domainGuess || "—"}</span>
                <span>Skill: {q.skillGuess || "—"}</span>
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
