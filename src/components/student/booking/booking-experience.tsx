"use client";

import { useEffect, useMemo, useRef, useState, useTransition } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { AlertCircle, ArrowLeft, ArrowRight, Check, X } from "lucide-react";

import { Button } from "@/components/ui/button";
import { useLocalTimezone } from "@/components/shared/local-time";
import type { TelegramState } from "@/components/student/telegram-requirement";
import { isSatTopic, topicOf } from "@/lib/booking/topics";
import { cn } from "@/lib/utils";
import { createBooking, type BookingContext, type OpenSlot } from "@/server/actions/student/bookings";

import {
  BookingSuccess,
  ConfirmDialog,
  NotEnoughCoins,
  PriceBreakdown,
  SessionFacts,
} from "./booking-panels";
import { DetailsStep, RequirementsStep, validateDetails, type DetailsErrors, type DetailsValues } from "./booking-steps";
import { Coins } from "./coins";
import { SessionBrowser } from "./session-browser";

export interface BookingPrefill {
  name: string;
  email: string;
  currentScore: number | null;
  targetScore: number | null;
  satDate: string | null;
  weakestArea: string | null;
}

type Step = 1 | 2 | 3;
const STEPS: { n: Step; label: string }[] = [
  { n: 1, label: "Community" },
  { n: 2, label: "About you" },
  { n: 3, label: "Review" },
];

type Banner = { tone: "error" | "info"; text: string; link?: { href: string; label: string } } | null;

/**
 * The student booking page: discover a session, then book it in three short
 * steps (community, about you, review), then a final confirmation.
 *
 * Nothing here decides anything that matters. Price, balance, capacity, the
 * one-active-booking rule and the community requirements are all decided again
 * by createBooking on the server; this component shows them honestly before
 * the student commits and routes each server answer to a clear next step.
 */
