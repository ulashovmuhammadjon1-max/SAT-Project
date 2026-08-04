import { PrismaClient } from "@prisma/client";
import bcrypt from "bcryptjs";

import { DOMAIN_TAXONOMY } from "../src/lib/constants";

const prisma = new PrismaClient();

async function main() {
  console.log("Seeding domains and skills...");
  for (const domain of DOMAIN_TAXONOMY) {
    const created = await prisma.domain.upsert({
      where: { code: domain.code },
      update: { name: domain.name, subject: domain.subject },
      create: { code: domain.code, name: domain.name, subject: domain.subject, order: 0 },
    });

    for (const skill of domain.skills) {
      await prisma.skill.upsert({
        where: { code: skill.code },
        update: { name: skill.name, domainId: created.id },
        create: { code: skill.code, name: skill.name, domainId: created.id, order: 0 },
      });
    }
  }

  console.log("Seeding users...");
  const adminPasswordHash = await bcrypt.hash("Admin123!", 12);
  const admin = await prisma.user.upsert({
    where: { email: "admin@summitprep.com" },
    update: {},
    create: {
      email: "admin@summitprep.com",
      name: "Summit Admin",
      role: "ADMIN",
      passwordHash: adminPasswordHash,
    },
  });

  const studentPasswordHash = await bcrypt.hash("Student123!", 12);
  await prisma.user.upsert({
    where: { email: "student@summitprep.com" },
    update: {},
    create: {
      email: "student@summitprep.com",
      name: "Demo Student",
      role: "STUDENT",
      passwordHash: studentPasswordHash,
      currentStreak: 3,
      longestStreak: 7,
    },
  });

  console.log("Seeding adaptive configuration...");
  await prisma.adaptiveConfig.upsert({
    where: { name: "Standard adaptive routing" },
    update: {},
    create: {
      name: "Standard adaptive routing",
      description: "Default Module 1 -> Module 2 routing thresholds.",
      rwThresholdPct: 70,
      mathThresholdPct: 70,
      isActive: true,
      updatedById: admin.id,
    },
  });

  console.log("Seeding feature flags...");
  const flags = [
    { key: "ai_tutor", label: "AI Tutor (review mode)", description: "Conversational AI tutor available during review." },
    { key: "ai_practice_generation", label: "AI-generated practice questions", description: "Generate new SAT-style questions on demand." },
    { key: "daily_study_plans", label: "Personalized daily study plans", description: "AI-recommended daily study plan based on weak areas." },
    { key: "voice_explanations", label: "Voice explanations", description: "Text-to-speech playback of question explanations." },
  ];
  for (const flag of flags) {
    await prisma.featureFlag.upsert({ where: { key: flag.key }, update: {}, create: { ...flag, isEnabled: false } });
  }

  console.log("Seeding welcome announcement...");
  await prisma.announcement.upsert({
    where: { id: "seed-welcome-announcement" },
    update: {},
    create: {
      id: "seed-welcome-announcement",
      title: "Welcome to Summit Prep",
      body: "Upload your first SAT practice PDF from the admin panel to get started.",
      audience: "ADMIN",
      isActive: true,
      createdById: admin.id,
    },
  });

  console.log("Seed complete.");
  console.log("Admin login: admin@summitprep.com / Admin123!");
  console.log("Student login: student@summitprep.com / Student123!");
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
