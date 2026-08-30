# AP Comparative Government and Politics — the CURRENT course framework

**Read this before authoring a single AP Comparative Government question.**
Every fact below was taken from the official College Board *Course and Exam
Description* supplied with this project at `ced-source/COMP_GOV_ced.txt.gz`
(a `pdftotext -layout` dump of the PDF) — not from memory and not from a
test-prep site.

The document reads **Effective Fall 2026**, every page footer reads
*AP Comparative Government and Politics Course and Exam Description … V.1 …
© 2026 College Board*. This is the redesigned framework.

---

## The six course countries — the whole content universe

> "the six required course countries (China, Iran, Mexico, Nigeria, Russia, and
> the United Kingdom)" — Unit 1 *Developing Understanding*, repeated verbatim in
> PAU-1.D.1 and in the Practice 2 description of the exam.

**China, Iran, Mexico, Nigeria, Russia, the United Kingdom.** A question about
any other country is off-syllabus, however tempting. The characteristic exam
move is comparison across two of these six — Practice 2 (Country Comparison) is
**25–32% of the multiple-choice section on its own**.

---

## Exam format

The exam is **2 hours 30 minutes**: 55 multiple-choice questions and 4
free-response questions.

| Section | Type | Count | Weight | Timing |
|---|---|---|---|---|
| I | Multiple-choice | 55 | 50% | 60 minutes |
| II | Free-response | 4 | 50% | 90 minutes |
| | Q1 Conceptual Analysis (4 points) | | 11% | 10 min |
| | Q2 Quantitative Analysis (5 points) | | 12.5% | 20 min |
| | Q3 Comparative Analysis (5 points) | | 12.5% | 20 min |
| | Q4 Argument Essay (5 points) | | 14% | 40 min |

### The shape of Section I, which dictates how questions should be written

| Question type | Number | Stimulus |
|---|---|---|
| Quantitative analysis | **three sets**, 2–3 questions per set | one line graph, chart, table, map or infographic per set |
| Text-based analysis | **two sets**, 2–3 questions per set | one secondary-source passage per set |
| Individual multiple-choice | **40–44** | no stimulus |

Two consequences for authoring:
- Data questions are **set-based** and the data is *in* the question. A prose
  description of a chart is not an acceptable substitute — hence the `table=`
  field on every quantitative item in this bank.
- Roughly three quarters of the section is stimulus-free application and
  comparison. That is the default question shape, not definition recall.

### Practice weighting on the multiple-choice section
| Practice | Share of MC |
|---|---|
| 1 Concept Application | 40–55% |
| 2 Country Comparison | 25–32% |
| 3 Data Analysis | 10–16% (**set-based only**) |
| 4 Source Analysis | 9–11% (**set-based only**) |
| 5 Argumentation | **0% — not assessed by MC at all** |

## Unit weighting

| Unit | Title | MC weighting | Class periods |
|---|---|---|---|
| 1 | Political Systems, Regimes, and Governments | 18–27% | ~22/~11 |
| 2 | Political Institutions | 22–33% | ~32/~16 |
| 3 | Political Culture and Participation | 11–18% | ~28/~14 |
| 4 | Party and Electoral Systems and Citizen Organizations | 13–18% | ~18/~9 |
| 5 | Political and Economic Changes and Development | 16–24% | ~20/~10 |

The five big ideas, which spiral across units: **PAU** Power and Authority,
**LEG** Legitimacy and Stability, **DEM** Democratization, **IEF**
Internal/External Forces, **MPA** Methods of Political Analysis.

---

## Where the CED contradicts what general knowledge would assume

These are the traps. Every one of them was found by reading the framework
against what an informed non-reader of the CED would have written.

### 1. The CED's own sample questions have FOUR choices; this bank uses FIVE
All fifteen sample multiple-choice questions printed in the Exam Information
section (pp. 154–159) offer options **(A)–(D)**. `SOCIAL_BRIEF.md` nevertheless
mandates **five choices (A–E)** for all three social-science banks, and
`export_units.py` accepts 4 or 5. This bank follows the brief and writes five.
Recording the discrepancy so nobody "fixes" it in the wrong direction later.

### 2. Only FOUR of the six countries are assigned an executive-legislative type
PAU-3.A.1–3 name **the United Kingdom** as parliamentary, **Mexico and Nigeria**
as presidential, and **Russia** as semi-presidential. **China and Iran are given
no such label anywhere in the framework.** Do not write a question that asks a
student to classify China or Iran as parliamentary/presidential/semi-
presidential — the CED does not support an answer, and the plausible one
("presidential", because both have a president) is wrong on the substance.

### 3. Russia is described three different ways in three different places
- PAU-3.A.3: a **semi-presidential system**.
- PAU-3.E.1e: a "**parliamentary-hybrid system**" (in the legislature list).
- DEM-1.C.5: a "**competitive authoritarian regime or illiberal democracy**",
  holding contested elections with limited competitiveness.

