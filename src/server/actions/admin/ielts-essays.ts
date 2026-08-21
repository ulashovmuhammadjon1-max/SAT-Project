"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import {
  analyzeEssay,
  countWords,
  EssayAnalysisError,
  hashEssayText,
} from "@/lib/ielts/essay-analysis";
import {
  annotationInputSchema,
  essayInputSchema,
  ideaInputSchema,
} from "@/lib/validations/ielts-essay";

/**
 * Admin curation of the Band 8+ Task 2 essay library.
 *
 * Every action here re-checks `requireAdmin` rather than trusting that the
 * route was protected. A server action is a public HTTP endpoint; the layout it
 * happens to be rendered under is not a permission check.
 *
 * The pipeline the statuses encode:
 *   DRAFT -> (analyze) -> ANALYZING -> NEEDS_REVIEW -> (admin approves) ->
 *   READY -> (publish) -> PUBLISHED
 * An essay cannot skip NEEDS_REVIEW, which is what keeps the model an
 * assistant rather than the author of what a student reads.
 */

export interface ActionResult {
  ok?: boolean;
  error?: string;
  essayId?: string;
  /** Non-fatal notes from an analysis run, for the admin only. */
  warnings?: string[];
}

const REVALIDATE = ["/admin/ielts/essays", "/ielts/essays"];
const revalidateAll = (essayId?: string) => {
  for (const p of REVALIDATE) revalidatePath(p);
  if (essayId) {
    revalidatePath(`/admin/ielts/essays/${essayId}`);
    revalidatePath(`/ielts/essays/${essayId}`);
  }
};

function readEssayForm(form: FormData) {
  const rawTags = String(form.get("tags") ?? "").trim();
  return essayInputSchema.safeParse({
    title: String(form.get("title") ?? ""),
    question: String(form.get("question") ?? ""),
    essayText: String(form.get("essayText") ?? ""),
    band: Number(form.get("band")),
    topic: String(form.get("topic") ?? ""),
    subtopic: String(form.get("subtopic") ?? ""),
    tags: rawTags ? rawTags.split(",").map((t) => t.trim()).filter(Boolean) : [],
  });
}

export async function createEssay(form: FormData): Promise<ActionResult> {
  await requireAdmin();
  const parsed = readEssayForm(form);
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Check the form." };
  }
  const admin = await requireAdmin();
  const d = parsed.data;

  const essay = await prisma.ieltsEssay.create({
    data: {
      title: d.title,
      question: d.question,
      essayText: d.essayText,
      band: d.band,
      topic: d.topic,
      subtopic: d.subtopic || null,
      tags: d.tags,
      wordCount: countWords(d.essayText),
      status: "DRAFT",
      createdById: admin.id,
    },
    select: { id: true },
  });

  revalidateAll(essay.id);
  return { ok: true, essayId: essay.id };
}

export async function updateEssay(essayId: string, form: FormData): Promise<ActionResult> {
  await requireAdmin();
  const parsed = readEssayForm(form);
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Check the form." };
  }
  const d = parsed.data;

  const existing = await prisma.ieltsEssay.findUnique({
    where: { id: essayId },
    select: { essayText: true, status: true, analyzedTextHash: true },
  });
  if (!existing) return { error: "That essay no longer exists." };

  // Editing the essay text moves every offset after the edit. Rather than
  // leave highlights pointing at the wrong words, the essay drops out of
  // PUBLISHED and back to a state that demands a re-analysis. Silently keeping
  // stale annotations would teach students the wrong thing about the right
  // sentence.
  const textChanged = existing.essayText !== d.essayText;
  const stale = textChanged && existing.analyzedTextHash !== null;

  await prisma.ieltsEssay.update({
    where: { id: essayId },
    data: {
      title: d.title,
      question: d.question,
      essayText: d.essayText,
      band: d.band,
      topic: d.topic,
      subtopic: d.subtopic || null,
      tags: d.tags,
      wordCount: countWords(d.essayText),
      ...(stale
        ? { status: "NEEDS_REVIEW" as const, publishedAt: null, analyzedTextHash: null }
        : {}),
    },
  });

  revalidateAll(essayId);
  return {
    ok: true,
    essayId,
    warnings: stale
      ? ["The essay text changed, so the existing highlights no longer line up. Re-analyse before publishing."]
      : undefined,
  };
}

