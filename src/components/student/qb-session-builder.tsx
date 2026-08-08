"use client";

import { useEffect, useMemo, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import type { QuestionDifficulty, Subject } from "@prisma/client";
import { Loader2, Target } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { cn } from "@/lib/utils";
import {
  countMatchingQuestions,
  type AttemptStatus,
  type QuestionBankFilters,
} from "@/server/actions/student/question-bank";

const DIFFICULTIES: { value: QuestionDifficulty; label: string }[] = [
  { value: "EASY", label: "Easy" },
  { value: "MEDIUM", label: "Medium" },
  { value: "HARD", label: "Hard" },
];

const STATUSES: { value: AttemptStatus; label: string }[] = [
  { value: "ALL", label: "All" },
  { value: "NOT_ATTEMPTED", label: "Not attempted" },
  { value: "ATTEMPTED", label: "Attempted" },
  { value: "CORRECT", label: "Correct" },
  { value: "INCORRECT", label: "Incorrect" },
  { value: "SAVED", label: "Saved" },
];

const SIZES = [5, 10, 20];

export interface DomainOption {
  id: string;
  name: string;
  skills: { id: string; name: string }[];
}

export function SessionBuilder({
  subject,
  domains,
  initialSkillId,
  initialNewOnly,
}: {
  subject: Subject;
  domains: DomainOption[];
  initialSkillId?: string;
  initialNewOnly?: boolean;
}) {
  const router = useRouter();
  const [isStarting, startTransition] = useTransition();

  const initialDomainId = initialSkillId
    ? domains.find((d) => d.skills.some((s) => s.id === initialSkillId))?.id
    : undefined;

  const [domainId, setDomainId] = useState<string | undefined>(initialDomainId);
  const [skillId, setSkillId] = useState<string | undefined>(initialSkillId);
  const [difficulties, setDifficulties] = useState<QuestionDifficulty[]>([]);
  const [status, setStatus] = useState<AttemptStatus>(initialNewOnly ? "NOT_ATTEMPTED" : "ALL");
  const [size, setSize] = useState(10);
  const [customSize, setCustomSize] = useState("");
  const [matchCount, setMatchCount] = useState<number | null>(null);
  const [isCounting, setIsCounting] = useState(false);

  const filters: QuestionBankFilters = useMemo(
    () => ({ subject, domainId, skillId, difficulties, status }),
    [subject, domainId, skillId, difficulties, status]
  );

  // Live match count so the student always knows what they're about to get.
  useEffect(() => {
    let cancelled = false;
    setIsCounting(true);
    countMatchingQuestions(filters)
      .then((n) => {
        if (!cancelled) setMatchCount(n);
      })
      .catch(() => {
        if (!cancelled) setMatchCount(null);
      })
      .finally(() => {
        if (!cancelled) setIsCounting(false);
      });
    return () => {
      cancelled = true;
    };
  }, [filters]);

  const requested = customSize ? Math.max(1, parseInt(customSize, 10) || 0) : size;
  const available = matchCount ?? 0;
  const actual = Math.min(requested, available);
  const isShort = matchCount !== null && available < requested;
  const nothingMatches = matchCount === 0;

  function toggleDifficulty(d: QuestionDifficulty) {
    setDifficulties((cur) => (cur.includes(d) ? cur.filter((x) => x !== d) : [...cur, d]));
  }

  function start() {
    const params = new URLSearchParams({ subject, size: String(actual) });
    if (domainId) params.set("domainId", domainId);
    if (skillId) params.set("skillId", skillId);
    if (difficulties.length) params.set("difficulties", difficulties.join(","));
    if (status !== "ALL") params.set("status", status);
    startTransition(() => router.push(`/practice/session?${params.toString()}`));
  }

  const activeDomain = domains.find((d) => d.id === domainId);

  return (
    <div className="space-y-5">
      <FilterGroup label="Domain">
        <Chip active={!domainId} onClick={() => { setDomainId(undefined); setSkillId(undefined); }}>
          All domains
        </Chip>
        {domains.map((d) => (
          <Chip
            key={d.id}
            active={domainId === d.id}
            onClick={() => {
              setDomainId(d.id);
              setSkillId(undefined);
            }}
          >
            {d.name}
          </Chip>
        ))}
      </FilterGroup>

      {activeDomain && (
        <FilterGroup label="Subtopic">
          <Chip active={!skillId} onClick={() => setSkillId(undefined)}>
            All subtopics
          </Chip>
          {activeDomain.skills.map((s) => (
            <Chip key={s.id} active={skillId === s.id} onClick={() => setSkillId(s.id)}>
              {s.name}
            </Chip>
          ))}
        </FilterGroup>
      )}

      <FilterGroup label="Difficulty" hint="Select any combination">
        {DIFFICULTIES.map((d) => (
          <Chip
            key={d.value}
            active={difficulties.includes(d.value)}
            onClick={() => toggleDifficulty(d.value)}
            pressed
          >
            {d.label}
          </Chip>
        ))}
      </FilterGroup>

      <FilterGroup label="Attempt status">
        {STATUSES.map((s) => (
          <Chip key={s.value} active={status === s.value} onClick={() => setStatus(s.value)}>
            {s.label}
          </Chip>
        ))}
      </FilterGroup>

      <FilterGroup label="Session length">
        {SIZES.map((n) => (
          <Chip
            key={n}
            active={!customSize && size === n}
            onClick={() => {
              setSize(n);
              setCustomSize("");
            }}
          >
            {n} questions
          </Chip>
        ))}
        <div className="flex items-center gap-2">
          <Label htmlFor="custom-size" className="text-xs text-muted-foreground">
            Custom
          </Label>
          <Input
            id="custom-size"
            type="number"
            min={1}
            inputMode="numeric"
            value={customSize}
            onChange={(e) => setCustomSize(e.target.value)}
            className="h-8 w-20"
            placeholder="—"
          />
        </div>
      </FilterGroup>

      <Card>
        <CardContent className="flex flex-wrap items-center justify-between gap-4 p-5">
          <div aria-live="polite" className="text-sm">
            {isCounting || matchCount === null ? (
              <span className="text-muted-foreground">Counting matching questions…</span>
            ) : nothingMatches ? (
              <span className="font-medium text-destructive">
                No questions match these filters.
              </span>
            ) : isShort ? (
              <>
                <span className="font-medium">
                  Only {available} question{available === 1 ? "" : "s"} match your filters.
                </span>
                <span className="block text-muted-foreground">
                  {status === "NOT_ATTEMPTED"
                    ? "Switch attempt status to “All” to include ones you've already tried."
                    : "Widen the filters to get more."}
                </span>
              </>
            ) : (
              <span className="text-muted-foreground">
                {available.toLocaleString()} questions match — practicing {actual}.
              </span>
            )}
          </div>

          <Button onClick={start} disabled={nothingMatches || isCounting || isStarting}>
            {isStarting ? (
              <Loader2 className="h-4 w-4 animate-spin" />
            ) : (
              <Target className="h-4 w-4" />
            )}
            {nothingMatches ? "Start practice" : `Practice ${actual} question${actual === 1 ? "" : "s"}`}
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}

function FilterGroup({
  label,
  hint,
  children,
}: {
  label: string;
  hint?: string;
  children: React.ReactNode;
}) {
  return (
    <fieldset>
      <legend className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">
        {label}
        {hint && <span className="ml-2 font-normal normal-case tracking-normal">({hint})</span>}
      </legend>
      <div className="mt-2 flex flex-wrap items-center gap-2">{children}</div>
    </fieldset>
  );
}

function Chip({
  active,
  onClick,
  children,
  pressed,
}: {
  active: boolean;
  onClick: () => void;
  children: React.ReactNode;
  pressed?: boolean;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      {...(pressed ? { "aria-pressed": active } : {})}
      className={cn(
        "rounded-full border px-3 py-1.5 text-sm transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
        active
          ? "border-primary bg-primary/10 font-medium text-primary"
          : "border-border text-muted-foreground hover:bg-secondary"
      )}
    >
      {children}
    </button>
  );
}
