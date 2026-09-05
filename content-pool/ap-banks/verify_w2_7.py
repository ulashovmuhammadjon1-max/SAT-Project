"""Key audit for AP WORLD HISTORY: MODERN 2.7 (Unit 2's reasoning topic).

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's OWN keyed choice and of no distractor; the claim
states the CED sentence the key rests on, with its Key Concept or Learning
Objective code.

WHAT THE KEYS REST ON
---------------------
This is the unit's final topic, and the CED says of every such page that it
"includes key concepts, which summarize the historical developments in the
unit". The page reprints five, and those plus the suggested skill are what
every key traces to:

  LO 2.L         the similarities AND differences among the various networks of
                 exchange in the period from c. 1200 to c. 1450
  skill 6.B      support an argument using specific and relevant evidence, in
                 two printed sub-bullets: DESCRIBE specific examples of
                 historically relevant evidence, and EXPLAIN HOW specific
                 examples support an argument
  KC-3.1         a DEEPENING AND WIDENING of networks of human interaction
                 within and across regions contributed to cultural,
                 technological, and biological diffusion within and between
                 various societies
  KC-3.1.I.A.i   improved commercial practices, increased volume, expanded range
                 of existing routes, powerful new trading cities
  KC-3.1.I.C.i   innovations in previously existing transportation and
                 commercial technologies -- caravanserai, forms of credit, money
                 economies
  KC-3.3         changes in trade networks RESULTED FROM AND STIMULATED
                 increasing productive capacity, with important implications for
                 SOCIAL AND GENDER STRUCTURES and ENVIRONMENTAL PROCESSES
  KC-3.3.I.B     demand for luxury goods increased in Afro-Eurasia; Chinese,
                 Persian, and Indian artisans and merchants expanded production
                 for export

HOW THIS MODULE WAS KEPT OFF TOPIC 3.4's GROUND
-------------------------------------------------
3.4 shares skill 6.B and asks chiefly WHICH evidence is relevant to a claim.
This module is built on the skill's SECOND sub-bullet instead -- how a given
piece of evidence bears on a stated argument, and what it leaves open. q2, q4,
q9, q12, q14, q17 and q27 all turn on that difference, which 3.4 does not ask
systematically. Two items here (q10, q18) do ask about relevance, and they are
the deliberate minimum.

A REASONING TOPIC IS NOT A LICENCE TO KEY REASONING ALONE
-----------------------------------------------------------
Every key below is anchored to something the framework says about THIS unit's
content, not to what makes an argument good in general: q6 and q12 to KC-3.3's
two-directional phrase, q11 and q21 to its clause about social and gender
structures and environmental processes, q15 and q16 to the exact reach of
KC-3.3.I.B, q24 to KC-3.1's pairing of deepening with widening.

WHERE THE ANCHOR CARRIES TWO CLAUSES, AND WHY
---------------------------------------------
Six distractors here are the SWAP of the key rather than an unrelated claim:

  q2   describing evidence and explaining its bearing, exchanged
  q3   similarity and difference, both read off one table
  q5   common direction and differing degree, one clause denied
  q6   trade resulting from capacity / stimulating it, one direction dropped
  q24  deepening and widening, one of the two denied
  q28  argument and summary, their definitions exchanged

Those anchors carry both clauses in order, which is the defect verify_e2_1.py
shipped and HISTORY_BRIEF.md records.

DATA QUESTIONS
--------------
Items 3, 5 and 7 carry tables of HYPOTHETICAL figures and each stem says so.
Each keyed conclusion is recomputed below from the table alone AND every
distractor is shown false on the same numbers. q3 and q5 are keyed to
conclusions that support BOTH halves of Learning Objective L from one table,
which is the characteristic move of this topic; q7's key says "consistent with"
rather than "shows", because two indexes rising together cannot settle which
moved first -- and KC-3.3 says the influence ran both ways in any case. The
control's per-table catch rate is never nine of nine: the label column cannot
be corrupted into a contradiction, and a corruption leaving the keyed
conclusion TRUE must not be caught. A zero would mean the check had stopped
reading its table.

NEGATIVE CONTROL: `python3 verify_w2_7.py --selftest`.
"""
import sys

import cg_check as cg
import w2_7
import wh_check

