"use client";

import { useCallback, useEffect, useRef, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Send } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { countWords } from "@/lib/ielts/answers";
import { saveWritingDraft, submitWriting } from "@/server/actions/student/ielts-writing";

const AUTOSAVE_MS = 5000;

/**
 * The Writing task editor.
 *
 * Deliberately plain: no spelling correction, no grammar hints, no rewriting.
 * The point of the exercise is the student's own English, and an editor that
 * quietly fixes it produces a submission the reviewer cannot mark.
 */
export function WritingEditor({
  partId,
  taskNumber,
  minWords,
  initialText,
  readOnly,
}: {
  partId: string;
  taskNumber: number;
  minWords: number;
  initialText: string;
  /** True once the response has gone for review — the text is frozen. */
  readOnly: boolean;
}) {
  const router = useRouter();
  const [text, setText] = useState(initialText);
  const [saved, setSaved] = useState<"idle" | "saving" | "saved">("idle");
  const [pending, startTransition] = useTransition();
  // What was last written to the server, so an unchanged draft is not re-sent
  // every five seconds for as long as the tab is open.
  const lastSaved = useRef(initialText);

  const words = countWords(text);
  const short = words > 0 && words < minWords;

  const save = useCallback(async () => {
    if (readOnly || text === lastSaved.current) return;
    setSaved("saving");
    const snapshot = text;
    const res = await saveWritingDraft(partId, snapshot);
    if (res.error) {
      setSaved("idle");
      return;
    }
    lastSaved.current = snapshot;
    setSaved("saved");
  }, [partId, text, readOnly]);

  useEffect(() => {
    if (readOnly) return;
    const t = setTimeout(save, AUTOSAVE_MS);
    return () => clearTimeout(t);
  }, [save, readOnly]);

  // A draft in a closed tab is a lost essay. This is best-effort — the browser
  // gives no guarantees during unload — but it costs nothing and catches the
  // common case of navigating away mid-task.
  useEffect(() => {
    if (readOnly) return;
    const onHide = () => {
      if (text !== lastSaved.current) void saveWritingDraft(partId, text);
    };
    window.addEventListener("visibilitychange", onHide);
    window.addEventListener("pagehide", onHide);
    return () => {
      window.removeEventListener("visibilitychange", onHide);
      window.removeEventListener("pagehide", onHide);
    };
  }, [partId, text, readOnly]);

  function onSubmit() {
    if (!text.trim()) {
      toast.error("Write your response before submitting.");
      return;
    }
    const warning = short
      ? `That is ${words} words, under the ${minWords} minimum for Task ${taskNumber}. ` +
        `Under-length responses lose marks. Submit anyway?`
      : "Send this response for free human review? You will not be able to edit it afterwards.";
    if (!window.confirm(warning)) return;

    startTransition(async () => {
      const res = await submitWriting(partId, text);
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success("Sent for review.");
      router.push("/ielts/feedback");
      router.refresh();
    });
  }

  return (
    <div className="flex h-full flex-col gap-3">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        onBlur={save}
        readOnly={readOnly}
        spellCheck={false}
        autoCorrect="off"
        autoCapitalize="off"
        aria-label={`Your response to Task ${taskNumber}`}
        placeholder={readOnly ? "" : "Type your response here."}
        className={cn(
          "min-h-[420px] flex-1 resize-y rounded-lg border border-border bg-card p-4",
          "font-sans text-[15px] leading-relaxed outline-none",
          "focus-visible:ring-2 focus-visible:ring-ring",
          readOnly && "cursor-default bg-secondary/40 text-muted-foreground"
        )}
      />

      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3 text-sm">
          <span className="tabular-nums">
            <span className={cn("font-semibold", short && "text-amber-600")}>{words}</span>
            <span className="text-muted-foreground"> / {minWords} words</span>
          </span>
          {!readOnly && (
            <span className="text-xs text-muted-foreground">
              {saved === "saving" ? "Saving…" : saved === "saved" ? "Draft saved" : ""}
            </span>
          )}
        </div>

        {readOnly ? (
          <span className="text-sm text-muted-foreground">Sent for review</span>
        ) : (
          <Button onClick={onSubmit} disabled={pending}>
            {pending ? (
              <Loader2 className="mr-1 h-4 w-4 animate-spin" />
            ) : (
              <Send className="mr-1 h-4 w-4" />
            )}
            Submit for free human review
          </Button>
        )}
      </div>
    </div>
  );
}
