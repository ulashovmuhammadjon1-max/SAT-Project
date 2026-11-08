import Link from "next/link";
import { Eye } from "lucide-react";

import { AdminMobileNav } from "@/components/admin/admin-sidebar";
import { UserMenu } from "@/components/shared/user-menu";
import { getCurrentUser } from "@/lib/session";

export async function AdminTopbar() {
  const user = await getCurrentUser();

  return (
    <header className="sticky top-0 z-30 flex h-16 shrink-0 items-center gap-2 pt-[env(safe-area-inset-top)] lg:static justify-between border-b border-border bg-background/80 px-4 backdrop-blur sm:px-6">
      <div className="flex min-w-0 items-center gap-2 sm:gap-3">
        <AdminMobileNav />
        {/* Deliberately not a "back" link — it always jumps to the live
            student dashboard, leaving the admin panel entirely, so it must
            not look like in-app back navigation (no arrow, explicit verb). */}
        <Link
          href="/dashboard"
          className="flex h-10 items-center gap-1.5 whitespace-nowrap text-sm text-muted-foreground hover:text-foreground"
        >
          <Eye className="h-3.5 w-3.5" /> View as student
        </Link>
      </div>
      {user && <UserMenu name={user.name} email={user.email} image={user.image} role={user.role} />}
    </header>
  );
}
