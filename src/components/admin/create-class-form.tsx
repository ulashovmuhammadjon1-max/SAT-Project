"use client";

import { useRouter } from "next/navigation";
import { useRef, useState, useTransition } from "react";
import { Loader2, Plus } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { createClass } from "@/server/actions/admin/schools";

export function CreateClassForm() {
  const router = useRouter();
  const formRef = useRef<HTMLFormElement>(null);
  const [pending, start] = useTransition();
  const [lastCode, setLastCode] = useState<string | null>(null);

  function submit(formData: FormData) {
    start(async () => {
      const res = await createClass(formData);
      if (res.error) {
        toast.error(res.error);
        return;
      }
      setLastCode(res.code ?? null);
      toast.success(`Class created — code ${res.code}`);
      formRef.current?.reset();
      router.refresh();
    });
  }

  return (
    <form ref={formRef} action={submit} className="space-y-4">
      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <Label htmlFor="name">Class name</Label>
          <Input id="name" name="name" placeholder="Grade 11 SAT — morning group" required />
        </div>
        <div className="space-y-1.5">
          <Label htmlFor="school">School</Label>
          <Input id="school" name="school" placeholder="School #42, Tashkent" required />
        </div>
        <div className="space-y-1.5">
          <Label htmlFor="teacherName">Teacher</Label>
          <Input id="teacherName" name="teacherName" placeholder="Teacher's full name" required />
        </div>
        <div className="space-y-1.5">
          <Label htmlFor="teacherEmail">Teacher email (optional)</Label>
          <Input id="teacherEmail" name="teacherEmail" type="email" placeholder="teacher@school.uz" />
        </div>
      </div>
      <div className="flex items-center gap-3">
        <Button type="submit" disabled={pending} className="gap-2">
          {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Plus className="h-4 w-4" />}
          Create class
        </Button>
        {lastCode && (
          <p className="text-sm text-muted-foreground">
            Give the teacher this code:{" "}
            <span className="rounded bg-secondary px-2 py-1 font-mono font-semibold tracking-widest text-foreground">
              {lastCode}
            </span>
          </p>
        )}
      </div>
    </form>
  );
}
