import { SearchView } from "@/components/community/search-view";
import { listChannels } from "@/server/actions/student/community";

export const metadata = { title: "Search · Community" };
export const dynamic = "force-dynamic";

export default async function CommunitySearchPage() {
  return <SearchView channels={await listChannels()} />;
}
