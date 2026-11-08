import Link from "next/link";
import { ArrowRight, BookOpenText, CalendarCheck, FlaskConical, Languages, UserPlus, Users } from "lucide-react";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { countedStudentWhere } from "@/lib/counted-students";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "Admin Overview" };
export const dynamic = "force-dynamic";

const DAY = 24 * 60 * 60 * 1000;

/**
 * The Scholarly overview — the whole platform at a glance, and the landing page
 * of the admin panel. Each product (SAT, IELTS, Research) has its own section
 * and overview; this page answers "how is the community doing, and what is
 * waiting on me?" across all of them.
 *
 * Every query is a count, so the page stays cheap however large the tables get.
 */
export default async function AdminOverviewPage() {
  const admin = await requireAdmin();
  const now = new Date();
  const [
    students,
    newThisWeek,
    newThisMonth,
    upcomingSessions,
    pendingProposals,
    pendingMentorApps,
    pendingSessionRequests,
    ieltsQueue,
    satUploadsToReview,
  ] = await Promise.all([
    prisma.user.count({ where: countedStudentWhere }),
    prisma.user.count({ where: { AND: [countedStudentWhere, { createdAt: { gte: new Date(now.getTime() - 7 * DAY) } }] } }),
    prisma.user.count({ where: { AND: [countedStudentWhere, { createdAt: { gte: new Date(now.getTime() - 30 * DAY) } }] } }),
    prisma.booking.count({ where: { status: "UPCOMING", slot: { hostId: admin.id, startsAt: { gte: now } } } }),
    prisma.researchProposal.count({ where: { status: "PENDING" } }),
    prisma.peerMentorApplication.count({ where: { status: "PENDING" } }),
    prisma.booking.count({ where: { status: "PENDING", slot: { hostId: admin.id } } }),
    Promise.all([
      prisma.ieltsWritingSubmission.count({ where: { status: { in: ["ASSIGNED", "IN_REVIEW"] } } }),
      prisma.ieltsSpeakingSubmission.count({ where: { status: { in: ["ASSIGNED", "IN_REVIEW"] } } }),
    ]).then(([w, s]) => w + s),
    prisma.pDFUpload.count({ where: { status: "NEEDS_REVIEW" } }),
  ]);

  const stats = [
    { label: "Students", value: students, icon: Users },
    { label: "New this week", value: newThisWeek, icon: UserPlus },
    { label: "New in 30 days", value: newThisMonth, icon: UserPlus },
    { label: "Your upcoming sessions", value: upcomingSessions, icon: CalendarCheck },
  ];

  const queue = [
    { label: "Research proposals awaiting a decision", value: pendingProposals, href: "/admin/research" },
    { label: "Peer-mentor applications to review", value: pendingMentorApps, href: "/admin/peer-mentors" },
    { label: "Requests for your sessions to approve", value: pendingSessionRequests, href: "/admin/bookings" },
    { label: "IELTS Writing and Speaking reviews in the queue", value: ieltsQueue, href: "/admin/ielts" },
    { label: "SAT PDF uploads that need review", value: satUploadsToReview, href: "/admin/uploads" },
  ];

  const sections = [
    { title: "SAT", body: "Tests, question bank, PDF ingestion, vocabulary.", href: "/admin/sat", icon: BookOpenText },
    { title: "IELTS", body: "Writing and Speaking reviews, essays, papers.", href: "/admin/ielts", icon: Languages },
    { title: "Research", body: "Student research proposals and decisions.", href: "/admin/research", icon: FlaskConical },
  ];

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Scholarly overview</h1>
        <p className="text-sm text-muted-foreground">The whole platform at a glance, and what is waiting on you.</p>
      </div>

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat) => (
          <Card key={stat.label}>
            <CardContent className="flex items-center justify-between p-6">
              <div>
                <p className="text-sm text-muted-foreground">{stat.label}</p>
                <p className="font-display text-3xl font-semibold">{stat.value}</p>
              </div>
              <span className="flex h-11 w-11 items-center justify-center rounded-xl bg-primary-50 text-primary-600">
                <stat.icon className="h-5 w-5" />
              </span>
            </CardContent>
          </Card>
        ))}
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Needs your attention</CardTitle>
        </CardHeader>
        <CardContent className="space-y-2">
          {queue.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="flex items-center justify-between gap-4 rounded-lg border border-border p-3 transition-colors hover:bg-secondary/60"
            >
              <span className="text-sm">{item.label}</span>
              <span className="flex items-center gap-2">
                <span
                  className={
                    item.value > 0
                      ? "rounded-full bg-warning/15 px-2.5 py-0.5 text-sm font-semibold tabular-nums text-foreground"
                      : "rounded-full bg-secondary px-2.5 py-0.5 text-sm tabular-nums text-muted-foreground"
                  }
                >
                  {item.value}
                </span>
                <ArrowRight className="h-4 w-4 text-muted-foreground" />
              </span>
            </Link>
          ))}
        </CardContent>
      </Card>

      <div className="grid grid-cols-1 gap-4 md:grid-cols-3">
        {sections.map((s) => (
          <Link key={s.href} href={s.href} className="group">
            <Card className="h-full transition-colors group-hover:border-primary/40">
              <CardContent className="flex items-start gap-4 p-6">
                <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-secondary text-foreground">
                  <s.icon className="h-5 w-5" />
                </span>
                <div>
                  <p className="font-semibold">{s.title}</p>
                  <p className="mt-1 text-sm text-muted-foreground">{s.body}</p>
                </div>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}
