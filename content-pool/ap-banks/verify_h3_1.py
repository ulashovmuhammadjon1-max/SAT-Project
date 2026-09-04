"""Key audit for AP CHEMISTRY 3.1 Intermolecular and Interparticle Forces.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. The five table items are recomputed from the
tabulated species types alone.

WHAT THE KEYS REST ON
---------------------
EK 3.1.A.1  London dispersion forces result from Coulombic interactions between
            temporary, fluctuating dipoles; they are OFTEN the strongest net
            intermolecular force between large molecules; and the term is NOT a
            synonym for van der Waals forces.        (items 1, 2, 3, 27, 30)
EK 3.1.A.2  A polar molecule's dipole moment leads to ADDITIONAL interactions;
            dipole-dipole interactions are present between polar molecules and
            depend on the magnitudes of the dipoles and their relative
            orientation; polar-polar interactions are TYPICALLY greater than
            nonpolar-nonpolar at comparable size BECAUSE they act in addition to
            dispersion forces; ion-dipole forces are present between ions and
            polar molecules and TEND to be stronger than dipole-dipole.
                    (items 4, 5, 6, 7, 8, 9, 16, 17, 18, 19, 20, 21, 26, 29)
EK 3.1.A.3  The relative strength and orientation dependence of dipole-dipole
            and ion-dipole forces can be understood QUALITATIVELY from the sign
            of the partial charges and how they interact with an ion or an
            adjacent dipole.                                (items 10, 22)
EK 3.1.A.4  Hydrogen bonding is a strong type of intermolecular interaction, for
            hydrogen covalently bonded to N, O or F and attracted to the
            negative end of a dipole formed by N, O or F in a different
            molecule or a different part of the same one.
                                                    (items 11, 12, 13, 14, 23)
EK 3.1.A.5  In large biomolecules, noncovalent interactions may occur between
            different molecules or between different regions of the same large
            biomolecule.                                    (items 15, 28)
LO 3.1.A    The two cases: molecules of the same chemical species, and molecules
            of two different chemical species.                     (item 24)

THE HOLE IN THE SOURCE. Three sub-points are missing from the CED PDF's text
layer -- 3.1.A.1's i and ii and 3.1.A.2's i -- and the word "polarizability"
does not occur anywhere in the dump. ``no_missing_subpoint_material`` asserts
that nothing in this module fills that gap from memory: no item claims
dispersion forces grow with polarizability or molar mass, or that they are
present in every substance. Those things are standard teaching and this source
does not contain them.

THE HEDGES ARE LOAD-BEARING. Every comparison the framework makes here is
qualified -- "often", "typically", "tend to" -- and hydrogen bonding is ranked
against nothing at all. ``no_unstated_ranking`` asserts that no keyed choice
compares hydrogen bonding by strength with another named force, EXCEPT in the
one item whose stem asks which comparison the framework does NOT make, where
naming it is the whole point.

NEGATIVE CONTROL: ``python3 verify_h3_1.py --selftest``.
"""
import re
import sys

import h_chem_notation as hn
import h3_1 as M

FIRST = "First species"
SECOND = "Second species"
POLARITY = "Polarity of its molecules"
SIZE = "Molecular size"

ION = "an ion"
POLAR = "a polar molecule"
NONPOLAR = "a nonpolar molecule"
KINDS = (ION, POLAR, NONPOLAR)

COUNTWORD = {0: "None of them", 1: "Exactly one", 2: "Exactly two",
             3: "Exactly three", 4: "All four"}

cg = hn.cg


# ----------------------------------------------------------------- helpers

def pairs(table):
    """[(label, first kind, second kind)], with every cell required to be a known kind."""
    heads = list(table["headers"])
    a, b = heads.index(FIRST), heads.index(SECOND)
    out = []
    for row in table["rows"]:
        first, second = str(row[a]).strip(), str(row[b]).strip()
        for cell in (first, second):
            assert cell in KINDS, (
                f"row {row[0]!r} names {cell!r}, which is not one of the three species "
                f"kinds this module classifies: {KINDS}"
            )
        out.append((str(row[0]), first, second))
    return out


def is_ion_dipole(row):
    """EK 3.1.A.2.iii: an ion together with a polar molecule."""
    _, a, b = row
    return {a, b} == {ION, POLAR}


