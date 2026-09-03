"""Key audit for AP CHEMISTRY 7.9 Introduction to Le Chatelier's Principle.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor.

WHAT THE KEYS REST ON. Two statements, and the topic boundary they draw:

  7.9.A.1  the four stresses -- addition or removal of a chemical species,
           change in temperature, change in volume/pressure of a gas-phase
           system, dilution of a reaction system -- and the response to each
  7.9.A.2  the effect of a stress on pH, temperature and colour of a solution

The next topic, 7.10, owns the MECHANISM: that a disturbance makes Q differ
from K and that the system responds by bringing them back into agreement.
``no_quotient_argument`` below asserts that no key or rationale in THIS module
argues from Q, so the two topics cannot converge on the same question. That is
a real separation, not a stylistic one: it is what stops thirty items here from
being thirty items there.

STIMULUS FACTS ARE SUPPLIED, NOT REMEMBERED. Every colour, every sign of an
enthalpy change and every pH direction is stated in the stem or the table, so
no key rests on recalling the behaviour of a particular indicator or complex
ion, which the CED does not describe.

NEGATIVE CONTROL: ``python3 verify_h7_9.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h7_9

REACT = "Moles of gas on the reactant side"
PROD = "Moles of gas on the product side"
CHANGE = "Change made to the flask"
COLOUR = "Colour after the change"
BATH = "Temperature of the water bath in degrees Celsius"
MIX = "Colour of the equilibrium mixture"

# 7.10 owns the Q-versus-K account. Explicit lookarounds, never \b beside a
# letter run: "Q" as a bare token, and the phrase "reaction quotient".
_QUOTIENT = re.compile(r"(?<![A-Za-z])(Q)(?![A-Za-z])|reaction quotient", re.I)


def no_quotient_argument(module):
    """Nothing in this module may argue from Q -- that is topic 7.10's material."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for name, text in (("stem", item["q"]), ("why", item["why"]),
                           *[("choice", c) for c in item["choices"]]):
            hit = _QUOTIENT.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: the {name} argues from the reaction quotient "
                f"({hit.group(0)!r}), which is topic 7.10's material -- {text[:60]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item argues from the reaction quotient, "
          "which belongs to 7.10.")


# ------------------------------------------------------------------ table items

def q6(table, item):
    same = [lab for lab in cg.labels(table)
            if cg.cell(table, lab, REACT) == cg.cell(table, lab, PROD)]
    assert same == ["2"], f"reactions with equal moles of gas on the two sides: {same}"
    h.shows(item, "Reaction 2")
    return f"of the three tabulated reactions only {same[0]} carries equal moles of gas"


def q7(table, item):
    more = [lab for lab in cg.labels(table)
            if cg.cell(table, lab, PROD) > cg.cell(table, lab, REACT)]
    assert more == ["3"], f"reactions with more moles of gas as products: {more}"
    h.shows(item, "Reaction 3")
    return f"only reaction {more[0]} has more moles of gas on its product side"


def q11(table, item):
    rows = {str(r[0]): r for r in table["rows"]}
    head = [str(x) for x in table["headers"]]
    ci, coli = head.index(CHANGE), head.index(COLOUR)
    removed = [lab for lab, r in rows.items()
               if "removed" in r[ci].lower() and "FeSCN2+" in r[ci]]
    assert removed == ["1"], f"trials removing the coloured product: {removed}"
    assert "paler" in rows["1"][coli], "the recorded colour after removal must be paler"
    h.shows(item, "Trial 1")
    return (f"trial {removed[0]} is the only tabulated change that removes the coloured "
            f"product, and the colour recorded after it is {rows['1'][coli]!r}")


def q12(table, item):
    rows = {str(r[0]): r for r in table["rows"]}
    head = [str(x) for x in table["headers"]]
    ci, coli = head.index(CHANGE), head.index(COLOUR)
    assert "dilute" in rows["3"][ci].lower(), "trial 3 must be the dilution"
    assert "paler" in rows["3"][coli], "the tabulated colour after dilution must be paler"
    assert rows["2"][coli] != rows["3"][coli], \
        "the addition and the dilution must not record the same colour"
    h.shows(item, "Dilution is a stress under the framework")
    return (f"trial 3 is the dilution and its recorded colour is {rows['3'][coli]!r}, "
            f"against {rows['2'][coli]!r} for the addition")


