import type { SessionType } from "@prisma/client";

/**
 * Display copy for each session type.
 *
 * Plain constants, so they must not live in a `"use server"` module — such a
 * file may only export async functions, and exporting an object there fails
 * the build rather than any test.
 */
export const EVENT_TYPE_LABELS: Record<SessionType, string> = {
  ONE_ON_ONE_SAT: "1-on-1 SAT guidance",
  TEST_ANALYSIS: "Weekly practice-test review",
  FINANCIAL_LITERACY: "Financial literacy",
  LECTURE: "Expert lecture",
  WORKSHOP: "Workshop",
};

export const EVENT_TYPE_BLURB: Record<SessionType, string> = {
  ONE_ON_ONE_SAT: "One-to-one strategy with a 1580 scorer.",
  TEST_ANALYSIS:
    "We work through the week's practice test together — the questions people missed, and why.",
  FINANCIAL_LITERACY: "How money actually works, taught properly and free.",
  LECTURE: "A guest expert on a subject worth an hour of your time.",
  WORKSHOP: "Hands-on, small group, bring your questions.",
};
