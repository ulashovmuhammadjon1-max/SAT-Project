/**
 * Server-only Pexels access for scenic backgrounds.
 *
 * SECURITY: `PEXELS_API_KEY` is read from the server environment and never
 * leaves it. This module has no "use client" and is imported only by server
 * components; the key has no NEXT_PUBLIC_ prefix, so Next will not inline it
 * into any browser bundle even if it were imported by mistake (it would read
 * as undefined on the client). Do not import this from a client component.
 *
 * CACHING: results are cached, not fetched per visit. The fetch is tagged with
 * a long `revalidate`, so Vercel's Data Cache serves the same Pexels response
 * to every visitor across requests and deploys until the window turns over.
 * Selection is deterministic per query, so a cached response always resolves to
 * the same photo — a page shows one stable image, not a new one each load.
 *
 * FAILURE: any problem (missing key, network error, empty result) resolves to
 * `null`. Callers render their theme's fallback gradient, so a surface is never
 * blank and a background never breaks a page.
 */

import { resolveTheme, type SceneThemeKey } from "@/lib/backgrounds/themes";

/** One week. Long on purpose — a background does not need to be fresh. */
const REVALIDATE_SECONDS = 60 * 60 * 24 * 7;

export interface ScenicImage {
  /** Optimised image URL for <Image> (Pexels large2x, ~1880px wide). */
  url: string;
  width: number;
  height: number;
  alt: string;
  /** A tiny solid-colour data URL for an instant placeholder. */
  blurDataURL: string;
  photographer: string;
  /** The photo's page on pexels.com — the attribution link. */
  pexelsUrl: string;
}

interface PexelsPhoto {
  width: number;
  height: number;
  url: string;
  photographer: string;
  avg_color: string | null;
  alt: string | null;
  src: Record<string, string>;
}

interface PexelsSearchResponse {
  photos?: PexelsPhoto[];
}

/** Stable 32-bit hash so a query always picks the same photo from a page. */
function hashString(input: string): number {
  let h = 2166136261;
  for (let i = 0; i < input.length; i++) {
    h ^= input.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

/** A solid-colour SVG data URL, used as the blur placeholder. */
function solidBlur(hex: string): string {
  const color = /^#[0-9a-fA-F]{6}$/.test(hex) ? hex : "#1f2a44";
  const svg = `<svg xmlns='http://www.w3.org/2000/svg' width='8' height='5'><rect width='100%' height='100%' fill='${color}'/></svg>`;
  return `data:image/svg+xml;base64,${Buffer.from(svg).toString("base64")}`;
}

/**
 * Resolve a themed scenic image, or null if none is available.
 *
 * `theme` selects the query; `queryOverride` lets a one-off caller pass its own
 * search without adding a theme. The result is cached (see the module note).
 */
export async function getScenicImage(
  theme: SceneThemeKey | undefined,
  queryOverride?: string,
): Promise<ScenicImage | null> {
  const key = process.env.PEXELS_API_KEY;
  if (!key) return null;

  const query = (queryOverride ?? resolveTheme(theme).query).trim();
  if (!query) return null;

  const endpoint =
    "https://api.pexels.com/v1/search?" +
    new URLSearchParams({
      query,
      orientation: "landscape",
      size: "large",
      per_page: "15",
    }).toString();

  let data: PexelsSearchResponse;
  try {
    const res = await fetch(endpoint, {
      headers: { Authorization: key },
      // Cache the response so we do not call Pexels on every visit.
      next: { revalidate: REVALIDATE_SECONDS, tags: ["pexels"] },
    });
    if (!res.ok) return null;
    data = (await res.json()) as PexelsSearchResponse;
  } catch {
    return null;
  }

  const landscape = (data.photos ?? []).filter((p) => p.width >= p.height && p.src?.large2x);
  if (landscape.length === 0) return null;

  // Deterministic pick: same query -> same photo, so the cached response yields
  // a stable background rather than shuffling on each render.
  const photo = landscape[hashString(query) % landscape.length];

  return {
    url: photo.src.large2x,
    width: photo.width,
    height: photo.height,
    alt: photo.alt?.trim() || "",
    blurDataURL: solidBlur(photo.avg_color ?? "#1f2a44"),
    photographer: photo.photographer,
    pexelsUrl: photo.url,
  };
}
