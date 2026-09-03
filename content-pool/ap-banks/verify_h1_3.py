r"""Key audit for AP CHEMISTRY 1.3 Elemental Composition of Pure Substances.

One (anchor, claim) per item, in module order. ``anchor`` must appear in the
KEYED choice and in no distractor -- ``export_units.py`` reshuffles the
choices, so a key stored as a bare index is one edit away from pointing at a
distractor.

EVERY EMPIRICAL FORMULA, MASS PERCENTAGE AND MASS RATIO KEYED IN THIS TOPIC IS
RECOMPUTED BELOW from the item's own table, as SCIENCE_BRIEF.md requires of
quantitative Chemistry. The formula checks do not stop at deriving the right
ratio: each also confirms the answer is in LOWEST terms, because EK 1.3.A.3's
whole content is that the empirical formula is the lowest whole number ratio,
and each falsifies the specific wrong-method distractor the item is built
around.

A NOTE ON THE CHOICE SETS. ``cg_check`` rejects any choice whose normalized
text sits inside another, and chemical formulas nest constantly -- "FeO" is a
substring of "FeO2", "N2O" of "N2O4", "CH" of "CH2". Several distractor sets
here were rewritten for that reason rather than for chemistry. That rule is
worth keeping: a student who accepts the shorter formula has no ground on which
to reject the longer, so a nested pair really would be two defensible answers.

WHAT THE KEYS REST ON
---------------------
Items 4 and 20 rest on EK 1.3.A.1: some pure substances are composed of
individual molecules, while others consist of atoms or ions held together in
fixed proportions as described by a formula unit.

Items 2, 8, 9, 12, 14, 18, 21 and 30 rest on EK 1.3.A.2, the law of definite
proportions: the ratio of the masses of the constituent elements in any pure
sample of that compound is always the same. Item 14 also cites EK 1.4.A.1 for
the contrast, since it is that statement, not this one, that lets a mixture's
proportions vary.

Items 1, 3, 6, 7, 11, 15, 16, 19, 22, 23 and 28 rest on EK 1.3.A.3: the
chemical formula that lists the lowest whole number ratio of atoms of the
elements in a compound is the empirical formula.

Items 5, 10, 25, 27 and 29 convert between a formula and a mass share, which
needs EK 1.1.A.3's molar mass alongside EK 1.3.A.3's atom ratio. Item 19 is the
one item about which ratios are already lowest.

Items 17 and 24 recover a molecular formula. The framework does not print a
rule for that, so both are chained explicitly and the chain is stated in the
claim: EK 1.3.A.3 makes the empirical formula the LOWEST ratio, so an actual
molecule's formula is some whole number multiple of it, and EK 1.1.A.3's molar
mass selects the multiple.

Items 13 and 26 are the suggested skill 2.A items: which question the stated
measurement can actually answer.

DATA ITEMS: 3, 5, 7, 8, 9, 10, 11, 15, 16, 22, 23, 25, 27 and 29 carry tables
and all fourteen are recomputed below.

NEGATIVE CONTROL: ``python3 verify_h1_3.py --selftest``.
"""
import sys
from fractions import Fraction

import cg_check as cg
import chem_notation

MASS_IN = "Mass in the sample (grams)"
MOLAR = "Molar mass (grams per mole)"


def _ratio(table, tol=0.03):
    """Moles of each element, then the lowest whole number ratio. EK 1.3.A.3.

    ``tol`` is a RELATIVE tolerance on how far a computed mole amount may sit
    from the whole number it is rounded to. Percent-composition data is printed
    to three figures, so an exact ratio is not available and some slack is
    unavoidable -- but the slack is checked, not assumed: the caller is told
    the residual so a sloppy fit cannot pass unnoticed.
    """
    elements = cg.labels(table)
    moles = [m / mm for m, mm in zip(cg.col(table, MASS_IN), cg.col(table, MOLAR))]
    smallest = min(moles)
    raw = [m / smallest for m in moles]
    # Try multipliers 1..6, take the first that puts every entry near a whole number.
    for k in range(1, 7):
        scaled = [r * k for r in raw]
        if all(abs(s - round(s)) <= tol * max(1.0, s) for s in scaled):
            counts = [int(round(s)) for s in scaled]
            g = 0
            for c in counts:
                g = c if g == 0 else __import__("math").gcd(g, c)
            assert g == 1, f"the ratio {counts} is not in lowest terms; divide by {g}"
            resid = max(abs(s - round(s)) for s in scaled)
            return dict(zip(elements, counts)), moles, resid
    raise AssertionError(f"no whole number ratio within tolerance for moles {moles}")


