"use server";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { SEAT_HOLDING_STATUSES } from "@/lib/booking/status";
import { topicOf } from "@/lib/booking/topics";
import { displayName, excerpt } from "@/lib/community/server";

/**
 * "Since your last visit" — what the welcome screen shows when a student opens
 * Scholarly. Everything here is real and recent; a section with nothing new is
 * simply left out, and if every section is empty the screen does not open.
 *
 * `since` comes from the browser (when this device last closed the screen).
 * It is clamped to at most 14 days back so a first visit, or a long absence,
 * shows a short digest rather than months of history.
 */

export interface WhatsNew {
  since: string;
  sessions: {
    total: number;
    items: { id: string; title: string; topic: string; startsAt: string; host: string | null; seatsLeft: number }[];
  };
  announcements: { id: string; channelSlug: string; title: string; body: string; createdAt: string }[];
  notifications: {
    /** All unread, for the count; `items` are only the ones new since the last visit. */
    unread: number;
    items: { id: string; title: string; body: string; url: string; createdAt: string }[];
  };
  messagesUnread: number;
  isEmpty: boolean;
}

const MAX_LOOKBACK_MS = 14 * 86_400_000;

export async function getWhatsNew(sinceIso: string | null): Promise<WhatsNew> {
  const user = await requireUser();
  const now = Date.now();
  const parsed = sinceIso ? Date.parse(sinceIso) : NaN;
  const since = new Date(
    Number.isNaN(parsed) ? now - 7 * 86_400_000 : Math.max(Math.min(parsed, now), now - MAX_LOOKBACK_MS),
  );

  const [slots, announcements, unreadCount, unreadItems, dmRows] = await Promise.all([
    // Explicit select: the slot row holds the host's Meet link, which a
    // student must never receive before a booking is approved.
    prisma.mentorSlot.findMany({
      where: {
        createdAt: { gt: since },
        startsAt: { gt: new Date() },
        isBlocked: false,
        sessionType: "ONE_ON_ONE_SAT",
      },
      orderBy: { startsAt: "asc" },
      take: 60,
      select: {
        id: true,
        startsAt: true,
        title: true,
        subject: true,
        capacity: true,
        host: { select: { name: true } },
        _count: { select: { bookings: { where: { status: { in: SEAT_HOLDING_STATUSES } } } } },
      },
    }),
    prisma.communityMessage.findMany({
      where: {
        createdAt: { gt: since },
        deletedAt: null,
        threadRootId: null,
        channel: { isArchived: false },
        OR: [{ kind: "ANNOUNCEMENT" }, { channel: { slug: "announcements" } }],
      },
      orderBy: { createdAt: "desc" },
      take: 3,
      select: { id: true, title: true, body: true, createdAt: true, channel: { select: { slug: true } } },
    }),
    prisma.communityNotification.count({
      where: { userId: user.id, readAt: null, type: { notIn: ["ANNOUNCEMENT"] } },
    }),
    prisma.communityNotification.findMany({
      where: { userId: user.id, readAt: null, createdAt: { gt: since }, type: { notIn: ["ANNOUNCEMENT", "DIRECT_MESSAGE"] } },
      orderBy: { createdAt: "desc" },
      take: 4,
      select: { id: true, title: true, body: true, url: true, createdAt: true },
    }),
    prisma.$queryRaw<{ n: bigint }[]>`
      SELECT count(*) AS n FROM "CommunityConversationMember" cm
      WHERE cm."userId" = ${user.id} AND EXISTS (
        SELECT 1 FROM "CommunityDirectMessage" dm
        WHERE dm."conversationId" = cm."conversationId" AND dm."authorId" <> ${user.id}
          AND dm."deletedAt" IS NULL AND dm."createdAt" > GREATEST(COALESCE(cm."lastReadAt", 'epoch'::timestamp), ${since}))`,
  ]);

  // Only sessions a student could still book.
  const open = slots.filter((s) => s._count.bookings < s.capacity);
  const result: WhatsNew = {
    since: since.toISOString(),
    sessions: {
      total: open.length,
      items: open.slice(0, 4).map((s) => ({
        id: s.id,
        title: s.title ?? "1-on-1 session",
        topic: topicOf(s.subject),
        startsAt: s.startsAt.toISOString(),
        host: s.host?.name ? displayName(s.host.name) : null,
        seatsLeft: s.capacity - s._count.bookings,
      })),
    },
    announcements: announcements.map((a) => ({
      id: a.id,
      channelSlug: a.channel.slug,
      title: a.title ?? excerpt(a.body.split("\n")[0], 90),
      body: a.title ? excerpt(a.body, 180) : "",
      createdAt: a.createdAt.toISOString(),
    })),
    notifications: {
      unread: unreadCount,
      items: unreadItems.map((n) => ({ ...n, createdAt: n.createdAt.toISOString() })),
    },
    messagesUnread: Number(dmRows[0]?.n ?? 0),
    isEmpty: false,
  };
  result.isEmpty =
    result.sessions.total === 0 &&
    result.announcements.length === 0 &&
    result.notifications.items.length === 0 &&
    result.messagesUnread === 0;
  return result;
}
