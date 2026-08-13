import type { SessionType } from "@prisma/client";

import { EVENT_TYPE_LABELS } from "@/lib/events";
import { button, layout, para, sendEmail } from "@/lib/email";

/**
 * The three emails an admin decision can produce.
 *
 * All of them carry the admin's reason when one was given, because a decision
 * a student cannot understand is worse than no email — "your session was
 * declined" with no cause reads as arbitrary, and the student has no way to
 * fix whatever went wrong before booking again.
 *
 * Times are written in UTC with the offset spelled out, matching the existing
 * confirmation email: the server cannot reliably render a student's local clock
 * in an email, and a wrong time is worse than an explicit one they convert.
 *
 * None of these throw. A mail provider being down must never roll back a
 * decision the admin already made — the booking's state is the source of truth
 * and the student can see it on My Sessions either way.
 */

interface DecisionArgs {
  to: string;
  name: string;
  startsAt: Date;
  durationMinutes: number;
  sessionType: SessionType;
  /** Student-facing prose the admin typed. Empty string when they gave none. */
  reason?: string | null;
  meetingUrl?: string | null;
  /** Coins returned to the balance, for a reject or a cancel. */
  refunded?: number;
}

const firstNameOf = (name: string) => name.trim().split(/\s+/)[0] || "there";

/** Reason block, in both the plain-text and HTML bodies, or nothing at all. */
function reasonText(reason?: string | null): string {
  const r = reason?.trim();
  return r ? `\nNote from the SATForge team:\n${r}\n` : "";
}

function reasonHtml(reason?: string | null): string {
  const r = reason?.trim();
  if (!r) return "";
  // escapeHtml, not raw interpolation: this string is typed by an admin and
  // lands in an HTML email.
  const safe = r
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\n/g, "<br/>");
  return (
    `<div style="margin:0 0 14px;padding:14px 16px;background:#0d1730;border-left:3px solid #2549ea;border-radius:8px;">` +
    `<p style="margin:0 0 6px;font-size:12px;text-transform:uppercase;letter-spacing:0.06em;color:#8a97b1;">Note from the SATForge team</p>` +
    `<p style="margin:0;font-size:15px;line-height:1.6;color:#d6dcea;">${safe}</p></div>`
  );
}

export async function sendBookingApproved(args: DecisionArgs) {
  const label = EVENT_TYPE_LABELS[args.sessionType];
  const when = args.startsAt.toUTCString();
  const first = firstNameOf(args.name);

  await sendEmail({
    to: args.to,
    subject: `Approved: ${label}`,
    text:
      `Hi ${first},\n\n` +
      `Your ${label} has been approved.\n\n` +
      `When: ${when}\n` +
      `Duration: ${args.durationMinutes} minutes\n` +
      (args.meetingUrl ? `Join: ${args.meetingUrl}\n` : `A join link will be sent before the session.\n`) +
      reasonText(args.reason) +
      `\nRemember to follow @satforge_org on Instagram and join the Telegram channel — ` +
      `volunteers check this before each session.\n\n` +
      `Need to cancel? Do it from My Sessions on satforge.org.`,
    html: layout(
      para(`Hi ${first},`) +
        para(`Your <strong style="color:#ffffff;">${label}</strong> has been approved.`) +
        para(`<strong style="color:#ffffff;">${when}</strong><br/>${args.durationMinutes} minutes`) +
        reasonHtml(args.reason) +
        (args.meetingUrl
          ? button(args.meetingUrl, "Join the session")
          : para("A join link will be sent before the session starts.")) +
        para(
          `<span style="color:#8a97b1;font-size:13px;">Volunteers check your Instagram and Telegram subscription before each session. Need to cancel? Do it from My Sessions.</span>`,
        ),
    ),
  }).catch((e) => console.error("[booking] approval email failed", e));
}

export async function sendBookingRejected(args: DecisionArgs) {
  const label = EVENT_TYPE_LABELS[args.sessionType];
  const when = args.startsAt.toUTCString();
  const first = firstNameOf(args.name);
  const refund = args.refunded
    ? `\nYour ${args.refunded} coin${args.refunded === 1 ? "" : "s"} ${args.refunded === 1 ? "has" : "have"} been returned to your balance.\n`
    : "";

  await sendEmail({
    to: args.to,
    subject: `Not approved: ${label}`,
    text:
      `Hi ${first},\n\n` +
      `Your request for a ${label} on ${when} was not approved.\n` +
      reasonText(args.reason) +
      refund +
      `\nYou can book another time from satforge.org/booking.`,
    html: layout(
      para(`Hi ${first},`) +
        para(`Your request for a <strong style="color:#ffffff;">${label}</strong> on ${when} was not approved.`) +
        reasonHtml(args.reason) +
        (args.refunded
          ? para(
              `Your <strong style="color:#ffffff;">${args.refunded} coin${args.refunded === 1 ? "" : "s"}</strong> ${args.refunded === 1 ? "has" : "have"} been returned to your balance.`,
            )
          : "") +
        button("https://satforge.org/booking", "Pick another time"),
    ),
  }).catch((e) => console.error("[booking] rejection email failed", e));
}

/** An approved session withdrawn afterwards — reads differently from a decline. */
export async function sendBookingCancelledByAdmin(args: DecisionArgs) {
  const label = EVENT_TYPE_LABELS[args.sessionType];
  const when = args.startsAt.toUTCString();
  const first = firstNameOf(args.name);

  await sendEmail({
    to: args.to,
    subject: `Cancelled: ${label}`,
    text:
      `Hi ${first},\n\n` +
      `Your ${label} on ${when} has been cancelled by the SATForge team. ` +
      `Sorry for the disruption.\n` +
      reasonText(args.reason) +
      (args.refunded
        ? `\nYour ${args.refunded} coin${args.refunded === 1 ? "" : "s"} ${args.refunded === 1 ? "has" : "have"} been returned to your balance.\n`
        : "") +
      `\nYou can rebook any open time from satforge.org/booking.`,
    html: layout(
      para(`Hi ${first},`) +
        para(
          `Your <strong style="color:#ffffff;">${label}</strong> on ${when} has been cancelled by the SATForge team. Sorry for the disruption.`,
        ) +
        reasonHtml(args.reason) +
        (args.refunded
          ? para(
              `Your <strong style="color:#ffffff;">${args.refunded} coin${args.refunded === 1 ? "" : "s"}</strong> ${args.refunded === 1 ? "has" : "have"} been returned to your balance.`,
            )
          : "") +
        button("https://satforge.org/booking", "Book another time"),
    ),
  }).catch((e) => console.error("[booking] cancellation email failed", e));
}
