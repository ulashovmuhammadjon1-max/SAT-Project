"""Key audit for AP CHEMISTRY 3.2 Properties of Solids.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. The eight table items are recomputed from a
transcription of what the CED actually says about each of the four solid types.

WHAT THE KEYS REST ON
---------------------
EK 3.2.A.1  Many properties of liquids and solids are determined by the
            strengths AND TYPES of intermolecular forces; vapor pressure and
            boiling point are DIRECTLY related to interaction strength because
            those interactions are overcome completely on vaporizing; melting
            points only TEND to correlate, and the relations can be more subtle
            because the interactions are merely rearranged.  (items 1, 2, 22)
EK 3.2.A.2  Particulate-level representations showing multiple interacting
            species are useful for communicating or understanding how
            intermolecular interactions establish macroscopic properties.
                                                                    (item 3)
EK 3.2.A.3  Ionic solids: low vapor pressure, high melting and boiling points;
            brittle because like charges repel when a layer slides; conduct only
            when the ions are mobile.         (items 4, 5, 6, 24, 27, 28)
EK 3.2.A.4  Covalent network solids: a 3-D network or layers of 2-D networks;
            only from nonmetals and metalloids; elemental or binary; high
            melting points; 3-D networks rigid and hard because the bond angles
            are fixed; graphite soft because its layers slide.
                                          (items 7, 8, 9, 10, 11, 12, 27, 30)
EK 3.2.A.5  Molecular solids: distinct covalently bonded molecules held by
            relatively weak intermolecular forces; low melting point; do NOT
            conduct, their valence electrons being tightly held; sometimes very
            large molecules or polymers.      (items 13, 14, 15, 16, 25, 26)
EK 3.2.A.6  Metallic solids: good conductors of electricity and heat from free
            valence electrons; malleable and ductile because the cores rearrange
            easily; interstitial atoms make the lattice more rigid; alloys
            retain a sea of mobile electrons.  (items 17, 18, 19, 20, 23, 29)
EK 3.2.A.7  In large biomolecules, functionality and properties depend strongly
            on shape, which noncovalent interactions largely dictate. (item 21)

THE SILENCE IS PART OF THE CONTENT. EK 3.2.A.4 describes covalent network solids
at length -- bonding, constituent elements, melting point, rigidity, hardness,
and why graphite is soft -- and never once says whether they conduct
electricity. ``CONDUCTION`` below transcribes what the framework says for each
of the four types, INCLUDING the ``None`` for covalent network, and every
conduction item is checked against it. Item 30 keys on that silence directly.

THE MELTING-POINT HEDGE. ``no_melting_point_as_a_direct_measure`` asserts that
no keyed choice calls a melting point directly related to interaction strength;
EK 3.2.A.1 reserves "directly related" for vapor pressure and boiling point and
explicitly says the melting relations can be more subtle.

NEGATIVE CONTROL: ``python3 verify_h3_2.py --selftest``.
"""
import re
import sys

import h_chem_notation as hn
import h3_2 as M

TYPE = "Type of solid"

# Transcribed from EK 3.2.A.3, 3.2.A.4, 3.2.A.5 and 3.2.A.6. ``None`` means the
# framework makes no statement -- which is itself keyed, in item 30.
CONDUCTION = {"ionic": "only when molten or dissolved",
              "covalent network": None,
              "molecular": "does not conduct",
              "metallic": "good conductor"}

MELTING = {"ionic": "high",
           "covalent network": "high",
           "molecular": "low",
           "metallic": None}

BRITTLE = {"ionic": True, "covalent network": False, "molecular": False,
           "metallic": False}

MALLEABLE = {"ionic": False, "covalent network": False, "molecular": False,
             "metallic": True}

COUNTWORD = {0: "None of them", 1: "Exactly one", 2: "Exactly two",
             3: "Exactly three", 4: "All four"}

cg = hn.cg


# ----------------------------------------------------------------- helpers

def solids(table):
    """[(label, type)], with every tabulated type required to be one this module knows."""
    heads = list(table["headers"])
    j = heads.index(TYPE)
    out = []
    for row in table["rows"]:
        kind = str(row[j]).strip().lower()
        assert kind in CONDUCTION, (
            f"row {row[0]!r} names the type {kind!r}, which is not one of the four the "
            f"framework describes: {sorted(CONDUCTION)}"
        )
        out.append((str(row[0]), kind))
    return out


def the_one(rows, predicate, what):
    """The single tabulated label satisfying ``predicate``, refused if not unique."""
    hits = [lab for lab, kind in rows if predicate(kind)]
    assert len(hits) == 1, (
        f"{len(hits)} tabulated types are {what}: {hits}; the item needs exactly one"
    )
    return hits[0]