LUX = "Share of recorded cargoes that were luxury goods (percent)"
BULK = "Share of recorded cargoes that were bulk goods (percent)"
EARLY_V = "Volume index at an earlier date"
LATE_V = "Volume index at a later date"
MADE = "Index of goods produced for exchange"
CARRIED = "Index of goods carried between regions"


def q3(table, item):
    """Luxury over half everywhere (similarity) and the shares differ (difference)."""
    lux, bulk = cg.col(table, LUX), cg.col(table, BULK)
    assert all(x + y == 100 for x, y in zip(lux, bulk)), \
        f"the two share columns must total one hundred: {lux} and {bulk}"
    assert all(x > 50 for x in lux), f"luxury must exceed half everywhere: {lux}"
    assert len(set(lux)) == len(lux), f"the shares must differ between networks: {lux}"
    # every distractor false on the same numbers
    assert not all(y > 50 for y in bulk), "'bulk over half everywhere' must be false"
    assert len(set(lux)) > 1, "'the same shares everywhere' must be false"
    assert not any(y > x for x, y in zip(lux, bulk)), \
        "'bulk larger on one network' must be false"
    assert sum(1 for x in lux if x > 50) > 1, \
        "'luxury over half on only one network' must be false"
    return (f"luxury shares {lux} against bulk {bulk}: every luxury share exceeds fifty, "
            f"which is the similarity, and all three differ, which is the difference")


def q5(table, item):
    """All rise (common direction) by different multiples (differing degree)."""
    early, late = cg.col(table, EARLY_V), cg.col(table, LATE_V)
    assert all(l > e for e, l in zip(early, late)), f"all must rise: {early} to {late}"
    mult = [l / e for e, l in zip(early, late)]
    assert len(set(mult)) == len(mult), f"the multiples must all differ: {mult}"
    # every distractor false on the same numbers
    assert len(set(mult)) > 1, "'the same multiple everywhere' must be false"
    assert not any(l < e for e, l in zip(early, late)), "'one network fell' must be false"
    gains = [l - e for e, l in zip(early, late)]
    assert mult.index(max(mult)) == gains.index(max(gains)), \
        ("'the network with the largest multiple grew least' must be false; on a common "
         "base the largest multiple is also the largest gain")
    assert any(m > 2 for m in mult), "'none more than doubled' must be false"
    return (f"earlier {early} to later {late}: all rise, and the multiples "
            f"{[round(m, 2) for m in mult]} are all different")


def q7(table, item):
    """Both indexes rise at every step -- consistent with, not proof of, a direction."""
    made, carried = cg.col(table, MADE), cg.col(table, CARRIED)
    assert all(b > a for a, b in zip(made, made[1:])), f"production must rise: {made}"
    assert all(b > a for a, b in zip(carried, carried[1:])), f"carriage must rise: {carried}"
    # every distractor false on the same numbers
    assert not any(b < a for a, b in zip(carried, carried[1:])), \
        "'carriage falls' must be false"
    assert not any(b < a for a, b in zip(made, made[1:])), "'production falls' must be false"
    assert len(set(made)) > 1, "'both unchanged' must be false"
    assert not any(a == b for a, b in zip(made[1:], made[:-1])), \
        "'production level at a step' must be false"
    assert not any(a == b for a, b in zip(carried[1:], carried[:-1])), \
        "'carriage level at a step' must be false"
    return (f"production {made} and carriage {carried} both rise at every step, which "
            f"fixes no order of cause between them")


TABLE_CHECKS = {3: q3, 5: q5, 7: q7}

