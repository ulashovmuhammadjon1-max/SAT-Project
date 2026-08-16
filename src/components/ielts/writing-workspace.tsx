"use client";

import {
  useCallback, useEffect, useRef, useState, useTransition, type CSSProperties,
} from "react";
import { useRouter } from "next/navigation";
import { Loader2, Send } from "lucide-react";
import { toast } from "sonner";

import { IeltsShell } from "@/components/ielts/ielts-shell";
import { NavButton } from "@/components/testing/primitives";
import { cn } from "@/lib/utils";
import { countWords } from "@/lib/ielts/answers";
import { saveWritingDraft, submitWriting } from "@/server/actions/student/ielts-writing";

const AUTOSAVE_MS = 5000;

const SPLIT_DEFAULT = 46;
const SPLIT_MIN = 25;
const SPLIT_MAX = 70;

const DIRECTIONS: Record<number, string[]> = {
  1: [
    "You should spend about 20 minutes on this task.",
    "Summarise the information by selecting and reporting the main features, and make comparisons where relevant. Write at least 150 words.",
    "Your response is marked by a human reviewer on Task Achievement, Coherence and Cohesion, Lexical Resource, and Grammatical Range and Accuracy.",
  ],
  2: [
    "You should spend about 40 minutes on this task.",
    "Give reasons for your answer and include any relevant examples from your own knowledge or experience. Write at least 250 words.",
    "Your response is marked by a human reviewer on Task Response, Coherence and Cohesion, Lexical Resource, and Grammatical Range and Accuracy.",
  ],
};

/**
 * The Writing room.
 *
 * A full-screen split: the task on the left, the answer box on the right, a
 * divider the student can drag. The editor itself is deliberately plain — no
 * spellcheck, no autocorrect, no grammar hints — because the point of the
 * exercise is the student's own English and an editor that quietly fixes it
 * produces a script the reviewer cannot mark.
 */