def is_dipole_dipole(row):
    """EK 3.1.A.2.ii: two polar molecules."""
    _, a, b = row
    return a == POLAR and b == POLAR


# ------------------------------------------------------------ table questions

def q16(t, item):
    rows = pairs(t)
    hits = [r[0] for r in rows if is_ion_dipole(r)]
    assert len(hits) == 1, (
        f"{len(hits)} tabulated pairs put an ion with a polar molecule: {hits}; the item "
        "needs exactly one"
    )
    hn.keyed(item, hits[0])
    return (f"of the {len(rows)} tabulated pairs only {hits[0]} puts an ion with a polar "
            "molecule, which is EK 3.1.A.2's ion-dipole case")


def q17(t, item):
    rows = pairs(t)
    hits = [r[0] for r in rows if is_dipole_dipole(r)]
    assert len(hits) == 1, (
        f"{len(hits)} tabulated pairs put two polar molecules together: {hits}; the item "
        "needs exactly one"
    )
    hn.keyed(item, hits[0])
    return (f"of the {len(rows)} tabulated pairs only {hits[0]} puts two polar molecules "
            "together, which is EK 3.1.A.2's dipole-dipole case")


def q18(t, item):
    rows = pairs(t)
    ion = [r[0] for r in rows if is_ion_dipole(r)]
    dip = [r[0] for r in rows if is_dipole_dipole(r)]
    assert len(ion) == 1 and len(dip) == 1, (
        f"the comparison needs exactly one of each named case; found {ion} and {dip}"
    )
    assert ion[0] != dip[0], "the same pair cannot carry both named forces"
    hn.keyed(item, ion[0])
    return (f"{ion[0]} carries the ion-dipole force and {dip[0]} the dipole-dipole force, "
            "and EK 3.1.A.2 says the first tends to be the stronger")


def q19(t, item):
    rows = pairs(t)
    neither = [r[0] for r in rows if not is_ion_dipole(r) and not is_dipole_dipole(r)]
    hn.keyed(item, COUNTWORD[len(neither)])
    return (f"{len(neither)} of the {len(rows)} tabulated pairs contain no polar molecule "
            f"paired as either sub-point describes, namely {', '.join(neither) or 'none'}")


def q20(t, item):
    heads = list(t["headers"])
    p, s = heads.index(POLARITY), heads.index(SIZE)
    polarity = [str(row[p]).strip() for row in t["rows"]]
    assert sorted(polarity) == ["nonpolar", "polar"], (
        f"the comparison needs exactly one polar and one nonpolar substance, not {polarity}"
    )
    for row in t["rows"]:
        assert "comparable" in str(row[s]).lower(), (
            f"row {row[0]!r} does not state a comparable molecular size, which is the "
            "condition EK 3.1.A.2 attaches to the comparison"
        )
    hn.keyed(item, "polar one, because dipole-dipole interactions act in addition")
    return ("exactly one tabulated substance is polar and one nonpolar, both at comparable "
            "size, which is the case EK 3.1.A.2 states the comparison for")


TABLE_CHECKS = {16: q16, 17: q17, 18: q18, 19: q19, 20: q20}


# ------------------------------------------------------- module-specific gates

# What the three missing sub-points most likely said. None of it is in this
# source, so none of it may appear in this module.
_MISSING_MATERIAL = re.compile(
    r"(?<![a-z])(?:polariz(?:ability|able|ability of)|molar mass|molecular mass|"
    r"atomic mass|number of electrons in the molecule)(?![a-z])", re.I)
_ALL_SUBSTANCES = re.compile(
    r"dispersion forces (?:are |act |exist )?(?:present |are )?in (?:all|every)", re.I)

_HBOND = re.compile(r"(?<![a-z])hydrogen bond(?:ing|s)?(?![a-z])", re.I)
_RANKING = re.compile(
    r"(?<![a-z])(?:stronger than|weaker than|strongest|weakest|stronger or weaker)"
    r"(?![a-z])", re.I)
_NOT_MAKE = re.compile(r"comparison does the framework NOT make")

_OTHER_TOPICS = re.compile(
    r"(?<![a-z])(?:melting point|boiling point|vapor pressure|solubility|soluble|"
    r"miscible|dissolves?)(?![a-z])", re.I)

_FIGURE = re.compile(
    r"(?<![a-z])(?:diagram|figure|the picture|shown above|shown below|pictured)(?![a-z])",
    re.I)


