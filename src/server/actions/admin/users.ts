"use server";

import { revalidatePath } from "next/cache";
import type { Role } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export async function updateUserRole(userId: string, role: Role) {
  const admin = await requireAdmin();
  await prisma.user.update({ where: { id: userId }, data: { role } });
  await prisma.auditLog.create({
    data: { userId: admin.id, action: `USER_ROLE_${role}`, targetType: "User", targetId: userId },
  });
  revalidatePath("/admin/users");
}
