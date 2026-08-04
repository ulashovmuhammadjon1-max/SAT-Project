"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";

import { Switch } from "@/components/ui/switch";
import { toggleAnnouncement } from "@/server/actions/admin/settings";

export function AnnouncementToggle({ id, isActive }: { id: string; isActive: boolean }) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  return (
    <Switch
      checked={isActive}
      disabled={isPending}
      onCheckedChange={(checked) =>
        startTransition(async () => {
          await toggleAnnouncement(id, checked);
          router.refresh();
        })
      }
    />
  );
}
