"""Key audit for AP WORLD HISTORY: MODERN 2.1 (Unit 2, The Silk Roads).

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's OWN keyed choice and of no distractor; the claim
states the CED sentence the key rests on, with its Key Concept or Learning
Objective code, so a later reader can check the history rather than take it on
trust.

WHAT THE KEYS REST ON
---------------------
  LO 2.A          explain the causes and effects of growth of networks of
                  exchange after 1200
  skill 4.A       identify and describe a historical CONTEXT for a specific
                  historical development or process
  KC-3.1.I.A.i    improved commercial practices led to an increased volume of
                  trade and expanded the geographical range of EXISTING trade
                  routes -- including the Silk Roads -- promoting the growth of
                  powerful new trading cities
  KC-3.1.I.C.i    the growth of interregional trade in luxury goods was
                  encouraged by innovations in PREVIOUSLY EXISTING
                  transportation and commercial technologies, including the
                  caravanserai, forms of credit, and the development of money
                  economies
  KC-3.3.I.B      demand for luxury goods increased in Afro-Eurasia; Chinese,
                  Persian, and Indian artisans and merchants expanded their
                  production of textiles and porcelains for export; manufacture
                  of iron and steel expanded in China
  the ECN thematic focus paragraph

TWO WORDS DO A LOT OF WORK HERE, and several keys turn on them: "existing" in
KC-3.1.I.A.i and "previously existing" in KC-3.1.I.C.i. Both sentences describe
the improvement of arrangements already in use rather than invention from
nothing, and that is the claim a prepared student is likeliest to overshoot.
q3, q12 and q29 are built on it directly.

WHAT IS DELIBERATELY NOT KEYED. KC-3.3.I.B's clause about iron and steel in
China is not made the subject of any key here, because topic 1.1 already keys
manufacturing output and production for export to the Song economy and a second
item on the same clause in a neighbouring module is a template repeat. This
module takes KC-3.3.I.B from the DEMAND side and from its naming of three
producing regions instead. Kashgar, Samarkand, bills of exchange, banking
houses and paper money are illustrative examples, which the CED says "do not in
any way constitute additional, preferred, or required information", so no key
turns on one.

WHERE THE ANCHOR CARRIES TWO CLAUSES, AND WHY
---------------------------------------------
Three distractors here are the SWAP of the key rather than an unrelated claim:

  q8   porcelain multiplying by more than silk, the two goods exchanged
  q20  transportation and commercial technologies, their definitions exchanged
  q4   the largest ABSOLUTE increase against the largest PROPORTIONAL one

Those anchors carry both clauses in order, which is the defect verify_e2_1.py
shipped and HISTORY_BRIEF.md records.

DATA QUESTIONS
--------------
Items 4, 6 and 8 carry tables of HYPOTHETICAL figures and each stem says so;
the CED prints no trade figures, and an invented one presented as a record
would be read by a student as real. Each keyed conclusion is recomputed below
from the table alone AND every distractor is shown false on the same numbers.
The control prints a catch rate per table: it is never nine of nine, because
the label column cannot be corrupted into a contradiction and because a
corruption leaving the keyed conclusion TRUE must not be caught. A zero would
mean the check had stopped reading its table.

NEGATIVE CONTROL: `python3 verify_w2_1.py --selftest`.
"""
import sys

import cg_check as cg
import w2_1
import wh_check

EARLY_C = "Caravans recorded in an earlier decade"
LATE_C = "Caravans recorded in a later decade"
COIN = "Transactions settled in coin"
PAPER = "Transactions settled by a written instrument"
EARLY_G = "Units carried westward in an earlier period"
LATE_G = "Units carried westward in a later period"


def q4(table, item):
    """All stages rise, and the biggest rise is not the biggest multiple."""
    early, late = cg.col(table, EARLY_C), cg.col(table, LATE_C)
    assert all(l > e for e, l in zip(early, late)), \
        f"every stage must rise: {early} to {late}"
    gains = [l - e for e, l in zip(early, late)]
    ratios = [l / e for e, l in zip(early, late)]
    assert gains.index(max(gains)) != ratios.index(max(ratios)), \
        f"the largest gain {gains} and the largest multiple {ratios} must be different stages"
    # every distractor false on the same numbers
    assert not all(l < e for e, l in zip(early, late)), "'every stage fell' must be false"
    assert not any(l == e for e, l in zip(early, late)), "'one stage unchanged' must be false"
    top_early = early.index(max(early))
    assert gains[top_early] == max(gains), \
        ("'the stage with the most caravans earlier had the smallest increase' must be false; "
         "it must in fact have the largest gain")
    return (f"earlier {early} to later {late}: gains {gains} peak at stage "
            f"{gains.index(max(gains)) + 1} while multiples {[round(r, 2) for r in ratios]} "
            f"peak at stage {ratios.index(max(ratios)) + 1}")


