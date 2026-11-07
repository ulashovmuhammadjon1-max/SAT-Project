/**
 * Appearance themes.
 *
 * A theme is two things: the light/dark MODE that next-themes already manages
 * (the `dark` class on <html>), and an optional PALETTE that re-tints the same
 * design tokens (`data-palette` on <html>, defined in globals.css). Keeping
 * them separate means every existing `dark:` utility and every shadcn
 * component keeps working untouched — a palette only changes the values of
 * --background, --card, --primary and friends, never the class names.
 *
 * The palette is remembered in localStorage and applied by an inline script in
 * the root layout before first paint, so there is no flash of the default
 * colours on reload.
 */
export type Palette = "default" | "midnight" | "forest" | "lavender" | "paper";

export interface Appearance {
  id: string;
  label: string;
  description: string;
  mode: "light" | "dark" | "system";
  palette: Palette;
  /** Background, surface, accent — for the preview tile only. */
  swatch: [string, string, string];
}

export const APPEARANCES: Appearance[] = [
  { id: "light", label: "Scholarly Light", description: "Bright and clean", mode: "light", palette: "default", swatch: ["#ffffff", "#f1f4f8", "#2f5be8"] },
  { id: "dark", label: "Scholarly Dark", description: "The signature navy", mode: "dark", palette: "default", swatch: ["#0a1020", "#111a2e", "#5b7cf0"] },
  { id: "midnight", label: "Midnight", description: "Deep navy, violet light", mode: "dark", palette: "midnight", swatch: ["#090d1c", "#10162b", "#7c83f5"] },
  { id: "forest", label: "Forest", description: "A quiet library green", mode: "dark", palette: "forest", swatch: ["#0e1612", "#141f19", "#4cb87a"] },
  { id: "lavender", label: "Lavender", description: "Soft violet, light", mode: "light", palette: "lavender", swatch: ["#fbf9fe", "#f1edfa", "#7a4fe0"] },
  { id: "paper", label: "Warm Paper", description: "Cream pages, ink and terracotta", mode: "light", palette: "paper", swatch: ["#f8f4ec", "#fcfaf5", "#a9512f"] },
  { id: "system", label: "Match my device", description: "Light or dark with your system", mode: "system", palette: "default", swatch: ["#ffffff", "#0a1020", "#2f5be8"] },
];

export const PALETTE_KEY = "scholarly-palette";
export const APPEARANCE_KEY = "scholarly-appearance";

/** Runs before paint. Kept tiny and dependency-free; it is inlined as a string. */
export const PALETTE_BOOT_SCRIPT = `try{var p=localStorage.getItem("${PALETTE_KEY}");if(p&&p!=="default")document.documentElement.setAttribute("data-palette",p)}catch(e){}`;

export function applyPalette(palette: Palette) {
  const root = document.documentElement;
  if (palette === "default") root.removeAttribute("data-palette");
  else root.setAttribute("data-palette", palette);
  try {
    localStorage.setItem(PALETTE_KEY, palette);
  } catch {
    /* private mode: the palette still applies for this page view */
  }
}

export function storedAppearanceId(): string | null {
  try {
    return localStorage.getItem(APPEARANCE_KEY);
  } catch {
    return null;
  }
}

export function storeAppearanceId(id: string) {
  try {
    localStorage.setItem(APPEARANCE_KEY, id);
  } catch {
    /* ignore */
  }
}
