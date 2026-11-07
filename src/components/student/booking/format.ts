"use client";

import { useEffect, useState } from "react";

/**
 * Local-time formatting for the booking page.
 *
 * Session times are stored as UTC instants and must be shown in the student's
 * own timezone, which the server does not know. Everything here runs in the
 * browser, and components render a placeholder until `useMounted` is true so
 * the server HTML never carries a UTC time that hydration would then change.
 */
export function useMounted() {
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);
  return mounted;
}

const asDate = (d: Date | string) => (d instanceof Date ? d : new Date(d));

export const monthShort = (d: Date | string) => asDate(d).toLocaleDateString(undefined, { month: "short" });
export const dayOfMonth = (d: Date | string) => asDate(d).getDate();
export const weekdayShort = (d: Date | string) => asDate(d).toLocaleDateString(undefined, { weekday: "short" });

export const dayLong = (d: Date | string) =>
  asDate(d).toLocaleDateString(undefined, { weekday: "long", month: "long", day: "numeric" });

export const timeOf = (d: Date | string) =>
  asDate(d).toLocaleTimeString(undefined, { hour: "numeric", minute: "2-digit" });

export function timeRange(start: Date | string, minutes: number) {
  const s = asDate(start);
  return `${timeOf(s)} – ${timeOf(new Date(s.getTime() + minutes * 60_000))}`;
}

/** A stable per-day key in the viewer's timezone, for grouping. */
export const dayKey = (d: Date | string) => asDate(d).toLocaleDateString("en-CA");

export const firstName = (name: string | null) => (name ? name.trim().split(/\s+/)[0] : null);
