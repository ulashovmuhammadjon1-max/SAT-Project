"""Key audit for AP CHEMISTRY 6.8 Enthalpy of Formation.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  6.8.A.1   tables of standard enthalpies of formation can be used to calculate
            the standard enthalpies of reactions, by the sum over the PRODUCTS
            minus the sum over the REACTANTS
                     1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                     19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
  6.6.A.1   the enthalpy change gives the heat energy RELEASED for negative
            values and ABSORBED for positive ones, at constant pressure
                     4, 6, 7, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 27,
                     28, 30
  6.6.A.2   the exothermic and endothermic words for those two cases
                     6, 7, and every keyed enthalpy of reaction

THE SUBTRACTION RUNS ONE WAY. Products minus reactants. Reversing it gives the
same magnitude with the wrong sign, and unlike a wrong magnitude that is a
number a student would go on to act on. Three separate guards stand on it:
``enthalpy_keys_state_a_direction`` requires every keyed enthalpy of reaction to
name exothermic or endothermic as well as its number,
``anchors_carry_the_direction`` requires the anchor to carry it too so the anchor
cannot match a sign-flipped key, and each table check compares the key's word
against the SIGN of the recomputed value through ``h6_thermo.agrees`` -- named
booleans, never two tuples read in parallel. ``signed_anchors`` covers the three
items whose key reports a signed value with no direction word attached.

THE REVERSED VALUE IS ALWAYS A DISTRACTOR, and ``mistake`` locates it, so an item
cannot quietly stop testing the one error it exists to test. Locating it goes
through ``h6_thermo.present``, which compares a signed value RAW: ``normalize``
drops a leading '+' and keeps '-', which once let an anchor for an endothermic
key match the exothermic distractor. ``h6_thermo.selftest`` negative-controls
that matcher, and this file will not run without it.

NOTHING IS ASSUMED, INCLUDING THE ZEROS. The framework nowhere states that an
element in its standard state has a standard enthalpy of formation of zero, so
h6_8.py prints those zeros in the table and every number below is read FROM THAT
TABLE. ``species_are_tabulated`` further asserts that every substance named in
every stated equation has a row, so an equation cannot quietly reach for a value
the student was not given. Every equation is atom- and charge-balanced by
``h_equation``, and appears VERBATIM in the stem of the item whose check uses it.

SCOPE. 6.7 owns the average bond energies and 6.9 owns Hess's law; no item here
reaches an enthalpy by either route. The CED attaches an exclusion statement to
6.9 -- the concept of state functions will not be assessed -- so ``no_excluded``
bans that phrase from every student-facing string and from every rationale.

NEGATIVE CONTROL: ``python3 verify_h6_8.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h_equation as eq
import h6_thermo as h6

import h6_8

FORMCOL = "Standard enthalpy of formation (kJ/mol)"

# Every reaction this module states, keyed by the item that states it. Each
# string must appear VERBATIM in that item's stem, which is asserted below, so
# the equation a check uses is the equation the student reads.
E1 = "CH4(g) + 2 O2(g) gives CO2(g) + 2 H2O(l)"
E2 = "2 H2(g) + O2(g) gives 2 H2O(l)"
E3 = "N2(g) + 3 H2(g) gives 2 NH3(g)"
E4 = "CaCO3(s) gives CaO(s) + CO2(g)"
E5 = "2 SO2(g) + O2(g) gives 2 SO3(g)"
E6 = "N2(g) + O2(g) gives 2 NO(g)"
E7 = "2 CO(g) + O2(g) gives 2 CO2(g)"
E8 = "2 NH3(g) gives N2(g) + 3 H2(g)"
E9 = "C(s) + O2(g) gives CO2(g)"
E10 = "2 NO(g) + O2(g) gives 2 NO2(g)"
E11 = "4 Fe(s) + 3 O2(g) gives 2 Fe2O3(s)"

REACTIONS = {
    5: [E2],
    11: [E1], 12: [E1], 13: [E1],
    14: [E2], 15: [E3], 16: [E4], 17: [E5], 18: [E6], 19: [E7], 20: [E8],
    21: [E9], 22: [E10], 23: [E11],
    24: [E3],
    25: [E8, E3],
}

# Items whose key reports a signed enthalpy of reaction with a direction word.
ENTHALPY_ITEMS = tuple(range(13, 24))
# Items whose key reports a signed value with NO direction word -- a tabulated
# entry or one of the two sums. Their anchors must still carry the sign.
SIGNED_ITEMS = (10, 11, 12)

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|picture|image|as shown|shown below|shown above|"
    r"the graph|graph above|graph below)(?![a-z])", re.I)

_OTHER_TOPIC = [
    (re.compile(r"(?<![A-Za-z])bond (?:enthalp(?:y|ies)|energ(?:y|ies))(?![A-Za-z])", re.I),
     "6.7's average bond energies"),
    (re.compile(r"(?<![A-Za-z])Hess(?![A-Za-z])", re.I), "6.9's law"),
    (re.compile(r"(?<![A-Za-z])specific heat(?![A-Za-z])", re.I), "6.4's specific heat"),
    (re.compile(r"(?<![A-Za-z])calorimet[a-z]*", re.I), "6.4's calorimetry"),
    (re.compile(r"(?<![A-Za-z])molar enthalpy of (?:fusion|vaporization|reaction)(?![A-Za-z])",
                re.I), "6.5's and 6.6's quantities"),
]

# The CED's exclusion statement on 6.9. Banned from EVERY string, including
# distractors and rationales -- an excluded concept has no place even as a wrong
# answer, because a student reading the rationale would take it as examinable.
_EXCLUDED = re.compile(r"(?<![A-Za-z])state functions?(?![A-Za-z])", re.I)

_SIGNED_ENTHALPY = re.compile(r"(?<![A-Za-z0-9.])[-+]\d[\d.]*\s*kJ/mol(?![A-Za-z])")
_DIRECTION = re.compile(r"(?<![A-Za-z0-9])(?:exothermic|endothermic)(?![A-Za-z0-9])", re.I)


# ------------------------------------------------------------------- helpers

def _facing(item):
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(x) for x in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def _species_name(term):
    """'2 H2O(l)' to 'H2O(l)'. The phase label is part of the table's row name."""
    m = re.match(r"^\d+\s+(\S.*)$", term.strip())
    return (m.group(1) if m else term).strip()


