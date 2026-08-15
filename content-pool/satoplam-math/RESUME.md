# RESUME — Math rebuild of Tests 6-31. Read this first.

The user asked for: check the answer keys (they report many mistakes), write
explanations for every question, then publish into Tests 6-31 Math using the
difficulty structure recorded at the top of CLAUDE.md.

## Where it stands

**Stage 1 (transcription) is RUNNING.** Twelve agents `mx-01` … `mx-12` are
transcribing the 1,102 questions whose maths did not survive text extraction.
Each appends to `out/mx-NN.jsonl` after every question, so progress is on disk
even if every agent dies.

    python3 -c "import json,glob,os; [print(os.path.basename(f), sum(1 for _ in open(f))) for f in sorted(glob.glob('content-pool/satoplam-math/out/mx-*.jsonl'))]"

If an agent stopped early, relaunch it with the same brief — `dump_q.py`
skips ids already in its JSONL, so it resumes exactly where it left off.

## The pipeline, in order

1. **Parse** (done) — `parse_math.py` for Math 2.0/3.0, `parse_hard.py` for
   the Hard Book. Output `math_parsed.json` (1,641) and `hard_parsed.json`
   (361). **2,002 questions, 1,952 with a printed key.**
2. **Transcribe** (running) — 1,102 questions flagged `needs_vision`. The
   other 900 extracted cleanly and need no transcription.
3. **Verify the keys** (next) — compare each agent's derived answer against
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
