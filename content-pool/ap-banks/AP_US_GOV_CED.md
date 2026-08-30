# AP U.S. Government and Politics — CED reference

Source: `ced-source/US_GOV_ced.txt.gz`, a `pdftotext -layout` dump of the
official College Board Course and Exam Description, **V.1, © 2026**. Every
fact below is quoted or paraphrased from that file; page numbers are the CED's
own printed page numbers.

Read this before authoring. Several things in it contradict what general
knowledge of AP U.S. Government would assume — the list is at the bottom and
it is the reason this file exists.

---

## Exam format (CED p. 167)

| Section | Question type | Number | Weighting | Timing |
|---|---|---|---|---|
| I | Multiple-choice | 55 | 50% | 80 minutes |
| II | Free-response | 4 | 50% | 100 minutes |

Total exam length 3 hours. The four free-response questions, each 12.5% of
the exam:

1. **Concept Application** — 3 points, 20 minutes recommended
2. **Quantitative Analysis** — 4 points, 20 minutes
3. **SCOTUS Comparison** — 4 points, 20 minutes
4. **Argument Essay** — 6 points, 40 minutes

Confirmed against the CED, not assumed: 55 MC in 80 minutes and 4 FRQ is
correct.

### Multiple-choice composition (CED p. 169)

| Question type | How many | Stimulus |
|---|---|---|
| Quantitative analysis | five sets, 2–3 questions per set | line graphs, charts, tables, maps, infographics |
| Text-based analysis | two sets, 3–4 questions per set | one set on a **foundational document**; one on another primary or secondary text |
| Visual source analysis | three sets, 2 questions per set | map, cartoon, or infographic |
| Individual multiple-choice | approximately 30 | no stimulus |

So roughly 25 of 55 questions hang off a stimulus. That is the reason the
authoring brief insists on real `table=` data rather than a prose description
of a figure: on this exam, stimulus questions are nearly half the section.

---

## Unit weightings (CED pp. 15, 167)

| Unit | Title | MC weighting | Class periods |
|---|---|---|---|
| 1 | Foundations of American Democracy | 15–22% | ~16 / ~8 |
| 2 | Interactions Among Branches of Government | 25–36% | ~28 / ~14 |
| 3 | Civil Liberties and Civil Rights | 13–18% | ~26 / ~13 |
| 4 | American Political Ideologies and Beliefs | 10–15% | ~22 / ~11 |
| 5 | Political Participation | 20–27% | ~18 / ~9 |

Sixty topics: 9 + 15 + 13 + 10 + 13. The full code-to-title map is
`US_GOV_topics.json`.

---

## Course skills (CED p. 14)

Five categories, and the exam question shapes map onto them directly.

1. **Concept Application** — 1.A describe / 1.B explain / 1.C compare /
   1.D describe in scenarios / 1.E explain in scenarios
2. **SCOTUS Application** — 2.A describe facts, issue, holding, reasoning,
   decision, majority opinion of a *required* case / 2.B relate a required
   case to a foundational document or other source / 2.C compare a required
   case to a **non-required** case / 2.D relate a required case to a political
   principle, institution, process, policy, or behavior
3. **Data Analysis** — 3.A describe the data / 3.B describe patterns and
   trends / 3.C explain patterns and trends to draw conclusions / 3.D explain
   what the data implies / 3.E explain limitations of the data / 3.F explain
   limitations of the visual representation
4. **Source Analysis** — 4.A describe the argument / 4.B relate it to
   political principles / 4.C explain implications / 4.D explain visual
   elements
5. **Argumentation** — 5.A claim / 5.B evidence / 5.C reasoning / 5.D rebuttal

---

## Big ideas (CED p. 16)

1. Constitutionalism
2. Liberty and Order
3. Civic Participation in a Representative Democracy
4. Competing Policymaking Interests
5. Methods of Political Analysis

---

## Required foundational documents (CED p. 25)

**Thirteen** documents, listed here in the CED's own order:

1. The Articles of Confederation
2. Brutus No. 1 — *To the Citizens of the State of New-York*
3. The Constitution of the United States (including the Bill of Rights and
   subsequent amendments)
4. The Declaration of Independence
5. Emancipation Proclamation
6. Federalist No. 10 — *The Same Subject Continued: The Union as a Safeguard
   Against Domestic Faction and Insurrection*
7. Federalist No. 39 — *Conformity of the Plan to Republican Principles*
8. Federalist No. 51 — *The Structure of the Government Must Furnish the
   Proper Checks and Balances Between the Different Departments*
9. Federalist No. 70 — *The Executive Department Further Considered*
10. Federalist No. 78 — *The Judiciary Department*
11. Gettysburg Address (by Abraham Lincoln)
12. "Letter from a Birmingham Jail" (by Martin Luther King, Jr.)
13. Core principles from Adam Smith's *The Wealth of Nations*

### Where each document is named in the framework (CED pp. 26–27)

