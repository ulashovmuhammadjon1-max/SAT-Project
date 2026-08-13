"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { ArrowDown, ArrowUp, ExternalLink, Loader2, Pencil, Plus, Trash2 } from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { ImageUploadField } from "@/components/admin/image-upload-field";
import {
  deletePartner,
  movePartner,
  savePartner,
  setPartnerPublished,
} from "@/server/actions/admin/partners";

export interface PartnerRow {
  id: string;
  name: string;
  logoUrl: string;
  href: string;
  blurb: string | null;
  order: number;
  isPublished: boolean;
}

export function PartnersAdmin({ partners }: { partners: PartnerRow[] }) {
  const router = useRouter();
  const [editing, setEditing] = useState<PartnerRow | "new" | null>(null);
  const [busy, setBusy] = useState<string | null>(null);
  const [, startTransition] = useTransition();

  function run(id: string, fn: () => Promise<{ ok: boolean; error?: string }>, okMsg: string) {
    setBusy(id);
    startTransition(async () => {
      const res = await fn();
      setBusy(null);
      if (res.ok) {
        toast.success(okMsg);
        router.refresh();
      } else {
        toast.error(res.error ?? "Something went wrong.");
      }
    });
  }

  return (
    <div className="space-y-4">
      <div className="flex justify-end">
        <Button onClick={() => setEditing("new")}>
          <Plus className="h-4 w-4" /> Add partner
        </Button>
      </div>

      {editing && (
        <PartnerForm
          partner={editing === "new" ? null : editing}
          onClose={() => setEditing(null)}
          onSaved={() => {
            setEditing(null);
            router.refresh();
          }}
        />
      )}

      {partners.length === 0 && !editing && (
        <Card>
          <CardContent className="p-8 text-center text-sm text-muted-foreground">
            No partners yet. Added partners appear on the landing page once published.
          </CardContent>
        </Card>
      )}

      <ul className="space-y-2">
        {partners.map((p, i) => (
          <li key={p.id}>
            <Card>
              <CardContent className="flex flex-wrap items-center gap-4 p-4">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={p.logoUrl}
                  alt=""
                  aria-hidden
                  className="h-12 w-12 shrink-0 rounded-full object-cover ring-1 ring-border"
                />
                <div className="min-w-0 flex-1">
                  <p className="flex items-center gap-2 font-medium">
                    {p.name}
                    {p.isPublished ? (
                      <Badge variant="success">Live</Badge>
                    ) : (
                      <Badge variant="secondary">Hidden</Badge>
                    )}
                  </p>
                  {p.blurb && <p className="text-xs text-muted-foreground">{p.blurb}</p>}
                  <a
                    href={p.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="mt-0.5 inline-flex items-center gap-1 text-xs text-primary hover:underline"
                  >
                    {p.href} <ExternalLink className="h-3 w-3" />
                  </a>
                </div>

                <div className="flex flex-wrap gap-1">
                  <Button
                    size="sm"
                    variant="ghost"
                    disabled={busy === p.id || i === 0}
                    onClick={() => run(p.id, () => movePartner(p.id, "up"), "Moved up.")}
                  >
                    <ArrowUp className="h-3.5 w-3.5" />
                  </Button>
                  <Button
                    size="sm"
                    variant="ghost"
                    disabled={busy === p.id || i === partners.length - 1}
                    onClick={() => run(p.id, () => movePartner(p.id, "down"), "Moved down.")}
                  >
                    <ArrowDown className="h-3.5 w-3.5" />
                  </Button>
                  <Button size="sm" variant="outline" onClick={() => setEditing(p)}>
                    <Pencil className="h-3.5 w-3.5" /> Edit
                  </Button>
                  <Button
                    size="sm"
                    variant="outline"
                    disabled={busy === p.id}
                    onClick={() =>
                      run(
                        p.id,
                        () => setPartnerPublished(p.id, !p.isPublished),
                        p.isPublished ? "Hidden from the site." : "Now live on the landing page.",
                      )
                    }
                  >
                    {p.isPublished ? "Hide" : "Publish"}
                  </Button>
                  <Button
                    size="sm"
                    variant="ghost"
                    className="text-destructive hover:text-destructive"
                    disabled={busy === p.id}
                    onClick={() => run(p.id, () => deletePartner(p.id), "Partner removed.")}
                  >
                    <Trash2 className="h-3.5 w-3.5" />
                  </Button>
                </div>
              </CardContent>
            </Card>
          </li>
        ))}
      </ul>
    </div>
  );
}

function PartnerForm({
  partner,
  onClose,
  onSaved,
}: {
  partner: PartnerRow | null;
  onClose: () => void;
  onSaved: () => void;
}) {
  const [name, setName] = useState(partner?.name ?? "");
  const [href, setHref] = useState(partner?.href ?? "");
  const [blurb, setBlurb] = useState(partner?.blurb ?? "");
  const [logoUrl, setLogoUrl] = useState<string | null>(partner?.logoUrl ?? null);
  const [isPending, startTransition] = useTransition();

  function submit(e: React.FormEvent) {
    e.preventDefault();
    startTransition(async () => {
      const res = await savePartner({
        id: partner?.id,
        name,
        href,
        blurb,
        logoUrl: logoUrl ?? "",
        order: partner?.order ?? 0,
        isPublished: partner?.isPublished ?? false,
      });
      if (res.ok) {
        toast.success(partner ? "Partner updated." : "Partner added. Press Publish to show it.");
        onSaved();
      } else {
        toast.error(res.error ?? "Couldn't save.");
      }
    });
  }

  return (
    <Card className="border-primary/40">
      <CardContent className="p-5">
        <form onSubmit={submit} className="space-y-4">
          <div className="grid gap-4 sm:grid-cols-2">
            <div className="space-y-1.5">
              <Label htmlFor="p-name">Name</Label>
              <Input id="p-name" value={name} onChange={(e) => setName(e.target.value)} placeholder="PrimeSAT" />
            </div>
            <div className="space-y-1.5">
              <Label htmlFor="p-href">Link</Label>
              <Input
                id="p-href"
                value={href}
                onChange={(e) => setHref(e.target.value)}
                placeholder="t.me/SAT_1601"
              />
              <p className="text-xs text-muted-foreground">
                Clicking the logo opens this. https:// is added if you leave it off.
              </p>
            </div>
          </div>

          <div className="space-y-1.5">
            <Label htmlFor="p-blurb">One line (optional)</Label>
            <Input
              id="p-blurb"
              value={blurb}
              onChange={(e) => setBlurb(e.target.value)}
              placeholder="SAT tips and practice on Telegram"
            />
          </div>

          <div className="space-y-1.5">
            <Label>Logo</Label>
            <ImageUploadField imageUrl={logoUrl} onChange={setLogoUrl} label="Upload logo" />
            <p className="text-xs text-muted-foreground">
              Square works best — it is shown in a circle at 64px.
            </p>
          </div>

          <div className="flex justify-end gap-2">
            <Button type="button" variant="ghost" onClick={onClose} disabled={isPending}>
              Cancel
            </Button>
            <Button type="submit" disabled={isPending}>
              {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
              {partner ? "Save changes" : "Add partner"}
            </Button>
          </div>
        </form>
      </CardContent>
    </Card>
  );
}
