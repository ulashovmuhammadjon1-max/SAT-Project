import Link from "next/link";

import { cn } from "@/lib/utils";

/**
 * The Scholarly mark: an open book drawn as two ruled pages, beside the name
 * set in the editorial serif. Deliberately not a crest, seal or shield —
 * Scholarly is an independent community and should never be mistaken for a
 * chartered institution.
 */
export function ScholarlyMark({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 32 32" aria-hidden className={cn("h-8 w-8", className)}>
      <rect width="32" height="32" rx="6" className="fill-foreground" />
      <path
        d="M7 10.5c3.2-.9 6.2-.6 9 1.2v11.8c-2.8-1.8-5.8-2.1-9-1.2V10.5Z"
        className="fill-background"
      />
      <path
        d="M25 10.5c-3.2-.9-6.2-.6-9 1.2v11.8c2.8-1.8 5.8-2.1 9-1.2V10.5Z"
        className="fill-background"
        opacity="0.82"
      />
      <path d="M9.4 14.3c1.8-.3 3.4-.1 4.9.6M9.4 17.3c1.8-.3 3.4-.1 4.9.6" className="stroke-foreground" strokeWidth="0.9" strokeLinecap="round" fill="none" opacity="0.55" />
    </svg>
  );
}

export function Wordmark({ className }: { className?: string }) {
  return (
    <Link
      href="/"
      className={cn(
        "inline-flex items-center gap-2.5 rounded-md focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background",
        className,
      )}
    >
      <ScholarlyMark className="h-7 w-7" />
      <span className="font-serif text-[1.3rem] font-semibold leading-none tracking-[-0.01em]">Scholarly</span>
    </Link>
  );
}
