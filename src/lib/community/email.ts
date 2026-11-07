/**
 * The community email outbox processor.
 *
 * Runs server-side only, from three places: right after a notification is
 * created (in the background, so posting never waits on it), on the presence
 * heartbeat any signed-in student's browser sends, and from the daily cron.
 * Every run is safe to overlap with another:
 *
 *   1. Rows are CLAIMED with a single UPDATE … WHERE status = 'PENDING' …
 *      FOR UPDATE SKIP LOCKED, so two runs can never pick the same row.
 *   2. Each claimed row is re-checked at send time — already read in the app?
 *      message deleted? preference turned off? recipient back online? — and
 *      skipped or deferred accordingly. A notification is never lost: the
 *      in-app row exists before any of this runs.
 *   3. All of one student's due rows go out as ONE email, and a student gets
 *      at most one community email per 15 minutes, so a busy thread does not
 *      become an inbox flood (and stays inside the provider's daily quota).
 *   4. A provider failure puts the rows back with exponential backoff; after
 *      five attempts they are marked FAILED and kept for inspection.
 */
import type { CommunityEmailDelivery } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { emailConfigured, sendEmail } from "@/lib/email";
import { escapeHtml, renderCommunityEmail, type EmailItem } from "@/lib/email/community-notification";
import { excerpt, isActiveNow, prefsFor } from "@/lib/community/server";
import { wantsEmail } from "@/lib/community/notify";

const BATCH = 40;
const MAX_ATTEMPTS = 5;
const MIN_GAP_MS = 15 * 60_000;
const DEFER_ACTIVE_MS = 10 * 60_000;
/** A notification still unread and unsent after this long is not worth an email. */
const EXPIRE_MS = 3 * 24 * 60 * 60_000;
/** A row stuck in SENDING this long belonged to a run that died. */
const STALE_SENDING_MS = 10 * 60_000;

function origin(): string {
  return (process.env.NEXT_PUBLIC_APP_URL || process.env.AUTH_URL || "https://scholarly.space").replace(/\/$/, "");
}

export interface OutboxResult {
  claimed: number;
  sent: number;
  skipped: number;
  deferred: number;
  failed: number;
}

/** Is anything due? A cheap indexed probe, so callers can skip the full run. */
export async function outboxHasDue(): Promise<boolean> {
  const row = await prisma.communityEmailDelivery.findFirst({
    where: { status: "PENDING", sendAfter: { lte: new Date() } },
    select: { id: true },
  });
  return Boolean(row);
}

