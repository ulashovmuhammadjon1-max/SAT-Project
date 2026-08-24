import { prisma } from "@/lib/prisma";
import { getSettings } from "@/lib/settings";
import { telegramConfigured } from "@/lib/telegram";

/**
 * Community follow/join requirements for booking a session.
 *
 * **This is an attestation, not a verification.** Neither the Instagram Graph
 * API nor the Telegram Bot API lets a third-party site confirm that an
 * arbitrary person follows an account:
 *
 *   - Instagram removed follower-relationship access for third parties. The
 *     Graph API only exposes aggregate follower counts for accounts you own,
 *     never "does user X follow account Y".
 *   - Telegram's `getChatMember` *can* answer that for a channel the bot
 *     administers, but only for a Telegram user id — which we do not have
 *     unless the student authenticates through Telegram Login first.
 *
 * **Telegram is now really verified** when `TELEGRAM_BOT_TOKEN` is configured:
 * the student signs in through the Login Widget, which gives us their Telegram
 * user id, and `getChatMember` answers whether that id is in the channel. See
 * lib/telegram.ts. With no token configured it falls back to the attestation
 * checkbox, so the site behaves exactly as it did before.
 *
 * Instagram stays attested and there is no path to changing that: the Graph API
 * exposes aggregate follower counts for accounts you own and never "does user X
 * follow account Y". A human still has to look.
 *
 * For attested requirements the honest implementation is: ask, record that they
 * confirmed, and timestamp it. `requirementsAckAt` on the booking is the audit
 * trail.
 */

export type RequirementVerification = "attested" | "verified";

export interface CommunityRequirement {
  id: string;
  label: string;
  href: string;
  handle: string;
  /** How this requirement is currently confirmed. */
  verification: RequirementVerification;
}

export async function getCommunityRequirements(): Promise<CommunityRequirement[]> {
  const settings = await getSettings();
  return [
    {
      id: "instagram",
      label: "Follow Scholarly on Instagram",
      handle: `@${settings.instagramHandle}`,
      href: `https://instagram.com/${settings.instagramHandle}`,
      verification: "attested",
    },
    {
      id: "telegram",
      label: "Join the Scholarly Telegram",
      handle: `@${settings.telegramHandle}`,
      href: `https://t.me/${settings.telegramHandle}`,
      verification: telegramConfigured() ? "verified" : "attested",
    },
  ];
}

/**
 * Check a student's confirmation against the current requirement list.
 *
 * An attested requirement passes when the student ticked it. A *verified* one
 * ignores the tick entirely and asks the database what the last real check
 * found — a checkbox cannot satisfy a requirement we can actually confirm, and
 * accepting one would put the honour system back in front of the real answer.
 */
export async function checkRequirements(
  acknowledgedIds: string[],
  userId?: string,
): Promise<{ ok: true } | { ok: false; missing: CommunityRequirement[] }> {
  const required = await getCommunityRequirements();
  const acked = new Set(acknowledgedIds);

  const verifiedState = new Map<string, boolean>();
  if (userId && required.some((r) => r.id === "telegram" && r.verification === "verified")) {
    const row = await prisma.user.findUnique({
      where: { id: userId },
      select: { telegramIsMember: true },
    });
    verifiedState.set("telegram", Boolean(row?.telegramIsMember));
  }

  const missing = required.filter((r) =>
    verifiedState.has(r.id) ? !verifiedState.get(r.id) : !acked.has(r.id),
  );
  return missing.length === 0 ? { ok: true } : { ok: false, missing };
}
