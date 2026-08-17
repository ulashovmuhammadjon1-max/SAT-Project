"use server";

import { Prisma } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

/**
 * Requests a student may spend per UTC day.
 *
 * Not exported: a "use server" module may only export async functions, and
 * exporting a plain const fails the Next compile with "Only async functions are
 * allowed to be exported in a 'use server' file" — which `tsc --noEmit` does
 * not catch, so it only shows up as a broken page.
 */
const DAILY_LIMIT = 5;

/**
 * Model alias rather than a pinned version, on purpose.
 *
 * The first version of this file hardcoded `gemini-1.5-flash`, which Google has
 * since retired — every call returned 404 NOT_FOUND. The `-latest` aliases keep
 * tracking whatever the current generation is, so the tutor does not silently
 * die the next time a version is sunset. Overridable by env for the day an
 * alias behaves differently from what the prompt expects.
 */
const MODEL = process.env.GEMINI_MODEL || "gemini-flash-lite-latest";

export interface TutorResponse {
  ok?: boolean;
  error?: string;
  message?: string;
  /** Requests left today, always returned so the UI can show the budget. */
  remaining?: number;
}

const startOfUtcDay = () => {
  const d = new Date();
  d.setUTCHours(0, 0, 0, 0);
  return d;
};

/**
 * Requests spent today. Read-only — spending happens in `spendRequest`.
 *
 * Split from the increment so a student is never charged for a request that
 * failed before it reached the model. Losing one of five daily hints to a
 * transient 503 is the kind of thing that reads as the product being broken.
 */
async function requestsUsedToday(userId: string): Promise<number> {
  const row = await prisma.tutorUsage.findUnique({
    where: { userId_date: { userId, date: startOfUtcDay() } },
    select: { requestCount: true },
  });
  return row?.requestCount ?? 0;
}

async function spendRequest(userId: string): Promise<void> {
  const date = startOfUtcDay();
  await prisma.tutorUsage.upsert({
    where: { userId_date: { userId, date } },
    update: { requestCount: { increment: 1 } },
    create: { userId, date, requestCount: 1 },
  });
}

/**
 * HTML out, mathematics in.
 *
 * Stems are stored as HTML carrying KaTeX spans, so the raw value is full of
 * `<p>`/`<u>`/`<table>` noise that costs tokens and tells the model nothing.
 * The `\( … \)` delimiters stay — they are how the mathematics is written, and
 * stripping them would turn `\frac{3}{4}` into something ambiguous.
 */
function toPlainText(html: string): string {
  return html
    .replace(/<br\s*\/?>/gi, "\n")
    .replace(/<\/(p|div|li|tr|h[1-6])>/gi, "\n")
    .replace(/<li[^>]*>/gi, "• ")
    .replace(/<td[^>]*>|<th[^>]*>/gi, "\t")
    .replace(/<[^>]+>/g, "")
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&deg;/g, "°")
    .replace(/\n{3,}/g, "\n\n")
    .replace(/[ \t]{2,}/g, " ")
    .trim();
}

interface QuestionForTutor {
  stem: string;
  type: string;
  choices: { label: string; content: string }[];
  passage: { content: string } | null;
  hasImage: boolean;
}

function buildPrompt(q: QuestionForTutor, studentNote: string): string {
  const parts: string[] = [];

  if (q.passage) {
    parts.push(`PASSAGE:\n${toPlainText(q.passage.content)}`);
  }

  parts.push(`QUESTION:\n${toPlainText(q.stem)}`);

  // A free-response question has no choices at all; the old prompt printed a
  // bare "Options:" header with nothing under it, which invites the model to
  // invent four.
  if (q.choices.length > 0) {
    parts.push(
      "ANSWER CHOICES:\n" +
        q.choices.map((c) => `${c.label}) ${toPlainText(c.content)}`).join("\n")
    );
  } else {
    parts.push(
      "This is a student-produced response question: the student types a number, there are no choices."
    );
  }

  // The model cannot see the figure, so it must not pretend to. Without this it
  // happily describes a graph it has never seen.
  if (q.hasImage) {
    parts.push(
      "NOTE: this question has an accompanying figure that you CANNOT see. Do not describe it or state values from it. Tell the student what to read off it instead."
    );
  }

  if (studentNote) {
    parts.push(`WHAT THE STUDENT SAID THEY ARE STUCK ON:\n${studentNote}`);
  }

  parts.push(
    [
      "You are an SAT tutor. Give ONE short hint — 2-3 sentences, under 60 words.",
      "",
      "Rules:",
      "- Never state or imply which choice is correct, and never give the final numeric answer.",
      "- Name the concept being tested and the FIRST step the student should take.",
      "- Address the student directly as 'you'. Be warm and brief.",
      "- Plain prose only: no markdown, no headings, no bullet points, no LaTeX.",
      "- If the student's note shows a specific misunderstanding, correct that misunderstanding.",
    ].join("\n")
  );

  return parts.join("\n\n");
}

