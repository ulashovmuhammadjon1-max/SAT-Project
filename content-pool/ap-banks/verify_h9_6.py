"""Key audit for AP CHEMISTRY 9.6 Free Energy of Dissolution.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  9.6.A.1  the three factors, the estimable sign and relative magnitude of each
           contribution, and the cancellation that makes the total hard to
           predict
                   1, 6, 7, 8, 9, 10, 11, 12, 13, 23, 24, 25, 27, 28, 29, 30
  6.7.A.2  energy is REQUIRED to break bonds and RELEASED when they form
                   2, 3, 12
  4.4.A.2  a salt dissolving breaks ionic bonds and forms ion-dipole
           interactions between ions and solvent          3, 23, 24
  9.1.A.1  entropy rises when matter becomes more dispersed    4, 5
  9.3.A.4  the dissolution of sodium nitrate needs both quantities weighed
                   19, 26
  9.3.A.5 and 9.3.A.6  the arithmetic and the sign table, wherever an enthalpy
           and an entropy change are combined  14, 15, 16, 17, 18, 19, 22, 26

THE POINT OF THE TOPIC IS THE CANCELLATION, so the verifier checks it as a
measured fact rather than as an assertion: ``q11`` and ``q29`` require the
tabulated total to be smaller than the largest single contribution by a factor
of at least a hundred, and a control flattens the table to contributions that do
NOT cancel and confirms the check fires.

SIGN CONVENTION. Every free energy value keyed here also states whether the
dissolution is favored, and ``sign_matches_favorability`` requires the two to
agree -- EK 9.3.A.2 pairs a negative value with a favored process, and writing
that backwards is the defect this unit is likeliest to ship.

SCOPE. 7.11 and 7.12 own the solubility product and the common-ion effect.
``no_solubility_product`` asserts that no item computes one.

NEGATIVE CONTROL: ``python3 verify_h9_6.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h9_check as h9

import h9_6

HCOL = "Contribution to the enthalpy change, kJ/mol"
GCOL = "Contribution to the free energy change, kJ/mol"
SHCOL = "Enthalpy change of dissolution, kJ/mol"
SSCOL = "Entropy change of dissolution, J/(mol K)"

# Explicit lookarounds, never \b.
_OUT_OF_SCOPE = re.compile(
    r"(?<![A-Za-z])(solubility product|ksp|common-ion|cell potential|electrode|"
    r"kinetic control|equilibrium constant|nernst|catalys[et])(?![A-Za-z])", re.I)

_VALUE_KJ = re.compile(r"\\\(\s*([+-]\d+(?:\.\d+)?)\s*\\\)\s*kJ/mol")
_SALT = re.compile(r"(?<![A-Za-z])salt ([A-D])(?![A-Za-z])", re.I)
_AT_T = re.compile(r"(?<![A-Za-z0-9])at (\d+) K(?![A-Za-z])")

# Keys stating both a signed kJ/mol value and a favorability verdict.
FAVORABILITY_ITEMS = (9, 14, 15)


def no_solubility_product(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _OUT_OF_SCOPE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: mentions {hit.group(0)!r}, which belongs to 7.11, "
                f"7.12 or another Unit 9 topic -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item computes a solubility product or reaches "
          "into the cells.")


def sign_matches_favorability(module):
    """EK 9.3.A.2: below zero is favored, above zero is unfavored.

    The sign is read from the number and the verdict from the words, as two
    separately named facts, so a key with the right value and the wrong verdict
    is caught. Named booleans rather than parallel tuples compared by index.
    """
    for i in FAVORABILITY_ITEMS:
        item = module.QUESTIONS[i - 1]
        key = h.keyed(item)
        m = _VALUE_KJ.search(key)
        assert m, f"{module.TOPIC[0]} q{i}: the key states no signed kJ/mol value: {key!r}"
        value_is_negative = float(m.group(1)) < 0
        verdict = h9.favorability_verdict(key)
        assert verdict is not None, (
            f"{module.TOPIC[0]} q{i}: the key states no single favorability verdict: {key!r}"
        )
        key_says_favored = verdict
        assert value_is_negative == key_says_favored, (
            f"{module.TOPIC[0]} q{i}: the key pairs {m.group(1)} kJ/mol with "
            f"{'favored' if key_says_favored else 'unfavored'}, which is EK 9.3.A.2 "
            f"backwards -- {key!r}"
        )
        h9.opposite_sign_offered(item, m.group(1))
    print(f"OK  {module.TOPIC[0]} swap guard: {len(FAVORABILITY_ITEMS)} keys pair a "
          "negative free energy change with a favored dissolution, each against a "
          "sign-flipped distractor.")


# --------------------------------------------------------- the factor table

def _column(table, header):
    return dict(zip(cg.labels(table), cg.col(table, header)))


def q9(table, item):
    parts = _column(table, GCOL)
    total = sum(parts.values())
    token = f"{total:+.1f}"
    h9.shows_signed(item, token)
    flipped = h9.opposite_sign_offered(item, token)
    return (f"the tabulated free energy contributions {parts} sum to {token} kJ/mol, "
            f"against {flipped} offered as the sign-flipped distractor")


def q10(table, item):
    parts = _column(table, GCOL)
    positive = [lab for lab, v in parts.items() if v > 0]
    assert len(positive) == 1, f"the tabulated positive contributions are {positive}"
    assert positive[0].lower().startswith("breaking"), (
        f"the only positive tabulated contribution is {positive[0]!r}, not the "
        f"lattice-breaking factor the key names"
    )
    h.shows(item, "Breaking the interactions that hold the solid together")
    return (f"exactly one tabulated free energy contribution is above zero: "
            f"{positive[0]!r}")


def _cancellation(table):
    """How far the total falls short of the largest single contribution."""
    parts = _column(table, GCOL)
    total = sum(parts.values())
    largest = max(abs(v) for v in parts.values())
    assert abs(total) > 0, "a total of exactly zero would make the ratio meaningless"
    return total, largest, largest / abs(total)


def q11(table, item):
    total, largest, ratio = _cancellation(table)
    assert ratio > 100, (
        f"the tabulated contributions do not cancel: the largest is {largest:g} kJ/mol "
        f"against a total of {total:+g}, a ratio of only {ratio:.1f}, so the item's claim "
        f"that they largely cancel is not what the table shows"
    )
    h.shows(item, "total is far smaller than the separate contributions")
    return (f"the largest tabulated contribution, {largest:g} kJ/mol, is {ratio:.0f} times "
            f"the size of the total, {total:+g} kJ/mol")


def q12(table, item):
    parts = _column(table, HCOL)
    total = sum(parts.values())
    token = f"{total:+.1f}"
    h9.shows_signed(item, token)
    h9.opposite_sign_offered(item, token)
    assert total < 0, f"the tabulated enthalpy contributions sum to {total:+g}, not below zero"
    return (f"the tabulated enthalpy contributions {parts} sum to {token} kJ/mol, a release "
            f"of energy under EK 6.6.A.1")


def q13(table, item):
    total, largest, ratio = _cancellation(table)
    assert total < 0, f"the tabulated contributions sum to {total:+g}, not below zero"
    assert abs(total) < 10.0, (
        f"the total {total:+g} kJ/mol is not the few kilojoules the key describes"
    )
    assert largest > 100.0, (
        f"the largest tabulated contribution, {largest:g} kJ/mol, is not the hundreds the "
        f"key contrasts it with"
    )
    h.shows(item, "only by a few kilojoules per mole out of contributions of hundreds")
    return (f"the tabulated contributions sum to {total:+g} kJ/mol, favored, beside a "
            f"largest single contribution of {largest:g}")


def q29(table, item):
    total, largest, ratio = _cancellation(table)
    assert ratio > 100, (
        f"the total is only {ratio:.1f} times smaller than the largest contribution, not "
        f"the factor of hundreds the key claims"
    )
    h.shows(item, "smaller by a factor of hundreds")
    return (f"the largest tabulated contribution is {ratio:.0f} times the size of the "
            f"total, which is a factor of hundreds")


# ----------------------------------------------------------- the salt table

def _salt_gibbs(table, label, t_kelvin):
    return h9.gibbs(cg.cell(table, label, SHCOL), cg.cell(table, label, SSCOL), t_kelvin)


def _named_salt(stem):
    m = _SALT.search(stem)
    assert m, f"the stem names no salt: {stem[:70]!r}"
    return f"Salt {m.group(1).upper()}"


def _stated_temperature(stem):
    m = _AT_T.search(stem)
    assert m, f"the stem states no temperature: {stem[:70]!r}"
    return float(m.group(1))


def salt_gibbs_item(table, item):
    label = _named_salt(item["q"])
    t = _stated_temperature(item["q"])
    value = _salt_gibbs(table, label, t)
    token = f"{value:+.1f}"
    h9.shows_signed(item, token)
    flipped = h9.opposite_sign_offered(item, token)
    return (f"the tabulated changes for {label} at {t:g} K recompute the free energy change "
            f"as {token} kJ/mol, against {flipped} offered as the sign-flipped distractor")


def _signs(table, label):
    return (cg.cell(table, label, SHCOL), cg.cell(table, label, SSCOL))


def q16(table, item):
    always = [lab for lab in cg.labels(table)
              if _signs(table, lab)[0] < 0 and _signs(table, lab)[1] > 0]
    assert always == ["Salt D"], (
        f"the tabulated salts favored at every temperature are {always}"
    )
    h.shows(item, "Salt D")
    return (f"exactly one tabulated salt pairs a negative enthalpy change with a positive "
            f"entropy change, which is EK 9.3.A.6's all-temperature row: {always[0]}")


def q17(table, item):
    never = [lab for lab in cg.labels(table)
             if _signs(table, lab)[0] > 0 and _signs(table, lab)[1] < 0]
    assert never == ["Salt C"], (
        f"the tabulated salts favored at no temperature are {never}"
    )
    h.shows(item, "Salt C")
    return (f"exactly one tabulated salt pairs a positive enthalpy change with a negative "
            f"entropy change, which is EK 9.3.A.6's no-temperature row: {never[0]}")


def q18(table, item):
    t = _stated_temperature(item["q"])
    favored = sorted(lab for lab in cg.labels(table) if _salt_gibbs(table, lab, t) < 0)
    assert favored == ["Salt A", "Salt D"], (
        f"the tabulated salts favored at {t:g} K are {favored}"
    )
    endothermic = [lab for lab in favored if cg.cell(table, lab, SHCOL) > 0]
    assert endothermic, (
        "one of the favored salts must be endothermic, or the item does not show that an "
        "endothermic dissolution can still be favored"
    )
    h.shows(item, "Salts A and D")
    return (f"recomputing each tabulated salt at {t:g} K leaves {favored} below zero, one "
            f"of them ({endothermic[0]}) endothermic")


def q19(table, item):
    label = _named_salt(item["q"])
    t = _stated_temperature(item["q"])
    dh, ds = _signs(table, label)
    assert dh > 0, f"{label} must be endothermic for the item's premise: {dh:+g} kJ/mol"
    assert ds > 0, f"{label} must have a positive entropy change: {ds:+g} J/(mol K)"
    assert t * ds / 1000.0 > dh, (
        f"the entropy term {t * ds / 1000.0:g} kJ/mol must exceed the enthalpy change "
        f"{dh:g} kJ/mol, or nothing outweighs anything"
    )
    assert _salt_gibbs(table, label, t) < 0, "the dissolution must come out favored"
    h.shows(item, "positive entropy change, multiplied by the temperature, outweighs")
    return (f"for {label} at {t:g} K the entropy term is {t * ds / 1000.0:g} kJ/mol against "
            f"an enthalpy change of {dh:+g}, so the difference falls below zero")


TABLE_CHECKS = {9: q9, 10: q10, 11: q11, 12: q12, 13: q13,
                14: salt_gibbs_item, 15: salt_gibbs_item, 16: q16, 17: q17,
                18: q18, 19: q19, 29: q29}

NUMERIC = {}


CLAIMS = [
 ("Breaking the interactions holding the solid together, reorganizing the solvent",
  "EK 9.6.A.1 names exactly three factors: breaking the interactions that hold the solid together, reorganizing the solvent around the dissolved species, and the interaction of the dissolved species with the solvent."),
 ("Positive, because energy is required to break the interactions",
  "EK 6.7.A.2 makes the energy required to break interactions an amount that must be supplied, so this factor is endothermic; EK 9.6.A.1 licenses the estimate. Dispersal is entropic, not enthalpic."),
 ("Negative, because energy is released as the new attractions form",
  "EK 6.7.A.2 makes the forming of attractions a release of energy, and EK 4.4.A.2 names the ion-dipole interactions between ions and solvent formed when a salt dissolves."),
 ("Positive, because the matter present becomes more dispersed",
  "EK 9.1.A.1 makes entropy increase when matter becomes more dispersed, and particles locked into a lattice become free to move through the solution."),
 ("Negative, because solvent molecules become held in place around the species",
  "EK 9.1.A.1's criterion applied the other way: solvent molecules arranged around a dissolved species are less free to move, so this factor lowers the entropy."),
 ("sign and relative magnitude of the enthalpic and entropic contributions to each factor",
  "EK 9.6.A.1 says exactly this is possible, and in the next sentence says the total is the challenging part."),
 ("Predicting the total change, because of cancellations among the three factors",
  "EK 9.6.A.1: making predictions for the total change in free energy of dissolution can be challenging due to the cancellations among the free energies associated with the three factors cited."),
 ("total is a small difference between large contributions of opposite sign",
  "EK 9.6.A.1 attributes the difficulty to cancellation, which means the contributions oppose one another and the sum is much smaller than any of them."),
 ("-2.0 kJ/mol, so the dissolution is thermodynamically favored",
  "EK 9.6.A.1 combines the three factors and EK 9.3.A.2 reads the total. q9 sums the tabulated free energy column with its signs and requires the result, sign and all, to be the keyed choice."),
 ("Breaking the interactions that hold the solid together",
  "EK 9.6.A.1 invites comparison of relative magnitudes, and EK 6.7.A.2 makes the lattice-breaking factor the endothermic one. q10 recomputes which tabulated contribution is above zero."),
 ("total is far smaller than the separate contributions",
  "EK 9.6.A.1's cancellation, measured rather than asserted: q11 requires the largest tabulated contribution to exceed the total by a factor of at least a hundred."),
 ("-5.0 kJ/mol, so the dissolution releases a little energy overall",
  "EK 9.6.A.1 treats the enthalpic contributions as separate amounts to be combined and EK 6.6.A.1 reads a negative enthalpy change as a release of energy. q12 sums the tabulated enthalpy column."),
 ("only by a few kilojoules per mole out of contributions of hundreds",
  "EK 9.3.A.2 reads the small negative total as favored and EK 9.6.A.1 explains why the margin is tiny. q13 recomputes the total and the largest contribution and checks both descriptions."),
 ("-5.0 kJ/mol, so the dissolution is thermodynamically favored",
  "EK 9.3.A.5's equation applied to the tabulated changes for one salt at the stated temperature, with the entropy change converted to kilojoules. Recomputed in salt_gibbs_item."),
 ("+5.0 kJ/mol, so the dissolution is thermodynamically unfavored",
  "EK 9.3.A.5 with a negative entropy term that adds to the enthalpy change, so an exothermic dissolution comes out unfavored. Recomputed in salt_gibbs_item."),
 ("Salt D",
  "EK 9.3.A.6's table puts a negative enthalpy change with a positive entropy change in the all-temperature row. q16 recomputes which tabulated salt has that pair of signs."),
 ("Salt C",
  "EK 9.3.A.6's table puts a positive enthalpy change with a negative entropy change in the no-temperature row. q17 recomputes which tabulated salt has that pair."),
 ("Salts A and D",
  "EK 9.3.A.5 applied to every tabulated salt at the stated temperature, with EK 9.3.A.2 reading the results. q18 recomputes all four and checks one of the favored pair is endothermic."),
 ("positive entropy change, multiplied by the temperature, outweighs",
  "EK 9.3.A.5 lets the temperature times a positive entropy change exceed a positive enthalpy change; EK 9.3.A.4 names salt dissolution as such a case. q19 recomputes both terms and compares them."),
 ("The dissolution of sodium nitrate",
  "EK 9.3.A.4 names the freezing of water and the dissolution of sodium nitrate as its examples of processes needing both quantities weighed."),
 ("solubility of a salt and the enthalpy and entropy changes of dissolution",
  "Learning objective 9.6.A asks for exactly this relationship, which is why EK 9.6.A.1 separates the enthalpic and entropic contribution of each factor."),
 ("temperature multiplies the entropy change, so the free energy change falls",
  "EK 9.3.A.5 multiplies the entropy change by the temperature before subtracting it, which EK 9.3.A.6 records as the favored-at-high-temperature case for two positive changes."),
 ("The interaction of the dissolved species with the solvent",
  "EK 4.4.A.2 names the formation of ion-dipole interactions between ions and solvent, which is EK 9.6.A.1's third factor."),
 ("The breaking of the interactions that hold the solid together",
  "EK 9.6.A.1's first factor, which EK 4.4.A.2 identifies for a salt as the breaking of its ionic bonds."),
 ("other two factors are of comparable size and largely cancel the first",
  "EK 9.6.A.1 lists three factors and attributes the difficulty of predicting the total to cancellations among all three, so keeping one discards most of what decides the answer."),
 ("sufficiently positive entropy change can outweigh a positive enthalpy change",
  "EK 9.3.A.4 names the dissolution of sodium nitrate as a case where both must be weighed, and EK 9.3.A.5's equation is what lets the entropy term win."),
 ("contributions oppose one another and their relative sizes decide the outcome",
  "EK 9.6.A.1 says the separate signs and relative magnitudes can be estimated but that the total is challenging because of cancellations, so the signs alone do not settle it."),
 ("An estimate of the sign and the relative magnitude",
  "EK 9.6.A.1 says it is possible to estimate the sign and relative magnitude of the enthalpic and entropic contributions to each factor -- less than an exact value, more than a sign."),
 ("smaller by a factor of hundreds",
  "EK 9.6.A.1's cancellation, measured in q29 as the ratio of the largest tabulated contribution to the total."),
 ("total made of large opposing contributions can be small and hard to predict",
  "EK 9.6.A.1 makes exactly this point about dissolution, which is why it says the separate contributions can be estimated while the total cannot easily be."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, which three factors are shown?"
        h9.no_figure_language(mod)

    def solubility_product_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = mod.QUESTIONS[0]["why"] + " The Ksp follows from it."
        no_solubility_product(mod)

    def verdict_flipped_on_a_key(mod, cl):
        ch = list(mod.QUESTIONS[13]["choices"])
        ch[0] = "\\( -5.0 \\) kJ/mol, so the dissolution is thermodynamically unfavored"
        mod.QUESTIONS[13]["choices"] = ch
        # The anchor carries the SAME sign as the corrupted choice, so this
        # control still exercises sign_matches_favorability -- the guard it
        # names -- rather than tripping the containment test first. Since
        # cg.normalize began keeping '+', an unsigned anchor no longer matches
        # a signed choice at all, so leaving it unsigned would make the control
        # pass for a reason that has nothing to do with favorability.
        cl[13] = ("-5.0 \\) kJ/mol, so the dissolution is thermodynamically unfavored",
                  cl[13][1])
        sign_matches_favorability(mod)

    def contributions_no_longer_cancel(mod, cl):
        # Three contributions of the SAME sign: the total is then the largest
        # quantity in the table, not a small residue, and the items that claim
        # cancellation must refuse it.
        mod.QUESTIONS[10]["table"] = dict(
            headers=h9_6._T_FACTORS["headers"],
            rows=[["Breaking the interactions that hold the solid together", "+780.0", "+765.0"],
                  ["Reorganizing the solvent around the dissolved species", "-30.0", "+16.0"],
                  ["Interaction of the dissolved species with the solvent", "-755.0", "+751.0"]])

    def total_contribution_corrupted(mod, cl):
        mod.QUESTIONS[8]["table"] = dict(
            headers=h9_6._T_FACTORS["headers"],
            rows=[["Breaking the interactions that hold the solid together", "+780.0", "+765.0"],
                  ["Reorganizing the solvent around the dissolved species", "-30.0", "-16.0"],
                  ["Interaction of the dissolved species with the solvent", "-755.0", "-741.0"]])

    def positive_contribution_moved(mod, cl):
        mod.QUESTIONS[9]["table"] = dict(
            headers=h9_6._T_FACTORS["headers"],
            rows=[["Breaking the interactions that hold the solid together", "+780.0", "-765.0"],
                  ["Reorganizing the solvent around the dissolved species", "-30.0", "+16.0"],
                  ["Interaction of the dissolved species with the solvent", "-755.0", "-751.0"]])

    def salt_entropy_corrupted(mod, cl):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h9_6._T_SALTS["headers"],
            rows=[["Salt A", "+25.0", "+40.0"], ["Salt B", "-10.0", "-50.0"],
                  ["Salt C", "+30.0", "-20.0"], ["Salt D", "-20.0", "+40.0"]])

    def temperature_changed_in_a_stem(mod, cl):
        mod.QUESTIONS[13]["q"] = mod.QUESTIONS[13]["q"].replace("at 300 K", "at 500 K")

    def all_temperature_row_duplicated(mod, cl):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h9_6._T_SALTS["headers"],
            rows=[["Salt A", "-25.0", "+100.0"], ["Salt B", "-10.0", "-50.0"],
                  ["Salt C", "+30.0", "-20.0"], ["Salt D", "-20.0", "+40.0"]])

    def favored_set_changed(mod, cl):
        mod.QUESTIONS[17]["table"] = dict(
            headers=h9_6._T_SALTS["headers"],
            rows=[["Salt A", "+45.0", "+100.0"], ["Salt B", "-10.0", "-50.0"],
                  ["Salt C", "+30.0", "-20.0"], ["Salt D", "-20.0", "+40.0"]])

    def endothermic_driver_removed(mod, cl):
        # Salt A made exothermic, so nothing is being outweighed and the item's
        # premise -- an endothermic dissolution that is favored anyway -- fails.
        mod.QUESTIONS[18]["table"] = dict(
            headers=h9_6._T_SALTS["headers"],
            rows=[["Salt A", "-25.0", "+100.0"], ["Salt B", "-10.0", "-50.0"],
                  ["Salt C", "+30.0", "-20.0"], ["Salt D", "-20.0", "+40.0"]])

    return [
        ("a stem pointing at a figure the bank cannot show", figure_language),
        ("a why reaching into the solubility product, which is 7.11's material",
         solubility_product_creeps_in),
        ("a negative free energy change keyed as an unfavored dissolution",
         verdict_flipped_on_a_key),
        ("tabulated contributions that no longer cancel, behind a key that says they do",
         contributions_no_longer_cancel),
        ("a tabulated contribution corrupted so the keyed total is wrong",
         total_contribution_corrupted),
        ("the only positive tabulated contribution moved to another factor",
         positive_contribution_moved),
        ("a tabulated entropy change corrupted so the keyed value is wrong",
         salt_entropy_corrupted),
        ("the temperature changed in a stem while the key stands",
         temperature_changed_in_a_stem),
        ("a second tabulated salt put in the all-temperature row",
         all_temperature_row_duplicated),
        ("a tabulated salt moved out of the favored set at the stated temperature",
         favored_set_changed),
        ("the endothermic salt made exothermic, so nothing outweighs anything",
         endothermic_driver_removed),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h9_6, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h9.no_figure_language(h9_6)
no_solubility_product(h9_6)
sign_matches_favorability(h9_6)
h.run(h9_6, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
