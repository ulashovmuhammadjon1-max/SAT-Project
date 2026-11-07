"use server";

import type { Prisma } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { displayName } from "@/lib/community/server";
import type { NotificationView } from "@/lib/community/types";

/**
 * The notification centre. Every query is scoped to the signed-in student's
 * own rows; nothing here takes a user id from the client.
 */

export type NotificationFilter = "all" | "unread" | "replies" | "mentions" | "messages";

const PAGE = 25;

export async function listNotifications(input: { filter?: NotificationFilter; cursor?: string | null; take?: number } = {}): Promise<{
  items: NotificationView[];
  nextCursor: string | null;
  unread: number;
}> {
  const user = await requireUser();
  const take = Math.min(Math.max(input.take ?? PAGE, 1), 50);

  const where: Prisma.CommunityNotificationWhereInput = { userId: user.id };
  switch (input.filter) {
    case "unread":
      where.readAt = null;
      break;
    case "replies":
      where.type = { in: ["REPLY", "THREAD_REPLY", "ANSWER", "ANSWER_ACCEPTED"] };
      break;
    case "mentions":
      where.type = "MENTION";
      break;
    case "messages":
      where.type = "DIRECT_MESSAGE";
      break;
  }

  const [rows, unread] = await Promise.all([
    prisma.communityNotification.findMany({
      where,
      orderBy: [{ createdAt: "desc" }, { id: "desc" }],
      take: take + 1,
      ...(input.cursor ? { cursor: { id: input.cursor }, skip: 1 } : {}),
      select: {
        id: true,
        type: true,
        title: true,
        body: true,
        url: true,
        readAt: true,
        createdAt: true,
        actor: { select: { name: true, image: true } },
      },
    }),
    prisma.communityNotification.count({ where: { userId: user.id, readAt: null } }),
  ]);

  const page = rows.slice(0, take);
  return {
    items: page.map((n) => ({
      id: n.id,
      type: n.type,
      title: n.title,
      body: n.body,
      url: n.url,
      read: n.readAt != null,
      createdAt: n.createdAt.toISOString(),
      actor: n.actor ? { name: displayName(n.actor.name), image: n.actor.image } : null,
    })),
    nextCursor: rows.length > take ? page[page.length - 1].id : null,
    unread,
  };
}

export async function markNotificationRead(id: string): Promise<void> {
  const user = await requireUser();
  await prisma.communityNotification.updateMany({
    where: { id, userId: user.id, readAt: null },
    data: { readAt: new Date() },
  });
}

export async function markAllNotificationsRead(): Promise<void> {
  const user = await requireUser();
  await prisma.communityNotification.updateMany({
    where: { userId: user.id, readAt: null },
    data: { readAt: new Date() },
  });
}

/** Opening a message marks every notification about it as read. */
export async function markNotificationsForMessage(messageId: string): Promise<void> {
  const user = await requireUser();
  await prisma.communityNotification.updateMany({
    where: { userId: user.id, messageId, readAt: null },
    data: { readAt: new Date() },
  });
}
