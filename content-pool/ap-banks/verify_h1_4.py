r"""Key audit for AP CHEMISTRY 1.4 Composition of Mixtures.

One (anchor, claim) per item, in module order. ``anchor`` must appear in the
KEYED choice and in no distractor; the exporter reshuffles the choices, so a
bare index is not a record of the key.

EVERY MASS SHARE, PURITY AND COMPONENT MASS KEYED HERE IS RECOMPUTED BELOW from
the item's own table, per SCIENCE_BRIEF.md's rule for quantitative Chemistry.
The purity checks in particular each recompute BOTH the correct comparison and
the specific short-cut the item's strongest distractor comes from -- dividing
the recovered element by the whole sample mass instead of by what a pure sample
would have yielded. If those two happened to coincide the item would have two
defensible answers, so the checks assert they do not.

WHAT THE KEYS REST ON
---------------------
Items 1, 4, 6, 9, 12, 13, 20, 22, 25, 27, 28 and 29 rest on EK 1.4.A.1: pure
substances contain atoms, molecules, or formula units of a single type, while
mixtures contain them of two or more types whose relative proportions can vary.

Items 3, 5, 10, 11, 14, 15, 17, 18, 21, 24, 26 and 30 rest on EK 1.4.A.2:
elemental analysis can be used to determine the relative numbers of atoms in a
substance and to determine its purity. Where a purity judgement needs a
baseline the claim also cites EK 1.3.A.2, the fixed mass ratio of a pure
sample, because that is what supplies the expected value; and item 24 cites EK
1.3.A.3 for the whole number atom ratio a pure compound must show.

Items 2, 7, 19 and 23 are pure percent-by-mass arithmetic on a stated mixture.
Items 8, 18 and 25 are the suggested skill 5.A items: which quantities the
problem actually requires.

NOTHING HERE ASSERTS MORE THAN THE FRAMEWORK. In particular no key claims that
elemental analysis can identify an unknown impurity, or that agreement between
two analyses proves a substance pure -- item 23 is written specifically to
refuse that inference.

DATA ITEMS: 2, 4, 5, 6, 9, 10, 11, 14 and 15 carry tables; all nine are
recomputed below.

NEGATIVE CONTROL: ``python3 verify_h1_4.py --selftest``.
"""
import sys

import cg_check as cg
import chem_notation

MASS = "Mass in the mixture (grams)"
VALUE = "Value"


def _shares(table):
    m = cg.col(table, MASS)
    total = sum(m)
    return dict(zip(cg.labels(table), [x / total * 100 for x in m])), total


def q2(table, item):
    pct, total = _shares(table)
    assert abs(total - 20.0) < 1e-9, f"the tabulated masses total {total}"
    assert abs(pct["Sodium chloride"] - 60.0) < 1e-9, \
        f"the sodium chloride share recomputes to {pct['Sodium chloride']}"
    other = cg.cell(table, "Sand", MASS)
    assert abs(cg.cell(table, "Sodium chloride", MASS) / other * 100 - 150.0) < 1e-9, \
        "the divide-by-the-other-component distractor should be 150"
    return f"12.0 of a total {total} grams is {pct['Sodium chloride']:.1f} percent"


def q4(table, item):
    pct, total = _shares(table)
    half = [lab for lab, v in pct.items() if abs(v - 50.0) < 1e-9]
    assert half == ["Substance B"], f"the components at fifty percent are {half}"
    a = cg.cell(table, "Substance A", MASS)
    c = cg.cell(table, "Substance C", MASS)
    assert abs((a + c) / total * 100 - 50.0) < 1e-9, (
        "the 'A and C together' distractor should also come to fifty, which is what "
        "obliges the item to ask for a SINGLE component -- and it does")
    return (f"shares are { {k: round(v, 1) for k, v in pct.items()} } percent, so exactly one "
            "single component reaches fifty")


def _purity(table, sample_row, recovered_row, baseline_row):
    sample = cg.cell(table, sample_row, VALUE)
    recovered = cg.cell(table, recovered_row, VALUE)
    baseline = cg.cell(table, baseline_row, VALUE)
    expected = sample * baseline / 100.0
    purity = recovered / expected * 100.0
    naive = recovered / sample * 100.0
    assert abs(purity - naive) > 5.0, \
        (f"the correct purity {purity} and the divide-by-sample-mass short cut {naive} are "
         "too close for the item to distinguish them")
    return purity, naive, expected