export function BookingExperience({
  slots,
  context,
  prefill,
  telegram,
  existing,
}: {
  slots: OpenSlot[];
  context: BookingContext;
  prefill: BookingPrefill;
  telegram: { botUsername: string; state: TelegramState } | null;
  /**
   * Rendered instead of the browser when the student already holds an active
   * booking. Passed in rather than rendered by the page so this component stays
   * mounted when booking revalidates the page: otherwise the fresh "already
   * booked" view would replace the success screen before it could be read.
   */
  existing: React.ReactNode | null;
}) {
  const router = useRouter();
  const timezone = useLocalTimezone();
  const [isPending, startTransition] = useTransition();
  const topRef = useRef<HTMLDivElement>(null);

  const [phase, setPhase] = useState<"browse" | "book" | "done">("browse");
  const [slotId, setSlotId] = useState<string | null>(null);
  const [step, setStep] = useState<Step>(1);
  const [banner, setBanner] = useState<Banner>(null);
  const [confirmOpen, setConfirmOpen] = useState(false);
  const [result, setResult] = useState<{ coinsSpent: number; balance: number } | null>(null);
  // Keep the booked slot after the list refreshes it away.
  const [bookedSlot, setBookedSlot] = useState<OpenSlot | null>(null);

  const [acked, setAcked] = useState<Set<string>>(new Set());
  const [values, setValues] = useState<DetailsValues>({
    name: prefill.name,
    email: prefill.email,
    currentScore: prefill.currentScore?.toString() ?? "",
    targetScore: prefill.targetScore?.toString() ?? "",
    satDate: prefill.satDate ?? "",
    weakest: prefill.weakestArea ?? "",
    hours: "",
    notes: "",
  });
  const [errors, setErrors] = useState<DetailsErrors>({});

  const selected = useMemo(() => slots.find((s) => s.id === slotId) ?? null, [slots, slotId]);
  const askSat = selected ? isSatTopic(topicOf(selected.subject)) : false;

  // A verified requirement is satisfied by the real check, not a tick.
  const requirementsDone = context.requirements.every((r) =>
    r.verification === "verified" && r.id === "telegram" && telegram ? telegram.state.isMember : acked.has(r.id),
  );

  // Move focus and view to the top of the flow whenever the stage changes,
  // so keyboard and screen-reader users land on the new content.
  const firstRender = useRef(true);
  useEffect(() => {
    if (firstRender.current) {
      firstRender.current = false;
      return;
    }
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    topRef.current?.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
    topRef.current?.focus({ preventScroll: true });
  }, [phase, step]);

  function startBooking(id: string) {
    setSlotId(id);
    setStep(requirementsDone ? 2 : 1);
    setBanner(null);
    setPhase("book");
  }

  function backToBrowse() {
    setPhase("browse");
    setBanner(null);
  }

  function goToStep(next: Step) {
    if (next >= 2 && !requirementsDone) {
      setStep(1);
      setBanner({ tone: "error", text: "Confirm both community steps to continue." });
      return;
    }
    if (next === 3) {
      const e = validateDetails(values, askSat);
      setErrors(e);
      if (Object.keys(e).length) {
        setStep(2);
        setBanner({ tone: "error", text: "Check the highlighted fields." });
        return;
      }
    }
    setBanner(null);
    setStep(next);
  }

  function book() {
    if (!selected) return;
    startTransition(async () => {
      const res = await createBooking({
        slotId: selected.id,
        name: values.name.trim(),
        email: values.email.trim(),
        currentScore: askSat && values.currentScore ? parseInt(values.currentScore, 10) : null,
        targetScore: askSat && values.targetScore ? parseInt(values.targetScore, 10) : null,
        satDate: askSat ? values.satDate || null : null,
        studyHoursPerWeek: values.hours ? parseInt(values.hours, 10) : null,
        weakestArea: askSat ? values.weakest || null : null,
        notes: values.notes.trim() || null,
        timezone,
        acknowledgedRequirements: [...acked],
      });
      setConfirmOpen(false);

      if (res.ok) {
        setBookedSlot(selected);
        setResult({ coinsSpent: res.coinsSpent, balance: res.balance });
        setPhase("done");
        // No router.refresh() here: the page would re-render as "you already
        // have a session booked" and replace this confirmation before it is read.
        return;
      }

      // Every failure leaves the coins untouched (the server rolls back), and
      // each one points at the step that can fix it.
      switch (res.reason) {
        case "slot_gone":
          setPhase("browse");
          setBanner({
            tone: "info",
            text: "That session is no longer available. It was just booked or closed. Your coins were not touched. Here is what is still open.",
          });
          router.refresh();
          break;
        case "insufficient_coins":
          setBanner({ tone: "error", text: res.error });
          router.refresh();
          break;
        case "requirements":
          setStep(1);
          setBanner({ tone: "error", text: res.error });
          break;
        case "validation":
          setStep(2);
          setBanner({ tone: "error", text: res.error });
          break;
        case "already_booked":
          setBanner({
            tone: "error",
            text: `${res.error} You can hold one 1-on-1 session at a time.`,
            link: { href: "/bookings", label: "Open My Sessions" },
          });
          break;
        default:
          setBanner({ tone: "error", text: res.error || "The booking could not be completed. Your coins have not been touched." });
      }
    });
  }

  if (phase === "done" && bookedSlot && result) {
    return (
      <div ref={topRef} tabIndex={-1} className="outline-none">
        <BookingSuccess slot={bookedSlot} coinsSpent={result.coinsSpent} balance={result.balance} email={values.email.trim()} />
      </div>
    );
  }

  if (existing) return <>{existing}</>;

  if (phase === "browse" || !selected) {
    return (
      <div ref={topRef} tabIndex={-1} className="space-y-6 outline-none">
        {banner && <BannerView banner={banner} onClose={() => setBanner(null)} />}
        {!context.canAfford && (
          <div className="flex flex-col gap-4 rounded-xl border border-border bg-secondary/40 p-5 sm:flex-row sm:items-center sm:justify-between">
            <p className="text-[15px] leading-relaxed">
              <strong>You need {context.shortfall} more coins to book.</strong>{" "}
              <span className="text-muted-foreground">
                A session costs {context.cost} coins and you have {context.balance}. Invite a friend to earn{" "}
                {context.referralRewardCoins}.
              </span>
            </p>
            <Button asChild variant="outline" className="h-11 shrink-0 px-5">
              <Link href="/invite">Earn coins</Link>
            </Button>
          </div>
        )}
        <SessionBrowser slots={slots} cost={context.cost} canAfford={context.canAfford} onBook={startBooking} />
      </div>
    );
  }

  return (
    <div ref={topRef} tabIndex={-1} className="space-y-6 outline-none">
      <Button type="button" variant="ghost" onClick={backToBrowse} className="-ml-3 h-11 gap-2 px-3 text-[15px]">
        <ArrowLeft className="h-4 w-4" aria-hidden /> All sessions
      </Button>

      <div className="grid grid-cols-1 gap-6 lg:grid-cols-[minmax(0,1fr)_22rem] lg:items-start lg:gap-8">
        {/* Summary: first on small screens so the student always sees what they are booking. */}
        <aside aria-label="Booking summary" className="space-y-5 rounded-xl border border-border bg-card p-5 sm:p-6 lg:sticky lg:top-6 lg:order-2">
          <SessionFacts slot={selected} />
          <div className="border-t border-border pt-5">
            <PriceBreakdown context={context} />
          </div>
        </aside>

        <div className="min-w-0 rounded-xl border border-border bg-card lg:order-1">
          {!context.canAfford ? (
            <div className="p-5 sm:p-7">
              {banner && <BannerView banner={banner} onClose={() => setBanner(null)} className="mb-5" />}
              <NotEnoughCoins context={context} />
            </div>
          ) : (
            <>
              <Stepper step={step} done={{ 1: requirementsDone, 2: step === 3 }} onGo={goToStep} />
              <div className="p-5 sm:p-7">
                {banner && <BannerView banner={banner} onClose={() => setBanner(null)} className="mb-6" />}

                <h2 className="mb-5 font-display text-xl font-semibold tracking-tight">
                  {step === 1 ? "Join the community" : step === 2 ? "About you" : "Review your booking"}
                </h2>

                {step === 1 && (
                  <RequirementsStep
                    requirements={context.requirements}
                    telegram={telegram}
                    acked={acked}
                    onToggle={(id, on) =>
                      setAcked((prev) => {
                        const next = new Set(prev);
                        if (on) next.add(id);
                        else next.delete(id);
                        return next;
                      })
                    }
                  />
                )}

                {step === 2 && (
                  <DetailsStep
                    values={values}
                    errors={errors}
                    askSat={askSat}
                    timezone={timezone}
                    onChange={(k, v) => {
                      setValues((prev) => ({ ...prev, [k]: v }));
                      if (errors[k]) setErrors((prev) => ({ ...prev, [k]: undefined }));
                    }}
                  />
                )}

                {step === 3 && (
                  <ReviewStep values={values} askSat={askSat} cost={context.cost} />
                )}

                <div className="mt-8 flex flex-col-reverse gap-3 border-t border-border pt-6 sm:flex-row sm:items-center sm:justify-between">
                  {step > 1 ? (
                    <Button
                      type="button"
                      variant="outline"
                      onClick={() => goToStep((step - 1) as Step)}
                      className="h-12 px-5 text-[15px]"
                    >
                      <ArrowLeft className="h-4 w-4" aria-hidden /> Back
                    </Button>
                  ) : (
                    <span className="hidden sm:block" />
                  )}
                  {step < 3 ? (
                    <div className="flex flex-col gap-2 sm:items-end">
                      <Button
                        type="button"
                        onClick={() => goToStep((step + 1) as Step)}
                        disabled={step === 1 && !requirementsDone}
                        className="h-12 px-6 text-[15px]"
                      >
                        Continue <ArrowRight className="h-4 w-4" aria-hidden />
                      </Button>
                      {step === 1 && !requirementsDone && (
                        <p className="text-sm text-muted-foreground">Confirm both accounts to continue.</p>
                      )}
                    </div>
                  ) : (
                    <Button
                      type="button"
                      onClick={() => setConfirmOpen(true)}
                      disabled={isPending}
                      className="h-[3.25rem] px-6 text-base"
                    >
                      Confirm booking · {context.cost} coins
                    </Button>
                  )}
                </div>
              </div>
            </>
          )}
        </div>
      </div>

      <ConfirmDialog
        open={confirmOpen}
        onOpenChange={setConfirmOpen}
        slot={selected}
        cost={context.cost}
        requirements={context.requirements}
        pending={isPending}
        onConfirm={book}
      />
    </div>
  );
}