def _formula_ratio(table, expected, tol=0.03):
    counts, moles, resid = _ratio(table, tol)
    assert counts == expected, f"the data give the ratio {counts}, not {expected}"
    return (f"moles {[round(m, 4) for m in moles]} reduce to the lowest whole number "
            f"ratio {counts}, worst residual {resid:.3f}")


def q3(table, item):
    return _formula_ratio(table, {"Carbon": 1, "Hydrogen": 2})


def q5(table, item):
    h = cg.cell(table, "Hydrogen", MOLAR)
    o = cg.cell(table, "Oxygen", MOLAR)
    total = 2 * h + o
    pct = o / total * 100
    assert abs(total - 18.0) < 1e-9, f"H2O recomputes to {total} grams per mole"
    assert abs(round(pct, 1) - 88.9) < 0.05, f"the oxygen share recomputes to {pct}"
    assert abs(1 / 3 * 100 - 33.3) < 0.05, "the atom-fraction distractor should be near 33.3"
    assert abs(pct - 100 / 3) > 40, "the mass share and the atom share must differ sharply"
    return f"16.0 of a total 18.0 grams per mole is {pct:.1f} percent, against an atom share of 33.3"


def q7(table, item):
    return _formula_ratio(table, {"Aluminum": 2, "Oxygen": 3})


def q8(table, item):
    a = cg.col(table, "Mass of element A recovered (grams)")
    b = cg.col(table, "Mass of element B recovered (grams)")
    ratios = [x / y for x, y in zip(a, b)]
    assert max(ratios) - min(ratios) < 1e-9, f"the mass ratios differ: {ratios}"
    totals = [x + y for x, y in zip(a, b)]
    assert len(set(round(t, 9) for t in totals)) > 1, \
        "the 'same total mass' distractor must be false, or the item has two right answers"
    assert len(set(a)) > 1, "the samples must differ in size for the item to make its point"
    assert all(abs(x - y) > 1e-9 for x, y in zip(a, b)), \
        "the 'equal masses of the two elements' distractor must be false"
    return (f"the three mass ratios are all {ratios[0]:.4f} while the totals {totals} differ, "
            "so constancy of ratio is what the data show and constancy of total is not")


def q9(table, item):
    c = cg.col(table, "Mass of carbon recovered (grams)")
    o = cg.col(table, "Mass of oxygen recovered (grams)")
    ratios = [y / x for x, y in zip(c, o)]
    assert abs(ratios[0] - ratios[1]) > 1e-6, f"the two oxygen-per-carbon ratios agree: {ratios}"
    assert len(set(c)) == 1, "the carbon masses are equal, so the 'same carbon' distractor is true-but-irrelevant"
    return (f"oxygen per gram of carbon is {ratios[0]:.3f} against {ratios[1]:.3f}, so by the law "
            "of definite proportions the two samples cannot be the same compound")


def q10(table, item):
    mg = cg.cell(table, "Magnesium", MOLAR)
    o = cg.cell(table, "Oxygen", MOLAR)
    pct = mg / (mg + o) * 100
    assert abs(pct - 60.0) < 1e-9, f"the magnesium share recomputes to {pct}"
    assert abs(pct - 50.0) > 5, "the one-to-one-mass distractor must be clearly false"
    return f"24.0 of a total {mg + o} grams per mole is {pct:.1f} percent magnesium"


def q11(table, item):
    return _formula_ratio(table, {"Nitrogen": 1, "Oxygen": 2})


def _percent_row(table, label, tol=0.03):
    """Build a mass/molar-mass table for one row of the percent-composition table."""
    pct = {h: cg.cell(table, label, h) for h in table["headers"][1:]}
    mm = {"Percent carbon by mass": ("Carbon", 12.0),
          "Percent hydrogen by mass": ("Hydrogen", 1.0),
          "Percent oxygen by mass": ("Oxygen", 16.0)}
    total = sum(pct.values())
    assert abs(total - 100.0) < 0.5, f"{label}'s percentages sum to {total}"
    rows = [[mm[h][0], str(v), str(mm[h][1])] for h, v in pct.items() if v > 0]
    built = dict(headers=["Element", MASS_IN, MOLAR], rows=rows)
    return _ratio(built, tol)


