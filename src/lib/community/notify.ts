/**
 * Creating community notifications.
 *
 * Every notification is written with a `dedupeKey` that is UNIQUE in the
 * database, so running the same code path twice (a retry, a double submit)
 * can never notify anyone twice. The email side is a separate outbox row
 * (`CommunityEmailDelivery`, unique per notification) that the processor in
 * `email.ts` picks up — posting a message never waits for a mail provider.
 *
 * Who is NOT notified, whatever else applies:
 *   - the person who caused it;
 *   - anyone who has blocked that person;
 *   - for discussion activity (not direct replies or mentions): anyone who
 *     muted that discussion or channel.
 */
import type { CommunityNotificationType, Prisma } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { runInBackground } from "@/lib/background";
import {
  displayName,
  excerpt,
  isActiveNow,
  messageUrl,
  nextDigestAt,
  prefsFor,
  type MemberPrefs,
} from "@/lib/community/server";

type NotifType = CommunityNotificationType;

/** Lower wins: a person who is both replied to and mentioned gets one "reply". */
const PRIORITY: Record<NotifType, number> = {
  REPLY: 0,
  MENTION: 1,
  ANSWER: 2,
  DIRECT_MESSAGE: 2,
  THREAD_REPLY: 3,
  ANSWER_ACCEPTED: 4,
  REACTION: 5,
  ANNOUNCEMENT: 6,
  MODERATION: 7,
};

export interface NewNotification {
  userId: string;
  type: NotifType;
  actorId: string | null;
  messageId?: string | null;
  channelId?: string | null;
  conversationId?: string | null;
  title: string;
  body: string;
  url: string;
  dedupeKey: string;
  /** For email preference routing: is this about the recipient's own post? */
  aboutOwnPost?: boolean;
}

/** Whether a notification of this type should be emailed under these prefs. */
export function wantsEmail(type: NotifType, prefs: MemberPrefs, aboutOwnPost = false): boolean {
  switch (type) {
    case "REPLY":
      return prefs.emailReplies;
    case "MENTION":
      return prefs.emailMentions;
    case "ANSWER":
    case "THREAD_REPLY":
      // A reply to your own post is a reply to you; activity elsewhere is not.
      return aboutOwnPost ? prefs.emailReplies : prefs.emailActivity;
    case "DIRECT_MESSAGE":
      return prefs.emailDirect;
    case "ANNOUNCEMENT":
      return prefs.emailAnnouncements;
    case "ANSWER_ACCEPTED":
    case "REACTION":
      return prefs.emailActivity;
    default:
      return false;
  }
}

/**
 * Write notifications and queue their emails. Idempotent on dedupeKey.
 * Returns how many notifications were newly created.
 */
export async function createNotifications(rows: NewNotification[]): Promise<number> {
  if (rows.length === 0) return 0;

  const created = await prisma.communityNotification.createMany({
    data: rows.map((r) => ({
      userId: r.userId,
      type: r.type,
      actorId: r.actorId,
      messageId: r.messageId ?? null,
      channelId: r.channelId ?? null,
      conversationId: r.conversationId ?? null,
      title: r.title.slice(0, 200),
      body: r.body.slice(0, 300),
      url: r.url,
      dedupeKey: r.dedupeKey,
    })),
    skipDuplicates: true,
  });
  if (created.count === 0) return 0;

  await queueEmails(rows);
  return created.count;
}

