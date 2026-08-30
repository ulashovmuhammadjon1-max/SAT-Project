"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useMemo, useState, useTransition } from "react";
import { toast } from "sonner";
import { ArrowRight, Check, Clock, Loader2, Plus, Search, X } from "lucide-react";

import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from "@/components/ui/alert-dialog";
import { AP_CATEGORIES } from "@/lib/ap/catalog";
import {
  addSubject,
  removeSubject,
  type CatalogSubject,
} from "@/server/actions/student/ap-subjects";
import { cn } from "@/lib/utils";

/**
 * The AP subject catalog.
 *
 * Every subject is handed down from the server in one payload, so search and
 * filtering are pure client-side work over an array — no round trip per
 * keystroke, and the list stays usable at thirty-odd subjects.
 *
 * Add and remove are real server actions, applied optimistically: the card
 * flips the moment it is clicked and only reverts if the action comes back
 * with an error. COMING_SOON subjects never render an Add control at all; the
 * server refuses them too, but a student should not be offered something that
 * cannot happen.
 */

type Availability = "all" | "added" | "soon";

const FILTERS: { id: Availability; label: string }[] = [
  { id: "added", label: "Added" },
  { id: "soon", label: "Coming soon" },
];

/** Chip styling, shared by the category row and the availability row. */
function chipClass(active: boolean) {
  return cn(
    "rounded-full border px-3.5 py-1.5 text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background",
    active
      ? "border-transparent bg-navy-900 text-white"
      : "border-border bg-card text-muted-foreground hover:border-primary/40 hover:text-foreground",
  );
}

