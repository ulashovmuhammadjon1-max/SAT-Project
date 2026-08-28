"use server";

import type { QuestionDifficulty, Subject } from "@prisma/client";
import { z } from "zod";

import { prisma } from "@/lib/prisma";
import { questionImageSrc } from "@/lib/question-image";
import { requireUser } from "@/lib/session";

/**
 * Assigning specific Question Bank questions.
 *
 * The teacher filters (subject, domain, skill, difficulty), asks for a count,
 * and gets back the *exact* questions — stems, choices and the marked answer —
 * before anything is assigned. The preview returns ids and the assignment is
 * created from those same ids, never from the filter: re-running the filter at
 * assign time would deal a different random set than the one the teacher read,
 * which is the same trap the pinned-ids practice session already avoids.
 */

const filterSchema = z.object({
  subject: z.enum(["MATH", "READING_WRITING"]),
  domainId: z.string().optional().or(z.literal("")),
  skillId: z.string().optional().or(z.literal("")),
  difficulties: z.array(z.enum(["EASY", "MEDIUM", "HARD"])).default([]),
  count: z.coerce.number().int().min(1).max(50),
});

export interface TaxonomyDomain {
  id: string;
  name: string;
  skills: { id: string; name: string }[];
}

/** Domains and skills for the picker's dropdowns. */
export async function getQuestionTaxonomy(subject: Subject): Promise<TaxonomyDomain[]> {
  await requireUser();
  const domains = await prisma.domain.findMany({
    where: { subject },
    orderBy: { code: "asc" },
    include: { skills: { orderBy: { code: "asc" } } },
  });
  return domains.map((d) => ({
    id: d.id,
    name: d.name,
    skills: d.skills.map((s) => ({ id: s.id, name: s.name })),
  }));
}

export interface PreviewQuestion {
  id: string;
  stem: string;
  imageUrl: string | null;
  difficulty: QuestionDifficulty;
  domainName: string;
  skillName: string;
  type: string;
  passage: string | null;
  /** Teacher-facing, so the key is included — this is the point of a preview. */
  choices: { label: string; content: string; isCorrect: boolean }[];
  correctAnswerFR: string | null;
}

export interface PreviewResult {
  questions?: PreviewQuestion[];
  /** How many questions match the filter in total, before the count is applied. */
  available?: number;
  error?: string;
}

/**
 * Draw a set for the teacher to read. Re-running reshuffles, which is how the
 * "not these ones" case is served — there is no accept/reject per question.
 */
export async function previewQuestionSet(input: {
  subject: string;
  domainId?: string;
  skillId?: string;
  difficulties?: string[];
  count: number;
}): Promise<PreviewResult> {
  await requireUser();

  const parsed = filterSchema.safeParse(input);
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Check the filters." };
  }
  const f = parsed.data;

  const where = {
    isPublished: true,
    domain: { subject: f.subject as Subject },
    ...(f.domainId ? { domainId: f.domainId } : {}),
    ...(f.skillId ? { skillId: f.skillId } : {}),
    ...(f.difficulties.length
      ? { difficulty: { in: f.difficulties as QuestionDifficulty[] } }
      : {}),
  };

  // Ids first, shuffled in memory — the same approach the student session
  // generator uses, and it keeps the draw provably inside the filter.
  const ids = await prisma.question.findMany({ where, select: { id: true } });
  if (ids.length === 0) {
    return { available: 0, questions: [], error: "No published questions match those filters." };
  }
  for (let i = ids.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [ids[i], ids[j]] = [ids[j], ids[i]];
  }
  const picked = ids.slice(0, f.count).map((r) => r.id);

  const rows = await prisma.question.findMany({
    where: { id: { in: picked } },
    select: {
      id: true,
      stem: true,
      imageUrl: true,
      difficulty: true,
      type: true,
      correctAnswerFR: true,
      domain: { select: { name: true } },
      skill: { select: { name: true } },
      passage: { select: { content: true } },
      choices: {
        select: { label: true, content: true, isCorrect: true },
        orderBy: { order: "asc" },
      },
    },
  });
  const byId = new Map(rows.map((r) => [r.id, r]));

  return {
    available: ids.length,
    questions: picked.flatMap((id) => {
      const q = byId.get(id);
      if (!q) return [];
      return [
        {
          id: q.id,
          stem: q.stem,
          imageUrl: questionImageSrc(q.id, q.imageUrl),
          difficulty: q.difficulty,
          domainName: q.domain.name,
          skillName: q.skill.name,
          type: q.type as string,
          passage: q.passage?.content ?? null,
          choices: q.choices,
          correctAnswerFR: q.correctAnswerFR,
        },
      ];
    }),
  };
}

/**
 * The questions in an already-created set, for the teacher to re-read later.
 * Ids are soft references, so a retired question simply drops out.
 */
export async function getAssignmentQuestions(assignmentId: string): Promise<PreviewQuestion[]> {
  const user = await requireUser();
  const assignment = await prisma.classAssignment.findUnique({
    where: { id: assignmentId },
    select: { questionIds: true, class: { select: { teacherUserId: true } } },
  });
  if (!assignment || assignment.class.teacherUserId !== user.id) return [];
  if (assignment.questionIds.length === 0) return [];

  const rows = await prisma.question.findMany({
    where: { id: { in: assignment.questionIds } },
    select: {
      id: true,
      stem: true,
      imageUrl: true,
      difficulty: true,
      type: true,
      correctAnswerFR: true,
      domain: { select: { name: true } },
      skill: { select: { name: true } },
      passage: { select: { content: true } },
      choices: { select: { label: true, content: true, isCorrect: true }, orderBy: { order: "asc" } },
    },
  });
  const byId = new Map(rows.map((r) => [r.id, r]));

  return assignment.questionIds.flatMap((id) => {
    const q = byId.get(id);
    if (!q) return [];
    return [
      {
        id: q.id,
        stem: q.stem,
        imageUrl: questionImageSrc(q.id, q.imageUrl),
        difficulty: q.difficulty,
        domainName: q.domain.name,
        skillName: q.skill.name,
        type: q.type as string,
        passage: q.passage?.content ?? null,
        choices: q.choices,
        correctAnswerFR: q.correctAnswerFR,
      },
    ];
  });
}
