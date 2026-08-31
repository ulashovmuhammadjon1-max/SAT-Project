# Comp Gov: the cross-topic repeats, and why they are structural

The finished COMP_GOV bank is 43 topics x 30 questions = 1,290 items. A
Jaccard scan over (stem + keyed choice) finds 22 cross-topic pairs at 0.60 or
above. This file records which of them are real, what was done, and — the part
that matters for the other two subjects — why rewriting them is not the fix.

Scan: `python3 export_units.py <k modules> --subject COMP_GOV --out cg.json`
then score pairs on the token signature of stem + keyed choice. Read every
pair; the threshold decides what to READ, never what to accept (CLAUDE.md).

## The measurement

| | |
|---|---|
| questions | 1,290 |
| distinct EK statements cited anywhere in the bank | 147 |
| mean questions per EK statement | **11.6** |
| EK statements cited by more than one topic | **79 of 147 (54%)** |

Five topics — 2.4, 4.4, 5.3, 5.6, 5.7 — have only **three** distinct EK
statements between them and their thirty questions. Ten per statement.

And the CED itself shares statements across topics: PAU-1.A.2 is cited from 11
different topics, LEG-1.A.1 from 10, PAU-1.B.1 / PAU-1.D.1 / PAU-2.A.1 /
PAU-3.C.2 / PAU-3.E.1 from 9 each.

## Why rewriting is not the fix

Four replacement angles were drafted for the worst pairs. All four were already
occupied by a different topic:

| intended replacement | already asked at |
|---|---|
| LEG-1.C.1.a, methods of combating corruption | k1_10 q2 |
| LEG-1.C.1.c, responses to mass protest | k1_10 q4 |
| PAU-3.C.2.b, the Supreme Leader appoints HALF the Guardian Council | k2_3 q11 |
| LEG-2.B.2.a, stable regimes and religious radicalism | k3_8 q12 |

That is the measurement showing up as an experience. At 11.6 questions per EK
statement the ordinary angles are spent, so a "fresh" replacement is more
likely than not to collide with something else in the bank — and the
alternative, inventing material the CED does not state, is exactly what
SOCIAL_BRIEF.md forbids. Ten padded questions dodging 1,290 existing ones would
make the bank worse, not better.

**The lever is the per-topic count, not the wording.** `PER_TOPIC["COMP_GOV"]`
is 30. The CED supports roughly 10-15 for the thinner topics. That is a content
decision for the user, not something to change unilaterally with 1,290
questions already authored.

## The pairs, classified

Two different things are living in this list.

**Same question asked twice** — near-identical stems, identical key. Nine
pairs. Indefensible as wording, but see above on why they were not rewritten:

    0.92  1.5 q17 / 2.3 q3     Iran's Supreme Leader's powers
    0.86  1.10 q5 / 3.9 q18    why states limit divisive and violent actors
    0.81  1.10 q26 / 3.8 q17   ethnicity in Nigeria vs Mexico
    0.71  3.1 q15 / 3.7 q15    restrictions on NGOs highlight liberties violations
    0.71  1.3 q11 / 3.7 q4     media restriction in Iran
    0.68  1.4 q28 / 4.2 q12    independent election commissions
    0.65  2.2 q18 / 2.7 q12    five ways legislatures reinforce legitimacy
    0.64  1.3 q21 / 3.7 q12    the authoritarian-democratic scale, asked in reverse
    0.63  2.6 q3 / 4.1 q2      indirect selection of China's NPC
    0.63  1.4 q26 / 4.3 q7     rules easing the transition from one-party dominance

**Same EK, genuinely different ask** — keep. A student practising 3.9
*should* meet LEG-1.C.2; it is part of that topic in the CED:

    0.77  1.6 q9 / 2.5 q18     one asks the means AND the countries, one only the countries
    0.74  1.10 q7 / 3.1 q16    one asks the five purposes, one asks the causal connection
    0.70  1.10 q3 / 3.9 q17    one asks challenges AND countries, one only the countries
    0.73  1.8 q27 / 3.9 q27    the same causal-brake skill on different data

**Not duplicates at all** — eight pairs whose stems share only the house
phrasing of a table question ("According to the same table, the total number
of..."). Different tables, different numbers, different answers. The scan
matches the boilerplate, not the question. Listed so nobody re-flags them:

    4.5 q23 / 5.1 q23, 3.1 q22 / 4.3 q22, 5.6 q26 / 5.7 q26, 1.9 q26 / 5.5 q22,
    1.6 q23 / 3.5 q24, 4.5 q23 / 5.9 q23, 3.6 q22 / 5.6 q26, 2.6 q22 / 4.1 q4

The independent read agreed with the authoring agent on all eight of these
exclusions, and disagreed with it on three of the same-question pairs it did
not report (1.4 q28 / 4.2 q12 at 0.68, 2.2 q18 / 2.7 q12 at 0.65, 2.6 q3 /
4.1 q2 at 0.63). It had scanned at 0.65 and read down to that line; two of the
three sat inside its own threshold. Reading lower catches more, which is the
rule this project already has.

## For HUMAN_GEO and US_GOV

Both are being authored at 30 per topic against CEDs of similar density, so
expect the same shape. Run the same scan before insertion. Do not spend a
session rewriting what it finds until the per-topic count is settled.
