# Repeated questions across the three social science banks

All three subjects were authored at 30 questions per CED topic. Two of them
came out with cross-topic repeats and one did not, and the difference is not
authoring care — it is a property of the CED each was written against.

Scan: export the subject, then score every pair of questions on the Jaccard
similarity of the token signature of **stem + keyed choice**. Read every pair
above the line; the threshold decides what to READ, never what to accept.

## The measurement

| subject | topics | distinct EK statements | questions per EK | EK shared by >1 topic | cross-topic pairs ≥0.60 |
|---|---|---|---|---|---|
| Human Geography | 68 | 149 | 12.8 | **27%** | **1** |
| US Government | 60 | 138 | 10.6 | **48%** | **16** |
| Comparative Government | 43 | 147 | 11.6 | **54%** | **22** |

**Questions-per-EK does not predict duplication — sharing does.** All three sit
between 10.6 and 12.8 questions per statement, but Human Geography produced one
cross-topic pair and Comparative Government twenty-two. What separates them is
the last column: the AP Human Geography CED gives each topic its own material,
while both Government CEDs cross-reference the same statements from many
topics. PAU-1.A.2 is cited from eleven Comp Gov topics; LEG-1.A.1 from ten.

So the rule is not "30 per topic is too many". It is **30 per topic is too many
on a CED whose topics share their statements**, and the two Government courses
are exactly that.

The extreme case is US Government topic 4.7, Ideologies of Political Parties,
which has **one** essential knowledge statement — that Democratic platforms
generally align more closely with liberal positions and Republican with
conservative — for thirty questions. Two more US Gov topics (3.11, 3.12) also
have one apiece; five Comp Gov topics have three.

## What was fixed, and what was not

**Fixed: US Gov 4.7.** It had reached into 4.9 and 4.10 for material, and q14
against 4.10 q3 was byte-identical. Rewritten as what LO 4.7.A actually asks —
how the two parties' ideologies shape policy debates — so each item now CHAINS
EK 4.7.A.1 to the position statement in 4.9 or 4.10. Neither topic can do that
alone: 4.9 and 4.10 name ideologies and no party, 4.7 names parties and no
position. That is a genuinely different question, not a reworded one.

**Not fixed: the rest.** Four replacement angles were drafted for the Comp Gov
pairs and **all four turned out to be already asked by another topic**:

| intended replacement | already asked at |
|---|---|
| LEG-1.C.1.a, methods of combating corruption | k1_10 q2 |
| LEG-1.C.1.c, responses to mass protest | k1_10 q4 |
| PAU-3.C.2.b, the Supreme Leader appoints HALF the Guardian Council | k2_3 q11 |
| LEG-2.B.2.a, stable regimes and religious radicalism | k3_8 q12 |

At this density a "fresh" replacement is more likely to collide than not, and
the alternative — inventing material the CED does not state — is what
SOCIAL_BRIEF.md forbids. Ten padded questions dodging 1,290 existing ones make
the bank worse, not better. **The lever is the per-topic count, and that is the
user's call**, so it has not been changed.

## The pairs that remain

**Comparative Government — same question asked twice (9):**

    0.86  1.10 q5 / 3.9 q18    why states limit divisive and violent actors
    0.81  1.10 q26 / 3.8 q17   ethnicity in Nigeria vs Mexico
    0.71  3.1 q15 / 3.7 q15    restrictions on NGOs highlight liberties violations
    0.71  1.3 q11 / 3.7 q4     media restriction in Iran
    0.68  1.4 q28 / 4.2 q12    independent election commissions
    0.65  2.2 q18 / 2.7 q12    five ways legislatures reinforce legitimacy
    0.64  1.3 q21 / 3.7 q12    the authoritarian-democratic scale, asked in reverse
    0.63  2.6 q3 / 4.1 q2      indirect selection of China's NPC
    0.63  1.4 q26 / 4.3 q7     rules easing the transition from one-party dominance

(1.5 q17 / 2.3 q3, on Iran's Supreme Leader, scored 0.92 and is the tenth.)

**US Government — same question asked twice (3):**

    1.00  5.8 q1 / 5.9 q6      the incumbency advantage phenomenon, byte-identical
    0.84  1.8 q6 / 3.7 q12     Wisconsin v. Yoder, same holding, same key
    0.69  1.7 q13 / 1.9 q16    Shaw v. Reno, same stem, keys worded differently

**Same EK, genuinely different ask — keep.** A student practising Comp Gov 3.9
*should* meet LEG-1.C.2; the CED puts it in that topic:

    0.77  1.6 q9 / 2.5 q18     one asks the means AND the countries, one only the countries
    0.74  1.10 q7 / 3.1 q16    one asks the five purposes, one the causal connection
    0.70  1.10 q3 / 3.9 q17    one asks challenges AND countries, one only the countries
    0.73  1.8 q27 / 3.9 q27    the same causal-brake skill on different data

**Not duplicates at all.** Eight Comp Gov pairs and most of the US Gov and
Human Geography hits share only the house phrasing of a table stem
("According to the same table, the total number of…") or are deliberate
contrast pairs — liberal against conservative, megacity against metacity,
intensive against extensive farming, the 15th Amendment against the 19th.
Different keys, different numbers. The scan is matching the stimulus or the
shared vocabulary of a contrast, not the question. Do not re-flag these.

Human Geography's only cross-topic hit, 5.6 q26 against 5.8 q26, is two
different bid-rent tables with different land uses and different answers.

## If the per-topic count is ever revisited

Reducing it is a content decision with real cost: the questions are already
authored and verified, and cutting to fit would discard work. The cheaper
option is to leave the count and accept that a shared CED statement is tested
from more than one topic angle, which is how the real exam treats them too.
What should NOT happen is another pass rewriting the listed pairs into thinner
corners of the same statements — that trade has been tried and it loses.
