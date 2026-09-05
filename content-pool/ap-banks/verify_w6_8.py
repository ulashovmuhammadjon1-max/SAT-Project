"""Key audit for AP WORLD HISTORY: MODERN 6.8 Causation in the Imperial Age.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The gate is ``wh_check.run``, the shared World History gate: ``cg_check.check``
for structure and anchors, ``es_check.style`` for notation (World History is a
prose subject that ``export_units.py`` does not typeset), plus the two rules
history adds -- a CED citation in every ``why`` and every ``claim``, and no
figure language, since the bank cannot display an image.

WHAT THE KEYS REST ON, AND WHY THIS TOPIC IS DIFFERENT
------------------------------------------------------
6.8 is the unit's FINAL topic, and the CED prints no new historical development
for it. What it prints is a skill, an objective and a review:

    Unit 6 Learning Objective I  Explain the relative significance of the effects
                                 of imperialism from 1750 to 1900.
    Suggested skill 6.D          Corroborate, qualify, or modify an argument using
                                 diverse and alternative evidence in order to
                                 develop a complex argument. This argument might:
                                 explain nuance of an issue by analyzing multiple
                                 variables; explain relevant and insightful
                                 connections within and across periods; explain
                                 the relative historical significance of a
                                 source's credibility and limitations; explain how
                                 or why a historical claim or argument is or is not
                                 effective.
    KC-5.1  The development of industrial capitalism led to increased standards of
            living FOR SOME, and to continued improvement in manufacturing methods
            that increased the availability, affordability, and variety of consumer
            goods.
    KC-5.2  As states industrialized, they also expanded existing overseas empires
            and established new colonies and transoceanic relationships.
    KC-5.3  The 18th century marked the beginning of an intense period of revolution
            and rebellion against existing governments, leading to the
            establishment of new nation-states around the world.
    KC-5.4  As a result of the emergence of transoceanic empires and a global
            capitalist economy, migration patterns changed dramatically, and the
            numbers of migrants increased significantly.

So the module is a REASONING set, as HISTORY_BRIEF.md requires of a unit's final
topic. Items 1, 2, 16 rest on Learning Objective I and the CED's own description
of what a final topic is for. Items 3 to 7 rest on the four bullets of suggested
skill 6.D, one each. Items 8 to 11 rest on the four review key concepts. Items
12, 13, 17, 18, 19, 20, 27, 28 apply 6.D to an argument, and their claims cite
the unit statement each argument is weighed against. Items 14, 15 are causation
items about the DIRECTION of a review statement. Items 29 and 30 concern what
the framework settles and what it leaves to the student to argue.

THREE THINGS THIS FILE IS BUILT TO CATCH
----------------------------------------
1. KC-5.1's qualification, "for some", is the most useful sentence in the topic
   and the easiest to drop. Items 8, 12, 22 and 30 all carry it, and the anchors
   for 8 and 30 include it so a key that overstated it could not match.
2. Causation is the reasoning process, so the direction of KC-5.2 and KC-5.4 is
   the content of items 14 and 15. Each offers the exact reversal, so each anchor
   carries both clauses.
3. AN ASSOCIATION IS NOT A CAUSE. Item 24 keys on that, and the table check
   below is written to make the point checkable rather than asserted: it
   CONFIRMS the association is real and strictly monotonic, so the objection
   cannot be that the pattern is absent or reversed, and the only thing left
   standing between the pattern and a cause is the inference itself.

DATA ITEMS: 21 to 26 carry tables labelled hypothetical in the stem, and every
keyed conclusion is recomputed below from that table alone. Row labels and the
two categorical columns of the resistance record are matched EXACTLY rather than
by substring, because ``es_check._corrupt`` appends " CORRUPTED" to a cell and a
substring test would still read "Religious CORRUPTED" as a religious appeal --
the control would pass while proving nothing.

NEGATIVE CONTROL: ``python3 verify_w6_8.py --selftest`` runs wh_check's full
control set -- every key rotated, every anchor broken, every table cell
corrupted, every banned notation form injected against legal prose that must
pass, figure language injected against the two phrases this project has seen
falsely flagged, an uncited why and an uncited claim, a duplicate choice, a thin
why and a why naming an option by letter -- and each control asserts WHICH
message came back. It then runs legal-value controls on the guards a corrupted
cell cannot reach, since such a cell trips the label vocabulary or an index
bound first.
"""
import sys