# ------------------------------------------------------------ table questions

def q23(t, item):
    rows = solids(t)
    lab = the_one(rows, lambda k: CONDUCTION[k] == "good conductor",
                  "described as good conductors")
    hn.keyed(item, lab)
    return (f"of the four tabulated types only {lab}'s is the one EK 3.2.A.6 calls a good "
            "conductor of electricity and heat")


def q24(t, item):
    rows = solids(t)
    lab = the_one(rows, lambda k: CONDUCTION[k] == "only when molten or dissolved",
                  "said to conduct only when mobile")
    hn.keyed(item, lab)
    return (f"of the four tabulated types only {lab}'s carries EK 3.2.A.3's condition that "
            "conduction requires the ions to be mobile")


def q25(t, item):
    rows = solids(t)
    lab = the_one(rows, lambda k: CONDUCTION[k] == "does not conduct",
                  "said not to conduct")
    hn.keyed(item, lab)
    return (f"of the four tabulated types only {lab}'s is the one EK 3.2.A.5 says does not "
            "conduct electricity")


def q26(t, item):
    rows = solids(t)
    lab = the_one(rows, lambda k: MELTING[k] == "low", "given a low melting point")
    hn.keyed(item, lab)
    return (f"of the four tabulated types only {lab}'s is given a low melting point, by EK "
            "3.2.A.5, while two others are given high ones")


def q27(t, item):
    rows = solids(t)
    high = [lab for lab, kind in rows if MELTING[kind] == "high"]
    hn.keyed(item, COUNTWORD[len(high)])
    return (f"{len(high)} of the {len(rows)} tabulated types are given a high melting point "
            f"by the framework, namely {', '.join(high) or 'none'}")


def q28(t, item):
    rows = solids(t)
    lab = the_one(rows, lambda k: BRITTLE[k], "described as brittle")
    hn.keyed(item, lab)
    return (f"of the four tabulated types only {lab}'s is called brittle, by EK 3.2.A.3, "
            "and for a stated reason about sliding layers")


def q29(t, item):
    rows = solids(t)
    lab = the_one(rows, lambda k: MALLEABLE[k], "described as malleable and ductile")
    other = the_one(rows, lambda k: BRITTLE[k], "described as brittle")
    assert lab != other, "the same type cannot be both the malleable and the brittle one"
    hn.keyed(item, lab)
    return (f"of the four tabulated types only {lab}'s is called malleable and ductile, "
            f"while {other}'s is given the opposite behavior")


def q30(t, item):
    rows = solids(t)
    lab = the_one(rows, lambda k: CONDUCTION[k] is None,
                  "left without any conduction statement")
    hn.keyed(item, lab)
    return (f"the framework states a conduction behavior for three of the four tabulated "
            f"types and says nothing at all for {lab}'s")


TABLE_CHECKS = {23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29,
                30: q30}


# ------------------------------------------------------- module-specific gates

_MELTING_DIRECT = re.compile(
    r"melting point[a-z ,]{0,40}(?:directly related|direct measure|exactly as boiling)",
    re.I)
_FIGURE = re.compile(
    r"(?<![a-z])(?:diagram|figure|the picture|shown above|shown below|pictured|"
    r"representation shown)(?![a-z])", re.I)


def no_melting_point_as_a_direct_measure(module):
    """EK 3.2.A.1 reserves 'directly related' for vapor pressure and boiling point."""
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]]
        hit = _MELTING_DIRECT.search(key)
        assert not hit, (
            f"{code} q{i}: the keyed choice treats a melting point as directly related to "
            f"interaction strength, which EK 3.2.A.1 explicitly hedges -- {key[:70]!r}"
        )
    print(f"OK  {code} hedge: no keyed choice makes a melting point a direct measure of "
          "interaction strength, which EK 3.2.A.1 reserves for vapor pressure and boiling "
          "point.")


