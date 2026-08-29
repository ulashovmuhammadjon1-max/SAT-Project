# AP Macroeconomics topic-fit audit — pass B (independent second reader)

All 42 modules (`m1_1`–`m6_6`, 2,100 questions) were read in full against the CED
topic titles in `src/lib/ap/courses.ts`. Method: for each topic, state what its CED
title covers and what a student who had studied *only up to that topic* would know,
then ask of every one of its 50 questions whether that student could answer it.
Building on **earlier** topics was treated as correct and expected; shared vocabulary
was never treated as a misfile. Only the **central demand** of a question counts.

`MISFILED` = the question's central demand belongs to another topic, and in almost
every case that topic comes **later** in the course. `UNSURE` = the question leans on
later machinery but is defensible where it sits; flagged for a human, not an accusation.

---

## Findings

| module | q# | stem (first 80 chars) | current topic | correct topic | verdict |
|---|---|---|---|---|---|
| m1_1 | 40 | The circular flow model shows that households | 1.1 Scarcity | 2.1 The Circular Flow and GDP | MISFILED |
| m1_1 | 41 | In the circular flow model, firms | 1.1 Scarcity | 2.1 The Circular Flow and GDP | MISFILED |
| m1_4 | 43 | An increase in demand accompanied by no change in supply will, in a competitive | 1.4 Demand | 1.6 Market Equilibrium | MISFILED |
| m1_4 | 44 | A decrease in demand with supply unchanged will | 1.4 Demand | 1.6 Market Equilibrium | MISFILED |
| m1_5 | 33 | An increase in supply with demand unchanged will, in a competitive market, | 1.5 Supply | 1.6 Market Equilibrium | MISFILED |
| m1_5 | 34 | A decrease in supply with demand unchanged will | 1.5 Supply | 1.6 Market Equilibrium | MISFILED |
| m1_5 | 38 | A fall in the price of oil, an input for plastics manufacturers, will in the pla | 1.5 Supply | 1.6 Market Equilibrium | UNSURE |
| m1_5 | 28 | A perfectly inelastic supply curve is | 1.5 Supply | (elasticity — not in the Macro CED) | UNSURE |
| m1_5 | 41 | Supply tends to be more elastic in the long run than in the short run because | 1.5 Supply | (elasticity — not in the Macro CED) | UNSURE |
| m2_3 | 22 | If the actual unemployment rate is below the natural rate, the economy is most l | 2.3 Unemployment | 2.7 Business Cycles / 3.5 | UNSURE |
| m2_3 | 33 | Which policy would most directly reduce cyclical unemployment? | 2.3 Unemployment | 3.8 Fiscal Policy / 4.6 Monetary Policy | UNSURE |
| m2_5 | 11 | The Fisher equation states, approximately, that | 2.5 Costs of Inflation | 4.2 Nominal vs. Real Interest Rates | UNSURE |
| m2_5 | 12 | If the nominal interest rate is 8% and inflation is 3%, the real interest rate i | 2.5 Costs of Inflation | 4.2 Nominal vs. Real Interest Rates | UNSURE |
| m2_5 | 13 | If the nominal interest rate is 6% and inflation turns out to be 9%, the realize | 2.5 Costs of Inflation | 4.2 Nominal vs. Real Interest Rates | UNSURE |
| m2_5 | 27 | With a nominal interest rate near zero and deflation of 2%, the real interest ra | 2.5 Costs of Inflation | 4.2 Nominal vs. Real Interest Rates | UNSURE |
| m2_5 | 28 | Because nominal interest rates cannot fall far below zero, deflation makes monet | 2.5 Costs of Inflation | 4.6 Monetary Policy | UNSURE |
| m2_6 | 43 | An economy's real GDP is $900 billion and potential (full-employment) real GDP i | 2.6 Real vs. Nominal GDP | 2.7 Business Cycles | MISFILED |
| m2_7 | 37 | An economy at a business cycle peak with an inflationary gap would most likely c | 2.7 Business Cycles | 3.8 Fiscal Policy / 4.6 | UNSURE |
| m2_7 | 38 | An economy in a deep recessionary gap would most likely call for | 2.7 Business Cycles | 3.8 Fiscal Policy / 4.6 | UNSURE |
| m2_7 | 39 | Automatic stabilizers such as progressive income taxes and unemployment benefits | 2.7 Business Cycles | 3.9 Automatic Stabilizers | MISFILED |
| m2_7 | 43 | Stagflation describes the unusual combination of | 2.7 Business Cycles | 3.6 Changes in AD-AS in the Short Run | UNSURE |
| m2_7 | 44 | A negative supply shock, such as a sharp rise in oil prices, tends to produce | 2.7 Business Cycles | 3.3 SRAS / 3.6 | UNSURE |
| m2_7 | 47 | Which of the following would tend to reduce the amplitude of business cycles? | 2.7 Business Cycles | 3.9 Automatic Stabilizers / 4.6 | UNSURE |
| m3_7 | 45 | Self-adjustment implies that the long-run Phillips curve relationship is | 3.7 Long-Run Self-Adjustment | 5.2 The Phillips Curve | MISFILED |
| m3_7 | 39 | The long-run neutrality of money is an application of self-adjustment because | 3.7 Long-Run Self-Adjustment | 5.3 Money Growth and Inflation / 4.6 | UNSURE |
| m3_8 | 31 | Crowding out refers to the possibility that | 3.8 Fiscal Policy | 5.5 Crowding Out (needs 4.7) | MISFILED |
| m3_8 | 49 | If a fiscal stimulus raises interest rates enough to reduce private investment b | 3.8 Fiscal Policy | 5.5 Crowding Out (needs 4.7) | MISFILED |
| m3_8 | 32 | Crowding out makes expansionary fiscal policy | 3.8 Fiscal Policy | 5.5 Crowding Out | UNSURE |
| m3_8 | 41 | Which of the following would make fiscal stimulus less effective? | 3.8 Fiscal Policy | 5.5 Crowding Out | UNSURE |
| m3_8 | 43 | Supply-side fiscal policies aim to | 3.8 Fiscal Policy | 5.7 Public Policy and Economic Growth | UNSURE |
| m4_5 | 38 | In the short run, an expansionary monetary policy will most likely | 4.5 The Money Market | 4.6 Monetary Policy | UNSURE |
| m4_6 | 36 | Expansionary monetary policy affects net exports because a lower domestic intere | 4.6 Monetary Policy | 6.4 Policy in the FX Market / 6.5 | MISFILED |
| m4_6 | 37 | Contractionary monetary policy tends to affect the exchange rate by | 4.6 Monetary Policy | 6.4 Policy in the FX Market | MISFILED |
| m4_6 | 45 | Monetary policy influences aggregate demand mainly through | 4.6 Monetary Policy | 6.5 (exchange-rate channel named) | UNSURE |
| m4_7 | 13 | The long-run consequence of persistent crowding out is | 4.7 The Loanable Funds Market | 5.5 Crowding Out / 5.6 | UNSURE |
| m5_1 | 41 | Expansionary monetary policy affects net exports because a lower domestic intere | 5.1 Policy Actions in the Short Run | 6.4 / 6.5 | MISFILED |
| m5_1 | 42 | Expansionary fiscal policy that raises the real interest rate tends to | 5.1 Policy Actions in the Short Run | 6.4 / 6.5 | MISFILED |
| m5_5 | 24 | An inflow of foreign financial capital caused by higher domestic interest rates | 5.5 Crowding Out | 6.3 The Foreign Exchange Market | MISFILED |
| m5_5 | 25 | An appreciation of the domestic currency caused by government borrowing will | 5.5 Crowding Out | 6.5 Changes in the FX Market and Net Exports | MISFILED |
| m5_5 | 23 | If government borrowing raises the domestic real interest rate, financial capita | 5.5 Crowding Out | 6.6 Real Interest Rates and Capital Flows | UNSURE |
| m5_5 | 26 | The reduction in net exports caused by a deficit-driven currency appreciation is | 5.5 Crowding Out | 6.5 Changes in the FX Market and Net Exports | UNSURE |
| m5_5 | 27 | Twin deficits refers to the observation that | 5.5 Crowding Out | 6.1 Balance of Payments / 6.6 | UNSURE |