The Constitution is deliberately omitted from the CED's cross-reference table
because it applies to nearly every learning objective.

| Document | Unit 1 | Unit 2 | Unit 3 | Unit 4 | Unit 5 |
|---|---|---|---|---|---|
| Articles of Confederation | 1.3.A, 1.4.A, 1.5.A, 1.7.A | | 3.7.A | | |
| Brutus No. 1 | 1.2.A, 1.3.A | | | | |
| Declaration of Independence | 1.1.A, 1.2.A, 1.3.A | | | | |
| Emancipation Proclamation | 1.1.A, 1.5.A | 2.4.A, 2.5.A | 3.10.A, 3.12.A | | |
| Federalist No. 10 | 1.2.A, 1.3.A, 1.4.A, 1.9.A | 2.1.A–2.6.A | | 4.7.A–4.10.A | 5.3.A–5.7.A, 5.10.A, 5.11.A |
| Federalist No. 39 | 1.1.A, 1.5.A, 1.7.A, 1.8.A, 1.9.A | | | | |
| Federalist No. 51 | 1.4.A, 1.5.A, 1.6.A, 1.6.B, 1.9.A | 2.2.A–2.6.A, 2.8.A, 2.10.A, 2.11.B, 2.14.A, 2.15.A | | | |
| Federalist No. 70 | 1.6.A | 2.4.A–2.8.A, 2.12.A, 2.13.A, 2.14.A, 2.15.A | | | |
| Federalist No. 78 | | 2.8.A, 2.9.A, 2.10.A, 2.11.A, 2.11.B | | | |
| Gettysburg Address | 1.1.A | 2.4.A, 2.7.A | 3.10.A, 3.11.A | | |
| Letter from a Birmingham Jail | | | 3.1.A, 3.1.B, 3.3.A, 3.4.A, 3.6.A, 3.7.A, 3.8.A, 3.10.A, 3.11.A, 3.12.A | | 5.7.A |
| Adam Smith, *The Wealth of Nations* | | | | 4.1.A, 4.2.A, 4.8.A, 4.9.A, 4.9.B | |

---

## Required Supreme Court cases (CED p. 30)

**Fourteen** cases. The holdings below are the CED's own wording, condensed
only where the dump wraps. A question that states a holding must state *this*
holding.

| Case | Holding as the CED states it |
|---|---|
| **Marbury v. Madison (1803)** | Deciding a case about judicial appointments, the Court established the principle of **judicial review**, empowering the Supreme Court to declare an act of the legislative or executive branch unconstitutional. |
| **McCulloch v. Maryland (1819)** | Deciding a case about a national bank and state taxes, the Court established **supremacy of the U.S. Constitution and federal laws over state laws**. |
| **Schenck v. United States (1919)** | Speech creating a **"clear and present danger"** was not protected by the First Amendment and could be limited. |
| **Brown v. Board of Education (1954)** | Race-based school segregation violates the **Equal Protection Clause of the Fourteenth Amendment**. |
| **Baker v. Carr (1962)** | Redistricting **did not raise political questions**, allowing federal courts to hear cases challenging redistricting plans that may violate the Equal Protection Clause of the Fourteenth Amendment. |
| **Engel v. Vitale (1962)** | School sponsorship of religious activities violates the **Establishment Clause** of the First Amendment. |
| **Gideon v. Wainwright (1963)** | The **Sixth Amendment's right to an attorney** extends procedural due process protections to felony defendants in state courts. |
| **Tinker v. Des Moines Independent Community School District (1969)** | A prohibition against public school students wearing black armbands to protest the Vietnam War violated the students' **freedom of speech** protections in the First Amendment. |
| **New York Times Co. v. United States (1971)** | Bolstered **freedom of the press**, establishing a "heavy presumption against prior restraint" even in cases involving national security. |
| **Wisconsin v. Yoder (1972)** | Compelling Amish students to attend school past the eighth grade violates the **Free Exercise Clause** of the First Amendment. |
| **Shaw v. Reno (1993)** | Under the Fourteenth Amendment's Equal Protection Clause, **majority-minority districts** created under the Voting Rights Act of 1965 may be constitutionally challenged by voters **if race is the only factor** used in creating the district. |
| **United States v. Lopez (1995)** | Congress **exceeded its power under the Commerce Clause** when it made possession of a gun in a school zone a federal crime. |
| **McDonald v. Chicago (2010)** | The **Second Amendment** right to keep and bear arms for self-defense **is applicable to the states**. |
| **Citizens United v. Federal Election Commission (2010)** | Political spending by corporations, associations, and labor unions is a form of **protected speech** under the First Amendment. |

The CED also fixes the vocabulary a SCOTUS question may use (p. 29):
**facts** = relevant events before courts became involved; **issue** = the legal
or constitutional question considered; **holding** = the court's response to
the issue; **reasoning** = the explanation of a holding; **decision** = the
outcome including facts, issue, holding, and reasoning; **opinion** = the
justices' written analysis, the majority opinion being the one agreed to by
more than half.

