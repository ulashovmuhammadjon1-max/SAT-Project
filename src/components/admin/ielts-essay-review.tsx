"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import {
  AlertTriangle, Check, Copy, Eye, EyeOff, Loader2, Sparkles, Trash2, X,
} from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { EssayReader } from "@/components/ielts/essay-reader";
import { CATEGORY_STYLES, type Category, type SegmentAnnotation } from "@/lib/ielts/essay-segments";
import { CATEGORY_LABELS, STATUS_LABELS } from "@/lib/validations/ielts-essay";
import {
  analyzeEssayAction, approveAllAnnotations, deleteAnnotation, deleteEssay,
  deleteIdea, duplicateEssay, publishEssay, setAnnotationReviewed, unpublishEssay,
} from "@/server/actions/admin/ielts-essays";
import { cn } from "@/lib/utils";

const ORDER: Category[] = ["GRAMMAR", "VOCABULARY", "COHESION", "COLLOCATION"];

/**
 * Stages shown while the analysis runs.
 *
 * These are a progress *narrative*, not separate backend calls — the brief asks
 * for a polished waiting state and also asks not to pretend these are discrete
 * operations, so they advance on a timer and the copy never claims a step has
 * finished.
 */
const STAGES = [
  "Reading the essay",
  "Identifying advanced grammar",
  "Finding topic vocabulary",
  "Analysing cohesion",
  "Finding useful collocations",
  "Extracting key ideas",
];

export interface ReviewAnnotation extends SegmentAnnotation {
  confidence: number | null;
  source: "AI" | "ADMIN";
  reviewed: boolean;
}

export interface ReviewIdea {
  id: string;
  claim: string;
  explanation: string;
  consequence: string | null;
  example: string | null;
  reviewed: boolean;
}

