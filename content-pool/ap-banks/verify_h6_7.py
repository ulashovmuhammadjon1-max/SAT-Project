"""Key audit for AP CHEMISTRY 6.7 Bond Enthalpies.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  6.7.A.1  bonds are broken AND/OR formed, and these events change the potential
           energy of the system                       1, 28
  6.7.A.2  the reactant sum is the energy REQUIRED, the product sum the energy
           RELEASED, both ESTIMATED from AVERAGE bond energies; released greater
           than required is exothermic, required greater than released is
           endothermic
                    2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                    19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30
  LO 6.7.A  the enthalpy change is the requirement minus the release
                    6, 14, 15, 16, 17, 18, 21, 23, 26, 29

THE BOND COUNTS ARE DERIVED, NOT ASSERTED. Each reaction is written out in its
own stem. ``bond_inventory`` parses that equation with ``h_equation``, looks up
the bonds in each species in ``SPECIES_BONDS``, and multiplies by the
coefficients -- so the numbers the check uses come from the question a student
reads. ``species_bonds_are_consistent`` then validates ``SPECIES_BONDS`` itself
against the molecular formulas parsed from the same equations: every one of
these molecules is acyclic, so it must carry exactly one fewer bond than it has
atoms. A miscounted species is caught by that arithmetic rather than by
somebody re-reading the table.

Every equation is atom- and charge-balanced by ``h_equation`` as well, and every
bond energy is read FROM THE MODULE'S OWN TABLE, never from a constant in this
file -- an edited table and a stale check cannot pass together.

THE SUBTRACTION RUNS ONE WAY. Requirement minus release. Reversing it gives the
same magnitude and the wrong sign, which is this topic's characteristic defect,
so ``enthalpy_keys_state_a_direction`` requires every keyed enthalpy to name
exothermic or endothermic as well as its number, ``anchors_carry_the_direction``
requires the anchor to carry it too, and each table check compares the key's
direction word against the SIGN of the recomputed value through
``h6_thermo.agrees`` -- named booleans, never two tuples read in parallel.

THE REVERSED VALUE IS ALWAYS A DISTRACTOR, and ``mistake`` locates it in the
choice list, so an item cannot quietly stop testing the one error it exists to
test.

SCOPE. 6.8 owns the standard enthalpies of formation and 6.9 owns Hess's law; no
item here reaches an enthalpy by either route. 6.6 owns the molar enthalpy of
reaction and the amount in moles, and nothing here multiplies by an amount.

NEGATIVE CONTROL: ``python3 verify_h6_7.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h_equation as eq
import h6_thermo as h6

import h6_7

ENERGY = "Average bond energy (kJ/mol)"

# The bonds in each species used by this module, as a chemist would draw them.
# Validated below against the molecular formulas parsed from the equations: each
# of these molecules is acyclic, so its bond count must be one less than its
# atom count.
SPECIES_BONDS = {
    "H2": {"H-H": 1},
    "Cl2": {"Cl-Cl": 1},
    "HCl": {"H-Cl": 1},
    "O2": {"O=O": 1},
    "H2O": {"O-H": 2},
    "N2": {"N-N triple bond": 1},
    "NH3": {"N-H": 3},
    "CH4": {"C-H": 4},
    "CO2": {"C=O": 2},
}

# Every reaction this module states, keyed by the item that states it. The
# string must appear VERBATIM in that item's stem, which is asserted below, so
# the equation the check uses is the equation the student reads.
REACTIONS = {
    12: "H2 + Cl2 gives 2 HCl",
    13: "H2 + Cl2 gives 2 HCl",
    14: "H2 + Cl2 gives 2 HCl",
    15: "N2 + 3 H2 gives 2 NH3",
    16: "2 H2 + O2 gives 2 H2O",
    17: "2 HCl gives H2 + Cl2",
    18: "CH4 + 2 O2 gives CO2 + 2 H2O",
    20: "N2 + 3 H2 gives 2 NH3",
}

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below)(?![a-z])", re.I)

_OTHER_TOPIC = [
    (re.compile(r"(?<![A-Za-z])enthalp(?:y|ies) of formation(?![A-Za-z])", re.I),
     "6.8's quantity"),
    (re.compile(r"(?<![A-Za-z])Hess(?![A-Za-z])", re.I), "6.9's law"),
    (re.compile(r"(?<![A-Za-z])specific heat(?![A-Za-z])", re.I), "6.4's specific heat"),
    (re.compile(r"(?<![A-Za-z])calorimet[a-z]*", re.I), "6.4's calorimetry"),
    (re.compile(r"(?<![A-Za-z])molar enthalpy of (?:fusion|vaporization|reaction)(?![A-Za-z])",
                re.I), "6.5's and 6.6's quantities"),
]

_SIGNED_ENTHALPY = re.compile(r"(?<![A-Za-z0-9.])[-+]\d[\d.]*\s*kJ/mol(?![A-Za-z])")
_DIRECTION = re.compile(r"(?<![A-Za-z0-9])(?:exothermic|endothermic)(?![A-Za-z0-9])", re.I)

# Items whose key reports a signed enthalpy change. Listed explicitly so the
# guard cannot quietly stop covering one that was edited.
ENTHALPY_ITEMS = (14, 15, 16, 17, 18, 29)


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
    print(f"OK  {module.TOPIC[0]} figures: every bond energy is carried in a table and no "
          "item points at a picture.")


def no_other_topic(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in (item["q"], h.keyed(item), item["why"]):
            for pat, owner in _OTHER_TOPIC:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: a stem, key or why uses {hit.group(0)!r}, "
                    f"which is {owner} -- {text[:70]!r}"
                )
    print(f"OK  {module.TOPIC[0]} scope: no stem, key or why reaches an enthalpy by 6.8's "
          "formation route or 6.9's law, or borrows 6.4's calorimetry.")


def equations_are_stated_and_balanced(module):
    """Every reaction the checks use appears in its own stem, and balances."""
    for i, equation in sorted(REACTIONS.items()):
        stem = module.QUESTIONS[i - 1]["q"]
        assert equation in stem, (
            f"{module.TOPIC[0]} q{i}: the check uses the equation {equation!r}, which does "
            f"not appear in the stem the student reads -- {stem[:90]!r}"
        )
        assert eq.atom_balanced(equation), (
            f"{module.TOPIC[0]} q{i}: {equation!r} does not conserve atoms -- "
            f"{eq.report(equation)}"
        )
        assert eq.charge_balanced(equation), (
            f"{module.TOPIC[0]} q{i}: {equation!r} does not conserve charge -- "
            f"{eq.report(equation)}"
        )
    print(f"OK  {module.TOPIC[0]} equations: {len(REACTIONS)} reaction(s) found verbatim in "
          "their own stems and atom- and charge-balanced from the written formulas.")


def species_bonds_are_consistent(module):
    """SPECIES_BONDS validated against the formulas, not taken on trust.

    Every molecule in this module is acyclic, so it must carry exactly one fewer
    bond than it has atoms -- water has three atoms and two bonds, methane five
    and four. A miscounted species is therefore an arithmetic failure rather
    than something a reader has to notice.
    """
    seen = set()
    for equation in set(REACTIONS.values()):
        for half in equation.split(" gives "):
            for term in half.split(" + "):
                name = _species_name(term)
                seen.add(name)
    assert seen == set(SPECIES_BONDS), (
        f"{module.TOPIC[0]}: the species in the stated equations are {sorted(seen)} but "
        f"SPECIES_BONDS covers {sorted(SPECIES_BONDS)}"
    )
    for name, bonds in sorted(SPECIES_BONDS.items()):
        _, atoms, charge = eq.species(name)
        n_atoms = sum(atoms.values())
        n_bonds = sum(bonds.values())
        assert charge == 0, f"{name} carries a charge, which this check does not cover"
        assert n_bonds == n_atoms - 1, (
            f"{module.TOPIC[0]}: {name} is written with {n_bonds} bond(s) but has "
            f"{n_atoms} atoms; an acyclic molecule must have one fewer bond than atoms"
        )
    print(f"OK  {module.TOPIC[0]} structures: all {len(SPECIES_BONDS)} species carry one "
          "fewer bond than they have atoms, checked against the formulas parsed from the "
          "stated equations.")


# ------------------------------------------------------------------- helpers

def _species_name(term):
    """'2 HCl' to 'HCl'."""
    m = re.match(r"^\d+\s+(\S.*)$", term.strip())
    return (m.group(1) if m else term).strip()


def _coefficient(term):
    m = re.match(r"^(\d+)\s+\S", term.strip())
    return int(m.group(1)) if m else 1


def bond_inventory(equation):
    """The bonds broken and the bonds formed, derived from the equation itself."""
    left, right = equation.split(" gives ")
    out = []
    for half in (left, right):
        counts = {}
        for term in half.split(" + "):
            coeff = _coefficient(term)
            for bond, n in SPECIES_BONDS[_species_name(term)].items():
                counts[bond] = counts.get(bond, 0) + coeff * n
        out.append(counts)
    return out[0], out[1]


def energies(table, counts):
    """``(count, average bond energy)`` pairs, read from the module's own table."""
    return [(n, cg.cell(table, bond, ENERGY)) for bond, n in sorted(counts.items())]


