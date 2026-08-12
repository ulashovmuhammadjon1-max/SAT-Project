import Link from "next/link";
import { Crown, Flame, Medal, Trophy } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  getLeaderboard,
  LEADERBOARD_LABELS,
  type LeaderboardKind,
  type LeaderboardRow,
} from "@/lib/leaderboard";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "Leaderboard" };
export const dynamic = "force-dynamic";

const TABS: { kind: LeaderboardKind; icon: typeof Trophy }[] = [
  { kind: "weekly", icon: Flame },
  { kind: "score", icon: Trophy },
  { kind: "streak", icon: Medal },
];

export default async function LeaderboardPage({
  searchParams,
}: {
  searchParams: { board?: string };
}) {
  const user = await requireUser();
  const kind: LeaderboardKind = TABS.some((t) => t.kind === searchParams.board)
    ? (searchParams.board as LeaderboardKind)
    : "weekly";

  const board = await getLeaderboard(kind, user.id);
  const labels = LEADERBOARD_LABELS[kind];

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Leaderboard</h1>
        <p className="text-sm text-muted-foreground">
          Three boards, because there is more than one way to be good at this.
        </p>
      </div>

      <div className="flex flex-wrap gap-2">
        {TABS.map(({ kind: k, icon: Icon }) => (
          <Link
            key={k}
            href={`/leaderboard?board=${k}`}
            className={cn(
              "pressable inline-flex items-center gap-1.5 rounded-full border px-3.5 py-1.5 text-sm transition-colors",
              k === kind
                ? "border-transparent bg-primary text-primary-foreground"
                : "border-border hover:bg-secondary"
            )}
          >
            <Icon className="h-3.5 w-3.5" />
            {LEADERBOARD_LABELS[k].title}
          </Link>
        ))}
      </div>

      <Card>
        <CardHeader className="pb-3">
          <CardTitle className="text-base">{labels.title}</CardTitle>
          <p className="text-sm text-muted-foreground">{labels.blurb}</p>
        </CardHeader>
        <CardContent className="p-0">
          {board.rows.length ? (
            <>
              <ol className="stagger">
                {board.rows.map((row) => (
                  <Row key={row.userId} row={row} unit={labels.unit} />
                ))}
              </ol>
              {board.me && (
                <>
                  <p className="border-t px-6 py-2 text-center text-xs text-muted-foreground">
                    ⋯ {board.me.rank - board.rows.length - 1} more
                  </p>
                  <ol className="border-t">
                    <Row row={board.me} unit={labels.unit} />
                  </ol>
                </>
              )}
            </>
          ) : (
            <p className="p-10 text-center text-sm text-muted-foreground">
              {kind === "weekly"
                ? "Nobody has answered a question yet this week. Answer one and you are first."
                : kind === "score"
                  ? "No completed practice tests yet. Finish one and the board is yours."
                  : "No active streaks yet. Study today and tomorrow to start one."}
            </p>
          )}
        </CardContent>
      </Card>

      <p className="text-xs text-muted-foreground">
        {board.participants} {board.participants === 1 ? "student" : "students"} on this board.
        Names are shown as a first name and last initial, and email addresses are never shown.
      </p>
    </div>
  );
}

/** Gold, silver and bronze get a colour; everyone else gets their number. */
function RankMark({ rank }: { rank: number }) {
  if (rank <= 3) {
    const tone = ["text-amber-400", "text-slate-400", "text-orange-400"][rank - 1];
    return <Crown className={cn("h-4 w-4", tone)} aria-hidden />;
  }
  return <span className="text-sm text-muted-foreground tabular-nums">{rank}</span>;
}

function Row({ row, unit }: { row: LeaderboardRow; unit: string }) {
  return (
    <li
      className={cn(
        "flex items-center gap-3 border-b px-6 py-2.5 last:border-0",
        row.isMe && "bg-primary/5"
      )}
    >
      <span className="flex w-7 shrink-0 justify-center">
        <RankMark rank={row.rank} />
      </span>
      {/* A div rather than a span, because Badge renders a div and nesting one
          inside phrasing content is invalid HTML. */}
      <div className="flex min-w-0 flex-1 items-center gap-2 text-sm">
        <span className="truncate">{row.displayName}</span>
        {row.isMe && <Badge variant="outline">You</Badge>}
      </div>
      {row.detail && (
        <span className="hidden shrink-0 text-xs text-muted-foreground sm:inline">{row.detail}</span>
      )}
      <span className="shrink-0 text-sm font-semibold tabular-nums">
        {row.value}
        <span className="ml-1 text-xs font-normal text-muted-foreground">{unit}</span>
      </span>
    </li>
  );
}
