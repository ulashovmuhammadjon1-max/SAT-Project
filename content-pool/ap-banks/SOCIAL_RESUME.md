# Social Sciences build — exact state, and how to resume

The user asked for the three remaining Social Sciences subjects and said to
continue after a usage-limit reset without waiting for approval. This file is
what the next session needs to pick the work up cold.

## The concurrency lesson — read this before spawning anything

Six Opus authoring agents were launched at once. **All six died on the session
usage limit within minutes**, each partway through its first or second topic.
Almost nothing was authored, and the budget for the window was gone.

**Do not run six agents in parallel again.** Two or three at a time is the
ceiling that leaves headroom for the coordinator to assemble, verify and
insert. The work is not urgent enough to justify losing a whole window to it.

What saved the run was the per-topic commit rule. Keep it, and keep it strict:
`git add -A && git commit && git push` after **every** topic, never at the end.

## What is DONE and committed

### The research — all three CEDs read, all 171 topics recorded
| file | contents |
|---|---|
| `HUMAN_GEO_topics.json` | all 68 topics, 7 units, verbatim CED titles |
| `US_GOV_topics.json` | all 60 topics, 5 units |
| `COMP_GOV_topics.json` | all 43 topics, 5 units |
| `AP_HUMAN_GEO_CED.md`, `AP_US_GOV_CED.md`, `AP_COMP_GOV_CED.md` | exam format, weightings, required documents/cases/countries |
| `ced-source/*.txt.gz` | the `pdftotext -layout` dumps, so none of this has to be re-fetched |

This is the expensive part and it is finished. Nothing below needs the PDFs
again except to double-check a wrapped topic title.

### Modules with a passing verifier (ready to export)
`g1_1 g4_1 g4_2 g4_3` (Human Geography), `v1_1 v3_1 v3_2` (US Gov),
`k1_1 k4_1` (Comparative Gov) — 9 topics, 270 questions.

### Modules committed as DRAFTS — no verifier, DO NOT EXPORT YET
`g1_2 g4_4 k1_2 k4_2 v1_2` — 5 topics, 150 questions.

Each was checked for 30 questions, five distinct choices, an in-range key and a
non-empty rationale before being committed, but that is not the gate. The gate
is the ANCHORS check in `verify_*.py`: it pins each key to a distinctive
substring of its own choice text, which is the only guard that survives an
edit, because `export_units.py` reshuffles the choices on the way out and a key
stored as a bare index is one careless edit away from pointing at a distractor.

**First job on resume: write those five verifiers and run them.**

### Shared checkers already built by the agents
`hg_check.py`, `geo_check.py` (Human Geography), `usgov_check.py`,
`gov345_check.py` (US Gov), `cg_check.py` (Comparative Gov). These are
libraries, not scripts — running one directly prints nothing, which is
expected. The `verify_*.py` files are the entry points.

### Tooling
- `gen_course_units.py <SUBJ>` turns a `*_topics.json` into the `ApUnit[]`
  literal for `src/lib/ap/courses.ts`.
- `scripts/check-ap-coverage.ts` asserts the course outline and the live
  question bank describe the same topics. Currently clean on all six live
  subjects (360 topics, 11,125 questions).
- `export_units.py` already knows the three new subjects at 30 questions each.

## What REMAINS

157 topics to author, at 30 questions each:

| subject | done | remaining |
|---|---|---|
| Human Geography (`g<unit>_<n>.py`) | 1.1, 1.2, 4.1–4.4 | 62 of 68 |
| US Government (`v<unit>_<n>.py`) | 1.1, 1.2, 3.1, 3.2 | 56 of 60 |
| Comparative Gov (`k<unit>_<n>.py`) | 1.1, 1.2, 4.1, 4.2 | 39 of 43 |

Then, in order:
1. Verifier for every module; all must pass.
2. `python3 export_units.py <modules> --subject <SUBJ> --out <file>` per subject
   — it enforces 30-per-topic and warns on near-duplicate stems.
3. `node content-pool/ap-banks/check_katex.mjs <spans>` on the exported spans.
4. `node scripts/insert-ap-questions.mjs <file>` with `PROD_URL` set.
5. `python3 gen_course_units.py <SUBJ>` → paste into `src/lib/ap/courses.ts`,
   widen `ApSubjectCode`, add the course entry.
6. Move the three subjects from `AP_PLANNED` to `AP_LIVE` in
   `src/lib/ap/catalog.ts` — **last**, and only once every topic has questions,
   or students tap through to empty sessions.
7. Add practice-test configs in `src/lib/ap/tests.ts` using the exam formats
   recorded in the three `AP_*_CED.md` files.
8. `npx tsx scripts/check-ap-coverage.ts` — must report no problems.

## The standing quality rule for these subjects

`SOCIAL_BRIEF.md` has the full spec. The part that matters most: there is no
sympy here. A wrong key in a Government bank is caught by a person reading or
not at all, so a key must trace to a CED sentence, and a question the author is
unsure of gets **cut, not guessed**. A short topic honestly reported beats a
full one with a lie in it.
