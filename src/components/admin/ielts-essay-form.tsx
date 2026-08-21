"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { AlertCircle, Loader2, Save } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { ALLOWED_BANDS, SUGGESTED_TOPICS } from "@/lib/validations/ielts-essay";
import { createEssay, updateEssay } from "@/server/actions/admin/ielts-essays";

export interface EssayFormValues {
  id?: string;
  title: string;
  question: string;
  essayText: string;
  band: number;
  topic: string;
  subtopic: string;
  tags: string[];
}

/**
 * Create or edit a Task 2 essay.
 *
 * The band control offers only 8.0, 8.5 and 9.0 — there is no way to type 7.5
 * here, and the server and the database both refuse it anyway. The three layers
 * are the point: the library's promise is that everything in it is Band 8+.
 */
export function IeltsEssayForm({ initial }: { initial?: EssayFormValues }) {
  const router = useRouter();
  const [pending, start] = useTransition();
  const [error, setError] = useState<string | null>(null);
  const [essayText, setEssayText] = useState(initial?.essayText ?? "");
  const [band, setBand] = useState<number>(initial?.band ?? 8);

  const words = essayText.trim().split(/\s+/).filter(Boolean).length;
  const editing = Boolean(initial?.id);

  function submit(formData: FormData) {
    setError(null);
    formData.set("band", String(band));
    start(async () => {
      const res = editing
        ? await updateEssay(initial!.id!, formData)
        : await createEssay(formData);
      if (res.error) {
        setError(res.error);
        return;
      }
      for (const w of res.warnings ?? []) toast.warning(w);
      toast.success(editing ? "Essay saved." : "Essay created.");
      router.push(`/admin/ielts/essays/${res.essayId ?? initial?.id}`);
      router.refresh();
    });
  }

  return (
    <form action={submit} className="space-y-5">
      {error && (
        <p className="flex items-start gap-2 rounded-lg bg-destructive/10 p-3 text-sm text-destructive">
          <AlertCircle className="mt-0.5 h-4 w-4 shrink-0" />
          {error}
        </p>
      )}

      <Card>
        <CardContent className="space-y-4 py-5">
          <div className="space-y-1.5">
            <Label htmlFor="title">Title</Label>
            <Input
              id="title"
              name="title"
              defaultValue={initial?.title}
              placeholder="Public transport investment — agree/disagree"
              required
            />
            <p className="text-xs text-muted-foreground">
              For the admin list. Students see the question, not this.
            </p>
          </div>

          <div className="space-y-1.5">
            <Label htmlFor="question">Task 2 question</Label>
            <Textarea
              id="question"
              name="question"
              rows={3}
              defaultValue={initial?.question}
              placeholder="Some people believe that governments should invest more in public transportation…"
              required
            />
          </div>

          <div className="grid gap-4 sm:grid-cols-3">
            <div className="space-y-1.5">
              <Label>Band</Label>
              {/* Only three values exist. A free number field here is how a 7.5
                  ends up in a Band 8+ library. */}
              <div className="flex gap-2">
                {ALLOWED_BANDS.map((b) => (
                  <button
                    key={b}
                    type="button"
                    onClick={() => setBand(b)}
                    className={`flex-1 rounded-lg border px-3 py-2 text-sm font-semibold tabular-nums transition-colors ${
                      band === b
                        ? "border-primary bg-primary text-primary-foreground"
                        : "border-border hover:bg-secondary"
                    }`}
                  >
                    {b.toFixed(1)}
                  </button>
                ))}
              </div>
            </div>

            <div className="space-y-1.5">
              <Label htmlFor="topic">Topic</Label>
              <Input
                id="topic"
                name="topic"
                list="essay-topics"
                defaultValue={initial?.topic}
                placeholder="Transport"
                required
              />
              <datalist id="essay-topics">
                {SUGGESTED_TOPICS.map((t) => (
                  <option key={t} value={t} />
                ))}
              </datalist>
            </div>

            <div className="space-y-1.5">
              <Label htmlFor="subtopic">Subtopic (optional)</Label>
              <Input
                id="subtopic"
                name="subtopic"
                defaultValue={initial?.subtopic}
                placeholder="Urban planning"
              />
            </div>
          </div>

          <div className="space-y-1.5">
            <Label htmlFor="tags">Tags (optional, comma separated)</Label>
            <Input
              id="tags"
              name="tags"
              defaultValue={initial?.tags.join(", ")}
              placeholder="agree-disagree, cities"
            />
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardContent className="space-y-2 py-5">
          <div className="flex items-center justify-between">
            <Label htmlFor="essayText">Essay</Label>
            <span className="text-xs tabular-nums text-muted-foreground">
              {words} words{words > 0 && words < 150 ? " — under 150" : ""}
            </span>
          </div>
          <Textarea
            id="essayText"
            name="essayText"
            rows={18}
            value={essayText}
            onChange={(e) => setEssayText(e.target.value)}
            placeholder="Paste the Band 8+ essay exactly as written…"
            className="font-serif text-[15px] leading-relaxed"
            required
          />
          <p className="text-xs text-muted-foreground">
            Stored and shown to students exactly as pasted — highlights are a layer over this text,
            never a rewrite. Editing it later invalidates the existing highlights and requires a
            re-analysis.
          </p>
        </CardContent>
      </Card>

      <div className="flex gap-2">
        <Button type="submit" disabled={pending} className="gap-2">
          {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Save className="h-4 w-4" />}
          {editing ? "Save changes" : "Create essay"}
        </Button>
        <Button type="button" variant="outline" onClick={() => router.back()} disabled={pending}>
          Cancel
        </Button>
      </div>
    </form>
  );
}
