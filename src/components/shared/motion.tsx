"use client";

import { useEffect, useRef, useState } from "react";

import { cn } from "@/lib/utils";

/**
 * Motion primitives.
 *
 * Two rules hold everything here together:
 *
 * 1. **Motion earns its place or it goes.** A number that counts up tells you
 *    it changed; a card that lifts tells you it is clickable. Decoration that
 *    says nothing is just latency the student has to sit through.
 * 2. **Nothing here runs inside the exam.** A timed test with a moving
 *    interface is actively hostile — the kiosk UI stays completely still.
 *
 * Everything respects `prefers-reduced-motion`: the hooks below check it and
 * jump straight to the final value, and `globals.css` collapses CSS animations
 * for anything they miss.
 */

function prefersReducedMotion(): boolean {
  if (typeof window === "undefined") return false;
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

/**
 * Runs a callback once the element is first scrolled into view.
 *
 * Animating on mount means everything below the fold has already finished
 * playing by the time the student scrolls to it, which is the same as no
 * animation at all.
 */
export function useInView<T extends HTMLElement>(rootMargin = "-40px") {
  const ref = useRef<T>(null);
  const [seen, setSeen] = useState(false);

  useEffect(() => {
    const el = ref.current;
    // No IntersectionObserver (or no element): show it rather than hide it
    // forever. A failed animation must never cost the content.
    if (!el || typeof IntersectionObserver === "undefined") {
      setSeen(true);
      return;
    }
    const io = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setSeen(true);
          io.disconnect();
        }
      },
      { rootMargin }
    );
    io.observe(el);
    return () => io.disconnect();
  }, [rootMargin]);

  return { ref, seen };
}

/** Fades a block up the first time it scrolls into view. */
export function Reveal({
  children,
  className,
  delay = 0,
}: {
  children: React.ReactNode;
  className?: string;
  delay?: number;
}) {
  const { ref, seen } = useInView<HTMLDivElement>();
  return (
    <div
      ref={ref}
      style={{ transitionDelay: `${delay}ms` }}
      className={cn(
        "transition-all duration-500 ease-out",
        seen ? "translate-y-0 opacity-100" : "translate-y-3 opacity-0",
        className
      )}
    >
      {children}
    </div>
  );
}

/**
 * A number that counts up to its value.
 *
 * Driven by requestAnimationFrame against a wall-clock duration rather than a
 * fixed step per frame, so it takes the same time on a 60Hz laptop and a 120Hz
 * phone instead of running twice as fast on one of them.
 */
export function CountUp({
  value,
  duration = 900,
  className,
  suffix,
}: {
  value: number;
  duration?: number;
  className?: string;
  suffix?: string;
}) {
  const { ref, seen } = useInView<HTMLSpanElement>();
  const [shown, setShown] = useState(0);

  useEffect(() => {
    if (!seen) return;
    if (prefersReducedMotion() || value === 0) {
      setShown(value);
      return;
    }

    let raf = 0;
    const start = performance.now();
    // Ease-out cubic: fast at first, settling at the end — a linear count
    // reads like a loading spinner rather than an arrival.
    const ease = (t: number) => 1 - Math.pow(1 - t, 3);

    const tick = (now: number) => {
      const t = Math.min(1, (now - start) / duration);
      setShown(Math.round(value * ease(t)));
      if (t < 1) raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [seen, value, duration]);

  return (
    <span ref={ref} className={cn("tabular-nums", className)}>
      {shown.toLocaleString()}
      {suffix}
    </span>
  );
}

/** A progress bar that fills from zero when it first appears. */
export function AnimatedProgress({
  value,
  className,
  barClassName,
}: {
  value: number;
  className?: string;
  barClassName?: string;
}) {
  const { ref, seen } = useInView<HTMLDivElement>();
  const pct = Math.max(0, Math.min(100, value));

  return (
    <div
      ref={ref}
      role="progressbar"
      aria-valuenow={pct}
      aria-valuemin={0}
      aria-valuemax={100}
      className={cn("h-2 w-full overflow-hidden rounded-full bg-muted", className)}
    >
      <div
        className={cn(
          "h-full rounded-full bg-primary transition-[width] duration-[900ms] ease-out",
          barClassName
        )}
        style={{ width: seen ? `${pct}%` : "0%" }}
      />
    </div>
  );
}

/**
 * Soft drifting colour behind a hero section.
 *
 * `aria-hidden` and pointer-events-none: it is wallpaper, and a screen reader
 * announcing three empty divs helps nobody.
 */
export function AuroraBackdrop({ className }: { className?: string }) {
  return (
    <div
      aria-hidden
      className={cn("pointer-events-none absolute inset-0 overflow-hidden", className)}
    >
      <div className="absolute -left-24 -top-24 h-72 w-72 rounded-full bg-primary/20 blur-3xl animate-float" />
      <div
        className="absolute -right-16 top-12 h-64 w-64 rounded-full bg-violet-500/15 blur-3xl animate-float"
        style={{ animationDelay: "2s" }}
      />
      <div
        className="absolute bottom-0 left-1/3 h-56 w-56 rounded-full bg-emerald-400/10 blur-3xl animate-float"
        style={{ animationDelay: "4s" }}
      />
    </div>
  );
}
