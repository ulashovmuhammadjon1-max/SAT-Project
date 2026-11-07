import Link from "next/link";
import { Search } from "lucide-react";
import type { Prisma } from "@prisma/client";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { UserRoleSelect } from "@/components/admin/user-role-select";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "Users" };
export const dynamic = "force-dynamic";

/** Rows per page. The full list is ~2,200 accounts; rendering all of them,
 *  each with its own role selector, made the page slow to open and scroll. */
const PAGE_SIZE = 100;

/**
 * Search runs on the server through a plain GET form (?q=), so it needs no
 * client script, the URL can be bookmarked or shared, and Back returns to the
 * previous search. It matches username, email or name, case-insensitively and
 * on any part of the text. A leading "@" is ignored, so "@alisher" finds the
 * username "alisher".
 */
export default async function AdminUsersPage({
  searchParams,
}: {
  searchParams: { q?: string; page?: string };
}) {
  const q = (searchParams.q ?? "").trim().replace(/^@/, "");
  const page = Math.max(1, Number.parseInt(searchParams.page ?? "1", 10) || 1);

  const where: Prisma.UserWhereInput = q
    ? {
        OR: [
          { username: { contains: q, mode: "insensitive" } },
          { email: { contains: q, mode: "insensitive" } },
          { name: { contains: q, mode: "insensitive" } },
        ],
      }
    : {};

  const [total, matching, users] = await Promise.all([
    prisma.user.count(),
    q ? prisma.user.count({ where }) : Promise.resolve(null),
    prisma.user.findMany({
      where,
      orderBy: { createdAt: "desc" },
      skip: (page - 1) * PAGE_SIZE,
      take: PAGE_SIZE,
      select: {
        id: true,
        name: true,
        username: true,
        email: true,
        role: true,
        currentStreak: true,
        createdAt: true,
        _count: { select: { attempts: true } },
      },
    }),
  ]);

  const count = matching ?? total;
  const pages = Math.max(1, Math.ceil(count / PAGE_SIZE));
  const pageHref = (p: number) => {
    const params = new URLSearchParams();
    if (q) params.set("q", q);
    if (p > 1) params.set("page", String(p));
    const s = params.toString();
    return s ? `/admin/users?${s}` : "/admin/users";
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Users</h1>
        <p className="text-sm text-muted-foreground">
          {q ? (
            <>
              {count} of {total} accounts match &ldquo;{q}&rdquo;
            </>
          ) : (
            <>{total} accounts</>
          )}
        </p>
      </div>

      <form action="/admin/users" method="get" role="search" className="flex max-w-xl gap-2">
        <div className="relative flex-1">
          <Search
            aria-hidden
            className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground"
          />
          <Input
            type="search"
            name="q"
            defaultValue={q}
            placeholder="Search by username, email or name"
            aria-label="Search users by username, email or name"
            autoComplete="off"
            className="pl-9"
          />
        </div>
        <Button type="submit">Search</Button>
        {q && (
          <Button variant="outline" asChild>
            <Link href="/admin/users">Clear</Link>
          </Button>
        )}
      </form>

      <Card>
        <CardContent className="p-0">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Name</TableHead>
                <TableHead>Username</TableHead>
                <TableHead>Email</TableHead>
                <TableHead>Role</TableHead>
                <TableHead>Attempts</TableHead>
                <TableHead>Streak</TableHead>
                <TableHead>Joined</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {users.length === 0 && (
                <TableRow>
                  <TableCell colSpan={7} className="py-10 text-center text-sm text-muted-foreground">
                    {q ? <>No account matches &ldquo;{q}&rdquo;.</> : "No accounts yet."}
                  </TableCell>
                </TableRow>
              )}
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
                  <TableCell className="text-sm text-muted-foreground">
                    {user.username ? `@${user.username}` : "—"}
                  </TableCell>
                  <TableCell className="text-sm text-muted-foreground">{user.email ?? "—"}</TableCell>
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

      {pages > 1 && (
        <nav aria-label="Pages" className="flex items-center justify-between text-sm">
          <span className="text-muted-foreground">
            Page {Math.min(page, pages)} of {pages}
          </span>
          <div className="flex gap-2">
            {page > 1 ? (
              <Button variant="outline" size="sm" asChild>
                <Link href={pageHref(page - 1)}>Previous</Link>
              </Button>
            ) : (
              <Button variant="outline" size="sm" disabled>
                Previous
              </Button>
            )}
            {page < pages ? (
              <Button variant="outline" size="sm" asChild>
                <Link href={pageHref(page + 1)}>Next</Link>
              </Button>
            ) : (
              <Button variant="outline" size="sm" disabled>
                Next
              </Button>
            )}
          </div>
        </nav>
      )}
    </div>
  );
}
