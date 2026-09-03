"""Key audit for AP BIOLOGY 8.1 Responses to the Environment.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Every non-data item is keyed to a sentence the CED prints: EK 8.1.A.1
(behavioral and physiological mechanisms), EK 8.1.A.2 (information exchanged in
response to internal changes and external cues, which can change behavior),
EK 8.1.B.1 (the five signal kinds; signaling behaviors changing others'
behavior and resulting in differential reproductive success; the four uses --
dominance, food, territory, reproductive success) and EK 8.1.B.2 (responses to
information are vital to natural selection and evolution; fitness favors innate
AND learned behaviors; cooperative behavior tends to increase the fitness of the
individual and the survival of the population).

THREE EXCLUSION STATEMENTS. The CED places specific behavioral and
physiological mechanisms, specific mechanisms of communication, and the details
of communication and community behavioral systems beyond the scope of the exam.
No key in this module requires knowing how any response or signal works; the
classification items turn only on the MODE or the USE the framework itself
names, and the design items turn on suggested skill 3.C.

Items 21 to 28 carry a table, and every number and every design claim their keys
make is RECOMPUTED below from that table alone -- including which column is
constant across groups (the dependent variable cannot be the one held fixed)
and which column varies by design. cg_check.check fails a table question with
no such callable.

NEGATIVE CONTROL. Moving any key, or changing any table cell the keys depend
on, makes this file raise; confirmed by running exactly that.
"""
import re

import cg_check as cg
import b8_1

QS = b8_1.QUESTIONS
T_TRIAL = b8_1._T_TRIAL
T_COOP = b8_1._T_COOP

SOUND = "Sound presented to the group"
TESTED = "Number of individuals tested"
RESPONDED = "Number that changed their behaviour within one minute"
ATTEMPTS = "Number of foraging attempts observed"
FED = "Number of attempts that obtained food"


def keyed(item):
    return item["choices"][item["ans"]]


def raw(table, row_label, header):
    j = [cg.normalize(h) for h in table["headers"]].index(cg.normalize(header))
    i = [cg.normalize(lab) for lab in cg.labels(table)].index(cg.normalize(row_label))
    return str(table["rows"][i][j])


def _groups_numbered(table):
    nums = [cg.num(lab) for lab in cg.labels(table)]
    assert nums == list(range(1, len(nums) + 1)), \
        f"group labels are {cg.labels(table)}; they must be numbered from one in row order"


def _design(table):
    """Which columns vary by design and which are held constant."""
    _groups_numbered(table)
    treatments = [cg.normalize(raw(table, lab, SOUND)) for lab in cg.labels(table)]
    assert len(set(treatments)) == len(treatments), \
        f"the treatment column must differ across groups; it reads {treatments}"
    tested = set(cg.col(table, TESTED))
    assert len(tested) == 1, \
        f"the number tested must be held constant, or the outcome counts are not comparable; {tested}"
    return treatments, tested.pop()


def q21(table, item):
    treatments, _ = _design(table)
    untreated = [lab for lab in cg.labels(table)
                 if cg.normalize(raw(table, lab, SOUND)) in ("no sound", "none")]
    assert len(untreated) == 1, f"exactly one group must receive no treatment; {untreated} do"
    assert cg.contains_phrase(keyed(item), untreated[0]), \
        f"q21 key {keyed(item)!r} but the untreated group is {untreated[0]}"
    return f"treatments are {treatments}; only {untreated[0]} receives none, so it is the control"


def q22(table, item):
    _design(table)
    assert cg.contains_phrase(keyed(item), "kind of sound"), \
        f"q22 key {keyed(item)!r} does not name the column that differs across groups"
    assert not cg.contains_phrase(keyed(item), "changed their behaviour"), \
        "the independent variable must not be the measured outcome"
    return "the sound column is the only column set differently for each group by the investigator"


def q23(table, item):
    _, tested = _design(table)
    responded = cg.col(table, RESPONDED)
    assert len(set(responded)) > 1, \
        f"the measured outcome must vary across groups; it reads {responded}"
    assert cg.contains_phrase(keyed(item), "changed their behaviour"), \
        f"q23 key {keyed(item)!r} does not name the measured outcome column"
    assert not cg.contains_phrase(keyed(item), "individuals tested"), \
        f"the number tested is held constant at {int(tested)} and so is not the outcome"
    return f"the outcome column reads {responded} while {int(tested)} individuals were tested in every group"


def q24(table, item):
    named = [lab for lab in cg.labels(table)
             if cg.contains_phrase(item["q"], raw(table, lab, SOUND))]
    assert len(named) == 1, f"the stem names treatments for rows {named}; it must name exactly one"
    n, r = cg.cell(table, named[0], TESTED), cg.cell(table, named[0], RESPONDED)
    pct = r / n * 100
    assert abs(pct - round(pct)) < 1e-9, "the percentage must be whole for a calculator-free item"
    assert keyed(item) == f"{int(round(pct))} percent", \
        f"q24 key {keyed(item)!r} but {int(r)} of {int(n)} is {pct} percent"
    return f"{named[0]} recorded {int(r)} of {int(n)} responding, which is {int(round(pct))} percent"


