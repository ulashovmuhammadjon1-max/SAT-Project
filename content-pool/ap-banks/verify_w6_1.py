"""Key audit for AP WORLD HISTORY: MODERN 6.1 Rationales for Imperialism from 1750 to 1900.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is ``cg_check.check``; the notation gate and the negative
control are ``es_check``, reused unchanged. World History is a prose subject
that ``export_units.py`` does not typeset, exactly as ENV_SCI is, so the same
notation ban applies: no backslash macro, no caret, no digit-hyphen-digit range
(the reason HISTORY_BRIEF.md requires "1750 to 1900"), no slash fraction, no
dollar sign and no non-ASCII character.

WHAT THE KEYS REST ON
---------------------
Every item in this module traces to the single historical development the CED
prints for topic 6.1:

    KC-5.2.III  A range of cultural, religious, and racial ideologies were used
                to justify imperialism, including Social Darwinism, nationalism,
                the concept of the civilizing mission, and the desire to
                religiously convert indigenous populations.

Items 1, 5, 6, 21 rest on Social Darwinism as one of the four named ideologies;
items 2, 16, 17 on the concept of the civilizing mission; items 3, 11 on
nationalism; items 4, 10 on the desire to religiously convert; items 8 and 18 on
two of them appearing together. Items 7, 9, 12, 26, 30 rest on the sentence's
own structure -- a RANGE of ideologies, USED TO JUSTIFY, four named and no
others. Item 19 rests on the unit's stated span, c. 1750 to c. 1900, and asserts
nothing that the CED's own "not constrained by the given dates" caveat loosens.
Item 20 rests on the Cultural Developments and Interactions thematic focus and
item 28 on the same focus read against governance and economics. Item 26 rests
on Unit 6 Learning Objective A, that ideologies contributed to the development
of imperialism.

Two items reach across a topic boundary and say so: item 22 pairs KC-5.2.III
with KC-5.3.III.D (growing nationalism contributed to anticolonial movements,
topic 6.3), and item 29 pairs it with KC-5.2.I.A (states assuming direct control
over colonies previously held by non-state entities, topic 6.2). Nothing here
uses a unit 5 statement; the industrial and free-trade material of KC-5.1.I,
KC-5.1.II.B and KC-5.1.III belongs to a sibling's unit.

Items 15, 24, 25 and 27 are reasoning items about what a source can and cannot
establish. Their keys rest on the logic of the evidence, not on a CED sentence
about history, and each claim below says so rather than citing a code it does
not follow from.

WHAT THE FRAMEWORK DOES NOT SUPPLY. It names the four ideologies and defines
none of them, as the Comparative Government framework names seven data
resources without defining them. Items that turn on what an ideology asserts use
the plainest sense of the named term and no more; no item asks for a person, a
date, a treaty or a statistic the CED does not print, and every source in the
module is unattributed and labelled illustrative.

DATA ITEMS: 13, 14, 15, 23 and 24 carry tables whose values are hypothetical and
labelled so in the stem. Each keyed conclusion is recomputed below from that
table alone, and each check also falsifies the distractors.

NEGATIVE CONTROL: ``python3 verify_w6_1.py --selftest`` rotates every key off
its anchor, corrupts every table cell in turn, injects each banned notation
form (and one legal string that must pass), duplicates a choice, thins a why and
makes a why name an option by letter, and requires every one of those to raise.
"""
import sys

import cg_check as cg
import es_check as es
import w6_1

PAM_EARLY = "Pamphlets containing it, sample of 40 from the 1830s (hypothetical)"
PAM_LATE = "Pamphlets containing it, sample of 40 from the 1890s (hypothetical)"
SHARE = "Share of appeals mentioning it (hypothetical, percent)"

STANDING = "A claim that colonies raise the nation's standing among rivals"
CONVERT = "A call to convert the population to the writer's religion"
DUTY = "A duty to bring law, schooling and medicine to the governed"
STRUGGLE = "A claim that peoples struggle and the stronger displace the weaker"

APPEAL_CONVERT = "Converting the population to the society's religion"
APPEAL_SCHOOL = "Opening schools"
APPEAL_MEDICAL = "Providing medical care"
APPEAL_TRADE = "Assisting merchants"
APPEAL_GARRISON = "Supporting military garrisons"


