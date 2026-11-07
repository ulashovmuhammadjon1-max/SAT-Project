import { notFound } from "next/navigation";

import { ChannelView } from "@/components/community/channel-view";
import { requireUser } from "@/lib/session";
import type { MessageKind } from "@/lib/community/types";
import { listChannels, listMessages, listPinned, myRestriction } from "@/server/actions/student/community";

export const dynamic = "force-dynamic";

export async function generateMetadata({ params }: { params: { slug: string } }) {
  const channel = (await listChannels()).find((c) => c.slug === params.slug);
  return { title: channel ? `#${channel.name} · Community` : "Community" };
}

const KINDS: MessageKind[] = ["QUESTION", "RESOURCE", "ACHIEVEMENT", "POLL", "ANNOUNCEMENT"];

export default async function ChannelPage({
  params,
  searchParams,
}: {
  params: { slug: string };
  searchParams: { m?: string; thread?: string; compose?: string };
}) {
  const user = await requireUser();
  const channel = (await listChannels()).find((c) => c.slug === params.slug);
  if (!channel) notFound();

  const [{ messages, hasMore }, pinned, restriction] = await Promise.all([
    listMessages(params.slug),
    listPinned(params.slug),
    myRestriction(),
  ]);
  const compose = KINDS.find((k) => k === searchParams.compose?.toUpperCase()) ?? undefined;

  return (
    <ChannelView
      // A new link target (from a notification or search) remounts the view so
      // it scrolls to that message; opening a thread from inside does not.
      key={`${channel.slug}:${searchParams.m ?? ""}:${compose ?? ""}`}
      channel={channel}
      initialMessages={messages}
      initialHasMore={hasMore}
      initialPinned={pinned}
      isAdmin={user.role === "ADMIN"}
      restriction={restriction}
      initialThread={searchParams.thread ?? null}
      focusMessage={searchParams.m ?? null}
      initialKind={compose}
    />
  );
}
