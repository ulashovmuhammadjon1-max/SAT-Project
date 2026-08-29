# AP Macroeconomics topic-fit audit — pass A

Independent read of all 42 Macro modules (m1_1–m6_6), 2,100 questions, judged against the
official CED topic titles in `src/lib/ap/courses.ts` (`MACRO_UNITS`). Every question in every
module was read; the regex pre-screen at `/tmp/macro_cand.txt` was consulted only afterwards,
as a cross-check.

The test applied: **would a student who had studied only this topic be unable to answer, because
the question's central demand is another topic's content?** Vocabulary borrowed from a
neighbouring topic is not a defect; a question whose whole task is the neighbour's task is.

Findings: **9 MISFILED**, **29 UNSURE**. 0.4% of the bank is judged misfiled — the bank is in
good shape, and the defects cluster in identifiable seams rather than being scattered.

## Findings

| module | q# | stem (first 80 chars) | current topic | correct topic | verdict |
|---|---|---|---|---|---|
| m1_1 | q40 | The circular flow model shows that households | 1.1 Scarcity | 2.1 The Circular Flow and GDP | MISFILED |
| m1_1 | q41 | In the circular flow model, firms | 1.1 Scarcity | 2.1 The Circular Flow and GDP | MISFILED |
| m1_4 | q43 | An increase in demand accompanied by no change in supply will, in a competitive | 1.4 Demand | 1.6 Market Equilibrium | UNSURE |
| m1_4 | q44 | A decrease in demand with supply unchanged will | 1.4 Demand | 1.6 Market Equilibrium | UNSURE |
| m1_5 | q33 | An increase in supply with demand unchanged will, in a competitive market, | 1.5 Supply | 1.6 Market Equilibrium | UNSURE |
| m1_5 | q34 | A decrease in supply with demand unchanged will | 1.5 Supply | 1.6 Market Equilibrium | UNSURE |
| m2_4 | q42 | If the GDP deflator is 125 and nominal GDP is $15 trillion, real GDP equals | 2.4 Price Indices and Inflation | 2.6 Real vs. Nominal GDP | UNSURE |
| m2_5 | q11 | The Fisher equation states, approximately, that | 2.5 Costs of Inflation | 4.2 Nominal vs. Real Interest Rates | UNSURE |
| m2_5 | q12 | If the nominal interest rate is 8% and inflation is 3%, the real interest rate i | 2.5 Costs of Inflation | 4.2 Nominal vs. Real Interest Rates | UNSURE |
| m2_6 | q43 | An economy's real GDP is $900 billion and potential (full-employment) real GDP i | 2.6 Real vs. Nominal GDP | 2.7 Business Cycles | MISFILED |
| m2_7 | q39 | Automatic stabilizers such as progressive income taxes and unemployment benefits | 2.7 Business Cycles | 3.9 Automatic Stabilizers | UNSURE |
| m2_7 | q44 | A negative supply shock, such as a sharp rise in oil prices, tends to produce | 2.7 Business Cycles | 3.3 SRAS / 3.6 Short-Run Changes | UNSURE |
| m3_5 | q20 | An economy at short-run equilibrium with output above potential will experience | 3.5 Equilibrium in AD-AS | 3.7 Long-Run Self-Adjustment | UNSURE |
| m3_5 | q21 | An economy at short-run equilibrium with output below potential will experience | 3.5 Equilibrium in AD-AS | 3.7 Long-Run Self-Adjustment | UNSURE |
| m3_5 | q35 | Suppose AD and SRAS intersect to the right of LRAS. Over time, without policy, t | 3.5 Equilibrium in AD-AS | 3.7 Long-Run Self-Adjustment | MISFILED |
| m3_5 | q36 | Suppose AD and SRAS intersect to the left of LRAS. Over time, without policy, th | 3.5 Equilibrium in AD-AS | 3.7 Long-Run Self-Adjustment | MISFILED |
| m3_8 | q28 | A budget deficit occurs when | 3.8 Fiscal Policy | 5.4 Deficits and the National Debt | UNSURE |
| m3_8 | q29 | The national debt is best described as | 3.8 Fiscal Policy | 5.4 Deficits and the National Debt | UNSURE |
| m3_8 | q31 | Crowding out refers to the possibility that | 3.8 Fiscal Policy | 5.5 Crowding Out | UNSURE |
| m3_8 | q49 | If a fiscal stimulus raises interest rates enough to reduce private investment b | 3.8 Fiscal Policy | 5.5 Crowding Out | UNSURE |
| m5_1 | q12 | With a marginal propensity to consume of 0.8, the spending multiplier is | 5.1 Policy Actions in the Short Run | 3.2 Multipliers | UNSURE |
| m5_1 | q29 | Automatic stabilizers refer to | 5.1 Policy Actions in the Short Run | 3.9 Automatic Stabilizers | MISFILED |
| m5_1 | q30 | During a recession, automatic stabilizers | 5.1 Policy Actions in the Short Run | 3.9 Automatic Stabilizers | MISFILED |
| m5_3 | q33 | If the real interest rate is 3 percent and expected inflation is 6 percent, the | 5.3 Money Growth and Inflation | 4.2 Nominal vs. Real Interest Rates | UNSURE |
| m5_3 | q34 | If the nominal interest rate is 7 percent and inflation turns out to be 4 percen | 5.3 Money Growth and Inflation | 4.2 Nominal vs. Real Interest Rates | UNSURE |
| m5_3 | q37 | Shoe-leather costs of inflation refer to | 5.3 Money Growth and Inflation | 2.5 Costs of Inflation | MISFILED |
| m5_3 | q38 | Menu costs of inflation are | 5.3 Money Growth and Inflation | 2.5 Costs of Inflation | MISFILED |
| m5_3 | q39 | Unexpected inflation redistributes wealth from | 5.3 Money Growth and Inflation | 2.5 Costs of Inflation | UNSURE |
| m5_3 | q40 | Unexpected deflation redistributes wealth from | 5.3 Money Growth and Inflation | 2.5 Costs of Inflation | UNSURE |
| m6_3 | q34 | Central bank intervention to weaken its own currency involves | 6.3 The Foreign Exchange Market | 6.4 Policy in the FX Market | UNSURE |
| m6_3 | q35 | Central bank intervention to strengthen its own currency involves | 6.3 The Foreign Exchange Market | 6.4 Policy in the FX Market | UNSURE |
| m6_3 | q42 | A country pegs its currency above the market equilibrium value. To defend the pe | 6.3 The Foreign Exchange Market | 6.4 Policy in the FX Market | UNSURE |
| m6_3 | q43 | A country pegs its currency below the market equilibrium value. Over time its ce | 6.3 The Foreign Exchange Market | 6.4 Policy in the FX Market | UNSURE |
| m6_6 | q2 | If the nominal interest rate is 7 percent and inflation is 3 percent, the real i | 6.6 Real Rates and Capital Flows | 4.2 Nominal vs. Real Interest Rates | UNSURE |
| m6_6 | q3 | If the nominal interest rate is 5 percent and inflation is 6 percent, the real i | 6.6 Real Rates and Capital Flows | 4.2 Nominal vs. Real Interest Rates | UNSURE |
| m6_6 | q4 | If the nominal interest rate is 9 percent and inflation is 2 percent, the real i | 6.6 Real Rates and Capital Flows | 4.2 Nominal vs. Real Interest Rates | UNSURE |
| m6_6 | q5 | A lender who wants a real return of 4 percent and expects 5 percent inflation sh | 6.6 Real Rates and Capital Flows | 4.2 Nominal vs. Real Interest Rates | UNSURE |
| m6_6 | q18 | Crowding out occurs when government borrowing raises the real interest rate and | 6.6 Real Rates and Capital Flows | 5.5 Crowding Out | UNSURE |

