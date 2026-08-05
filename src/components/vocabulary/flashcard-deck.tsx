"use client";

import { useState, useTransition } from "react";
import Link from "next/link";
import { motion, AnimatePresence } from "framer-motion";
import { PartyPopper, RotateCw } from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { reviewWord } from "@/server/actions/student/vocab";

interface FlashcardWord {
  id: string;
  term: string;
  partOfSpeech: string | null;
  definition: string;
  exampleSentence: string | null;
  synonyms: string[];
  antonyms: string[];
}

const RATINGS: { label: string; quality: 0 | 1 | 2 | 3 | 4 | 5; className: string }[] = [
  { label: "Forgot", quality: 1, className: "border-destructive/40 text-destructive hover:bg-destructive/10" },
  { label: "Hard", quality: 3, className: "border-warning/40 text-warning-foreground hover:bg-warning/10" },
  { label: "Good", quality: 4, className: "border-primary/40 text-primary hover:bg-primary/10" },
  { label: "Easy", quality: 5, className: "border-success/40 text-success hover:bg-success/10" },
];

export function FlashcardDeck({ words }: { words: FlashcardWord[] }) {
  const [index, setIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const [isPending, startTransition] = useTransition();

  const word = words[index];

  function rate(quality: 0 | 1 | 2 | 3 | 4 | 5) {
    if (!word) return;
    startTransition(async () => {
      try {
        await reviewWord(word.id, quality);
      } catch {
        // Still move on -- getting stuck on one card because of a network
        // blip is worse than one review not being recorded, but say so.
        toast.error("That review didn't save, but you can keep going.");
      }
      setFlipped(false);
      setIndex((i) => i + 1);
    });
  }

  if (words.length === 0) {
    return (
      <div className="flex flex-col items-center gap-4 py-24 text-center">
        <PartyPopper className="h-10 w-10 text-primary" />
        <p className="font-display text-xl font-semibold">No words due right now</p>
        <p className="text-sm text-muted-foreground">Check back later, or browse the full vocabulary list.</p>
        <Button asChild variant="outline">
          <Link href="/vocabulary">Back to vocabulary</Link>
        </Button>
      </div>
    );
  }

  if (!word) {
    return (
      <div className="flex flex-col items-center gap-4 py-24 text-center">
        <PartyPopper className="h-10 w-10 text-success" />
        <p className="font-display text-xl font-semibold">Session complete!</p>
        <p className="text-sm text-muted-foreground">You reviewed {words.length} words.</p>
        <Button asChild>
          <Link href="/vocabulary">Back to vocabulary</Link>
        </Button>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-xl space-y-6">
      <div className="space-y-2">
        <div className="flex items-center justify-between text-sm text-muted-foreground">
          <span>
            {index + 1} / {words.length}
          </span>
          <Link href="/vocabulary" className="hover:underline">
            Exit
          </Link>
        </div>
        <Progress value={(index / words.length) * 100} />
      </div>

      <AnimatePresence mode="wait">
        <motion.div
          key={word.id}
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -20 }}
          transition={{ duration: 0.25 }}
        >
          <Card
            className="min-h-[320px] cursor-pointer select-none"
            onClick={() => setFlipped((f) => !f)}
          >
            <CardContent className="flex min-h-[320px] flex-col items-center justify-center gap-4 p-8 text-center">
              {!flipped ? (
                <>
                  <p className="font-display text-3xl font-semibold">{word.term}</p>
                  {word.partOfSpeech && <Badge variant="outline">{word.partOfSpeech}</Badge>}
                  <p className="flex items-center gap-1.5 text-xs text-muted-foreground">
                    <RotateCw className="h-3.5 w-3.5" /> Tap to reveal definition
                  </p>
                </>
              ) : (
                <div className="space-y-3">
                  <p className="font-display text-xl font-semibold">{word.term}</p>
                  <p className="text-sm leading-relaxed">{word.definition}</p>
                  {word.exampleSentence && (
                    <p className="text-sm italic text-muted-foreground">&ldquo;{word.exampleSentence}&rdquo;</p>
                  )}
                  {word.synonyms.length > 0 && (
                    <p className="text-xs text-muted-foreground">Synonyms: {word.synonyms.join(", ")}</p>
                  )}
                </div>
              )}
            </CardContent>
          </Card>
        </motion.div>
      </AnimatePresence>

      {flipped && (
        <div className="grid grid-cols-4 gap-2">
          {RATINGS.map((r) => (
            <Button
              key={r.label}
              variant="outline"
              disabled={isPending}
              className={r.className}
              onClick={() => rate(r.quality)}
            >
              {r.label}
            </Button>
          ))}
        </div>
      )}
    </div>
  );
}
