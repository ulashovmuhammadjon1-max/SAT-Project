"""Key audit for AP BIOLOGY 1.5 Lipids.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
EK 1.5.A.1 -- lipids are typically nonpolar, hydrophobic molecules whose
structure and function are derived from the way their subcomponents are
assembled; fatty acids can be described as saturated or unsaturated -- carries
items 1, 20 and 25. Its four sub-points carry the rest of the first half:
i (saturated means only single bonds between carbon atoms) items 2 and 7;
ii (at least one double bond, which causes the chain to kink) items 3, 8 and 25;
iii (more double bonds, more unsaturated) items 4 and 6;
iv (more unsaturated, more liquid at room temperature) items 5, 9, 10, 11, 12,
19, 29 and 30.

EK 1.5.A.2 and its sub-points carry the second half:
i (fats: energy storage, support of cell function, and in some cases insulation
that helps keep mammals warm) items 13, 27 and 28;
ii (steroids are hormones supporting growth and development, energy metabolism
and homeostasis) items 14, 17 and 23;
iii (cholesterol provides essential structural stability to animal cell
membranes) items 15, 21 and 22;
iv (phospholipids group together to form the lipid bilayers found in plasma and
cell membranes) items 16 and 18.

Item 26 chains to EK 1.2.A.1 ii for the phosphorus in a phospholipid. Item 24 is
an experimental-design item and rests on what a control is, not on content.

Items 9, 12, 19, 29 and 30 CHAIN iii to iv -- double bond count to unsaturation
to physical state -- and each claim says so.

DATA ITEMS: 6 to 12 and 21 to 24 carry tables. Every keyed conclusion is
recomputed below from the table alone. Every table is labelled hypothetical in
its stem or headers, because the CED prints no melting point, no fatty acid name
and no measured membrane value; nothing here is a remembered number.

NEGATIVE CONTROL: ``python3 verify_b1_5.py --selftest`` corrupts a key, an
anchor, two table cells and the notation on purpose and confirms each fails.
"""
import re
import sys

import cg_check as cg

_BANNED = [
    (re.compile(r"\\"), "a backslash: Biology is not typeset, so LaTeX would print raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\$"), "a dollar sign, which a converter reads as inline math"),
]


def style(module):
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


DB = "Number of carbon to carbon double bonds in each fatty acid tail"
MP = "Melting point (degrees Celsius)"
CHOL = "Cholesterol as a percentage of the membrane lipid"
FORCE = "Force needed to rupture the membrane (arbitrary units)"
DOSE = "Steroid hormone supplied (units per day)"
GAIN = "Mean gain in body length over eight weeks (millimeters)"
ROOM = 22.0


def q6(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, DB)))
    most = max(vals, key=vals.get)
    assert most == "Lipid 4", f"the largest double bond count is {most}"
    assert list(vals.values()).count(vals[most]) == 1, "the maximum must be unique to rank them"
    return f"double bond counts are {vals}; the unique maximum is {most}"


def q7(table, item):
    zeros = [lab for lab, v in zip(cg.labels(table), cg.col(table, DB)) if v == 0]
    assert zeros == ["Lipid 1"], f"rows with no carbon to carbon double bond: {zeros}"
    return f"exactly one row records zero double bonds, {zeros[0]}, which is EK 1.5.A.1 i's saturated case"


def q8(table, item):
    kinked = sorted(lab for lab, v in zip(cg.labels(table), cg.col(table, DB)) if v > 0)
    assert kinked == ["Lipid 2", "Lipid 3", "Lipid 4"], f"rows with at least one double bond: {kinked}"
    return f"three rows record at least one double bond and so are kinked: {kinked}"


def q9(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, DB)))
    most = max(vals, key=vals.get)
    assert most == "Lipid 4", f"the most unsaturated row is {most}"
    assert len(set(vals.values())) == len(vals), "'all equally liquid' must be false"
    return f"the most unsaturated row is {most} and no two rows share a count, so they are not alike"


