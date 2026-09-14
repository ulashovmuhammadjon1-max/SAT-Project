/**
 * Scenic background themes.
 *
 * The single place to define what each page or section looks for. A theme is a
 * Pexels search query plus a CSS gradient used as the fallback when Pexels is
 * unavailable (no key, network error, empty result) — so a surface always has
 * a considered background and never a blank rectangle.
 *
 * To theme a new surface: add a key here, then render
 * `<ScenicHeader theme="yourKey">…</ScenicHeader>`. Nothing else needs to know
 * the query exists. To retune an existing surface, change its query string —
 * the cache turns over on its own (see `pexels.ts`).
 *
 * Queries are written for calm, wide, scenic photography — the kind that reads
 * well behind text once a gradient sits over it. Keep them landscape in spirit;
 * the fetcher already asks Pexels for landscape orientation.
 */

export interface SceneTheme {
  /** What to search Pexels for. */
  query: string;
  /** CSS `background` value used when no photo is available. */
  fallbackGradient: string;
}

export const SCENE_THEMES = {
  // Calm natural landscape — the dashboard's daily home.
  dashboard: {
    query: "calm serene mountain lake reflection landscape",
    fallbackGradient:
      "linear-gradient(120deg, hsl(226 60% 22%), hsl(199 70% 30%) 55%, hsl(174 55% 32%))",
  },

  // Mathematics — mountains, peaks, exploration.
  math: {
    query: "dramatic mountain peaks summit alpine",
    fallbackGradient:
      "linear-gradient(120deg, hsl(222 55% 20%), hsl(226 70% 34%) 60%, hsl(244 55% 42%))",
  },

  // English — city, library, culture, architecture.
  english: {
    query: "grand old library architecture interior",
    fallbackGradient:
      "linear-gradient(120deg, hsl(28 45% 22%), hsl(20 55% 34%) 55%, hsl(340 40% 38%))",
  },

  // Science — space, nature, technology.
  science: {
    query: "starry night sky galaxy milky way",
    fallbackGradient:
      "linear-gradient(120deg, hsl(250 60% 16%), hsl(262 65% 30%) 55%, hsl(199 70% 34%))",
  },

  // Achievements — sunrise, summit, inspiring landscape.
  achievements: {
    query: "sunrise mountain summit golden hour clouds",
    fallbackGradient:
      "linear-gradient(120deg, hsl(24 80% 40%), hsl(14 75% 46%) 50%, hsl(280 45% 40%))",
  },

  // Reading & Writing — quieter, literary.
  reading: {
    query: "misty forest morning light path",
    fallbackGradient:
      "linear-gradient(120deg, hsl(160 40% 20%), hsl(174 45% 30%) 60%, hsl(199 55% 34%))",
  },

  // Ocean / focus sessions — wide, level horizon.
  ocean: {
    query: "calm ocean horizon minimal seascape",
    fallbackGradient:
      "linear-gradient(120deg, hsl(206 70% 22%), hsl(199 75% 34%) 55%, hsl(186 60% 40%))",
  },

  // Neutral default for anything not otherwise themed.
  default: {
    query: "scenic minimal nature landscape",
    fallbackGradient:
      "linear-gradient(120deg, hsl(226 45% 24%), hsl(210 40% 32%) 60%, hsl(199 45% 36%))",
  },
} satisfies Record<string, SceneTheme>;

export type SceneThemeKey = keyof typeof SCENE_THEMES;

export function resolveTheme(key: SceneThemeKey | undefined): SceneTheme {
  return SCENE_THEMES[key ?? "default"] ?? SCENE_THEMES.default;
}