def q6(table, item):
    """Both kinds everywhere, and the written-instrument SHARE rising."""
    coin, paper = cg.col(table, COIN), cg.col(table, PAPER)
    assert all(c > 0 for c in coin) and all(p > 0 for p in paper), \
        f"every market must record both kinds: coin {coin}, written {paper}"
    shares = [p / (c + p) for c, p in zip(coin, paper)]
    assert all(b > a for a, b in zip(shares, shares[1:])), \
        f"the written-instrument share must RISE at every step: {shares}"
    # every distractor false on the same numbers
    assert not all(p > c for c, p in zip(coin, paper)), \
        "'written instruments lead in every market' must be false"
    coin_shares = [c / (c + p) for c, p in zip(coin, paper)]
    assert not all(b > a for a, b in zip(coin_shares, coin_shares[1:])), \
        "'the coin share rises across the markets' must be false"
    assert not any(p == 0 for p in paper), "'one market records none' must be false"
    assert coin.index(max(coin)) != paper.index(max(paper)), \
        "'the market with the most coin also has the most written' must be false"
    return (f"coin {coin} against written instruments {paper}: both present everywhere and "
            f"the written share {[round(s, 2) for s in shares]} rises at every step")


def q8(table, item):
    """All three goods rise, and PORCELAIN multiplies by more than SILK."""
    early, late = cg.col(table, EARLY_G), cg.col(table, LATE_G)
    assert all(l > e for e, l in zip(early, late)), f"all must rise: {early} to {late}"
    silk_e = cg.cell(table, "Silk textiles", EARLY_G)
    silk_l = cg.cell(table, "Silk textiles", LATE_G)
    porc_e = cg.cell(table, "Porcelain", EARLY_G)
    porc_l = cg.cell(table, "Porcelain", LATE_G)
    assert porc_l / porc_e > silk_l / silk_e, \
        f"porcelain must multiply by more than silk: {porc_l / porc_e} vs {silk_l / silk_e}"
    # every distractor false on the same numbers
    assert not silk_l / silk_e > porc_l / porc_e, "'silk multiplied by more' must be false"
    assert not any(l < e for e, l in zip(early, late)), "'one good fell' must be false"
    ratios = [l / e for e, l in zip(early, late)]
    assert len(set(ratios)) > 1, "'all multiplied by the same factor' must be false"
    top_early = early.index(max(early))
    assert ratios[top_early] != max(ratios), \
        "'the largest quantity earlier multiplied by the largest factor' must be false"
    return (f"earlier {early} to later {late}: all rise, and porcelain multiplies by "
            f"{porc_l / porc_e} against silk's {silk_l / silk_e}")


TABLE_CHECKS = {4: q4, 6: q6, 8: q8}