def _coefficient(term):
    m = re.match(r"^(\d+)\s+\S", term.strip())
    return int(m.group(1)) if m else 1


def _side(half):
    return [(_coefficient(t), _species_name(t)) for t in half.split(" + ")]


def sides(equation):
    """``(products, reactants)`` as ``(coefficient, name)`` pairs, from the equation."""
    left, right = equation.split(" gives ")
    return _side(right), _side(left)


def hf(table, name):
    """One standard enthalpy of formation, read from the module's own table."""
    return cg.cell(table, name, FORMCOL)


def _priced(table, terms):
    return [(n, hf(table, name)) for n, name in terms]


def product_sum(table, equation):
    products, _ = sides(equation)
    return sum(n * v for n, v in _priced(table, products))


def reactant_sum(table, equation):
    _, reactants = sides(equation)
    return sum(n * v for n, v in _priced(table, reactants))


def delta_h(table, equation):
    """EK 6.8.A.1's EQN, through h6_thermo so the order is written once."""
    products, reactants = sides(equation)
    return h6.formation_enthalpy(_priced(table, products), _priced(table, reactants))


def _close(a, b, tol=1e-9):
    return abs(a - b) < tol


def signed(value):
    """A value as this module writes it in a choice: '-891 kJ/mol', '0 kJ/mol'."""
    return "0 kJ/mol" if value == 0 else f"{value:+g} kJ/mol"


def key_shows(item, value_text, what):
    """The recomputed value sits in the KEYED choice and in no distractor."""
    assert h6.present(h.keyed(item), value_text), (
        f"the recomputed {what} {value_text!r} is not in the keyed choice {h.keyed(item)!r}"
    )
    also = [k for k, c in enumerate(item["choices"])
            if k != item["ans"] and h6.present(c, value_text)]
    assert not also, (
        f"the recomputed {what} {value_text!r} also appears in choice(s) {also} -- "
        f"{item['choices']}"
    )
    return value_text


def mistake(item, value_text, origin):
    """A recomputed WRONG value must sit in exactly one distractor, never the key."""
    assert not h6.present(h.keyed(item), value_text), (
        f"the mistaken value {value_text!r} ({origin}) appears in the KEYED choice, so the "
        f"item has two defensible answers -- {h.keyed(item)!r}"
    )
    hits = [k for k, c in enumerate(item["choices"])
            if k != item["ans"] and h6.present(c, value_text)]
    assert len(hits) == 1, (
        f"the recomputed mistake {value_text!r} ({origin}) appears in {len(hits)} "
        f"distractor(s); exactly one must carry it -- choices {item['choices']}"
    )
    return value_text


def _unique_extreme(values, pick):
    lab = pick(values, key=values.get)
    ties = [k for k, v in values.items() if _close(v, values[lab])]
    assert ties == [lab], f"the extreme is not unique: {ties} all hold {values[lab]}"
    return lab


# --------------------------------------------------------------- module gates

def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every standard enthalpy of formation is carried in "
          "a table and no item points at a picture.")


def no_other_topic(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in (item["q"], h.keyed(item), item["why"]):
            for pat, owner in _OTHER_TOPIC:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: a stem, key or why uses {hit.group(0)!r}, "
                    f"which is {owner} -- {text[:70]!r}"
                )
    print(f"OK  {module.TOPIC[0]} scope: no stem, key or why reaches an enthalpy by 6.7's "
          "bond energies or 6.9's law, or borrows 6.4's calorimetry.")


