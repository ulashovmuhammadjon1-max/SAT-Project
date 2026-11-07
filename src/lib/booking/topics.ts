/**
 * How the student booking page groups sessions into topics.
 *
 * The topic is the subject the host gave the session. Older slots predate
 * subjects and were always SAT study-plan sessions, so they are listed under
 * that name rather than as "Other".
 */
export const LEGACY_TOPIC = "SAT study plan";

export function topicOf(subject: string | null | undefined): string {
  return subject?.trim() || LEGACY_TOPIC;
}

/** SAT-specific questions are only asked when the session is about the SAT. */
export function isSatTopic(topic: string): boolean {
  return topic === LEGACY_TOPIC || /\bSAT\b/i.test(topic);
}
