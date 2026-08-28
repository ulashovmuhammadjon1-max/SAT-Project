"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

/**
 * Team-page management. Photos arrive as data URIs (the certificate pattern):
 * no Blob token dependency, and the public page renders them directly.
 */

const memberSchema = z.object({
  name: z.string().trim().min(2).max(120),
  title: z.string().trim().min(2).max(120),
  email: z.string().trim().email().optional().or(z.literal("")),
  bio: z.string().trim().max(600).optional().or(z.literal("")),
  photo: z
    .string()
    .regex(/^data:image\/(png|jpe?g|webp);base64,[A-Za-z0-9+/=]+$/, "Photo must be a PNG, JPG or WEBP image.")
    .max(2_800_000, "Keep the photo under 2MB.")
    .optional()
    .or(z.literal("")),
  order: z.coerce.number().int().min(0).max(999).default(0),
});

export async function saveTeamMember(input: {
  id?: string;
  name: unknown;
  title: unknown;
  email?: unknown;
  bio?: unknown;
  photo?: unknown;
  order?: unknown;
}): Promise<{ ok?: boolean; error?: string }> {
  await requireAdmin();

  const parsed = memberSchema.safeParse({
    name: input.name,
    title: input.title,
    email: input.email ?? "",
    bio: input.bio ?? "",
    photo: input.photo ?? "",
    order: input.order ?? 0,
  });
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Check the member details." };
  }
  const d = parsed.data;
  const data = {
    name: d.name,
    title: d.title,
    email: d.email || null,
    bio: d.bio || null,
    order: d.order,
    // An empty photo on edit means "keep the existing one" — handled below.
    ...(d.photo ? { photo: d.photo } : {}),
  };

  if (input.id && typeof input.id === "string") {
    await prisma.teamMember.update({ where: { id: input.id }, data });
  } else {
    await prisma.teamMember.create({ data });
  }

  revalidatePath("/admin/team");
  revalidatePath("/team");
  return { ok: true };
}

export async function deleteTeamMember(id: string): Promise<{ ok?: boolean; error?: string }> {
  await requireAdmin();
  await prisma.teamMember.delete({ where: { id } });
  revalidatePath("/admin/team");
  revalidatePath("/team");
  return { ok: true };
}

export async function setTeamMemberActive(id: string, isActive: boolean): Promise<{ ok?: boolean; error?: string }> {
  await requireAdmin();
  await prisma.teamMember.update({ where: { id }, data: { isActive } });
  revalidatePath("/admin/team");
  revalidatePath("/team");
  return { ok: true };
}
