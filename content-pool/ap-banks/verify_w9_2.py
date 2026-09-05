"""Key audit for AP WORLD HISTORY: MODERN 9.2 Technological Advances and
Limitations After 1900: Disease.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither.

KC-6.1.III.A IS THREE CLAIMS IN ONE PARAGRAPH, and the whole topic is the work
of keeping them apart:

  (a) diseases associated with poverty PERSISTED WHILE other diseases EMERGED as
      new epidemics -- a continuity and a change at once, not one replacing the
      other -- and IN SOME CASES this led to social disruption;
  (b) those outbreaks SPURRED technological and medical advances, so the
      direction runs from the outbreak to the advance and not the reverse;
  (c) some diseases occurred at higher incidence MERELY BECAUSE OF increased
      longevity -- a rise in the recorded count that is not a rise in danger.

(c) is the subtlest sentence on the page and the one a student is likeliest to
read as (a). q4, q10, q16, q20, q26 and q27 all turn on that distinction and the
claims below say which of the three each key belongs to.

WHAT NO CLAIM BELOW ASSERTS. Epidemic disease is ground on which people hold
strong and current views. Every claim is limited to the framework's descriptive
sentences: none assigns blame for an outbreak to any country, government or
group; none states a death toll; none recommends or condemns a public health
measure; and none describes any disease as characteristic of any people. Where
an item involves a source arguing about a disease, the key is what the source
claims or what would test it, never whether the source is right.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Seven items are built on a reversal a prepared student could believe:

  q1   persistence and emergence exchanged, one replacing the other
  q5   outbreak and advance reversed, the advance spurring the outbreak
  q7   "in some cases" swapped for "always" and for "never"
  q12  simultaneous developments swapped for sequential ones
  q18  the NOT-supported item, where the key is deliberately the false claim
  q22  the advance-spurs-outbreak reversal again, from a source
  q21  "in some cases" tested against two regions with different outcomes

For each the anchor spans the whole relation, so an anchor that matched the
swapped distractor would fail the gate rather than pass it. That defect is on
record in `verify_e2_1.py`.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions.

NEGATIVE CONTROL: `python3 verify_w9_2.py --selftest`. It rotates all thirty
keys, breaks all thirty anchors, corrupts every cell of every table, injects
each banned notation form, injects figure language into a stem and a choice,
strips the citation from a why and from a claim, duplicates a choice, thins a
why and makes a why name an option by letter -- and asserts not merely that
something raised but WHICH message came back. It also runs positive controls,
so a gate that rejected everything would fail here rather than look thorough.
"""
import sys

import cg_check as cg
import wh_check as wh
import w9_2

T_CASES = w9_2._T_CASES
T_AGES = w9_2._T_AGES
T_PROGRAMMES = w9_2._T_PROGRAMMES

CASES = "Cases recorded"
POVERTY = "Of those, from diseases long associated with poverty"
EMERGENT = "Of those, from diseases newly emergent in the period"
PERSONS = "Persons in the group"
AFFECTED = "Of those, living with a condition of the kind associated with longer life"
UNAFFECTED = "Of those, not so affected"
PROGRAMMES = "New programmes begun"
AFTER_OUTBREAK = "Of those, begun within two years of a recorded outbreak"
NOT_AFTER = "Of those, not so begun"


def _parts_sum_to_whole(table, whole, parts, what):
    """Every row's parts must total its whole.

    This is what makes the negative control mean anything on these tables. The
    corruption in `es_check` only ever makes a number LARGER, so a check of the
    form "this count is above zero" is monotone and can never fail: it reads the
    table without being able to object to anything in it. Sibling module 8.5
    shipped a first draft whose table check caught 1 of 12 corrupted cells for
    exactly that reason. Each row here states a whole and the two parts it was
    divided into, and every stem says so.
    """
    labs = cg.labels(table)
    totals = cg.col(table, whole)
    cols = [cg.col(table, p) for p in parts]
    for i, lab in enumerate(labs):
        got = sum(c[i] for c in cols)
        assert got == totals[i], (
            f"{lab}: the {what} split into {[c[i] for c in cols]} totals {got}, but the "
            f"row states {totals[i]} in all -- the parts do not sum to the whole")


