# Sciences build — state, and how to resume cold

The owner asked for the AP sciences, **excluding all four Physics courses**,
one subject at a time, and said to continue after a usage-limit reset without
waiting for approval. This file is what the next session needs to pick the work
up with no memory of this one.

## Scope

| subject | prefix | topics | typeset? | state |
|---|---|---|---|---|
| Biology | `b` | 60 | no (prose) | **in progress** |
| Chemistry | `h` | 91 | **YES** | not started |
| Environmental Science | `e` | 99 | no (prose) | not started |

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

At the last check Biology was **38 of 60 authored, 37 verified**, with four
agents running. A module with no verifier is a module with **no gate** — it was
in flight when its agent stopped. Import it, count its questions, and write the
verifier before exporting.

## Resume order

1. Finish Biology's remaining topics. Then Chemistry, then Environmental
   Science — one subject at a time, all its units together, which is the
   owner's explicit instruction.
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
- **Chemistry is in `TYPESET_SUBJECTS`; Biology and ES are not.** Running
  mathfmt over prose turned the Niger *Delta* into the symbol delta and set
  year ranges as subtractions. Do not "fix" this by adding them.
- **No stem may reference a figure the bank cannot show.** No images are
  supported. Data goes in a `table=`.
- **Four agents at a time.** Six died together on the session limit with almost
  nothing authored; three lost two of its number. The per-topic commit rule is
  what makes any of this survivable — `git add content-pool/ap-banks`, never
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

## Open question the owner has not answered

**30 questions per topic may be too many.** `SOCIAL_DEDUPE.md` measured that 30
produces same-question repeats whenever a CED shares statements across topics —
Comparative Government shipped ten such pairs. At 250 science topics, 30 each is
7,500 questions. Environmental Science's 99 topics over a repetitive framework
is the most likely to suffer. Measure statement density per subject before
assuming 30 works; the lever is `PER_TOPIC` in `export_units.py`.
