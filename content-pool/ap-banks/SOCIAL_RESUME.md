# Social Sciences build — FINISHED authoring; what is left is insertion

The user asked for the three remaining Social Sciences subjects and said to
continue after a usage-limit reset without waiting for approval. All 171 topics
are authored, verified and committed. The only step still outstanding needs a
production connection string.

## State: 171 of 171 topics, 5,130 questions, every one gated

| subject | topics | questions | key spread |
|---|---|---|---|
| Human Geography (`g<unit>_<n>.py`) | **68 / 68** | 2,040 | 408 each A-E |
| US Government (`v<unit>_<n>.py`) | **60 / 60** | 1,800 | 360 each A-E |
| Comparative Government (`k<unit>_<n>.py`) | **43 / 43** | 1,290 | 258 each A-E |

Checks that have actually been run, not assumed:

* **171 of 171 verifiers pass.**
* **All 5,130 exported questions cross-checked against their source modules:
  0 keys moved by the choice shuffle, 0 choice sets altered.** This is the one
  that matters most, because `ApQuestionAttempt` stores the *index* a student
  chose, so a moved choice would silently rewrite past answers.
* **0 strings carrying math markup** in any of the three exports.
* 171 modules swept for topic title/code drift against `*_topics.json`: 0
  mismatches (one was found and fixed — `g5_8` was missing an umlaut).
* `check-ap-coverage.ts --complete --from` on all three exports: 68/68, 60/60,
  43/43 topics with questions, no orphans, no thin topics.
* `check-ap-tests.ts`: all 22 practice tests pass, including the six new ones.
* `insert-ap-questions.mjs --dry-run` on all three banks: every id distinct.

## What REMAINS — one step, and it needs PROD_URL

```
PROD_URL='postgresql://...' node scripts/insert-ap-questions.mjs /tmp/HUMAN_GEO.json
PROD_URL='postgresql://...' node scripts/insert-ap-questions.mjs /tmp/US_GOV.json
PROD_URL='postgresql://...' node scripts/insert-ap-questions.mjs /tmp/COMP_GOV.json
PROD_URL='postgresql://...' npx tsx scripts/check-ap-coverage.ts        # must be clean
# then, and only then, flip the three subjects COMING_SOON -> LIVE in
# src/lib/ap/catalog.ts, and re-run check-ap-coverage.ts
```

Regenerate an export with
`python3 export_units.py <modules> --subject <SUBJ> --out <file>`.

The insert is idempotent — ids are a pure function of subject, topic and order
— so a partial run is safe to repeat. It batches 250 rows per round trip; the
older one-row-per-request version would not have survived 2,040 questions.

**Flip the catalog LAST.** `/ap/[slug]` refuses any subject the catalog does
not mark LIVE, so the outlines can sit in `courses.ts` indefinitely without a
student reaching an empty topic.

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

See `SOCIAL_DEDUPE.md`. The finished Comp Gov bank carries ten cross-topic
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