def q3(table, item):
    """Poverty-associated cases persist throughout; emergent cases rise."""
    periods = cg.labels(table)
    assert periods == ["1950s", "1970s", "1990s"], \
        f"the key speaks of every period in the record; the rows are {periods}"
    _parts_sum_to_whole(table, CASES, [POVERTY, EMERGENT], "cases recorded")
    total = cg.col(table, CASES)
    pov = cg.col(table, POVERTY)
    eme = cg.col(table, EMERGENT)
    assert all(p > 0 for p in pov), \
        f"the key needs poverty-associated cases in every period; they run {pov}"
    assert all(b > a for a, b in zip(eme, eme[1:])), \
        f"the key says newly emergent cases rise across the record; they run {eme}"
    # every distractor false on the same numbers
    assert pov[-1] > 0, \
        "'cases from diseases associated with poverty disappear from the record' must be false"
    assert eme[-1] > eme[0], \
        "'cases from newly emergent diseases fall across the record' must be false"
    assert not all(b > a for a, b in zip(total, total[1:])), \
        "'the total number of cases rose in each period' must be false"
    assert not all(e > p for e, p in zip(eme, pov)), \
        "'more cases come from newly emergent diseases in every period' must be false"
    return (f"poverty-associated cases run {pov}, present throughout, while newly emergent "
            f"cases run {eme}, rising at every step, against totals {total} that do not; "
            f"the parts sum to the stated wholes and all four distractors recompute false")


def q8(table, item):
    """Prevalence of the longevity-associated condition rises with age."""
    groups = cg.labels(table)
    assert groups == ["Under 40", "40 to 64", "65 and over"], \
        f"the key speaks of each older age group in turn; the rows are {groups}"
    _parts_sum_to_whole(table, PERSONS, [AFFECTED, UNAFFECTED], "persons in the group")
    total = cg.col(table, PERSONS)
    aff = cg.col(table, AFFECTED)
    shares = [a / t for a, t in zip(aff, total)]
    assert all(b > a for a, b in zip(shares, shares[1:])), (
        f"the key says the share rises with each older group; the shares run "
        f"{[round(s, 3) for s in shares]}")
    # every distractor false on the same numbers
    assert shares[-1] > shares[0], \
        "'the share falls with each older age group' must be false"
    assert aff[0] > 0, \
        "'no person under 40 is recorded with such a condition' must be false"
    assert not all(b > a for a, b in zip(total, total[1:])), \
        "'the number of persons in each group rises with age' must be false"
    assert not all(s > 0.5 for s in shares), (
        "'the share is above half in every age group' must be false; the shares are "
        f"{[round(s, 3) for s in shares]}")
    return (f"the affected share runs {[round(s, 3) for s in shares]} across groups of "
            f"{total} persons, rising with age while the groups themselves shrink; the "
            f"parts sum to the stated wholes and all four distractors recompute false")


def q13(table, item):
    """New programmes rise, and most follow an outbreak in every decade."""
    decades = cg.labels(table)
    assert decades == ["1950s", "1970s", "1990s"], \
        f"the key speaks of each decade recorded; the rows are {decades}"
    _parts_sum_to_whole(table, PROGRAMMES, [AFTER_OUTBREAK, NOT_AFTER], "new programmes")
    total = cg.col(table, PROGRAMMES)
    after = cg.col(table, AFTER_OUTBREAK)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says the number of new programmes rose in each decade; it runs {total}"
    shares = [a / t for a, t in zip(after, total)]
    for d, s in zip(decades, shares):
        assert s > 0.5, (
            f"the key needs most of {d}'s programmes to follow an outbreak within two "
            f"years; the share is {s:.3f}")
    # every distractor false on the same numbers
    assert not all(s < 0.5 for s in shares), \
        "'most programmes began without a recorded outbreak' must be false"
    assert total[-1] > total[0], \
        "'the number of new programmes fell in each decade after the first' must be false"
    assert after[0] > 0, \
        "'no 1950s programme began within two years of an outbreak' must be false"
    assert len(set(total)) > 1, \
        "'the three decades recorded the same number of new programmes' must be false"
    return (f"new programmes run {total}, rising throughout, with the post-outbreak share "
            f"{[round(s, 3) for s in shares]}, a majority in every decade; the parts sum "
            f"to the stated wholes and all four distractors recompute false")


TABLE_CHECKS = {3: q3, 8: q8, 13: q13}

