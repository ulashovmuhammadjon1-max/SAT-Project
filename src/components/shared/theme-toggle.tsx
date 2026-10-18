"use client";

import { useEffect, useState } from "react";
import { Monitor, Moon, Sun } from "lucide-react";
import { useTheme } from "next-themes";

import { cn } from "@/lib/utils";

/**
 * Light / dark / system switch.
 *
 * Three options rather than two: a plain toggle forces a student to keep the
 * site in sync with their phone by hand, and "system" is what most people
 * actually want once they know it exists. Dark stays the default for anyone
 * who never touches this.
 *
 * `next-themes` cannot know the resolved theme until after hydration, so the
 * control renders a same-sized placeholder on the server. Rendering the real
 * state immediately would either mismatch or flash the wrong icon.
 */

const OPTIONS = [
  { value: "light", label: "Light", icon: Sun },
  { value: "dark", label: "Dark", icon: Moon },
  { value: "system", label: "System", icon: Monitor },
] as const;

export function ThemeToggle({ className }: { className?: string }) {
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);

  if (!mounted) {
    return <div className={cn("h-9 w-[7.5rem] rounded-full bg-secondary/60", className)} aria-hidden />;
  }

  return (
    <div
      role="radiogroup"
      aria-label="Colour theme"
      className={cn(
        "inline-flex items-center gap-0.5 rounded-full border border-border bg-secondary/60 p-0.5",
        className,
      )}
    >
      {OPTIONS.map((o) => {
        const active = theme === o.value;
        return (
          <button
            key={o.value}
            type="button"
            role="radio"
            aria-checked={active}
            aria-label={o.label}
            title={o.label}
            onClick={() => setTheme(o.value)}
            className={cn(
              "flex h-8 w-8 items-center justify-center rounded-full transition-colors",
              "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
              active
                ? "bg-background text-foreground shadow-sm"
                : "text-muted-foreground hover:text-foreground",
            )}
          >
            <o.icon className="h-4 w-4" />
          </button>
        );
      })}
    </div>
  );
}

/**
 * Single-button variant for tight spaces (the marketing nav).
 *
 * Cycles light → dark → system so every state is still reachable, rather than
 * hiding "system" behind a menu nobody opens.
 */
export function ThemeToggleCompact({ className }: { className?: string }) {
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);

  if (!mounted) {
    return <div className={cn("h-9 w-9 rounded-full bg-secondary/60", className)} aria-hidden />;
  }

  const current = OPTIONS.find((o) => o.value === theme) ?? OPTIONS[1];
  const next = OPTIONS[(OPTIONS.indexOf(current) + 1) % OPTIONS.length];
  const Icon = current.icon;

  return (
    <button
      type="button"
      onClick={() => setTheme(next.value)}
      aria-label={`Theme: ${current.label}. Switch to ${next.label}.`}
      title={`Theme: ${current.label} — click for ${next.label}`}
      className={cn(
        "flex h-9 w-9 items-center justify-center rounded-full border border-border",
        "bg-secondary/60 text-muted-foreground transition-colors hover:text-foreground",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
        className,
      )}
    >
      <Icon className="h-4 w-4" />
    </button>
  );
}
