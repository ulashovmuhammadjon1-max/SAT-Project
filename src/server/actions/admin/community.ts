"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import { runInBackground } from "@/lib/background";
import { createNotifications } from "@/lib/community/notify";
import { displayName, excerpt } from "@/lib/community/server";
import { CHANNEL_ICON_KEYS } from "@/lib/community/icons";

/**
 * Community administration: channels, categories and moderation.
 *
 * Every function starts with requireAdmin(). The admin pages are also behind
 * the /admin middleware check, but that is navigation, not authorisation —
 * these actions are callable directly and check for themselves.
 * Every moderation action writes a row to CommunityModerationLog.
 */

type Result<T = object> = ({ ok: true } & T) | { ok: false; error: string };

/** Paths a channel slug must never take, because a page already lives there. */
const RESERVED = new Set(["search", "bookmarks", "settings", "messages", "new", "admin", "notifications"]);

const channelSchema = z.object({
  name: z.string().trim().min(2, "Name the channel.").max(40, "Keep the name under 40 characters."),
  slug: z
    .string()
    .trim()
    .toLowerCase()
    .regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/, "The URL name may use lowercase letters, numbers and single hyphens.")
    .max(40),
  description: z.string().trim().max(200, "Keep the description under 200 characters."),
  icon: z.string().refine((v) => (CHANNEL_ICON_KEYS as readonly string[]).includes(v) === true, "Pick an icon from the list."),
  categoryId: z.string().nullable(),
  isReadOnly: z.boolean(),
  slowModeSeconds: z.coerce.number().int().min(0).max(3600),
});

export type ChannelInput = z.infer<typeof channelSchema>;

async function log(actorId: string, action: string, data: { targetUserId?: string | null; messageId?: string | null; reportId?: string | null; note?: string | null } = {}) {
  await prisma.communityModerationLog.create({ data: { actorId, action, ...data } });
}

function revalidate() {
  revalidatePath("/admin/community");
  revalidatePath("/community", "layout");
}

export async function getCommunityAdmin() {
  await requireAdmin();
  const [categories, channels, counts, reports, restrictions, logRows] = await Promise.all([
    prisma.communityCategory.findMany({ orderBy: [{ order: "asc" }, { name: "asc" }] }),
    prisma.communityChannel.findMany({ orderBy: [{ order: "asc" }, { name: "asc" }] }),
    prisma.communityMessage.groupBy({ by: ["channelId"], where: { deletedAt: null }, _count: { _all: true } }),
    prisma.communityReport.findMany({
      orderBy: [{ status: "asc" }, { createdAt: "desc" }],
      take: 100,
      include: {
        reporter: { select: { id: true, name: true } },
        targetUser: { select: { id: true, name: true, email: true } },
        message: {
          select: {
            id: true,
            body: true,
            title: true,
            deletedAt: true,
            threadRootId: true,
            createdAt: true,
            channel: { select: { slug: true, name: true } },
            attachments: { select: { id: true, fileName: true, url: true, kind: true } },
          },
        },
        directMessage: { select: { id: true, body: true, deletedAt: true, createdAt: true } },
      },
    }),
    prisma.communityRestriction.findMany({
      where: { until: { gt: new Date() } },
      orderBy: { until: "desc" },
      include: { user: { select: { id: true, name: true, email: true } } },
    }),
    prisma.communityModerationLog.findMany({ orderBy: { createdAt: "desc" }, take: 60 }),
  ]);
  const countBy = new Map(counts.map((c) => [c.channelId, c._count._all]));
  const actorIds = [...new Set(logRows.flatMap((l) => [l.actorId, l.targetUserId].filter(Boolean) as string[]))];
  const people = await prisma.user.findMany({ where: { id: { in: actorIds } }, select: { id: true, name: true } });
  const nameBy = new Map(people.map((p) => [p.id, p.name ?? "Unknown"]));

  return {
    categories: categories.map((c) => ({ id: c.id, name: c.name, order: c.order })),
    channels: channels.map((c) => ({
      id: c.id,
      name: c.name,
      slug: c.slug,
      description: c.description ?? "",
      icon: c.icon,
      categoryId: c.categoryId,
      isReadOnly: c.isReadOnly,
      isArchived: c.isArchived,
      slowModeSeconds: c.slowModeSeconds,
      order: c.order,
      messages: countBy.get(c.id) ?? 0,
    })),
    reports: reports.map((r) => ({
      id: r.id,
      reason: r.reason,
      details: r.details,
      status: r.status,
      resolution: r.resolution,
      createdAt: r.createdAt.toISOString(),
      reporter: r.reporter.name ?? "Unknown",
      target: r.targetUser ? { id: r.targetUser.id, name: r.targetUser.name ?? "Unknown", email: r.targetUser.email } : null,
      message: r.message
        ? {
            id: r.message.id,
            text: r.message.title ? `${r.message.title} — ${r.message.body}` : r.message.body,
            deleted: r.message.deletedAt != null,
            channel: r.message.channel.name,
            link: `/community/${r.message.channel.slug}?${r.message.threadRootId ? `thread=${r.message.threadRootId}&` : ""}m=${r.message.id}`,
            attachments: r.message.attachments,
          }
        : null,
      directMessage: r.directMessage
        ? { id: r.directMessage.id, text: r.directMessage.body, deleted: r.directMessage.deletedAt != null }
        : null,
    })),
    restrictions: restrictions.map((r) => ({
      userId: r.userId,
      name: r.user.name ?? "Unknown",
      email: r.user.email,
      until: r.until.toISOString(),
      reason: r.reason,
    })),
    log: logRows.map((l) => ({
      id: l.id,
      action: l.action,
      actor: nameBy.get(l.actorId) ?? "Unknown",
      target: l.targetUserId ? nameBy.get(l.targetUserId) ?? "Unknown" : null,
      note: l.note,
      createdAt: l.createdAt.toISOString(),
    })),
  };
}

