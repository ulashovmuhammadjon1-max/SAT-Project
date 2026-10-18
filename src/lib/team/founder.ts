/**
 * The founder's card on the public team page.
 *
 * Static rather than a TeamMember row: the TeamMember table has no columns for
 * age, phone or Telegram, and adding them is a schema change that must ship
 * with its production migration (see CLAUDE.md). Founder details rarely
 * change, so a reviewed edit to this file is the right gate anyway.
 *
 * Every contact field is optional. A field left null is simply not shown, so
 * nothing half-filled ever reaches the page. Everything here is PUBLIC.
 */
export interface FounderCard {
  name: string;
  title: string;
  bio: string;
  /** Shown as "Age 17". */
  age: number | null;
  /** International format, e.g. "+998 90 123 45 67". Shown with a tel: link. */
  phone: string | null;
  email: string | null;
  /** A Telegram channel or handle: "@name" or "https://t.me/name". */
  telegram: string | null;
}

export const FOUNDER: FounderCard = {
  name: "Muhammadjon Ulashov",
  title: "Founder",
  bio:
    "Built Scholarly as a free academic community: a research programme with mentors, AP courses, " +
    "IELTS and SAT preparation, and financial literacy classes. Runs the 1-on-1 sessions and reviews " +
    "every research proposal and peer-mentor application personally.",
  age: null,
  phone: null,
  email: "ulashovmuhammadjon1@gmail.com",
  telegram: "@ulashovmuhammadjon1",
};

export interface MentorCard {
  name: string;
  /** One line under the name, e.g. the score that earned the place. */
  headline: string;
  subjects: string[];
}

/**
 * Peer mentors named by the founder. Shown alongside any mentor approved
 * through /mentor (PeerMentorApplication), so both routes onto the page work.
 */
export const PEER_MENTORS: MentorCard[] = [
  { name: "Jasurbek", headline: "SAT 1450 · Math 790", subjects: ["SAT"] },
  { name: "Rustambek", headline: "SAT 1480 · Math 800", subjects: ["SAT"] },
  { name: "Yusufbek", headline: "SAT Math 730", subjects: ["SAT"] },
];

/** Mentors on the research programme. */
export const RESEARCH_MENTORS: MentorCard[] = [
  { name: "Sardorbek", headline: "Research mentor", subjects: [] },
  { name: "Muhammadjon", headline: "Research mentor", subjects: [] },
  { name: "Farrukh", headline: "Research mentor", subjects: [] },
];

/** "@name" or "t.me/name" or a full URL, normalised to a link and a label. */
export function telegramLink(value: string): { href: string; label: string } {
  const handle = value
    .trim()
    .replace(/^https?:\/\//, "")
    .replace(/^(www\.)?t(elegram)?\.me\//, "")
    .replace(/^@/, "");
  return { href: `https://t.me/${handle}`, label: `@${handle}` };
}
