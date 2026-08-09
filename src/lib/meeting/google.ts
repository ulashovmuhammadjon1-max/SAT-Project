import type { MeetingProvider, MeetingRequest, MeetingResult } from "@/lib/meeting/types";

/**
 * Google Calendar + Meet.
 *
 * Creates a Calendar event with `conferenceData` requested, which is what makes
 * Google mint a Meet link. Implemented against the REST API with a JWT signed
 * by a service account, rather than pulling in `googleapis` — that package is
 * tens of megabytes for two endpoints, and the JWT is 30 lines of Web Crypto
 * that also runs on the edge.
 *
 * ## What you must configure
 *
 *   GOOGLE_SERVICE_ACCOUNT_EMAIL        …@….iam.gserviceaccount.com
 *   GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY  the PEM, newlines as \n
 *   GOOGLE_CALENDAR_ID                  usually the mentor's Gmail address
 *   GOOGLE_IMPERSONATE_EMAIL            optional; see below
 *
 * ## The part that catches everyone
 *
 * A service account has no calendar of its own, and **Meet links cannot be
 * created on a calendar the service account merely has write access to** —
 * Google refuses `conferenceData` unless the request is made *as* a real user.
 * There are two ways to satisfy that:
 *
 *   a) **Domain-wide delegation** (Google Workspace only). In the Admin
 *      console, grant the service account's client ID the scope
 *      `https://www.googleapis.com/auth/calendar`, then set
 *      GOOGLE_IMPERSONATE_EMAIL to the mentor's Workspace address. The token
 *      is then issued on that user's behalf and Meet links work.
 *
 *   b) **A plain @gmail.com account cannot do this.** Consumer Gmail has no
 *      admin console, so there is no delegation to grant. With a personal
 *      Gmail the service account can still create *events* on a shared
 *      calendar, but Google will not attach a Meet link to them.
 *
 * If delegation is not configured, `createMeeting` returns an event without a
 * link rather than throwing, and the booking still succeeds. For a personal
 * Gmail, the `static` provider with one recurring Meet room is the honest
 * choice — see MEETING_STATIC_URL.
 */

const TOKEN_URL = "https://oauth2.googleapis.com/token";
const SCOPE = "https://www.googleapis.com/auth/calendar";

function privateKey(): string {
  // Vercel stores the PEM with literal \n; a real newline works too.
  return (process.env.GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY ?? "").replace(/\\n/g, "\n");
}

function base64url(input: ArrayBuffer | string): string {
  const bytes =
    typeof input === "string" ? new TextEncoder().encode(input) : new Uint8Array(input);
  let binary = "";
  for (const b of bytes) binary += String.fromCharCode(b);
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

/** PEM → CryptoKey for RS256 signing. */
async function importKey(pem: string): Promise<CryptoKey> {
  const body = pem
    .replace(/-----BEGIN PRIVATE KEY-----/, "")
    .replace(/-----END PRIVATE KEY-----/, "")
    .replace(/\s+/g, "");
  const der = Uint8Array.from(atob(body), (c) => c.charCodeAt(0));
  return crypto.subtle.importKey(
    "pkcs8",
    der,
    { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" },
    false,
    ["sign"],
  );
}

/**
 * Exchange a self-signed JWT for an access token.
 *
 * Not cached deliberately: tokens last an hour, bookings are rare, and a
 * module-level cache would be per-serverless-instance anyway — so it would add
 * a stale-token failure mode in exchange for saving a request nobody notices.
 */
async function accessToken(): Promise<string> {
  const iss = process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL;
  const key = privateKey();
  if (!iss || !key) throw new Error("Google service account is not configured");

  const now = Math.floor(Date.now() / 1000);
  const claim: Record<string, unknown> = {
    iss,
    scope: SCOPE,
    aud: TOKEN_URL,
    iat: now,
    exp: now + 3600,
  };
  // Present only with domain-wide delegation; this is what lets Google mint
  // a Meet link, because the request then acts as a real user.
  if (process.env.GOOGLE_IMPERSONATE_EMAIL) claim.sub = process.env.GOOGLE_IMPERSONATE_EMAIL;

  const header = base64url(JSON.stringify({ alg: "RS256", typ: "JWT" }));
  const payload = base64url(JSON.stringify(claim));
  const signature = await crypto.subtle.sign(
    "RSASSA-PKCS1-v1_5",
    await importKey(key),
    new TextEncoder().encode(`${header}.${payload}`),
  );
  const assertion = `${header}.${payload}.${base64url(signature)}`;

  const res = await fetch(TOKEN_URL, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "urn:ietf:params:oauth:grant-type:jwt-bearer",
      assertion,
    }),
  });
  if (!res.ok) {
    const detail = await res.text();
    throw new Error(`Google token exchange failed (${res.status}): ${detail.slice(0, 300)}`);
  }
  return ((await res.json()) as { access_token: string }).access_token;
}

