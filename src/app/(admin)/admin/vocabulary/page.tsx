import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "Vocabulary" };
export const dynamic = "force-dynamic";

export default async function AdminVocabularyPage() {
  const [decks, words] = await Promise.all([
    prisma.vocabDeck.findMany({ include: { _count: { select: { words: true } } }, orderBy: { createdAt: "desc" } }),
    prisma.vocabWord.findMany({ orderBy: { createdAt: "desc" }, take: 100 }),
  ]);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Vocabulary</h1>
        <p className="text-sm text-muted-foreground">Decks and words published from vocabulary PDF uploads.</p>
      </div>

      <div className="grid gap-4 sm:grid-cols-3">
        {decks.map((deck) => (
          <Card key={deck.id}>
            <CardHeader className="pb-2">
              <CardTitle className="text-base">{deck.name}</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-2xl font-display font-semibold">{deck._count.words}</p>
              <p className="text-xs text-muted-foreground">words</p>
            </CardContent>
          </Card>
        ))}
        {decks.length === 0 && (
          <p className="text-sm text-muted-foreground">No decks yet — publish a vocabulary PDF upload.</p>
        )}
      </div>

      <Card>
        <CardContent className="p-0">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Term</TableHead>
                <TableHead>Definition</TableHead>
                <TableHead>Difficulty</TableHead>
                <TableHead>Synonyms</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {words.map((word) => (
                <TableRow key={word.id}>
                  <TableCell className="font-medium">{word.term}</TableCell>
                  <TableCell className="max-w-md text-sm text-muted-foreground line-clamp-1">
                    {word.definition}
                  </TableCell>
                  <TableCell>
                    <Badge variant="outline">{word.difficulty}</Badge>
                  </TableCell>
                  <TableCell className="text-sm text-muted-foreground">
                    {((word.synonyms as string[] | null) ?? []).slice(0, 3).join(", ") || "—"}
                  </TableCell>
                </TableRow>
              ))}
              {words.length === 0 && (
                <TableRow>
                  <TableCell colSpan={4} className="py-12 text-center text-sm text-muted-foreground">
                    No vocabulary words yet.
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
