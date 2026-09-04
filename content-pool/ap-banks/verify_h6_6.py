"""Key audit for AP CHEMISTRY 6.6 Introduction to Enthalpy of Reaction.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  6.6.A.1  the enthalpy change gives the heat RELEASED for negative values and
           ABSORBED for positive values, at constant pressure
                    1, 2, 3, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25,
                    26, 27, 28
  6.6.A.2  products at a different temperature from their surroundings exchange
           energy to reach thermal equilibrium; thermal energy goes TO the
           surroundings in an exothermic reaction and FROM them in an
           endothermic one                     4, 5, 6, 16, 20, 21, 29
  6.6.A.3  bonds broken and formed make the products' chemical POTENTIAL energy
           differ, that difference becomes KINETIC energy of the particles, and
           that manifests as a temperature change     7, 8, 9, 24, 25, 30
  LO 6.6.A  q is the amount in moles times the molar enthalpy of reaction
                    10, 11, 12, 13, 17, 18, 23, 26

THE TWO-BY-TWO GUARD IS THE HEART OF THIS FILE. EK 6.6.A.1 pairs NEGATIVE with
released and POSITIVE with absorbed. There are exactly two ways to get an item
here wrong, and a student who has learned only one of the two words can guess
past a badly built item. So ``sign_items_are_full_two_by_twos`` asserts, for
every item whose key states both a sign and a direction, that the choice list
also offers the SAME sign with the opposite direction and the SAME direction
with the opposite sign. Without both, the item is answerable from half the
convention.

``anchors_carry_both_clauses`` then requires each of those anchors to name the
sign AND the direction, so a key cannot be pinned by whichever half happens to
be unique today.

THE EXCLUSION STATEMENT. EK 6.6.A.3's note says the technical distinctions
between enthalpy and internal energy will not be assessed. ``no_internal_energy``
bans the phrase from stems, keys, whys AND DISTRACTORS -- unlike every other
scope check in this unit, which exempts distractors -- because choosing among
options that require the distinction is assessing it.

ARITHMETIC. Every quantitative key is the amount in moles times the molar
enthalpy, recomputed from the stimulus alone, and each arithmetic distractor is
recomputed and located in the choice list by ``mistake``.

NEGATIVE CONTROL: ``python3 verify_h6_6.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h6_thermo as h6

import h6_6

DH = "Molar enthalpy of reaction (kJ/mol)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below)(?![a-z])", re.I)

_OTHER_TOPIC = [
    (re.compile(r"(?<![A-Za-z])(?:average )?bond (?:energ(?:y|ies)|enthalp(?:y|ies))"
                r"(?![A-Za-z])", re.I), "6.7's bond energies"),
    (re.compile(r"(?<![A-Za-z])enthalp(?:y|ies) of formation(?![A-Za-z])", re.I),
     "6.8's quantity"),
    (re.compile(r"(?<![A-Za-z])Hess(?![A-Za-z])", re.I), "6.9's law"),
    (re.compile(r"(?<![A-Za-z])specific heat(?![A-Za-z])", re.I), "6.4's specific heat"),
    (re.compile(r"(?<![A-Za-z])calorimet[a-z]*", re.I), "6.4's calorimetry"),
    (re.compile(r"(?<![A-Za-z])molar enthalpy of (?:fusion|vaporization)(?![A-Za-z])", re.I),
     "6.5's phase quantities"),
]

_INTERNAL_ENERGY = re.compile(r"(?<![A-Za-z])internal energy(?![A-Za-z])", re.I)

_NEGATIVE = re.compile(r"(?<![A-Za-z0-9])(?:negative|-\d)", re.I)
_POSITIVE = re.compile(r"(?<![A-Za-z0-9])(?:positive|\+\d)", re.I)
_RELEASED = re.compile(
    r"(?<![A-Za-z])(?:released|given out|to the surroundings|warms)(?![A-Za-z])", re.I)
_ABSORBED = re.compile(
    r"(?<![A-Za-z])(?:absorbed|taken in|from the surroundings|cools)(?![A-Za-z])", re.I)

_QUANTITY = re.compile(r"(?<![A-Za-z0-9.])\d[\d.]*\s*kJ(?![A-Za-z/])")
_TRANSFER = re.compile(r"(?<![A-Za-z])(?:absorbed|released)(?![A-Za-z])", re.I)

# Items whose key states BOTH a sign and a direction of transfer. Listed
# explicitly so the guard cannot quietly stop covering one that was edited.
SIGN_ITEMS = (1, 2, 12, 20, 21, 27)
# Items whose key reports an amount of energy in kJ for a directional transfer.
DIRECTIONAL_ENERGY_ITEMS = (11, 17, 18, 26)


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
    print(f"OK  {module.TOPIC[0]} figures: every measured value is carried as a table or "
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
    print(f"OK  {module.TOPIC[0]} scope: the breaking and forming of bonds is named only "
          "as EK 6.6.A.3 names it; no stem, key or why borrows 6.7's bond energies, 6.8's "
          "enthalpies of formation, 6.9's law or 6.4's calorimetry.")


def no_internal_energy(module):
    """EK 6.6.A.3's exclusion statement, enforced over DISTRACTORS too.

    The framework says the technical distinctions between enthalpy and internal
    energy will not be assessed. Every other scope check in this unit exempts
    distractors, because a wrong answer naming a neighbouring topic is a fair
    wrong answer. This one does not, because choosing among options that require
    the distinction IS assessing it.
    """
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _INTERNAL_ENERGY.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: mentions internal energy, whose distinction from "
                f"enthalpy EK 6.6.A.3's exclusion statement rules out -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} exclusion: internal energy appears nowhere, not even in "
          "a distractor, as EK 6.6.A.3's exclusion statement requires.")


def _sign_of(text):
    """Which sign the text states, or None if it states both or neither."""
    neg, pos = bool(_NEGATIVE.search(text)), bool(_POSITIVE.search(text))
    if neg and not pos:
        return "negative"
    if pos and not neg:
        return "positive"
    return None


def _direction_of(text):
    """Which direction of transfer the text states, or None for both or neither."""
    rel, abso = bool(_RELEASED.search(text)), bool(_ABSORBED.search(text))
    if rel and not abso:
        return "released"
    if abso and not rel:
        return "absorbed"
    return None


def sign_items_are_full_two_by_twos(module):
    """EK 6.6.A.1's pairing must be tested, not guessable from half of it.

    Named booleans throughout, never two tuples read in parallel -- the sign and
    the direction are separate facts about the same choice, and comparing them
    by position is how a checker in this project rejected a correct key.
    """
    for i in SIGN_ITEMS:
        item = module.QUESTIONS[i - 1]
        key = h.keyed(item)
        key_sign, key_direction = _sign_of(key), _direction_of(key)
        assert key_sign, (
            f"{module.TOPIC[0]} q{i}: listed as a sign item but the keyed choice states no "
            f"single sign -- {key!r}"
        )
        assert key_direction, (
            f"{module.TOPIC[0]} q{i}: the keyed choice states a sign without a direction "
            f"of transfer, so half the convention goes untested -- {key!r}"
        )
        # EK 6.6.A.1: negative goes with released, positive with absorbed.
        key_is_negative = key_sign == "negative"
        key_says_released = key_direction == "released"
        assert key_is_negative == key_says_released, (
            f"{module.TOPIC[0]} q{i}: the key pairs {key_sign} with {key_direction}, which "
            f"is EK 6.6.A.1 backwards -- {key!r}"
        )

        same_sign_other_direction = [
            k for k, c in enumerate(item["choices"])
            if k != item["ans"] and _sign_of(c) == key_sign
            and _direction_of(c) not in (None, key_direction)]
        same_direction_other_sign = [
            k for k, c in enumerate(item["choices"])
            if k != item["ans"] and _direction_of(c) == key_direction
            and _sign_of(c) not in (None, key_sign)]
        assert same_sign_other_direction, (
            f"{module.TOPIC[0]} q{i}: no distractor pairs {key_sign} with the OTHER "
            f"direction, so a student who knows only the sign word can answer it -- "
            f"choices {item['choices']}"
        )
        assert same_direction_other_sign, (
            f"{module.TOPIC[0]} q{i}: no distractor pairs {key_direction} with the OTHER "
            f"sign, so a student who knows only the direction word can answer it -- "
            f"choices {item['choices']}"
        )
    print(f"OK  {module.TOPIC[0]} sign convention: all {len(SIGN_ITEMS)} sign items are "
          "full two-by-twos, each keying EK 6.6.A.1's own pairing and each offering both "
          "half-right alternatives as distractors.")


def anchors_carry_both_clauses(module, claims):
    for i in SIGN_ITEMS:
        anchor = claims[i - 1][0]
        assert _sign_of(anchor), (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} names no single sign, so it "
            "could match a key with the sign reversed"
        )
        assert _direction_of(anchor), (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} names no direction, so it "
            "could match a key with the direction reversed"
        )
    print(f"OK  {module.TOPIC[0]} anchor guard: every sign-item anchor names both the sign "
          "and the direction.")


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
    print(f"OK  {module.TOPIC[0]} quantity guard: each of the "
          f"{len(DIRECTIONAL_ENERGY_ITEMS)} key(s) reporting energy in kJ says whether it "
          "was absorbed or released.")


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
        f"distractor(s); exactly one must carry it -- choices {item['choices']}"
    )
    return value_text


# ------------------------------------------------------------- stem numerics

def n11(item):
    q = h6.reaction_heat(3.00, -46.0)
    assert _close(q, -138.0), f"the heat recomputes to {q}"
    assert h6.direction(q)["exothermic"], "a negative molar enthalpy must come out a release"
    assert h6.agrees(q, h.keyed(item), transfer=True), (
        f"the recomputed q is {h6.report(q, 'kJ')} but the keyed choice says "
        f"{h6.stated_transfer(h.keyed(item))!r}: {h.keyed(item)!r}"
    )
    h.shows(item, "138 kJ released")
    mistake(item, "138 kJ absorbed", "the direction reversed while the number stays right")
    mistake(item, "46 kJ released", "the amount in moles left out")
    assert _close(46.0 / 3.00, 15.333333333333334)
    mistake(item, "15.3 kJ released", "divided by the amount instead of multiplied")
    assert _close(46.0 + 3.00, 49.0)
    mistake(item, "49 kJ released", "the two quantities added instead of multiplied")
    return (f"3.00 mol times -46 kJ/mol recomputes as {h6.report(q, 'kJ')}, with the "
            "reversed, amount-omitted, divided and added mistakes each in one distractor")


def n12(item):
    dh = h6.opposite(150.0) / 2.00
    assert _close(dh, -75.0), f"the molar enthalpy recomputes to {dh}"
    assert h6.direction(dh)["exothermic"], (
        "a reaction that RELEASED heat must come out with a negative molar enthalpy under "
        "EK 6.6.A.1"
    )
    h.shows(item, "-75 kJ/mol, a negative value because the reaction released the energy")
    assert _close(h6.opposite(150.0) * 2.00, -300.0)
    mistake(item, "-300 kJ/mol", "multiplied by the amount instead of divided")
    mistake(item, "-150 kJ/mol", "the amount in moles ignored")
    return (f"150 kJ given out by 2.00 mol recomputes the molar enthalpy as "
            f"{h6.report(dh)}, with the multiplied and amount-ignored mistakes each in one "
            "distractor")


def n13(item):
    n = 276.0 / 92.0
    assert _close(n, 3.00), f"the amount recomputes to {n}"
    h.shows(item, "3.00 mol")
    assert _close(92.0 / 276.0, 0.3333333333333333)
    mistake(item, "0.333 mol", "the division taken the other way round")
    assert _close(276.0 * 92.0, 25392.0)
    mistake(item, "25392 mol", "multiplied instead of divided")
    assert _close(276.0 - 92.0, 184.0)
    mistake(item, "184 mol", "subtracted instead of divided")
    return (f"276 kJ divided by the 92 kJ per mole released recomputes the amount as "
            f"{n:g} mol, with three recomputed mistakes each in one distractor")


def n26(item):
    q = h6.reaction_heat(0.250, 180.0)
    assert _close(q, 45.0), f"the heat recomputes to {q}"
    assert h6.direction(q)["endothermic"], "a positive molar enthalpy must come out an uptake"
    assert h6.agrees(q, h.keyed(item), transfer=True), (
        f"the recomputed q is {h6.report(q, 'kJ')} but the keyed choice says "
        f"{h6.stated_transfer(h.keyed(item))!r}"
    )
    h.shows(item, "45.0 kJ absorbed")
    mistake(item, "45.0 kJ released", "the direction reversed while the number stays right")
    mistake(item, "180 kJ absorbed", "the amount in moles left out")
    assert _close(180.0 / 0.250, 720.0)
    mistake(item, "720 kJ absorbed", "divided by the amount instead of multiplied")
    assert _close(180.0 + 0.250, 180.25)
    mistake(item, "180.25 kJ absorbed", "the two quantities added instead of multiplied")
    return (f"0.250 mol times +180 kJ/mol recomputes as {h6.report(q, 'kJ')}, with four "
            "recomputed mistakes each found in one distractor")


NUMERIC = {11: n11, 12: n12, 13: n13, 26: n26}


# -------------------------------------------------------------- table items

def q14(table, item):
    dhs = {lab: cg.cell(table, lab, DH) for lab in cg.labels(table)}
    lab = _unique_extreme(dhs, min)
    assert h6.direction(dhs[lab])["exothermic"], (
        f"the extreme reaction {lab} does not release energy at all: {dhs}")
    assert lab == "Reaction C", f"the most negative tabulated value is at {lab}: {dhs}"
    h.shows(item, "Reaction C")
    return (f"the tabulated molar enthalpies are {dhs} kJ/mol, whose unique minimum "
            f"{h6.report(dhs[lab])} is at {lab}")


def q15(table, item):
    dhs = {lab: cg.cell(table, lab, DH) for lab in cg.labels(table)}
    lab = _unique_extreme(dhs, max)
    assert h6.direction(dhs[lab])["endothermic"], (
        f"the extreme reaction {lab} does not absorb energy at all: {dhs}")
    assert lab == "Reaction B", f"the most positive tabulated value is at {lab}: {dhs}"
    h.shows(item, "Reaction B")
    return (f"the tabulated molar enthalpies are {dhs} kJ/mol, whose unique maximum "
            f"{h6.report(dhs[lab])} is at {lab}")


def q16(table, item):
    dhs = {lab: cg.cell(table, lab, DH) for lab in cg.labels(table)}
    endo = sorted(lab for lab, v in dhs.items() if h6.direction(v)["endothermic"])
    assert endo == ["Reaction B", "Reaction D"], (
        f"the endothermic reactions recompute as {endo}: {dhs}")
    h.shows(item, "Reaction B and Reaction D")
    return (f"exactly two tabulated molar enthalpies are positive, {endo}, which EK "
            f"6.6.A.1 makes absorptions of heat: {dhs}")


def q17(table, item):
    dh = cg.cell(table, "Reaction A", DH)
    q = h6.reaction_heat(2.00, dh)
    assert _close(q, -184.0), f"the heat recomputes to {q}"
    assert h6.agrees(q, h.keyed(item), transfer=True), (
        f"the recomputed q is {h6.report(q, 'kJ')} but the keyed choice says "
        f"{h6.stated_transfer(h.keyed(item))!r}"
    )
    h.shows(item, "184 kJ released")
    mistake(item, "184 kJ absorbed", "the direction reversed while the number stays right")
    mistake(item, "92 kJ released", "the amount in moles left out")
    assert _close(abs(dh) / 2.00, 46.0)
    mistake(item, "46 kJ released", "divided by the amount instead of multiplied")
    assert _close(abs(dh) + 2.00, 94.0)
    mistake(item, "94 kJ released", "the two quantities added instead of multiplied")
    return (f"2.00 mol times the tabulated {dh:g} kJ/mol recomputes as "
            f"{h6.report(q, 'kJ')}, with four recomputed mistakes each in one distractor")


def q18(table, item):
    dh = cg.cell(table, "Reaction D", DH)
    q = h6.reaction_heat(0.500, dh)
    assert _close(q, 28.5), f"the heat recomputes to {q}"
    assert h6.agrees(q, h.keyed(item), transfer=True), (
        f"the recomputed q is {h6.report(q, 'kJ')} but the keyed choice says "
        f"{h6.stated_transfer(h.keyed(item))!r}"
    )
    h.shows(item, "28.5 kJ absorbed")
    mistake(item, "28.5 kJ released", "the direction reversed while the number stays right")
    mistake(item, "57 kJ absorbed", "the amount in moles left out")
    assert _close(dh / 0.500, 114.0)
    mistake(item, "114 kJ absorbed", "divided by the amount instead of multiplied")
    assert _close(dh + 0.500, 57.5)
    mistake(item, "57.5 kJ absorbed", "the two quantities added instead of multiplied")
    return (f"0.500 mol times the tabulated {dh:g} kJ/mol recomputes as "
            f"{h6.report(q, 'kJ')}, with four recomputed mistakes each in one distractor")


def q19(table, item):
    sizes = {lab: abs(cg.cell(table, lab, DH)) for lab in cg.labels(table)}
    lab = _unique_extreme(sizes, min)
    assert lab == "Reaction E", f"the smallest tabulated magnitude is at {lab}: {sizes}"
    h.shows(item, "Reaction E")
    return (f"the sizes of the tabulated molar enthalpies are {sizes} kJ/mol, whose unique "
            f"minimum is at {lab}, so the sign gives only the direction")


TABLE_CHECKS = {14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19}


CLAIMS = [
 ("That heat is released, since a negative enthalpy change reports energy given out",
  "EK 6.6.A.1: the enthalpy change gives the amount of heat energy released for negative values. Both clauses are in the key because either can be shipped backwards."),
 ("That heat is absorbed, since a positive enthalpy change reports energy taken in",
  "EK 6.6.A.1's second half, which assigns absorbed to positive values in the same sentence."),
 ("At constant pressure",
  "EK 6.6.A.1 ends with those words, and the framework's own note adds that most reactions studied at this level are carried out that way."),
 ("To the surroundings",
  "EK 6.6.A.2 states that thermal energy is transferred to the surroundings as the reactants convert to products in an exothermic reaction."),
 ("From the surroundings",
  "EK 6.6.A.2's mirror clause for an endothermic reaction, in the same statement."),
 ("They exchange energy with the surroundings, in order to reach thermal equilibrium",
  "EK 6.6.A.2's opening sentence, verbatim in substance: products at a different temperature than their surroundings exchange energy with them to reach thermal equilibrium."),
 ("Because of the breaking and forming of bonds",
  "EK 6.6.A.3's first sentence gives exactly this reason for the products' chemical potential energy differing from the reactants'."),
 ("A change in the kinetic energy of the particles",
  "EK 6.6.A.3 states that the energy difference results in a change in the kinetic energy of the particles, the middle link of its chain."),
 ("As a temperature change",
  "EK 6.6.A.3 closes by saying the change in kinetic energy manifests as a temperature change, which is what makes the enthalpy change observable."),
 ("The amount of the reacting substance in moles and the molar enthalpy of reaction",
  "Learning objective 6.6.A names exactly these two quantities, whose product is the heat q for the reaction."),
 ("138 kJ released",
  "The learning objective's product with EK 6.6.A.1's direction for a negative value. n11 recomputes the signed value and four mistaken routes."),
 ("-75 kJ/mol, a negative value because the reaction released the energy",
  "The learning objective's product rearranged, with EK 6.6.A.1 making a release a negative value. n12 recomputes it and the multiplied and amount-ignored mistakes."),
 ("3.00 mol",
  "The learning objective's product rearranged for the amount. n13 recomputes it and three mistaken routes."),
 ("Reaction C",
  "EK 6.6.A.1 makes a negative value a release and its size the amount released. q14 recomputes the tabulated values and checks the minimum is unique and really negative."),
 ("Reaction B",
  "The same statement read the other way. q15 checks the maximum is unique and really positive."),
 ("Reaction B and Reaction D",
  "EK 6.6.A.1 with EK 6.6.A.2's name for a reaction that takes energy from the surroundings. q16 recomputes the sign of every tabulated value and checks exactly two are positive."),
 ("184 kJ released",
  "The learning objective's product using the tabulated molar enthalpy, with EK 6.6.A.1's direction. q17 recomputes the key and four mistakes."),
 ("28.5 kJ absorbed",
  "The same product for a positive tabulated value. q18 recomputes the key and four mistakes."),
 ("Reaction E",
  "EK 6.6.A.1 makes the SIZE of the enthalpy change the amount of heat and the sign only the direction. q19 recomputes every magnitude and checks the minimum is unique."),
 ("It cools, because a positive enthalpy change means energy is absorbed from the surroundings",
  "EK 6.6.A.1 makes a positive value an absorption and EK 6.6.A.2 takes that energy FROM the surroundings, which leaves them cooler."),
 ("Negative, because heat was released to the surroundings",
  "EK 6.6.A.2 sends thermal energy to the surroundings in an exothermic reaction and EK 6.6.A.1 attaches negative values to heat released."),
 ("the same amount of energy per mole, in opposite directions",
  "EK 6.6.A.1 makes the size of the enthalpy change the amount of heat and the sign the direction, so equal sizes with opposite signs are equal transfers running opposite ways."),
 ("The heat transferred doubles and the molar enthalpy of reaction is unchanged",
  "Learning objective 6.6.A makes the heat the amount in moles times the molar enthalpy, so the amount is what scales; the molar value is stated per mole and belongs to the reaction."),
 ("Bonds break and form, the chemical potential energy changes, the kinetic energy of the particles changes, and a temperature change is observed",
  "EK 6.6.A.3 runs in exactly this order, and the two middle links are what a shortened account drops."),
 ("close to zero, since the enthalpy change gives the heat released or absorbed",
  "EK 6.6.A.1 makes the enthalpy change the heat released or absorbed and EK 6.6.A.3 makes a temperature change how that shows itself, so an unmoved thermometer reports little either way."),
 ("45.0 kJ absorbed",
  "The learning objective's product with EK 6.6.A.1's direction for a positive value. n26 recomputes the key and four mistakes."),
 ("A positive enthalpy change reports energy taken in by the reaction",
  "EK 6.6.A.1 assigns released to negative values and absorbed to positive ones, so the claim has the size right and the direction wrong."),
 ("The heat of the reaction, since these reactions are carried out at constant pressure",
  "EK 6.6.A.1 gives the enthalpy change as the heat at constant pressure, and the framework's own note says most reactions at this level are carried out there, where the enthalpy change equals the heat of reaction."),
 ("They transfer energy to the surroundings until thermal equilibrium is reached",
  "EK 6.6.A.2 has products at a different temperature exchange energy with the surroundings to reach thermal equilibrium, and hotter products are the ones giving energy up."),
 ("Breaking and forming bonds changes the chemical potential energy, the difference appears as kinetic energy of the particles, and that is read as a temperature change",
  "EK 6.6.A.3's chain whole and in order, with the potential and kinetic links the right way round."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[2]["q"] = "In the diagram above, what condition is assumed?"
        no_figure_language(mod)

    def bond_energy_creeps_in(mod, cl):
        mod.QUESTIONS[6]["q"] = (
            "Using average bond energies, why do the potential energies differ?")
        no_other_topic(mod)

    def internal_energy_in_a_distractor(mod, cl):
        # NOT in the key -- in a distractor. Every other scope check in this
        # unit would let it through, and choosing among options that require
        # the excluded distinction is exactly what the exclusion statement
        # forbids.
        ch = list(mod.QUESTIONS[2]["choices"])
        ch[4] = "Only when the internal energy of the system is constant"
        mod.QUESTIONS[2]["choices"] = ch
        no_internal_energy(mod)

    def sign_key_reversed(mod, cl):
        # The key moved to the choice pairing NEGATIVE with absorbed. Every
        # choice is untouched, so they stay distinct and the new anchor matches
        # only the new key; only the two-by-two guard's pairing assertion can
        # reject it.
        mod.QUESTIONS[0]["ans"] = 1
        cl[0] = ("That heat is absorbed, since a negative enthalpy change reports energy "
                 "taken in", cl[0][1])
        sign_items_are_full_two_by_twos(mod)

    def sign_item_loses_its_half_right_distractor(mod, cl):
        # The choice pairing the key's sign with the opposite direction is
        # replaced by something with no sign in it at all. The key is still
        # right and every choice is still distinct -- the item has simply
        # become answerable by anyone who knows the word "negative".
        ch = list(mod.QUESTIONS[20]["choices"])
        ch[1] = "The sign cannot be determined without the amount of reactant used"
        mod.QUESTIONS[20]["choices"] = ch
        sign_items_are_full_two_by_twos(mod)

    def sign_anchor_drops_its_direction(mod, cl):
        cl[19] = ("It cools", cl[19][1])
        anchors_carry_both_clauses(mod, cl)

    def energy_key_loses_its_direction(mod, cl):
        ch = list(mod.QUESTIONS[10]["choices"])
        ch[0] = "138 kJ"
        mod.QUESTIONS[10]["choices"] = ch
        cl[10] = ("138 kJ", cl[10][1])
        energy_keys_state_a_direction(mod)

    def numeric_key_direction_reversed(mod, cl):
        # The arithmetic stays right and the direction goes backwards.
        mod.QUESTIONS[25]["ans"] = 1
        cl[25] = ("45.0 kJ released", cl[25][1])

    def most_negative_moved(mod, cl):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h6_6._T_RXN["headers"],
            rows=[["Reaction A", "-92"], ["Reaction B", "+180"], ["Reaction C", "-566"],
                  ["Reaction D", "+57"], ["Reaction E", "-800"]])

    def all_signs_flipped(mod, cl):
        # Every tabulated sign reversed and every magnitude preserved, so the
        # endothermic pair becomes the exothermic one and nothing but the sign
        # check notices.
        mod.QUESTIONS[15]["table"] = dict(
            headers=h6_6._T_RXN["headers"],
            rows=[["Reaction A", "+92"], ["Reaction B", "-180"], ["Reaction C", "+566"],
                  ["Reaction D", "-57"], ["Reaction E", "+46"]])

    def keyed_reaction_value_changed(mod, cl):
        mod.QUESTIONS[16]["table"] = dict(
            headers=h6_6._T_RXN["headers"],
            rows=[["Reaction A", "-95"], ["Reaction B", "+180"], ["Reaction C", "-566"],
                  ["Reaction D", "+57"], ["Reaction E", "-46"]])

    def distractor_drifts_off_its_mistake(mod, cl):
        ch = list(mod.QUESTIONS[17]["choices"])
        ch[3] = "200 kJ absorbed"
        mod.QUESTIONS[17]["choices"] = ch

    return [("a stem referring to a diagram the bank cannot show", figure_language),
            ("a stem borrowing 6.7's average bond energies", bond_energy_creeps_in),
            ("internal energy appearing in a DISTRACTOR, which the exclusion statement "
             "still forbids", internal_energy_in_a_distractor),
            ("a key pairing a negative enthalpy change with heat absorbed", sign_key_reversed),
            ("a sign item whose same-sign, opposite-direction distractor was removed",
             sign_item_loses_its_half_right_distractor),
            ("a sign anchor cut back to the direction alone", sign_anchor_drops_its_direction),
            ("a key reporting a quantity of energy with no direction",
             energy_key_loses_its_direction),
            ("a numeric key with the arithmetic right and the direction reversed",
             numeric_key_direction_reversed),
            ("the most negative tabulated value moved off the keyed reaction", most_negative_moved),
            ("every tabulated sign reversed, which preserves every magnitude and swaps "
             "the endothermic pair", all_signs_flipped),
            ("the tabulated value changed under a numeric key", keyed_reaction_value_changed),
            ("a distractor drifted off the mistake it was written to test",
             distractor_drifts_off_its_mistake)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h6.selftest()
    h.selftest(h6_6, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h6_6)
no_other_topic(h6_6)
no_internal_energy(h6_6)
sign_items_are_full_two_by_twos(h6_6)
anchors_carry_both_clauses(h6_6, CLAIMS)
energy_keys_state_a_direction(h6_6)
h.run(h6_6, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
