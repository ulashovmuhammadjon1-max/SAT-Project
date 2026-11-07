import type { Metadata } from "next";
import { Inter, Lexend, Newsreader } from "next/font/google";
import { Providers } from "@/components/shared/providers";
import { PALETTE_BOOT_SCRIPT } from "@/lib/appearance";
import "./globals.css";
import "katex/dist/katex.min.css";

const sans = Inter({
  subsets: ["latin"],
  variable: "--font-sans",
  display: "swap",
});

// Editorial serif for community headlines and post titles. Only downloaded on
// pages that actually set text in it.
const serif = Newsreader({
  subsets: ["latin"],
  variable: "--font-serif",
  display: "swap",
  style: ["normal", "italic"],
  adjustFontFallback: false,
});

const display = Lexend({
  subsets: ["latin"],
  variable: "--font-display",
  display: "swap",
});

export const metadata: Metadata = {
  title: {
    default: "Scholarly — Research, Mentorship & Learning",
    template: "%s | Scholarly",
  },
  description:
    "A free academic community for students: a research programme with mentors, AP courses, IELTS preparation, financial literacy, and SAT practice — all in one place.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        {/* Applies the saved appearance palette before first paint. */}
        <script dangerouslySetInnerHTML={{ __html: PALETTE_BOOT_SCRIPT }} />
      </head>
      <body className={`${sans.variable} ${display.variable} ${serif.variable} font-sans`}>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
