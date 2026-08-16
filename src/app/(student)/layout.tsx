import { requireVerifiedUser } from "@/lib/session";
import { examContextOrDefault } from "@/lib/exam/mode";
import { StudentSidebar } from "@/components/student/student-sidebar";
import { StudentTopbar } from "@/components/student/student-topbar";
import { StudentContainer } from "@/components/student/student-container";

export default async function StudentLayout({ children }: { children: React.ReactNode }) {
  await requireVerifiedUser();
  // Resolved once here and passed down, so the sidebar and the topbar cannot
  // disagree about which exam the student is in.
  const exam = await examContextOrDefault();

  return (
    <div className="flex min-h-screen bg-secondary/30">
      <StudentSidebar activeExam={exam.active} />
      <div className="flex min-w-0 flex-1 flex-col">
        <StudentTopbar activeExam={exam.active} />
        <main className="flex-1 overflow-y-auto p-4 sm:p-6 lg:p-8">
          <StudentContainer>{children}</StudentContainer>
        </main>
      </div>
    </div>
  );
}
