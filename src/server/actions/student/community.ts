"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { shortName } from "@/lib/leaderboard";
import {
  MAX_ATTACHMENTS,
  MAX_BODY,
  PAGE_SIZE,
  RATE_LIMIT_PER_MINUTE,
  REACTIONS,
  type ChannelView,
  type CommunityMessageView,
  type NewAttachment,
  type ReactionSummary,
} from "@/lib/community/types";

/**
 * Community chat.
 *
 * Message bodies are stored and returned as **plain text, never HTML**. The
 * client escapes them at render time and linkifies afterwards, so a student
 * cannot post markup that executes in another student's browser. Nothing in
 * this file ever builds an HTML string.
 */

/* -------------------------------------------------------------------------- */
/* Reads                                                                       */
/* -------------------------------------------------------------------------- */

/** Channels with this student's unread counts. */
export async function listChannels(): Promise<ChannelView[]> {
  const user = await requireUser();

  const [channels, reads, account] = await Promise.all([
    prisma.communityChannel.findMany({
      where: { isArchived: false },
      orderBy: [{ order: "asc" }, { name: "asc" }],
    }),
    prisma.communityRead.findMany({ where: { userId: user.id } }),
    // The session user carries only id/role, so the join date needed for the
    // unread window has to be read separately.
    prisma.user.findUnique({ where: { id: user.id }, select: { createdAt: true } }),
  ]);

  const lastRead = new Map(reads.map((r) => [r.channelId, r.lastReadAt]));

  return Promise.all(
    channels.map(async (c) => {
      // A channel never read before counts everything, but from the epoch the
      // count would be the whole history — cap the window at the account's own
      // creation so joining does not present a thousand unread messages.
      const since = lastRead.get(c.id) ?? account?.createdAt ?? new Date(0);
      const [unread, mentionsUnread] = await Promise.all([
        prisma.communityMessage.count({
          where: {
            channelId: c.id,
            createdAt: { gt: since },
            deletedAt: null,
            // Your own messages are not news to you.
            authorId: { not: user.id },
          },
        }),
        prisma.communityMention.count({
          where: {
            userId: user.id,
            message: { channelId: c.id, createdAt: { gt: since }, deletedAt: null },
          },
        }),
      ]);
      return {
        id: c.id,
        slug: c.slug,
        name: c.name,
        description: c.description,
        isReadOnly: c.isReadOnly,
        unread,
        mentionsUnread,
      };
    })
  );
}

function excerptOf(text: string, deleted: boolean): string {
  if (deleted) return "message deleted";
  const flat = text.replace(/\s+/g, " ").trim();
  return flat.length > 120 ? `${flat.slice(0, 119)}…` : flat;
}

/**
 * A page of messages, oldest first.
 *
 * `before` pages backwards through history. The rows are fetched newest-first
 * so the limit takes the *most recent* page, then reversed for display —
 * fetching oldest-first with a limit would return the beginning of the channel
 * forever.
 */