CLAIMS = [
 ("innovations in transportation and commercial technologies that were already in use",
  "KC-3.1.I.C.i states that the growth of interregional trade in luxury goods was encouraged by innovations in previously existing transportation and commercial technologies, and Learning Objective L asks for the similarities and differences among the various networks of exchange. The rejected options are true of any trade anywhere and so distinguish nothing about these networks."),

 ("describe a specific example of relevant evidence, and the second is to explain how that example supports an argument",
  "Suggested skill 6.B for this topic is printed with two sub-bullets: describe specific examples of historically relevant evidence, and explain how specific examples of historically relevant evidence support an argument, and Learning Objective L supplies the arguments those two operations are performed on. The anchor carries both halves in order because the strongest distractor exchanges them."),

 ("which supports a claim of similarity, while the shares differ from one network to another",
  "Recomputed in q3 above from the two columns, distractors included. Learning Objective L asks for the similarities AND differences among the various networks of exchange, and KC-3.1.I.C.i and KC-3.3.I.B both make the luxury trade a subject of the framework. One table can support both halves of the objective, which is the characteristic move of this topic."),

 ("shows the general claim holding in a particular case",
  "KC-3.1.I.C.i names forms of credit and the development of money economies among the innovations in previously existing commercial technologies, and suggested skill 6.B asks students to explain how a specific example supports an argument. An instance supports a general claim without establishing it."),

 ("which supports a claim of common direction, but by different multiples",
  "Recomputed in q5 above from the two columns. KC-3.1 states that a deepening and widening of networks of human interaction contributed to diffusion within and between various societies, and Learning Objective L asks for similarities AND differences among those networks. The anchor carries both clauses because a distractor keeps the first and denies the second."),

 ("resulted from increasing productive capacity and also stimulated it",
  "KC-3.3 states that changes in trade networks RESULTED FROM AND STIMULATED increasing productive capacity, with important implications for social and gender structures and environmental processes. The anchor carries both directions because each of the two strongest distractors keeps one and drops the other."),

 ("consistent with the two moving together rather than one running ahead",
  "Recomputed in q7 above from the two columns. KC-3.3 states that changes in trade networks resulted from and stimulated increasing productive capacity, and two measures rising together is what a two-way relation looks like in figures. The keyed wording says consistent with rather than proves, because figures moving together do not settle which moved first."),

 ("naming increased volume and expanded range of routes already in use",
  "KC-3.1.I.A.i states that improved commercial practices led to an increased volume of trade and expanded the geographical range of existing trade routes, and the framework's parallel sentences say the same of other networks. Learning Objective L asks for similarities as well as differences, so a claim of total difference must answer them."),

 ("without measuring how large a share of all cargoes such goods were",
  "Suggested skill 6.B asks students to explain HOW a specific example supports an argument, and KC-3.1.I.C.i and KC-3.3.I.B make the luxury trade a subject of the framework. A single cargo illustrates a claim about proportion without establishing the proportion."),

 ("gives a reader a reason to accept or doubt that claim rather than some other",
  "Suggested skill 6.B asks students to support an argument using specific and RELEVANT evidence, and Learning Objective L supplies the arguments in this unit, about similarities and differences among the various networks of exchange. Accuracy and date are separate virtues from bearing on the claim."),

 ("important implications for social and gender structures and for environmental processes",
  "KC-3.3 states that changes in trade networks resulted from and stimulated increasing productive capacity, WITH IMPORTANT IMPLICATIONS FOR SOCIAL AND GENDER STRUCTURES AND ENVIRONMENTAL PROCESSES. The four rejected options are commercial facts drawn from KC-3.1.I.A.i and KC-3.1.I.C.i and do not reach past commerce."),

 ("does not by itself rule out that the district's output had been rising already",
  "KC-3.3 states that changes in trade networks resulted from AND STIMULATED increasing productive capacity, so the framework itself allows influence in both directions, and suggested skill 6.B asks students to explain how an example supports an argument. Saying what a piece of evidence leaves open is part of that explanation."),

 ("contributed to cultural, technological, and biological diffusion",
  "KC-3.1 states that a deepening and widening of networks of human interaction within and across regions contributed to cultural, technological, and biological diffusion within and between various societies. That is asserted of the networks generally, and none of the four uniformities is asserted anywhere in the framework."),

 ("must say why the city's growth would be expected if practice improved",
  "KC-3.1.I.A.i states that improved commercial practices led to an increased volume of trade and expanded the geographical range of existing trade routes, PROMOTING the growth of powerful new trading cities, and suggested skill 6.B asks students to EXPLAIN HOW an example supports an argument rather than only to name it."),

 ("carried a greater volume of goods than the others did",
  "KC-3.1.I.A.i, KC-3.1.I.C.i and KC-3.3.I.B assert increased volume, expanded range, rising demand and the encouragement given by innovations, but they never compare one network's volume with another's. A claim of greater volume adds a comparison of magnitude the framework does not make."),

 ("names artisans and merchants in three regions",
  "KC-3.3.I.B states that demand for luxury goods increased in Afro-Eurasia and that Chinese, Persian, and Indian artisans and merchants expanded their production of textiles and porcelains for export. Three sets of producers are named, and a claim about every region of Afro-Eurasia is broader than the sentence supports."),

 ("held at one point on the network",
  "Suggested skill 6.B asks students to describe specific examples of historically relevant evidence AND to explain how they support an argument, and Learning Objective L frames the arguments as claims about the various networks. A point on a network supports a claim about the network without settling it."),

 ("an arrangement for shelter and for payment at a distance coming into general use",
  "KC-3.1.I.C.i names the caravanserai, forms of credit, and the development of money economies as innovations in previously existing transportation and commercial technologies that encouraged the growth of interregional trade, and suggested skill 6.B asks for SPECIFIC AND RELEVANT evidence. The rejected pairings attach true facts that give no reason to accept or doubt the claim."),

 ("its own unit of analysis is larger than any single route",
  "KC-3.1 states that a deepening and widening of networks of human interaction WITHIN AND ACROSS REGIONS contributed to cultural, technological, and biological diffusion within and between various societies, and Learning Objective L asks for a comparison AMONG the various networks."),

 ("alike in what encouraged them to grow and unlike in what they carried",
  "Learning Objective L asks students to explain the similarities and differences among the various networks of exchange, and KC-3.1.I.C.i and KC-3.3.I.B describe an encouragement and a demand that several networks shared while the framework nowhere asserts that their cargoes matched. A comparison needs its respect stated for that reason."),

 ("shows who did what work changing as production for market grew",
  "KC-3.3 states that changes in trade networks resulted from and stimulated increasing productive capacity, WITH IMPORTANT IMPLICATIONS FOR SOCIAL AND GENDER STRUCTURES and environmental processes, and KC-3.3.I.B records artisans and merchants expanding production of textiles for export."),

 ("before the rise in demand became general",
  "KC-3.3.I.B supplies the rising demand and KC-3.1.I.C.i the innovations in previously existing transportation and commercial technologies, which the framework names as a separate encouragement. Suggested skill 6.B asks how evidence bears on an argument, and evidence for a second cause is what tells against a single-cause account."),

 ("a feature common to every case and a variation in its size",
  "Learning Objective L asks students to explain the similarities AND differences among the various networks of exchange in the period from c. 1200 to c. 1450, and suggested skill 6.B asks how a specific example supports an argument. A shared feature and a varying magnitude are two readings of one set of figures."),

 ("more intense within the regions already connected as well as reaching across to further ones",
  "KC-3.1 states that a DEEPENING AND WIDENING of networks of human interaction within and across regions contributed to cultural, technological, and biological diffusion within and between various societies. Two changes are named, and the anchor carries both because a distractor keeps one and denies the other."),

 ("two different kinds of thing arriving in one place",
  "KC-3.1 states that a deepening and widening of networks of human interaction contributed to CULTURAL, TECHNOLOGICAL, AND BIOLOGICAL diffusion within and between various societies. A crop and a technique are two of the three kinds that one sentence names."),

 ("explain why the argument survives it",
  "Suggested skill 6.B asks students to support an argument using specific and relevant evidence and to explain how examples support it, and Learning Objective L's demand for similarities AND differences means the evidence in this unit rarely points one way only."),

 ("Naming the environmental processes the framework attaches to changes in trade networks",
  "KC-3.3 states that changes in trade networks resulted from and stimulated increasing productive capacity, with important implications for social and gender structures and ENVIRONMENTAL PROCESSES, and suggested skill 6.B asks students to describe specific examples of relevant evidence and explain how they support an argument."),

 ("An argument makes a claim that a reader could dispute and offers evidence for it",
  "Suggested skill 6.B asks students to SUPPORT AN ARGUMENT using specific and relevant evidence, and Learning Objective L supplies the claims to be argued, about similarities and differences among the various networks. The anchor carries both halves in order because the strongest distractor exchanges them."),

 ("rather than asserting of the period what only one route's record supports",
  "Suggested skill 6.B asks students to support an argument using specific and relevant evidence, and Learning Objective L asks for claims about the VARIOUS networks of exchange. Fitting a claim to what the evidence can carry is what supporting it with that evidence means."),

 ("unlike in the particular routes, technologies and cargoes through which each did so",
  "KC-3.1 supplies the deepening and widening of networks contributing to cultural, technological, and biological diffusion, KC-3.1.I.A.i and KC-3.1.I.C.i the improved practices and the innovations in previously existing technologies, and KC-3.3.I.B the demand met by producers in several regions. Learning Objective L asks for the similarities AND differences, which is what the key names and each rejected option drops."),
]

wh_check.run(w2_7, CLAIMS, TABLE_CHECKS, sys.argv)
