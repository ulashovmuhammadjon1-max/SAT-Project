"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { Loader2, LogIn } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { joinClass } from "@/server/actions/student/school-class";

export function JoinClassForm() {
  const router = useRouter();
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
      setCode("");
      router.refresh();
    });
  }

  return (
    <div className="flex flex-wrap gap-2">
      <Input
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Class code, e.g. K7M2XQ"
        className="w-[220px] font-mono uppercase tracking-widest"
        maxLength={12}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            e.preventDefault();
            submit();
          }
        }}
      />
      <Button onClick={submit} disabled={pending || code.trim().length < 4} className="gap-2">
        {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <LogIn className="h-4 w-4" />}
        Join class
      </Button>
    </div>
  );
}
