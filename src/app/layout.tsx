import type { Metadata } from "next";
import { Inter, Source_Serif_4 } from "next/font/google";
import { Providers } from "@/components/shared/providers";
import "./globals.css";
import "katex/dist/katex.min.css";

const sans = Inter({
  subsets: ["latin"],
  variable: "--font-sans",
  display: "swap",
});

/**
 * Two families, each with a job. Inter carries the interface: navigation,
 * labels, body copy, every control. Source Serif 4 carries the editorial
 * voice — page headlines and statements about scholarship — and is set with
 * its optical-size axis so large headlines get the display cut and small
 * captions the text cut from one file.
 */
const serif = Source_Serif_4({
  subsets: ["latin"],
  variable: "--font-serif",
  display: "swap",
  style: ["normal", "italic"],
  axes: ["opsz"],
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
      <body className={`${sans.variable} ${serif.variable} font-sans`}>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
