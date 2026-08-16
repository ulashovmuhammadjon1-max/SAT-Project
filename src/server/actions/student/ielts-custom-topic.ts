"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { savePromptImage } from "@/lib/ielts/image-storage";

export interface CustomTopicResult {
  ok?: boolean;
  error?: string;
  /** The paper created, for redirecting into the room. */
  testId?: string;
  /** The single task's part id, when only one task was created. */
  partId?: string;
}

/**
 * Escape a student-supplied prompt into safe HTML.
 *
 * The prompt is rendered with `dangerouslySetInnerHTML` in both the writing
 * room and the reviewer's screen, so it is escaped here rather than trusted.
 * Paragraph breaks survive because a real IELTS prompt has them — a Task 2
 * question is a situation, then the instruction — and flattening it would make
 * the student's own topic read worse than the authored ones.
 */
function toPromptHtml(text: string): string {
  const escaped = text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
  return escaped
    .split(/\n{2,}/)
    .map((p) => `<p>${p.trim().replace(/\n/g, "<br/>")}</p>`)
    .filter((p) => p !== "<p></p>")
    .join("");
}

const MIN_PROMPT_CHARS = 20;

export interface CustomTopicInput {
  /** Which tasks to create. Both is a full 60-minute practice. */
  mode: "TASK_1" | "TASK_2" | "BOTH";
  task1Text?: string;
  task2Text?: string;
}

/**
 * Create a paper from a student's own topic.
 *
 * The topic becomes a real `IeltsPart` on a real (unpublished) `IeltsTest`,
 * rather than a special case threaded through the submission. Everything
 * downstream — the writing room, the word minimum, the reviewer's screen, the
 * band roll-up, the feedback page — then works on it unchanged, because it is
 * not a different kind of thing. The paper is DRAFT, so it never appears in
 * anyone else's list.
 *
 * One paper per sitting rather than one shared "custom" paper: the attempt is
 * what the whole-paper Writing band is computed over, and piling every custom
 * topic a student ever writes into one attempt would average unrelated essays
 * together.
 */
export async function createCustomTopic(form: FormData): Promise<CustomTopicResult> {
  const user = await requireUser();

  const mode = String(form.get("mode") ?? "TASK_2") as CustomTopicInput["mode"];
  const task1Text = String(form.get("task1Text") ?? "").trim();
  const task2Text = String(form.get("task2Text") ?? "").trim();
  const image = form.get("task1Image");

  const needsTask1 = mode === "TASK_1" || mode === "BOTH";
  const needsTask2 = mode === "TASK_2" || mode === "BOTH";

  if (needsTask1 && task1Text.length < MIN_PROMPT_CHARS) {
    return { error: "Write out the Task 1 question — at least a sentence." };
  }
  if (needsTask2 && task2Text.length < MIN_PROMPT_CHARS) {
    return { error: "Write out the Task 2 question — at least a sentence." };
  }

  // Task 1 IS the figure. A Task 1 with no chart is not a Task 1 — there is
  // nothing to select, report or compare, and a reviewer cannot mark Task
  // Achievement against a description of a picture nobody can see.
  let imagePath: string | null = null;
  if (needsTask1) {
    if (!(image instanceof File) || image.size === 0) {
      return { error: "Task 1 needs its chart, table or diagram. Upload the image." };
    }
    try {
      imagePath = await savePromptImage(image, user.id);
    } catch (err) {
      return { error: err instanceof Error ? err.message : "That image could not be saved." };
    }
  }

  // Just the paper's name. The room appends the task ("Your own topic —
  // Task 1") or the mode ("— full practice"), so naming the task here too
  // produced "Your own topic — Task 1 — Task 1" in the header.
  const label = "Your own topic";

  const created = await prisma.ieltsTest.create({
    data: {
      title: label,
      // cuid keeps the unique slug unique without a lookup-and-retry loop.
      slug: `custom-${user.id.slice(0, 6)}-${Date.now().toString(36)}`,
      module: "ACADEMIC",
      status: "DRAFT",
      description: "A topic this student supplied.",
      sections: {
        create: {
          skill: "WRITING",
          order: 1,
          durationMinutes: mode === "BOTH" ? 60 : mode === "TASK_1" ? 20 : 40,
          instructions:
            mode === "BOTH"
              ? "Spend about 20 minutes on Task 1 and about 40 minutes on Task 2."
              : null,
          parts: {
            create: [
              ...(needsTask1
                ? [{
                    partNumber: 1,
                    title: "Task 1",
                    promptHtml: toPromptHtml(task1Text),
                    imageUrl: imagePath,
                    imageAlt: "The chart, table or diagram for this Task 1",
                    minWords: 150,
                  }]
                : []),
              ...(needsTask2
                ? [{
                    partNumber: 2,
                    title: "Task 2",
                    promptHtml: toPromptHtml(task2Text),
                    minWords: 250,
                  }]
                : []),
            ],
          },
        },
      },
    },
    select: { id: true, sections: { select: { parts: { select: { id: true, partNumber: true } } } } },
  });

  // The attempt is created now, not on first save: it is what proves ownership
  // of this paper, and the prompt-image route reads it before any work exists.
  await prisma.ieltsAttempt.create({
    data: {
      userId: user.id,
      testId: created.id,
      mode: "PRACTICE",
      status: "IN_PROGRESS",
      skills: ["WRITING"],
    },
  });

  const parts = created.sections[0]?.parts ?? [];
  revalidatePath("/ielts/writing");
  return {
    ok: true,
    testId: created.id,
    partId: mode === "BOTH" ? undefined : parts[0]?.id,
  };
}
