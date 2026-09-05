"""Key audit for AP WORLD HISTORY: MODERN 5.3 Industrial Revolution Begins.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim cites the Key Concept or Learning
Objective the key traces to.

WHAT THE KEYS REST ON
---------------------
Only two statements, and every key traces to one of them:

  KC-5.1.I.A  a variety of factors contributed to the growth of industrial
              production and eventually resulted in the Industrial Revolution,
              INCLUDING proximity to waterways with access to rivers and canals;
              the geographical distribution of coal, iron, and timber;
              urbanization; improved agricultural productivity; legal protection
              of private property; access to foreign resources; accumulation of
              capital.
  KC-5.1.I.C  the development of the factory system concentrated production in a
              single location and led to an increasing degree of specialization
              of labor.

Items 2 through 8 pair one illustrative situation with the one bullet it
matches. Item 1 keys the framework's own hedges -- "a variety of" and
"including" -- because the commonest way to get this topic wrong is to promote
one bullet to a sufficient cause or to treat the list as closed. Item 12 keys
Unit 5 Learning Objective D, which is what makes the first two bullets the
environmental ones.

WHAT THEY DELIBERATELY DO NOT REST ON
-------------------------------------
The framework names no first industrial country, no first factory, no inventor
and no date in these two statements, so no key here does either. Every region,
works, ledger and charter in the module is explicitly illustrative and
unattributed, and every key is recoverable from the stimulus plus a printed
sentence. The tables carry hypothetical figures and say so in the stem.

SWAP ANCHORS
------------
Items 11 and 14 carry a distractor that is the key reversed -- the factory
system and the specialization of labor exchanged as cause and effect, and the
two rising columns of a table exchanged for one rising and one falling. Both
anchors carry BOTH clauses, which is the defect found in verify_e2_1.py. The
key-rotation control below requires all thirty keys to fail when moved one place.

FIVE choices per item (A-E); see HISTORY_BRIEF.md.
"""
import sys

import cg_check as cg
import wh_check as wh
import w5_3

WATER = "Miles of navigable river and canal"
COAL = "Coal raised (thousands of tons per year)"
TOWN = "Population of the largest town"
YIELD = "Wheat yield per acre (bushels, hypothetical)"
NEARBY = "Population of the nearby towns"


def q13(table, item):
    """District 1 leads on all three columns; each rival claim is false on them."""
    assert len(table["headers"]) == 4, "the table must carry one label column and three measures"
    cols = {h: dict(zip(cg.labels(table), cg.col(table, h))) for h in (WATER, COAL, TOWN)}
    for header, values in cols.items():
        top = max(values, key=values.get)
        assert top == "District 1", f"District 1 must lead on {header}; the largest is {top}"
    for header, values in cols.items():
        low = min(values, key=values.get)
        assert low != "District 2", (
            f"'District 2 is smallest on every measure but one' must be false, but it is "
            f"lowest on {header}"
        )
    assert cols[WATER]["District 3"] < cols[WATER]["District 1"], \
        "'District 3 leads on navigable water' must be false"
    assert cols[COAL]["District 4"] == 0, "District 4 must raise no coal, as its option states"
    return ("recomputed from the table: District 1 holds the largest value in the navigable "
            "water, coal and town population columns, and District 2 is lowest in none of them")


def q14(table, item):
    """Both columns rise in each successive decade; no mixed or flat reading survives."""
    labels = cg.labels(table)
    assert labels == ["First decade", "Second decade", "Third decade"], \
        f"the three rows must be the three decades in order; got {labels}"
    yields = cg.col(table, YIELD)
    towns = cg.col(table, NEARBY)
    for series, name in ((yields, "wheat yield"), (towns, "town population")):
        assert all(b > a for a, b in zip(series, series[1:])), \
            f"the {name} column must rise in every step; got {series}"
    assert not (yields[-1] < yields[0]), "'the wheat yield falls' must be false"
    assert not (towns[-1] < towns[0]), "'the town population falls' must be false"
    assert len(set(yields)) > 1 and len(set(towns)) > 1, "'both remain unchanged' must be false"
    return (f"recomputed from the table: yields {yields} and town populations {towns} each rise "
            f"at every step, which is co-movement and not evidence of causation")


