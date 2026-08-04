"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, RefreshCw } from "lucide-react";

import { Button } from "@/components/ui/button";
import { reprocessUpload } from "@/server/actions/admin/uploads";

export function ReprocessButton({ uploadId }: { uploadId: string }) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  return (
    <Button
      variant="outline"
      disabled={isPending}
      onClick={() =>
        startTransition(async () => {
          await reprocessUpload(uploadId);
          router.refresh();
        })
      }
    >
      {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <RefreshCw className="h-4 w-4" />}
      Retry extraction
    </Button>
  );
}
