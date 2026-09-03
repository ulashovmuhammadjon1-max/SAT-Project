"""Key audit for AP BIOLOGY 7.8 Continuing Evolution.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1 to 10, 20 to 21 and 27 to 30 are keyed to EK 7.8.A.1, which asserts
that all species have evolved and continue to evolve and names four examples:
genomic changes over time, continuous change in the fossil record, evolution of
resistance to antibiotics, pesticides, herbicides or chemotherapy drugs, and
pathogens evolving and causing emergent diseases.

Items 16 to 19 and 22 to 26 are keyed to the topic's suggested skill 3.D,
propose a new investigation based on an evaluation of the experimental design
or evidence. Their keys rest on a stated defect in the design described -- a
confound, a missing comparison group, a measurement that changes with time --
and each claim below names that defect rather than restating the answer.

Items 11 to 15 carry a table, and every number their keys state is RECOMPUTED
below from that table alone, through cg_check's header-and-label accessors. The
row a stem names is located by parsing the stem, not by trusting a row index.
cg_check.check fails a table question with no such callable.

None of this says whether the biology is right; that is gated by the CLAIMS
text and by the rule in SCIENCE_BRIEF.md that a key must trace to a CED
sentence.

NEGATIVE CONTROL. Moving any key, or changing any table cell the keys depend
on, makes this file raise; confirmed by running exactly that.
"""
import re

import cg_check as cg
import b7_8

QS = b7_8.QUESTIONS
T_RESIST = b7_8._T_RESIST
T_FIELDS = b7_8._T_FIELDS

TESTED = "Number of bacterial colonies tested"
GREW = "Number of colonies that grew on the antibiotic"
SEASONS = "Number of seasons the insecticide has been applied"
SURVIVING = "Percentage of the pest population surviving the standard dose"


def keyed(item):
    return item["choices"][item["ans"]]


def named_row(table, item):
    """The single row label the stem names outright."""
    hits = [lab for lab in cg.labels(table) if cg.contains_phrase(item["q"], lab)]
    assert len(hits) == 1, f"the stem names rows {hits}; it must name exactly one"
    return hits[0]


def q11(table, item):
    lab = named_row(table, item)
    n, g = cg.cell(table, lab, TESTED), cg.cell(table, lab, GREW)
    pct = g / n * 100
    assert abs(pct - round(pct)) < 1e-9, "the percentage must be whole for a calculator-free item"
    assert keyed(item) == f"{int(round(pct))} percent", \
        f"q11 key {keyed(item)!r} but {int(g)} of {int(n)} is {pct} percent"
    return f"{lab} reports {int(g)} of {int(n)} colonies growing, which is {int(round(pct))} percent"


def q12(table, item):
    grew = cg.col(table, GREW)
    rise = grew[-1] - grew[0]
    assert keyed(item) == f"{int(rise)} colonies", \
        f"q12 key {keyed(item)!r} but the column rises from {grew[0]} to {grew[-1]}"
    return f"the growing column runs {grew}, a rise of {int(rise)} between the first and last rounds"


def q13(table, item):
    grew = cg.col(table, GREW)
    tested = set(cg.col(table, TESTED))
    assert all(b > a for a, b in zip(grew, grew[1:])), \
        f"the key says the count rose at every round; the column reads {grew}"
    assert len(tested) == 1, \
        f"the key says the number tested stayed the same; the column holds {tested}"
    return f"the growing column {grew} rises at every step while every round tested {int(tested.pop())} colonies"


def q14(table, item):
    pairs = sorted(zip(cg.col(table, SEASONS), cg.col(table, SURVIVING)))
    surv = [s for _, s in pairs]
    assert all(b > a for a, b in zip(surv, surv[1:])), \
        f"the key says survival rises with seasons applied; sorted survival is {surv}"
    return f"sorting the rows by seasons applied gives survival {surv}, rising at every step"


def q15(table, item):
    seasons = {lab: cg.cell(table, lab, SEASONS) for lab in cg.labels(table)}
    most = max(seasons, key=seasons.get)
    never = [lab for lab, v in seasons.items() if v == 0]
    assert len(never) == 1, f"the stem names one untreated field; {never} have no seasons applied"
    gap = cg.cell(table, most, SURVIVING) - cg.cell(table, never[0], SURVIVING)
    assert keyed(item) == f"{int(gap)} percentage points", \
        f"q15 key {keyed(item)!r} but the gap is {gap}"
    return (f"{most} has the most seasons applied and {never[0]} none, and their survival "
            f"percentages differ by {int(gap)}")


