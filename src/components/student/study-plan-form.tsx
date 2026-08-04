"use client";

import { useState, useTransition } from "react";
import { Loader2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { CountryPicker, MonthPicker, UniversityPicker } from "@/components/onboarding/controls";
import { updateStudyPlan } from "@/server/actions/student/profile";
import {
  GRADE_LABELS,
  GRADE_LEVELS,
  GOAL_LABELS,
  ONBOARDING_GOALS,
  SECTIONS,
  SECTION_LABELS,
  WEAK_AREAS,
  type OnboardingProfile,
} from "@/lib/validations/onboarding";
import { cn } from "@/lib/utils";

const SCORES = [400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600];

export function StudyPlanForm({ initial }: { initial: OnboardingProfile }) {
  const [profile, setProfile] = useState<OnboardingProfile>(initial);
  const [isPending, startTransition] = useTransition();

  function patch(p: Partial<OnboardingProfile>) {
    setProfile((prev) => ({ ...prev, ...p }));
  }

  function save() {
    startTransition(async () => {
      const result = await updateStudyPlan(profile);
      if (result.error) toast.error(result.error);
      else toast.success("Study plan saved.");
    });
  }

  return (
    <div className="space-y-7">
      <Row label="What brings you here?">
        <Select
          value={profile.goal ?? ""}
          onChange={(v) => patch({ goal: (v || null) as OnboardingProfile["goal"] })}
          options={[
            { value: "", label: "Not set" },
            ...ONBOARDING_GOALS.map((g) => ({ value: g, label: GOAL_LABELS[g] })),
          ]}
        />
      </Row>

      <div className="grid gap-5 sm:grid-cols-2">
        <Row label="Current score">
          <Select
            value={profile.currentScore?.toString() ?? ""}
            onChange={(v) => patch({ currentScore: v ? Number(v) : null })}
            options={[{ value: "", label: "Not set" }, ...SCORES.map((s) => ({ value: String(s), label: String(s) }))]}
          />
        </Row>
        <Row label="Target score">
          <Select
            value={profile.targetScore?.toString() ?? ""}
            onChange={(v) => patch({ targetScore: v ? Number(v) : null })}
            options={[{ value: "", label: "Not set" }, ...SCORES.map((s) => ({ value: String(s), label: String(s) }))]}
          />
        </Row>
      </div>

      <div className="grid gap-5 sm:grid-cols-2">
        <Row label="Grade level">
          <Select
            value={profile.gradeLevel ?? ""}
            onChange={(v) => patch({ gradeLevel: (v || null) as OnboardingProfile["gradeLevel"] })}
            options={[
              { value: "", label: "Not set" },
              ...GRADE_LEVELS.map((g) => ({ value: g, label: GRADE_LABELS[g] })),
            ]}
          />
        </Row>
        <Row label="Study time per day">
          <Select
            value={profile.studyMinutesPerDay?.toString() ?? ""}
            onChange={(v) => patch({ studyMinutesPerDay: v ? Number(v) : null })}
            options={[
              { value: "", label: "Not set" },
              { value: "15", label: "15 minutes" },
              { value: "30", label: "30 minutes" },
              { value: "60", label: "1 hour" },
              { value: "120", label: "2+ hours" },
            ]}
          />
        </Row>
      </div>

      <div className="grid gap-5 sm:grid-cols-2">
        <Row label="Strongest section">
          <Select
            value={profile.strongestSection ?? ""}
            onChange={(v) => patch({ strongestSection: (v || null) as OnboardingProfile["strongestSection"] })}
            options={[
              { value: "", label: "Not set" },
              ...SECTIONS.map((s) => ({ value: s, label: SECTION_LABELS[s] })),
            ]}
          />
        </Row>
        <Row label="Needs the most work">
          <Select
            value={profile.weakestArea ?? ""}
            onChange={(v) => patch({ weakestArea: (v || null) as OnboardingProfile["weakestArea"] })}
            options={[
              { value: "", label: "Not set" },
              ...WEAK_AREAS.map((s) => ({ value: s, label: SECTION_LABELS[s] })),
            ]}
          />
        </Row>
      </div>

      <div className="grid gap-5 sm:grid-cols-2">
        <Row label="Daily goal type">
          <Select
            value={profile.dailyGoalType ?? ""}
            onChange={(v) => patch({ dailyGoalType: (v || null) as OnboardingProfile["dailyGoalType"] })}
            options={[
              { value: "", label: "Not set" },
              { value: "QUESTIONS", label: "Questions per day" },
              { value: "MINUTES", label: "Minutes per day" },
            ]}
          />
        </Row>
        <Row label="Daily goal amount">
          <input
            type="number"
            min={1}
            max={500}
            value={profile.dailyGoalValue ?? ""}
            onChange={(e) => patch({ dailyGoalValue: e.target.value ? Number(e.target.value) : null })}
            placeholder="e.g. 20"
            className="h-10 w-full rounded-md border border-input bg-background px-3 text-sm outline-none focus:border-primary"
          />
        </Row>
      </div>

      <Row label="When is your SAT?">
        <MonthPicker value={profile.satMonth} onChange={(v) => patch({ satMonth: v })} />
      </Row>

      <Row label="Country">
        <CountryPicker value={profile.countryCode} onChange={(code) => patch({ countryCode: code })} />
      </Row>

      <Row label="Dream universities">
        <UniversityPicker value={profile.dreamUniversities} onChange={(v) => patch({ dreamUniversities: v })} />
      </Row>

      <Button onClick={save} disabled={isPending} className="w-full sm:w-auto">
        {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
        Save study plan
      </Button>
    </div>
  );
}

function Row({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div className="space-y-2">
      <Label>{label}</Label>
      {children}
    </div>
  );
}

function Select({
  value,
  onChange,
  options,
}: {
  value: string;
  onChange: (v: string) => void;
  options: { value: string; label: string }[];
}) {
  return (
    <select
      value={value}
      onChange={(e) => onChange(e.target.value)}
      className={cn(
        "h-10 w-full rounded-md border border-input bg-background px-3 text-sm outline-none",
        "focus:border-primary focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-1"
      )}
    >
      {options.map((o) => (
        <option key={o.value} value={o.value}>
          {o.label}
        </option>
      ))}
    </select>
  );
}
