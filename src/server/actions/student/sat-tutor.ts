"use server";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

const DAILY_LIMIT = 5;
const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
const GEMINI_MODEL = "gemini-1.5-flash";

export interface TutorResponse {
  ok?: boolean;
  error?: string;
  message?: string;
  remainingRequests?: number;
}

/**
 * Check if user has exhausted their daily tutor requests.
 */
async function checkAndUpdateUsage(userId: string): Promise<{ allowed: boolean; remaining: number }> {
  const today = new Date();
  today.setUTCHours(0, 0, 0, 0);

  const usage = await prisma.tutorUsage.findUnique({
    where: { userId_date: { userId, date: today } },
  });

  const requestCount = usage?.requestCount ?? 0;
  const allowed = requestCount < DAILY_LIMIT;

  if (allowed) {
    await prisma.tutorUsage.upsert({
      where: { userId_date: { userId, date: today } },
      update: { requestCount: { increment: 1 } },
      create: { userId, date: today, requestCount: 1 },
    });
  }

  return { allowed, remaining: Math.max(0, DAILY_LIMIT - (allowed ? requestCount + 1 : requestCount)) };
}

/**
 * Call Gemini API to get tutoring help on an SAT question.
 */
async function callGeminiAPI(
  stem: string,
  choices: string[],
  context: string
): Promise<string | null> {
  if (!GEMINI_API_KEY) {
    throw new Error("GEMINI_API_KEY not configured");
  }

  const questionText = `
${stem}

Options:
${choices.map((c, i) => `${String.fromCharCode(65 + i)}) ${c}`).join("\n")}
`;

  const prompt = `You are a friendly SAT tutor. A student is working on this question:

${questionText}

${context ? `Student's note: "${context}"` : ""}

Provide a brief, helpful hint or explanation (2-3 sentences max). Do NOT give away the answer directly. Instead:
- Point out what the question is really asking
- Remind them of the key concept
- Suggest how to eliminate wrong answers

Keep it concise and encouraging.`;

  try {
    const response = await fetch("https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        contents: [
          {
            parts: [{ text: prompt }],
          },
        ],
      }),
      cache: "no-store",
    });

    if (!response.ok) {
      const error = await response.text();
      console.error("Gemini API error:", error);
      return null;
    }

    const data = await response.json() as {
      candidates?: Array<{
        content?: {
          parts?: Array<{ text?: string }>;
        };
      }>;
    };

    const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
    return text ?? null;
  } catch (err) {
    console.error("Tutor API call failed:", err);
    return null;
  }
}

/**
 * Get tutoring help on an SAT question. Respects daily rate limit (5 requests/day, free tier).
 */
export async function askSATTutor(
  questionId: string,
  studentContext?: string
): Promise<TutorResponse> {
  const user = await requireUser();

  const { allowed, remaining } = await checkAndUpdateUsage(user.id);

  if (!allowed) {
    return {
      error: `You've used all 5 daily tutor requests. Come back tomorrow for more help!`,
      remainingRequests: 0,
    };
  }

  const question = await prisma.question.findUnique({
    where: { id: questionId },
    select: {
      stem: true,
      choices: { select: { content: true, label: true }, orderBy: { order: "asc" } },
      passage: { select: { content: true } },
    },
  });

  if (!question) {
    return { error: "Question not found." };
  }

  const tutorResponse = await callGeminiAPI(
    question.stem,
    question.choices.map((c) => c.content),
    studentContext || ""
  );

  if (!tutorResponse) {
    return {
      error: "Could not reach the tutor service right now. Please try again.",
      remainingRequests: remaining,
    };
  }

  return {
    ok: true,
    message: tutorResponse,
    remainingRequests: remaining,
  };
}
