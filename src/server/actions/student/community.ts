"use server";

import { revalidatePath } from "next/cache";
import type { Prisma } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { runInBackground } from "@/lib/background";
import { validateAttachments } from "@/lib/community/attachments";
import { notifyForMessage, notifyReaction, createNotifications } from "@/lib/community/notify";
import {
  activeRestriction,
  blockSets,
  displayName,
  excerpt,
  isActiveNow,
  mentorIds,
  messageUrl,
  restrictionMessage,
} from "@/lib/community/server";
import {
  MAX_BODY,
  MAX_SUBJECT,
  MAX_TITLE,
  PAGE_SIZE,
  POLL_MAX_OPTIONS,
  POLL_MIN_OPTIONS,
  RATE_LIMIT_PER_MINUTE,
  REACTIONS,
  STUDENT_KINDS,
  type CategoryView,
  type ChannelView,
  type CommunityMessageView,
  type MemberProfileView,
  type MessageKind,
  type ReactionSummary,
} from "@/lib/community/types";

/**
 * Community — channels, posts, threads, polls and everything students do in
 * them.
 *
 * Message bodies are stored and returned as **plain text, never HTML**. The
 * client renders a small markdown subset by building React elements, so a
 * student cannot post markup that runs in another student's browser. Nothing
 * in this file builds an HTML string.
 *
 * Every permission is checked here, server-side. The client hides buttons a
 * student cannot use, but a hidden button is a hint, not a rule.
 */

type Result<T = object> = ({ ok: true } & T) | { ok: false; error: string };

/* -------------------------------------------------------------------------- */
/* Channels                                                                    */
/* -------------------------------------------------------------------------- */

/**
 * Every live channel, grouped by category, with this student's unread and
 * mention counts. Two grouped queries for all channels together — not two per
 * channel, which is what the first version did.
 */
export async function listCategories(): Promise<CategoryView[]> {
  const user = await requireUser();

  const [categories, channels, reads, account] = await Promise.all([
    prisma.communityCategory.findMany({ orderBy: [{ order: "asc" }, { name: "asc" }] }),
    prisma.communityChannel.findMany({
      where: { isArchived: false },
      orderBy: [{ order: "asc" }, { name: "asc" }],
    }),
    prisma.communityRead.findMany({ where: { userId: user.id } }),
    prisma.user.findUnique({ where: { id: user.id }, select: { createdAt: true } }),
  ]);
  const joined = account?.createdAt ?? new Date(0);

  const [unreadRows, mentionRows] = await Promise.all([
    prisma.$queryRaw<{ channelId: string; n: bigint }[]>`
      SELECT m."channelId", count(*) AS n
      FROM "CommunityMessage" m
      LEFT JOIN "CommunityRead" r ON r."channelId" = m."channelId" AND r."userId" = ${user.id}
      WHERE m."deletedAt" IS NULL AND m."threadRootId" IS NULL AND m."authorId" <> ${user.id}
        AND m."createdAt" > COALESCE(r."lastReadAt", ${joined})
      GROUP BY m."channelId"`,
    prisma.$queryRaw<{ channelId: string; n: bigint }[]>`
      SELECT m."channelId", count(*) AS n
      FROM "CommunityMention" x
      JOIN "CommunityMessage" m ON m."id" = x."messageId"
      LEFT JOIN "CommunityRead" r ON r."channelId" = m."channelId" AND r."userId" = ${user.id}
      WHERE x."userId" = ${user.id} AND m."deletedAt" IS NULL
        AND m."createdAt" > COALESCE(r."lastReadAt", ${joined})
      GROUP BY m."channelId"`,
  ]);
  const unread = new Map(unreadRows.map((r) => [r.channelId, Number(r.n)]));
  const mentions = new Map(mentionRows.map((r) => [r.channelId, Number(r.n)]));
  const readBy = new Map(reads.map((r) => [r.channelId, r]));

  const views: ChannelView[] = channels.map((c) => {
    const muted = Boolean(readBy.get(c.id)?.mutedAt);
    return {
      id: c.id,
      slug: c.slug,
      name: c.name,
      description: c.description,
      icon: c.icon,
      isReadOnly: c.isReadOnly,
      slowModeSeconds: c.slowModeSeconds,
      categoryId: c.categoryId,
      unread: muted ? 0 : unread.get(c.id) ?? 0,
      mentionsUnread: mentions.get(c.id) ?? 0,
      muted,
    };
  });

  const grouped: CategoryView[] = categories.map((cat) => ({
    id: cat.id,
    name: cat.name,
    channels: views.filter((v) => v.categoryId === cat.id),
  }));
  const loose = views.filter((v) => !v.categoryId || !categories.some((c) => c.id === v.categoryId));
  if (loose.length) grouped.push({ id: null, name: "Other", channels: loose });
  return grouped.filter((g) => g.channels.length > 0);
}

/** Flat list, kept for callers that only need channels. */
export async function listChannels(): Promise<ChannelView[]> {
  return (await listCategories()).flatMap((c) => c.channels);
}

/* -------------------------------------------------------------------------- */
/* Messages — reading                                                          */
/* -------------------------------------------------------------------------- */

function includeFor(userId: string) {
  return {
    author: { select: { id: true, name: true, image: true, role: true } },
    channel: { select: { slug: true } },
    attachments: true,
    mentions: { where: { userId }, select: { id: true } },
    reactions: { select: { emoji: true, userId: true } },
    replyTo: {
      select: { id: true, body: true, title: true, deletedAt: true, threadRootId: true, author: { select: { name: true, role: true } } },
    },
    pollOptions: {
      orderBy: { order: "asc" as const },
      select: { id: true, label: true, _count: { select: { votes: true } } },
    },
    bookmarks: { where: { userId }, select: { id: true } },
    follows: { where: { userId }, select: { state: true } },
  } satisfies Prisma.CommunityMessageInclude;
}

type Row = Prisma.CommunityMessageGetPayload<{ include: ReturnType<typeof includeFor> }>;

