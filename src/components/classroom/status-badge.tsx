import {
  AlertTriangle,
  CheckCircle2,
  Circle,
  CircleDashed,
  FileClock,
} from "lucide-react";

import type { SubmissionStatus } from "@/lib/classroom/status";
import { cn } from "@/lib/utils";

/**
 * One badge per submission status, used identically on student and teacher
 * screens. Icon + text on every state — colour alone never carries meaning.
 */

const META: Record<
  SubmissionStatus,
  { label: string; icon: typeof Circle; className: string }
> = {
  NOT_STARTED: {
    label: "Not started",
    icon: Circle,
    className: "bg-secondary text-muted-foreground",
  },
  IN_PROGRESS: {
    label: "In progress",
    icon: CircleDashed,
    className: "bg-primary/10 text-primary",
  },
  DRAFT: {
    label: "Draft saved",
    icon: FileClock,
    className: "bg-warning/15 text-warning-foreground",
  },
  SUBMITTED: {
    label: "Submitted",
    icon: CheckCircle2,
    className: "bg-success/10 text-success",
  },
  LATE: {
    label: "Submitted late",
    icon: CheckCircle2,
    className: "bg-success/10 text-success",
  },
  MISSING: {
    label: "Missing",
    icon: AlertTriangle,
    className: "bg-destructive/10 text-destructive",
  },
};

export function StatusBadge({
  status,
  className,
}: {
  status: SubmissionStatus;
  className?: string;
}) {
  const meta = META[status];
  const Icon = meta.icon;
  return (
    <span
      className={cn(
        "inline-flex shrink-0 items-center gap-1.5 rounded-full px-2.5 py-1 text-xs font-medium",
        meta.className,
        className,
      )}
    >
      <Icon className="h-3.5 w-3.5" />
      {meta.label}
    </span>
  );
}
