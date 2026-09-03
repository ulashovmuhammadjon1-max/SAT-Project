r"""Key audit for AP CHEMISTRY 2.1 Types of Chemical Bonds.

One (anchor, claim) per item, in module order. ``anchor`` must appear in the
KEYED choice and in no distractor, since the exporter reshuffles choices.

WHAT IS RECOMPUTED. Every polarity comparison keyed here is recomputed from the
item's own tabulated electronegativities as an absolute DIFFERENCE, which is
what EK 2.1.A.3.ii ties the bond dipole to. Three things are checked beyond the
key itself:

  * that the winning difference is UNIQUE, since a tie would give the item two
    defensible answers;
  * that a nonpolar key really has a difference of zero rather than merely a
    small one, because EK 2.1.A.2's "similar" is doing different work from
    "identical" and only the second is checkable;
  * that no key implies a numerical cutoff between ionic and covalent. The
    framework prints none (EK 2.1.A.3.iii calls the distinction a continuum),
    so ``_no_cutoff`` scans every keyed choice for a number attached to the word
    ionic or covalent and fails if one appears. That check exists because
    inventing a threshold is the single most likely way this topic could ship a
    falsehood, and it would look entirely reasonable on the page.

WHAT THE KEYS REST ON
---------------------
Item 1 rests on EK 2.1.A.1, the electronegativity trend across a period and
down a group.

Items 2, 6, 12, 19 and 27 rest on EK 2.1.A.2: valence electrons shared between
atoms of similar electronegativity constitute a nonpolar covalent bond, with
carbon-to-hydrogen as the framework's own example of "effectively nonpolar".

Items 3, 4, 13, 16, 17, 18, 22, 23, 28 rest on EK 2.1.A.3 and its three
sub-points: the polar covalent bond, the partial negative charge on the more
electronegative atom, the growth of the dipole with the difference IN SINGLE
BONDS, and the ionic character every polar bond carries.

Items 7, 11, 15, 25 and 26 rest on EK 2.1.A.3.iii's continuum specifically --
these are the items that refuse a sharp boundary.

Items 8, 9, 14, 20, 24, 26 rest on EK 2.1.A.4: the electronegativity difference
is not the only factor, metal with nonmetal is generally ionic and nonmetal
with nonmetal generally covalent, and examining the properties of a compound is
the best way to characterize the bonding. Where an item reads a property table
the claim also cites EK 3.2.A.3 for what ionic solids actually do.

Items 10, 21 and 30 rest on EK 2.1.A.5: in a metallic solid the valence
electrons are delocalized and not associated with any individual atom.

Items 17 and 24 are the suggested skill 6.A items: which claim the evidence
supports.

DATA ITEMS: 4, 5, 11, 12, 14, 16, 17, 20, 21, 23, 24, 26 and 28 carry tables;
all thirteen are recomputed below.

NEGATIVE CONTROL: ``python3 verify_h2_1.py --selftest``.
"""
import re
import sys

import cg_check as cg
import chem_notation

EN = "Electronegativity"
EN1 = "Electronegativity of the first atom"
EN2 = "Electronegativity of the second atom"
PEN1 = "Electronegativity of the first element"
PEN2 = "Electronegativity of the second element"

# A number sitting next to "ionic" or "covalent" would be a cutoff the CED does
# not state. Explicit lookarounds either side, never \b next to a digit.
_CUTOFF = re.compile(
    r"(?<![a-z0-9])(?:ionic|covalent)(?:\s+\w+){0,3}\s+\d|"
    r"\d(?:\s+\w+){0,3}\s+(?:ionic|covalent)(?![a-z0-9])", re.I)


def _no_cutoff(module):
    """No keyed choice may state a numerical ionic/covalent boundary."""
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]]
        hit = _CUTOFF.search(key)
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the keyed choice attaches a number to ionic or "
            f"covalent bonding ({hit.group(0)!r}). EK 2.1.A.3.iii calls the distinction "
            "a continuum and the CED prints no cutoff anywhere.")
    print(f"OK  {module.TOPIC[0]} continuum: no keyed choice invents a numerical "
          "ionic/covalent boundary.")


def _diffs(table, a=EN1, b=EN2):
    return dict(zip(cg.labels(table), [abs(x - y) for x, y in
                                       zip(cg.col(table, a), cg.col(table, b))]))