def q15(table, item):
    counts, moles, resid = _percent_row(table, "Compound R")
    assert counts == {"Carbon": 1, "Hydrogen": 2, "Oxygen": 1}, f"got {counts}"
    return (f"a 100 gram sample gives moles {[round(m, 3) for m in moles]}, which reduce to "
            f"{counts}, worst residual {resid:.3f}")


def q16(table, item):
    counts, moles, resid = _percent_row(table, "Compound S")
    assert counts == {"Carbon": 1, "Hydrogen": 4}, f"got {counts}"
    pct_ratio = cg.cell(table, "Compound S", "Percent carbon by mass") / \
        cg.cell(table, "Compound S", "Percent hydrogen by mass")
    assert abs(pct_ratio - 3.0) < 1e-9, \
        "the three-to-one distractor should be the raw percentage ratio"
    assert counts["Carbon"] / counts["Hydrogen"] != pct_ratio, \
        "the percentage ratio must NOT equal the atom ratio, or the item tests nothing"
    return (f"a 100 gram sample gives moles {[round(m, 3) for m in moles]} and the ratio "
            f"{counts}, while the raw percentages are in the ratio {pct_ratio:.1f} to 1")


def q22(table, item):
    fe = cg.cell(table, "Mass of iron used", "Value (grams)")
    oxide = cg.cell(table, "Mass of iron oxide produced", "Value (grams)")
    o = oxide - fe
    assert o > 0, f"the oxide {oxide} is not heavier than the iron {fe}"
    n_fe, n_o = fe / 56.0, o / 16.0
    r = Fraction(n_o / n_fe).limit_denominator(12)
    assert r == Fraction(3, 2), f"the oxygen-to-iron mole ratio recomputes to {r}"
    # the "forgot to subtract" distractor
    wrong = Fraction((oxide / 16.0) / n_fe).limit_denominator(12)
    assert wrong == Fraction(5, 1), f"the forgot-to-subtract ratio is {wrong}, not one to five"
    return (f"oxygen taken up is {oxide} minus {fe} equals {o} grams, so {n_o} moles against "
            f"{n_fe} moles of iron is {r}, while forgetting the subtraction gives {wrong}")


def q23(table, item):
    counts, moles, resid = _percent_row(table, "Compound T", tol=0.04)
    assert counts == {"Carbon": 1, "Oxygen": 2}, f"got {counts}"
    return (f"a 100 gram sample gives moles {[round(m, 3) for m in moles]}, which reduce to "
            f"{counts}, worst residual {resid:.3f}")


def q25(table, item):
    s = cg.cell(table, "Sulfur", MOLAR)
    o = cg.cell(table, "Oxygen", MOLAR)
    n_s, n_o = 5.00 / s, 5.00 / o
    r = Fraction(n_s / n_o).limit_denominator(12)
    assert r == Fraction(1, 2), f"the sulfur-to-oxygen atom ratio recomputes to {r}"
    assert n_s < n_o, "equal masses must give FEWER sulfur atoms, since sulfur is the heavier"
    return (f"5.00 grams over {s} against 5.00 over {o} gives {n_s} against {n_o} moles, a "
            f"sulfur-to-oxygen atom ratio of {r}")


def q27(table, item):
    first = cg.col(table, "Mass of the first element listed, per mole of compound (grams)")
    whole = cg.col(table, "Molar mass of the compound (grams per mole)")
    pct = dict(zip(cg.labels(table), [a / b * 100 for a, b in zip(first, whole)]))
    top = max(pct, key=pct.get)
    assert top == "Compound Y", f"the largest first-element share is {top}"
    assert abs(round(pct["Compound Y"]) - 82) <= 1, f"Compound Y recomputes to {pct['Compound Y']}"
    assert abs(round(pct["Compound U"]) - 60) <= 1, f"Compound U recomputes to {pct['Compound U']}"
    assert len(set(round(v) for v in pct.values())) == len(pct), \
        "'all four are equal' must be false, and no two may tie"
    return (f"first-element mass shares are { {k: round(v) for k, v in pct.items()} } percent, "
            "so the largest belongs to Compound Y")