def required(table, equation):
    broken, _ = bond_inventory(equation)
    return sum(n * e for n, e in energies(table, broken))


def released(table, equation):
    _, formed = bond_inventory(equation)
    return sum(n * e for n, e in energies(table, formed))


def delta_h(table, equation):
    """EK 6.7.A.2's subtraction, through h6_thermo so the order is written once."""
    broken, formed = bond_inventory(equation)
    return h6.bond_enthalpy(energies(table, broken), energies(table, formed))


def _close(a, b, tol=1e-9):
    return abs(a - b) < tol


def _unique_extreme(values, pick):
    lab = pick(values, key=values.get)
    ties = [k for k, v in values.items() if _close(v, values[lab])]
    assert ties == [lab], f"the extreme is not unique: {ties} all hold {values[lab]}"
    return lab


_SIGNED_VALUE = re.compile(r"^[-+]\d")


def _present(text, value_text):
    """Is ``value_text`` in ``text``, with a SIGNED value compared raw?

    ``cg.normalize`` keeps a leading minus and strips a leading plus, so
    "+183 kJ/mol" and "-183 kJ/mol" collapse to the same normalized token and
    ``contains_phrase`` reports the reversed value as present in the key. That
    is exactly the family of own-goal this project keeps paying for -- a
    matcher that looks right and quietly cannot tell two things apart -- and it
    matters most here, because the reversed value is the one defect this topic
    exists to catch. Signed values are therefore compared on the RAW string,
    with a digit after the match rejected so "-183" cannot match inside
    "-1830".
    """
    if not _SIGNED_VALUE.match(value_text):
        return cg.contains_phrase(text, value_text)
    idx = text.find(value_text)
    if idx < 0:
        return False
    after = text[idx + len(value_text):idx + len(value_text) + 1]
    return not after.isdigit()