**Totals: 15 MISFILED, 27 UNSURE, out of 2,100 questions (2.0% flagged, 0.7% called misfiled).**

---

## Units and modules that are clean

Read in full and found free of topic-fit defects:

- **Unit 6 is entirely clean** — `m6_1`–`m6_6`. Being the last unit it cannot make a
  forward reference, and every question sits on its own topic; the real-interest-rate
  recap that opens `m6_6` is a legitimate backward reference to 4.2, which 6.6's own
  title requires.
- **Unit 1**: `m1_2` (PPC) and `m1_3` (comparative advantage) are clean. `m1_6` is clean —
  price ceilings and floors belong under "Disequilibrium" in its own title.
- **Unit 2**: `m2_1` (circular flow and GDP), `m2_2` (limitations of GDP) and `m2_4`
  (price indices) are clean. The GDP deflator questions in `m2_4` are correct there —
  2.4's title covers price indices, so the deflator is not a 2.6 intruder.
- **Unit 3**: `m3_1` (AD), `m3_2` (multipliers), `m3_3` (SRAS), `m3_4` (LRAS), `m3_5`
  (equilibrium), `m3_6` (short-run changes) and `m3_9` (automatic stabilizers) are clean.
  The multiplier questions that size a gap-closing fiscal change are correct in 3.2 —
  the gap concept comes from 2.7, which is earlier.
- **Unit 4**: `m4_1` (financial assets), `m4_2` (nominal vs. real rates), `m4_3` (money),
  `m4_4` (banking) are clean. `m4_7` is clean apart from one flagged item; the loanable
  funds treatment of government borrowing belongs there, since 4.7 is where the
  mechanism is drawn.
- **Unit 5**: `m5_2` (Phillips curve), `m5_3` (money growth and inflation), `m5_4`
  (deficits and debt), `m5_6` (economic growth) and `m5_7` (public policy and growth)
  are clean. The menu-cost / shoe-leather questions in `m5_3` reach *back* to 2.5,
  which is allowed.

