# Tests 6 and 7 — build in progress

Target: two full tests, 147 questions each. R&W 27/27/27 + Math 22/22/22.

## Where this stands

| Piece | Needed | Done | Where |
|---|---|---|---|
| R&W questions | 162 | **107** | `rw_*.py`, hand-transcribed and hand-answered |
| Math M2 Easy (both tests) | 44 | **44 — complete and verified** | `math_m2easy.py`, `verify_math_m2easy.py` |
| Math M1 + M2 Hard | 88 | 47 clean, already transcribed | `content-pool/new-source-transcripts/` leftovers |

**Resume here.** In order:

1. **R&W is 55 short** — 25 reading, 30 writing. About 30 usable August pages
   remain (listed below); the rest must be authored. Writing-domain items are the
   ones to author, for the reason given in the supply section.
2. **Math M1 / M2 Hard**: pull 88 from the 47 clean `new-source-transcripts`
   leftovers plus the untranscribed October Math pages (Oct IntB M2 p073-p096,
   Oct USB M1 p055-p075, unused Oct USC Math). Dedupe against production and
   verify every answer with sympy — the October *Math* keys were reliable
   (Oct IntB scored 22/22) unlike the R&W keys.
3. **Assemble** with the block-ordering rule below, reusing
   `../test-5-build/assemble_rw.py`'s rank-sort approach.
4. **Insert locally, sweep the real exam interface, then insert to production
   and publish** — the `insert_test5.mjs` / `seed_attempt.mjs` pair in
   `../test-5-build/` generalises with only the title changed.

### Math Module 2 (Easy) — done

44 authored questions, 22 per test, 19 MC + 3 FR each, domain mix 8 ALG / 6 ADV
/ 4 PSDA / 4 GT. `verify_math_m2easy.py` passes: sympy re-derives every answer
independently, module shape and numbering check out, the Test 1/2 house style is
enforced, and template dedupe runs against all 330 live production Math stems.

Nine first-draft questions were rewritten after the dedupe pass caught them
repeating a live template — including one that had reproduced a production
marble-jar question's exact 6/4/10 counts, and a factorable-quadratic item that
repeated one authored for Test 5. The metric itself had to be fixed first: prose
similarity alone scored exponential-evaluation against cubic-evaluation at 1.00.
Details are in `math_m2easy.py`'s docstring.

## The two findings that shape this build

**1. The October papers are parallel forms of one administration and share questions.**
Oct IntB, Oct USB and Oct USC are not three independent sources. Items recur across them
verbatim or with only proper nouns and numbers swapped. Oct USC Module 2 is close to a straight
clone of Oct USB Module 2 — six of its first seven questions are USB items in disguise. Every
October transcription in this directory was therefore deduped against the other October papers
as well as against the 735 questions live in production. 26 questions have been rejected this
way so far, and each rejection carries its reasoning in the `DROPPED` dict of its module file.

The single worst offender, rejected three separate times, is a fast-animal template: "X can
run/swim very fast — up to N km/hr — but it is significantly slower than the [falcon/eagle],
which can fly at speeds up to M km/hr. The difference between these speeds is largely _____ of
the fact that the features that make flight possible do less to limit top speeds…", with the
same four choices every time. It appears as OctIntB M1 Q5 (swordfish), OctUSB M2 Q3 (Indian
antelope) and OctUSC M2 Q4 (springbok).

**2. Answers are derived here, never taken from the source key.**
This is the Test 5 lesson applied from the start rather than as a later audit. Test 5 found 6
wrong answers in 81 banked R&W questions, and the October papers' own R&W keys disagreed with a
careful reading on 7 of 18 spot-checked items. Every question in this directory carries a `why`
field recording the reasoning that produced its answer. A side effect: the seven October
questions set aside during the Test 5 build *because* the key conflicted are usable again, and
four of them are included here.

The test-taker's on-screen selection is visible in many captures and is also not trusted — it
disagrees with the reasoning on several items (for instance OctIntB M1 Q17, where the student
picked C and the sentence boundary requires D).

## R&W transcription status

