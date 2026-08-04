"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Pencil, Save } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { updateModuleTimeLimit, updateTestDetails } from "@/server/actions/admin/tests";

interface ModuleRow {
  id: string;
  subject: string;
  order: number;
  difficulty: string;
  timeLimitMinutes: number;
}

interface AdaptiveConfigOption {
  id: string;
  name: string;
}

export function EditTestDialog({
  testId,
  title,
  description,
  adaptiveConfigId,
  modules,
  adaptiveConfigs,
}: {
  testId: string;
  title: string;
  description: string | null;
  adaptiveConfigId: string | null;
  modules: ModuleRow[];
  adaptiveConfigs: AdaptiveConfigOption[];
}) {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [titleValue, setTitleValue] = useState(title);
  const [descriptionValue, setDescriptionValue] = useState(description ?? "");
  const [configId, setConfigId] = useState(adaptiveConfigId ?? "none");
  const [timeLimits, setTimeLimits] = useState<Record<string, number>>(
    Object.fromEntries(modules.map((m) => [m.id, m.timeLimitMinutes]))
  );
  const [isSaving, startSave] = useTransition();

  function save() {
    startSave(async () => {
      await updateTestDetails(testId, {
        title: titleValue,
        description: descriptionValue || null,
        adaptiveConfigId: configId === "none" ? null : configId,
      });
      await Promise.all(
        modules
          .filter((m) => timeLimits[m.id] !== m.timeLimitMinutes)
          .map((m) => updateModuleTimeLimit(m.id, timeLimits[m.id]))
      );
      toast.success("Test updated.");
      setOpen(false);
      router.refresh();
    });
  }

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button variant="outline">
          <Pencil className="h-4 w-4" /> Edit
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-lg">
        <DialogHeader>
          <DialogTitle>Edit test</DialogTitle>
          <DialogDescription>Title, description, adaptive routing config, and per-module time limits.</DialogDescription>
        </DialogHeader>

        <div className="space-y-4">
          <div className="space-y-1.5">
            <Label>Title</Label>
            <Input value={titleValue} onChange={(e) => setTitleValue(e.target.value)} />
          </div>
          <div className="space-y-1.5">
            <Label>Description</Label>
            <Textarea value={descriptionValue} onChange={(e) => setDescriptionValue(e.target.value)} rows={3} />
          </div>
          <div className="space-y-1.5">
            <Label>Adaptive routing config</Label>
            <Select value={configId} onValueChange={setConfigId}>
              <SelectTrigger>
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="none">None (use module-level thresholds only)</SelectItem>
                {adaptiveConfigs.map((c) => (
                  <SelectItem key={c.id} value={c.id}>
                    {c.name}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
          {modules.length > 0 && (
            <div className="space-y-2">
              <Label>Module time limits (minutes)</Label>
              {modules.map((m) => (
                <div key={m.id} className="flex items-center justify-between gap-3 text-sm">
                  <span className="text-muted-foreground">
                    {m.subject.replace("_", " ")} · Module {m.order} ({m.difficulty})
                  </span>
                  <Input
                    type="number"
                    min={1}
                    className="w-24"
                    value={timeLimits[m.id]}
                    onChange={(e) => setTimeLimits((prev) => ({ ...prev, [m.id]: Number(e.target.value) }))}
                  />
                </div>
              ))}
            </div>
          )}
        </div>

        <DialogFooter>
          <Button onClick={save} disabled={isSaving}>
            {isSaving ? <Loader2 className="h-4 w-4 animate-spin" /> : <Save className="h-4 w-4" />}
            Save changes
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