def q5(table, item):
    purity, naive, expected = _purity(
        table, "Mass of the sample taken",
        "Mass of calcium recovered from the sample",
        "Percent calcium by mass in pure calcium carbonate")
    assert abs(purity - 90.0) < 1e-9, f"the purity recomputes to {purity}, not 90.0"
    assert abs(naive - 36.0) < 1e-9, f"the short-cut distractor recomputes to {naive}"
    assert purity <= 100.0, "a purity above one hundred percent would mean the baseline is wrong"
    return (f"a pure 5.00 gram sample would give {expected} grams of calcium and 1.80 was "
            f"recovered, so the purity is {purity:.1f} percent against a short cut of {naive:.1f}")


def q6(table, item):
    vals = cg.col(table, "Percent carbon by mass")
    assert len(set(vals)) == len(vals), f"the four portions do not all differ: {vals}"
    assert max(vals) - min(vals) > 3.0, \
        f"the spread {max(vals) - min(vals)} is too small to be evidence of anything"
    assert all(24.0 <= v <= 32.0 for v in vals), (
        "the 'all between 24 and 32' distractor must be TRUE but irrelevant, which is "
        "what makes it a real distractor rather than filler")
    return (f"the four tabulated percentages {vals} are all different, spanning "
            f"{max(vals) - min(vals):.1f} points, which no set of portions of one pure "
            "substance would do")


def q9(table, item):
    kcl = cg.col(table, "Mass of potassium chloride added (grams)")
    suc = cg.col(table, "Mass of sucrose added (grams)")
    fracs = [a / (a + b) for a, b in zip(kcl, suc)]
    assert len(set(round(f, 9) for f in fracs)) == 3, f"the three proportions are not distinct: {fracs}"
    totals = [a + b for a, b in zip(kcl, suc)]
    assert len(set(totals)) == 1, (
        "every preparation has the same total mass, so the 'total mass 10.0' option is "
        "true but does not bear on whether the material is a mixture")
    return (f"the potassium chloride shares are {[round(f * 100) for f in fracs]} percent, three "
            f"different proportions of the same two substances at a constant total of {totals[0]} grams")


def q10(table, item):
    total = cg.cell(table, "Mass of the copper and copper(II) oxide mixture", VALUE)
    oxy = cg.cell(table, "Mass of oxygen recovered from the mixture", VALUE)
    pct = cg.cell(table, "Percent oxygen by mass in pure copper(II) oxide", VALUE)
    oxide = oxy / (pct / 100.0)
    assert abs(oxide - 8.0) < 1e-9, f"the mass of oxide recomputes to {oxide}, not 8.0"
    assert oxide < total, f"the oxide mass {oxide} cannot exceed the mixture mass {total}"
    return f"1.6 grams of oxygen at {pct} percent implies {oxide} grams of copper(II) oxide"


def q11(table, item):
    total = cg.cell(table, "Mass of the copper and copper(II) oxide mixture", VALUE)
    oxy = cg.cell(table, "Mass of oxygen recovered from the mixture", VALUE)
    pct = cg.cell(table, "Percent oxygen by mass in pure copper(II) oxide", VALUE)
    metal = total - oxy / (pct / 100.0)
    assert abs(metal - 2.0) < 1e-9, f"the mass of copper metal recomputes to {metal}, not 2.0"
    return f"{total} grams of mixture less {total - metal} grams of oxide leaves {metal} grams of metal"


def q14(table, item):
    first = cg.col(table, "Percent nitrogen by mass, first analysis")
    second = cg.col(table, "Percent nitrogen by mass, second analysis")
    agree = [lab for lab, a, b in zip(cg.labels(table), first, second) if abs(a - b) < 1e-9]
    assert agree == ["Solid E"], f"the solids whose two analyses agree are {agree}"
    others = [abs(a - b) for lab, a, b in zip(cg.labels(table), first, second)
              if lab != "Solid E"]
    assert min(others) > 3.0, "a second solid agrees closely enough to make the choice ambiguous"
    shared = [lab for lab, a in zip(cg.labels(table), first) if abs(a - 35.0) < 1e-9]
    assert len(shared) == 2, (
        "two solids should share a first-analysis value, so the item cannot be answered "
        "by reading one column alone")
    return (f"only Solid E repeats its value; the other three differ by {[round(d, 1) for d in others]} "
            "points, and two solids share a first-analysis value so one column is not enough")


