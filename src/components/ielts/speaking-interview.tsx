"use client";

import { useMemo, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Check, Lock } from "lucide-react";
import { toast } from "sonner";

import { IeltsShell } from "@/components/ielts/ielts-shell";
import { SpeakingRecorder } from "@/components/ielts/speaking-recorder";
import { NavButton } from "@/components/testing/primitives";
import { cn } from "@/lib/utils";
import { submitSpeaking } from "@/server/actions/student/ielts-speaking";

export interface SpeakingPrompt {
  partId: string;
  partNumber: number;
  partTitle: string;
  questionIndex: number;
  /** Plain text for Parts 1 and 3; the cue-card heading for Part 2. */
  promptText: string;
  /** Part 2's cue card, as HTML. Null elsewhere. */
  cueCardHtml?: string | null;
  prepSeconds?: number | null;
  maxSeconds: number;
}

const DIRECTIONS = [
  "This is a practice IELTS Speaking interview. You will answer one question at a time.",
  "Part 1 is a short interview about familiar topics. Part 2 gives you a cue card: you have one minute to prepare and then speak for up to two minutes. Part 3 is a longer discussion of the Part 2 topic.",
  "Record your answer to each question before moving on. You cannot see the next question until the current one is answered, which is how the real interview works — there is no reading ahead.",
  "A human reviewer marks the whole interview on Fluency and Coherence, Lexical Resource, Grammatical Range and Accuracy, and Pronunciation.",
];

/**
 * The Speaking room: one cue card at a time, in order.
 *
 * The sequencing is the point. In a real interview the examiner asks one
 * question and you answer it; you never see what is coming. A page listing all
 * twelve prompts lets a student read ahead, plan every answer, and practise a
 * test they will not sit. So the next card does not exist on screen — not
 * hidden with CSS, not rendered and disabled — until the current one has an
 * answer stored on the server.
 *
 * Going *back* is allowed: re-recording an answer you are unhappy with is
 * ordinary practice, and it gives away nothing you have not already seen.
 */