import cg_check as cg
import wh_check as wh
import w6_8

OWN_START = "Households in every hundred owning it at the start of the period"
OWN_END = "Households in every hundred owning it at the end of the period"
GOODS = ["A factory-woven cotton garment", "A cast-iron cooking vessel",
         "A printed book or newspaper", "A clock or watch"]

CONC = "Share of export earnings from its single largest commodity (percent)"
URBAN = "Share of its population living in towns at the end of the period (percent)"
TERRITORIES = ["Territory 1", "Territory 2", "Territory 3", "Territory 4"]

EVIDENCE = "Evidence the claim rests on"
MECHANISM = "Whether the claim states a mechanism"
CLAIM_ROWS = ["Claim 1", "Claim 2", "Claim 3", "Claim 4"]
ONE_SOURCE = "One official report"
DIVERSE = "Several kinds of source, including ones that disagree"
EVIDENCE_KINDS = {ONE_SOURCE, DIVERSE}
YES, NO = "Yes", "No"
MECHANISM_VALUES = {YES, NO}


def _rows(table):
    idx = {h: j for j, h in enumerate(table["headers"])}
    return [{h: str(r[j]) for h, j in idx.items()} for r in table["rows"]]


def _by_label(table, expected):
    """Rows keyed by an EXACT first-column label drawn from `expected`.

    Exact membership, never a substring test. The negative control corrupts a
    cell by appending " CORRUPTED"; a substring test would still read
    "Group 4 CORRUPTED" as Group 4, and the control would pass without
    exercising anything.
    """
    rows = _rows(table)
    label_col = table["headers"][0]
    got = [r[label_col] for r in rows]
    assert got == list(expected), f"row labels must be {list(expected)}, not {got}"
    return {r[label_col]: r for r in rows}


def _goods(table):
    by = _by_label(table, GOODS)
    out = {}
    for name in GOODS:
        s, e = cg.num(by[name][OWN_START]), cg.num(by[name][OWN_END])
        # Both columns count households in every hundred, so a value outside 0 to
        # 100 is not a reading. This is the bound that catches half the corrupted
        # cells; the ordering guard in q21 catches the rest.
        for v, which in ((s, "start"), (e, "end")):
            assert 0 <= v <= 100, \
                f"{name} {which} is {v:g}, which is not a count in every hundred households"
        out[name] = (s, e)
    return out


def q21(table, item):
    v = _goods(table)
    assert all(e > s for s, e in v.values()), \
        f"every good must reach more households for the keyed reading: {v}"
    rises = {k: e - s for k, (s, e) in v.items()}
    by_start = sorted(v, key=lambda k: -v[k][0])
    ordered = [rises[k] for k in by_start]
    # The key and the reversed distractor differ only in WHICH end of the starting
    # order spread furthest, so the check has to fix the direction, not merely the
    # fact of a spread. Strict ordering also means no corrupted cell can leave the
    # pattern intact.
    assert all(b < a for a, b in zip(ordered, ordered[1:])), \
        f"ranked by starting share the rises must fall strictly: {ordered}"
    assert len(set(rises.values())) == len(rises), "'the same extent' must be false"
    assert len([k for k in rises if rises[k] > 0]) == 4, \
        "'none spread' and 'only one spread' must both be false"
    return (f"ranked by starting share the rises run {ordered}, so all four spread and the "
            "commonest spread furthest")


