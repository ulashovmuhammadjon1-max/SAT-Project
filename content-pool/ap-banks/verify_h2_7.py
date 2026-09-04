"""Key audit for AP CHEMISTRY 2.7 VSEPR and Hybridization.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Eight stem items and four table items are
recomputed here against EK 2.7.A.3's own printed correspondence.

WHAT THE KEYS REST ON
---------------------
EK 2.7.A.1  VSEPR theory uses the Coulombic repulsion between electrons as a
            basis for predicting the arrangement of electron pairs around a
            central atom.                                       (items 1, 2)
EK 2.7.A.2  Both Lewis diagrams and VSEPR theory must be used for predicting
            electronic and structural properties, including molecular geometry,
            bond angles, relative bond energies based on bond order, relative
            bond lengths, presence of a dipole moment, and hybridization.
                                                    (items 3, 24, 25, 26)
EK 2.7.A.3  Hybridization and hybrid atomic orbital describe the arrangement of
            electrons around a central atom; sp gives 180 degrees, sp2 gives 120
            degrees, sp3 gives 109.5 degrees.
                       (items 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 28, 29, 30)
EK 2.7.A.4  Bond formation is associated with orbital overlap; multiple bonds
            give both sigma and pi bonds; overlap is stronger in sigma, so sigma
            bonds have greater bond energy; a pi bond prevents rotation and
            leads to geometric isomers.             (items 14, 15, 16, 17, 18, 19)
Exclusions  Derivation and depiction of hybrid orbitals, d-orbital
            hybridization, and molecular orbital theory are all excluded; the
            course includes the sigma/pi distinction, VSEPR for shapes, and the
            sp nomenclature; beyond four pairs only the SHAPE is required.
                                                    (items 20, 21, 22, 23, 27)

THE ONE NUMERICAL SENTENCE IN UNIT 2. EK 2.7.A.3 prints three
hybridization-to-angle pairings and nothing else in the unit prints a number
like that, so ``ANGLE`` below is transcribed from that sentence and thirteen
items are checked against it -- in both directions, and including the two
difference items, whose answers are arithmetic on those three printed values.

WHAT IS DELIBERATELY NOT KEYED. The framework never states how many regions of
electron density produce which hybridization, nor which counts of bonding and
lone pairs produce which geometry name. Supplying either from a textbook and
keying answers to it is what SOCIAL_BRIEF.md forbids, so
``no_unlicensed_structure_rule`` asserts that no stem or keyed choice invokes
regions of electron density, electron domains or a steric number, and that no
KEYED choice names one of the framework's molecular geometries -- because
naming one would mean predicting a geometry the CED gives no rule for.

``geometry_names_are_the_frameworks`` checks the one recognition item against
the CED's own list of eleven geometries: its key must be absent from that list
and every one of its rejected options present in it.

NEGATIVE CONTROL: ``python3 verify_h2_7.py --selftest``.
"""
import re
import sys

import h_chem_notation as hn
import h2_7 as M

HYB = "Hybridization stated"
ANG = "Ideal bond angle stated"

# EK 2.7.A.3, transcribed. These three pairings are the only numerical
# correspondence the unit prints, and every angle key in the module is checked
# against this dict rather than against anything remembered.
ANGLE = {"sp": 180.0, "sp2": 120.0, "sp3": 109.5}

# EK 2.7.A.2 (i), the framework's own list of molecular geometries.
GEOMETRIES = ["linear", "trigonal planar", "tetrahedral", "trigonal pyramidal",
              "bent", "trigonal bipyramidal", "seesaw", "t-shaped", "octahedral",
              "square pyramidal", "square planar"]

_HYB_SPAN = re.compile(r"\\\(\s*sp(?:\^\{(\d)\})?\s*\\\)")
_ANGLE_IN_STEM = re.compile(r"are (\d+(?:\.\d+)?) degrees")

cg = hn.cg


# ----------------------------------------------------------------- helpers

def label(match):
    """'sp', 'sp2' or 'sp3' from a matched hybridization span."""
    return "sp" + (match.group(1) or "")


def hybridizations(text):
    """Every hybridization label the text states, in order."""
    return [label(m) for m in _HYB_SPAN.finditer(text)]


def angle_of(hyb):
    assert hyb in ANGLE, f"EK 2.7.A.3 prints no angle for {hyb!r}"
    return ANGLE[hyb]


def degrees(value):
    return f"{value:g} degrees"


# --------------------------------------------------------- stem-numeric checks

