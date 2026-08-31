import { button, layout, para, type EmailMessage } from "@/lib/email";

/**
 * The "first to 100 invites" announcement.
 *
 * Every recipient gets THEIR OWN invite link in the body. That is the whole
 * design: a broadcast telling 650 people to "go and invite friends" without
 * handing them the link they need converts far worse than one that does, and
 * the link is also the only thing that makes a referral countable — an invite
 * that does not go through a code cannot be attributed to anyone.
 *
 * THE RULES STATED HERE ARE THE RULES THE SYSTEM ENFORCES, which is the point.
 * `src/lib/referrals.ts` already decides all three:
 *
 *   - a referral is attributed only when the invited person SIGNS UP through
 *     the code, so sharing a link is not itself worth anything;
 *   - `Referral.referredUserId` is unique, so one person counts once no matter
 *     how many times a code is replayed;
 *   - self-referral is rejected outright.
 *
 * The count starts from zero on announcement day, by the owner's decision. One
 * student already had 45 lifetime referrals; carrying those over would have
 * meant announcing a race to 650 people that one of them had already almost
 * won. The email says the reset out loud rather than leaving anyone to work
 * out why their total looks different.
 */

export interface ContestInvite {
  to: string;
  name: string | null;
  /** The student's own referral code. */
  code: string;
  /** Absolute site origin. */
  origin: string;
}

export const CONTEST_TARGET = 100;
export const CONTEST_SUBJECT = `Invite ${CONTEST_TARGET} friends, win a full Desmos course from a 1580 scorer`;

export function buildContestEmail(invite: ContestInvite): EmailMessage {
  const firstName = (invite.name ?? "").trim().split(/\s+/)[0] || "there";
  // MUST match referralSummary()'s construction in lib/referrals.ts exactly.
  // The code is read at /onboarding?ref=, and nowhere else -- an earlier draft
  // of this email pointed at /register?ref=, which renders a perfectly normal
  // signup page that ignores the parameter. Every invite would have been
  // untracked and the contest would have had no winner, with nothing in any
  // log to say why.
  const link = `${invite.origin.replace(/\/$/, "")}/onboarding?ref=${invite.code}`;

  const opening =
    `We are running something new on Scholarly, and it is open to every student on the platform, ` +
    `starting today.`;

  const prize =
    `The first person to bring ${CONTEST_TARGET} friends onto Scholarly gets a full Desmos course ` +
    `— the complete graphing-calculator method for the Digital SAT Math section — taught by a 1580 scorer, free.`;

  const how =
    `Invites only count through your own invite link. Share the link below; when a friend uses it to ` +
    `create their account, they are added to your total. Sharing the link on its own does not count — ` +
    `your friend has to actually join.`;

  const reset =
    `Everyone starts from zero today, including students who have invited people before, so the race is ` +
    `open to everyone equally.`;

  const fine =
    `Each person counts once. You cannot invite yourself. The race runs until someone reaches ${CONTEST_TARGET}.`;

  const text =
    `Hi ${firstName},\n\n${opening}\n\n${prize}\n\n${how}\n\nYour invite link:\n${link}\n\n` +
    `${reset}\n\n${fine}\n\nGood luck,\nScholarly\n\n` +
    `You can track your invites any time at ${invite.origin}/invite`;

  const html = layout(
    para(`Hi ${firstName},`) +
      para(opening) +
      para(
        `<strong style="color:#ffffff;">${prize}</strong>`,
      ) +
      para(how) +
      button(link, "Copy my invite link") +
      para(
        `<span style="color:#8a97b1;font-size:13px;">Your link: <span style="color:#c7d2e5;">${link}</span></span>`,
      ) +
      para(reset) +
      para(
        `<span style="color:#8a97b1;font-size:13px;">${fine} Track your invites any time on your ` +
          `<a href="${invite.origin}/invite" style="color:#38bdf8;">invites page</a>.</span>`,
      ),
  );

  return { to: invite.to, subject: CONTEST_SUBJECT, text, html };
}