All three are the CED's own words about the same country. A question must be
written so that only one of these framings is at issue, or it becomes
unanswerable. This bank keeps them apart by topic: institutional type in 2.1–2.2,
regime classification in 1.3 and 3.7.

### 4. Federal / unitary does not track democratic / authoritarian
PAU-2.A.1: federal — **Mexico, Nigeria, Russia**; unitary — **China, Iran, the
United Kingdom**. So the unitary group contains the course's clearest democracy
(UK) and its clearest one-party state (China), and the federal group contains
two multiparty republics and a competitive-authoritarian regime. The obvious
"authoritarian states centralise, democracies federalise" generalisation is
directly refuted by the framework's own list.

### 5. The CED calls the National People's Congress the most powerful institution
PAU-3.E.1a: China's constitution "recognizes [the NPC] as the government's most
powerful institution that elects the president, approves the premier, and
legitimizes policies of the executive." PAU-3.F.1a then says the **Politburo
Standing Committee** "is the actual center of power in the Chinese state."
Both sentences are the framework's; the first is a statement about the
*constitution*, the second about *actual* power. Any China legislature question
must make clear which of the two it is asking about.

### 6. The Federation Council and the House of Lords are both "appointed"
PAU-3.E.1e calls Russia's Federation Council **appointed** (approving budget
legislation, treaties, judicial nominees, troop deployment); PAU-3.E.1f calls
the UK's House of Lords **appointed** (reviewing and amending Commons bills,
"effectively delaying implementation as a power check"). Real-world nuance about
how Federation Council members are actually designated is outside the framework
and must not be asserted.

### 7. Term limits: only two are stated, and they differ
- **Mexico's president is restricted to one term** (PAU-3.C.2c).
- **Iran's president is elected for up to two 4-year terms** (PAU-3.C.2b).
No term-limit figure is given for China, Nigeria, Russia or the UK. The CED
mentions China's 2018 removal of presidential term limits only in an *optional
sample instructional activity* (Unit 2, Activity 2), not in any essential
knowledge statement. This bank does not key a question to it.

### 8. Iran's Supreme Leader appoints *half* of the Guardian Council
PAU-3.C.2b: the Supreme Leader "appoints top ministers, the Expediency Council,
half of the Guardian Council, and the head of the judiciary." PAU-3.G.1b: the
head of the judiciary "can nominate half of the Guardian Council with approval
by the Majles." Half, twice — not the whole body.

### 9. Mexico's Supreme Court term is a stated number: 15 years
PAU-3.G.1d: magistrates "nominated by the president and approved by the Senate
for a term of 15 years." One of very few precise numbers in Units 1–3; the
others are Iran's two 4-year presidential terms, China's "at least 55 recognized
ethnic minorities", Nigeria's "more than 250 ethnic groups", and Russia's
ethnic Russians at "more than 80 percent of the population."

### 10. The named data sources are a closed list
MPA-1.A.8 names exactly seven: **Human Development Index; GDP and GDP per
capita; GDP growth rate; Gini index (coefficient); Freedom House; Transparency
International; Failed States Index.** The sample question keys HDI as the best
measure of living standards over GDP per capita. Note the CED says *Failed*
States Index, not *Fragile* States Index — use the framework's name.

### 11. "Democratic regimes can maintain sovereignty using *less* power"
PAU-1.D.2 makes this a positive claim of the framework, not a value judgement to
be hedged. Similarly PAU-3.B.1: parliamentary systems have **fewer**
institutional obstacles to enacting policy than presidential systems — but "have
their own checks on the executive branch", which is the half students drop.

### 12. Devolution is explicitly two-sided
LEG-1.B.4 lists benefits (policy innovation, matching policy to local needs,
checking central power, better minority representation) **and** costs
(contradictory policies, inefficient implementation, interregional inequality,
competition for resources, exacerbated ethnic and local tensions) in the same
statement. A question that treats devolution as unambiguously good or bad
contradicts the framework.

### 13. Restrictions on participation are NOT exclusive to authoritarian regimes
DEM-1.B.3: **both** authoritarian and democratic regimes regulate formal
participation and disallow disruptive and violent protest; authoritarian regimes
simply do so "to a much greater extent." Likewise DEM-1.C.2: **both** constrain
media. The sample question set (Q7) is built precisely on this — three of its
four distractors are "only authoritarian regimes…" statements.

### 14. Separatist movements: five countries, not the two you would guess
LEG-2.B.4a: separatist movements have emerged in **China, Iran, Nigeria, Russia,
and the United Kingdom**. LEG-2.B.4b: groups demanding **autonomy but not
independence** have emerged in **Mexico and the United Kingdom**. The UK is on
both lists; Mexico is on the second only.

### 15. Unit 4 has six topics, not nine
Topic counts per unit are **10 / 9 / 9 / 6 / 9 = 43**. Unit 4 is the short one.

---

## Topic list

Verbatim CED titles for all 43 topics live in `COMP_GOV_topics.json`, keyed by
code, with unit titles under `"_units"`.
