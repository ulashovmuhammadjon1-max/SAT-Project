"use server";

import { randomInt } from "crypto";
import { headers } from "next/headers";
import { revalidatePath } from "next/cache";
import { z } from "zod";

import { sendClassTeacherInvite } from "@/lib/email/class-invite";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import { issueVerificationLink } from "@/server/actions/auth/email-verification";

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

function origin(): string {
  const h = headers();
  const host = h.get("x-forwarded-host") ?? h.get("host") ?? "scholarly.space";
  const proto = h.get("x-forwarded-proto") ?? (host.startsWith("localhost") ? "http" : "https");
  return `${proto}://${host}`;
}

/**
 * Links the address to an account if one exists, then emails the teacher.
 *
 * Called whenever a teacher email becomes attached to a class — on creation,
 * on a later edit, and on an explicit resend. Before this existed the teacher
 * was told nothing at all and had to be chased by hand, which is exactly the
 * failure that was reported.
 *
 * Delivery failure is logged, never thrown: an admin creating a class must not
 * see it fail because a mail provider was briefly unreachable. The class is
 * the durable thing; the invite can be resent.
 */
async function linkAndInvite(classId: string): Promise<{ invited: boolean; reason?: string }> {
  const cls = await prisma.schoolClass.findUnique({
    where: { id: classId },
    select: { code: true, name: true, school: true, teacherName: true, teacherEmail: true },
  });
  if (!cls?.teacherEmail) return { invited: false, reason: "no teacher email on this class" };

  const email = cls.teacherEmail.toLowerCase();
  const user = await prisma.user.findUnique({
    where: { email },
    select: { id: true, emailVerified: true },
  });

  // Link now if the account already exists; otherwise the lazy claim in
  // server/actions/teacher/classes.ts picks it up on their first visit.
  if (user) {
    await prisma.schoolClass.updateMany({
      where: { id: classId, teacherUserId: null },
      data: { teacherUserId: user.id },
    });
  }

  // An unverified account is a dead end without this: the student layout
  // requires a verified email, so they would sign in and never reach /teach.
  const verifyLink = user && !user.emailVerified ? await issueVerificationLink(email) : null;

  try {
    await sendClassTeacherInvite({
      to: email,
      teacherName: cls.teacherName,
      className: cls.name,
      school: cls.school,
      code: cls.code,
      origin: origin(),
      hasAccount: Boolean(user),
      verifyLink,
    });
    return { invited: true };
  } catch (error) {
    console.error("[schools] teacher invite failed", { classId, error });
    return { invited: false, reason: "the email could not be sent — try Resend invite" };
  }
}

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
      const created = await prisma.schoolClass.findUnique({
        where: { code },
        select: { id: true },
      });
      // Teachers are told automatically now. This is the fix for the reported
      // bug: previously nothing was sent and the teacher learned about the
      // class only if an admin happened to message them.
      if (created && teacherEmail) await linkAndInvite(created.id);
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

const teacherSchema = z.object({
  teacherName: z.string().trim().min(2).max(120),
  teacherEmail: z.string().trim().email().optional().or(z.literal("")),
});

/**
 * Sets or changes a class's teacher, and emails them.
 *
 * There was no way to do this at all before — a class created without a
 * teacher email, or with the wrong one, could not be corrected without a
 * database edit.
 */
export async function setClassTeacher(
  classId: string,
  formData: FormData,
): Promise<{ ok?: boolean; error?: string; note?: string }> {
  await requireAdmin();

  const parsed = teacherSchema.safeParse({
    teacherName: formData.get("teacherName"),
    teacherEmail: formData.get("teacherEmail"),
  });
  if (!parsed.success) return { error: "Give the teacher's name, and a valid email if you set one." };

  const teacherEmail = parsed.data.teacherEmail ? parsed.data.teacherEmail.toLowerCase() : null;
  const before = await prisma.schoolClass.findUnique({
    where: { id: classId },
    select: { teacherEmail: true },
  });
  if (!before) return { error: "That class no longer exists." };

  const changed = (before.teacherEmail ?? null) !== teacherEmail;

  await prisma.schoolClass.update({
    where: { id: classId },
    data: {
      teacherName: parsed.data.teacherName,
      teacherEmail,
      // A new address must not inherit the previous teacher's link, or the old
      // account keeps access to a class that is no longer theirs.
      ...(changed ? { teacherUserId: null } : {}),
    },
  });

  let note: string | undefined;
  if (teacherEmail && changed) {
    const res = await linkAndInvite(classId);
    note = res.invited ? `Invite emailed to ${teacherEmail}.` : res.reason;
  }

  revalidatePath("/admin/schools");
  return { ok: true, note };
}

/** Sends the invite again, for a teacher who lost it or never saw it. */
export async function resendClassInvite(
  classId: string,
): Promise<{ ok?: boolean; error?: string; note?: string }> {
  await requireAdmin();
  const res = await linkAndInvite(classId);
  if (!res.invited) return { error: res.reason ?? "Could not send the invite." };
  revalidatePath("/admin/schools");
  return { ok: true, note: "Invite sent." };
}
