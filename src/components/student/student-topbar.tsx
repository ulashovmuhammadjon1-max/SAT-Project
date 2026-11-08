import type { ExamMode } from "@prisma/client";
import Link from "next/link";
import { Flame, GraduationCap } from "lucide-react";

import { ExamSwitcher } from "@/components/student/exam-switcher";
import { MobileNavTrigger } from "@/components/student/student-mobile-nav";
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
    <header className="sticky top-0 z-30 flex h-16 shrink-0 items-center justify-between gap-2 border-b border-border bg-background/80 px-4 pt-[env(safe-area-inset-top)] backdrop-blur sm:px-6 lg:static">
      {/* The sidebar carries the brand and the switcher on desktop. Below lg
          the top bar holds the menu button and the brand; the exam switcher
          joins them on tablets, and on phones it lives in the drawer. */}
      <div className="flex min-w-0 items-center gap-2 lg:hidden">
        <MobileNavTrigger />
        <Link href="/dashboard" className="flex min-w-0 items-center gap-2" aria-label="Scholarly home">
          <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-navy-900 text-white">
            <GraduationCap className="h-4 w-4" />
          </span>
          <span className="hidden font-display text-base font-semibold min-[400px]:inline">Scholarly</span>
        </Link>
        <div className="ml-2 hidden md:block">
          <ExamSwitcher active={activeExam} />
        </div>
      </div>
      <div className="hidden lg:block" />
      <div className="flex shrink-0 items-center gap-1.5 sm:gap-3">
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