def _unique_max(d, want, where):
    top = max(d.values())
    winners = [k for k, v in d.items() if abs(v - top) < 1e-12]
    assert winners == [want], f"{where}: the largest difference belongs to {winners}"
    return top


def q4(table, item):
    d = _diffs(table)
    top = _unique_max(d, "Bond 5: fluorine to hydrogen", "q4")
    return f"the tabulated differences are { {k.split(':')[0]: round(v, 1) for k, v in d.items()} }, uniquely largest at {top}"


def q5(table, item):
    d = _diffs(table)
    zero = [k for k, v in d.items() if v == 0]
    assert zero == ["Bond 1: hydrogen to hydrogen"], f"the zero-difference bonds are {zero}"
    return (f"exactly one tabulated bond has an electronegativity difference of zero; the "
            f"others are { {k.split(':')[0]: round(v, 1) for k, v in d.items() if v} }")


def q11(table, item):
    d = _diffs(table, PEN1, PEN2)
    top = _unique_max(d, "Sodium and fluorine", "q11")
    assert len(set(round(v, 6) for v in d.values())) > 1, "'all four equal' must be false"
    return f"the tabulated differences are { {k: round(v, 1) for k, v in d.items()} }, uniquely largest at {top}"


def q12(table, item):
    d = _diffs(table, PEN1, PEN2)
    zero = [k for k, v in d.items() if v == 0]
    assert zero == ["Carbon and sulfur"], f"the zero-difference pairs are {zero}"
    a, b = table["rows"][0][0].split(" and ")
    assert a != b, "the nonpolar pair must be two DIFFERENT elements, which is the item's point"
    return (f"exactly one tabulated pair has a difference of zero, and it is two different "
            f"elements ({a} and {b})")


def q14(table, item):
    mp = dict(zip(cg.labels(table), cg.col(table, "Melting point (degrees Celsius)")))
    cond = dict(zip(cg.labels(table),
                    [r[2].strip().lower() for r in table["rows"]]))
    conducting = [k for k in mp if cond[k] == "yes"]
    top = max(conducting, key=lambda k: mp[k])
    assert top == "Substance T", f"the highest-melting conductor is {top}"
    assert len(conducting) > 1, "there must be more than one conductor, or the item is trivial"
    assert min(mp[k] for k in conducting) > max(mp[k] for k in mp if k not in conducting), (
        "every conductor should melt above every non-conductor, so the two properties "
        "point the same way and the item has one defensible answer")
    return (f"the conductors are {sorted(conducting)} with melting points "
            f"{ {k: mp[k] for k in conducting} }, so the keyed substance is the highest-melting "
            "of them and every non-conductor melts lower still")


def q16(table, item):
    en = dict(zip(cg.labels(table), cg.col(table, EN)))
    assert en["Chlorine"] > en["Hydrogen"], \
        f"chlorine {en['Chlorine']} does not exceed hydrogen {en['Hydrogen']}"
    return (f"the tabulated values put chlorine at {en['Chlorine']} against hydrogen at "
            f"{en['Hydrogen']}, so the partial negative charge sits on chlorine")


def q17(table, item):
    en = dict(zip(cg.labels(table), cg.col(table, EN)))
    kf = abs(en["Potassium"] - en["Fluorine"])
    cs = abs(en["Carbon"] - en["Sulfur"])
    assert kf > cs, f"the keyed comparison fails: {kf} against {cs}"
    assert cs == 0, f"the carbon-sulfur difference is {cs}, so 'none at all' is not exact"
    return (f"potassium to fluorine differs by {kf:.1f} against {cs:.1f} for carbon to "
            "sulfur, so the keyed claim is the one the data support")


def q20(table, item):
    kind = dict(zip(cg.labels(table), [r[3].strip().lower() for r in table["rows"]]))
    nonmetals = sorted(k for k, v in kind.items() if v == "nonmetal")
    assert nonmetals == ["Element B", "Element C"], f"the nonmetals are {nonmetals}"
    metals = sorted(k for k, v in kind.items() if v == "metal")
    assert len(metals) == 2, f"there must be exactly two metals for the distractors: {metals}"
    return (f"the table marks {nonmetals} as nonmetals and {metals} as metals, so exactly one "
            "offered pairing is nonmetal with nonmetal")