## Notes on the individual MISFILED calls

- **m1_1 q40, q41.** The circular flow model is the *name* of topic 2.1 and appears nowhere in
  the CED's 1.1 (Scarcity: unlimited wants, limited resources, factors of production, the three
  economic questions). Decisive evidence: m2_1 q6 and q7 are near-verbatim twins of these two
  ("In the circular flow model, households… supply factors of production… and buy goods";
  "…firms buy resources in the factor market and sell goods and services in the product market").
  A student practising Scarcity has not met resource markets or product markets yet.
- **m2_6 q43.** Nothing in the item turns on real versus nominal measurement. Given actual and
  potential real GDP, the task is to name a recessionary output gap — the definitional content of
  2.7, where m2_7 q14/q16/q18 already ask exactly this.
- **m3_5 q35, q36.** These trace the whole self-correction path (wages rise → SRAS shifts left →
  output returns to potential at a higher price level). That is 3.7's learning objective verbatim;
  m3_7 q22 and q23 are the same question. 3.5 asks a student to *identify* an equilibrium and a
  gap, not to run the adjustment forward.
- **m5_1 q29, q30.** q29 is a bare definition of automatic stabilizers, near-identical to m3_9 q1;
  q30 is the recession mechanics, near-identical to m3_9 q36. Neither involves the combined
  fiscal/monetary short-run policy analysis that 5.1 exists to test.
- **m5_3 q37, q38.** Bare definitions of shoe-leather and menu costs, near-identical to m2_5 q2 and
  m2_5 q1. Money growth is not part of either question; they are pure 2.5 items.

## Patterns

**1. Duplicate-and-drift is the dominant mechanism.** Almost every MISFILED item has a
near-verbatim twin sitting in its correct home module (m1_1 q40/q41 ↔ m2_1 q6/q7; m5_1 q29/q30 ↔
m3_9 q1/q36; m5_3 q37/q38 ↔ m2_5 q1/q2; m3_5 q35/q36 ↔ m3_7 q22/q23). The generator appears to
have re-derived shared background material inside each module that touches it, rather than the
misfiles being random. Checking for cross-module near-duplicates would find most of these
mechanically, and would find them more reliably than any keyword screen.