def no_missing_subpoint_material(module):
    """The gap left by the three missing sub-points stays unfilled."""
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            hit = _MISSING_MATERIAL.search(text)
            assert not hit, (
                f"{code} q{i}: invokes {hit.group(0)!r}, which belongs to the sub-points "
                f"missing from this CED's text layer -- {text[:70]!r}"
            )
            hit = _ALL_SUBSTANCES.search(text)
            assert not hit, (
                f"{code} q{i}: claims dispersion forces act in all substances, which this "
                f"source does not state -- {text[:70]!r}"
            )
    print(f"OK  {code} source: nothing fills the three sub-points missing from the CED's "
          "text layer; no item invokes polarizability or molar mass.")


def no_unstated_ranking(module):
    """Hydrogen bonding is ranked against nothing, so no key may rank it."""
    code = module.TOPIC[0]
    exempt = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]]
        # The item counts as ranking hydrogen bonding if the KEY ranks anything and
        # hydrogen bonding is what the item is about -- looking only inside the key
        # for the words "hydrogen bond" missed a key reading "an interaction stronger
        # than any ion-dipole force" under a stem that had already named it.
        about_hbond = _HBOND.search(key) or _HBOND.search(item["q"])
        if about_hbond and _RANKING.search(key):
            assert _NOT_MAKE.search(item["q"]), (
                f"{code} q{i}: the keyed choice ranks hydrogen bonding by strength, which "
                f"EK 3.1.A.4 never does -- {key[:70]!r}"
            )
            exempt += 1
    assert exempt == 1, (
        f"{code}: {exempt} items name a hydrogen-bonding ranking under the "
        "'comparison the framework does NOT make' stem; exactly one should"
    )
    print(f"OK  {code} hedge: no keyed choice ranks hydrogen bonding against another force, "
          "and exactly one item exists to point out that the framework never does.")


def no_other_topics(module):
    """Stems and KEYS only. A rejected option may name a macroscopic property --
    "measure the boiling point" is a real thing a student might wrongly reach for
    where EK 3.1.A.3 asks for a qualitative account, and banning it from the
    distractors too would delete a good wrong answer rather than a defect."""
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for where, text in (("stem", item["q"]),
                            ("keyed choice", item["choices"][item["ans"]])):
            hit = _OTHER_TOPICS.search(text)
            assert not hit, (
                f"{code} q{i}: the {where} rests on {hit.group(0)!r}, which is topic 3.2's "
                f"or 3.10's material -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: no stem or key rests on a macroscopic property or on "
          "solubility, which topics 3.2 and 3.10 own.")


def no_figure_language(module):
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{code} q{i}: refers to {hit.group(0)!r}, which the bank cannot show -- "
                f"{text[:70]!r}"
            )
    print(f"OK  {code} figures: interacting species are described in words or tabulated by "
          "type, never drawn.")


