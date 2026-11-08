"use client";

import {
  useCallback, useEffect, useRef, useState, useTransition, type CSSProperties,
} from "react";
import { useRouter } from "next/navigation";
import { ImagePlus, Loader2, X } from "lucide-react";
import { toast } from "sonner";

import { IeltsShell } from "@/components/ielts/ielts-shell";
import { NavButton } from "@/components/testing/primitives";
import { cn } from "@/lib/utils";
import { countWords } from "@/lib/ielts/answers";
import { ACCEPTED_IMAGE_TYPES, MAX_IMAGE_BYTES } from "@/lib/ielts/image-types";
import {
  attachWritingImage, removeWritingImage, saveWritingDraft, submitWriting,
} from "@/server/actions/student/ielts-writing";

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

const FULL_DIRECTIONS = [
  "This is a full Writing practice: both tasks, in one sitting, on one clock.",
  "Spend about 20 minutes on Task 1 and about 40 minutes on Task 2. Task 2 carries twice the weight of Task 1 in your Writing band, so do not run out of time on it.",
  "Move between the tasks whenever you like — unlike Speaking, nothing is hidden. Both go to the reviewer together, and you get a band for each task and one for the paper as a whole.",
];

export interface WritingTask {
  partId: string;
  taskNumber: number;
  title: string;
  promptHtml: string;
  /** Task 1's chart, table or diagram. */
  imageUrl?: string | null;
  imageAlt?: string | null;
  minWords: number;
  initialText: string;
  /** Task 1 only: the image the student attached to their answer, if any. */
  responseImageUrl?: string | null;
  /** True once this task has gone for review — its text is frozen. */
  readOnly: boolean;
}

/**
 * The Writing room.
 *
 * One component for a single task and for a full two-task sitting, because the
 * room is the same room — a split screen with the task on the left and the
 * answer on the right — and the only real difference is how many tasks the
 * footer can move between and whether one clock covers both. Building the full
 * practice as a second screen would have meant two copies of the autosave, the
 * divider and the word count, and they would have drifted.
 */