def q10(table, item):
    liquid = sorted(lab for lab in cg.labels(table) if cg.cell(table, lab, MP) < ROOM)
    assert liquid == ["Lipid Q", "Lipid R", "Lipid S"], f"rows melting below {ROOM}: {liquid}"
    solid = [lab for lab in cg.labels(table) if cg.cell(table, lab, MP) >= ROOM]
    assert len(solid) == 1, f"exactly one row should melt above room temperature, got {solid}"
    return f"{liquid} melt below {ROOM:.0f} degrees and {solid[0]} melts above it"


def q11(table, item):
    pairs = sorted(zip(cg.col(table, DB), cg.col(table, MP)))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"melting point must fall as double bonds rise; got {pairs}"
    return f"sorted by double bonds the melting points are {[m for _, m in pairs]}, strictly falling"


def q12(table, item):
    pairs = sorted(zip(cg.col(table, DB), cg.col(table, MP)))
    assert max(d for d, _ in pairs) < 4, "the predicted lipid must carry more double bonds than any row"
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        "the trend must be monotone for the extrapolation to be the keyed one"
    lowest = min(m for _, m in pairs)
    return (f"the table tops out at {max(d for d, _ in pairs):.0f} double bonds with a "
            f"falling trend and a minimum of {lowest:.0f} degrees, so four bonds extrapolates below it")


def q21(table, item):
    pairs = sorted(zip(cg.col(table, CHOL), cg.col(table, FORCE)))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"force must rise with cholesterol; got {pairs}"
    assert pairs[0][1] == min(f for _, f in pairs), "the zero-cholesterol row must be the weakest"
    return f"sorted by cholesterol the forces are {[f for _, f in pairs]}, strictly rising from the zero row"


def q22(table, item):
    hi = [lab for lab in cg.labels(table) if cg.cell(table, lab, CHOL) == 20]
    lo = [lab for lab in cg.labels(table) if cg.cell(table, lab, CHOL) == 0]
    assert len(hi) == 1 and len(lo) == 1, f"the stem's two preparations matched {hi} and {lo}"
    ratio = cg.cell(table, hi[0], FORCE) / cg.cell(table, lo[0], FORCE)
    assert 1.75 <= ratio <= 2.5, f"the ratio recomputes to {ratio}, not near two"
    return f"{cg.cell(table, hi[0], FORCE):.0f} over {cg.cell(table, lo[0], FORCE):.0f} is {ratio:.2f}, near two"


def q23(table, item):
    pairs = sorted(zip(cg.col(table, DOSE), cg.col(table, GAIN)))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"gain must rise with dose; got {pairs}"
    assert pairs[0][1] > 0, "'only the untreated group gained length' must be false in the other direction too"
    return f"sorted by dose the mean gains are {[g for _, g in pairs]}, strictly rising"


def q24(table, item):
    zeros = [lab for lab in cg.labels(table) if cg.cell(table, lab, DOSE) == 0]
    assert zeros == ["Group 1"], f"groups receiving no steroid: {zeros}"
    return f"exactly one group was supplied zero units per day, {zeros[0]}, which is the untreated baseline"