def q21(table, item):
    kind = [r[3].strip().lower() for r in table["rows"]]
    assert kind.count("metal") >= 2, f"the table must offer two metals: {kind}"
    return f"the table's metal-or-nonmetal column reads {kind}, so two metals are available to combine"


def q23(table, item):
    d = _diffs(table)
    order = [k for k, _ in sorted(d.items(), key=lambda kv: kv[1])]
    assert order == [f"Bond {i}: " + s for i, s in
                     ((1, "hydrogen to hydrogen"), (2, "carbon to hydrogen"),
                      (3, "nitrogen to hydrogen"), (4, "oxygen to hydrogen"),
                      (5, "fluorine to hydrogen"))], \
        f"sorted by difference the bonds run {order}"
    assert len(set(round(v, 6) for v in d.values())) == len(d), \
        "two bonds share a difference, so the ranking is not unique"
    return (f"sorted by tabulated difference the bonds run {[k.split(':')[0] for k in order]}, "
            "with no two differences equal")


def q24(table, item):
    cond = dict(zip(cg.labels(table), [r[2].strip().lower() for r in table["rows"]]))
    mp = dict(zip(cg.labels(table), cg.col(table, "Melting point (degrees Celsius)")))
    low_and_insulating = [k for k in mp if mp[k] < 25 and cond[k] == "no"]
    assert low_and_insulating, "the table must contain a low-melting non-conductor to point at"
    assert all(cond[k] == "yes" for k in mp if mp[k] > 500), \
        "every high-melting substance in the table should conduct, or the contrast is muddied"
    return (f"the table holds {sorted(low_and_insulating)} melting below room temperature and "
            "not conducting when melted, which is the opposite of the ionic pattern")


def q26(table, item):
    mp = dict(zip(cg.labels(table), cg.col(table, "Melting point (degrees Celsius)")))
    assert any(v < 25 for v in mp.values()), \
        "the table must contain a substance melting below room temperature"
    assert any(v > 500 for v in mp.values()), \
        "and one melting far above it, or the contrast the item draws is not in the data"
    return (f"the tabulated melting points {mp} span from below room temperature to far above "
            "it, so 'melts far below room temperature' is a real category in this table")


def q28(table, item):
    en = dict(zip(cg.labels(table), cg.col(table, EN)))
    target = abs(en["Carbon"] - en["Oxygen"])
    cands = {"A bond between nitrogen and hydrogen": abs(en["Nitrogen"] - en["Hydrogen"]),
             "A bond between hydrogen and phosphorus": abs(en["Hydrogen"] - en["Phosphorus"]),
             "A bond between sodium and fluorine": abs(en["Sodium"] - en["Fluorine"]),
             "A bond between carbon and sulfur": abs(en["Carbon"] - en["Sulfur"]),
             "A bond between potassium and fluorine": abs(en["Potassium"] - en["Fluorine"])}
    best = min(cands, key=lambda k: abs(cands[k] - target))
    assert cg.contains_phrase(item["choices"][item["ans"]], best), \
        f"the closest difference to {target} belongs to {best!r}, not to the keyed choice"
    runners = sorted(abs(v - target) for v in cands.values())
    assert runners[1] - runners[0] > 0.05, \
        f"a second option is nearly as close ({runners[:2]}), so the answer is not clean"
    return (f"the carbon-to-oxygen difference is {target:.1f} and the candidates differ by "
            f"{ {k.split('between ')[1]: round(v, 1) for k, v in cands.items()} }")


