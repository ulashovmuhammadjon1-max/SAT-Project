"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { updatePlatformSettings } from "@/server/actions/admin/economy";
import type { PlatformSettings } from "@/lib/settings";

/**
 * The economy knobs.
 *
 * Every value is re-validated server-side; this form's job is to make the
 * consequences legible before saving, which is why the price ladder is
 * previewed live from the two numbers that generate it.
 */
export function EconomySettingsForm({
  current,
  defaults,
}: {
  current: PlatformSettings;
  defaults: PlatformSettings;
}) {
  const router = useRouter();
  const [pending, startTransition] = useTransition();
  const [form, setForm] = useState<PlatformSettings>(current);

  function set<K extends keyof PlatformSettings>(key: K, value: PlatformSettings[K]) {
    setForm((f) => ({ ...f, [key]: value }));
  }

  const ladder = Array.from(
    { length: 5 },
    (_, i) => form.bookingBaseCost + i * form.bookingCostIncrement,
  );

  function save() {
    startTransition(async () => {
      const res = await updatePlatformSettings(form);
      if (res.ok) {
        toast.success("Settings saved");
        router.refresh();
      } else {
        toast.error(res.error);
      }
    });
  }

  return (
    <div className="space-y-6">
      <Card>
        <CardHeader>
          <CardTitle className="text-base">Coins</CardTitle>
        </CardHeader>
        <CardContent className="grid gap-4 sm:grid-cols-2">
          <NumberField
            id="signupBonusCoins"
            label="Welcome bonus"
            hint={`New accounts start with this. Default ${defaults.signupBonusCoins}.`}
            value={form.signupBonusCoins}
            onChange={(v) => set("signupBonusCoins", v)}
          />
          <NumberField
            id="referralRewardCoins"
            label="Referral reward"
            hint={`Paid when an invite creates an account. Default ${defaults.referralRewardCoins}.`}
            value={form.referralRewardCoins}
            onChange={(v) => set("referralRewardCoins", v)}
          />
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Booking price ladder</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid gap-4 sm:grid-cols-2">
            <NumberField
              id="bookingBaseCost"
              label="First booking costs"
              hint={`Default ${defaults.bookingBaseCost}.`}
              value={form.bookingBaseCost}
              onChange={(v) => set("bookingBaseCost", v)}
            />
            <NumberField
              id="bookingCostIncrement"
              label="Increase per booking"
              hint={`Default ${defaults.bookingCostIncrement}.`}
              value={form.bookingCostIncrement}
              onChange={(v) => set("bookingCostIncrement", v)}
            />
          </div>

          <div className="rounded-lg border border-border bg-secondary/40 p-3">
            <p className="text-xs font-medium text-muted-foreground">
              Resulting price for a student&apos;s 1st to 5th booking
            </p>
            <p className="mt-1 font-mono text-sm tabular-nums">{ladder.join(" → ")} → …</p>
            {form.signupBonusCoins >= form.bookingBaseCost ? (
              <p className="mt-1 text-xs text-success">
                The welcome bonus covers a first booking, so it is effectively free.
              </p>
            ) : (
              <p className="mt-1 text-xs text-warning">
                The welcome bonus ({form.signupBonusCoins}) does not cover a first booking (
                {form.bookingBaseCost}), so new students cannot book immediately.
              </p>
            )}
          </div>

          <NumberField
            id="bookingRefundHours"
            label="Refund window (hours before start)"
            hint="Cancel earlier than this and coins are returned. Leave empty to never refund."
            value={form.bookingRefundHours}
            nullable
            onChange={(v) => set("bookingRefundHours", v)}
          />
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Community requirements</CardTitle>
        </CardHeader>
        <CardContent className="grid gap-4 sm:grid-cols-2">
          <TextField
            id="instagramHandle"
            label="Instagram handle"
            prefix="@"
            value={form.instagramHandle}
            onChange={(v) => set("instagramHandle", v)}
          />
          <TextField
            id="telegramHandle"
            label="Telegram handle"
            prefix="@"
            value={form.telegramHandle}
            onChange={(v) => set("telegramHandle", v)}
          />
          <p className="text-xs text-muted-foreground sm:col-span-2">
            Students confirm these themselves. Neither platform lets a third-party site verify that
            a specific person follows an account, so this is an attestation and is presented that
            way. Telegram could be verified later via Telegram Login.
          </p>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Meeting provider</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <Label htmlFor="meetingProvider">Provider</Label>
          <select
            id="meetingProvider"
            value={form.meetingProvider}
            onChange={(e) => set("meetingProvider", e.target.value)}
            className="w-full rounded-lg border border-input bg-background px-3 py-2 text-sm"
          >
            <option value="manual">Manual — you send the link yourself</option>
            <option value="static">Static link — one room for every session</option>
            <option value="google_meet">Google Meet — needs credentials</option>
          </select>
          <p className="text-xs text-muted-foreground">
            &ldquo;Static&rdquo; needs <code>MEETING_STATIC_URL</code>. Google Meet needs a service
            account and is not implemented yet — selecting it falls back to manual rather than
            failing a booking.
          </p>
        </CardContent>
      </Card>

      <div className="flex justify-end gap-2">
        <Button variant="outline" onClick={() => setForm(defaults)} disabled={pending}>
          Reset to defaults
        </Button>
        <Button onClick={save} disabled={pending}>
          {pending ? "Saving…" : "Save settings"}
        </Button>
      </div>
    </div>
  );
}

function NumberField({
  id,
  label,
  hint,
  value,
  onChange,
  nullable,
}: {
  id: string;
  label: string;
  hint?: string;
  value: number | null;
  onChange: (v: never) => void;
  nullable?: boolean;
}) {
  return (
    <div className="space-y-1.5">
      <Label htmlFor={id}>{label}</Label>
      <Input
        id={id}
        type="number"
        min={0}
        value={value ?? ""}
        onChange={(e) => {
          const raw = e.target.value;
          if (raw === "" && nullable) return onChange(null as never);
          const n = parseInt(raw, 10);
          onChange((Number.isFinite(n) ? n : 0) as never);
        }}
      />
      {hint && <p className="text-xs text-muted-foreground">{hint}</p>}
    </div>
  );
}

function TextField({
  id,
  label,
  prefix,
  value,
  onChange,
}: {
  id: string;
  label: string;
  prefix?: string;
  value: string;
  onChange: (v: never) => void;
}) {
  return (
    <div className="space-y-1.5">
      <Label htmlFor={id}>{label}</Label>
      <div className="flex items-center gap-1">
        {prefix && <span className="text-sm text-muted-foreground">{prefix}</span>}
        <Input id={id} value={value} onChange={(e) => onChange(e.target.value as never)} />
      </div>
    </div>
  );
}
