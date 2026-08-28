import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { TeamMemberForm } from "@/components/admin/team-member-form";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "Team Page" };
export const dynamic = "force-dynamic";

export default async function AdminTeamPage() {
  await requireAdmin();

  const members = await prisma.teamMember.findMany({
    orderBy: [{ order: "asc" }, { createdAt: "asc" }],
  });

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Team page</h1>
        <p className="text-sm text-muted-foreground">
          Who appears on the public /team page. Approved peer mentors are added there
          automatically; this list is for the core team.
        </p>
      </div>

      <Card className="max-w-3xl">
        <CardHeader>
          <CardTitle className="text-base">Add a member</CardTitle>
          <CardDescription>Photo is optional but makes the page far more credible.</CardDescription>
        </CardHeader>
        <CardContent>
          <TeamMemberForm />
        </CardContent>
      </Card>

      {members.map((m) => (
        <Card key={m.id} className={`max-w-3xl ${m.isActive ? "" : "opacity-60"}`}>
          <CardHeader className="pb-3">
            <div className="flex items-center gap-2">
              <CardTitle className="text-base">{m.name}</CardTitle>
              <Badge variant="outline">{m.title}</Badge>
              {!m.isActive && <Badge variant="destructive">Hidden</Badge>}
            </div>
          </CardHeader>
          <CardContent>
            <TeamMemberForm
              initial={{
                id: m.id,
                name: m.name,
                title: m.title,
                email: m.email ?? "",
                bio: m.bio ?? "",
                photo: m.photo,
                order: m.order,
                isActive: m.isActive,
              }}
            />
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