export async function deleteEssay(essayId: string): Promise<ActionResult> {
  await requireAdmin();
  // Annotations and ideas cascade — they are meaningless without their essay,
  // unlike a student's answer history, which is why a hard delete is right here
  // and wrong for Question.
  await prisma.ieltsEssay.delete({ where: { id: essayId } });
  revalidateAll();
  return { ok: true };
}

export async function duplicateEssay(essayId: string): Promise<ActionResult> {
  const admin = await requireAdmin();
  const source = await prisma.ieltsEssay.findUnique({
    where: { id: essayId },
    include: { annotations: true, ideas: true },
  });
  if (!source) return { error: "That essay no longer exists." };

  // The copy keeps the annotations, because the text is identical and the
  // offsets therefore still hold — but it starts unpublished and unreviewed, so
  // a duplicate can never reach students without its own approval.
  const copy = await prisma.ieltsEssay.create({
    data: {
      title: `${source.title} (copy)`,
      question: source.question,
      essayText: source.essayText,
      band: source.band,
      topic: source.topic,
      subtopic: source.subtopic,
      tags: source.tags,
      wordCount: source.wordCount,
      analyzedTextHash: source.analyzedTextHash,
      status: source.annotations.length ? "NEEDS_REVIEW" : "DRAFT",
      createdById: admin.id,
      annotations: {
        create: source.annotations.map((a) => ({
          category: a.category, subtype: a.subtype, quote: a.quote,
          startOffset: a.startOffset, endOffset: a.endOffset,
          explanation: a.explanation, ieltsValue: a.ieltsValue, pattern: a.pattern,
          confidence: a.confidence, source: a.source, reviewed: false,
        })),
      },
      ideas: {
        create: source.ideas.map((i) => ({
          claim: i.claim, explanation: i.explanation, consequence: i.consequence,
          example: i.example, startOffset: i.startOffset, endOffset: i.endOffset,
          order: i.order, source: i.source, reviewed: false,
        })),
      },
    },
    select: { id: true },
  });

  revalidateAll();
  return { ok: true, essayId: copy.id };
}

/**
 * Run the model over the essay and replace the previous analysis.
 *
 * Replacing rather than merging is deliberate: a re-analysis exists because the
 * previous one was wrong or the text moved, so keeping the old rows would
 * reintroduce exactly what the admin asked to be rid of. Hand-written
 * annotations are the exception — an admin's own work is not the model's to
 * discard.
 */
export async function analyzeEssayAction(essayId: string): Promise<ActionResult> {
  await requireAdmin();

  const essay = await prisma.ieltsEssay.findUnique({
    where: { id: essayId },
    select: { id: true, question: true, essayText: true, topic: true, band: true },
  });
  if (!essay) return { error: "That essay no longer exists." };

  await prisma.ieltsEssay.update({
    where: { id: essayId },
    data: { status: "ANALYZING", analysisError: null },
  });
  revalidateAll(essayId);

  let analysis;
  try {
    analysis = await analyzeEssay({
      question: essay.question,
      essayText: essay.essayText,
      topic: essay.topic,
      band: essay.band,
    });
  } catch (err) {
    const message =
      err instanceof EssayAnalysisError
        ? err.message
        : "The analysis failed unexpectedly. Try again.";
    // Back to DRAFT, not stuck in ANALYZING — an essay that can never leave a
    // transient state is a support ticket.
    await prisma.ieltsEssay.update({
      where: { id: essayId },
      data: { status: "DRAFT", analysisError: message },
    });
    revalidateAll(essayId);
    return { error: message };
  }

  await prisma.$transaction([
    prisma.ieltsEssayAnnotation.deleteMany({ where: { essayId, source: "AI" } }),
    prisma.ieltsEssayIdea.deleteMany({ where: { essayId, source: "AI" } }),
    prisma.ieltsEssayAnnotation.createMany({
      data: analysis.annotations.map((a) => ({
        essayId,
        category: a.category,
        subtype: a.subtype,
        quote: a.quote,
        startOffset: a.startOffset,
        endOffset: a.endOffset,
        explanation: a.explanation,
        ieltsValue: a.ieltsValue,
        pattern: a.pattern,
        confidence: a.confidence,
        source: "AI" as const,
        reviewed: false,
      })),
    }),
    prisma.ieltsEssayIdea.createMany({
      data: analysis.ideas.map((i, index) => ({
        essayId,
        claim: i.claim,
        explanation: i.explanation,
        consequence: i.consequence,
        example: i.example,
        startOffset: i.startOffset,
        endOffset: i.endOffset,
        order: index,
        source: "AI" as const,
        reviewed: false,
      })),
    }),
    prisma.ieltsEssay.update({
      where: { id: essayId },
      data: {
        status: "NEEDS_REVIEW",
        analyzedTextHash: hashEssayText(essay.essayText),
        analysisError: null,
      },
    }),
  ]);

  revalidateAll(essayId);
  return { ok: true, essayId, warnings: analysis.warnings };
}

