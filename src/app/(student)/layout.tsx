import { requireVerifiedUser } from "@/lib/session";
import { StudentSidebar } from "@/components/student/student-sidebar";
import { StudentTopbar } from "@/components/student/student-topbar";

export default async function StudentLayout({ children }: { children: React.ReactNode }) {
  await requireVerifiedUser();

  return (
    <div className="flex min-h-screen bg-secondary/30">
      <StudentSidebar />
      <div className="flex min-w-0 flex-1 flex-col">
        <StudentTopbar />
        <main className="flex-1 overflow-y-auto p-4 sm:p-6 lg:p-8">
          <div className="mx-auto max-w-6xl animate-fade-in">{children}</div>
        </main>
      </div>
    </div>
  );
}
