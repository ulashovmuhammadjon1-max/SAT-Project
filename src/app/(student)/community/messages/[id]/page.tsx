import { notFound } from "next/navigation";

import { MessagesView } from "@/components/community/messages-view";
import { getConversation, listConversations } from "@/server/actions/student/community-dm";

export const metadata = { title: "Messages · Community" };
export const dynamic = "force-dynamic";

export default async function ConversationPage({ params }: { params: { id: string } }) {
  const [list, conversation] = await Promise.all([listConversations(), getConversation(params.id)]);
  // Not a member: the same 404 as a conversation that does not exist.
  if (!conversation) notFound();
  return <MessagesView initialList={list} conversation={conversation} />;
}