def q15(table, item):
    temps = dict(zip(cg.labels(table), cg.col(table, BATH)))
    head = [str(x) for x in table["headers"]]
    colours = {str(r[0]): r[head.index(MIX)] for r in table["rows"]}
    hottest = max(temps, key=temps.get)
    coldest = min(temps, key=temps.get)
    assert colours[hottest] == "blue", f"the hottest bath records {colours[hottest]}"
    assert colours[coldest] == "pink", f"the coldest bath records {colours[coldest]}"
    h.shows(item, "It is endothermic, because raising the temperature")
    return (f"the {temps[hottest]:g} degree bath records {colours[hottest]!r} and the "
            f"{temps[coldest]:g} degree bath records {colours[coldest]!r}")


def q16(table, item):
    temps = dict(zip(cg.labels(table), cg.col(table, BATH)))
    head = [str(x) for x in table["headers"]]
    colours = {str(r[0]): r[head.index(MIX)] for r in table["rows"]}
    assert temps["Cold bath"] < temps["Hot bath"], "the cold bath must be the cooler one"
    assert colours["Cold bath"] == "pink", "the cold bath must record pink"
    h.shows(item, "return toward pink")
    return (f"moving from the {temps['Hot bath']:g} degree bath to the "
            f"{temps['Cold bath']:g} degree bath returns the tabulated colour to "
            f"{colours['Cold bath']!r}")


TABLE_CHECKS = {6: q6, 7: q7, 11: q11, 12: q12, 15: q15, 16: q16}


CLAIMS = [
 ("consuming some of the added",
  "EK 7.9.A.1 names addition of a chemical species as a stress; the response to added reactant is a shift toward the products, which consumes part of what was added. A rigid vessel fixes the volume, not the concentrations."),
 ("shifts toward the products, forming more NH3",
  "EK 7.9.A.1 names REMOVAL of a chemical species as a stress in its own right, alongside addition. Removing a product is relieved by forming more of it."),
 ("side that absorbs energy",
  "EK 7.9.A.1 names a change in temperature as a stress. An exothermic forward reaction releases energy, so supplying energy is relieved by the reverse direction. A temperature change moves the position, not only the rate."),
 ("decreases, because cooling favours the direction that releases energy",
  "EK 7.9.A.1, temperature stress, on an endothermic forward reaction: removing energy is relieved by the exothermic reverse direction, which consumes the gaseous product. Solids in the equation do not exempt the system."),
 ("fewer moles of gas",
  "EK 7.9.A.1 names a change in volume or pressure of a gas-phase system as a stress; compression is relieved by moving toward the side carrying fewer moles of gas."),
 ("Reaction 2",
  "EK 7.9.A.1: compression is relieved only when the two sides differ in moles of gas. The tabulated counts are compared in q6 and exactly one reaction has them equal."),
 ("Reaction 3",
  "EK 7.9.A.1: expansion is relieved by moving toward more moles of gas. The tabulated counts are compared in q7 and exactly one reaction has more on its product side."),
 ("Dilution of a reaction system",
  "EK 7.9.A.1 lists four stresses and names dilution of a reaction system separately from a change in the volume of a gas-phase system. A catalyst is on neither list."),
 ("red colour deepens",
  "EK 7.9.A.1, addition of a chemical species, with EK 7.9.A.2, which names colour of a solution as a measurable property. The stem supplies which species is coloured, so no key rests on recalling the colour of a complex ion."),
 ("fades, because removing a reactant shifts the system toward the reactants",
  "EK 7.9.A.1 names removal of a chemical species as a stress; precipitating a reactant removes it. The response consumes the coloured product, which EK 7.9.A.2 makes the observable."),
 ("Trial 1",
  "EK 7.9.A.1, removal of a chemical species. The tabulated changes are read in q11, where exactly one removes the coloured product and the colour recorded after it is paler."),
 ("Dilution is a stress under the framework",
  "EK 7.9.A.1 lists dilution of a reaction system among the stresses and EK 7.9.A.2 makes colour the property that reports it. The tabulated colour after dilution is checked in q12."),
 ("rises, because the system shifts toward the un-ionized acid",
  "EK 7.9.A.1, addition of a chemical species that is already a product of the ionization, with EK 7.9.A.2, which names pH as a measurable property. Consuming hydronium ion raises pH."),
 ("proportion of the acid present as CH3COO- falls",
  "EK 7.9.A.1, addition of a chemical species: hydronium ion is a product of the ionization, so adding it is relieved by the reverse direction. A strong acid does not destroy a weak one."),
 ("It is endothermic, because raising the temperature",
  "EK 7.9.A.1, temperature stress, with EK 7.9.A.2, colour. The direction favoured by heating is the one that absorbs energy. The tabulated colours are read in q15 and put the blue species at the hot end."),
 ("return toward pink",
  "EK 7.9.A.1 makes a temperature change a stress in either direction, so cooling is relieved by the energy-releasing direction and returns the mixture toward the colour tabulated for the cold bath, as recomputed in q16."),
 ("concentrations of the reacting gases are unchanged",
  "EK 7.9.A.1 makes a change in volume or pressure of a gas-phase system a stress. In a rigid vessel the volume is fixed and a gas taking no part in the reaction changes the amount of no reacting species in that volume, so nothing is there to be relieved."),
 ("equal moles of gas",
  "EK 7.9.A.1: a volume change is relieved by moving toward the side with a different number of moles of gas, and this equation has the same number on both sides, so no direction offers relief."),
 ("rises, because the shift toward the products releases energy",
  "EK 7.9.A.1, addition of a chemical species, with EK 7.9.A.2, which names temperature as a measurable property the principle can be used to predict. A forward shift in an exothermic reaction releases energy into an insulated flask."),
 ("Adding a catalyst",
  "EK 7.9.A.1 lists addition or removal of a chemical species, change in temperature, change in volume or pressure of a gas-phase system, and dilution of a reaction system. A catalyst is not among them."),
 ("pH, temperature, and colour of a solution",
  "EK 7.9.A.2, verbatim: experimentally measurable properties such as pH, temperature, and color of a solution."),
 ("more dissolved particles",
  "EK 7.9.A.1 lists dilution of a reaction system as a stress; lowering every concentration is relieved by moving toward the side made of more dissolved particles, which the change affects more strongly."),
 ("relieves by making more product, so the forward reaction continues",
  "EK 7.9.A.1 names removal of a chemical species as a stress, and the response to removing a product is a shift toward the products, which keeps the forward reaction running rather than halting it."),
 ("Paler than at first",
  "EK 7.9.A.1, compression of a gas-phase system, with EK 7.9.A.2, colour. The stem supplies which species is coloured and which side carries fewer moles of gas, so nothing is assumed."),
 ("concentration that does not depend on how much of it is present",
  "A stress must change something the equilibrium can respond to. A pure solid's concentration is fixed however much is present, so adding more of it leaves the system with nothing to relieve, even though EK 7.9.A.1 makes addition a stress in general."),
 ("shift toward the products, and an increase in the equilibrium amount",
  "EK 7.9.A.1, temperature stress, on an endothermic forward reaction: supplying energy is relieved by the energy-absorbing direction, which leaves more product once the system settles."),
 ("partially offsets the change",
  "EK 7.9.A.1 has the principle predict the RESPONSE to a stress. The response counters the imposed change in part: some of an added reactant is consumed, but more of it remains than before."),
 ("lower concentrations of every species",
  "EK 7.9.A.1 names dilution as a stress; adding solvent lowers every concentration and the shift that follows only partly offsets it. The equilibrium constant is set by temperature, which both flasks share."),
 ("colour of the settled mixture is different",
  "EK 7.9.A.2 names colour of a solution as an experimentally measurable property. A difference in the SETTLED colour reports a different composition at equilibrium, whereas arriving at the same state sooner is a claim about rate."),
 ("replacing part of what was removed",
  "EK 7.9.A.1 names removal of a chemical species as a stress, and the response to removing a product is a shift that makes more of it. The shift replaces part of what was taken and does not run to completion."),
]


