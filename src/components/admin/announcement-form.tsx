"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { createAnnouncement } from "@/server/actions/admin/settings";

export function AnnouncementForm() {
  const router = useRouter();
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [audience, setAudience] = useState<"ALL" | "STUDENT" | "ADMIN">("ALL");
  const [isPending, startTransition] = useTransition();

  function submit() {
    if (!title.trim() || !body.trim()) {
      toast.error("Title and message are required.");
      return;
    }
    startTransition(async () => {
      await createAnnouncement({ title, body, audience });
      setTitle("");
      setBody("");
      toast.success("Announcement published.");
      router.refresh();
    });
  }

  return (
    <div className="space-y-4">
      <div className="grid gap-4 sm:grid-cols-[1fr_180px]">
        <div className="space-y-1.5">
          <Label>Title</Label>
          <Input value={title} onChange={(e) => setTitle(e.target.value)} />
        </div>
        <div className="space-y-1.5">
          <Label>Audience</Label>
          <Select value={audience} onValueChange={(v) => setAudience(v as typeof audience)}>
            <SelectTrigger>
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="ALL">Everyone</SelectItem>
              <SelectItem value="STUDENT">Students</SelectItem>
              <SelectItem value="ADMIN">Admins</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>
      <div className="space-y-1.5">
        <Label>Message</Label>
        <Textarea value={body} onChange={(e) => setBody(e.target.value)} rows={3} />
      </div>
      <Button onClick={submit} disabled={isPending}>
        {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
        Publish announcement
      </Button>
    </div>
  );
}