/* ------------------------------- channels --------------------------------- */

export async function saveChannel(id: string | null, input: ChannelInput): Promise<Result> {
  const admin = await requireAdmin();
  const parsed = channelSchema.safeParse(input);
  if (!parsed.success) return { ok: false, error: parsed.error.issues[0]?.message ?? "Check the form." };
  const d = parsed.data;
  if (RESERVED.has(d.slug)) return { ok: false, error: `“${d.slug}” is reserved. Choose another URL name.` };
  if (d.categoryId) {
    const cat = await prisma.communityCategory.findUnique({ where: { id: d.categoryId }, select: { id: true } });
    if (!cat) return { ok: false, error: "That category no longer exists." };
  }
  const clash = await prisma.communityChannel.findUnique({ where: { slug: d.slug }, select: { id: true } });
  if (clash && clash.id !== id) return { ok: false, error: "Another channel already uses that URL name." };

  const data = {
    name: d.name,
    slug: d.slug,
    description: d.description || null,
    icon: d.icon,
    categoryId: d.categoryId,
    isReadOnly: d.isReadOnly,
    slowModeSeconds: d.slowModeSeconds,
  };
  if (id) {
    await prisma.communityChannel.update({ where: { id }, data });
    await log(admin.id, "EDIT_CHANNEL", { note: d.name });
  } else {
    const last = await prisma.communityChannel.aggregate({ where: { categoryId: d.categoryId }, _max: { order: true } });
    await prisma.communityChannel.create({ data: { ...data, order: (last._max.order ?? -1) + 1 } });
    await log(admin.id, "CREATE_CHANNEL", { note: d.name });
  }
  revalidate();
  return { ok: true };
}

export async function setChannelArchived(id: string, archived: boolean): Promise<Result> {
  const admin = await requireAdmin();
  const c = await prisma.communityChannel.update({ where: { id }, data: { isArchived: archived }, select: { name: true } });
  await log(admin.id, archived ? "ARCHIVE_CHANNEL" : "RESTORE_CHANNEL", { note: c.name });
  revalidate();
  return { ok: true };
}

/** Swap a channel with its neighbour inside the same category. */
export async function moveChannel(id: string, direction: -1 | 1): Promise<Result> {
  await requireAdmin();
  const c = await prisma.communityChannel.findUnique({ where: { id } });
  if (!c) return { ok: false, error: "Channel not found." };
  const siblings = await prisma.communityChannel.findMany({
    where: { categoryId: c.categoryId },
    orderBy: [{ order: "asc" }, { name: "asc" }],
    select: { id: true },
  });
  const idx = siblings.findIndex((s) => s.id === id);
  const swap = siblings[idx + direction];
  if (!swap) return { ok: true };
  const ids = siblings.map((s) => s.id);
  [ids[idx], ids[idx + direction]] = [ids[idx + direction], ids[idx]];
  await prisma.$transaction(ids.map((cid, order) => prisma.communityChannel.update({ where: { id: cid }, data: { order } })));
  revalidate();
  return { ok: true };
}

