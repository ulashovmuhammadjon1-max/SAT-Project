import { SettingsView } from "@/components/community/settings-view";
import { getCommunitySettings, listBlocked } from "@/server/actions/student/community";

export const metadata = { title: "Profile & notifications · Community" };
export const dynamic = "force-dynamic";

export default async function CommunitySettingsPage() {
  const [settings, blocked] = await Promise.all([getCommunitySettings(), listBlocked()]);
  return <SettingsView initial={settings} blocked={blocked} />;
}
