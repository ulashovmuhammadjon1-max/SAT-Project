# Sciences build — state, and how to resume cold

The owner asked for the AP sciences, **excluding all four Physics courses**,
one subject at a time, and said to continue after a usage-limit reset without
waiting for approval. This file is what the next session needs to pick the work
up with no memory of this one.

## Scope

| subject | prefix | topics | questions | state |
|---|---|---|---|---|
| Biology | `b` | 60 | 1,800 | **LIVE** |
| Chemistry | `h` | 91 | 2,730 | **LIVE** |
| Environmental Science | `e` | 99 | 2,970 | **LIVE** |

**ALL THREE ARE DONE, INSERTED AND LIVE.** The catalog carries 12 subjects
and 23,755 questions. `check-ap-coverage --complete` is clean for all 12,
every outline topic backed by questions.

Nothing below is work still to do; it is the record of how it was done and
what went wrong, kept because the same traps recur in every build.

Agent territories, so a restart does not double-assign. Each is disjoint by
unit, which is what stopped siblings converging on the same question during
the Social Sciences build:

| agent | subject | topics | also gates |
|---|---|---|---|
| H-A | Chemistry | 3.4-3.13 (10) | `h3_3` |
| H-B | Chemistry | 6.1-6.9, 8.11 (10) | `h5_11` |
| H-C | Chemistry | 9.1-9.11 (11) | — |
| E-A | Env Sci | 4.1-4.6 (6) | `e3_5`, `e9_4` |
| E-B | Env Sci | 6.3-6.13 (11) | `e6_2` |
| E-C | Env Sci | 3.6-3.9, 9.5-9.10 (10) | — |

The first round of six ran until the session limit and authored **27 Chemistry
and 35 Environmental Science topics** between them, which is the per-topic
commit rule doing exactly what it exists for. Every one of the six stopped
mid-topic; five left an ungated module behind and one left a module whose
verifier failed.

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

A second round of rescues found the sharpest case yet. `verify_h8_10`
**rejected a correct key** — q3, which restates EK 8.10.A.2 almost verbatim.
The check was inverted: it built one tuple ordered `(acid, base)` and another
ordered `(base, acid)`, then compared index 0 against index 0 as though they
were parallel, so it demanded exactly the pairing the framework forbids. The
lesson generalises past this module: **when a checker disagrees with a
question, establish which one is wrong before "fixing" the question.** An
agent under time pressure will edit the content, because the checker looks
like infrastructure and the content looks like the thing being tested. Prefer
named booleans to indexing into tuples that merely read as parallel.

That check also could not be stated as one rule, because its items are three
different shapes: the key states both halves, or the stem states the excess
and the choices differ only in the addition, or the key states the rule
abstractly and one word pins its direction. A single blanket assertion
rejected a correct key and would have rejected the other two shapes in turn.

And one of `verify_e2_1`'s negative controls **could not fail**: it lowered a
generalist count to invert a specialist-first ordering, but the specialists had
already fallen 100%, the maximum, so no change to the other column could
outpace them. It passed silently while proving nothing. Swapping the two
columns is what actually inverts the claim. Check that your mutation really
violates the thing you are asserting.

## The sign bug, twice — the most transferable finding of this build

`cg_check.normalize` treated `+` and `-` asymmetrically: it **dropped a `+`
and kept a `-`**. That produced two separate holes in the answer-key gate, and
each was found by an authoring agent that then worked around it locally.

1. **`contains_phrase` matched a sign-flipped key.** An anchor of
   `+183 kJ/mol` matched a keyed choice of `-183 kJ/mol`, because the
   surviving `-` read as an ordinary delimiter to the lookbehind. In
   Chemistry units 6 and 9 the sign IS the answer, so the swap guard that
   exists to catch exactly that was blind to it.
2. **A sum and a product normalized to the same string.**
   `c = \lambda + \nu` and `c = \lambda \nu` both became `c lambda nu`.
   Those are the key and its distractor in topic 3.12.

Both are fixed in the shared helper: `contains_phrase` refuses a sign before a
phrase that opens with a digit, and `normalize` now keeps `+`.

**The lesson is about the workarounds, not the bug.** One agent wrote a
private raw matcher; another rewrote two distractors. Both were right that
their content had to ship, and both left the shared gate broken for every
other bank. One of them did the thing that made this recoverable: it left a
**tripwire** asserting the shared helper still had the bug, with a message
saying to come back if it ever stopped. Fixing the helper fired it.

**Measure the blast radius; do not reason about it.** Both fixes were run
against all 622 verifiers before and after. Each exposed a batch of anchors
that omitted a sign their keyed choice carried — 20 negative, then 15
positive — every one a real under-specification that would have matched a
sign-flipped distractor. Zero regressions after repair.

Three guards earned their keep while repairing:

- replacement was scoped to the `CLAIMS` block **by AST line range**, because
  one literal also appears inside a negative control where the anchor is
  deliberately unsigned, and a whole-file replace would have rewritten the
  control;
- a uniqueness check refused a literal shared by two questions until it was
  confirmed both need the same signed form (they do: different stems that
  both recompute to `+20.0`);
- one control had to be re-signed so it kept exercising the guard it names
  rather than tripping containment first. **A control that fires for the
  wrong reason proves nothing about the guard it is attached to.**

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
- **`git add content-pool/ap-banks` sweeps up a sibling's in-flight files.**
  Commit `de16559`, titled "AP Chemistry 8.10 Buffer Capacity", also contains
  five unrelated draft modules that five other agents had left uncommitted in
  the tree. Nothing was lost and the drafts needed committing anyway, but the
  history now misreports what that commit holds — the same defect CLAUDE.md
  records for the teacher-invite fix. It was **not** rewritten, because
  rewriting a pushed branch under running agents loses their work; the rule is
  to record it and move on. Before committing, run `git status --short`, and
  where other agents' files are dirty, name your own files explicitly instead
  of staging the directory.
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
