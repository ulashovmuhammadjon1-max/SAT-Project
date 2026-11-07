import { BookmarksView } from "@/components/community/bookmarks-view";
import { listBookmarks } from "@/server/actions/student/community";

export const metadata = { title: "Saved · Community" };
export const dynamic = "force-dynamic";

export default async function BookmarksPage() {
  return <BookmarksView initial={await listBookmarks()} />;
}
