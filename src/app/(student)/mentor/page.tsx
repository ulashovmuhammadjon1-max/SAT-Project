import { Award, BadgeCheck, Clock, HeartHandshake, ShieldCheck } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { MentorStudio } from "@/components/student/mentor-studio";
import { PeerMentorApplyForm } from "@/components/student/peer-mentor-apply-form";
import { getMyMentorState, getMySlots } from "@/server/actions/student/peer-mentor";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Peer-Mentor Programme" };
export const dynamic = "force-dynamic";

const PERKS = [
  {
    icon: HeartHandshake,
    title: "Teach what you mastered",
    body: "Host 1-on-1 sessions with students working toward the score you already earned.",
  },
  {
    icon: Award,
    title: "A real leadership credential",
    body: "Approved mentors carry the Peer Mentor badge — verified by certificates, not self-declared.",
  },
  {
    icon: Clock,
    title: "Your schedule, your call",
    body: "Publish only the slots you want. Students book them exactly like founder sessions.",
  },
];

export default async function MentorPage() {
  await requireUser();
  const state = await getMyMentorState();
  const slots = state.status === "APPROVED" ? await getMySlots() : [];

  return (
    <div className="space-y-6">
      <div>
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[hsl(266_84%_60%)]">
          <BadgeCheck className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
          Peer-Mentor Programme
        </p>
        <h1 className="font-display text-2xl font-semibold tracking-tight">
          {state.status === "APPROVED" ? "Your mentor studio" : "Become a peer mentor"}
        </h1>
        <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
          {state.status === "APPROVED"
            ? "Publish session slots and students will book time with you from the booking page."
            : "Scored high? Turn it into leadership: get verified, host sessions, and help the next cohort get there."}
        </p>
      </div>

      {state.status === "PENDING" && (
        <Card className="border-warning/40">
          <CardContent className="flex items-start gap-3 py-5">
            <ShieldCheck className="mt-0.5 h-5 w-5 shrink-0 text-warning" />
            <div>
              <p className="font-medium">Your application is under review</p>
              <p className="mt-0.5 text-sm text-muted-foreground">
                We check every certificate by hand, so this can take a day or two. You will get an
                email either way.
              </p>
            </div>
          </CardContent>
        </Card>
      )}

      {state.status === "REJECTED" && (
        <Card className="border-destructive/40">
          <CardContent className="space-y-1.5 py-5">
            <p className="font-medium">Your previous application was not approved</p>
            {state.adminNote && (
              <p className="text-sm text-muted-foreground">
                <span className="font-medium text-foreground">Note from the team: </span>
                {state.adminNote}
              </p>
            )}
            <p className="text-sm text-muted-foreground">
              You can apply again below — a clearer score report is usually what makes the
              difference.
            </p>
          </CardContent>
        </Card>
      )}

      {state.status === "APPROVED" ? (
        <>
          <div className="flex items-center gap-2">
            <Badge variant="success" className="gap-1">
              <BadgeCheck className="h-3.5 w-3.5" /> Peer Mentor
            </Badge>
            {state.headline && <span className="text-sm text-muted-foreground">{state.headline}</span>}
          </div>
          <Card>
            <CardHeader>
              <CardTitle className="text-base">Session slots</CardTitle>
              <CardDescription>
                Times are in your local timezone. A slot with a booking can only be cancelled by the
                team, so students are never silently stood up.
              </CardDescription>
            </CardHeader>
            <CardContent>
              <MentorStudio slots={slots} />
            </CardContent>
          </Card>
        </>
      ) : (
        <>
          <div className="grid gap-4 sm:grid-cols-3">
            {PERKS.map((p) => (
              <Card key={p.title}>
                <CardContent className="space-y-2 py-5">
                  <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-[hsl(266_84%_60%)]/10 text-[hsl(266_84%_60%)]">
                    <p.icon className="h-4 w-4" />
                  </span>
                  <p className="font-medium">{p.title}</p>
                  <p className="text-sm leading-relaxed text-muted-foreground">{p.body}</p>
                </CardContent>
              </Card>
            ))}
          </div>

          {state.status !== "PENDING" && (
            <Card className="max-w-3xl">
              <CardHeader>
                <CardTitle className="text-base">Apply</CardTitle>
                <CardDescription>
                  Approval is manual and certificate-based: upload the score report for the exam you
                  want to mentor, and an admin verifies it before you appear anywhere.
                </CardDescription>
              </CardHeader>
              <CardContent>
                <PeerMentorApplyForm />
              </CardContent>
            </Card>
          )}
        </>
      )}
    </div>
  );
}