def q25(table, item):
    _design(table)
    rates = {lab: cg.cell(table, lab, RESPONDED) / cg.cell(table, lab, TESTED)
             for lab in cg.labels(table)}
    best = max(rates, key=rates.get)
    others = sorted(v for lab, v in rates.items() if lab != best)
    assert others[-1] * 2 < rates[best], \
        f"the key says one treatment responded far more often; the rates are {rates}"
    assert cg.normalize(raw(table, best, SOUND)) not in ("no sound", "none"), \
        "the key attributes the largest response to a treatment, not to the control"
    return f"response rates are {rates}; the largest is {best} at more than twice any other"


def q26(table, item):
    named = [lab for lab in cg.labels(table) if cg.contains_phrase(item["q"], lab)]
    assert len(named) == 1, f"the stem names rows {named}; it must name exactly one"
    a, f = cg.cell(table, named[0], ATTEMPTS), cg.cell(table, named[0], FED)
    pct = f / a * 100
    assert abs(pct - round(pct)) < 1e-9, "the percentage must be whole for a calculator-free item"
    assert keyed(item) == f"{int(round(pct))} percent", \
        f"q26 key {keyed(item)!r} but {int(f)} of {int(a)} is {pct} percent"
    return f"{named[0]} obtained food on {int(f)} of {int(a)} attempts, which is {int(round(pct))} percent"


def q27(table, item):
    pcts = {lab: cg.cell(table, lab, FED) / cg.cell(table, lab, ATTEMPTS) * 100
            for lab in cg.labels(table)}
    group = [lab for lab in pcts if cg.contains_phrase(lab, "as a group")]
    alone = [lab for lab in pcts if cg.contains_phrase(lab, "alone")]
    assert len(group) == 1 and len(alone) == 1, f"rows must name one group and one solitary condition; {pcts}"
    gap = pcts[group[0]] - pcts[alone[0]]
    assert abs(gap - round(gap)) < 1e-9, "the difference must be whole for a calculator-free item"
    assert keyed(item) == f"{int(round(gap))} percentage points", \
        f"q27 key {keyed(item)!r} but the gap is {gap}"
    return f"success is {pcts[group[0]]:.0f} percent as a group against {pcts[alone[0]]:.0f} alone, a gap of {int(round(gap))}"


def q28(table, item):
    pcts = {lab: cg.cell(table, lab, FED) / cg.cell(table, lab, ATTEMPTS) * 100
            for lab in cg.labels(table)}
    group = [lab for lab in pcts if cg.contains_phrase(lab, "as a group")][0]
    alone = [lab for lab in pcts if cg.contains_phrase(lab, "alone")][0]
    assert pcts[group] > pcts[alone], \
        f"the key says the group condition did better; the rates are {pcts}"
    attempts = set(cg.col(table, ATTEMPTS))
    assert len(attempts) == 1, \
        f"the two conditions must observe the same number of attempts to be compared directly; {attempts}"
    return (f"the group condition succeeded on {pcts[group]:.0f} percent of attempts against "
            f"{pcts[alone]:.0f} percent alone, over the same number of attempts")


TABLE_CHECKS = {21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28}


