"use client";

import { cloneElement } from "react";
import { Check, ExternalLink, Info, ShieldCheck } from "lucide-react";

import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { InstagramIcon, TelegramIcon } from "@/components/shared/brand-icons";
import { TelegramRequirement, type TelegramState } from "@/components/student/telegram-requirement";
import { cn } from "@/lib/utils";
import type { CommunityRequirement } from "@/lib/community";

/* -------------------------------------------------------------------------- */
/* Step 1 — community                                                          */
/* -------------------------------------------------------------------------- */

/**
 * The two community accounts. Instagram is always the student's own word (the
 * Graph API cannot say who follows whom). Telegram is checked for real when a
 * bot is configured — then it renders Telegram's own login widget instead of a
 * tick box, exactly as before — and is the student's word otherwise.
 */
export function RequirementsStep({
  requirements,
  telegram,
  acked,
  onToggle,
}: {
  requirements: CommunityRequirement[];
  telegram: { botUsername: string; state: TelegramState } | null;
  acked: Set<string>;
  onToggle: (id: string, on: boolean) => void;
}) {
  return (
    <div className="space-y-5">
      <p className="text-[15px] leading-relaxed text-muted-foreground">
        Scholarly is free because the community keeps it going. Before booking, follow us on both. It takes a
        minute, and it is how you hear about new sessions first.
      </p>

      <ul className="space-y-3">
        {requirements.map((r) => {
          if (r.verification === "verified" && r.id === "telegram" && telegram) {
            return (
              <li key={r.id}>
                <TelegramRequirement
                  botUsername={telegram.botUsername}
                  channelHandle={r.handle}
                  channelHref={r.href}
                  label={r.label}
                  state={telegram.state}
                />
                <p className="mt-2 flex items-center gap-1.5 text-xs text-muted-foreground">
                  <ShieldCheck className="h-3.5 w-3.5" aria-hidden /> Checked automatically through Telegram
                </p>
              </li>
            );
          }
          const checked = acked.has(r.id);
          const Icon = r.id === "instagram" ? InstagramIcon : TelegramIcon;
          const inputId = `req-${r.id}`;
          return (
            <li
              key={r.id}
              className={cn(
                "rounded-xl border p-4 transition-colors sm:p-5",
                checked ? "border-success/50 bg-success/5" : "border-border bg-card",
              )}
            >
              <div className="flex flex-col gap-4 sm:flex-row sm:items-center">
                <div className="flex min-w-0 flex-1 items-center gap-4">
                  <span
                    className={cn(
                      "flex h-12 w-12 shrink-0 items-center justify-center rounded-xl",
                      r.id === "instagram"
                        ? "bg-[hsl(330_70%_95%)] text-[hsl(330_70%_42%)] dark:bg-[hsl(330_40%_18%)] dark:text-[hsl(330_80%_72%)]"
                        : "bg-[hsl(200_80%_94%)] text-[hsl(200_80%_36%)] dark:bg-[hsl(200_50%_16%)] dark:text-[hsl(200_85%_70%)]",
                    )}
                  >
                    <Icon className="h-6 w-6" />
                  </span>
                  <div className="min-w-0">
                    <p className="font-semibold">{r.label}</p>
                    <p className="truncate text-sm text-muted-foreground">{r.handle}</p>
                  </div>
                </div>
                <a
                  href={r.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex h-11 items-center justify-center gap-2 rounded-lg border border-input px-4 text-sm font-medium transition-colors hover:bg-secondary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
                >
                  Open {r.handle}
                  <ExternalLink className="h-4 w-4" aria-hidden />
                  <span className="sr-only">(opens in a new tab)</span>
                </a>
              </div>

              <label
                htmlFor={inputId}
                className="mt-4 flex min-h-12 cursor-pointer items-center gap-3 rounded-lg bg-secondary/60 px-4 py-3"
              >
                <input
                  id={inputId}
                  type="checkbox"
                  checked={checked}
                  onChange={(e) => onToggle(r.id, e.target.checked)}
                  className="h-6 w-6 shrink-0 cursor-pointer rounded border-input accent-primary"
                />
                <span className="text-[15px] font-medium">
                  {r.id === "instagram" ? "I follow" : "I have joined"} {r.handle}
                </span>
                {checked && <Check className="ml-auto h-5 w-5 text-success" aria-hidden />}
              </label>
            </li>
          );
        })}
      </ul>

      <div className="flex gap-3 rounded-xl border border-warning/40 bg-warning/5 p-4">
        <Info className="mt-0.5 h-5 w-5 shrink-0 text-warning" aria-hidden />
        <p className="text-sm leading-relaxed text-muted-foreground">
          <strong className="text-foreground">Reviewers check this before approving.</strong> If you have not followed,
          the booking is cancelled and your coins are returned.
        </p>
      </div>
    </div>
  );
}

/* -------------------------------------------------------------------------- */
/* Step 2 — about you                                                          */
/* -------------------------------------------------------------------------- */

export interface DetailsValues {
  name: string;
  email: string;
  currentScore: string;
  targetScore: string;
  satDate: string;
  weakest: string;
  hours: string;
  notes: string;
}

export type DetailsErrors = Partial<Record<keyof DetailsValues, string>>;

const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

/** Mirrors the server's rules so mistakes surface here, not after a round trip. */
export function validateDetails(v: DetailsValues, askSat: boolean): DetailsErrors {
  const e: DetailsErrors = {};
  if (!v.name.trim()) e.name = "Enter your name.";
  if (!v.email.trim()) e.email = "Enter your email so we can confirm the session.";
  else if (!EMAIL.test(v.email.trim())) e.email = "Enter a valid email address, like name@example.com.";
  const score = (s: string) => {
    if (!s) return null;
    const n = Number(s);
    return Number.isInteger(n) && n >= 400 && n <= 1600 ? null : "Enter a score between 400 and 1600.";
  };
  if (askSat) {
    const c = score(v.currentScore);
    if (c) e.currentScore = c;
    const t = score(v.targetScore);
    if (t) e.targetScore = t;
  }
  if (v.hours) {
    const n = Number(v.hours);
    if (!Number.isInteger(n) || n < 0 || n > 80) e.hours = "Enter a number of hours between 0 and 80.";
  }
  return e;
}

export function DetailsStep({
  values,
  errors,
  askSat,
  timezone,
  onChange,
}: {
  values: DetailsValues;
  errors: DetailsErrors;
  askSat: boolean;
  timezone: string;
  onChange: (key: keyof DetailsValues, value: string) => void;
}) {
  return (
    <div className="space-y-8">
      <fieldset className="space-y-5">
        <legend className="mb-1 text-sm font-semibold text-muted-foreground">Contact</legend>
        <div className="grid gap-5 sm:grid-cols-2">
          <Field id="name" label="Your name" required error={errors.name}>
            <Input
              id="name"
              value={values.name}
              onChange={(e) => onChange("name", e.target.value)}
              autoComplete="name"
              placeholder="e.g. Aziza Karimova"
            />
          </Field>
          <Field
            id="email"
            label="Email"
            required
            error={errors.email}
            hint="Where we send the confirmation and, once approved, the join link."
          >
            <Input
              id="email"
              type="email"
              inputMode="email"
              value={values.email}
              onChange={(e) => onChange("email", e.target.value)}
              autoComplete="email"
              placeholder="name@example.com"
            />
          </Field>
        </div>
      </fieldset>

      {askSat && (
        <fieldset className="space-y-5">
          <legend className="mb-1 text-sm font-semibold text-muted-foreground">Your SAT preparation (optional)</legend>
          <div className="grid gap-5 sm:grid-cols-2">
            <Field id="currentScore" label="Current SAT score" optional error={errors.currentScore}>
              <Input
                id="currentScore"
                type="number"
                inputMode="numeric"
                min={400}
                max={1600}
                value={values.currentScore}
                onChange={(e) => onChange("currentScore", e.target.value)}
                placeholder="e.g. 1250"
              />
            </Field>
            <Field id="targetScore" label="Target SAT score" optional error={errors.targetScore}>
              <Input
                id="targetScore"
                type="number"
                inputMode="numeric"
                min={400}
                max={1600}
                value={values.targetScore}
                onChange={(e) => onChange("targetScore", e.target.value)}
                placeholder="e.g. 1450"
              />
            </Field>
            <Field id="satDate" label="Upcoming test date" optional>
              <Input
                id="satDate"
                type="date"
                value={values.satDate}
                onChange={(e) => onChange("satDate", e.target.value)}
              />
            </Field>
            <Field id="weakest" label="Biggest SAT weakness" optional>
              <Input
                id="weakest"
                value={values.weakest}
                onChange={(e) => onChange("weakest", e.target.value)}
                placeholder="e.g. running out of time on Reading"
              />
            </Field>
          </div>
        </fieldset>
      )}

      <fieldset className="space-y-5">
        <legend className="mb-1 text-sm font-semibold text-muted-foreground">The session</legend>
        <Field
          id="notes"
          label="What would you like to focus on?"
          optional
          hint="Your mentor reads this before the session, so a sentence or two helps a lot."
        >
          <Textarea
            id="notes"
            value={values.notes}
            onChange={(e) => onChange("notes", e.target.value)}
            rows={4}
            className="h-auto min-h-[7.5rem] text-base"
            placeholder="e.g. I want to check whether my research question is narrow enough."
          />
        </Field>
        <div className="grid gap-5 sm:grid-cols-2">
          <Field id="hours" label="Study hours per week" optional error={errors.hours}>
            <Input
              id="hours"
              type="number"
              inputMode="numeric"
              min={0}
              max={80}
              value={values.hours}
              onChange={(e) => onChange("hours", e.target.value)}
              placeholder="e.g. 6"
            />
          </Field>
          <div className="space-y-2">
            <p className="text-sm font-medium">Your timezone</p>
            <p className="flex h-12 items-center rounded-lg border border-dashed border-border px-4 text-[15px] text-muted-foreground">
              {timezone || "Detecting…"}
            </p>
            <p className="text-xs text-muted-foreground">Detected from your device. Times are shown in it.</p>
          </div>
        </div>
      </fieldset>
    </div>
  );
}

function Field({
  id,
  label,
  required,
  optional,
  hint,
  error,
  children,
}: {
  id: string;
  label: string;
  required?: boolean;
  optional?: boolean;
  hint?: string;
  error?: string;
  children: React.ReactElement<{ className?: string; "aria-invalid"?: boolean; "aria-describedby"?: string }>;
}) {
  const describedBy = [hint && `${id}-hint`, error && `${id}-error`].filter(Boolean).join(" ") || undefined;
  const control = cloneElement(children, {
    className: cn("h-12 text-base", children.props.className, error && "border-destructive focus-visible:ring-destructive"),
    "aria-invalid": Boolean(error) || undefined,
    "aria-describedby": describedBy,
  });
  return (
    <div className="space-y-2">
      <Label htmlFor={id} className="text-sm font-medium">
        {label}
        {required && (
          <span className="ml-1 text-destructive" aria-hidden>
            *
          </span>
        )}
        {optional && <span className="ml-2 text-xs font-normal text-muted-foreground">Optional</span>}
      </Label>
      {control}
      {hint && !error && (
        <p id={`${id}-hint`} className="text-xs text-muted-foreground">
          {hint}
        </p>
      )}
      {error && (
        <p id={`${id}-error`} className="text-sm font-medium text-destructive">
          {error}
        </p>
      )}
    </div>
  );
}
