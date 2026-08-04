"use client";

import { useMemo, useState, type ReactNode } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { Check, Search, X } from "lucide-react";

import { COUNTRIES, PRIORITY_COUNTRIES, countryByCode } from "@/lib/data/countries";
import { searchUniversities } from "@/lib/data/universities";
import { cn } from "@/lib/utils";

/* -------------------------------------------------------------------------- */
/* Option cards                                                                */
/* -------------------------------------------------------------------------- */

export function OptionCard({
  selected,
  onSelect,
  icon,
  title,
  subtitle,
  index = 0,
}: {
  selected: boolean;
  onSelect: () => void;
  icon?: ReactNode;
  title: string;
  subtitle?: string;
  index?: number;
}) {
  return (
    <motion.button
      type="button"
      onClick={onSelect}
      initial={{ opacity: 0, y: 14 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.05 + index * 0.04, duration: 0.35, ease: [0.22, 1, 0.36, 1] }}
      whileHover={{ y: -2 }}
      whileTap={{ scale: 0.985 }}
      aria-pressed={selected}
      className={cn(
        "group flex w-full items-center gap-3.5 rounded-2xl border-2 bg-card p-4 text-left transition-colors",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2",
        selected
          ? "border-primary bg-primary/[0.04] shadow-soft"
          : "border-border/70 hover:border-primary/40 hover:bg-secondary/40"
      )}
    >
      {icon && (
        <span
          className={cn(
            "flex h-10 w-10 shrink-0 items-center justify-center rounded-xl text-lg transition-colors",
            selected ? "bg-primary text-white" : "bg-secondary text-muted-foreground group-hover:text-foreground"
          )}
        >
          {icon}
        </span>
      )}
      <span className="min-w-0 flex-1">
        <span className="block text-[15px] font-semibold leading-snug">{title}</span>
        {subtitle && <span className="mt-0.5 block text-[13px] text-muted-foreground">{subtitle}</span>}
      </span>
      <span
        className={cn(
          "flex h-5 w-5 shrink-0 items-center justify-center rounded-full border-2 transition-colors",
          selected ? "border-primary bg-primary" : "border-border"
        )}
      >
        <AnimatePresence>
          {selected && (
            <motion.span initial={{ scale: 0 }} animate={{ scale: 1 }} exit={{ scale: 0 }}>
              <Check className="h-3 w-3 text-white" strokeWidth={3} />
            </motion.span>
          )}
        </AnimatePresence>
      </span>
    </motion.button>
  );
}

/** Compact chip used for score bands and short lists. */
export function ChipOption({
  selected,
  onSelect,
  children,
  index = 0,
}: {
  selected: boolean;
  onSelect: () => void;
  children: ReactNode;
  index?: number;
}) {
  return (
    <motion.button
      type="button"
      onClick={onSelect}
      initial={{ opacity: 0, scale: 0.94 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ delay: 0.05 + index * 0.04, duration: 0.3 }}
      whileTap={{ scale: 0.96 }}
      aria-pressed={selected}
      className={cn(
        "rounded-xl border-2 px-4 py-3 text-center text-[15px] font-semibold transition-colors",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2",
        selected
          ? "border-primary bg-primary text-white shadow-soft"
          : "border-border/70 bg-card hover:border-primary/40 hover:bg-secondary/40"
      )}
    >
      {children}
    </motion.button>
  );
}

/* -------------------------------------------------------------------------- */
/* Country picker                                                              */
/* -------------------------------------------------------------------------- */

