import Link from "next/link";
import { ArrowLeft } from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";
import { CustomTopicForm } from "@/components/ielts/custom-topic-form";
import { ReviewBalance } from "@/components/ielts/review-balance";
import { getReviewAllowance } from "@/lib/ielts/economy";
import { requireUser } from "@/lib/session";
import { REVIEWER_CLAIM } from "@/lib/ielts/constants";

export const metadata = { title: "Your Own Topic" };
export const dynamic = "force-dynamic";

export default async function CustomTopicPage() {
  const user = await requireUser();
  const allowance = await getReviewAllowance(user.id);

  return (
    <div className="space-y-6">
      <Link
        href="/ielts/writing"
        className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground"
      >
        <ArrowLeft className="h-4 w-4" /> Writing
      </Link>

      <div className="space-y-2">
        <h1 className="font-display text-2xl font-semibold tracking-tight">
          Write on your own topic
        </h1>
        <p className="max-w-2xl text-sm text-muted-foreground">
          Bring the question your teacher set, or one from a past paper, and get it marked
          the same way as ours. {REVIEWER_CLAIM.WRITING}.
        </p>
      </div>

      <ReviewBalance allowance={allowance} />

      <Card>
        <CardContent className="py-6">
          <CustomTopicForm />
        </CardContent>
      </Card>

      <p className="text-xs text-muted-foreground">
        Your topic and any image you upload are private to you and the reviewer who marks
        your work. They are never added to the published papers.
      </p>
    </div>
  );
}
