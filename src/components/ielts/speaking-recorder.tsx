"use client";

import { useEffect, useRef, useState } from "react";
import { Mic, Square, Loader2, Check, RotateCcw } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { saveSpeakingRecording } from "@/server/actions/student/ielts-speaking";

function clock(s: number) {
  return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`;
}

/**
 * Record one Speaking answer.
 *
 * The whole component is one prompt, because that is the unit that gets saved:
 * an answer is uploaded as soon as it is finished, so losing a connection
 * halfway through a fourteen-minute test costs the current answer, not the
 * sitting.
 *
 * Part 2 gets a preparation phase before recording can start. Everywhere else
 * `prepSeconds` is null and the button records immediately.
 */
export function SpeakingRecorder({
  partId,
  questionIndex,
  promptText,
  prepSeconds,
  maxSeconds,
  alreadyRecorded,
  locked,
}: {
  partId: string;
  questionIndex: number;
  promptText: string;
  prepSeconds?: number | null;
  maxSeconds: number;
  alreadyRecorded?: boolean;
  /** True once the sitting has gone for review. */
  locked?: boolean;
}) {
  type Phase = "idle" | "prep" | "recording" | "uploading" | "done";
  const [phase, setPhase] = useState<Phase>(alreadyRecorded ? "done" : "idle");
  const [elapsed, setElapsed] = useState(0);
  const [prepLeft, setPrepLeft] = useState(prepSeconds ?? 0);

  const recorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<BlobPart[]>([]);
  const streamRef = useRef<MediaStream | null>(null);
  const tickRef = useRef<ReturnType<typeof setInterval> | null>(null);

  // The microphone must be released when this unmounts, or the browser keeps
  // showing the recording indicator after the student has navigated away.
  useEffect(() => () => {
    tickRef.current && clearInterval(tickRef.current);
    streamRef.current?.getTracks().forEach((t) => t.stop());
  }, []);

  async function beginRecording() {
    let stream: MediaStream;
    try {
      stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    } catch {
      toast.error("SATForge needs microphone access to record your answer.");
      setPhase("idle");
      return;
    }
    streamRef.current = stream;
    chunksRef.current = [];

    const recorder = new MediaRecorder(stream);
    recorderRef.current = recorder;
    recorder.ondataavailable = (e) => e.data.size && chunksRef.current.push(e.data);
    recorder.onstop = () => void upload();
    recorder.start();

    setElapsed(0);
    setPhase("recording");
    tickRef.current = setInterval(() => {
      setElapsed((s) => {
        // Stop at the limit rather than letting the answer run on: the real
        // test cuts you off, and an over-long take is not the practice.
        if (s + 1 >= maxSeconds) stopRecording();
        return s + 1;
      });
    }, 1000);
  }

  function stopRecording() {
    tickRef.current && clearInterval(tickRef.current);
    tickRef.current = null;
    if (recorderRef.current?.state === "recording") recorderRef.current.stop();
    streamRef.current?.getTracks().forEach((t) => t.stop());
  }

  async function upload() {
    setPhase("uploading");
    const blob = new Blob(chunksRef.current, {
      type: recorderRef.current?.mimeType || "audio/webm",
    });
    const form = new FormData();
    form.set("partId", partId);
    form.set("questionIndex", String(questionIndex));
    form.set("promptText", promptText);
    form.set("durationSeconds", String(elapsed));
    form.set("audio", new File([blob], "answer.webm", { type: blob.type }));

    const res = await saveSpeakingRecording(form);
    if (res.error) {
      toast.error(res.error);
      setPhase("idle");
      return;
    }
    setPhase("done");
  }

  function startPrep() {
    if (!prepSeconds) return void beginRecording();
    setPrepLeft(prepSeconds);
    setPhase("prep");
    tickRef.current = setInterval(() => {
      setPrepLeft((s) => {
        if (s <= 1) {
          tickRef.current && clearInterval(tickRef.current);
          void beginRecording();
          return 0;
        }
        return s - 1;
      });
    }, 1000);
  }

  if (locked) {
    return (
      <span className="inline-flex items-center gap-1.5 text-sm text-muted-foreground">
        <Check className="h-4 w-4" /> {alreadyRecorded ? "Recorded" : "Not answered"}
      </span>
    );
  }

  return (
    <div className="flex flex-wrap items-center gap-3">
      {phase === "idle" && (
        <Button size="sm" onClick={startPrep}>
          <Mic className="mr-1 h-4 w-4" />
          {prepSeconds ? `Start (${prepSeconds}s to prepare)` : "Record answer"}
        </Button>
      )}

      {phase === "prep" && (
        <span className="inline-flex items-center gap-2 text-sm">
          <span className="font-semibold tabular-nums">{clock(prepLeft)}</span>
          <span className="text-muted-foreground">to prepare — recording starts automatically</span>
        </span>
      )}

      {phase === "recording" && (
        <>
          <span className="inline-flex items-center gap-2 text-sm font-medium text-red-600">
            <span className="h-2.5 w-2.5 animate-pulse rounded-full bg-red-600" />
            Recording {clock(elapsed)}
            <span className="text-muted-foreground">/ {clock(maxSeconds)}</span>
          </span>
          <Button size="sm" variant="outline" onClick={stopRecording}>
            <Square className="mr-1 h-3.5 w-3.5" /> Stop
          </Button>
        </>
      )}

      {phase === "uploading" && (
        <span className="inline-flex items-center gap-2 text-sm text-muted-foreground">
          <Loader2 className="h-4 w-4 animate-spin" /> Saving your answer…
        </span>
      )}

      {phase === "done" && (
        <>
          <span className="inline-flex items-center gap-1.5 text-sm text-emerald-700 dark:text-emerald-400">
            <Check className="h-4 w-4" /> Answer saved
          </span>
          <Button
            size="sm"
            variant="ghost"
            onClick={() => { setPhase("idle"); setElapsed(0); }}
            className={cn("text-muted-foreground")}
          >
            <RotateCcw className="mr-1 h-3.5 w-3.5" /> Record again
          </Button>
        </>
      )}
    </div>
  );
}