export function CountryPicker({
  value,
  onChange,
}: {
  value: string | null;
  onChange: (code: string) => void;
}) {
  const [query, setQuery] = useState("");

  const results = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) {
      // Lead with the platform's core markets, then the rest alphabetically.
      const priority = PRIORITY_COUNTRIES.map((c) => countryByCode(c)).filter(
        (c): c is NonNullable<typeof c> => c !== null
      );
      const seen = new Set(PRIORITY_COUNTRIES);
      return [...priority, ...COUNTRIES.filter((c) => !seen.has(c.code))];
    }
    return COUNTRIES.filter((c) => c.name.toLowerCase().includes(q) || c.code.toLowerCase() === q).sort((a, b) => {
      const ai = a.name.toLowerCase().indexOf(q);
      const bi = b.name.toLowerCase().indexOf(q);
      return ai - bi || a.name.localeCompare(b.name);
    });
  }, [query]);

  const selected = countryByCode(value);

  return (
    <div className="space-y-3">
      <div className="relative">
        <Search className="pointer-events-none absolute left-3.5 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search 249 countries…"
          autoComplete="off"
          className="h-12 w-full rounded-xl border-2 border-border/70 bg-card pl-10 pr-10 text-[15px] outline-none transition-colors placeholder:text-muted-foreground focus:border-primary"
        />
        {query && (
          <button
            type="button"
            onClick={() => setQuery("")}
            aria-label="Clear search"
            className="absolute right-3 top-1/2 flex h-6 w-6 -translate-y-1/2 items-center justify-center rounded-full text-muted-foreground hover:bg-secondary"
          >
            <X className="h-3.5 w-3.5" />
          </button>
        )}
      </div>

      {selected && (
        <div className="flex items-center gap-2 rounded-xl border-2 border-primary bg-primary/[0.04] px-3.5 py-2.5">
          <span className="text-xl leading-none">{selected.flag}</span>
          <span className="text-[15px] font-semibold">{selected.name}</span>
          <Check className="ml-auto h-4 w-4 text-primary" strokeWidth={3} />
        </div>
      )}

      <div className="max-h-[280px] overflow-y-auto rounded-xl border border-border/70 bg-card">
        {results.length === 0 ? (
          <p className="px-4 py-6 text-center text-sm text-muted-foreground">No country matches “{query}”.</p>
        ) : (
          <ul className="divide-y divide-border/60">
            {results.map((c) => (
              <li key={c.code}>
                <button
                  type="button"
                  onClick={() => onChange(c.code)}
                  className={cn(
                    "flex w-full items-center gap-3 px-4 py-2.5 text-left text-[15px] transition-colors hover:bg-secondary/60",
                    value === c.code && "bg-primary/[0.06] font-semibold"
                  )}
                >
                  <span className="text-lg leading-none">{c.flag}</span>
                  <span className="flex-1">{c.name}</span>
                  {value === c.code && <Check className="h-4 w-4 text-primary" strokeWidth={3} />}
                </button>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

/* -------------------------------------------------------------------------- */
/* University picker (multi-select)                                            */
/* -------------------------------------------------------------------------- */

const MAX_UNIVERSITIES = 12;

export function UniversityPicker({
  value,
  onChange,
}: {
  value: string[];
  onChange: (next: string[]) => void;
}) {
  const [query, setQuery] = useState("");
  const results = useMemo(() => searchUniversities(query), [query]);

  function toggle(name: string) {
    if (value.includes(name)) {
      onChange(value.filter((v) => v !== name));
    } else if (value.length < MAX_UNIVERSITIES) {
      onChange([...value, name]);
    }
  }

  const trimmed = query.trim();
  const canAddCustom =
    trimmed.length > 2 &&
    !results.some((r) => r.name.toLowerCase() === trimmed.toLowerCase()) &&
    !value.some((v) => v.toLowerCase() === trimmed.toLowerCase());

  return (
    <div className="space-y-3">
      <div className="relative">
        <Search className="pointer-events-none absolute left-3.5 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search universities…"
          autoComplete="off"
          className="h-12 w-full rounded-xl border-2 border-border/70 bg-card pl-10 pr-4 text-[15px] outline-none transition-colors placeholder:text-muted-foreground focus:border-primary"
        />
      </div>

      {value.length > 0 && (
        <div className="flex flex-wrap gap-2">
          <AnimatePresence mode="popLayout">
            {value.map((name) => (
              <motion.button
                key={name}
                type="button"
                layout
                initial={{ opacity: 0, scale: 0.85 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.85 }}
                onClick={() => toggle(name)}
                className="flex items-center gap-1.5 rounded-full bg-primary px-3 py-1.5 text-[13px] font-medium text-white"
              >
                {name}
                <X className="h-3.5 w-3.5 opacity-80" />
              </motion.button>
            ))}
          </AnimatePresence>
        </div>
      )}

      <div className="max-h-[260px] overflow-y-auto rounded-xl border border-border/70 bg-card">
        <ul className="divide-y divide-border/60">
          {canAddCustom && (
            <li>
              <button
                type="button"
                onClick={() => {
                  toggle(trimmed);
                  setQuery("");
                }}
                className="flex w-full items-center gap-2 px-4 py-2.5 text-left text-[15px] text-primary transition-colors hover:bg-secondary/60"
              >
                Add &ldquo;{trimmed}&rdquo;
              </button>
            </li>
          )}
          {results.map((u) => {
            const selected = value.includes(u.name);
            const atLimit = !selected && value.length >= MAX_UNIVERSITIES;
            return (
              <li key={u.name}>
                <button
                  type="button"
                  disabled={atLimit}
                  onClick={() => toggle(u.name)}
                  className={cn(
                    "flex w-full items-center gap-3 px-4 py-2.5 text-left transition-colors hover:bg-secondary/60",
                    selected && "bg-primary/[0.06]",
                    atLimit && "cursor-not-allowed opacity-40"
                  )}
                >
                  <span className="min-w-0 flex-1">
                    <span className={cn("block truncate text-[15px]", selected && "font-semibold")}>{u.name}</span>
                    <span className="block text-[12px] text-muted-foreground">{u.country}</span>
                  </span>
                  {selected && <Check className="h-4 w-4 shrink-0 text-primary" strokeWidth={3} />}
                </button>
              </li>
            );
          })}
          {results.length === 0 && !canAddCustom && (
            <li className="px-4 py-6 text-center text-sm text-muted-foreground">Keep typing to add your own.</li>
          )}
        </ul>
      </div>

      <p className="text-center text-xs text-muted-foreground">
        {value.length}/{MAX_UNIVERSITIES} selected · pick as many as you like
      </p>
    </div>
  );
}

/* -------------------------------------------------------------------------- */
/* Month picker                                                                */
/* -------------------------------------------------------------------------- */

const MONTH_NAMES = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December",
];

export function MonthPicker({ value, onChange }: { value: string | null; onChange: (v: string) => void }) {
  const now = new Date();
  const [year, setYear] = useState(() => (value ? Number(value.slice(0, 4)) : now.getUTCFullYear()));

  const thisYear = now.getUTCFullYear();
  const thisMonth = now.getUTCMonth();

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-center gap-2">
        {[thisYear, thisYear + 1, thisYear + 2].map((y) => (
          <button
            key={y}
            type="button"
            onClick={() => setYear(y)}
            className={cn(
              "rounded-lg px-4 py-1.5 text-sm font-semibold transition-colors",
              year === y ? "bg-primary text-white" : "bg-secondary text-muted-foreground hover:text-foreground"
            )}
          >
            {y}
          </button>
        ))}
      </div>

      <div className="grid grid-cols-3 gap-2.5">
        {MONTH_NAMES.map((m, i) => {
          const key = `${year}-${String(i + 1).padStart(2, "0")}`;
          const past = year === thisYear && i < thisMonth;
          const selected = value === key;
          return (
            <motion.button
              key={key}
              type="button"
              disabled={past}
              onClick={() => onChange(key)}
              whileTap={past ? undefined : { scale: 0.96 }}
              className={cn(
                "rounded-xl border-2 py-3 text-[14px] font-semibold transition-colors",
                "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2",
                selected
                  ? "border-primary bg-primary text-white shadow-soft"
                  : "border-border/70 bg-card hover:border-primary/40 hover:bg-secondary/40",
                past && "cursor-not-allowed opacity-30 hover:border-border/70 hover:bg-card"
              )}
            >
              {m.slice(0, 3)}
            </motion.button>
          );
        })}
      </div>
    </div>
  );
}

/* -------------------------------------------------------------------------- */
/* Score slider                                                                */
/* -------------------------------------------------------------------------- */

export function ScoreSlider({
  value,
  onChange,
  min = 400,
  max = 1600,
}: {
  value: number;
  onChange: (v: number) => void;
  min?: number;
  max?: number;
}) {
  const pct = ((value - min) / (max - min)) * 100;

  return (
    <div className="space-y-5">
      <div className="text-center">
        <motion.p
          key={value}
          initial={{ scale: 0.92, opacity: 0.6 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ duration: 0.15 }}
          className="font-display text-5xl font-semibold tracking-tight text-primary"
        >
          {value}
        </motion.p>
        <p className="mt-1 text-sm text-muted-foreground">out of 1600</p>
      </div>

      <div className="px-1">
        <input
          type="range"
          min={min}
          max={max}
          step={10}
          value={value}
          onChange={(e) => onChange(Number(e.target.value))}
          aria-label="SAT score"
          className="h-2 w-full cursor-pointer appearance-none rounded-full outline-none focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2 [&::-moz-range-thumb]:h-6 [&::-moz-range-thumb]:w-6 [&::-moz-range-thumb]:cursor-pointer [&::-moz-range-thumb]:rounded-full [&::-moz-range-thumb]:border-2 [&::-moz-range-thumb]:border-white [&::-moz-range-thumb]:bg-primary [&::-moz-range-thumb]:shadow-card [&::-webkit-slider-thumb]:h-6 [&::-webkit-slider-thumb]:w-6 [&::-webkit-slider-thumb]:cursor-pointer [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:border-2 [&::-webkit-slider-thumb]:border-white [&::-webkit-slider-thumb]:bg-primary [&::-webkit-slider-thumb]:shadow-card"
          style={{
            background: `linear-gradient(to right, hsl(var(--primary)) ${pct}%, hsl(var(--secondary)) ${pct}%)`,
          }}
        />
        <div className="mt-2 flex justify-between text-xs text-muted-foreground">
          <span>{min}</span>
          <span>{max}</span>
        </div>
      </div>
    </div>
  );
}
