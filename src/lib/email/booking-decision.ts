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
  return r ? `\nNote from the Scholarly team:\n${r}\n` : "";
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
    `<p style="margin:0 0 6px;font-size:12px;text-transform:uppercase;letter-spacing:0.06em;color:#8a97b1;">Note from the Scholarly team</p>` +
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
      `\nRemember to follow @scholarly_space on Instagram and join the Telegram channel — ` +
      `volunteers check this before each session.\n\n` +
      `Need to cancel? Do it from My Sessions on scholarly.space.`,
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
      `\nYou can book another time from scholarly.space/booking.`,
    html: layout(
      para(`Hi ${first},`) +
        para(`Your request for a <strong style="color:#ffffff;">${label}</strong> on ${when} was not approved.`) +
        reasonHtml(args.reason) +
        (args.refunded
          ? para(
              `Your <strong style="color:#ffffff;">${args.refunded} coin${args.refunded === 1 ? "" : "s"}</strong> ${args.refunded === 1 ? "has" : "have"} been returned to your balance.`,
            )
          : "") +
        button("https://scholarly.space/booking", "Pick another time"),
    ),
  }).catch((e) => console.error("[booking] rejection email failed", e));
}

/**
 * An approval taken back, pending a re-check.
 *
 * This is the subscription case: the community requirements are self-attested
 * at booking time (see lib/community.ts), and a volunteer checks them properly
 * before the session. When the check fails, the session is not cancelled — the
 * seat and the coins stay held and the student can still make it — so the email
 * has to be an actionable "fix this", not a refusal. Saying "cancelled" here
 * would be false and would send students off to rebook a slot they still hold.
 */
export async function sendBookingNeedsRecheck(
  args: DecisionArgs & { requirements?: { label: string; handle: string; href: string }[] },
) {
  const label = EVENT_TYPE_LABELS[args.sessionType];
  const when = args.startsAt.toUTCString();
  const first = firstNameOf(args.name);
  const reqs = args.requirements ?? [];

  await sendEmail({
    to: args.to,
    subject: `Action needed to keep your ${label}`,
    text:
      `Hi ${first},\n\n` +
      `Your ${label} on ${when} is on hold. We could not confirm the community steps ` +
      `you agreed to when booking.\n` +
      reasonText(args.reason) +
      (reqs.length
        ? `\nPlease complete these, then reply to this email so we can re-approve:\n` +
          reqs.map((r) => `  - ${r.label} (${r.handle}): ${r.href}\n`).join("")
        : "") +
      `\nYour time slot is still reserved and your coins are still held — nothing has ` +
      `been cancelled and you do not need to rebook.`,
    html: layout(
      para(`Hi ${first},`) +
        para(
          `Your <strong style="color:#ffffff;">${label}</strong> on ${when} is on hold. We could not confirm the community steps you agreed to when booking.`,
        ) +
        reasonHtml(args.reason) +
        (reqs.length
          ? `<ul style="margin:0 0 14px;padding-left:20px;color:#d6dcea;font-size:15px;line-height:1.7;">` +
            reqs
              .map(
                (r) =>
                  `<li>${r.label} — <a href="${r.href}" style="color:#608ffa;">${r.handle}</a></li>`,
              )
              .join("") +
            `</ul>`
          : "") +
        para(
          `<strong style="color:#ffffff;">Your slot is still reserved and your coins are still held.</strong> Nothing has been cancelled and you do not need to rebook — complete the steps above and reply to this email so we can re-approve.`,
        ),
    ),
  }).catch((e) => console.error("[booking] re-check email failed", e));
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
      `Your ${label} on ${when} has been cancelled by the Scholarly team. ` +
      `Sorry for the disruption.\n` +
      reasonText(args.reason) +
      (args.refunded
        ? `\nYour ${args.refunded} coin${args.refunded === 1 ? "" : "s"} ${args.refunded === 1 ? "has" : "have"} been returned to your balance.\n`
        : "") +
      `\nYou can rebook any open time from scholarly.space/booking.`,
    html: layout(
      para(`Hi ${first},`) +
        para(
          `Your <strong style="color:#ffffff;">${label}</strong> on ${when} has been cancelled by the Scholarly team. Sorry for the disruption.`,
        ) +
        reasonHtml(args.reason) +
        (args.refunded
          ? para(
              `Your <strong style="color:#ffffff;">${args.refunded} coin${args.refunded === 1 ? "" : "s"}</strong> ${args.refunded === 1 ? "has" : "have"} been returned to your balance.`,
            )
          : "") +
        button("https://scholarly.space/booking", "Book another time"),
    ),
  }).catch((e) => console.error("[booking] cancellation email failed", e));
}
