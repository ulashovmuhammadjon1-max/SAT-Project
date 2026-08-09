import { Flame } from "lucide-react";

import { ThemeToggleCompact } from "@/components/shared/theme-toggle";
import { UserMenu } from "@/components/shared/user-menu";
import { getCurrentUser } from "@/lib/session";
import { prisma } from "@/lib/prisma";

export async function StudentTopbar() {
  const sessionUser = await getCurrentUser();
  if (!sessionUser) return null;

  const user = await prisma.user.findUnique({
    where: { id: sessionUser.id },
    select: { name: true, email: true, image: true, currentStreak: true, role: true },
  });

  return (
    <header className="flex h-16 items-center justify-between border-b border-border bg-background/80 px-4 backdrop-blur sm:px-6">
      <div />
      <div className="flex items-center gap-4">
        <div className="flex items-center gap-1.5 rounded-full bg-warning/15 px-3 py-1.5 text-sm font-semibold text-warning-foreground">
          <Flame className="h-4 w-4 text-warning" />
          {user?.currentStreak ?? 0} day streak
        </div>
        <ThemeToggleCompact />
        <UserMenu name={user?.name} email={user?.email} image={user?.image} role={user?.role} />
      </div>
    </header>
  );
}