export function SpeakingInterview({
  testId,
  testTitle,
  prompts,
  recordedKeys,
  locked,
  studentName,
}: {
  testId: string;
  testTitle: string;
  prompts: SpeakingPrompt[];
  /** `${partId}:${questionIndex}` for every answer already stored. */
  recordedKeys: string[];
  locked: boolean;
  studentName: string;
}) {
  const router = useRouter();
  const [done, setDone] = useState<Set<string>>(() => new Set(recordedKeys));
  const [pending, start] = useTransition();

  const keyOf = (p: SpeakingPrompt) => `${p.partId}:${p.questionIndex}`;

  // Resume where the student left off rather than at question 1, so a reload
  // does not walk them back through answers they have already given.
  const [index, setIndex] = useState(() => {
    const first = prompts.findIndex((p) => !recordedKeys.includes(`${p.partId}:${p.questionIndex}`));
    return first === -1 ? Math.max(0, prompts.length - 1) : first;
  });

  const current = prompts[index];
  const currentKey = current ? keyOf(current) : "";
  const answered = done.has(currentKey);
  const isLast = index === prompts.length - 1;
  const allDone = prompts.every((p) => done.has(keyOf(p)));

  // Where each part starts, so the card can announce "Part 2 of 3" without the
  // page needing a second grouped copy of the prompts.
  const partPositions = useMemo(() => {
    const seen: number[] = [];
    for (const p of prompts) if (!seen.includes(p.partNumber)) seen.push(p.partNumber);
    return seen;
  }, [prompts]);

  const inPart = prompts.filter((p) => p.partNumber === current?.partNumber);
  const positionInPart = inPart.findIndex((p) => keyOf(p) === currentKey) + 1;

  function onSubmit() {
    const recorded = prompts.filter((p) => done.has(keyOf(p))).length;
    const message =
      recorded < prompts.length
        ? `You have recorded ${recorded} of ${prompts.length} answers. Send anyway? You cannot add more afterwards.`
        : "Send your Speaking test for free human review? You cannot re-record afterwards.";
    if (!window.confirm(message)) return;

    start(async () => {
      const res = await submitSpeaking(testId);
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success("Sent for review.");
      router.push("/ielts/feedback");
      router.refresh();
    });
  }

  if (!current) {
    return (
      <IeltsShell
        title={testTitle}
        studentName={studentName}
        exitHref="/ielts/speaking"
        bannerText="IELTS Speaking · practice"
      >
        <div className="flex h-full items-center justify-center p-10 text-center text-[15px] text-exam-muted">
          This Speaking paper has no prompts yet.
        </div>
      </IeltsShell>
    );
  }

  return (
    <IeltsShell
      title={`${testTitle} — ${current.partTitle}`}
      directions={DIRECTIONS}
      bannerText="IELTS Speaking · practice"
      studentName={studentName}
      exitHref="/ielts/speaking"
      centreLabel={`Question ${index + 1} of ${prompts.length}`}
      actions={
        <>
          {index > 0 && <NavButton variant="ghost" action="prev-question" onClick={() => setIndex(index - 1)}>Back</NavButton>}
          {!isLast ? (
            <NavButton action="next-question" onClick={() => setIndex(index + 1)} disabled={!answered}>
              Next
            </NavButton>
          ) : (
            !locked && (
              <NavButton action="submit" onClick={onSubmit} disabled={pending || done.size === 0}>
                {pending ? "Sending…" : "Submit"}
              </NavButton>
            )
          )}
        </>
      }
    >
      <div className="exam-scroll h-full overflow-y-auto px-4 py-8">
        <div className="mx-auto w-full max-w-[46rem] space-y-5">
          {/* Progress across the three parts, without naming a single unasked
              question. */}
          <div className="flex flex-wrap items-center justify-center gap-2">
            {partPositions.map((n) => {
              const partPrompts = prompts.filter((p) => p.partNumber === n);
              const complete = partPrompts.every((p) => done.has(keyOf(p)));
              const active = n === current.partNumber;
              return (
                <span
                  key={n}
                  className={cn(
                    "inline-flex items-center gap-1.5 rounded-full border px-3 py-1 text-[12px] font-medium",
                    active
                      ? "border-exam-blue bg-exam-blue text-white"
                      : complete
                        ? "border-exam-border bg-white text-exam-text"
                        : "border-exam-border bg-transparent text-exam-muted"
                  )}
                >
                  {complete && !active && <Check className="h-3 w-3" />}
                  Part {n}
                </span>
              );
            })}
          </div>

          <div className="rounded-md border border-exam-border bg-white shadow-sm">
            <div className="flex items-center justify-between gap-3 border-b border-exam-border bg-exam-header px-5 py-2">
              <p className="text-[13px] font-semibold">{current.partTitle}</p>
              <p className="text-[12px] text-exam-muted">
                Question {positionInPart} of {inPart.length} in this part
              </p>
            </div>

            <div className="px-6 py-7">
              {current.cueCardHtml ? (
                <>
                  <p className="mb-4 text-[13px] text-exam-muted">
                    You have {Math.round((current.prepSeconds ?? 60) / 60) || 1} minute to prepare,
                    then up to {Math.round((current.maxSeconds ?? 120) / 60)} minutes to speak.
                    Recording starts automatically when preparation time ends.
                  </p>
                  <div
                    className="rounded-md border border-exam-border bg-exam-passage p-5 text-[17px] leading-[1.7] [&_li]:ml-5 [&_li]:list-disc [&_p]:mb-2 [&_ul]:my-2 [&_ul]:space-y-1"
                    dangerouslySetInnerHTML={{ __html: current.cueCardHtml }}
                  />
                </>
              ) : (
                // Parts 1 and 3 get the same card treatment, large and alone on
                // the screen, so the student is looking at one question the way
                // they would be listening to one.
                <p className="text-[20px] font-medium leading-[1.55]">{current.promptText}</p>
              )}
            </div>

            <div className="border-t border-exam-border px-6 py-5">
              {locked ? (
                <span className="inline-flex items-center gap-1.5 text-[14px] text-exam-muted">
                  <Lock className="h-4 w-4" />
                  This sitting has been sent for review.
                </span>
              ) : (
                <SpeakingRecorder
                  // Remounted per prompt: the recorder holds a microphone
                  // stream and a phase, and carrying either across questions is
                  // how a student ends up recording answer 4 into slot 3.
                  key={currentKey}
                  partId={current.partId}
                  questionIndex={current.questionIndex}
                  promptText={current.promptText}
                  prepSeconds={current.prepSeconds}
                  maxSeconds={current.maxSeconds}
                  alreadyRecorded={answered}
                  onRecorded={() => setDone((s) => new Set(s).add(currentKey))}
                />
              )}
            </div>
          </div>

          {!answered && !locked && (
            <p className="text-center text-[13px] text-exam-muted">
              Record this answer to continue. The next question stays hidden until you do.
            </p>
          )}

          {isLast && allDone && !locked && (
            <p className="text-center text-[13px] text-exam-muted">
              That is the last question. Submit when you are ready — a reviewer will listen to the
              whole interview and score all four criteria.
            </p>
          )}
        </div>
      </div>
    </IeltsShell>
  );
}