/* ------------------------------ categories -------------------------------- */

export async function saveCategory(id: string | null, name: string): Promise<Result> {
  const admin = await requireAdmin();
  const n = name.trim().slice(0, 40);
  if (n.length < 2) return { ok: false, error: "Name the category." };
  if (id) await prisma.communityCategory.update({ where: { id }, data: { name: n } });
  else {
    const last = await prisma.communityCategory.aggregate({ _max: { order: true } });
    await prisma.communityCategory.create({ data: { name: n, order: (last._max.order ?? -1) + 1 } });
  }
  await log(admin.id, id ? "RENAME_CATEGORY" : "CREATE_CATEGORY", { note: n });
  revalidate();
  return { ok: true };
}

export async function moveCategory(id: string, direction: -1 | 1): Promise<Result> {
  await requireAdmin();
  const all = await prisma.communityCategory.findMany({ orderBy: [{ order: "asc" }, { name: "asc" }], select: { id: true } });
  const idx = all.findIndex((c) => c.id === id);
  if (idx < 0 || !all[idx + direction]) return { ok: true };
  const ids = all.map((c) => c.id);
  [ids[idx], ids[idx + direction]] = [ids[idx + direction], ids[idx]];
  await prisma.$transaction(ids.map((cid, order) => prisma.communityCategory.update({ where: { id: cid }, data: { order } })));
  revalidate();
  return { ok: true };
}

/** Deleting a category keeps its channels; they move to "Other". */
export async function deleteCategory(id: string): Promise<Result> {
  const admin = await requireAdmin();
  const c = await prisma.communityCategory.delete({ where: { id }, select: { name: true } });
  await log(admin.id, "DELETE_CATEGORY", { note: c.name });
  revalidate();
  return { ok: true };
}

/* ------------------------------- moderation ------------------------------- */

export async function resolveReport(
  reportId: string,
  action: "DISMISS" | "DELETE_MESSAGE" | "RESTRICT",
  opts: { note?: string; days?: number } = {},
): Promise<Result> {
  const admin = await requireAdmin();
  const report = await prisma.communityReport.findUnique({ where: { id: reportId } });
  if (!report) return { ok: false, error: "Report not found." };
  const note = (opts.note ?? "").trim().slice(0, 500) || null;

  if (action === "DELETE_MESSAGE") {
    if (report.messageId) {
      const r = await adminRemoveMessage(report.messageId, note ?? `Report ${report.reason.toLowerCase()}`);
      if (!r.ok) return r;
    } else if (report.directMessageId) {
      await prisma.communityDirectMessage.update({ where: { id: report.directMessageId }, data: { deletedAt: new Date() } });
      await log(admin.id, "DELETE_DIRECT_MESSAGE", { targetUserId: report.targetUserId, reportId, note });
    }
  }
  if (action === "RESTRICT") {
    if (!report.targetUserId) return { ok: false, error: "This report has no student to restrict." };
    const r = await restrictUser(report.targetUserId, opts.days ?? 3, note ?? `Reported for ${report.reason.toLowerCase()}`);
    if (!r.ok) return r;
  }

  await prisma.communityReport.update({
    where: { id: reportId },
    data: {
      status: action === "DISMISS" ? "DISMISSED" : "ACTIONED",
      reviewedById: admin.id,
      reviewedAt: new Date(),
      resolution: note ?? (action === "DISMISS" ? "Dismissed" : action === "DELETE_MESSAGE" ? "Message removed" : "Student restricted"),
    },
  });
  await log(admin.id, `REPORT_${action}`, { reportId, targetUserId: report.targetUserId, messageId: report.messageId, note });
  revalidate();
  return { ok: true };
}