export function SubjectCatalog({ subjects }: { subjects: CatalogSubject[] }) {
  const router = useRouter();
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState<string>("ALL");
  const [availability, setAvailability] = useState<Availability>("all");
  /**
   * Optimistic overrides keyed by subject code. The server value stays the
   * source of truth; an entry here just wins until the page revalidates, at
   * which point the two agree and nothing flickers.
   */
  const [overrides, setOverrides] = useState<Record<string, boolean>>({});
  const [pendingCode, setPendingCode] = useState<string | null>(null);
  const [confirming, setConfirming] = useState<CatalogSubject | null>(null);
  const [, startTransition] = useTransition();

  const isAdded = (s: CatalogSubject) => overrides[s.code] ?? s.added;

  const categoryLabel = useMemo(
    () => new Map(AP_CATEGORIES.map((c) => [c.id as string, c.label])),
    [],
  );

  const visible = useMemo(() => {
    const needle = query.trim().toLowerCase();
    return subjects.filter((s) => {
      if (category !== "ALL" && s.category !== category) return false;
      if (availability === "added" && !(overrides[s.code] ?? s.added)) return false;
      if (availability === "soon" && s.status !== "COMING_SOON") return false;
      if (!needle) return true;
      const haystack = `${s.name} ${s.short} ${s.blurb} ${categoryLabel.get(s.category) ?? ""}`;
      return haystack.toLowerCase().includes(needle);
    });
  }, [subjects, query, category, availability, overrides, categoryLabel]);

  function runAdd(subject: CatalogSubject) {
    setOverrides((o) => ({ ...o, [subject.code]: true }));
    setPendingCode(subject.code);
    startTransition(async () => {
      const result = await addSubject({ subject: subject.code });
      setPendingCode(null);
      if (result.error) {
        // Put the card back the way the server still sees it.
        setOverrides((o) => ({ ...o, [subject.code]: false }));
        toast.error(result.error);
        return;
      }
      toast.success(`${subject.name} added to My Subjects.`);
      router.refresh();
    });
  }

  function runRemove(subject: CatalogSubject) {
    setConfirming(null);
    setOverrides((o) => ({ ...o, [subject.code]: false }));
    setPendingCode(subject.code);
    startTransition(async () => {
      const result = await removeSubject({ subject: subject.code });
      setPendingCode(null);
      if (result.error) {
        setOverrides((o) => ({ ...o, [subject.code]: true }));
        toast.error(result.error);
        return;
      }
      toast.success(`${subject.name} removed. Your progress is kept.`);
      router.refresh();
    });
  }

  const addedCount = subjects.filter((s) => isAdded(s)).length;

  return (
    <section aria-labelledby="ap-explore-heading" className="space-y-4">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h2
            id="ap-explore-heading"
            className="font-display text-lg font-semibold tracking-tight"
          >
            Explore AP subjects
          </h2>
          <p className="mt-0.5 text-sm text-muted-foreground">
            {subjects.length} subjects · {addedCount} in your list. Add the ones you are sitting
            and they follow you into the sidebar.
          </p>
        </div>
      </div>

      {/* Search */}
      <div className="relative">
        <label htmlFor="ap-subject-search" className="sr-only">
          Search AP subjects
        </label>
        <Search
          aria-hidden
          className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground"
        />
        <input
          id="ap-subject-search"
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search subjects — calculus, history, psychology…"
          className="h-11 w-full rounded-xl border border-input bg-card pl-9 pr-10 text-sm shadow-sm transition-colors placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-1"
        />
        {query && (
          <button
            type="button"
            onClick={() => setQuery("")}
            aria-label="Clear search"
            className="absolute right-2 top-1/2 flex h-7 w-7 -translate-y-1/2 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
          >
            <X className="h-4 w-4" />
          </button>
        )}
      </div>

      {/* Category chips */}
      <div className="flex flex-wrap gap-2" role="group" aria-label="Filter by category">
        <button
          type="button"
          aria-pressed={category === "ALL"}
          onClick={() => setCategory("ALL")}
          className={chipClass(category === "ALL")}
        >
          All
        </button>
        {AP_CATEGORIES.map((c) => (
          <button
            key={c.id}
            type="button"
            aria-pressed={category === c.id}
            onClick={() => setCategory(c.id)}
            className={chipClass(category === c.id)}
          >
            {c.label}
          </button>
        ))}
      </div>

      {/* Availability chips. Mutually exclusive on purpose — "Added" and
          "Coming soon" can never both be true of one subject, so letting both
          be pressed would only ever produce an empty list. */}
      <div className="flex flex-wrap gap-2" role="group" aria-label="Filter by availability">
        {FILTERS.map((f) => {
          const active = availability === f.id;
          return (
            <button
              key={f.id}
              type="button"
              aria-pressed={active}
              onClick={() => setAvailability(active ? "all" : f.id)}
              className={cn(
                chipClass(active),
                !active && "border-dashed",
              )}
            >
              {f.id === "added" ? (
                <Check aria-hidden className="mr-1.5 inline h-3.5 w-3.5 align-[-2px]" />
              ) : (
                <Clock aria-hidden className="mr-1.5 inline h-3.5 w-3.5 align-[-2px]" />
              )}
              {f.label}
            </button>
          );
        })}
      </div>

      {visible.length === 0 ? (
        <p className="rounded-2xl border border-dashed border-border bg-card/60 px-5 py-10 text-center text-sm text-muted-foreground">
          No subjects match “{query.trim() || "that filter"}”. Try a different search or clear the
          filters.
        </p>
      ) : (
        <ul className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
          {visible.map((s) => (
            <SubjectCard
              key={s.code}
              subject={s}
              added={isAdded(s)}
              busy={pendingCode === s.code}
              categoryLabel={categoryLabel.get(s.category) ?? s.category}
              onAdd={() => runAdd(s)}
              onRemove={() => setConfirming(s)}
            />
          ))}
        </ul>
      )}

      <AlertDialog
        open={confirming !== null}
        onOpenChange={(open) => !open && setConfirming(null)}
      >
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>Remove from My Subjects?</AlertDialogTitle>
            <AlertDialogDescription>
              Your progress and scores are kept — you can add it back any time.
              {confirming && <> Removing {confirming.name} only takes it out of your sidebar.</>}
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>Keep it</AlertDialogCancel>
            <AlertDialogAction onClick={() => confirming && runRemove(confirming)}>
              Remove
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </section>
  );
}