/** Create outbox rows for the notifications whose recipients want email. */
async function queueEmails(rows: NewNotification[]) {
  const recipients = [...new Set(rows.map((r) => r.userId))];
  const [prefs, presence, notes] = await Promise.all([
    prefsFor(recipients),
    prisma.communityPresence.findMany({ where: { userId: { in: recipients } } }),
    prisma.communityNotification.findMany({
      where: { dedupeKey: { in: rows.map((r) => r.dedupeKey) } },
      select: { id: true, dedupeKey: true, userId: true },
    }),
  ]);
  const presenceBy = new Map(presence.map((p) => [p.userId, p]));
  const idByKey = new Map(notes.map((n) => [n.dedupeKey, n.id]));
  const now = Date.now();

  const deliveries: Prisma.CommunityEmailDeliveryCreateManyInput[] = [];
  for (const r of rows) {
    const id = idByKey.get(r.dedupeKey);
    const p = prefs.get(r.userId);
    if (!id || !p || !wantsEmail(r.type, p, r.aboutOwnPost)) continue;
    // Someone using Scholarly right now sees it in-app first; the email only
    // goes if it is still unread a few minutes later (re-checked at send time).
    const sendAfter = p.emailDigest
      ? nextDigestAt()
      : isActiveNow(presenceBy.get(r.userId), now)
        ? new Date(now + 5 * 60_000)
        : new Date(now);
    deliveries.push({ notificationId: id, userId: r.userId, sendAfter });
  }
  if (deliveries.length === 0) return;
  await prisma.communityEmailDelivery.createMany({ data: deliveries, skipDuplicates: true });

  if (deliveries.some((d) => (d.sendAfter as Date).getTime() <= now)) {
    // Imported lazily: email.ts imports this module's types.
    runInBackground("community-email", async () => {
      const { processEmailOutbox } = await import("@/lib/community/email");
      await processEmailOutbox();
    });
  }
}

/**
 * Everyone who should hear about a new channel message, with the single most
 * important reason for each.
 */
export async function notifyForMessage(messageId: string): Promise<void> {
  const m = await prisma.communityMessage.findUnique({
    where: { id: messageId },
    select: {
      id: true,
      body: true,
      kind: true,
      title: true,
      authorId: true,
      threadRootId: true,
      deletedAt: true,
      author: { select: { name: true, role: true } },
      channel: { select: { id: true, slug: true, name: true } },
      replyTo: { select: { authorId: true, deletedAt: true } },
      threadRoot: { select: { id: true, authorId: true, kind: true, deletedAt: true, title: true } },
      mentions: { select: { userId: true } },
    },
  });
  if (!m || m.deletedAt) return;

  const actor = displayName(m.author.name, m.author.role);
  const where = `#${m.channel.name}`;
  const text = excerpt(m.title ? `${m.title} — ${m.body}` : m.body) || "Shared an attachment";
  const url = messageUrl(m.channel.slug, m.id, m.threadRootId);

  // Announcements go to everyone. Email only for those who opted in.
  if (m.kind === "ANNOUNCEMENT" && !m.threadRootId && m.author.role === "ADMIN") {
    const users = await prisma.user.findMany({ where: { id: { not: m.authorId } }, select: { id: true } });
    const rows: NewNotification[] = users.map((u) => ({
      userId: u.id,
      type: "ANNOUNCEMENT",
      actorId: m.authorId,
      messageId: m.id,
      channelId: m.channel.id,
      title: m.title ? `Announcement: ${m.title}` : `New announcement in ${where}`,
      body: excerpt(m.body),
      url,
      dedupeKey: `msg:${m.id}:${u.id}`,
    }));
    for (let i = 0; i < rows.length; i += 1000) await createNotifications(rows.slice(i, i + 1000));
    return;
  }

  // recipient -> [type, aboutOwnPost]
  const best = new Map<string, { type: NotifType; own: boolean }>();
  const offer = (userId: string | null | undefined, type: NotifType, own = false) => {
    if (!userId || userId === m.authorId) return;
    const cur = best.get(userId);
    if (!cur || PRIORITY[type] < PRIORITY[cur.type]) best.set(userId, { type, own: own || Boolean(cur?.own) });
  };

  if (m.replyTo && !m.replyTo.deletedAt) offer(m.replyTo.authorId, "REPLY", true);
  for (const mention of m.mentions) offer(mention.userId, "MENTION");

  let mutedThread = new Set<string>();
  if (m.threadRoot && !m.threadRoot.deletedAt) {
    offer(m.threadRoot.authorId, m.threadRoot.kind === "QUESTION" ? "ANSWER" : "THREAD_REPLY", true);
    const follows = await prisma.communityThreadFollow.findMany({
      where: { rootId: m.threadRoot.id },
      select: { userId: true, state: true },
    });
    mutedThread = new Set(follows.filter((f) => f.state === "MUTED").map((f) => f.userId));
    for (const f of follows) if (f.state === "FOLLOWING") offer(f.userId, "THREAD_REPLY");
  }

  const ids = [...best.keys()];
  if (ids.length === 0) return;

  const [blocks, channelMutes] = await Promise.all([
    prisma.communityBlock.findMany({
      where: { blockerId: { in: ids }, blockedId: m.authorId },
      select: { blockerId: true },
    }),
    prisma.communityRead.findMany({
      where: { channelId: m.channel.id, userId: { in: ids }, mutedAt: { not: null } },
      select: { userId: true },
    }),
  ]);
  const blockedBy = new Set(blocks.map((b) => b.blockerId));
  const channelMuted = new Set(channelMutes.map((c) => c.userId));

  const rows: NewNotification[] = [];
  for (const [userId, { type, own }] of best) {
    if (blockedBy.has(userId)) continue;
    const ambient = type === "THREAD_REPLY" || type === "ANSWER";
    // Muting quiets discussion activity; a direct reply or mention still lands.
    if (ambient && (mutedThread.has(userId) || (!own && channelMuted.has(userId)))) continue;

    const title =
      type === "REPLY"
        ? `${actor} replied to your message in ${where}`
        : type === "MENTION"
          ? `${actor} mentioned you in ${where}`
          : type === "ANSWER"
            ? `${actor} answered your question${m.threadRoot?.title ? `: ${m.threadRoot.title}` : ""}`
            : own
              ? `${actor} replied to your post in ${where}`
              : `${actor} replied in a discussion you follow`;

    rows.push({
      userId,
      type,
      actorId: m.authorId,
      messageId: m.id,
      channelId: m.channel.id,
      title,
      body: text,
      url,
      dedupeKey: `msg:${m.id}:${userId}`,
      aboutOwnPost: own,
    });
  }
  await createNotifications(rows);
}

