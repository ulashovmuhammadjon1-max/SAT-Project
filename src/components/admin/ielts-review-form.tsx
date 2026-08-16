"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { cn } from "@/lib/utils";
import {
  BAND_STEPS, formatBand, toHalfBand, writingBandFromTasks,
} from "@/lib/ielts/bands";
import { SPEAKING_CRITERIA, WRITING_CRITERIA } from "@/lib/ielts/constants";
import {
  submitSpeakingReview, submitWritingReview,
} from "@/server/actions/admin/ielts-review";

/**
 * Criteria are marked in WHOLE bands.
 *
 * An examiner awards 6 or 7 on Lexical Resource, never 6.5 — the half bands
 * appear only in the average of the four. Offering halves here invited a
 * precision the descriptors do not support, and made the arithmetic below
 * produce quarter bands that had to be rounded away again.
 */
const CHOOSABLE = [3, 4, 5, 6, 7, 8, 9];

function BandPicker({
  label, value, onChange,
}: {
  label: string;
  value: number | null;
  onChange: (v: number) => void;
}) {
  return (
    // `data-criterion` marks this as one of the four descriptor scores rather
    // than a reportable overall band. The two look alike on screen and are
    // scored on different scales, so anything reading the form — a test, an
    // audit script — needs to be able to tell them apart.
    <div className="space-y-1.5" data-criterion={label}>
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

/**
 * A reportable band — half steps, unlike the criteria.
 *
 * `null` means "take the computed one", which is why the suggestion is a
 * button rather than a preselected value: a reviewer who never touches this
 * control gets the arithmetic, and one who does is making a deliberate choice
 * that survives a later recalculation of the four criteria.
 */
function OverallPicker({
  label, hint, suggestion, suggestionLabel, value, onChange,
}: {
  label: string;
  hint?: string;
  suggestion: number | null;
  suggestionLabel: string;
  value: number | null;
  onChange: (v: number | null) => void;
}) {
  return (
    <div className="space-y-2 rounded-lg border border-border bg-secondary/40 p-3">
      <div className="flex flex-wrap items-baseline justify-between gap-2">
        <Label className="text-sm font-medium">{label}</Label>
        <span className="font-display text-lg font-semibold tabular-nums">
          {formatBand(value ?? suggestion)}
        </span>
      </div>
      {hint && <p className="text-xs text-muted-foreground">{hint}</p>}
      <div className="flex flex-wrap gap-1">
        <button
          type="button"
          onClick={() => onChange(null)}
          aria-pressed={value === null}
          className={cn(
            "h-8 rounded-md border px-3 text-sm font-semibold transition-colors",
            value === null
              ? "border-navy-900 bg-navy-900 text-white"
              : "border-border bg-card text-muted-foreground hover:bg-secondary"
          )}
        >
          {suggestionLabel}
          {suggestion != null && ` (${formatBand(suggestion)})`}
        </button>
        {BAND_STEPS.filter((b) => b >= 3).map((b) => (
          <button
            key={b}
            type="button"
            onClick={() => onChange(b)}
            aria-pressed={value === b}
            className={cn(
              "h-8 w-11 rounded-md border text-sm font-semibold tabular-nums transition-colors",
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
  wholeMock,
}: {
  kind: "WRITING" | "SPEAKING";
  submissionId: string;
  initial?: {
    bands?: Bands;
    notes?: Record<string, string>;
    /** A band already saved for this task, if it was not the plain average. */
    overall?: number | null;
    /** The band already saved for the whole Writing paper. */
    attemptOverall?: number | null;
  };
  /**
   * Writing only. Set when the student sat both tasks as one mock, in which
   * case the reviewer also gives the paper a band — Task 2's double weight
   * produces a default, but the human who read both scripts has the last word.
   */
  wholeMock?: { taskNumber: number; otherTaskBand: number | null } | null;
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
  // rather than discovering it after submitting. Four whole bands average to a
  // whole or a half, which is exactly the reportable scale.
  const computed = complete
    ? toHalfBand((values as number[]).reduce((a, b) => a + b, 0) / 4)
    : null;
  // The reviewer may override it. The average is a guide, not a verdict: an
  // examiner who reads the whole response and judges it a 7 should be able to
  // say 7 without reverse-engineering four criteria to make the mean agree.
  //
  // Seeded only when the saved band DIFFERS from the average of the saved
  // criteria. Seeding it unconditionally would pin a reviewer's second visit
  // to the old number: they would raise a criterion and watch the band not
  // move, with nothing on screen explaining why.
  const [override, setOverride] = useState<number | null>(() => {
    const saved = initial?.overall;
    if (saved == null || !initial?.bands) return null;
    const v = criteria.map((c) => initial.bands?.[c.key]);
    if (v.some((x) => x == null)) return null;
    const avg = toHalfBand((v as number[]).reduce((a, b) => a + b, 0) / 4);
    return saved === avg ? null : saved;
  });
  const overall = override ?? computed;

  // The whole Writing paper, when both tasks were sat together. Task 2 counts
  // twice, which is the one rule most easily lost by averaging.
  const [paperOverride, setPaperOverride] = useState<number | null>(() => {
    // Same reasoning as `override`: only a band that the weighting could not
    // have produced is a real human decision worth restoring.
    const saved = initial?.attemptOverall;
    if (saved == null || !wholeMock || initial?.overall == null) return null;
    const weighted =
      wholeMock.taskNumber === 2
        ? writingBandFromTasks(wholeMock.otherTaskBand, initial.overall)
        : writingBandFromTasks(initial.overall, wholeMock.otherTaskBand);
    return saved === (weighted ?? initial.overall) ? null : saved;
  });
  // With the sibling task unreviewed there is nothing to weight, so this
  // task's band stands — the same fallback `rollUpWriting` uses on the server.
  const paperComputed =
    wholeMock && overall != null
      ? (wholeMock.taskNumber === 2
          ? writingBandFromTasks(wholeMock.otherTaskBand, overall)
          : writingBandFromTasks(overall, wholeMock.otherTaskBand)) ?? overall
      : null;
  const paperBand = paperOverride ?? paperComputed;

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
              overallOverride: override ?? undefined,
              attemptOverride: paperOverride ?? undefined,
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
              overallOverride: override ?? undefined,
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

        {complete && (
          <OverallPicker
            label={`Band for this ${kind === "WRITING" ? "task" : "interview"}`}
            suggestion={computed}
            suggestionLabel="Use the average"
            value={override}
            onChange={setOverride}
          />
        )}

        {complete && wholeMock && (
          <OverallPicker
            label="Band for the whole Writing paper"
            hint={
              wholeMock.otherTaskBand == null
                ? "The other task has not been reviewed yet, so this is the only script marked so far."
                : `Task 1 ${formatBand(
                    wholeMock.taskNumber === 1 ? overall : wholeMock.otherTaskBand
                  )}, Task 2 ${formatBand(
                    wholeMock.taskNumber === 2 ? overall : wholeMock.otherTaskBand
                  )} — Task 2 counts twice.`
            }
            suggestion={paperBand}
            suggestionLabel="Use the weighted band"
            value={paperOverride}
            onChange={setPaperOverride}
          />
        )}

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
