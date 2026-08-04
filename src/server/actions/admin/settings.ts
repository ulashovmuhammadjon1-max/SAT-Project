"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export async function updateAdaptiveConfig(input: {
  id?: string;
  name: string;
  description?: string;
  rwThresholdPct: number;
  mathThresholdPct: number;
  isActive: boolean;
}) {
  const admin = await requireAdmin();

  if (input.isActive) {
    await prisma.adaptiveConfig.updateMany({ data: { isActive: false } });
  }

  if (input.id) {
    await prisma.adaptiveConfig.update({
      where: { id: input.id },
      data: {
        name: input.name,
        description: input.description,
        rwThresholdPct: input.rwThresholdPct,
        mathThresholdPct: input.mathThresholdPct,
        isActive: input.isActive,
        updatedById: admin.id,
      },
    });
  } else {
    await prisma.adaptiveConfig.create({
      data: {
        name: input.name,
        description: input.description,
        rwThresholdPct: input.rwThresholdPct,
        mathThresholdPct: input.mathThresholdPct,
        isActive: input.isActive,
        updatedById: admin.id,
      },
    });
  }

  revalidatePath("/admin/settings");
}

export async function deleteAdaptiveConfig(id: string) {
  await requireAdmin();
  await prisma.adaptiveConfig.delete({ where: { id } });
  revalidatePath("/admin/settings");
}

export async function toggleFeatureFlag(key: string, isEnabled: boolean) {
  await requireAdmin();
  await prisma.featureFlag.update({ where: { key }, data: { isEnabled } });
  revalidatePath("/admin/settings");
}

export async function createAnnouncement(input: {
  title: string;
  body: string;
  audience: "ALL" | "STUDENT" | "ADMIN";
}) {
  const admin = await requireAdmin();
  await prisma.announcement.create({ data: { ...input, createdById: admin.id } });
  revalidatePath("/admin/announcements");
}

export async function toggleAnnouncement(id: string, isActive: boolean) {
  await requireAdmin();
  await prisma.announcement.update({ where: { id }, data: { isActive } });
  revalidatePath("/admin/announcements");
}

export async function deleteAnnouncement(id: string) {
  await requireAdmin();
  await prisma.announcement.delete({ where: { id } });
  revalidatePath("/admin/announcements");
}
