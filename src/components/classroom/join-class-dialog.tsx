"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { Loader2, LogIn } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { joinClass } from "@/server/actions/student/school-class";

/**
 * Joining a class, from anywhere: the trigger is whatever the caller wraps.
 * On success the student is taken straight into the class they just joined —
 * no second navigation to find it.
 */
export function JoinClassDialog({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [pending, start] = useTransition();
  const [code, setCode] = useState("");

  function submit() {
    start(async () => {
      const res = await joinClass(code);
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success(`Joined ${res.className}.`);
      setOpen(false);
      setCode("");
      router.push(`/classes/${res.classId}`);
      router.refresh();
    });
  }

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>{children}</DialogTrigger>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Join a class</DialogTitle>
          <DialogDescription>
            Enter the class code your teacher gave you. Your teacher sees your practice progress —
            never your password or anything outside your studying.
          </DialogDescription>
        </DialogHeader>
        <div className="flex gap-2">
          <Input
            value={code}
            onChange={(e) => setCode(e.target.value)}
            placeholder="e.g. K7M2XQ"
            className="font-mono uppercase tracking-widest"
            maxLength={12}
            autoFocus
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                e.preventDefault();
                submit();
              }
            }}
          />
          <Button onClick={submit} disabled={pending || code.trim().length < 4} className="gap-2">
            {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <LogIn className="h-4 w-4" />}
            Join
          </Button>
        </div>
      </DialogContent>
    </Dialog>
  );
}