CLAIMS = [
 ("No single factor is presented as sufficient on its own",
  "KC-5.1.I.A opens with 'a variety of factors contributed' and introduces its bullets with 'including'. Neither word ranks the factors or closes the list, and reading those hedges is what keeps a key inside the CED rather than beyond it."),
 ("with access to rivers and canals",
  "KC-5.1.I.A's first bullet names proximity to waterways; access to rivers and canals. The stimulus describes goods moving cheaply along a river and a canal and says nothing about capital, law, farming or foreign supply."),
 ("distribution of coal, iron, and timber",
  "KC-5.1.I.A's second bullet names the geographical distribution of coal, iron, and timber. A survey of how those three lie relative to one another reports that factor itself, not a demographic, financial or legal condition on the same list."),
 ("Urbanization",
  "KC-5.1.I.A names urbanization among the factors contributing to the growth of industrial production. A shift of population from scattered farms into towns is that bullet; the framework lists it beside, not in place of, the resource and agricultural conditions."),
 ("Improved agricultural productivity",
  "KC-5.1.I.A names improved agricultural productivity among its factors. More food from the same acreage is that improvement, and the framework places it on the contributing side rather than among consequences."),
 ("legal protection of private property",
  "KC-5.1.I.A names the legal protection of private property among the factors contributing to the growth of industrial production. A code securing ownership and enforcing contracts over productive assets is that protection."),
 ("Access to foreign resources",
  "KC-5.1.I.A names access to foreign resources among its factors. Materials drawn from distant places into domestic workshops is that access, and the ledger by itself evidences none of the other bullets."),
 ("accumulation of capital",
  "KC-5.1.I.A names the accumulation of capital among the factors contributing to the growth of industrial production. A fund built up over decades and then committed to plant is that accumulation."),
 ("concentrated production in a single location",
  "KC-5.1.I.C, near verbatim: the development of the factory system concentrated production in a single location. Concentration is the framework's own word and is what the rest of that statement builds on."),
 ("increasing degree of specialization of labor",
  "KC-5.1.I.C attaches a second consequence in the same sentence: the factory system led to an increasing degree of specialization of labor. Only one of the five options is that second consequence."),
 ("factory system concentrated production and led to an increasing specialization",
  "KC-5.1.I.C runs in one direction: the development of the factory system concentrated production in a single location AND LED TO an increasing degree of specialization of labor. The anchor carries both clauses because a distractor exchanges cause and effect, which is the reasoning process this topic is built on."),
 ("waterways and the geographical distribution of coal",
  "Unit 5 Learning Objective D asks how ENVIRONMENTAL factors contributed to industrialization, and the two bullets of KC-5.1.I.A describing the physical setting are proximity to waterways and the geographical distribution of coal, iron, and timber. The rejected pairs are legal, financial and demographic."),
 ("District 1",
  "KC-5.1.I.A names proximity to waterways, the distribution of coal and urbanization among its factors, and the table gives one column for each. Recomputed in q13 above: District 1 leads all three columns and District 2 is lowest in none, so the rival readings are false on the figures."),
 ("Both the wheat yield and the town population rise",
  "KC-5.1.I.A names improved agricultural productivity and urbanization as SEPARATE factors, and q14 above recomputes both columns rising at every step. The anchor carries both columns because two distractors reverse one of them, and the causal reading is excluded because co-movement in three rows cannot establish it."),
 ("one endowment settles little by itself",
  "KC-5.1.I.A lists a variety of factors contributing together and ranks none of them. A district strong in one bullet and weak in four is not what that statement describes, which is why a conclusion from the coal alone overreaches the framework."),
 ("brought the stages into one location and divided them among specialized workers",
  "KC-5.1.I.C names both effects in one sentence: production concentrated in a single location, and an increasing degree of specialization of labor. Splitting one worker's whole task among several is that specialization, and the concentration is what makes the split possible."),
 ("among the conditions that contributed to industrial growth",
  "KC-5.1.I.A places urbanization in its bulleted list of factors that CONTRIBUTED to the growth of industrial production. The framework treats urban growth as a consequence separately, in KC-5.1.VI.C, but this statement is where it appears on the contributing side."),
 ("legal protection of private property",
  "KC-5.1.I.A names the legal protection of private property. A charter creates a secure claim rather than the mineral itself, so it supplies the legal bullet and not the geological one, although both operate in the same district."),
 ("share one named factor and differ on another",
  "KC-5.1.I.A names the geographical distribution of coal, iron, and timber and, separately, proximity to waterways with access to rivers and canals. The two regions match on the first and differ on the second, and the framework's refusal to rank its bullets is what holds the comparison at that level."),
 ("development of the factory system",
  "KC-5.1.I.C describes the factory system as concentrating production in a single location. Work moving from scattered cottages under one roof is that concentration in the pamphlet's own terms."),
 ("preceding and eventually resulting in the Industrial Revolution",
  "KC-5.1.I.A says a variety of factors contributed to the GROWTH of industrial production and EVENTUALLY resulted in the Industrial Revolution. The framework puts a period of growth before the name, and eventually is its own signal that the process was not instantaneous."),
 ("Proximity to waterways",
  "KC-5.1.I.A names proximity to waterways with access to rivers and canals among the factors contributing to the growth of industrial production. The cost of moving heavy goods by water against by road is the practical form that bullet takes."),
 ("divided so that a worker performed a narrower part of it",
  "KC-5.1.I.C describes an INCREASING DEGREE of specialization of labor following the concentration of production. An increasing degree of specialization narrows what any one worker does, which is the reverse of the student's reading."),
 ("large sums held and then committed to building and equipping works",
  "KC-5.1.I.A names the accumulation of capital as a factor distinct from mineral endowment and agricultural conditions, so evidence for it must be evidence about funds gathered and invested. Seam depth, livestock, parish boundaries and rainfall evidence other bullets or none."),
 ("foreign resources and proximity to waterways",
  "KC-5.1.I.A names access to foreign resources and, separately, proximity to waterways with access to rivers and canals. Materials landed at ports and carried inland engage both bullets at once."),
 ("Whether the other factors the framework names were also present",
  "KC-5.1.I.A presents a variety of factors contributing together, so isolating one requires knowing what else was present. The reasoning process assigned to this topic is causation, and the rejected questions gather facts that leave the causal question untouched."),
 ("a factor the framework names, the legal protection of private property",
  "KC-5.1.I.A names the legal protection of private property among its contributing factors, so a difference in enforceable title falls on the framework's own list. The rejected options relocate the difference onto bullets the comparison has already held equal."),
 ("contributed to a growth in industrial production that eventually resulted",
  "KC-5.1.I.A states that a variety of factors contributed to the growth of industrial production and eventually resulted in the Industrial Revolution. The chain runs from the factors through growth to the Revolution, and no rejected option preserves that order."),
 ("concentrated production in one place and increased the specialization of labor",
  "KC-5.1.I.C names both halves of what the account describes. The rejected options are true statements of KC-5.1.I.A, but each describes a condition outside the works rather than the arrangement inside it, which is what the stimulus reports."),
 ("conditions together fed a growth in production that the factory system then reorganized",
  "The summary joins KC-5.1.I.A's variety of contributing conditions and growth in production with KC-5.1.I.C's reorganization of work. Each rejected option contradicts one of those two statements or collapses the framework's list to a single cause."),
]

TABLE_CHECKS = {13: q13, 14: q14}

wh.run(w5_3, CLAIMS, TABLE_CHECKS, sys.argv)
