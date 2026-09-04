"""Key audit for AP CHEMISTRY 6.5 Energy of Phase Changes.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  6.5.A.1  energy must go IN for a substance to melt or boil and the system's
           energy rises; a system RELEASES energy when it freezes or condenses
           and its energy falls; the temperature of a pure substance remains
           constant during a phase change
                    1, 2, 3, 4, 5, 6, 11, 12, 17, 18, 20, 21, 22, 23, 27, 30
  6.5.A.2  the energy absorbed in a phase change equals the energy released in
           the complementary change; the molar enthalpy of condensation is the
           NEGATIVE of that of vaporization; the molar enthalpy of fusion serves
           for melting and for freezing
                    7, 8, 9, 12, 17, 19, 22, 23, 25, 26, 30
  LO 6.5.A  q is the amount in moles times the molar enthalpy of the transition
                    10, 11, 13, 14, 15, 16, 18, 24, 26, 28, 29

THREE GUARDS, one for each way this topic can lie to a student.

``energy_keys_state_a_direction``  A key reading "19.3 kJ" is what a student
    with the arithmetic right and the physics backwards would write. Every key
    reporting a quantity of energy for a transition states whether it was
    absorbed or released, and ``anchors_carry_the_direction`` requires the
    anchor to carry that word too -- so the guard holds even before a swapped
    distractor exists to make cg_check notice.

``complement_keys_say_negative``  EK 6.5.A.2's example is that the molar
    enthalpy of condensation is the NEGATIVE of the molar enthalpy of
    vaporization. A key stating the bare magnitude would be read as "the same",
    which is the distractor sitting beside it. So the complement keys must say
    "the negative of", and the guard asserts it.

``constant_temperature_keys``  EK 6.5.A.1's last sentence is the half most
    easily lost: energy goes in while the thermometer stands still. The four
    items built on it must key the constancy, and none of them may have the
    temperature rising or falling during the change.

ARITHMETIC. Every quantitative key is the amount in moles times the molar
enthalpy, recomputed here from the stimulus alone, and every arithmetic
distractor is recomputed AND located in the choice list by ``mistake`` -- a
distractor that has drifted off the error it was written to test, or into a
second correct answer, is caught by the value going missing.

SCOPE. 6.4 owns q = mc(delta T) and the specific heat capacity; no item here
warms a substance without changing its state. 6.6 owns the molar enthalpy of
reaction and 6.9 owns Hess's law, so nothing here is a chemical change.

NEGATIVE CONTROL: ``python3 verify_h6_5.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h6_thermo as h6

import h6_5

FUS = "Molar enthalpy of fusion (kJ/mol)"
VAP = "Molar enthalpy of vaporization (kJ/mol)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|heating curve above)(?![a-z])", re.I)

_OTHER_TOPIC = [
    (re.compile(r"(?<![A-Za-z])specific heat(?![A-Za-z])", re.I), "6.4's specific heat"),
    (re.compile(r"(?<![A-Za-z])heat capacit(?:y|ies)(?![A-Za-z])", re.I), "6.4's heat capacity"),
    (re.compile(r"(?<![A-Za-z])calorimet[a-z]*", re.I), "6.4's calorimetry"),
    (re.compile(r"(?<![A-Za-z])enthalpy of reaction(?![A-Za-z])", re.I), "6.6's quantity"),
    (re.compile(r"(?<![A-Za-z])enthalp(?:y|ies) of formation(?![A-Za-z])", re.I),
     "6.8's quantity"),
    (re.compile(r"(?<![A-Za-z])Hess(?![A-Za-z])", re.I), "6.9's law"),
    (re.compile(r"(?<![A-Za-z])bond energ(?:y|ies)(?![A-Za-z])", re.I), "6.7's bond energies"),
    (re.compile(r"(?<![A-Za-z])energy diagram(?![A-Za-z])", re.I), "6.2's representation"),
]

_QUANTITY = re.compile(r"(?<![A-Za-z0-9.])\d[\d.]*\s*kJ(?![A-Za-z/])")
_TRANSFER = re.compile(r"(?<![A-Za-z])(?:absorbed|released)(?![A-Za-z])", re.I)

_NEGATIVE_OF = re.compile(r"(?<![A-Za-z])the negative of(?![A-Za-z])", re.I)
_SAME_AS = re.compile(r"(?<![A-Za-z])the same as(?![A-Za-z])", re.I)

_CONSTANT = re.compile(
    r"(?<![A-Za-z])(?:remains constant|stays constant|hold(?:s)? still|"
    r"without changing its temperature|does not change)(?![A-Za-z])", re.I)
_TEMP_MOVES = re.compile(
    r"(?<![A-Za-z])temperature\s+(?:rises|falls|increases|decreases|climbs|drops)"
    r"(?![A-Za-z])", re.I)

# Items whose key reports an amount of energy for a transition that HAS a
# direction. Listed explicitly so the guard cannot quietly stop covering one.
DIRECTIONAL_ENERGY_ITEMS = (11, 12, 17, 18, 30)
# Items built on EK 6.5.A.2's "negative of" relationship.
COMPLEMENT_ITEMS = (8, 19)
# Items built on EK 6.5.A.1's constant temperature.
CONSTANT_TEMPERATURE_ITEMS = (5, 6, 20, 21)


def _facing(item):
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(x) for x in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every measured quantity is carried as a table or "
          "stated in the stem, and no item points at a picture.")


def no_other_topic(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in (item["q"], h.keyed(item), item["why"]):
            for pat, owner in _OTHER_TOPIC:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: a stem, key or why uses {hit.group(0)!r}, "
                    f"which is {owner} -- {text[:70]!r}"
                )
    print(f"OK  {module.TOPIC[0]} scope: no stem, key or why borrows 6.4's specific heat "
          "capacity or calorimeter, 6.6's enthalpy of reaction, 6.7's bond energies or "
          "6.9's law.")


def energy_keys_state_a_direction(module):
    for i in DIRECTIONAL_ENERGY_ITEMS:
        key = h.keyed(module.QUESTIONS[i - 1])
        assert _QUANTITY.search(key), (
            f"{module.TOPIC[0]} q{i}: listed as a directional energy item but the keyed "
            f"choice reports no quantity in kJ -- {key!r}"
        )
        assert _TRANSFER.search(key), (
            f"{module.TOPIC[0]} q{i}: the keyed choice reports a quantity of energy "
            f"without saying whether it was absorbed or released -- {key!r}"
        )
    print(f"OK  {module.TOPIC[0]} sign guard: each of the {len(DIRECTIONAL_ENERGY_ITEMS)} "
          "key(s) reporting a quantity of energy says whether it was absorbed or released.")


def anchors_carry_the_direction(module, claims):
    for i in DIRECTIONAL_ENERGY_ITEMS:
        anchor = claims[i - 1][0]
        assert _TRANSFER.search(anchor), (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} names a quantity of energy "
            "without its direction, so it would still match a key with the sign reversed"
        )
    print(f"OK  {module.TOPIC[0]} anchor guard: every directional-energy anchor carries "
          "absorbed or released as well as its number.")


def complement_keys_say_negative(module, claims):
    """EK 6.5.A.2's example is a NEGATIVE, not a magnitude.

    A key reading "23.4 kJ/mol" would be read as agreeing with the distractor
    that says the two are the same, which is the one thing EK 6.5.A.2 rules out.
    """
    for i in COMPLEMENT_ITEMS:
        item = module.QUESTIONS[i - 1]
        key, anchor = h.keyed(item), claims[i - 1][0]
        says_negative = bool(_NEGATIVE_OF.search(key))
        says_same = bool(_SAME_AS.search(key))
        assert says_negative, (
            f"{module.TOPIC[0]} q{i}: the keyed choice does not say the complementary "
            f"molar enthalpy is THE NEGATIVE OF the other, which is EK 6.5.A.2's own "
            f"wording -- {key!r}"
        )
        assert not says_same, (
            f"{module.TOPIC[0]} q{i}: the keyed choice calls the two the same as well as "
            f"the negative of one another -- {key!r}"
        )
        assert _NEGATIVE_OF.search(anchor), (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} drops the words the negative "
            "of, so it would match a key claiming the two are equal"
        )
        # And a distractor must offer the "same as" reading, or the item does
        # not test the distinction at all.
        same_distractors = [k for k, c in enumerate(item["choices"])
                            if k != item["ans"] and _SAME_AS.search(c)]
        assert same_distractors, (
            f"{module.TOPIC[0]} q{i}: no distractor offers the equal-magnitude reading, "
            "so the item never tests EK 6.5.A.2's sign at all"
        )
    print(f"OK  {module.TOPIC[0]} complement guard: {len(COMPLEMENT_ITEMS)} item(s) key "
          "the NEGATIVE of the complementary molar enthalpy, with the equal-magnitude "
          "reading offered as a distractor.")


def constant_temperature_keys(module):
    """EK 6.5.A.1's last sentence, held in the keys that depend on it."""
    for i in CONSTANT_TEMPERATURE_ITEMS:
        key = h.keyed(module.QUESTIONS[i - 1])
        assert _CONSTANT.search(key), (
            f"{module.TOPIC[0]} q{i}: the keyed choice does not state that the temperature "
            f"stays where it is, which is what EK 6.5.A.1's last sentence says -- {key!r}"
        )
        hit = _TEMP_MOVES.search(key)
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the keyed choice has the temperature {hit.group(0)!r} "
            f"during a phase change, which EK 6.5.A.1 forbids -- {key!r}"
        )
    print(f"OK  {module.TOPIC[0]} constancy guard: each of the "
          f"{len(CONSTANT_TEMPERATURE_ITEMS)} item(s) built on EK 6.5.A.1's last sentence "
          "keys the constant temperature and none has it moving.")


