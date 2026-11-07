import { CommunityAdmin } from "@/components/admin/community-admin";
import { requireAdmin } from "@/lib/session";
import { getCommunityAdmin } from "@/server/actions/admin/community";

export const metadata = { title: "Community" };
export const dynamic = "force-dynamic";

export default async function CommunityAdminPage() {
  await requireAdmin();
  return <CommunityAdmin data={await getCommunityAdmin()} />;
}