def conduction_claims_match_the_framework(module):
    """Every conduction key agrees with the transcribed statements, silence included."""
    code = module.TOPIC[0]
    checked = 0
    for i in (23, 24, 25, 30):
        item = module.QUESTIONS[i - 1]
        table = item.get("table")
        assert table, f"{code} q{i}: expected a conduction item carrying the solids table"
        rows = solids(table)
        kinds = {lab: kind for lab, kind in rows}
        key = item["choices"][item["ans"]]
        named = [lab for lab in kinds if cg.contains_phrase(key, lab)]
        assert len(named) == 1, (
            f"{code} q{i}: the keyed choice names {len(named)} tabulated solids"
        )
        checked += 1
    assert set(CONDUCTION.values()) == {"good conductor", None, "does not conduct",
                                        "only when molten or dissolved"}, (
        "the transcribed conduction statements no longer match the four the CED makes"
    )
    silent = [k for k, v in CONDUCTION.items() if v is None]
    assert silent == ["covalent network"], (
        f"the framework's silence should fall on covalent network solids alone, not {silent}"
    )
    print(f"OK  {code} source: all {checked} conduction item(s) key to a tabulated type, and "
          "the transcribed statements keep the framework's one silence intact.")


def no_figure_language(module):
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{code} q{i}: refers to {hit.group(0)!r}, which the bank cannot show -- "
                f"{text[:70]!r}"
            )
    print(f"OK  {code} figures: the particulate-representation item asks what such a "
          "representation is for, never asks one to be read.")


