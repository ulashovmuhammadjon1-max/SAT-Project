"use client";

import { SessionProvider } from "next-auth/react";
import { ThemeProvider } from "next-themes";
import { Toaster } from "@/components/ui/sonner";

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <SessionProvider>
      {/*
        Deep navy is the Scholarly brand, so dark is the default — that is what
        a visitor who never touches the switch sees, and what the marketing
        site and every product screenshot show.

        `enableSystem` is back on so "System" is a real option in the theme
        switch, but it is not the default: `defaultTheme="dark"` means a
        light-mode laptop still lands on the branded dark site until the
        student chooses otherwise. Their choice is remembered in localStorage.

        The exam interface is unaffected either way — it has its own fixed
        kiosk palette that never follows this theme, because a student should
        not be able to make a mock test look unlike the real one.
      */}
      <ThemeProvider attribute="class" defaultTheme="dark" enableSystem disableTransitionOnChange>
        {children}
        <Toaster richColors position="top-right" />
      </ThemeProvider>
    </SessionProvider>
  );
}
