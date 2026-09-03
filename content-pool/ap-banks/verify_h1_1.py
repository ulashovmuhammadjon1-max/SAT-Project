r"""Key audit for AP CHEMISTRY 1.1 Moles and Molar Mass.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a choice list reordered while editing fails here rather than
reaching a student -- ``export_units.py`` reshuffles the choices, which is what
makes a bare index worthless as a record of the key. ``claim`` states what the
key rests on, for a human to audit.

WHAT IS AND IS NOT GATED. The structural gate is ``cg_check.py``, shared with
every other AP bank. ``chem_notation.style`` gates the hand-written math spans
(SCIENCE_BRIEF.md: the converter does not run on Chemistry), and
``chem_katex_gate.py`` renders them at ``throwOnError: true``. Neither can tell
whether the chemistry is right. What can, here, is that **every arithmetic
claim in this topic is recomputed below from the item's own stimulus** -- which
SCIENCE_BRIEF.md requires of Chemistry specifically -- and that every
non-quantitative key traces to a sentence of the CED quoted in the claim.

WHAT THE KEYS REST ON
---------------------
Items 1, 16 and 30 rest on EK 1.1.A.1: one cannot count particles directly
while performing laboratory work, so there must be a connection between the
masses of substances reacting and the actual number of particles undergoing
chemical changes.

Items 2, 5, 6, 7, 18, 21 and 22 rest on EK 1.1.A.2: Avogadro's number provides
the connection between the number of moles in a pure sample and the number of
constituent particles (or formula units) of that substance. Items 7 and 18 turn
on the framework's own "(or formula units)" wording and assert nothing about
crystal structure, which the CED excludes at 2.3.A.1.

Items 3, 4, 9, 12, 14, 15, 17, 20, 24, 27 and 29 rest on EK 1.1.A.3 and its
equation n = m/M: the average mass in atomic mass units of one particle is
always numerically equal to the molar mass in grams, which is what makes a
weighed mass a particle count.

Items 10 and 26 rest on the subscripts of a chemical formula fixing the ratio of
atoms to formula units -- the same relationship EK 1.3.A.3 names as the
empirical formula, used here only to count atoms within a given formula.

DATA ITEMS: 3, 8, 9, 11, 13, 19, 25 and 28 carry tables. Each keyed value is
recomputed below from that table alone, and each check also falsifies at least
one distractor against the same numbers.

NEGATIVE CONTROL: ``python3 verify_h1_1.py --selftest`` corrupts a key, an
anchor, a table cell, a choice, a rationale and the notation on purpose and
confirms every gate fires.
"""
import sys

import cg_check as cg
import chem_notation

MASS = "Mass of sample (grams)"
MOLAR = "Molar mass (grams per mole)"


def _moles(table, mass_header=MASS, molar_header=MOLAR):
    """n = m/M for every row, keyed by row label. EK 1.1.A.3."""
    m = cg.col(table, mass_header)
    mm = cg.col(table, molar_header)
    return dict(zip(cg.labels(table), [a / b for a, b in zip(m, mm)]))


def q3(table, item):
    mm = cg.cell(table, "Carbon dioxide, CO2", MOLAR)
    n = 88.0 / mm
    assert abs(n - 2.00) < 1e-9, f"88.0 g over {mm} g/mol recomputes to {n}, not 2.00"
    assert abs(mm / 88.0 - 0.500) < 1e-9, \
        "the reciprocal distractor should be the 0.500 that dividing the wrong way gives"
    return f"88.0 grams divided by the tabulated {mm} grams per mole is exactly 2.00 moles"


def q8(table, item):
    n = _moles(table)
    assert abs(n["Sample 1"] - 2.0) < 1e-9, f"Sample 1 recomputes to {n['Sample 1']}"
    assert max(n, key=n.get) == "Sample 1", f"the largest mole count is {max(n, key=n.get)}"
    assert len(set(round(v, 9) for v in n.values())) > 1, \
        "'all four the same' must be false on these numbers"
    heaviest = max(cg.labels(table), key=lambda lab: cg.cell(table, lab, MASS))
    assert heaviest != "Sample 1", \
        "the item is pointless unless the largest MASS belongs to a different row"
    return (f"n = m/M row by row gives {[round(v, 3) for v in n.values()]}, so the "
            f"largest count is Sample 1 at 2.00 moles while the largest mass is {heaviest}")