export async function processEmailOutbox(): Promise<OutboxResult> {
  const result: OutboxResult = { claimed: 0, sent: 0, skipped: 0, deferred: 0, failed: 0 };

  // Recover rows from a run that died between claim and update.
  await prisma.communityEmailDelivery.updateMany({
    where: { status: "SENDING", lastAttemptAt: { lt: new Date(Date.now() - STALE_SENDING_MS) } },
    data: { status: "PENDING" },
  });

  const claimed = await prisma.$queryRaw<CommunityEmailDelivery[]>`
    UPDATE "CommunityEmailDelivery" SET "status" = 'SENDING', "lastAttemptAt" = now()
    WHERE "id" IN (
      SELECT "id" FROM "CommunityEmailDelivery"
      WHERE "status" = 'PENDING' AND "sendAfter" <= now()
      ORDER BY "sendAfter" ASC
      LIMIT ${BATCH}
      FOR UPDATE SKIP LOCKED
    )
    RETURNING *`;
  result.claimed = claimed.length;
  if (claimed.length === 0) return result;

  const byUser = new Map<string, CommunityEmailDelivery[]>();
  for (const d of claimed) byUser.set(d.userId, [...(byUser.get(d.userId) ?? []), d]);
  const userIds = [...byUser.keys()];

  const [users, prefs, presence, lastSent, notes] = await Promise.all([
    prisma.user.findMany({ where: { id: { in: userIds } }, select: { id: true, name: true, email: true } }),
    prefsFor(userIds),
    prisma.communityPresence.findMany({ where: { userId: { in: userIds } } }),
    prisma.communityEmailDelivery.groupBy({
      by: ["userId"],
      where: { userId: { in: userIds }, status: "SENT" },
      _max: { sentAt: true },
    }),
    prisma.communityNotification.findMany({
      where: { id: { in: claimed.map((c) => c.notificationId) } },
      select: {
        id: true,
        type: true,
        title: true,
        body: true,
        url: true,
        readAt: true,
        messageId: true,
        createdAt: true,
      },
    }),
  ]);
  const userBy = new Map(users.map((u) => [u.id, u]));
  const presenceBy = new Map(presence.map((p) => [p.userId, p]));
  const lastSentBy = new Map(lastSent.map((l) => [l.userId, l._max.sentAt]));
  const noteBy = new Map(notes.map((n) => [n.id, n]));

  // Message state for "was it deleted?" and for the quoted context in the email.
  const messageIds = notes.map((n) => n.messageId).filter((x): x is string => Boolean(x));
  const messages = messageIds.length
    ? await prisma.communityMessage.findMany({
        where: { id: { in: messageIds } },
        select: {
          id: true,
          deletedAt: true,
          channel: { select: { name: true } },
          replyTo: { select: { body: true, deletedAt: true } },
          threadRoot: { select: { body: true, title: true, deletedAt: true } },
        },
      })
    : [];
  const messageBy = new Map(messages.map((m) => [m.id, m]));
  const dmMessageIds = notes
    .filter((n) => n.type === "DIRECT_MESSAGE" && n.messageId)
    .map((n) => n.messageId as string);
  const dmMessages = dmMessageIds.length
    ? await prisma.communityDirectMessage.findMany({
        where: { id: { in: dmMessageIds } },
        select: { id: true, deletedAt: true },
      })
    : [];
  const dmBy = new Map(dmMessages.map((m) => [m.id, m]));

  const now = Date.now();
  const skip = async (ids: string[], reason: string) => {
    if (!ids.length) return;
    result.skipped += ids.length;
    await prisma.communityEmailDelivery.updateMany({
      where: { id: { in: ids } },
      data: { status: "SKIPPED", skipReason: reason },
    });
  };
  const defer = async (ids: string[], until: Date) => {
    if (!ids.length) return;
    result.deferred += ids.length;
    await prisma.communityEmailDelivery.updateMany({
      where: { id: { in: ids } },
      data: { status: "PENDING", sendAfter: until },
    });
  };

  for (const [userId, rows] of byUser) {
    const user = userBy.get(userId);
    const p = prefs.get(userId)!;

    if (!user?.email) {
      await skip(rows.map((r) => r.id), "NO_EMAIL");
      continue;
    }

    const sendable: { delivery: CommunityEmailDelivery; item: EmailItem }[] = [];
    const reasons = new Map<string, string[]>();
    const addSkip = (reason: string, id: string) => reasons.set(reason, [...(reasons.get(reason) ?? []), id]);

    for (const d of rows) {
      const n = noteBy.get(d.notificationId);
      if (!n) {
        addSkip("NOTIFICATION_GONE", d.id);
        continue;
      }
      if (n.readAt) {
        addSkip("READ_IN_APP", d.id);
        continue;
      }
      if (now - n.createdAt.getTime() > EXPIRE_MS) {
        addSkip("EXPIRED", d.id);
        continue;
      }
      // Same routing as at creation: a THREAD_REPLY is "about your own post"
      // only when it says so; replies and answers always are.
      const own = n.type === "THREAD_REPLY" ? n.title.includes("replied to your post") : true;
      if (!wantsEmail(n.type, p, own)) {
        addSkip("PREFERENCE_OFF", d.id);
        continue;
      }
      const msg = n.messageId ? messageBy.get(n.messageId) : undefined;
      if (n.type === "DIRECT_MESSAGE") {
        if (n.messageId && dmBy.get(n.messageId)?.deletedAt) {
          addSkip("MESSAGE_DELETED", d.id);
          continue;
        }
      } else if (n.messageId && (!msg || msg.deletedAt)) {
        addSkip("MESSAGE_DELETED", d.id);
        continue;
      }
      const parentText = msg?.replyTo
        ? msg.replyTo.deletedAt
          ? null
          : msg.replyTo.body
        : msg?.threadRoot && !msg.threadRoot.deletedAt
          ? msg.threadRoot.title || msg.threadRoot.body
          : null;
      sendable.push({
        delivery: d,
        item: {
          type: n.type,
          title: n.title,
          excerpt: n.body,
          context: parentText ? excerpt(parentText, 140) : null,
          channel: msg?.channel.name ?? null,
          url: `${origin()}${n.url}`,
        },
      });
    }
    for (const [reason, ids] of reasons) await skip(ids, reason);
    if (sendable.length === 0) continue;

    const ids = sendable.map((s) => s.delivery.id);
    // Digest rows were scheduled for the daily digest time; they are sent as
    // one summary and are not held back by presence.
    const digest = p.emailDigest;

    // Back in Scholarly: they will see it in the bell. Look again later; if it
    // is still unread once they have left, it is emailed then.
    if (!digest && isActiveNow(presenceBy.get(userId), now)) {
      await defer(ids, new Date(now + DEFER_ACTIVE_MS));
      continue;
    }
    const last = lastSentBy.get(userId);
    if (!digest && last && now - last.getTime() < MIN_GAP_MS) {
      await defer(ids, new Date(last.getTime() + MIN_GAP_MS));
      continue;
    }

    const email = renderCommunityEmail({
      name: user.name,
      items: sendable.map((s) => s.item),
      digest,
      settingsUrl: `${origin()}/community/settings`,
      inboxUrl: `${origin()}/notifications`,
    });
    const res = await sendEmail({ to: user.email, ...email });

    if (res.ok) {
      result.sent += ids.length;
      await prisma.communityEmailDelivery.updateMany({
        where: { id: { in: ids } },
        data: { status: "SENT", sentAt: new Date(), provider: res.provider, attempts: { increment: 1 }, lastError: null },
      });
      lastSentBy.set(userId, new Date());
    } else {
      // Per-row attempt counts can differ; back off on the worst of them.
      const attempts = Math.max(...sendable.map((s) => s.delivery.attempts)) + 1;
      const finalFailure = attempts >= MAX_ATTEMPTS;
      if (finalFailure) result.failed += ids.length;
      else result.deferred += ids.length;
      await prisma.communityEmailDelivery.updateMany({
        where: { id: { in: ids } },
        data: {
          status: finalFailure ? "FAILED" : "PENDING",
          attempts: { increment: 1 },
          lastError: (res.error ?? "unknown error").slice(0, 500),
          sendAfter: new Date(now + 2 ** attempts * 60_000),
        },
      });
    }
  }

  return result;
}

export { escapeHtml, emailConfigured };
