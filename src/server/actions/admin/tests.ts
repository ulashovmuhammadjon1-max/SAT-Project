"use server";

import { revalidatePath } from "next/cache";
import type { TestStatus } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export async function setTestStatus(testId: string, status: TestStatus) {
  const admin = await requireAdmin();
  await prisma.test.update({ where: { id: testId }, data: { status } });
  await prisma.auditLog.create({
    data: { userId: admin.id, action: `TEST_${status}`, targetType: "Test", targetId: testId },
  });
  revalidatePath("/admin/tests");
  revalidatePath(`/admin/tests/${testId}`);
}

export async function publishAllQuestionsInTest(testId: string): Promise<{ count: number }> {
  const admin = await requireAdmin();
  const { count } = await prisma.question.updateMany({
    where: { module: { testId }, isPublished: false },
    data: { isPublished: true },
  });
  await prisma.auditLog.create({
    data: { userId: admin.id, action: "TEST_QUESTIONS_PUBLISHED", targetType: "Test", targetId: testId },
  });
  revalidatePath("/admin/questions");
  revalidatePath(`/admin/tests/${testId}`);
  return { count };
}

export interface DeleteTestResult {
  error?: string;
  success?: boolean;
}

export async function deleteTest(testId: string): Promise<DeleteTestResult> {
  const admin = await requireAdmin();

  try {
    await prisma.$transaction(async (tx) => {
      const moduleIds = (await tx.module.findMany({ where: { testId }, select: { id: true } })).map((m) => m.id);

      // Every FK below this test is either SET NULL (Question->Module) or has
      // no onDelete override, which Postgres/Prisma defaults to RESTRICT
      // (Attempt->Test, ModuleAttempt->Module). Deleting the test row — or
      // letting the Test->Module cascade fire — would fail outright the
      // moment any student had ever started this test. Since "delete this
      // test" is an explicit, confirmed, whole-object destroy (not a partial
      // edit), it takes its attempt history down with it: responses, then
      // module attempts, then attempts, then questions, then the test.
      const attemptIds = (
        await tx.attempt.findMany({ where: { testId }, select: { id: true } })
      ).map((a) => a.id);
      if (attemptIds.length > 0) {
        await tx.response.deleteMany({ where: { attemptId: { in: attemptIds } } });
        await tx.moduleAttempt.deleteMany({ where: { attemptId: { in: attemptIds } } });
        await tx.attempt.deleteMany({ where: { id: { in: attemptIds } } });
      }

      // Question->Module is SET NULL on delete, not cascade, so deleting a
      // test's modules directly would silently orphan every question in them
      // (they'd stop appearing anywhere, but the rows — and their answer
      // choices, explanations, passages — would linger in the DB forever).
      // Delete questions explicitly first so a deleted test actually goes away.
      await tx.question.deleteMany({ where: { moduleId: { in: moduleIds } } });
      await tx.test.delete({ where: { id: testId } });
    });
  } catch (error) {
    console.error("[admin] Failed to delete test", testId, error);
    return { error: "Couldn't delete this test. Please try again, or check the server logs for details." };
  }

  await prisma.auditLog.create({
    data: { userId: admin.id, action: "TEST_DELETED", targetType: "Test", targetId: testId },
  });
  revalidatePath("/admin/tests");
  return { success: true };
}

export async function updateModuleTimeLimit(moduleId: string, minutes: number) {
  await requireAdmin();
  await prisma.module.update({ where: { id: moduleId }, data: { timeLimitMinutes: minutes } });
  revalidatePath("/admin/tests");
}

export async function updateTestDetails(
  testId: string,
  data: { title: string; description?: string | null; adaptiveConfigId?: string | null }
) {
  await requireAdmin();
  if (!data.title.trim()) throw new Error("Title cannot be empty.");
  await prisma.test.update({
    where: { id: testId },
    data: { title: data.title.trim(), description: data.description, adaptiveConfigId: data.adaptiveConfigId },
  });
  revalidatePath("/admin/tests");
  revalidatePath(`/admin/tests/${testId}`);
}

// Removes a single module so an admin can redo a badly-extracted module
// without deleting the whole test. Questions are deleted explicitly first
// (rather than relying on the module->question relation, which is SET NULL
// on delete) so a redo doesn't leave orphaned draft questions behind. Fails
// with a foreign-key error if any student has already answered a question
// in this module — that data is never silently destroyed.
export interface DeleteModuleResult {
  error?: string;
  success?: boolean;
}

export async function deleteModule(moduleId: string): Promise<DeleteModuleResult> {
  const admin = await requireAdmin();

  let testId: string;
  try {
    testId = await prisma.$transaction(async (tx) => {
      const mod = await tx.module.findUniqueOrThrow({ where: { id: moduleId } });
      await tx.question.deleteMany({ where: { moduleId } });
      await tx.module.delete({ where: { id: moduleId } });
      return mod.testId;
    });
  } catch (error) {
    console.error("[admin] Failed to delete module", moduleId, error);
    // The FK from ModuleAttempt->Module has no cascade, by design: deleting
    // one module for a redo should never silently wipe attempt history that
    // also belongs to sibling modules in the same test.
    return {
      error: "Couldn't delete this module — students have already attempted it, so its history is preserved.",
    };
  }

  await prisma.auditLog.create({
    data: { userId: admin.id, action: "MODULE_DELETED", targetType: "Module", targetId: moduleId },
  });
  revalidatePath(`/admin/tests/${testId}`);
  return { success: true };
}
