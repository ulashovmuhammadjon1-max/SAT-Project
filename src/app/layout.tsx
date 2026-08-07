import type { Metadata } from "next";
import { Inter, Lexend } from "next/font/google";
import { Providers } from "@/components/shared/providers";
import "./globals.css";
import "katex/dist/katex.min.css";

const sans = Inter({
  subsets: ["latin"],
  variable: "--font-sans",
  display: "swap",
});

const display = Lexend({
  subsets: ["latin"],
  variable: "--font-display",
  display: "swap",
});

export const metadata: Metadata = {
  title: {
    default: "SATForge — Digital SAT Practice",
    template: "%s | SATForge",
  },
  description:
    "A premium Digital SAT preparation platform with adaptive full-length tests, a Bluebook-accurate exam interface, targeted practice, and vocabulary mastery.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={`${sans.variable} ${display.variable} font-sans`}>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