def hyb_to_angle(item):
    """The stem states a hybridization; the key must state EK 2.7.A.3's angle for it."""
    hybs = hybridizations(item["q"])
    assert len(hybs) == 1, f"the stem states {len(hybs)} hybridizations, expected one: {hybs}"
    value = angle_of(hybs[0])
    hn.keyed(item, degrees(value))
    return (f"EK 2.7.A.3 pairs {hybs[0]} with {degrees(value)}, which is what the keyed "
            "choice states")


def angle_to_hyb(item):
    """The stem states an angle; the key must name EK 2.7.A.3's hybridization for it."""
    hit = _ANGLE_IN_STEM.search(item["q"])
    assert hit, f"the stem states no angle this check can read: {item['q'][:80]!r}"
    value = float(hit.group(1))
    matches = [h for h, a in ANGLE.items() if a == value]
    assert len(matches) == 1, (
        f"{value} degrees matches {len(matches)} of EK 2.7.A.3's printed angles: {matches}"
    )
    hyb = matches[0]
    anchor = "is \\( sp \\) hybridized" if hyb == "sp" else f"sp^{{{hyb[2]}}} hybridized"
    hn.keyed(item, anchor)
    return (f"EK 2.7.A.3 pairs {degrees(value)} with {hyb}, and no other printed angle "
            "takes that value")


def a30(item):
    """Both hybridizations come from the stem; the keyed difference is their gap."""
    hybs = hybridizations(item["q"])
    assert len(hybs) == 2, f"the stem states {len(hybs)} hybridizations, expected two: {hybs}"
    gap = abs(angle_of(hybs[0]) - angle_of(hybs[1]))
    others = {abs(ANGLE[a] - ANGLE[b]) for a in ANGLE for b in ANGLE if a != b}
    assert gap in others, "the computed gap is not one of the framework's own differences"
    hn.keyed(item, degrees(gap))
    return (f"EK 2.7.A.3 gives {hybs[0]} {degrees(angle_of(hybs[0]))} and {hybs[1]} "
            f"{degrees(angle_of(hybs[1]))}, a difference of {degrees(gap)}")


ARITH = {4: hyb_to_angle, 5: hyb_to_angle, 6: hyb_to_angle,
         7: angle_to_hyb, 8: angle_to_hyb, 9: angle_to_hyb,
         28: hyb_to_angle, 30: a30}


# ------------------------------------------------------------ table questions

def _rows(table):
    """[(label, hybridization)] from a table whose second column is a hybridization."""
    heads = list(table["headers"])
    j = heads.index(HYB)
    out = []
    for row in table["rows"]:
        hybs = hybridizations(str(row[j]))
        assert len(hybs) == 1, f"row {row[0]!r} states {len(hybs)} hybridizations"
        out.append((str(row[0]), hybs[0]))
    return out


def q10(t, item):
    heads = list(t["headers"])
    j = heads.index(ANG)
    bad = []
    for (lab, hyb), row in zip(_rows(t), t["rows"]):
        stated = _ANGLE_IN_STEM.search("are " + str(row[j]))
        assert stated, f"cannot read the tabulated angle {row[j]!r}"
        if float(stated.group(1)) != angle_of(hyb):
            bad.append(lab)
    assert len(bad) == 1, (
        f"{len(bad)} tabulated rows disagree with EK 2.7.A.3: {bad}; the item needs "
        "exactly one"
    )
    hn.keyed(item, bad[0])
    return (f"checking each tabulated pairing against EK 2.7.A.3 leaves exactly one "
            f"disagreement, {bad[0]}, and the other three rows match the framework")


def q11(t, item):
    rows = [(lab, angle_of(h)) for lab, h in _rows(t)]
    ordered = sorted(rows, key=lambda r: -r[1])
    assert ordered[0][1] > ordered[1][1], "two tabulated atoms tie for the largest angle"
    hn.keyed(item, ordered[0][0])
    return (f"{ordered[0][0]} carries the largest of the tabulated angles at "
            f"{degrees(ordered[0][1])}, read off EK 2.7.A.3")


def q12(t, item):
    rows = [(lab, angle_of(h)) for lab, h in _rows(t)]
    ordered = sorted(rows, key=lambda r: r[1])
    assert ordered[0][1] < ordered[1][1], "two tabulated atoms tie for the smallest angle"
    hn.keyed(item, ordered[0][0])
    return (f"{ordered[0][0]} carries the smallest of the tabulated angles at "
            f"{degrees(ordered[0][1])}, read off EK 2.7.A.3")


