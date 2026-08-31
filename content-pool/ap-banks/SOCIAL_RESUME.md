# Social Sciences build — exact state, and how to resume

The user asked for the three remaining Social Sciences subjects and said to
continue after a usage-limit reset without waiting for approval. This file is
what the next session needs to pick the work up cold.

## State: 164 of 171 topics authored, every one of them gated

| subject | authored | remaining |
|---|---|---|
| Comparative Government (`k<unit>_<n>.py`) | **43 / 43 — COMPLETE** | none |
| Human Geography (`g<unit>_<n>.py`) | 64 / 68 | 7.5, 7.6, 7.7, 7.8 |
| US Government (`v<unit>_<n>.py`) | 57 / 60 | 5.11, 5.12, 5.13 |

Every authored topic has a passing `verify_*.py`. There are no ungated drafts
left — the eight that were listed here previously have all been gated, and the
short module (`g4_8`) has its thirtieth question.

Comp Gov exports clean: 1,290 questions, 43 topics x exactly 30, five choices
each, answer key **6/6/6/6/6 on every single topic**, zero near-duplicate
warnings, zero math spans.

## The concurrency lesson — read this before spawning anything

Six Opus authoring agents were launched at once. **All six died on the session
usage limit within minutes**, each partway through its first or second topic.
Almost nothing was authored, and the budget for the window was gone. A later
run of three agents also lost two of them to the limit mid-topic.

**Two at a time is the working ceiling.** It leaves the coordinator headroom to
assemble, verify and insert, and it is why the per-topic commit rule matters:
`git add content-pool/ap-banks && git commit && git push` after **every**
topic, never at the end.

Stage that PATH, never `git add -A`. `-A` stages everything dirty in the tree,
including app-code edits the coordinator is midway through, and it has twice
shipped unrelated work inside a content commit.

**A stopped agent leaves damage, not just absence.** Validate anything that was
in flight before trusting it: one module was left syntactically broken (a stray
`july := None,` between `ans=` and `why=`), one was left with no verifier at
all, and one had a verifier that failed a question whose arithmetic was
correct. Import the module, count the questions, and run the verifier before
assuming a rescued file is fine.

## What REMAINS, in order

1. Seven topics (above), 30 questions each, each with a passing verifier.
2. Per subject: `python3 export_units.py <modules> --subject <SUBJ> --out <file>`
   — enforces 30-per-topic and warns on near-duplicate stems.
3. `node content-pool/ap-banks/check_katex.mjs <spans>` on the exported spans.
   All three subjects are now **prose subjects** and should export **zero** math
   spans (see below), so this is a formality that should come back empty.
4. `PROD_URL=... node scripts/insert-ap-questions.mjs <file>`.
5. Move the three subjects from COMING_SOON to LIVE in `src/lib/ap/catalog.ts`
   — **last**, and only once every topic has questions behind it, or students
   tap through to empty sessions. `/ap/[slug]` already refuses non-live
   subjects, so nothing is exposed before this step.
6. `npx tsx scripts/check-ap-coverage.ts` — must report no problems. It starts
   failing the moment a subject goes live with an empty topic, which is exactly
   what it is for.

Already DONE and not to be repeated: all three CEDs read and all 171 topics
recorded (`*_topics.json`, `AP_*_CED.md`, `ced-source/*.txt.gz`); the course
outlines generated into `src/lib/ap/courses.ts`; `ApSubjectCode` widened; and
the six practice-test configs in `src/lib/ap/tests.ts`.

## These are PROSE subjects — the converter does not run on them

`export_units.py` typesets only `CALC_AB`, `CALC_BC` and `STATISTICS`
(`TYPESET_SUBJECTS`). Running mathfmt over Comp Gov produced 78 spans of which
**70 were damage**: 46 year ranges (`2000-2020` set with a real minus, so it
reads as subtraction), 12 numeric scales, the Niger **Delta** turned into the
symbol delta, and CED codes like `LEG-2.A.1f` broken apart.

None of it was catchable by the converter's round-trip gate, because a misread
loses no characters — only meaning. Do not re-enable typesetting for these
subjects, and do not hand-write LaTeX into the modules.

## The standing quality rule for these subjects

`SOCIAL_BRIEF.md` has the full spec. The part that matters most: there is no
sympy here. A wrong key in a Government bank is caught by a person reading or
not at all, so a key must trace to a CED sentence, and a question the author is
unsure of gets **cut, not guessed**.

The gate is the ANCHORS check: it pins each key to a distinctive substring of
its own choice text, because `export_units.py` reshuffles choices on the way
out and a key stored as a bare index is one careless edit away from pointing at
a distractor. Writing a verifier also forces the author to read all 30
questions, which is the only realistic way a wrong key gets caught here.

**Run negative controls on every check.** A checker that cannot fail is worse
than none, and this project has now paid for that five times.

## Known, and deliberately not fixed: cross-topic repeats

See `COMP_GOV_DEDUPE.md`. The finished Comp Gov bank carries ten cross-topic
pairs that are the same question asked twice. This is structural, not
sloppiness: 1,290 questions rest on 147 distinct CED statements — 11.6 per
statement — five topics have only three statements between them and their
thirty questions, and 54% of statements are cited from more than one topic
because the CED itself shares them.

Four replacement angles were drafted and all four were already asked by another
topic. **The lever is `PER_TOPIC`, not the wording** — 30 for these subjects,
where the CED supports roughly 10-15 on the thin topics. That is the user's
call with the questions already authored; it has not been changed.

Expect the same shape in Human Geography and US Government. Run the same scan
before insertion; do not spend a session rewriting what it finds until the
per-topic count is settled.
