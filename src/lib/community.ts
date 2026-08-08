import { getSettings } from "@/lib/settings";

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
 * So the honest implementation is: ask, record that they confirmed, and
 * timestamp it. `requirementsAckAt` on the booking is the audit trail.
 *
 * The shape below is deliberately provider-ish so real verification can be
 * added later without touching the booking flow: a `verify` function per
 * requirement, defaulting to attestation. Telegram is the realistic first
 * candidate, via Telegram Login + `getChatMember`.
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
      label: "Follow SATForge on Instagram",
      handle: `@${settings.instagramHandle}`,
      href: `https://instagram.com/${settings.instagramHandle}`,
      verification: "attested",
    },
    {
      id: "telegram",
      label: "Join the SATForge Telegram",
      handle: `@${settings.telegramHandle}`,
      href: `https://t.me/${settings.telegramHandle}`,
      verification: "attested",
    },
  ];
}

/**
 * Check a student's confirmation against the current requirement list.
 *
 * Today every requirement is attested, so this reduces to "did they tick all of
 * them". It exists as a seam: when a requirement gains a real `verify`, only
 * this function changes and `createBooking` keeps calling it the same way.
 */
export async function checkRequirements(
  acknowledgedIds: string[],
): Promise<{ ok: true } | { ok: false; missing: CommunityRequirement[] }> {
  const required = await getCommunityRequirements();
  const acked = new Set(acknowledgedIds);
  const missing = required.filter((r) => !acked.has(r.id));
  return missing.length === 0 ? { ok: true } : { ok: false, missing };
}