def q22(table, item):
    v = _goods(table)
    assert all(e > s for s, e in v.values()), \
        "the first clause of the key requires every good to reach more households"
    # The second clause says the record cannot reach wellbeing. That is checkable
    # against the table's own columns: it counts households owning goods and
    # reports no income, wage, group or person, so nothing in it measures how any
    # member of the society fared.
    heads = " ".join(table["headers"]).lower()
    for word in ("income", "wage", "earnings", "standard of living", "wellbeing"):
        assert word not in heads, \
            f"a column naming {word!r} would let the record speak to wellbeing after all"
    assert "households" in heads and "owning" in heads, \
        "the record must count households owning goods, which is what limits its reach"
    return ("all four goods reach more households, while every column counts ownership and "
            "none reports an income or a condition, so the record stops short of wellbeing")


def _territories(table):
    by = _by_label(table, TERRITORIES)
    out = {}
    for name in TERRITORIES:
        c, u = cg.num(by[name][CONC]), cg.num(by[name][URBAN])
        for v, which in ((c, "concentration"), (u, "urban share")):
            assert 0 <= v <= 100, f"{name} {which} is {v:g}, which is not a percentage"
        out[name] = (c, u)
    return out


def q23(table, item):
    t = _territories(table)
    ordered = sorted(t.values(), key=lambda p: -p[0])
    urban = [u for _c, u in ordered]
    assert all(b > a for a, b in zip(urban, urban[1:])), \
        f"urban shares must rise strictly as concentration falls: {urban}"
    conc = [c for c, _u in ordered]
    assert len(set(conc)) == len(conc), "'the same export concentration' must be false"
    assert len(urban) == 4, "the stem says four territories and both columns must be given"
    return (f"ranked by concentration the urban shares run {urban}, so the two columns move "
            "strictly in opposite directions")


def q24(table, item):
    t = _territories(table)
    ordered = sorted(t.values(), key=lambda p: -p[0])
    urban = [u for _c, u in ordered]
    # The objection in the key is NOT that the pattern is missing or reversed, so
    # the check has to confirm the pattern is real and in the direction the student
    # describes. What remains unwarranted is the step from that pattern to a cause,
    # and no arithmetic can license or refuse that step -- which is the point of
    # the item and the reason this check states its own limit.
    assert all(b > a for a, b in zip(urban, urban[1:])), \
        "'the table shows no association' must be false: the association is real"
    assert urban[0] < urban[-1], \
        "'the table shows the opposite association' must be false"
    assert len(t) == 4, f"the key says four territories; the table holds {len(t)}"
    return ("the association is real and strictly monotonic across all four territories, so "
            "the only thing left unwarranted is the step from it to a cause")


def _arguments(table):
    by = _by_label(table, CLAIM_ROWS)
    out = {}
    for name in CLAIM_ROWS:
        e, m = by[name][EVIDENCE], by[name][MECHANISM]
        assert e in EVIDENCE_KINDS, f"{name}: unexpected evidence {e!r}"
        assert m in MECHANISM_VALUES, f"{name}: unexpected mechanism entry {m!r}"
        out[name] = (e, m)
    return out


def q25(table, item):
    a = _arguments(table)
    both = [k for k, (e, m) in a.items() if e == DIVERSE and m == YES]
    # Uniqueness before identity, so a tie is reported as a tie. If two rows met
    # both tests, naming only the first would let a control aimed at the
    # uniqueness guard be answered by the identity assert instead, which proves
    # nothing about the guard it names -- a mistake this session made twice and
    # caught only because the controls check the message.
    assert len(both) == 1, f"exactly one claim may meet both tests; got {both}"
    assert both == ["Claim 2"], f"the claim meeting both tests is {both}, not Claim 2"
    # Each rejected claim must satisfy AT MOST one test, or it would be defensible.
    for name, (e, m) in a.items():
        if name == both[0]:
            continue
        assert not (e == DIVERSE and m == YES), f"{name} also meets both tests"
    assert any(e == DIVERSE for e, _m in a.values()), "the evidence column must vary"
    assert any(m == YES for _e, m in a.values()), "the mechanism column must vary"
    return ("Claim 2 alone both rests on several kinds of source including ones that "
            "disagree and states a mechanism; every other claim meets at most one test")