export const googleMeetProvider: MeetingProvider = {
  id: "google_meet",

  isConfigured: () =>
    Boolean(
      process.env.GOOGLE_CALENDAR_ID &&
        process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL &&
        process.env.GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY,
    ),

  async createMeeting(req: MeetingRequest): Promise<MeetingResult> {
    const token = await accessToken();
    const calendarId = encodeURIComponent(process.env.GOOGLE_CALENDAR_ID!);
    const end = new Date(req.startsAt.getTime() + req.durationMinutes * 60_000);

    const res = await fetch(
      `https://www.googleapis.com/calendar/v3/calendars/${calendarId}/events` +
        `?conferenceDataVersion=1&sendUpdates=all`,
      {
        method: "POST",
        headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
        body: JSON.stringify({
          summary: req.title,
          description:
            `SATForge 1-on-1 SAT guidance with ${req.studentName}.\n` +
            `Booking reference: ${req.bookingId}`,
          start: { dateTime: req.startsAt.toISOString() },
          end: { dateTime: end.toISOString() },
          attendees: [{ email: req.studentEmail, displayName: req.studentName }],
          // requestId must be stable per booking so a retry reuses the same
          // conference instead of creating a second one.
          conferenceData: {
            createRequest: {
              requestId: `satforge-${req.bookingId}`,
              conferenceSolutionKey: { type: "hangoutsMeet" },
            },
          },
          reminders: {
            useDefault: false,
            overrides: [
              { method: "email", minutes: 24 * 60 },
              { method: "popup", minutes: 10 },
            ],
          },
        }),
      },
    );

    if (!res.ok) {
      const detail = await res.text();
      throw new Error(`Google Calendar event creation failed (${res.status}): ${detail.slice(0, 300)}`);
    }

    const event = (await res.json()) as {
      id: string;
      hangoutLink?: string;
      htmlLink?: string;
      conferenceData?: { entryPoints?: { entryPointType: string; uri: string }[] };
    };

    const video = event.conferenceData?.entryPoints?.find((e) => e.entryPointType === "video");
    // hangoutLink is absent when delegation is not configured. The event still
    // exists, so fall back to the calendar link rather than reporting failure.
    const url = event.hangoutLink ?? video?.uri ?? event.htmlLink ?? null;

    return { url, provider: "google_meet", externalId: event.id };
  },

  async cancelMeeting(externalId: string): Promise<void> {
    const token = await accessToken();
    const calendarId = encodeURIComponent(process.env.GOOGLE_CALENDAR_ID!);
    const res = await fetch(
      `https://www.googleapis.com/calendar/v3/calendars/${calendarId}/events/${externalId}?sendUpdates=all`,
      { method: "DELETE", headers: { Authorization: `Bearer ${token}` } },
    );
    // 410 means it was already deleted, which is the desired end state.
    if (!res.ok && res.status !== 404 && res.status !== 410) {
      throw new Error(`Google Calendar event deletion failed (${res.status})`);
    }
  },
};
