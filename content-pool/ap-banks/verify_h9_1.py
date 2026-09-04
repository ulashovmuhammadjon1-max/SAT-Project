"""Key audit for AP CHEMISTRY 9.1 Introduction to Entropy.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  9.1.A.1  entropy increases when matter becomes more dispersed -- the phase
           changes toward the gas state, an increase in the volume of a gas at
           constant temperature, and a surplus of gas-phase product moles over
           gas-phase reactant moles
                   1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                   21, 22, 24, 26, 27, 28, 29, 30
  9.1.A.2  entropy increases when energy is dispersed -- the distribution of
           kinetic energy among the particles of a gas broadens as the
           temperature rises            6, 7, 19, 20, 23, 25, 30

THE SIGN IS THE ANSWER HERE, so every gas-phase item's key is checked against a
COUNT rather than against the author's word. ``gas_rule`` parses the equation
out of the stem, counts the moles of gas on each side, and fails if the keyed
direction disagrees. Its negative controls flip an equation and, separately,
flip the direction word in a key while leaving the anchor intact -- the second
is the one that matters, because a key can be turned backwards without
disturbing anything the structural gate looks at.

SCOPE. 9.2 owns the arithmetic of absolute entropies and 9.3 owns every energy
quantity, so ``no_next_topic_arithmetic`` asserts that nothing here states a
value in J or kJ. A topic that quietly does the next topic's arithmetic is not
the topic the student selected.

NEGATIVE CONTROL: ``python3 verify_h9_1.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h9_check as h9

import h9_1

RCT = "Total moles of gas-phase reactants"
PRD = "Total moles of gas-phase products"

# A standalone J or kJ token. Explicit lookarounds, never \b: a digit and a
# letter are both word characters, so \b is not a boundary where it looks
# like one.
_ENERGY_UNIT = re.compile(r"(?<![A-Za-z])k?J(?![A-Za-z])")

# How dispersed the matter is in each state, in the order EK 9.1.A.1 names:
# solid to liquid to gas, "as the individual particles become freer to move".
DISPERSAL = {"solid": 0, "liquid": 1, "gas": 2}


def no_next_topic_arithmetic(module):
    """9.2 owns the absolute-entropy arithmetic; 9.3 owns the energies."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _ENERGY_UNIT.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: states a value in {hit.group(0)!r}, which is "
                f"9.2's or 9.3's arithmetic -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item states an entropy or energy value; the "
          "topic stays on the sign and the relative magnitude.")


# ---------------------------------------------------------------- stem numerics

def gas_rule(item):
    """EK 9.1.A.1's gas-mole rule, recomputed from the equation in the stem.

    Named booleans, not a pair of parallel tuples compared by index. The
    direction the key states and the direction the count gives are two separate
    facts and are written as two separate names, because a verifier that builds
    them as tuples and compares position 0 against position 0 is how this
    project once rejected a correct key.
    """
    dn = h9.delta_n_gas(h9.equation_from(item["q"]))
    key = h.keyed(item).lower()
    says_increase = key.startswith("positive")
    says_decrease = key.startswith("negative")
    assert says_increase != says_decrease, (
        f"the keyed choice must open with exactly one direction: {h.keyed(item)!r}"
    )
    counted_increase = dn > 0
    assert counted_increase == says_increase, (
        f"the equation in the stem changes the moles of gas by {dn:+d}, but the key says "
        f"the entropy change is {'positive' if says_increase else 'negative'}"
    )
    return (f"counting the gas-phase species on each side of the equation in the stem "
            f"gives a change of {dn:+d} moles of gas, matching the keyed direction")


def n12(item):
    """The one equation whose two gas totals are EQUAL, so the rule is silent."""
    dn = h9.delta_n_gas(h9.equation_from(item["q"]))
    assert dn == 0, f"the equation in the stem changes the moles of gas by {dn:+d}, not 0"
    h.shows(item, "the total moles of gas are the same on both sides")
    return ("counting the gas-phase species on each side of the equation in the stem "
            "gives equal totals, so the rule predicts no increase")


def n22(item):
    counts = [int(x) for x in
              re.findall(r"(?<![0-9])(\d+)\s+moles?\s+of\s+gas", item["q"])]
    assert len(counts) == 4, f"expected four gas-mole counts in the stem, found {counts}"
    p_gain = counts[1] - counts[0]
    q_gain = counts[3] - counts[2]
    assert p_gain > q_gain, (
        f"the stem gives reaction P a gain of {p_gain:+d} moles of gas against reaction "
        f"Q's {q_gain:+d}, so P is not the larger increase the key claims"
    )
    h.shows(item, "Reaction P")
    return (f"the two gains recomputed from the stem are {p_gain:+d} and {q_gain:+d} "
            f"moles of gas, so the keyed reaction has the larger increase")


