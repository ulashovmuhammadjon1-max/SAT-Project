/**
 * Server-only community helpers shared by the student actions, the admin
 * actions, the sync route and the email processor.
 */
import { prisma } from "@/lib/prisma";
import { shortName } from "@/lib/leaderboard";

/** A tab that heartbeated recently AND a person who touched it recently. */
export const PRESENCE_SEEN_MS = 90_000;
export const PRESENCE_ACTIVE_MS = 5 * 60_000;

export function isActiveNow(p: { lastSeenAt: Date; lastActiveAt: Date } | null | undefined, now = Date.now()) {
  if (!p) return false;
  return now - p.lastSeenAt.getTime() < PRESENCE_SEEN_MS && now - p.lastActiveAt.getTime() < PRESENCE_ACTIVE_MS;
}

export const displayName = (name: string | null | undefined) => shortName(name ?? null, "A student");

/** Plain one-line excerpt with the markdown markers stripped. */
export function excerpt(text: string, max = 160): string {
  const flat = text
    .replace(/```[\s\S]*?```/g, " [code] ")
    .replace(/[*_`~>#]/g, "")
    .replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g, "$1")
    .replace(/\s+/g, " ")
    .trim();
  return flat.length > max ? `${flat.slice(0, max - 1)}…` : flat;
}

export function messageUrl(channelSlug: string, messageId: string, threadRootId?: string | null) {
  const q = threadRootId ? `thread=${threadRootId}&m=${messageId}` : `m=${messageId}`;
  return `/community/${channelSlug}?${q}`;
}

/** Ids this user blocked, and ids that blocked this user. */
export async function blockSets(userId: string) {
  const rows = await prisma.communityBlock.findMany({
    where: { OR: [{ blockerId: userId }, { blockedId: userId }] },
    select: { blockerId: true, blockedId: true },
  });
  const iBlocked = new Set<string>();
  const blockedMe = new Set<string>();
  for (const r of rows) {
    if (r.blockerId === userId) iBlocked.add(r.blockedId);
    else blockedMe.add(r.blockerId);
  }
  return { iBlocked, blockedMe };
}

/** An active posting restriction, or null. */
export async function activeRestriction(userId: string) {
  const r = await prisma.communityRestriction.findUnique({ where: { userId } });
  return r && r.until.getTime() > Date.now() ? r : null;
}

export function restrictionMessage(until: Date) {
  return `A moderator has paused your posting until ${until.toUTCString().replace(" GMT", " UTC")}.`;
}

/** Approved peer mentors among these user ids, for the mentor badge. */
export async function mentorIds(userIds: string[]): Promise<Set<string>> {
  if (userIds.length === 0) return new Set();
  const rows = await prisma.peerMentorApplication.findMany({
    where: { userId: { in: userIds }, status: "APPROVED" },
    select: { userId: true },
  });
  return new Set(rows.map((r) => r.userId));
}

export interface MemberPrefs {
  emailReplies: boolean;
  emailMentions: boolean;
  emailDirect: boolean;
  emailActivity: boolean;
  emailAnnouncements: boolean;
  emailDigest: boolean;
  dmPolicy: "EVERYONE" | "NOBODY";
  showPresence: boolean;
}

/** Defaults for a student who never opened their settings: replies and mentions on. */
export const DEFAULT_PREFS: MemberPrefs = {
  emailReplies: true,
  emailMentions: true,
  emailDirect: true,
  emailActivity: false,
  emailAnnouncements: false,
  emailDigest: false,
  dmPolicy: "EVERYONE",
  showPresence: true,
};

export async function prefsFor(userIds: string[]): Promise<Map<string, MemberPrefs>> {
  const rows = userIds.length
    ? await prisma.communityMember.findMany({
        where: { userId: { in: userIds } },
        select: {
          userId: true,
          emailReplies: true,
          emailMentions: true,
          emailDirect: true,
          emailActivity: true,
          emailAnnouncements: true,
          emailDigest: true,
          dmPolicy: true,
          showPresence: true,
        },
      })
    : [];
  const map = new Map<string, MemberPrefs>();
  for (const id of userIds) map.set(id, DEFAULT_PREFS);
  for (const r of rows) map.set(r.userId, r);
  return map;
}

/** The next daily digest send time: 16:00 UTC (21:00 in Tashkent). */
export function nextDigestAt(now = new Date()): Date {
  const d = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate(), 16, 0, 0));
  if (d.getTime() <= now.getTime()) d.setUTCDate(d.getUTCDate() + 1);
  return d;
}
