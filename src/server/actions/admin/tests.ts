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
