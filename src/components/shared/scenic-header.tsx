import Image from "next/image";

import { cn } from "@/lib/utils";
import { getScenicImage } from "@/lib/backgrounds/pexels";
import { resolveTheme, type SceneThemeKey } from "@/lib/backgrounds/themes";

/**
 * A scenic hero band: a themed Pexels photo behind a readable gradient, with
 * the section's own content laid over it in white.
 *
 * Reusable and declarative — a page says `<ScenicHeader theme="math">…` and
 * gets a calm, immersive header without touching Pexels, caching, overlays or
 * attribution. It is an async Server Component, so the image is resolved on the
 * server and the key stays there.
 *
 * Readability first: a dark gradient always sits between the photo and the
 * content, so white text stays legible over any image. When no photo is
 * available the theme's fallback gradient renders instead, and the band looks
 * intentional rather than broken.
 *
 * Performance: the image uses next/image (responsive `sizes`, automatic
 * format/size), a solid-colour blur placeholder for instant paint, and the
 * cached Pexels result (one request per query per week, not per visit).
 */

type Overlay = "soft" | "medium" | "strong";

const OVERLAY_CLASS: Record<Overlay, string> = {
  // Lighter, for short bands where the photo should read.
  soft: "bg-gradient-to-tr from-black/60 via-black/35 to-black/15",
  // Default balance of image and legibility.
  medium: "bg-gradient-to-tr from-black/75 via-black/50 to-black/25",
  // Heaviest, for long text or busy images.
  strong: "bg-gradient-to-tr from-black/85 via-black/65 to-black/40",
};

export interface ScenicHeaderProps {
  /** Theme key from the registry (selects the search query + fallback). */
  theme?: SceneThemeKey;
  /** One-off search query, overriding the theme's query. */
  query?: string;
  /** Overlay strength for text legibility. Defaults to "medium". */
  overlay?: Overlay;
  /** Extra classes on the outer band (e.g. min-height, margin). */
  className?: string;
  /** Extra classes on the content wrapper (padding, layout). */
  contentClassName?: string;
  /** Load eagerly — set true only for an above-the-fold hero. */
  priority?: boolean;
  children: React.ReactNode;
}

export async function ScenicHeader({
  theme,
  query,
  overlay = "medium",
  className,
  contentClassName,
  priority = false,
  children,
}: ScenicHeaderProps) {
  const image = await getScenicImage(theme, query);
  const fallbackGradient = resolveTheme(theme).fallbackGradient;

  return (
    <section className={cn("relative isolate overflow-hidden rounded-2xl", className)}>
      {/* Background layer, always behind the content. */}
      <div className="absolute inset-0 -z-10">
        {image ? (
          <>
            <Image
              src={image.url}
              alt={image.alt}
              fill
              // One big band across breakpoints, so serve near full-width.
              sizes="(max-width: 640px) 100vw, (max-width: 1280px) 90vw, 1200px"
              quality={68}
              placeholder="blur"
              blurDataURL={image.blurDataURL}
              priority={priority}
              className="object-cover"
            />
            <div aria-hidden className={cn("absolute inset-0", OVERLAY_CLASS[overlay])} />
          </>
        ) : (
          <div aria-hidden className="absolute inset-0" style={{ background: fallbackGradient }} />
        )}
      </div>

      {/* Content, in white over the overlay. */}
      <div
        className={cn(
          "relative text-white [text-wrap:balance] [&_*]:border-white/20",
          "px-5 py-6 sm:px-8 sm:py-8",
          contentClassName,
        )}
      >
        {children}
      </div>

      {/* Attribution, per Pexels API guidelines: credit the photographer and
          link to Pexels. Quiet, but always present when a photo is shown. */}
      {image && (
        <a
          href={image.pexelsUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="absolute bottom-1.5 right-2.5 z-10 rounded bg-black/25 px-1.5 py-0.5 text-[10px] font-medium text-white/70 backdrop-blur-sm transition-colors hover:text-white"
        >
          Photo: {image.photographer} / Pexels
        </a>
      )}
    </section>
  );
}