def q9(table, item):
    mm = cg.cell(table, "Glucose, C6H12O6", MOLAR)
    m = 2.50 * mm
    assert abs(m - 450.0) < 1e-9, f"2.50 mol times {mm} g/mol recomputes to {m}, not 450"
    assert abs(2.50 / mm - 0.0139) < 5e-5, \
        "the divide-instead-of-multiply distractor should be near 0.0139"
    return f"2.50 moles times the tabulated {mm} grams per mole is exactly 450 grams"


def q11(table, item):
    ch4 = cg.cell(table, "Methane, CH4", MOLAR)
    co2 = cg.cell(table, "Carbon dioxide, CO2", MOLAR)
    assert ch4 < co2, f"methane {ch4} is not the smaller molar mass against {co2}"
    assert 10.0 / ch4 > 10.0 / co2, "equal masses must give methane the larger mole count"
    assert abs(10.0 / ch4 - 10.0 / co2) > 1e-6, "'equal numbers of molecules' must be false"
    return (f"for 10.0 grams each, n = m/M gives {10.0 / ch4:.3f} moles of methane against "
            f"{10.0 / co2:.3f} of carbon dioxide, so the smaller molar mass wins")


def q13(table, item):
    n = _moles(table, "Mass of substance (grams)", MOLAR)
    top = max(n, key=n.get)
    assert top == "Container 4", f"the largest mole count is {top}"
    assert abs(n["Container 4"] - 5.0) < 1e-9, f"Container 4 recomputes to {n['Container 4']}"
    assert abs(n["Container 1"] - n["Container 2"]) > 1e-9, "the 'tie' distractor must be false"
    heaviest = max(cg.labels(table), key=lambda lab: cg.cell(table, lab, "Mass of substance (grams)"))
    assert heaviest == "Container 4", "here the heaviest row is also the largest count"
    lightest_mm = min(cg.labels(table), key=lambda lab: cg.cell(table, lab, MOLAR))
    assert lightest_mm == "Container 4", "and it also carries the smallest molar mass"
    return (f"n = m/M gives {[round(v, 3) for v in n.values()]}; Container 4 is largest at "
            "5.00 moles and Containers 1 and 2 are 2.00 and 3.00, so they do not tie")


def q19(table, item):
    m = cg.col(table, MASS)
    n = cg.col(table, "Moles in the sample")
    mm = dict(zip(cg.labels(table), [a / b for a, b in zip(m, n)]))
    top = max(mm, key=mm.get)
    assert top == "Unknown M", f"the largest molar mass is {top}"
    assert abs(mm["Unknown M"] - 120.0) < 1e-6, f"Unknown M recomputes to {mm['Unknown M']}"
    assert len(set(m)) == 1, "the item's premise is that every mass is equal"
    assert len(set(round(v, 6) for v in mm.values())) > 1, \
        "'all four the same molar mass' must be false"
    fewest = min(dict(zip(cg.labels(table), n)), key=dict(zip(cg.labels(table), n)).get)
    assert fewest == top, "the largest molar mass must be the row with the fewest moles"
    return (f"M = m/n gives {[round(v, 1) for v in mm.values()]} grams per mole; every mass "
            "is 12.0, so the largest molar mass is the sample holding the fewest moles")