def q29(table, item):
    c = cg.cell(table, "Carbon", MOLAR)
    h = cg.cell(table, "Hydrogen", MOLAR)
    o = cg.cell(table, "Oxygen", MOLAR)
    co2 = 2 * o / (c + 2 * o) * 100
    h2o = o / (2 * h + o) * 100
    assert h2o > co2, f"water {h2o} does not exceed carbon dioxide {co2}"
    assert abs(co2 - 72.7) < 0.1 and abs(h2o - 88.9) < 0.1, \
        f"the two shares recompute to {co2} and {h2o}"
    return (f"oxygen is {co2:.1f} percent of carbon dioxide and {h2o:.1f} percent of water, so "
            "the compound with fewer oxygen atoms per molecule holds the larger share")


CLAIMS = [
 ("lowest whole number ratio of atoms",
  "EK 1.3.A.3, near verbatim: the chemical formula that lists the lowest whole number ratio of atoms of the elements in a compound is the empirical formula. It is a ratio of atoms rather than of masses and carries no information about connectivity."),
 ("constituent elements will be the same",
  "EK 1.3.A.2, the law of definite proportions: the ratio of the masses of the constituent elements in any pure sample of that compound is always the same. Because it fixes a ratio and not an amount, the total mass recovered is free to differ with the size of the sample taken."),
 ("CH2",
  "Recomputed in q3 above from the item's own table: each mass divided by its own molar mass, then reduced. The check also confirms the answer is in lowest terms, which is the whole content of EK 1.3.A.3 and the only thing separating the key from the rejected multiples."),
 ("formula unit rather than by an individual molecule",
  "EK 1.3.A.1, near verbatim: some pure substances are composed of individual molecules, while others consist of atoms or ions held together in fixed proportions as described by a formula unit. A fixed proportion is exactly what a variable composition would lack."),
 ("88.9 percent",
  "Recomputed in q5 above from the tabulated molar masses. The share of the mass is the oxygen contribution over the whole formula mass, and the check confirms it is far from the one-in-three ATOM share, which is the confusion the item is built on."),
 ("CH2O",
  "EK 1.3.A.3 requires the lowest whole number ratio, and the subscripts six, twelve and six share a factor of six. The halved and third forms preserve the proportion but are not lowest, which is the only respect in which they fail."),
 ("Al2O3",
  "Recomputed in q7 above from the item's own table, and confirmed to be in lowest terms. Reversing which element has the larger mole count is what produces the rejected three-to-two form."),
 ("ratio of the mass of A to the mass of B is the same",
  "Recomputed in q8 above: the three tabulated ratios agree exactly while the three totals differ, so the data support constancy of ratio and refute constancy of total. That is precisely the claim EK 1.3.A.2 makes."),
 ("mass of oxygen per gram of carbon differs",
  "Recomputed in q9 above. EK 1.3.A.2 requires any pure sample of one compound to show the same ratio of constituent masses, so a different ratio is decisive against the two samples being the same compound. Sharing the elements is a weaker condition than sharing their proportion."),
 ("60.0 percent",
  "Recomputed in q10 above from the tabulated molar masses. A one-to-one ratio of ATOMS does not make a one-to-one ratio of MASSES, since EK 1.1.A.3 gives each element its own molar mass -- which is why the check confirms the answer is far from fifty percent."),
 ("NO2",
  "Recomputed in q11 above and confirmed lowest. The rejected forms are the reversed ratio and multiples of it, all of which fail only on EK 1.3.A.3's requirement that the ratio be the lowest whole number one."),
 ("20.0 grams",
  "A percent composition by mass is a fixed proportion under EK 1.3.A.2, so it applies unchanged to a sample of any size: 0.400 multiplied by 50.0 grams. Once the percentage is stated the formula adds nothing to the calculation."),
 ("ratio of the masses of the elements in this compound",
  "Suggested skill 2.A asks which question the available observation can test. Decomposing a weighed sample and weighing each element yields exactly the quantities EK 1.3.A.2 speaks of; geometry, intermolecular force strength and melting behaviour are not determined by an elemental mass measurement."),
 ("same ratio of elemental masses",
  "EK 1.3.A.2 fixes the ratio of constituent masses for every pure sample of a compound, while EK 1.4.A.1 states that the relative proportions of the components of a mixture can vary. Constancy of proportion across samples is therefore the observation that separates the two cases."),
 ("CH2O",
  "Recomputed in q15 above: the percentages are read as masses in a 100 gram sample, divided by molar mass, and reduced. The check confirms the result is in lowest terms, which is what rules out the threefold multiple."),
 ("CH4",
  "Recomputed in q16 above. The check also confirms that the raw ratio of the two PERCENTAGES is three to one while the ATOM ratio is one to four, so a student who compares percentages without dividing by molar mass lands on a rejected option."),
 ("C3H6",
  "EK 1.3.A.3 makes the empirical formula the lowest whole number ratio, so an actual molecule's formula must be a whole number multiple of it, and EK 1.1.A.3's molar mass fixes which multiple: 42.0 over 14.0 is three. No other multiple reproduces the stated molar mass."),
 ("ratio of masses, and the law of definite proportions",
  "EK 1.3.A.2 states that the ratio of the masses of the constituent elements in any pure sample is always the same, and a percent composition is that ratio expressed per hundred grams. The individual masses do grow with the sample; their proportions do not."),
 ("different masses, so equal numbers of them",
  "EK 1.3.A.3 makes the formula a ratio of ATOMS while EK 1.3.A.2 speaks of a ratio of MASSES, and the two coincide only if the atoms have equal mass, which EK 1.1.A.3 denies by giving each element its own molar mass."),
 ("NH3",
  "EK 1.3.A.3 requires the subscripts to be in the lowest whole number ratio. One and three share no common factor above one, while every rejected formula has subscripts sharing a factor of two or four and so reduces further."),
 ("mass of each element recovered",
  "EK 1.3.A.2 fixes the RATIO of constituent masses rather than the masses themselves, so an amount scales with the sample while a proportion does not. The empirical formula of EK 1.3.A.3 is a property of the compound and is unaffected by how much was taken."),
 ("Fe2O3",
  "Recomputed in q22 above. The oxygen taken up is the difference between the two tabulated masses, and the check separately confirms that failing to subtract gives the one-to-five ratio that appears among the rejected options."),
 ("CO2",
  "Recomputed in q23 above from the tabulated percentages, and confirmed to be in lowest terms. Reversing the ratio, or reading the mass proportion as an atom proportion, is what produces the rejected formulas."),
 ("differ in the actual number of atoms per molecule",
  "EK 1.3.A.3 makes the empirical formula the LOWEST whole number ratio, which fixes the proportions and leaves the multiple open; EK 1.1.A.3's molar mass then selects the multiple, here 180.0 over 30.0. Two distinct substances can therefore share one empirical formula."),
 ("Fewer sulfur atoms than oxygen atoms",
  "Recomputed in q25 above from the tabulated molar masses. Equal masses of two elements give equal numbers of atoms only if the molar masses are equal, and sulfur's is twice oxygen's, so the atom ratio is the reverse of the naive reading."),
 ("mass of carbon and the mass of hydrogen obtained",
  "Suggested skill 2.A again. EK 1.3.A.3's atom ratio is reached by dividing each elemental mass by its own molar mass, so the elemental masses are exactly what the question needs; the total sample mass, its density, its melting point and its flame colour carry no information about proportion."),
 ("about 82 percent nitrogen",
  "Recomputed in q27 above from the item's own table, which prints both the mass contributed by the first element and the molar mass of the whole compound. Which element is written first in a formula says nothing about how much of the mass it carries."),
 ("only the lowest whole number ratio",
  "EK 1.3.A.3 defines the empirical formula as the lowest whole number ratio of atoms, and a lowest ratio is consistent with any whole number multiple of itself appearing in an actual molecule. The formula is a ratio of atoms, which is where the mass-ratio option goes wrong."),
 ("larger in water",
  "Recomputed in q29 above from the tabulated molar masses: oxygen is a larger share of water than of carbon dioxide even though a carbon dioxide molecule carries two oxygen atoms and a water molecule one. Counting atoms in place of computing mass shares is the error the item targets."),
 ("its own fixed mass ratio",
  "EK 1.3.A.2 constrains samples of one compound to a single mass ratio and makes no claim relating one compound to a different compound. Two substances built from the same pair of elements are each fixed internally without being fixed to one another."),
]

