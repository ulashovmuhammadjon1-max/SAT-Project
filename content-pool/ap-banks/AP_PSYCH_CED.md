# AP Psychology — the CURRENT course framework (confirmed, not remembered)

**Read this before authoring a single AP Psychology question.** Everything below
was taken from the official College Board Course and Exam Description PDF,
downloaded and text-extracted in this session — not from memory and not from a
test-prep site.

**Source (confirmed 2026-08-30):**
<https://apcentral.collegeboard.org/media/pdf/ap-psychology-course-and-exam-description.pdf>
Cover reads *Effective Fall 2025*; the inner title page reads *Effective Fall
2024*; every page footer reads *AP Psychology Course and Exam Description …
Course Framework V.1 … © 2024 College Board*. This is the redesigned CED.

Supporting pages:
- Course at a Glance (topic list, cross-checked against the CED):
  <https://apcentral.collegeboard.org/media/pdf/ap-psychology-course-at-a-glance.pdf>
- Revision landing page: <https://apcentral.collegeboard.org/courses/ap-psychology/revisions-2024-25/course>

---

## READ THIS FIRST: two things that are commonly wrong

### 1. There are FIVE units, not nine
The old framework had nine units (Scientific Foundations of Psychology;
Biological Bases of Behavior; Sensation and Perception; Learning; Cognitive
Psychology; Developmental Psychology; Motivation, Emotion, and Personality;
Clinical Psychology; Social Psychology). **That framework is superseded.** If a
source lists "Sensation and Perception", "Learning", or "Clinical Psychology" as
a *top-level unit*, it is describing the pre-2024 course and must not be used.

The old Unit 1, Scientific Foundations of Psychology, no longer exists as a unit
at all. Research methods, experimental design, and data interpretation were
folded into the **science practices**, which are assessed *inside* all five
content units. So research-methods questions are still on the exam — they are
just attached to the content of Units 1–5 rather than sitting in a unit of their
own.

### 2. Multiple-choice questions have FOUR choices (A–D), not five
Confirmed two independent ways:
- College Board's own revision announcement: "The AP Psychology Exam … will have
  fewer multiple-choice questions, and the questions will have **four answer
  choices instead of five**."
- Every sample multiple-choice question printed in the current CED (Exam
  Information, pp. 151+) has exactly options (A), (B), (C), (D).

The five-option (A–E) format is the **pre-redesign** exam. It is also what
`ap-banks`' economics modules use, which makes it an easy assumption to carry in
by accident.

**Therefore every AP Psychology module in this directory is authored with four
choices, A–D.** `export_units.py` accepts 4 or 5, so it will not catch a module
that drifts to five — the consistency has to be maintained by hand. Sibling
agents authoring Units 4 and 5: use four.

---

## Exam format (CED, Exam Information, p. 147)

Total time **2 hours 40 minutes**. The two sections are weighted equally per
question type as below.

| Section | Question type | Number | Weighting | Timing |
|---|---|---|---|---|
| I | Multiple-choice questions | 75 | 66.7% | 90 minutes |
| II | Free-response questions | 2 | 33.3% | 70 minutes |
| | Question 1: Article Analysis Question (AAQ) | 1 | 16.65% | |
| | Question 2: Evidence-Based Question (EBQ) | 1 | 16.65% | |

Section I contains both **set-based and discrete** multiple-choice questions.
Administered digitally.

**AAQ** — students read one provided research article/summary and answer six
parts (A–F): identify the research method; state an operational definition;
describe what a difference in means indicates; identify and describe application
of an ethical guideline; explain the extent of generalizability using evidence
from the study; explain how a finding supports or refutes the hypothesis.

**EBQ** — students read three provided sources and answer three parts: (A)
propose a specific, defensible claim grounded in psychological science; (B)(i)
support it with specific evidence from one source and (ii) explain how that
evidence supports the claim using a psychological perspective/theory/concept/
finding; (C)(i) the same with evidence from a *different* source and (ii) a
*different* psychological concept. Sources must be cited parenthetically or
embedded. Each FRQ is scored out of 7 points.

