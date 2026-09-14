import Link from "next/link";
import { GraduationCap } from "lucide-react";

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
    <div className="flex min-h-screen flex-col items-center justify-center bg-muted/40 px-4 py-10 sm:py-16">
      <Link
        href="/"
        className="mb-8 inline-flex items-center gap-2 text-foreground/90 transition-opacity hover:opacity-80"
        aria-label="Scholarly home"
      >
        <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-navy-900 text-white">
          <GraduationCap className="h-5 w-5" />
        </span>
        <span className="font-display text-lg font-semibold tracking-tight">Scholarly</span>
      </Link>

      <main className="w-full max-w-[420px] animate-fade-up">{children}</main>

      <p className="mt-8 text-xs text-muted-foreground">
        © {new Date().getFullYear()} Scholarly
      </p>
    </div>
  );
}