/** Turn rows into views. Batches the lookups every row needs. */
async function toViews(
  rows: Row[],
  viewer: { id: string; role: string },
  opts: { acceptedAnswerId?: string | null; questionOwnerId?: string | null } = {},
): Promise<CommunityMessageView[]> {
  if (rows.length === 0) return [];
  const isAdmin = viewer.role === "ADMIN";
  const pollIds = rows.filter((r) => r.kind === "POLL").map((r) => r.id);
  const [mentors, blocks, myVotes] = await Promise.all([
    mentorIds([...new Set(rows.map((r) => r.authorId))]),
    blockSets(viewer.id),
    pollIds.length
      ? prisma.communityPollVote.findMany({
          where: { messageId: { in: pollIds }, userId: viewer.id },
          select: { messageId: true, optionId: true },
        })
      : Promise.resolve([]),
  ]);
  const voteBy = new Map(myVotes.map((v) => [v.messageId, v.optionId]));

  return rows.map((m): CommunityMessageView => {
    const deleted = m.deletedAt != null;
    const byEmoji = new Map<string, ReactionSummary>();
    for (const r of m.reactions) {
      const e = byEmoji.get(r.emoji) ?? { emoji: r.emoji, count: 0, mine: false };
      e.count += 1;
      if (r.userId === viewer.id) e.mine = true;
      byEmoji.set(r.emoji, e);
    }
    const totalVotes = m.pollOptions.reduce((n, o) => n + o._count.votes, 0);
    const isMine = m.authorId === viewer.id;
    return {
      id: m.id,
      channelSlug: m.channel.slug,
      kind: m.kind as MessageKind,
      title: deleted ? null : m.title,
      subject: deleted ? null : m.subject,
      linkUrl: deleted ? null : m.linkUrl,
      body: deleted ? "" : m.body,
      createdAt: m.createdAt.toISOString(),
      editedAt: m.editedAt?.toISOString() ?? null,
      deleted,
      author: {
        id: m.author.id,
        name: displayName(m.author.name, m.author.role),
        image: m.author.image,
        isAdmin: m.author.role === "ADMIN",
        isMentor: mentors.has(m.author.id),
        isMe: isMine,
      },
      authorBlocked: blocks.iBlocked.has(m.authorId),
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
            authorName: displayName(m.replyTo.author.name, m.replyTo.author.role),
            excerpt: m.replyTo.deletedAt ? "message deleted" : excerpt(m.replyTo.title ?? m.replyTo.body, 140) || "attachment",
            deleted: m.replyTo.deletedAt != null,
            threadRootId: m.replyTo.threadRootId,
          }
        : null,
      threadRootId: m.threadRootId,
      replyCount: m.replyCount,
      lastReplyAt: m.lastReplyAt?.toISOString() ?? null,
      acceptedAnswerId: m.acceptedAnswerId,
      isAcceptedAnswer: Boolean(opts.acceptedAnswerId && opts.acceptedAnswerId === m.id),
      pinned: m.pinnedAt != null,
      bookmarked: m.bookmarks.length > 0,
      following: m.follows[0]?.state ?? null,
      poll:
        m.kind === "POLL" && !deleted
          ? {
              options: m.pollOptions.map((o) => ({ id: o.id, label: o.label, votes: o._count.votes })),
              totalVotes,
              myVote: voteBy.get(m.id) ?? null,
              closed: m.pollClosedAt != null,
            }
          : null,
      reactions: deleted ? [] : [...byEmoji.values()],
      canEdit: !deleted && isMine,
      canDelete: !deleted && (isMine || isAdmin),
      canPin: !deleted && isAdmin && !m.threadRootId,
      canAccept:
        !deleted &&
        Boolean(m.threadRootId) &&
        (isAdmin || (opts.questionOwnerId != null && opts.questionOwnerId === viewer.id)),
    };
  });
}

async function viewer() {
  const user = await requireUser();
  return { id: user.id, role: user.role as string };
}

/**
 * A page of the main stream (thread replies live in their thread), oldest
 * first. `before` pages back through history; `around` returns the page that
 * contains one message, for "jump to message" from a notification or search.
 */
export async function listMessages(
  channelSlug: string,
  opts: { before?: string; around?: string } | string = {},
): Promise<{ messages: CommunityMessageView[]; hasMore: boolean }> {
  const me = await viewer();
  const o = typeof opts === "string" ? { before: opts } : opts;

  const channel = await prisma.communityChannel.findUnique({ where: { slug: channelSlug } });
  if (!channel) return { messages: [], hasMore: false };

  let createdBefore: Date | null = null;
  if (o.before) {
    const c = await prisma.communityMessage.findUnique({ where: { id: o.before }, select: { createdAt: true } });
    createdBefore = c?.createdAt ?? null;
  }
  if (o.around) {
    const target = await prisma.communityMessage.findUnique({
      where: { id: o.around },
      select: { createdAt: true, channelId: true, threadRootId: true },
    });
    if (target && target.channelId === channel.id && !target.threadRootId) {
      // Everything from the target to now, plus a little context above it.
      const newer = await prisma.communityMessage.count({
        where: { channelId: channel.id, threadRootId: null, createdAt: { gte: target.createdAt } },
      });
      const take = Math.min(Math.max(newer + 10, PAGE_SIZE), 300);
      const rows = await prisma.communityMessage.findMany({
        where: { channelId: channel.id, threadRootId: null },
        orderBy: { createdAt: "desc" },
        take: take + 1,
        include: includeFor(me.id),
      });
      const hasMore = rows.length > take;
      return { messages: await toViews(rows.slice(0, take).reverse(), me), hasMore };
    }
  }

  const rows = await prisma.communityMessage.findMany({
    where: {
      channelId: channel.id,
      threadRootId: null,
      ...(createdBefore ? { createdAt: { lt: createdBefore } } : {}),
    },
    orderBy: { createdAt: "desc" },
    take: PAGE_SIZE + 1,
    include: includeFor(me.id),
  });
  const hasMore = rows.length > PAGE_SIZE;
  const page = (hasMore ? rows.slice(0, PAGE_SIZE) : rows).reverse();
  return { messages: await toViews(page, me), hasMore };
}

/** Pinned posts in a channel, newest pin first. */
export async function listPinned(channelSlug: string): Promise<CommunityMessageView[]> {
  const me = await viewer();
  const rows = await prisma.communityMessage.findMany({
    where: { channel: { slug: channelSlug }, pinnedAt: { not: null }, deletedAt: null, threadRootId: null },
    orderBy: { pinnedAt: "desc" },
    take: 20,
    include: includeFor(me.id),
  });
  return toViews(rows, me);
}

