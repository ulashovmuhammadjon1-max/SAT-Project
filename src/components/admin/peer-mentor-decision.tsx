"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { Check, Loader2, X } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { decidePeerMentor } from "@/server/actions/admin/peer-mentors";

export function PeerMentorDecision({ applicationId }: { applicationId: string }) {
  const router = useRouter();
  const [pending, start] = useTransition();
  const [note, setNote] = useState("");

  function decide(decision: "APPROVED" | "REJECTED") {
    start(async () => {
      const res = await decidePeerMentor({ applicationId, decision, note });
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success(decision === "APPROVED" ? "Approved — they can host sessions now." : "Rejected — the student has been emailed.");
      router.refresh();
    });
  }

  return (
    <div className="space-y-2">
      <Textarea
        value={note}
        onChange={(e) => setNote(e.target.value)}
        rows={2}
        placeholder="Note to the applicant (goes into the email) — optional"
        className="text-sm"
      />
      <div className="flex gap-2">
        <Button size="sm" disabled={pending} onClick={() => decide("APPROVED")} className="gap-1.5">
          {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Check className="h-4 w-4" />}
          Approve as mentor
        </Button>
        <Button
          size="sm"
          variant="outline"
          disabled={pending}
          onClick={() => decide("REJECTED")}
          className="gap-1.5 text-destructive hover:text-destructive"
        >
          <X className="h-4 w-4" /> Reject
        </Button>
      </div>
    </div>
  );
}