# ------------------------------------------------------------------- helpers

def _close(a, b, tol=1e-9):
    return abs(a - b) < tol


def _unique_extreme(values, pick):
    lab = pick(values, key=values.get)
    ties = [k for k, v in values.items() if _close(v, values[lab])]
    assert ties == [lab], f"the extreme is not unique: {ties} all hold {values[lab]}"
    return lab


def mistake(item, value_text, origin):
    """A recomputed WRONG value must sit in exactly one distractor, never in the key."""
    assert not cg.contains_phrase(h.keyed(item), value_text), (
        f"the mistaken value {value_text!r} ({origin}) appears in the KEYED choice, so the "
        f"item has two defensible answers -- {h.keyed(item)!r}"
    )
    hits = [k for k, c in enumerate(item["choices"])
            if k != item["ans"] and cg.contains_phrase(c, value_text)]
    assert len(hits) == 1, (
        f"the recomputed mistake {value_text!r} ({origin}) appears in {len(hits)} "
        f"distractor(s); exactly one must carry it, or the item has stopped testing that "
        f"mistake -- choices {item['choices']}"
    )
    return value_text


# ------------------------------------------------------------- stem numerics

def n11(item):
    q = h6.phase_heat(3.00, 40.7)
    assert _close(q, 122.1), f"the heat recomputes to {q}"
    assert h6.direction(q)["endothermic"], (
        "boiling takes energy in under EK 6.5.A.1, so the molar enthalpy is positive"
    )
    h.shows(item, "122.1 kJ absorbed")
    mistake(item, "122.1 kJ released", "the direction reversed while the number stays right")
    mistake(item, "40.7 kJ absorbed", "the amount in moles left out")
    assert _close(40.7 / 3.00, 13.566666666666666)
    mistake(item, "13.6 kJ absorbed", "divided by the amount instead of multiplied")
    assert _close(40.7 + 3.00, 43.7)
    mistake(item, "43.7 kJ absorbed", "the two quantities added instead of multiplied")
    return (f"3.00 mol times 40.7 kJ/mol recomputes as {q:g} kJ taken in, with the "
            "reversed, amount-omitted, divided and added mistakes each found in exactly "
            "one distractor")


