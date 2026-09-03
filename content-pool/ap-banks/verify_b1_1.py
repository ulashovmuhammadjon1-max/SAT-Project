"""Key audit for AP BIOLOGY 1.1 Structure of Water and Hydrogen Bonding.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is shared with the social science banks (``cg_check.py``);
nothing in it is specific to that subject. It cannot tell whether the biology is
right. That is gated by the CLAIMS text below and by the rule in
SCIENCE_BRIEF.md that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
Items 1, 2, 16, 23, 24 and 29 rest on EK 1.1.A.1 i, which states that water has
polarity because of polar covalent bonds between hydrogen and oxygen WITHIN
water molecules, and that this polarity contributes to hydrogen bonding between
and within biological molecules. The distinction between the intramolecular
covalent bond and the intermolecular hydrogen bond is the framework's own.

Items 4, 12, 21, 25, 26 and 30 rest on EK 1.1.A.1 ii, the high specific heat
capacity and the maintenance of homeostatic body temperature. Items 5, 6, 13,
22 and 25 rest on EK 1.1.A.1 iii, the high heat of vaporization and evaporative
cooling.

Items 7 to 11, 14, 17, 18, 20, 27 and 28 rest on EK 1.1.A.2: the hydrogen bonds
between adjacent polar water molecules result in cohesion, adhesion, and
surface tension. The framework names those three and does not define them.
Where an item turns on which of the three is acting (9, 14, 20), the key rests
only on cohesion being water holding to water and adhesion being water holding
to another surface -- the minimum content required for the framework to list
them as separate results.

Item 19 rests on the opening sentence of EK 1.1.A.1: living systems depend on
the properties of water to sustain life.

DATA ITEMS: 3, 6, 10, 12, 13, 15, 17 and 26 carry tables. Each keyed conclusion
is recomputed below from that table alone, and each check also falsifies the
distractors against the same numbers. No item asks a student to recall a
measured value.

NEGATIVE CONTROL: run ``python3 verify_b1_1.py --selftest`` to corrupt a key, an
anchor and a table cell on purpose and confirm the checks fail.
"""
import re
import sys

import cg_check as cg

# SCIENCE_BRIEF.md: Biology is exported as prose. export_units.py does not typeset
# it, so a backslash macro would reach a student as literal text, and a
# digit-hyphen-digit or digit-slash-digit range is what the converter mangled on
# the prose subjects. Explicit lookarounds, never \b beside a digit.
_BANNED = [
    (re.compile(r"\\"), "a backslash: Biology is not typeset, so LaTeX would print raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\$"), "a dollar sign, which the converter reads as inline math"),
]


def style(module):
    """No typeset notation anywhere in the module's student-facing text."""
    for i, item in enumerate(module.QUESTIONS, 1):
        texts = [item["q"], item["why"]] + list(item["choices"])
        t = item.get("table")
        if t:
            texts += [str(h) for h in t["headers"]] + [str(c) for r in t["rows"] for c in r]
        for text in texts:
            for pat, msg in _BANNED:
                hit = pat.search(text)
                assert not hit, f"{module.TOPIC[0]} q{i}: {msg} -- {hit.group(0)!r} in {text[:70]!r}"
    print(f"OK  {module.TOPIC[0]} notation: no typeset markup in "
          f"{len(module.QUESTIONS)} questions.")

SH = "Specific heat capacity (joules per gram per degree Celsius)"
HV = "Heat of vaporization (joules per gram)"
LOW = "Lowest air temperature recorded in one day (degrees Celsius)"
HIGH = "Highest air temperature recorded in the same day (degrees Celsius)"
LOST = "Water lost from the skin in one hour (grams)"
CORE = "Core body temperature after one hour (degrees Celsius)"
BORE = "Inside diameter (millimeters)"
RISE = "Height water rose inside the tube (millimeters)"
ST = "Surface tension (millinewtons per meter)"


def q3(table, item):
    caps = dict(zip(cg.labels(table), cg.col(table, SH)))
    hottest = max(caps, key=caps.get)
    assert hottest == "Water", f"largest specific heat capacity is {hottest}"
    # For fixed mass and fixed heat, the temperature rise goes as 1/capacity, so
    # every other substance must rise MORE than water does.
    for lab, c in caps.items():
        if lab != "Water":
            assert 1.0 / c > 1.0 / caps["Water"], f"{lab} would not rise more than water"
    return (f"water 4.18 is the largest of {sorted(caps.values())}, so for equal mass and "
            "equal heat every other substance rises more")