export async function setAnnotationReviewed(
  annotationId: string,
  reviewed: boolean
): Promise<ActionResult> {
  await requireAdmin();
  const row = await prisma.ieltsEssayAnnotation.update({
    where: { id: annotationId },
    data: { reviewed },
    select: { essayId: true },
  });
  revalidateAll(row.essayId);
  return { ok: true };
}

export async function approveAllAnnotations(essayId: string): Promise<ActionResult> {
  await requireAdmin();
  await prisma.$transaction([
    prisma.ieltsEssayAnnotation.updateMany({ where: { essayId }, data: { reviewed: true } }),
    prisma.ieltsEssayIdea.updateMany({ where: { essayId }, data: { reviewed: true } }),
    prisma.ieltsEssay.update({ where: { id: essayId }, data: { status: "READY" } }),
  ]);
  revalidateAll(essayId);
  return { ok: true };
}

export async function deleteAnnotation(annotationId: string): Promise<ActionResult> {
  await requireAdmin();
  const row = await prisma.ieltsEssayAnnotation.delete({
    where: { id: annotationId },
    select: { essayId: true },
  });
  revalidateAll(row.essayId);
  return { ok: true };
}

export async function updateAnnotation(
  annotationId: string,
  form: FormData
): Promise<ActionResult> {
  await requireAdmin();
  const existing = await prisma.ieltsEssayAnnotation.findUnique({
    where: { id: annotationId },
    select: { essayId: true, startOffset: true, endOffset: true, quote: true },
  });
  if (!existing) return { error: "That annotation no longer exists." };

  const parsed = annotationInputSchema.safeParse({
    category: String(form.get("category") ?? ""),
    subtype: String(form.get("subtype") ?? ""),
    quote: existing.quote,
    startOffset: existing.startOffset,
    endOffset: existing.endOffset,
    explanation: String(form.get("explanation") ?? ""),
    ieltsValue: String(form.get("ieltsValue") ?? ""),
    pattern: String(form.get("pattern") ?? ""),
  });
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Check the annotation." };
  }
  const d = parsed.data;

  await prisma.ieltsEssayAnnotation.update({
    where: { id: annotationId },
    data: {
      category: d.category,
      subtype: d.subtype,
      explanation: d.explanation,
      ieltsValue: d.ieltsValue || null,
      pattern: d.pattern || null,
      // An admin edit is an admin's annotation from then on, and is reviewed by
      // definition — they just looked at it.
      source: "ADMIN",
      reviewed: true,
    },
  });
  revalidateAll(existing.essayId);
  return { ok: true };
}

/**
 * Add an annotation by hand over a span the admin selected in the essay.
 *
 * The offsets come from the browser, so they are re-verified against the stored
 * essay here — a client that sends a span past the end of the text, or one
 * whose quote does not match, would otherwise write an annotation that can
 * never render.
 */
export async function addAnnotation(essayId: string, form: FormData): Promise<ActionResult> {
  await requireAdmin();
  const essay = await prisma.ieltsEssay.findUnique({
    where: { id: essayId },
    select: { essayText: true },
  });
  if (!essay) return { error: "That essay no longer exists." };

  const startOffset = Number(form.get("startOffset"));
  const endOffset = Number(form.get("endOffset"));
  if (
    !Number.isInteger(startOffset) ||
    !Number.isInteger(endOffset) ||
    startOffset < 0 ||
    endOffset <= startOffset ||
    endOffset > essay.essayText.length
  ) {
    return { error: "Select some text in the essay first." };
  }
  const quote = essay.essayText.slice(startOffset, endOffset);

  const parsed = annotationInputSchema.safeParse({
    category: String(form.get("category") ?? ""),
    subtype: String(form.get("subtype") ?? "manual"),
    quote,
    startOffset,
    endOffset,
    explanation: String(form.get("explanation") ?? ""),
    ieltsValue: String(form.get("ieltsValue") ?? ""),
    pattern: String(form.get("pattern") ?? ""),
  });
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Check the annotation." };
  }
  const d = parsed.data;

  await prisma.ieltsEssayAnnotation.create({
    data: {
      essayId,
      category: d.category,
      subtype: d.subtype,
      quote,
      startOffset,
      endOffset,
      explanation: d.explanation,
      ieltsValue: d.ieltsValue || null,
      pattern: d.pattern || null,
      source: "ADMIN",
      reviewed: true,
    },
  });
  revalidateAll(essayId);
  return { ok: true };
}