def n12(item):
    q = h6.phase_heat(0.250, h6.opposite(44.0))
    assert _close(q, -11.0), f"the heat recomputes to {q}"
    assert h6.direction(q)["exothermic"], (
        "condensing releases energy under EK 6.5.A.1, so its molar enthalpy is negative"
    )
    assert h6.agrees(q, h.keyed(item), transfer=True), (
        f"the recomputed q is {h6.report(q, 'kJ')} but the keyed choice says "
        f"{h6.stated_transfer(h.keyed(item))!r}: {h.keyed(item)!r}"
    )
    h.shows(item, "11.0 kJ released")
    mistake(item, "11.0 kJ absorbed", "the direction reversed while the number stays right")
    mistake(item, "44.0 kJ released", "the amount in moles left out")
    assert _close(44.0 / 0.250, 176.0)
    mistake(item, "176 kJ released", "divided by the amount instead of multiplied")
    mistake(item, "0.250 kJ released", "the molar enthalpy left out")
    return (f"0.250 mol times the negative of 44.0 kJ/mol recomputes as "
            f"{h6.report(q, 'kJ')}, so the sample gives the energy up")


def n13(item):
    n = 24.04 / 6.01
    assert _close(n, 4.00), f"the amount recomputes to {n}"
    h.shows(item, "4.00 mol")
    assert _close(6.01 / 24.04, 0.25)
    mistake(item, "0.250 mol", "the division taken the other way round")
    assert _close(24.04 * 6.01, 144.4804)
    mistake(item, "144 mol", "multiplied instead of divided")
    assert _close(24.04 - 6.01, 18.03)
    mistake(item, "18.0 mol", "subtracted instead of divided")
    mistake(item, "6.01 mol", "the molar enthalpy reported as the amount")
    return (f"24.04 kJ divided by 6.01 kJ/mol recomputes the amount as {n:g} mol, with "
            "the reversed, multiplied, subtracted and copied mistakes each in one "
            "distractor")


