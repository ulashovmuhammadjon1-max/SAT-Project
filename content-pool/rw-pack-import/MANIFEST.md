# R&W pack import

Pipeline for importing a large Reading & Writing question pack into its own
collection, kept separable from the 4,557 questions already in the bank.

## How separation works

`QuestionCollection` (added in `prisma/migrations/manual/009_question_collections.sql`)
is a named batch. `Question.collectionId` points at it, `ON DELETE SET NULL`.

- **Original bank** = `collectionId IS NULL`. Nothing that existed before this
  migration has a collection, and nothing backfills one.
- **Imported pack** = `collectionId = <the collection>`.

That gives three things a `source` string could not: the admin bank filters on
it (`/admin/questions?collection=<slug>`), a bulk publish/hide/delete has a
stable key, and two import runs cannot disagree about spelling.

Students never see an unpublished question — the Question Bank's `where`
starts at `isPublished: true` — so an imported batch is invisible until it is
explicitly published, without any extra gating.

## Layout

```
content-pool/rw-pack-import/
  import_pack.mjs
  <slug>/
    collection.json      name, description, origin
    batches/*.json       arrays of questions
```

`collection.json`:

```json
{
  "name": "R&W Pack 2026",
  "slug": "rw-pack-2026",
  "description": "1,800 Reading & Writing questions imported from <source>.",
  "origin": "<filename>.pdf",
  "order": 1
}
```

Each batch file is an array of:

```json
{
  "ref": "p012-q3",
  "domainCode": "CAS",
  "skillCode": "CAS-WV",
  "difficulty": "MEDIUM",
  "passageTitle": null,
  "passage": "<p>… _____ …</p>",
  "stem": "Which choice completes the text with the most logical and precise word or phrase?",
  "choices": [
    { "label": "A", "content": "…", "isCorrect": false },
    { "label": "B", "content": "…", "isCorrect": true },
    { "label": "C", "content": "…", "isCorrect": false },
    { "label": "D", "content": "…", "isCorrect": false }
  ],
  "whyCorrect": "optional",
  "whyWrong": { "A": "…", "C": "…", "D": "…" }
}
```

`ref` must be unique across the whole pack — it is the resume key. Domain and
skill are looked up by `code`, never by `name`.

## Running it

```
node import_pack.mjs --slug rw-pack-2026              # validate, write nothing
node import_pack.mjs --slug rw-pack-2026 --apply      # write, unpublished
node import_pack.mjs --slug rw-pack-2026 --publish    # flip live, after audit
```

Local dev reads `DATABASE_URL`; production reads `PROD_URL` over Neon's HTTP
driver (this sandbox blocks raw Postgres on 5432).

The run is idempotent by `ref` and resumes where it stopped, which at 1,800
questions is not optional.

## What the validator refuses to write

Nothing is written unless every question passes. It rejects: a duplicate or
missing `ref`; an unknown domain/skill code, or a skill that does not belong to
its stated domain; anything other than exactly 4 choices labelled A–D with
exactly one correct; two choices with the same text; a "completes the text"
question with no `_____`; an "underlined portion" question with no `<u>`; a
cross-text question missing `Text 1`/`Text 2`; a stem naming a graph/table/
figure with neither `<table>` nor an `imageUrl`; a LaTeX macro or markdown
asterisks in prose; unbalanced HTML tags; and a stem that already exists in the
bank verbatim.

The tag-balance check uses `<u(?![a-z])` so `<ul>` is not counted as a `<u>` —
that exact substring bug has cost this project a build before.

## Answer keys — the part that actually decides whether this ships

This is transcribed R&W. Per CLAUDE.md, that is the one content type whose keys
have never survived contact with a careful reading:

| batch | wrong keys |
|---|---|
| Test 5 R&W (81 transcribed) | 6 (7.4%) |
| Tests 3–4 R&W (transcribed) | 44 |
| Tests 6–11 R&W (authored) | 3 in 648 |

At the transcribed rate, 1,800 questions carries on the order of 130 wrong
answers. Publishing before an independent answer pass would teach students the
wrong answer 130 times. So the sequence is: import unpublished → re-answer every
question independently of the supplied key → reconcile → publish.