/** A discussion: the root post and every reply in it. */
export async function getThread(rootId: string): Promise<{
  root: CommunityMessageView;
  replies: CommunityMessageView[];
  channel: { slug: string; name: string; isReadOnly: boolean };
} | null> {
  const me = await viewer();
  const root = await prisma.communityMessage.findUnique({
    where: { id: rootId },
    include: { ...includeFor(me.id), channel: { select: { slug: true, name: true, isReadOnly: true, isArchived: true } } },
  });
  if (!root || root.threadRootId || root.channel.isArchived) return null;
  const replies = await prisma.communityMessage.findMany({
    where: { threadRootId: rootId },
    orderBy: { createdAt: "asc" },
    take: 500,
    include: includeFor(me.id),
  });
  const opts = {
    acceptedAnswerId: root.acceptedAnswerId,
    questionOwnerId: root.kind === "QUESTION" ? root.authorId : null,
  };
  const [rootView] = await toViews([root], me, opts);
  return {
    root: rootView,
    replies: await toViews(replies, me, opts),
    channel: { slug: root.channel.slug, name: root.channel.name, isReadOnly: root.channel.isReadOnly },
  };
}

/** Where a message lives, for links that only carry its id. */
export async function locateMessage(messageId: string) {
  await requireUser();
  const m = await prisma.communityMessage.findUnique({
    where: { id: messageId },
    select: { threadRootId: true, channel: { select: { slug: true } } },
  });
  return m ? { channelSlug: m.channel.slug, threadRootId: m.threadRootId } : null;
}

/** Students matching a partial @mention. Never surfaces email addresses. */
export async function searchMembers(query: string): Promise<{ id: string; name: string; handle: string; image: string | null }[]> {
  const user = await requireUser();
  const q = query.trim();
  if (q.length < 1) return [];
  const { iBlocked, blockedMe } = await blockSets(user.id);
  const users = await prisma.user.findMany({
    where: {
      OR: [{ name: { contains: q, mode: "insensitive" } }, { username: { startsWith: q, mode: "insensitive" } }],
      NOT: { name: null },
      id: { notIn: [...iBlocked, ...blockedMe] },
    },
    select: { id: true, name: true, image: true, role: true },
    orderBy: { name: "asc" },
    take: 8,
  });
  return users.map((u) => ({
    id: u.id,
    name: displayName(u.name, u.role),
    image: u.image,
    // The token typed into the body. The mention row stores the id, so two
    // people with the same first name still resolve to whoever was picked.
    handle: (u.name ?? "").trim().split(/\s+/)[0],
  }));
}

/* -------------------------------------------------------------------------- */
/* Messages — writing                                                          */
/* -------------------------------------------------------------------------- */

function cleanUrl(raw: string | null | undefined): string | null | "invalid" {
  const v = (raw ?? "").trim();
  if (!v) return null;
  if (v.length > 500) return "invalid";
  try {
    const u = new URL(v);
    if (u.protocol !== "https:" && u.protocol !== "http:") return "invalid";
    if (u.username || u.password) return "invalid";
    return u.toString();
  } catch {
    return "invalid";
  }
}

export interface PostInput {
  channelSlug: string;
  body: string;
  kind?: MessageKind;
  title?: string | null;
  subject?: string | null;
  linkUrl?: string | null;
  pollOptions?: string[];
  replyToId?: string | null;
  threadRootId?: string | null;
  mentionUserIds?: string[];
  attachments?: unknown;
}

