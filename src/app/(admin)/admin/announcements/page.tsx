import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { AnnouncementForm } from "@/components/admin/announcement-form";
import { AnnouncementToggle } from "@/components/admin/announcement-toggle";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "Announcements" };
export const dynamic = "force-dynamic";

export default async function AdminAnnouncementsPage() {
  const announcements = await prisma.announcement.findMany({ orderBy: { createdAt: "desc" } });

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Announcements</h1>
        <p className="text-sm text-muted-foreground">Broadcast messages shown to students, admins, or everyone.</p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>New announcement</CardTitle>
        </CardHeader>
        <CardContent>
          <AnnouncementForm />
        </CardContent>
      </Card>

      <div className="space-y-3">
        {announcements.map((a) => (
          <Card key={a.id}>
            <CardContent className="flex items-start justify-between gap-4 p-5">
              <div>
                <div className="mb-1 flex items-center gap-2">
                  <p className="font-medium">{a.title}</p>
                  <Badge variant="outline">{a.audience}</Badge>
                </div>
                <p className="text-sm text-muted-foreground">{a.body}</p>
              </div>
              <AnnouncementToggle id={a.id} isActive={a.isActive} />
            </CardContent>
          </Card>
        ))}
        {announcements.length === 0 && <p className="text-sm text-muted-foreground">No announcements yet.</p>}
      </div>
    </div>
  );
}
