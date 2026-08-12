import { redirect } from "next/navigation";

import { listChannels } from "@/server/actions/student/community";

export const dynamic = "force-dynamic";

/** No channel chosen — open one rather than showing an empty shell. */
export default async function CommunityIndex() {
  const channels = await listChannels();
  if (!channels.length) {
    return (
      <p className="rounded-xl border bg-card p-10 text-center text-sm text-muted-foreground">
        No channels have been created yet.
      </p>
    );
  }

  // Prefer somewhere they can actually post. Announcements sorts first in the
  // sidebar (that is where a pinned channel belongs), but landing a student in
  // a read-only channel makes the whole feature look broken — the first thing
  // they see is a composer telling them they cannot type.
  const landing = channels.find((c) => !c.isReadOnly) ?? channels[0];
  redirect(`/community/${landing.slug}`);
}
