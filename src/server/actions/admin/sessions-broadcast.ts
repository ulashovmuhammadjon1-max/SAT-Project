"use server";

import { headers } from "next/headers";

import { SEAT_HOLDING_STATUSES, ACTIVE_STATUSES } from "@/lib/booking/status";
import { EMAIL_BATCH_MAX, sendEmailBatch } from "@/lib/email";
import { buildSessionsAnnouncement, type AnnouncedSession } from "@/lib/email/sessions-announcement";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import { getSettings } from "@/lib/settings";

/**
 * "New sessions are open" email to the most active students.
 *
 * Same durability design as the referral broadcast (broadcast.ts): progress
 * lives in PlatformSetting, so a batch that times out or a double-click can
 * never email anyone twice, and reopening the page resumes. The recipient
 * list is frozen when the first batch goes out, so the ranking cannot shift
 * between batches. "Start a new round" clears it for the next announcement.
 *
 * Who counts as "most active": a score over the last 90 days of SAT question
 * practice, AP practice, full tests (started and finished), IELTS submissions,
 * longest streak, and having been active in the last 30 days. Only students
 * with a verified email, and none who already hold an active booking (they
 * cannot book another).
 */

const RECIPIENTS_KEY = "sessionsAnnouncementRecipientIds";
const SENT_KEY = "sessionsAnnouncementSentUserIds";
const STARTED_KEY = "sessionsAnnouncementStartedAt";

/** Activity score a student needs to be included. ~170 students at launch. */
const MIN_SCORE = 50;
/** Never fewer than this many, if that many active students exist. */
const MIN_RECIPIENTS = 150;

async function readJson<T>(key: string, fallback: T): Promise<T> {
  const row = await prisma.platformSetting.findUnique({ where: { key }, select: { value: true } });
  return row ? (row.value as T) : fallback;
}

async function writeJson(key: string, value: unknown, description: string) {
  await prisma.platformSetting.upsert({
    where: { key },
    create: { key, value: value as never, description },
    update: { value: value as never },
  });
}

async function origin(): Promise<string> {
  const h = await headers();
  const host = h.get("x-forwarded-host") ?? h.get("host") ?? "scholarly.space";
  const proto = h.get("x-forwarded-proto") ?? "https";
  return `${proto}://${host}`;
}

async function openSessions(): Promise<AnnouncedSession[]> {
  const slots = await prisma.mentorSlot.findMany({
    where: { isBlocked: false, startsAt: { gt: new Date() }, sessionType: "ONE_ON_ONE_SAT" },
    orderBy: { startsAt: "asc" },
    select: {
      title: true,
      subject: true,
      startsAt: true,
      capacity: true,
      host: { select: { name: true } },
      _count: { select: { bookings: { where: { status: { in: SEAT_HOLDING_STATUSES } } } } },
    },
  });
  return slots
    .filter((s) => s._count.bookings < s.capacity)
    .map((s) => ({ title: s.title, subject: s.subject, startsAt: s.startsAt, hostName: s.host?.name ?? null }));
}

/** Ranked most-active students, best first. */
async function rankedStudents(): Promise<{ id: string; score: number }[]> {
  return prisma.$queryRaw<{ id: string; score: number }[]>`
    WITH since AS (SELECT now() - interval '90 days' AS t),
    qa AS (SELECT "userId", count(*)::int n FROM "QuestionAttempt", since WHERE "createdAt" >= since.t GROUP BY 1),
    ap AS (SELECT "userId", count(*)::int n FROM "ApQuestionAttempt", since WHERE "createdAt" >= since.t GROUP BY 1),
    te AS (SELECT "userId", count(*)::int started, count("submittedAt")::int submitted FROM "Attempt", since WHERE "startedAt" >= since.t GROUP BY 1),
    iw AS (SELECT "userId", count(*)::int n FROM "IeltsWritingSubmission", since WHERE "submittedAt" >= since.t GROUP BY 1),
    isp AS (SELECT "userId", count(*)::int n FROM "IeltsSpeakingSubmission", since WHERE "submittedAt" >= since.t GROUP BY 1)
    SELECT u.id,
      ( coalesce(qa.n,0) + coalesce(ap.n,0)
      + 15*coalesce(te.started,0) + 25*coalesce(te.submitted,0)
      + 10*(coalesce(iw.n,0)+coalesce(isp.n,0))
      + 3*u."longestStreak"
      + CASE WHEN u."lastActiveDate" >= now() - interval '30 days' THEN 20 ELSE 0 END )::int AS score
    FROM "User" u
    LEFT JOIN qa ON qa."userId"=u.id LEFT JOIN ap ON ap."userId"=u.id LEFT JOIN te ON te."userId"=u.id
    LEFT JOIN iw ON iw."userId"=u.id LEFT JOIN isp ON isp."userId"=u.id
    WHERE u.role = 'STUDENT' AND u.email IS NOT NULL AND trim(u.email) <> '' AND u."emailVerified" IS NOT NULL
    ORDER BY score DESC, u."lastActiveDate" DESC NULLS LAST`;
}