def q6(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, HV)))
    best = max(vals, key=vals.get)
    assert best == "Water", f"largest heat of vaporization is {best}"
    assert vals["Water"] > 2 * max(v for k, v in vals.items() if k != "Water"), \
        "water should be more than twice the next largest, as the stem's premise implies"
    return (f"water 2,260 joules per gram is the largest value in the table and more than "
            f"twice the next, {sorted(vals.values())[-2]}")


def q10(table, item):
    bores = cg.col(table, BORE)
    rises = cg.col(table, RISE)
    pairs = sorted(zip(bores, rises))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"rise must fall as bore grows; got {pairs}"
    # the 'proportional to diameter' distractor must be false on these numbers
    ratios = [r / b for b, r in pairs]
    assert len(set(round(x, 6) for x in ratios)) > 1, "rise/diameter is constant, so 'proportional' would be true"
    return (f"sorted by bore the rises are {[r for _, r in pairs]}, strictly decreasing, "
            "and rise divided by diameter is not constant")


def q12(table, item):
    rng = {lab: cg.cell(table, lab, HIGH) - cg.cell(table, lab, LOW)
           for lab in cg.labels(table)}
    shore, inland = rng["Lakeshore station"], rng["Station 40 km inland"]
    assert shore < inland, f"lakeshore range {shore} is not smaller than inland {inland}"
    assert cg.cell(table, "Station 40 km inland", HIGH) > cg.cell(table, "Lakeshore station", HIGH), \
        "'inland never warmer' must be false"
    assert cg.cell(table, "Lakeshore station", LOW) > cg.cell(table, "Station 40 km inland", LOW), \
        "'lakeshore had the lower minimum' must be false"
    return (f"lakeshore range {shore} degrees against inland {inland} degrees, and the "
            "two comparison distractors are false on the same four values")


def q13(table, item):
    lost = {lab: cg.cell(table, lab, LOST) for lab in cg.labels(table)}
    temp = {lab: cg.cell(table, lab, CORE) for lab in cg.labels(table)}
    wetter = max(lost, key=lost.get)
    cooler = min(temp, key=temp.get)
    assert wetter == cooler, f"the group losing most water ({wetter}) is not the coolest ({cooler})"
    assert temp["Sweating allowed"] != temp["Sweating blocked"], "'same temperature' must be false"
    assert lost["Sweating allowed"] > lost["Sweating blocked"], \
        "'sweating group lost less water' must be false"
    return (f"{wetter} lost the most water and ended coolest at {temp[cooler]} degrees; "
            "the equal-temperature and less-water readings are both false")


def q15(table, item):
    joules = cg.cell(table, "Water", SH) * 100 * 10
    assert abs(joules - 4180) < 1e-6, f"recomputed {joules}, not 4,180"
    for wrong in (418.0, 41.8):
        assert abs(joules - wrong) > 1, "a decimal-shift distractor must not equal the key"
    sand = cg.cell(table, "Dry sand", SH) * 100 * 10
    assert abs(sand - 830) < 1e-6 and abs(sand - joules) > 1, \
        "the 830 distractor must come from a different substance in the same table"
    return "4.18 times 100 grams times 10 degrees is 4,180 joules; 830 is the same product for dry sand"


def q17(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, ST)))
    assert max(vals, key=vals.get) == "Water", "water must hold the largest surface tension"
    assert vals["Ethanol"] < vals["Water"], "'ethanol higher than water' must be false"
    assert abs(vals["Hexane"] - vals["Water"]) > 10, "'hexane nearly equal to water' must be false"
    assert vals["Glycerol"] < 2 * vals["Water"], "'glycerol more than twice water' must be false"
    assert any(v < 50 for v in vals.values()), "'every value above 50' must be false"
    return (f"water 72.8 is the maximum of {sorted(vals.values())}; each of the four "
            "distractors is false against those same values")


def q26(table, item):
    heat, mass = 8360.0, 200.0
    d_water = heat / (mass * cg.cell(table, "Water", SH))
    d_iron = heat / (mass * cg.cell(table, "Iron", SH))
    assert abs(d_water - 10) < 0.1, f"water change recomputes to {d_water}"
    assert 90 < d_iron < 96, f"iron change recomputes to {d_iron}"
    assert d_iron > d_water, "iron must warm more than water"
    return (f"8,360 joules over 200 grams gives {d_water:.1f} degrees for water and "
            f"{d_iron:.0f} degrees for iron")


