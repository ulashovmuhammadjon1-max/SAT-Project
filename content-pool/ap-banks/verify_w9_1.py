"""Key audit for AP WORLD HISTORY: MODERN 9.1 Advances in Technology and
Exchange After 1900.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither, because a key traceable only to an author's knowledge of the
twentieth century cannot be checked by anyone reading this bank later.

FIVE KEY CONCEPTS, AND THE CHARACTERISTIC ERROR IS CROSSING THEM. This topic
prints KC-6.1.I.A (communication and transport reduced the problem of geographic
distance), KC-6.1.I.D (energy technologies raised productivity and increased the
production of material goods), KC-6.1.III.B (better birth control gave women
greater control over fertility, transformed reproductive practices, and
contributed to declining fertility in much of the world), KC-6.1.I.B (the Green
Revolution and commercial agriculture increased productivity and sustained the
growing population as it spread chemically and genetically modified agriculture)
and KC-6.1.I.C (vaccines and antibiotics increased the ability of humans to
survive and live longer lives). Each names a technology and the change it
produced. The error a student makes is attaching a technology from one sentence
to the effect stated in another, so q16 and several distractor sets are built
from exactly that mismatch and the claims below name which sentence each key
belongs to.

THE QUALIFIERS ARE LOAD-BEARING. KC-6.1.III.B says CONTRIBUTED TO declining
rates of fertility IN MUCH OF THE WORLD -- two hedges, not one, and q14 turns on
both. KC-6.1.I.B says the Green Revolution sustained the growing population AS
IT SPREAD chemically and genetically modified forms of agriculture, so the
sentence carries a consequence alongside the benefit; q6, q17 and q22 report
both halves because a key that reported one would not be reporting the sentence.

CONTESTED GROUND. Birth control and genetically modified agriculture are
subjects on which people disagree today. Every claim below is limited to the
framework's descriptive wording and NONE endorses, condemns or recommends any of
these technologies. q17 and q24 involve sources arguing for and against, and
both key what the source claims or what would establish the facts, never whether
the source is right.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Six items are built on a reversal a prepared student could believe:

  q6   increased productivity swapped for reduced productivity
  q11  the NOT-supported item, where the key is deliberately the false claim
  q13  a population sustained swapped for a population reduced
  q14  "much of the world" swapped for "everywhere" and for "nowhere"
  q16  a technology matched to another sentence's effect
  q20  a class of energy technologies swapped for one fuel replacing all others

For each the anchor spans the whole relation, so an anchor that matched the
swapped distractor would fail the gate rather than pass it. That defect is on
record in `verify_e2_1.py`.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions.

NEGATIVE CONTROL: `python3 verify_w9_1.py --selftest`. It rotates all thirty
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
import w9_1

T_FREIGHT = w9_1._T_FREIGHT
T_ENERGY = w9_1._T_ENERGY
T_FERTILITY = w9_1._T_FERTILITY

CONSIGNMENTS = "Consignments recorded"
FAST = "Of those, carried by container ship or by air"
OTHER_WAY = "Of those, carried by other means"
TOTAL_ENERGY = "Total energy consumed"
PETRO_NUKE = "Of that, from petroleum and nuclear sources"
OTHER_ENERGY = "Of that, from other sources"
WOMEN = "Women surveyed"
USING = "Of those, reporting use of a modern method of birth control"
NOT_USING = "Of those, not reporting such use"


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


def q4(table, item):
    """A rising count whose fast-freight SHARE also rises."""
    periods = cg.labels(table)
    assert periods == ["1950s", "1970s", "1990s"], \
        f"the key speaks of each period recorded; the rows are {periods}"
    _parts_sum_to_whole(table, CONSIGNMENTS, [FAST, OTHER_WAY], "consignments recorded")
    total = cg.col(table, CONSIGNMENTS)
    fast = cg.col(table, FAST)
    other = cg.col(table, OTHER_WAY)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says consignments rose in each period; they run {total}"
    shares = [f / t for f, t in zip(fast, total)]
    assert all(b > a for a, b in zip(shares, shares[1:])), (
        f"the key says the container-and-air portion rose AS A SHARE; the shares run "
        f"{[round(s, 3) for s in shares]}")
    # every distractor false on the same numbers
    assert total[-1] > total[0], \
        "'the number of consignments fell in each period after the first' must be false"
    assert shares[-1] > shares[0], \
        "'the container-and-air share fell across the record' must be false"
    assert fast[0] > 0, \
        "'no 1950s consignment was carried by container ship or by air' must be false"
    assert not all(b > a for a, b in zip(other, other[1:])), \
        "'consignments carried by other means rose in each period' must be false"
    return (f"consignments run {total} and the container-and-air share "
            f"{[round(s, 3) for s in shares]}, both rising throughout, against {other} "
            f"carried otherwise; the parts sum to the stated wholes and all four "
            f"distractors recompute false")


def q8(table, item):
    """A rising energy total whose petroleum-and-nuclear SHARE also rises."""
    periods = cg.labels(table)
    assert periods == ["1920s", "1950s", "1980s"], \
        f"the key speaks of each period recorded; the rows are {periods}"
    _parts_sum_to_whole(table, TOTAL_ENERGY, [PETRO_NUKE, OTHER_ENERGY], "energy consumed")
    total = cg.col(table, TOTAL_ENERGY)
    pn = cg.col(table, PETRO_NUKE)
    other = cg.col(table, OTHER_ENERGY)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says total energy rose in each period; it runs {total}"
    shares = [p / t for p, t in zip(pn, total)]
    assert all(b > a for a, b in zip(shares, shares[1:])), (
        f"the key says the petroleum-and-nuclear portion rose AS A SHARE; the shares run "
        f"{[round(s, 3) for s in shares]}")
    # every distractor false on the same numbers
    assert total[-1] > total[0], \
        "'total energy fell in each period after the first' must be false"
    assert shares[-1] > shares[0], \
        "'the petroleum-and-nuclear share fell across the record' must be false"
    assert all(b > a for a, b in zip(other, other[1:])), \
        "'energy from other sources fell in each period' must be false"
    assert not all(s > 0.5 for s in shares), (
        "'petroleum and nuclear supplied more than half in every period' must be false; "
        f"the shares are {[round(s, 3) for s in shares]}")
    return (f"total energy runs {total} and the petroleum-and-nuclear share "
            f"{[round(s, 3) for s in shares]}, both rising, against {other} from other "
            f"sources; the parts sum to the stated wholes and all four distractors "
            f"recompute false")


def q12(table, item):
    """A rising share of reported use, reaching a majority only at the end."""
    periods = cg.labels(table)
    assert periods == ["1960s", "1970s", "1980s"], \
        f"the key speaks of each period recorded; the rows are {periods}"
    _parts_sum_to_whole(table, WOMEN, [USING, NOT_USING], "women surveyed")
    total = cg.col(table, WOMEN)
    using = cg.col(table, USING)
    shares = [u / t for u, t in zip(using, total)]
    assert all(b > a for a, b in zip(shares, shares[1:])), (
        f"the key says the share reporting use rose in each period; the shares run "
        f"{[round(s, 3) for s in shares]}")
    assert shares[-1] > 0.5, \
        f"the key says the last period's share was a majority; it is {shares[-1]:.3f}"
    # every distractor false on the same numbers
    assert shares[-1] > shares[0], \
        "'the share reporting use fell across the record' must be false"
    assert using[0] > 0, \
        "'no woman surveyed in the 1960s reported such use' must be false"
    assert not all(s > 0.5 for s in shares), (
        "'the share was a majority in every period' must be false; the shares are "
        f"{[round(s, 3) for s in shares]}")
    assert all(b > a for a, b in zip(total, total[1:])), \
        "'the number of women surveyed fell in each period' must be false"
    return (f"the share reporting use runs {[round(s, 3) for s in shares]} of totals "
            f"{total}, rising throughout and a majority only in the last period; the parts "
            f"sum to the stated wholes and all four distractors recompute false")


TABLE_CHECKS = {4: q4, 8: q8, 12: q12}

CLAIMS = [
 ("reduced the problem of geographic distance",
  "KC-6.1.I.A states that new modes of communication, including radio communication, cellular communication, and the internet, as well as transportation, including air travel and shipping containers, reduced the problem of geographic distance. A container crossing an ocean unopened and a message arriving the same day are the transport and communication halves of that one sentence, which is why the framework groups them."),

 ("Radio communication, cellular communication, and the internet",
  "KC-6.1.I.A names exactly these three as the new modes of COMMUNICATION. Shipping containers and air travel appear in the same sentence as transportation rather than communication, and the remaining lists belong to KC-6.1.I.C, KC-6.1.III.B, KC-6.1.I.D and KC-6.1.I.B, which is the cross-sentence error this item is built to catch."),

 ("energy technologies raising productivity and increasing the production of material goods",
  "KC-6.1.I.D states that energy technologies, including the use of petroleum and nuclear power, raised productivity and increased the production of material goods. A power station letting factories run longer and produce more is both halves of that sentence, so the anchor carries both."),

 ("share carried by container ship or by air rose with it",
  "KC-6.1.I.A names shipping containers and air travel among the transportation developments that reduced the problem of geographic distance, and a rising share of freight moving by those means is one form that reduction takes. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in q4 above."),

 ("medical innovations, including vaccines and antibiotics, that increased the ability of humans to survive and live longer lives",
  "KC-6.1.I.C states that medical innovations, including vaccines and antibiotics, increased the ability of humans to survive and live longer lives. Inoculation against a childhood disease and a postwar class of medicines making infections survivable are the two innovations that sentence names."),

 ("increased productivity and sustained the earth's growing population as it spread chemically modified forms of agriculture",
  "KC-6.1.I.B states that the Green Revolution and commercial agriculture increased productivity and sustained the earth's growing population as it spread chemically and genetically modified forms of agriculture. The framework carries the yield and the spread of modified agriculture in one sentence, and a distractor reverses productivity into a reduction, so the anchor spans the whole of it."),

 ("changed something about how far, how much, how long or how many people could live and produce",
  "KC-6.1.I.A reduces the problem of distance, KC-6.1.I.D raises productivity and output, KC-6.1.I.C lengthens life, KC-6.1.I.B sustains a growing population and KC-6.1.III.B alters fertility. Skill 5.A asks a student to identify patterns among or connections between developments, and that common effect is the pattern."),

 ("portion from petroleum and nuclear sources rose as a share of the total",
  "KC-6.1.I.D states that energy technologies, including the use of petroleum and nuclear power, raised productivity and increased the production of material goods, and a rising share of a rising total is one form the growth of those technologies takes. The index is hypothetical and is recomputed from the table alone in q8 above."),

 ("gave women greater control over fertility and contributed to declining rates of fertility",
  "KC-6.1.III.B states that more effective forms of birth control gave women greater control over fertility, transformed reproductive practices, and contributed to declining rates of fertility in much of the world. Fewer births together with decisions about their timing are the control and the decline that sentence names, so the anchor carries both."),

 ("new modes of communication, as part of the reduction of the problem of geographic distance",
  "KC-6.1.I.A puts new modes of communication and new modes of transportation, air travel among them, in a single sentence whose effect is the reduction of the problem of geographic distance. Skill 5.A asks for connections between developments, and the framework's own sentence places these two side by side."),

 ("energy technologies of the century reduced the production of material goods",
  "KC-6.1.I.D states that energy technologies raised productivity and INCREASED the production of material goods, so a reduction reverses the framework's sentence. The item asks which statement is NOT supported, so the anchor is pinned to the false claim deliberately; the other four restate KC-6.1.I.A, KC-6.1.I.C, KC-6.1.I.B and KC-6.1.III.B."),

 ("in the last period recorded it was a majority",
  "KC-6.1.III.B states that more effective forms of birth control gave women greater control over fertility and contributed to declining rates of fertility in much of the world, and a rising share reporting use is one measure of that spread. The survey is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in q12 above."),

 ("first lengthened lives and the second sustained the growing population that resulted",
  "KC-6.1.I.C states that medical innovations increased the ability of humans to survive and live longer lives, and KC-6.1.I.B that the Green Revolution and commercial agriculture sustained the earth's GROWING population. A distractor has the second reducing the population instead, so the anchor carries both halves of the connection skill 5.A asks a student to identify."),

 ("declining rates of fertility in much of the world, not in all of it",
  "KC-6.1.III.B carries two hedges the framework chose: CONTRIBUTED TO declining rates of fertility, and IN MUCH OF THE WORLD. The correction must keep both rather than replace one overstatement with another, so the anchor names the qualifier together with what it excludes."),

 ("communication and transportation working together to reduce the problem of geographic distance",
  "KC-6.1.I.A names new modes of communication and new modes of transportation, including shipping containers, in one sentence whose stated effect is the reduction of the problem of geographic distance. Drawings sent in minutes and goods returned in standard boxes are the two halves of that sentence in one commercial arrangement."),

 ("Antibiotics, matched with an increased ability of humans to survive and live longer lives",
  "KC-6.1.I.C names vaccines and antibiotics as the medical innovations that increased the ability of humans to survive and live longer lives. Each distractor takes a technology the framework names in one sentence and attaches it to the effect stated in a different one, so the anchor has to carry the technology and its own effect together."),

 ("spread of chemically and genetically modified forms of agriculture",
  "KC-6.1.I.B states that the Green Revolution and commercial agriculture increased productivity and sustained the earth's growing population AS IT SPREAD chemically and genetically modified forms of agriculture. An account confined to yields leaves out half of the framework's sentence. The key states what the framework states and takes no position on whether the methods are good or bad."),

 ("greater control over fertility and transformed reproductive practices",
  "KC-6.1.III.B names three changes: greater control over fertility, transformed reproductive practices, and declining rates of fertility in much of the world. The item asks for the two beyond the rate itself, so the anchor carries both of them."),

 ("Distance made less of an obstacle, output raised, harvests enlarged, and lives lengthened",
  "KC-6.1.I.A, KC-6.1.I.D, KC-6.1.I.B and KC-6.1.I.C between them record a reduced problem of distance, raised productivity and output, a sustained growing population and longer lives. Skill 5.A asks a student to identify a pattern among developments, and the distractor sets name developments the framework places in other units and topics."),

 ("names petroleum and nuclear power together rather than one replacing all others",
  "KC-6.1.I.D states that energy technologies, INCLUDING the use of petroleum and nuclear power, raised productivity and increased the production of material goods. The sentence names two together inside a wider class and asserts no replacement of one by another, so a claim of universal obsolescence goes past what the framework supports."),

 ("new mode of communication reducing the problem of geographic distance",
  "KC-6.1.I.A names radio communication first among the new modes of communication that reduced the problem of geographic distance. Hearing a distant event as it happens is that reduction in its earliest form, and the framework distinguishes communication from the transportation named in the same sentence."),

 ("increased productivity and sustained a growing population while spreading modified forms of agriculture",
  "KC-6.1.I.B states that the Green Revolution and commercial agriculture increased productivity and sustained the earth's growing population as it spread chemically and genetically modified forms of agriculture. The key carries the yield, the population and the spread of modified methods because the sentence names all three."),

 ("vaccination coverage and of deaths from infections treatable by antibiotics",
  "KC-6.1.I.C states that medical innovations, INCLUDING vaccines and antibiotics, increased the ability of humans to survive and live longer lives, so vaccination coverage and deaths from treatable infections are the direct measures. The other records bear on KC-6.1.I.A, KC-6.1.I.D and KC-6.1.I.B rather than on the claim in question."),

 ("each describes the same development from a different position",
  "Skill 5.A asks a student to identify patterns among or connections between historical developments, which requires establishing what a development was before judging it. KC-6.1.I.B and KC-6.1.III.B describe changes people argued about then and argue about now, and the framework's sentences describe the changes rather than settling the arguments."),

 ("reduction of the problem of geographic distance by new modes of transportation",
  "KC-6.1.I.A states that transportation, including air travel and shipping containers, reduced the problem of geographic distance. A cost of moving goods falling faster than the cost of making them is that reduction stated economically, and it is distinct from the productivity gain KC-6.1.I.D attributes to energy technologies."),

 ("when and whether people have children, decided by the women concerned",
  "KC-6.1.III.B distinguishes three things in one sentence: greater control over fertility, transformed reproductive practices, and declining rates of fertility. A change in who decides and when is the practice, while a count of births in a year is the rate, which is the distinction this item turns on."),

 ("energy technologies raised productivity and increased the production of material goods",
  "KC-6.1.I.D is the sentence the paper's premise rests on: that output depends on power. Each distractor names a change the framework attributes to a different technology in a different sentence."),

 ("technology whose spread the framework connects to a measurable change in how people lived",
  "KC-6.1.I.A, KC-6.1.I.B, KC-6.1.I.C, KC-6.1.I.D and KC-6.1.III.B each pair a technology with a stated change: distance, yields and population, survival and longevity, productivity and output, and control over fertility. Skill 5.A asks for the pattern among developments, and technology joined to a measurable change in living is it."),

 ("development of new technologies changed the world from 1900 to the present",
  "Unit 9 Learning Objective A is to explain how the development of new technologies changed the world from 1900 to present, and it is the objective printed on this topic's page. The distractors name the learning objectives of other topics in this course."),

 ("new agriculture fed a growing population while spreading modified methods, medicine lengthened life",
  "KC-6.1.I.A supplies the reduced problem of distance, KC-6.1.I.D the raised productivity and output, KC-6.1.I.B the sustained growing population and the spread of modified agriculture, KC-6.1.I.C the longer lives, and KC-6.1.III.B the greater control over fertility. The key is the conjunction of those five and each distractor contradicts at least one."),
]

wh.run(w9_1, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