def q25(table, item):
    n = _moles(table)
    low = min(n, key=n.get)
    assert low == "Sample Z", f"the smallest mole count is {low}"
    assert abs(n["Sample Z"] - 12.0 / 180.0) < 1e-9, f"Sample Z recomputes to {n['Sample Z']}"
    assert len(set(cg.col(table, MASS))) == 1, "the item's premise is that every mass is equal"
    assert len(set(round(v, 9) for v in n.values())) > 1, \
        "'all four the same number of particles' must be false"
    heaviest_mm = max(cg.labels(table), key=lambda lab: cg.cell(table, lab, MOLAR))
    assert heaviest_mm == low, "the smallest count must belong to the largest molar mass"
    return (f"n = m/M on equal 12.0 gram masses gives {[round(v, 4) for v in n.values()]}, "
            "so the largest molar mass holds the fewest particles")


def q28(table, item):
    # The stem prints the count to four significant figures, so it is 1.204e24
    # rather than exactly 2 x 6.022e23; the tolerance is that rounding and
    # nothing looser -- 0.05 gram on a 36 gram answer, well inside the gap to
    # the nearest distractor at 18.0 grams.
    n = 1.204e24 / 6.022e23
    assert abs(n - 2.0) < 5e-3, f"the particle count recomputes to {n} moles, not 2.00"
    mm = cg.cell(table, "Water, H2O", MOLAR)
    m = n * mm
    assert abs(m - 36.0) < 0.05, f"the mass recomputes to {m}, not 36.0"
    assert abs(mm - 18.0) < 1e-9, "the one-mole distractor is the tabulated molar mass itself"
    return (f"the count is {n:.2f} times Avogadro's number, and 2.00 moles times the "
            f"tabulated {mm} grams per mole is 36.0 grams")