NUMERIC = {8: gas_rule, 9: gas_rule, 10: gas_rule, 11: gas_rule, 12: n12,
           21: gas_rule, 22: n22, 29: gas_rule}


# ------------------------------------------------------------------ table items

def gas_mole_changes(table):
    return {lab: cg.cell(table, lab, PRD) - cg.cell(table, lab, RCT)
            for lab in cg.labels(table)}


def q13(table, item):
    d = gas_mole_changes(table)
    biggest = max(d, key=d.get)
    assert biggest == "Z", f"the largest tabulated increase is at {biggest}: {d}"
    assert len([v for v in d.values() if abs(v - d[biggest]) < 1e-12]) == 1, (
        f"the largest tabulated increase must be unique, or the key is not the only "
        f"defensible answer: {d}"
    )
    h.shows(item, "Reaction Z")
    return f"the tabulated gas-mole changes are {d}, whose unique maximum is at {biggest}"


def q14(table, item):
    d = gas_mole_changes(table)
    falling = [lab for lab, v in d.items() if v < 0]
    assert falling == ["X"], f"the tabulated reactions losing moles of gas are {falling}"
    h.shows(item, "Reaction X")
    return (f"the tabulated gas-mole changes are {d}, and exactly one of them is "
            f"negative, at {falling[0]}")


def q15(table, item):
    d = gas_mole_changes(table)
    level = [lab for lab, v in d.items() if abs(v) < 1e-12]
    assert level == ["Y"], f"the tabulated reactions with equal gas totals are {level}"
    h.shows(item, "Reaction Y, because the total moles of gas are equal")
    return (f"the tabulated gas-mole changes are {d}, and exactly one row has the two "
            f"totals equal, at {level[0]}")


def dispersal_changes(table):
    out = {}
    for row in table["rows"]:
        lab, before, after = str(row[0]), str(row[1]).strip().lower(), str(row[2]).strip().lower()
        assert before in DISPERSAL, f"row {row} names an unknown state before the change"
        assert after in DISPERSAL, f"row {row} names an unknown state after the change"
        out[lab] = DISPERSAL[after] - DISPERSAL[before]
    return out


def q26(table, item):
    d = dispersal_changes(table)
    rising = sorted(lab for lab, v in d.items() if v > 0)
    assert rising == ["1", "3"], f"the tabulated processes dispersing matter are {rising}"
    h.shows(item, "Processes 1 and 3")
    return (f"ranking the tabulated states as solid, liquid, gas gives changes {d}, and "
            f"the processes that move toward the gas state are {rising}")


def q27(table, item):
    d = dispersal_changes(table)
    falling = sorted(lab for lab, v in d.items() if v < 0)
    assert falling == ["2", "4"], f"the tabulated processes concentrating matter are {falling}"
    h.shows(item, "Processes 2 and 4")
    return (f"ranking the tabulated states as solid, liquid, gas gives changes {d}, and "
            f"the processes that move toward the solid state are {falling}")


TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 26: q26, 27: q27}