def q26(table, item):
    a = _arguments(table)
    with_mechanism = [k for k, (_e, m) in a.items() if m == YES]
    # The student's premise must be TRUE of the record -- two claims do state a
    # mechanism -- or the item would be answering a premise the table denies.
    assert len(with_mechanism) == 2, \
        f"the student compares two claims that state a mechanism; the record holds {len(with_mechanism)}"
    kinds = {a[k][0] for k in with_mechanism}
    assert kinds == EVIDENCE_KINDS, \
        "the two claims stating a mechanism must differ in their evidence, which is the point"
    weaker = [k for k in with_mechanism if a[k][0] == ONE_SOURCE]
    stronger = [k for k in with_mechanism if a[k][0] == DIVERSE]
    assert len(weaker) == 1 and len(stronger) == 1, \
        f"one of each is required; got weaker {weaker} and stronger {stronger}"
    return (f"{weaker[0]} and {stronger[0]} both state a mechanism and differ only in their "
            "evidence, one official report against several disagreeing kinds of source")


TABLE_CHECKS = {21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26}

CLAIMS = [
 ("The relative significance of the effects of imperialism from 1750 to 1900",
  "Unit 6 Learning Objective I verbatim. The word relative is the framework's own and asks for a weighing, not for the dates, biographies or preselected effect the rejected options offer."),
 ("draw upon the key concepts and historical developments they have studied in the unit",
  "The CED's description of this topic states that the final topic in the unit focuses on the skill of argumentation and provides an opportunity for students to draw upon the key concepts and historical developments they have studied in the unit, using evidence relevant to those key concepts. It introduces no new development and no new period, which is why Unit 6 Learning Objective I is a skill objective."),
 ("Corroborate it, qualify it, or modify it",
  "Suggested skill 6.D reads: corroborate, qualify, or modify an argument using diverse and alternative evidence in order to develop a complex argument. Those three verbs are the framework's own; repeating, accepting or rejecting an argument outright is none of them, and Unit 6 Learning Objective I is the objective they serve."),
 ("Explain nuance of an issue by analyzing multiple variables",
  "Suggested skill 6.D lists this among the things a complex argument might do. Reducing an issue to a single variable or to one person's intentions is its opposite, and declaring every variable equally important abandons the weighing Unit 6 Learning Objective I asks for."),
 ("Explain the relative historical significance of a source's credibility and limitations",
  "Suggested skill 6.D lists this among the things a complex argument might do. It is a judgement about what a particular source can and cannot show, which is neither a blanket ruling on all sources, nor a count, nor a preference for length, and it serves Unit 6 Learning Objective I's demand for relative significance."),
 ("Explain relevant and insightful connections within and across periods",
  "Suggested skill 6.D lists this among the things a complex argument might do. Confining an argument to one topic or refusing to relate periods is what it rules out, and Unit 6 Learning Objective I asks students to weigh effects running across the unit's topics."),
 ("Explain how or why a historical claim or argument is or is not effective",
  "Suggested skill 6.D lists this among the things a complex argument might do. It asks for reasons about the claim itself, which no blanket verdict, no judgement of the author's standing and no measure of confidence supplies, and Unit 6 Learning Objective I expects such reasons to be given."),
 ("Their availability, their affordability and their variety",
  "KC-5.1, printed in this unit's review, states that continued improvement in manufacturing methods increased the availability, affordability, and variety of consumer goods. Those three nouns are the framework's own, and every rejected option drops one of them or substitutes a list the sentence does not contain."),
 ("expanded existing overseas empires and established new colonies and transoceanic relationships",
  "KC-5.2, printed in this unit's review: as states industrialized, they also expanded existing overseas empires and established new colonies and transoceanic relationships. All three are asserted together, so an option keeping one and denying the others misreports the sentence."),
 ("The establishment of new nation-states around the world",
  "KC-5.3, printed in this unit's review, states that the intense period of revolution and rebellion against existing governments led to the establishment of new nation-states around the world. Consolidation of existing governments and abolition of the nation-state are each the reverse of that clause."),
 ("migration patterns changed dramatically, and that the numbers of migrants increased significantly",
  "KC-5.4, printed in this unit's review, asserts both in one sentence: migration patterns changed dramatically AND the numbers of migrants increased significantly. The anchor carries both clauses because a distractor keeps one half and reverses the other. Item 15 covers the CAUSE side of the same sentence, so this item does not repeat it."),
 ("raised standards of living for some",
  "KC-5.1's own wording is increased standards of living FOR SOME, which is narrower than the student's everyone and therefore limits the claim rather than contradicting or confirming it. Suggested skill 6.D calls that qualifying; KC-5.2, KC-5.3 and KC-5.4 concern empire, revolution and migration and bear on this claim only indirectly."),
 ("qualifying the argument",
  "Suggested skill 6.D names corroborate, qualify and modify as what a student may do to an argument with diverse and alternative evidence. Narrowing where a claim holds while keeping the claim is what qualifying means, and it is neither confirmation without change nor rejection. Unit 6 Learning Objective I asks for exactly this kind of weighing."),
 ("reverses the direction the review gives, which runs from states industrializing to their expanding empires",
  "KC-5.2 reads that AS STATES INDUSTRIALIZED, they also expanded existing overseas empires and established new colonies, which puts industrialization first in that sentence. Causation is this topic's reasoning process, so the anchor carries both clauses because the exact reversal is offered as a distractor."),
 ("reverses the direction the review gives, which makes changed migration the result of those empires and that economy",
  "KC-5.4 reads that AS A RESULT OF the emergence of transoceanic empires and a global capitalist economy, migration patterns changed dramatically. The phrase as a result of fixes which side is the cause, and the anchor carries both clauses because the exact reversal is offered."),
 ("weigh the effects against one another and give reasons for ranking them",
  "Unit 6 Learning Objective I asks students to explain the relative significance of the effects of imperialism from 1750 to 1900, and suggested skill 6.D asks for a complex argument built with diverse evidence. A ranking with reasons is what those require; a bare list, an easy choice, a flat declaration of equality and a page count each avoid the weighing."),
 ("the unit names economic and strategic factors alongside the ideological ones",
  "KC-5.2.III names the ideologies used to justify imperialism, while KC-5.1.II.A names the need for raw materials and food supplies and KC-5.1.II.C and KC-5.2.I.E describe trade organized to European and American advantage and economic imperialism. Suggested skill 6.D asks students to explain nuance by analyzing multiple variables, and it does not follow that ideology played no part."),
 ("credibility and its limitations both bear on how much the argument can carry",
  "Suggested skill 6.D asks students to explain the relative historical significance of a source's credibility and limitations, which is a judgement about what a source can bear rather than a verdict of proof or worthlessness. KC-5.4.III.C and KC-5.2.I.A are framework statements rather than any one official's report, which is why a single document cannot settle a claim of this size."),
 ("because it states a mechanism and offers evidence a reader can test",
  "Suggested skill 6.D asks students to explain how or why a historical claim or argument is or is not effective, so effectiveness is a judgement the framework expects to be defended. Naming a process and citing evidence gives a reader something to check, which brevity, confidence and length do not, and Unit 6 Learning Objective I asks for the reasons behind a weighing."),
 ("parts of one interconnected system",
  "KC-5.1.II.A describes export economies growing to supply factories and urban populations, and KC-5.4 states that migration patterns changed as a result of transoceanic empires and a global capitalist economy. Suggested skill 6.D asks for relevant connections within and across periods, and these two statements describe one economy from two sides rather than unrelated or opposed developments."),
 ("the goods that were already commonest spread furthest",
  "Recomputed in q21 above: ranked by starting share the rises run 61, 56, 42 and 22, strictly falling, so all four goods spread and the commonest spread furthest. The exact reversal of that direction is offered as a distractor, so the anchor carries it. KC-5.1 states that continued improvement in manufacturing methods increased the availability, affordability, and variety of consumer goods."),
 ("It establishes that these four goods reached more households, but not that every member of the society was better off",
  "Recomputed in q22 above, and BOTH clauses are checked: every good reaches more households, and no column of the record names an income, a wage or a standard of living, so nothing in it measures how any member of the society fared. KC-5.1 keeps the two apart itself, and suggested skill 6.D asks for the relative significance of a source's credibility and limitations. The anchor carries both clauses because the exact reversal is offered."),
 ("The territories with the most concentrated exports have the smallest urban shares",
  "Recomputed in q23 above: ranked by concentration the urban shares run 14, 19, 38 and 44, so the two columns move strictly in opposite directions across all four rows. KC-5.1.II.A describes export economies specializing in extraction and in food and industrial crops, which is what the first column measures."),
 ("which does not by itself establish which way any cause ran or whether a third factor produced both",
  "Recomputed in q24 above, which CONFIRMS the association is real and strictly monotonic, so the objection cannot be that the pattern is absent or reversed. Causation is this topic's reasoning process and suggested skill 6.D asks for nuance across multiple variables, which is what a jump from four associated cases to a single cause skips. Unit 6 Learning Objective I asks for a weighing of effects, which rests on knowing which way a cause ran."),
 ("Claim 2",
  "Recomputed in q25 above: exactly one row both rests on several kinds of source including ones that disagree and states a mechanism, and every other row is checked to meet at most one of those tests. Suggested skill 6.D asks for diverse and alternative evidence and for an explanation of how or why a claim is effective, and Unit 6 Learning Objective I asks for reasons behind a weighing, which is what a stated mechanism supplies."),
 ("The weaker claim rests on one official report, while the stronger rests on several kinds of source including ones that disagree",
  "Recomputed in q26 above: exactly two rows state a mechanism, so the student's premise is true of the record, and those two differ only in their evidence. Suggested skill 6.D asks for the relative historical significance of a source's credibility and limitations and for diverse and alternative evidence; the anchor carries both clauses because the reversal of which claim rests on which is offered. Unit 6 Learning Objective I asks students to defend a weighing, which is what the evidence behind a claim decides."),
 ("anti-imperial resistance took various forms, including direct resistance within empires and the creation of new states on the peripheries",
  "KC-5.2.II.C verbatim, and it is broader than rebellion alone, so it limits the student's claim rather than refuting it. KC-5.3.III.E, that discontent led to rebellions some of which were influenced by religious ideas, is the statement the student has generalized from, and suggested skill 6.D calls this qualifying."),
 ("more than one kind of source or vantage point, including ones that do not simply agree with the argument",
  "Suggested skill 6.D asks students to corroborate, qualify or modify an argument using DIVERSE AND ALTERNATIVE evidence, and an argument can only be qualified or modified by evidence that does not merely repeat it. A count of documents, a selection of congenial ones, a single category of source and a language test are none of them that, and Unit 6 Learning Objective I's weighing needs the same breadth."),
 ("which single effect was the most significant cannot, since that is the argument the student is asked to make",
  "The unit review names KC-5.1, KC-5.2, KC-5.3 and KC-5.4, so the kinds of effect are settled by the framework. Unit 6 Learning Objective I asks students to explain relative significance, which makes the ranking the argument to be defended rather than a fact to look up. The anchor carries both clauses because the exact reversal is offered."),
 ("Industrial capitalism raised living standards for some and improved manufacturing",
  "KC-5.1, KC-5.2, KC-5.3 and KC-5.4 are the four statements the CED prints as this unit's review, and the key states each in turn, including KC-5.1's qualification that living standards rose for some. Each rejected option deletes one of the four or overstates KC-5.1, and Unit 6 Learning Objective I asks students to weigh them rather than to drop any."),
]