def sign_matcher_self_check():
    """Positive AND negative control for ``_present`` itself, run every time.

    The negative half is the point: it asserts that the normalized matcher
    genuinely CANNOT separate the two signs, which is what makes the raw one
    necessary rather than decorative.
    """
    key = "-183 kJ/mol, so the reaction is exothermic"
    assert _present(key, "-183 kJ/mol"), "the raw matcher fails to find the value it holds"
    assert not _present(key, "+183 kJ/mol"), (
        "POSITIVE CONTROL FAILED: the signed matcher cannot tell + from -, which is the "
        "whole reason it exists"
    )
    assert not _present("-1830 kJ/mol", "-183 kJ/mol"), (
        "the signed matcher must not match a longer number that starts the same way"
    )
    assert cg.contains_phrase(key, "+183 kJ/mol"), (
        "NEGATIVE CONTROL FAILED: the normalized matcher was expected to confuse the two "
        "signs, and if it no longer does then this helper's reason for existing has "
        "changed and should be re-read"
    )
    print("OK  6.7 sign matcher: raw comparison separates +183 from -183, and the "
          "normalized comparison is confirmed unable to, which is why it is not used here.")


def mistake(item, value_text, origin):
    """A recomputed WRONG value must sit in exactly one distractor, never in the key."""
    assert not _present(h.keyed(item), value_text), (
        f"the mistaken value {value_text!r} ({origin}) appears in the KEYED choice, so the "
        f"item has two defensible answers -- {h.keyed(item)!r}"
    )
    hits = [k for k, c in enumerate(item["choices"])
            if k != item["ans"] and _present(c, value_text)]
    assert len(hits) == 1, (
        f"the recomputed mistake {value_text!r} ({origin}) appears in {len(hits)} "
        f"distractor(s); exactly one must carry it -- choices {item['choices']}"
    )
    return value_text


