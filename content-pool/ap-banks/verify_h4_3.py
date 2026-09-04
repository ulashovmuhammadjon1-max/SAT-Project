"""Key audit for AP CHEMISTRY 4.3 Representations of Reactions.

One ``(anchor, claim)`` per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EK 4.3.A.1  Balanced chemical equations in their various forms can be
            translated into symbolic particulate representations.  (every item)
EK 4.2.A.2  supplies what survives that translation -- equal numbers of atoms
            of every element, with mass and charge conserved.
            (items 3, 4, 5, 7, 12, 13, 14, 15, 18, 19, 21, 22, 23, 24, 25, 26,
            27, 28, 29, 30)
EK 4.2.A.3  supplies the "various forms" EK 4.3.A.1 refers to.
            (items 2, 9, 10)
EK 4.1.A.1  supplies the physical-process case, where composition survives.
            (items 11, 17)

THE PARTICULATE BOXES ARE COUNTS, AND THE COUNTS ARE RECOMPUTED. Every box in
this module is written as "4 H2 molecules and 2 O2 molecules". ``box_atoms``
below parses that into element counts through ``h_equation``, so each "which
proposal is consistent" item is settled by ADDING UP the proposals rather than
by trusting the author -- and the check requires the consistent proposal to be
unique, so a second correct box would fail rather than ship an item with two
defensible answers.

Fifteen items carry no table but state their counts in the stem; those are
recomputed the same way in ``NUMERIC``.

NO FIGURE LANGUAGE. This is the topic most at risk from the bank's inability to
show a picture, so ``no_figure_language`` runs over every stem and choice.

NEGATIVE CONTROL: ``python3 verify_h4_3.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h_equation as heq

import h4_3

PARTS = "Particles in the box"

# "4 H2O molecules", "2 Ca2+ particles", "4 CaCO3 formula units". The formula
# must start with a capital, which is what keeps ordinary words out; an optional
# single-digit charge with its sign may follow, as h_equation writes ions.
_PARTICLE = re.compile(r"(\d+)\s+([A-Z][A-Za-z0-9()]*(?:\d?[+-])?)")

_FIGURE = re.compile(
    r"(?<![a-z])(as shown|shown below|shown above|figure|image|picture|depicted|"
    r"pictured|illustrated|(?:diagram|graph|profile|curve|plot|chart|box)e?s?\s+"
    r"(?:above|below))(?![a-z])", re.I)


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, but every particulate "
                f"box in this module is a count -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every particulate model is carried as a count of "
          "particles, and no stem or choice points at a drawing.")


def box(text):
    """``('4 H2 molecules and 2 O2 molecules')`` to ``(atoms, charge, particles)``."""
    hits = _PARTICLE.findall(str(text))
    assert hits, f"no particle counts readable in {text!r}"
    atoms, charge, particles = {}, 0, 0
    for count, formula in hits:
        n = int(count)
        _, els, q = heq.species(formula)
        for el, k in els.items():
            atoms[el] = atoms.get(el, 0) + n * k
        charge += n * q
        particles += n
    return atoms, charge, particles


def box_atoms(text):
    return box(text)[0]


def consistent_proposal(table, item, anchor):
    """Exactly one tabulated proposal conserves the atoms of the starting box."""
    rows = {r[0]: r[table["headers"].index(PARTS)] for r in table["rows"]}
    assert "Before" in rows, f"the table has no 'Before' row: {list(rows)}"
    start = box_atoms(rows["Before"])
    ok = sorted(lab for lab, cell in rows.items()
                if lab != "Before" and box_atoms(cell) == start)
    assert len(ok) == 1, (
        f"proposals conserving every element: {ok} (starting box {start}); exactly one "
        "must, or the item has more than one defensible answer"
    )
    h.shows(item, anchor)
    assert cg.contains_phrase(item["choices"][item["ans"]], ok[0].split()[-1]), (
        f"the consistent proposal is {ok[0]} but the key reads {item['choices'][item['ans']]!r}"
    )
    counts = {lab: box_atoms(cell) for lab, cell in rows.items() if lab != "Before"}
    return (f"the starting box holds {start} and the proposals hold {counts}, so exactly "
            f"one, {ok[0]}, conserves the atoms of every element")


def stem_box(item, expected, anchor, note):
    """The keyed box holds ``expected`` atoms, and no distractor box does."""
    key = item["choices"][item["ans"]]
    got = box_atoms(key)
    assert got == expected, f"the keyed box holds {got}, not the required {expected}"
    also = [i for i, c in enumerate(item["choices"])
            if i != item["ans"] and _readable(c) and box_atoms(c) == expected]
    assert not also, f"choice(s) {also} also conserve the atoms, so the item has two answers"
    h.shows(item, anchor)
    return f"{note}; the keyed box recomputes to {got}, matched by no other choice"


def _readable(text):
    try:
        box_atoms(text)
        return True
    except AssertionError:
        return False


# ---------------------------------------------------------------- table items

def q4(table, item):
    return consistent_proposal(table, item, "Proposal W")


def q7(table, item):
    return consistent_proposal(table, item, "Proposal J")


def q13(table, item):
    return consistent_proposal(table, item, "Proposal P")


def q20(table, item):
    """A compound is a particle holding atoms of more than one element."""
    rows = {r[0]: r[table["headers"].index(PARTS)] for r in table["rows"]}
    kinds = {}
    for lab, cell in rows.items():
        formulas = [f for _, f in _PARTICLE.findall(cell)]
        kinds[lab] = [f for f in formulas if len(heq.species(f)[1]) > 1]
        assert formulas, f"{lab}: no particles readable"
    mixed = sorted(lab for lab, cs in kinds.items()
                   if len(cs) > 1 and len(set(cs)) > 1)
    assert mixed == ["Box 3"], (
        f"boxes holding more than one kind of compound particle: {mixed} (compounds per "
        f"box {kinds})"
    )
    h.shows(item, "Box 3")
    return (f"classifying every tabulated particle by how many elements it contains gives "
            f"{kinds}, so exactly one box holds two different compounds")


def q22(table, item):
    return consistent_proposal(table, item, "Proposal T")


TABLE_CHECKS = {4: q4, 7: q7, 13: q13, 20: q20, 22: q22}


# --------------------------------------------------------------- stem numerics

def n5(item):
    return stem_box(item, box_atoms("3 N2 molecules and 9 H2 molecules"), "6 NH3",
                    "three nitrogen molecules with nine hydrogen molecules give "
                    "six ammonia molecules")


def n8(item):
    key = item["choices"][item["ans"]]
    counts = dict((f, int(n)) for n, f in _PARTICLE.findall(key))
    assert counts["CO"] == 2 * counts["O2"], (
        f"the keyed box holds {counts}, which is not the two to one ratio the equation needs"
    )
    also = [i for i, c in enumerate(item["choices"]) if i != item["ans"]
            and dict((f, int(n)) for n, f in _PARTICLE.findall(c)).get("CO")
            == 2 * dict((f, int(n)) for n, f in _PARTICLE.findall(c)).get("O2", 0)]
    assert not also, f"choice(s) {also} are also in the required ratio"
    h.shows(item, "4 CO molecules and 2 O2 molecules")
    return f"the keyed box holds {counts}, the only choice at the two to one ratio the equation sets"


def n14(item):
    atoms = box_atoms("5 CH4 molecules")
    assert atoms["H"] == 20, f"five methane molecules hold {atoms} hydrogen atoms"
    h.shows(item, "20")
    return f"counting four hydrogens in each of five molecules gives {atoms['H']} atoms"


def n18(item):
    return stem_box(item, box_atoms("3 CH4 molecules and 6 O2 molecules"),
                    "3 CO2 molecules and 6 H2O molecules",
                    "three sets of the equation consume three methane and six oxygen molecules")


def n19(item):
    return stem_box(item, box_atoms("6 H2 molecules and 2 O2 molecules"),
                    "4 H2O molecules and 2 H2 molecules",
                    "two oxygen molecules can consume only four of the six hydrogen molecules")


def n21(item):
    key = item["choices"][item["ans"]]
    n_cl = dict((f, int(n)) for n, f in _PARTICLE.findall(key))
    atoms, charge, _ = box("3 Ca2+ particles and " + key.split(",")[0] + " Cl- particles")
    assert charge == 0, f"the box carries a total charge of {charge:+d}, not zero"
    assert n_cl.get("6") is None
    h.shows(item, "6, two chloride ions for each calcium ion")
    return (f"three calcium ions of plus two need six chloride ions of minus one to bring the "
            f"total charge to {charge:+d}, which is what CaCl2 requires")


def n24(item):
    atoms = box_atoms("8 Mg atoms")
    assert atoms == {"Mg": 8}, atoms
    assert box_atoms("8 MgO formula units")["Mg"] == atoms["Mg"], \
        "the magnesium count must carry across unchanged"
    h.shows(item, "8, one formula unit for each magnesium atom")
    return (f"the equation pairs each magnesium atom with one formula unit of the oxide, so "
            f"{atoms['Mg']} atoms give {atoms['Mg']} formula units")


def n29(item):
    _, charge, particles = box("5 Ag+ particles and 5 Cl- particles")
    assert charge == 0, f"the starting box carries a total charge of {charge:+d}"
    pairs = particles // 2
    assert pairs == 5, f"the ion pairs recompute to {pairs}"
    assert box_atoms("5 AgCl formula units") == box_atoms("5 Ag+ particles and 5 Cl- particles"), \
        "the solid must carry the same atoms as the ions it came from"
    h.shows(item, "5, one for each pair of ions")
    return f"ten ions of total charge {charge:+d} pair off into {pairs} formula units of the solid"


NUMERIC = {5: n5, 8: n8, 14: n14, 18: n18, 19: n19, 21: n21, 24: n24, 29: n29}


CLAIMS = [
 ("Symbolic particulate representations",
  "EK 4.3.A.1, verbatim in substance: balanced chemical equations in their various forms can be translated into symbolic particulate representations."),
 ("balanced molecular, complete ionic and net ionic forms alike",
  "EK 4.3.A.1 says the equations IN THEIR VARIOUS FORMS, and EK 4.2.A.3 names those forms."),
 ("number of atoms of each element, before and after",
  "EK 4.3.A.1 makes the model a translation of the balanced equation and EK 4.2.A.2 requires equal numbers of atoms of every element before and after; molecule counts are not constrained."),
 ("Proposal W",
  "EK 4.2.A.2's atom counts carried into the model by EK 4.3.A.1. Recomputed in q4, which also requires the consistent proposal to be unique."),
 ("6 NH3",
  "EK 4.3.A.1's translation of the coefficients into particles. Recomputed in n5 from the starting box's own atom counts."),
 ("two oxygen atoms joined to one another",
  "EK 4.3.A.1 translates the formula in the equation into the particle drawn, and the equation writes the substance as O2, so a particle carries two atoms."),
 ("Proposal J",
  "EK 4.2.A.2's atom counts carried into the model by EK 4.3.A.1, recomputed in q7."),
 ("4 CO molecules and 2 O2 molecules",
  "EK 4.3.A.1 translates the coefficients into a particle ratio. Recomputed in n8, which checks the keyed box is the only one at two carbon monoxide molecules per oxygen molecule."),
 ("separate positive and negative ions dispersed among the solvent particles",
  "EK 4.3.A.1 permits any of EK 4.2.A.3's forms to be translated, and the complete ionic form writes each dissolved substance as separate ions."),
 ("Only the ions that combine and the product they form",
  "EK 4.3.A.1's translation applied to EK 4.2.A.3's net ionic form, which omits the species standing unaltered on both sides."),
 ("same water molecules appear in both, farther apart in the vapor",
  "The learning objective extends the consistent particulate model to a physical process, and EK 4.1.A.1 makes a phase change one in which composition does not change."),
 ("Equal numbers of separate Na+ and Cl- particles surrounded by water molecules",
  "EK 4.3.A.1 translates the dissolution equation into particles and EK 4.2.A.2 requires charge to be conserved, so one ion of each kind per formula unit gives a neutral box."),
 ("Proposal P",
  "EK 4.2.A.2's atom counts carried into the model by EK 4.3.A.1, recomputed in q13."),
 ("20",
  "EK 4.3.A.1 translates a formula's subscript into a count of atoms in one particle. Recomputed in n14."),
 ("atoms as having been created",
  "EK 4.2.A.2 requires any representation of a chemical change to contain equal numbers of atoms of every element before and after, and EK 4.3.A.1 makes the particulate model such a representation."),
 ("coefficients written in front of the formulas",
  "EK 4.3.A.1's translation carries the coefficients of the balanced equation into how many particles of each substance take part."),
 ("subscripts written inside each formula",
  "EK 4.3.A.1's translation carries a subscript into how many atoms of an element are joined within one particle, which EK 4.1.A.1 makes the identity of the substance."),
 ("3 CO2 molecules and 6 H2O molecules",
  "EK 4.3.A.1's translation of the coefficients into particles, recomputed in n18 against the starting box's atom counts."),
 ("4 H2O molecules and 2 H2 molecules",
  "EK 4.3.A.1's translation with one reactant in excess; recomputed in n19, where the leftover hydrogen is what keeps EK 4.2.A.2's counts equal."),
 ("Box 3",
  "EK 4.3.A.1 makes the model a symbolic representation of the substances present. Recomputed in q20 by counting how many elements each tabulated particle contains."),
 ("6, two chloride ions for each calcium ion",
  "EK 4.3.A.1 translates the formula into the picture and EK 4.2.A.2 requires charge to be conserved. Recomputed in n21, where the box comes out neutral."),
 ("Proposal T",
  "EK 4.2.A.2's atom counts carried into the model by EK 4.3.A.1, recomputed in q22 for a decomposition."),
 ("oxygen atom would have to disappear",
  "EK 4.2.A.2 forbids a representation of a chemical change from losing atoms, and EK 4.3.A.1 makes the drawing such a representation."),
 ("8, one formula unit for each magnesium atom",
  "EK 4.3.A.1's translation of the coefficients into particles, recomputed in n24."),
 ("may differ before and after",
  "EK 4.2.A.2 constrains the numbers of ATOMS of every element rather than the number of particles, and EK 4.3.A.1 carries only that requirement into the model."),
 ("ratio of the particles rather than how many are drawn",
  "EK 4.3.A.1 makes the model a translation of an equation whose coefficients state proportions, and EK 4.2.A.2's conservation is satisfied within each box separately."),
 ("same total charge in the box before and after",
  "EK 4.2.A.2 states that equations demonstrate that mass and charge are conserved, and EK 4.3.A.1 carries that into the model; the box is not neutral, since it holds an ion throughout."),
 ("number of separate particles drawn",
  "EK 4.2.A.2 requires atoms, mass and charge to survive, and EK 4.3.A.1 carries those requirements over, but nothing there fixes how many particles the box holds."),
 ("5, one for each pair of ions",
  "EK 4.3.A.1's translation of the net ionic equation at a one to one ratio, recomputed in n29 together with the neutrality of the starting box."),
 ("contradicts the balanced equation misrepresents",
  "EK 4.3.A.1 makes the model a TRANSLATION of the balanced equation, so consistency means agreeing with what the equation asserts, and EK 4.2.A.2 fixes what must survive."),
]


def _extra_mutations():
    def second_consistent_proposal(mod, cl):
        """A second proposal made to conserve the atoms too, so the key is not unique."""
        t = mod.QUESTIONS[3]["table"]
        mod.QUESTIONS[3]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "4 H2O molecules"] if r[0] == "Proposal X" else list(r)
                  for r in t["rows"]])

    def key_proposal_broken(mod, cl):
        """The keyed proposal retyped so it no longer conserves the atoms."""
        t = mod.QUESTIONS[6]["table"]
        mod.QUESTIONS[6]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "3 NH3 molecules"] if r[0] == "Proposal J" else list(r)
                  for r in t["rows"]])

    def starting_box_corrupted(mod, cl):
        """The starting box retyped, so the recomputed proposal changes."""
        t = mod.QUESTIONS[12]["table"]
        mod.QUESTIONS[12]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "4 CO molecules and 3 O2 molecules"] if r[0] == "Before"
                  else list(r) for r in t["rows"]])

    def second_mixture_box(mod, cl):
        """A second box given two different compounds, so the key is not unique."""
        t = mod.QUESTIONS[19]["table"]
        mod.QUESTIONS[19]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "3 CO molecules and 3 NO molecules"] if r[0] == "Box 1"
                  else list(r) for r in t["rows"]])

    def stem_key_miscounted(mod, cl):
        """A stem-count key moved to a box that does not conserve the atoms."""
        mod.QUESTIONS[4]["choices"][0] = "5 NH3 molecules"
        cl[4] = ("5 NH3", cl[4][1])

    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "Which model matches the boxes shown above?"
        no_figure_language(mod)

    return [("a second proposal made consistent, so the key is not unique",
             second_consistent_proposal),
            ("the keyed proposal retyped so it loses atoms", key_proposal_broken),
            ("the starting box retyped so the recomputed proposal changes",
             starting_box_corrupted),
            ("a second box given two different compounds", second_mixture_box),
            ("a stem-count key moved to a box that does not conserve atoms",
             stem_key_miscounted),
            ("a stem pointing at boxes the bank cannot show", figure_language)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h4_3, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

heq.selftest()
no_figure_language(h4_3)
h.run(h4_3, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
