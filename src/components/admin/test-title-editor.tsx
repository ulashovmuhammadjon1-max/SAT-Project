"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Check, Loader2, Pencil, X } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { updateTestDetails } from "@/server/actions/admin/tests";

export function TestTitleEditor({ testId, title }: { testId: string; title: string }) {
  const router = useRouter();
  const [editing, setEditing] = useState(false);
  const [value, setValue] = useState(title);
  const [isPending, startTransition] = useTransition();

  if (!editing) {
    return (
      <button
        type="button"
        onClick={() => setEditing(true)}
        className="group flex items-center gap-2 text-left"
      >
        <h1 className="font-display text-2xl font-semibold tracking-tight">{title}</h1>
        <Pencil className="h-4 w-4 text-muted-foreground opacity-0 transition-opacity group-hover:opacity-100" />
      </button>
    );
  }

  function save() {
    startTransition(async () => {
      await updateTestDetails(testId, { title: value });
      setEditing(false);
      router.refresh();
    });
  }

  return (
    <div className="flex items-center gap-2">
      <Input
        value={value}
        onChange={(e) => setValue(e.target.value)}
        className="h-9 max-w-md text-lg font-semibold"
        autoFocus
      />
      <Button size="icon" variant="ghost" onClick={save} disabled={isPending}>
        {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Check className="h-4 w-4" />}
      </Button>
      <Button
        size="icon"
        variant="ghost"
        onClick={() => {
          setValue(title);
          setEditing(false);
        }}
      >
        <X className="h-4 w-4" />
      </Button>
    </div>
  );
}