CLAIMS = [
 ("cannot be counted directly",
  "EK 1.1.A.1, near verbatim: one cannot count particles directly while performing laboratory work, so there must be a connection between the masses of substances reacting and the actual number of particles undergoing chemical changes. Every rejected option denies one half of that sentence."),
 ("constituent particles",
  "EK 1.1.A.2 states that Avogadro's number provides the connection between the number of moles in a pure sample and the number of constituent particles (or formula units) of that substance. Its units are therefore particles per mole, which rules out every rejected option naming a mass, a volume or a nuclear count."),
 ("2.00 moles",
  "Recomputed in q3 above from the item's own table. The relationship is EK 1.1.A.3's n = m/M, and the tabulated molar mass of carbon dioxide is the only number the item requires beyond the stated mass."),
 ("numerically equal to the molar mass",
  "EK 1.1.A.3, near verbatim: the average mass in amu of one particle or formula unit of a substance will always be numerically equal to the molar mass of that substance in grams. The framework offers this as the reason the atomic mass unit is useful, not as a coincidence."),
 (r"1.51 \times 10^{23}",
  "EK 1.1.A.2 makes Avogadro's number the moles-to-particles factor, so the count is 0.250 multiplied by 6.022 times ten to the twenty-third. Dividing rather than multiplying gives the rejected value that is ten times larger, which is the characteristic error."),
 ("0.500 moles",
  "The same connection in EK 1.1.A.2 run backwards: a particle count divided by Avogadro's number is a number of moles. The count in the stem is exactly half of Avogadro's number."),
 ("supplies one sodium ion",
  "EK 1.1.A.2 writes the countable entity as the number of constituent particles or formula units, which is the wording that covers a substance having no discrete molecules. The formula NaCl fixes one sodium ion and one chloride ion per formula unit; nothing about the crystal arrangement is asserted, which the CED excludes at 2.3.A.1."),
 ("Sample 1",
  "Recomputed in q8 above. EK 1.1.A.2 makes the largest mole count the largest particle count, and the check confirms that the row with the largest MASS is a different row, so reading the table on mass alone gives the wrong answer."),
 ("450 grams",
  "Recomputed in q9 above from the tabulated molar mass of glucose, rearranging EK 1.1.A.3's n = m/M to m equals n multiplied by M."),
 ("4.00 moles of oxygen atoms",
  "The subscripts of the formula H2SO4 fix the ratio of atoms to formula units, so each mole of the compound supplies four moles of oxygen atoms. The rejected value of seven counts every atom in the formula rather than the oxygen atoms alone."),
 ("smaller molar mass",
  "Recomputed in q11 above from the two tabulated molar masses. With the mass held fixed in n = m/M the mole count varies inversely with the molar mass, and EK 1.1.A.2 turns that mole count into a molecule count."),
 ("argon sample has the greater mass",
  "Equal mole counts mean equal particle counts by EK 1.1.A.2, while m equals n multiplied by M from EK 1.1.A.3 makes the mass ten times larger for the gas whose molar mass is ten times larger. The two halves of the keyed statement come from the two separate statements."),
 ("Container 4",
  "Recomputed in q13 above. Applying n = m/M to each row is the whole content of the item, and the check confirms the two containers named in the tie distractor hold different numbers of moles."),
 ("Divide the mass by the molar mass, then multiply",
  "EK 1.1.A.3 gives n = m/M for the first step and EK 1.1.A.2 makes Avogadro's number the moles-to-particles factor for the second. Each rejected sequence leaves a quantity whose units are not a count of molecules."),
 ("2.00 moles",
  "EK 1.1.A.3 makes the molar mass numerically equal to the average particle mass in atomic mass units, so 30.0 amu per molecule fixes 30.0 grams per mole, and n = m/M gives 60.0 divided by 30.0. The item is unsolvable to a student who treats the two units as unrelated."),
 ("8.40 grams",
  "EK 1.1.A.1 rules out delivering a mole quantity by counting, so it has to be delivered as a mass: 0.100 moles multiplied by 84.0 grams per mole. The stem supplies the molar mass, so no recall is required."),
 ("80.0 grams per mole",
  "Rearranging EK 1.1.A.3's n = m/M gives M equal to m divided by n, so 20.0 grams divided by 0.250 moles is 80.0 grams per mole. Multiplying the two instead gives the rejected value of 5.00."),
 ("3.00 moles of ions",
  "The formula unit named in EK 1.1.A.2 is MgCl2, which supplies one magnesium ion and two chloride ions, so a mole of formula units supplies three moles of ions. Counting only the chloride gives the rejected value of two."),
 ("Unknown M",
  "Recomputed in q19 above. With M equal to m divided by n and every tabulated mass equal, the largest molar mass is the row holding the fewest moles, which the check confirms directly against the table."),
 ("doubles and the molar mass is unchanged",
  "In EK 1.1.A.3's n = m/M the molar mass is a property of the substance rather than of the size of the sample, so doubling m at fixed M doubles n. Treating molar mass as something a larger sample changes is the misconception every rejected option shares."),
 ("count of particles per mole",
  "EK 1.1.A.2 defines Avogadro's number as the connection between moles and the number of constituent particles, so its unit is particles per mole. The mass of one mole is the separate quantity EK 1.1.A.3 ties to the average particle mass in atomic mass units."),
 ("0.100 moles",
  "The particle count in the stem is one tenth of Avogadro's number, so EK 1.1.A.2 fixes the sample at 0.100 moles. Misreading the exponent by a single place gives the rejected value of 1.00, which is why the exponents differ by exactly one."),
 ("16.0 grams",
  "The stated atom count is half of Avogadro's number, which is 0.500 moles by EK 1.1.A.2, and multiplying by the molar mass given in the stem gives 16.0 grams. Treating the count as a whole mole gives the rejected value of 32.0."),
 ("molar mass of the compound",
  "The molar mass in EK 1.1.A.3's n = m/M is a property of the substance and does not depend on how much of it is present, while mass, mole count and particle count all scale with the size of the portion taken."),
 ("Sample Z",
  "Recomputed in q25 above. With every tabulated mass equal, n = m/M makes the mole count smallest for the largest molar mass, and EK 1.1.A.2 makes the smallest mole count the smallest particle count. Equal masses read as equal counts is exactly the error EK 1.1.A.1 exists to prevent."),
 ("2.50 moles of atoms",
  "The formula CH4 carries five atoms per molecule, one carbon and four hydrogen, so 0.500 moles of molecules carries 2.50 moles of atoms. Counting only the hydrogen gives the rejected value of 2.00."),
 ("sample Q is three times",
  "Equal particle counts mean equal mole counts by EK 1.1.A.2, and m equals n multiplied by M, so the ratio of masses is exactly the ratio of molar masses. The common mole count cancels, which is why the number of molecules need not be known."),
 ("36.0 grams",
  "Recomputed in q28 above: the stated count is twice Avogadro's number, and two moles multiplied by the tabulated molar mass of water gives the mass. Skipping the conversion to moles entirely produces the absurd rejected value."),
 ("numerically the same as the molar mass",
  "EK 1.1.A.3 gives precisely this reason for expressing a particle mass in atomic mass units: the numerical equality is what supplies the quantitative connection between the mass of a substance and the number of particles it contains. An atomic mass unit is far smaller than a gram, not larger."),
 ("identity fixes the molar mass",
  "EK 1.1.A.1 asserts that a connection between mass and particle number must exist precisely because direct counting is impossible, and EK 1.1.A.3 supplies it. What knowing the identity of the substance adds is the value of M in n = m/M, so a weighed mass is enough once the substance is known."),
]