function Stepper({
  step,
  done,
  onGo,
}: {
  step: Step;
  done: Record<1 | 2, boolean>;
  onGo: (s: Step) => void;
}) {
  return (
    <nav aria-label="Booking steps" className="border-b border-border px-5 py-4 sm:px-7">
      <ol className="flex items-center gap-2 sm:gap-3">
        {STEPS.map((s, i) => {
          const current = s.n === step;
          const complete = s.n < step && (s.n === 3 || done[s.n as 1 | 2]);
          const reachable = s.n < step;
          return (
            <li key={s.n} className="flex min-w-0 flex-1 items-center gap-2 sm:gap-3">
              <button
                type="button"
                onClick={() => reachable && onGo(s.n)}
                disabled={!reachable}
                aria-current={current ? "step" : undefined}
                className={cn(
                  "flex min-h-11 min-w-0 items-center gap-2.5 rounded-lg pr-2 text-left text-sm font-medium",
                  "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
                  reachable ? "cursor-pointer hover:text-foreground" : "cursor-default",
                  current ? "text-foreground" : "text-muted-foreground",
                )}
              >
                <span
                  className={cn(
                    "flex h-8 w-8 shrink-0 items-center justify-center rounded-full border text-sm tabular-nums",
                    current && "border-primary bg-primary text-primary-foreground",
                    complete && "border-success bg-success text-white",
                    !current && !complete && "border-border",
                  )}
                >
                  {complete ? <Check className="h-4 w-4" aria-hidden /> : s.n}
                </span>
                <span className={cn("truncate", !current && "hidden sm:inline")}>{s.label}</span>
                {complete && <span className="sr-only">(completed)</span>}
              </button>
              {i < STEPS.length - 1 && <span aria-hidden className="h-px flex-1 bg-border" />}
            </li>
          );
        })}
      </ol>
    </nav>
  );
}

