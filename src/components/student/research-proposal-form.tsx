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

const SUGGESTED_FIELDS = [
  "Education", "Economics", "Psychology", "Data Science", "Linguistics",
  "Biology", "Computer Science", "History", "Environmental Science",
];

export function ResearchProposalForm() {
  const router = useRouter();
  const formRef = useRef<HTMLFormElement>(null);
  const [pending, start] = useTransition();
  const [error, setError] = useState<string | null>(null);

  function submit(formData: FormData) {
    setError(null);
    start(async () => {
      const res = await submitResearchProposal(formData);
      if (res.error) {
        setError(res.error);
        return;
      }
      toast.success("Proposal submitted — we will review it and email you.");
      formRef.current?.reset();
      router.refresh();
    });
  }

  return (
    <form ref={formRef} action={submit} className="space-y-4">
      {error && (
        <p className="flex items-start gap-2 rounded-lg bg-destructive/10 p-3 text-sm text-destructive">
          <AlertCircle className="mt-0.5 h-4 w-4 shrink-0" />
          {error}
        </p>
      )}

      <div className="grid gap-4 sm:grid-cols-[1fr_220px]">
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
        <Label htmlFor="motivation">Why this question, and why you</Label>
        <Textarea
          id="motivation"
          name="motivation"
          rows={4}
          placeholder="What made you curious about this? What would an answer change?"
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

      <Button type="submit" disabled={pending} className="gap-2">
        {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Send className="h-4 w-4" />}
        Submit proposal
      </Button>
    </form>
  );
}
