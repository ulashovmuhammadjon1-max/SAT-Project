import { ChannelNav } from "@/components/community/channel-nav";
import { listChannels } from "@/server/actions/student/community";

export const metadata = { title: "Community" };
export const dynamic = "force-dynamic";

export default async function CommunityLayout({ children }: { children: React.ReactNode }) {
  const channels = await listChannels();

  return (
    // Fills the viewport below the topbar rather than sitting in a short box.
    // A chat that occupies a third of the screen feels like a widget; students
    // treat it as one and never settle into it.
    <div className="flex h-[calc(100vh-9rem)] flex-col gap-3">
      <div className="shrink-0">
        <h1 className="font-display text-xl font-semibold tracking-tight">Community</h1>
        <p className="text-sm text-muted-foreground">
          Ask questions, share what worked, help someone else out.
        </p>
      </div>

      <div className="grid min-h-0 flex-1 gap-4 lg:grid-cols-[15rem_1fr]">
        <div className="lg:overflow-y-auto">
          <ChannelNav channels={channels} />
        </div>
        <div className="flex min-h-0 min-w-0 flex-col">{children}</div>
      </div>
    </div>
  );
}