export async function listMessages(
  channelSlug: string,
  before?: string
): Promise<{ messages: CommunityMessageView[]; hasMore: boolean }> {
  const user = await requireUser();

  const channel = await prisma.communityChannel.findUnique({ where: { slug: channelSlug } });
  if (!channel) return { messages: [], hasMore: false };

  const cursor = before
    ? await prisma.communityMessage.findUnique({
        where: { id: before },
        select: { createdAt: true },
      })
    : null;

  const rows = await prisma.communityMessage.findMany({
    where: {
      channelId: channel.id,
      ...(cursor ? { createdAt: { lt: cursor.createdAt } } : {}),
    },
    orderBy: { createdAt: "desc" },
    take: PAGE_SIZE + 1,
    include: {
      author: { select: { id: true, name: true, role: true } },
      attachments: true,
      mentions: { where: { userId: user.id }, select: { id: true } },
      reactions: { select: { emoji: true, userId: true } },
      replyTo: {
        select: {
          id: true,
          body: true,
          deletedAt: true,
          author: { select: { name: true } },
        },
      },
    },
  });

  const hasMore = rows.length > PAGE_SIZE;
  const page = hasMore ? rows.slice(0, PAGE_SIZE) : rows;
  const isAdmin = user.role === "ADMIN";

  const messages = page.reverse().map((m): CommunityMessageView => {
    const deleted = m.deletedAt != null;

    // Group by emoji, preserving the order they were first used so the row of
    // pills does not reshuffle every time someone reacts.
    const byEmoji = new Map<string, ReactionSummary>();
    for (const r of m.reactions) {
      const entry = byEmoji.get(r.emoji) ?? { emoji: r.emoji, count: 0, mine: false };
      entry.count += 1;
      if (r.userId === user.id) entry.mine = true;
      byEmoji.set(r.emoji, entry);
    }

    return {
      id: m.id,
      // A deleted message keeps its slot in the thread but surrenders its text.
      body: deleted ? "" : m.body,
      createdAt: m.createdAt.toISOString(),
      editedAt: m.editedAt?.toISOString() ?? null,
      deleted,
      author: {
        id: m.author.id,
        name: shortName(m.author.name),
        isAdmin: m.author.role === "ADMIN",
        isMe: m.author.id === user.id,
      },
      attachments: deleted
        ? []
        : m.attachments.map((a) => ({
            id: a.id,
            kind: a.kind,
            url: a.url,
            fileName: a.fileName,
            contentType: a.contentType,
            sizeBytes: a.sizeBytes,
          })),
      mentionedMe: m.mentions.length > 0,
      replyTo: m.replyTo
        ? {
            id: m.replyTo.id,
            authorName: shortName(m.replyTo.author.name),
            excerpt: excerptOf(m.replyTo.body, m.replyTo.deletedAt != null),
            deleted: m.replyTo.deletedAt != null,
          }
        : null,
      // Reactions come off a deleted message with its content.
      reactions: deleted ? [] : [...byEmoji.values()],
      // Editing is the author's alone. An admin can remove a message but must
      // not be able to rewrite what somebody else said.
      canEdit: !deleted && m.author.id === user.id,
      canDelete: !deleted && (m.author.id === user.id || isAdmin),
    };
  });

  return { messages, hasMore };
}

/** Students matching a partial @mention. */
export async function searchMembers(
  query: string
): Promise<{ id: string; name: string; handle: string }[]> {
  await requireUser();
  const q = query.trim();
  if (q.length < 1) return [];

  const users = await prisma.user.findMany({
    where: {
      name: { contains: q, mode: "insensitive" },
      // Never surfaces email addresses — a mention picker is not a directory.
      NOT: { name: null },
    },
    select: { id: true, name: true, role: true },
    orderBy: { name: "asc" },
    take: 8,
  });

  return users.map((u) => ({
    id: u.id,
    name: shortName(u.name),
    // The token typed into the body. Spaces would break parsing, so the
    // first name alone is the handle; ties resolve to whoever is picked in
    // the list, since the mention row stores the id, not the text.
    handle: (u.name ?? "").trim().split(/\s+/)[0],
  }));
}

/* -------------------------------------------------------------------------- */
/* Writes                                                                      */
/* -------------------------------------------------------------------------- */

export async function postMessage(input: {
  channelSlug: string;
  body: string;
  replyToId?: string | null;
  mentionUserIds?: string[];
  attachments?: NewAttachment[];
}): Promise<{ ok: true } | { ok: false; error: string }> {
  const user = await requireUser();

  const body = input.body.trim();
  const attachments = (input.attachments ?? []).slice(0, MAX_ATTACHMENTS);

  // A message must carry something. An empty body with no files is a stray
  // Enter keypress, not a post.
  if (!body && attachments.length === 0) return { ok: false, error: "Write something first." };
  if (body.length > MAX_BODY) return { ok: false, error: `Keep it under ${MAX_BODY} characters.` };

  const channel = await prisma.communityChannel.findUnique({
    where: { slug: input.channelSlug },
  });
  if (!channel || channel.isArchived) return { ok: false, error: "Channel not found." };
  if (channel.isReadOnly && user.role !== "ADMIN") {
    return { ok: false, error: "This channel is read-only." };
  }

  const aMinuteAgo = new Date(Date.now() - 60_000);
  const recent = await prisma.communityMessage.count({
    where: { authorId: user.id, createdAt: { gte: aMinuteAgo } },
  });
  if (recent >= RATE_LIMIT_PER_MINUTE) {
    return { ok: false, error: "You're posting very fast — wait a moment." };
  }

  // A reply must point at a message in the same channel, or a crafted id could
  // quote a message from a channel the reader cannot see.
  let replyToId: string | null = null;
  if (input.replyToId) {
    const parent = await prisma.communityMessage.findUnique({
      where: { id: input.replyToId },
      select: { id: true, channelId: true },
    });
    if (parent?.channelId === channel.id) replyToId = parent.id;
  }

  // Mentions are trusted only as far as they resolve to real users; the ids
  // arrive from the client and are otherwise unvalidated.
  const mentionIds = [...new Set(input.mentionUserIds ?? [])].slice(0, 20);
  const validMentions = mentionIds.length
    ? await prisma.user.findMany({
        where: { id: { in: mentionIds } },
        select: { id: true },
      })
    : [];

  await prisma.communityMessage.create({
    data: {
      channelId: channel.id,
      authorId: user.id,
      body,
      replyToId,
      attachments: { create: attachments },
      mentions: { create: validMentions.map((m) => ({ userId: m.id })) },
    },
  });

  revalidatePath(`/community/${channel.slug}`);
  return { ok: true };
}