CLAIMS = [
 ("typically nonpolar, hydrophobic molecules",
  "EK 1.5.A.1, near verbatim: lipids are typically nonpolar, hydrophobic molecules whose structure and function are derived from the way their subcomponents are assembled. Polar, hydrophilic and charged are the opposite property, and the framework does not describe lipids as polymers of a repeating monomer."),
 ("only single bonds between its carbon atoms",
  "EK 1.5.A.1 i: saturated fatty acids contain only single bonds between carbon atoms. Carrying at least one double bond is EK 1.5.A.1 ii's definition of unsaturated, so the two are the halves of one distinction."),
 ("causes the carbon chain to kink",
  "EK 1.5.A.1 ii: unsaturated fatty acids contain at least one double bond between carbon atoms, which causes the carbon chain to kink. The framework attaches no change of polarity, of hydrophobicity or of class to that bond."),
 ("belongs to the more unsaturated lipid",
  "EK 1.5.A.1 iii: the more double bonds in a fatty acid tail, the more unsaturated the lipid becomes. EK 1.5.A.1 i defines saturated by the absence of such bonds, so the rejected saturation readings invert the framework's relation."),
 ("the more liquid it is at room temperature",
  "EK 1.5.A.1 iv, near verbatim: the more unsaturated a lipid is, the more liquid it is at room temperature."),
 ("Lipid 4",
  "Recomputed in q6 above: the tabulated double bond count has a unique maximum, and EK 1.5.A.1 iii makes that count the measure of how unsaturated a lipid is."),
 ("Lipid 1",
  "Recomputed in q7 above: exactly one row records zero carbon to carbon double bonds, which is what EK 1.5.A.1 i means by containing only single bonds between carbon atoms."),
 ("Lipid 2, Lipid 3 and Lipid 4",
  "Recomputed in q8 above: three rows record at least one double bond. EK 1.5.A.1 ii attaches the kink to the presence of such a bond, so the zero row is the only unkinked one."),
 ("Lipid 4",
  "Recomputed in q9 above, chaining EK 1.5.A.1 iii to EK 1.5.A.1 iv: the largest double bond count is the most unsaturated lipid and the most unsaturated lipid is the most liquid at room temperature. No two rows share a count, so they cannot be alike."),
 ("Lipid Q, Lipid R and Lipid S",
  "Recomputed in q10 above: three rows melt below the 22 degrees the stem names as room temperature and one melts above it. A substance is liquid above its melting point, which is how EK 1.5.A.1 iv's claim shows up in measured data."),
 ("melting point falls",
  "Recomputed in q11 above: sorting the rows by double bond count leaves the melting points strictly falling. A lower melting point is what makes a lipid more liquid at a given room temperature, so this is the quantitative form of EK 1.5.A.1 iv."),
 ("Lower than the melting point of any lipid",
  "Recomputed in q12 above: the trend is monotone and the new lipid carries more double bonds than any tabulated row, so extrapolation runs below the lowest value shown. EK 1.5.A.1 iii and iv are what make the extrapolation principled rather than arbitrary."),
 ("insulation that helps keep mammals warm",
  "EK 1.5.A.2 i: fats provide energy storage and support cell function, and in some cases they can also provide insulation to help keep mammals warm. Bilayer formation, hormone action and membrane stability belong to iv, ii and iii of the same statement."),
 ("Hormones that support growth and development",
  "EK 1.5.A.2 ii: steroids are hormones that support physiological functions including growth and development, energy metabolism, and homeostasis. Bilayer formation is phospholipids' role under iv and energy storage is fats' under i."),
 ("essential structural stability to animal cell membranes",
  "EK 1.5.A.2 iii, near verbatim: cholesterol provides essential structural stability to animal cell membranes. EK 1.5.A.2 iv gives bilayer formation to phospholipids, and the framework names no lipid monomer."),
 ("Phospholipids",
  "EK 1.5.A.2 iv: phospholipids group together to form the lipid bilayers found in plasma and cell membranes. Cholesterol is given the different role of providing structural stability in iii."),
 ("A steroid",
  "EK 1.5.A.2 ii is the only sub-point describing a lipid as a hormone, and it names growth and development among the functions steroids support. Fats and phospholipids are given storage and membrane roles instead."),
 ("group together into the two facing layers",
  "EK 1.5.A.2 iv states that phospholipids group together to form the lipid bilayers found in plasma and cell membranes, which is the two-layer arrangement described. No other sub-point of EK 1.5.A.2 assigns a bilayer to any other lipid."),
 ("less liquid at room temperature than the usual ones",
  "Chaining EK 1.5.A.1 iii to EK 1.5.A.1 iv: fewer carbon to carbon double bonds means a less unsaturated lipid, and a less unsaturated lipid is less liquid at room temperature. Nothing in EK 1.5.A.1 lets a double bond change a lipid's polarity or its class."),
 ("way its subcomponents are assembled",
  "EK 1.5.A.1 states that the structure and function of lipids are derived from the way their subcomponents are assembled. Abundance, temperature of synthesis and hydrogen bonding with water are not offered by the framework as sources of lipid function."),
 ("withstood a greater rupturing force",
  "Recomputed in q21 above: the rupturing force rises at every step as cholesterol content rises, with the cholesterol-free preparation weakest. That is the pattern EK 1.5.A.2 iii describes."),
 ("About twice as great",
  "Recomputed in q22 above from the two tabulated forces named by the stem. It turns the qualitative claim of EK 1.5.A.2 iii into a reading taken off the data."),
 ("increased as the amount of steroid supplied increased",
  "Recomputed in q23 above: the mean gain rises at every step as the supplied amount rises, and the untreated group is not the only one to gain. EK 1.5.A.2 ii names growth and development among the functions steroids support."),
 ("Group 1",
  "Recomputed in q24 above: exactly one group received zero units per day. A control receives none of the treatment whose effect is under test, so that group is the baseline for the other three."),
 ("typically nonpolar and hydrophobic",
  "EK 1.5.A.1 describes lipids as typically nonpolar and hydrophobic, and EK 1.5.A.1 ii attaches the double bond to a kink in the carbon chain and to nothing else. The framework nowhere makes a double bond a source of polarity."),
 ("Phosphorus",
  "EK 1.2.A.1 ii states that phosphorus is used in the building of phospholipids, which it identifies as a type of lipid, while carbon, hydrogen and oxygen are the elements EK 1.2.A.1 assigns to biological molecules generally, carbohydrates included. Sulfur goes to proteins under EK 1.2.A.1 i."),
 ("Fats store energy, whereas phospholipids form the bilayer",
  "EK 1.5.A.2 i assigns energy storage and support of cell function to fats and EK 1.5.A.2 iv assigns the formation of lipid bilayers to phospholipids. Each rejected option moves a function onto a lipid the framework gives a different one."),
 ("Insulation that helps keep the mammal warm",
  "EK 1.5.A.2 i states that fats can in some cases provide insulation to help keep mammals warm alongside their energy storage role. The rejected options belong to phospholipids, steroids and cholesterol under the other sub-points."),
 ("only single bonds is unkinked",
  "EK 1.5.A.1 i makes a tail with only single bonds saturated, EK 1.5.A.1 ii confines the kink to tails carrying at least one double bond, and EK 1.5.A.1 iii and iv make the more unsaturated lipid the more liquid one. Those three fix both halves of the prediction."),
 ("many carbon to carbon double bonds and it is liquid",
  "EK 1.5.A.1 iii makes the double bond count the measure of unsaturation and EK 1.5.A.1 iv predicts the more unsaturated lipid is the more liquid at room temperature, so the two observations agree. Dissolving in water contradicts EK 1.5.A.1's hydrophobic character, and phosphorus and bilayer formation identify a phospholipid without reporting saturation."),
]