export async function deleteIdea(ideaId: string): Promise<ActionResult> {
  await requireAdmin();
  const row = await prisma.ieltsEssayIdea.delete({
    where: { id: ideaId },
    select: { essayId: true },
  });
  revalidateAll(row.essayId);
  return { ok: true };
}

export async function updateIdea(ideaId: string, form: FormData): Promise<ActionResult> {
  await requireAdmin();
  const parsed = ideaInputSchema.safeParse({
    claim: String(form.get("claim") ?? ""),
    explanation: String(form.get("explanation") ?? ""),
    consequence: String(form.get("consequence") ?? ""),
    example: String(form.get("example") ?? ""),
  });
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Check the idea." };
  }
  const d = parsed.data;
  const row = await prisma.ieltsEssayIdea.update({
    where: { id: ideaId },
    data: {
      claim: d.claim,
      explanation: d.explanation,
      consequence: d.consequence || null,
      example: d.example || null,
      source: "ADMIN",
      reviewed: true,
    },
    select: { essayId: true },
  });
  revalidateAll(row.essayId);
  return { ok: true };
}

/**
 * Publish, with the gate the spec asks for.
 *
 * Every condition is re-checked here against the database rather than trusted
 * from the page that offered the button, and the failure message says which one
 * is missing so the admin can act on it.
 */
export async function publishEssay(essayId: string): Promise<ActionResult> {
  await requireAdmin();
  const essay = await prisma.ieltsEssay.findUnique({
    where: { id: essayId },
    include: {
      annotations: { select: { id: true, reviewed: true, quote: true, startOffset: true, endOffset: true } },
      ideas: { select: { id: true } },
    },
  });
  if (!essay) return { error: "That essay no longer exists." };

  if (essay.taskType !== "TASK_2") return { error: "Only Task 2 essays belong in this library." };
  if (![8, 8.5, 9].includes(essay.band)) {
    return { error: "Only Band 8.0, 8.5 and 9.0 essays can be published." };
  }
  if (!essay.question.trim()) return { error: "Add the Task 2 question before publishing." };
  if (!essay.essayText.trim()) return { error: "The essay is empty." };
  if (!essay.topic.trim()) return { error: "Give the essay a topic before publishing." };
  if (essay.annotations.length === 0) {
    return { error: "Analyse the essay before publishing — students need the highlights." };
  }
  if (essay.analyzedTextHash !== hashEssayText(essay.essayText)) {
    return {
      error:
        "The essay text has changed since it was analysed, so the highlights would land on the wrong words. Re-analyse first.",
    };
  }
  const unreviewed = essay.annotations.filter((a) => !a.reviewed).length;
  if (unreviewed > 0) {
    return { error: `${unreviewed} annotation${unreviewed === 1 ? "" : "s"} still need review.` };
  }
  // Last line of defence against drift: the stored quote must still be exactly
  // the text at its own offsets.
  const drifted = essay.annotations.find(
    (a) => essay.essayText.slice(a.startOffset, a.endOffset) !== a.quote
  );
  if (drifted) {
    return { error: "Some highlights no longer match the essay text. Re-analyse before publishing." };
  }

  await prisma.ieltsEssay.update({
    where: { id: essayId },
    data: { status: "PUBLISHED", publishedAt: new Date() },
  });
  revalidateAll(essayId);
  return { ok: true };
}

export async function unpublishEssay(essayId: string): Promise<ActionResult> {
  await requireAdmin();
  await prisma.ieltsEssay.update({
    where: { id: essayId },
    data: { status: "READY", publishedAt: null },
  });
  revalidateAll(essayId);
  return { ok: true };
}
