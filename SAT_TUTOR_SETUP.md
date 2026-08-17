# SAT Tutor — setup and operation

A hint button on every Question Bank question, answered by Google's Gemini free
tier. Verified working end to end on 2026-08-17.

## What a student gets

One hint at a time, 2–3 sentences, capped at **5 per student per UTC day**. The
prompt forbids naming the correct choice or giving the final number, so the
question still has to be worked. Four question shapes were probed against the
live model — Math multiple-choice, student-produced response, Reading & Writing
with a passage, and a question carrying a figure — and none of the hints leaked
the answer.

## Setup

### 1. Get a key

<https://aistudio.google.com/app/apikey> → **Get API key** → create one in a new
project.

### 2. Put it in the environment

This repo reads `.env` (not `.env.local`). `.gitignore` covers `.env*`, so it
will not be committed.

```bash
GEMINI_API_KEY="AIza…"
```

Optionally pin a model — the default is `gemini-flash-lite-latest`:

```bash
GEMINI_MODEL="gemini-flash-latest"
```

### 3. Apply the migration

**Do not run `prisma migrate dev`.** This repo keeps hand-applied SQL in
`prisma/migrations/manual/`, and `migrate dev` tries to read that directory as a
migration and fails with P3015. Apply the SQL directly:

```bash
# local dev
PGPASSWORD=postgres psql -h localhost -U postgres -d sat_platform \
  -v ON_ERROR_STOP=1 -f prisma/migrations/manual/013_tutor_usage.sql

npx prisma generate
```

For production, run the same file against the Neon database — the SQL editor in
the Neon dashboard is the simplest route.

### 4. Restart

```bash
npm run dev
```

Open any question under `/practice/<id>` and click **Stuck? Get a hint**.

## Deploying

1. Set `GEMINI_API_KEY` in the host's environment variables (Vercel: Project →
   Settings → Environment Variables).
2. Apply `013_tutor_usage.sql` to the production database.

Order matters only in that the table must exist before a student clicks the
button; until it does the panel says the tutor is not set up rather than
throwing. Nothing else in the app touches `TutorUsage`, so an unapplied
migration cannot break another page — see the schema rule in CLAUDE.md.

## Cost

The free tier covers this comfortably. Each hint is roughly 400–900 input tokens
and under 100 output. At the 5/day cap, a thousand daily active students who all
spend their full budget is ~5,000 calls a day; the constraint you would hit
first is the per-minute rate limit, not a bill.

## Changing the limits

`src/server/actions/student/sat-tutor.ts`:

- `DAILY_LIMIT` — hints per student per UTC day.
- `MODEL` — model alias, overridden by `GEMINI_MODEL`.
- `buildPrompt()` — the tutor's instructions, including the no-answer rules.

## Things that will bite you

**The model name goes stale.** The first version of this file hardcoded
`gemini-1.5-flash`, which Google has retired; every call returned 404. The
default is now a `-latest` alias for that reason. To see what a key can actually
reach:

```bash
curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY" \
  | grep -o '"models/[^"]*"'
```

**`tsc` does not catch `"use server"` violations.** A `"use server"` module may
only export async functions. Exporting a plain `const` from one typechecks fine
and then fails at page load with *"Only async functions are allowed to be
exported in a 'use server' file"*. It cost a debugging round here; if the tutor
button vanishes from the page, check the dev server log for that message before
anything else.

**Failed calls do not cost the student a hint.** The budget is only spent after
the model has answered. If you refactor `askSATTutor`, keep the spend after the
call, not before — losing one of five hints to a transient 503 reads as the
product being broken.

## Troubleshooting

| Symptom | Cause |
|---|---|
| "not configured yet — GEMINI_API_KEY is not set" | Key missing from `.env`, or the server was not restarted after adding it |
| "API key was rejected" | Key is wrong, or the Generative Language API is not enabled on the project |
| "model (…) is unavailable" | That model name is retired — list the available ones with the curl above |
| "not set up yet — its database migration has not been run" | `013_tutor_usage.sql` has not been applied to this database |
| Button missing entirely | Check the dev log for the `"use server"` export error |
