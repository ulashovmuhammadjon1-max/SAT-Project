"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import type { Subject, UploadCategory } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import { saveUploadedFile, readUploadedFile, deleteUploadedFile } from "@/lib/storage";
import { extractPdfText } from "@/lib/pdf/text-extract";
import { getExtractionProvider } from "@/lib/ai/extraction-service";
import type { TestExtractionResult, VocabExtractionResult } from "@/lib/ai/types";

export interface UploadFormState {
  error?: string;
  uploadId?: string;
}

export async function createUpload(_prev: UploadFormState, formData: FormData): Promise<UploadFormState> {
  const admin = await requireAdmin();

  const file = formData.get("file") as File | null;
  const category = formData.get("category") as UploadCategory | null;

  if (!file || file.size === 0) return { error: "Choose a PDF file to upload." };
  if (file.type !== "application/pdf") return { error: "Only PDF files are supported." };
  if (!category) return { error: "Choose an upload category." };

  try {
    const { storedPath, fileName, fileSize } = await saveUploadedFile(file);
    return await finishUpload(admin.id, { fileName, fileUrl: storedPath, fileSize, category });
  } catch (error) {
    return { error: error instanceof Error ? error.message : "Upload failed." };
  }
}

// Used for large files: the browser uploads the PDF directly to Vercel Blob
// (see /api/blob-upload), so only this small JSON payload — no file bytes —
// passes through the Server Action body limit.
export async function createUploadFromBlob(input: {
  pathname: string;
  fileName: string;
  fileSize: number;
  category: UploadCategory;
}): Promise<UploadFormState> {
  const admin = await requireAdmin();
  if (!input.category) return { error: "Choose an upload category." };

  try {
    return await finishUpload(admin.id, {
      fileName: input.fileName,
      fileUrl: input.pathname,
      fileSize: input.fileSize,
      category: input.category,
    });
  } catch (error) {
    return { error: error instanceof Error ? error.message : "Upload failed." };
  }
}

async function finishUpload(
  adminId: string,
  data: { fileName: string; fileUrl: string; fileSize: number; category: UploadCategory }
): Promise<UploadFormState> {
  const upload = await prisma.pDFUpload.create({
    data: { ...data, status: "PENDING", uploadedById: adminId },
  });

  await prisma.auditLog.create({
    data: { userId: adminId, action: "UPLOAD_CREATED", targetType: "PDFUpload", targetId: upload.id },
  });

  await runExtractionJob(upload.id);

  revalidatePath("/admin/uploads");
  return { uploadId: upload.id };
}

export async function runExtractionJob(uploadId: string): Promise<void> {
  const upload = await prisma.pDFUpload.findUniqueOrThrow({ where: { id: uploadId } });

  const job = await prisma.aIProcessingJob.create({
    data: { uploadId, status: "RUNNING", startedAt: new Date() },
  });
  await prisma.pDFUpload.update({ where: { id: uploadId }, data: { status: "PROCESSING" } });

  try {
    const buffer = await readUploadedFile(upload.fileUrl);
    const { text } = await extractPdfText(buffer);
    const provider = getExtractionProvider();

    const result =
      upload.category === "VOCABULARY" ? await provider.extractVocabulary(text) : await provider.extractTest(text);

    await prisma.aIProcessingJob.update({
      where: { id: job.id },
      data: {
        status: "SUCCEEDED",
        completedAt: new Date(),
        confidenceScore: result.overallConfidence,
        extractedData: result as unknown as object,
        logs: [{ step: "extract_text", provider: "unpdf" }, { step: "structure", provider: provider.name }],
      },
    });

    // Extraction success never auto-publishes — COMPLETED is reserved for
    // "an admin reviewed and published this," set by publishTestUpload /
    // publishVocabUpload. Every successful extraction lands in NEEDS_REVIEW
    // so the confidence score is a hint for the reviewer, not a bypass.
    await prisma.pDFUpload.update({
      where: { id: uploadId },
      data: { status: "NEEDS_REVIEW" },
    });
  } catch (error) {
    await prisma.aIProcessingJob.update({
      where: { id: job.id },
      data: {
        status: "FAILED",
        completedAt: new Date(),
        errorMessage: error instanceof Error ? error.message : "Unknown extraction error",
      },
    });
    await prisma.pDFUpload.update({ where: { id: uploadId }, data: { status: "FAILED" } });
  }

  revalidatePath("/admin/uploads");
  revalidatePath(`/admin/uploads/${uploadId}`);
}

