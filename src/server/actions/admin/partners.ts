"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export type PartnerResult = { ok: boolean; error?: string; id?: string };

/**
 * Only http(s) links are allowed.
 *
 * This value goes straight into an `href` on a public page. A `javascript:` URL
 * there is stored XSS, and `data:` is only marginally better, so the scheme is
 * checked on write rather than trusted at render time — the render site is easy
 * to forget when a second one appears.
 */
function normalizeHref(raw: string): string | null {
  const trimmed = raw.trim();
  if (!trimmed) return null;
  // Bare "t.me/SAT_1601" is what an admin will actually paste.
  const withScheme = /^https?:\/\//i.test(trimmed) ? trimmed : `https://${trimmed}`;
  try {
    const url = new URL(withScheme);
    if (url.protocol !== "http:" && url.protocol !== "https:") return null;
    return url.toString();
  } catch {
    return null;
  }
}

/** Same rule for the logo, which lands in an `img src`. Relative /api paths are ours. */
function normalizeLogo(raw: string): string | null {
  const trimmed = raw.trim();
  if (!trimmed) return null;
  if (trimmed.startsWith("/")) return trimmed;
  return normalizeHref(trimmed);
}

export interface PartnerInput {
  id?: string;
  name: string;
  logoUrl: string;
  href: string;
  blurb?: string | null;
  order?: number;
  isPublished?: boolean;
}

export async function savePartner(input: PartnerInput): Promise<PartnerResult> {
  await requireAdmin();

  const name = input.name?.trim();
  if (!name) return { ok: false, error: "Give the partner a name." };

  const href = normalizeHref(input.href ?? "");
  if (!href) return { ok: false, error: "That link isn't a valid http or https URL." };

  const logoUrl = normalizeLogo(input.logoUrl ?? "");
  if (!logoUrl) return { ok: false, error: "Add a logo — upload one or paste an image URL." };

  const data = {
    name,
    href,
    logoUrl,
    blurb: input.blurb?.trim() || null,
    order: Number.isFinite(input.order) ? Number(input.order) : 0,
    isPublished: input.isPublished ?? false,
  };

  const row = input.id
    ? await prisma.partner.update({ where: { id: input.id }, data, select: { id: true } })
    : await prisma.partner.create({ data, select: { id: true } });

  revalidatePath("/admin/partners");
  revalidatePath("/");
  return { ok: true, id: row.id };
}

export async function setPartnerPublished(id: string, isPublished: boolean): Promise<PartnerResult> {
  await requireAdmin();
  await prisma.partner.update({ where: { id }, data: { isPublished } });
  revalidatePath("/admin/partners");
  revalidatePath("/");
  return { ok: true };
}

export async function deletePartner(id: string): Promise<PartnerResult> {
  await requireAdmin();
  await prisma.partner.delete({ where: { id } }).catch(() => null);
  revalidatePath("/admin/partners");
  revalidatePath("/");
  return { ok: true };
}

/** Move one row up or down. Swaps `order` with its neighbour rather than
 *  renumbering everything, so two admins reordering at once cannot collide. */
export async function movePartner(id: string, direction: "up" | "down"): Promise<PartnerResult> {
  await requireAdmin();
  const all = await prisma.partner.findMany({
    orderBy: [{ order: "asc" }, { createdAt: "asc" }],
    select: { id: true, order: true },
  });
  const i = all.findIndex((p) => p.id === id);
  if (i === -1) return { ok: false, error: "Partner not found." };
  const j = direction === "up" ? i - 1 : i + 1;
  if (j < 0 || j >= all.length) return { ok: true };

  await prisma.$transaction([
    prisma.partner.update({ where: { id: all[i].id }, data: { order: all[j].order } }),
    prisma.partner.update({ where: { id: all[j].id }, data: { order: all[i].order } }),
  ]);

  revalidatePath("/admin/partners");
  revalidatePath("/");
  return { ok: true };
}
