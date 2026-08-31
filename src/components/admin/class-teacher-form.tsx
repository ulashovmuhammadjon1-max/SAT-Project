"use client";

import { useState, useTransition } from "react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { resendClassInvite, setClassTeacher } from "@/server/actions/admin/schools";

/**
 * Set or change a class's teacher, and resend their invite.
 *
 * Neither was possible before: a class created with the wrong teacher email —
 * or with none — could only be corrected by editing the database, and a
 * teacher who never received their invite had no way to be sent another.
 *
 * Saving a NEW address emails that teacher automatically. The status line says
 * so explicitly rather than leaving the admin to guess whether anything left
 * the building, because "did they get it?" is the exact question that started
 * this.
 */
export function ClassTeacherForm({
  classId,
  teacherName,
  teacherEmail,
}: {
  classId: string;
  teacherName: string;
  teacherEmail: string | null;
}) {
  const [open, setOpen] = useState(false);
  const [status, setStatus] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [pending, start] = useTransition();

  function save(formData: FormData) {
    setStatus(null);
    setError(null);
    start(async () => {
      const res = await setClassTeacher(classId, formData);
      if (res.error) setError(res.error);
      else {
        setStatus(res.note ?? "Saved.");
        setOpen(false);
      }
    });
  }

  function resend() {
    setStatus(null);
    setError(null);
    start(async () => {
      const res = await resendClassInvite(classId);
      if (res.error) setError(res.error);
      else setStatus(res.note ?? "Invite sent.");
    });
  }

  return (
    <div className="mt-4 border-t border-border pt-3">
      <div className="flex flex-wrap items-center gap-2">
        <Button type="button" variant="outline" size="sm" onClick={() => setOpen((v) => !v)}>
          {open ? "Cancel" : "Edit teacher"}
        </Button>
        {teacherEmail ? (
          <Button type="button" variant="ghost" size="sm" disabled={pending} onClick={resend}>
            {pending ? "Sending…" : "Resend invite"}
          </Button>
        ) : (
          <span className="text-xs text-muted-foreground">
            No teacher email on this class — nobody was invited.
          </span>
        )}
        {status && <span className="text-xs text-emerald-500">{status}</span>}
        {error && <span className="text-xs text-destructive">{error}</span>}
      </div>

      {open && (
        <form action={save} className="mt-3 grid gap-3 sm:grid-cols-[1fr_1fr_auto] sm:items-end">
          <div className="space-y-1.5">
            <Label htmlFor={`tn-${classId}`} className="text-xs">
              Teacher name
            </Label>
            <Input
              id={`tn-${classId}`}
              name="teacherName"
              defaultValue={teacherName}
              required
              minLength={2}
            />
          </div>
          <div className="space-y-1.5">
            <Label htmlFor={`te-${classId}`} className="text-xs">
              Teacher email
            </Label>
            <Input
              id={`te-${classId}`}
              name="teacherEmail"
              type="email"
              defaultValue={teacherEmail ?? ""}
              placeholder="teacher@school.uz"
            />
          </div>
          <Button type="submit" size="sm" disabled={pending}>
            {pending ? "Saving…" : "Save and invite"}
          </Button>
          <p className="text-xs text-muted-foreground sm:col-span-3">
            Changing the email emails the new teacher straight away and unlinks the previous
            account, so an old teacher does not keep access to the class.
          </p>
        </form>
      )}
    </div>
  );
}
