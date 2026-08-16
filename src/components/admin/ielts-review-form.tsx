"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { cn } from "@/lib/utils";
import { BAND_STEPS, formatBand, toHalfBand } from "@/lib/ielts/bands";
import { SPEAKING_CRITERIA, WRITING_CRITERIA } from "@/lib/ielts/constants";
import {
  submitSpeakingReview, submitWritingReview,
} from "@/server/actions/admin/ielts-review";

/** Bands below 3 never appear in practice; offering 0-9 in full is noise. */
const CHOOSABLE = BAND_STEPS.filter((b) => b >= 3);

function BandPicker({
  label, value, onChange,
}: {
  label: string;
  value: number | null;
  onChange: (v: number) => void;
}) {
  return (
    <div className="space-y-1.5">
      <Label className="text-sm font-medium">{label}</Label>
      <div className="flex flex-wrap gap-1">
        {CHOOSABLE.map((b) => (
          <button
            key={b}
            type="button"
            onClick={() => onChange(b)}
            aria-pressed={value === b}
            className={cn(
              "h-8 w-11 rounded-md border text-sm font-semibold tabular-nums transition-colors",
              "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
              value === b
                ? "border-navy-900 bg-navy-900 text-white"
                : "border-border bg-card text-muted-foreground hover:bg-secondary"
            )}
          >
            {formatBand(b)}
          </button>
        ))}
      </div>
    </div>
  );
}

function Field({
  label, value, onChange, rows = 3, placeholder,
}: {
  label: string; value: string; onChange: (v: string) => void;
  rows?: number; placeholder?: string;
}) {
  return (
    <div className="space-y-1.5">
      <Label className="text-sm font-medium">{label}</Label>
      <Textarea
        value={value}
        rows={rows}
        placeholder={placeholder}
        onChange={(e) => onChange(e.target.value)}
      />
    </div>
  );
}

type Bands = Record<string, number | null>;

/**
 * The reviewer's scoring form.
 *
 * One component for both skills because the shape is identical — four criteria,
 * a live average, then written feedback — while the criteria themselves are
 * not. Writing is marked on Task Achievement/Response and Coherence; Speaking
 * on Fluency and Pronunciation. Passing the criteria in rather than branching
 * inside keeps the two from drifting into each other.
 */
export function IeltsReviewForm({
  kind,
  submissionId,
  initial,
}: {
  kind: "WRITING" | "SPEAKING";
  submissionId: string;
  initial?: { bands?: Bands; notes?: Record<string, string> };
}) {
  const router = useRouter();
  const criteria = kind === "WRITING" ? WRITING_CRITERIA : SPEAKING_CRITERIA;
  const [bands, setBands] = useState<Bands>(
    initial?.bands ?? Object.fromEntries(criteria.map((c) => [c.key, null])));
  const [notes, setNotes] = useState<Record<string, string>>(initial?.notes ?? {});
  const [pending, start] = useTransition();

  const values = criteria.map((c) => bands[c.key]);
  const complete = values.every((v) => v !== null);
  // Shown live so the reviewer sees the band they are producing as they score,
  // rather than discovering it after submitting.
  const overall = complete
    ? toHalfBand((values as number[]).reduce((a, b) => a + b, 0) / 4)
    : null;

  const note = (k: string) => notes[k] ?? "";
  const setNote = (k: string) => (v: string) => setNotes((n) => ({ ...n, [k]: v }));

  function onSubmit() {
    if (!complete) {
      toast.error("Give a band for all four criteria.");
      return;
    }
    start(async () => {
      const res =
        kind === "WRITING"
          ? await submitWritingReview({
              submissionId,
              taskBand: bands.task as number,
              coherenceBand: bands.coherence as number,
              lexicalBand: bands.lexical as number,
              grammarBand: bands.grammar as number,
              overallFeedback: note("overall"),
              didWell: note("didWell"),
              toImprove: note("toImprove"),
              taskResponseNotes: note("taskNotes"),
              coherenceNotes: note("coherenceNotes"),
              vocabularyNotes: note("lexicalNotes"),
              grammarNotes: note("grammarNotes"),
              nextSteps: note("nextSteps"),
            })
          : await submitSpeakingReview({
              submissionId,
              fluencyBand: bands.fluency as number,
              lexicalBand: bands.lexical as number,
              grammarBand: bands.grammar as number,
              pronunciationBand: bands.pronunciation as number,
              overallFeedback: note("overall"),
              fluencyNotes: note("fluencyNotes"),
              vocabularyNotes: note("lexicalNotes"),
              grammarNotes: note("grammarNotes"),
              pronunciationNotes: note("pronunciationNotes"),
              strongPoints: note("didWell"),
              weaknesses: note("toImprove"),
              howToImprove: note("nextSteps"),
            });
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success("Review sent to the student.");
      router.push(`/admin/ielts/${kind.toLowerCase()}`);
      router.refresh();
    });
  }

  const perCriterionNoteKey: Record<string, string> = {
    task: "taskNotes", coherence: "coherenceNotes",
    lexical: "lexicalNotes", grammar: "grammarNotes",
    fluency: "fluencyNotes", pronunciation: "pronunciationNotes",
  };

  return (
    <div className="space-y-6">
      <div className="space-y-4 rounded-lg border border-border bg-card p-5">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <h2 className="font-display text-lg font-semibold">Assessment</h2>
          <div className="text-right">
            <p className="text-xs uppercase tracking-wide text-muted-foreground">
              Overall {kind === "WRITING" ? "Writing" : "Speaking"} band
            </p>
            <p className="font-display text-3xl font-semibold tabular-nums">
              {overall != null ? formatBand(overall) : "—"}
            </p>
          </div>
        </div>

        <div className="grid gap-5">
          {criteria.map((c) => (
            <div key={c.key} className="space-y-2 border-t border-border pt-4 first:border-0 first:pt-0">
              <BandPicker
                label={c.label}
                value={bands[c.key] ?? null}
                onChange={(v) => setBands((b) => ({ ...b, [c.key]: v }))}
              />
              <Field
                label="Notes on this criterion"
                rows={2}
                value={note(perCriterionNoteKey[c.key])}
                onChange={setNote(perCriterionNoteKey[c.key])}
                placeholder="What the student did, and what would move this band up."
              />
            </div>
          ))}
        </div>
      </div>

      <div className="space-y-4 rounded-lg border border-border bg-card p-5">
        <h2 className="font-display text-lg font-semibold">Feedback</h2>
        <Field label="Overall feedback" rows={4} value={note("overall")}
          onChange={setNote("overall")}
          placeholder="Address the student directly. Be specific about what you saw." />
        <Field label={kind === "WRITING" ? "What you did well" : "Strong points"}
          value={note("didWell")} onChange={setNote("didWell")} />
        <Field label={kind === "WRITING" ? "What to improve" : "Main weaknesses"}
          value={note("toImprove")} onChange={setNote("toImprove")} />
        <Field label="Recommended next steps" value={note("nextSteps")}
          onChange={setNote("nextSteps")}
          placeholder="One or two concrete things to practise before the next attempt." />
      </div>

      <div className="flex flex-wrap items-center gap-3">
        <Button onClick={onSubmit} disabled={pending || !complete}>
          {pending && <Loader2 className="mr-1 h-4 w-4 animate-spin" />}
          Send review to student
        </Button>
        {!complete && (
          <span className="text-sm text-muted-foreground">
            All four criteria need a band.
          </span>
        )}
      </div>
    </div>
  );
}
