/**
 * The fixed set of channel icons. Channels store one of these keys, never a
 * URL or arbitrary string; the client maps keys to icon components.
 */
export const CHANNEL_ICON_KEYS = [
  "hash",
  "messages",
  "megaphone",
  "trophy",
  "lightbulb",
  "hand",
  "sigma",
  "book-open",
  "languages",
  "award",
  "flask",
  "library",
  "graduation",
  "calculator",
  "atom",
  "globe",
  "code",
  "pen",
  "coffee",
  "briefcase",
  "music",
  "heart",
  "sparkles",
  "bookmark",
] as const;

export type ChannelIconKey = (typeof CHANNEL_ICON_KEYS)[number];

export function isChannelIcon(v: string): v is ChannelIconKey {
  return (CHANNEL_ICON_KEYS as readonly string[]).includes(v);
}
