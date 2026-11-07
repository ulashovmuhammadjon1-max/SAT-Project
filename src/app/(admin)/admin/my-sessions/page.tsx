import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import {
  CreateSessionForm,
  DeleteSessionButton,
  EditSessionButton,
  HostDefaultsForm,
} from "@/components/admin/create-session-form";
import { LocalTime } from "@/components/shared/local-time";
import { SEAT_HOLDING_STATUSES } from "@/lib/booking/status";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "My Sessions" };
export const dynamic = "force-dynamic";

/**
 * Every admin's own 1-on-1 sessions: publish one (title, subject, a one-hour
 * time, a Google Meet link) and see who has booked the ones coming up.
 * Requests are still approved on the Sessions page, as for every booking.
 */
export default async function MySessionsPage() {
  const admin = await requireAdmin();

  const [saved, sessions] = await Promise.all([
    prisma.hostProfile.findUnique({
      where: { userId: admin.id },
      select: { meetingUrl: true, defaultSubject: true, defaultTitle: true },
    }),
    prisma.mentorSlot.findMany({
      where: { hostId: admin.id, startsAt: { gt: new Date(Date.now() - 60 * 60_000) } },
      orderBy: { startsAt: "asc" },
      select: {
        id: true,
        startsAt: true,
        title: true,
        subject: true,
        meetingUrl: true,
        bookings: {
          where: { status: { in: SEAT_HOLDING_STATUSES } },
          select: { status: true, name: true },
          take: 1,
        },
      },
    }),
  ]);
  const defaults = {
    meetingUrl: saved?.meetingUrl ?? "",
    defaultSubject: saved?.defaultSubject ?? "",
    defaultTitle: saved?.defaultTitle ?? "",
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">My Sessions</h1>
        <p className="text-sm text-muted-foreground">
          Publish 1-on-1 sessions you will teach. Students book them from their Sessions page, and requests are
          approved on the Sessions page here.
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Create a session</CardTitle>
          <CardDescription>One student, one hour, on your own Google Meet link.</CardDescription>
        </CardHeader>
        <CardContent>
          {/* Keyed on the saved values so a fresh save re-seeds the form. */}
          <CreateSessionForm key={JSON.stringify(defaults)} defaults={defaults} />
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">My saved details</CardTitle>
          <CardDescription>
            Saved for you only. New sessions start with your Meet link, subject and title already filled in.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <HostDefaultsForm defaults={defaults} />
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Your upcoming sessions</CardTitle>
        </CardHeader>
        <CardContent>
          {sessions.length === 0 ? (
            <p className="text-sm text-muted-foreground">No upcoming sessions yet. Create one above.</p>
          ) : (
            <ul className="divide-y divide-border">
              {sessions.map((s) => {
                const booking = s.bookings[0];
                const editable = {
                  id: s.id,
                  title: s.title ?? "",
                  subject: s.subject ?? "",
                  startsAt: s.startsAt.toISOString(),
                  meetingUrl: s.meetingUrl ?? "",
                  // COMPLETED holds a seat too, but only PENDING/UPCOMING lock the time.
                  booked: Boolean(booking && booking.status !== "COMPLETED"),
                };
                return (
                  <li key={s.id} className="flex flex-wrap items-start justify-between gap-3 py-3">
                    <div className="min-w-[240px] flex-1">
                      <p className="text-sm font-medium">{s.title ?? "1-on-1 session"}</p>
                      <p className="text-xs text-muted-foreground">
                        {s.subject ? `${s.subject} · ` : ""}
                        <LocalTime iso={s.startsAt.toISOString()} format="full" /> · 1 hour
                      </p>
                      {s.meetingUrl && (
                        <a
                          href={s.meetingUrl}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="mt-0.5 inline-block text-xs text-primary underline-offset-4 hover:underline"
                        >
                          {s.meetingUrl.replace(/^https:\/\//, "")}
                        </a>
                      )}
                    </div>
                    <div className="flex flex-wrap items-center gap-2">
                      {s.startsAt.getTime() > Date.now() && <EditSessionButton session={editable} />}
                      {booking ? (
                        <Badge variant={booking.status === "PENDING" ? "warning" : "success"}>
                          {booking.status === "PENDING" ? `Requested by ${booking.name}` : `Booked by ${booking.name}`}
                        </Badge>
                      ) : (
                        <>
                          <Badge variant="outline">Open</Badge>
                          <DeleteSessionButton slotId={s.id} />
                        </>
                      )}
                    </div>
                  </li>
                );
              })}
            </ul>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