CLAIMS = [
 ("diseases associated with poverty persisting while other diseases emerged as new epidemics",
  "KC-6.1.III.A states that diseases associated with poverty PERSISTED WHILE other diseases emerged as new epidemics and threats to human populations. The framework describes a continuity and a change running at once rather than one kind displacing the other, and two distractors exchange the two halves, so the anchor carries the whole relation."),

 ("They spurred technological and medical advances",
  "KC-6.1.III.A states that these outbreaks spurred technological and medical advances. The direction runs from the outbreak to the advance, which is the connection skill 5.B asks a student to explain, and none of the other consequences appears in the framework's sentence."),

 ("appear in every period, while cases from newly emergent diseases rise across the record",
  "KC-6.1.III.A states that diseases associated with poverty persisted while other diseases emerged as new epidemics, which is a continuity and a change at once. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in q3 above."),

 ("higher incidence merely because of increased longevity",
  "KC-6.1.III.A states that some diseases occurred at higher incidence MERELY BECAUSE OF increased longevity. The framework distinguishes that rise from the emergence of a new epidemic, and the note supplies the framework's own explanation, that more people now reach the ages at which the condition appears."),

 ("outbreak spurred the advance, running from the disease to the response",
  "KC-6.1.III.A states that these outbreaks spurred technological and medical advances, fixing the outbreak as prior and the advance as the response. A distractor reverses that order, so the anchor names the direction as well as the two terms, which is what skill 5.B's relation of one process to another requires."),

 ("Malaria, tuberculosis, and cholera",
  "The CED prints malaria, tuberculosis and cholera beside KC-6.1.III.A as illustrative examples of diseases associated with poverty. The second option is the same page's examples of emergent epidemic diseases and the third its examples of diseases associated with increased longevity, while the rest belong to KC-6.1.I.C, KC-6.1.III.B and KC-6.1.II.A."),

 ("social disruption in some cases, not in every case",
  "KC-6.1.III.A states that other diseases emerged as new epidemics and threats to human populations, IN SOME CASES leading to social disruption. The qualifier rules out the universal claim and the opposite absolute alike, so the correction must preserve the middle position and the anchor carries both halves of it."),

 ("share living with such a condition rises with each older age group",
  "KC-6.1.III.A states that some diseases occurred at higher incidence merely because of increased longevity, and a condition whose prevalence climbs with age is what makes a longer-lived population record more of it. The survey is hypothetical and is recomputed from the table alone in q8 above."),

 ("Significant effects on populations around the world",
  "KC-6.1.III states that diseases, as well as medical and scientific developments, had significant effects on populations around the world. The framework pairs the diseases with the responses to them and states that the effects were both significant and worldwide."),

 ("higher incidence merely because more people live to the ages at which they appear",
  "KC-6.1.III.A states that some diseases occurred at higher incidence MERELY BECAUSE OF increased longevity, which is a rise that is not the emergence of a new epidemic. Skill 5.B asks how one development relates to another, and the relation between an ageing population and a rising count is what the administrator's inference leaves out."),

 ("outbreak spurring technological and medical advance",
  "KC-6.1.III.A states that these outbreaks spurred technological and medical advances, and the CED prints the 1918 influenza pandemic among its illustrative examples of emergent epidemic diseases. An editorial reporting that an epidemic taught the profession about contagion is that spur described from inside the profession."),

 ("persistence of diseases associated with poverty, and the emergence of new epidemic diseases",
  "KC-6.1.III.A states that diseases associated with poverty PERSISTED WHILE other diseases emerged as new epidemics, and the word while makes the two simultaneous rather than sequential. The framework nowhere states that diseases of poverty were eliminated, which is what each distractor supposes, so the anchor carries both members of the pair."),

 ("in every decade most began within two years of a recorded outbreak",
  "KC-6.1.III.A states that these outbreaks spurred technological and medical advances, and research programmes clustering after outbreaks are one form that spur takes. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in q13 above."),

 ("Heart disease and Alzheimer's disease",
  "The CED prints heart disease and Alzheimer's disease beside KC-6.1.III.A as illustrative examples of diseases associated with increased longevity, which is the sentence about higher incidence arising merely because more people reach the relevant ages. The other options are the same page's examples of diseases of poverty and of emergent epidemics, or belong to other topics."),

 ("continuity in one kind of disease alongside a change in another",
  "KC-6.1.III.A states that diseases associated with poverty persisted while other diseases emerged as new epidemics, which is a continuity and a change side by side. The reasoning process the CED prints beside this topic is continuity and change, and the report is that process observed in one region's figures."),

 ("states that some diseases occurred at higher incidence merely because of increased longevity",
  "KC-6.1.III.A is the sentence the demographer's argument needs, and KC-6.1.I.C in the adjacent topic supplies the lengthening of life it presupposes. The framework therefore supports both halves of the argument rather than treating every rise in incidence as a new epidemic."),

 ("environmental factor affecting human populations over time",
  "Unit 9 Learning Objective B, printed on this topic's page, is to explain how environmental factors affected human populations over time, and the thematic focus the CED prints beside it is Humans and the Environment. KC-6.1.III then states that diseases had significant effects on populations around the world."),

 ("were eliminated as new epidemic diseases emerged",
  "KC-6.1.III.A states that diseases associated with poverty PERSISTED while other diseases emerged, so their elimination is the claim the framework does not support. The item asks which statement is NOT supported, so the anchor is pinned to the false one deliberately; the other four restate parts of KC-6.1.III.A."),

 ("diseases associated with poverty persisted through this period",
  "KC-6.1.III.A states that diseases associated with poverty persisted, and a waterborne infection recurring only where piped water is absent is that association and that persistence in one document. The CED prints cholera among its illustrative examples of diseases associated with poverty."),

 ("incidence of the condition within each age group, compared across the same years",
  "KC-6.1.III.A states that some diseases occurred at higher incidence MERELY BECAUSE OF increased longevity, which is a claim about the composition of a population rather than about the disease. Incidence held constant within each age group while the population ages is what would establish it, and a bare total cannot separate the two explanations."),

 ("social disruption in some cases rather than in all",
  "KC-6.1.III.A states that other diseases emerged as new epidemics and threats to human populations, IN SOME CASES leading to social disruption. A framework using some rather than all or none is one that both regions fit, so the anchor names the qualifier together with the alternative it excludes."),

 ("outbreaks spurred technological and medical advances",
  "KC-6.1.III.A fixes the direction of this relation: the outbreak comes first and the advance answers it. A research programme established in direct response to a recently identified disease is that relation documented by the laboratory itself, and the reversed relation is the distractor the anchor's wording excludes."),

 ("emerged as new epidemics and threats to human populations, in some cases leading to social disruption",
  "KC-6.1.III.A is the sentence, and the key restates it and no more of it. It names no country, no group of people and no death toll, because the framework names none, and the qualifier in some cases is carried into the anchor."),

 ("presents the outbreaks as having spurred the technological and medical advances that followed",
  "KC-6.1.III.A states that these outbreaks spurred technological and medical advances. Skill 5.B, the suggested skill for this topic, asks a student to explain how one development or process relates to another, and the framework's own sentence fixes both the pair and the direction between them."),

 ("spurred technological and medical advances, and that diseases associated with poverty persisted",
  "KC-6.1.III.A supplies both halves in one paragraph, the spur to advance and the persistence of diseases associated with poverty. Skill 5.B asks a student to relate one development to another, and the historian's double claim holds precisely because the framework asserts both together, so the anchor carries both."),

 ("higher incidence arising merely because of increased longevity",
  "KC-6.1.III.A states that some diseases occurred at higher incidence merely because of increased longevity, and an actuary attributing more claims to more policyholders reaching the relevant ages gives the framework's own reason. The framework distinguishes this from the emergence of a new epidemic, which is the distractor it is set against."),

 ("new threat or a population in which more people reach the relevant ages",
  "KC-6.1.III.A distinguishes diseases emerging as new epidemics and threats from diseases occurring at higher incidence merely because of increased longevity, which are two different explanations of the same rising number. Skill 5.B asks how one development relates to another, and which relation holds is what a rising count leaves open."),

 ("emerged as epidemics during this period alongside the diseases associated with poverty",
  "KC-6.1.III.A states that diseases associated with poverty persisted WHILE other diseases emerged as new epidemics and threats to human populations. An argument addressing only the first kind leaves the second unaccounted for, which is the complication the framework's own conjunction supplies."),

 ("continued while new epidemics appeared and some conditions rose merely because people lived longer",
  "KC-6.1.III.A gives the continuity in the persistence of diseases associated with poverty, the change in the emergence of new epidemics, and a third element, the higher incidence arising merely from increased longevity. The reasoning process the CED prints beside this topic is continuity and change, and the anchor carries all three strands."),

 ("those outbreaks drove medical and technological advance, and some conditions grew more common simply because more people lived to an age at which they appear",
  "KC-6.1.III states that diseases and the medical and scientific developments answering them had significant effects on populations around the world, and KC-6.1.III.A supplies the persistence, the emergence, the social disruption in some cases, the spur to advance, and the higher incidence arising merely from increased longevity. The key is the conjunction of those and each distractor contradicts at least one."),
]

wh.run(w9_2, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
