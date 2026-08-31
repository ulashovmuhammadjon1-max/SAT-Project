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
  // Default to the verified production domain, not Resend's test sender —
  // onboarding@resend.dev may only email the account owner, so with
  // EMAIL_FROM unset every student email was rejected 403 in silence.
  return process.env.EMAIL_FROM || "Scholarly <noreply@scholarly.space>";
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

/** Resend's batch endpoint takes at most 100 messages per request. */
export const EMAIL_BATCH_MAX = 100;

/**
 * Send many DIFFERENT messages in one request.
 *
 * Not a mailing list: each entry keeps its own recipient, subject and body, so
 * a broadcast stays personalised (every student gets their own invite link)
 * while costing one HTTP round trip per hundred rather than per person.
 *
 * That matters for a reason beyond speed. A 650-recipient announcement sent
 * one call at a time is 650 round trips against a provider rate limit, inside
 * a serverless function with a wall-clock timeout — it would be cut off
 * partway through, having already delivered to some unknowable prefix of the
 * list. Seven requests fit comfortably.
 *
 * Returns per-message results in the SAME ORDER as the input, so the caller
 * can record exactly who was reached. Never throws, for the same reason
 * `sendEmail` does not.
 */
export async function sendEmailBatch(
  messages: EmailMessage[],
): Promise<{ provider: string; results: EmailResult[] }> {
  if (messages.length === 0) return { provider: "none", results: [] };
  if (messages.length > EMAIL_BATCH_MAX) {
    throw new Error(`sendEmailBatch takes at most ${EMAIL_BATCH_MAX} messages`);
  }
  if (!process.env.RESEND_API_KEY) {
    // Deliberately NOT reported as success here, unlike sendEmail's console
    // fallback. A password reset with no provider is still a valid reset; a
    // broadcast with no provider is 650 people not told anything, and
    // recording them as "sent" would make it impossible to retry.
    return {
      provider: "console",
      results: messages.map(() => ({
        ok: false,
        provider: "console",
        error: "no email provider configured (RESEND_API_KEY unset)",
      })),
    };
  }
  try {
    const res = await fetch("https://api.resend.com/emails/batch", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(
        messages.map((m) => ({
          from: fromAddress(),
          to: [m.to],
          subject: m.subject,
          text: m.text,
          ...(m.html ? { html: m.html } : {}),
        })),
      ),
    });
    if (!res.ok) {
      const error = (await res.text()).slice(0, 300);
      return { provider: "resend", results: messages.map(() => ({ ok: false, provider: "resend", error })) };
    }
    const body = (await res.json()) as { data?: { id?: string }[] };
    const sent = body.data?.length ?? 0;
    // Resend returns one entry per accepted message, in order. If it somehow
    // returns fewer, treat only the ones it acknowledged as sent rather than
    // assuming the tail succeeded.
    return {
      provider: "resend",
      results: messages.map((_, i) =>
        i < sent
          ? { ok: true, provider: "resend" }
          : { ok: false, provider: "resend", error: "not acknowledged by provider" },
      ),
    };
  } catch (error) {
    return {
      provider: "resend",
      results: messages.map(() => ({ ok: false, provider: "resend", error: String(error).slice(0, 300) })),
    };
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
<p style="margin:0 0 24px;font-size:20px;font-weight:700;color:#ffffff;letter-spacing:-0.01em;">Scholarly</p>
${bodyHtml}
<p style="margin:32px 0 0;padding-top:20px;border-top:1px solid #1e2b4a;font-size:12px;color:#8a97b1;">
Free academic preparation. Real strategy. No paywall on the essentials.
</p>
</td></tr></table></td></tr></table></body></html>`;
}

export const button = (href: string, label: string) =>
  `<p style="margin:24px 0;"><a href="${href}" style="display:inline-block;background:#2549ea;color:#ffffff;text-decoration:none;padding:12px 22px;border-radius:10px;font-weight:600;font-size:15px;">${label}</a></p>`;

export const para = (text: string) =>
  `<p style="margin:0 0 14px;font-size:15px;line-height:1.6;color:#d6dcea;">${text}</p>`;