# --------------------------------------------------------- legal-value controls
#
# wh_check's cell control appends " CORRUPTED", which trips the exact label and
# category vocabularies, and multiplies a number by three and adds eleven, which
# the percentage and index bounds catch first. Both are real guards, but neither
# is the guard that makes a keyed reading the only defensible one. So each of
# those gets a control that substitutes one LEGAL value for another: the table
# stays well formed and the only thing that changes is whether the key still
# stands. Each control asserts on the MESSAGE, because a control that fires for
# the wrong reason proves nothing about the guard it names.

def _fires(base, mutate, check, needle, label):
    import copy
    table = copy.deepcopy(base)
    mutate(table["rows"])
    try:
        check(table, None)
    except AssertionError as exc:
        assert needle in str(exc), \
            f"CONTROL FIRED FOR THE WRONG REASON ({label}): expected {needle!r}, got {exc}"
        return
    raise SystemExit(f"CONTROL FAILED: {label} -- {check.__name__} accepted the mutation")


def legal_value_control():
    gds, ter, arg = w6_8._T_GOODS, w6_8._T_TERRITORIES, w6_8._T_ARGUMENTS

    # 95 is a legal count in every hundred, and it makes the RAREST good spread
    # furthest -- which is the reversed distractor item 21 must reject. The
    # ordering guard is the only thing that can catch it, since every good still
    # reaches more households.
    _fires(gds, lambda rows: rows[3].__setitem__(2, "95"), q21,
           "ranked by starting share the rises must fall strictly",
           "item 21 with the rarest good spreading furthest")
    # 20 is a legal count and puts one good below where it began, so the first
    # clause of item 22's key no longer holds.
    _fires(gds, lambda rows: rows[0].__setitem__(2, "20"), q22,
           "requires every good to reach more households",
           "item 22 with one good reaching fewer households")
    # A header naming an income would let the record speak to wellbeing, which is
    # exactly what the second clause of item 22's key denies. This control mutates
    # a HEADER rather than a cell, because no cell corruption can reach that guard.
    import copy as _copy
    _mutated = _copy.deepcopy(gds)
    # The LABEL column is renamed, not a data column: _by_label reads headers[0]
    # dynamically, so the record still parses and the guard under test is the only
    # thing that can fire. Renaming a data column instead raised a KeyError from
    # the lookup -- a control firing for the wrong reason, caught by this control
    # asserting on the message rather than on the fact of an exception.
    _mutated["headers"][0] = "Consumer good, and the real income of the households owning it"
    try:
        q22(_mutated, None)
    except AssertionError as exc:
        assert "would let the record speak to wellbeing" in str(exc), \
            f"CONTROL FIRED FOR THE WRONG REASON (item 22 with an income column): {exc}"
    else:
        raise SystemExit("CONTROL FAILED: item 22 accepted a record carrying an income column")

    # 46 is a legal percentage and breaks the monotone pattern without removing
    # the columns, so the guard under test is the ordering itself.
    _fires(ter, lambda rows: rows[1].__setitem__(2, "46"), q23,
           "urban shares must rise strictly as concentration falls",
           "item 23 with the pattern broken in the middle")
    _fires(ter, lambda rows: rows[1].__setitem__(2, "46"), q24,
           "the association is real", "item 24 with the association no longer monotonic")

    # A legal entry, but it gives Claim 3 a mechanism too, so two rows now meet
    # both of item 25's tests and the key is no longer the only defensible answer.
    _fires(arg, lambda rows: rows[2].__setitem__(2, "Yes"), q25,
           "exactly one claim may meet both tests", "item 25 with two claims meeting both tests")
    # A legal entry that takes the mechanism away from Claim 4, so the student's
    # premise in item 26 -- that two claims state a mechanism -- is no longer true
    # of the record and the item would have nothing to compare.
    _fires(arg, lambda rows: rows[3].__setitem__(2, "No"), q26,
           "the student compares two claims that state a mechanism",
           "item 26 with only one claim stating a mechanism")
    # A legal entry that makes both mechanism-stating claims rest on the same kind
    # of evidence, which removes the very difference the key names.
    _fires(arg, lambda rows: rows[3].__setitem__(1, DIVERSE), q26,
           "must differ in their evidence", "item 26 with the evidence difference removed")

    # POSITIVE control: the same six checks must ACCEPT the module's own tables,
    # so a check that rejected everything would be caught here rather than counted
    # as several successes.
    for fn in (q21, q22):
        fn(gds, None)
    for fn in (q23, q24):
        fn(ter, None)
    for fn in (q25, q26):
        fn(arg, None)
    print("  control OK  every uniqueness, ordering and qualification guard fires on a "
          "legal-value mutation, for the reason it names, and passes the real tables")


if "--selftest" in sys.argv:
    legal_value_control()

wh.run(w6_8, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