CLAIMS = [
 ("overcome completely when the substance vaporizes",
  "EK 3.2.A.1 gives exactly this reason for vapor pressure and boiling point being directly related to interaction strength; rearrangement rather than removal is what the same sentence says happens in melting."),
 ("tend to correlate with it, but the relations can be more subtle",
  "EK 3.2.A.1 hedges melting points deliberately, because the interactions are only rearranged in melting. The direct relation is reserved for vapor pressure and boiling point."),
 ("how intermolecular interactions help to establish macroscopic properties",
  "EK 3.2.A.2 states the purpose of particulate-level representations in those words, and specifies that they show multiple interacting chemical species."),
 ("Low vapor pressures, high melting points and high boiling points",
  "EK 3.2.A.3, verbatim in substance: due to strong interactions between ions, ionic solids tend to have low vapor pressures, high melting points, and high boiling points."),
 ("repulsion of like charges caused when one layer slides",
  "EK 3.2.A.3 gives that reason for brittleness in its own words. Ease of rearrangement is EK 3.2.A.6's explanation for the opposite property in metals."),
 ("Only when the ions are mobile",
  "EK 3.2.A.3: they conduct electricity only when the ions are mobile, as when the ionic solid is melted or dissolved in water or another solvent."),
 ("three-dimensional network or into layers of two-dimensional networks",
  "EK 3.2.A.4 names both arrangements, with diamond and graphite as its own examples."),
 ("Only from nonmetals and metalloids",
  "EK 3.2.A.4 states the restriction directly. A metal with a nonmetal is EK 2.1.A.4's ionic generalization instead."),
 ("Elemental, or binary compounds",
  "EK 3.2.A.4 gives both, with diamond and graphite as the elemental examples and silicon dioxide and silicon carbide as the binary ones."),
 ("strong covalent interactions",
  "EK 3.2.A.4: due to the strong covalent interactions, covalent solids have high melting points. Weak intermolecular forces are EK 3.2.A.5's reason for the opposite."),
 ("covalent bond angles are fixed",
  "EK 3.2.A.4 gives that reason for three-dimensional network solids being rigid and hard."),
 ("Adjacent layers can slide past each other",
  "EK 3.2.A.4 attributes graphite's softness to exactly this, rather than to any weakness in the covalent bonds."),
 ("Distinct, individual units of covalently bonded molecules",
  "EK 3.2.A.5, verbatim in substance. The word 'distinct' is what separates a molecular solid from EK 3.2.A.4's continuous network."),
 ("relatively weak intermolecular forces present between the molecules",
  "EK 3.2.A.5 gives that reason for the low melting point; the covalent bonds within each molecule are not what melting overcomes."),
 ("tightly held within the covalent bonds and the lone pairs",
  "EK 3.2.A.5 gives that reason for molecular solids not conducting. Immobile ions and delocalized electrons are the other two types' cases."),
 ("sometimes composed of very large molecules or polymers",
  "EK 3.2.A.5 closes with that sentence, which keeps polymers inside the molecular category."),
 ("presence of free valence electrons",
  "EK 3.2.A.6 gives that reason for metallic solids conducting electricity and heat, which is the sea of electrons EK 2.4.A.1 describes."),
 ("ease with which the metal cores can rearrange their structure",
  "EK 3.2.A.6 gives that reason for malleability and ductility; EK 3.2.A.3's sliding-layer repulsion produces the opposite behavior in an ionic solid."),
 ("more rigid, decreasing malleability and ductility",
  "EK 3.2.A.6 states the effect of interstitial atoms in exactly those terms, while adding that the alloy nevertheless remains conducting."),
 ("retain a sea of mobile electrons and so remain conducting",
  "EK 3.2.A.6 closes with that sentence. Conducting only when molten is EK 3.2.A.3's ionic case."),
 ("shape of the molecule, which is largely dictated by noncovalent interactions",
  "EK 3.2.A.7 states it in those words, so the noncovalent interactions reach the properties through the shape."),
 ("strengths and types of intermolecular forces",
  "EK 3.2.A.1 opens by naming both, so dropping either half understates what the framework says determines the properties."),
 ("Solid 4",
  "EK 3.2.A.6 calls metallic solids good conductors of electricity and heat. Recomputed in q23 against the transcribed statements for all four types."),
 ("Solid 1",
  "EK 3.2.A.3 makes conduction in an ionic solid conditional on the ions being mobile. Recomputed in q24."),
 ("Solid 3",
  "EK 3.2.A.5 says molecular solids do not conduct electricity. Recomputed in q25."),
 ("Solid 3",
  "EK 3.2.A.5 gives molecular solids a low melting point. Recomputed in q26 against the melting statements for all four types."),
 ("Exactly two",
  "EK 3.2.A.3 and EK 3.2.A.4 each state a high melting point, EK 3.2.A.5 a low one, and EK 3.2.A.6 none at all. Recomputed in q27."),
 ("Solid 1",
  "EK 3.2.A.3 calls ionic solids brittle, for a stated reason about sliding layers. Recomputed in q28."),
 ("Solid 4",
  "EK 3.2.A.6 calls metallic solids malleable and ductile. Recomputed in q29, which also asserts the brittle type is a different one."),
 ("Solid 2",
  "EK 3.2.A.4 describes covalent network solids at length and never states whether they conduct, while the other three types each carry a conduction statement. Recomputed in q30 from the transcription, whose ``None`` records that silence."),
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


def _two_metallic_rows(mod, cl):
    """Two metallic rows leave the good-conductor item without a unique answer."""
    _retable(mod, 23, "Solid 1", **{TYPE: "metallic"})


def _no_ionic_row(mod, cl):
    """Remove the only ionic row, so the conducts-when-molten item has no answer."""
    _retable(mod, 24, "Solid 1", **{TYPE: "molecular"})


def _high_melting_count_changes(mod, cl):
    """Change how many tabulated types carry a high melting point."""
    _retable(mod, 27, "Solid 2", **{TYPE: "metallic"})


def _brittle_and_malleable_collapse(mod, cl):
    """Make the brittle and malleable types the same row."""
    _retable(mod, 29, "Solid 1", **{TYPE: "metallic"})


def _silence_filled_in(mod, cl):
    """Replace the covalent network row, so no tabulated type is left silent."""
    _retable(mod, 30, "Solid 2", **{TYPE: "metallic"})


def _unknown_solid_type(mod, cl):
    """A type the transcription does not cover must fail loudly, not be skipped."""
    _retable(mod, 23, "Solid 2", **{TYPE: "amorphous"})


def _melting_point_made_direct(mod, cl):
    ch = list(mod.QUESTIONS[1]["choices"])
    # NOT a copy of an existing distractor: the first draft of this control reused
    # one verbatim and the run raised "duplicate choice strings" instead, which
    # proved the structural check works and said nothing about this gate.
    ch[0] = ("They are related to it so closely that a melting point is a direct measure "
             "of interaction strength")
    mod.QUESTIONS[1]["choices"] = ch
    cl[1] = ("melting point is a direct measure", cl[1][1])
    no_melting_point_as_a_direct_measure(mod)


def _figure_language(mod, cl):
    mod.QUESTIONS[2]["q"] = "In the representation shown, what is being communicated?"
    no_figure_language(mod)


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, extra=[
        ("a second metallic row, leaving the conductor item without a unique answer",
         _two_metallic_rows),
        ("the only ionic row removed from under its key", _no_ionic_row),
        ("the count of types with a high melting point changed",
         _high_melting_count_changes),
        ("the brittle and the malleable type collapsed into one",
         _brittle_and_malleable_collapse),
        ("the framework's one silence filled in, leaving the silence item no answer",
         _silence_filled_in),
        ("a solid type the transcription does not cover", _unknown_solid_type),
        ("a keyed choice making a melting point a direct measure of interaction strength",
         _melting_point_made_direct),
        ("a stem pointing at a representation the bank cannot show", _figure_language),
    ])

no_melting_point_as_a_direct_measure(M)
conduction_claims_match_the_framework(M)
no_figure_language(M)
hn.audit(M, CLAIMS, TABLE_CHECKS)
