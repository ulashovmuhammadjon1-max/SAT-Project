# RESUME — Math rebuild of Tests 6-31. Read this first.

The user asked for: check the answer keys (they report many mistakes), write
explanations for every question, then publish into Tests 6-31 Math using the
difficulty structure recorded at the top of CLAUDE.md.

## Where it stands

**Stage 2 (transcription) is COMPLETE — 1,102 of 1,102.** All twelve agents
finished. Every question was transcribed from its page image, solved
independently of the printed key, given a difficulty and an explanation.

**Stage 3 (verify the keys) is NEXT and has not started.** Nothing is in the
database: production still carries the original 2,046 authored/EliteXSAT Math
questions, and zero rows exist under `SATMATH:` or `SATHARD:`.

    python3 -c "import json,glob,os; [print(os.path.basename(f), sum(1 for _ in open(f))) for f in sorted(glob.glob('content-pool/satoplam-math/out/mx-*.jsonl'))]"

If an agent stopped early, relaunch it with the same brief — `dump_q.py`
skips ids already in its JSONL, so it resumes exactly where it left off.

## The pipeline, in order

1. **Parse** (done) — `parse_math.py` for Math 2.0/3.0, `parse_hard.py` for
   the Hard Book. Output `math_parsed.json` (1,641) and `hard_parsed.json`
   (361). **2,002 questions, 1,952 with a printed key.**
2. **Transcribe** (DONE) — 1,102 questions in `out/mx-*.jsonl`. The other 900
   extracted cleanly and need no transcription.
3. **Verify the keys** (START HERE) — compare each agent's derived answer against
   `printed_keys.json`. Where they disagree, a second independent reader
   adjudicates, exactly as `explanations/apply_key_verdicts.mjs` does for R&W:
   flip only when two independent readings agree against the printed key,
   never on one opinion. **Expect many disagreements — the user says the keys
   are full of mistakes, and the R&W equivalent found 21 wrong in 26.**
4. **Allocate** — fill Tests 6-31 to the CLAUDE.md mix. Every Hard Book
   question is a Module 2 Hard question. Screen each module's picks against
   every other question in the same test before assembling — the R&W build
   skipped that step and shipped 33 same-test duplicates.
5. **Insert** — retire the current Math (`moduleId = NULL, isPublished =
   false`), never delete: `Response.questionId` has no onDelete rule.
   Source prefix `SATMATH:` / `SATHARD:`, distinct from `AUTHORED/…`.

## Numbers that matter

- Tests 6-31 need **1,716** Math questions: EASY 364 / MEDIUM 676 / HARD 676.
- Supply is 2,002, so ~286 spare — but **multiple choice is the binding
  constraint**: 1,343 MC available against 1,482 needed at 3 free-response per
  module. The cap moves to ~5 FR per module, which closes it exactly and is
  closer to the real Digital SAT. Recorded in CLAUDE.md.
- Hard Book: 361 curated-hard against 364 Module 2 Hard slots. Near-exact fit.

## Traps already hit here — do not repeat

- **The article "A".** In `parse_hard.py`, a bare `A ` choice marker matched
  the article opening a sentence and swallowed 63 question bodies. Fixed by
  requiring the text after the marker to look like mathematics. CLAUDE.md
  already documented this as `LETTER_REF` and it came back anyway.
- **Math 3.0 prints no page numbers.** 418 questions had `page: None` and were
  unreachable. Records now carry `pdf_page` and `src`; page images are named
  `{src}-{pdf_page}.png` because naming by printed page silently pointed a
  Math 2.0 question at the wrong file's page 2.
- **Book 3 renames three Geometry sections.** Until its answer tables were
  aliased the same way its questions are, 53 keys silently failed to attach.
  Nothing errored; the count was just quietly lower.
- **The key is withheld from the agents on purpose.** `printed_keys.json` is
  held aside and `dump_q.py` never prints it. Do not "helpfully" put it back —
  it is the entire gate.

## Cosmetic, working, do not "fix" mid-run

Hard Book records carry no `src`, so their page images are named
`None-042.png`. It is unambiguous — that book has exactly one source file, and
`dump_q.py` reads and writes the same name — so it works. Changing the naming
while agents are running would make every one of them re-render. Set `src` in
`parse_hard.py` only once the transcription stage is finished.

## The books repeat themselves — dedupe at assembly, not after

mx-07 found, inside a single 93-question slice, the same probability item five
times, one solve-for-x item four times, and three more families twice or three
times each — differing only in a constant or a sitting. These books collect
real exam questions across many administrations, and the exams reuse
templates, so this is the EliteXSAT and SAToplam finding again in a third
corpus.