def q15(table, item):
    sample = cg.cell(table, "Mass of ore sample", VALUE)
    iron = cg.cell(table, "Mass of iron recovered from the ore sample", VALUE)
    pct = cg.cell(table, "Percent iron by mass in the pure mineral being sought", VALUE)
    mineral = iron / (pct / 100.0)
    share = mineral / sample * 100.0
    naive = iron / sample * 100.0
    assert abs(share - 40.0) < 1e-9, f"the mineral share recomputes to {share}, not 40.0"
    assert abs(naive - 28.0) < 1e-9, f"the short-cut distractor recomputes to {naive}"
    assert abs(share - naive) > 5.0, "the correct answer and the short cut must be far apart"
    assert mineral <= sample, "the mineral cannot outweigh the ore it came from"
    return (f"14.0 grams of iron at {pct} percent implies {mineral} grams of mineral, which is "
            f"{share:.1f} percent of the {sample} gram ore, against a short cut of {naive:.1f}")


CLAIMS = [
 ("particles of a single type",
  "EK 1.4.A.1, near verbatim: pure substances contain atoms, molecules, or formula units of a single type, while mixtures contain them of two or more types whose relative proportions can vary. A compound of several elements is still one type of particle, which is where the element-counting option fails."),
 ("60.0 percent",
  "Recomputed in q2 above from the item's own table. A component's percent by mass is its own mass over the total mass of the mixture, and the check confirms that dividing by the other component instead produces one of the rejected values."),
 ("relative numbers of atoms in the substance and the purity",
  "EK 1.4.A.2, near verbatim: elemental analysis can be used to determine the relative numbers of atoms in a substance and to determine its purity. Identifying an unknown impurity by name is a stronger claim than the framework makes anywhere."),
 ("Substance B",
  "Recomputed in q4 above. The share of a component is its mass over the tabulated total, and the check confirms that the two smaller components do together reach half, which is why the item asks for a single component."),
 ("90.0 percent",
  "Recomputed in q5 above. EK 1.4.A.2 makes elemental analysis a purity test, and EK 1.3.A.2 supplies the baseline it is compared against: what a fully pure sample of that mass would have yielded. The check confirms the short cut of dividing by the sample mass gives a clearly different, rejected number."),
 ("differs from portion to portion",
  "Recomputed in q6 above: all four tabulated percentages differ, over a spread of several points. EK 1.4.A.1 permits that of a mixture and not of a pure substance, and EK 1.4.A.2 makes elemental analysis a legitimate basis for the judgement."),
 ("6.00 grams",
  "A percent by mass is a share of the whole sample, so the component's mass is 0.150 multiplied by 40.0 grams. What the rest of the mixture consists of does not enter the calculation, which is why the item can be answered without it."),
 ("mass of that component and the total mass",
  "Suggested skill 5.A asks which quantities the problem needs. A percent by mass is one mass divided by another, so those two masses are exactly sufficient, and volume, molar mass and temperature do not appear in the ratio."),
 ("proportions that vary from one preparation to the next",
  "Recomputed in q9 above: three distinct proportions of the same two substances. EK 1.4.A.1 makes the ability of relative proportions to vary the defining feature of a mixture, and the check also confirms that the equal total masses are a true but irrelevant feature of the table."),
 ("8.0 grams",
  "Recomputed in q10 above. Only one component of the mixture contains oxygen, so all the recovered oxygen came from it, and the tabulated percent oxygen in that pure component converts the oxygen mass into the component's mass."),
 ("2.0 grams",
  "Recomputed in q11 above as the remainder: the mixture mass less the mass of oxide implied by the recovered oxygen. Reporting the oxide mass rather than the remainder gives the rejected value."),
 ("keeps its own chemical formula",
  "EK 1.4.A.1 describes a mixture as containing atoms, molecules, or formula units of two or more types, which is a statement about which particles are present rather than about a new substance forming. The proportions are the only part the framework lets vary."),
 ("Solid E",
  "Recomputed in q14 above: only one solid returns the same percentage from two different portions, and the check confirms no second solid comes close. EK 1.4.A.1 allows a mixture's proportions to vary from place to place, so agreement between portions is the evidence a purity judgement rests on."),
 ("40.0 percent",
  "Recomputed in q15 above. The recovered iron all came from the mineral, so the tabulated percent iron in the pure mineral converts it into a mineral mass, which is then taken as a share of the ore. The check confirms the short cut of dividing iron by ore gives a different, rejected value."),
 ("compound must agree with each other, while the two",
  "EK 1.3.A.2 fixes the ratio of constituent masses for any pure sample of a compound, while EK 1.4.A.1 states that the relative proportions of a mixture can vary. Sample size affects neither, since a percent composition is a proportion."),
 ("not pure, since a pure sample would contain only the particle type",
  "EK 1.4.A.1 makes a pure substance one containing particles of a single type, and EK 1.4.A.2 makes elemental analysis a test of purity. An element the claimed compound does not contain is evidence that a second type of particle is present."),
 ("color of the sample",
  "Suggested skill 5.A asks which of the offered quantities the decision requires. EK 1.4.A.2 grounds a purity judgement in elemental analysis, which needs the elemental masses and the sample mass they are compared against; the framework connects no property of color to composition."),
 ("10.0 grams",
  "If 95.0 percent of the mass is the substance, the impurity is the remaining 5.00 percent of the 200 gram sample. Reading the stated percentage itself as a mass in grams gives the rejected value."),
 ("Seawater",
  "EK 1.4.A.1 defines a mixture as containing particles of two or more types whose relative proportions can vary, and every rejected option is described in the stem as containing a single type of particle throughout."),
 ("15.0 grams",
  "Substance A is 0.400 of 25.0 grams, which is 10.0 grams, so in a mixture of only two components the remaining 15.0 grams is substance B. Reporting A's mass rather than the remainder gives the rejected value."),
 ("lowers the measured percentage",
  "A percent by mass is the element's mass over the total mass, so a component adding to the denominator alone must reduce the ratio. EK 1.4.A.1 makes such a change in relative proportion available to a mixture and EK 1.4.A.2 is why it is detectable."),
 ("does not by itself prove the material is a pure substance",
  "EK 1.4.A.1 lets the proportions of a mixture vary but does not require them to vary within one well-stirred container. Agreement between portions is therefore evidence against non-uniformity, not evidence that only one type of particle is present -- and the framework licenses no stronger inference."),
 ("not a single pure compound",
  "EK 1.3.A.3 makes the atom ratio in a pure compound a whole number ratio, and EK 1.4.A.2 makes elemental analysis a purity test, so a reliable non-whole ratio indicates more than one type of particle. Scaling both molar masses would leave their ratio unchanged, so that explanation cannot account for it."),
 ("mass of the whole sample",
  "Suggested skill 5.A. A percentage is one mass divided by a total mass, so the total is the quantity still missing; a molar mass would be needed to convert to moles, which the question does not ask for."),
 ("relative proportions are free to vary",
  "EK 1.4.A.1 states that the relative proportions of the components of a mixture can vary, so two mixtures of the same components may differ in composition with neither analysis in error. The fixed-proportion requirement of EK 1.3.A.2 governs a pure compound instead."),
 ("one composition by mass that can be predicted from its formula",
  "EK 1.4.A.2 states that elemental analysis can determine purity, and EK 1.3.A.2 supplies the reason by fixing the ratio of constituent masses in any pure sample. The test is therefore a comparison against a predicted composition, not a direct count of impurity particles."),
 ("about 33.3 percent",
  "The share of a component is its own mass over the new total, so ten grams of that component in a thirty gram mixture is one third. EK 1.4.A.1 makes precisely this kind of change in relative proportion available to a mixture."),
 ("no single set of subscripts describes it",
  "EK 1.4.A.1 makes variable relative proportions the defining feature of a mixture, while a chemical formula records a fixed ratio. Having a definite total mass is a property of any sample and carries no implication of fixed proportions."),
 ("something to be compared against",
  "EK 1.4.A.2 lists determining relative numbers of atoms and determining purity as two separate uses of the technique, and the second requires a baseline; EK 1.3.A.2's fixed mass ratio for a pure sample is what supplies it. An analysis on its own reports composition, not purity."),
]

