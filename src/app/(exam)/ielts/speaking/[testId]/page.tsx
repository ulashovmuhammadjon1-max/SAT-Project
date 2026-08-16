import { notFound } from "next/navigation";

import {
  SpeakingInterview, type SpeakingPrompt,
} from "@/components/ielts/speaking-interview";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import {
  SPEAKING_PART2_PREP_SECONDS, SPEAKING_PART2_SPEAK_SECONDS,
} from "@/lib/ielts/constants";

export const metadata = { title: "Speaking Test" };
export const dynamic = "force-dynamic";

/**
 * Part 1 and Part 3 store their prompts as a JSON array of questions; Part 2 is
 * a single cue card held as HTML. One shape per part rather than a uniform one,
 * because the interview and the long turn genuinely differ.
 */
function questionsOf(part: { promptHtml: string | null; partNumber: number }): string[] | null {
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

  // Flattened to one ordered list, because the student walks it one card at a
  // time and the part boundaries are a label rather than a structure.
  const prompts: SpeakingPrompt[] = [];
  for (const part of test.sections[0].parts) {
    const title = part.title ?? `Part ${part.partNumber}`;
    if (part.partNumber === 2) {
      prompts.push({
        partId: part.id,
        partNumber: part.partNumber,
        partTitle: title,
        questionIndex: 0,
        promptText: title,
        cueCardHtml: part.promptHtml ?? "",
        prepSeconds: part.prepSeconds ?? SPEAKING_PART2_PREP_SECONDS,
        maxSeconds: part.speakSeconds ?? SPEAKING_PART2_SPEAK_SECONDS,
      });
      continue;
    }
    for (const [i, q] of (questionsOf(part) ?? []).entries()) {
      prompts.push({
        partId: part.id,
        partNumber: part.partNumber,
        partTitle: title,
        questionIndex: i,
        promptText: q,
        cueCardHtml: null,
        prepSeconds: null,
        maxSeconds: part.speakSeconds ?? 60,
      });
    }
  }

  const submission = await prisma.ieltsSpeakingSubmission.findFirst({
    where: { userId: user.id, attempt: { testId: test.id } },
    orderBy: { submittedAt: "desc" },
    include: { recordings: { select: { partId: true, questionIndex: true } } },
  });

  return (
    <SpeakingInterview
      testId={test.id}
      testTitle={test.title}
      prompts={prompts}
      recordedKeys={(submission?.recordings ?? []).map((r) => `${r.partId}:${r.questionIndex}`)}
      locked={Boolean(submission && submission.status !== "PENDING")}
      studentName={user.name ?? user.email ?? "Student"}
    />
  );
}
