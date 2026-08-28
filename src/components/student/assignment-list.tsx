"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useTransition } from "react";
import { CheckCircle2, Circle, Loader2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import type { MyAssignment } from "@/server/actions/student/school-class";
import { markAssignmentDone } from "@/server/actions/teacher/assignments";

export function AssignmentList({ assignments }: { assignments: MyAssignment[] }) {
  const router = useRouter();
  const [pending, start] = useTransition();

  function done(id: string) {
    start(async () => {
      const res = await markAssignmentDone(id);
      if (res.error) toast.error(res.error);
      else {
        toast.success("Marked as done — your teacher sees it.");
        router.refresh();
      }
    });
  }

  return (
    <ul className="divide-y divide-border">
      {assignments.map((a) => (
        <li key={a.id} className="flex flex-wrap items-center gap-3 py-3">
          {a.done ? (
            <CheckCircle2 className="h-5 w-5 shrink-0 text-success" />
          ) : (
            <Circle className="h-5 w-5 shrink-0 text-muted-foreground" />
          )}
          <div className="min-w-[200px] flex-1">
            <p className={a.done ? "text-sm font-medium text-muted-foreground line-through" : "text-sm font-medium"}>
              {a.title}
            </p>
            <p className="text-xs text-muted-foreground">
              {a.className}
              {a.dueAt &&
                ` · due ${a.dueAt.toLocaleDateString(undefined, { month: "short", day: "numeric" })}`}
            </p>
            {a.instructions && !a.done && (
              <p className="mt-0.5 text-xs leading-relaxed text-muted-foreground">{a.instructions}</p>
            )}
          </div>
          {!a.done &&
            (a.testId ? (
              <Button size="sm" variant="outline" asChild>
                <Link href="/tests">Take {a.testTitle ?? "the test"}</Link>
              </Button>
            ) : (
              <Button size="sm" variant="outline" disabled={pending} onClick={() => done(a.id)}>
                {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : "Mark done"}
              </Button>
            ))}
        </li>
      ))}
    </ul>
  );
}