CLAIMS = [
 ("increase from left to right across a period and decrease down a group",
  "EK 2.1.A.1, near verbatim: electronegativity values for the representative elements increase going from left to right across a period and decrease going down a group. The framework adds that the trends are understood through electronic structure, the shell model and Coulomb's law."),
 ("nonpolar covalent bond",
  "EK 2.1.A.2, near verbatim: valence electrons shared between atoms of similar electronegativity constitute a nonpolar covalent bond. Sharing is what makes it covalent; similarity is what makes it nonpolar."),
 ("partial negative charge on the atom of higher electronegativity",
  "EK 2.1.A.3 makes shared valence electrons between atoms of unequal electronegativity a polar covalent bond, and EK 2.1.A.3.i puts the partial negative charge on the more electronegative atom. The charges are PARTIAL, which is what separates the case from an ionic bond."),
 ("Bond 5",
  "Recomputed in q4 above from the item's own table. EK 2.1.A.3.ii states that in single bonds greater differences in electronegativity lead to greater bond dipoles, and the check confirms the largest tabulated difference is unique so the item has one answer."),
 ("Bond 1",
  "Recomputed in q5 above: exactly one tabulated bond has a difference of ZERO rather than merely a small one. EK 2.1.A.2 makes shared electrons between atoms of similar electronegativity a nonpolar covalent bond, and zero is the limiting case."),
 ("small difference in electronegativity produces a bond that is treated as nonpolar",
  "EK 2.1.A.2's own example: bonds between carbon and hydrogen are effectively nonpolar EVEN THOUGH carbon is slightly more electronegative than hydrogen. That wording asserts a small difference treated as none, not the absence of a difference."),
 ("continuum rather than a sharp division",
  "EK 2.1.A.3.iii, near verbatim: all polar bonds have some ionic character, and the difference between ionic and covalent bonding is not distinct but rather a continuum. The framework prints no numerical cutoff anywhere, which is what the rejected threshold option invents."),
 ("generally ionic, though the electronegativity difference is not the only factor",
  "EK 2.1.A.4 states both halves in one breath: generally, bonds between a metal and nonmetal are ionic, AND the difference in electronegativity is not the only factor in determining the designation. A key that kept only the first half would misreport the framework."),
 ("Examination of the properties of the compound",
  "EK 2.1.A.4, near verbatim: examination of the properties of a compound is the best way to characterize the type of bonding. The same statement offers the electronegativity difference as one factor among others rather than as the test."),
 ("delocalized, and not associated with any individual atom",
  "EK 2.1.A.5, near verbatim: in a metallic solid, the valence electrons from the metal atoms are considered to be delocalized and not associated with any individual atom. A localized shared pair would be covalent and a complete transfer ionic."),
 ("Sodium and fluorine",
  "Recomputed in q11 above: the largest tabulated electronegativity difference, and checked to be unique. EK 2.1.A.3.ii ties the dipole to that difference and EK 2.1.A.3.iii puts every polar bond somewhere on the ionic-covalent continuum, so the largest difference lies farthest toward the ionic end."),
 ("Carbon and sulfur",
  "Recomputed in q12 above: exactly one tabulated pair has a difference of zero, and the check confirms it is a pair of DIFFERENT elements, which is what makes the 'only identical atoms' option false. EK 2.1.A.2's own carbon-to-hydrogen example makes the same point."),
 ("bond dipole grows as well",
  "EK 2.1.A.3.ii, near verbatim: in single bonds, greater differences in electronegativity lead to greater bond dipoles. The framework attaches the claim specifically to single bonds, which is why the stem specifies one."),
 ("Substance T",
  "Recomputed in q14 above. EK 2.1.A.4 makes examination of properties the best way to characterize bonding and EK 3.2.A.3 supplies the ionic pattern -- high melting point, conduction when molten. The check confirms every conductor in the table melts above every non-conductor, so the two properties agree and the item has one defensible answer."),
 ("difference between ionic and covalent bonding is described as a continuum",
  "EK 2.1.A.3.iii states that all polar bonds have some ionic character and that the difference between ionic and covalent bonding is not distinct but rather a continuum, and the CED prints no dividing value. EK 2.1.A.4 adds that the electronegativity difference is not the only factor in any case."),
 ("Chlorine, because its tabulated electronegativity is the higher",
  "Recomputed in q16 above from the item's own table. EK 2.1.A.3.i states that the atom with the higher electronegativity develops a partial negative charge relative to the other atom in the bond; mass and electron count do not appear in the framework's statement."),
 ("potassium and fluorine would be more polar",
  "Recomputed in q17 above: the first pair's tabulated difference is large and the second's is exactly zero. Suggested skill 6.A asks which claim the evidence supports, and EK 2.1.A.3.ii is what licenses reading a difference as a dipole. A FULL charge would make the bond ionic rather than polar covalent."),
 ("partial charges that resemble a small version of the complete transfer",
  "EK 2.1.A.3.iii states that all polar bonds have some ionic character and that the two bonding types form a continuum, and EK 2.1.A.3.i describes the partial charges unequal sharing produces. A complete transfer would put the bond at the end of the continuum rather than partway along."),
 ("electronegativity difference of zero",
  "Two atoms of one element have identical electronegativities, and EK 2.1.A.2 makes shared valence electrons between atoms of similar electronegativity a nonpolar covalent bond. Zero difference is the limiting case of similarity rather than an exception to it."),
 ("Element B with element C, because both are nonmetals",
  "Recomputed in q20 above from the table's own metal-or-nonmetal column: exactly one offered pairing is nonmetal with nonmetal. EK 2.1.A.4 states that bonds between two nonmetals are generally covalent, and EK 2.1.A.3 makes covalent bonds between different elements ordinary."),
 ("delocalized and are not associated with any individual atom",
  "Recomputed in q21 above only to the extent of confirming the table offers two metals. EK 2.1.A.5 supplies the model: in a metallic solid the valence electrons are delocalized and not associated with any individual atom."),
 ("rises steadily across a period, so elements farther apart differ more",
  "EK 2.1.A.1 gives the rise in electronegativity across a period and EK 2.1.A.3.ii makes a greater difference a greater single-bond dipole. Elements of one period occupy the same valence shell, which is what makes the shell-based rejected option false on the framework's own terms."),
 ("Bond 1, then Bond 2, then Bond 3, then Bond 4, then Bond 5",
  "Recomputed in q23 above by sorting the tabulated differences, with a check that no two differences are equal so the ranking is unique. EK 2.1.A.3.ii is what makes the ordering of differences an ordering of dipoles."),
 ("the framework calls best",
  "Recomputed in q24 above to the extent of confirming the table really contains the contrast the item draws on. EK 2.1.A.4 states outright that examination of a compound's properties is the best way to characterize its bonding, while the periodic table gives a general expectation rather than a settled answer."),
 ("toward the ionic end of the continuum without being fully ionic",
  "EK 2.1.A.4 makes bonds between two nonmetals generally covalent while denying that the electronegativity difference settles the designation alone, and EK 2.1.A.3.iii supplies the continuum such a bond sits on. The framework describes intermediate cases explicitly, so the 'impossible to place' option contradicts it."),
 ("melts far below room temperature and does not conduct",
  "Recomputed in q26 above against the item's own table. EK 2.1.A.4 makes properties the best characterization and denies the electronegativity difference is decisive, and EK 3.2.A.3 gives the ionic pattern that these observations contradict."),
 ("partial rather than full, because the electrons are shared",
  "EK 2.1.A.3 defines a polar covalent bond as SHARED valence electrons between atoms of unequal electronegativity, and EK 2.1.A.3.i calls the resulting charge partial. EK 2.1.A.3.iii places such a bond partway along the continuum toward ionic rather than at its end."),
 ("nitrogen and hydrogen",
  "Recomputed in q28 above: every offered pair's tabulated difference is compared against the target and the nearest is keyed, with a check that no second option comes within a twentieth of a unit of it. EK 2.1.A.3.ii is what makes a difference a proxy for a dipole."),
 ("understood qualitatively, alongside electronic structure and Coulomb's law",
  "EK 2.1.A.1 states that the electronegativity trends can be understood qualitatively through the electronic structure of the atoms, the shell model, and Coulomb's law. That is an explanatory role rather than a definition, and the framework restricts it to no class of substance."),
 ("without belonging to any one atom",
  "EK 2.1.A.5 states that in a metallic solid the valence electrons from the metal atoms are considered to be delocalized and not associated with any individual atom, which is exactly what an observation of electrons belonging to no single atom would show."),
]