export function WritingWorkspace({
  tasks,
  paperTitle,
  suggestedMinutes,
  studentName,
  full = false,
}: {
  tasks: WritingTask[];
  paperTitle: string;
  /** The whole sitting's allowance: 20, 40, or 60 for a full practice. */
  suggestedMinutes: number;
  studentName: string;
  /** True when this is both tasks under one clock. */
  full?: boolean;
}) {
  const router = useRouter();

  // Start on the first task that still needs writing, so reopening a
  // half-finished sitting does not land on the essay already sent.
  const [index, setIndex] = useState(() => {
    const i = tasks.findIndex((t) => !t.readOnly);
    return i === -1 ? 0 : i;
  });
  const task = tasks[index];

  const [texts, setTexts] = useState<Record<string, string>>(() =>
    Object.fromEntries(tasks.map((t) => [t.partId, t.initialText]))
  );
  const [saved, setSaved] = useState<"idle" | "saving" | "saved">("idle");
  const [images, setImages] = useState<Record<string, string | null>>(() =>
    Object.fromEntries(tasks.map((t) => [t.partId, t.responseImageUrl ?? null]))
  );
  const [uploading, setUploading] = useState(false);
  const fileRef = useRef<HTMLInputElement>(null);
  const hasAnswer = (t: WritingTask) => Boolean((texts[t.partId] ?? "").trim() || images[t.partId]);
  const [pending, startTransition] = useTransition();
  const lastSaved = useRef<Record<string, string>>(
    Object.fromEntries(tasks.map((t) => [t.partId, t.initialText]))
  );

  const text = texts[task.partId] ?? "";
  const words = countWords(text);
  const short = words > 0 && words < task.minWords;
  const allReadOnly = tasks.every((t) => t.readOnly);

  const setText = (v: string) => setTexts((m) => ({ ...m, [task.partId]: v }));

  const save = useCallback(async () => {
    if (task.readOnly) return;
    const snapshot = texts[task.partId] ?? "";
    if (snapshot === lastSaved.current[task.partId]) return;
    setSaved("saving");
    const res = await saveWritingDraft(task.partId, snapshot);
    if (res.error) {
      setSaved("idle");
      return;
    }
    lastSaved.current[task.partId] = snapshot;
    setSaved("saved");
  }, [task.partId, task.readOnly, texts]);

  useEffect(() => {
    if (task.readOnly) return;
    const t = setTimeout(save, AUTOSAVE_MS);
    return () => clearTimeout(t);
  }, [save, task.readOnly]);

  // A draft in a closed tab is a lost essay. Best-effort — the browser gives no
  // guarantees during unload — but it catches the common case of navigating
  // away mid-task. Every task is flushed, not just the visible one: in a full
  // sitting the student may have moved to Task 2 with Task 1 unsaved.
  useEffect(() => {
    const onHide = () => {
      for (const t of tasks) {
        if (t.readOnly) continue;
        const v = texts[t.partId] ?? "";
        if (v !== lastSaved.current[t.partId]) void saveWritingDraft(t.partId, v);
      }
    };
    window.addEventListener("visibilitychange", onHide);
    window.addEventListener("pagehide", onHide);
    return () => {
      window.removeEventListener("visibilitychange", onHide);
      window.removeEventListener("pagehide", onHide);
    };
  }, [tasks, texts]);

  // Switching tasks flushes the one being left, so the draft is never a
  // keystroke behind when the student comes back to it.
  function goTo(i: number) {
    void save();
    setIndex(i);
    setSaved("idle");
  }

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

  async function onPickImage(file: File | undefined) {
    if (!file) return;
    if (!ACCEPTED_IMAGE_TYPES.includes(file.type)) {
      toast.error("Attach a PNG, JPEG, WebP or GIF image.");
      return;
    }
    if (file.size > MAX_IMAGE_BYTES) {
      toast.error("That image is larger than 8 MB. Try a smaller one.");
      return;
    }
    // Flush the text first so the draft row the image lands on is current.
    await save();
    const form = new FormData();
    form.set("partId", task.partId);
    form.set("image", file);
    setUploading(true);
    try {
      const res = await attachWritingImage(form);
      if (res.error) toast.error(res.error);
      else {
        setImages((m) => ({ ...m, [task.partId]: res.imageSrc ?? null }));
        toast.success("Image attached.");
      }
    } catch {
      toast.error("The image could not be uploaded. Check your connection and try again.");
    } finally {
      setUploading(false);
    }
  }

  async function onRemoveImage() {
    setUploading(true);
    try {
      const res = await removeWritingImage(task.partId);
      if (res.error) toast.error(res.error);
      else setImages((m) => ({ ...m, [task.partId]: null }));
    } finally {
      setUploading(false);
    }
  }

  function onSubmit() {
    const pendingTasks = tasks.filter((t) => !t.readOnly);
    const empty = pendingTasks.filter((t) => !hasAnswer(t));
    if (empty.length === pendingTasks.length) {
      toast.error("Write your response, or attach an image of it, before submitting.");
      return;
    }

    const shortOnes = pendingTasks
      .filter((t) => {
        const w = countWords(texts[t.partId] ?? "");
        return w > 0 && w < t.minWords;
      })
      .map((t) => `${t.title} is ${countWords(texts[t.partId] ?? "")} of ${t.minWords} words`);

    const lead = full
      ? `Send both tasks for free human review? This is one review — you get a band for each task and one for the paper.`
      : "Send this response for free human review? You will not be able to edit it afterwards.";
    const warning = [
      shortOnes.length ? `${shortOnes.join("; ")}. Under-length responses lose marks.` : "",
      empty.length ? `${empty.map((t) => t.title).join(" and ")} is empty and will not be sent.` : "",
      lead,
    ]
      .filter(Boolean)
      .join("\n\n");
    if (!window.confirm(warning)) return;

    startTransition(async () => {
      // Sequential rather than parallel: both submissions upsert the same
      // attempt row, and two at once would race on its status update.
      for (const t of pendingTasks) {
        const body = (texts[t.partId] ?? "").trim();
        if (!body && !images[t.partId]) continue;
        const res = await submitWriting(t.partId, body);
        if (res.error) {
          toast.error(res.error);
          return;
        }
      }
      toast.success(full ? "Both tasks sent for review." : "Sent for review.");
      router.push("/ielts/feedback");
      router.refresh();
    });
  }

  const directions = full ? FULL_DIRECTIONS : DIRECTIONS[task.taskNumber] ?? DIRECTIONS[2];

  return (
    <IeltsShell
      title={
        full
          ? `${paperTitle} — full practice`
          : `${paperTitle} — ${task.title}`
      }
      directions={directions}
      totalSeconds={allReadOnly ? null : suggestedMinutes * 60}
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
          {/* On a phone the task is already named by the Task 1 / Task 2
              buttons beside this, so the chip keeps only the count. */}
          {full && <span className="mr-2 hidden opacity-80 sm:inline">{task.title}</span>}
          <span className="hidden sm:inline">Word Count:&nbsp;</span>
          <span className="sm:hidden">Words&nbsp;</span>
          <span className={cn("tabular-nums", short && "text-exam-warning")}>{words}</span>
          <span className="opacity-70">&nbsp;/ {task.minWords}</span>
        </>
      }
      actions={
        <>
          {full && tasks.length > 1 && (
            <>
              {index > 0 && (
                <NavButton variant="ghost" action="prev-task" onClick={() => goTo(index - 1)}>
                  {tasks[index - 1].title}
                </NavButton>
              )}
              {index < tasks.length - 1 && (
                <NavButton variant="ghost" action="next-task" onClick={() => goTo(index + 1)}>
                  {tasks[index + 1].title}
                </NavButton>
              )}
            </>
          )}
          {allReadOnly ? (
            <span className="text-[13px] text-exam-muted">Sent for review</span>
          ) : (
            <>
              {/* Fixed width, always present.
                  The textarea saves on blur, so mousedown on a footer button
                  fires the save, which swapped this label from "" to "Saving…"
                  and pushed every button along — mouseup then landed on
                  nothing and the click never completed. Typing and then
                  clicking "Task 2" did nothing at all. Reserving the space
                  means the bar cannot reflow under the pointer. */}
              <span
                aria-live="polite"
                className="hidden w-[68px] shrink-0 text-right text-[12px] text-exam-muted sm:inline-block"
              >
                {saved === "saving" ? "Saving…" : saved === "saved" ? "Draft saved" : ""}
              </span>
              <NavButton action="submit" onClick={onSubmit} disabled={pending}>
                {pending ? "Sending…" : full ? "Submit both" : "Submit"}
              </NavButton>
            </>
          )}
        </>
      }
    >
      <div
        ref={splitRef}
        className="grid h-full grid-rows-[38vh_auto_1fr] overflow-hidden lg:grid-cols-[var(--prompt-w,46%)_auto_1fr] lg:grid-rows-1"
        style={promptPct ? ({ "--prompt-w": `${promptPct}%` } as CSSProperties) : undefined}
      >
        <section className="flex min-h-0 flex-col border-b border-exam-border bg-exam-passage lg:border-b-0">
          <div className="flex shrink-0 items-center justify-between gap-3 border-b border-exam-border bg-exam-header px-6 py-1.5 lg:px-10">
            <p className="text-[13px] font-semibold">{task.title}</p>
            {full && (
              <p className="text-[12px] text-exam-muted">
                Task {index + 1} of {tasks.length}
              </p>
            )}
          </div>
          <div className="exam-scroll min-h-0 flex-1 overflow-y-auto px-6 pb-10 pt-6 lg:px-10">
            <div className="max-w-[44rem] space-y-4">
              <div
                className="space-y-4 text-[16px] leading-[1.65] [&_li]:ml-5 [&_li]:list-disc [&_table]:border-collapse [&_ul]:space-y-1"
                dangerouslySetInnerHTML={{ __html: task.promptHtml }}
              />
              {/* Task 1's figure. It is the thing being described, so it sits
                  with the prompt and scrolls with it rather than living in a
                  lightbox the student has to keep reopening. */}
              {task.imageUrl && (
                // eslint-disable-next-line @next/next/no-img-element
                <img
                  src={task.imageUrl}
                  alt={task.imageAlt ?? "The figure for this task"}
                  className="max-w-full rounded border border-exam-border bg-white"
                />
              )}
            </div>
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
            <p className="text-[13px] font-semibold">{task.title} answer</p>
            <p className="text-[12px] tabular-nums text-exam-muted">
              Word Count: <span className={cn(short && "text-exam-warning font-semibold")}>{words}</span>
            </p>
          </div>
          {/* The textarea fills the pane rather than sitting in a fixed box:
              a student writing 300 words should never be typing into a
              four-line window with the rest of the screen empty.
              Keyed by part so switching tasks does not carry the caret,
              scroll position or undo history from the other essay. */}
          <textarea
            key={task.partId}
            value={text}
            onChange={(e) => setText(e.target.value)}
            onBlur={save}
            readOnly={task.readOnly}
            spellCheck={false}
            autoCorrect="off"
            autoCapitalize="off"
            autoComplete="off"
            aria-label={`Your response to ${task.title}`}
            placeholder={task.readOnly ? "" : "Type your response here."}
            className={cn(
              "exam-scroll min-h-0 flex-1 resize-none border-0 bg-transparent px-6 py-6 lg:px-10",
              "font-sans text-[16px] leading-[1.75] text-exam-text outline-none",
              "placeholder:text-exam-disabled focus-visible:ring-0",
              task.readOnly && "cursor-default text-exam-muted"
            )}
          />
          {/* Task 1 only: an optional image with the answer — a photo of a
              response written by hand, or a sketch of the figure. */}
          {task.taskNumber === 1 && (!task.readOnly || images[task.partId]) && (
            <div className="flex shrink-0 flex-wrap items-center gap-3 border-t border-exam-border bg-exam-header px-6 py-3 lg:px-10">
              {images[task.partId] ? (
                <>
                  <a
                    href={images[task.partId] ?? undefined}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="shrink-0"
                    title="Open the image full size"
                  >
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img
                      src={images[task.partId] ?? undefined}
                      alt="The image attached to your answer"
                      className="h-16 w-auto max-w-[8rem] rounded border border-exam-border bg-white object-contain"
                    />
                  </a>
                  <div className="min-w-0 flex-1">
                    <p className="text-[13px] font-semibold">Image attached</p>
                    <p className="text-[12px] text-exam-muted">
                      {task.readOnly ? "Sent with your answer." : "The reviewer sees it alongside your text."}
                    </p>
                  </div>
                  {!task.readOnly && (
                    <div className="flex items-center gap-2">
                      <button
                        type="button"
                        onClick={() => fileRef.current?.click()}
                        disabled={uploading || pending}
                        className="rounded border border-exam-border bg-white px-3 py-1.5 text-[13px] font-medium hover:bg-exam-passage disabled:opacity-50"
                      >
                        Replace
                      </button>
                      <button
                        type="button"
                        onClick={onRemoveImage}
                        disabled={uploading || pending}
                        aria-label="Remove the attached image"
                        className="inline-flex items-center gap-1 rounded border border-exam-border bg-white px-3 py-1.5 text-[13px] font-medium hover:bg-exam-passage disabled:opacity-50"
                      >
                        <X className="h-3.5 w-3.5" aria-hidden /> Remove
                      </button>
                    </div>
                  )}
                </>
              ) : (
                <>
                  <button
                    type="button"
                    onClick={() => fileRef.current?.click()}
                    disabled={uploading || pending}
                    className="inline-flex items-center gap-2 rounded border border-exam-border bg-white px-3 py-1.5 text-[13px] font-medium hover:bg-exam-passage disabled:opacity-50"
                  >
                    {uploading ? (
                      <Loader2 className="h-4 w-4 animate-spin" aria-hidden />
                    ) : (
                      <ImagePlus className="h-4 w-4" aria-hidden />
                    )}
                    {uploading ? "Uploading…" : "Attach an image"}
                  </button>
                  <p className="text-[12px] text-exam-muted">
                    Optional. A photo of a handwritten answer, or a sketch. PNG, JPEG, WebP or GIF, up to 8 MB.
                  </p>
                </>
              )}
              <input
                ref={fileRef}
                type="file"
                accept={ACCEPTED_IMAGE_TYPES.join(",")}
                className="hidden"
                onChange={(e) => {
                  void onPickImage(e.target.files?.[0]);
                  e.target.value = "";
                }}
              />
            </div>
          )}
        </section>
      </div>
    </IeltsShell>
  );
}
