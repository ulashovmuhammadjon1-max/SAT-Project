"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";
import { Check, ChevronDown, Plus, School } from "lucide-react";

import { JoinClassDialog } from "@/components/classroom/join-class-dialog";
import { cn } from "@/lib/utils";

export interface SwitcherClass {
  id: string;
  name: string;
  teacherName: string;
}

/**
 * The class selector at the top of the School sidebar. It answers the one
 * question a classroom UI must never leave open — "which class am I in?" —
 * and switches in a single click. Joining a new class lives here too, so a
 * student is never sent hunting through settings for a code box.
 */
export function ClassSwitcher({ classes }: { classes: SwitcherClass[] }) {
  const pathname = usePathname();
  const [open, setOpen] = useState(false);

  const currentId = pathname.match(/^\/classes\/([^/]+)/)?.[1] ?? null;
  const current = classes.find((c) => c.id === currentId) ?? null;

  const initials = (name: string) =>
    name
      .split(/\s+/)
      .map((w) => w[0])
      .join("")
      .slice(0, 2)
      .toUpperCase();

  return (
    <div className="border-b border-border p-3">
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        aria-expanded={open}
        className="flex w-full items-center gap-2.5 rounded-xl border border-border bg-secondary/50 px-3 py-2 text-left text-sm font-semibold transition-colors hover:bg-secondary"
      >
        <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-md bg-success/15 text-[10px] font-bold text-success">
          {current ? initials(current.name) : <School className="h-3.5 w-3.5" />}
        </span>
        <span className="min-w-0 flex-1 truncate">{current ? current.name : "Your classes"}</span>
        <ChevronDown
          className={cn(
            "h-4 w-4 shrink-0 text-muted-foreground transition-transform duration-200",
            open && "rotate-180",
          )}
        />
      </button>

      {open && (
        <div className="mt-1.5 space-y-0.5 rounded-xl border border-border bg-card p-1.5 shadow-soft">
          {classes.map((c) => {
            const active = c.id === currentId;
            return (
              <Link
                key={c.id}
                href={`/classes/${c.id}`}
                onClick={() => setOpen(false)}
                className={cn(
                  "flex items-center gap-2.5 rounded-lg px-2.5 py-2 text-sm font-medium transition-colors",
                  active
                    ? "bg-secondary text-foreground"
                    : "text-muted-foreground hover:bg-secondary hover:text-foreground",
                )}
              >
                <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-md bg-success/15 text-[10px] font-bold text-success">
                  {initials(c.name)}
                </span>
                <span className="min-w-0 flex-1">
                  <span className="block truncate">{c.name}</span>
                  <span className="block truncate text-[11px] font-normal text-muted-foreground">
                    {c.teacherName}
                  </span>
                </span>
                {active && <Check className="h-4 w-4 shrink-0 text-primary" />}
              </Link>
            );
          })}
          {classes.length > 0 && <div className="mx-2 my-1 border-t border-border" />}
          <JoinClassDialog>
            <button
              type="button"
              className="flex w-full items-center gap-2.5 rounded-lg px-2.5 py-2 text-sm font-medium text-primary transition-colors hover:bg-secondary"
            >
              <span className="flex h-6 w-6 items-center justify-center rounded-md bg-primary/10">
                <Plus className="h-3.5 w-3.5" />
              </span>
              Join a class
            </button>
          </JoinClassDialog>
        </div>
      )}
    </div>
  );
}