TABLE_CHECKS = {11: q11, 12: q12, 13: q13, 14: q14, 15: q15}


CLAIMS = [
 ("All species have evolved",
  "EK 7.8.A.1 opens with the sentence that all species have evolved and continue to evolve. The four examples that follow are introduced with the words examples include, so they illustrate the claim rather than bounding it."),
 ("Genomic changes over time",
  "EK 7.8.A.1 lists genomic changes over time as its first example. The study reports change in the genome of a living lineage across generations, which is that example and none of the other three."),
 ("Continuous change in the fossil record",
  "EK 7.8.A.1 lists continuous change in the fossil record as its second example. A graded shift in form through successive levels of rock is a record of change over time within one lineage."),
 ("resistance to a herbicide",
  "EK 7.8.A.1's third example is the evolution of resistance to antibiotics, pesticides, herbicides or chemotherapy drugs, naming herbicides outright. The observation is a loss of effect of a chemical treatment on the population it targets."),
 ("Pathogens evolving and causing emergent diseases",
  "EK 7.8.A.1's fourth example names pathogens evolving and causing emergent diseases. The scenario reports a pathogen changing and a disease appearing where it had not been reported before."),
 ("number of individuals in a population",
  "EK 7.8.A.1 lists four examples and a change in population size is not among them. Numbers can rise or fall with no change in the heritable makeup of the species, which is what all four named examples report."),
 ("quickest to observe",
  "EK 7.8.A.1 asserts that ALL species have evolved and continue to evolve and offers resistance as one example. Short generation times under intense treatment make the change fast enough to watch, which is a fact about observability rather than a limit on the claim."),
 ("short generation time, so that many generations pass",
  "Heritable change accumulates between generations, and EK 7.8.A.1's examples that are watched in real time involve organisms that turn over quickly. Calendar time matters only through the number of generations it contains."),
 ("too few generations",
  "EK 7.8.A.1 asserts ongoing change without specifying a rate, so a failure to detect change is not a demonstration that there is none. Skill 3.D asks for an evaluation of the evidence, and this evidence is underpowered rather than negative."),
 ("sampled at more than one time",
  "EK 7.8.A.1 offers both the fossil record and genomic change as examples of CONTINUING evolution, and continuity is a property of a sequence. Only a comparison across time turns a description of a lineage into evidence that it has changed."),
 ("30 percent",
  "Skill 5.A includes percentages, and EK 7.8.A.1 names antibiotic resistance as an example of continuing evolution. The table check above locates the round the stem names and divides its two counts."),
 ("116 colonies",
  "Skill 4.B, identifying specific data points, with skill 5.A for the arithmetic. The table check above takes the first and last entries of the column of colonies that grew and recomputes their difference."),
 ("rose at every round while the number tested stayed the same",
  "Skill 4.B asks for the trend and the relationship between variables. The table check above confirms both halves of the key separately: the count rose at every step, and every round tested the same number of colonies, which is what makes the rise a change in the population rather than in sampling effort."),
 ("the larger the percentage of the pest population surviving",
  "Skill 4.B asks for the relationship between variables. The table check above sorts the fields by seasons of application and confirms that survival rises without exception, which is the pattern EK 7.8.A.1's resistance example describes."),
 ("61 percentage points",
  "Skill 5.A includes percentages and percent changes. The table check above identifies the field with the most seasons applied and the single field with none, and recomputes the difference between their survival percentages."),
 ("soil, climate and neighbouring crops",
  "Skill 3.D asks for an evaluation of the design. Fields selected because they differ in treatment history differ in other ways as well, so the comparison cannot separate the effect of treatment from everything that varies alongside it."),
 ("at random",
  "Skill 3.D asks for a new investigation that repairs the design. Random assignment of comparable fields to treatment and no treatment severs the link between treatment history and the other differences among fields, which is precisely what the original comparison could not do."),
 ("freshly prepared batch",
  "Skill 3.D asks for an investigation separating two explanations of one result. Testing early and late colonies at the same time against the same fresh antibiotic holds the chemical constant, so a remaining difference must lie in the bacteria."),
 ("before any antibiotic is applied",
  "Skill 3.D asks for a design that discriminates between two accounts. Only a sample that has never met the antibiotic can show whether resistant cells were present beforehand, so every option beginning with exposure leaves both accounts standing."),
 ("before and after the change in outcomes",
  "EK 7.8.A.1 names the evolution of resistance as continuing evolution, and a claim of change requires a comparison across time. Testing early and late pathogen samples under identical conditions is that comparison; patient numbers and drug prices are facts about the clinic."),
 ("applied dose has fallen steadily",
  "Skill 3.D asks for an evaluation of evidence. If less insecticide is being applied, greater survival is accounted for with no heritable change in the pest, so the observation no longer requires the evolutionary explanation."),
 ("every level of the sequence and compare the values level by level",
  "EK 7.8.A.1 names continuous change in the fossil record, and continuity is a claim about a sequence of comparable measurements. One level alone, or a different character at each level, yields nothing comparable across time."),
 ("comparing like with like across the levels",
  "Skill 3.D asks for evaluation of a design. A difference between two measurements of different characters is not evidence of change in either, so a sequence measured inconsistently cannot bear on EK 7.8.A.1's fossil example."),
 ("differ systematically from those of earlier years",
  "EK 7.8.A.1 names genomic changes over time and pathogens evolving among its examples. A systematic early-to-late difference in sequence is a heritable change in the population, whereas geographic spread and sampling effort describe where and how hard people looked."),
 ("produced by the change in method",
  "Skill 3.D asks for an evaluation of the design. A measurement change that coincides with the passage of time is confounded with the change being measured, so the observed difference no longer identifies its own cause."),
 ("Re-sequence the stored early samples",
  "Skill 3.D asks for the investigation that repairs the design. Applying one method to samples from both periods holds the measurement constant, so any difference that survives is a difference between the samples themselves."),
 ("not an exhaustive list",
  "EK 7.8.A.1 introduces its four examples with the words examples include, after asserting that all species have evolved and continue to evolve. A list of examples illustrates a general claim rather than bounding it."),
 ("resistance to a chemotherapy drug",
  "EK 7.8.A.1's third example names chemotherapy drugs alongside antibiotics, pesticides and herbicides. Comparing early and late cells at the same drug concentration is what makes the observation a change in the cell population."),
 ("survivors are the source of the next generation",
  "EK 7.8.A.1 names the evolution of resistance as continuing evolution, which is a heritable change in a population across generations. Only survivors contribute to the next generation, so whatever heritable difference distinguished them is what that generation inherits."),
 ("observed and investigated in living populations and in the record",
  "EK 7.8.A.1 asserts that all species have evolved and continue to evolve, and its four examples span living populations, the fossil record, managed systems and pathogens. That span is what makes the claim general rather than tied to one setting."),
]


