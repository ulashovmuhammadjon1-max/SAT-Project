import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Bookmarks" };
export const dynamic = "force-dynamic";

export default async function BookmarksPage() {
  const user = await requireUser();

  const bookmarks = await prisma.bookmark.findMany({
    where: { userId: user.id },
    orderBy: { createdAt: "desc" },
    include: { question: { include: { domain: true, skill: true } } },
  });

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Bookmarks</h1>
        <p className="text-sm text-muted-foreground">Questions you saved to revisit later.</p>
      </div>

      <div className="space-y-3">
        {bookmarks.map((b) => (
          <Card key={b.id}>
            <CardContent className="space-y-2 p-5">
              <div className="flex flex-wrap gap-2">
                <Badge variant="outline">{b.question.domain.name}</Badge>
                <Badge variant="outline">{b.question.skill.name}</Badge>
                <Badge variant="outline">{b.question.difficulty}</Badge>
              </div>
              <p
                className="line-clamp-2 text-sm leading-relaxed"
                dangerouslySetInnerHTML={{ __html: b.question.stem }}
              />
            </CardContent>
          </Card>
        ))}
        {bookmarks.length === 0 && (
          <p className="text-sm text-muted-foreground">
            No bookmarks yet. Bookmark questions from the review screen after completing a test.
          </p>
        )}
      </div>
    </div>
  );
}
