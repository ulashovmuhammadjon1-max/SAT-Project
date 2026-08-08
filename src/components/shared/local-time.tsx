"use client";

import { useEffect, useState } from "react";

export type LocalTimeFormat = "full" | "date" | "time" | "dayLabel" | "dateShort";

const OPTIONS: Record<LocalTimeFormat, Intl.DateTimeFormatOptions> = {
  full: { weekday: "long", month: "long", day: "numeric", hour: "numeric", minute: "2-digit" },
  date: { weekday: "long", month: "long", day: "numeric" },
  dateShort: { weekday: "short", month: "short", day: "numeric", hour: "numeric", minute: "2-digit" },
  time: { hour: "numeric", minute: "2-digit" },
  dayLabel: { weekday: "short", month: "short", day: "numeric" },
};

/**
 * Renders an instant in the *viewer's* timezone.
 *
 * Formatting is deliberately deferred to an effect: the server and the browser
 * are usually in different timezones, so formatting during SSR produces markup
 * that can't match on hydration. Rendering nothing on the first pass and the
 * real local time immediately after mount keeps booking times correct for the
 * student without a hydration mismatch or a flash of the wrong time.
 */
export function LocalTime({
  iso,
  format = "full",
  className,
}: {
  iso: string;
  format?: LocalTimeFormat;
  className?: string;
}) {
  const [text, setText] = useState("");

  useEffect(() => {
    setText(new Date(iso).toLocaleString(undefined, OPTIONS[format]));
  }, [iso, format]);

  // Before mount there is no reliable local value; reserve space so the layout
  // doesn't jump when it arrives.
  return (
    <span className={className} suppressHydrationWarning>
      {text || " "}
    </span>
  );
}

/** The viewer's IANA timezone, e.g. "Asia/Tashkent". Empty until mounted. */
export function useLocalTimezone() {
  const [tz, setTz] = useState("");
  useEffect(() => {
    setTz(Intl.DateTimeFormat().resolvedOptions().timeZone ?? "");
  }, []);
  return tz;
}
