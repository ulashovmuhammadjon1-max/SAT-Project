import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { CreateClassForm } from "@/components/admin/create-class-form";
import { ClassTeacherForm } from "@/components/admin/class-teacher-form";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "Schools" };
export const dynamic = "force-dynamic";

export default async function AdminSchoolsPage() {
  await requireAdmin();

  const classes = await prisma.schoolClass.findMany({
    orderBy: { createdAt: "desc" },
    include: {
      memberships: {
        select: {
          joinedAt: true,
          user: {
            select: {
              id: true,
              name: true,
              email: true,
              _count: { select: { attempts: { where: { status: "SUBMITTED" } } } },
            },
          },
        },
        orderBy: { joinedAt: "asc" },
      },
    },
  });

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Schools</h1>
        <p className="text-sm text-muted-foreground">
          Pilot classes. Create one per teacher, hand over the code, and their students join from
          the My Class page.
        </p>
      </div>

      <Card className="max-w-3xl">
        <CardHeader>
          <CardTitle className="text-base">New class</CardTitle>
          <CardDescription>The join code is generated on creation — copy it from here.</CardDescription>
        </CardHeader>
        <CardContent>
          <CreateClassForm />
        </CardContent>
      </Card>

      {classes.map((c) => (
        <Card key={c.id} className={c.isArchived ? "opacity-60" : undefined}>
          <CardHeader className="pb-3">
            <div className="flex flex-wrap items-center gap-2">
              <CardTitle className="text-base">{c.name}</CardTitle>
              <Badge variant="outline" className="font-mono tracking-widest">{c.code}</Badge>
              {c.isArchived && <Badge variant="destructive">Archived</Badge>}
              <span className="ml-auto text-xs text-muted-foreground">
                {c.school} · {c.teacherName}
                {c.teacherEmail ? ` · ${c.teacherEmail}` : ""}
              </span>
            </div>
          </CardHeader>
          <CardContent>
            <ClassTeacherForm
              classId={c.id}
              teacherName={c.teacherName}
              teacherEmail={c.teacherEmail}
            />
            {c.memberships.length === 0 ? (
              <p className="mt-4 text-sm text-muted-foreground">No students have joined yet.</p>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b border-border text-left text-xs uppercase tracking-wide text-muted-foreground">
                      <th className="py-2 pr-4 font-medium">Student</th>
                      <th className="py-2 pr-4 font-medium">Email</th>
                      <th className="py-2 pr-4 font-medium">Joined</th>
                      <th className="py-2 font-medium">Tests completed</th>
                    </tr>
                  </thead>
                  <tbody>
                    {c.memberships.map((m) => (
                      <tr key={m.user.id} className="border-b border-border/60">
                        <td className="py-2 pr-4 font-medium">{m.user.name ?? "—"}</td>
                        <td className="py-2 pr-4 text-muted-foreground">{m.user.email}</td>
                        <td className="py-2 pr-4 text-muted-foreground">
                          {m.joinedAt.toLocaleDateString(undefined, { month: "short", day: "numeric" })}
                        </td>
                        <td className="py-2 tabular-nums">{m.user._count.attempts}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
