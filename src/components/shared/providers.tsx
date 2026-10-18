"use client";

import { SessionProvider } from "next-auth/react";
import { ThemeProvider } from "next-themes";
import { Toaster } from "@/components/ui/sonner";

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <SessionProvider>
      {/*
        Paper and ink is the Scholarly brand, so light is the default — that is
        what a visitor who never touches the switch sees. The dark theme is a
        fully designed alternative (layered ink, not black), not an inversion.

        `enableSystem` keeps "System" as a real option in the theme switch, but
        it is not the default. A student's choice is remembered in localStorage,
        so anyone who already picked dark keeps it.

        The exam interface is unaffected either way — it has its own fixed
        kiosk palette that never follows this theme, because a student should
        not be able to make a mock test look unlike the real one.
      */}
      <ThemeProvider attribute="class" defaultTheme="light" enableSystem disableTransitionOnChange>
        {children}
        <Toaster richColors position="top-right" />
      </ThemeProvider>
    </SessionProvider>
  );
}
