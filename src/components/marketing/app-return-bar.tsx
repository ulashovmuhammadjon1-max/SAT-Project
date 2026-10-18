import Link from "next/link";
import { ArrowLeft } from "lucide-react";

import { ScholarlyMark } from "@/components/marketing/wordmark";

/**
 * Shown instead of the marketing SiteNav when a signed-in student lands on a
 * public page (Team, For Schools) from inside the app. The marketing nav's
 * links all lead to the landing page — pressing any of them threw students out
 * of the app, which read as a bug. This bar leads back to where they came from.
 */
export function AppReturnBar({ backHref, backLabel }: { backHref: string; backLabel: string }) {
  return (
    <header className="sticky top-0 z-50 border-b border-border bg-background/95">
      <div className="mx-auto flex h-14 max-w-6xl items-center justify-between px-4 sm:px-6 lg:px-8">
        <Link
          href={backHref}
          className="inline-flex items-center gap-1.5 rounded-md text-sm font-medium text-muted-foreground transition-colors hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
        >
          <ArrowLeft className="h-4 w-4" />
          {backLabel}
        </Link>
        <Link href="/dashboard" className="flex items-center gap-2 rounded-md focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring">
          <ScholarlyMark className="h-6 w-6" />
          <span className="font-serif text-[1.1rem] font-semibold">Scholarly</span>
        </Link>
      </div>
    </header>
  );
}
