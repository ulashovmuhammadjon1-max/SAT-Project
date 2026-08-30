# Authoring brief: AP Human Geography, US Government, Comparative Government

Read this before writing a single question. It is the spec the three social
science banks are held to, and the verifier you write will be checked against
it.

## The hard part: there is no sympy here

Every Math bank in this project rests on a computational check — the key is
right because `sp.diff` says so. **These three subjects have no such backstop.**
A wrong key in a Government bank is not caught by a machine; it is caught by a
person reading, or it is not caught at all and it teaches a student something
false.

So the discipline is different, and it is stricter:

1. **Every key must be traceable to the CED.** Not to your memory of the
   subject — to a sentence in the Course and Exam Description. The essential
   knowledge statements (`EK 3.5.A.1` and friends) are the citation. Put the
   citation in the module comment for any question whose answer is a matter of
   course content rather than reasoning.
2. **Every question's `why` must state the reason, not restate the answer.**
   "Because it is the correct definition" is not a reason. "Because Article I
   Section 8 enumerates the taxing power to Congress, not the President" is.
3. **If you are not certain, do not ship it.** Cut the question. A 28-question
   topic that is right beats a 30-question topic with two lies in it. Report
   the shortfall rather than padding.

## Real exam style — this is what the user asked for, specifically

Read the sample questions in the CED before writing. Do not write quiz-style
definition recall. The real exams test *application*, and the question shapes
are recognisable:

**AP US Government** (55 MC in 80 min, then 4 FRQ)
- **Quantitative analysis**: a table, chart or map, then "which of the
  following is an accurate conclusion". The data must be in the question.
- **Qualitative source**: a passage from a foundational document, then a
  question about its argument. The nine foundational documents are named in
  the CED — use them, quote them accurately, and never invent a quotation.
- **SCOTUS comparison**: a description of a non-required case, compared with
  one of the fifteen required cases. Get the holding right.
- **Concept application**: a scenario, then which principle it illustrates.

**AP Comparative Government** (55 MC in 60 min, then 4 FRQ)
- The **six course countries** — China, Iran, Mexico, Nigeria, Russia, the
  United Kingdom — are the whole content universe. A question about a country
  outside those six is off-syllabus. Comparison across two of them is the
  characteristic move.
- Country-specific facts must be current to the CED, not to your training
  data. If the CED does not state it, do not assert it.

**AP Human Geography** (60 MC in 60 min, then 3 FRQ)
- Heavy on **models** (von Thünen, Weber, Christaller, Rostow, Wallerstein,
  demographic transition, Burgess/Hoyt/Harris-Ullman) — ask students to apply
  a model, not to name it.
- **Map, chart and image stimulus** questions are a large share. Where a
  question needs data, put a real `table=` on it, the same way the economics
  banks do. Never describe a figure in prose instead of providing it.
- Scale of analysis (local / national / global) is a recurring axis.

## Mechanics, identical to the other banks

- `TOPIC = ("1.3", "Exact CED Title", 1)` — code, verbatim CED title, unit.
- `QUESTIONS = [dict(q=..., choices=[...], ans=<0-based>, why=...), ...]`
- **Five choices** (A–E) for all three subjects, matching the real exams.
- **30 questions per topic**, exactly. The exporter enforces it.
- Optional `table=dict(headers=[...], rows=[[...]])` for stimulus data.
- Write the key first (`ans=0`) if that is natural — `export_units.py`
  redistributes the keys across A–E deterministically, so do not hand-balance.
- One `verify_<module>.py` per module. It cannot check the politics, so it
  checks what it can: 30 questions, five distinct choices each, a valid key, a
  non-empty `why`, no duplicate stems, no choice that is a superset of
  another, and every arithmetic claim in a data question recomputed from the
  `table`.

## Notation

Prose, with real numbers. `mathfmt.py` typesets what needs typesetting on
export — percentages, ratios, `−` signs and data all come out right without
you writing any LaTeX. Do not write LaTeX by hand.

## The failure modes this project has already paid for

- **A checker that under-matches is worse than none.** Use explicit
  lookarounds, never `\b` next to a digit or a letter run.
- **Agents converge.** If you are one of several working in parallel, keep to
  your assigned units and check the shared bank before writing a question you
  think is obvious — it probably occurred to a sibling too.
- **Deduplicate against the whole subject, not just your unit.** A student
  practising a topic sees only that topic, but the Question Bank shows them
  everything.
- **Commit after every topic.** Not at the end. A stopped agent should lose
  one module at most.
