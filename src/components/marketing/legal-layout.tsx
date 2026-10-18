import Link from "next/link";

import { SiteNav } from "@/components/marketing/site-nav";

/**
 * Shell for the Terms and Privacy pages.
 *
 * Uses the marketing nav so a visitor reading the policy is still on the same
 * site, and a prose column narrow enough to actually read.
 */
export function LegalLayout({
  title,
  updated,
  children,
}: {
  title: string;
  updated: string;
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-background">
      <SiteNav />
      <main id="main" className="mx-auto w-full max-w-3xl px-4 py-16 sm:px-6 lg:px-8 lg:py-20">
        <p className="text-[13px] text-muted-foreground">Last updated {updated}</p>
        <h1 className="mt-3 font-serif text-[2.4rem] font-medium leading-tight tracking-[-0.015em]">{title}</h1>
        <div className="mt-10 space-y-10 border-t border-border pt-10">{children}</div>
        <div className="mt-16 border-t border-border pt-6 text-sm text-muted-foreground">
          <Link href="/terms" className="hover:text-foreground">
            Terms
          </Link>
          {" · "}
          <Link href="/privacy" className="hover:text-foreground">
            Privacy
          </Link>
          {" · "}
          <Link href="/" className="hover:text-foreground">
            Home
          </Link>
        </div>
      </main>
    </div>
  );
}

export function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section>
      <h2 className="font-serif text-[1.4rem] font-medium leading-snug">{title}</h2>
      <div className="mt-3 max-w-[40rem] space-y-3 text-[16px] leading-[1.7] text-foreground/80 [&_a]:underline [&_a]:underline-offset-4">
        {children}
      </div>
    </section>
  );
}
