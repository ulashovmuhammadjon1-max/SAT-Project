import Link from "next/link";
import { GraduationCap } from "lucide-react";

export default function AuthLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="grid min-h-screen lg:grid-cols-2">
      <div className="flex flex-col justify-center px-6 py-12 sm:px-12 lg:px-20">
        <Link href="/" className="mb-10 flex items-center gap-2">
          <span className="flex h-9 w-9 items-center justify-center rounded-lg bg-navy-900 text-white">
            <GraduationCap className="h-5 w-5" />
          </span>
          <span className="font-display text-lg font-semibold tracking-tight">Summit Prep</span>
        </Link>
        <div className="mx-auto w-full max-w-sm animate-fade-up">{children}</div>
      </div>
      <div className="relative hidden overflow-hidden bg-navy-950 lg:block">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_20%_20%,_hsl(226_84%_30%/0.5),_transparent_45%),radial-gradient(circle_at_80%_70%,_hsl(226_84%_40%/0.35),_transparent_50%)]" />
        <div className="relative z-10 flex h-full flex-col justify-between p-16 text-white">
          <div />
          <div className="max-w-md space-y-4">
            <p className="font-display text-3xl font-semibold leading-tight text-balance">
              Practice the exact way you&apos;ll test.
            </p>
            <p className="text-navy-200">
              Full-length adaptive Digital SAT practice tests, a Bluebook-accurate exam interface, and
              analytics that show exactly what to study next.
            </p>
          </div>
          <p className="text-sm text-navy-300">© {new Date().getFullYear()} Summit Prep</p>
        </div>
      </div>
    </div>
  );
}