CLAIMS = [
 ("Matter becoming more dispersed",
  "EK 9.1.A.1's opening sentence: entropy increases when matter becomes more dispersed, as when particles become freer to move."),
 ("particles become freer to move and generally occupy a larger volume",
  "EK 9.1.A.1 names the solid-to-liquid change as a dispersal of matter in which the individual particles become freer to move and generally occupy a larger volume."),
 ("matter present becomes less dispersed",
  "EK 9.1.A.1 read in reverse: a gas collapsing into a liquid concentrates matter that had been dispersed, so the entropy falls. A phase change does not alter the number of molecules."),
 ("able to move within a larger space",
  "EK 9.1.A.1, verbatim in substance: for a gas the entropy increases when there is an increase in volume at constant temperature, and the gas molecules are able to move within a larger space."),
 ("confined to a smaller space",
  "EK 9.1.A.1's volume statement run backwards: reducing the volume at constant temperature reduces the space the molecules can move within, so the entropy falls."),
 ("distribution of kinetic energy among the particles broadens",
  "EK 9.1.A.2: according to kinetic molecular theory the distribution of kinetic energy among the particles of a gas broadens as the temperature increases, and the entropy of the system therefore increases."),
 ("600 K, because entropy increases with increasing temperature",
  "EK 9.1.A.2's conclusion that the entropy of the system increases with an increase in temperature. Energy really is less dispersed in the colder sample, which is a reason for it to have the SMALLER entropy."),
 ("total moles of gas-phase products exceed the total moles of gas-phase reactants",
  "EK 9.1.A.1's closing rule, verbatim in substance. The gas-mole change is recomputed from the equation in the stem by gas_rule."),
 ("four moles of gas are replaced by two moles of gas",
  "EK 9.1.A.1's gas-mole rule applied in the falling direction. Recomputed from the equation in the stem by gas_rule."),
 ("a gas is produced where there was none among the reactants",
  "EK 9.1.A.1's gas-mole rule with no gas-phase reactant at all, so the total rises from none to one. Recomputed by gas_rule."),
 ("three moles of gas become two moles of gas",
  "EK 9.1.A.1's gas-mole rule counting moles rather than molecular size or identity. Recomputed by gas_rule from the equation in the stem."),
 ("the total moles of gas are the same on both sides",
  "EK 9.1.A.1 predicts an increase only where the gas-phase product moles exceed the gas-phase reactant moles, and here the two totals are equal. Recomputed by n12."),
 ("Reaction Z",
  "EK 9.1.A.1's gas-mole rule across four tabulated reactions. q13 recomputes every gas-mole change and checks that the largest is unique."),
 ("Reaction X",
  "EK 9.1.A.1's rule predicts a decrease where the gas-phase product moles fall short. q14 recomputes the changes and checks exactly one is negative."),
 ("Reaction Y, because the total moles of gas are equal",
  "EK 9.1.A.1's rule turns on a comparison of two totals and is silent where they agree. q15 recomputes the changes and checks exactly one row is level."),
 ("far freer to move as the solid becomes a gas",
  "EK 9.1.A.1 describes the phase changes toward the gas state as a dispersal of matter in which the particles become freer to move and occupy a larger volume; sublimation does both at once."),
 ("matter that was dispersed as a gas becomes a fixed solid",
  "EK 9.1.A.1's dispersal criterion run backwards: fixing gas particles into a solid concentrates matter, so the entropy falls."),
 ("freer to move and occupy a much larger volume",
  "EK 9.1.A.1 names the liquid-to-gas change as a dispersal of matter in which the individual particles become freer to move and generally occupy a larger volume."),
 ("Matter becoming more dispersed and energy becoming more dispersed",
  "EK 9.1.A.1 opens with the dispersal of matter and EK 9.1.A.2 with the dispersal of energy; together they are this topic's whole account of when entropy increases."),
 ("Entropy also increases with temperature",
  "EK 9.1.A.2 supplies a route to higher entropy that does not involve volume at all, since the distribution of kinetic energy broadens as the temperature rises."),
 ("a gas is formed from liquids alone",
  "EK 9.1.A.1's gas-mole rule where the reactants contribute no gas at all. Recomputed by gas_rule from the equation in the stem."),
 ("Reaction P, because it produces the greater increase in the moles of gas",
  "Learning objective 9.1.A asks for relative magnitude, and EK 9.1.A.1 ties the increase to the surplus of gas-phase product moles. n22 recomputes both gains from the stem."),
 ("Heating a sealed sample of argon",
  "EK 9.1.A.2 attributes the temperature effect to the broadening distribution of kinetic energy, which is a dispersal of ENERGY; every other change listed moves matter into a larger volume."),
 ("expand from a small bulb into a much larger one",
  "EK 9.1.A.1 attributes the volume effect to the gas molecules being able to move within a larger space, which is a dispersal of MATTER, while the temperature changes listed are EK 9.1.A.2's route."),
 ("It broadens, and the entropy of the gas therefore increases",
  "EK 9.1.A.2 states both halves in one sentence: the distribution broadens as the temperature increases, and as a result the entropy of the system increases."),
 ("Processes 1 and 3",
  "EK 9.1.A.1 names the solid-to-liquid and liquid-to-gas changes as dispersals of matter. q26 ranks the tabulated states and recomputes which rows move toward the gas."),
 ("Processes 2 and 4",
  "EK 9.1.A.1's criterion applied to the tabulated changes that move toward the solid state. q27 recomputes which rows those are."),
 ("10.0 L sample, because its particles can move within a larger space",
  "EK 9.1.A.1's volume statement, with equal amounts and equal temperatures leaving the volume as the only difference between the two samples."),
 ("three moles of gas appear where the reactants contained none",
  "EK 9.1.A.1's gas-mole rule with no gas-phase reactant. Recomputed by gas_rule from the equation in the stem."),
 ("Compressing the sample into a smaller volume",
  "EK 9.1.A.1 raises the entropy of a gas when its volume rises and EK 9.1.A.2 when its temperature rises, so reducing the space available to the molecules is the one listed change that lowers it."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the figure above, which change increases the entropy?"
        h9.no_figure_language(mod)

    def entropy_value_creeps_in(mod, cl):
        ch = list(mod.QUESTIONS[0]["choices"])
        ch[1] = "The entropy change of the sample is 130 J/(mol K)"
        mod.QUESTIONS[0]["choices"] = ch
        no_next_topic_arithmetic(mod)

    def equation_reversed(mod, cl):
        # The stem's equation turned round while the key still says the moles of
        # gas fall. Confirmed to violate gas_rule, and confirmed to violate
        # NOTHING ELSE first: the opening of the mutated stem is distinct from
        # every other stem's, so the duplicate-opening check cannot fire ahead
        # of it and let this control pass for a reason it did not test.
        mod.QUESTIONS[10]["q"] = (
            "For the reaction 2 CO2(g) gives 2 CO(g) + O2(g), what is the sign of the "
            "entropy change?")

    def key_direction_flipped(mod, cl):
        # The defect the structural gate cannot see: the direction word swapped
        # while the anchor phrase is left exactly as it was, so the key now
        # claims an increase over an equation that loses two moles of gas.
        ch = list(mod.QUESTIONS[8]["choices"])
        ch[0] = "Positive, because four moles of gas are replaced by two moles of gas"
        mod.QUESTIONS[8]["choices"] = ch

    def table_maximum_moved(mod, cl):
        mod.QUESTIONS[12]["table"] = dict(
            headers=h9_1._T_GASMOLES["headers"],
            rows=[["W", "2", "4"], ["X", "3", "2"], ["Y", "1", "1"], ["Z", "4", "4"]])

    def table_maximum_tied(mod, cl):
        # Two tabulated reactions gaining three moles each: the key is then no
        # longer the only defensible answer, which q13 must refuse. The keyed
        # row is listed FIRST on purpose, so max() still returns it and the
        # identity assertion passes -- otherwise this control would fire on
        # "the maximum is at W" and the uniqueness check it exists to exercise
        # would never run.
        mod.QUESTIONS[12]["table"] = dict(
            headers=h9_1._T_GASMOLES["headers"],
            rows=[["Z", "4", "7"], ["W", "2", "5"], ["X", "3", "2"], ["Y", "1", "1"]])

    def phase_table_corrupted(mod, cl):
        mod.QUESTIONS[25]["table"] = dict(
            headers=h9_1._T_PHASES["headers"],
            rows=[["1", "solid", "liquid"], ["2", "gas", "liquid"],
                  ["3", "gas", "liquid"], ["4", "gas", "solid"]])

    def unknown_state_in_table(mod, cl):
        mod.QUESTIONS[25]["table"] = dict(
            headers=h9_1._T_PHASES["headers"],
            rows=[["1", "solid", "plasma"], ["2", "gas", "liquid"],
                  ["3", "liquid", "gas"], ["4", "gas", "solid"]])

    def relative_magnitude_reversed(mod, cl):
        mod.QUESTIONS[21]["q"] = (
            "Reaction P converts 1 mole of gas into 2 moles of gas, and reaction Q "
            "converts 1 mole of gas into 3 moles of gas. Which has the greater increase "
            "in entropy on the framework's gas-mole rule?")

    return [
        ("a stem pointing at a figure the bank cannot show", figure_language),
        ("a numeric entropy value, which is 9.2's arithmetic", entropy_value_creeps_in),
        ("the equation in a stem reversed while the key still says the entropy falls",
         equation_reversed),
        ("a key's direction word flipped with its anchor phrase left intact",
         key_direction_flipped),
        ("the tabulated gas-mole maximum moved off the keyed reaction",
         table_maximum_moved),
        ("a second tabulated reaction tied with the keyed one for the maximum",
         table_maximum_tied),
        ("a tabulated phase change altered so the keyed pair is wrong",
         phase_table_corrupted),
        ("a state in the phase table that the dispersal ranking does not know",
         unknown_state_in_table),
        ("the two gas-mole gains in a relative-magnitude stem exchanged",
         relative_magnitude_reversed),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h9_1, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h9.no_figure_language(h9_1)
no_next_topic_arithmetic(h9_1)
h.run(h9_1, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