def enthalpy_keys_state_a_direction(module):
    for i in ENTHALPY_ITEMS:
        key = h.keyed(module.QUESTIONS[i - 1])
        assert _SIGNED_ENTHALPY.search(key), (
            f"{module.TOPIC[0]} q{i}: listed as an enthalpy item but the keyed choice "
            f"reports no signed value in kJ/mol -- {key!r}"
        )
        assert _DIRECTION.search(key), (
            f"{module.TOPIC[0]} q{i}: the keyed choice reports an enthalpy change without "
            f"saying whether the reaction is exothermic or endothermic -- {key!r}"
        )
    print(f"OK  {module.TOPIC[0]} sign guard: each of the {len(ENTHALPY_ITEMS)} key(s) "
          "reporting an enthalpy change states its direction as well as its number.")


def anchors_carry_the_direction(module, claims):
    for i in ENTHALPY_ITEMS:
        anchor = claims[i - 1][0]
        assert _DIRECTION.search(anchor), (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} names a value without its "
            "direction, so it would still match a key with the sign reversed"
        )
    print(f"OK  {module.TOPIC[0]} anchor guard: every enthalpy anchor carries exothermic or "
          "endothermic as well as its number.")


def _enthalpy_item(table, item, i, expected, reversed_text):
    """Recompute one reaction's enthalpy change and check the key against it."""
    equation = REACTIONS[i]
    dh = delta_h(table, equation)
    assert _close(dh, expected), f"{equation!r} recomputes to {dh}, not {expected}"
    assert h6.agrees(dh, h.keyed(item)), (
        f"{equation!r} recomputes to {h6.report(dh)}, but the keyed choice says "
        f"{h6.stated_direction(h.keyed(item))!r}: {h.keyed(item)!r}"
    )
    broken, formed = bond_inventory(equation)
    mistake(item, reversed_text, "the subtraction taken the other way round")
    return (f"the bonds broken are {broken} and the bonds formed {formed}, so the tabulated "
            f"energies give {required(table, equation):g} required against "
            f"{released(table, equation):g} released and an enthalpy change of "
            f"{h6.report(dh)}")


# -------------------------------------------------------------- table items

def q10(table, item):
    es = {lab: cg.cell(table, lab, ENERGY) for lab in cg.labels(table)}
    lab = _unique_extreme(es, max)
    assert lab == "N-N triple bond", f"the largest tabulated bond energy is at {lab}: {es}"
    h.shows(item, "N-N triple bond")
    return (f"the tabulated average bond energies are {es} kJ/mol, whose unique maximum is "
            f"at {lab}")


def q11(table, item):
    es = {lab: cg.cell(table, lab, ENERGY) for lab in cg.labels(table)}
    lab = _unique_extreme(es, min)
    assert lab == "Cl-Cl", f"the smallest tabulated bond energy is at {lab}: {es}"
    h.shows(item, "Cl-Cl")
    return (f"the tabulated average bond energies are {es} kJ/mol, whose unique minimum is "
            f"at {lab}")


