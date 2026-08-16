"use client";

import type { Role } from "@prisma/client";
import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { toast } from "sonner";

import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { updateUserRole } from "@/server/actions/admin/users";

export function UserRoleSelect({ userId, role }: { userId: string; role: Role }) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  return (
    <Select
      value={role}
      disabled={isPending}
      onValueChange={(v) =>
        startTransition(async () => {
          const result = await updateUserRole(userId, v as Role);
          if (result.error) {
            toast.error(result.error);
            return;
          }
          router.refresh();
        })
      }
    >
      <SelectTrigger className="h-8 w-32">
        <SelectValue />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="STUDENT">Student</SelectItem>
        <SelectItem value="REVIEWER">Reviewer</SelectItem>
        <SelectItem value="ADMIN">Admin</SelectItem>
      </SelectContent>
    </Select>
  );
}
