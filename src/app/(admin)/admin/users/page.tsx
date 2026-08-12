import Link from "next/link";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { UserRoleSelect } from "@/components/admin/user-role-select";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "Users" };
export const dynamic = "force-dynamic";

export default async function AdminUsersPage() {
  const users = await prisma.user.findMany({
    orderBy: { createdAt: "desc" },
    include: { _count: { select: { attempts: true } } },
  });

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Users</h1>
        <p className="text-sm text-muted-foreground">{users.length} accounts</p>
      </div>

      <Card>
        <CardContent className="p-0">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Name</TableHead>
                <TableHead>Email</TableHead>
                <TableHead>Role</TableHead>
                <TableHead>Attempts</TableHead>
                <TableHead>Streak</TableHead>
                <TableHead>Joined</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {users.map((user) => (
                <TableRow key={user.id}>
                  <TableCell className="font-medium">
                    {/* Only students have a profile page — it has nothing to
                        show for an admin account, so it 404s on one. */}
                    {user.role === "STUDENT" ? (
                      <Link
                        href={`/admin/statistics/students/${user.id}`}
                        className="hover:text-primary hover:underline"
                      >
                        {user.name ?? "—"}
                      </Link>
                    ) : (
                      (user.name ?? "—")
                    )}
                  </TableCell>
                  <TableCell className="text-sm text-muted-foreground">{user.email}</TableCell>
                  <TableCell>
                    <UserRoleSelect userId={user.id} role={user.role} />
                  </TableCell>
                  <TableCell className="text-sm">{user._count.attempts}</TableCell>
                  <TableCell className="text-sm">
                    <Badge variant="outline">{user.currentStreak} days</Badge>
                  </TableCell>
                  <TableCell className="text-sm text-muted-foreground">
                    {user.createdAt.toLocaleDateString()}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