CLAIMS = [
 ("temporary, fluctuating dipoles",
  "EK 3.1.A.1, verbatim: London dispersion forces are a result of the Coulombic interactions between temporary, fluctuating dipoles."),
 ("often the strongest net intermolecular force",
  "EK 3.1.A.1, verbatim: London dispersion forces are often the strongest net intermolecular force between large molecules. The hedge 'often' is the framework's own."),
 ("should not be used synonymously",
  "EK 3.1.A.1's third sub-point: the term London dispersion forces should not be used synonymously with the term van der Waals forces."),
 ("Additional interactions with other chemical species",
  "EK 3.1.A.2, verbatim: the dipole moment of a polar molecule leads to additional interactions with other chemical species."),
 ("Between polar molecules",
  "EK 3.1.A.2's second sub-point: dipole-dipole interactions are present between polar molecules. Interactions within one molecule are intramolecular and belong to topic 2.2."),
 ("magnitudes of the dipoles and on their relative orientation",
  "EK 3.1.A.2's second sub-point names both factors: the interaction strength depends on the magnitudes of the dipoles and their relative orientation."),
 ("act in addition to London dispersion forces",
  "EK 3.1.A.2's second sub-point gives exactly this reason for polar-polar interactions typically exceeding nonpolar-nonpolar ones at comparable size."),
 ("Between ions and polar molecules",
  "EK 3.1.A.2's third sub-point: ion-dipole forces of attraction are present between ions and polar molecules."),
 ("Ion-dipole forces tend to be the stronger",
  "EK 3.1.A.2's third sub-point: these tend to be stronger than dipole-dipole forces. The framework does make this comparison, hedged with 'tend'."),
 ("Qualitatively, by considering the sign of the partial charges",
  "EK 3.1.A.3: the relative strength and orientation dependence can be understood qualitatively by considering the sign of the partial charges responsible for the molecular dipole moment."),
 ("Nitrogen, oxygen or fluorine",
  "EK 3.1.A.4 names those three atoms twice in one sentence. The framework's definition is a list of three elements, not a general electronegativity rule."),
 ("negative end of a dipole",
  "EK 3.1.A.4: the hydrogen atoms are attracted to the NEGATIVE end of a dipole formed by the electronegative atom. Swapping the sign reverses the interaction."),
 ("different molecule, or in a different part of the same molecule",
  "EK 3.1.A.4 allows both in its own sentence, so restricting the definition to either case alone drops half of it."),
 ("strong type of intermolecular interaction",
  "EK 3.1.A.4 opens with exactly that phrase, which places hydrogen bonding among the forces BETWEEN molecules rather than among the bonds within them."),
 ("between different molecules or between different regions of the same large biomolecule",
  "EK 3.1.A.5 states both cases in one sentence."),
 ("Pair 1",
  "EK 3.1.A.2's third sub-point places ion-dipole forces between ions and polar molecules. Recomputed in q16, which asserts exactly one tabulated pair is of that kind."),
 ("Pair 2",
  "EK 3.1.A.2's second sub-point places dipole-dipole interactions between polar molecules. Recomputed in q17, which asserts exactly one tabulated pair is of that kind."),
 ("Pair 1",
  "EK 3.1.A.2's third sub-point says ion-dipole forces tend to be stronger than dipole-dipole forces. Recomputed in q18, which identifies both named cases from the table before comparing them."),
 ("Exactly two",
  "EK 3.1.A.2 names a force only for a pair containing a polar molecule with an ion or with another polar molecule. Recomputed in q19 by classifying every tabulated pair."),
 ("polar one, because dipole-dipole interactions act in addition",
  "EK 3.1.A.2's second sub-point states the comparison and its reason together. Recomputed in q20, which asserts the table really does hold one polar and one nonpolar substance at comparable size."),
 ("depends on the relative orientation of the dipoles",
  "EK 3.1.A.2's second sub-point names relative orientation as one of the two things the strength depends on, and EK 3.1.A.3 makes that dependence something to understand from the partial charges."),
 ("With an ion, or with an adjacent dipole",
  "EK 3.1.A.3 names both, and those two cases are exactly the ion-dipole and dipole-dipole forces the same statement is about."),
 ("definition names hydrogen bonded to nitrogen, oxygen or fluorine",
  "EK 3.1.A.4 defines hydrogen bonding for hydrogen covalently bonded to N, O and F and names no other element, so a carbon-bound hydrogen falls outside the definition as written."),
 ("same chemical species, and when they are of two different chemical species",
  "LO 3.1.A states its two cases in exactly those words as sub-points i and ii."),
 ("hydrogen bonding is stronger or weaker than an ion-dipole force",
  "EK 3.1.A.4 calls hydrogen bonding a strong type of intermolecular interaction and ranks it against nothing, while EK 3.1.A.1 and EK 3.1.A.2 make each of the four rejected comparisons explicitly."),
 ("London dispersion forces that the same statement says these interactions act in addition to",
  "EK 3.1.A.2's second sub-point spells out what the addition is to. Covalent bonds are intramolecular, so they are not what an intermolecular force is added to."),
 ("They are temporary and fluctuating",
  "EK 3.1.A.1 describes the dipoles behind dispersion forces in exactly those two words, while EK 3.1.A.2 speaks of the dipole moment OF a polar molecule as a property of the molecule."),
 ("between different regions of the same large biomolecule",
  "EK 3.1.A.5 allows exactly this, and EK 3.1.A.4 makes the same allowance for hydrogen bonding within a single molecule."),
 ("holding without exception in every case",
  "EK 3.1.A.2's third sub-point says ion-dipole forces TEND to be stronger, which asserts a tendency rather than an exceptionless rule; the rejected statements are each part of what it does assert."),
 ("two names for the same thing",
  "EK 3.1.A.1's third sub-point says the two terms should NOT be used synonymously, which contradicts the keyed statement; the four rejected statements are each stated in EK 3.1.A.1, 3.1.A.2 or 3.1.A.4."),
]