def no_excluded(module):
    """The CED's exclusion statement on 6.9, enforced across every string."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _EXCLUDED.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: uses {hit.group(0)!r}. The CED's exclusion "
                "statement on 6.9 says the concept of state functions will not be assessed, "
                f"so it does not belong even in a distractor -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} exclusions: the concept of state functions, which the CED "
          "says will not be assessed, appears nowhere -- not in a stem, a choice or a why.")


def equations_are_stated_and_balanced(module):
    """Every reaction a check uses appears in its own stem, and balances."""
    n = 0
    for i, equations in sorted(REACTIONS.items()):
        stem = module.QUESTIONS[i - 1]["q"]
        for equation in equations:
            n += 1
            assert equation in stem, (
                f"{module.TOPIC[0]} q{i}: the check uses the equation {equation!r}, which "
                f"does not appear in the stem the student reads -- {stem[:90]!r}"
            )
            assert eq.atom_balanced(equation), (
                f"{module.TOPIC[0]} q{i}: {equation!r} does not conserve atoms -- "
                f"{eq.report(equation)}"
            )
            assert eq.charge_balanced(equation), (
                f"{module.TOPIC[0]} q{i}: {equation!r} does not conserve charge -- "
                f"{eq.report(equation)}"
            )
    print(f"OK  {module.TOPIC[0]} equations: {n} statement(s) of a reaction found verbatim in "
          "their own stems and atom- and charge-balanced from the written formulas.")


def species_are_tabulated(module):
    """Nothing a stated equation names may be missing from the table.

    A substance with no row would have to be priced from memory, which is
    exactly what the printed zeros exist to avoid.
    """
    table = h6_8._T_FORM
    listed = {cg.normalize(lab) for lab in cg.labels(table)}
    named = set()
    for equations in REACTIONS.values():
        for equation in equations:
            products, reactants = sides(equation)
            for _, name in products + reactants:
                named.add(name)
    missing = sorted(x for x in named if cg.normalize(x) not in listed)
    assert not missing, (
        f"{module.TOPIC[0]}: the stated equations name {missing}, which the table does not "
        "price, so a student would have to supply the value from memory"
    )
    print(f"OK  {module.TOPIC[0]} sourcing: all {len(named)} substance(s) named in the stated "
          f"equations have a row in the table, including the {sum(1 for lab in cg.labels(table) if hf(table, lab) == 0)} "
          "tabulated at zero, which the framework nowhere states.")


def enthalpy_keys_state_a_direction(module):
    for i in ENTHALPY_ITEMS:
        key = h.keyed(module.QUESTIONS[i - 1])
        assert _SIGNED_ENTHALPY.search(key), (
            f"{module.TOPIC[0]} q{i}: listed as an enthalpy item but the keyed choice "
            f"reports no signed value in kJ/mol -- {key!r}"
        )
        assert _DIRECTION.search(key), (
            f"{module.TOPIC[0]} q{i}: the keyed choice reports an enthalpy of reaction "
            f"without saying whether it is exothermic or endothermic -- {key!r}"
        )
    print(f"OK  {module.TOPIC[0]} sign guard: each of the {len(ENTHALPY_ITEMS)} key(s) "
          "reporting an enthalpy of reaction states its direction as well as its number.")


def anchors_carry_the_direction(module, claims):
    for i in ENTHALPY_ITEMS:
        anchor = claims[i - 1][0]
        assert _DIRECTION.search(anchor), (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} names a value without its "
            "direction, so it would still match a key with the sign reversed"
        )
        assert _SIGNED_ENTHALPY.search(anchor), (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} names a direction without a "
            "signed value"
        )
    print(f"OK  {module.TOPIC[0]} anchor guard: every enthalpy anchor carries the sign AND "
          "exothermic or endothermic.")


def signed_anchors(module, claims):
    """The items whose key is a bare signed value still pin the sign."""
    for i in SIGNED_ITEMS:
        anchor = claims[i - 1][0]
        assert _SIGNED_ENTHALPY.search(anchor) or anchor.startswith("0 kJ/mol"), (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} reports a tabulated value or a "
            "sum without its sign, so it would match the sign-dropped distractor"
        )
    print(f"OK  {module.TOPIC[0]} sum guard: the {len(SIGNED_ITEMS)} anchor(s) on a tabulated "
          "value or a partial sum carry their sign.")


# -------------------------------------------------------------- table items

def _enthalpy_item(table, item, i, expected, wrong):
    """Recompute one reaction's standard enthalpy and check the key against it."""
    (equation,) = REACTIONS[i]
    dh = delta_h(table, equation)
    assert _close(dh, expected), f"{equation!r} recomputes to {dh}, not {expected}"
    key_shows(item, signed(dh), "standard enthalpy of reaction")
    assert h6.agrees(dh, h.keyed(item)), (
        f"{equation!r} recomputes to {h6.report(dh)}, but the keyed choice says "
        f"{h6.stated_direction(h.keyed(item))!r}: {h.keyed(item)!r}"
    )
    for value, origin in wrong:
        mistake(item, signed(value), origin)
    return (f"the tabulated values give a product sum of {product_sum(table, equation):g} and "
            f"a reactant sum of {reactant_sum(table, equation):g} kJ/mol for {equation!r}, so "
            f"EK 6.8.A.1's subtraction gives {h6.report(dh)}, with {len(wrong)} mistaken "
            "route(s) each recomputed into one distractor")


def q8(table, item):
    values = {lab: hf(table, lab) for lab in cg.labels(table)}
    lab = _unique_extreme(values, min)
    assert lab == "CaCO3(s)", f"the most negative tabulated value is at {lab}: {values}"
    h.shows(item, lab)
    return (f"the tabulated standard enthalpies of formation are {values} kJ/mol, whose "
            f"unique minimum -- the value furthest below zero -- is at {lab}")


def q9(table, item):
    listed = {cg.normalize(lab): lab for lab in cg.labels(table)}
    for c in item["choices"]:
        assert cg.normalize(c) in listed, (
            f"choice {c!r} is not a row of the table, so this item cannot be settled by "
            "reading it"
        )
    values = {c: hf(table, c) for c in item["choices"]}
    positive = sorted(c for c, v in values.items() if v > 0)
    assert len(positive) == 1, (
        f"exactly one of the five choices must be tabulated above zero; {positive} are, "
        f"from {values}"
    )
    h.shows(item, positive[0])
    # The table must hold more than one positive entry, or the item would be
    # testing a single exception rather than the sign of the tabulated values.
    all_positive = sorted(lab for lab in cg.labels(table) if hf(table, lab) > 0)
    assert len(all_positive) >= 2, (
        f"only {all_positive} is tabulated above zero, so the sign carries no weight in this "
        "table"
    )
    return (f"the five offered substances are tabulated at {values} kJ/mol, of which exactly "
            f"one is above zero, and the table holds {all_positive} above zero in all")