def q29(t, item):
    rows = [(lab, angle_of(h)) for lab, h in _rows(t)]
    pairs = [(a, b, abs(a[1] - b[1])) for i, a in enumerate(rows) for b in rows[i + 1:]]
    sixty = [(a[0], b[0]) for a, b, d in pairs if d == 60]
    assert len(sixty) == 1, (
        f"{len(sixty)} tabulated pairs differ by exactly sixty degrees: {sixty}; the item "
        "needs exactly one"
    )
    first, second = sixty[0]
    hn.keyed(item, f"{first} and {second}")
    return (f"of the {len(pairs)} tabulated pairs only {first} and {second} differ by "
            "exactly sixty degrees under EK 2.7.A.3's printed angles")


TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 29: q29}


# ------------------------------------------------------- module-specific gates

_UNLICENSED = re.compile(
    r"(?<![a-z])(?:regions? of electron density|electron domains?|steric number)(?![a-z])",
    re.I)
_GEOMETRY_NAME = re.compile(
    "(?<![a-z])(?:" + "|".join(re.escape(g) for g in GEOMETRIES) + r")(?![a-z])", re.I)
_FIGURE = re.compile(
    r"(?<![a-z])(?:diagram shown|shown above|shown below|the figure|the picture|"
    r"pictured|as drawn above)(?![a-z])", re.I)


def no_unlicensed_structure_rule(module):
    """The CED gives no rule from electron-pair counts to hybridization or geometry.

    So no item may invoke one, and no KEYED choice may name a molecular geometry --
    naming one as the answer would be predicting a geometry the framework supplies no
    rule for. Rejected options may name geometries, which is how the recognition item
    works.
    """
    code = module.TOPIC[0]
    named_in_distractors = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _UNLICENSED.search(text)
            assert not hit, (
                f"{code} q{i}: invokes {hit.group(0)!r}, a rule the framework never states "
                f"-- {text[:70]!r}"
            )
        key = item["choices"][item["ans"]]
        hit = _GEOMETRY_NAME.search(key)
        assert not hit, (
            f"{code} q{i}: the keyed choice names the geometry {hit.group(0)!r}, but the "
            f"framework gives no rule for predicting one -- {key[:70]!r}"
        )
        named_in_distractors += sum(
            1 for j, c in enumerate(item["choices"])
            if j != item["ans"] and _GEOMETRY_NAME.search(c))
    print(f"OK  {code} honesty: no item invokes an electron-domain rule the CED never "
          f"states, and no keyed choice predicts a molecular geometry; {named_in_distractors} "
          "rejected option(s) name one.")


def geometry_names_are_the_frameworks(module):
    """The recognition item is checked against EK 2.7.A.2's own list of eleven."""
    code = module.TOPIC[0]
    hits = [i for i, item in enumerate(module.QUESTIONS, 1)
            if "NOT among the molecular geometries" in item["q"]]
    assert len(hits) == 1, f"{code}: {len(hits)} geometry-recognition items, expected one"
    item = module.QUESTIONS[hits[0] - 1]
    key = item["choices"][item["ans"]].strip().lower()
    assert key not in GEOMETRIES, (
        f"{code} q{hits[0]}: the keyed choice {key!r} IS one of the framework's eleven "
        "geometries, so the item's answer is wrong"
    )
    for j, ch in enumerate(item["choices"]):
        if j == item["ans"]:
            continue
        assert ch.strip().lower() in GEOMETRIES, (
            f"{code} q{hits[0]}: the rejected option {ch!r} is not on the framework's list "
            "either, so the item has two defensible answers"
        )
    print(f"OK  {code} list: q{hits[0]}'s key is absent from EK 2.7.A.2's eleven geometries "
          "and all four rejected options are present in it.")


def no_figure_language(module):
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{code} q{i}: refers to {hit.group(0)!r}, which the bank cannot show -- "
                f"{text[:70]!r}"
            )
    print(f"OK  {code} figures: no stem or choice points at a drawn molecule.")