function ReviewStep({ values, askSat, cost }: { values: DetailsValues; askSat: boolean; cost: number }) {
  const rows: [string, string][] = [
    ["Name", values.name.trim()],
    ["Email", values.email.trim()],
    ...(values.notes.trim() ? ([["Focus", values.notes.trim()]] as [string, string][]) : []),
    ...(askSat && values.currentScore ? ([["Current SAT score", values.currentScore]] as [string, string][]) : []),
    ...(askSat && values.targetScore ? ([["Target SAT score", values.targetScore]] as [string, string][]) : []),
  ];
  return (
    <div className="space-y-6">
      <dl className="divide-y divide-border rounded-xl border border-border">
        {rows.map(([k, v]) => (
          <div key={k} className="grid grid-cols-1 gap-1 px-4 py-3 sm:grid-cols-[10rem_minmax(0,1fr)] sm:gap-4">
            <dt className="text-sm text-muted-foreground">{k}</dt>
            <dd className="break-words text-[15px]">{v}</dd>
          </div>
        ))}
      </dl>
      <div className="flex items-center justify-between gap-4 rounded-xl bg-secondary/60 px-5 py-4">
        <p className="text-[15px] font-semibold">Total for this session</p>
        <Coins value={cost} size="lg" />
      </div>
      <p className="text-sm leading-relaxed text-muted-foreground">
        This sends a request. It stays <strong className="text-foreground">pending</strong> until it is approved, and
        you get an email either way.
      </p>
    </div>
  );
}

function BannerView({ banner, onClose, className }: { banner: NonNullable<Banner>; onClose: () => void; className?: string }) {
  return (
    <div
      role={banner.tone === "error" ? "alert" : "status"}
      className={cn(
        "flex items-start gap-3 rounded-xl border p-4",
        banner.tone === "error" ? "border-destructive/40 bg-destructive/5" : "border-primary/30 bg-primary/5",
        className,
      )}
    >
      <AlertCircle
        className={cn("mt-0.5 h-5 w-5 shrink-0", banner.tone === "error" ? "text-destructive" : "text-primary")}
        aria-hidden
      />
      <div className="min-w-0 flex-1 text-[15px] leading-relaxed">
        <p>{banner.text}</p>
        {banner.link && (
          <Link href={banner.link.href} className="mt-1 inline-block font-medium text-primary underline-offset-4 hover:underline">
            {banner.link.label}
          </Link>
        )}
      </div>
      <button
        type="button"
        onClick={onClose}
        aria-label="Dismiss"
        className="-m-2 flex h-11 w-11 shrink-0 items-center justify-center rounded-md text-muted-foreground hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
      >
        <X className="h-4 w-4" />
      </button>
    </div>
  );
}