def _extra_mutations():
    def corrupt_table(mod, cl):
        mod.QUESTIONS[5]["table"] = dict(
            headers=h7_9._T_GASCOUNT["headers"],
            rows=[[lab, eq, r, ("4" if lab == "2" else p)]
                  for lab, eq, r, p in h7_9._T_GASCOUNT["rows"]])

    def quotient_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = ("The reaction quotient falls below the equilibrium "
                                   "constant, so the system reacts forward until the two "
                                   "agree once more.")
        no_quotient_argument(mod)

    def colour_table_corrupted(mod, cl):
        mod.QUESTIONS[14]["table"] = dict(
            headers=h7_9._T_TEMP["headers"],
            rows=[[lab, t, ("pink" if lab == "Hot bath" else c)]
                  for lab, t, c in h7_9._T_TEMP["rows"]])

    return [("a gas-count cell corrupted so the keyed reaction is false", corrupt_table),
            ("a rationale arguing from the reaction quotient, which is 7.10's material",
             quotient_creeps_in),
            ("the colour recorded for the hot bath corrupted", colour_table_corrupted)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h7_9, CLAIMS, table_checks=TABLE_CHECKS, mutations=_extra_mutations())

no_quotient_argument(h7_9)
h.run(h7_9, CLAIMS, table_checks=TABLE_CHECKS)
