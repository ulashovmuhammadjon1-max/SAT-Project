"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { AP_CATALOG, isLiveSubject, subjectByCode } from "@/lib/ap/catalog";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

/**
 * A student's personal AP subject list.
 *
 * Enrollment is deliberately separate from progress. Question attempts and
 * test attempts key on (userId, subject string), never on an enrollment row,
 * so removing a subject takes it out of the sidebar and nothing else — add it
 * back and every answer, score and attempt is still there.
 */

const subjectSchema = z.object({ subject: z.string().min(1).max(64) });

export interface MySubject {
  code: string;
  slug: string;
  name: string;
  short: string;
  gradient: string;
  addedAt: Date;
}

/** The subjects this student has added, in the order they added them. */
export async function getMySubjects(): Promise<MySubject[]> {
  const user = await requireUser();
  const rows = await prisma.apSubjectEnrollment.findMany({
    where: { userId: user.id },
    orderBy: { addedAt: "asc" },
    select: { subject: true, addedAt: true },
  });

  // A subject removed from the catalog should disappear from the sidebar
  // rather than render as a broken link; the enrollment row is left alone so
  // nothing is destroyed by a catalog edit.
  return rows.flatMap((row) => {
    const entry = subjectByCode(row.subject);
    if (!entry) return [];
    return [
      {
        code: entry.code,
        slug: entry.slug,
        name: entry.name,
        short: entry.short,
        gradient: entry.gradient,
        addedAt: row.addedAt,
      },
    ];
  });
}

/** Just the codes — cheaper for the catalog page, which only needs membership. */
export async function getMySubjectCodes(): Promise<string[]> {
  const user = await requireUser();
  const rows = await prisma.apSubjectEnrollment.findMany({
    where: { userId: user.id },
    select: { subject: true },
  });
  return rows.map((r) => r.subject);
}

export interface SubjectActionResult {
  ok?: boolean;
  error?: string;
}

export async function addSubject(input: { subject: string }): Promise<SubjectActionResult> {
  const user = await requireUser();
  const parsed = subjectSchema.safeParse(input);
  if (!parsed.success) return { error: "That subject does not exist." };

  const entry = subjectByCode(parsed.data.subject);
  if (!entry) return { error: "That subject does not exist." };
  // A student must never land inside a course with no questions.
  if (!isLiveSubject(entry.code)) {
    return { error: `${entry.name} isn't ready yet — we'll add it soon.` };
  }

  // Upsert rather than create: adding twice (a double click, two tabs) is a
  // no-op instead of a unique-constraint error surfacing as "went wrong".
  await prisma.apSubjectEnrollment.upsert({
    where: { userId_subject: { userId: user.id, subject: entry.code } },
    create: { userId: user.id, subject: entry.code },
    update: {},
  });

  revalidatePath("/ap");
  revalidatePath("/ap/tests");
  revalidatePath(`/ap/${entry.slug}`);
  return { ok: true };
}

export async function removeSubject(input: { subject: string }): Promise<SubjectActionResult> {
  const user = await requireUser();
  const parsed = subjectSchema.safeParse(input);
  if (!parsed.success) return { error: "That subject does not exist." };

  const entry = subjectByCode(parsed.data.subject);
  if (!entry) return { error: "That subject does not exist." };

  // deleteMany, not delete: removing a subject that is already gone should
  // succeed quietly rather than throw on a missing row.
  await prisma.apSubjectEnrollment.deleteMany({
    where: { userId: user.id, subject: entry.code },
  });

  revalidatePath("/ap");
  revalidatePath("/ap/tests");
  revalidatePath(`/ap/${entry.slug}`);
  return { ok: true };
}

export interface CatalogSubject {
  code: string;
  slug: string;
  name: string;
  short: string;
  blurb: string;
  category: string;
  status: "LIVE" | "COMING_SOON";
  gradient: string;
  added: boolean;
  /** Live question count, so a card can say what it actually holds. */
  questionCount: number;
}

/**
 * The whole catalog, annotated with whether this student has added each
 * subject and how many questions it holds.
 *
 * One groupBy for every subject rather than a count per card — the catalog is
 * ~26 entries today and will be larger, so a query per card would be a real
 * N+1 on the page a student sees first.
 */
export async function getCatalog(): Promise<CatalogSubject[]> {
  const [mine, counts] = await Promise.all([
    getMySubjectCodes(),
    prisma.apQuestion.groupBy({ by: ["subject"], _count: { id: true } }),
  ]);
  const added = new Set(mine);
  const countBy = new Map(counts.map((c) => [c.subject, c._count.id]));

  return AP_CATALOG.map((s) => ({
    code: s.code,
    slug: s.slug,
    name: s.name,
    short: s.short,
    blurb: s.blurb,
    category: s.category,
    status: s.status,
    gradient: s.gradient,
    added: added.has(s.code),
    questionCount: countBy.get(s.code) ?? 0,
  }));
}