Both FRQ types are new with the 2025 exam. The old FRQ types (a "concept
application" essay and a "research design" essay) are gone.

## Unit weightings (CED, p. 148)

| Unit | Title | Exam weighting |
|---|---|---|
| 1 | Biological Bases of Behavior | 15–25% |
| 2 | Cognition | 15–25% |
| 3 | Development and Learning | 15–25% |
| 4 | Social Psychology and Personality | 15–25% |
| 5 | Mental and Physical Health | 15–25% |

All five units carry the same published band. There is no lightly-weighted unit.

## Science practices (assessed across all five units)

| Code | Practice |
|---|---|
| 1.A | Apply psychological perspectives, theories, concepts, and research findings to a scenario. |
| 1.B | Explain how cultural norms, expectations, and circumstances, as well as cognitive biases, apply to behavior and mental processes. |
| 2.A | Determine the type of research design(s) used in a given study. |
| 2.B | Evaluate the appropriate use of research design elements in experimental methodology. |
| 2.C | Evaluate the appropriate use of research design elements in non-experimental methodologies. |
| 2.D | Evaluate whether a psychological research scenario followed appropriate ethical procedures. |
| 3.A | Identify psychology-related concepts in descriptions or representations of data. |
| 3.B | Calculate and interpret measures of central tendency, variation, and percentile rank in a given data set. |
| 3.C | Interpret quantitative or qualitative inferential data from a given table, graph, chart, figure, or diagram. |
| 4.A | Propose a defensible claim. |
| 4.B | Provide reasoning that is grounded in scientific, psychology-derived evidence to support, refute, or modify a claim, policy, or norm. |

Because Practice 2 (research methods and design) has no unit of its own, **every
unit's question bank must carry research-design items**: correlation vs.
causation, independent vs. dependent variable, operational definitions,
confounding variables, experimental vs. correlational vs. naturalistic
observation, and research ethics.

---

## The complete topic list

Topic codes and titles are verbatim from the CED's UNIT AT A GLANCE tables,
cross-checked against the Course at a Glance.

### Unit 1 — Biological Bases of Behavior (6 topics)
| Code | Title |
|---|---|
| 1.1 | Interaction of Heredity and Environment |
| 1.2 | Overview of the Nervous System |
| 1.3 | The Neuron and Neural Firing |
| 1.4 | The Brain |
| 1.5 | Sleep |
| 1.6 | Sensation |

Note the split that trips people up: **Sensation is 1.6, in Unit 1; Perception is
2.1, in Unit 2.** The old course had one "Sensation and Perception" unit.
Exclusion statement on 1.1: genotype, phenotype, DNA, chromosomes, and dominant/
recessive gene expression are explicitly *out of scope*.

### Unit 2 — Cognition (8 topics)
| Code | Title |
|---|---|
| 2.1 | Perception |
| 2.2 | Thinking, Problem-Solving, Judgments, and Decision-Making |
| 2.3 | Introduction to Memory |
| 2.4 | Encoding Memories |
| 2.5 | Storing Memories |
| 2.6 | Retrieving Memories |
| 2.7 | Forgetting and Other Memory Challenges |
| 2.8 | Intelligence and Achievement |

Memory is deliberately split across four topics along the **encode / store /
retrieve** pipeline, with failures in 2.7. Keep a question in the topic whose
stage it actually tests.

### Unit 3 — Development and Learning (9 topics)
| Code | Title |
|---|---|
| 3.1 | Themes and Methods in Developmental Psychology |
| 3.2 | Physical Development Across the Lifespan |
| 3.3 | Gender and Sexual Orientation |
| 3.4 | Cognitive Development Across the Lifespan |
| 3.5 | Communication and Language Development |
| 3.6 | Social-Emotional Development Across the Lifespan |
| 3.7 | Classical Conditioning |
| 3.8 | Operant Conditioning |
| 3.9 | Social, Cognitive, and Neurological Factors in Learning |

Learning is *inside* the development unit now; it is not a unit of its own.

### Unit 4 — Social Psychology and Personality (7 topics)
| Code | Title |
|---|---|
| 4.1 | Attribution Theory and Person Perception |
| 4.2 | Attitude Formation and Attitude Change |
| 4.3 | Psychology of Social Situations |
| 4.4 | Psychodynamic and Humanistic Theories of Personality |
| 4.5 | Social-Cognitive and Trait Theories of Personality |
| 4.6 | Motivation |
| 4.7 | Emotion |

Motivation and Emotion sit in Unit 4, alongside personality — not with biology.

### Unit 5 — Mental and Physical Health (5 topics)
| Code | Title |
|---|---|
| 5.1 | Introduction to Health Psychology |
| 5.2 | Positive Psychology |
| 5.3 | Explaining and Classifying Psychological Disorders |
| 5.4 | Selection of Categories of Psychological Disorders |
| 5.5 | Treatment of Psychological Disorders |

Health psychology (5.1) and positive psychology (5.2) are **new** in the
redesign — the old course had neither. Disorders follow current DSM-5-TR
terminology in the CED.

**35 topics in total.** Files: `p<unit>_<topic>.py`, e.g. `p1_3.py` for topic
1.3, with `verify_p1_3.py` beside it. 25 questions each.

---

## Validating a psychology module

`export_units.py` defaults to 50 questions per topic for any subject that is not
Calculus, so **the `--per-topic 25` flag is required** or the export exits:

```bash
cd content-pool/ap-banks
python3 export_units.py p1_1 --subject PSYCHOLOGY --per-topic 25 --out /tmp/chk_p.json
```

There is nothing to verify with sympy here. `verify_p<unit>_<topic>.py` instead
records, for every one of the 25 items, the specific claim the key rests on and
where in the framework it comes from — a definition, a named study, a theory's
actual prediction — and asserts mechanically that the key text still matches
that claim. An assertion nobody checked is how a wrong key ships.

Two further checks the exporter cannot make, which each module's verifier does:
- **No two choices may be synonyms.** "Negative reinforcement" and "removing an
  unpleasant stimulus to increase a behavior" are one answer written twice, and a
  question with two correct choices is unanswerable. This is psychology's version
  of the duplicate-distractor defect.
- **No question may depend on a figure.** There are no images in this bank.
