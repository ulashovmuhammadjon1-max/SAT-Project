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

export async function deleteTest(testId: string) {
  const admin = await requireAdmin();
  await prisma.test.delete({ where: { id: testId } });
  await prisma.auditLog.create({
    data: { userId: admin.id, action: "TEST_DELETED", targetType: "Test", targetId: testId },
  });
  revalidatePath("/admin/tests");
}

export async function updateModuleTimeLimit(moduleId: string, minutes: number) {
  await requireAdmin();
  await prisma.module.update({ where: { id: moduleId }, data: { timeLimitMinutes: minutes } });
  revalidatePath("/admin/tests");
}

export async function updateTestDetails(testId: string, data: { title: string; description?: string | null }) {
  await requireAdmin();
  if (!data.title.trim()) throw new Error("Title cannot be empty.");
  await prisma.test.update({ where: { id: testId }, data: { title: data.title.trim(), description: data.description } });
  revalidatePath("/admin/tests");
  revalidatePath(`/admin/tests/${testId}`);
}

// Removes a single module so an admin can redo a badly-extracted module
// without deleting the whole test. Questions are deleted explicitly first
// (rather than relying on the module->question relation, which is SET NULL
// on delete) so a redo doesn't leave orphaned draft questions behind. Fails
// with a foreign-key error if any student has already answered a question
// in this module — that data is never silently destroyed.
export async function deleteModule(moduleId: string) {
  const admin = await requireAdmin();
  const testId = await prisma.$transaction(async (tx) => {
    const mod = await tx.module.findUniqueOrThrow({ where: { id: moduleId } });
    await tx.question.deleteMany({ where: { moduleId } });
    await tx.module.delete({ where: { id: moduleId } });
    return mod.testId;
  });
  await prisma.auditLog.create({
    data: { userId: admin.id, action: "MODULE_DELETED", targetType: "Module", targetId: moduleId },
  });
  revalidatePath(`/admin/tests/${testId}`);
}
