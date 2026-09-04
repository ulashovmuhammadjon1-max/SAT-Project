# Sciences build — state, and how to resume cold

The owner asked for the AP sciences, **excluding all four Physics courses**,
one subject at a time, and said to continue after a usage-limit reset without
waiting for approval. This file is what the next session needs to pick the work
up with no memory of this one.

## Scope

| subject | prefix | topics | typeset? | state |
|---|---|---|---|---|
| Biology | `b` | 60 | no (prose) | **DONE — 1,800 questions LIVE in production** |
| Chemistry | `h` | 91 | no — hand-written spans | 33 authored, 6 agents running |
| Environmental Science | `e` | 99 | no (prose) | 37 authored, 6 agents running |

Agent territories, so a restart does not double-assign. Each is disjoint by
unit, which is what stopped siblings converging on the same question during
the Social Sciences build:

| agent | subject | units | topics |
|---|---|---|---|
| H-A | Chemistry | 2, 3 | 2.3-2.7, 3.1-3.13 (18) + validate `h2_2` |
| H-B | Chemistry | 4, 5, 6 | 4.1-4.3, 5.6-5.11, 6.1-6.9 (18) |
| H-C | Chemistry | 7, 8, 9 | 7.1-7.5, 8.6-8.11, 9.1-9.11 (22) |
| E-A | Env Sci | 2, 3, 4 | 2.2-2.7, 3.1-3.9, 4.1-4.6 (21) |
| E-B | Env Sci | 5, 6 | 5.10-5.17, 6.1-6.13 (21) + validate `e5_9` |
| E-C | Env Sci | 8, 9 | 8.6-8.15, 9.1-9.10 (20) |

Physics 1, Physics 2, Physics C Mechanics and Physics C E&M are **out of
scope**. They stay COMING_SOON in `src/lib/ap/catalog.ts`. Their CED dumps are
kept in `ced-source/` in case that ever changes; their topic files were
deliberately removed so nothing reads as planned work.

## Where things stand

Everything below is committed and pushed. Run the counter rather than trusting
this table, because agents are probably still adding to it:

```
python3 - <<'PY'
import json, os, re
for subj, pre in (("BIOLOGY","b"), ("CHEMISTRY","h"), ("ENV_SCI","e")):
    t = json.load(open(f"{subj}_topics.json"))
    codes = [k for k in t if k != "_units"]
    have = {f"{m.group(1)}.{m.group(2)}" for f in os.listdir(".")
            if (m := re.match(rf"^{pre}(\d+)_(\d+)\.py$", f))}
    ver = {f"{m.group(1)}.{m.group(2)}" for f in os.listdir(".")
           if (m := re.match(rf"^verify_{pre}(\d+)_(\d+)\.py$", f))}
    print(f"{subj:10s} {len(have)}/{len(codes)} authored, {len(ver)} verified")
    print("   missing:", " ".join(c for c in codes if c not in have) or "none")
    print("   NO verifier:", " ".join(sorted(c for c in codes if c in have and c not in ver)) or "none")
PY
```

A module with no verifier is a module with **no gate** — it was in flight when
its agent stopped. Import it, count its questions, and write the verifier
before exporting.

**A stopped agent leaves damage, not just absence, and the counter cannot see
it.** Four modules were left orphaned by the last session limit and all four
had 30 well-formed questions, so nothing about them looked wrong. Running
their verifiers found three real defects:

- `h8_5`'s diprotic titration table was sampled every 10.00 mL and climbed at a
  near-constant rate, behind a stem asking the student to read **two separate
  pH jumps** off it. There was nothing to read. The table was resampled around
  each equivalence volume.
- That module's own check counted raw pH differences between adjacent rows,
  which measures how finely the table was sampled as much as it measures
  chemistry. It measures slope now, and merges contiguous steep intervals so
  one jump straddling an equivalence volume counts once.
- `verify_e2_1` had an anchor that matched the **swapped distractor** as well
  as the key — precisely the ambiguity anchors exist to catch. When a
  distractor is the swap, the anchor has to carry both clauses.

And one of that file's negative controls **could not fail**: it lowered a
generalist count to invert a specialist-first ordering, but the specialists had
already fallen 100%, the maximum, so no change to the other column could
outpace them. It passed silently while proving nothing. Swapping the two
columns is what actually inverts the claim. Check that your mutation really
violates the thing you are asserting.

## Resume order

1. Finish Chemistry and Environmental Science. Each subject's units all go
   together and each gets ONE Vercel build when it flips live, which is what
   the owner asked for.
