# Summit Prep — Digital SAT Preparation Platform

A production-oriented Digital SAT practice platform: full-length adaptive tests with a Bluebook-style
exam interface, a question bank, vocabulary flashcards with spaced repetition, an admin panel with an
AI-assisted PDF ingestion pipeline, and student/admin analytics.

This is an original implementation — it is not affiliated with or a copy of College Board's Bluebook
application. The exam UI recreates general layout conventions (timer placement, question palette,
passage-left/question-right reading layout) without copying any proprietary assets or text.

## Stack

- **Next.js 14** (App Router) + **React 18** + **TypeScript**
- **Tailwind CSS** + a hand-built **shadcn/ui**-style component library
- **Framer Motion** for transitions
- **PostgreSQL** + **Prisma**
- **Auth.js (NextAuth v5)** — credentials auth, JWT sessions, role-based middleware
- **Claude Opus 5** (via `@anthropic-ai/sdk`) for PDF structuring and explanation generation, with a
  no-API-key heuristic fallback so the full pipeline is testable without credentials
- **Recharts** for analytics charts, **Desmos API** for the in-exam graphing calculator

## Getting started

```bash
npm install
cp .env.example .env      # edit if your DB isn't the docker-compose default
docker compose up -d      # starts local Postgres
npm run db:push           # creates the schema (or `npm run db:migrate` for a tracked migration)
npm run db:seed           # domains/skills taxonomy, admin + demo student accounts, adaptive config
npm run dev
```

Visit `http://localhost:3000`.

**Seeded accounts:**

| Role    | Email                     | Password     |
| ------- | ------------------------- | ------------ |
| Admin   | `admin@summitprep.com`    | `Admin123!`  |
| Student | `student@summitprep.com`  | `Student123!`|

The database starts with only the SAT domain/skill taxonomy — no test content. Sign in as the admin
and upload a PDF from **Admin → PDF Ingestion** to populate tests, questions, or vocabulary.

### Enabling AI-assisted extraction

Without `ANTHROPIC_API_KEY` set, PDF uploads are processed by a regex-based heuristic extractor
(`src/lib/ai/providers/heuristic-provider.ts`) — it works end-to-end but produces lower-confidence
extractions that need manual correction before publishing. Set `ANTHROPIC_API_KEY` in `.env` to swap
in the real extraction provider (`src/lib/ai/providers/claude-provider.ts`, model `claude-opus-5`)
with no other code changes — `getExtractionProvider()` in `src/lib/ai/extraction-service.ts` picks
the provider automatically. The same provider powers AI-generated question explanations in the
question editor.

## Architecture

```
prisma/schema.prisma        Full data model: users, tests/modules/questions, attempts/responses,
                             vocabulary + SRS progress, PDF uploads + AI jobs, adaptive config,
                             feature flags, announcements, audit log, and future-AI-tutor tables.
src/lib/
  ai/                        Pluggable AI extraction interface + heuristic and Claude providers.
  pdf/                       PDF text extraction (pdf-parse).
  adaptive/                  Module 1 -> Module 2 branching logic.
  srs/                       SM-2 spaced repetition scheduler for vocabulary.
  scoring/                   Simplified accuracy -> scaled-score estimate for the dashboard.
src/server/actions/         Server Actions, split by domain (admin/*, student/*, auth/*).
src/components/
  ui/                        Design-system primitives (button, card, dialog, table, ...).
  admin/                     PDF review/publish flow, question/test/vocab editors, settings.
  exam/                      The Bluebook-style test-taking interface and review mode.
  vocabulary/                Flashcards and quiz mode.
src/app/
  (marketing)                Public landing page.
  (auth)                     Login / register.
  (student)                  Dashboard, tests, practice, vocabulary, bookmarks, analytics.
  (admin)                    Admin panel (role-gated by src/middleware.ts + requireAdmin()).
```

### Adaptive modules

Every full-length test has up to four modules: Reading & Writing Module 1 → Module 2 (EASY/HARD
branch) → Math Module 1 → Module 2 (EASY/HARD branch). After a student submits Module 1,
`submitModule()` (`src/server/actions/student/attempts.ts`) computes accuracy and routes to the
HARD or EASY Module 2 using the **active** `AdaptiveConfig` threshold — editable per-subject from
**Admin → Adaptive Settings**, matching the "editable threshold" requirement (e.g. 70/75/80/85%).

### PDF ingestion pipeline

`Admin → PDF Ingestion` → `createUpload()` stores the file, extracts text (`pdf-parse`), and runs it
through the configured `AIExtractionProvider`. Results land in `AIProcessingJob.extractedData` with a
confidence score; uploads below the confidence threshold are flagged `NEEDS_REVIEW`. The review page
(`/admin/uploads/[id]`) lets an admin edit extracted questions/vocabulary inline before publishing,
which materializes real `Test`/`Module`/`Question`/`AnswerChoice`/`Passage` or `VocabWord`/`VocabDeck`
records.

### Known trade-offs (by design, for this scope)

- **Next.js 14.2** (latest patch) was chosen over the freshly-released Next 16 for ecosystem stability
  with Auth.js, Prisma, and shadcn/ui. `npm audit` still lists a handful of Next.js advisories whose
  patched line is 16.x; most apply to configurations this app doesn't use (custom servers, Pages
  Router i18n). Revisit before a real production deploy.
- The Desmos calculator and Google Fonts both require outbound network access from the *browser* at
  runtime (not at build time) — they degrade gracefully (calculator shows a fallback message) if
  unreachable.
- Dashboard score estimates use a simplified linear accuracy→200-800 mapping
  (`src/lib/scoring/estimate.ts`), not College Board's official (proprietary) adaptive scoring curve.
- File storage is local disk (`storage/uploads/`, gitignored) — swap `src/lib/storage.ts` for an
  S3/Vercel Blob client before deploying anywhere without a persistent filesystem.
- Practice-mode (question bank) answers are not persisted to `Response` rows (that table is
  attempt-scoped); only full-test attempts feed analytics and score trends.

## Scripts

| Command             | Purpose                                    |
| -------------------- | ------------------------------------------- |
| `npm run dev`         | Start the dev server                        |
| `npm run build`       | Production build                            |
| `npm run lint`        | ESLint                                       |
| `npm run typecheck`   | `tsc --noEmit`                              |
| `npm run db:push`     | Push the Prisma schema without a migration   |
| `npm run db:migrate`  | Create/apply a tracked migration             |
| `npm run db:seed`     | Run `prisma/seed.ts`                        |
| `npm run db:studio`   | Prisma Studio                               |

## Deployment

Designed for Vercel + a managed Postgres instance (Neon, Supabase, RDS, etc.). Set `DATABASE_URL`,
`AUTH_SECRET`, `NEXTAUTH_URL`, and optionally `ANTHROPIC_API_KEY` in the deployment environment, then
run `prisma migrate deploy` against the target database before or during the build step. Swap
`src/lib/storage.ts` for object storage first — local disk writes don't persist across serverless
invocations.
