"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";

import { Switch } from "@/components/ui/switch";
import { toggleFeatureFlag } from "@/server/actions/admin/settings";

export function FeatureFlagToggle({ flagKey, isEnabled }: { flagKey: string; isEnabled: boolean }) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  return (
    <Switch
      checked={isEnabled}
      disabled={isPending}
      onCheckedChange={(checked) =>
        startTransition(async () => {
          await toggleFeatureFlag(flagKey, checked);
          router.refresh();
        })
      }
    />
  );
}
