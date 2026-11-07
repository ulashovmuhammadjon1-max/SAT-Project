"use server";

import type { Prisma } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { runInBackground } from "@/lib/background";
import { validateAttachments } from "@/lib/community/attachments";
import { createNotifications } from "@/lib/community/notify";
import {
  activeRestriction,
  blockSets,
  displayName,
  excerpt,
  isActiveNow,
  mentorIds,
  restrictionMessage,
} from "@/lib/community/server";
import { MAX_BODY, RATE_LIMIT_PER_MINUTE, type CommunityAttachmentView } from "@/lib/community/types";

/**
 * Private one-to-one messages.
 *
 * Separate tables from the public channels on purpose: a private message must
 * never be reachable through any channel query, search or home-page list.
 * Every read checks that the requester is a member of the conversation.
 *
 * Safety rules, all enforced here:
 *   - either side blocking the other stops new messages in both directions;
 *   - a student whose "who can message me" is NOBODY cannot be contacted
 *     (moderators excepted, so a safety message can always reach someone);
 *   - restricted students cannot send;
 *   - email addresses are never part of any payload.
 */

type Result<T = object> = ({ ok: true } & T) | { ok: false; error: string };

const pairKey = (a: string, b: string) => [a, b].sort().join(":");

export interface ConversationSummary {
  id: string;
  other: { id: string; name: string; image: string | null; activeNow: boolean };
  lastMessage: { body: string; mine: boolean; at: string } | null;
  unread: number;
  muted: boolean;
}

export interface DirectMessageView {
  id: string;
  body: string;
  createdAt: string;
  editedAt: string | null;
  deleted: boolean;
  mine: boolean;
  attachments: CommunityAttachmentView[];
  replyTo: { id: string; excerpt: string; mine: boolean } | null;
}

async function membership(conversationId: string, userId: string) {
  return prisma.communityConversationMember.findUnique({
    where: { conversationId_userId: { conversationId, userId } },
  });
}

/** Whether `fromId` may message `toId` right now, and why not. */
async function canMessage(fromId: string, fromRole: string, toId: string): Promise<string | null> {
  if (fromId === toId) return "You cannot message yourself.";
  const [target, blocks] = await Promise.all([
    prisma.user.findUnique({ where: { id: toId }, select: { id: true, communityMember: { select: { dmPolicy: true } } } }),
    blockSets(fromId),
  ]);
  if (!target) return "That student no longer exists.";
  if (blocks.iBlocked.has(toId)) return "You blocked this student. Unblock them to send a message.";
  if (blocks.blockedMe.has(toId)) return "This student is not accepting messages from you.";
  if (target.communityMember?.dmPolicy === "NOBODY" && fromRole !== "ADMIN") {
    return "This student has turned off private messages.";
  }
  return null;
}

export async function listConversations(): Promise<ConversationSummary[]> {
  const user = await requireUser();
  const mine = await prisma.communityConversationMember.findMany({
    where: { userId: user.id },
    orderBy: { conversation: { lastMessageAt: "desc" } },
    take: 50,
    select: {
      conversationId: true,
      lastReadAt: true,
      mutedAt: true,
      conversation: {
        select: {
          members: {
            where: { userId: { not: user.id } },
            select: {
              user: {
                select: {
                  id: true,
                  name: true,
                  image: true,
                  communityPresence: true,
                  communityMember: { select: { showPresence: true } },
                },
              },
            },
          },
          messages: { orderBy: { createdAt: "desc" }, take: 1, select: { body: true, authorId: true, createdAt: true, deletedAt: true, attachments: true } },
        },
      },
    },
  });
  const ids = mine.map((m) => m.conversationId);
  const unread = ids.length
    ? await prisma.$queryRaw<{ conversationId: string; n: bigint }[]>`
        SELECT dm."conversationId", count(*) AS n
        FROM "CommunityDirectMessage" dm
        JOIN "CommunityConversationMember" me ON me."conversationId" = dm."conversationId" AND me."userId" = ${user.id}
        WHERE dm."conversationId" = ANY(${ids}) AND dm."authorId" <> ${user.id} AND dm."deletedAt" IS NULL
          AND dm."createdAt" > COALESCE(me."lastReadAt", 'epoch'::timestamp)
        GROUP BY dm."conversationId"`
    : [];
  const unreadBy = new Map(unread.map((u) => [u.conversationId, Number(u.n)]));

  return mine
    .filter((m) => m.conversation.members[0] && m.conversation.messages.length > 0)
    .map((m) => {
      const other = m.conversation.members[0].user;
      const last = m.conversation.messages[0];
      return {
        id: m.conversationId,
        other: {
          id: other.id,
          name: displayName(other.name),
          image: other.image,
          activeNow: other.communityMember?.showPresence !== false && isActiveNow(other.communityPresence),
        },
        lastMessage: last
          ? {
              body: last.deletedAt ? "Message deleted" : excerpt(last.body, 80) || (last.attachments ? "Attachment" : ""),
              mine: last.authorId === user.id,
              at: last.createdAt.toISOString(),
            }
          : null,
        unread: unreadBy.get(m.conversationId) ?? 0,
        muted: Boolean(m.mutedAt),
      };
    });
}

