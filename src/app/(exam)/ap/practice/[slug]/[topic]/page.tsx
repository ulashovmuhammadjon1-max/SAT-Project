import { notFound } from "next/navigation";

import { TopicRunner } from "@/components/ap/topic-runner";
import { courseBySlug } from "@/lib/ap/courses";
import { getTopicSession } from "@/server/actions/student/ap";
import { requireUser } from "@/lib/session";

export const metadata = { title: "AP Practice" };
export const dynamic = "force-dynamic";

/**
 * One topic's practice session.
 *
 * This lives in the (exam) route group rather than under the student shell:
 * practice gets the whole viewport, with no sidebar or topbar competing with
 * the question, exactly like the practice test and Question Bank sessions.
 */
export default async function ApPracticePage({
  params,
}: {
  params: { slug: string; topic: string };
}) {
  await requireUser();
  const course = courseBySlug(params.slug);
  if (!course) notFound();

  const topicMeta = course.units
    .flatMap((u) => u.topics ?? [])
    .find((t) => t.code === params.topic);
  if (!topicMeta) notFound();

  const questions = await getTopicSession(course.code, params.topic);
  if (questions.length === 0) notFound();

  return (
    <TopicRunner
      questions={questions}
      backHref={`/ap/${course.slug}`}
      topicLabel={params.topic}
      topicTitle={topicMeta.title}
      courseName={course.name}
    />
  );
}
