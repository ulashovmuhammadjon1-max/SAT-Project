"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { AnimatePresence, motion } from "framer-motion";
import { GraduationCap, Menu, X } from "lucide-react";

import { Button } from "@/components/ui/button";
import { ThemeToggle, ThemeToggleCompact } from "@/components/shared/theme-toggle";
import { cn } from "@/lib/utils";

const LINKS = [
  { href: "/#programmes", label: "Programmes" },
  { href: "/#research", label: "Research" },
  { href: "/#courses", label: "AP Courses" },
  { href: "/team", label: "Team" },
  { href: "/#faq", label: "FAQ" },
];

export function SiteNav() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    function onScroll() {
      setScrolled(window.scrollY > 12);
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open]);

  return (
    <header
      className={cn(
        "fixed inset-x-0 top-0 z-50 transition-all duration-300",
        scrolled || open
          ? "border-b border-border/60 bg-background/80 backdrop-blur-xl supports-[backdrop-filter]:bg-background/60"
          : "border-b border-transparent bg-transparent"
      )}
    >
      <nav className="mx-auto flex h-16 max-w-7xl items-center justify-between px-5 sm:px-8">
        <Link href="/" className="flex items-center gap-2.5">
          <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-navy-950 text-white shadow-soft">
            <GraduationCap className="h-[18px] w-[18px]" />
          </span>
          <span className="font-display text-[17px] font-semibold tracking-tight">Scholarly</span>
        </Link>

        <div className="hidden items-center gap-1 md:flex">
          {LINKS.map((l) => (
            <a
              key={l.href}
              href={l.href}
              className="rounded-md px-3 py-2 text-sm font-medium text-muted-foreground transition-colors hover:text-foreground"
            >
              {l.label}
            </a>
          ))}
        </div>

        <div className="hidden items-center gap-2 md:flex">
          <ThemeToggleCompact />
          <Button variant="ghost" size="sm" asChild>
            <Link href="/login">Sign in</Link>
          </Button>
          <Button size="sm" className="rounded-full px-4 shadow-soft" asChild>
            <Link href="/onboarding">Join free</Link>
          </Button>
        </div>

        <button
          type="button"
          onClick={() => setOpen((v) => !v)}
          aria-label={open ? "Close menu" : "Open menu"}
          aria-expanded={open}
          aria-controls="site-nav-mobile"
          className="-mr-2 flex h-10 w-10 items-center justify-center rounded-lg text-foreground md:hidden"
        >
          {open ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
        </button>
      </nav>

      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.2 }}
            id="site-nav-mobile"
            className="max-h-[calc(100dvh-4rem)] overflow-y-auto border-t border-border/60 bg-background/95 backdrop-blur-xl md:hidden"
          >
            <div className="space-y-1 px-5 py-4">
              {LINKS.map((l) => (
                <a
                  key={l.href}
                  href={l.href}
                  onClick={() => setOpen(false)}
                  className="flex min-h-11 items-center rounded-md px-3 text-[15px] font-medium text-muted-foreground active:bg-secondary"
                >
                  {l.label}
                </a>
              ))}
              {/* Full three-way switch on mobile: there is room for it here,
                  and the cycling button is harder to understand on a phone. */}
              <div className="flex items-center justify-between px-3 pt-2">
                <span className="text-sm font-medium text-muted-foreground">Theme</span>
                <ThemeToggle />
              </div>
              <div className="flex gap-2 pt-2">
                <Button variant="outline" className="h-11 flex-1" asChild>
                  <Link href="/login">Sign in</Link>
                </Button>
                <Button className="h-11 flex-1" asChild>
                  <Link href="/onboarding">Join free</Link>
                </Button>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
