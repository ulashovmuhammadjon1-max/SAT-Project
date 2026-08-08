import { getSettings } from "@/lib/settings";

/**
 * Meeting-link providers.
 *
 * Booking should not care how a join link comes into existence, so it calls
 * `createMeeting` and stores whatever comes back. Swapping Google Meet for
 * Calendly, or adding Zoom, means adding one object here and changing the
 * `meetingProvider` setting — no change to the booking flow.
 *
 * The default provider is `manual`, which creates no link. That keeps the whole
 * system working with **no credentials configured at all**: the booking
 * succeeds, coins move correctly, and the student sees "link to follow" instead
 * of a broken integration. Real providers activate only once their environment
 * variables are present.
 */

export interface MeetingRequest {
  bookingId: string;
  startsAt: Date;
  durationMinutes: number;
  studentName: string;
  studentEmail: string;
  title: string;
}

export interface MeetingResult {
  /** Null means "no link yet" — a valid, non-error outcome. */
  url: string | null;
  provider: string;
  externalId?: string | null;
}

export interface MeetingProvider {
  id: string;
  /** False when required credentials are absent. */
  isConfigured(): boolean;
  createMeeting(req: MeetingRequest): Promise<MeetingResult>;
  cancelMeeting(externalId: string): Promise<void>;
}

/**
 * No integration. The mentor sends a link out of band, or an admin pastes one
 * onto the booking later.
 */
const manualProvider: MeetingProvider = {
  id: "manual",
  isConfigured: () => true,
  async createMeeting() {
    return { url: null, provider: "manual", externalId: null };
  },
  async cancelMeeting() {
    /* nothing upstream to cancel */
  },
};

/**
 * A single static room (a personal Google Meet code, a Jitsi room, a Zoom PMI)
 * shared by every session. Configure with `MEETING_STATIC_URL`.
 *
 * Crude but genuinely useful for a one-mentor operation, and it needs no OAuth.
 */
const staticLinkProvider: MeetingProvider = {
  id: "static",
  isConfigured: () => Boolean(process.env.MEETING_STATIC_URL),
  async createMeeting() {
    return {
      url: process.env.MEETING_STATIC_URL ?? null,
      provider: "static",
      externalId: null,
    };
  },
  async cancelMeeting() {},
};

/**
 * Google Calendar + Meet.
 *
 * Not implemented yet, and deliberately not faked. It needs a service account
 * with domain-wide delegation, or a stored OAuth refresh token for the mentor's
 * calendar:
 *
 *   GOOGLE_CALENDAR_ID
 *   GOOGLE_SERVICE_ACCOUNT_EMAIL
 *   GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY
 *
 * Until those exist, `isConfigured()` is false and `resolveProvider` falls back
 * to manual rather than throwing at booking time — a missing integration must
 * never cost a student their booking.
 */
const googleMeetProvider: MeetingProvider = {
  id: "google_meet",
  isConfigured: () =>
    Boolean(
      process.env.GOOGLE_CALENDAR_ID &&
        process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL &&
        process.env.GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY,
    ),
  async createMeeting() {
    throw new Error("Google Meet provider is not implemented yet");
  },
  async cancelMeeting() {
    throw new Error("Google Meet provider is not implemented yet");
  },
};

const PROVIDERS: Record<string, MeetingProvider> = {
  manual: manualProvider,
  static: staticLinkProvider,
  google_meet: googleMeetProvider,
};

/** The configured provider, or manual if it is unavailable. */
export async function resolveProvider(): Promise<MeetingProvider> {
  const settings = await getSettings();
  const chosen = PROVIDERS[settings.meetingProvider];
  if (!chosen) {
    console.warn(`[meeting] unknown provider "${settings.meetingProvider}", using manual`);
    return manualProvider;
  }
  if (!chosen.isConfigured()) {
    console.warn(`[meeting] provider "${chosen.id}" is not configured, using manual`);
    return manualProvider;
  }
  return chosen;
}

/**
 * Create a meeting for a booking. Never throws.
 *
 * A booking that is paid for and recorded is more important than its join link,
 * so a provider failure degrades to no link rather than rolling the booking
 * back. The admin panel can attach one afterwards.
 */
export async function createMeetingSafely(req: MeetingRequest): Promise<MeetingResult> {
  try {
    const provider = await resolveProvider();
    return await provider.createMeeting(req);
  } catch (error) {
    console.error("[meeting] creation failed; booking keeps its slot without a link", error);
    return { url: null, provider: "manual", externalId: null };
  }
}

export function listProviders() {
  return Object.values(PROVIDERS).map((p) => ({ id: p.id, configured: p.isConfigured() }));
}
