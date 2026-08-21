import Link from "next/link";
import { ArrowLeft } from "lucide-react";

import { IeltsEssayForm } from "@/components/admin/ielts-essay-form";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "New Task 2 essay" };
export const dynamic = "force-dynamic";

export default async function NewEssayPage() {
  await requireAdmin();
  return (
    <div className="max-w-3xl space-y-6">
      <Link
        href="/admin/ielts/essays"
        className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground"
      >
        <ArrowLeft className="h-4 w-4" /> Task 2 Essays
      </Link>
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">New Task 2 essay</h1>
        <p className="text-sm text-muted-foreground">
          Add the essay first. Analysis, review and publishing come after it is saved.
        </p>
      </div>
      <IeltsEssayForm />
    </div>
  );
}
