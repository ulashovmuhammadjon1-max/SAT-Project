"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { createEvent } from "@/server/actions/admin/bookings";
import { EVENT_TYPE_LABELS } from "@/lib/events";

const TYPES = ["TEST_ANALYSIS", "FINANCIAL_LITERACY", "LECTURE", "WORKSHOP"] as const;

/**
 * Publish a group event.
 *
 * `repeatWeeks` exists because the weekly review is the main use of this form
 * and publishing it one week at a time would be a chore that quietly stops
 * happening.
 */
export function EventCreator() {
  const router = useRouter();
  const [pending, startTransition] = useTransition();
  const [type, setType] = useState<(typeof TYPES)[number]>("TEST_ANALYSIS");
  const [title, setTitle] = useState(EVENT_TYPE_LABELS.TEST_ANALYSIS);
  const [description, setDescription] = useState("");
  const [date, setDate] = useState("");
  const [time, setTime] = useState("18:00");
  const [duration, setDuration] = useState(60);
  const [capacity, setCapacity] = useState(30);
  const [repeatWeeks, setRepeatWeeks] = useState(1);

  function submit() {
    startTransition(async () => {
      const res = await createEvent({
        date,
        time,
        durationMinutes: duration,
        // The admin types a wall-clock time; the server turns it into an
        // absolute instant using this offset.
        tzOffsetMinutes: new Date().getTimezoneOffset(),
        sessionType: type,
        title,
        description,
        capacity,
        repeatWeeks,
      });
      if (res.ok) {
        toast.success(
          res.created === 0
            ? "Nothing new — those times already exist."
            : `Published ${res.created} event${res.created === 1 ? "" : "s"}`,
        );
        setDate("");
        router.refresh();
      } else {
        toast.error(res.error ?? "Couldn't publish that.");
      }
    });
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-base">Publish an event</CardTitle>
      </CardHeader>
      <CardContent className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <Label htmlFor="ev-type">Type</Label>
          <select
            id="ev-type"
            value={type}
            onChange={(e) => {
              const next = e.target.value as (typeof TYPES)[number];
              setType(next);
              // Only overwrite a title the admin has not customised.
              if (TYPES.some((t) => EVENT_TYPE_LABELS[t] === title)) {
                setTitle(EVENT_TYPE_LABELS[next]);
              }
            }}
            className="w-full rounded-lg border border-input bg-background px-3 py-2 text-sm"
          >
            {TYPES.map((t) => (
              <option key={t} value={t}>
                {EVENT_TYPE_LABELS[t]}
              </option>
            ))}
          </select>
        </div>

        <div className="space-y-1.5">
          <Label htmlFor="ev-title">Title</Label>
          <Input id="ev-title" value={title} onChange={(e) => setTitle(e.target.value)} />
        </div>

        <div className="space-y-1.5 sm:col-span-2">
          <Label htmlFor="ev-desc">Description</Label>
          <Textarea
            id="ev-desc"
            rows={2}
            placeholder="What will you cover? Students read this before registering."
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>

        <div className="space-y-1.5">
          <Label htmlFor="ev-date">Date</Label>
          <Input id="ev-date" type="date" value={date} onChange={(e) => setDate(e.target.value)} />
        </div>
        <div className="space-y-1.5">
          <Label htmlFor="ev-time">Start time (your timezone)</Label>
          <Input id="ev-time" type="time" value={time} onChange={(e) => setTime(e.target.value)} />
        </div>

        <div className="space-y-1.5">
          <Label htmlFor="ev-dur">Duration (minutes)</Label>
          <Input
            id="ev-dur"
            type="number"
            min={10}
            max={240}
            value={duration}
            onChange={(e) => setDuration(parseInt(e.target.value, 10) || 60)}
          />
        </div>
        <div className="space-y-1.5">
          <Label htmlFor="ev-cap">Seats</Label>
          <Input
            id="ev-cap"
            type="number"
            min={1}
            max={500}
            value={capacity}
            onChange={(e) => setCapacity(parseInt(e.target.value, 10) || 30)}
          />
        </div>

        <div className="space-y-1.5 sm:col-span-2">
          <Label htmlFor="ev-repeat">Repeat weekly for</Label>
          <Input
            id="ev-repeat"
            type="number"
            min={1}
            max={26}
            value={repeatWeeks}
            onChange={(e) => setRepeatWeeks(parseInt(e.target.value, 10) || 1)}
          />
          <p className="text-xs text-muted-foreground">
            {repeatWeeks === 1
              ? "A single event."
              : `Publishes ${repeatWeeks} weekly repeats — the usual way to schedule the review.`}
          </p>
        </div>

        <div className="sm:col-span-2">
          <Button onClick={submit} disabled={pending || !date || !title.trim()}>
            {pending ? "Publishing…" : "Publish event"}
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}
