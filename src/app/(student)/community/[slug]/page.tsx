import { notFound } from "next/navigation";

import { ChannelView } from "@/components/community/channel-view";
import { listChannels, listMessages } from "@/server/actions/student/community";

export const dynamic = "force-dynamic";

export async function generateMetadata({ params }: { params: { slug: string } }) {
  const channel = (await listChannels()).find((c) => c.slug === params.slug);
  return { title: channel ? `#${channel.name}` : "Community" };
}

export default async function ChannelPage({ params }: { params: { slug: string } }) {
  const channel = (await listChannels()).find((c) => c.slug === params.slug);
  if (!channel) notFound();

  const { messages, hasMore } = await listMessages(params.slug);

  return (
    <ChannelView
      channelSlug={channel.slug}
      channelName={channel.name}
      description={channel.description}
      isReadOnly={channel.isReadOnly}
      initialMessages={messages}
      initialHasMore={hasMore}
    />
  );
}
