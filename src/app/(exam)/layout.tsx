import { requireVerifiedUser } from "@/lib/session";

// Deliberately no app shell here — no sidebar, no topbar, no max-width
// content container. The real Digital SAT app runs as a dedicated
// full-screen kiosk with none of that chrome, so the exam and review pages
// get the entire viewport to themselves, same as the app they're modeled on.
export default async function ExamLayout({ children }: { children: React.ReactNode }) {
  await requireVerifiedUser();
  // dvh, not vh: on a phone 100vh includes the strip behind the browser's own
  // toolbar, which would hide the exam's Back/Next bar.
  return <div className="h-screen w-screen overflow-hidden supports-[height:100dvh]:h-dvh">{children}</div>;
}
