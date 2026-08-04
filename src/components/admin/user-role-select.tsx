"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";

import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { updateUserRole } from "@/server/actions/admin/users";

export function UserRoleSelect({ userId, role }: { userId: string; role: "STUDENT" | "ADMIN" }) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  return (
    <Select
      value={role}
      disabled={isPending}
      onValueChange={(v) =>
        startTransition(async () => {
          await updateUserRole(userId, v as "STUDENT" | "ADMIN");
          router.refresh();
        })
      }
    >
      <SelectTrigger className="h-8 w-32">
        <SelectValue />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="STUDENT">Student</SelectItem>
        <SelectItem value="ADMIN">Admin</SelectItem>
      </SelectContent>
    </Select>
  );
}
