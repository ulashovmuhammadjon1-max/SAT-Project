import Link from "next/link";
import { ScholarlyMark } from "@/components/marketing/wordmark";

/**
 * Auth shell.
 *
 * A single centered column on a soft, near-white ground — the premium,
 * minimal frame the sign-in page is designed around. The individual pages
 * supply their own card (see the login page), so this layout stays neutral
 * and every auth screen — login, forgot/reset password, verify email — sits
 * in the same calm, centered space rather than the old two-column split.
 */
export default function AuthLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-background px-4 py-10 sm:py-16">
      <header>
        <Link
          href="/"
          className="mb-8 inline-flex items-center gap-2.5 rounded-md text-foreground transition-opacity hover:opacity-80 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
          aria-label="Scholarly home"
        >
          <ScholarlyMark className="h-8 w-8" />
          <span className="font-serif text-[1.35rem] font-semibold">Scholarly</span>
        </Link>
      </header>

      <main className="w-full max-w-[420px] animate-fade-up">{children}</main>

      <footer className="mt-8 text-xs text-muted-foreground">
        © {new Date().getFullYear()} Scholarly
      </footer>
    </div>
  );
}