CLAIMS = [
 ("polar covalent bonds",
  "EK 1.1.A.1 i, near verbatim: water has polarity because of the formation of polar covalent bonds between hydrogen and oxygen within water molecules. A covalent bond is a shared pair, and a polar one is shared unequally, which is what leaves partial rather than whole charges."),
 ("hydrogen bonding between biological molecules",
  "EK 1.1.A.1 i states that this polarity contributes to hydrogen bonding between and within biological molecules. The four rejected options all name covalent bonding events, which do not depend on water being polar."),
 ("Water",
  "Recomputed in q3 above. Specific heat capacity is heat per gram per degree, so for equal masses and equal heat the temperature rise varies inversely with capacity, and water holds the largest capacity in the table."),
 ("high specific heat capacity",
  "EK 1.1.A.1 ii: water has a high specific heat capacity, which allows for the maintenance of homeostatic body temperature within living organisms. That is the property that resists temperature change; the heat of vaporization acts only where water is leaving as vapor."),
 ("high heat of vaporization",
  "EK 1.1.A.1 iii: water has a high heat of vaporization, which allows for the evaporative cooling of the surrounding environment and, in living organisms, for body temperature to be maintained. The cooling comes from the heat carried off by escaping molecules."),
 ("Water",
  "Recomputed in q6 above. Heat of vaporization is heat absorbed per gram converted to vapor, so the largest tabulated value removes the most heat per gram, and water's is the largest by more than a factor of two."),
 ("between adjacent polar water molecules",
  "EK 1.1.A.2, near verbatim: the hydrogen bonds between adjacent polar water molecules result in cohesion, adhesion, and surface tension. The covalent bonds of EK 1.1.A.1 i lie inside a single molecule and are not what links one molecule to the next."),
 ("producing surface tension",
  "EK 1.1.A.2 names surface tension as one of the three results of hydrogen bonding between adjacent water molecules. Resistance at the surface is a mechanical consequence of that attraction, not of a thermal property such as specific heat capacity."),
 ("Adhesion pulls water up along the glass",
  "EK 1.1.A.2 names cohesion and adhesion as separate results of hydrogen bonding. Adhesion is water holding to another surface, so it acts between water and glass; cohesion is water holding to water, so it is what keeps the rising column unbroken. The rejected option swaps the two."),
 ("narrower the tube",
  "Recomputed in q10 above: sorting the three tubes by bore leaves the rise strictly decreasing, and the ratio of rise to diameter is not constant, so the proportionality option is false on the same data."),
 ("would all be lost",
  "Chaining EK 1.1.A.1 i to EK 1.1.A.2. Polarity is the stated source of hydrogen bonding, and hydrogen bonding between adjacent molecules is the stated source of all three of cohesion, adhesion and surface tension, so removing the polarity removes the cause of the three together."),
 ("smaller than the range inland",
  "Recomputed in q12 above from the four tabulated temperatures. A large body of water resists temperature change for a given input of heat, which is the property EK 1.1.A.1 ii names."),
 ("lower core body temperature",
  "Recomputed in q13 above: the group that lost the most water from the skin ended coolest. EK 1.1.A.1 iii attributes evaporative cooling and the maintenance of body temperature to the high heat of vaporization of water."),
 ("hold to one another and to the vessel walls",
  "EK 1.1.A.2 attributes cohesion and adhesion to hydrogen bonds between adjacent polar water molecules, and those two attractions are exactly what the keyed explanation uses. The framework attributes no repulsion, no intermolecular covalent bonding, and no lifting effect of stored heat to water."),
 ("4,180 joules",
  "Recomputed in q15 above from the tabulated capacity: 4.18 times 100 grams times 10 degrees. The 830 distractor is the same product formed with dry sand's capacity from the same table."),
 ("second student is correct",
  "EK 1.1.A.1 i places the polar covalent bonds within water molecules and EK 1.1.A.2 places the hydrogen bonds between adjacent water molecules. The two bond types therefore act at different levels, and neither can be substituted for the other."),
 ("higher surface tension than any other liquid",
  "Recomputed in q17 above: water's value is the maximum, and each of the four rejected statements is checked false against the same tabulated values."),
 ("unusually high surface tension",
  "EK 1.1.A.2 traces surface tension to attraction between adjacent molecules, and vaporization requires that attraction to be overcome. Unusually large values of both therefore point to unusually strong intermolecular attraction, whereas being colorless, dissolving a salt, or expanding on heating are shared by liquids with no such bonding."),
 ("depend on those properties to sustain life",
  "EK 1.1.A.1, the opening sentence: living systems depend on the properties of water to sustain life. Water supplies no carbon skeleton, and EK 1.3.A.1 makes it a reactant in hydrolysis rather than an inert medium."),
 ("water to water is strong",
  "EK 1.1.A.2 names cohesion, water holding to water, and adhesion, water holding to another surface, as separate results of hydrogen bonding. A drop beads when the first outweighs the second and spreads when the second outweighs the first."),
 ("Specific heat capacity",
  "EK 1.1.A.1 ii names the high specific heat capacity as the property behind resistance to temperature change, and specific heat capacity is heat per gram per degree of change. The rejected option attaches that same definition to the heat of vaporization, which is heat per gram converted to vapor."),
 ("moving dry air",
  "The claim under test concerns the effect of evaporation, so the treatments must differ in how readily water can evaporate while everything else is held constant. Air already saturated with water vapor suppresses net evaporation; dry moving air promotes it. EK 1.1.A.1 iii is the statement being tested."),
 ("Hydrogen bonds between adjacent polar water molecules",
  "EK 1.1.A.2 identifies the attraction between adjacent polar water molecules as hydrogen bonding. Peptide bonds belong to proteins under EK 1.7.A.1, and water contains no hydrocarbon region for a nonpolar interaction."),
 ("Water is polar",
  "EK 1.1.A.1 i states that the polarity of water contributes to hydrogen bonding between and within biological molecules, which is the interaction an exposed charged or polar side group makes with the surrounding water. The thermal properties do not determine where a side group sits."),
 ("Specific heat capacity buffers",
  "EK 1.1.A.1 ii assigns the maintenance of homeostatic body temperature to the high specific heat capacity, and EK 1.1.A.1 iii assigns evaporative cooling to the high heat of vaporization. The rejected options swap the two or substitute the mechanical properties of EK 1.1.A.2."),
 ("93 degrees and the water",
  "Recomputed in q26 above: heat divided by mass and by specific heat capacity gives the change, which is 10 degrees for water and about 93 for iron on the tabulated capacities. This is the quantitative form of the claim in EK 1.1.A.1 ii."),
 ("weaker than a covalent bond",
  "EK 1.1.A.2 makes hydrogen bonds present in liquid water and collectively responsible for cohesion, adhesion and surface tension, while EK 1.1.A.1 i reserves the covalent bond for the link holding hydrogen to oxygen inside a molecule. If a hydrogen bond fused two molecules the liquid would no longer consist of water molecules."),
 ("lower surface tension than water",
  "EK 1.1.A.2 traces surface tension to hydrogen bonds between adjacent polar molecules, so a liquid whose molecules form none has less intermolecular attraction to overcome at its surface. Nothing in the framework makes surface tension a function of mass."),
 ("Dashed lines are hydrogen bonds",
  "EK 1.1.A.1 i places polar covalent bonds between the hydrogen and oxygen atoms within a molecule, and EK 1.1.A.2 places hydrogen bonds between adjacent molecules, which is exactly the division the two kinds of line follow in the description."),
 ("large input of heat is needed for each degree",
  "Specific heat capacity is heat per gram per degree of temperature change, so a large value slows the change without abolishing it. EK 1.1.A.1 ii claims only that the property allows homeostatic body temperature to be maintained."),
]