def q10(table, item):
    value = hf(table, "CO2(g)")
    assert _close(value, -394.0), f"the tabulated value recomputes to {value}"
    key_shows(item, signed(value), "tabulated value")
    # EK 6.6.A.1's reading of the sign, checked as a direction and not just as a
    # number: a value below zero reports heat energy released.
    assert h6.agrees(value, h.keyed(item), transfer=True), (
        f"the tabulated value is {h6.report(value)}, but the keyed choice reports "
        f"{h6.stated_transfer(h.keyed(item))!r}: {h.keyed(item)!r}"
    )
    mistake(item, signed(-value), "the sign of the tabulated value dropped")
    mistake(item, signed(hf(table, "H2O(l)")), "the row for water read instead")
    mistake(item, signed(hf(table, "CO(g)")), "the row for carbon monoxide read instead")
    mistake(item, signed(hf(table, "O2(g)")), "the row for oxygen read instead")
    return (f"the table prices that substance at {signed(value)}, which EK 6.6.A.1 reads as "
            "heat energy released, with the sign-dropped value and three neighbouring rows "
            "each recomputed into one distractor")


def q11(table, item):
    p = product_sum(table, E1)
    assert _close(p, -966.0), f"the product sum recomputes to {p}"
    key_shows(item, signed(p), "sum over the products")
    mistake(item, signed(reactant_sum(table, E1)), "the reactant sum computed instead")
    mistake(item, signed(hf(table, "CO2(g)") + hf(table, "H2O(l)")),
            "the coefficient on the water dropped")
    mistake(item, signed(delta_h(table, E1)), "the whole subtraction completed")
    mistake(item, signed(p + reactant_sum(table, E1)), "the two sums added")
    return (f"the products of {E1!r} are priced from the table and summed with their "
            f"coefficients to {signed(p)}, with four mistaken routes each in one distractor")


def q12(table, item):
    r = reactant_sum(table, E1)
    assert _close(r, -75.0), f"the reactant sum recomputes to {r}"
    key_shows(item, signed(r), "sum over the reactants")
    mistake(item, signed(product_sum(table, E1)), "the product sum computed instead")
    mistake(item, signed(2 * hf(table, "O2(g)")), "the oxygen counted and the methane dropped")
    mistake(item, signed(delta_h(table, E1)), "the whole subtraction completed")
    mistake(item, signed(r + product_sum(table, E1)), "the two sums added")
    return (f"the reactants of {E1!r} are priced from the table and summed with their "
            f"coefficients to {signed(r)}, the tabulated zero for oxygen contributing nothing")


def q13(table, item):
    p, r = product_sum(table, E1), reactant_sum(table, E1)
    return _enthalpy_item(table, item, 13, -891.0, [
        (891.0, "the subtraction taken the other way round"),
        (p + r, "the two sums added"),
        (p, "the product sum reported alone"),
        (r, "the reactant sum reported alone")])


def q14(table, item):
    water = hf(table, "H2O(l)")
    return _enthalpy_item(table, item, 14, -572.0, [
        (572.0, "the subtraction taken the other way round"),
        (water, "the coefficient on the water dropped"),
        (2 * -572.0, "the coefficient applied a second time"),
        (-water, "the coefficient dropped and the subtraction reversed")])


def q15(table, item):
    ammonia = hf(table, "NH3(g)")
    return _enthalpy_item(table, item, 15, -92.0, [
        (92.0, "the subtraction taken the other way round"),
        (ammonia, "the coefficient on the ammonia dropped"),
        (2 * -92.0, "the coefficient applied a second time"),
        (-ammonia, "the coefficient dropped and the subtraction reversed")])


def q16(table, item):
    p, r = product_sum(table, E4), reactant_sum(table, E4)
    return _enthalpy_item(table, item, 16, 178.0, [
        (-178.0, "the subtraction taken the other way round"),
        (p + r, "the two sums added"),
        (p, "the product sum reported alone"),
        (r, "the reactant sum reported alone")])


def q17(table, item):
    p, r = product_sum(table, E5), reactant_sum(table, E5)
    return _enthalpy_item(table, item, 17, -198.0, [
        (198.0, "the subtraction taken the other way round"),
        (p + r, "the two sums added"),
        (p, "the product sum reported alone"),
        (r, "the reactant sum reported alone")])


def q18(table, item):
    no = hf(table, "NO(g)")
    return _enthalpy_item(table, item, 18, 180.0, [
        (-180.0, "the subtraction taken the other way round"),
        (no, "the coefficient on the nitrogen monoxide dropped"),
        (2 * 180.0, "the coefficient applied a second time"),
        (-no, "the coefficient dropped and the subtraction reversed")])


def q19(table, item):
    p, r = product_sum(table, E7), reactant_sum(table, E7)
    return _enthalpy_item(table, item, 19, -566.0, [
        (566.0, "the subtraction taken the other way round"),
        (p + r, "the two sums added"),
        (p, "the product sum reported alone"),
        (r, "the reactant sum reported alone")])


def q20(table, item):
    ammonia = hf(table, "NH3(g)")
    return _enthalpy_item(table, item, 20, 92.0, [
        (-92.0, "the subtraction taken the other way round"),
        (ammonia, "the tabulated ammonia value reported as it stands"),
        (2 * 92.0, "the coefficient applied a second time"),
        (-ammonia, "the coefficient dropped from the reactant sum")])


def q21(table, item):
    return _enthalpy_item(table, item, 21, -394.0, [
        (394.0, "the subtraction taken the other way round"),
        (2 * -394.0, "the single product counted twice"),
        (hf(table, "CO(g)"), "the row for carbon monoxide read instead"),
        (reactant_sum(table, E9), "the reactant sum reported alone")])


