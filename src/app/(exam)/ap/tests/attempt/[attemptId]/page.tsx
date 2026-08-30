import { notFound, redirect } from "next/navigation";

import { ApTestRunner } from "@/components/ap/test-runner";
import { getTestAttempt, submitTest } from "@/server/actions/student/ap-tests";
import { requireUser } from "@/lib/session";

export const metadata = { title: "AP Practice Test" };
export const dynamic = "force-dynamic";

/**
 * One sitting of an AP practice test.
 *
 * In the (exam) route group, so the test gets the whole viewport with no
 * sidebar or topbar competing with the question — the same treatment the SAT
 * exam and the AP topic runner get.
 *
 * Two states are resolved here rather than in the browser: an already-submitted
 * attempt goes straight to its result, and an attempt whose clock ran out while
 * the tab was closed is graded on arrival instead of reopening for more time.
 * `getTestAttempt` filters on the signed-in user, so an attempt id belonging to
 * someone else resolves to nothing and 404s.
 */
export default async function ApTestAttemptPage({
  params,
}: {
  params: { attemptId: string };
}) {
  await requireUser();
  const payload = await getTestAttempt(params.attemptId);
  if (!payload) notFound();

  if (payload.status !== "IN_PROGRESS") {
    redirect(`/ap/tests/result/${payload.attemptId}`);
  }

  if (new Date(payload.expiresAt).getTime() <= Date.now()) {
    await submitTest(payload.attemptId);
    redirect(`/ap/tests/result/${payload.attemptId}`);
  }

  return <ApTestRunner payload={payload} exitHref={`/ap/tests/${payload.subjectSlug}`} />;
}
