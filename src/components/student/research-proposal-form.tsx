"use client";

import { useRouter } from "next/navigation";
import { useRef, useState, useTransition } from "react";
import { AlertCircle, Loader2, Send } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { submitResearchProposal } from "@/server/actions/student/research";
import { INTRO_MAX_WORDS, INTRO_MIN_WORDS, countWords } from "@/lib/validations/research";
import { cn } from "@/lib/utils";

const SUGGESTED_FIELDS = [
  "Education", "Economics", "Psychology", "Data Science", "Linguistics",
  "Biology", "Computer Science", "History", "Environmental Science",
];

export function ResearchProposalForm() {
  const router = useRouter();
  const formRef = useRef<HTMLFormElement>(null);
  const [pending, start] = useTransition();
  const [error, setError] = useState<string | null>(null);
  const [intro, setIntro] = useState("");
  const words = countWords(intro);
  const overLimit = words > INTRO_MAX_WORDS;

  function submit(formData: FormData) {
    setError(null);
    // Checked here too so a long essay is caught before a round trip, with
    // the counter already showing why. The server checks again.
    if (overLimit) {
      setError(`Your introduction is ${words} words. Please keep it to ${INTRO_MAX_WORDS} or fewer.`);
      return;
    }
    start(async () => {
      const res = await submitResearchProposal(formData);
      if (res.error) {
        setError(res.error);
        return;
      }
      toast.success("Proposal submitted — we will review it and email you.");
      formRef.current?.reset();
      setIntro("");
      router.refresh();
    });
  }

  return (
    <form ref={formRef} action={submit} className="space-y-5">
      {error && (
        <p className="flex items-start gap-2 rounded-lg bg-destructive/10 p-3 text-sm text-destructive">
          <AlertCircle className="mt-0.5 h-4 w-4 shrink-0" />
          {error}
        </p>
      )}

      <div>
        <h3 className="font-display text-base font-semibold">Your project</h3>
      </div>

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-[1fr_220px]">
        <div className="space-y-1.5">
          <Label htmlFor="title">Project title</Label>
          <Input
            id="title"
            name="title"
            placeholder="How does test anxiety affect adaptive-test performance?"
            required
          />
        </div>
        <div className="space-y-1.5">
          <Label htmlFor="field">Field</Label>
          <Input id="field" name="field" list="research-fields" placeholder="Psychology" required />
          <datalist id="research-fields">
            {SUGGESTED_FIELDS.map((f) => (
              <option key={f} value={f} />
            ))}
          </datalist>
        </div>
      </div>

      <div className="space-y-1.5">
        <Label htmlFor="question">Your research question</Label>
        <Textarea
          id="question"
          name="question"
          rows={3}
          placeholder="What exactly do you want to find out? One clear question beats five vague ones."
          required
        />
      </div>

      <div className="space-y-1.5">
        <Label htmlFor="priorWork">What have you already done about this question?</Label>
        <Textarea
          id="priorWork"
          name="priorWork"
          rows={3}
          placeholder="Papers or articles you have read, data you have looked at, people you have asked, a small experiment, notes. Starting points count."
          required
        />
      </div>

      <div className="space-y-1.5">
        <Label htmlFor="motivation">Why this question, and why you</Label>
        <Textarea
          id="motivation"
          name="motivation"
          rows={4}
          placeholder="What made you curious about this? What would an answer change?"
          required
        />
      </div>

      <div className="border-t border-border pt-5">
        <h3 className="font-display text-base font-semibold">About you</h3>
        <p className="text-sm text-muted-foreground">So your mentor knows who they are working with.</p>
      </div>

      <div className="space-y-1.5">
        <Label htmlFor="qualifications">Your qualifications</Label>
        <Textarea
          id="qualifications"
          name="qualifications"
          rows={2}
          placeholder="Exams and scores, e.g. SAT 1450 (Oct 2026), IELTS 7.0, AP Biology 5, a school olympiad. Write “None yet” if you have not taken any."
          required
        />
      </div>

      <div className="space-y-1.5">
        <Label htmlFor="experience">Relevant experience (optional)</Label>
        <Textarea
          id="experience"
          name="experience"
          rows={2}
          placeholder="Courses, projects, tools you know — it's fine if this is your first project."
        />
      </div>

      <div className="space-y-1.5">
        <div className="flex flex-wrap items-baseline justify-between gap-2">
          <Label htmlFor="introEssay">Introduce yourself</Label>
          <span
            id="introEssay-count"
            aria-live="polite"
            className={cn(
              "text-xs tabular-nums",
              overLimit ? "font-semibold text-destructive" : words >= INTRO_MIN_WORDS ? "text-success" : "text-muted-foreground"
            )}
          >
            {words} / {INTRO_MAX_WORDS} words
          </span>
        </div>
        <p className="text-sm text-muted-foreground">
          A short essay, {INTRO_MIN_WORDS} to {INTRO_MAX_WORDS} words: who you are, what you are curious about, and
          what you hope to get out of research.
        </p>
        <Textarea
          id="introEssay"
          name="introEssay"
          rows={8}
          value={intro}
          onChange={(e) => setIntro(e.target.value)}
          aria-describedby="introEssay-count"
          aria-invalid={overLimit || undefined}
          className={cn(overLimit && "border-destructive focus-visible:ring-destructive")}
          required
        />
        {overLimit && (
          <p className="text-sm text-destructive">
            {words - INTRO_MAX_WORDS} {words - INTRO_MAX_WORDS === 1 ? "word" : "words"} over the limit.
          </p>
        )}
      </div>

      <Button type="submit" disabled={pending || overLimit} className="gap-2">
        {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Send className="h-4 w-4" />}
        Submit proposal
      </Button>
    </form>
  );
}