TABLE_CHECKS = {4: q4, 5: q5, 11: q11, 12: q12, 14: q14, 16: q16, 17: q17,
                20: q20, 21: q21, 23: q23, 24: q24, 26: q26, 28: q28}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate, cutoff=False):
        mod = types.ModuleType("h2_1_mutant")
        mod.TOPIC = h2_1.TOPIC
        mod.QUESTIONS = copy.deepcopy(h2_1.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            if cutoff:
                _no_cutoff(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:95]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[3]["ans"] = 1

    def break_anchor(mod, claims):
        claims[10] = ("no such phrase anywhere in the choice", claims[10][1])

    def tie_the_largest_difference(mod, claims):
        mod.QUESTIONS[3]["table"] = dict(
            headers=h2_1._T_BONDS["headers"],
            rows=[["Bond 1: hydrogen to hydrogen", "2.1", "2.1"],
                  ["Bond 2: carbon to hydrogen", "2.5", "2.1"],
                  ["Bond 3: nitrogen to hydrogen", "3.0", "2.1"],
                  ["Bond 4: oxygen to hydrogen", "4.0", "2.1"],
                  ["Bond 5: fluorine to hydrogen", "4.0", "2.1"]])

    def make_the_nonpolar_bond_merely_small(mod, claims):
        mod.QUESTIONS[4]["table"] = dict(
            headers=h2_1._T_BONDS["headers"],
            rows=[["Bond 1: hydrogen to hydrogen", "2.2", "2.1"],
                  ["Bond 2: carbon to hydrogen", "2.5", "2.1"],
                  ["Bond 3: nitrogen to hydrogen", "3.0", "2.1"],
                  ["Bond 4: oxygen to hydrogen", "3.5", "2.1"],
                  ["Bond 5: fluorine to hydrogen", "4.0", "2.1"]])

    def flip_an_electronegativity(mod, claims):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h2_1._T_EN["headers"],
            rows=[[el, ("1.5" if el == "Chlorine" else v)] for el, v in h2_1._T_EN["rows"]])

    def muddy_the_property_table(mod, claims):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h2_1._T_PROPERTIES["headers"],
            rows=[["Substance R", "801", "yes"], ["Substance S", "-114", "no"],
                  ["Substance T", "1,291", "yes"], ["Substance U", "900", "no"]])

    def break_the_ranking_uniqueness(mod, claims):
        mod.QUESTIONS[22]["table"] = dict(
            headers=h2_1._T_BONDS["headers"],
            rows=[["Bond 1: hydrogen to hydrogen", "2.1", "2.1"],
                  ["Bond 2: carbon to hydrogen", "2.5", "2.1"],
                  ["Bond 3: nitrogen to hydrogen", "2.5", "2.1"],
                  ["Bond 4: oxygen to hydrogen", "3.5", "2.1"],
                  ["Bond 5: fluorine to hydrogen", "4.0", "2.1"]])

    def make_a_second_option_nearly_as_close(mod, claims):
        mod.QUESTIONS[27]["table"] = dict(
            headers=h2_1._T_EN["headers"],
            rows=[[el, ("1.1" if el == "Phosphorus" else v)] for el, v in h2_1._T_EN["rows"]])

    def invent_a_cutoff(mod, claims):
        mod.QUESTIONS[6]["choices"][mod.QUESTIONS[6]["ans"]] = (
            "A bond is ionic above an electronegativity difference of 1.7 and covalent "
            "below it, which is the sharp division the framework draws.")

    def forget_table_check(mod, claims):
        mod.QUESTIONS[0]["table"] = h2_1._T_EN

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[8]["choices"][3] = mod.QUESTIONS[8]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[18]["why"] = "Zero difference."

    def letter_reference(mod, claims):
        mod.QUESTIONS[2]["why"] = ("Option B is excluded because the framework says so, "
                                   "and the rest of the reasoning follows from that.")

    def notation_slips_in(mod, claims):
        mod.QUESTIONS[15]["choices"][2] = "Chlorine, which carries a charge of delta^-"
        chem_notation.style(mod)

    print("negative controls:")
    must_fail("a partial charge written as a bare superscript", notation_slips_in)
    must_fail("a keyed choice inventing a numerical ionic/covalent cutoff",
              invent_a_cutoff, cutoff=True)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer present in the keyed choice", break_anchor)
    must_fail("two bonds tied for the largest difference, so the key is not unique",
              tie_the_largest_difference)
    must_fail("the nonpolar bond given a small difference instead of none",
              make_the_nonpolar_bond_merely_small)
    must_fail("an electronegativity flipped so the partial charge sits elsewhere",
              flip_an_electronegativity)
    must_fail("a high-melting non-conductor added, muddying the property contrast",
              muddy_the_property_table)
    must_fail("two bonds given equal differences, so the ranking is not unique",
              break_the_ranking_uniqueness)
    must_fail("a second option made nearly as close as the key",
              make_a_second_option_nearly_as_close)
    must_fail("a table added with no recompute behind it", forget_table_check)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a rationale reduced below the minimum", thin_why)
    must_fail("a rationale naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import h2_1  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

chem_notation.style(h2_1)
_no_cutoff(h2_1)
cg.check(h2_1, CLAIMS, table_checks=TABLE_CHECKS)