def n26(item):
    dh = 20.4 / 0.500
    assert _close(dh, 40.8), f"the molar enthalpy recomputes to {dh}"
    h.shows(item, "40.8 kJ/mol")
    assert _close(20.4 * 0.500, 10.2)
    mistake(item, "10.2 kJ/mol", "multiplied instead of divided")
    mistake(item, "20.4 kJ/mol", "the amount in moles ignored")
    assert _close(0.500 / 20.4, 0.024509803921568627)
    mistake(item, "0.0245 kJ/mol", "the division taken the other way round")
    assert _close(20.4 + 0.500, 20.9)
    mistake(item, "20.9 kJ/mol", "added instead of divided")
    return (f"20.4 kJ divided by 0.500 mol recomputes the molar enthalpy of fusion as "
            f"{dh:g} kJ/mol, with four recomputed mistakes each found in one distractor")


def n29(item):
    q1 = h6.phase_heat(2.00, 30.0)
    q2 = h6.phase_heat(3.00, 20.0)
    assert _close(q1, 60.0) and _close(q2, 60.0), (q1, q2)
    assert _close(q1, q2), "the item's whole point is that the two products agree"
    # The distractor values must be the products a student gets by pairing the
    # wrong amount with the wrong enthalpy.
    assert _close(3.00 * 30.0, 90.0) and _close(2.00 * 20.0, 40.0)
    h.shows(item, "each absorbs 60.0 kJ")
    mistake(item, "90.0 kJ", "the larger amount paired with the larger molar enthalpy")
    mistake(item, "40.0 kJ", "the smaller amount paired with the smaller molar enthalpy")
    return (f"2.00 mol times 30.0 kJ/mol and 3.00 mol times 20.0 kJ/mol both recompute as "
            f"{q1:g} kJ, while the crossed pairings give the 90.0 and 40.0 kJ distractors")


def n30(item):
    q = h6.phase_heat(2.00, h6.opposite(25.0))
    assert _close(q, -50.0), f"the heat recomputes to {q}"
    assert h6.agrees(q, h.keyed(item), transfer=True), (
        f"the recomputed q is {h6.report(q, 'kJ')} but the keyed choice says "
        f"{h6.stated_transfer(h.keyed(item))!r}: {h.keyed(item)!r}"
    )
    h.shows(item, "50.0 kJ released")
    mistake(item, "50.0 kJ absorbed", "the direction reversed while the number stays right")
    mistake(item, "25.0 kJ released", "the amount in moles left out")
    assert _close(25.0 / 2.00, 12.5)
    mistake(item, "12.5 kJ released", "divided by the amount instead of multiplied")
    assert _close(25.0 + 2.00, 27.0)
    mistake(item, "27.0 kJ released", "the two quantities added instead of multiplied")
    return (f"2.00 mol times the negative of 25.0 kJ/mol recomputes as "
            f"{h6.report(q, 'kJ')}, so the vapour gives the energy up")


