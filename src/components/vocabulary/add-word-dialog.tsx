"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Plus } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { addPersonalWord } from "@/server/actions/student/vocab";

export function AddWordDialog() {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [term, setTerm] = useState("");
  const [definition, setDefinition] = useState("");
  const [exampleSentence, setExampleSentence] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  function submit() {
    if (!term.trim() || !definition.trim()) {
      setError("A term and definition are required.");
      return;
    }
    setError(null);
    startTransition(async () => {
      try {
        await addPersonalWord({ term, definition, exampleSentence: exampleSentence || undefined });
        toast.success(`"${term}" added to your vocabulary.`);
        setTerm("");
        setDefinition("");
        setExampleSentence("");
        setOpen(false);
        router.refresh();
      } catch (err) {
        setError(err instanceof Error ? err.message : "Couldn't add that word.");
      }
    });
  }

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button variant="outline">
          <Plus className="h-4 w-4" /> Add your own word
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Add a word</DialogTitle>
          <DialogDescription>
            Your own words join your flashcard and quiz rotation right away — only you see them.
          </DialogDescription>
        </DialogHeader>

        <div className="space-y-3">
          <div className="space-y-1.5">
            <Label>Term</Label>
            <Input value={term} onChange={(e) => setTerm(e.target.value)} placeholder="e.g. ubiquitous" />
          </div>
          <div className="space-y-1.5">
            <Label>Definition</Label>
            <Textarea value={definition} onChange={(e) => setDefinition(e.target.value)} rows={2} />
          </div>
          <div className="space-y-1.5">
            <Label>Example sentence (optional)</Label>
            <Textarea value={exampleSentence} onChange={(e) => setExampleSentence(e.target.value)} rows={2} />
          </div>
          {error && <p className="text-sm text-destructive">{error}</p>}
        </div>

        <DialogFooter>
          <Button onClick={submit} disabled={isPending}>
            {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Plus className="h-4 w-4" />}
            Add word
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