function SubjectCard({
  subject,
  added,
  busy,
  categoryLabel,
  onAdd,
  onRemove,
}: {
  subject: CatalogSubject;
  added: boolean;
  busy: boolean;
  categoryLabel: string;
  onAdd: () => void;
  onRemove: () => void;
}) {
  const soon = subject.status === "COMING_SOON";

  return (
    <li className="flex flex-col rounded-2xl border border-border/70 bg-card p-5 shadow-soft transition-shadow hover:shadow-lg">
      <div className="flex items-start gap-3">
        <span
          aria-hidden
          className={cn(
            "flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-gradient-to-br text-xs font-bold text-white",
            subject.gradient,
          )}
        >
          {subject.short.slice(0, 2).toUpperCase()}
        </span>
        <div className="min-w-0 flex-1">
          <h3 className="font-display text-base font-semibold leading-snug tracking-tight">
            {subject.name}
          </h3>
          <p className="mt-0.5 text-xs text-muted-foreground">{categoryLabel}</p>
        </div>
        {added && (
          <span className="shrink-0 rounded-full bg-success/15 px-2 py-0.5 text-[10px] font-bold uppercase tracking-wide text-success">
            Added
          </span>
        )}
      </div>

      <p className="mt-3 flex-1 text-sm leading-relaxed text-muted-foreground">{subject.blurb}</p>

      <p className="mt-3 text-xs text-muted-foreground">
        {soon ? (
          <span className="inline-flex items-center gap-1.5">
            <Clock aria-hidden className="h-3 w-3" /> Questions in progress
          </span>
        ) : subject.questionCount > 0 ? (
          <>{subject.questionCount.toLocaleString()} questions ready</>
        ) : (
          <>First units landing shortly</>
        )}
      </p>

      <div className="mt-4 flex items-center gap-2">
        {soon ? (
          <button
            type="button"
            disabled
            aria-disabled="true"
            className="inline-flex h-9 flex-1 cursor-not-allowed items-center justify-center gap-1.5 rounded-lg border border-dashed border-border bg-secondary/50 px-3 text-sm font-medium text-muted-foreground"
          >
            <Clock aria-hidden className="h-3.5 w-3.5" /> Coming soon
          </button>
        ) : added ? (
          <>
            <Link
              href={`/ap/${subject.slug}`}
              className="inline-flex h-9 flex-1 items-center justify-center gap-1.5 rounded-lg bg-primary px-3 text-sm font-semibold text-primary-foreground shadow-soft transition-colors hover:bg-primary-600 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
            >
              Open <ArrowRight aria-hidden className="h-3.5 w-3.5" />
            </Link>
            <button
              type="button"
              onClick={onRemove}
              disabled={busy}
              aria-label={`Remove ${subject.name} from My Subjects`}
              className="inline-flex h-9 items-center justify-center gap-1.5 rounded-lg border border-border px-3 text-sm font-medium text-muted-foreground transition-colors hover:border-destructive/50 hover:text-destructive focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:opacity-60"
            >
              {busy ? (
                <Loader2 aria-hidden className="h-3.5 w-3.5 animate-spin" />
              ) : (
                <X aria-hidden className="h-3.5 w-3.5" />
              )}
              Remove
            </button>
          </>
        ) : (
          <button
            type="button"
            onClick={onAdd}
            disabled={busy}
            className="inline-flex h-9 flex-1 items-center justify-center gap-1.5 rounded-lg border border-border bg-background px-3 text-sm font-semibold transition-colors hover:border-primary/50 hover:text-primary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:opacity-60"
          >
            {busy ? (
              <Loader2 aria-hidden className="h-3.5 w-3.5 animate-spin" />
            ) : (
              <Plus aria-hidden className="h-3.5 w-3.5" />
            )}
            Add to My Subjects
          </button>
        )}
      </div>
    </li>
  );
}