NUMERIC = {11: n11, 12: n12, 13: n13, 26: n26, 29: n29, 30: n30}


# -------------------------------------------------------------- table items

def q14(table, item):
    vaps = {lab: cg.cell(table, lab, VAP) for lab in cg.labels(table)}
    lab = _unique_extreme(vaps, max)
    assert lab == "Mercury", f"the largest tabulated enthalpy of vaporization is at {lab}"
    h.shows(item, "Mercury")
    return (f"the tabulated molar enthalpies of vaporization are {vaps} kJ/mol, whose "
            f"unique maximum is at {lab}")


def q15(table, item):
    fus = {lab: cg.cell(table, lab, FUS) for lab in cg.labels(table)}
    lab = _unique_extreme(fus, min)
    assert lab == "Methane", f"the smallest tabulated enthalpy of fusion is at {lab}"
    h.shows(item, "Methane")
    return (f"the tabulated molar enthalpies of fusion are {fus} kJ/mol, whose unique "
            f"minimum is at {lab}")


def q16(table, item):
    ratios = {lab: cg.cell(table, lab, VAP) / cg.cell(table, lab, FUS)
              for lab in cg.labels(table)}
    lab = _unique_extreme(ratios, min)
    assert lab == "Ammonia", f"the smallest tabulated ratio is at {lab}: {ratios}"
    h.shows(item, "Ammonia")
    return (f"dividing each tabulated enthalpy of vaporization by the same substance's "
            f"enthalpy of fusion gives {({k: round(v, 3) for k, v in ratios.items()})}, "
            f"whose unique minimum is at {lab}")


def q17(table, item):
    q = h6.phase_heat(2.00, h6.opposite(cg.cell(table, "Water", FUS)))
    assert _close(q, -12.02), f"the heat recomputes to {q}"
    assert h6.direction(q)["exothermic"], (
        "freezing releases energy under EK 6.5.A.1, so its molar enthalpy is negative"
    )
    assert h6.agrees(q, h.keyed(item), transfer=True), (
        f"the recomputed q is {h6.report(q, 'kJ')} but the keyed choice says "
        f"{h6.stated_transfer(h.keyed(item))!r}"
    )
    h.shows(item, "12.02 kJ released")
    mistake(item, "12.02 kJ absorbed", "the direction reversed while the number stays right")
    assert _close(2.00 * cg.cell(table, "Water", VAP), 81.4)
    mistake(item, "81.4 kJ released", "the tabulated enthalpy of VAPORIZATION used instead")
    mistake(item, "6.01 kJ released", "the amount in moles left out")
    assert _close(cg.cell(table, "Water", FUS) / 2.00, 3.005)
    mistake(item, "3.01 kJ released", "divided by the amount instead of multiplied")
    return (f"2.00 mol times the negative of the tabulated "
            f"{cg.cell(table, 'Water', FUS):g} kJ/mol recomputes as {h6.report(q, 'kJ')}, "
            "with the reversed, wrong-transition, amount-omitted and divided mistakes each "
            "in one distractor")


def q18(table, item):
    q = h6.phase_heat(0.500, cg.cell(table, "Ethanol", VAP))
    assert _close(q, 19.3), f"the heat recomputes to {q}"
    assert h6.direction(q)["endothermic"], "boiling takes energy in under EK 6.5.A.1"
    h.shows(item, "19.3 kJ absorbed")
    mistake(item, "19.3 kJ released", "the direction reversed while the number stays right")
    mistake(item, "38.6 kJ absorbed", "the amount in moles left out")
    assert _close(cg.cell(table, "Ethanol", FUS) / 2.0, 2.465)
    mistake(item, "2.47 kJ absorbed", "the tabulated enthalpy of FUSION used instead")
    assert _close(cg.cell(table, "Ethanol", VAP) / 0.500, 77.2)
    mistake(item, "77.2 kJ absorbed", "divided by the amount instead of multiplied")
    return (f"0.500 mol times the tabulated {cg.cell(table, 'Ethanol', VAP):g} kJ/mol "
            f"recomputes as {q:g} kJ taken in, with four recomputed mistakes each in one "
            "distractor")