export async function reprocessUpload(uploadId: string) {
  await requireAdmin();
  await runExtractionJob(uploadId);
}

export async function updateExtractedData(jobId: string, data: TestExtractionResult | VocabExtractionResult) {
  await requireAdmin();
  await prisma.aIProcessingJob.update({
    where: { id: jobId },
    data: { extractedData: data as unknown as object },
  });
  const job = await prisma.aIProcessingJob.findUniqueOrThrow({ where: { id: jobId } });
  revalidatePath(`/admin/uploads/${job.uploadId}`);
}

async function resolveDomainAndSkill(
  db: Pick<typeof prisma, "domain">,
  subject: Subject,
  domainGuess?: string,
  skillGuess?: string
) {
  const domains = await db.domain.findMany({ where: { subject }, include: { skills: true } });
  if (domains.length === 0) {
    throw new Error(`No ${subject} domains are seeded. Run the database seed before publishing.`);
  }
  const domain =
    domains.find((d) => domainGuess && d.name.toLowerCase().includes(domainGuess.toLowerCase())) ?? domains[0];
  const skill =
    domain.skills.find((s) => skillGuess && s.name.toLowerCase().includes(skillGuess.toLowerCase())) ??
    domain.skills[0];
  return { domainId: domain.id, skillId: skill.id };
}

export interface PublishTestOptions {
  subject: Subject;
  order: 1 | 2;
  difficulty: "STANDARD" | "EASY" | "HARD";
  /** Module 1 -> Module 2 routing threshold for this specific module, overriding the test's AdaptiveConfig. */
  thresholdPct?: number | null;
  /** Publish into an already-existing test instead of creating a new one (e.g. adding the Math module to an R&W test). */
  targetTestId?: string | null;
}

