"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { Check, Loader2, Mic, MicOff, RotateCcw, Square } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { saveSpeakingRecording } from "@/server/actions/student/ielts-speaking";

function clock(s: number) {
  return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`;
}

/**
 * The container the browser will actually produce.
 *
 * Chrome and Firefox give WebM/Opus; Safari — desktop and every iOS browser,
 * since they are all WebKit — gives MP4/AAC and rejects a WebM mimeType
 * outright. Constructing `new MediaRecorder(stream)` with no type at all works
 * on all of them, but then the blob's type is whatever the engine chose and
 * the file extension has to follow it, which is why the type is read back off
 * the recorder at upload rather than assumed here.
 */
function pickMimeType(): string | undefined {
  if (typeof MediaRecorder === "undefined") return undefined;
  const candidates = [
    "audio/webm;codecs=opus",
    "audio/webm",
    "audio/ogg;codecs=opus",
    "audio/mp4",
  ];
  return candidates.find((t) => MediaRecorder.isTypeSupported?.(t));
}

function extensionFor(mime: string): string {
  if (mime.includes("mp4")) return "m4a";
  if (mime.includes("ogg")) return "ogg";
  if (mime.includes("mpeg")) return "mp3";
  return "webm";
}

type Phase = "idle" | "prep" | "recording" | "uploading" | "done";

/**
 * Record one Speaking answer.
 *
 * One prompt per component, because that is the unit that gets saved: an answer
 * uploads as soon as it is finished, so losing a connection halfway through a
 * fourteen-minute interview costs the current answer, not the sitting.
 *
 * The parts that are easy to get wrong, and are deliberate here:
 *
 * - **Tracks are released in `onstop`, not after `stop()`.** `MediaRecorder.stop()`
 *   is asynchronous; killing the microphone track on the next line can cut off
 *   the final `dataavailable` and produce a blob missing its tail — or, when the
 *   answer is short, an empty one.
 * - **A timeslice is passed to `start()`**, so audio arrives in chunks
 *   throughout rather than in a single flush at the end. A tab closed mid-answer
 *   then still has most of the take in memory.
 * - **The elapsed count is a ref driven by the wall clock.** Reading React state
 *   inside `onstop` reads the value captured when recording began — which is
 *   zero, and was being saved as the answer's duration.
 * - **Auto-stop is never called from inside a state updater.** A side effect in
 *   an updater runs twice under StrictMode, and the second `stop()` throws
 *   `InvalidStateError` on an already-inactive recorder.
 * - **A live level meter runs while recording**, because the failure students
 *   actually hit is a muted or wrong input device, and that is invisible until
 *   they have already spoken for two minutes.
 */
export function SpeakingRecorder({
  partId,
  questionIndex,
  promptText,
  prepSeconds,
  maxSeconds,
  alreadyRecorded,
  locked,
  onRecorded,
}: {
  partId: string;
  questionIndex: number;
  promptText: string;
  prepSeconds?: number | null;
  maxSeconds: number;
  alreadyRecorded?: boolean;
  /** True once the sitting has gone for review. */
  locked?: boolean;
  /** Fired after an answer is stored, so a sequential runner can unlock Next. */
  onRecorded?: () => void;
}) {
  const [phase, setPhase] = useState<Phase>(alreadyRecorded ? "done" : "idle");
  const [elapsed, setElapsed] = useState(0);
  const [prepLeft, setPrepLeft] = useState(prepSeconds ?? 0);
  const [level, setLevel] = useState(0);
  const [playbackUrl, setPlaybackUrl] = useState<string | null>(null);
  const [heardSound, setHeardSound] = useState(false);

  const recorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);
  const streamRef = useRef<MediaStream | null>(null);
  const tickRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const prepRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const startedAtRef = useRef(0);
  const durationRef = useRef(0);
  const audioCtxRef = useRef<AudioContext | null>(null);
  const rafRef = useRef<number | null>(null);
  const heardRef = useRef(false);

  const clearTimers = useCallback(() => {
    if (tickRef.current) clearInterval(tickRef.current);
    if (prepRef.current) clearInterval(prepRef.current);
    if (rafRef.current) cancelAnimationFrame(rafRef.current);
    tickRef.current = null;
    prepRef.current = null;
    rafRef.current = null;
  }, []);

  const releaseMic = useCallback(() => {
    streamRef.current?.getTracks().forEach((t) => t.stop());
    streamRef.current = null;
    void audioCtxRef.current?.close().catch(() => {});
    audioCtxRef.current = null;
  }, []);

  // The microphone must be released on unmount, or the browser keeps showing
  // the recording indicator after the student has navigated away.
  useEffect(
    () => () => {
      clearTimers();
      releaseMic();
    },
    [clearTimers, releaseMic]
  );

  // Object URLs are revoked when they are replaced, not on every render, so a
  // student who re-records ten times does not leak ten blobs.
  useEffect(() => {
    return () => {
      if (playbackUrl) URL.revokeObjectURL(playbackUrl);
    };
  }, [playbackUrl]);

  const upload = useCallback(async () => {
    setPhase("uploading");
    const mime = recorderRef.current?.mimeType || "audio/webm";
    const blob = new Blob(chunksRef.current, { type: mime });

    if (blob.size === 0) {
      toast.error(
        "Nothing was recorded. Check that the right microphone is selected and that the browser tab is not muted, then try again."
      );
      setPhase("idle");
      return;
    }

    const form = new FormData();
    form.set("partId", partId);
    form.set("questionIndex", String(questionIndex));
    form.set("promptText", promptText);
    form.set("durationSeconds", String(Math.max(1, durationRef.current)));
    form.set("audio", new File([blob], `answer.${extensionFor(mime)}`, { type: mime }));

    // A rejected server action is the case this whole design exists for — a
    // connection that drops mid-interview. Without the catch the phase sticks
    // on "Saving your answer…" forever and the student has no way back to the
    // Record button.
    let res: Awaited<ReturnType<typeof saveSpeakingRecording>>;
    try {
      res = await saveSpeakingRecording(form);
    } catch {
      toast.error("Your answer could not be uploaded. Check your connection and record it again.");
      setPhase("idle");
      return;
    }
    if (res.error) {
      toast.error(res.error);
      setPhase("idle");
      return;
    }

    // Kept locally so the student can play back what was actually captured.
    // "It recorded nothing" is otherwise only discoverable after submitting.
    setPlaybackUrl((old) => {
      if (old) URL.revokeObjectURL(old);
      return URL.createObjectURL(blob);
    });
    setHeardSound(heardRef.current);
    setPhase("done");
    onRecorded?.();
  }, [partId, questionIndex, promptText, onRecorded]);

  const stopRecording = useCallback(() => {
    clearTimers();
    const rec = recorderRef.current;
    // Guarded: auto-stop and the Stop button can both land, and calling stop()
    // on an inactive recorder throws.
    if (rec && rec.state !== "inactive") rec.stop();
    else releaseMic();
  }, [clearTimers, releaseMic]);

  const beginRecording = useCallback(async () => {
    if (typeof navigator === "undefined" || !navigator.mediaDevices?.getUserMedia) {
      // getUserMedia is undefined outside a secure context, which is the single
      // most common reason recording "just does not work" — and it looks
      // identical to a permission problem unless it is named.
      toast.error(
        window.isSecureContext === false
          ? "Recording needs a secure connection (https). Open SATForge over https and try again."
          : "This browser cannot record audio. Try Chrome, Edge, Firefox or Safari."
      );
      setPhase("idle");
      return;
    }
    if (typeof MediaRecorder === "undefined") {
      toast.error("This browser cannot record audio. Try Chrome, Edge, Firefox or Safari.");
      setPhase("idle");
      return;
    }

    let stream: MediaStream;
    try {
      stream = await navigator.mediaDevices.getUserMedia({
        audio: { echoCancellation: true, noiseSuppression: true },
      });
    } catch (err) {
      const name = (err as DOMException)?.name;
      toast.error(
        name === "NotAllowedError"
          ? "Microphone access was blocked. Allow it in the address bar, then try again."
          : name === "NotFoundError"
            ? "No microphone was found. Plug one in or pick a different input device."
            : "SATForge could not start your microphone."
      );
      setPhase("idle");
      return;
    }
    streamRef.current = stream;
    chunksRef.current = [];
    heardRef.current = false;
    setHeardSound(false);

    const mimeType = pickMimeType();
    let recorder: MediaRecorder;
    try {
      recorder = new MediaRecorder(stream, mimeType ? { mimeType } : undefined);
    } catch {
      recorder = new MediaRecorder(stream);
    }
    recorderRef.current = recorder;
    recorder.ondataavailable = (e) => {
      if (e.data && e.data.size > 0) chunksRef.current.push(e.data);
    };
    recorder.onerror = () => {
      clearTimers();
      releaseMic();
      toast.error("Recording stopped unexpectedly. Please record the answer again.");
      setPhase("idle");
    };
    recorder.onstop = () => {
      // Only now is the last chunk in hand; releasing the microphone earlier
      // truncates it.
      releaseMic();
      void upload();
    };
    // A timeslice, so audio streams into chunks instead of arriving in one
    // flush at the very end.
    recorder.start(1000);

    startedAtRef.current = Date.now();
    durationRef.current = 0;
    setElapsed(0);
    setPhase("recording");

    tickRef.current = setInterval(() => {
      const s = Math.floor((Date.now() - startedAtRef.current) / 1000);
      durationRef.current = s;
      setElapsed(s);
      // Outside the state updater on purpose — see the component doc.
      if (s >= maxSeconds) stopRecording();
    }, 250);

    // Level meter. Failures here are cosmetic, so nothing about the recording
    // itself depends on the AudioContext starting.
    try {
      const Ctor: typeof AudioContext =
        window.AudioContext ??
        (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      const ctx = new Ctor();
      audioCtxRef.current = ctx;
      const analyser = ctx.createAnalyser();
      analyser.fftSize = 512;
      ctx.createMediaStreamSource(stream).connect(analyser);
      const buf = new Uint8Array(analyser.frequencyBinCount);
      const draw = () => {
        analyser.getByteTimeDomainData(buf);
        let peak = 0;
        for (let i = 0; i < buf.length; i++) peak = Math.max(peak, Math.abs(buf[i] - 128));
        const v = Math.min(1, peak / 64);
        if (v > 0.06) heardRef.current = true;
        setLevel(v);
        rafRef.current = requestAnimationFrame(draw);
      };
      draw();
    } catch {
      /* no meter; recording is unaffected */
    }
  }, [maxSeconds, stopRecording, upload, clearTimers, releaseMic]);

  const startPrep = useCallback(() => {
    if (!prepSeconds) {
      void beginRecording();
      return;
    }
    setPrepLeft(prepSeconds);
    setPhase("prep");
    const endsAt = Date.now() + prepSeconds * 1000;
    prepRef.current = setInterval(() => {
      const left = Math.ceil((endsAt - Date.now()) / 1000);
      setPrepLeft(Math.max(0, left));
      if (left <= 0) {
        if (prepRef.current) clearInterval(prepRef.current);
        prepRef.current = null;
        void beginRecording();
      }
    }, 250);
  }, [prepSeconds, beginRecording]);

  function skipPrep() {
    if (prepRef.current) clearInterval(prepRef.current);
    prepRef.current = null;
    void beginRecording();
  }

  if (locked) {
    return (
      <span className="inline-flex items-center gap-1.5 text-sm text-muted-foreground">
        {alreadyRecorded ? <Check className="h-4 w-4" /> : <MicOff className="h-4 w-4" />}
        {alreadyRecorded ? "Recorded" : "Not answered"}
      </span>
    );
  }

  return (
    <div className="space-y-3">
      {phase === "idle" && (
        <Button onClick={startPrep}>
          <Mic className="mr-1.5 h-4 w-4" />
          {prepSeconds ? `Start — ${prepSeconds}s to prepare` : "Record answer"}
        </Button>
      )}

      {phase === "prep" && (
        <div className="flex flex-wrap items-center gap-3">
          <span className="inline-flex items-center gap-2 text-sm">
            <span className="font-display text-2xl font-semibold tabular-nums">{clock(prepLeft)}</span>
            <span className="text-muted-foreground">
              to prepare — recording starts automatically
            </span>
          </span>
          <Button size="sm" variant="outline" onClick={skipPrep}>
            Start now
          </Button>
        </div>
      )}

      {phase === "recording" && (
        <div className="space-y-2">
          <div className="flex flex-wrap items-center gap-3">
            <span className="inline-flex items-center gap-2 text-sm font-medium text-red-600">
              <span className="h-2.5 w-2.5 animate-pulse rounded-full bg-red-600" />
              Recording {clock(elapsed)}
              <span className="text-muted-foreground">/ {clock(maxSeconds)}</span>
            </span>
            <Button size="sm" variant="outline" onClick={stopRecording}>
              <Square className="mr-1 h-3.5 w-3.5" /> Stop
            </Button>
          </div>
          {/* Proof the microphone is live before the student talks for two
              minutes into a muted input. */}
          <div className="flex items-center gap-2">
            <Mic className="h-3.5 w-3.5 text-muted-foreground" />
            <div className="h-1.5 w-40 overflow-hidden rounded-full bg-secondary">
              <div
                className={cn(
                  "h-full rounded-full transition-[width] duration-75",
                  level > 0.06 ? "bg-emerald-500" : "bg-muted-foreground/40"
                )}
                style={{ width: `${Math.round(level * 100)}%` }}
              />
            </div>
            {!heardRef.current && elapsed > 3 && (
              <span className="text-xs text-amber-600">
                No sound detected — check your microphone.
              </span>
            )}
          </div>
        </div>
      )}

      {phase === "uploading" && (
        <span className="inline-flex items-center gap-2 text-sm text-muted-foreground">
          <Loader2 className="h-4 w-4 animate-spin" /> Saving your answer…
        </span>
      )}

      {phase === "done" && (
        <div className="space-y-2">
          <div className="flex flex-wrap items-center gap-3">
            <span className="inline-flex items-center gap-1.5 text-sm font-medium text-emerald-700 dark:text-emerald-400">
              <Check className="h-4 w-4" /> Answer saved
            </span>
            <Button
              size="sm"
              variant="ghost"
              onClick={() => {
                setPhase("idle");
                setElapsed(0);
                setLevel(0);
              }}
              className="text-muted-foreground"
            >
              <RotateCcw className="mr-1 h-3.5 w-3.5" /> Record again
            </Button>
          </div>
          {playbackUrl && (
            <div className="space-y-1">
              <audio src={playbackUrl} controls className="h-9 w-full max-w-sm" />
              {!heardSound && (
                <p className="text-xs text-amber-600">
                  Very little sound was picked up. Play it back — if you cannot hear yourself,
                  record the answer again.
                </p>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