Students are **not** expected to know dissenting or concurring opinions of
required cases (p. 29). Any non-required case on the exam "will be accompanied
by a summary containing all information necessary to compare" it — which is
why every SCOTUS-comparison item in this bank prints the non-required case's
facts and holding in the stem rather than assuming the student knows it.

---

## Things in this CED that contradict what you would assume

These are the reasons to read the CED rather than write from memory. Each was
checked against the text dump, not recalled.

1. **There are fourteen required cases, not fifteen. `Roe v. Wade` is gone.**
   The long-standing list of fifteen included *Roe v. Wade (1973)*; this CED's
   list does not contain it. A question that treats *Roe* as a required case,
   or that keys a comparison against it, is off-syllabus.

2. **There are thirteen required foundational documents, not nine.** The
   familiar nine (Declaration, Articles, Constitution, Brutus No. 1,
   Federalist 10/51/70/78, Letter from a Birmingham Jail) have been joined by
   **Federalist No. 39**, the **Emancipation Proclamation**, the **Gettysburg
   Address**, and **core principles from Adam Smith's *The Wealth of
   Nations***. Federalist No. 39 in particular is now a Unit 1 workhorse: the
   CED attaches it to 1.1.A, 1.5.A, 1.7.A, 1.8.A and 1.9.A, and EK 1.7.A.1
   cites it by name for the proposition that the division of authority
   "combines national and state features."

3. **Unit 1 has nine topics and Unit 2 has fifteen**, with titles that do not
   match the older framework. Unit 2 in particular now splits the presidency
   across four topics (2.4 Roles and Powers, 2.5 Checks on the Presidency,
   2.6 Expansion of Presidential Power, 2.7 Presidential Communication) and
   the judiciary across four (2.8 The Judicial Branch, 2.9 The Role of the
   Judicial Branch, 2.10 The Court in Action, 2.11 Checks on the Judicial
   Branch). "2.10 The Court in Action" is entirely about **life tenure** —
   EK 2.10.A.1 is its only essential knowledge statement — not about the
   certiorari process, which the framework never mentions.

4. **The Gettysburg Address is now part of Topic 1.1's learning objective.**
   LO 1.1.A reads "Explain how democratic ideals are reflected in the
   Declaration of Independence, the U.S. Constitution, **and the Gettysburg
   Address**," and EK 1.1.A.3 credits the Address with reaffirming *equality
   and popular sovereignty*.

5. **EK 1.1.A.3 names people the older framework did not.** It credits the
   Declaration to Jefferson "with help from Adams and Franklin," and the
   Constitution to "James Madison at the Constitutional Convention in
   Philadelphia that was led by George Washington (with important
   contributions from Hamilton and members of the 'Grand Committee')."

6. **Pocket vetoes cannot be overridden — the CED says so explicitly.**
   EK 2.4.A.2.i: "vetoes can be overridden with a 2/3 vote while pocket
   vetoes cannot be overridden with a 2/3 vote."

7. **The CED ranks the grant types.** EK 1.7.A.5: revenue sharing is "the
   least used form of funding"; block grants are "preferred by the states";
   categorical grants are "preferred by the national government, and [are] the
   most commonly used form of funding." Those preference and frequency claims
   are course content, not commentary.

8. **Impeachment and removal are defined in Unit 1, not Unit 2.**
   EK 1.6.B.2 places both under separation of powers and checks and balances:
   the House "formally charges an official with abuse of power or misconduct,"
   and removal follows only "if the official is convicted in a Senate
   impeachment trial."

9. **Baker v. Carr is dated 1962 in the required-case list but 1961 in the
   CED's own sample question 15.** The required-case list on p. 30 says
   *Baker v. Carr (1962)*; the sample multiple-choice question on p. 177 says
   *Baker v. Carr (1961)*. The list is authoritative, and this bank uses
   **1962** throughout. (The case was argued in 1961 and decided in 1962.)

10. **The CED's own sample multiple-choice questions have FOUR options
    (A–D), not five.** See CED pp. 172–177. This bank is authored with **five**
    options per the project's `SOCIAL_BRIEF.md`, which is a deliberate house
    decision to make the banks harder than the exam and consistent across the
    three social-science subjects — it is *not* the CED's format. Anyone
    reading these modules as a model of exam formatting should know that.

11. **EK 2.2.A.3.i says a discharge petition is filed by "an individual
    representative."** The real chamber rule requires 218 signatures; the CED's
    sentence describes who *files* it, and adds "but it is rarely done." Items
    in this bank are worded to be true of both readings.

12. **Topic 2.3 Congressional Behavior is where the trustee/delegate/politico
    distinction lives** (EK 2.3.A.4), and where *Baker v. Carr* and *Shaw v.
    Reno* attach (EK 2.3.A.2), even though the topic's title says nothing
    about either.
