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
    default: "Scholarly — SAT, IELTS & More",
    template: "%s | Scholarly",
  },
  description:
    "A free academic community: adaptive Digital SAT practice, full IELTS preparation, financial literacy, mentorship, and research programmes — all in one place.",
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