export async function postMessage(input: PostInput): Promise<Result<{ id: string }>> {
  const user = await requireUser();
  const isAdmin = user.role === "ADMIN";

  const restriction = await activeRestriction(user.id);
  if (restriction) return { ok: false, error: restrictionMessage(restriction.until) };

  const body = (input.body ?? "").trim();
  const inThread = Boolean(input.threadRootId);
  const kind: MessageKind = inThread ? "MESSAGE" : input.kind ?? "MESSAGE";
  if (kind === "ANNOUNCEMENT" && !isAdmin) return { ok: false, error: "Only the Scholarly team can post announcements." };
  if (!isAdmin && !STUDENT_KINDS.includes(kind)) return { ok: false, error: "That kind of post is not available." };

  const title = (input.title ?? "").trim().slice(0, MAX_TITLE) || null;
  const subject = (input.subject ?? "").trim().slice(0, MAX_SUBJECT) || null;
  const link = cleanUrl(input.linkUrl);
  if (link === "invalid") return { ok: false, error: "That link is not a valid web address." };

  const files = validateAttachments(input.attachments);
  if (!files.ok) return { ok: false, error: files.error };
  const attachments = files.attachments;

  if (body.length > MAX_BODY) return { ok: false, error: `Keep it under ${MAX_BODY} characters.` };
  if ((kind === "QUESTION" || kind === "RESOURCE" || kind === "POLL") && !title) {
    return { ok: false, error: kind === "POLL" ? "Give the poll a question." : "Give it a title." };
  }
  if (kind === "RESOURCE" && !link && attachments.length === 0) {
    return { ok: false, error: "A resource needs a link or a file." };
  }
  let pollOptions: string[] = [];
  if (kind === "POLL") {
    pollOptions = [...new Set((input.pollOptions ?? []).map((o) => o.trim().slice(0, 80)).filter(Boolean))];
    if (pollOptions.length < POLL_MIN_OPTIONS || pollOptions.length > POLL_MAX_OPTIONS) {
      return { ok: false, error: `A poll needs ${POLL_MIN_OPTIONS} to ${POLL_MAX_OPTIONS} different options.` };
    }
  }
  // A plain message must carry something. An empty body with no files is a
  // stray Enter keypress, not a post.
  if (!body && attachments.length === 0 && !title) return { ok: false, error: "Write something first." };

  const channel = await prisma.communityChannel.findUnique({ where: { slug: input.channelSlug } });
  if (!channel || channel.isArchived) return { ok: false, error: "Channel not found." };
  if (channel.isReadOnly && !isAdmin) return { ok: false, error: "Only the Scholarly team posts in this channel." };

  const now = Date.now();
  const recent = await prisma.communityMessage.count({
    where: { authorId: user.id, createdAt: { gte: new Date(now - 60_000) } },
  });
  if (recent >= RATE_LIMIT_PER_MINUTE) return { ok: false, error: "You're posting very fast — wait a moment." };
  if (channel.slowModeSeconds > 0 && !isAdmin) {
    const last = await prisma.communityMessage.findFirst({
      where: { authorId: user.id, channelId: channel.id },
      orderBy: { createdAt: "desc" },
      select: { createdAt: true },
    });
    const wait = last ? channel.slowModeSeconds * 1000 - (now - last.createdAt.getTime()) : 0;
    if (wait > 0) return { ok: false, error: `Slow mode is on here. You can post again in ${Math.ceil(wait / 1000)}s.` };
  }

  // A thread root must be a top-level post in this channel.
  let threadRootId: string | null = null;
  if (input.threadRootId) {
    const root = await prisma.communityMessage.findUnique({
      where: { id: input.threadRootId },
      select: { id: true, channelId: true, threadRootId: true, deletedAt: true },
    });
    if (!root || root.channelId !== channel.id || root.threadRootId || root.deletedAt) {
      return { ok: false, error: "That discussion is no longer available." };
    }
    threadRootId = root.id;
  }

  // A reply must point at a message in the same channel AND the same place
  // (stream or this thread), or a crafted id could quote something the reader
  // cannot see.
  let replyToId: string | null = null;
  if (input.replyToId) {
    const parent = await prisma.communityMessage.findUnique({
      where: { id: input.replyToId },
      select: { id: true, channelId: true, threadRootId: true },
    });
    if (parent && parent.channelId === channel.id) {
      const sameStream = !threadRootId && !parent.threadRootId;
      const sameThread = threadRootId && (parent.threadRootId === threadRootId || parent.id === threadRootId);
      if (sameStream || sameThread) replyToId = parent.id;
    }
  }

  // Mentions are trusted only as far as they resolve to real users.
  const mentionIds = [...new Set(input.mentionUserIds ?? [])].filter((id) => id !== user.id).slice(0, 20);
  const validMentions = mentionIds.length
    ? await prisma.user.findMany({ where: { id: { in: mentionIds } }, select: { id: true } })
    : [];

  const message = await prisma.$transaction(async (tx) => {
    const created = await tx.communityMessage.create({
      data: {
        channelId: channel.id,
        authorId: user.id,
        body,
        kind,
        title: kind === "MESSAGE" ? null : title,
        subject: kind === "QUESTION" || kind === "RESOURCE" ? subject : null,
        linkUrl: kind === "RESOURCE" ? link : null,
        replyToId,
        threadRootId,
        attachments: { create: attachments },
        mentions: { create: validMentions.map((m) => ({ userId: m.id })) },
        pollOptions: { create: pollOptions.map((label, order) => ({ label, order })) },
      },
      select: { id: true },
    });
    const rootToFollow = threadRootId ?? created.id;
    if (threadRootId) {
      await tx.communityMessage.update({
        where: { id: threadRootId },
        data: { replyCount: { increment: 1 }, lastReplyAt: new Date() },
      });
    }
    // Writing in a discussion follows it — unless the student muted it, which
    // is a choice a reply must not quietly undo.
    await tx.communityThreadFollow.upsert({
      where: { userId_rootId: { userId: user.id, rootId: rootToFollow } },
      create: { userId: user.id, rootId: rootToFollow, state: "FOLLOWING" },
      update: {},
    });
    return created;
  });

  // Notifications and emails run after the response. A failure there must not
  // make a message that was saved look like it failed.
  runInBackground("community-notify", () => notifyForMessage(message.id));
  revalidatePath(`/community/${channel.slug}`);
  return { ok: true, id: message.id };
}

/** Soft-delete. Authors may remove their own; admins may remove any. */
export async function deleteMessage(messageId: string): Promise<Result> {
  const user = await requireUser();
  const message = await prisma.communityMessage.findUnique({
    where: { id: messageId },
    select: {
      id: true,
      authorId: true,
      deletedAt: true,
      threadRootId: true,
      body: true,
      channel: { select: { slug: true, name: true, id: true } },
    },
  });
  if (!message) return { ok: false, error: "Message not found." };
  if (message.deletedAt) return { ok: true };
  const isAuthor = message.authorId === user.id;
  if (!isAuthor && user.role !== "ADMIN") return { ok: false, error: "You can only delete your own messages." };

  await prisma.$transaction(async (tx) => {
    await tx.communityMessage.update({
      where: { id: message.id },
      data: { deletedAt: new Date(), deletedById: user.id, pinnedAt: null },
    });
    if (message.threadRootId) {
      await tx.communityMessage.updateMany({
        where: { id: message.threadRootId, replyCount: { gt: 0 } },
        data: { replyCount: { decrement: 1 } },
      });
      await tx.communityMessage.updateMany({
        where: { id: message.threadRootId, acceptedAnswerId: message.id },
        data: { acceptedAnswerId: null },
      });
    }
    if (!isAuthor) {
      await tx.communityModerationLog.create({
        data: {
          actorId: user.id,
          action: "DELETE_MESSAGE",
          targetUserId: message.authorId,
          messageId: message.id,
          note: excerpt(message.body, 200),
        },
      });
    }
  });

  if (!isAuthor) {
    runInBackground("community-moderation-notice", () =>
      createNotifications([
        {
          userId: message.authorId,
          type: "MODERATION",
          actorId: null,
          messageId: message.id,
          channelId: message.channel.id,
          title: `A moderator removed one of your messages in #${message.channel.name}`,
          body: "If you think this was a mistake, reply in #feedback.",
          url: `/community/${message.channel.slug}`,
          dedupeKey: `mod-delete:${message.id}`,
        },
      ]),
    );
  }
  revalidatePath(`/community/${message.channel.slug}`);
  return { ok: true };
}

/**
 * Edit a message's text. Authors only — an admin may remove a message but must
 * never be able to rewrite what someone else said and leave it under their
 * name. Mentions and attachments are untouched.
 */
