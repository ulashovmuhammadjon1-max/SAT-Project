import Link from "next/link";
import { ArrowLeft, GraduationCap } from "lucide-react";

/**
 * Shown instead of the marketing SiteNav when a signed-in student lands on a
 * public page (Journal, For Schools) from inside the app. The marketing nav's
 * links all lead to the landing page — pressing any of them threw students out
 * of the app, which read as a bug. This bar leads back to where they came from.
 */
export function AppReturnBar({ backHref, backLabel }: { backHref: string; backLabel: string }) {
  return (
    <header className="sticky top-0 z-50 border-b border-border/60 bg-background/80 backdrop-blur-xl">
      <div className="mx-auto flex h-14 max-w-6xl items-center justify-between px-4 sm:px-6 lg:px-8">
        <Link
          href={backHref}
          className="inline-flex items-center gap-1.5 text-sm font-medium text-muted-foreground transition-colors hover:text-foreground"
        >
          <ArrowLeft className="h-4 w-4" />
          {backLabel}
        </Link>
        <Link href="/dashboard" className="flex items-center gap-2">
          <span className="flex h-7 w-7 items-center justify-center rounded-lg bg-navy-900 text-white">
            <GraduationCap className="h-3.5 w-3.5" />
          </span>
          <span className="font-display text-[15px] font-semibold tracking-tight">Scholarly</span>
        </Link>
      </div>
    </header>
  );
}
