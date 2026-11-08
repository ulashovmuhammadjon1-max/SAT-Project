"use client";

import { useState, useTransition } from "react";
import { Bell, Loader2, Lock, Palette, Settings, UserRound, X } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";
import { Textarea } from "@/components/ui/textarea";
import { AppearancePicker } from "@/components/shared/appearance-menu";
import { BrowserAlertsPrompt } from "@/components/notifications/browser-alerts";
import { unblockUser, updateCommunitySettings, updateMyProfile, type CommunitySettings } from "@/server/actions/student/community";

import { MemberAvatar } from "./bits";
import { PageHeader } from "./community-shell";

export function SettingsView({
  initial,
  blocked: initialBlocked,
}: {
  initial: CommunitySettings;
  blocked: { id: string; name: string; image: string | null }[];
}) {
  const [s, setS] = useState(initial);
  const [blocked, setBlocked] = useState(initialBlocked);
  const [savingProfile, startProfile] = useTransition();

  function setPref<K extends keyof CommunitySettings>(key: K, value: CommunitySettings[K]) {
    const next = { ...s, [key]: value };
    setS(next);
    void updateCommunitySettings(next).then((r) => (r.ok ? toast.success("Saved.") : toast.error(r.error)));
  }

  return (
    <div className="flex min-h-0 min-w-0 flex-1 flex-col">
      <PageHeader title="Profile & notifications" subtitle="How you appear and what reaches you" icon={Settings} />
      <div className="min-h-0 flex-1 overflow-y-auto">
        <div className="mx-auto max-w-3xl space-y-6 px-4 py-6 sm:px-6">
          <Card icon={UserRound} title="Your community profile" desc="Shown when someone opens your name. Your email is never shown.">
            <label className="block text-sm font-medium">
              Short bio
              <Textarea value={s.bio} onChange={(e) => setS({ ...s, bio: e.target.value })} maxLength={280} className="mt-1.5 min-h-20" placeholder="e.g. Grade 11, aiming for 1500 and a CS degree. Happy to help with algebra." />
              <span className="mt-1 block text-right text-xs text-muted-foreground">{s.bio.length}/280</span>
            </label>
            <TagInput label="I can help with" value={s.helpsWith} onChange={(v) => setS({ ...s, helpsWith: v })} placeholder="SAT Math, IELTS Speaking…" />
            <TagInput label="Currently studying" value={s.studying} onChange={(v) => setS({ ...s, studying: v })} placeholder="AP Biology, Calculus…" />
            <TagInput label="Interests" value={s.interests} onChange={(v) => setS({ ...s, interests: v })} placeholder="Economics, robotics, debate…" />
            <Button
              disabled={savingProfile}
              onClick={() =>
                startProfile(async () => {
                  const r = await updateMyProfile({ bio: s.bio, interests: s.interests, helpsWith: s.helpsWith, studying: s.studying });
                  if (r.ok) toast.success("Profile saved.");
                  else toast.error(r.error);
                })
              }
            >
              {savingProfile && <Loader2 className="h-4 w-4 animate-spin" />} Save profile
            </Button>
          </Card>

          <Card icon={Bell} title="Email notifications" desc={s.hasEmail ? "Sent only when you are not using Scholarly at the time, and at most one email every 15 minutes." : "Your account has no email address, so no emails can be sent. In-app notifications still work."}>
            <Toggle label="Replies to my messages and posts" hint="Someone replies to you, or answers your question" checked={s.emailReplies} onChange={(v) => setPref("emailReplies", v)} disabled={!s.hasEmail} />
            <Toggle label="Mentions" hint="Someone writes @your-name" checked={s.emailMentions} onChange={(v) => setPref("emailMentions", v)} disabled={!s.hasEmail} />
            <Toggle label="Private messages" hint="A new message in a conversation" checked={s.emailDirect} onChange={(v) => setPref("emailDirect", v)} disabled={!s.hasEmail} />
            <Toggle label="Other activity" hint="Replies in discussions you follow, accepted answers, reactions" checked={s.emailActivity} onChange={(v) => setPref("emailActivity", v)} disabled={!s.hasEmail} />
            <Toggle label="Announcements" hint="Posts from the Scholarly team" checked={s.emailAnnouncements} onChange={(v) => setPref("emailAnnouncements", v)} disabled={!s.hasEmail} />
            <Toggle label="Daily digest instead" hint="One summary email a day (around 21:00 Tashkent) instead of emails as things happen" checked={s.emailDigest} onChange={(v) => setPref("emailDigest", v)} disabled={!s.hasEmail} />
            <div className="border-t border-border pt-4">
              <BrowserAlertsPrompt />
            </div>
          </Card>

          <Card icon={Lock} title="Privacy & safety" desc="Control who can reach you.">
            <div className="flex items-start justify-between gap-4">
              <div>
                <p className="text-sm font-medium">Who can send me private messages</p>
                <p className="text-xs text-muted-foreground">Moderators can always reach you about your account.</p>
              </div>
              <select value={s.dmPolicy} onChange={(e) => setPref("dmPolicy", e.target.value as "EVERYONE" | "NOBODY")} className="rounded-lg border border-input bg-background px-2.5 py-1.5 text-sm">
                <option value="EVERYONE">Any student</option>
                <option value="NOBODY">Nobody</option>
              </select>
            </div>
            <Toggle label="Show when I'm active" hint="Appear in “Active now” and as online on your profile" checked={s.showPresence} onChange={(v) => setPref("showPresence", v)} />
            <div className="border-t border-border pt-4">
              <p className="text-sm font-medium">Blocked students</p>
              {blocked.length === 0 ? (
                <p className="mt-1 text-xs text-muted-foreground">You have not blocked anyone. Block someone from their profile card.</p>
              ) : (
                <ul className="mt-2 space-y-2">
                  {blocked.map((b) => (
                    <li key={b.id} className="flex items-center gap-3">
                      <MemberAvatar id={b.id} name={b.name} image={b.image} size={30} />
                      <span className="flex-1 text-sm">{b.name}</span>
                      <Button
                        size="sm"
                        variant="outline"
                        onClick={async () => {
                          const r = await unblockUser(b.id);
                          if (r.ok) setBlocked((xs) => xs.filter((x) => x.id !== b.id));
                        }}
                      >
                        Unblock
                      </Button>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </Card>

          <Card icon={Palette} title="Appearance" desc="Applies across Scholarly on this device.">
            <AppearancePicker className="sm:grid-cols-3" />
          </Card>
        </div>
      </div>
    </div>
  );
}

function Card({ icon: Icon, title, desc, children }: { icon: typeof Bell; title: string; desc: string; children: React.ReactNode }) {
  return (
    <section className="rounded-2xl border border-border bg-card p-5 shadow-sm">
      <div className="mb-4 flex items-start gap-3">
        <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-primary/10 text-primary">
          <Icon className="h-[18px] w-[18px]" />
        </span>
        <div>
          <h2 className="font-display text-base font-semibold">{title}</h2>
          <p className="text-sm text-muted-foreground">{desc}</p>
        </div>
      </div>
      <div className="space-y-4">{children}</div>
    </section>
  );
}

function Toggle({ label, hint, checked, onChange, disabled }: { label: string; hint: string; checked: boolean; onChange: (v: boolean) => void; disabled?: boolean }) {
  return (
    <div className="flex items-start justify-between gap-4">
      <div>
        <p className="text-sm font-medium">{label}</p>
        <p className="text-xs text-muted-foreground">{hint}</p>
      </div>
      <Switch checked={checked} onCheckedChange={onChange} disabled={disabled} aria-label={label} />
    </div>
  );
}

function TagInput({ label, value, onChange, placeholder }: { label: string; value: string[]; onChange: (v: string[]) => void; placeholder: string }) {
  const [draft, setDraft] = useState("");
  const add = () => {
    const t = draft.trim().replace(/,$/, "").slice(0, 40);
    if (t && !value.includes(t) && value.length < 8) onChange([...value, t]);
    setDraft("");
  };
  return (
    <div>
      <p className="text-sm font-medium">{label}</p>
      <div className="mt-1.5 flex flex-wrap items-center gap-1.5 rounded-lg border border-input bg-background px-2 py-1.5 focus-within:ring-2 focus-within:ring-ring">
        {value.map((t) => (
          <span key={t} className="inline-flex items-center gap-1 rounded-full bg-secondary px-2.5 py-0.5 text-xs font-medium">
            {t}
            <button type="button" onClick={() => onChange(value.filter((x) => x !== t))} aria-label={`Remove ${t}`} className="rounded-full hover:text-destructive">
              <X className="h-3 w-3" />
            </button>
          </span>
        ))}
        <input
          value={draft}
          onChange={(e) => setDraft(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" || e.key === ",") {
              e.preventDefault();
              add();
            }
            if (e.key === "Backspace" && !draft && value.length) onChange(value.slice(0, -1));
          }}
          onBlur={add}
          placeholder={value.length ? "" : placeholder}
          className="min-w-[8rem] flex-1 bg-transparent py-0.5 text-sm focus:outline-none"
        />
      </div>
      <p className="mt-1 text-xs text-muted-foreground">Press Enter after each one. Up to 8.</p>
    </div>
  );
}