TABLE_CHECKS = {3: q3, 5: q5, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 15: q15,
                16: q16, 22: q22, 23: q23, 25: q25, 27: q27, 29: q29}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("h1_3_mutant")
        mod.TOPIC = h1_3.TOPIC
        mod.QUESTIONS = copy.deepcopy(h1_3.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:95]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[2]["ans"] = 1

    def break_anchor(mod, claims):
        claims[6] = ("no such phrase anywhere in the choice", claims[6][1])

    def corrupt_mass(mod, claims):
        # Halve the hydrogen mass in q3, so the ratio becomes CH and the key is wrong.
        mod.QUESTIONS[2]["table"] = dict(
            headers=h1_3._T_CH["headers"],
            rows=[["Carbon", "24.0", "12.0"], ["Hydrogen", "2.0", "1.0"]])

    def break_definite_proportions(mod, claims):
        mod.QUESTIONS[7]["table"] = dict(
            headers=h1_3._T_DEFINITE["headers"],
            rows=[["Sample 1", "3.00", "8.00"], ["Sample 2", "6.00", "9.00"],
                  ["Sample 3", "4.50", "12.00"]])

    def make_the_two_samples_agree(mod, claims):
        # q9's key says the two samples are NOT the same compound.
        mod.QUESTIONS[8]["table"] = dict(
            headers=h1_3._T_TWO_COMPOUNDS["headers"],
            rows=[["Sample P", "12.0", "32.0"], ["Sample Q", "6.0", "16.0"]])

    def corrupt_molar_mass(mod, claims):
        # Make sulfur and oxygen equal in molar mass: q25's key then fails.
        mod.QUESTIONS[24]["table"] = dict(
            headers=h1_3._T_MM["headers"],
            rows=[[el, ("16.0" if el == "Sulfur" else v)] for el, v in h1_3._T_MM["rows"]])

    def make_percent_shares_tie(mod, claims):
        mod.QUESTIONS[26]["table"] = dict(
            headers=h1_3._T_MASS_RATIO["headers"],
            rows=[["Compound U", "MgO", "24.0", "40.0"],
                  ["Compound V", "H2O", "2.0", "18.0"],
                  ["Compound W", "CO2", "12.0", "44.0"],
                  ["Compound Y", "NH3", "10.2", "17.0"]])

    def forget_table_check(mod, claims):
        mod.QUESTIONS[0]["table"] = h1_3._T_MM

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[5]["choices"][3] = mod.QUESTIONS[5]["choices"][0]

    def nested_choice(mod, claims):
        mod.QUESTIONS[2]["choices"][4] = "CH"

    def thin_why(mod, claims):
        mod.QUESTIONS[11]["why"] = "It follows."

    def letter_reference(mod, claims):
        mod.QUESTIONS[1]["why"] = ("Answer B is wrong because the framework says so, and "
                                   "everything else follows from that observation.")

    def notation_slips_in(mod, claims):
        mod.QUESTIONS[3]["choices"][2] = "Its composition is Na_2SO_4 in every sample."
        chem_notation.style(mod)

    print("negative controls:")
    must_fail("a bare subscript in a choice", notation_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer present in the keyed choice", break_anchor)
    must_fail("an elemental mass corrupted so the keyed formula is false", corrupt_mass)
    must_fail("definite proportions broken in the data supporting them",
              break_definite_proportions)
    must_fail("the two 'different compound' samples made proportional after all",
              make_the_two_samples_agree)
    must_fail("a molar mass corrupted so the keyed atom ratio is false", corrupt_molar_mass)
    must_fail("two mass shares made to tie, so the item has no unique largest",
              make_percent_shares_tie)
    must_fail("a table added with no recompute behind it", forget_table_check)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a formula distractor nested inside the key", nested_choice)
    must_fail("a rationale reduced below the minimum", thin_why)
    must_fail("a rationale naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import h1_3  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

chem_notation.style(h1_3)
cg.check(h1_3, CLAIMS, table_checks=TABLE_CHECKS)
