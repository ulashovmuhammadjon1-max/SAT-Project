import { CommunityShell } from "@/components/community/community-shell";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { displayName } from "@/lib/community/server";
import { listCategories } from "@/server/actions/student/community";

export const metadata = { title: "Community" };
export const dynamic = "force-dynamic";

export default async function CommunityLayout({ children }: { children: React.ReactNode }) {
  const user = await requireUser();
  const [categories, me] = await Promise.all([
    listCategories(),
    prisma.user.findUnique({ where: { id: user.id }, select: { name: true, image: true } }),
  ]);
  return (
    <CommunityShell
      initialCategories={categories}
      me={{ id: user.id, name: displayName(me?.name, user.role), image: me?.image ?? null }}
      isAdmin={user.role === "ADMIN"}
    >
      {children}
    </CommunityShell>
  );
}