CLAIMS = [
 ("Coulombic repulsion between electrons",
  "EK 2.7.A.1, verbatim: VSEPR theory uses the Coulombic repulsion between electrons as a basis for predicting the arrangement of electron pairs around a central atom."),
 ("arrangement of electron pairs around a central atom",
  "EK 2.7.A.1 names exactly this as what VSEPR predicts. Counting the valence electrons contributed is the Lewis diagram's job under EK 2.5.A.1."),
 ("Both Lewis diagrams and VSEPR theory",
  "EK 2.7.A.2, verbatim: both Lewis diagrams and VSEPR theory must be used for predicting electronic and structural properties of many covalently bonded molecules and polyatomic ions."),
 ("180 degrees",
  "EK 2.7.A.3: when the central atom is sp hybridized, its ideal bond angles are 180 degrees. Recomputed against the transcribed correspondence."),
 ("120 degrees",
  "EK 2.7.A.3: for sp2 hybridized atoms the bond angles are 120 degrees. Recomputed against the transcribed correspondence."),
 ("109.5 degrees",
  "EK 2.7.A.3: for sp3 hybridized atoms the bond angles are 109.5 degrees. Recomputed against the transcribed correspondence."),
 ("sp^{3} hybridized",
  "EK 2.7.A.3 pairs 109.5 degrees with sp3, and the three angles it prints are all different, so the correspondence runs in both directions. Recomputed."),
 ("is \\( sp \\) hybridized",
  "EK 2.7.A.3 pairs 180 degrees with sp. Recomputed, including a check that no other printed angle takes that value."),
 ("sp^{2} hybridized",
  "EK 2.7.A.3 pairs 120 degrees with sp2. Recomputed, including a check that no other printed angle takes that value."),
 ("Atom S",
  "EK 2.7.A.3 fixes all three pairings. Recomputed in q10 row by row, which finds exactly one tabulated row disagreeing with the framework."),
 ("Atom U",
  "EK 2.7.A.3 attaches an angle to each hybridization, so the tabulated labels order the angles. Recomputed in q11, refusing a tie."),
 ("Atom T",
  "EK 2.7.A.3 gives sp3 the smallest of the three printed angles. Recomputed in q12, refusing a tie."),
 ("arrangement of electrons around a central atom",
  "EK 2.7.A.3 opens by saying the terms hybridization and hybrid atomic orbital are used to describe the arrangement of electrons around a central atom."),
 ("Overlap between atomic orbitals",
  "EK 2.7.A.4, verbatim: bond formation is associated with overlap between atomic orbitals. Complete transfer is EK 2.1.A.4's ionic case and delocalization EK 2.4.A.1's metallic one."),
 ("Both sigma and pi bonds",
  "EK 2.7.A.4, verbatim: in multiple bonds, such overlap leads to the formation of both sigma and pi bonds."),
 ("Sigma bonds have greater bond energy than pi bonds",
  "EK 2.7.A.4: the overlap is stronger in sigma than pi bonds, which is reflected in sigma bonds having greater bond energy than pi bonds. The framework attaches no dependence on the elements involved."),
 ("overlap is stronger in sigma bonds",
  "EK 2.7.A.4 gives the reason and the consequence in one sentence, the stronger overlap being what the greater bond energy reflects."),
 ("Rotation of the bond",
  "EK 2.7.A.4: the presence of a pi bond also prevents the rotation of the bond. No other prohibition is attached to it there."),
 ("leads to geometric isomers",
  "EK 2.7.A.4 states the consequence in those words, immediately after the prevention of rotation."),
 ("derivation and depiction of hybrid orbitals",
  "The exclusion statement attached to LO 2.7.A says an understanding of the derivation and depiction of hybrid orbitals will not be assessed, and then names three things the course DOES include, three of which are the rejected options here."),
 ("sigma and pi distinction, the use of VSEPR to explain shapes",
  "The same exclusion statement lists the included material in those words: the distinction between sigma and pi bonding, the use of VSEPR to explain the shapes of molecules, and the sp, sp2 and sp3 nomenclature."),
 ("Only the shape of the resulting molecule",
  "The exclusion statement says that when an atom has more than four pairs of electrons surrounding the central atom, students are only responsible for the shape of the resulting molecule."),
 ("bonding, nonbonding and antibonding orbitals",
  "The molecular orbital exclusion statement says the exam will neither assess molecular orbital diagrams, nor filling of molecular orbitals, nor the distinction between bonding, nonbonding and antibonding orbitals."),
 ("presence of a dipole moment",
  "EK 2.7.A.2 lists it as item v among the properties predicted using Lewis diagrams together with VSEPR theory. Reaction rate, molar mass and boiling point are not on that list."),
 ("Relative bond energies based on bond order",
  "EK 2.7.A.2 names this as item iii of its list, and item iv as relative bond lengths; the framework's list is relative throughout rather than absolute."),
 ("Trigonal prismatic",
  "EK 2.7.A.2 lists eleven geometries by name and this is not among them. Checked in geometry_names_are_the_frameworks, which also asserts every rejected option IS on that list."),
 ("d orbitals",
  "The exclusion statement says hybridization involving d orbitals will not be assessed, while EK 2.7.A.3's sp, sp2 and sp3 nomenclature, built from s and p orbitals, is what the course includes."),
 ("120 degrees",
  "EK 2.7.A.3 gives 120 degrees for an sp2 hybridized atom, and the CED's own sample multiple-choice question asks exactly this about this molecule. Recomputed from the hybridization the stem states."),
 ("Atom U and Atom V",
  "EK 2.7.A.3's three printed angles fix the three pairwise differences. Recomputed in q29, which asserts exactly one tabulated pair differs by sixty degrees."),
 ("70.5 degrees",
  "EK 2.7.A.3 gives 180 degrees for sp and 109.5 for sp3, and the difference between those printed values is what the item asks for. Recomputed in a30."),
]