def q12(table, item):
    equation = REACTIONS[12]
    req = required(table, equation)
    assert _close(req, 679.0), f"the requirement recomputes to {req}"
    h.shows(item, "679 kJ/mol")
    mistake(item, "862 kJ/mol", "the product bonds summed instead of the reactant bonds")
    assert _close(req + released(table, equation), 1541.0)
    mistake(item, "1541 kJ/mol", "the two totals added together")
    assert _close(abs(delta_h(table, equation)), 183.0)
    mistake(item, "183 kJ/mol", "the difference reported in place of the requirement")
    broken, _ = bond_inventory(equation)
    return (f"the bonds broken in {equation!r} are {broken}, whose tabulated energies sum "
            f"to {req:g} kJ/mol")


def q13(table, item):
    equation = REACTIONS[13]
    rel = released(table, equation)
    assert _close(rel, 862.0), f"the release recomputes to {rel}"
    h.shows(item, "862 kJ/mol")
    mistake(item, "679 kJ/mol", "the reactant bonds summed instead of the product bonds")
    mistake(item, "431 kJ/mol", "only one of the two product bonds counted")
    assert _close(rel + required(table, equation), 1541.0)
    mistake(item, "1541 kJ/mol", "the two totals added together")
    _, formed = bond_inventory(equation)
    return (f"the bonds formed in {equation!r} are {formed}, whose tabulated energies sum "
            f"to {rel:g} kJ/mol")


def q14(table, item):
    return _enthalpy_item(table, item, 14, -183.0, "+183 kJ/mol")


def q15(table, item):
    return _enthalpy_item(table, item, 15, -92.0, "+92 kJ/mol")


def q16(table, item):
    return _enthalpy_item(table, item, 16, -482.0, "+482 kJ/mol")


def q17(table, item):
    return _enthalpy_item(table, item, 17, 183.0, "-183 kJ/mol")


def q18(table, item):
    return _enthalpy_item(table, item, 18, -802.0, "+802 kJ/mol")


def q19(table, item):
    formed = SPECIES_BONDS["H2O"]
    assert list(formed) == ["O-H"], f"water is written with the bonds {formed}"
    n = 2 * formed["O-H"]
    assert n == 4, f"two molecules of water carry {n} such bonds"
    assert cg.cell(table, "O-H", ENERGY) > 0, "the bond must be one the table prices"
    h.shows(item, "Four")
    return (f"water is written with {formed['O-H']} bonds of that kind, so two molecules "
            f"carry {n}")


def q20(table, item):
    equation = REACTIONS[20]
    broken, _ = bond_inventory(equation)
    triple = broken["N-N triple bond"] * cg.cell(table, "N-N triple bond", ENERGY)
    hh = broken["H-H"] * cg.cell(table, "H-H", ENERGY)
    # Named, not compared by position: the two contributions are separate sums
    # over the same reactant side, and which is larger is the whole question.
    hydrogen_wins = hh > triple
    assert hydrogen_wins, (
        f"the three hydrogen bonds contribute {hh:g} kJ/mol against the triple bond's "
        f"{triple:g}, so the key is false"
    )
    assert not _close(hh, triple), "the two contributions must not be equal"
    h.shows(item, "The three hydrogen to hydrogen bonds together")
    return (f"the tabulated energies give {hh:g} kJ/mol for the {broken['H-H']} hydrogen "
            f"bonds against {triple:g} kJ/mol for the triple bond")


TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17,
                18: q18, 19: q19, 20: q20}


# ------------------------------------------------------------- stem numerics

def n25(item):
    first = h6.bond_enthalpy([(1, 2000.0)], [(1, 2400.0)])
    second = h6.bond_enthalpy([(1, 2400.0)], [(1, 2000.0)])
    assert _close(first, -400.0) and _close(second, 400.0), (first, second)
    first_is_exothermic = h6.direction(first)["exothermic"]
    second_is_exothermic = h6.direction(second)["exothermic"]
    assert first_is_exothermic and not second_is_exothermic, (first, second)
    h.shows(item, "The first, because the energy released exceeds the energy required")
    return (f"the stated totals give {h6.report(first)} for the first reaction and "
            f"{h6.report(second)} for the second, so only the first releases more than it "
            "requires")