/** Calls Gemini. Returns the hint, or throws with a message safe to show. */
async function callGemini(prompt: string): Promise<string> {
  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    // Deliberately explicit: this is the single most likely setup mistake, and
    // "something went wrong" would send someone hunting through the code.
    throw new Error("The tutor is not configured yet — GEMINI_API_KEY is not set.");
  }

  let res: Response;
  try {
    res = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent`,
      {
        method: "POST",
        // The key goes in the header, not the query string: query strings end
        // up in proxy and server logs.
        headers: { "Content-Type": "application/json", "x-goog-api-key": apiKey },
        body: JSON.stringify({
          contents: [{ parts: [{ text: prompt }] }],
          generationConfig: { temperature: 0.4, maxOutputTokens: 2000 },
        }),
        cache: "no-store",
      }
    );
  } catch (err) {
    console.error("[sat-tutor] network error", err);
    throw new Error("Could not reach the tutor. Check your connection and try again.");
  }

  if (!res.ok) {
    const body = await res.text().catch(() => "");
    console.error(`[sat-tutor] Gemini ${res.status}: ${body.slice(0, 500)}`);
    if (res.status === 429) {
      throw new Error("The tutor is busy right now. Try again in a minute.");
    }
    if (res.status === 400 || res.status === 403) {
      throw new Error("The tutor's API key was rejected. An admin needs to check it.");
    }
    if (res.status === 404) {
      throw new Error(`The tutor's model (${MODEL}) is unavailable. An admin needs to update it.`);
    }
    throw new Error("The tutor service is unavailable right now. Try again shortly.");
  }

  const data = (await res.json()) as {
    candidates?: {
      content?: { parts?: { text?: string }[] };
      finishReason?: string;
    }[];
    promptFeedback?: { blockReason?: string };
  };

  if (data.promptFeedback?.blockReason) {
    throw new Error("The tutor could not answer that one. Try rephrasing your question.");
  }

  const candidate = data.candidates?.[0];
  // Parts are joined rather than indexed at [0]: a response can arrive split
  // across several parts, and taking only the first truncates the hint.
  const text = (candidate?.content?.parts ?? [])
    .map((p) => p.text ?? "")
    .join("")
    .trim();

  if (!text) {
    console.error(
      `[sat-tutor] empty completion, finishReason=${candidate?.finishReason ?? "none"}`
    );
    throw new Error("The tutor did not return anything. Try again.");
  }

  return text;
}

/**
 * Ask the SAT tutor for a hint on a question.
 *
 * Rate-limited per student per UTC day. The budget is only spent once the model
 * has actually answered.
 */
export async function askSATTutor(
  questionId: string,
  studentNote?: string
): Promise<TutorResponse> {
  const user = await requireUser();

  let used: number;
  try {
    used = await requestsUsedToday(user.id);
  } catch (err) {
    // The table is created by 013_tutor_usage.sql. Until that migration has
    // been applied the whole feature is off, and saying so beats a stack trace.
    if (
      err instanceof Prisma.PrismaClientKnownRequestError &&
      (err.code === "P2021" || err.code === "P2022")
    ) {
      return { error: "The tutor is not set up yet — its database migration has not been run." };
    }
    throw err;
  }

  if (used >= DAILY_LIMIT) {
    return {
      error: `You have used all ${DAILY_LIMIT} tutor hints for today. They reset at midnight UTC.`,
      remaining: 0,
    };
  }

  const question = await prisma.question.findUnique({
    where: { id: questionId },
    select: {
      stem: true,
      type: true,
      imageUrl: true,
      choices: { select: { label: true, content: true }, orderBy: { order: "asc" } },
      passage: { select: { content: true } },
    },
  });

  if (!question) return { error: "That question could not be found.", remaining: DAILY_LIMIT - used };

  const note = (studentNote ?? "").trim().slice(0, 500);

  let hint: string;
  try {
    hint = await callGemini(
      buildPrompt(
        {
          stem: question.stem,
          type: question.type,
          choices: question.choices,
          passage: question.passage,
          hasImage: Boolean(question.imageUrl),
        },
        note
      )
    );
  } catch (err) {
    // Nothing spent — the student keeps the request.
    return {
      error: err instanceof Error ? err.message : "The tutor is unavailable right now.",
      remaining: DAILY_LIMIT - used,
    };
  }

  await spendRequest(user.id);

  return { ok: true, message: hint, remaining: Math.max(0, DAILY_LIMIT - (used + 1)) };
}

/** The student's remaining budget, for rendering the panel before they ask. */
export async function getTutorBudget(): Promise<{ remaining: number; limit: number }> {
  const user = await requireUser();
  try {
    return { remaining: Math.max(0, DAILY_LIMIT - (await requestsUsedToday(user.id))), limit: DAILY_LIMIT };
  } catch {
    return { remaining: DAILY_LIMIT, limit: DAILY_LIMIT };
  }
}