CLAIMS = [
 ("Behavioral and physiological mechanisms",
  "EK 8.1.A.1 states that organisms respond to changes in their environment through behavioral and physiological mechanisms. The statement concerns the responding individual and is restricted neither to animals nor to evolutionary timescales."),
 ("without requiring knowledge of any particular mechanism",
  "EK 8.1.A.1 states the general claim and carries an exclusion statement placing knowledge of specific behavioral or physiological mechanisms beyond the scope of the exam. What is assessable is that responses of those two kinds occur."),
 ("Internal changes and external cues",
  "EK 8.1.A.2 states that organisms exchange information with one another in response to internal changes AND external cues. Both sources are named, so options admitting only one contradict the statement."),
 ("A change in behavior",
  "EK 8.1.A.2 states that the exchange of information in response to internal changes and external cues can change behavior. Behavior is the outcome the statement names, not sequence, species or habitat."),
 ("Visual, audible, tactile, electrical, and chemical",
  "EK 8.1.B.1 states that organisms communicate through various mechanisms and names those five kinds. Each other option drops kinds the statement includes or adds one it does not."),
 ("A chemical signal",
  "EK 8.1.B.1 names chemical signals among the kinds of communication. A released substance detected by another organism is chemical, and how the detection works is placed beyond the scope by this topic's own exclusion statement."),
 ("A visual signal",
  "EK 8.1.B.1 names visual signals among the kinds of communication. A display that must be seen to have its effect is visual, whatever produces the colour."),
 ("An audible signal",
  "EK 8.1.B.1 names audible signals among the kinds of communication. A produced sound that changes the behaviour of those who hear it is audible."),
 ("A tactile signal",
  "EK 8.1.B.1 names tactile signals among the kinds of communication. Patterned physical contact that changes the receiver's behaviour is tactile."),
 ("An electrical signal",
  "EK 8.1.B.1 names electrical signals among the kinds of communication, and the scenario rules out the other four by description. How the field is generated or detected is beyond the scope by the topic's exclusion statement."),
 ("changes in the behavior of other organisms and differential reproductive success",
  "EK 8.1.B.1 states that signaling behaviors produce changes in the behavior of other organisms and can result in differential reproductive success. Differential means unequal, which is the opposite of the option claiming identical success."),
 ("Indicating dominance",
  "EK 8.1.B.1 lists indicating dominance, finding food, establishing territory and ensuring reproductive success as the uses animals make of signals. A display causing a rival to withdraw from a contested resource is the first."),
 ("Finding food",
  "EK 8.1.B.1 names finding food among the four uses. The signal changes the receivers' behaviour so that they reach the resource, which is the first sub-point of the same statement in action."),
 ("Establishing territory",
  "EK 8.1.B.1 names establishing territory among the four uses. A signal at the boundary of an occupied area that keeps others out is that use."),
 ("ensure reproductive success, and that signaling behaviors can result in differential reproductive success",
  "EK 8.1.B.1 names ensuring reproductive success among the four uses AND separately states that signaling behaviors can result in differential reproductive success. The scenario reports both a use and an unequal outcome."),
 ("Changing the season in which a habitat receives rainfall",
  "EK 8.1.B.1 lists exactly four uses of signals and altering a habitat's climate is not among them, nor is it something a signal between organisms could do."),
 ("Natural selection and evolution",
  "EK 8.1.B.2 states that responses to information and communication of information are vital to natural selection and evolution. Behaviour bears on survival and reproduction, which is what selection acts through."),
 ("Innate and learned behaviors",
  "EK 8.1.B.2 states that fitness favors innate AND learned behaviors that increase survival and reproductive success. Both kinds of behavior and both outcomes are named."),
 ("because the statement names innate and learned behaviors alike",
  "EK 8.1.B.2 distinguishes innate from learned behaviors and then treats them alike with respect to what fitness favours, namely behaviors that increase survival and reproductive success."),
 ("fitness of the individual and the survival of the population",
  "EK 8.1.B.2 states that cooperative behavior tends to increase the fitness of the individual AND the survival of the population. The statement joins the two outcomes rather than trading one against the other."),
 ("Group 3",
  "Skill 3.C includes identifying appropriate controls. The table check above confirms that exactly one group receives no treatment on the manipulated variable and that the number tested is the same in every group."),
 ("kind of sound",
  "Skill 3.C includes identifying independent variables. The table check above confirms the sound column differs for every group by design and that the key does not instead name the measured outcome."),
 ("changed their behaviour",
  "Skill 3.C includes identifying dependent variables. The table check above confirms the outcome column varies across groups while the number tested is held constant, so the outcome is what was measured rather than what was set."),
 ("85 percent",
  "Skill 5.A includes percentages. The table check above finds the row whose treatment the stem names and divides its two counts."),
 ("far more often than either the other call or silence",
  "EK 8.1.A.2 states that organisms exchange information in response to external cues and that this can change behavior. The table check above confirms one treatment produced a response rate more than twice that of any other, and that the treatment concerned is not the control."),
 ("15 percent",
  "Skill 5.A includes percentages. The table check above locates the row the stem names and divides its number of successful attempts by its number of attempts."),
 ("33 percentage points",
  "Skill 5.A includes percentages and percent changes. The table check above recomputes each condition's success percentage from its own counts and takes the difference."),
 ("Cooperative behavior tends to increase the fitness of the individual",
  "EK 8.1.B.2 states that cooperative behavior tends to increase the fitness of the individual and the survival of the population. The table check above confirms the group condition succeeded on a larger share of attempts over the same number of attempts."),
 ("at random to forage alone or in a group",
  "Skill 3.C includes justifying appropriate controls. Individuals that choose to forage together may differ from those that do not, and sites and times may differ too, so only assignment breaking those links leaves grouping as the difference between conditions."),
 ("when the manipulated variable is absent entirely",
  "Skill 3.C includes justifying appropriate controls. A control establishes the baseline rate of the measured behaviour with the treatment absent, whereas a quieter version of the same call is a smaller dose of the treatment rather than its absence."),
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

_FIGURE_TALK = re.compile(
    r"(?<![A-Za-z])(the (?:graph|figure|diagram|chart|image) (?:shown|above|below)|"
    r"in the (?:graph|figure|diagram|chart|image) (?:shown|above|below)|"
    r"shown in the (?:graph|figure|diagram|chart|image))(?![A-Za-z])",
    re.IGNORECASE)


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
            m = _FIGURE_TALK.search(text)
            assert not m, (
                f"q{i} {where} says {m.group(0)!r}, promising a figure the bank cannot show"
            )
            hits += 1
    return hits


def main():
    n_style = style()
    cg.check(b8_1, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation and figure-reference checks clean.")


main()