**2. The four "real interest rate arithmetic" clusters.** The identical computation
(real = nominal − inflation) appears as bare arithmetic in four topics: 4.2 (its home, ~15
questions), 2.5 (q11–q14), 5.3 (q33–q34) and 6.6 (q2–q5). Only in 4.2 is the arithmetic the point.
Elsewhere it is scaffolding — defensible where the surrounding items use the result (2.5's
borrower/lender redistribution, 5.3's Fisher-effect discussion, 6.6's capital flows), which is why
all of them are UNSURE rather than MISFILED. But a bank owner may want to cut the pure-arithmetic
duplicates and keep only the versions that carry the host topic's content (e.g. m6_6 q38/q39,
which combine the arithmetic with a capital-flow conclusion, are properly 6.6).

**3. Crowding out and deficit/debt vocabulary is spread across four topics.** 4.7, 5.5 and 6.6 all
carry crowding-out questions, and 3.8 carries three. In 4.7 and 6.6 this is correct: the CED
analyses crowding out *in* the loanable funds market and *through* capital flows. In 3.8 the
definitional items (q31, q49) and the deficit/debt definitions (q28, q29, exact twins of m5_4 q1
and q2) are the weakest fits. None rise to MISFILED because 3.8 legitimately covers the limits and
financing of fiscal policy.

**4. Unit 4 — the flagged danger zone — is clean.** All seven Unit 4 modules read as correctly
filed, including the 4.5/4.7 boundary the brief warned about. Both modules are internally
consistent and *explicitly* reinforce the distinction: m4_5 q1 and q49, and m4_7 q1, q19 and q28,
all state that the money market determines the nominal rate and loanable funds the real rate. No
question in 4.5 asks about saving-and-borrowing equilibrium and no question in 4.7 asks about
money supply/money demand equilibrium. The money-multiplier items in 4.6 (q23–q25) are about the
size of an open market operation's effect, which is monetary-policy content, not a 4.4 leak.

**5. The seams that produce UNSURE, not MISFILED, questions.** 1.4/1.5 each close with two items
on the equilibrium consequences of a demand or supply shift (1.6 content), and 6.3 carries four
central-bank-intervention items (6.4 content, with m6_4 q14/q15 as near-twins). These are the
kind of "one step past the topic" endings that read as reasonable extension in a practice set but
would be better placed one topic later.

**6. Where the regex pre-screen agreed and where it did not.** It independently flagged the 5.3
and 6.6 real-rate clusters, m5_3 q38/q40 → 2.5, and m6_2 q34 → 6.4, which corroborates findings 2
and 3. It missed every one of the nine MISFILED items except by accident, and it produced large
blocks of false positives from shared vocabulary alone — e.g. all of 2.2 q2–q50 "reads as 2.1"
(the Limitations-of-GDP module necessarily says "GDP" in every stem), 1.2 and 1.3 "reads as 1.1"
(opportunity cost), and 5.2 q21–q32 "reads as 2.3" (the Phillips curve necessarily says
"unemployment"). A vocabulary screen cannot distinguish a topic's own subject matter from an
intrusion, which is the same lesson recorded in CLAUDE.md about over-matching checkers.

## Clean modules (no findings)

Stated explicitly, module by module:

- **Unit 1:** m1_2 (1.2 Opportunity Cost and the PPC), m1_3 (1.3 Comparative Advantage),
  m1_6 (1.6 Market Equilibrium) — clean. m1_1, m1_4, m1_5 carry the findings above.
- **Unit 2:** m2_1 (2.1 Circular Flow and GDP), m2_2 (2.2 Limitations of GDP),
  m2_3 (2.3 Unemployment) — clean. m2_4, m2_5, m2_6, m2_7 carry findings.
- **Unit 3:** m3_1 (3.1 AD), m3_2 (3.2 Multipliers), m3_3 (3.3 SRAS), m3_4 (3.4 LRAS),
  m3_6 (3.6 Short-Run Changes), m3_7 (3.7 Self-Adjustment), m3_9 (3.9 Automatic Stabilizers) —
  clean. Only m3_5 and m3_8 carry findings.
- **Unit 4: entirely clean.** m4_1, m4_2, m4_3, m4_4, m4_5, m4_6, m4_7 — no misfiled or unsure
  questions found in any of the seven modules.
- **Unit 5:** m5_2 (5.2 Phillips Curve), m5_4 (5.4 Deficits and Debt), m5_5 (5.5 Crowding Out),
  m5_6 (5.6 Economic Growth), m5_7 (5.7 Public Policy and Growth) — clean. m5_1 and m5_3 carry
  findings.
- **Unit 6:** m6_1 (6.1 Balance of Payments), m6_2 (6.2 Exchange Rates), m6_4 (6.4 Policy in the
  FX Market), m6_5 (6.5 FX Changes and Net Exports) — clean. m6_3 and m6_6 carry findings.

The 6.2/6.3/6.5 boundary named in the brief held up well: 6.2 keeps to what an exchange rate is
and how to convert with one, 6.3 keeps to the supply-and-demand diagram for a currency, and 6.5
keeps to the net-export and AD consequences. The only leakage across that boundary is the
intervention/peg material in 6.3 noted above, which belongs to 6.4 rather than to 6.2 or 6.5.
