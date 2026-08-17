"use client";

import { useEffect, useState, useTransition } from "react";
import { AlertCircle, Loader2, Send, Sparkles, X } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { cn } from "@/lib/utils";
import { askSATTutor, getTutorBudget, type TutorMode } from "@/server/actions/student/sat-tutor";

const COPY: Record<TutorMode, { trigger: string; submit: string; placeholder: string; foot: string }> = {
  hint: {
    trigger: "Stuck? Get a hint",
    submit: "Get a hint",
    placeholder: "What is confusing you? (optional — you can just ask for a nudge)",
    foot: "Hints only — the tutor will not tell you the answer, so you still get the practice.",
  },
  explain: {
    trigger: "Explain this question",
    submit: "Explain it",
    placeholder: "Anything specific you want explained? (optional)",
    foot: "Written by AI from the marked answer. If it contradicts the answer above, trust the answer.",
  },
};

/**
 * Which design system the panel is sitting inside.
 *
 * Not cosmetic. The testing screens are a Bluebook clone that is **always
 * light**, on its own `exam-*` tokens, while the rest of the app follows the
 * student's theme. Rendered with the app's tokens inside the exam chrome, a
 * dark-theme student got dark text on a dark card inside a white panel — the
 * hint was there and unreadable. So every theme-dependent surface below has to
 * switch, not just the outer container.
 */
type Surface = "app" | "testing";

const SKIN: Record<
  Surface,
  { shell: string; body: string; note: string; foot: string; label: string; ghost: string }
> = {
  app: {
    shell: "border-border bg-secondary/40",
    body: "border-border bg-card",
    note: "text-muted-foreground",
    foot: "border-border text-muted-foreground",
    label: "",
    ghost: "",
  },
  testing: {
    shell: "border-exam-divider bg-white",
    body: "border-exam-divider bg-exam-bg text-exam-text",
    note: "text-exam-muted",
    foot: "border-exam-divider text-exam-muted",
    label: "text-exam-text",
    ghost: "text-exam-text hover:bg-exam-hover",
  },
};

/**
 * The SAT tutor panel.
 *
 * Deliberately a one-shot box and not a chat: a conversation invites a student
 * to keep asking until the model concedes the answer, which is the one thing
 * hint mode must not do. One question in, one answer out, and the budget on
 * screen the whole time so the cost of asking is never a surprise.
 */
export function SATTutor({
  questionId,
  mode = "hint",
  surface = "app",
}: {
  questionId: string;
  mode?: TutorMode;
  surface?: Surface;
}) {
  const copy = COPY[mode];
  const skin = SKIN[surface];
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
      const res = await askSATTutor(questionId, note, mode);
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
      <Button
        variant="outline"
        size="sm"
        className={cn("gap-2", surface === "testing" && "border-exam-border bg-white text-exam-text hover:bg-exam-hover")}
        onClick={() => setOpen(true)}
      >
        <Sparkles className="h-4 w-4" />
        {copy.trigger}
      </Button>
    );
  }

  const exhausted = remaining === 0;

  return (
    <div className={cn("space-y-3 rounded-xl border p-4", skin.shell)}>
      <div className="flex items-center justify-between gap-2">
        <p className={cn("flex items-center gap-2 text-sm font-semibold", skin.label)}>
          <Sparkles className="h-4 w-4" />
          SAT tutor
        </p>
        <div className="flex items-center gap-2">
          {remaining !== null && (
            <span className={cn("text-xs tabular-nums", skin.note)}>{remaining} left today</span>
          )}
          <Button
            variant="ghost"
            size="sm"
            aria-label="Close the tutor"
            className={skin.ghost}
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
        <p
          className={cn(
            "flex items-start gap-2 rounded-lg p-3 text-xs",
            surface === "testing"
              ? "bg-exam-incorrectSoft text-exam-incorrect"
              : "bg-destructive/10 text-destructive"
          )}
        >
          <AlertCircle className="mt-0.5 h-4 w-4 shrink-0" />
          {error}
        </p>
      )}

      {hint ? (
        <div className="space-y-3">
          {/* Plain text, not MathContent: the prompt forbids LaTeX, and running
              model output through a renderer would execute markup the model
              chose rather than markup we wrote. */}
          <p
            className={cn(
              "whitespace-pre-wrap rounded-lg border p-3 text-sm leading-relaxed",
              skin.body
            )}
          >
            {hint}
          </p>
          {!exhausted && (
            <Button
              variant="outline"
              size="sm"
              className={cn(surface === "testing" && "border-exam-border bg-white text-exam-text hover:bg-exam-hover")}
              onClick={() => setHint(null)}
            >
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
            placeholder={copy.placeholder}
            className={cn("text-sm", surface === "testing" && "border-exam-border bg-white text-exam-text")}
          />
          <Button
            size="sm"
            className={cn("gap-2", surface === "testing" && "bg-exam-blue text-white hover:bg-exam-blueHover")}
            disabled={pending || exhausted}
            onClick={ask}
          >
            {pending ? (
              <>
                <Loader2 className="h-4 w-4 animate-spin" />
                Thinking…
              </>
            ) : (
              <>
                <Send className="h-4 w-4" />
                {copy.submit}
              </>
            )}
          </Button>
        </>
      )}

      <p className={cn("border-t pt-2 text-xs", skin.foot)}>{copy.foot}</p>
    </div>
  );
}
