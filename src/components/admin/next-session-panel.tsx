import Link from "next/link";
import { CalendarClock, Mail, NotebookPen, Target, Video } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { LocalTime } from "@/components/shared/local-time";

export interface NextSessionInfo {
  bookingId: string;
  startsAt: string;
  durationMinutes: number;
  name: string;
  email: string;
  currentScore: number | null;
  targetScore: number | null;
  weakestArea: string | null;
  notes: string | null;
  timezone: string | null;
  meetingUrl: string | null;
}

/**
 * "Up next" for the mentor.
 *
 * The admin session list showed who had booked but never how to actually join
 * — the meeting link lived on the booking row and was never rendered, so the
 * only way in was remembering the URL. This puts the join button, the time and
 * everything worth reading before a 30-minute session in one place.
 *
 * The join button is always live here, unlike the student's, which only
 * activates ten minutes before. The mentor owns the room and has good reason
 * to open it early.
 */
export function NextSessionPanel({ session }: { session: NextSessionInfo | null }) {
  if (!session) {
    return (
      <Card className="border-dashed">
        <CardContent className="p-6 text-center">
          <CalendarClock className="mx-auto mb-2 h-8 w-8 text-muted-foreground" />
          <p className="font-medium">No upcoming sessions</p>
          <p className="mt-1 text-sm text-muted-foreground">
            Publish some availability below and students can book it.
          </p>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="overflow-hidden border-primary/30 bg-gradient-to-br from-primary/10 via-primary/5 to-transparent">
      <CardContent className="p-6">
        <div className="flex flex-wrap items-start justify-between gap-4">
          <div className="min-w-0">
            <p className="text-xs font-semibold uppercase tracking-wide text-primary">Up next</p>
            <p className="mt-1 font-display text-xl font-semibold">
              <LocalTime iso={session.startsAt} format="full" />
            </p>
            <p className="text-sm text-muted-foreground">
              {session.durationMinutes} minutes with {session.name}
              {session.timezone && ` · they are in ${session.timezone}`}
            </p>
          </div>

          <div className="flex flex-wrap gap-2">
            {session.meetingUrl ? (
              <Button asChild>
                <a href={session.meetingUrl} target="_blank" rel="noopener noreferrer">
                  <Video className="mr-2 h-4 w-4" />
                  Join session
                </a>
              </Button>
            ) : (
              <Button disabled title="No meeting link is configured for this booking">
                <Video className="mr-2 h-4 w-4" />
                No link yet
              </Button>
            )}
            <Button asChild variant="outline">
              <a href={`mailto:${session.email}`}>
                <Mail className="mr-2 h-4 w-4" />
                Email
              </a>
            </Button>
          </div>
        </div>

        {/* Everything worth knowing before the call, without opening another page. */}
        <div className="mt-5 grid gap-4 border-t border-border/60 pt-4 sm:grid-cols-3">
          <Detail
            icon={Target}
            label="Score"
            value={
              session.currentScore || session.targetScore
                ? `${session.currentScore ?? "—"} → ${session.targetScore ?? "—"}`
                : "Not shared"
            }
          />
          <Detail icon={NotebookPen} label="Weakest area" value={session.weakestArea ?? "Not shared"} />
          <Detail icon={Mail} label="Email" value={session.email} />
        </div>

        {session.notes && (
          <div className="mt-4 rounded-lg border border-border bg-card/70 p-3">
            <p className="text-xs font-medium text-muted-foreground">What they asked for</p>
            <p className="mt-1 whitespace-pre-wrap text-sm">{session.notes}</p>
          </div>
        )}

        {!session.meetingUrl && (
          <p className="mt-4 text-xs text-muted-foreground">
            This booking has no link — it was made before a meeting provider was configured. Set one
            in{" "}
            <Link href="/admin/economy" className="font-medium text-primary underline-offset-4 hover:underline">
              Economy → Meeting provider
            </Link>
            , then send this student a link by email.
          </p>
        )}
      </CardContent>
    </Card>
  );
}

function Detail({
  icon: Icon,
  label,
  value,
}: {
  icon: typeof Target;
  label: string;
  value: string;
}) {
  return (
    <div className="flex items-start gap-2">
      <Icon className="mt-0.5 h-4 w-4 shrink-0 text-muted-foreground" />
      <div className="min-w-0">
        <p className="text-xs text-muted-foreground">{label}</p>
        <p className="truncate text-sm font-medium">{value}</p>
      </div>
    </div>
  );
}

/** Standing room link, so the mentor can open it outside any booking. */
export function RoomLinkCard({ url, provider }: { url: string | null; provider: string }) {
  if (!url) return null;
  return (
    <Card>
      <CardContent className="flex flex-wrap items-center justify-between gap-3 p-4">
        <div className="min-w-0">
          <p className="flex items-center gap-2 text-sm font-medium">
            Your meeting room
            <Badge variant="secondary" className="text-xs">
              {provider === "static" ? "shared room" : provider}
            </Badge>
          </p>
          <p className="truncate font-mono text-xs text-muted-foreground">{url}</p>
        </div>
        <Button asChild variant="outline" size="sm">
          <a href={url} target="_blank" rel="noopener noreferrer">
            <Video className="mr-2 h-3.5 w-3.5" />
            Open room
          </a>
        </Button>
      </CardContent>
    </Card>
  );
}