| File | Module | Usable | Dropped | Notes |
|---|---|---|---|---|
| `rw_octusb_m1.py` | OctUSB M1 | 25 | 2 | 1 cut-off capture, 1 template repeat of a live Test 5 item |
| `rw_octintb_m1.py` | OctIntB M1 | 21 | 2 | 4 questions never captured by the recording |
| `rw_octusc_m1.py` | OctUSC M1 | 13 | 3 | 11 never captured; all 3 drops are Oct IntB duplicates |
| `rw_octintb_m2.py` | OctIntB M2 | 20 | 7 | includes the build's only Cross-Text item |
| `rw_octusb_m2.py` | OctUSB M2 | 15 | 12 | |
| `rw_octusc_m2.py` | OctUSC M2 | 1 | 5 | near-clone of OctUSB M2; abandoned after Q7 |
| `rw_auguse.py` | AugUSE M1+M2 | 12 | 2 | writing-domain pages transcribed first |
| **Total** | | **107** | **33** | |

Still unread and believed usable (checked against production and against this
directory, no lexical match): **August USE** M1 p004, p005, p006, p009, p010,
p011, p012, p013, p014, p015 and M2 p031, p036, p039, p042, p043, p044 —
mostly reading-domain; **August USC** p002, p005, p007, p010, p012, p013, p014.

Domain mix so far: reading 59, writing 36. Six modules need roughly 84 reading and 78 writing,
so **writing is the binding constraint**, as it was for Tests 3–5. Boundaries and Form/Structure
are in reasonable supply; Transitions and Rhetorical Synthesis are the scarce ones, exactly as
`CLAUDE.md` warns.

## What is left, and the supply problem

Remaining untranscribed R&W: **August USE (54 pages) and August USC (13 pages)**. These are a
different administration from the October set, so they should not carry the October
cross-duplication — but they have not been checked yet, and the same dedupe pass is required
against everything in this directory and against production.

**The August papers overlap too, and the shortfall is now measured rather than guessed.** A
lexical check of every August page against all 405 R&W questions live in production and all 95
transcribed here (Jaccard similarity on content words, threshold 0.30) finds:

- **August USE: 24 of 54 pages already exist** — 5 duplicate an October question transcribed in
  this directory (Mary Seacole at 0.87, fruit-fly wing centroids at 0.66, "Tomato" loanwords at
  0.59, Buenos Aires walkability at 0.50, Austronesian languages at 0.39) and 19 duplicate a
  question already shipped in Tests 1–5 (Michelin Guide 0.70, Australian railroads 0.72,
  Pleistocene 0.54, text corpora 0.59, Basquiat 0.40 …).
- **August USC: 6 of 13 pages already exist**, including the Moran park-use study and the Cuaya
  dog-language study, both already live in Test 5.

So the EliteXSAT corpus as a whole recycles heavily — not just within the October administration
but across administrations and into the material already shipped. Usable remainder is about **30
August USE pages plus 7 August USC pages**, and some of those will still fail on capture quality
or on template (rather than lexical) duplication.

**Projected R&W total from source: about 128 of the 162 needed.** The shortfall of roughly 34 is
concentrated in the writing domains, which is also where the October yield was weakest.

The fallback is the one `CLAUDE.md` already sanctions and which Test 5's Math Module 2 already
used: author original SAT-style questions rather than ship an undersized module or reuse
content. Writing-domain items (Boundaries, Form/Structure/Sense, Transitions) are the right ones
to author, because their correctness is decidable by grammar rather than by judgement — the same
property that makes sympy verification work for Math. Each authored item must be checked against
every question in production and in this directory for template repetition, not just for exact
duplication.

## Module ordering requirement (from the user, restated)

Every R&W module runs the reading domains first and starts the writing block **at about question
14–15, never earlier**. `assemble_rw.py` in `../test-5-build/` enforces this by sorting on the
block rank rather than by inspection, and the same approach is to be reused here: reading blocks
in the order Words in Context → Text Structure/Purpose → Cross-Text → Central Ideas → Command of
Evidence → Inferences, then Boundaries → Form/Structure/Sense → Transitions → Rhetorical
Synthesis. Inference is always the last reading question; Rhetorical Synthesis is always last
overall. Verify programmatically that the block sequence is monotonic before shipping.

## Files

Each `rw_*.py` module exposes `SOURCE`, `MODULE`, `QUESTIONS` (a list of dicts with `num`,
`skill`, `passage`, `stem`, `choices`, `answer`, `why`, and optionally `table` or
`needs_figure`) and `DROPPED` (a dict of question number to the reason it was rejected). Passage
and choice text is already HTML with entities, matching the Test 1/2 house style required by
`CLAUDE.md`.
