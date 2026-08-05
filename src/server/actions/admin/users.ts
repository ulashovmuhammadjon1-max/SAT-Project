"use server";

import { revalidatePath } from "next/cache";
import type { Role } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export interface UpdateUserRoleResult {
  error?: string;
  success?: boolean;
}

export async function updateUserRole(userId: string, role: Role): Promise<UpdateUserRoleResult> {
  const admin = await requireAdmin();

  const target = await prisma.user.findUnique({ where: { id: userId }, select: { role: true } });
  if (!target) return { error: "That user no longer exists." };

  // Nothing stopped this from dropping to zero admins — whether by demoting
  // yourself or the last other admin — which locks everyone out of the
  // admin panel with no way back in short of editing the database directly.
  if (target.role === "ADMIN" && role !== "ADMIN") {
    const adminCount = await prisma.user.count({ where: { role: "ADMIN" } });
    if (adminCount <= 1) {
      return {
        error: "This is the only admin account. Promote another user to admin first — changing this one would lock everyone out of the admin panel.",
      };
    }
  }

  await prisma.user.update({ where: { id: userId }, data: { role } });
  await prisma.auditLog.create({
    data: { userId: admin.id, action: `USER_ROLE_${role}`, targetType: "User", targetId: userId },
  });
  revalidatePath("/admin/users");
  return { success: true };
}
