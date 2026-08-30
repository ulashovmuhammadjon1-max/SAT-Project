# AP question banks — authored source

These Python modules are the source of truth for every AP question in the
`ApQuestion` table. They live here, not in a scratchpad, because a Claude Code
container is ephemeral and this repository is the only memory that survives.

## Layout

One module per CED topic. Each defines:

```python
TOPIC = ("3.2", "Short-Run Production Costs", 3)   # code, title, unit number
QUESTIONS = [dict(q=..., choices=[...], ans=<index>, why=..., table=<optional>), ...]
```

| files | subject | unit | topics |
|---|---|---|---|
| `t11.py`–`t16.py` | MICRO | 1 | 1.1–1.6 |
| `u2_1.py`–`u2_9.py` | MICRO | 2 | 2.1–2.9 |
| `u3_1.py`–`u3_7.py` | MICRO | 3 | 3.1–3.7 |

Exactly 50 questions per topic.

## Building and inserting

```bash
python3 export_units.py u3_1 u3_2 u3_3 u3_4 u3_5 u3_6 u3_7 --out micro_unit3.json
PROD_URL='postgresql://...' node ../../scripts/insert-ap-questions.mjs micro_unit3.json
```

`export_units.py` is the gate, and it refuses to produce a file rather than
letting a defect reach the inserter. It requires exactly fifty questions per
topic, four or five *distinct* choices (five for economics, four for calculus),
and an in-range answer key; it warns on a repeated stem. That warning is how a
question keyed to the wrong side of a tax-incidence argument was caught in Unit 2
and cut rather than shipped — so read the warnings, don't just watch the exit code.

The inserter derives each row's id from `(subject, topic, order)`, so re-running
it updates rows in place instead of duplicating them. Editing a module and
re-exporting is therefore the correct way to fix a live question.

## NEVER read `QUESTIONS` directly — the shuffle is load-bearing

The `ans` index in a module file is **not** the index a student should see. Keys
are written wherever was convenient while authoring, and they cluster hard: one
Calculus module has 20 of its 25 keys at index 0, one economics module has 38 of
50 at index 1. `export_units.py` is what disperses them.

So any code that consumes a module — a PDF builder, a preview tool, a new
inserter — **must go through the exporter**, or it will emit a bank whose answer
is the first choice four times out of five. Nothing currently bypasses it; this
is written down so nothing starts to.

## Answer keys are shuffled at export, not written balanced

Hand-authored banks cluster hard on one letter — Unit 1's raw distribution was
A11/B186/C84/D16/E3. `export_units.py` applies a per-topic deterministic shuffle
(seeded from the topic code) so the key spreads across A–E while the export stays
reproducible. A choice list that is a **numeric ladder** is left in its written
order, because a student reasonably expects ascending values and shuffling them
reads as a typo. Keep numeric choices sorted when authoring; the exporter will
respect that.

## Tables

A question needing data carries `table=dict(headers=[...], rows=[[...]])`, and the
runner renders it above the stem. Every table's arithmetic is verified in a
comment at the top of its module — the marginal, average, and total columns are
worked out there so a reviewer can check the key without recomputing the table.

## Typesetting: `mathfmt.py`

The modules are written in the plain-text notation the briefs specify
(`x^2`, `1/2`, `int from 0 to 4 of f(x) dx`). `export_units.py` runs every
string through `mathfmt.convert` on the way out, which parses that notation and
emits KaTeX, so students see real exponents, stacked fractions, integral signs
and Greek letters. The modules themselves stay plain: that is what the 167
`verify_*.py` files assert against and what a human edits.

CLAUDE.md's rule is "never bulk auto-convert Math text to LaTeX", written about
the regex converters that caused every Test 3/4 defect. This one is different
in kind and is gated twice, which is the only reason it is allowed to run:

- **Round trip.** The parse tree is rendered back to plain text and compared to
  the source fragment. A mismatch of one character and the fragment is left
  alone. A conversion can therefore only re-typeset a string, never change what
  it says.
- **KaTeX.** `check_katex.mjs` parses every emitted span with KaTeX itself, at
  `throwOnError: true` — production renders with `throwOnError: false`, which
  would silently show a broken span as red source text instead of failing.

Both checks carry their own positive AND negative controls, because a checker
that has never rejected anything is indistinguishable from one wired to
nothing. `test_mathfmt.py` has 46 positive controls, 38 negative controls
(prose that must come back byte-identical), and a gate control that corrupts
the renderer on purpose and asserts the round trip catches it.

Run it as:

    python3 test_mathfmt.py                  # must be 0 failing
    python3 export_units.py <modules> --subject CALC_BC --out bank.json
    node check_katex.mjs <spans.json>

Current state over all 167 Calculus and Statistics modules: 29,104 strings,
13,497 typeset, 20,541 spans, **0 round-trip rejections and 0 KaTeX failures**.

### It is scoped to Calculus and Statistics on purpose

Do **not** run it over the Microeconomics, Macroeconomics or Psychology banks.
Measured on those 109 modules it damages 557 strings: thousands separators
split into fractions (`300/6,000`), `$50 a year` read as `$50a`, CED reference
codes mangled (`EK 3.5.A.1`), and "an infinity of ideas" turned into `∞`. Those
banks are prose with numbers in it, not mathematics, and the notation the
converter is built to read is not what they are written in.

### To re-apply to the live database

Converting the LIVE rows, not re-exporting the modules, is deliberate:
re-exporting re-runs the choice shuffle, and `ApQuestionAttempt` stores the
index a student selected, so a moved choice silently rewrites history.

    PROD_URL=... node scripts/ap-latex-dump.mjs dump.json CALC_AB CALC_BC STATISTICS
    python3 convert_db_rows.py dump.json patch.json
    node check_katex.mjs patch.json.spans.json
    PROD_URL=... node scripts/ap-latex-apply.mjs patch.json          # dry run
    PROD_URL=... node scripts/ap-latex-apply.mjs patch.json --apply
