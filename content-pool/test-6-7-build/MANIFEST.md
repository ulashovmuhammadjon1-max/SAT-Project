# Tests 6 and 7 — build in progress

Target: two full tests, 147 questions each. R&W 27/27/27 + Math 22/22/22.

## Where this stands

| Piece | Needed | Done | Source |
|---|---|---|---|
| R&W questions | 162 | **95** | October papers, hand-transcribed and hand-answered |
| Math M1 + M2 Hard | 88 | 47 clean already transcribed | `content-pool/new-source-transcripts/` leftovers |
| Math M2 Easy (both tests) | 44 | 0 | must be **originally authored** per the standing rule |

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
| **Total** | | **95** | **31** | |

Domain mix so far: reading 59, writing 36. Six modules need roughly 84 reading and 78 writing,
so **writing is the binding constraint**, as it was for Tests 3–5. Boundaries and Form/Structure
are in reasonable supply; Transitions and Rhetorical Synthesis are the scarce ones, exactly as
`CLAUDE.md` warns.

## What is left, and the supply problem

Remaining untranscribed R&W: **August USE (54 pages) and August USC (13 pages)**. These are a
different administration from the October set, so they should not carry the October
cross-duplication — but they have not been checked yet, and the same dedupe pass is required
against everything in this directory and against production.

Best case that gets R&W to roughly 160 of the 162 needed, with no margin. The realistic
expectation is a shortfall, concentrated in the writing domains. The fallback is the one
`CLAUDE.md` already sanctions for Math and applies equally here: author original SAT-style
questions rather than ship an undersized module or reuse content. Writing-domain items
(Boundaries, Form/Structure/Sense, Transitions) are the safest to author, since correctness is
decidable by grammar rather than by judgement.

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
