import Link from "next/link";
import { notFound } from "next/navigation";

import { TopicRunner } from "@/components/ap/topic-runner";
import { courseBySlug } from "@/lib/ap/courses";
import { getTopicSession } from "@/server/actions/student/ap";
import { requireUser } from "@/lib/session";

export const metadata = { title: "AP Practice" };
export const dynamic = "force-dynamic";

/** One topic's practice session. */
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
    <div className="space-y-6">
      <nav className="flex flex-wrap items-center gap-1.5 text-sm text-muted-foreground">
        <Link href="/ap" className="hover:text-foreground">
          AP Prep
        </Link>
        <span>/</span>
        <Link href={`/ap/${course.slug}`} className="font-medium hover:text-foreground">
          {course.name}
        </Link>
        <span>/</span>
        <span className="text-foreground">
          {params.topic} {topicMeta.title}
        </span>
      </nav>

      <TopicRunner
        questions={questions}
        backHref={`/ap/${course.slug}`}
        topicLabel={params.topic}
      />
    </div>
  );
}