def q22(table, item):
    p, r = product_sum(table, E10), reactant_sum(table, E10)
    return _enthalpy_item(table, item, 22, -114.0, [
        (114.0, "the subtraction taken the other way round"),
        (p + r, "the two sums added"),
        (p, "the product sum reported alone"),
        (r, "the reactant sum reported alone")])


def q23(table, item):
    oxide = hf(table, "Fe2O3(s)")
    return _enthalpy_item(table, item, 23, -1648.0, [
        (1648.0, "the subtraction taken the other way round"),
        (oxide, "the coefficient on the iron oxide dropped"),
        (2 * -1648.0, "the coefficient applied a second time"),
        (reactant_sum(table, E11), "the reactant sum reported alone")])


def q24(table, item):
    r = reactant_sum(table, E3)
    p = product_sum(table, E3)
    assert _close(r, 0.0), f"the reactant sum recomputes to {r}, not zero"
    assert not _close(p, 0.0), (
        "the product sum is zero as well, so the item's premise -- that only the reactants "
        "drop out -- is empty"
    )
    _, reactants = sides(E3)
    values = {name: hf(table, name) for _, name in reactants}
    assert all(v == 0 for v in values.values()), values
    h.shows(item, "Because the table gives a standard enthalpy of formation of zero for both "
                  "reactants")
    return (f"the table prices the reactants of {E3!r} at {values} kJ/mol, so their sum is "
            f"{r:g} while the product sum is {p:g}")


def q25(table, item):
    stated, original = REACTIONS[25]
    forward = delta_h(table, original)
    reverse = delta_h(table, stated)
    assert not _close(forward, 0.0), "a thermoneutral pair would make the comparison empty"
    assert _close(reverse, -forward), (
        f"the reverse reaction recomputes to {reverse}, which is not the negative of the "
        f"forward reaction's {forward}"
    )
    same_size = _close(abs(reverse), abs(forward))
    opposite_sign = h6.word(reverse) != h6.word(forward)
    assert same_size and opposite_sign, (h6.report(forward), h6.report(reverse))
    h.shows(item, "They are equal in magnitude and opposite in sign")
    return (f"the tabulated values give {h6.report(forward)} for the forward reaction and "
            f"{h6.report(reverse)} for its reverse, the same size with the direction word "
            "changed")


def q26(table, item):
    named = ["CO(g)", "CO2(g)", "CH4(g)"]
    values = {lab: hf(table, lab) for lab in named}
    lab = _unique_extreme(values, min)
    h.shows(item, lab)
    return (f"the three named substances are tabulated at {values} kJ/mol, whose unique "
            f"minimum is at {lab}")


def q29(table, item):
    value = hf(table, "O2(g)")
    assert _close(value, 0.0), f"the table prices that substance at {value}, not zero"
    contribution = 3 * value
    assert _close(contribution, 0.0), contribution
    h.shows(item, "Nothing at all, since zero multiplied by the coefficient is still zero")
    return (f"the table prices that substance at {value:g} kJ/mol, so three moles of it "
            f"contribute {contribution:g} to the sum over the reactants")


TABLE_CHECKS = {8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15,
                16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 29: q29}


# ------------------------------------------------------------- stem numerics

def n5(item):
    """The coefficient a check would use, read from the equation in the stem."""
    (equation,) = REACTIONS[5]
    products, _ = sides(equation)
    counts = {name: n for n, name in products}
    assert list(counts) == ["H2O(l)"], f"the products of {equation!r} are {counts}"
    n = counts["H2O(l)"]
    assert n == 2, f"that substance is produced in {n} mol, not two"
    h.shows(item, "Twice, once for each mole of it produced")
    return (f"the equation the stem states produces {n} mol of that substance, so its "
            "tabulated value enters the sum over the products that many times")


def n27(item):
    first = h6.formation_enthalpy([(1, -500.0)], [(1, -200.0)])
    second = h6.formation_enthalpy([(1, -200.0)], [(1, -500.0)])
    assert _close(first, -300.0) and _close(second, 300.0), (first, second)
    first_is_exothermic = h6.direction(first)["exothermic"]
    second_is_exothermic = h6.direction(second)["exothermic"]
    assert first_is_exothermic and not second_is_exothermic, (first, second)
    h.shows(item, "The first, since its standard enthalpy of reaction comes out negative")
    return (f"the stated sums give {h6.report(first)} for the first reaction and "
            f"{h6.report(second)} for the second, so only the first releases heat energy")


def n28(item):
    dh = h6.formation_enthalpy([(1, -500.0)], [(1, -500.0)])
    assert _close(dh, 0.0), f"equal sums recompute to {dh}, not zero"
    state = h6.direction(dh)
    assert state["neither"] and not state["exothermic"] and not state["endothermic"], state
    assert h6.word(dh) is None, (
        "a thermoneutral result must carry no direction word, or the key would have to name "
        "one"
    )
    h.shows(item, "Zero, since the two sums cancel in the framework's subtraction")
    return (f"two equal sums give {dh:g} kJ/mol through EK 6.8.A.1's subtraction, which is "
            "neither of EK 6.6.A.1's two cases")


NUMERIC = {5: n5, 27: n27, 28: n28}


