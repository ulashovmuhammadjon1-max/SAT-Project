import { createHash, createHmac, timingSafeEqual } from "crypto";

import { getSettings } from "@/lib/settings";

/**
 * Real Telegram membership verification.
 *
 * Two pieces, because neither works alone:
 *
 *  1. **Telegram Login Widget** tells us *who* the student is on Telegram. The
 *     widget hands back a signed payload; the signature is an HMAC keyed on
 *     SHA256(bot token), so a payload cannot be forged without the token. This
 *     is the step that was missing before — `getChatMember` needs a numeric
 *     Telegram user id, and a username typed into a form is not one.
 *  2. **`getChatMember`** then answers whether that id is in the channel. It
 *     only works if the bot is an administrator of the channel.
 *
 * Setup, once:
 *   - Create a bot with @BotFather, put the token in `TELEGRAM_BOT_TOKEN`.
 *   - `/setdomain` in BotFather to the site's domain, or the widget refuses to
 *     render.
 *   - Add the bot as an administrator of the channel.
 *
 * With no token configured every function here degrades to "not configured" and
 * the booking flow falls back to the attestation checkbox, so the site keeps
 * working exactly as it did.
 *
 * Instagram has no equivalent. The Graph API exposes aggregate follower counts
 * for accounts you own and never "does user X follow account Y", so that
 * requirement stays attested and a human still has to look.
 */

export function telegramConfigured(): boolean {
  return Boolean(process.env.TELEGRAM_BOT_TOKEN);
}

/** The fields Telegram's Login Widget posts back. */
export interface TelegramLoginPayload {
  id: string;
  first_name?: string;
  last_name?: string;
  username?: string;
  photo_url?: string;
  auth_date: string;
  hash: string;
}

/** How stale a login payload may be before we refuse it. */
const MAX_AUTH_AGE_SECONDS = 24 * 60 * 60;

/**
 * Verify a Login Widget payload came from Telegram and is fresh.
 *
 * The check string is every field except `hash`, sorted by key, joined with
 * newlines — Telegram's documented format. Getting the sort or the separator
 * wrong produces a mismatch that looks like a forged payload, so this is
 * written to their spec exactly rather than "close enough".
 */
export function verifyLoginPayload(payload: TelegramLoginPayload): { ok: boolean; error?: string } {
  const token = process.env.TELEGRAM_BOT_TOKEN;
  if (!token) return { ok: false, error: "Telegram verification is not configured." };
  if (!payload?.hash || !payload?.id || !payload?.auth_date) {
    return { ok: false, error: "That Telegram response was incomplete." };
  }

  const { hash, ...rest } = payload;
  const checkString = Object.keys(rest)
    .filter((k) => rest[k as keyof typeof rest] !== undefined && rest[k as keyof typeof rest] !== null)
    .sort()
    .map((k) => `${k}=${rest[k as keyof typeof rest]}`)
    .join("\n");

  const secret = createHash("sha256").update(token).digest();
  const expected = createHmac("sha256", secret).update(checkString).digest("hex");

  // Constant-time, and length-guarded because timingSafeEqual throws on a
  // length mismatch rather than returning false.
  const a = Buffer.from(expected, "utf8");
  const b = Buffer.from(hash, "utf8");
  if (a.length !== b.length || !timingSafeEqual(a, b)) {
    return { ok: false, error: "That Telegram sign-in could not be verified." };
  }

  const age = Math.floor(Date.now() / 1000) - Number(payload.auth_date);
  if (!Number.isFinite(age) || age > MAX_AUTH_AGE_SECONDS) {
    return { ok: false, error: "That Telegram sign-in has expired. Try again." };
  }

  return { ok: true };
}

export type MembershipResult =
  | { status: "member" }
  | { status: "not_member" }
  | { status: "unknown"; error: string };

/**
 * Is this Telegram user in the channel?
 *
 * `left` and `kicked` are the two statuses that mean no. Everything else
 * (`creator`, `administrator`, `member`, `restricted`) means they are in it —
 * `restricted` included, since a restricted member is still a member.
 *
 * A network or API failure returns `unknown`, never `not_member`. Treating an
 * outage as "this student did not subscribe" would decline people for the
 * platform's own problem, which is worse than not knowing.
 */
export async function checkChannelMembership(telegramUserId: string): Promise<MembershipResult> {
  const token = process.env.TELEGRAM_BOT_TOKEN;
  if (!token) return { status: "unknown", error: "Telegram verification is not configured." };

  const settings = await getSettings();
  const chatId = `@${settings.telegramHandle}`;

  try {
    const res = await fetch(
      `https://api.telegram.org/bot${token}/getChatMember?chat_id=${encodeURIComponent(chatId)}&user_id=${encodeURIComponent(telegramUserId)}`,
      { cache: "no-store" },
    );
    const body = (await res.json()) as {
      ok: boolean;
      description?: string;
      result?: { status?: string };
    };

    if (!body.ok) {
      // "user not found" is Telegram's answer for someone who has never been in
      // the chat, so it is a real negative rather than an error.
      const d = (body.description ?? "").toLowerCase();
      if (d.includes("user not found") || d.includes("participant_id_invalid")) {
        return { status: "not_member" };
      }
      return { status: "unknown", error: body.description ?? "Telegram rejected the request." };
    }

    const status = body.result?.status ?? "";
    if (status === "left" || status === "kicked") return { status: "not_member" };
    if (!status) return { status: "unknown", error: "Telegram returned no membership status." };
    return { status: "member" };
  } catch (error) {
    return { status: "unknown", error: String(error).slice(0, 200) };
  }
}

/** The bot username the Login Widget needs, derived from the token's own record. */
export async function getBotUsername(): Promise<string | null> {
  const token = process.env.TELEGRAM_BOT_TOKEN;
  if (!token) return null;
  try {
    const res = await fetch(`https://api.telegram.org/bot${token}/getMe`, {
      // The bot's username never changes in practice; an hour of caching keeps
      // the booking page from calling Telegram on every render.
      next: { revalidate: 3600 },
    });
    const body = (await res.json()) as { ok: boolean; result?: { username?: string } };
    return body.ok ? (body.result?.username ?? null) : null;
  } catch {
    return null;
  }
}
