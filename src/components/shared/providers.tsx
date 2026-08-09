"use client";

import { SessionProvider } from "next-auth/react";
import { ThemeProvider } from "next-themes";
import { Toaster } from "@/components/ui/sonner";

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <SessionProvider>
      {/*
        Deep navy is the SATForge brand, not a user preference — the hero, the
        marketing site and every product screenshot are dark, so defaulting to
        light made the app look like a different product to anyone who had not
        toggled.

        `enableSystem` is off deliberately: with it on, a visitor whose OS is in
        light mode saw a white SATForge, which is exactly the inconsistency the
        brand guidance rules out. The exam interface is unaffected either way —
        it has its own fixed kiosk palette that never follows this theme.
      */}
      <ThemeProvider attribute="class" defaultTheme="dark" enableSystem={false} disableTransitionOnChange>
        {children}
        <Toaster richColors position="top-right" />
      </ThemeProvider>
    </SessionProvider>
  );
}
