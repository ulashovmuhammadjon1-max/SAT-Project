# Authoring brief: AP Biology, Chemistry, Environmental Science

Read this in full before writing a question. It is the sibling of
`SOCIAL_BRIEF.md`; everything there about honesty and gates applies, and the
differences below are what the sciences add.

## Module prefixes — do not improvise one

| subject | prefix | example | typeset? |
|---|---|---|---|
| Biology | `b` | `b3_2.py`, `verify_b3_2.py` | **no** |
| Chemistry | `h` | `h4_7.py`, `verify_h4_7.py` | **YES** |
| Environmental Science | `e` | `e6_1.py`, `verify_e6_1.py` | **no** |

`c`, `g`, `k`, `m`, `p`, `s`, `u` and `v` are already taken by the Calculus,
Human Geography, Comparative Government, Macro, Psychology, Statistics, Micro
and US Government banks. Using one of those overwrites live content.

## The gate, and what it can and cannot do

Biology and Environmental Science are like the Government banks: **no sympy**.
A wrong key is caught by a person reading, or not at all. So the rule is the
same one, and it is not negotiable:

> A key must trace to a sentence in the CED. A question you are unsure of is
> **cut and replaced**, never guessed. A short topic honestly reported beats a
> full one with a lie in it — but the exporter requires exactly 30, so cut and
> write another.

Chemistry is different in one respect only: where a question is quantitative,
the arithmetic **must** be recomputed in the verifier from the stimulus alone.
That is a real check and you must use it. It still says nothing about whether
the chemistry is right — only the CED citation does that.

## Where the CED is

    zcat ced-source/BIOLOGY_ced.txt.gz > /tmp/bio.txt

Same for `CHEMISTRY_ced.txt.gz` and `ENV_SCI_ced.txt.gz`. These are
`pdftotext -layout` dumps of the official Course and Exam Descriptions —
Biology effective Fall 2025, Chemistry Fall 2024, Environmental Science Fall
2026. Cite essential knowledge by its code (`ENE-1.A.1`, `SYI-1.B.2`, `TRA-1`)
in every `why`.

**The layout is two interleaved columns.** A sentence can be split across
lines with unrelated text between the halves. Read enough surrounding lines to
be certain you have the whole statement before you key anything to it — this
is exactly how the topic extractor produced "Gibbs" for a topic actually
called "Gibbs Free Energy and Thermodynamic Favorability".

## Notation

**Biology and Environmental Science: plain prose, no LaTeX.** `export_units.py`
does not typeset these subjects, by design — running the converter over prose
turned the Niger *Delta* into the symbol δ and set year ranges with a minus
sign. Write `2000 to 2020`, never `2000-2020`.

**Chemistry: write the notation the converter understands, still not LaTeX by
hand.** `mathfmt.py` typesets Chemistry on export. Write `1.2 x 10^-3`,
`[H3O+]`, `Ka = 4.5 x 10^-5`, `DeltaH`, `1/2`. Do not write `\frac` or `\(`
yourself. Chemical formulas stay as ordinary text: `H2SO4`, `Fe2O3`.

## Figures

These courses lean on graphs and apparatus diagrams and **the bank cannot
carry images**. So:

- Never write a stem that says "the graph shows" or "in the diagram" with
  nothing behind it. That is the defect this project has already shipped once.
- Put the data in a `table=` instead, and ask the question of the table.
- If a question genuinely cannot be asked without a picture, it is not a
  question you can write here. Choose a different one.

## Real exam style

- Five choices, A–E.
- Every distractor must be a claim a prepared student could believe — a
  misapplied rule, a swapped variable, the right idea about the wrong
  structure. Never filler.
- Lean on the CED's own science practices: identify, explain, represent,
  analyse data, justify a claim with evidence.
- Quantitative items should be answerable without a calculator, in one or two
  steps.

## Mechanics

- `TOPIC = ("1.3", "Exact CED Title", 1)` — code, **verbatim** title from
  `<SUBJECT>_topics.json`, unit.
- `QUESTIONS = [dict(q=..., choices=[...], ans=<0-based>, why=...), ...]`
- **30 questions per topic**, exactly.
- Optional `table=dict(headers=[...], rows=[[...]])`.
- Do not hand-balance the key; `export_units.py` redistributes A–E
  deterministically.
- One passing `verify_<module>.py` per module, with one anchor per question
  pinned to a distinctive substring of that question's own keyed choice. The
  exporter reshuffles choices, so a key stored as a bare index is one edit away
  from pointing at a distractor.

## The failure modes this project has already paid for

- **Run a negative control on every check you write.** Corrupt a key or a
  figure on purpose and confirm the check fails. A checker that cannot fail is
  worse than none — it has cost this project five separate times, most recently
  a topic extractor that returned zero topics and reported success.
- **A checker that under-matches is worse than none.** Explicit lookarounds,
  never `\b` beside a digit or a letter run.
- **Agents converge.** Keep to your assigned units, and grep the subject's
  existing modules for your key phrases before writing something obvious — it
  occurred to a sibling too.
- **Commit after EVERY topic**, never at the end:
  `git add content-pool/ap-banks && git commit -m "AP Biology 3.2 <title>: 30 questions + verifier" && git push -u origin claude/new-session-3w59v3`
  Stage that path, never `git add -A`; `-A` sweeps up app-code edits in
  progress at the repo root. Pull and retry if a push is rejected — siblings
  share the branch.
- **A stopped agent leaves damage, not just absence.** If you resume, import
  every module you did not personally finish, count its questions, and run its
  verifier before trusting it.
