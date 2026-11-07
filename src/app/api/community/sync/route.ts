import { NextResponse } from "next/server";

import { prisma } from "@/lib/prisma";
import { getCurrentUser } from "@/lib/session";
import { runInBackground } from "@/lib/background";
import type { SyncPayload } from "@/lib/community/types";

export const dynamic = "force-dynamic";

/**
 * The community's "has anything changed?" endpoint.
 *
 * The browser polls this instead of re-downloading messages: one round trip to
 * the database returns a handful of version stamps and counts, and the client
 * fetches real data only when a stamp moves. That is what makes fast polling
 * (a few seconds while someone is looking at a channel) cheap enough to run,
 * and why it stops entirely in a hidden tab.
 *
 * It doubles as the presence heartbeat: `beat=1` records that a signed-in tab
 * is open and visible, `active=1` that the person touched it recently. The
 * email processor reads that to decide between "they will see it in the bell"
 * and "email them". A heartbeat also nudges the email outbox, so deferred
 * emails go out without waiting for the daily cron.
 *
 * Why not WebSockets or Server-Sent Events: on Vercel both hold a function
 * open for the whole connection and bill for it, which this project's plan
 * cannot afford for every open tab. Version polling gets replies on screen in
 * about three seconds at a fraction of the cost.
 */
export async function GET(req: Request) {
  const user = await getCurrentUser();
  if (!user) return NextResponse.json({ error: "unauthorised" }, { status: 401 });

  const q = new URL(req.url).searchParams;
  const channel = q.get("c")?.slice(0, 80) || null;
  const thread = q.get("t")?.slice(0, 40) || null;
  const conversation = q.get("d")?.slice(0, 40) || null;

  if (q.get("beat") === "1") {
    const now = new Date();
    const active = q.get("active") === "1";
    await prisma.communityPresence.upsert({
      where: { userId: user.id },
      create: { userId: user.id, lastSeenAt: now, lastActiveAt: now },
      update: active ? { lastSeenAt: now, lastActiveAt: now } : { lastSeenAt: now },
    });
    runInBackground("community-email-heartbeat", async () => {
      const { outboxHasDue, processEmailOutbox } = await import("@/lib/community/email");
      if (await outboxHasDue()) await processEmailOutbox();
    });
  }

  const rows = await prisma.$queryRaw<
    {
      n_unread: bigint;
      n_latest: Date | null;
      dm_unread: bigint;
      community_v: Date | null;
      channel_v: string | null;
      thread_v: string | null;
      conv_v: string | null;
    }[]
  >`
    SELECT
      (SELECT count(*) FROM "CommunityNotification" WHERE "userId" = ${user.id} AND "readAt" IS NULL) AS n_unread,
      (SELECT max("createdAt") FROM "CommunityNotification" WHERE "userId" = ${user.id}) AS n_latest,
      (SELECT count(*) FROM "CommunityConversationMember" cm
         WHERE cm."userId" = ${user.id} AND EXISTS (
           SELECT 1 FROM "CommunityDirectMessage" dm
           WHERE dm."conversationId" = cm."conversationId" AND dm."authorId" <> ${user.id}
             AND dm."deletedAt" IS NULL AND dm."createdAt" > COALESCE(cm."lastReadAt", 'epoch'::timestamp))
      ) AS dm_unread,
      (SELECT max("createdAt") FROM "CommunityMessage" WHERE "threadRootId" IS NULL AND "deletedAt" IS NULL) AS community_v,
      CASE WHEN ${channel}::text IS NULL THEN NULL ELSE (
        SELECT concat_ws('|',
          max(GREATEST(m."createdAt", m."editedAt", m."deletedAt", m."lastReplyAt", m."pinnedAt", m."pollClosedAt")),
          count(*),
          (SELECT count(*) || ':' || COALESCE(max(r."createdAt")::text, '') FROM "CommunityReaction" r JOIN "CommunityMessage" x ON x."id" = r."messageId" JOIN "CommunityChannel" c2 ON c2."id" = x."channelId" WHERE c2."slug" = ${channel} AND x."threadRootId" IS NULL),
          (SELECT count(*) FROM "CommunityPollVote" v JOIN "CommunityMessage" x ON x."id" = v."messageId" JOIN "CommunityChannel" c3 ON c3."id" = x."channelId" WHERE c3."slug" = ${channel}))
        FROM "CommunityMessage" m JOIN "CommunityChannel" c ON c."id" = m."channelId"
        WHERE c."slug" = ${channel} AND m."threadRootId" IS NULL
      ) END AS channel_v,
      CASE WHEN ${thread}::text IS NULL THEN NULL ELSE (
        SELECT concat_ws('|',
          max(GREATEST(m."createdAt", m."editedAt", m."deletedAt", m."pinnedAt")),
          count(*),
          (SELECT count(*) || ':' || COALESCE(max(r."createdAt")::text, '') FROM "CommunityReaction" r JOIN "CommunityMessage" x ON x."id" = r."messageId" WHERE x."id" = ${thread} OR x."threadRootId" = ${thread}),
          (SELECT "acceptedAnswerId" FROM "CommunityMessage" WHERE "id" = ${thread}))
        FROM "CommunityMessage" m WHERE m."id" = ${thread} OR m."threadRootId" = ${thread}
      ) END AS thread_v,
      CASE WHEN ${conversation}::text IS NULL THEN NULL ELSE (
        SELECT concat_ws('|',
          max(GREATEST(dm."createdAt", dm."editedAt", dm."deletedAt")),
          count(*),
          (SELECT max(o."lastReadAt")::text FROM "CommunityConversationMember" o WHERE o."conversationId" = ${conversation} AND o."userId" <> ${user.id}))
        FROM "CommunityDirectMessage" dm
        WHERE dm."conversationId" = ${conversation}
          AND EXISTS (SELECT 1 FROM "CommunityConversationMember" me WHERE me."conversationId" = ${conversation} AND me."userId" = ${user.id})
      ) END AS conv_v`;

  const r = rows[0];
  const body: SyncPayload = {
    now: new Date().toISOString(),
    notificationsUnread: Number(r?.n_unread ?? 0),
    latestNotificationAt: r?.n_latest ? r.n_latest.toISOString() : null,
    dmUnread: Number(r?.dm_unread ?? 0),
    communityVersion: r?.community_v ? r.community_v.toISOString() : null,
    channelVersion: r?.channel_v ?? null,
    threadVersion: r?.thread_v ?? null,
    conversationVersion: r?.conv_v ?? null,
  };
  return NextResponse.json(body, { headers: { "Cache-Control": "no-store" } });
}