CLAIMS = [
 ("The standard enthalpies of reactions",
  "EK 6.8.A.1's own sentence: tables of standard enthalpies of formation can be used to calculate the standard enthalpies of reactions."),
 ("The sum over the products minus the sum over the reactants",
  "EK 6.8.A.1's EQN, in words. Taking the larger sum minus the smaller would force a positive answer every time and destroy what the sign reports."),
 ("The two sums must be subtracted, one from the other, rather than added",
  "EK 6.8.A.1's equation is a difference, not a total; a sum of the two grows with both sides at once and reports no direction."),
 ("The magnitude is right and the sign is reversed",
  "EK 6.8.A.1 takes products minus reactants, so exchanging the terms negates the difference and leaves its size alone, which under EK 6.6.A.1 reports the opposite heat flow."),
 ("Twice, once for each mole of it produced",
  "EK 6.8.A.1's sum runs over the products of the reaction as written. n5 reads the coefficient from the equation stated in the stem."),
 ("Heat energy is released by the reaction at constant pressure",
  "EK 6.6.A.1: the enthalpy change gives the amount of heat energy released for negative values, at constant pressure."),
 ("Heat energy is absorbed by the reaction at constant pressure",
  "EK 6.6.A.1's other clause: absorbed for positive values. EK 6.6.A.2 supplies the word endothermic for that case."),
 ("CaCO3(s)",
  "EK 6.8.A.1 uses the tabulated values with their signs, so the most negative is the entry furthest below zero. q8 recomputes every row and checks the minimum is unique."),
 ("NO(g)",
  "EK 6.8.A.1 carries the tabulated signs into the sums, so which entries are above zero decides which reactions are endothermic. q9 checks exactly one of the five offered is."),
 ("-394 kJ/mol",
  "The table's own entry, read with its sign. q10 recomputes the sign-dropped value and three neighbouring rows as the distractors."),
 ("-966 kJ/mol",
  "EK 6.8.A.1's first term, summed over the products of the stated equation with their coefficients. q11 recomputes it and four mistaken routes."),
 ("-75 kJ/mol",
  "EK 6.8.A.1's second term over the same equation, the tabulated zero for oxygen contributing nothing. q12 recomputes it and four mistaken routes."),
 ("-891 kJ/mol, so the reaction is exothermic",
  "EK 6.8.A.1's subtraction on the equation in the stem, with EK 6.6.A.1 supplying the direction. q13 checks the key's word against the sign of the recomputed value."),
 ("-572 kJ/mol, so the reaction is exothermic",
  "The same subtraction for the formation of water from its elements, where the table makes the reactant sum zero. q14 recomputes it."),
 ("-92 kJ/mol, so the reaction is exothermic",
  "The same subtraction for the synthesis of ammonia. q15 recomputes it and checks the reversed value sits in a distractor."),
 ("+178 kJ/mol, so the reaction is endothermic",
  "The same subtraction where the single reactant is tabulated further below zero than the two products, so EK 6.6.A.1's absorbed case applies. q16 recomputes it."),
 ("-198 kJ/mol, so the reaction is exothermic",
  "The same subtraction with both sums negative, so the answer is the gap between them rather than either sum. q17 recomputes it."),
 ("+180 kJ/mol, so the reaction is endothermic",
  "The same subtraction where the only tabulated value in play is above zero. q18 recomputes it."),
 ("-566 kJ/mol, so the reaction is exothermic",
  "The same subtraction with both tabulated oxides doubled. q19 recomputes it and four mistaken routes."),
 ("+92 kJ/mol, so the reaction is endothermic",
  "The reverse of the ammonia synthesis, where the tabulated zeros are now on the product side, so the subtraction comes out positive. q20 recomputes it."),
 ("-394 kJ/mol, so the reaction is exothermic",
  "A reaction whose single product is the only substance with a non-zero tabulated value, so EK 6.8.A.1's answer is that entry itself. q21 recomputes it."),
 ("-114 kJ/mol, so the reaction is exothermic",
  "A subtraction that comes out negative although both tabulated nitrogen oxides are above zero, because the product sum lies below the reactant sum. q22 recomputes it."),
 ("-1648 kJ/mol, so the reaction is exothermic",
  "The same subtraction with the tabulated iron oxide doubled against a reactant sum the table makes zero. q23 recomputes it."),
 ("Because the table gives a standard enthalpy of formation of zero for both reactants",
  "EK 6.8.A.1 always subtracts the reactant sum; here that sum is zero because of what the table lists, not because of the reactants' role. q24 recomputes both sums."),
 ("They are equal in magnitude and opposite in sign",
  "Reversing the equation exchanges EK 6.8.A.1's two sums, which negates the difference and leaves its size untouched. q25 recomputes both reactions from the same table."),
 ("CO2(g)",
  "EK 6.8.A.1 reads the tabulated values with their signs, so ranking three of them is a reading of the table. q26 recomputes all three and checks the minimum is unique."),
 ("The first, since its standard enthalpy of reaction comes out negative",
  "EK 6.8.A.1's subtraction on two stated pairs of sums, with EK 6.6.A.1 making the negative one the reaction that releases heat energy. n27 recomputes both."),
 ("Zero, since the two sums cancel in the framework's subtraction",
  "EK 6.8.A.1's equation is a difference, so equal sums leave nothing, and EK 6.6.A.1's two cases are a negative and a positive value, neither of which this is. n28 recomputes it."),
 ("Nothing at all, since zero multiplied by the coefficient is still zero",
  "EK 6.8.A.1's sum multiplies each tabulated value by the moles of that substance in the equation, and this one is tabulated at zero. q29 recomputes the contribution."),
 ("products minus the sum over the reactants, with a negative result meaning heat energy is released",
  "EK 6.8.A.1 supplies the subtraction and its direction; EK 6.6.A.1 supplies what the sign reports. Each rejected option breaks one of those two links."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, what can the tables be used for?"
        no_figure_language(mod)

    def bond_energies_creep_in(mod, cl):
        mod.QUESTIONS[1]["q"] = "Which expression uses the average bond energies of a reaction?"
        no_other_topic(mod)

    def hess_creeps_in(mod, cl):
        mod.QUESTIONS[2]["q"] = "How is the enthalpy change found using Hess's law here?"
        no_other_topic(mod)

    def excluded_concept_in_a_distractor(mod, cl):
        # The CED says state functions will not be assessed. A distractor is
        # still student-facing, and a rationale is worse.
        ch = list(mod.QUESTIONS[3]["choices"])
        ch[4] = "The result is unchanged, since enthalpy is a state function"
        mod.QUESTIONS[3]["choices"] = ch
        no_excluded(mod)

    def equation_edited_out_of_a_stem(mod, cl):
        # The check would go on using the equation it holds while the student
        # reads a different one.
        mod.QUESTIONS[15]["q"] = (
            "What is the standard enthalpy of the decomposition of calcium carbonate, from "
            "the tabulated values?")
        equations_are_stated_and_balanced(mod)

    def equation_unbalanced(mod, cl):
        mod.QUESTIONS[13]["q"] = mod.QUESTIONS[13]["q"].replace(
            "2 H2(g) + O2(g) gives 2 H2O(l)", "2 H2(g) + O2(g) gives 3 H2O(l)")
        REACTIONS[14] = ["2 H2(g) + O2(g) gives 3 H2O(l)"]
        try:
            equations_are_stated_and_balanced(mod)
        finally:
            REACTIONS[14] = [E2]

    def a_species_loses_its_row(mod, cl):
        # The table edited so one substance an equation names is no longer
        # priced. A student would have to supply the value from memory, which is
        # the whole thing the printed zeros exist to prevent.
        saved = h6_8._T_FORM["rows"]
        h6_8._T_FORM = dict(headers=_T_HEADERS,
                            rows=[r for r in saved if r[0] != "Fe(s)"])
        try:
            species_are_tabulated(mod)
        finally:
            h6_8._T_FORM = dict(headers=_T_HEADERS, rows=saved)

    def enthalpy_key_loses_its_direction(mod, cl):
        ch = list(mod.QUESTIONS[12]["choices"])
        ch[0] = "-891 kJ/mol"
        mod.QUESTIONS[12]["choices"] = ch
        cl[12] = ("-891 kJ/mol", cl[12][1])
        enthalpy_keys_state_a_direction(mod)

    def anchor_loses_its_direction(mod, cl):
        cl[15] = ("+178 kJ/mol", cl[15][1])
        anchors_carry_the_direction(mod, cl)

    def sum_anchor_loses_its_sign(mod, cl):
        cl[10] = ("966 kJ/mol", cl[10][1])
        signed_anchors(mod, cl)

    def enthalpy_key_direction_reversed(mod, cl):
        # The key moved to the reversed value. Every choice is untouched, so
        # they stay distinct and the new anchor matches only the new key; only
        # the comparison against the SIGN of the recomputed value can reject it.
        mod.QUESTIONS[14]["ans"] = 1
        cl[14] = ("+92 kJ/mol, so the reaction is endothermic", cl[14][1])

    def endothermic_key_direction_reversed(mod, cl):
        mod.QUESTIONS[15]["ans"] = 1
        cl[15] = ("-178 kJ/mol, so the reaction is exothermic", cl[15][1])

    def tabulated_value_changed(mod, cl):
        # One row edited under a keyed enthalpy, so the key no longer follows
        # from the table the student is given.
        mod.QUESTIONS[12]["table"] = dict(
            headers=_T_HEADERS,
            rows=[[lab, ("-300" if lab == "CO2(g)" else v)]
                  for lab, v in h6_8._T_FORM["rows"]])

    def tabulated_sign_flipped(mod, cl):
        # A tabulated value's SIGN flipped, with its magnitude untouched. Both
        # the recomputed enthalpy and its direction move.
        mod.QUESTIONS[17]["table"] = dict(
            headers=_T_HEADERS,
            rows=[[lab, ("-90" if lab == "NO(g)" else v)]
                  for lab, v in h6_8._T_FORM["rows"]])

    def direction_word_alone_reversed(mod, cl):
        # The NUMBER in the keyed choice is left exactly right and only its
        # direction word is flipped. Every earlier guard passes -- the anchor
        # still matches, the value still recomputes, the choices are still
        # distinct -- so only the comparison of the key's word against the SIGN
        # of the recomputed value can reject it. Without this control that
        # comparison would never be exercised, because in every other mutation
        # the value check fires first.
        # The wording after the number differs from the reversed distractor's
        # ("and the reaction" against "so the reaction"). A first version wrote
        # them identically and the containment check fired instead, so the
        # control passed while proving nothing about the guard it names.
        ch = list(mod.QUESTIONS[12]["choices"])
        ch[0] = "-891 kJ/mol, and the reaction is endothermic"
        mod.QUESTIONS[12]["choices"] = ch
        cl[12] = ("-891 kJ/mol, and the reaction is endothermic", cl[12][1])

    def tabulated_sign_reading_reversed(mod, cl):
        # The same isolation for the tabulated-value item: the number stays
        # right and only EK 6.6.A.1's reading of its sign is flipped.
        ch = list(mod.QUESTIONS[9]["choices"])
        ch[0] = "-394 kJ/mol, and the negative sign reports heat energy absorbed"
        mod.QUESTIONS[9]["choices"] = ch
        cl[9] = ("-394 kJ/mol, and the negative sign reports heat energy absorbed", cl[9][1])

    def reversed_distractor_removed(mod, cl):
        # The distractor carrying the reversed value replaced. The key is still
        # right and every choice still distinct -- the item has simply stopped
        # testing the one error it exists to test.
        ch = list(mod.QUESTIONS[16]["choices"])
        ch[1] = "+500 kJ/mol, so the reaction is endothermic"
        mod.QUESTIONS[16]["choices"] = ch

    def most_negative_row_moved(mod, cl):
        mod.QUESTIONS[7]["table"] = dict(
            headers=_T_HEADERS,
            rows=[[lab, ("-2000" if lab == "Fe2O3(s)" else v)]
                  for lab, v in h6_8._T_FORM["rows"]])

    def a_second_offered_row_made_positive(mod, cl):
        mod.QUESTIONS[8]["table"] = dict(
            headers=_T_HEADERS,
            rows=[[lab, ("+50" if lab == "CO(g)" else v)]
                  for lab, v in h6_8._T_FORM["rows"]])

    def the_positive_rows_all_removed(mod, cl):
        # Only one entry left above zero, so the item stops testing the sign of
        # the tabulated values and becomes a single exception.
        mod.QUESTIONS[8]["table"] = dict(
            headers=_T_HEADERS,
            rows=[[lab, ("-33" if lab == "NO2(g)" else v)]
                  for lab, v in h6_8._T_FORM["rows"]])

    def reverse_pair_broken(mod, cl):
        # The ammonia row changed so the forward and reverse reactions no longer
        # negate one another... which they still would. So instead the check is
        # attacked where it can fail: the item is re-pointed at two reactions
        # that are not a reversed pair.
        REACTIONS[25] = [E8, E5]
        mod.QUESTIONS[24]["q"] = mod.QUESTIONS[24]["q"].replace(
            "N2(g) + 3 H2(g) gives 2 NH3(g)", "2 SO2(g) + O2(g) gives 2 SO3(g)")
        try:
            equations_are_stated_and_balanced(mod)
            cg.check(mod, cl, table_checks=TABLE_CHECKS)
        finally:
            REACTIONS[25] = [E8, E3]

    def zero_row_given_a_value(mod, cl):
        mod.QUESTIONS[28]["table"] = dict(
            headers=_T_HEADERS,
            rows=[[lab, ("-20" if lab == "O2(g)" else v)]
                  for lab, v in h6_8._T_FORM["rows"]])

    def reactant_zero_broken(mod, cl):
        mod.QUESTIONS[23]["table"] = dict(
            headers=_T_HEADERS,
            rows=[[lab, ("-10" if lab == "H2(g)" else v)]
                  for lab, v in h6_8._T_FORM["rows"]])

    def coefficient_item_key_moved(mod, cl):
        mod.QUESTIONS[4]["ans"] = 1
        cl[4] = ("Once, no matter how many moles are produced", cl[4][1])

    def stated_sums_swapped(mod, cl):
        ch = list(mod.QUESTIONS[26]["choices"])
        ch[0], ch[1] = ch[1], ch[0]
        mod.QUESTIONS[26]["choices"] = ch
        cl[26] = ("The second, since its standard enthalpy of reaction comes out negative",
                  cl[26][1])

    return [
        ("a stem referring to a diagram the bank cannot show", figure_language),
        ("a stem borrowing 6.7's average bond energies", bond_energies_creep_in),
        ("a stem borrowing 6.9's Hess's law", hess_creeps_in),
        ("the CED's excluded state-function concept used as a distractor",
         excluded_concept_in_a_distractor),
        ("the equation removed from a stem while the check keeps using it",
         equation_edited_out_of_a_stem),
        ("an equation in a stem that does not conserve atoms", equation_unbalanced),
        ("a substance named in an equation left with no row in the table",
         a_species_loses_its_row),
        ("a key reporting an enthalpy of reaction with no direction",
         enthalpy_key_loses_its_direction),
        ("an anchor cut back to a bare value while the key keeps its direction",
         anchor_loses_its_direction),
        ("a partial-sum anchor stripped of its sign", sum_anchor_loses_its_sign),
        ("an exothermic key moved to the reversed value", enthalpy_key_direction_reversed),
        ("an endothermic key moved to the reversed value",
         endothermic_key_direction_reversed),
        ("a tabulated value changed under a keyed enthalpy", tabulated_value_changed),
        ("a tabulated value's sign flipped with its magnitude untouched",
         tabulated_sign_flipped),
        ("a keyed direction word flipped with its number left right",
         direction_word_alone_reversed),
        ("a tabulated value's sign read as absorbed instead of released",
         tabulated_sign_reading_reversed),
        ("the reversed-subtraction distractor replaced, so the item stops testing it",
         reversed_distractor_removed),
        ("the most negative tabulated value moved off the keyed row", most_negative_row_moved),
        ("a second offered substance made positive, so two choices are defensible",
         a_second_offered_row_made_positive),
        ("the table left with only one entry above zero", the_positive_rows_all_removed),
        ("the reversed-pair item re-pointed at two reactions that are not a reversed pair",
         reverse_pair_broken),
        ("the tabulated zero given a value under the item that rests on it",
         zero_row_given_a_value),
        ("a reactant's tabulated zero given a value", reactant_zero_broken),
        ("the coefficient item keyed to a single count", coefficient_item_key_moved),
        ("the two stated pairs of sums exchanged in the choices", stated_sums_swapped),
    ]


_T_HEADERS = h6_8._T_FORM["headers"]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h6.selftest()
    eq.selftest()
    h.selftest(h6_8, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h6_8)
no_other_topic(h6_8)
no_excluded(h6_8)
equations_are_stated_and_balanced(h6_8)
species_are_tabulated(h6_8)
enthalpy_keys_state_a_direction(h6_8)
anchors_carry_the_direction(h6_8, CLAIMS)
signed_anchors(h6_8, CLAIMS)
h.run(h6_8, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
