import { MessagesView } from "@/components/community/messages-view";
import { listConversations } from "@/server/actions/student/community-dm";

export const metadata = { title: "Messages · Community" };
export const dynamic = "force-dynamic";

export default async function MessagesPage() {
  return <MessagesView initialList={await listConversations()} conversation={null} />;
}
