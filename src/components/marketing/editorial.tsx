import Link from "next/link";
import { ArrowRight } from "lucide-react";

import { cn } from "@/lib/utils";

/**
 * The public site's layout primitives. One container width, one section
 * rhythm, one heading pattern — so the homepage, team page and school page
 * read as one publication rather than three templates.
 *
 * Type roles:
 *  - serif (Source Serif 4): page headlines, section headlines, statements.
 *  - sans (Inter): everything functional — navigation, labels, body, controls.
 */

export function Container({ className, children }: { className?: string; children: React.ReactNode }) {
  return <div className={cn("mx-auto w-full max-w-6xl px-4 sm:px-6 lg:px-8", className)}>{children}</div>;
}

/**
 * A short sentence-case label set off by a rule. Colour is a meaning, not a
 * flourish: `research` marks the research programme, everything else is ink.
 */
export function Eyebrow({
  children,
  tone = "default",
  className,
}: {
  children: React.ReactNode;
  tone?: "default" | "research";
  className?: string;
}) {
  return (
    <p
      className={cn(
        "flex items-center gap-3 text-[13px] font-medium",
        tone === "research" ? "text-research" : "text-muted-foreground",
        className,
      )}
    >
      <span aria-hidden className="h-px w-6 bg-current opacity-70" />
      {children}
    </p>
  );
}

export function SectionTitle({
  as: Tag = "h2",
  className,
  children,
  id,
}: {
  as?: "h1" | "h2" | "h3";
  className?: string;
  children: React.ReactNode;
  id?: string;
}) {
  return (
    <Tag
      id={id}
      className={cn(
        "font-serif text-[2rem] font-medium leading-[1.12] tracking-[-0.012em] text-balance sm:text-[2.5rem]",
        className,
      )}
    >
      {children}
    </Tag>
  );
}

export function Lede({ className, children }: { className?: string; children: React.ReactNode }) {
  return <p className={cn("max-w-[38rem] text-[17px] leading-[1.65] text-muted-foreground", className)}>{children}</p>;
}

/** A text link with a trailing arrow — the site's secondary action. */
export function ArrowLink({
  href,
  children,
  className,
}: {
  href: string;
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <Link
      href={href}
      className={cn(
        "group inline-flex items-center gap-1.5 whitespace-nowrap rounded-sm text-[15px] font-medium text-primary underline-offset-4 hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background",
        className,
      )}
    >
      {children}
      <ArrowRight aria-hidden className="h-4 w-4 transition-transform duration-150 group-hover:translate-x-0.5 motion-reduce:transition-none" />
    </Link>
  );
}

/** The primary action. One per view; never two of these side by side. */
export function PrimaryLink({
  href,
  children,
  className,
}: {
  href: string;
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <Link
      href={href}
      className={cn(
        "inline-flex h-11 items-center justify-center gap-2 whitespace-nowrap rounded-md bg-primary px-5 text-[15px] font-medium text-primary-foreground transition-colors duration-150 hover:bg-primary/90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background",
        className,
      )}
    >
      {children}
    </Link>
  );
}