/** Soft-delete. Authors may remove their own; admins may remove any. */
export async function deleteMessage(
  messageId: string
): Promise<{ ok: true } | { ok: false; error: string }> {
  const user = await requireUser();

  const message = await prisma.communityMessage.findUnique({
    where: { id: messageId },
    select: { id: true, authorId: true, deletedAt: true, channel: { select: { slug: true } } },
  });
  if (!message) return { ok: false, error: "Message not found." };
  if (message.deletedAt) return { ok: true };
  if (message.authorId !== user.id && user.role !== "ADMIN") {
    return { ok: false, error: "You can only delete your own messages." };
  }

  await prisma.communityMessage.update({
    where: { id: message.id },
    data: { deletedAt: new Date(), deletedById: user.id },
  });

  revalidatePath(`/community/${message.channel.slug}`);
  return { ok: true };
}

/**
 * Edit a message's text.
 *
 * Authors only — an admin may remove a message but must never be able to
 * rewrite what someone else said and leave it under their name.
 *
 * Attachments and mentions are untouched: this edits the words, and silently
 * re-resolving mentions would let an edit tag people who were never in the
 * original conversation.
 */
export async function editMessage(
  messageId: string,
  body: string
): Promise<{ ok: true } | { ok: false; error: string }> {
  const user = await requireUser();

  const trimmed = body.trim();
  if (!trimmed) return { ok: false, error: "A message cannot be emptied — delete it instead." };
  if (trimmed.length > MAX_BODY) return { ok: false, error: `Keep it under ${MAX_BODY} characters.` };

  const message = await prisma.communityMessage.findUnique({
    where: { id: messageId },
    select: { id: true, authorId: true, deletedAt: true, channel: { select: { slug: true } } },
  });
  if (!message || message.deletedAt) return { ok: false, error: "Message not found." };
  if (message.authorId !== user.id) {
    return { ok: false, error: "You can only edit your own messages." };
  }

  await prisma.communityMessage.update({
    where: { id: message.id },
    data: { body: trimmed, editedAt: new Date() },
  });

  revalidatePath(`/community/${message.channel.slug}`);
  return { ok: true };
}

/**
 * Add or remove one emoji reaction, whichever the student is not currently in.
 *
 * The emoji is checked against the fixed set rather than trusted: the column
 * would otherwise accept any string the client cared to send, which is how a
 * reaction row becomes a place to store arbitrary text.
 */
export async function toggleReaction(
  messageId: string,
  emoji: string
): Promise<{ ok: true; reacted: boolean } | { ok: false; error: string }> {
  const user = await requireUser();

  if (!(REACTIONS as readonly string[]).includes(emoji)) {
    return { ok: false, error: "Unsupported reaction." };
  }

  const message = await prisma.communityMessage.findUnique({
    where: { id: messageId },
    select: { id: true, deletedAt: true, channel: { select: { slug: true } } },
  });
  if (!message || message.deletedAt) return { ok: false, error: "Message not found." };

  const existing = await prisma.communityReaction.findUnique({
    where: { messageId_userId_emoji: { messageId, userId: user.id, emoji } },
    select: { id: true },
  });

  if (existing) {
    await prisma.communityReaction.delete({ where: { id: existing.id } });
    return { ok: true, reacted: false };
  }

  await prisma.communityReaction.create({ data: { messageId, userId: user.id, emoji } });
  return { ok: true, reacted: true };
}

/** Move this student's read marker to now. */
export async function markChannelRead(channelSlug: string): Promise<void> {
  const user = await requireUser();
  const channel = await prisma.communityChannel.findUnique({
    where: { slug: channelSlug },
    select: { id: true },
  });
  if (!channel) return;

  await prisma.communityRead.upsert({
    where: { userId_channelId: { userId: user.id, channelId: channel.id } },
    create: { userId: user.id, channelId: channel.id, lastReadAt: new Date() },
    update: { lastReadAt: new Date() },
  });
}
