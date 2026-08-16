"use client";

import { useRef, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { ImageUp, Loader2, X } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { cn } from "@/lib/utils";
import { ACCEPTED_IMAGE_TYPES, MAX_IMAGE_BYTES } from "@/lib/ielts/image-types";
import { createCustomTopic } from "@/server/actions/student/ielts-custom-topic";

type Mode = "TASK_1" | "TASK_2" | "BOTH";

const MODES: { value: Mode; label: string; blurb: string }[] = [
  {
    value: "TASK_2",
    label: "Task 2 only",
    blurb: "An essay question. 40 minutes, at least 250 words.",
  },
  {
    value: "TASK_1",
    label: "Task 1 only",
    blurb: "A chart, table or diagram to describe. 20 minutes, at least 150 words.",
  },
  {
    value: "BOTH",
    label: "Full practice",
    blurb: "Both tasks in one 60-minute sitting, and one band for the paper.",
  },
];

/**
 * Bring your own topic.
 *
 * A student preparing for a specific exam usually has the questions their
 * teacher set, or last year's paper, and the useful thing is feedback on
 * *those* — not on whichever two prompts happen to be published here.
 */
export function CustomTopicForm() {
  const router = useRouter();
  const [mode, setMode] = useState<Mode>("TASK_2");
  const [task1, setTask1] = useState("");
  const [task2, setTask2] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [pending, start] = useTransition();
  const inputRef = useRef<HTMLInputElement>(null);

  const needsTask1 = mode === "TASK_1" || mode === "BOTH";
  const needsTask2 = mode === "TASK_2" || mode === "BOTH";

  function pickFile(f: File | null) {
    if (!f) return;
    if (!ACCEPTED_IMAGE_TYPES.includes(f.type)) {
      toast.error("Upload a PNG, JPEG, WebP or GIF image.");
      return;
    }
    if (f.size > MAX_IMAGE_BYTES) {
      toast.error("That image is larger than 8 MB. Try a smaller one.");
      return;
    }
    setFile(f);
    setPreview((old) => {
      if (old) URL.revokeObjectURL(old);
      return URL.createObjectURL(f);
    });
  }

  function clearFile() {
    setFile(null);
    setPreview((old) => {
      if (old) URL.revokeObjectURL(old);
      return null;
    });
    if (inputRef.current) inputRef.current.value = "";
  }

  function onSubmit() {
    // Checked here so the student is told before the round trip; the server
    // enforces the same rule, because this one is not optional.
    if (needsTask1 && !file) {
      toast.error("Task 1 needs its chart, table or diagram. Upload the image.");
      return;
    }

    const form = new FormData();
    form.set("mode", mode);
    if (needsTask1) form.set("task1Text", task1);
    if (needsTask2) form.set("task2Text", task2);
    if (file) form.set("task1Image", file);

    start(async () => {
      const res = await createCustomTopic(form);
      if (res.error) {
        toast.error(res.error);
        return;
      }
      router.push(
        res.partId ? `/ielts/writing/${res.partId}` : `/ielts/writing/full/${res.testId}`
      );
      router.refresh();
    });
  }

  return (
    <div className="space-y-6">
      <div className="space-y-2">
        <Label className="text-sm font-medium">What do you want to write?</Label>
        <div className="grid gap-2 sm:grid-cols-3">
          {MODES.map((m) => (
            <button
              key={m.value}
              type="button"
              onClick={() => setMode(m.value)}
              aria-pressed={mode === m.value}
              className={cn(
                "rounded-xl border p-3 text-left transition-colors",
                mode === m.value
                  ? "border-primary bg-primary/5"
                  : "border-border hover:bg-secondary"
              )}
            >
              <p className="text-sm font-semibold">{m.label}</p>
              <p className="mt-0.5 text-xs text-muted-foreground">{m.blurb}</p>
            </button>
          ))}
        </div>
      </div>

      {needsTask1 && (
        <div className="space-y-4 rounded-xl border border-border p-4">
          <div className="space-y-1.5">
            <Label className="text-sm font-medium">Task 1 question</Label>
            <Textarea
              rows={4}
              value={task1}
              onChange={(e) => setTask1(e.target.value)}
              placeholder={
                "The chart below shows … Summarise the information by selecting and reporting " +
                "the main features, and make comparisons where relevant."
              }
            />
          </div>

          <div className="space-y-1.5">
            <Label className="text-sm font-medium">
              The chart, table or diagram <span className="text-destructive">*</span>
            </Label>
            {/* Required, and said plainly. A Task 1 with no figure is not a
                Task 1 — there is nothing to select, report or compare, and a
                reviewer cannot mark Task Achievement against a picture nobody
                can see. */}
            <p className="text-xs text-muted-foreground">
              Photograph it or screenshot it. PNG, JPEG, WebP or GIF, up to 8 MB. Your
              reviewer sees this next to your writing; nobody else does.
            </p>

            {preview ? (
              <div className="relative inline-block">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={preview}
                  alt="The figure you uploaded"
                  className="max-h-64 rounded-lg border border-border bg-white"
                />
                <button
                  type="button"
                  onClick={clearFile}
                  aria-label="Remove this image"
                  className="absolute -right-2 -top-2 rounded-full border border-border bg-card p-1 shadow-soft hover:bg-secondary"
                >
                  <X className="h-3.5 w-3.5" />
                </button>
              </div>
            ) : (
              <button
                type="button"
                onClick={() => inputRef.current?.click()}
                className="flex w-full flex-col items-center gap-2 rounded-lg border border-dashed border-border p-6 text-sm text-muted-foreground transition-colors hover:bg-secondary"
              >
                <ImageUp className="h-6 w-6" />
                Choose an image
              </button>
            )}
            <input
              ref={inputRef}
              type="file"
              accept={ACCEPTED_IMAGE_TYPES.join(",")}
              className="hidden"
              onChange={(e) => pickFile(e.target.files?.[0] ?? null)}
            />
          </div>
        </div>
      )}

      {needsTask2 && (
        <div className="space-y-1.5 rounded-xl border border-border p-4">
          <Label className="text-sm font-medium">Task 2 question</Label>
          <Textarea
            rows={5}
            value={task2}
            onChange={(e) => setTask2(e.target.value)}
            placeholder={
              "Some people believe that … Others argue that …\n\n" +
              "Discuss both views and give your own opinion."
            }
          />
          <p className="text-xs text-muted-foreground">
            Paste it exactly as it was set. A blank line starts a new paragraph.
          </p>
        </div>
      )}

      <div className="flex flex-wrap items-center gap-3">
        <Button onClick={onSubmit} disabled={pending}>
          {pending && <Loader2 className="mr-1 h-4 w-4 animate-spin" />}
          Start writing
        </Button>
        <span className="text-sm text-muted-foreground">
          You can review the question before you submit — nothing is sent yet.
        </span>
      </div>
    </div>
  );
}