/** Find or create the conversation with another student. */
export async function openConversation(otherUserId: string): Promise<Result<{ id: string }>> {
  const user = await requireUser();
  const key = pairKey(user.id, otherUserId);
  const existing = await prisma.communityConversation.findUnique({ where: { pairKey: key }, select: { id: true } });
  if (existing) return { ok: true, id: existing.id };

  const why = await canMessage(user.id, user.role, otherUserId);
  if (why) return { ok: false, error: why };
  const restriction = await activeRestriction(user.id);
  if (restriction) return { ok: false, error: restrictionMessage(restriction.until) };

  try {
    const c = await prisma.communityConversation.create({
      data: {
        pairKey: key,
        members: { create: [{ userId: user.id, lastReadAt: new Date() }, { userId: otherUserId }] },
      },
      select: { id: true },
    });
    return { ok: true, id: c.id };
  } catch {
    // Created by the other side at the same moment.
    const again = await prisma.communityConversation.findUnique({ where: { pairKey: key }, select: { id: true } });
    return again ? { ok: true, id: again.id } : { ok: false, error: "Could not start the conversation." };
  }
}

export async function getConversation(conversationId: string): Promise<{
  id: string;
  other: { id: string; name: string; image: string | null; isAdmin: boolean; isMentor: boolean; activeNow: boolean };
  messages: DirectMessageView[];
  otherLastReadAt: string | null;
  canSend: boolean;
  blockReason: string | null;
  muted: boolean;
} | null> {
  const user = await requireUser();
  const me = await membership(conversationId, user.id);
  if (!me) return null;

  const [otherMember, rows] = await Promise.all([
    prisma.communityConversationMember.findFirst({
      where: { conversationId, userId: { not: user.id } },
      select: {
        lastReadAt: true,
        user: {
          select: { id: true, name: true, image: true, role: true, communityPresence: true, communityMember: { select: { showPresence: true } } },
        },
      },
    }),
    prisma.communityDirectMessage.findMany({
      where: { conversationId },
      orderBy: { createdAt: "desc" },
      take: 200,
      include: { replyTo: { select: { id: true, body: true, authorId: true, deletedAt: true } } },
    }),
  ]);
  if (!otherMember) return null;
  const other = otherMember.user;
  const blockReason = await canMessage(user.id, user.role, other.id);
  const mentors = await mentorIds([other.id]);

  return {
    id: conversationId,
    other: {
      id: other.id,
      name: displayName(other.name),
      image: other.image,
      isAdmin: other.role === "ADMIN",
      isMentor: mentors.has(other.id),
      activeNow: other.communityMember?.showPresence !== false && isActiveNow(other.communityPresence),
    },
    messages: rows.reverse().map((m) => ({
      id: m.id,
      body: m.deletedAt ? "" : m.body,
      createdAt: m.createdAt.toISOString(),
      editedAt: m.editedAt?.toISOString() ?? null,
      deleted: m.deletedAt != null,
      mine: m.authorId === user.id,
      attachments: m.deletedAt ? [] : ((m.attachments as unknown as CommunityAttachmentView[] | null) ?? []),
      replyTo: m.replyTo
        ? {
            id: m.replyTo.id,
            excerpt: m.replyTo.deletedAt ? "message deleted" : excerpt(m.replyTo.body, 100) || "attachment",
            mine: m.replyTo.authorId === user.id,
          }
        : null,
    })),
    otherLastReadAt: otherMember.lastReadAt?.toISOString() ?? null,
    canSend: !blockReason,
    blockReason,
    muted: Boolean(me.mutedAt),
  };
}

