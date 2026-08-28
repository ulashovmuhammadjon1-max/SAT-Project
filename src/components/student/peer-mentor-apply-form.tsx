"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { AlertCircle, FileCheck2, Loader2, Send, Upload, X } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { cn } from "@/lib/utils";
import { applyPeerMentor } from "@/server/actions/student/peer-mentor";

const SUBJECTS = [
  "SAT Math",
  "SAT Reading & Writing",
  "IELTS Writing",
  "IELTS Speaking",
  "Study planning",
  "Test-day strategy",
];

const MAX_FILE_BYTES = 4 * 1024 * 1024;
const ACCEPTED = ["image/png", "image/jpeg", "image/webp", "application/pdf"];

interface Certificate {
  name: string;
  dataUrl: string;
}

export function PeerMentorApplyForm() {
  const router = useRouter();
  const [pending, start] = useTransition();
  const [error, setError] = useState<string | null>(null);
  const [subjects, setSubjects] = useState<string[]>([]);
  const [certificates, setCertificates] = useState<Certificate[]>([]);

  async function addFiles(list: FileList | null) {
    if (!list) return;
    const next: Certificate[] = [...certificates];
    for (const file of Array.from(list)) {
      if (next.length >= 3) break;
      if (!ACCEPTED.includes(file.type)) {
        toast.error(`${file.name}: use PNG, JPG, WEBP or PDF.`);
        continue;
      }
      if (file.size > MAX_FILE_BYTES) {
        toast.error(`${file.name} is over 4MB.`);
        continue;
      }
      const dataUrl = await new Promise<string>((resolve, reject) => {
        const r = new FileReader();
        r.onload = () => resolve(String(r.result));
        r.onerror = reject;
        r.readAsDataURL(file);
      });
      next.push({ name: file.name, dataUrl });
    }
    setCertificates(next.slice(0, 3));
  }

  function submit(formData: FormData) {
    setError(null);
    start(async () => {
      const res = await applyPeerMentor({
        headline: formData.get("headline"),
        bio: formData.get("bio"),
        satScore: formData.get("satScore") || "",
        ieltsBand: formData.get("ieltsBand") || "",
        telegram: formData.get("telegram") || "",
        subjects,
        certificates,
      });
      if (res.error) {
        setError(res.error);
        return;
      }
      toast.success("Application submitted — we will review your certificates and email you.");
      router.refresh();
    });
  }

  return (
    <form action={submit} className="space-y-4">
      {error && (
        <p className="flex items-start gap-2 rounded-lg bg-destructive/10 p-3 text-sm text-destructive">
          <AlertCircle className="mt-0.5 h-4 w-4 shrink-0" />
          {error}
        </p>
      )}

      <div className="space-y-1.5">
        <Label htmlFor="headline">Headline</Label>
        <Input id="headline" name="headline" placeholder="1520 SAT — strong on Math and pacing" required />
        <p className="text-xs text-muted-foreground">One line students will see next to your name.</p>
      </div>

      <div className="grid gap-4 sm:grid-cols-3">
        <div className="space-y-1.5">
          <Label htmlFor="satScore">SAT score</Label>
          <Input id="satScore" name="satScore" type="number" min={400} max={1600} placeholder="1520" />
        </div>
        <div className="space-y-1.5">
          <Label htmlFor="ieltsBand">IELTS band</Label>
          <Input id="ieltsBand" name="ieltsBand" type="number" step="0.5" min={1} max={9} placeholder="8.0" />
        </div>
        <div className="space-y-1.5">
          <Label htmlFor="telegram">Telegram (optional)</Label>
          <Input id="telegram" name="telegram" placeholder="@username" />
        </div>
      </div>

      <div className="space-y-1.5">
        <Label>What can you help with?</Label>
        <div className="flex flex-wrap gap-2">
          {SUBJECTS.map((s) => {
            const on = subjects.includes(s);
            return (
              <button
                key={s}
                type="button"
                onClick={() => setSubjects((cur) => (on ? cur.filter((x) => x !== s) : [...cur, s]))}
                aria-pressed={on}
                className={cn(
                  "rounded-full border px-3 py-1.5 text-sm transition-colors",
                  on
                    ? "border-primary bg-primary/10 font-medium text-primary"
                    : "border-border text-muted-foreground hover:bg-secondary"
                )}
              >
                {s}
              </button>
            );
          })}
        </div>
      </div>

      <div className="space-y-1.5">
        <Label htmlFor="bio">About you</Label>
        <Textarea
          id="bio"
          name="bio"
          rows={4}
          placeholder="How you studied, what you struggled with, how you'd run a session. Students read this before booking."
          required
        />
      </div>

      <div className="space-y-2">
        <Label>Score reports / certificates (required)</Label>
        <p className="text-xs text-muted-foreground">
          Upload your official score report — a College Board score screenshot, IELTS TRF, or
          similar. PNG, JPG, WEBP or PDF, up to 3 files, 4MB each. We verify these before approval
          and never show them to other students.
        </p>
        <label className="flex cursor-pointer items-center justify-center gap-2 rounded-xl border border-dashed border-border px-4 py-6 text-sm text-muted-foreground transition-colors hover:border-primary/50 hover:bg-secondary/50">
          <Upload className="h-4 w-4" />
          Choose files
          <input
            type="file"
            multiple
            accept={ACCEPTED.join(",")}
            className="hidden"
            onChange={(e) => {
              void addFiles(e.target.files);
              e.target.value = "";
            }}
          />
        </label>
        {certificates.length > 0 && (
          <ul className="space-y-1.5">
            {certificates.map((c, i) => (
              <li
                key={`${c.name}-${i}`}
                className="flex items-center gap-2 rounded-lg border border-border bg-card px-3 py-2 text-sm"
              >
                <FileCheck2 className="h-4 w-4 shrink-0 text-success" />
                <span className="min-w-0 flex-1 truncate">{c.name}</span>
                <button
                  type="button"
                  onClick={() => setCertificates((cur) => cur.filter((_, j) => j !== i))}
                  className="text-muted-foreground hover:text-destructive"
                  aria-label={`Remove ${c.name}`}
                >
                  <X className="h-4 w-4" />
                </button>
              </li>
            ))}
          </ul>
        )}
      </div>

      <Button type="submit" disabled={pending} className="gap-2">
        {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Send className="h-4 w-4" />}
        Apply to become a peer mentor
      </Button>
    </form>
  );
}
