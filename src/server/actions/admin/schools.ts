"use server";

import { randomInt } from "crypto";
import { revalidatePath } from "next/cache";
import { z } from "zod";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

/**
 * Admin side of the schools programme. Classes are created here during the
 * pilot phase — a teacher asks for a class, an admin makes it and hands the
 * code over. No teacher self-serve yet, on purpose: each pilot class is a
 * relationship, not a signup.
 */

const createSchema = z.object({
  name: z.string().trim().min(2).max(120),
  school: z.string().trim().min(2).max(160),
  teacherName: z.string().trim().min(2).max(120),
  teacherEmail: z.string().trim().email().optional().or(z.literal("")),
});

/** No 0/O/1/I — the code gets read off a whiteboard. */
const CODE_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";

function makeCode(): string {
  let out = "";
  for (let i = 0; i < 6; i++) out += CODE_ALPHABET[randomInt(CODE_ALPHABET.length)];
  return out;
}

export async function createClass(formData: FormData): Promise<{ ok?: boolean; error?: string; code?: string }> {
  await requireAdmin();

  const parsed = createSchema.safeParse({
    name: formData.get("name"),
    school: formData.get("school"),
    teacherName: formData.get("teacherName"),
    teacherEmail: formData.get("teacherEmail"),
  });
  if (!parsed.success) return { error: "Fill in the class name, school and teacher name." };

  // If the teacher already has an account, link it now — their Teacher Panel
  // lights up immediately. Otherwise the class is claimed by email the first
  // time that address registers and opens /teach.
  const teacherEmail = parsed.data.teacherEmail ? parsed.data.teacherEmail.toLowerCase() : null;
  const teacherUser = teacherEmail
    ? await prisma.user.findUnique({ where: { email: teacherEmail }, select: { id: true } })
    : null;

  // Collisions over a 32^6 space are vanishingly rare; retry a few times
  // rather than pretend they are impossible.
  for (let attempt = 0; attempt < 5; attempt++) {
    const code = makeCode();
    try {
      await prisma.schoolClass.create({
        data: {
          code,
          name: parsed.data.name,
          school: parsed.data.school,
          teacherName: parsed.data.teacherName,
          teacherEmail,
          teacherUserId: teacherUser?.id ?? null,
        },
      });
      revalidatePath("/admin/schools");
      return { ok: true, code };
    } catch (error) {
      if (attempt === 4) throw error;
    }
  }
  return { error: "Could not generate a class code — try again." };
}

export async function setClassArchived(classId: string, archived: boolean): Promise<{ ok?: boolean; error?: string }> {
  await requireAdmin();
  await prisma.schoolClass.update({ where: { id: classId }, data: { isArchived: archived } });
  revalidatePath("/admin/schools");
  return { ok: true };
}