export async function sendDirectMessage(input: {
  conversationId: string;
  body: string;
  replyToId?: string | null;
  attachments?: unknown;
}): Promise<Result<{ id: string }>> {
  const user = await requireUser();
  const me = await membership(input.conversationId, user.id);
  if (!me) return { ok: false, error: "Conversation not found." };

  const restriction = await activeRestriction(user.id);
  if (restriction) return { ok: false, error: restrictionMessage(restriction.until) };

  const body = (input.body ?? "").trim();
  if (body.length > MAX_BODY) return { ok: false, error: `Keep it under ${MAX_BODY} characters.` };
  const files = validateAttachments(input.attachments);
  if (!files.ok) return { ok: false, error: files.error };
  if (!body && files.attachments.length === 0) return { ok: false, error: "Write something first." };

  const other = await prisma.communityConversationMember.findFirst({
    where: { conversationId: input.conversationId, userId: { not: user.id } },
    select: { userId: true, mutedAt: true },
  });
  if (!other) return { ok: false, error: "Conversation not found." };
  // Re-checked on every message, not only when the conversation was opened:
  // a block placed mid-conversation takes effect immediately.
  const why = await canMessage(user.id, user.role, other.userId);
  if (why) return { ok: false, error: why };

  const recent = await prisma.communityDirectMessage.count({
    where: { authorId: user.id, createdAt: { gte: new Date(Date.now() - 60_000) } },
  });
  if (recent >= RATE_LIMIT_PER_MINUTE) return { ok: false, error: "You're sending very fast — wait a moment." };

  let replyToId: string | null = null;
  if (input.replyToId) {
    const parent = await prisma.communityDirectMessage.findUnique({
      where: { id: input.replyToId },
      select: { conversationId: true },
    });
    if (parent?.conversationId === input.conversationId) replyToId = input.replyToId;
  }

  const now = new Date();
  const [msg] = await prisma.$transaction([
    prisma.communityDirectMessage.create({
      data: {
        conversationId: input.conversationId,
        authorId: user.id,
        body,
        replyToId,
        attachments: files.attachments.length
          ? (files.attachments.map((a, i) => ({ ...a, id: `a${i}` })) as unknown as Prisma.InputJsonValue)
          : undefined,
      },
      select: { id: true },
    }),
    prisma.communityConversation.update({ where: { id: input.conversationId }, data: { lastMessageAt: now } }),
    prisma.communityConversationMember.update({
      where: { conversationId_userId: { conversationId: input.conversationId, userId: user.id } },
      data: { lastReadAt: now },
    }),
  ]);

  if (!other.mutedAt) {
    const recipient = other.userId;
    runInBackground("community-dm-notify", async () => {
      const author = await prisma.user.findUnique({ where: { id: user.id }, select: { name: true } });
      const title = `${displayName(author?.name)} sent you a message`;
      const preview = excerpt(body, 160) || "Sent an attachment";
      // One live notification per unread stretch of a conversation: while the
      // last one is unread it is refreshed, so ten quick messages are one
      // notification and (at most) one email, not ten.
      const open = await prisma.communityNotification.findFirst({
        where: { userId: recipient, conversationId: input.conversationId, type: "DIRECT_MESSAGE", readAt: null },
        select: { id: true },
      });
      if (open) {
        await prisma.communityNotification.update({
          where: { id: open.id },
          data: { body: preview, messageId: msg.id, createdAt: new Date() },
        });
        return;
      }
      await createNotifications([
        {
          userId: recipient,
          type: "DIRECT_MESSAGE",
          actorId: user.id,
          messageId: msg.id,
          conversationId: input.conversationId,
          title,
          body: preview,
          url: `/community/messages/${input.conversationId}`,
          dedupeKey: `dm:${msg.id}:${recipient}`,
        },
      ]);
    });
  }
  return { ok: true, id: msg.id };
}

export async function deleteDirectMessage(id: string): Promise<Result> {
  const user = await requireUser();
  const m = await prisma.communityDirectMessage.findUnique({ where: { id }, select: { authorId: true, deletedAt: true } });
  if (!m) return { ok: false, error: "Message not found." };
  if (m.authorId !== user.id && user.role !== "ADMIN") return { ok: false, error: "You can only delete your own messages." };
  if (!m.deletedAt) await prisma.communityDirectMessage.update({ where: { id }, data: { deletedAt: new Date() } });
  return { ok: true };
}

export async function editDirectMessage(id: string, body: string): Promise<Result> {
  const user = await requireUser();
  const trimmed = body.trim();
  if (!trimmed) return { ok: false, error: "A message cannot be emptied — delete it instead." };
  if (trimmed.length > MAX_BODY) return { ok: false, error: `Keep it under ${MAX_BODY} characters.` };
  const m = await prisma.communityDirectMessage.findUnique({ where: { id }, select: { authorId: true, deletedAt: true } });
  if (!m || m.deletedAt) return { ok: false, error: "Message not found." };
  if (m.authorId !== user.id) return { ok: false, error: "You can only edit your own messages." };
  await prisma.communityDirectMessage.update({ where: { id }, data: { body: trimmed, editedAt: new Date() } });
  return { ok: true };
}

export async function markConversationRead(conversationId: string): Promise<void> {
  const user = await requireUser();
  const now = new Date();
  await prisma.communityConversationMember.updateMany({
    where: { conversationId, userId: user.id },
    data: { lastReadAt: now },
  });
  await prisma.communityNotification.updateMany({
    where: { userId: user.id, conversationId, readAt: null },
    data: { readAt: now },
  });
}

export async function setConversationMuted(conversationId: string, muted: boolean): Promise<Result> {
  const user = await requireUser();
  const r = await prisma.communityConversationMember.updateMany({
    where: { conversationId, userId: user.id },
    data: { mutedAt: muted ? new Date() : null },
  });
  return r.count ? { ok: true } : { ok: false, error: "Conversation not found." };
}