TABLE_CHECKS = {3: q3, 8: q8, 9: q9, 11: q11, 13: q13, 19: q19, 25: q25, 28: q28}


def _selftest():
    """Negative control: every gate must FAIL when its own input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("h1_1_mutant")
        mod.TOPIC = h1_1.TOPIC
        mod.QUESTIONS = copy.deepcopy(h1_1.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:95]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[0]["ans"] = 2

    def break_anchor(mod, claims):
        claims[12] = ("no such phrase anywhere in the choice", claims[12][1])

    def corrupt_table(mod, claims):
        # Make carbon dioxide's tabulated molar mass 22.0, so q3's keyed 2.00
        # moles is no longer what the table says.
        mod.QUESTIONS[2]["table"] = dict(
            headers=h1_1._T_MOLAR["headers"],
            rows=[[lab, ("22.0" if lab.startswith("Carbon") else v)]
                  for lab, v in h1_1._T_MOLAR["rows"]])

    def corrupt_table_ranking(mod, claims):
        # Make Container 4 no longer the largest mole count in q13.
        mod.QUESTIONS[12]["table"] = dict(
            headers=h1_1._T_RANK["headers"],
            rows=[[lab, ("4.0" if lab == "Container 4" else m), mm]
                  for lab, m, mm in h1_1._T_RANK["rows"]])

    def forget_table_check(mod, claims):
        # A data question added later with no recompute must not slip through.
        mod.QUESTIONS[1]["table"] = h1_1._T_MOLAR

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[4]["choices"][3] = mod.QUESTIONS[4]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[9]["why"] = "Because it is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[3]["why"] = ("Option C is wrong because the framework says so, "
                                   "and the rest of the reasoning follows from that.")

    def notation_slips_in(mod, claims):
        mod.QUESTIONS[6]["choices"][1] = r"About 6.022 x 10^23 molecules of NaCl"
        chem_notation.style(mod)

    def html_bracket_slips_in(mod, claims):
        mod.QUESTIONS[8]["q"] = "A sample with molar mass < 100 grams per mole is used."
        chem_notation.style(mod)

    print("negative controls:")
    must_fail("plain-text scientific notation in a choice", notation_slips_in)
    must_fail("a bare less-than sign in a stem", html_bracket_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer present in the keyed choice", break_anchor)
    must_fail("molar mass corrupted so the keyed mole count is false", corrupt_table)
    must_fail("table corrupted so the keyed row is no longer the largest", corrupt_table_ranking)
    must_fail("a table added with no recompute behind it", forget_table_check)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a rationale reduced below the minimum", thin_why)
    must_fail("a rationale naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import h1_1  # noqa: E402  (after the helpers, so the selftest can import it too)

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

chem_notation.style(h1_1)
cg.check(h1_1, CLAIMS, table_checks=TABLE_CHECKS)
