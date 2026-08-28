"use client";

import { useEffect, useState, useTransition } from "react";
import { Check, Eye, Loader2, RefreshCw, Trash2 } from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "@/components/ui/select";
import { MathContent } from "@/components/shared/math-content";
import {
  getQuestionTaxonomy,
  previewQuestionSet,
  type PreviewQuestion,
  type TaxonomyDomain,
} from "@/server/actions/teacher/question-sets";

/**
 * Picking Question Bank questions to assign.
 *
 * The teacher narrows by subject, domain, skill and difficulty, asks for a
 * number, and then *reads the actual questions* — stems, choices, and the
 * marked answer — before any of it becomes homework. Reshuffling redraws;
 * removing drops a single question from the set. What the parent form
 * receives is the exact list on screen, never the filter that produced it.
 */

const ANY = "any";
const SUBJECTS = [
  { value: "READING_WRITING", label: "Reading & Writing" },
  { value: "MATH", label: "Math" },
] as const;
const DIFFICULTIES = ["EASY", "MEDIUM", "HARD"] as const;

export function QuestionPicker({
  onChange,
}: {
  onChange: (questions: PreviewQuestion[]) => void;
}) {
  const [pending, start] = useTransition();
  const [subject, setSubject] = useState<string>("READING_WRITING");
  const [domains, setDomains] = useState<TaxonomyDomain[]>([]);
  const [domainId, setDomainId] = useState<string>(ANY);
  const [skillId, setSkillId] = useState<string>(ANY);
  const [difficulties, setDifficulties] = useState<string[]>([]);
  const [count, setCount] = useState(10);
  const [picked, setPicked] = useState<PreviewQuestion[]>([]);
  const [available, setAvailable] = useState<number | null>(null);
  const [openId, setOpenId] = useState<string | null>(null);

  // Domains are per subject, so switching subject invalidates both dropdowns.
  useEffect(() => {
    let cancelled = false;
    setDomainId(ANY);
    setSkillId(ANY);
    getQuestionTaxonomy(subject as "MATH" | "READING_WRITING").then((rows) => {
      if (!cancelled) setDomains(rows);
    });
    return () => {
      cancelled = true;
    };
  }, [subject]);

  function update(next: PreviewQuestion[]) {
    setPicked(next);
    onChange(next);
  }

  function draw() {
    start(async () => {
      const res = await previewQuestionSet({
        subject,
        domainId: domainId === ANY ? "" : domainId,
        skillId: skillId === ANY ? "" : skillId,
        difficulties,
        count,
      });
      setAvailable(res.available ?? null);
      if (res.error) {
        toast.error(res.error);
        update([]);
        return;
      }
      update(res.questions ?? []);
    });
  }

  const skills = domains.find((d) => d.id === domainId)?.skills ?? [];

  return (
    <div className="space-y-3">
      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <div className="space-y-1">
          <Label>Subject</Label>
          <Select value={subject} onValueChange={setSubject}>
            <SelectTrigger><SelectValue /></SelectTrigger>
            <SelectContent>
              {SUBJECTS.map((s) => (
                <SelectItem key={s.value} value={s.value}>{s.label}</SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        <div className="space-y-1">
          <Label>Area</Label>
          <Select
            value={domainId}
            onValueChange={(v) => {
              setDomainId(v);
              setSkillId(ANY);
            }}
          >
            <SelectTrigger><SelectValue /></SelectTrigger>
            <SelectContent>
              <SelectItem value={ANY}>Every area</SelectItem>
              {domains.map((d) => (
                <SelectItem key={d.id} value={d.id}>{d.name}</SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        <div className="space-y-1">
          <Label>Skill</Label>
          <Select value={skillId} onValueChange={setSkillId} disabled={domainId === ANY}>
            <SelectTrigger><SelectValue /></SelectTrigger>
            <SelectContent>
              <SelectItem value={ANY}>Every skill in this area</SelectItem>
              {skills.map((s) => (
                <SelectItem key={s.id} value={s.id}>{s.name}</SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        <div className="space-y-1">
          <Label>How many</Label>
          <Input
            type="number"
            min={1}
            max={50}
            value={count}
            onChange={(e) => setCount(Math.min(50, Math.max(1, Number(e.target.value) || 1)))}
          />
        </div>
      </div>

      <div className="flex flex-wrap items-center gap-2">
        <span className="text-xs font-medium text-muted-foreground">Difficulty</span>
        {DIFFICULTIES.map((d) => {
          const on = difficulties.includes(d);
          return (
            <button
              key={d}
              type="button"
              onClick={() =>
                setDifficulties(on ? difficulties.filter((x) => x !== d) : [...difficulties, d])
              }
              className={`rounded-full border px-3 py-1 text-xs font-medium transition-colors ${
                on
                  ? "border-primary bg-primary text-primary-foreground"
                  : "border-border text-muted-foreground hover:border-primary/50"
              }`}
            >
              {on && <Check className="mr-1 inline h-3 w-3 align-[-1px]" />}
              {d.charAt(0) + d.slice(1).toLowerCase()}
            </button>
          );
        })}
        <span className="text-[11px] text-muted-foreground">
          {difficulties.length === 0 && "none selected = any difficulty"}
        </span>

        <Button type="button" variant="secondary" className="ml-auto gap-2" disabled={pending} onClick={draw}>
          {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Eye className="h-4 w-4" />}
          {picked.length > 0 ? "Draw a different set" : "Preview questions"}
        </Button>
      </div>

      {available !== null && picked.length > 0 && (
        <p className="text-xs text-muted-foreground">
          Showing {picked.length} of {available.toLocaleString()} questions matching these filters.
          Read them below — this exact set is what gets assigned.
        </p>
      )}

      {picked.length > 0 && (
        <ul className="divide-y divide-border rounded-xl border border-border">
          {picked.map((q, i) => (
            <li key={q.id} className="p-3">
              <div className="flex flex-wrap items-start gap-2">
                <span className="mt-0.5 w-6 shrink-0 text-sm tabular-nums text-muted-foreground">
                  {i + 1}.
                </span>
                <div className="min-w-0 flex-1">
                  <div className="flex flex-wrap items-center gap-1.5">
                    <Badge variant="outline" className="text-[10px]">{q.skillName}</Badge>
                    <Badge variant="secondary" className="text-[10px]">
                      {q.difficulty.charAt(0) + q.difficulty.slice(1).toLowerCase()}
                    </Badge>
                  </div>
                  <div className="mt-1.5 text-sm leading-relaxed [&_table]:my-2 [&_table]:text-xs">
                    <MathContent html={q.stem} />
                  </div>

                  {openId === q.id && (
                    <div className="mt-3 space-y-2 rounded-lg bg-secondary/40 p-3">
                      {q.passage && (
                        <div className="max-h-56 overflow-y-auto border-b border-border pb-2 text-sm leading-relaxed">
                          <MathContent html={q.passage} />
                        </div>
                      )}
                      {q.imageUrl && (
                        // eslint-disable-next-line @next/next/no-img-element
                        <img src={q.imageUrl} alt="" className="max-h-56 rounded-md" />
                      )}
                      {q.choices.length > 0 ? (
                        <ul className="space-y-1 text-sm">
                          {q.choices.map((c) => (
                            <li
                              key={c.label}
                              className={c.isCorrect ? "font-medium text-success" : "text-muted-foreground"}
                            >
                              <span className="mr-1.5">{c.label}.</span>
                              <MathContent html={c.content} />
                              {c.isCorrect && <span className="ml-1.5 text-xs">← answer</span>}
                            </li>
                          ))}
                        </ul>
                      ) : (
                        <p className="text-sm">
                          <span className="text-muted-foreground">Student-produced response. Answer: </span>
                          <span className="font-medium text-success">
                            {formatFreeResponse(q.correctAnswerFR)}
                          </span>
                        </p>
                      )}
                    </div>
                  )}
                </div>

                <div className="flex shrink-0 gap-1">
                  <Button
                    type="button"
                    size="sm"
                    variant="ghost"
                    className="h-7 px-2 text-xs"
                    onClick={() => setOpenId(openId === q.id ? null : q.id)}
                  >
                    {openId === q.id ? "Hide" : "Answer"}
                  </Button>
                  <Button
                    type="button"
                    size="sm"
                    variant="ghost"
                    className="h-7 px-2 text-destructive hover:text-destructive"
                    onClick={() => update(picked.filter((p) => p.id !== q.id))}
                  >
                    <Trash2 className="h-3.5 w-3.5" />
                  </Button>
                </div>
              </div>
            </li>
          ))}
        </ul>
      )}

      {picked.length > 0 && (
        <p className="flex items-center gap-1.5 text-xs text-muted-foreground">
          <RefreshCw className="h-3 w-3" />
          {picked.length} question{picked.length === 1 ? "" : "s"} ready to assign.
        </p>
      )}
    </div>
  );
}

/** `correctAnswerFR` is a JSON-encoded array string, e.g. '["40"]'. */
function formatFreeResponse(raw: string | null): string {
  if (!raw) return "—";
  try {
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed.join(" or ") : String(parsed);
  } catch {
    return raw;
  }
}