2. `python3 export_units.py <modules> --subject BIOLOGY --out /tmp/BIOLOGY.json`
3. `node check_katex.mjs <spans>` — Biology and ES are prose subjects and should
   export **zero** math spans. Chemistry will have real ones.
4. Cross-check every exported key against its source module (0 keys may move —
   `ApQuestionAttempt` stores the chosen INDEX, so a shifted choice silently
   rewrites past answers).
5. `PROD_URL=... node scripts/insert-ap-questions.mjs /tmp/BIOLOGY.json`
6. `PROD_URL=... npx tsx scripts/check-ap-coverage.ts --complete` — must be clean.
7. Generate the course outline into `src/lib/ap/courses.ts` with
   `gen_course_units.py`, add a practice-test blueprint to `src/lib/ap/tests.ts`,
   then move the subject COMING_SOON -> LIVE in `src/lib/ap/catalog.ts`.

**Steps 1–6 cost NO Vercel builds** — `vercel.json` skips the build when every
changed path is under `content-pool/`. Step 7 is app code and is the single
build per subject. That is why the owner asked for one subject at a time.

**Flip the catalog LAST.** `/ap/[slug]` refuses any subject the catalog does not
mark LIVE, so outlines can sit in `courses.ts` safely, but a live subject with
an empty topic drops a student into an empty session.

## Things already decided — do not relitigate

- **Prefixes are `b`, `h`, `e`.** `c`, `g`, `k`, `m`, `p`, `s`, `u`, `v` are
  taken by live banks (`c` alone is 111 Calculus modules). Reusing one
  overwrites shipped content.
- **NOTHING here is in `TYPESET_SUBJECTS`.** Chemistry was added and then
  removed after testing: mathfmt split `H2SO4` into `\(H_{2}\)SO4`, read
  `Fe2O3 + 3 CO` across the formula boundary, and set the electron
  configuration `1s2 2s2 2p6` with SUBscripts where it needs SUPERscripts.
  Chemistry authors hand-write `\( ... \)` spans instead, per CLAUDE.md's
  standing rule for Math content. Do not re-add any of the three.
- **No stem may reference a figure the bank cannot show.** No images are
  supported. Data goes in a `table=`.
- **Six agents are currently running** (three per subject) at the owner's
  explicit request. Six once died together on the session limit with almost
  nothing authored; what makes it survivable now is the per-topic commit rule,
  which has held through four runs. `git add content-pool/ap-banks`, never
  `-A`.

## The extractor, if a topic list ever needs regenerating

`extract_topics.py <ced.txt> <SUBJECT>` reads the UNIT AT A GLANCE tables, falls
back to the TOPIC pages for anything they omit, and repairs truncated titles by
preferring whichever source gives the longer one. It refuses to write a file
when numbering is not contiguous or a title looks mangled.

Chemistry needed four passes and still has four hand-transcribed `OVERRIDES`
with CED line citations, because unit 9's pages interleave the two columns
WITHIN a line — 9.1 reads "Support a claim Introduction" then "to Entropy". No
indent rule separates that, and guessing is what the brief forbids.

## A hole in the Biology CED source — do not fill it from memory

`EK 2.5.B.1` sub-point **ii**, the exocytosis mechanism, is **not in the PDF's
text layer at all**. The page ends at a bare "ii." and the next page opens
topic 2.6. Both `pdftotext` modes agree, so it is unrecoverable from this
source — presumably rendered as part of a graphic.

An authoring agent found this and handled it correctly, which is the behaviour
to preserve. The bank keys only what the *surviving* lead sentence supports:
that exocytosis moves large substances **out** of cells (from "into and out of
cells" plus sub-point i naming endocytosis as the inward one), and that it
**requires energy**. **No key asserts a mechanism** — no vesicle fusion, no
membrane budding — even though that is standard teaching.

Do not "complete" this from a textbook. A scan of all three science CED dumps
for sub-points truncated at a page break found this as the **only** instance,
so the extraction is otherwise sound.

## Open question the owner has not answered

**30 questions per topic may be too many.** `SOCIAL_DEDUPE.md` measured that 30
produces same-question repeats whenever a CED shares statements across topics —
Comparative Government shipped ten such pairs. At 250 science topics, 30 each is
7,500 questions. Environmental Science's 99 topics over a repetitive framework
is the most likely to suffer. Measure statement density per subject before
assuming 30 works; the lever is `PER_TOPIC` in `export_units.py`.
