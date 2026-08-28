"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { Loader2, Save, Trash2, Upload } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { deleteTeamMember, saveTeamMember, setTeamMemberActive } from "@/server/actions/admin/team";

export interface TeamMemberValues {
  id: string;
  name: string;
  title: string;
  email: string;
  bio: string;
  photo: string | null;
  order: number;
  isActive: boolean;
}

const MAX_PHOTO_BYTES = 2 * 1024 * 1024;

/** One form, used both for "add new" (no initial) and editing an existing row. */
export function TeamMemberForm({ initial }: { initial?: TeamMemberValues }) {
  const router = useRouter();
  const [pending, start] = useTransition();
  const [name, setName] = useState(initial?.name ?? "");
  const [title, setTitle] = useState(initial?.title ?? "");
  const [email, setEmail] = useState(initial?.email ?? "");
  const [bio, setBio] = useState(initial?.bio ?? "");
  const [order, setOrder] = useState(String(initial?.order ?? 0));
  const [photo, setPhoto] = useState<string>("");

  async function pickPhoto(file: File | undefined) {
    if (!file) return;
    if (!["image/png", "image/jpeg", "image/webp"].includes(file.type)) {
      toast.error("Use a PNG, JPG or WEBP image.");
      return;
    }
    if (file.size > MAX_PHOTO_BYTES) {
      toast.error("Keep the photo under 2MB.");
      return;
    }
    const dataUrl = await new Promise<string>((resolve, reject) => {
      const r = new FileReader();
      r.onload = () => resolve(String(r.result));
      r.onerror = reject;
      r.readAsDataURL(file);
    });
    setPhoto(dataUrl);
  }

  function save() {
    start(async () => {
      const res = await saveTeamMember({ id: initial?.id, name, title, email, bio, photo, order });
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success(initial ? "Member updated." : "Member added to the team page.");
      if (!initial) {
        setName(""); setTitle(""); setEmail(""); setBio(""); setOrder("0"); setPhoto("");
      }
      router.refresh();
    });
  }

  const preview = photo || initial?.photo || null;

  return (
    <div className="space-y-3">
      <div className="flex items-start gap-4">
        <label className="group relative flex h-20 w-20 shrink-0 cursor-pointer items-center justify-center overflow-hidden rounded-2xl border border-dashed border-border bg-secondary/40 text-muted-foreground transition-colors hover:border-primary/50">
          {preview ? (
            // eslint-disable-next-line @next/next/no-img-element
            <img src={preview} alt="" className="h-full w-full object-cover" />
          ) : (
            <Upload className="h-5 w-5" />
          )}
          <input
            type="file"
            accept="image/png,image/jpeg,image/webp"
            className="hidden"
            onChange={(e) => {
              void pickPhoto(e.target.files?.[0]);
              e.target.value = "";
            }}
          />
        </label>
        <div className="grid flex-1 gap-3 sm:grid-cols-2">
          <div className="space-y-1">
            <Label>Name</Label>
            <Input value={name} onChange={(e) => setName(e.target.value)} placeholder="Full name" />
          </div>
          <div className="space-y-1">
            <Label>Role title</Label>
            <Input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Community Lead" />
          </div>
          <div className="space-y-1">
            <Label>Email (shown publicly — optional)</Label>
            <Input value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="name@example.com" />
          </div>
          <div className="space-y-1">
            <Label>Display order</Label>
            <Input value={order} onChange={(e) => setOrder(e.target.value)} type="number" min={0} />
          </div>
        </div>
      </div>
      <div className="space-y-1">
        <Label>Short bio (optional)</Label>
        <Textarea value={bio} onChange={(e) => setBio(e.target.value)} rows={2} placeholder="One or two sentences." />
      </div>
      <div className="flex flex-wrap gap-2">
        <Button onClick={save} disabled={pending || !name.trim() || !title.trim()} className="gap-2">
          {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Save className="h-4 w-4" />}
          {initial ? "Save changes" : "Add member"}
        </Button>
        {initial && (
          <>
            <Button
              variant="outline"
              disabled={pending}
              onClick={() =>
                start(async () => {
                  const res = await setTeamMemberActive(initial.id, !initial.isActive);
                  if (res.error) toast.error(res.error);
                  else {
                    toast.success(initial.isActive ? "Hidden from the team page." : "Visible again.");
                    router.refresh();
                  }
                })
              }
            >
              {initial.isActive ? "Hide" : "Show"}
            </Button>
            <Button
              variant="ghost"
              className="text-destructive hover:text-destructive"
              disabled={pending}
              onClick={() => {
                if (!confirm(`Remove ${initial.name} from the team page?`)) return;
                start(async () => {
                  const res = await deleteTeamMember(initial.id);
                  if (res.error) toast.error(res.error);
                  else {
                    toast.success("Removed.");
                    router.refresh();
                  }
                });
              }}
            >
              <Trash2 className="h-4 w-4" />
            </Button>
          </>
        )}
      </div>
    </div>
  );
}
