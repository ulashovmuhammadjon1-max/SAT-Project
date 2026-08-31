import { button, layout, para, sendEmail } from "@/lib/email";

/**
 * The email a teacher gets when their address is attached to a class.
 *
 * This did not exist, which is the whole of the reported bug: an admin created
 * a class with a teacher's email and the teacher was never told. Nothing in
 * the product reached them, so from their side they had been given neither an
 * email nor a panel.
 *
 * The message has to cover three states, because "add the email first, the
 * teacher registers later" is a supported flow and each state needs a
 * different single action:
 *
 *   no account          -> create one, with the address pre-filled
 *   account, unverified -> confirm the address first; the student layout uses
 *                          requireVerifiedUser, so without this they sign in
 *                          and get bounced to the verify screen forever
 *   account, verified   -> straight into the Teacher Panel
 *
 * The class code is in every variant. It is what the teacher reads out to a
 * room, and it is the one thing they need that is not a link.
 */

export interface ClassInvite {
  to: string;
  teacherName: string;
  className: string;
  school: string;
  /** The six-character join code students type. */
  code: string;
  /** Absolute site origin, resolved by the caller from request headers. */
  origin: string;
  /** Present when the address has an account that is not yet verified. */
  verifyLink?: string | null;
  hasAccount: boolean;
}

export async function sendClassTeacherInvite(invite: ClassInvite) {
  const firstName = invite.teacherName.trim().split(/\s+/)[0] || "there";
  const teachUrl = `${invite.origin}/teach`;
  const registerUrl = `${invite.origin}/register?email=${encodeURIComponent(invite.to)}`;

  const opening =
    `You have been set up as the teacher for ${invite.className} at ${invite.school} on Scholarly. ` +
    `Your class join code is ${invite.code}.`;

  let action: { url: string; label: string };
  let instruction: string;

  if (!invite.hasAccount) {
    action = { url: registerUrl, label: "Create your teacher account" };
    instruction =
      "Create an account with this email address and your Teacher Panel appears automatically — " +
      "the class is already waiting for it. Use this address, not another one, or the class will not find you.";
  } else if (invite.verifyLink) {
    action = { url: invite.verifyLink, label: "Confirm my email" };
    instruction =
      "You already have an account, but this address has not been confirmed yet, and Scholarly keeps " +
      "unconfirmed accounts out of the panel. Confirm it and your Teacher Panel opens straight away. " +
      "The link works once and expires in 24 hours.";
  } else {
    action = { url: teachUrl, label: "Open my Teacher Panel" };
    instruction =
      "Your Teacher Panel is ready. You will see who has joined, set assignments, and follow each " +
      "student's progress from there.";
  }

  const students =
    `Students join by signing up and entering the code ${invite.code} — you do not have to add them one by one.`;

  await sendEmail({
    to: invite.to,
    subject: `You are the teacher for ${invite.className} on Scholarly`,
    text:
      `Hi ${firstName},\n\n${opening}\n\n${instruction}\n\n${action.url}\n\n${students}\n\n` +
      `If you were not expecting this, you can ignore this email.`,
    html: layout(
      para(`Hi ${firstName},`) +
        para(opening) +
        para(instruction) +
        button(action.url, action.label) +
        para(
          `<span style="color:#8a97b1;font-size:13px;">${students}</span>`,
        ) +
        para(
          `<span style="color:#8a97b1;font-size:13px;">If you were not expecting this, ignore this email.</span>`,
        ),
    ),
  });
}