# ------------------------------------------------------------ negative controls

def _swap(mod, i, old, new):
    before = mod.QUESTIONS[i - 1]["q"]
    after = before.replace(old, new)
    assert after != before, f"the control's replacement {old!r} did not match q{i}'s stem"
    mod.QUESTIONS[i - 1]["q"] = after


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


def _hybridization_changes(mod, cl):
    """Change the stem's hybridization, leaving the keyed angle behind."""
    _swap(mod, 5, r"\( sp^{2} \)", r"\( sp^{3} \)")


def _angle_changes(mod, cl):
    """Change the stem's angle, leaving the keyed hybridization behind."""
    _swap(mod, 7, "are 109.5 degrees", "are 120 degrees")


def _difference_pair_changes(mod, cl):
    """Change one of the two hybridizations, so the keyed difference is false."""
    _swap(mod, 30, r"an \( sp^{3} \) hybridized central atom",
          r"an \( sp^{2} \) hybridized central atom")


def _second_bad_row(mod, cl):
    """Corrupt a second tabulated pairing, so the inconsistent row is not unique."""
    _retable(mod, 10, "Atom Q", **{ANG: "180 degrees"})


def _tie_for_largest_angle(mod, cl):
    """Give two tabulated atoms the same hybridization, so no single angle is largest."""
    _retable(mod, 11, "Atom V", **{HYB: r"\( sp \)"})


def _no_sixty_degree_pair(mod, cl):
    """Remove the one pair differing by sixty degrees."""
    _retable(mod, 29, "Atom V", **{HYB: r"\( sp^{3} \)"})


def _geometry_in_a_key(mod, cl):
    ch = list(mod.QUESTIONS[0]["choices"])
    ch[0] = "The tetrahedral arrangement of the four electron pairs"
    mod.QUESTIONS[0]["choices"] = ch
    cl[0] = ("tetrahedral arrangement", cl[0][1])
    no_unlicensed_structure_rule(mod)


def _electron_domain_rule(mod, cl):
    mod.QUESTIONS[1]["q"] = ("How many regions of electron density does VSEPR count "
                             "around a central atom?")
    no_unlicensed_structure_rule(mod)


def _recognition_key_is_on_the_list(mod, cl):
    ch = list(mod.QUESTIONS[25]["choices"])
    ch[0] = "Octahedral"
    mod.QUESTIONS[25]["choices"] = ch
    geometry_names_are_the_frameworks(mod)


def _recognition_distractor_is_off_the_list(mod, cl):
    ch = list(mod.QUESTIONS[25]["choices"])
    ch[1] = "Pentagonal planar"
    mod.QUESTIONS[25]["choices"] = ch
    geometry_names_are_the_frameworks(mod)


def _figure_language(mod, cl):
    mod.QUESTIONS[2]["q"] = "In the molecule shown above, what must be used to predict it?"
    no_figure_language(mod)


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH, extra=[
        ("the stem's hybridization changed under a keyed angle", _hybridization_changes),
        ("the stem's angle changed under a keyed hybridization", _angle_changes),
        ("one of the two hybridizations changed under a keyed angle difference",
         _difference_pair_changes),
        ("a second tabulated pairing corrupted, so the inconsistent row is not unique",
         _second_bad_row),
        ("two tabulated atoms given the same hybridization, so no angle is largest",
         _tie_for_largest_angle),
        ("the one sixty-degree pair removed from the table", _no_sixty_degree_pair),
        ("a molecular geometry moved into a keyed choice", _geometry_in_a_key),
        ("an electron-domain rule the CED never states, moved into a stem",
         _electron_domain_rule),
        ("the recognition item keyed to a geometry that IS on the framework's list",
         _recognition_key_is_on_the_list),
        ("a recognition distractor replaced by a name not on the list either",
         _recognition_distractor_is_off_the_list),
        ("a stem pointing at a molecule the bank cannot show", _figure_language),
    ])

no_unlicensed_structure_rule(M)
geometry_names_are_the_frameworks(M)
no_figure_language(M)
hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