Stage 4 must therefore score candidate pairs before assembling, exactly as
`cb-question-bank/plan_dupe_fix.py` does for R&W: co-visible pairs only
(Module 1 plus one Module 2 branch), a detect threshold set by READING the
band rather than guessing it, and a reject line for incoming questions
stricter than the detect line. The R&W build skipped this and shipped 33
same-test duplicates.

## Defects the transcribers are finding — repair before allocation

Agents record these in each record's `note`; grep the JSONL for non-empty
notes to collect them. Representative so far:

- **Incomplete stems.** `linear-equations-54` drops the whole second half of a
  definition ("...divided by the time over which the speed changes") and a
  noun from the next sentence. It happens to stay answerable on units alone,
  which is exactly why a checker would not catch it. Needs repair or replacing.
- **Choices mislabelled in the book.** `linear-system-of-equations-3` prints
  its fourth choice as "E)". The parser also merged C and D into one string
  there — the same failure the key-vs-type cross-check flags.
- **Duplicate choices.** `expressions-51` prints A and D identically.
- **Choice labels wrong in print.** `quadratics-111` prints ALL FOUR choices as
  "A)"; `quadratics-127` prints its last two both as "C)". Transcribed A-D in
  printed order.
- **Missing choice text.** `quadratics-133` prints "D)" with nothing after it.
- **No choice block at all.** `quadratics-140` has none, and its answer is an
  ordered pair (6, 185), which no grid-in can accept — the choices are
  probably missing from the book. Cannot ship in either format.
- **Internally inconsistent numbers.** `quadratics-93` gives a point (1, 58)
  that does not satisfy its own equation (which yields −6.25 at x = 1). Still
  answerable as an interpretation question, so no checker flags it.
- **The bare-`A` marker fails in BOTH directions.** Loosening it swallowed 63
  question bodies via the article "A"; tightening it with `LOOKS_MATHS` now
  rejects genuine maths choices, so at least 12 Hard Book questions are typed
  FREE_RESPONSE while the page prints four choices (`sathard-algebra-5, 8, 9,
  26, 29, 31, 37`, `sathard-advanced-math-1, 7, 9, 11, 14`). The transcribers
  corrected them. **Always trust the transcriber's type over the parse** — the
  key-vs-type cross-check already routes these to transcription for exactly
  this reason, so nothing is lost, but do not re-derive type from the parse at
  assembly time.
- **Type mislabelled by the parser.** `quadratics-74` is multiple choice; the
  book uses "(A)"-style markers there and the parser missed them. The
  transcriber corrected it. Trust the transcriber's type over the parse.
- **Exact duplicate questions inside one book**, e.g. four pairs in the linear
  slice alone. See the recycling section above.

- **Unanswerable as printed** — these carry `answerLabel: null` and must be
  dropped or repaired, never imported:
  `ma3-linear-functions-20` (correct value 50 is not among the choices, and
  choice D is the *answer equation from the previous question* printed by
  mistake); `ma3-linear-functions-25` (stem says "in the given equation" and
  no equation is printed anywhere on the page); `ma3-exponential-functions-12`
  (correct 4/11 is printed as "4/1", a dropped digit, which equals 4 and
  duplicates choice A).
- **Figure contradicts the stem.** `ma3-linear-inequalities-2` says point
  P(−3, 5) lies in the shaded region; the region actually shaded is the wedge
  below both lines, which does not contain it.

- **Answer not among the choices** — `ma2-quadratics-20`. `65x + 20 = -15x²`
  solves to −1/3 and −4, while all four printed choices are positive, and no
  positive x can satisfy it (left side positive, right side negative). The
  choices fit `15x² − 65x + 20 = 0`, so the printed sign on the `65x` term is
  wrong. Recorded `answerLabel: "NONE"` with all four choices refuted. Needs a
  human decision: fix the sign or drop it.
- **Two correct answers.** `ma2-quadratics-22` (−14 or −21) and `-32` (−10 or
  −15) ask what a value "could be", and two values qualify. Either accept both
  in `correctAnswerFR` or drop them.

**Questions needing a figure** carry `needsFigure: true`. Agents were told to
put their reading of the graph in `note`, never in the stem, so a prose
description cannot leak the answer — CLAUDE.md rule 3. Those need a real
figure built (matplotlib to base64 PNG) or must be dropped at allocation.

## Known gaps

- ~~30 Areas&Volumes answers on book page 382~~ **CLOSED.** The user supplied
  the page as an image; the answers live in `key_overrides.json` and are
  applied on top of the parse, because that page is not in any PDF on disk and
  a re-parse would otherwise drop them again. Unkeyed fell 48 → 18.
- 11 questions have a key contradicting their parsed type, meaning the choice
  block failed to parse. They are in the transcribe pile.

## Still outstanding, unrelated to this job

Rotate the Neon database password, the Resend API key and the Gmail password —
all three were pasted into the session that produced this work.
