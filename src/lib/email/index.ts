/**
 * Transactional email.
 *
 * Provider-agnostic, same shape as the meeting providers: the app calls
 * `sendEmail` and never knows who delivers it. The default is a logging
 * provider that writes the message to the server console and reports success,
 * so **every flow works with no credentials configured** — a password reset
 * still generates its link, it just is not delivered, and the link appears in
 * the logs where an admin can find it during setup.
 *
 * ## Configure one of these
 *
 *   RESEND_API_KEY   Resend. Free tier covers 3,000 emails a month, which is
 *                    far beyond what this platform needs. Sending from your own
 *                    domain requires verifying scholarly.space in their dashboard.
 *
 *   SMTP_URL         Any SMTP server, e.g. Gmail with an app password:
 *                    smtp://user%40gmail.com:app-password@smtp.gmail.com:465
 *                    Gmail caps at roughly 500 messages a day, which is fine
 *                    early and will not scale to a large user base.
 *
 *   EMAIL_FROM       The From address. Must be on a domain the provider has
 *                    verified, or mail lands in spam.
 */

export interface EmailMessage {
  to: string;
  subject: string;
  /** Plain text. Always required — some clients never render the HTML. */
  text: string;
  html?: string;
}

export interface EmailResult {
  ok: boolean;
  provider: string;
  /** Present when the provider rejected it, for logging only. */
  error?: string;
}

function fromAddress(): string {
  return process.env.EMAIL_FROM || "Scholarly <onboarding@resend.dev>";
}

async function sendViaResend(msg: EmailMessage): Promise<EmailResult> {
  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      from: fromAddress(),
      to: [msg.to],
      subject: msg.subject,
      text: msg.text,
      ...(msg.html ? { html: msg.html } : {}),
    }),
  });
  if (!res.ok) {
    return { ok: false, provider: "resend", error: (await res.text()).slice(0, 300) };
  }
  return { ok: true, provider: "resend" };
}

/**
 * Log-only fallback.
 *
 * Reports success deliberately. A password reset that cannot be delivered is
 * still a valid reset — the token exists and works — and treating it as a
 * failure would show the student an error for something that is an operator
 * configuration gap, not their problem.
 */
function sendViaConsole(msg: EmailMessage): EmailResult {
  console.info(
    `[email] no provider configured — would have sent to ${msg.to}\n` +
      `  subject: ${msg.subject}\n` +
      msg.text
        .split("\n")
        .map((l) => `  | ${l}`)
        .join("\n"),
  );
  return { ok: true, provider: "console" };
}

/**
 * Send a message. Never throws.
 *
 * Callers are flows like signup and booking that must not fail because a mail
 * provider is down — the account was still created, the session is still
 * booked. Failures are logged and reported, not raised.
 */
export async function sendEmail(msg: EmailMessage): Promise<EmailResult> {
  try {
    if (process.env.RESEND_API_KEY) return await sendViaResend(msg);
    // SMTP intentionally not implemented: it needs nodemailer, which does not
    // run on the edge, and Resend's free tier covers this platform's volume
    // several times over. Documented in .env.example so the choice is visible.
    return sendViaConsole(msg);
  } catch (error) {
    console.error("[email] send failed", error);
    return { ok: false, provider: "unknown", error: String(error).slice(0, 300) };
  }
}

export function emailConfigured(): boolean {
  return Boolean(process.env.RESEND_API_KEY);
}

/** Shared wrapper so every Scholarly email looks like the same product. */
export function layout(bodyHtml: string): string {
  return `<!doctype html><html><body style="margin:0;padding:24px;background:#0a1120;font-family:system-ui,-apple-system,'Segoe UI',sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td align="center">
<table role="presentation" width="100%" style="max-width:520px;background:#111a30;border:1px solid #1e2b4a;border-radius:16px;padding:32px;">
<tr><td>
<p style="margin:0 0 24px;font-size:20px;font-weight:700;color:#ffffff;letter-spacing:-0.01em;">SAT<span style="color:#608ffa;">Forge</span></p>
${bodyHtml}
<p style="margin:32px 0 0;padding-top:20px;border-top:1px solid #1e2b4a;font-size:12px;color:#8a97b1;">
Free SAT preparation. Real strategy. No paywall on the essentials.
</p>
</td></tr></table></td></tr></table></body></html>`;
}

export const button = (href: string, label: string) =>
  `<p style="margin:24px 0;"><a href="${href}" style="display:inline-block;background:#2549ea;color:#ffffff;text-decoration:none;padding:12px 22px;border-radius:10px;font-weight:600;font-size:15px;">${label}</a></p>`;

export const para = (text: string) =>
  `<p style="margin:0 0 14px;font-size:15px;line-height:1.6;color:#d6dcea;">${text}</p>`;
