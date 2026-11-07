"use client";

import { useEffect, useState } from "react";
import { Check, Palette as PaletteIcon } from "lucide-react";
import { useTheme } from "next-themes";

import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import {
  APPEARANCES,
  applyPalette,
  storeAppearanceId,
  storedAppearanceId,
  type Appearance,
} from "@/lib/appearance";
import { cn } from "@/lib/utils";

/** Which appearance is in effect, from the stored id or the plain mode. */
export function useAppearance() {
  const { theme, setTheme } = useTheme();
  const [id, setId] = useState<string | null>(null);

  useEffect(() => {
    const stored = storedAppearanceId();
    if (stored && APPEARANCES.some((a) => a.id === stored)) setId(stored);
    else setId(theme === "light" ? "light" : theme === "system" ? "system" : "dark");
  }, [theme]);

  function choose(a: Appearance) {
    setTheme(a.mode);
    applyPalette(a.palette);
    storeAppearanceId(a.id);
    setId(a.id);
  }

  return { current: id, choose };
}

/** The tile grid, used by the topbar popover and the community settings page. */
export function AppearancePicker({ className }: { className?: string }) {
  const { current, choose } = useAppearance();
  return (
    <div role="radiogroup" aria-label="Appearance" className={cn("grid grid-cols-2 gap-2", className)}>
      {APPEARANCES.map((a) => {
        const active = current === a.id;
        const [bg, surface, accent] = a.swatch;
        return (
          <button
            key={a.id}
            type="button"
            role="radio"
            aria-checked={active}
            onClick={() => choose(a)}
            className={cn(
              "group rounded-xl border p-2 text-left transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
              active ? "border-primary ring-1 ring-primary" : "border-border hover:border-foreground/30",
            )}
          >
            {/* A miniature of the page: canvas, a card, an accent line. */}
            <span
              aria-hidden
              className="relative block h-14 overflow-hidden rounded-lg border border-black/5"
              style={{
                background:
                  a.id === "system" ? `linear-gradient(135deg, ${bg} 50%, ${surface} 50%)` : bg,
              }}
            >
              {a.id !== "system" && (
                <>
                  <span className="absolute left-2 top-2 h-2 w-10 rounded-full" style={{ background: accent }} />
                  <span
                    className="absolute bottom-2 left-2 right-6 top-6 rounded-md"
                    style={{ background: surface, boxShadow: "0 1px 2px rgba(0,0,0,.12)" }}
                  />
                </>
              )}
              {active && (
                <span className="absolute right-1.5 top-1.5 flex h-5 w-5 items-center justify-center rounded-full bg-primary text-primary-foreground">
                  <Check className="h-3 w-3" />
                </span>
              )}
            </span>
            <span className="mt-1.5 block text-[13px] font-medium leading-tight">{a.label}</span>
            <span className="block text-[11px] leading-tight text-muted-foreground">{a.description}</span>
          </button>
        );
      })}
    </div>
  );
}

/** Topbar button that opens the picker. */
export function AppearanceMenu({ className }: { className?: string }) {
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);
  if (!mounted) return <div className={cn("h-9 w-9 rounded-full bg-secondary/60", className)} aria-hidden />;

  return (
    <Popover>
      <PopoverTrigger asChild>
        <button
          type="button"
          aria-label="Appearance"
          title="Appearance"
          className={cn(
            "flex h-9 w-9 items-center justify-center rounded-full border border-border bg-secondary/60",
            "text-muted-foreground transition-colors hover:text-foreground",
            "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
            className,
          )}
        >
          <PaletteIcon className="h-4 w-4" />
        </button>
      </PopoverTrigger>
      <PopoverContent align="end" className="w-[22rem] p-3">
        <p className="px-1 pb-2 text-sm font-semibold">Appearance</p>
        <AppearancePicker />
        <p className="px-1 pt-2 text-[11px] text-muted-foreground">Saved on this device and used across Scholarly.</p>
      </PopoverContent>
    </Popover>
  );
}
