# Authoring brief: AP World History: Modern

Read this in full before writing a question. It is the sibling of
`SOCIAL_BRIEF.md` and `SCIENCE_BRIEF.md`; everything they say about honesty
and gates applies. What follows is what history adds, and it is not a small
difference.

## Module prefix — do not improvise one

| subject | prefix | example |
|---|---|---|
| World History: Modern | `w` | `w3_2.py`, `verify_w3_2.py` |

`b`, `c`, `e`, `g`, `h`, `k`, `m`, `p`, `s`, `u` and `v` are taken by the
Biology, Calculus, Environmental Science, Human Geography, Chemistry,
Comparative Government, Macro, Psychology, Statistics, Micro and US
Government banks. Using one overwrites live content.

## 71 topics across 9 units

`WORLD_HISTORY_topics.json` is the topic list, extracted from the official CED
(effective Fall 2024) and verified word by word against each topic's own page.
Unit sizes are 7, 7, 4, 8, 10, 8, 9, 9, 9. Unit 3 really does have only four
topics — that is not a truncated extraction.

Copy each title **verbatim** out of that JSON. Do not retype it.

## The gate, and why history is the hardest case yet

There is no sympy here and no arithmetic to recompute. Worse than the
Government banks, a history claim can be *nearly* true — right process, wrong
century; right cause, wrong region — and read perfectly well to someone who
half-knows the material. So:

> **A key must trace to a sentence in the CED.** Not to your knowledge of
> history, however confident. The CED's Key Concepts (`KC-3.2.I.A`) and
> Learning Objectives are the source, and the code goes in every `why`.
> A question you are unsure of is **cut and replaced**, never guessed.

This is stricter than it sounds and it is the whole point. You know a great
deal about world history that the CED does not assert. A question resting on
that knowledge is not an AP question and cannot be checked by anyone reading
this bank later.

    zcat ced-source/WORLD_HISTORY_ced.txt.gz > /tmp/wh.txt

**The layout is two interleaved columns**, and history is worse for this than
the sciences: on a TOPIC page the title sits in a narrow column beside the
skill statement, so a sentence can be split across lines with unrelated text
BETWEEN its halves. Six topic titles had to be reassembled by hand for exactly
this reason, and a seventh ran on into an un-spaced paragraph. Read enough
surrounding lines to be certain you have the whole statement before keying
anything to it.

## Dates and periodisation — the defect this subject invites

- **Write a span as "1450 to 1750", never "1450-1750".** This bank is not
  typeset and a hyphen between numerals is exactly what the converter once
  read as subtraction elsewhere. Prose only, no LaTeX at all.
- The CED's own dates are approximate and it says so: *"Events, processes, and
  developments are not constrained by the given dates and may begin before, or
  continue after, the period."* Do not write a question whose key depends on a
  boundary the CED explicitly loosens.
- A distractor that is right about the process and wrong only about the
  century is the best kind here — and it is also the easiest way to ship a
  wrong key. If you cannot cite the sentence that fixes the date, cut it.

## Real exam style

- Five choices, A–E. (The real Section I has four; the bank uses five
  throughout, and the practice-test config says so.)
- AP World History Section I is **stimulus-based**: nearly every question
  hangs off a source. You cannot show images, so use a **quoted or described
  textual source** — an excerpt, a treaty clause, a traveller's account, a
  table of figures — and ask the question of it.
- **Never invent a quotation and attribute it to a real person or document.**
  That is fabrication, and it will be read by students as fact. Either quote
  what the CED itself contains, or write an explicitly *unattributed,
  illustrative* source ("A merchant's account from the period describes…")
  and make the question turn on reasoning, not on who said it.
- Lean on the CED's own reasoning skills: contextualisation, comparison,
  causation, continuity and change. The "final topic" of each unit is
  explicitly a reasoning topic — 4.8, 9.9 and their siblings — so write those
  as reasoning questions, not as fact recall.
- Every distractor must be a claim a prepared student could believe.

## Figures

**No images are supported.** Never write "the map shows" or "in the image".
Put data in a `table=` and ask the question of the table. A stem that refers
to something the bank cannot display is the defect this project has already
shipped once.

## Mechanics

- `TOPIC = ("3.2", "Exact CED Title", 3)` — code, verbatim title, unit.
- `QUESTIONS = [dict(q=..., choices=[...], ans=<0-based>, why=...), ...]`
- **30 questions per topic**, exactly.
- Optional `table=dict(headers=[...], rows=[[...]])`.
- Do not hand-balance the key; `export_units.py` redistributes A–E.
- One passing `verify_<module>.py` per module, one anchor per question pinned
  to a distinctive substring of that question's own keyed choice.

## The failure modes this project has already paid for

- **An anchor must not match a distractor.** Where a distractor is the SWAP of
  the key — two regions exchanged, two centuries exchanged, cause and effect
  reversed — the anchor must carry **both** clauses. A real defect found in
  `verify_e2_1.py`, where an anchor matched the swapped distractor too.
- **Run a negative control on every check.** Corrupt a key on purpose and
  confirm the check fails. A control that *cannot* fail is worse than none: one
  in this repo lowered a count to invert an ordering when the other column had
  already fallen 100%, the maximum, so nothing could outpace it — it passed
  silently and proved nothing.
- **A control that fires for the wrong reason proves nothing** about the guard
  it is attached to. Check which assertion actually raised.
- **When a checker disagrees with your question, work out which is wrong
  BEFORE "fixing" the question.** A verifier here rejected a correct key
  because the check itself was inverted. The checker reads as infrastructure
  and the content reads as the thing under test, which makes editing the
  content the tempting move and often the wrong one.
- **A checker that under- or over-matches is worse than none.** Explicit
  lookarounds, never `\b` beside a digit or a letter run. A figure-language
  check in this repo fired on "the fullest picture of" and on a distractor
  naming an age structure *diagram* as a concept — both false.
- **Agents converge.** Keep to your assigned units, and grep the subject's
  existing modules for your key phrases before writing something obvious.
- **Commit after EVERY topic**, never at the end:
  `git add content-pool/ap-banks && git commit -m "AP World History 3.2 <title>: 30 questions + verifier" && git push -u origin claude/new-session-3w59v3`
  Stage that path, never `git add -A`. If a sibling's files are dirty, name
  your own files explicitly — a previous run swept five siblings' drafts into
  an unrelated commit and the history now misreports what it contains.
- **A stopped agent leaves damage, not just absence.** If you resume, import
  every module you did not personally finish, count its questions, and run its
  verifier before trusting it.
