import { prisma } from "@/lib/prisma";

/**
 * Admin-tunable platform values.
 *
 * Defaults live here, in code, so the app is fully functional against an empty
 * `PlatformSetting` table — a fresh database, a new environment, or a preview
 * deploy all behave correctly with nothing seeded. A row only exists once an
 * admin has overridden that key.
 *
 * Reads are cached per request. The values are tiny and change rarely, but the
 * booking flow reads them several times in one action and there is no reason to
 * hit Postgres each time.
 */

export interface PlatformSettings {
  /** Coins granted once, when an account is created. */
  signupBonusCoins: number;
  /** Coins paid to the referrer when a referral qualifies. */
  referralRewardCoins: number;
  /** Cost of a student's first booking. */
  bookingBaseCost: number;
  /** Added to the cost for each booking the student has already made. */
  bookingCostIncrement: number;
  /**
   * Refund coins when a booking is cancelled at least this many hours before it
   * starts. Below the threshold the coins are kept. `null` disables refunds.
   */
  bookingRefundHours: number | null;
  /** Community accounts a student must join before booking. */
  instagramHandle: string;
  telegramHandle: string;
  /** Which meeting provider to use. See lib/meeting/index.ts. */
  meetingProvider: string;
}

export const DEFAULT_SETTINGS: PlatformSettings = {
  signupBonusCoins: 10,
  referralRewardCoins: 15,
  bookingBaseCost: 10,
  bookingCostIncrement: 5,
  bookingRefundHours: 24,
  instagramHandle: "satforge_org",
  telegramHandle: "satforgeorg",
  meetingProvider: "manual",
};

export type SettingKey = keyof PlatformSettings;

/**
 * Coerce a stored JSON value to the shape of its default.
 *
 * A settings row is written by an admin form, so it can legitimately hold a
 * string where a number belongs. Rather than let that propagate into the coin
 * arithmetic, anything that does not coerce cleanly falls back to the default.
 */
function coerce<K extends SettingKey>(key: K, raw: unknown): PlatformSettings[K] {
  const fallback = DEFAULT_SETTINGS[key];

  if (key === "bookingRefundHours" && (raw === null || raw === "")) {
    return null as PlatformSettings[K];
  }
  if (typeof fallback === "number") {
    const n = typeof raw === "number" ? raw : Number(raw);
    return (Number.isFinite(n) ? n : fallback) as PlatformSettings[K];
  }
  if (typeof fallback === "string") {
    return (typeof raw === "string" && raw.trim() ? raw.trim() : fallback) as PlatformSettings[K];
  }
  // bookingRefundHours with a real value
  const n = typeof raw === "number" ? raw : Number(raw);
  return (Number.isFinite(n) ? n : fallback) as PlatformSettings[K];
}

let cache: { value: PlatformSettings; at: number } | null = null;
const TTL_MS = 30_000;

export async function getSettings(): Promise<PlatformSettings> {
  if (cache && Date.now() - cache.at < TTL_MS) return cache.value;

  let rows: { key: string; value: unknown }[] = [];
  try {
    rows = await prisma.platformSetting.findMany({ select: { key: true, value: true } });
  } catch (error) {
    // Never let a settings read take down a page — the defaults are valid.
    console.error("[settings] read failed, using defaults", error);
    return DEFAULT_SETTINGS;
  }

  const merged = { ...DEFAULT_SETTINGS };
  for (const row of rows) {
    if (row.key in DEFAULT_SETTINGS) {
      const key = row.key as SettingKey;
      // @ts-expect-error — key/value are correlated, TS can't see it here.
      merged[key] = coerce(key, row.value);
    }
  }

  cache = { value: merged, at: Date.now() };
  return merged;
}

/** Drop the cache so an admin sees their own write immediately. */
export function invalidateSettingsCache() {
  cache = null;
}

/**
 * The price of a student's next booking.
 *
 * A formula, not a table: base + (bookings already made x increment). With the
 * defaults that is 10, 15, 20, 25, ... and changing the ladder is a settings
 * edit rather than a code change.
 *
 * Cancelled bookings still count. The ladder prices the mentor's time being
 * reserved, and letting a cancel-and-rebook cycle reset the price would make
 * the increment meaningless.
 */
export function bookingCostFor(previousBookings: number, settings: PlatformSettings): number {
  const n = Math.max(0, Math.floor(previousBookings));
  return settings.bookingBaseCost + n * settings.bookingCostIncrement;
}