TABLE_CHECKS = {6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12,
                21: q21, 22: q22, 23: q23, 24: q24}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b1_5_mutant")
        mod.TOPIC = b1_5.TOPIC
        mod.QUESTIONS = copy.deepcopy(b1_5.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def melting_trend_broken(mod, claims):
        mod.QUESTIONS[10]["table"] = dict(
            headers=b1_5._T_MELT["headers"],
            rows=[[lab, d, ("40" if lab == "Lipid S" else m)]
                  for lab, d, m in b1_5._T_MELT["rows"]])

    def second_saturated(mod, claims):
        mod.QUESTIONS[6]["table"] = dict(
            headers=b1_5._T_FATTY["headers"],
            rows=[[lab, ("0" if lab == "Lipid 2" else v)] for lab, v in b1_5._T_FATTY["rows"]])

    def cholesterol_trend_broken(mod, claims):
        mod.QUESTIONS[20]["table"] = dict(
            headers=b1_5._T_CHOL["headers"],
            rows=[[lab, c, ("6" if lab == "Preparation 4" else f)]
                  for lab, c, f in b1_5._T_CHOL["rows"]])

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[1].__setitem__("ans", 1))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(12, ("no such phrase", c[12][1])))
    must_fail("a melting point altered so the trend is no longer monotone", melting_trend_broken)
    must_fail("a second lipid given zero double bonds", second_saturated)
    must_fail("the cholesterol trend reversed at the top row", cholesterol_trend_broken)
    must_fail("a backslash macro in a choice",
              lambda m, c: m.QUESTIONS[4]["choices"].__setitem__(2, "\\text{no relationship}"))
    print("all negative controls raised as required.")


import b1_5  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b1_5)
cg.check(b1_5, CLAIMS, table_checks=TABLE_CHECKS)