def q19(table, item):
    vap = cg.cell(table, "Ammonia", VAP)
    cond = h6.opposite(vap)
    assert _close(cond, -23.4), f"the condensation enthalpy recomputes to {cond}"
    assert h6.direction(vap)["endothermic"] and h6.direction(cond)["exothermic"], (
        "the complementary pair must run in opposite directions, or EK 6.5.A.2 is not "
        "being applied at all"
    )
    h.shows(item, "The negative of 23.4 kJ/mol")
    mistake(item, "The negative of 5.65 kJ/mol", "the tabulated enthalpy of FUSION used")
    assert _close((vap + cg.cell(table, "Ammonia", FUS)) / 2.0, 14.525)
    return (f"the tabulated molar enthalpy of vaporization is {vap:g} kJ/mol, so EK "
            f"6.5.A.2 makes the condensation value {cond:g} kJ/mol, opposite in sign and "
            "equal in size")


TABLE_CHECKS = {14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19}


CLAIMS = [
 ("Energy must be transferred to the system",
  "EK 6.5.A.1's opening sentence: energy must be transferred to a system to cause a substance to melt or boil."),
 ("It increases",
  "EK 6.5.A.1 states that the energy of the system therefore increases as it undergoes a solid-to-liquid phase transition."),
 ("It releases energy",
  "EK 6.5.A.1 states that a system releases energy when it freezes or condenses, the mirror of the transfer melting and boiling require."),
 ("It decreases",
  "EK 6.5.A.1 states that the energy of the system decreases as it undergoes a liquid-to-solid or gas-to-liquid phase transition."),
 ("It remains constant",
  "EK 6.5.A.1's last sentence: the temperature of a pure substance remains constant during a phase change."),
 ("Into the phase change itself, which increases the energy of the system without changing its temperature",
  "EK 6.5.A.1 states both halves of the same interval: energy is transferred in and the energy of the system increases, while the temperature of a pure substance stays put."),
 ("They are equal",
  "EK 6.5.A.2's opening sentence: the energy absorbed during a phase change is equal to the energy released during a complementary phase change in the opposite direction."),
 ("It is the negative of the molar enthalpy of vaporization",
  "EK 6.5.A.2's own worked example, in its own words, and the word NEGATIVE is what separates it from the equal-magnitude distractor beside it."),
 ("The energy absorbed when melting a substance and the energy released when freezing it",
  "EK 6.5.A.2 names exactly these two uses for the molar enthalpy of fusion, which is its complementary rule applied to one pair of transitions."),
 ("The amount of the substance in moles and the molar enthalpy of the transition",
  "Learning objective 6.5.A names exactly these two quantities as what q for a phase transition is based on."),
 ("122.1 kJ absorbed",
  "The learning objective's product with EK 6.5.A.1's direction for boiling. n11 recomputes the key and the reversed, amount-omitted, divided and added mistakes."),
 ("11.0 kJ released",
  "EK 6.5.A.2 makes condensation the negative of vaporization and EK 6.5.A.1 has a condensing system release energy. n12 recomputes the signed value and checks the key's direction word against it."),
 ("4.00 mol",
  "The learning objective's product rearranged for the amount. n13 recomputes it and four mistaken routes."),
 ("Mercury",
  "The energy for one mole is the molar enthalpy itself. q14 recomputes the tabulated enthalpies of vaporization and checks the maximum is unique."),
 ("Methane",
  "The same reading for melting. q15 checks the minimum tabulated enthalpy of fusion is unique."),
 ("Ammonia",
  "A comparison of the two transitions within one substance. q16 recomputes all five ratios of vaporization to fusion and checks the minimum is unique."),
 ("12.02 kJ released",
  "EK 6.5.A.2 lets the enthalpy of fusion give the energy released on freezing, and EK 6.5.A.1 makes freezing a release. q17 recomputes the signed value and four mistakes, including the wrong transition's tabulated value."),
 ("19.3 kJ absorbed",
  "The learning objective's product using the tabulated enthalpy of vaporization, with EK 6.5.A.1's direction. q18 recomputes the key and four mistakes."),
 ("The negative of 23.4 kJ/mol",
  "EK 6.5.A.2's example applied to a tabulated substance. q19 recomputes the value and checks the pair really runs in opposite directions."),
 ("While the sample melts and while it boils, since the temperature of a pure substance remains constant during a phase change",
  "EK 6.5.A.1's last sentence applied to a heating experiment: the two stages at which the substance is changing state are the two at which the reading holds."),
 ("the temperature remains constant but the energy of the system increases",
  "EK 6.5.A.1 states both about the same interval, which is why the pair is not a contradiction."),
 ("Positive, because energy must be transferred to the system for it to melt",
  "EK 6.5.A.1 has energy transferred INTO a melting system so its energy increases, and EK 6.5.A.2's example makes the complementary transition the negative member of the pair."),
 ("Negative, because the system releases energy as it freezes",
  "EK 6.5.A.1 states that a system releases energy when it freezes and that its energy decreases, and EK 6.5.A.2 makes freezing the negative of melting."),
 ("The molar enthalpy of fusion is the one that belongs to melting",
  "EK 6.5.A.2 attaches the enthalpy of fusion to melting and freezing and the enthalpy of vaporization to boiling and condensing, and the learning objective pairs the amount with the enthalpy of the transition taking place."),
 ("the energy absorbed in a phase change equals the energy released in the complementary change in the opposite direction",
  "EK 6.5.A.2's opening sentence, which is exactly why one number serves both directions."),
 ("40.8 kJ/mol",
  "EK 6.5.A.2 makes the energy released on freezing equal to that absorbed on melting the same amount. n26 recomputes the division and four mistaken routes."),
 ("Melting and vaporizing",
  "EK 6.5.A.1 has energy transferred INTO a system to melt or boil it and RELEASED when it freezes or condenses, which splits the four transitions into two pairs."),
 ("three times as much, since the heat is the amount in moles times the molar enthalpy",
  "Learning objective 6.5.A makes the heat that product, so tripling the amount triples the heat while the molar enthalpy, a property of the substance, is unchanged."),
 ("each absorbs 60.0 kJ",
  "The learning objective's product, computed for both samples. n29 recomputes the two products, checks they agree, and recomputes the crossed pairings that give the distractors."),
 ("50.0 kJ released",
  "EK 6.5.A.2 with EK 6.5.A.1 for a condensation. n30 recomputes the signed value and checks the key's direction word against it."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the heating curve above, what must happen for melting?"
        no_figure_language(mod)

    def calorimetry_creeps_in(mod, cl):
        mod.QUESTIONS[0]["q"] = (
            "Using the specific heat of the solid, what must happen for it to melt?")
        no_other_topic(mod)

    def energy_key_loses_its_direction(mod, cl):
        ch = list(mod.QUESTIONS[10]["choices"])
        ch[0] = "122.1 kJ"
        mod.QUESTIONS[10]["choices"] = ch
        cl[10] = ("122.1 kJ", cl[10][1])
        energy_keys_state_a_direction(mod)

    def anchor_loses_its_direction(mod, cl):
        cl[16] = ("12.02 kJ", cl[16][1])
        anchors_carry_the_direction(mod, cl)

    def condensation_key_says_absorbed(mod, cl):
        # The arithmetic stays right, the direction goes backwards. Every choice
        # stays distinct and the new anchor matches only the new key, so only
        # n12's comparison against the SIGNED recomputed value can reject it.
        mod.QUESTIONS[11]["ans"] = 1
        cl[11] = ("11.0 kJ absorbed", cl[11][1])

    def complement_key_drops_the_negative(mod, cl):
        # The key moved to the choice calling the two molar enthalpies the same.
        # EK 6.5.A.2 says the opposite in as many words.
        mod.QUESTIONS[7]["ans"] = 1
        cl[7] = ("It is the same as the molar enthalpy of vaporization", cl[7][1])
        complement_keys_say_negative(mod, cl)

    def complement_item_loses_its_distractor(mod, cl):
        # The equal-magnitude reading removed from the choice list. The key is
        # still right, but the item no longer tests the sign EK 6.5.A.2 is
        # about, and nothing else would notice.
        ch = list(mod.QUESTIONS[18]["choices"])
        ch[1] = "The negative of 40.7 kJ/mol, taken from a different substance"
        mod.QUESTIONS[18]["choices"] = ch
        complement_keys_say_negative(mod, cl)

    def constancy_key_has_the_temperature_move(mod, cl):
        ch = list(mod.QUESTIONS[4]["choices"])
        ch[0] = "It remains constant while the temperature rises steadily"
        mod.QUESTIONS[4]["choices"] = ch
        cl[4] = ("It remains constant while the temperature rises", cl[4][1])
        constant_temperature_keys(mod)

    def constancy_key_drops_the_constancy(mod, cl):
        ch = list(mod.QUESTIONS[19]["choices"])
        ch[0] = "While the sample melts and while it boils"
        mod.QUESTIONS[19]["choices"] = ch
        cl[19] = ("While the sample melts and while it boils", cl[19][1])
        constant_temperature_keys(mod)

    def vaporization_maximum_moved(mod, cl):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h6_5._T_PHASE["headers"],
            rows=[["Water", "6.01", "40.7"], ["Ethanol", "4.93", "38.6"],
                  ["Ammonia", "5.65", "23.4"], ["Methane", "0.94", "80.0"],
                  ["Mercury", "2.29", "59.1"]])

    def ratio_made_ambiguous(mod, cl):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h6_5._T_PHASE["headers"],
            rows=[["Water", "6.01", "40.7"], ["Ethanol", "4.93", "20.4082"],
                  ["Ammonia", "5.65", "23.4"], ["Methane", "0.94", "8.17"],
                  ["Mercury", "2.29", "59.1"]])

    def keyed_substance_enthalpy_changed(mod, cl):
        # The tabulated enthalpy of fusion of water changed, so the keyed
        # 12.02 kJ is no longer what the table gives.
        mod.QUESTIONS[16]["table"] = dict(
            headers=h6_5._T_PHASE["headers"],
            rows=[["Water", "7.01", "40.7"], ["Ethanol", "4.93", "38.6"],
                  ["Ammonia", "5.65", "23.4"], ["Methane", "0.94", "8.17"],
                  ["Mercury", "2.29", "59.1"]])

    def distractor_drifts_off_its_mistake(mod, cl):
        # The wrong-transition distractor on the freezing item edited to a
        # number that is not the mistake it was written to test. Five distinct
        # choices, one correct answer, and the item has quietly stopped testing
        # the confusion between fusion and vaporization.
        ch = list(mod.QUESTIONS[16]["choices"])
        ch[2] = "70.0 kJ released"
        mod.QUESTIONS[16]["choices"] = ch

    return [("a stem referring to a heating curve the bank cannot show", figure_language),
            ("a stem borrowing 6.4's specific heat", calorimetry_creeps_in),
            ("a key reporting a quantity of energy with no direction",
             energy_key_loses_its_direction),
            ("an anchor cut back to a bare number while the key keeps its direction",
             anchor_loses_its_direction),
            ("a key calling a condensation an absorption, with the arithmetic still right",
             condensation_key_says_absorbed),
            ("a key calling the complementary molar enthalpy the SAME rather than the "
             "negative", complement_key_drops_the_negative),
            ("a complement item whose equal-magnitude distractor was removed, so it no "
             "longer tests the sign", complement_item_loses_its_distractor),
            ("a constancy key with the temperature rising during the change",
             constancy_key_has_the_temperature_move),
            ("a constancy key that drops the constancy altogether",
             constancy_key_drops_the_constancy),
            ("the largest tabulated enthalpy of vaporization moved off the keyed substance",
             vaporization_maximum_moved),
            ("a second tabulated substance given the keyed substance's ratio",
             ratio_made_ambiguous),
            ("the tabulated enthalpy of the keyed substance changed under a numeric key",
             keyed_substance_enthalpy_changed),
            ("a distractor drifted off the mistake it was written to test",
             distractor_drifts_off_its_mistake)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h6.selftest()
    h.selftest(h6_5, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h6_5)
no_other_topic(h6_5)
energy_keys_state_a_direction(h6_5)
anchors_carry_the_direction(h6_5, CLAIMS)
complement_keys_say_negative(h6_5, CLAIMS)
constant_temperature_keys(h6_5)
h.run(h6_5, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
