import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { SpeakingRecorder } from "@/components/ielts/speaking-recorder";
import { SubmitSpeakingButton } from "@/components/ielts/submit-speaking-button";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { PRACTICE_DISCLAIMER } from "@/lib/ielts/bands";
import {
  REVIEWER_CLAIM, SPEAKING_PART2_PREP_SECONDS, SPEAKING_PART2_SPEAK_SECONDS,
} from "@/lib/ielts/constants";

export const metadata = { title: "Speaking Test" };
export const dynamic = "force-dynamic";

/**
 * Part 1 and Part 3 store their prompts as a JSON array of questions; Part 2 is
 * a single cue card held as HTML. One shape per part rather than a uniform one,
 * because the interview and the long turn genuinely differ.
 */
function promptsOf(part: { promptHtml: string | null; partNumber: number }) {
  if (part.partNumber === 2) return null;
  try {
    const parsed = JSON.parse(part.promptHtml ?? "[]");
    return Array.isArray(parsed) ? (parsed as string[]) : null;
  } catch {
    return null;
  }
}

export default async function SpeakingTestPage({ params }: { params: { testId: string } }) {
  const user = await requireUser();

  const test = await prisma.ieltsTest.findFirst({
    where: { id: params.testId, status: "PUBLISHED" },
    include: {
      sections: {
        where: { skill: "SPEAKING" },
        include: { parts: { orderBy: { partNumber: "asc" } } },
      },
    },
  });
  if (!test || !test.sections.length) notFound();
  const parts = test.sections[0].parts;

  const submission = await prisma.ieltsSpeakingSubmission.findFirst({
    where: { userId: user.id, attempt: { testId: test.id } },
    orderBy: { submittedAt: "desc" },
    include: { recordings: { select: { partId: true, questionIndex: true } } },
  });
  const locked = Boolean(submission && submission.status !== "PENDING");
  const done = new Set(
    (submission?.recordings ?? []).map((r) => `${r.partId}:${r.questionIndex}`)
  );

  const totalPrompts = parts.reduce(
    (n, p) => n + (p.partNumber === 2 ? 1 : (promptsOf(p)?.length ?? 1)), 0);

  return (
    <div className="space-y-5">
      <Link
        href="/ielts/speaking"
        className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground"
      >
        <ArrowLeft className="h-4 w-4" /> Speaking
      </Link>

      <div className="flex flex-wrap items-center gap-2">
        <h1 className="font-display text-xl font-semibold tracking-tight">{test.title}</h1>
        <Badge variant="outline">{done.size} of {totalPrompts} recorded</Badge>
        {locked && <Badge variant="navy">Sent for review</Badge>}
      </div>

      {parts.map((part) => {
        const questions = promptsOf(part);
        return (
          <Card key={part.id}>
            <CardHeader>
              <CardTitle className="text-base">{part.title ?? `Part ${part.partNumber}`}</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              {part.partNumber === 2 ? (
                <>
                  <p className="text-sm text-muted-foreground">
                    You have one minute to prepare, then up to two minutes to speak.
                    Recording starts automatically when preparation time ends.
                  </p>
                  <div
                    className="rounded-lg border border-border bg-secondary/40 p-4 text-sm leading-relaxed [&_li]:ml-5 [&_li]:list-disc [&_ul]:my-2 [&_ul]:space-y-1"
                    dangerouslySetInnerHTML={{ __html: part.promptHtml ?? "" }}
                  />
                  <SpeakingRecorder
                    partId={part.id}
                    questionIndex={0}
                    promptText={part.title ?? "Part 2 long turn"}
                    prepSeconds={part.prepSeconds ?? SPEAKING_PART2_PREP_SECONDS}
                    maxSeconds={part.speakSeconds ?? SPEAKING_PART2_SPEAK_SECONDS}
                    alreadyRecorded={done.has(`${part.id}:0`)}
                    locked={locked}
                  />
                </>
              ) : (
                <div className="space-y-3">
                  {(questions ?? []).map((q, i) => (
                    <div
                      key={i}
                      className="flex flex-wrap items-center justify-between gap-3 rounded-lg border border-border p-3"
                    >
                      <p className="min-w-[240px] flex-1 text-sm">{q}</p>
                      <SpeakingRecorder
                        partId={part.id}
                        questionIndex={i}
                        promptText={q}
                        maxSeconds={part.speakSeconds ?? 60}
                        alreadyRecorded={done.has(`${part.id}:${i}`)}
                        locked={locked}
                      />
                    </div>
                  ))}
                </div>
              )}
            </CardContent>
          </Card>
        );
      })}

      {!locked && (
        <div className="flex flex-wrap items-center gap-3 border-t border-border pt-4">
          <SubmitSpeakingButton
            testId={test.id}
            recordedCount={done.size}
            totalPrompts={totalPrompts}
          />
          <span className="text-sm text-muted-foreground">
            {REVIEWER_CLAIM.SPEAKING}. No payment required.
          </span>
        </div>
      )}

      <p className="text-xs text-muted-foreground">{PRACTICE_DISCLAIMER}</p>
    </div>
  );
}
