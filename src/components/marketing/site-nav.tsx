"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Menu, X } from "lucide-react";

import { Wordmark } from "@/components/marketing/wordmark";
import { ThemeToggle, ThemeToggleCompact } from "@/components/shared/theme-toggle";

/**
 * Every link resolves to a real destination: the four homepage sections by
 * anchor (as absolute "/#…" paths, so they also work from /team or /schools),
 * and the team page.
 */
const LINKS = [
  { href: "/#programmes", label: "Programmes" },
  { href: "/#research", label: "Research" },
  { href: "/#courses", label: "AP Courses" },
  { href: "/team", label: "Team" },
  { href: "/#faq", label: "FAQ" },
];

/**
 * The public header. Sticky, because the page is long and the join action
 * should stay one click away — but kept to 64px with a solid paper surface
 * and a single hairline, rather than a tall frosted panel.
 */
export function SiteNav() {
  const [open, setOpen] = useState(false);

  // Close the mobile menu on Escape, the way a native disclosure behaves.
  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open]);

  return (
    <header className="sticky top-0 z-50 border-b border-border bg-background/95 supports-[backdrop-filter]:bg-background/90 supports-[backdrop-filter]:backdrop-blur-sm">
      <a
        href="#main"
        className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-3 focus:z-50 focus:rounded-md focus:bg-card focus:px-3 focus:py-2 focus:text-sm focus:shadow-card"
      >
        Skip to content
      </a>
      <nav aria-label="Main" className="mx-auto flex h-16 max-w-6xl items-center justify-between gap-6 px-4 sm:px-6 lg:px-8">
        <Wordmark />

        <ul className="hidden items-center gap-1 lg:flex">
          {LINKS.map((l) => (
            <li key={l.href}>
              <Link
                href={l.href}
                className="whitespace-nowrap rounded-md px-3 py-2 text-[14px] text-muted-foreground transition-colors hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
              >
                {l.label}
              </Link>
            </li>
          ))}
        </ul>

        <div className="hidden items-center gap-1 lg:flex">
          <ThemeToggleCompact />
          <Link
            href="/login"
            className="whitespace-nowrap rounded-md px-3 py-2 text-[14px] font-medium text-foreground transition-colors hover:text-primary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
          >
            Sign in
          </Link>
          <Link
            href="/onboarding"
            className="ml-1 inline-flex h-9 items-center whitespace-nowrap rounded-md bg-primary px-4 text-[14px] font-medium text-primary-foreground transition-colors hover:bg-primary/90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background"
          >
            Join free
          </Link>
        </div>

        <button
          type="button"
          onClick={() => setOpen((v) => !v)}
          aria-expanded={open}
          aria-controls="mobile-menu"
          aria-label={open ? "Close menu" : "Open menu"}
          className="-mr-2 flex h-11 w-11 items-center justify-center rounded-md text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring lg:hidden"
        >
          {open ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
        </button>
      </nav>

      <div
        id="mobile-menu"
        hidden={!open}
        className="border-t border-border bg-background lg:hidden"
      >
        <ul className="px-4 py-2">
          {LINKS.map((l) => (
            <li key={l.href}>
              <Link
                href={l.href}
                onClick={() => setOpen(false)}
                className="flex min-h-11 items-center border-b border-border/70 text-[15px] text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
              >
                {l.label}
              </Link>
            </li>
          ))}
        </ul>
        <div className="flex items-center justify-between px-4 py-3">
          <span className="text-sm text-muted-foreground">Theme</span>
          <ThemeToggle />
        </div>
        <div className="grid grid-cols-2 gap-2 px-4 pb-4">
          <Link
            href="/login"
            className="inline-flex h-11 items-center justify-center rounded-md border border-input text-[15px] font-medium focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
          >
            Sign in
          </Link>
          <Link
            href="/onboarding"
            className="inline-flex h-11 items-center justify-center rounded-md bg-primary text-[15px] font-medium text-primary-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
          >
            Join free
          </Link>
        </div>
      </div>
    </header>
  );
}