/** Who would receive it if a round started now. */
async function selectRecipients(): Promise<string[]> {
  const [ranked, busy] = await Promise.all([
    rankedStudents(),
    prisma.booking.findMany({ where: { status: { in: ACTIVE_STATUSES } }, select: { userId: true }, distinct: ["userId"] }),
  ]);
  const holding = new Set(busy.map((b) => b.userId));
  const eligible = ranked.filter((r) => r.score > 0 && !holding.has(r.id));
  const above = eligible.filter((r) => r.score >= MIN_SCORE);
  return (above.length >= MIN_RECIPIENTS ? above : eligible.slice(0, MIN_RECIPIENTS)).map((r) => r.id);
}

export interface SessionsBroadcastStatus {
  sessions: number;
  total: number;
  sent: number;
  remaining: number;
  startedAt: string | null;
  previewHtml?: string;
  previewSubject?: string;
  error?: string;
}

async function buildFor(users: { id: string; email: string | null; name: string | null }[], sessions: AnnouncedSession[]) {
  const [settings, site] = await Promise.all([getSettings(), origin()]);
  return users.map((u) =>
    buildSessionsAnnouncement({
      to: u.email!,
      name: u.name,
      sessions,
      instagram: `@${settings.instagramHandle}`,
      telegram: `@${settings.telegramChannel}`,
      contactEmail: settings.contactEmail,
      origin: site,
    }),
  );
}

export async function sessionsBroadcastStatus(): Promise<SessionsBroadcastStatus> {
  await requireAdmin();
  const [sessions, frozen, sentIds, startedAt] = await Promise.all([
    openSessions(),
    readJson<string[] | null>(RECIPIENTS_KEY, null),
    readJson<string[]>(SENT_KEY, []),
    readJson<string | null>(STARTED_KEY, null),
  ]);
  const ids = frozen ?? (await selectRecipients());
  const sent = new Set(sentIds);
  const [preview] = await buildFor([{ id: "preview", email: "you@example.com", name: "Student" }], sessions);
  return {
    sessions: sessions.length,
    total: ids.length,
    sent: ids.filter((id) => sent.has(id)).length,
    remaining: ids.filter((id) => !sent.has(id)).length,
    startedAt,
    previewHtml: preview.html,
    previewSubject: preview.subject,
  };
}

/** Send the next batch. Call repeatedly until `remaining` is zero. */
export async function sendSessionsBroadcastBatch(): Promise<SessionsBroadcastStatus> {
  await requireAdmin();
  const sessions = await openSessions();
  if (sessions.length === 0) {
    return { sessions: 0, total: 0, sent: 0, remaining: 0, startedAt: null, error: "There are no open sessions to announce." };
  }

  let ids = await readJson<string[] | null>(RECIPIENTS_KEY, null);
  let startedAt = await readJson<string | null>(STARTED_KEY, null);
  if (!ids) {
    ids = await selectRecipients();
    startedAt = new Date().toISOString();
    await writeJson(RECIPIENTS_KEY, ids, "Frozen recipient list for the current new-sessions announcement.");
    await writeJson(STARTED_KEY, startedAt, "When the current new-sessions announcement started sending.");
  }

  const sentIds = await readJson<string[]>(SENT_KEY, []);
  const sent = new Set(sentIds);
  const pendingIds = ids.filter((id) => !sent.has(id)).slice(0, EMAIL_BATCH_MAX);
  if (pendingIds.length === 0) {
    return { sessions: sessions.length, total: ids.length, sent: ids.length, remaining: 0, startedAt };
  }

  const users = await prisma.user.findMany({
    where: { id: { in: pendingIds }, email: { not: null } },
    select: { id: true, email: true, name: true },
  });
  const messages = await buildFor(users, sessions);
  const { results } = await sendEmailBatch(messages);
  const delivered = users.filter((_, i) => results[i]?.ok).map((u) => u.id);
  // Accounts that lost their email since the list froze are marked done too,
  // so they cannot block the round forever.
  const vanished = pendingIds.filter((id) => !users.some((u) => u.id === id));
  if (delivered.length || vanished.length) {
    await writeJson(
      SENT_KEY,
      [...sentIds, ...delivered, ...vanished],
      "User ids already emailed the current new-sessions announcement, so a retry cannot double-send.",
    );
  }

  const done = sent.size + delivered.length + vanished.length;
  const failure = results.find((r) => !r.ok);
  return {
    sessions: sessions.length,
    total: ids.length,
    sent: done,
    remaining: ids.length - done,
    startedAt,
    error:
      delivered.length === 0 && failure
        ? `Nothing sent: ${failure.error ?? "the email provider rejected the batch"}`
        : failure
          ? `${users.length - delivered.length} of ${users.length} failed: ${failure.error ?? ""}`
          : undefined,
  };
}

/** Clear the finished round so the next announcement picks fresh recipients. */
export async function resetSessionsBroadcast(): Promise<SessionsBroadcastStatus> {
  await requireAdmin();
  await prisma.platformSetting.deleteMany({ where: { key: { in: [RECIPIENTS_KEY, SENT_KEY, STARTED_KEY] } } });
  return sessionsBroadcastStatus();
}