export async function publishTestUpload(uploadId: string, options: PublishTestOptions) {
  const admin = await requireAdmin();
  const { subject, order, difficulty, thresholdPct, targetTestId } = options;
  const upload = await prisma.pDFUpload.findUniqueOrThrow({
    where: { id: uploadId },
    include: { jobs: { orderBy: { createdAt: "desc" }, take: 1 } },
  });
  const job = upload.jobs[0];
  if (!job?.extractedData) throw new Error("No extracted data to publish.");

  const data = job.extractedData as unknown as TestExtractionResult;

  const testId = await prisma.$transaction(async (tx) => {
    let test;
    if (targetTestId) {
      test = await tx.test.findUniqueOrThrow({ where: { id: targetTestId } });
      const clash = await tx.module.findUnique({
        where: { testId_subject_order_difficulty: { testId: test.id, subject, order, difficulty } },
      });
      if (clash) {
        throw new Error("That test already has a module in this subject/module slot. Pick a different slot or test.");
      }
    } else {
      test = await tx.test.create({
        data: {
          title: upload.fileName.replace(/\.pdf$/i, ""),
          type: upload.category === "FULL_TEST" ? "FULL_LENGTH" : "PRACTICE_SET",
          status: "DRAFT",
          isAdaptive: upload.category === "FULL_TEST",
          createdById: admin.id,
        },
      });
    }

    const mod = await tx.module.create({
      data: {
        testId: test.id,
        subject,
        order,
        difficulty,
        title: order === 1 ? "Module 1" : `Module 2 (${difficulty === "HARD" ? "Hard" : "Easy"})`,
        adaptiveThresholdPct: order === 1 ? thresholdPct ?? null : null,
      },
    });

    const passageIds: string[] = [];
    for (const passage of data.passages) {
      const created = await tx.passage.create({
        data: { moduleId: mod.id, title: passage.title, content: passage.content },
      });
      passageIds.push(created.id);
    }

    for (const q of data.questions) {
      const { domainId, skillId } =
        q.domainId && q.skillId
          ? { domainId: q.domainId, skillId: q.skillId }
          : await resolveDomainAndSkill(tx, subject, q.domainGuess, q.skillGuess);
      const question = await tx.question.create({
        data: {
          moduleId: mod.id,
          passageId: q.passageIndex !== undefined && q.passageIndex !== null ? passageIds[q.passageIndex] : null,
          domainId,
          skillId,
          type: q.type,
          difficulty: q.difficultyGuess,
          stem: q.stem,
          imageUrl: q.imageUrl ?? null,
          order: q.number,
          source: "AI_EXTRACTED",
          sourceUploadId: uploadId,
          // Publishing the test IS the admin's approval gate -- if questions
          // defaulted to unpublished here, every one of them would need a
          // second, separate manual toggle in the per-question editor before
          // students could practice it standalone (they'd still be playable
          // in the timed test either way, since exam-taking doesn't filter
          // on isPublished). Admins can still unpublish an individual
          // question afterward if they want to pull just that one.
          isPublished: true,
          correctAnswerFR: q.correctAnswerFreeResponse ?? null,
        },
      });

      for (const [i, choice] of q.choices.entries()) {
        await tx.answerChoice.create({
          data: {
            questionId: question.id,
            label: choice.label,
            content: choice.content,
            isCorrect: choice.isCorrect,
            order: i,
          },
        });
      }

      if (q.explanation) {
        await tx.explanation.create({
          data: { questionId: question.id, content: q.explanation, source: "AI_GENERATED" },
        });
      }
    }

    await tx.pDFUpload.update({ where: { id: uploadId }, data: { status: "COMPLETED" } });
    await tx.aIProcessingJob.update({
      where: { id: job.id },
      data: { reviewedById: admin.id, reviewedAt: new Date(), publishedAt: new Date() },
    });
    await tx.auditLog.create({
      data: { userId: admin.id, action: "UPLOAD_PUBLISHED", targetType: "Test", targetId: test.id },
    });

    return test.id;
  });

  // redirect() throws internally — it must run after the transaction has
  // committed, never inside the $transaction callback (which would roll back).
  revalidatePath("/admin/tests");
  redirect(`/admin/tests/${testId}`);
}

export async function publishVocabUpload(uploadId: string) {
  const admin = await requireAdmin();
  const upload = await prisma.pDFUpload.findUniqueOrThrow({
    where: { id: uploadId },
    include: { jobs: { orderBy: { createdAt: "desc" }, take: 1 } },
  });
  const job = upload.jobs[0];
  if (!job?.extractedData) throw new Error("No extracted data to publish.");

  const data = job.extractedData as unknown as VocabExtractionResult;

  await prisma.$transaction(async (tx) => {
    const deck = await tx.vocabDeck.create({
      data: { name: upload.fileName.replace(/\.pdf$/i, "") },
    });

    for (const [i, word] of data.words.entries()) {
      const created = await tx.vocabWord.create({
        data: {
          term: word.term,
          partOfSpeech: word.partOfSpeech,
          definition: word.definition,
          exampleSentence: word.exampleSentence,
          synonyms: word.synonyms,
          antonyms: word.antonyms,
          difficulty: word.difficultyGuess,
          createdById: admin.id,
          sourceUploadId: uploadId,
        },
      });
      await tx.vocabDeckWord.create({ data: { deckId: deck.id, wordId: created.id, order: i } });
    }

    await tx.pDFUpload.update({ where: { id: uploadId }, data: { status: "COMPLETED" } });
    await tx.aIProcessingJob.update({
      where: { id: job.id },
      data: { reviewedById: admin.id, reviewedAt: new Date(), publishedAt: new Date() },
    });
    await tx.auditLog.create({
      data: { userId: admin.id, action: "UPLOAD_PUBLISHED", targetType: "VocabDeck", targetId: deck.id },
    });
  });

  revalidatePath("/admin/vocabulary");
  redirect("/admin/vocabulary");
}

export async function deleteUpload(uploadId: string) {
  await requireAdmin();
  const upload = await prisma.pDFUpload.delete({ where: { id: uploadId } });
  await deleteUploadedFile(upload.fileUrl);
  revalidatePath("/admin/uploads");
}