export function WritingWorkspace({
  partId,
  taskNumber,
  taskTitle,
  paperTitle,
  promptHtml,
  minWords,
  suggestedMinutes,
  initialText,
  readOnly,
  studentName,
}: {
  partId: string;
  taskNumber: number;
  taskTitle: string;
  paperTitle: string;
  promptHtml: string;
  minWords: number;
  suggestedMinutes: number;
  initialText: string;
  /** True once the response has gone for review — the text is frozen. */
  readOnly: boolean;
  studentName: string;
}) {
  const router = useRouter();
  const [text, setText] = useState(initialText);
  const [saved, setSaved] = useState<"idle" | "saving" | "saved">("idle");
  const [pending, startTransition] = useTransition();
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

  // A draft in a closed tab is a lost essay. Best-effort — the browser gives no
  // guarantees during unload — but it catches the common case of navigating
  // away mid-task.
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

  // ---- the draggable divider -------------------------------------------
  const splitRef = useRef<HTMLDivElement>(null);
  const [promptPct, setPromptPct] = useState<number | null>(null);
  const [dragging, setDragging] = useState(false);

  useEffect(() => {
    if (!dragging) return;
    const onMove = (e: MouseEvent) => {
      const box = splitRef.current?.getBoundingClientRect();
      if (!box) return;
      const pct = ((e.clientX - box.left) / box.width) * 100;
      setPromptPct(Math.min(SPLIT_MAX, Math.max(SPLIT_MIN, pct)));
    };
    const onUp = () => setDragging(false);
    window.addEventListener("mousemove", onMove);
    window.addEventListener("mouseup", onUp);
    return () => {
      window.removeEventListener("mousemove", onMove);
      window.removeEventListener("mouseup", onUp);
    };
  }, [dragging]);

  function onSubmit() {
    if (!text.trim()) {
      toast.error("Write your response before submitting.");
      return;
    }
    const warning = short
      ? `That is ${words} words, under the ${minWords} minimum for Task ${taskNumber}. ` +
        "Under-length responses lose marks. Submit anyway?"
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
    <IeltsShell
      title={`${paperTitle} — ${taskTitle}`}
      directions={DIRECTIONS[taskNumber] ?? DIRECTIONS[2]}
      totalSeconds={readOnly ? null : suggestedMinutes * 60}
      onTimeUp={() =>
        toast.warning(
          `Your ${suggestedMinutes} minutes are up. Nothing has been submitted — finish your sentence and send it when you are ready.`
        )
      }
      bannerText="IELTS Academic Writing · practice"
      studentName={studentName}
      exitHref="/ielts/writing"
      centreLabel={
        <>
          Word Count:&nbsp;
          <span className={cn("tabular-nums", short && "text-exam-warning")}>{words}</span>
          <span className="opacity-70">&nbsp;/ {minWords}</span>
        </>
      }
      actions={
        readOnly ? (
          <span className="text-[13px] text-exam-muted">Sent for review</span>
        ) : (
          <>
            <span className="hidden text-[12px] text-exam-muted sm:inline">
              {saved === "saving" ? "Saving…" : saved === "saved" ? "Draft saved" : ""}
            </span>
            <NavButton onClick={onSubmit} disabled={pending}>
              {pending ? "Sending…" : "Submit"}
            </NavButton>
          </>
        )
      }
    >
      <div
        ref={splitRef}
        className="grid h-full grid-rows-[38vh_auto_1fr] overflow-hidden lg:grid-cols-[var(--prompt-w,46%)_auto_1fr] lg:grid-rows-1"
        style={promptPct ? ({ "--prompt-w": `${promptPct}%` } as CSSProperties) : undefined}
      >
        <section className="flex min-h-0 flex-col border-b border-exam-border bg-exam-passage lg:border-b-0">
          <div className="shrink-0 border-b border-exam-border bg-exam-header px-6 py-1.5 lg:px-10">
            <p className="text-[13px] font-semibold">{taskTitle}</p>
          </div>
          <div className="exam-scroll min-h-0 flex-1 overflow-y-auto px-6 pb-10 pt-6 lg:px-10">
            <div
              className="max-w-[44rem] space-y-4 text-[16px] leading-[1.65] [&_img]:my-4 [&_img]:max-w-full [&_li]:ml-5 [&_li]:list-disc [&_table]:border-collapse [&_ul]:space-y-1"
              dangerouslySetInnerHTML={{ __html: promptHtml }}
            />
          </div>
        </section>

        {/* Drag to resize. Double-click restores the default split. */}
        <div
          role="separator"
          aria-orientation="vertical"
          aria-label="Resize the task and answer panes"
          aria-valuemin={SPLIT_MIN}
          aria-valuemax={SPLIT_MAX}
          aria-valuenow={Math.round(promptPct ?? SPLIT_DEFAULT)}
          tabIndex={0}
          onMouseDown={() => setDragging(true)}
          onDoubleClick={() => setPromptPct(null)}
          onKeyDown={(e) => {
            if (e.key === "ArrowLeft") setPromptPct((p) => Math.max(SPLIT_MIN, (p ?? SPLIT_DEFAULT) - 2));
            if (e.key === "ArrowRight") setPromptPct((p) => Math.min(SPLIT_MAX, (p ?? SPLIT_DEFAULT) + 2));
          }}
          title="Drag to resize — double-click to reset"
          className={cn(
            "group relative hidden lg:flex lg:h-full lg:w-[9px] lg:cursor-col-resize lg:items-center lg:justify-center",
            "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-exam-blue",
            dragging ? "bg-exam-blue/15" : "bg-transparent"
          )}
        >
          <span
            className={cn(
              "absolute inset-y-0 left-1/2 w-px -translate-x-1/2",
              dragging ? "bg-exam-blue" : "bg-exam-divider group-hover:bg-exam-disabled"
            )}
          />
          <span
            className={cn(
              "relative h-9 w-[5px] rounded-full transition-colors",
              dragging ? "bg-exam-blue" : "bg-exam-divider group-hover:bg-exam-disabled"
            )}
          />
        </div>

        <section className="flex min-h-0 flex-col bg-exam-question">
          <div className="flex shrink-0 items-center justify-between gap-3 border-b border-exam-border bg-exam-header px-6 py-1.5 lg:px-10">
            <p className="text-[13px] font-semibold">Task {taskNumber} answer</p>
            <p className="text-[12px] tabular-nums text-exam-muted">
              Word Count: <span className={cn(short && "text-exam-warning font-semibold")}>{words}</span>
            </p>
          </div>
          {/* The textarea fills the pane rather than sitting in a fixed box:
              a student writing 300 words should never be typing into a
              four-line window with the rest of the screen empty. */}
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            onBlur={save}
            readOnly={readOnly}
            spellCheck={false}
            autoCorrect="off"
            autoCapitalize="off"
            autoComplete="off"
            aria-label={`Your response to Task ${taskNumber}`}
            placeholder={readOnly ? "" : "Type your response here."}
            className={cn(
              "exam-scroll min-h-0 flex-1 resize-none border-0 bg-transparent px-6 py-6 lg:px-10",
              "font-sans text-[16px] leading-[1.75] text-exam-text outline-none",
              "placeholder:text-exam-disabled focus-visible:ring-0",
              readOnly && "cursor-default text-exam-muted"
            )}
          />
        </section>
      </div>
    </IeltsShell>
  );
}
