"use server";

import { headers } from "next/headers";

import { EMAIL_BATCH_MAX, sendEmailBatch } from "@/lib/email";
import { buildContestEmail, CONTEST_TARGET } from "@/lib/email/referral-contest";
import { prisma } from "@/lib/prisma";
import { ensureReferralCode } from "@/lib/referrals";
import { requireAdmin } from "@/lib/session";

/**
 * One-off email broadcast to every registered student.
 *
 * WHY THIS IS BATCHED AND RESUMABLE, rather than a single "send to everyone"
 * call: 650 recipients cannot be delivered inside one serverless invocation.
 * A function that times out halfway has already sent to some prefix of the
 * list and has no record of which, so the only safe retry would be to send
 * again — and some students would get it twice.
 *
 * So progress is durable. Each call sends at most EMAIL_BATCH_MAX and records
 * exactly who was reached, in `PlatformSetting`, which already exists as a
 * JSON key/value store — no schema change, and therefore none of the
 * schema-ahead-of-database risk that has taken this site down twice.
 *
 * Only addresses the PROVIDER ACKNOWLEDGED are recorded, so a failed batch is
 * retried rather than silently skipped.
 */

const SENT_KEY = "referralContestSentUserIds";
const STARTED_KEY = "referralContestStartedAt";

async function readJson<T>(key: string, fallback: T): Promise<T> {
  const row = await prisma.platformSetting.findUnique({ where: { key } });
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

/**
 * Everyone who should receive it.
 *
 * `User.email` is non-nullable and unique in this schema, so every registered
 * account has an address and there is nothing to filter out. Ordered oldest
 * first purely so batches are deterministic across calls -- the resume logic
 * relies on the same person not moving between pages mid-send.
 */
async function recipients() {
  return prisma.user.findMany({
    select: { id: true, email: true, name: true },
    orderBy: { createdAt: "asc" },
  });
}

export interface BroadcastStatus {
  total: number;
  sent: number;
  remaining: number;
  startedAt: string | null;
  /** Rendered preview of the message the next recipient would receive. */
  previewHtml?: string;
  previewSubject?: string;
  error?: string;
}

export async function referralContestStatus(): Promise<BroadcastStatus> {
  await requireAdmin();
  const [all, sentIds, startedAt] = await Promise.all([
    recipients(),
    readJson<string[]>(SENT_KEY, []),
    readJson<string | null>(STARTED_KEY, null),
  ]);
  const sent = new Set(sentIds);
  const preview = buildContestEmail({
    to: "you@example.com",
    name: all.find((u) => !sent.has(u.id))?.name ?? "Student",
    code: "ABC2345",
    origin: await origin(),
  });
  return {
    total: all.length,
    sent: all.filter((u) => sent.has(u.id)).length,
    remaining: all.filter((u) => !sent.has(u.id)).length,
    startedAt,
    previewHtml: preview.html,
    previewSubject: preview.subject,
  };
}

/**
 * Send the next batch. Call repeatedly until `remaining` reaches zero.
 *
 * The first call stamps the contest start time, which is what makes "everyone
 * starts from zero" enforceable: the winner is decided on referrals created
 * after this instant, not on lifetime totals.
 */
export async function sendReferralContestBatch(): Promise<BroadcastStatus> {
  await requireAdmin();

  const [all, sentIds] = await Promise.all([recipients(), readJson<string[]>(SENT_KEY, [])]);
  const sent = new Set(sentIds);
  const pending = all.filter((u) => !sent.has(u.id));

  let startedAt = await readJson<string | null>(STARTED_KEY, null);
  if (!startedAt) {
    startedAt = new Date().toISOString();
    await writeJson(
      STARTED_KEY,
      startedAt,
      `Start of the "first to ${CONTEST_TARGET} invites" contest. Referrals created ` +
        "at or after this instant are the ones that count.",
    );
  }

  if (pending.length === 0) {
    return { total: all.length, sent: all.length, remaining: 0, startedAt };
  }

  const batch = pending.slice(0, EMAIL_BATCH_MAX);
  const site = await origin();

  // A code is assigned lazily on first use, so most accounts do not have one
  // yet. The link is the only countable route into the contest, so every
  // recipient needs theirs before the message is built.
  const messages = [];
  for (const user of batch) {
    const code = await ensureReferralCode(user.id);
    messages.push(buildContestEmail({ to: user.email, name: user.name, code, origin: site }));
  }

  const { results } = await sendEmailBatch(messages);
  const delivered = batch.filter((_, i) => results[i]?.ok).map((u) => u.id);
  if (delivered.length) {
    await writeJson(
      SENT_KEY,
      [...sentIds, ...delivered],
      "User ids already emailed the referral contest announcement, so a retry cannot double-send.",
    );
  }

  const failure = results.find((r) => !r.ok);
  return {
    total: all.length,
    sent: sent.size + delivered.length,
    remaining: all.length - (sent.size + delivered.length),
    startedAt,
    error:
      delivered.length === 0 && failure
        ? `Nothing sent: ${failure.error ?? "provider rejected the batch"}`
        : failure
          ? `${batch.length - delivered.length} of ${batch.length} failed: ${failure.error ?? ""}`
          : undefined,
  };
}

export interface Standing {
  name: string | null;
  qualified: number;
}

/** Live standings, counted the way the announcement promised. */
export async function referralContestStandings(): Promise<{
  startedAt: string | null;
  target: number;
  rows: Standing[];
}> {
  await requireAdmin();
  const startedAt = await readJson<string | null>(STARTED_KEY, null);
  if (!startedAt) return { startedAt: null, target: CONTEST_TARGET, rows: [] };

  const rows = await prisma.referral.groupBy({
    by: ["referrerId"],
    where: { status: "REWARDED", createdAt: { gte: new Date(startedAt) } },
    _count: { _all: true },
    orderBy: { _count: { referrerId: "desc" } },
    take: 20,
  });
  const users = await prisma.user.findMany({
    where: { id: { in: rows.map((r) => r.referrerId) } },
    select: { id: true, name: true },
  });
  const byId = new Map(users.map((u) => [u.id, u.name]));
  return {
    startedAt,
    target: CONTEST_TARGET,
    rows: rows.map((r) => ({ name: byId.get(r.referrerId) ?? null, qualified: r._count._all })),
  };
}
