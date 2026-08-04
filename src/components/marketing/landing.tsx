"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowRight, BarChart3, BookOpenCheck, Brain, GraduationCap, SplitSquareHorizontal, Timer } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

const FEATURES = [
  {
    icon: Timer,
    title: "Bluebook-accurate exam interface",
    description:
      "Timer placement, question palette, flagging, highlighting, and module transitions built to match the real Digital SAT experience.",
  },
  {
    icon: SplitSquareHorizontal,
    title: "True adaptive modules",
    description: "Module 2 difficulty routes automatically based on your Module 1 performance, just like test day.",
  },
  {
    icon: BookOpenCheck,
    title: "Deep review mode",
    description: "Every question reviewed with your answer, the correct answer, difficulty, timing, and a full explanation.",
  },
  {
    icon: Brain,
    title: "Vocabulary mastery",
    description: "Flashcards, quiz mode, and spaced repetition scheduling that adapts to what you already know.",
  },
  {
    icon: BarChart3,
    title: "Analytics that matter",
    description: "Track accuracy by domain and skill, time per question, and your predicted score over time.",
  },
  {
    icon: GraduationCap,
    title: "Built for every learner",
    description: "Full-length adaptive tests, targeted practice sets, and custom quizzes tailored to your weak spots.",
  },
];

export function Landing() {
  return (
    <div className="relative overflow-hidden">
      <div className="pointer-events-none absolute inset-x-0 top-0 -z-10 h-[600px] bg-[radial-gradient(circle_at_50%_-10%,_hsl(226_84%_92%),_transparent_60%)]" />

      <header className="mx-auto flex max-w-7xl items-center justify-between px-6 py-6">
        <Link href="/" className="flex items-center gap-2">
          <span className="flex h-9 w-9 items-center justify-center rounded-lg bg-navy-900 text-white">
            <GraduationCap className="h-5 w-5" />
          </span>
          <span className="font-display text-lg font-semibold tracking-tight">Summit Prep</span>
        </Link>
        <div className="flex items-center gap-2">
          <Button variant="ghost" asChild>
            <Link href="/login">Sign in</Link>
          </Button>
          <Button asChild>
            <Link href="/register">Get started</Link>
          </Button>
        </div>
      </header>

      <section className="mx-auto max-w-4xl px-6 pb-20 pt-16 text-center sm:pt-24">
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <span className="mb-6 inline-flex items-center rounded-full border border-border bg-card px-3 py-1 text-xs font-medium text-muted-foreground shadow-soft">
            Adaptive · Full-length · Bluebook-accurate
          </span>
          <h1 className="font-display text-4xl font-semibold tracking-tight text-balance sm:text-6xl">
            Practice the Digital SAT the way you&apos;ll actually take it.
          </h1>
          <p className="mx-auto mt-6 max-w-2xl text-lg text-muted-foreground text-balance">
            Full-length adaptive practice tests, an exam interface built to match Bluebook, and analytics that show
            exactly what to study next — all in one polished platform.
          </p>
          <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
            <Button size="lg" asChild>
              <Link href="/register">
                Start practicing free <ArrowRight className="h-4 w-4" />
              </Link>
            </Button>
            <Button size="lg" variant="outline" asChild>
              <Link href="/login">I have an account</Link>
            </Button>
          </div>
        </motion.div>
      </section>

      <section className="mx-auto max-w-7xl px-6 pb-24">
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {FEATURES.map((feature, i) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-60px" }}
              transition={{ duration: 0.4, delay: i * 0.05 }}
            >
              <Card className="h-full">
                <CardContent className="p-6">
                  <span className="mb-4 flex h-11 w-11 items-center justify-center rounded-xl bg-primary-50 text-primary-600">
                    <feature.icon className="h-5 w-5" />
                  </span>
                  <h3 className="mb-1.5 font-display text-lg font-semibold">{feature.title}</h3>
                  <p className="text-sm text-muted-foreground">{feature.description}</p>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </section>

      <footer className="border-t border-border py-8">
        <div className="mx-auto flex max-w-7xl flex-col items-center justify-between gap-3 px-6 text-sm text-muted-foreground sm:flex-row">
          <p>© {new Date().getFullYear()} Summit Prep. All rights reserved.</p>
          <p>An original, independent Digital SAT preparation platform.</p>
        </div>
      </footer>
    </div>
  );
}