export function IeltsEssayReview({
  essayId,
  essayText,
  status,
  annotations,
  ideas,
  analysisError,
  offsetsStale,
}: {
  essayId: string;
  essayText: string;
  status: string;
  annotations: ReviewAnnotation[];
  ideas: ReviewIdea[];
  analysisError: string | null;
  /** The essay text has moved since the analysis — highlights cannot be trusted. */
  offsetsStale: boolean;
}) {
  const router = useRouter();
  const [pending, start] = useTransition();
  const [analyzing, setAnalyzing] = useState(false);
  const [stage, setStage] = useState(0);
  const [preview, setPreview] = useState(false);

  const unreviewed = annotations.filter((a) => !a.reviewed).length;
  const intact = annotations.filter((a) => essayText.slice(a.startOffset, a.endOffset) === a.quote);
  const drifted = annotations.length - intact.length;

  function run(fn: () => Promise<{ ok?: boolean; error?: string; warnings?: string[] }>, success: string) {
    start(async () => {
      const res = await fn();
      if (res.error) {
        toast.error(res.error);
        return;
      }
      for (const w of res.warnings ?? []) toast.warning(w);
      toast.success(success);
      router.refresh();
    });
  }

  function analyze() {
    setAnalyzing(true);
    setStage(0);
    const timer = setInterval(() => setStage((s) => Math.min(s + 1, STAGES.length - 1)), 4000);
    start(async () => {
      const res = await analyzeEssayAction(essayId);
      clearInterval(timer);
      setAnalyzing(false);
      if (res.error) {
        toast.error(res.error);
        router.refresh();
        return;
      }
      for (const w of res.warnings ?? []) toast.warning(w);
      toast.success("Analysis ready for review.");
      router.refresh();
    });
  }

  return (
    <div className="space-y-5">
      <div className="flex flex-wrap items-center gap-2">
        <Badge variant={status === "PUBLISHED" ? "success" : "outline"}>
          {STATUS_LABELS[status] ?? status}
        </Badge>
        {unreviewed > 0 && (
          <Badge variant="warning">{unreviewed} to review</Badge>
        )}
        {drifted > 0 && <Badge variant="destructive">{drifted} drifted</Badge>}

        <div className="ml-auto flex flex-wrap gap-2">
          <Button size="sm" variant="outline" onClick={() => setPreview((p) => !p)}>
            {preview ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
            {preview ? "Hide student view" : "Student view"}
          </Button>
          <Button size="sm" variant="outline" disabled={pending || analyzing} onClick={analyze}>
            <Sparkles className="h-4 w-4" />
            {annotations.length ? "Re-analyse" : "Analyse essay"}
          </Button>
          <Button
            size="sm"
            variant="outline"
            disabled={pending}
            onClick={() => run(() => duplicateEssay(essayId), "Duplicated.")}
          >
            <Copy className="h-4 w-4" /> Duplicate
          </Button>
          {status === "PUBLISHED" ? (
            <Button size="sm" variant="outline" disabled={pending}
              onClick={() => run(() => unpublishEssay(essayId), "Unpublished.")}>
              Unpublish
            </Button>
          ) : (
            <Button size="sm" disabled={pending}
              onClick={() => run(() => publishEssay(essayId), "Published to students.")}>
              Publish
            </Button>
          )}
          <Button
            size="sm"
            variant="ghost"
            className="text-destructive hover:text-destructive"
            disabled={pending}
            onClick={() => {
              if (!confirm("Delete this essay and all its annotations? This cannot be undone.")) return;
              start(async () => {
                const res = await deleteEssay(essayId);
                if (res.error) {
                  toast.error(res.error);
                  return;
                }
                toast.success("Deleted.");
                router.push("/admin/ielts/essays");
              });
            }}
          >
            <Trash2 className="h-4 w-4" />
          </Button>
        </div>
      </div>

      {analysisError && !analyzing && (
        <p className="flex items-start gap-2 rounded-lg bg-destructive/10 p-3 text-sm text-destructive">
          <AlertTriangle className="mt-0.5 h-4 w-4 shrink-0" />
          {analysisError}
        </p>
      )}

      {(offsetsStale || drifted > 0) && (
        <p className="flex items-start gap-2 rounded-lg bg-amber-500/10 p-3 text-sm text-amber-700 dark:text-amber-400">
          <AlertTriangle className="mt-0.5 h-4 w-4 shrink-0" />
          The essay text has changed since it was analysed, so some highlights no longer line up
          with the words they describe. Re-analyse before publishing — publishing is blocked until
          you do.
        </p>
      )}

      {analyzing && (
        <Card>
          <CardContent className="space-y-3 py-6">
            <p className="flex items-center gap-2 text-sm font-medium">
              <Loader2 className="h-4 w-4 animate-spin" />
              Analysing this Task 2 essay
            </p>
            <ul className="space-y-1.5">
              {STAGES.map((s, i) => (
                <li
                  key={s}
                  className={cn(
                    "flex items-center gap-2 text-sm transition-colors",
                    i < stage ? "text-muted-foreground" : i === stage ? "text-foreground" : "text-muted-foreground/50"
                  )}
                >
                  {i < stage ? (
                    <Check className="h-3.5 w-3.5 text-emerald-500" />
                  ) : i === stage ? (
                    <Loader2 className="h-3.5 w-3.5 animate-spin" />
                  ) : (
                    <span className="h-3.5 w-3.5" />
                  )}
                  {s}
                </li>
              ))}
            </ul>
            <p className="text-xs text-muted-foreground">
              Nothing reaches students until you have reviewed the result.
            </p>
          </CardContent>
        </Card>
      )}

      {preview && (
        <Card className="border-primary/40">
          <CardContent className="space-y-2 py-5">
            <p className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
              Exactly what a student will see
            </p>
            <EssayReader essayText={essayText} annotations={intact} />
          </CardContent>
        </Card>
      )}

      {annotations.length > 0 && (
        <div className="flex items-center gap-2">
          <h2 className="text-sm font-semibold">Annotations</h2>
          <span className="text-xs tabular-nums text-muted-foreground">{annotations.length}</span>
          {unreviewed > 0 && (
            <Button
              size="sm"
              variant="outline"
              className="ml-auto"
              disabled={pending}
              onClick={() => run(() => approveAllAnnotations(essayId), "All annotations approved.")}
            >
              <Check className="h-4 w-4" /> Approve all
            </Button>
          )}
        </div>
      )}

      <div className="space-y-3">
        {ORDER.map((c) => {
          const items = annotations.filter((a) => a.category === c);
          if (!items.length) return null;
          const style = CATEGORY_STYLES[c];
          return (
            <Card key={c}>
              <CardContent className="space-y-3 py-4">
                <div className="flex items-center gap-2">
                  <span className={cn("h-2 w-2 rounded-full", style.dot)} />
                  <h3 className="text-sm font-semibold">{CATEGORY_LABELS[c]}</h3>
                  <span className="text-xs tabular-nums text-muted-foreground">{items.length}</span>
                </div>
                <ul className="divide-y divide-border">
                  {items.map((a) => {
                    const ok = essayText.slice(a.startOffset, a.endOffset) === a.quote;
                    return (
                      <li key={a.id} className="flex flex-wrap items-start gap-3 py-3">
                        <div className="min-w-[200px] flex-1 space-y-1">
                          <div className="flex flex-wrap items-center gap-2">
                            <p className="text-sm font-medium">{a.quote}</p>
                            <Badge variant="outline" className="text-[10px]">
                              {a.subtype.replace(/_/g, " ")}
                            </Badge>
                            {a.source === "ADMIN" && <Badge variant="navy" className="text-[10px]">yours</Badge>}
                            {a.confidence != null && (
                              <span className="text-[10px] tabular-nums text-muted-foreground">
                                {Math.round(a.confidence * 100)}%
                              </span>
                            )}
                            {!ok && <Badge variant="destructive" className="text-[10px]">drifted</Badge>}
                          </div>
                          <p className="text-xs leading-relaxed text-muted-foreground">{a.explanation}</p>
                          {a.pattern && (
                            <p className="font-mono text-[11px] text-muted-foreground">{a.pattern}</p>
                          )}
                        </div>
                        <div className="flex items-center gap-1">
                          <Button
                            size="sm"
                            variant={a.reviewed ? "outline" : "default"}
                            disabled={pending}
                            onClick={() =>
                              run(() => setAnnotationReviewed(a.id, !a.reviewed),
                                a.reviewed ? "Marked unreviewed." : "Kept.")
                            }
                          >
                            {a.reviewed ? <Check className="h-4 w-4" /> : "Keep"}
                          </Button>
                          <Button
                            size="sm"
                            variant="ghost"
                            className="text-destructive hover:text-destructive"
                            disabled={pending}
                            onClick={() => run(() => deleteAnnotation(a.id), "Removed.")}
                          >
                            <X className="h-4 w-4" />
                          </Button>
                        </div>
                      </li>
                    );
                  })}
                </ul>
              </CardContent>
            </Card>
          );
        })}
      </div>

      {ideas.length > 0 && (
        <Card>
          <CardContent className="space-y-3 py-4">
            <h3 className="text-sm font-semibold">Ideas</h3>
            <ul className="divide-y divide-border">
              {ideas.map((i) => (
                <li key={i.id} className="flex flex-wrap items-start gap-3 py-3">
                  <div className="min-w-[200px] flex-1 space-y-1">
                    <p className="text-sm font-medium">{i.claim}</p>
                    <p className="text-xs leading-relaxed text-muted-foreground">{i.explanation}</p>
                    {i.consequence && (
                      <p className="text-xs text-muted-foreground">
                        <span className="font-medium text-foreground">Result: </span>{i.consequence}
                      </p>
                    )}
                    {i.example && (
                      <p className="text-xs text-muted-foreground">
                        <span className="font-medium text-foreground">Example: </span>{i.example}
                      </p>
                    )}
                  </div>
                  <Button
                    size="sm"
                    variant="ghost"
                    className="text-destructive hover:text-destructive"
                    disabled={pending}
                    onClick={() => run(() => deleteIdea(i.id), "Removed.")}
                  >
                    <X className="h-4 w-4" />
                  </Button>
                </li>
              ))}
            </ul>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