export async function editMessage(messageId: string, body: string): Promise<Result> {
  const user = await requireUser();
  const trimmed = body.trim();
  if (trimmed.length > MAX_BODY) return { ok: false, error: `Keep it under ${MAX_BODY} characters.` };

  const message = await prisma.communityMessage.findUnique({
    where: { id: messageId },
    select: {
      id: true,
      authorId: true,
      deletedAt: true,
      title: true,
      channel: { select: { slug: true } },
      _count: { select: { attachments: true } },
    },
  });
  if (!message || message.deletedAt) return { ok: false, error: "Message not found." };
  if (message.authorId !== user.id) return { ok: false, error: "You can only edit your own messages." };
  if (!trimmed && !message.title && message._count.attachments === 0) {
    return { ok: false, error: "A message cannot be emptied — delete it instead." };
  }

  await prisma.communityMessage.update({ where: { id: message.id }, data: { body: trimmed, editedAt: new Date() } });
  revalidatePath(`/community/${message.channel.slug}`);
  return { ok: true };
}

/** Add or remove one emoji reaction from the fixed set. */
export async function toggleReaction(messageId: string, emoji: string): Promise<Result<{ reacted: boolean }>> {
  const user = await requireUser();
  if (!(REACTIONS as readonly string[]).includes(emoji)) return { ok: false, error: "Unsupported reaction." };
  const restriction = await activeRestriction(user.id);
  if (restriction) return { ok: false, error: restrictionMessage(restriction.until) };

  const message = await prisma.communityMessage.findUnique({
    where: { id: messageId },
    select: { id: true, deletedAt: true, authorId: true },
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
  try {
    await prisma.communityReaction.create({ data: { messageId, userId: user.id, emoji } });
  } catch {
    // A double click raced the unique constraint; the reaction exists.
    return { ok: true, reacted: true };
  }
  runInBackground("community-reaction", () => notifyReaction(messageId, user.id, emoji));
  return { ok: true, reacted: true };
}

/** Move this student's read marker to now. */
export async function markChannelRead(channelSlug: string): Promise<void> {
  const user = await requireUser();
  const channel = await prisma.communityChannel.findUnique({ where: { slug: channelSlug }, select: { id: true } });
  if (!channel) return;
  await prisma.communityRead.upsert({
    where: { userId_channelId: { userId: user.id, channelId: channel.id } },
    create: { userId: user.id, channelId: channel.id, lastReadAt: new Date() },
    update: { lastReadAt: new Date() },
  });
}

export async function setChannelMuted(channelSlug: string, muted: boolean): Promise<Result> {
  const user = await requireUser();
  const channel = await prisma.communityChannel.findUnique({ where: { slug: channelSlug }, select: { id: true } });
  if (!channel) return { ok: false, error: "Channel not found." };
  await prisma.communityRead.upsert({
    where: { userId_channelId: { userId: user.id, channelId: channel.id } },
    create: { userId: user.id, channelId: channel.id, mutedAt: muted ? new Date() : null },
    update: { mutedAt: muted ? new Date() : null },
  });
  return { ok: true };
}

/* -------------------------------------------------------------------------- */
/* Polls, answers, pins, bookmarks, follows                                    */
/* -------------------------------------------------------------------------- */

/** One vote per student per poll; voting again moves the vote. */
export async function votePoll(messageId: string, optionId: string): Promise<Result> {
  const user = await requireUser();
  const restriction = await activeRestriction(user.id);
  if (restriction) return { ok: false, error: restrictionMessage(restriction.until) };
  const option = await prisma.communityPollOption.findUnique({
    where: { id: optionId },
    select: { messageId: true, message: { select: { kind: true, deletedAt: true, pollClosedAt: true } } },
  });
  if (!option || option.messageId !== messageId || option.message.kind !== "POLL" || option.message.deletedAt) {
    return { ok: false, error: "Poll not found." };
  }
  if (option.message.pollClosedAt) return { ok: false, error: "This poll is closed." };
  await prisma.communityPollVote.upsert({
    where: { messageId_userId: { messageId, userId: user.id } },
    create: { messageId, optionId, userId: user.id },
    update: { optionId },
  });
  return { ok: true };
}

export async function closePoll(messageId: string): Promise<Result> {
  const user = await requireUser();
  const m = await prisma.communityMessage.findUnique({ where: { id: messageId }, select: { authorId: true, kind: true } });
  if (!m || m.kind !== "POLL") return { ok: false, error: "Poll not found." };
  if (m.authorId !== user.id && user.role !== "ADMIN") return { ok: false, error: "Only the poll's author can close it." };
  await prisma.communityMessage.update({ where: { id: messageId }, data: { pollClosedAt: new Date() } });
  return { ok: true };
}

/**
 * Accept an answer to a question (or clear it with `replyId = null`). The
 * asker or an admin only, and only a reply in that question's own thread.
 */
export async function acceptAnswer(rootId: string, replyId: string | null): Promise<Result> {
  const user = await requireUser();
  const root = await prisma.communityMessage.findUnique({
    where: { id: rootId },
    select: { id: true, kind: true, authorId: true, title: true, deletedAt: true, channel: { select: { id: true, slug: true } } },
  });
  if (!root || root.kind !== "QUESTION" || root.deletedAt) return { ok: false, error: "Question not found." };
  if (root.authorId !== user.id && user.role !== "ADMIN") return { ok: false, error: "Only the person who asked can accept an answer." };

  let reply: { id: string; authorId: string } | null = null;
  if (replyId) {
    reply = await prisma.communityMessage.findFirst({
      where: { id: replyId, threadRootId: rootId, deletedAt: null },
      select: { id: true, authorId: true },
    });
    if (!reply) return { ok: false, error: "That answer is not in this discussion." };
  }
  await prisma.communityMessage.update({ where: { id: rootId }, data: { acceptedAnswerId: reply?.id ?? null } });

  if (reply && reply.authorId !== user.id) {
    const who = await prisma.user.findUnique({ where: { id: user.id }, select: { name: true, role: true } });
    const answer = reply;
    runInBackground("community-accepted", () =>
      createNotifications([
        {
          userId: answer.authorId,
          type: "ANSWER_ACCEPTED",
          actorId: user.id,
          messageId: answer.id,
          channelId: root.channel.id,
          title: `${displayName(who?.name, who?.role)} accepted your answer`,
          body: root.title ?? "Your answer was marked as the solution.",
          url: messageUrl(root.channel.slug, answer.id, rootId),
          dedupeKey: `accept:${rootId}:${answer.id}`,
        },
      ]),
    );
  }
  return { ok: true };
}

/** Pin or unpin a top-level post. Admins only. */
export async function togglePin(messageId: string): Promise<Result<{ pinned: boolean }>> {
  const user = await requireUser();
  if (user.role !== "ADMIN") return { ok: false, error: "Only moderators can pin." };
  const m = await prisma.communityMessage.findUnique({
    where: { id: messageId },
    select: { pinnedAt: true, threadRootId: true, deletedAt: true, channel: { select: { slug: true } } },
  });
  if (!m || m.deletedAt || m.threadRootId) return { ok: false, error: "Only a top-level post can be pinned." };
  const pinned = !m.pinnedAt;
  await prisma.$transaction([
    prisma.communityMessage.update({
      where: { id: messageId },
      data: pinned ? { pinnedAt: new Date(), pinnedById: user.id } : { pinnedAt: null, pinnedById: null },
    }),
    prisma.communityModerationLog.create({
      data: { actorId: user.id, action: pinned ? "PIN" : "UNPIN", messageId },
    }),
  ]);
  revalidatePath(`/community/${m.channel.slug}`);
  return { ok: true, pinned };
}

export async function toggleBookmark(messageId: string): Promise<Result<{ bookmarked: boolean }>> {
  const user = await requireUser();
  const existing = await prisma.communityBookmark.findUnique({
    where: { userId_messageId: { userId: user.id, messageId } },
    select: { id: true },
  });
  if (existing) {
    await prisma.communityBookmark.delete({ where: { id: existing.id } });
    return { ok: true, bookmarked: false };
  }
  const m = await prisma.communityMessage.findUnique({ where: { id: messageId }, select: { deletedAt: true } });
  if (!m || m.deletedAt) return { ok: false, error: "Message not found." };
  await prisma.communityBookmark.create({ data: { userId: user.id, messageId } });
  return { ok: true, bookmarked: true };
}

export async function listBookmarks(): Promise<CommunityMessageView[]> {
  const me = await viewer();
  const marks = await prisma.communityBookmark.findMany({
    where: { userId: me.id, message: { deletedAt: null } },
    orderBy: { createdAt: "desc" },
    take: 100,
    select: { message: { include: includeFor(me.id) } },
  });
  return toViews(
    marks.map((b) => b.message),
    me,
  );
}

/** Follow, mute, or clear (`null`) a discussion. */
export async function setFollow(rootId: string, state: "FOLLOWING" | "MUTED" | null): Promise<Result> {
  const user = await requireUser();
  const root = await prisma.communityMessage.findUnique({ where: { id: rootId }, select: { threadRootId: true } });
  if (!root || root.threadRootId) return { ok: false, error: "Discussion not found." };
  if (state === null) {
    await prisma.communityThreadFollow.deleteMany({ where: { userId: user.id, rootId } });
  } else {
    await prisma.communityThreadFollow.upsert({
      where: { userId_rootId: { userId: user.id, rootId } },
      create: { userId: user.id, rootId, state },
      update: { state },
    });
  }
  return { ok: true };
}

/* -------------------------------------------------------------------------- */
/* Search                                                                      */
/* -------------------------------------------------------------------------- */

export interface SearchFilters {
  q: string;
  channel?: string | null;
  author?: string | null;
  kind?: MessageKind | null;
  hasAttachments?: boolean;
  from?: string | null;
  to?: string | null;
  page?: number;
}

export async function searchMessages(f: SearchFilters): Promise<{ results: CommunityMessageView[]; hasMore: boolean }> {
  const me = await viewer();
  const q = f.q.trim().slice(0, 120);
  const { iBlocked } = await blockSets(me.id);
  const page = Math.max(0, Math.min(50, f.page ?? 0));
  const take = 25;

  const where: Prisma.CommunityMessageWhereInput = {
    deletedAt: null,
    channel: { isArchived: false, ...(f.channel ? { slug: f.channel } : {}) },
    authorId: { notIn: [...iBlocked] },
    ...(q
      ? {
          OR: [
            { body: { contains: q, mode: "insensitive" } },
            { title: { contains: q, mode: "insensitive" } },
            { subject: { contains: q, mode: "insensitive" } },
          ],
        }
      : {}),
    ...(f.kind ? { kind: f.kind } : {}),
    ...(f.hasAttachments ? { attachments: { some: {} } } : {}),
    ...(f.author ? { author: { name: { contains: f.author.trim().slice(0, 60), mode: "insensitive" } } } : {}),
  };
  const created: Prisma.DateTimeFilter = {};
  if (f.from && !Number.isNaN(Date.parse(f.from))) created.gte = new Date(f.from);
  if (f.to && !Number.isNaN(Date.parse(f.to))) created.lte = new Date(new Date(f.to).getTime() + 86_400_000);
  if (created.gte || created.lte) where.createdAt = created;

  if (!q && !f.kind && !f.hasAttachments && !f.author && !created.gte && !created.lte) {
    return { results: [], hasMore: false };
  }

  const rows = await prisma.communityMessage.findMany({
    where,
    orderBy: { createdAt: "desc" },
    skip: page * take,
    take: take + 1,
    include: includeFor(me.id),
  });
  return { results: await toViews(rows.slice(0, take), me), hasMore: rows.length > take };
}

/* -------------------------------------------------------------------------- */
/* Community home                                                              */
/* -------------------------------------------------------------------------- */

export interface CommunityHome {
  me: { name: string; image: string | null };
  announcements: CommunityMessageView[];
  trending: CommunityMessageView[];
  unanswered: CommunityMessageView[];
  resources: CommunityMessageView[];
  achievements: CommunityMessageView[];
  recent: CommunityMessageView[];
  activeMembers: { id: string; name: string; image: string | null }[];
}

/**
 * Everything on /community. Every list is drawn from real activity and is
 * simply empty when there is none — nothing is padded or invented.
 */
export async function getCommunityHome(): Promise<CommunityHome> {
  const me = await viewer();
  const weekAgo = new Date(Date.now() - 7 * 86_400_000);
  const live = { deletedAt: null, threadRootId: null, channel: { isArchived: false } } as const;

  const [account, announcements, candidates, unanswered, resourceRows, achievements, recent, presence] =
    await Promise.all([
      prisma.user.findUnique({ where: { id: me.id }, select: { name: true, image: true, role: true } }),
      prisma.communityMessage.findMany({
        where: { ...live, OR: [{ kind: "ANNOUNCEMENT" }, { channel: { slug: "announcements" } }] },
        orderBy: { createdAt: "desc" },
        take: 3,
        include: includeFor(me.id),
      }),
      prisma.communityMessage.findMany({
        where: { ...live, createdAt: { gte: new Date(Date.now() - 14 * 86_400_000) }, kind: { not: "ANNOUNCEMENT" } },
        orderBy: { createdAt: "desc" },
        take: 120,
        include: { ...includeFor(me.id), _count: { select: { reactions: true, bookmarks: true } } },
      }),
      prisma.communityMessage.findMany({
        where: { ...live, kind: "QUESTION", acceptedAnswerId: null, replyCount: 0 },
        orderBy: { createdAt: "desc" },
        take: 5,
        include: includeFor(me.id),
      }),
      prisma.communityMessage.findMany({
        where: {
          ...live,
          OR: [{ kind: "RESOURCE" }, { channel: { slug: "resources" }, attachments: { some: {} } }],
        },
        orderBy: { createdAt: "desc" },
        take: 30,
        include: { ...includeFor(me.id), _count: { select: { reactions: true, bookmarks: true } } },
      }),
      prisma.communityMessage.findMany({
        where: { ...live, kind: "ACHIEVEMENT" },
        orderBy: { createdAt: "desc" },
        take: 4,
        include: includeFor(me.id),
      }),
      prisma.communityMessage.findMany({
        where: { ...live, createdAt: { gte: weekAgo } },
        orderBy: { createdAt: "desc" },
        take: 6,
        include: includeFor(me.id),
      }),
      prisma.communityPresence.findMany({
        where: { lastActiveAt: { gte: new Date(Date.now() - 10 * 60_000) } },
        orderBy: { lastActiveAt: "desc" },
        take: 30,
        select: {
          userId: true,
          lastSeenAt: true,
          lastActiveAt: true,
          user: { select: { name: true, image: true, role: true, communityMember: { select: { showPresence: true } } } },
        },
      }),
    ]);

  // Engagement, not recency: replies weigh most because they are conversation.
  const score = (m: { replyCount: number; _count: { reactions: number; bookmarks: number } }) =>
    m.replyCount * 3 + m._count.reactions + m._count.bookmarks * 2;
  const trendingRows = candidates
    .filter((m) => score(m) >= 2)
    .sort((a, b) => score(b) - score(a))
    .slice(0, 5);
  const resources = resourceRows.sort((a, b) => score(b) - score(a)).slice(0, 4);

  const { iBlocked } = await blockSets(me.id);
  const activeMembers = presence
    .filter((p) => p.user.communityMember?.showPresence !== false && !iBlocked.has(p.userId))
    .filter((p) => isActiveNow(p, Date.now()) || Date.now() - p.lastActiveAt.getTime() < 10 * 60_000)
    .slice(0, 12)
    .map((p) => ({ id: p.userId, name: displayName(p.user.name, p.user.role), image: p.user.image }));

  const [a, t, u, r, ach, rec] = await Promise.all([
    toViews(announcements, me),
    toViews(trendingRows, me),
    toViews(unanswered, me),
    toViews(resources, me),
    toViews(achievements, me),
    toViews(recent, me),
  ]);
  return {
    me: { name: displayName(account?.name, account?.role), image: account?.image ?? null },
    announcements: a,
    trending: t,
    unanswered: u.filter((m) => !m.authorBlocked),
    resources: r.filter((m) => !m.authorBlocked),
    achievements: ach.filter((m) => !m.authorBlocked),
    recent: rec.filter((m) => !m.authorBlocked),
    activeMembers,
  };
}

/* -------------------------------------------------------------------------- */
/* Profiles                                                                    */
/* -------------------------------------------------------------------------- */

export async function getMemberProfile(userId: string): Promise<MemberProfileView | null> {
  const me = await requireUser();
  const [u, posts, accepted, presence, blocks] = await Promise.all([
    prisma.user.findUnique({
      where: { id: userId },
      select: {
        id: true,
        name: true,
        image: true,
        role: true,
        createdAt: true,
        communityMember: true,
      },
    }),
    prisma.communityMessage.count({ where: { authorId: userId, deletedAt: null } }),
    prisma.$queryRaw<{ n: bigint }[]>`
      SELECT count(*) AS n FROM "CommunityMessage" root
      JOIN "CommunityMessage" ans ON ans."id" = root."acceptedAnswerId"
      WHERE ans."authorId" = ${userId} AND ans."deletedAt" IS NULL`,
    prisma.communityPresence.findUnique({ where: { userId } }),
    blockSets(me.id),
  ]);
  if (!u) return null;
  const mentors = await mentorIds([u.id]);
  const member = u.communityMember;
  const isMe = u.id === me.id;
  const policyAllows = member?.dmPolicy !== "NOBODY" || me.role === "ADMIN";
  return {
    id: u.id,
    name: displayName(u.name, u.role),
    image: u.image,
    joined: u.createdAt.toISOString(),
    isAdmin: u.role === "ADMIN",
    isMentor: mentors.has(u.id),
    isMe,
    bio: member?.bio ?? null,
    interests: member?.interests ?? [],
    helpsWith: member?.helpsWith ?? [],
    studying: member?.studying ?? [],
    posts,
    acceptedAnswers: Number(accepted[0]?.n ?? 0),
    activeNow: member?.showPresence !== false && isActiveNow(presence),
    canMessage: !isMe && policyAllows && !blocks.iBlocked.has(u.id) && !blocks.blockedMe.has(u.id),
    blockedByMe: blocks.iBlocked.has(u.id),
  };
}

function cleanTags(v: unknown): string[] {
  if (!Array.isArray(v)) return [];
  return [...new Set(v.map((x) => String(x).trim().slice(0, 40)).filter(Boolean))].slice(0, 8);
}

export async function updateMyProfile(input: {
  bio: string;
  interests: string[];
  helpsWith: string[];
  studying: string[];
}): Promise<Result> {
  const user = await requireUser();
  const bio = (input.bio ?? "").trim().slice(0, 280) || null;
  const data = {
    bio,
    interests: cleanTags(input.interests),
    helpsWith: cleanTags(input.helpsWith),
    studying: cleanTags(input.studying),
  };
  await prisma.communityMember.upsert({ where: { userId: user.id }, create: { userId: user.id, ...data }, update: data });
  return { ok: true };
}

export interface CommunitySettings {
  emailReplies: boolean;
  emailMentions: boolean;
  emailDirect: boolean;
  emailActivity: boolean;
  emailAnnouncements: boolean;
  emailDigest: boolean;
  dmPolicy: "EVERYONE" | "NOBODY";
  showPresence: boolean;
  bio: string;
  interests: string[];
  helpsWith: string[];
  studying: string[];
  hasEmail: boolean;
}

export async function getCommunitySettings(): Promise<CommunitySettings> {
  const user = await requireUser();
  const [m, account] = await Promise.all([
    prisma.communityMember.findUnique({ where: { userId: user.id } }),
    prisma.user.findUnique({ where: { id: user.id }, select: { email: true } }),
  ]);
  return {
    emailReplies: m?.emailReplies ?? true,
    emailMentions: m?.emailMentions ?? true,
    emailDirect: m?.emailDirect ?? true,
    emailActivity: m?.emailActivity ?? false,
    emailAnnouncements: m?.emailAnnouncements ?? false,
    emailDigest: m?.emailDigest ?? false,
    dmPolicy: m?.dmPolicy ?? "EVERYONE",
    showPresence: m?.showPresence ?? true,
    bio: m?.bio ?? "",
    interests: m?.interests ?? [],
    helpsWith: m?.helpsWith ?? [],
    studying: m?.studying ?? [],
    hasEmail: Boolean(account?.email),
  };
}

export async function updateCommunitySettings(input: {
  emailReplies: boolean;
  emailMentions: boolean;
  emailDirect: boolean;
  emailActivity: boolean;
  emailAnnouncements: boolean;
  emailDigest: boolean;
  dmPolicy: "EVERYONE" | "NOBODY";
  showPresence: boolean;
}): Promise<Result> {
  const user = await requireUser();
  const data = {
    emailReplies: Boolean(input.emailReplies),
    emailMentions: Boolean(input.emailMentions),
    emailDirect: Boolean(input.emailDirect),
    emailActivity: Boolean(input.emailActivity),
    emailAnnouncements: Boolean(input.emailAnnouncements),
    emailDigest: Boolean(input.emailDigest),
    dmPolicy: input.dmPolicy === "NOBODY" ? ("NOBODY" as const) : ("EVERYONE" as const),
    showPresence: Boolean(input.showPresence),
  };
  await prisma.communityMember.upsert({ where: { userId: user.id }, create: { userId: user.id, ...data }, update: data });
  return { ok: true };
}

/* -------------------------------------------------------------------------- */
/* Safety: reports and blocks                                                  */
/* -------------------------------------------------------------------------- */

const REASONS = ["SPAM", "HARASSMENT", "INAPPROPRIATE", "MISINFORMATION", "OTHER"] as const;
type Reason = (typeof REASONS)[number];

export async function reportContent(input: {
  messageId?: string | null;
  directMessageId?: string | null;
  userId?: string | null;
  reason: Reason;
  details?: string;
}): Promise<Result> {
  const user = await requireUser();
  if (!REASONS.includes(input.reason)) return { ok: false, error: "Pick a reason." };
  const today = await prisma.communityReport.count({
    where: { reporterId: user.id, createdAt: { gte: new Date(Date.now() - 86_400_000) } },
  });
  if (today >= 20) return { ok: false, error: "You have sent a lot of reports today. The team will review them." };

  let targetUserId = input.userId ?? null;
  if (input.messageId) {
    const m = await prisma.communityMessage.findUnique({ where: { id: input.messageId }, select: { authorId: true } });
    if (!m) return { ok: false, error: "Message not found." };
    targetUserId = m.authorId;
  } else if (input.directMessageId) {
    const dm = await prisma.communityDirectMessage.findUnique({
      where: { id: input.directMessageId },
      select: { authorId: true, conversation: { select: { members: { select: { userId: true } } } } },
    });
    // Only a participant can report a private message.
    if (!dm || !dm.conversation.members.some((x) => x.userId === user.id)) return { ok: false, error: "Message not found." };
    targetUserId = dm.authorId;
  }
  if (!targetUserId || targetUserId === user.id) return { ok: false, error: "Nothing to report." };

  try {
    await prisma.communityReport.create({
      data: {
        reporterId: user.id,
        messageId: input.messageId ?? null,
        directMessageId: input.directMessageId ?? null,
        targetUserId,
        reason: input.reason,
        details: (input.details ?? "").trim().slice(0, 1000) || null,
      },
    });
  } catch {
    return { ok: true }; // already reported by this student
  }
  return { ok: true };
}

export async function blockUser(userId: string): Promise<Result> {
  const user = await requireUser();
  if (userId === user.id) return { ok: false, error: "You cannot block yourself." };
  const target = await prisma.user.findUnique({ where: { id: userId }, select: { role: true } });
  if (!target) return { ok: false, error: "User not found." };
  if (target.role === "ADMIN") return { ok: false, error: "Moderators cannot be blocked. Report a message instead." };
  await prisma.communityBlock.upsert({
    where: { blockerId_blockedId: { blockerId: user.id, blockedId: userId } },
    create: { blockerId: user.id, blockedId: userId },
    update: {},
  });
  return { ok: true };
}

export async function unblockUser(userId: string): Promise<Result> {
  const user = await requireUser();
  await prisma.communityBlock.deleteMany({ where: { blockerId: user.id, blockedId: userId } });
  return { ok: true };
}

export async function listBlocked(): Promise<{ id: string; name: string; image: string | null }[]> {
  const user = await requireUser();
  const rows = await prisma.communityBlock.findMany({
    where: { blockerId: user.id },
    orderBy: { createdAt: "desc" },
    select: { blocked: { select: { id: true, name: true, image: true } } },
  });
  return rows.map((r) => ({ id: r.blocked.id, name: displayName(r.blocked.name), image: r.blocked.image }));
}

/** Am I restricted? For the composer banner. */
export async function myRestriction(): Promise<{ until: string; reason: string } | null> {
  const user = await requireUser();
  const r = await activeRestriction(user.id);
  return r ? { until: r.until.toISOString(), reason: r.reason } : null;
}