# SCIENCE_BRIEF.md: Biology is exported untypeset, so a backslash macro or a
# dollar span would reach a student as literal characters, and a
# digit-hyphen-digit run reads as a subtraction. Explicit lookarounds, never \b.
_BANNED = [
    (re.compile(r"\\"), "a backslash: this bank carries no LaTeX"),
    (re.compile(r"\$"), "a dollar-delimited math span"),
    (re.compile(r"(?<![A-Za-z])\d+\s*-\s*\d+(?![A-Za-z])"), "a digit-hyphen-digit range"),
    (re.compile(r"\d\s*/\s*\d"), "a digit-slash-digit fraction"),
]


def style():
    hits = 0
    for i, item in enumerate(QS, 1):
        texts = [("stem", item["q"]), ("why", item["why"])]
        texts += [(f"choice {k}", c) for k, c in enumerate(item["choices"])]
        if item.get("table"):
            texts.append(("table", " | ".join(item["table"]["headers"])))
            texts += [("table", " | ".join(str(c) for c in r)) for r in item["table"]["rows"]]
        for where, text in texts:
            for pat, why_bad in _BANNED:
                m = pat.search(text)
                assert not m, f"q{i} {where} contains {m.group(0)!r}, {why_bad}"
                hits += 1
    return hits


def main():
    n_style = style()
    cg.check(b7_8, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation checks clean (no LaTeX, no ranges, no slash fractions).")


main()