CLAIMS = [
 ("shelter for caravans, forms of credit and the spread of money economies",
  "KC-3.1.I.C.i states that the growth of interregional trade in luxury goods was encouraged by innovations in previously existing transportation and commercial technologies, including the caravanserai, forms of credit, and the development of money economies. The handbook in the stem describes all three, and each rejected option denies something the sentence asserts."),

 ("expanded the geographical range the routes covered",
  "KC-3.1.I.A.i states that improved commercial practices led to an increased volume of trade AND expanded the geographical range of existing trade routes, including the Silk Roads. Both halves stand in the one sentence, and the sentence is about routes already in use rather than new ones."),

 ("improvement of what was already in use rather than invention from nothing",
  "KC-3.1.I.C.i speaks of innovations in PREVIOUSLY EXISTING transportation and commercial technologies. The adjective is the framework's own, and it is exactly what a claim of invention from nothing contradicts."),

 ("the stage with the largest increase in number is not the stage whose traffic multiplied by the largest factor",
  "Recomputed in q4 above from the table alone, distractors included. KC-3.1.I.A.i states that improved commercial practices led to an increased volume of trade on existing routes, and a rise at every stage of one route is an increase in volume expressed in figures. The anchor carries both measures because the strongest distractor asserts that they coincide."),

 ("cities of this kind grew because they stood where that traffic passed",
  "Suggested skill 4.A asks for the historical CONTEXT of a development rather than a restatement of it, and KC-3.1.I.A.i supplies that context: improved commercial practices increased the volume of trade and expanded the range of existing routes, PROMOTING THE GROWTH of powerful new trading cities. The four rejected options describe features of the city itself."),

 ("records settlement of both kinds, and the share settled by a written instrument rises",
  "Recomputed in q6 above from the two columns. KC-3.1.I.C.i names forms of credit and the development of money economies among the innovations that encouraged the growth of interregional trade in luxury goods, and written settlement beside coin is what such a development looks like in a market's records."),

 ("artisans and merchants in China, Persia and India expanded their production",
  "KC-3.3.I.B states that demand for luxury goods increased in Afro-Eurasia and that Chinese, Persian, and Indian artisans and merchants expanded their production of textiles and porcelains for export. Three regions of producers are named rather than one, and the demand and the response are asserted in the same sentence."),

 ("porcelain multiplied by a larger factor than silk textiles",
  "Recomputed in q8 above from the two columns. KC-3.3.I.B states that demand for luxury goods increased in Afro-Eurasia and that artisans and merchants expanded production of textiles and porcelains for export. The anchor carries both goods in order because the strongest distractor exchanges them."),

 ("so that a rise in demand could be met rather than merely felt",
  "KC-3.3.I.B supplies the demand side and KC-3.1.I.C.i the means side, naming innovations in previously existing transportation and commercial technologies among the encouragements to interregional trade. An argument that one cause is insufficient is strengthened by evidence bearing on the other."),

 ("the framework names forms of credit among the innovations",
  "KC-3.1.I.C.i names forms of credit and the development of money economies among the innovations in previously existing commercial technologies that encouraged the growth of interregional trade in luxury goods. A sum deposited in one place and drawn in another is credit, which the framework groups with commerce rather than with transport."),

 ("improvement to the conditions under which goods and animals move",
  "KC-3.1.I.C.i states that the growth of interregional trade in luxury goods was encouraged by innovations in previously existing TRANSPORTATION and commercial technologies, INCLUDING THE CARAVANSERAI. The caravanserai is the CED's own instance of the transportation half of that pair."),

 ("expanded, which is extension of something already in use",
  "KC-3.1.I.A.i states that improved commercial practices expanded the geographical range of EXISTING trade routes, including the Silk Roads. The word existing settles the dispute, and the CED separately states that developments may begin before the period it assigns them to."),

 ("growth of interregional trade in luxury goods",
  "KC-3.1.I.C.i speaks specifically of the growth of interregional trade in LUXURY GOODS as what the period's innovations in previously existing technologies encouraged, and KC-3.3.I.B states that demand for luxury goods increased in Afro-Eurasia. High value in small bulk is the trade those two sentences are about."),

 ("produced far away in both directions and were not consumed in the surrounding country",
  "KC-3.1.I.A.i states that improved commercial practices increased the volume of trade and expanded the range of existing routes, PROMOTING THE GROWTH OF POWERFUL NEW TRADING CITIES. Goods that neither originate in the district nor stop there are what distinguish a city of passage from a market serving its own region."),

 ("the effect reached the places where the goods were made",
  "KC-3.3.I.B states that demand for luxury goods increased in Afro-Eurasia and that Chinese, Persian, and Indian artisans and merchants expanded their production of textiles and porcelains for export, while the Economics thematic focus states that societies affect and are affected by the ways they produce, exchange, and consume goods and services."),

 ("set against a rise in the volume of trade and an extension of the routes",
  "Suggested skill 4.A asks a student to identify and describe a historical CONTEXT for a development, which is the circumstance in which it occurred and not the development restated. KC-3.1.I.A.i supplies exactly such a context for the growth of trading cities. The four rejected pairings each set a development against itself."),

 ("An improvement in commercial practice",
  "KC-3.1.I.A.i states that IMPROVED COMMERCIAL PRACTICES led to an increased volume of trade and expanded the geographical range of existing trade routes. An agreement distributing the risk of a journey between two merchants is a commercial practice rather than a transport technology, which is the distinction KC-3.1.I.C.i draws."),

 ("because rulers compelled merchants to travel",
  "KC-3.1.I.A.i and KC-3.1.I.C.i between them assert increased volume, expanded range, the growth of powerful new trading cities, and the encouragement given by innovations in previously existing technologies. Compulsion by rulers appears in neither sentence, which is what makes it the unsupported claim."),

 ("taken with its account of producers expanding output for distant markets",
  "The Economics thematic focus states that as societies develop, they affect and are affected by the ways that they produce, exchange, and consume goods and services, and KC-3.3.I.B records artisans and merchants in China, Persia and India expanding production for export. Together they carry the argument to the producing societies."),

 ("One concerns how goods and people are moved and the other how payment and obligation are arranged",
  "KC-3.1.I.C.i names innovations in previously existing TRANSPORTATION AND COMMERCIAL technologies and then gives an instance of each side: the caravanserai on one, forms of credit and the development of money economies on the other. The anchor carries both halves in order because the strongest distractor exchanges them."),

 ("artisans and merchants in several producing regions responded by expanding output for export",
  "KC-3.3.I.B states that demand for luxury goods increased in Afro-Eurasia and that Chinese, Persian, and Indian artisans and merchants expanded their production of textiles and porcelains for export. Output far exceeding what the district could absorb is production for export in exactly that sense."),

 ("its standing rested on the exchange passing through it",
  "KC-3.1.I.A.i states that improved commercial practices increased the volume of trade and expanded the geographical range of existing routes, promoting the growth of POWERFUL NEW TRADING CITIES. The framework ties the standing of such a city to the traffic rather than to its size, its buildings or its state."),

 ("the key concepts name improved practices, innovations in existing technologies and rising demand as those causes",
  "Learning Objective A of this unit asks students to explain the causes and effects of the growth of networks of exchange after 1200, and KC-3.1.I.A.i, KC-3.1.I.C.i and KC-3.3.I.B each supply one of those causes."),

 ("The growth of powerful new trading cities along the routes",
  "KC-3.1.I.A.i places the growth of powerful new trading cities on the far side of its own sentence from improved commercial practices, which lead to increased volume and expanded range and thereby PROMOTE that growth. Learning Objective A asks for causes and effects; the four rejected options are named among the causes."),

 ("an improvement whose absence was felt",
  "KC-3.1.I.A.i names improved commercial practices as a cause of increased volume of trade, and KC-3.1.I.C.i names forms of credit and the development of money economies among the innovations encouraging interregional trade. A complaint about their absence is evidence for what their presence did."),

 ("without stating how far it increased or in what proportion between regions",
  "KC-3.3.I.B states that demand for luxury goods increased in Afro-Eurasia and names Chinese, Persian, and Indian artisans and merchants as expanding production of textiles and porcelains for export. It supplies no magnitude and no comparison between regions, so a claim about how much would go past the sentence."),

 ("what each was written to accomplish is part of what the historian must weigh",
  "Learning Objective A asks students to explain the causes and effects of the growth of networks of exchange after 1200, and KC-3.1.I.A.i is a claim about volume and range that a merchant's book and a toll register both bear on. Weighing purpose is how two such records are used together rather than ranked by type."),

 ("offered as an instance of the transportation technologies",
  "KC-3.1.I.C.i names the caravanserai, forms of credit, and the development of money economies together as innovations in previously existing transportation and commercial technologies that encouraged the growth of interregional trade in luxury goods. It is one instance among several, and the word previously rules out novelty."),

 ("continuity of the route is consistent with change in the trade",
  "KC-3.1.I.A.i states that improved commercial practices led to an increased volume of trade and expanded the geographical range of EXISTING trade routes, including the Silk Roads. The sentence asserts an old route and a changed trade in the same breath, which is what the student's inference misses."),

 ("was driven by a demand for luxury goods that producers in several regions worked to meet",
  "KC-3.1.I.A.i supplies the increased volume and expanded range of existing routes, KC-3.1.I.C.i the innovations in previously existing transportation and commercial technologies, and KC-3.3.I.B the increase in demand met by artisans and merchants in China, Persia and India. The key states all three and each rejected option contradicts at least one."),
]

wh_check.run(w2_1, CLAIMS, TABLE_CHECKS, sys.argv)