def _pam(table, label):
    return cg.cell(table, label, PAM_EARLY), cg.cell(table, label, PAM_LATE)


def q13(table, item):
    st_e, st_l = _pam(table, STANDING)
    cv_e, cv_l = _pam(table, CONVERT)
    du_e, du_l = _pam(table, DUTY)
    sg_e, sg_l = _pam(table, STRUGGLE)
    assert st_l > st_e, "key requires the standing argument to rise between the samples"
    assert not cv_l > cv_e, "'conversion rises' must be false"
    assert not all(l > e for e, l in ((st_e, st_l), (cv_e, cv_l), (du_e, du_l), (sg_e, sg_l))), \
        "'every argument rises' must be false"
    early = {STANDING: st_e, CONVERT: cv_e, DUTY: du_e, STRUGGLE: sg_e}
    assert max(early, key=early.get) != STRUGGLE, \
        "'struggle is the most common earlier argument' must be false"
    assert du_l > 0, "'the duty argument disappears' must be false"
    return (f"standing rises {st_e:g} to {st_l:g} while conversion falls {cv_e:g} to {cv_l:g}; "
            f"struggle is the smallest earlier value and the duty argument survives at {du_l:g}")


def q14(table, item):
    gains = {lab: cg.cell(table, lab, PAM_LATE) - cg.cell(table, lab, PAM_EARLY)
             for lab in (STANDING, CONVERT, DUTY, STRUGGLE)}
    best = max(gains, key=gains.get)
    assert best == STANDING, f"largest increase is {best!r}, not the standing argument"
    assert sorted(gains.values())[-1] > sorted(gains.values())[-2], \
        "the largest increase must be strictly larger than the next"
    assert len(set(gains.values())) > 1, "'all four increase equally' must be false"
    return (f"the four changes recompute as {', '.join(f'{v:+g}' for v in gains.values())}, "
            "so the standing argument gains most and the gains are not equal")


def q15(table, item):
    st_e, st_l = _pam(table, STANDING)
    cv_e, cv_l = _pam(table, CONVERT)
    du_e, du_l = _pam(table, DUTY)
    sg_e, sg_l = _pam(table, STRUGGLE)
    # Each REJECTED option is a count the table settles; the key is the one claim
    # the table cannot reach, so the check confirms the other four are readable.
    assert st_l > st_e, "the standing comparison must be answerable from the table"
    assert cv_l < cv_e, "the conversion comparison must be answerable from the table"
    assert sg_e == min(st_e, cv_e, du_e, sg_e), "the struggle comparison must be answerable"
    assert du_l > 40 / 2, "the 'more than half of the later sample' comparison must be answerable"
    text = " ".join(str(c) for row in table["rows"] for c in row)
    assert "persuad" not in text.lower(), "the table must record nothing about persuasion"
    return ("all four rejected options recompute from the table while nothing in it records "
            "how any reader responded")


def q23(table, item):
    shares = {lab: cg.cell(table, lab, SHARE) for lab in
              (APPEAL_CONVERT, APPEAL_SCHOOL, APPEAL_MEDICAL, APPEAL_TRADE, APPEAL_GARRISON)}
    top = max(shares, key=shares.get)
    assert top == APPEAL_CONVERT, f"largest share is {top!r}"
    assert not shares[APPEAL_GARRISON] > shares[APPEAL_SCHOOL], "'garrisons above schooling' must be false"
    assert not shares[APPEAL_TRADE] > 50, "'merchants in more than half' must be false"
    assert not shares[APPEAL_MEDICAL] > shares[APPEAL_CONVERT], "'medical above conversion' must be false"
    assert any(v < 25 for v in shares.values()), "'every purpose above a quarter' must be false"
    return (f"conversion at {shares[APPEAL_CONVERT]:g} is the largest of the five shares and each "
            "distractor is false on the same numbers")


def q24(table, item):
    shares = {lab: cg.cell(table, lab, SHARE) for lab in
              (APPEAL_CONVERT, APPEAL_SCHOOL, APPEAL_MEDICAL, APPEAL_TRADE, APPEAL_GARRISON)}
    order = sorted(shares, key=shares.get)
    assert order[1] == APPEAL_TRADE, f"second smallest share is {order[1]!r}, not assisting merchants"
    assert shares[APPEAL_TRADE] < shares[APPEAL_CONVERT], "trade must fall below conversion"
    return (f"assisting merchants at {shares[APPEAL_TRADE]:g} is the second smallest of the five "
            "shares, which is what the objection to a trade-only reading rests on")


TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 23: q23, 24: q24}

CLAIMS = [
 ("transfers a struggle among species",
  "KC-5.2.III names Social Darwinism among the cultural, religious and racial ideologies used to justify imperialism. The source presents expansion as a law of survival among peoples, with no benefit offered to the governed, no religious purpose and no tariff claim."),
 ("concept of the civilizing mission",
  "KC-5.2.III names the concept of the civilizing mission among the four justifications. The source rests on a claimed improvement of the governed and their eventual fitness to govern themselves, which is that ideology and no other on the list."),
 ("making empire a measure of the nation's standing",
  "KC-5.2.III names nationalism among the four justifications. The source's whole argument is the country's rank among other countries, which is the nationalist justification rather than the civilizing, Darwinist or religious one."),
 ("religiously convert indigenous populations",
  "KC-5.2.III names the desire to religiously convert indigenous populations, in those words, among the four justifications. The source asks for funds for preaching and conversion and for nothing else on the list."),
 ("natural outcome rather than as a condition that instruction could change",
  "KC-5.2.III lists Social Darwinism and the concept of the civilizing mission separately. The mission argument holds the governed improvable by instruction; a Darwinist argument makes their decline the natural working out of a struggle. The anchor carries both clauses because the reversed reading is offered as a distractor."),
 ("temporary while Text 2 treats it as permanent",
  "KC-5.2.III names both ideologies used here. A tutelage that ends when its work is done asserts a temporary difference; a permanent ascendancy of the fitter asserts the opposite. The anchor carries both clauses because the exact swap is a distractor."),
 ("reason offered in public for imperial rule",
  "KC-5.2.III's verb is that these ideologies were used to justify imperialism, which makes each of them a publicly offered reason. The framework does not describe them as colonial in origin, as economic doctrines, as statutes, or as abandoned within the period."),
 ("standing and a claimed duty to improve the governed",
  "KC-5.2.III names both nationalism and the concept of the civilizing mission, and the source carries one clause answering to each: standing among the powers, and the lifting of the inhabitants. No clause in it concerns religion, racial fitness, tariffs or an empty territory."),
 ("free movement of goods across borders without tariffs",
  "KC-5.2.III lists exactly four ideologies: Social Darwinism, nationalism, the concept of the civilizing mission, and the desire to religiously convert indigenous populations. A tariff doctrine is not among them; the framework treats economic factors in topics 6.4 and 6.5."),
 ("religious conversion as a justification for imperial rule",
  "KC-5.2.III names the desire to religiously convert indigenous populations as one of the justifications for imperialism, and the source justifies the imperial presence by the replacement of local practice with the missions' religion."),
 ("national prestige in competition with other states",
  "KC-5.2.III names nationalism among the four justifications. The stated stake in the source is humiliation before rivals, a claim about standing among states rather than a religious, biological, educational or commercial one."),
 ("claim about the arguments offered rather than about everything",
  "KC-5.2.III says a range of ideologies were USED TO JUSTIFY imperialism. That is a statement about the arguments offered in support of expansion, and the unit treats environmental and economic factors separately under Learning Objectives D, E, F and G."),
 ("standing appears in more of the later pamphlets",
  "Recomputed from the table in q13 above: the standing argument rises from 9 to 28 while conversion falls from 22 to 12, the struggle argument is the smallest earlier value, and the duty argument survives in the later sample. Each distractor is false on the same numbers."),
 ("colonies raise the nation's standing among rivals",
  "Recomputed in q14 above: the four changes are plus 19, minus 10, plus 8 and plus 16, so the standing argument gains most and the four gains are not equal."),
 ("readers were persuaded by the arguments",
  "A tally of the arguments a pamphlet contains is evidence of what was printed and of nothing else. q15 above confirms that each rejected option is a count the table settles and that no column records a reader's response, so the effect on readers is the one claim the data cannot reach."),
 ("civilizing mission alone",
  "KC-5.2.III separates the four justifications, and the source carries the marks of one: improvement of the governed through order, law and instruction. Silence about faith, race and rivals rules out the other three."),
 ("benefit claimed for the governed, while an appeal to prestige justifies it by a gain claimed for the governing nation",
  "KC-5.2.III lists the civilizing mission and nationalism as separate ideologies. The distinction is whom the claimed benefit is said to belong to; the anchor carries both clauses because the exact reversal is offered as a distractor. The framework attaches no region and no sub-period to either, and it states that its dates are approximate."),
 ("religious conversion together with the concept of the civilizing mission",
  "KC-5.2.III names both the desire to religiously convert indigenous populations and the concept of the civilizing mission. Preaching answers to the first; treating the sick and teaching the young answer to the second."),
 ("within the period from 1750 to 1900",
  "KC-5.2.III sits under Unit 6, whose stated span is c. 1750 to c. 1900, and asserts that these ideologies were used to justify imperialism. The key claims only that the use falls within the period, which the CED's caveat that developments may begin before or continue after does not disturb; a key that fixed a boundary would."),
 ("shaped how it governed them",
  "The Cultural Developments and Interactions thematic focus states that the interactions of societies and their beliefs often have political, social and cultural implications. KC-5.2.III is that statement in operation, since beliefs about other peoples supplied the justification for ruling them."),
 ("Social Darwinism to a question of land",
  "KC-5.2.III names Social Darwinism among the justifications for imperialism. The source presents dispossession as a natural passing rather than as an improvement offered, a conversion sought, an argument against empire or a claim about prices."),
 ("to justify empire and, in other hands, to oppose it",
  "KC-5.2.III names nationalism among the ideologies used to justify imperialism, while KC-5.3.III.D states that growing nationalism contributed to anticolonial movements. Both sit in the same unit and the same period, so one ideology serves two opposite purposes rather than changing meaning at a date."),
 ("named in a larger share of the appeals than any other purpose",
  "Recomputed in q23 above: conversion at 84 percent is the largest of the five shares, garrisons fall below schooling, assisting merchants is not a majority, medical care falls below conversion, and two purposes fall below a quarter."),
 ("second least often named purpose",
  "Recomputed in q24 above: assisting merchants at 12 percent is the second smallest of the five shares. The objection has to come from the data the student is using, and the other four statements are true of the survey but leave the claim untouched."),
 ("material addressed to readers at home with those used in material addressed to serving officials",
  "The argument under test is a claim about which audience received which argument, so only evidence that compares material by audience can test it. A total count, a list of acquisitions, biographies and circulation figures each measure something the claim does not assert."),
 ("appear legitimate to the publics and governments",
  "Unit 6 Learning Objective A asks how ideologies contributed to the development of imperialism, and KC-5.2.III says they were used to justify it. A justification works on those who authorize and accept a policy; the framework attaches no machinery, capital, boundary drawing or relinquishment to these ideologies."),
 ("offered in public can be settled by reading it; whether its author sincerely believed them cannot",
  "A text is direct evidence of the argument it makes and not of the state of mind behind it or of its effect on readers. The anchor carries both clauses because the exact reversal is offered as a distractor; this is also why KC-5.2.III describes these ideologies as justifications that were used rather than as beliefs that were sincerely held."),
 ("beliefs a society held about itself and about other peoples",
  "The Cultural Developments and Interactions focus is defined as the development of ideas, beliefs and religions and how groups in society view themselves. The four ideologies of KC-5.2.III are beliefs of that kind, while statutes, prices and administrative institutions belong to the governance and economics themes treated elsewhere in the unit."),
 ("colonial control, defended in the language of improvement",
  "KC-5.2.I.A states that some states assumed direct control over colonies previously held by non-state entities, which is the change the source describes, and KC-5.2.III supplies the language of improvement in which it is defended. The source reports no end of control, no migration and no prices."),
 ("range of ideologies used to justify imperialism rather than a single one",
  "KC-5.2.III opens with a range of cultural, religious and racial ideologies and then names four, so the framework's claim is plural on its face. It singles out none of them, dates none of them within the period, and confines none to one empire or continent."),
]

es.run(w6_1, CLAIMS, TABLE_CHECKS, sys.argv)