def n29(item):
    dh = h6.bond_enthalpy([(1, 1500.0)], [(1, 1750.0)])
    assert _close(dh, -250.0), f"the enthalpy change recomputes to {dh}"
    assert h6.agrees(dh, h.keyed(item)), (
        f"the recomputed value is {h6.report(dh)} but the keyed choice says "
        f"{h6.stated_direction(h.keyed(item))!r}"
    )
    h.shows(item, "-250 kJ/mol, so the reaction is exothermic")
    mistake(item, "+250 kJ/mol", "the subtraction taken the other way round")
    assert _close(1500.0 + 1750.0, 3250.0)
    mistake(item, "-3250 kJ/mol", "the two totals added instead of subtracted")
    mistake(item, "-1750 kJ/mol", "the release reported in place of the difference")
    mistake(item, "-1500 kJ/mol", "the requirement reported in place of the difference")
    return (f"1500 kJ/mol required minus 1750 kJ/mol released recomputes as "
            f"{h6.report(dh)}, with three recomputed mistakes each in one distractor")


NUMERIC = {25: n25, 29: n29}


CLAIMS = [
 ("It changes the potential energy of the system",
  "EK 6.7.A.1: during a chemical reaction bonds are broken and/or formed, and these events change the potential energy of the system."),
 ("By adding up the average bond energies of all the bonds in the reactant molecules",
  "EK 6.7.A.2's first sentence, verbatim in substance, and the reactant sum is the energy REQUIRED."),
 ("The average energy released in forming the bonds in the product molecules",
  "EK 6.7.A.2's second sentence: likewise the average energy released in forming the bonds in the product molecules can be estimated."),
 ("It is exothermic",
  "EK 6.7.A.2: if the energy released is greater than the energy required, the reaction is exothermic."),
 ("It is endothermic",
  "EK 6.7.A.2's mirror clause: if the energy required is greater than the energy released, the reaction is endothermic."),
 ("The energy required to break the reactant bonds minus the energy released forming the product bonds",
  "Learning objective 6.7.A with EK 6.7.A.2: this order of subtraction is what makes an exothermic reaction, in which the release is greater, come out negative."),
 ("It requires energy",
  "EK 6.7.A.2 speaks throughout of the energy REQUIRED to break the bonds in the reactant molecules, which is why the reactant total is a cost."),
 ("It releases energy",
  "EK 6.7.A.2 speaks of the energy RELEASED in forming the bonds in the product molecules, which is why the product total is a refund."),
 ("Because the bond energies used are averages over the molecules a bond occurs in",
  "EK 6.7.A.2 twice says a total can be ESTIMATED and twice calls the values AVERAGE bond energies, so the imprecision enters with the values."),
 ("N-N triple bond",
  "EK 6.7.A.2 makes the average bond energy the energy required to break the bond. q10 recomputes every tabulated value and checks the maximum is unique."),
 ("Cl-Cl",
  "The same reading downward. q11 checks the minimum tabulated value is unique."),
 ("679 kJ/mol",
  "EK 6.7.A.2's reactant sum. q12 derives the bonds broken from the equation in the stem, prices them from the table, and recomputes three mistaken totals as well."),
 ("862 kJ/mol",
  "EK 6.7.A.2's product sum, derived the same way. q13 recomputes it and three mistakes."),
 ("-183 kJ/mol, so the reaction is exothermic",
  "Learning objective 6.7.A's subtraction on the bonds derived from the stem's own equation, with EK 6.7.A.2 supplying the direction. q14 checks the key's word against the sign."),
 ("-92 kJ/mol, so the reaction is exothermic",
  "The same subtraction for the ammonia synthesis, with the triple bond and six product bonds derived from the equation. q15 recomputes it."),
 ("-482 kJ/mol, so the reaction is exothermic",
  "The same subtraction for the formation of water. q16 recomputes it and checks the reversed value is a distractor."),
 ("+183 kJ/mol, so the reaction is endothermic",
  "The reverse reaction of item 14, where the bonds broken are now the stronger set, so EK 6.7.A.2's endothermic clause applies. q17 recomputes it."),
 ("-802 kJ/mol, so the reaction is exothermic",
  "The same subtraction for the combustion of methane, with ten bonds broken and six formed. q18 recomputes it."),
 ("Four",
  "EK 6.7.A.2 requires ALL the bonds in the product molecules to be counted. q19 reads the count from the structure table validated against the formula."),
 ("The three hydrogen to hydrogen bonds together",
  "EK 6.7.A.2 sums over every reactant bond, so three weaker bonds can outweigh one stronger. q20 recomputes both contributions from the tabulated energies."),
 ("The product total must be subtracted from the reactant total, not added to it",
  "EK 6.7.A.2 makes one total a requirement and the other a release, so they enter with opposite effect and their sum reports nothing."),
 ("The reaction is exothermic, since more energy was released than required",
  "EK 6.7.A.2's exothermic clause is exactly the case in which the requirement minus the release falls below zero."),
 ("The magnitude is right and the sign is reversed",
  "Learning objective 6.7.A takes the requirement minus the release, so exchanging the terms negates the difference and leaves its size alone."),
 ("Because energy must be supplied to break the bonds in the reactant molecules",
  "EK 6.7.A.2 calls the reactant total the energy REQUIRED, which is energy put in before anything is given back."),
 ("The first, because the energy released exceeds the energy required",
  "EK 6.7.A.2's exothermic clause applied to two stated pairs of totals. n25 recomputes both differences and checks only one is negative."),
 ("About zero, since the energy required and the energy released are the same",
  "Learning objective 6.7.A subtracts the release from the requirement, so identical sets of bonds give identical totals and neither of EK 6.7.A.2's two named cases."),
 ("The bond energies themselves are averages, so the enthalpy change obtained is an estimate",
  "EK 6.7.A.2 calls the tabulated quantities AVERAGE bond energies and says each total can be ESTIMATED from them, so the hedge belongs to the values."),
 ("No; it says bonds are broken and/or formed",
  "EK 6.7.A.1's own wording is and/or, which allows either or both rather than requiring the pair."),
 ("-250 kJ/mol, so the reaction is exothermic",
  "Learning objective 6.7.A's subtraction on two stated totals. n29 recomputes it and three mistaken routes."),
 ("The reaction is exothermic when the energy released forming the product bonds exceeds the energy required to break the reactant bonds",
  "EK 6.7.A.2's own sentence: the comparison is between the two totals, not between counts of bonds or individual bond strengths."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, what do the bonds do?"
        no_figure_language(mod)

    def hess_creeps_in(mod, cl):
        mod.QUESTIONS[5]["q"] = "How is the enthalpy change found using Hess's law here?"
        no_other_topic(mod)

    def equation_edited_out_of_the_stem(mod, cl):
        # The check would go on using the equation it holds while the student
        # reads a different one. Nothing else in the file would notice.
        mod.QUESTIONS[14]["q"] = (
            "What is the enthalpy change of the ammonia synthesis, estimated from the "
            "tabulated bond energies?")
        equations_are_stated_and_balanced(mod)

    def equation_unbalanced(mod, cl):
        mod.QUESTIONS[15]["q"] = mod.QUESTIONS[15]["q"].replace(
            "2 H2 + O2 gives 2 H2O", "2 H2 + O2 gives 3 H2O")
        REACTIONS[16] = "2 H2 + O2 gives 3 H2O"
        try:
            equations_are_stated_and_balanced(mod)
        finally:
            REACTIONS[16] = "2 H2 + O2 gives 2 H2O"

    def species_miscounted(mod, cl):
        SPECIES_BONDS["NH3"] = {"N-H": 4}
        try:
            species_bonds_are_consistent(mod)
        finally:
            SPECIES_BONDS["NH3"] = {"N-H": 3}

    def enthalpy_key_loses_its_direction(mod, cl):
        ch = list(mod.QUESTIONS[13]["choices"])
        ch[0] = "-183 kJ/mol"
        mod.QUESTIONS[13]["choices"] = ch
        cl[13] = ("-183 kJ/mol", cl[13][1])
        enthalpy_keys_state_a_direction(mod)

    def anchor_loses_its_direction(mod, cl):
        cl[17] = ("+183 kJ/mol", cl[17][1])
        anchors_carry_the_direction(mod, cl)

    def enthalpy_key_direction_reversed(mod, cl):
        # The key moved to the reversed value. Every choice is untouched, so
        # they stay distinct and the new anchor matches only the new key; only
        # the comparison against the SIGN of the recomputed value can reject it.
        mod.QUESTIONS[14]["ans"] = 1
        cl[14] = ("+92 kJ/mol, so the reaction is endothermic", cl[14][1])

    def bond_energy_changed(mod, cl):
        # One tabulated value edited, so the keyed enthalpy no longer follows
        # from the table the student is given.
        mod.QUESTIONS[13]["table"] = dict(
            headers=h6_7._T_BOND["headers"],
            rows=[[lab, ("450" if lab == "H-H" else v)]
                  for lab, v in h6_7._T_BOND["rows"]])

    def reversed_distractor_removed(mod, cl):
        # The distractor carrying the reversed value replaced. The key is still
        # right and every choice still distinct -- the item has simply stopped
        # testing the one error it exists to test.
        ch = list(mod.QUESTIONS[17]["choices"])
        ch[1] = "-500 kJ/mol, so the reaction is exothermic"
        mod.QUESTIONS[17]["choices"] = ch

    def strongest_bond_moved(mod, cl):
        mod.QUESTIONS[9]["table"] = dict(
            headers=h6_7._T_BOND["headers"],
            rows=[[lab, ("1200" if lab == "C=O" else v)]
                  for lab, v in h6_7._T_BOND["rows"]])

    def hydrogen_contribution_flipped(mod, cl):
        # The H-H bond weakened so that three of them no longer outweigh the
        # triple bond. The magnitudes are all still plausible; only the
        # comparison changes.
        mod.QUESTIONS[19]["table"] = dict(
            headers=h6_7._T_BOND["headers"],
            rows=[[lab, ("300" if lab == "H-H" else v)]
                  for lab, v in h6_7._T_BOND["rows"]])

    return [("a stem referring to a diagram the bank cannot show", figure_language),
            ("a stem borrowing 6.9's Hess's law", hess_creeps_in),
            ("the equation removed from a stem while the check keeps using it",
             equation_edited_out_of_the_stem),
            ("an equation in a stem that does not conserve atoms", equation_unbalanced),
            ("a species written with one bond too many for its formula", species_miscounted),
            ("a key reporting an enthalpy change with no direction",
             enthalpy_key_loses_its_direction),
            ("an anchor cut back to a bare value while the key keeps its direction",
             anchor_loses_its_direction),
            ("a key moved to the reversed value, with the magnitude still right",
             enthalpy_key_direction_reversed),
            ("a tabulated bond energy changed under a keyed enthalpy", bond_energy_changed),
            ("the reversed-subtraction distractor replaced, so the item stops testing it",
             reversed_distractor_removed),
            ("the strongest tabulated bond moved off the keyed one", strongest_bond_moved),
            ("the tabulated H-H energy lowered so the keyed comparison is false",
             hydrogen_contribution_flipped)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h6.selftest()
    eq.selftest()
    h.selftest(h6_7, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

sign_matcher_self_check()
no_figure_language(h6_7)
no_other_topic(h6_7)
equations_are_stated_and_balanced(h6_7)
species_bonds_are_consistent(h6_7)
enthalpy_keys_state_a_direction(h6_7)
anchors_carry_the_direction(h6_7, CLAIMS)
h.run(h6_7, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
