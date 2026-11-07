import { NextResponse } from "next/server";

import { processEmailOutbox } from "@/lib/community/email";

export const dynamic = "force-dynamic";
export const maxDuration = 60;

/**
 * Daily backstop for the community email outbox (see vercel.json). It also
 * sends the daily digests, which are scheduled for 16:00 UTC.
 *
 * Most emails never wait for this: they are processed right after the
 * notification is created, and again on every presence heartbeat. This run
 * catches anything left over — retries after a provider outage, emails that
 * were deferred while the recipient was online on a quiet day.
 *
 * Vercel sends `Authorization: Bearer $CRON_SECRET` when CRON_SECRET is set.
 * Without the secret configured the route refuses everything.
 */
export async function GET(req: Request) {
  const secret = process.env.CRON_SECRET;
  if (!secret || req.headers.get("authorization") !== `Bearer ${secret}`) {
    return NextResponse.json({ error: "unauthorised" }, { status: 401 });
  }
  const totals = { claimed: 0, sent: 0, skipped: 0, deferred: 0, failed: 0 };
  const started = Date.now();
  // Several batches, bounded by time so the function never runs out its clock.
  while (Date.now() - started < 45_000) {
    const r = await processEmailOutbox();
    for (const k of Object.keys(totals) as (keyof typeof totals)[]) totals[k] += r[k];
    if (r.claimed === 0) break;
  }
  return NextResponse.json(totals);
}
