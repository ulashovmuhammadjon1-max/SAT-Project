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

  // Deactivating every other config and then writing this one used to be two
  // separate statements — if the second one failed for any reason, every
  // config would already be inactive with no way back short of a manual fix.
  // A transaction makes the whole "make this the one active config" swap
  // atomic: either both happen or neither does.
  await prisma.$transaction(async (tx) => {
    if (input.isActive) {
      await tx.adaptiveConfig.updateMany({ data: { isActive: false } });
    }

    if (input.id) {
      await tx.adaptiveConfig.update({
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
      await tx.adaptiveConfig.create({
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
  });

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