TABLE_CHECKS = {2: q2, 4: q4, 5: q5, 6: q6, 9: q9, 10: q10, 11: q11, 14: q14, 15: q15}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("h1_4_mutant")
        mod.TOPIC = h1_4.TOPIC
        mod.QUESTIONS = copy.deepcopy(h1_4.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:95]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[4]["ans"] = 1

    def break_anchor(mod, claims):
        claims[9] = ("no such phrase anywhere in the choice", claims[9][1])

    def corrupt_purity_baseline(mod, claims):
        mod.QUESTIONS[4]["table"] = dict(
            headers=h1_4._T_PURITY["headers"],
            rows=[["Mass of the sample taken", "5.00 grams"],
                  ["Mass of calcium recovered from the sample", "1.80 grams"],
                  ["Percent calcium by mass in pure calcium carbonate", "30.0 percent"]])

    def make_portions_agree(mod, claims):
        mod.QUESTIONS[5]["table"] = dict(
            headers=h1_4._T_PORTIONS["headers"],
            rows=[["Portion 1", "27.3"], ["Portion 2", "27.3"],
                  ["Portion 3", "27.3"], ["Portion 4", "27.3"]])

    def make_two_solids_agree(mod, claims):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h1_4._T_FOUR_SOLIDS["headers"],
            rows=[["Solid E", "35.0", "35.0"], ["Solid F", "35.0", "35.0"],
                  ["Solid G", "12.9", "19.7"], ["Solid H", "46.6", "41.2"]])

    def make_preparations_identical(mod, claims):
        mod.QUESTIONS[8]["table"] = dict(
            headers=h1_4._T_VARY["headers"],
            rows=[["Preparation 1", "5.0", "5.0"], ["Preparation 2", "4.0", "4.0"],
                  ["Preparation 3", "3.0", "3.0"]])

    def corrupt_ore(mod, claims):
        # 35.0 grams of iron from a 70 percent mineral needs 50.0 grams of mineral,
        # which is the whole ore -- the keyed 40.0 percent is then false.
        mod.QUESTIONS[14]["table"] = dict(
            headers=h1_4._T_ORE["headers"],
            rows=[["Mass of ore sample", "50.0 grams"],
                  ["Mass of iron recovered from the ore sample", "35.0 grams"],
                  ["Percent iron by mass in the pure mineral being sought", "70.0 percent"]])

    def forget_table_check(mod, claims):
        mod.QUESTIONS[0]["table"] = h1_4._T_MIX1

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[6]["choices"][4] = mod.QUESTIONS[6]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[19]["why"] = "Because."

    def letter_reference(mod, claims):
        mod.QUESTIONS[2]["why"] = ("Option E fails because the framework says so, and the "
                                   "remaining reasoning follows straight from that.")

    def notation_slips_in(mod, claims):
        mod.QUESTIONS[9]["choices"][2] = "About 2.0 x 10^1 grams of the oxide"
        chem_notation.style(mod)

    print("negative controls:")
    must_fail("plain-text scientific notation in a choice", notation_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer present in the keyed choice", break_anchor)
    must_fail("the purity baseline corrupted so the keyed purity is false",
              corrupt_purity_baseline)
    must_fail("the varying portions made to agree, refuting the key", make_portions_agree)
    must_fail("a second solid made to repeat its value, so the key is not unique",
              make_two_solids_agree)
    must_fail("the three preparations made identical in proportion", make_preparations_identical)
    must_fail("the ore data corrupted so the keyed mineral share is false", corrupt_ore)
    must_fail("a table added with no recompute behind it", forget_table_check)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a rationale reduced below the minimum", thin_why)
    must_fail("a rationale naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import h1_4  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

chem_notation.style(h1_4)
cg.check(h1_4, CLAIMS, table_checks=TABLE_CHECKS)
