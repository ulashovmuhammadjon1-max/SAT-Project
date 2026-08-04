"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Pencil } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Slider } from "@/components/ui/slider";
import { Switch } from "@/components/ui/switch";
import { Textarea } from "@/components/ui/textarea";
import { deleteAdaptiveConfig, updateAdaptiveConfig } from "@/server/actions/admin/settings";

interface Existing {
  id: string;
  name: string;
  description: string | null;
  rwThresholdPct: number;
  mathThresholdPct: number;
  isActive: boolean;
}

function FormFields({
  name,
  setName,
  description,
  setDescription,
  rw,
  setRw,
  math,
  setMath,
  active,
  setActive,
}: {
  name: string;
  setName: (v: string) => void;
  description: string;
  setDescription: (v: string) => void;
  rw: number;
  setRw: (v: number) => void;
  math: number;
  setMath: (v: number) => void;
  active: boolean;
  setActive: (v: boolean) => void;
}) {
  return (
    <div className="space-y-4">
      <div className="space-y-1.5">
        <Label>Configuration name</Label>
        <Input value={name} onChange={(e) => setName(e.target.value)} placeholder="e.g. Standard adaptive routing" />
      </div>
      <div className="space-y-1.5">
        <Label>Description</Label>
        <Textarea value={description} onChange={(e) => setDescription(e.target.value)} rows={2} />
      </div>
      <div className="space-y-2">
        <div className="flex items-center justify-between">
          <Label>Reading &amp; Writing threshold</Label>
          <span className="text-sm font-semibold text-primary">{rw}%</span>
        </div>
        <Slider value={[rw]} min={40} max={95} step={5} onValueChange={([v]) => setRw(v)} />
      </div>
      <div className="space-y-2">
        <div className="flex items-center justify-between">
          <Label>Math threshold</Label>
          <span className="text-sm font-semibold text-primary">{math}%</span>
        </div>
        <Slider value={[math]} min={40} max={95} step={5} onValueChange={([v]) => setMath(v)} />
      </div>
      <div className="flex items-center justify-between rounded-lg border border-border px-3 py-2">
        <Label className="text-sm">Set as active configuration</Label>
        <Switch checked={active} onCheckedChange={setActive} />
      </div>
    </div>
  );
}

export function AdaptiveConfigForm({ existing }: { existing?: Existing }) {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [name, setName] = useState(existing?.name ?? "");
  const [description, setDescription] = useState(existing?.description ?? "");
  const [rw, setRw] = useState(existing?.rwThresholdPct ?? 70);
  const [math, setMath] = useState(existing?.mathThresholdPct ?? 70);
  const [active, setActive] = useState(existing?.isActive ?? false);
  const [isPending, startTransition] = useTransition();

  function save() {
    if (!name.trim()) {
      toast.error("Give the configuration a name.");
      return;
    }
    startTransition(async () => {
      await updateAdaptiveConfig({
        id: existing?.id,
        name,
        description,
        rwThresholdPct: rw,
        mathThresholdPct: math,
        isActive: active,
      });
      toast.success("Adaptive configuration saved.");
      setOpen(false);
      router.refresh();
    });
  }

  function remove() {
    if (!existing) return;
    startTransition(async () => {
      await deleteAdaptiveConfig(existing.id);
      setOpen(false);
      router.refresh();
    });
  }

  if (!existing) {
    return (
      <div className="space-y-4">
        <FormFields
          name={name}
          setName={setName}
          description={description}
          setDescription={setDescription}
          rw={rw}
          setRw={setRw}
          math={math}
          setMath={setMath}
          active={active}
          setActive={setActive}
        />
        <Button onClick={save} disabled={isPending}>
          {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
          Create configuration
        </Button>
      </div>
    );
  }

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button variant="outline" size="sm">
          <Pencil className="h-4 w-4" /> Edit
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Edit adaptive configuration</DialogTitle>
        </DialogHeader>
        <FormFields
          name={name}
          setName={setName}
          description={description}
          setDescription={setDescription}
          rw={rw}
          setRw={setRw}
          math={math}
          setMath={setMath}
          active={active}
          setActive={setActive}
        />
        <DialogFooter className="sm:justify-between">
          <Button variant="ghost" className="text-destructive" onClick={remove} disabled={isPending}>
            Delete
          </Button>
          <Button onClick={save} disabled={isPending}>
            {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
            Save
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
