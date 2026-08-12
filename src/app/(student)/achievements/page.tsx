import { Card, CardContent } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { AchievementTile, CATEGORY_ICONS } from "@/components/student/achievement-tile";
import { getAchievements } from "@/lib/achievements/service";
import { CATEGORY_LABELS, type AchievementCategory } from "@/lib/achievements/definitions";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Achievements" };
export const dynamic = "force-dynamic";

const CATEGORY_ORDER: AchievementCategory[] = [
  "CONSISTENCY",
  "VOLUME",
  "TESTS",
  "SCORE",
  "ACCURACY",
  "VOCABULARY",
  "COMMUNITY",
];

export default async function AchievementsPage() {
  const user = await requireUser();
  const { all, unlockedCount, totalCount } = await getAchievements(user.id);
  const pct = totalCount ? Math.round((unlockedCount / totalCount) * 100) : 0;

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Achievements</h1>
        <p className="text-sm text-muted-foreground">
          Earned automatically from what you have already done — nothing to claim.
        </p>
      </div>

      <Card>
        <CardContent className="flex flex-wrap items-center gap-6 p-6">
          <div>
            <p className="font-display text-4xl font-semibold tabular-nums">
              {unlockedCount}
              <span className="text-xl text-muted-foreground">/{totalCount}</span>
            </p>
            <p className="text-sm text-muted-foreground">unlocked</p>
          </div>
          <div className="min-w-[12rem] flex-1">
            <Progress value={pct} className="h-2" />
            <p className="mt-2 text-xs text-muted-foreground">{pct}% complete</p>
          </div>
        </CardContent>
      </Card>

      {CATEGORY_ORDER.map((category) => {
        const items = all.filter((a) => a.category === category);
        if (!items.length) return null;
        const Icon = CATEGORY_ICONS[category];
        const done = items.filter((a) => a.unlocked).length;

        return (
          <section key={category}>
            <h2 className="mb-3 flex items-center gap-2 font-display text-lg font-semibold">
              <Icon className="h-4 w-4" />
              {CATEGORY_LABELS[category]}
              <span className="text-sm font-normal text-muted-foreground">
                {done}/{items.length}
              </span>
            </h2>
            <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
              {items.map((a) => (
                <AchievementTile key={a.id} achievement={a} />
              ))}
            </div>
          </section>
        );
      })}
    </div>
  );
}
