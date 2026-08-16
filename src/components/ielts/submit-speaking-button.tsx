"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Send } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { submitSpeaking } from "@/server/actions/student/ielts-speaking";

export function SubmitSpeakingButton({
  testId,
  recordedCount,
  totalPrompts,
}: {
  testId: string;
  recordedCount: number;
  totalPrompts: number;
}) {
  const router = useRouter();
  const [pending, start] = useTransition();

  function onClick() {
    // A partly-answered test is still worth reviewing, but the student should
    // know what they are sending rather than discovering it in the feedback.
    const message =
      recordedCount < totalPrompts
        ? `You have recorded ${recordedCount} of ${totalPrompts} answers. ` +
          `Send anyway? You cannot add more afterwards.`
        : "Send your Speaking test for free human review? You cannot re-record afterwards.";
    if (!window.confirm(message)) return;

    start(async () => {
      const res = await submitSpeaking(testId);
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success("Sent for review.");
      router.push("/ielts/feedback");
      router.refresh();
    });
  }

  return (
    <Button onClick={onClick} disabled={pending || recordedCount === 0}>
      {pending ? <Loader2 className="mr-1 h-4 w-4 animate-spin" /> : <Send className="mr-1 h-4 w-4" />}
      Submit for free human review
    </Button>
  );
}