/** Soft-delete a channel message as a moderator, telling its author. */
export async function adminRemoveMessage(messageId: string, reason: string | null): Promise<Result> {
  const admin = await requireAdmin();
  const m = await prisma.communityMessage.findUnique({
    where: { id: messageId },
    select: { id: true, authorId: true, deletedAt: true, body: true, threadRootId: true, channel: { select: { id: true, slug: true, name: true } } },
  });
  if (!m) return { ok: false, error: "Message not found." };
  if (m.deletedAt) return { ok: true };
  await prisma.$transaction(async (tx) => {
    await tx.communityMessage.update({ where: { id: m.id }, data: { deletedAt: new Date(), deletedById: admin.id, pinnedAt: null } });
    if (m.threadRootId) {
      await tx.communityMessage.updateMany({ where: { id: m.threadRootId, replyCount: { gt: 0 } }, data: { replyCount: { decrement: 1 } } });
      await tx.communityMessage.updateMany({ where: { id: m.threadRootId, acceptedAnswerId: m.id }, data: { acceptedAnswerId: null } });
    }
  });
  await log(admin.id, "DELETE_MESSAGE", { targetUserId: m.authorId, messageId: m.id, note: reason ?? excerpt(m.body, 200) });
  if (m.authorId !== admin.id) {
    runInBackground("moderation-notice", () =>
      createNotifications([
        {
          userId: m.authorId,
          type: "MODERATION",
          actorId: null,
          messageId: m.id,
          channelId: m.channel.id,
          title: `A moderator removed one of your messages in #${m.channel.name}`,
          body: reason ?? "It did not follow the community guidelines.",
          url: `/community/${m.channel.slug}`,
          dedupeKey: `mod-delete:${m.id}`,
        },
      ]),
    );
  }
  revalidate();
  return { ok: true };
}

/** Remove one attachment (an inappropriate image) and keep the message text. */
export async function removeAttachment(attachmentId: string): Promise<Result> {
  const admin = await requireAdmin();
  const a = await prisma.communityAttachment.findUnique({
    where: { id: attachmentId },
    select: { id: true, url: true, fileName: true, message: { select: { id: true, authorId: true } } },
  });
  if (!a) return { ok: true };
  await prisma.communityAttachment.delete({ where: { id: a.id } });
  // Best effort: also delete the file from storage so the URL stops working.
  if (process.env.BLOB_READ_WRITE_TOKEN) {
    runInBackground("blob-delete", async () => {
      const { del } = await import("@vercel/blob");
      await del(a.url);
    });
  }
  await log(admin.id, "REMOVE_ATTACHMENT", { targetUserId: a.message.authorId, messageId: a.message.id, note: a.fileName });
  revalidate();
  return { ok: true };
}

export async function restrictUser(userId: string, days: number, reason: string): Promise<Result> {
  const admin = await requireAdmin();
  const target = await prisma.user.findUnique({ where: { id: userId }, select: { role: true, name: true } });
  if (!target) return { ok: false, error: "Student not found." };
  if (target.role === "ADMIN") return { ok: false, error: "Moderators cannot be restricted." };
  const d = Math.min(Math.max(Math.round(days), 1), 365);
  const until = new Date(Date.now() + d * 86_400_000);
  const why = reason.trim().slice(0, 300) || "Community guidelines";
  await prisma.communityRestriction.upsert({
    where: { userId },
    create: { userId, until, reason: why, createdById: admin.id },
    update: { until, reason: why, createdById: admin.id },
  });
  await log(admin.id, "RESTRICT_USER", { targetUserId: userId, note: `${d} day(s): ${why}` });
  runInBackground("restriction-notice", () =>
    createNotifications([
      {
        userId,
        type: "MODERATION",
        actorId: null,
        title: `Your community posting is paused for ${d} day${d === 1 ? "" : "s"}`,
        body: `Reason: ${why}. You can still read everything.`,
        url: "/community",
        dedupeKey: `restrict:${userId}:${until.toISOString()}`,
      },
    ]),
  );
  revalidate();
  return { ok: true };
}

export async function liftRestriction(userId: string): Promise<Result> {
  const admin = await requireAdmin();
  await prisma.communityRestriction.deleteMany({ where: { userId } });
  await log(admin.id, "LIFT_RESTRICTION", { targetUserId: userId });
  revalidate();
  return { ok: true };
}

/** Find a student to restrict by name, username or email. Admin-only, so email is fine here. */
export async function findStudents(q: string) {
  await requireAdmin();
  const t = q.trim();
  if (t.length < 2) return [];
  const rows = await prisma.user.findMany({
    where: {
      OR: [
        { name: { contains: t, mode: "insensitive" } },
        { email: { contains: t, mode: "insensitive" } },
        { username: { contains: t, mode: "insensitive" } },
      ],
    },
    select: { id: true, name: true, email: true, username: true },
    take: 8,
  });
  return rows.map((r) => ({ id: r.id, label: `${displayName(r.name)}${r.username ? ` · @${r.username}` : ""}${r.email ? ` · ${r.email}` : ""}` }));
}