---

## Patterns

### 1. The dominant defect is the open-economy channel appearing before Unit 6
Nine of the fifteen misfiles, plus five of the UNSURE calls, are one recurring move:
a Unit 4 or Unit 5 question completes the chain *interest rate → capital flow →
exchange rate → net exports*. `m4_6` q36–37, `m5_1` q41–42 and `m5_5` q23–27 all do it.
A student who has reached 4.6 or 5.5 has met the interest rate but has not met the
foreign exchange market, capital flows, or the balance of payments — every one of
those is Unit 6 (6.3, 6.4, 6.5, 6.6). Unit 6's own modules cover this material
thoroughly and correctly (`m6_4` q1–13 is almost a line-for-line better version of
`m4_6` q36–37 and `m5_1` q41–42), so the earlier appearances are redundant as well as
premature. This is the single cluster most worth acting on.

### 2. Crowding out is spread across three topics, and the earliest is the wrong one
5.5 is a whole topic named *Crowding Out*. `m3_8` (q31, q32, q41, q49) introduces it
before either the loanable funds market (4.7) or 5.5 exists for the student, and 4.7
(q10, q13) introduces it again. The 4.7 appearance is defensible — the loanable funds
diagram is where the mechanism is actually drawn — but the 3.8 appearance is not:
it needs a market the student has not seen. `m3_8` q31 and `m5_5` q1 are near-identical
definitional questions in two different units.

### 3. Unit 2 previews Unit 3's whole apparatus
`m2_7` in particular reaches forward repeatedly — automatic stabilizers (a Unit 3
topic by name), stagflation, supply shocks, and "what policy does this gap call for".
`m2_3` q33 does the same. Individually each is answerable by memory; collectively they
mean a student sitting 2.7 as a topic quiz is asked about material from three later
topics. The strongest single case is `m2_7` q39, whose subject is the *title* of 3.9.

### 4. A handful of one-topic-ahead leaks inside a unit
`m1_4` q43–44 and `m1_5` q33–34 ask for equilibrium price-and-quantity outcomes before
1.6; `m2_6` q43 asks the student to identify a recessionary gap in a real-vs-nominal-GDP
topic; `m4_5` q38 asks for monetary policy's real effects one topic before 4.6. These
are the mildest defects here, but they are the same error in kind: the question's
central demand is the *next* topic's.

### 5. Two questions use elasticity, which is not in the Macro CED at all
`m1_5` q28 and q41. Not a misfile to another Macro topic — an out-of-course concept
(it belongs to AP Microeconomics). Flagged as UNSURE for a human to decide.

### 6. Repeated stems mark where duplicated coverage sits
An exact-stem scan across the 42 modules found 8 repeated stems, and the pairs are
diagnostic — in six of the eight the second appearance is the topic actually devoted
to the concept:

    m2_4 q32 = m5_2 q25   "Disinflation refers to"
    m2_5 q2  = m5_3 q37   "Shoe-leather costs of inflation refer to"
    m2_7 q14 = m3_5 q3    "A recessionary gap exists when"
    m2_7 q15 = m3_5 q4    "An inflationary gap exists when"
    m3_8 q2  = m5_1 q1    "Expansionary fiscal policy consists of"
    m3_8 q29 = m5_4 q2    "The national debt is best described as"
    m4_6 q36 = m5_1 q41   "Expansionary monetary policy affects net exports because…"
    m4_7 q10 = m5_5 q1    "Crowding out refers to"

The 2.7/3.5 output-gap pair is legitimate (2.7's CED title covers the business cycle
and potential output). The rest are worth a look, and `m4_6 q36 = m5_1 q41` is a
byte-identical forward reference appearing twice.

---

## One defect found that is not a topic-fit issue

`m3_1` q36 has a **wrong answer key**. The stem is "A decrease in aggregate demand is
best described as"; the keyed choice is *"a higher price level with the same output"*,
while the correct choice — *"less real output demanded at every price level"* — is
present as a distractor and is exactly what the question's own `why` field describes
("A shift means the quantity of real GDP demanded changes at every possible price
level"). This is outside the scope of this audit but should be fixed before the item
reaches a student.

---

## What was deliberately not flagged

- Vocabulary overlap without a shift in central demand (e.g. "aggregate demand"
  appearing in a Unit 2 stem where the question is really about unemployment).
- Backward references of any kind — `m5_3`'s menu costs, `m6_6`'s real-rate arithmetic,
  `m5_7`'s comparative advantage, `m3_4`'s PPC comparison. Building on earlier topics
  is the course working as intended.
- `m3_1` q18/q21 and `m3_6` q28/q44, which describe interest rate changes in words
  without invoking the money market. 3.1's own list of AD determinants includes the
  real interest rate, so no Unit 4 machinery is actually required.
- `m4_7` q17/q18/q41/q42 on capital inflows. They shift loanable funds supply without
  any exchange-rate reasoning, which 4.7 can carry on its own.
