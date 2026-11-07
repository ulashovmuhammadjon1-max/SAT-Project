import type { ExamMode } from "@prisma/client";
import { Flame } from "lucide-react";

import { ExamSwitcher } from "@/components/student/exam-switcher";
import { AppearanceMenu } from "@/components/shared/appearance-menu";
import { NotificationBell } from "@/components/notifications/notification-bell";
import { UserMenu } from "@/components/shared/user-menu";
import { isTeacher } from "@/server/actions/teacher/classes";
import { getCurrentUser } from "@/lib/session";
import { prisma } from "@/lib/prisma";

export async function StudentTopbar({ activeExam = "SAT" }: { activeExam?: ExamMode }) {
  const sessionUser = await getCurrentUser();
  if (!sessionUser) return null;

  const user = await prisma.user.findUnique({
    where: { id: sessionUser.id },
    select: { name: true, email: true, image: true, currentStreak: true, role: true },
  });
  const teaching = user ? await isTeacher(sessionUser.id, user.email ?? null) : false;

  return (
    <header className="flex h-16 items-center justify-between border-b border-border bg-background/80 px-4 backdrop-blur sm:px-6">
      {/* The sidebar carries the switcher on desktop; the topbar copy exists
          for screens where the sidebar is hidden. */}
      <div className="flex items-center gap-3 lg:hidden">
        <ExamSwitcher active={activeExam} />
      </div>
      <div className="hidden lg:block" />
      <div className="flex items-center gap-2 sm:gap-3">
        <div className="flex items-center gap-1.5 rounded-full bg-warning/15 px-2.5 py-1.5 text-sm font-semibold text-warning-foreground sm:px-3">
          <Flame className="h-4 w-4 text-warning" />
          {user?.currentStreak ?? 0}
          <span className="hidden sm:inline">day streak</span>
        </div>
        <NotificationBell />
        <AppearanceMenu />
        <UserMenu
          name={user?.name}
          email={user?.email}
          image={user?.image}
          role={user?.role}
          teaching={teaching}
        />
      </div>
    </header>
  );
}
