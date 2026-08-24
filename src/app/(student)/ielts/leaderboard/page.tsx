import Link from "next/link";
import { Crown, Flame, Mic, PenLine } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  getIeltsLeaderboard,
  IELTS_BOARD_LABELS,
  type IeltsBoardKind,
  type IeltsLeaderboardRow,
} from "@/lib/ielts/leaderboard";
import { formatBand } from "@/lib/ielts/bands";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "IELTS Leaderboard" };
export const dynamic = "force-dynamic";

const TABS: { kind: IeltsBoardKind; icon: typeof Flame }[] = [
  { kind: "writing", icon: PenLine },
  { kind: "speaking", icon: Mic },
  { kind: "effort", icon: Flame },
];

export default async function IeltsLeaderboardPage({
  searchParams,
}: {
  searchParams: { board?: string };
}) {
  const user = await requireUser();
  const kind: IeltsBoardKind = TABS.some((t) => t.kind === searchParams.board)
    ? (searchParams.board as IeltsBoardKind)
    : "writing";

  const board = await getIeltsLeaderboard(kind, user.id);
  const labels = IELTS_BOARD_LABELS[kind];
  const isBand = kind !== "effort";

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">IELTS Leaderboard</h1>
        <p className="text-sm text-muted-foreground">
          Three boards, because the strongest writer and the hardest worker are rarely the
          same person.
        </p>
      </div>

      <div className="flex flex-wrap gap-2">
        {TABS.map(({ kind: k, icon: Icon }) => (
          <Link
            key={k}
            href={`/ielts/leaderboard?board=${k}`}
            className={cn(
              "pressable inline-flex items-center gap-1.5 rounded-full border px-3.5 py-1.5 text-sm transition-colors",
              k === kind
                ? "border-transparent bg-primary text-primary-foreground"
                : "border-border hover:bg-secondary"
            )}
          >
            <Icon className="h-3.5 w-3.5" />
            {IELTS_BOARD_LABELS[k].title}
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
                  <Row key={row.userId} row={row} unit={labels.unit} isBand={isBand} />
                ))}
              </ol>
              {board.me && (
                <>
                  <p className="border-t px-6 py-2 text-center text-xs text-muted-foreground">
                    ⋯ {board.me.rank - board.rows.length - 1} more
                  </p>
                  <ol className="border-t">
                    <Row row={board.me} unit={labels.unit} isBand={isBand} />
                  </ol>
                </>
              )}
            </>
          ) : (
            <p className="p-10 text-center text-sm text-muted-foreground">{labels.empty}</p>
          )}
        </CardContent>
      </Card>

      <p className="text-xs text-muted-foreground">
        {board.participants} {board.participants === 1 ? "student" : "students"} on this board.
        Names are shown as a first name and last initial; email addresses and the work itself are
        never shown. Bands are Scholarly practice estimates, not official IELTS results.
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

function Row({
  row, unit, isBand,
}: {
  row: IeltsLeaderboardRow;
  unit: string;
  isBand: boolean;
}) {
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
        {isBand ? (
          <>
            <span className="mr-1 text-xs font-normal text-muted-foreground">{unit}</span>
            {formatBand(row.value)}
          </>
        ) : (
          <>
            {row.value}
            <span className="ml-1 text-xs font-normal text-muted-foreground">{unit}</span>
          </>
        )}
      </span>
    </li>
  );
}