# ------------------------------------------------------------ negative controls

def _retable(mod, i, label_, **cells):
    t = mod.QUESTIONS[i - 1]["table"]
    heads = list(t["headers"])
    rows = []
    for row in t["rows"]:
        row = list(row)
        if str(row[0]) == label_:
            for header, value in cells.items():
                row[heads.index(header)] = value
        rows.append(row)
    mod.QUESTIONS[i - 1]["table"] = dict(headers=heads, rows=rows)


def _second_ion_dipole_pair(mod, cl):
    """Make a second tabulated pair an ion-dipole case, so the item has two answers."""
    _retable(mod, 16, "Pair 4", **{SECOND: POLAR})


def _no_dipole_dipole_pair(mod, cl):
    """Remove the only two-polar pair, so the dipole-dipole item has no answer."""
    _retable(mod, 17, "Pair 2", **{SECOND: NONPOLAR})


def _neither_count_changes(mod, cl):
    """Change how many pairs fall under neither sub-point."""
    _retable(mod, 19, "Pair 3", **{FIRST: ION, SECOND: POLAR})


def _both_substances_polar(mod, cl):
    """Break the polar-against-nonpolar premise of the comparison item."""
    _retable(mod, 20, "Substance K", **{POLARITY: "polar"})


def _sizes_stop_being_comparable(mod, cl):
    """Drop the comparable-size condition EK 3.1.A.2 attaches to the comparison."""
    _retable(mod, 20, "Substance K", **{SIZE: "much larger than that of Substance J"})


def _unknown_species_kind(mod, cl):
    """A cell the classifier cannot read must fail loudly rather than be skipped."""
    _retable(mod, 16, "Pair 3", **{FIRST: "a slightly polar molecule"})


def _polarizability_creeps_in(mod, cl):
    mod.QUESTIONS[0]["q"] = ("Dispersion forces grow with the polarizability of a molecule. "
                             "What do they result from?")
    no_missing_subpoint_material(mod)


def _all_substances_claim(mod, cl):
    ch = list(mod.QUESTIONS[1]["choices"])
    ch[0] = "Dispersion forces are present in all substances without exception"
    mod.QUESTIONS[1]["choices"] = ch
    cl[1] = ("present in all substances", cl[1][1])
    no_missing_subpoint_material(mod)


def _hydrogen_bond_ranked_in_a_key(mod, cl):
    ch = list(mod.QUESTIONS[13]["choices"])
    ch[0] = "As an interaction stronger than any ion-dipole force"  # stem names it
    mod.QUESTIONS[13]["choices"] = ch
    cl[13] = ("stronger than any ion-dipole force", cl[13][1])
    no_unstated_ranking(mod)


def _macroscopic_property(mod, cl):
    """Put it in the STEM, since the gate deliberately permits it in a distractor."""
    mod.QUESTIONS[2]["q"] = "Which term describes the boiling point of a molecular liquid?"
    no_other_topics(mod)


def _figure_language(mod, cl):
    mod.QUESTIONS[3]["q"] = "In the diagram, what does a polar molecule's dipole lead to?"
    no_figure_language(mod)


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, extra=[
        ("a second tabulated pair made an ion-dipole case", _second_ion_dipole_pair),
        ("the only two-polar pair removed", _no_dipole_dipole_pair),
        ("the count of pairs falling under neither sub-point changed",
         _neither_count_changes),
        ("both tabulated substances made polar, breaking the comparison",
         _both_substances_polar),
        ("the comparable-size condition dropped from the comparison",
         _sizes_stop_being_comparable),
        ("a species kind the classifier cannot read", _unknown_species_kind),
        ("polarizability, which this CED's text layer does not contain, moved into a stem",
         _polarizability_creeps_in),
        ("a claim that dispersion forces act in all substances", _all_substances_claim),
        ("a keyed choice ranking hydrogen bonding against another force",
         _hydrogen_bond_ranked_in_a_key),
        ("a macroscopic property, which is topic 3.2's", _macroscopic_property),
        ("a stem pointing at a diagram the bank cannot show", _figure_language),
    ])

no_missing_subpoint_material(M)
no_unstated_ranking(M)
no_other_topics(M)
no_figure_language(M)
hn.audit(M, CLAIMS, TABLE_CHECKS)
