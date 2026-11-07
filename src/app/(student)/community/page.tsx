import { CommunityHomeView } from "@/components/community/home";
import { getCommunityHome, listCategories } from "@/server/actions/student/community";

export const dynamic = "force-dynamic";

export default async function CommunityHomePage() {
  const [data, categories] = await Promise.all([getCommunityHome(), listCategories()]);
  return <CommunityHomeView data={data} categories={categories} />;
}