TABLE_CHECKS = {3: q3, 6: q6, 10: q10, 12: q12, 13: q13, 15: q15, 17: q17, 26: q26}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b1_1_mutant")
        mod.TOPIC = b1_1.TOPIC
        mod.QUESTIONS = copy.deepcopy(b1_1.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[0]["ans"] = 1

    def break_anchor(mod, claims):
        claims[6] = ("no such phrase anywhere", claims[6][1])

    def corrupt_table(mod, claims):
        # make ethanol out-boil water, so q6's key is no longer the largest value
        mod.QUESTIONS[5]["table"] = dict(
            headers=b1_1._T_VAPORIZATION["headers"],
            rows=[[lab, ("9,999" if lab == "Ethanol" else v)]
                  for lab, v in b1_1._T_VAPORIZATION["rows"]])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[0]["choices"][4] = mod.QUESTIONS[0]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[9]["why"] = "Because it is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[3]["why"] = ("Option B is wrong because the framework says so and "
                                   "the rest follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[2]["choices"][1] = "Ethanol, at \\frac{1}{2} the capacity of water"
        style(mod)

    print("negative controls:")
    must_fail("a backslash macro in a choice", latex_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer in the keyed choice", break_anchor)
    must_fail("table value corrupted so the keyed conclusion is false", corrupt_table)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a why reduced below the minimum", thin_why)
    must_fail("a why naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import b1_1  # noqa: E402  (after the helpers, so the selftest can import it too)

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b1_1)
cg.check(b1_1, CLAIMS, table_checks=TABLE_CHECKS)