/**
 * A reaction notification. One live notification per message: a second
 * reaction updates it ("Ali and 2 others reacted") instead of adding a row.
 */
export async function notifyReaction(messageId: string, reactorId: string, emoji: string) {
  const m = await prisma.communityMessage.findUnique({
    where: { id: messageId },
    select: {
      authorId: true,
      body: true,
      title: true,
      threadRootId: true,
      deletedAt: true,
      channel: { select: { id: true, slug: true } },
      reactions: { select: { userId: true }, distinct: ["userId"] },
    },
  });
  if (!m || m.deletedAt || m.authorId === reactorId) return;
  const blocked = await prisma.communityBlock.findUnique({
    where: { blockerId_blockedId: { blockerId: m.authorId, blockedId: reactorId } },
    select: { id: true },
  });
  if (blocked) return;

  const reactor = await prisma.user.findUnique({ where: { id: reactorId }, select: { name: true, role: true } });
  const others = m.reactions.filter((r) => r.userId !== reactorId && r.userId !== m.authorId).length;
  const who = displayName(reactor?.name, reactor?.role);
  const title =
    others > 0
      ? `${who} and ${others} other${others === 1 ? "" : "s"} reacted to your message`
      : `${who} reacted ${emoji} to your message`;
  const key = `react:${messageId}`;
  const existing = await prisma.communityNotification.findUnique({ where: { dedupeKey: key }, select: { id: true } });
  if (existing) {
    await prisma.communityNotification.update({
      where: { id: existing.id },
      data: { title, actorId: reactorId, readAt: null, createdAt: new Date() },
    });
    return;
  }
  await createNotifications([
    {
      userId: m.authorId,
      type: "REACTION",
      actorId: reactorId,
      messageId,
      channelId: m.channel.id,
      title,
      body: excerpt(m.title ?? m.body) || "Your attachment",
      url: messageUrl(m.channel.slug, messageId, m.threadRootId),
      dedupeKey: key,
    },
  ]);
}
