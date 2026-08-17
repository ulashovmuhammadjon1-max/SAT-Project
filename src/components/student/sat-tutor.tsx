"use client";

import { useEffect, useState, useTransition } from "react";
import { AlertCircle, Loader2, Send, Sparkles, X } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { askSATTutor, getTutorBudget } from "@/server/actions/student/sat-tutor";

/**
 * The SAT tutor panel.
 *
 * Deliberately a hint box and not a chat: a conversation invites a student to
 * keep asking until the model concedes the answer, which is the one thing this
 * must not do. One question in, one hint out, and the budget on screen the
 * whole time so the cost of asking is never a surprise.
 */
export function SATTutor({ questionId }: { questionId: string }) {
  const [open, setOpen] = useState(false);
  const [note, setNote] = useState("");
  const [hint, setHint] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [remaining, setRemaining] = useState<number | null>(null);
  const [pending, startTransition] = useTransition();

  // Fetched on open rather than on mount: a student who never asks for a hint
  // should not cost a query on every practice question they load.
  useEffect(() => {
    if (!open || remaining !== null) return;
    let cancelled = false;
    getTutorBudget()
      .then((b) => !cancelled && setRemaining(b.remaining))
      .catch(() => undefined);
    return () => {
      cancelled = true;
    };
  }, [open, remaining]);

  function ask() {
    setError(null);
    startTransition(async () => {
      const res = await askSATTutor(questionId, note);
      if (res.remaining !== undefined) setRemaining(res.remaining);
      if (res.ok && res.message) {
        setHint(res.message);
        setNote("");
      } else {
        setError(res.error ?? "The tutor is unavailable right now.");
      }
    });
  }

  if (!open) {
    return (
      <Button variant="outline" size="sm" className="gap-2" onClick={() => setOpen(true)}>
        <Sparkles className="h-4 w-4" />
        Stuck? Get a hint
      </Button>
    );
  }

  const exhausted = remaining === 0;

  return (
    <div className="space-y-3 rounded-xl border border-border bg-secondary/40 p-4">
      <div className="flex items-center justify-between gap-2">
        <p className="flex items-center gap-2 text-sm font-semibold">
          <Sparkles className="h-4 w-4" />
          SAT tutor
        </p>
        <div className="flex items-center gap-2">
          {remaining !== null && (
            <span className="text-xs tabular-nums text-muted-foreground">
              {remaining} left today
            </span>
          )}
          <Button
            variant="ghost"
            size="sm"
            aria-label="Close the tutor"
            onClick={() => {
              setOpen(false);
              setHint(null);
              setError(null);
            }}
          >
            <X className="h-4 w-4" />
          </Button>
        </div>
      </div>

      {error && (
        <p className="flex items-start gap-2 rounded-lg bg-destructive/10 p-3 text-xs text-destructive">
          <AlertCircle className="mt-0.5 h-4 w-4 shrink-0" />
          {error}
        </p>
      )}

      {hint ? (
        <div className="space-y-3">
          {/* Plain text, not MathContent: the prompt forbids LaTeX, and running
              model output through a renderer would execute markup the model
              chose rather than markup we wrote. */}
          <p className="whitespace-pre-wrap rounded-lg border border-border bg-card p-3 text-sm leading-relaxed">
            {hint}
          </p>
          {!exhausted && (
            <Button variant="outline" size="sm" onClick={() => setHint(null)}>
              Ask something else
            </Button>
          )}
        </div>
      ) : (
        <>
          <Textarea
            value={note}
            onChange={(e) => setNote(e.target.value)}
            disabled={pending || exhausted}
            maxLength={500}
            rows={3}
            placeholder="What is confusing you? (optional — you can just ask for a nudge)"
            className="text-sm"
          />
          <Button size="sm" className="gap-2" disabled={pending || exhausted} onClick={ask}>
            {pending ? (
              <>
                <Loader2 className="h-4 w-4 animate-spin" />
                Thinking…
              </>
            ) : (
              <>
                <Send className="h-4 w-4" />
                Get a hint
              </>
            )}
          </Button>
        </>
      )}

      <p className="border-t border-border pt-2 text-xs text-muted-foreground">
        Hints only — the tutor will not tell you the answer, so you still get the practice.
      </p>
    </div>
  );
}
