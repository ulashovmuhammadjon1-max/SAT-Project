"""Key audit for AP BIOLOGY 2.3 Plasma Membrane.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
EK 2.3.A.1 (phospholipids have both hydrophilic and hydrophobic regions; the
polar hydrophilic phosphate regions face the aqueous environment while the
nonpolar hydrophobic fatty acid regions face each other in the membrane
interior) carries items 1, 2, 3, 4, 21, 24, 27 and 29.

EK 2.3.A.2 (embedded proteins can be hydrophilic with charged and polar side
groups, hydrophobic with nonpolar side groups, or both) carries items 5 and 8;
sub-point i (hydrophilic regions inside the protein or exposed to the cytosol)
items 6 and 15; sub-point ii (hydrophobic regions on the surface that interacts
with the interior fatty acids) items 7, 14, 20 and 26; both sub-points together,
item 22.

EK 2.3.B.1 (a structural framework of phospholipids embedded with proteins,
steroids such as cholesterol in vertebrate animals, glycoproteins and
glycolipids, all of which can move around the surface of the cell within the
membrane, as illustrated by the fluid mosaic model) carries items 9, 10, 11, 12,
13, 16, 17, 18, 19, 23, 25, 28 and 30.

OUT OF SCOPE ON PURPOSE. Selective permeability is topic 2.4 and transport is
topics 2.5 to 2.8; no item here asks what crosses the membrane or how. Item 21
does chain to EK 1.5.A.2 iv for phospholipids grouping into bilayers and item 28
to EK 1.5.A.2 ii for steroids being lipids, and both claims say so.

DATA ITEMS: 14 to 19 carry tables. The two protein-segment items are checked
against EK 2.3.A.2's own two-way classification of side groups, and any cell
outside that classification fails. The composition table is checked to sum to
100 before its complement is taken.

NEGATIVE CONTROL: ``python3 verify_b2_3.py --selftest`` corrupts a key, an
anchor, two table cells and the notation on purpose and confirms each fails.
"""
import re
import sys

import cg_check as cg

_BANNED = [
    (re.compile(r"\\"), "a backslash: Biology is not typeset, so LaTeX would print raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\^"), "a caret exponent: Biology is not typeset, so write it in words"),
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


CHAR = "Chemical character of the side groups in that segment"
TIME = "Time after the membrane protein was labelled (minutes)"
DIST = "Mean distance the labelled protein had moved within the membrane (micrometers)"
PCT = "Percentage of all molecules in the membrane"

# EK 2.3.A.2's own two-way split of side groups. A cell outside this fails.
HYDROPHOBIC = "nonpolar"
HYDROPHILIC = "polar and charged"


def _segments(table):
    j = table["headers"].index(CHAR)
    cells = {r[0]: r[j] for r in table["rows"]}
    unknown = set(cells.values()) - {HYDROPHOBIC, HYDROPHILIC}
    assert not unknown, f"side group cells outside EK 2.3.A.2's two kinds: {unknown}"
    return cells


def q14(table, item):
    cells = _segments(table)
    nonpolar = sorted(k for k, v in cells.items() if v == HYDROPHOBIC)
    assert nonpolar == ["Segment 2", "Segment 4"], f"nonpolar segments: {nonpolar}"
    assert len(nonpolar) < len(cells), "'all four segments' must be false"
    return (f"exactly two segments carry nonpolar side groups, {nonpolar}, which EK 2.3.A.2 "
            "identifies as the hydrophobic kind")


def q15(table, item):
    cells = _segments(table)
    polar = sorted(k for k, v in cells.items() if v == HYDROPHILIC)
    assert polar == ["Segment 1", "Segment 3"], f"polar and charged segments: {polar}"
    assert polar, "'none of the segments' must be false"
    return (f"exactly two segments carry polar and charged side groups, {polar}, which EK "
            "2.3.A.2 identifies as the hydrophilic kind")


def q16(table, item):
    d = cg.col(table, DIST)
    t = cg.col(table, TIME)
    assert all(d[i] < d[i + 1] for i in range(len(d) - 1)), f"distance must keep rising: {d}"
    assert d[0] == 0, "the first measurement must be the labelling moment"
    assert d[-1] > d[-2], "'moved only in the first ten minutes' must be false"
    return f"distances {d} at times {t} rise at every step, so movement continues to the end"


def q17(table, item):
    d = cg.col(table, DIST)
    t = cg.col(table, TIME)
    rate = (d[-1] - d[0]) / (t[-1] - t[0])
    assert 0.15 < rate < 0.25, f"the mean rate recomputes to {rate}, not about 0.2"
    return f"{d[-1]} micrometers over {t[-1]:.0f} minutes is {rate:.2f} micrometers per minute"


def q18(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, PCT)))
    top = max(vals, key=vals.get)
    assert top == "Phospholipid", f"the largest share belongs to {top}"
    assert list(vals.values()).count(vals[top]) == 1, "the maximum must be unique"
    return f"shares are {vals}; the unique maximum is {top}, which EK 2.3.B.1 also calls the framework"


def q19(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, PCT)))
    assert sum(vals.values()) == 100, f"the column sums to {sum(vals.values())}, not 100"
    rest = 100 - vals["Phospholipid"]
    assert rest == 45, f"the complement recomputes to {rest}"
    assert vals["Protein"] == 25, "the 25 distractor must be the protein share alone"
    return f"100 minus the phospholipid share {vals['Phospholipid']:.0f} is {rest:.0f}"


CLAIMS = [
 ("both a hydrophilic region and a hydrophobic region",
  "EK 2.3.A.1 opens by stating that phospholipids have both hydrophilic and hydrophobic regions. That dual character is what lets one end face water while the other faces away from it."),
 ("polar hydrophilic phosphate region",
  "EK 2.3.A.1 states that the polar hydrophilic phosphate regions of the phospholipids are oriented toward the aqueous external or internal environment. The fatty acid regions sit on the opposite side of that same sentence."),
 ("face each other within the interior of the membrane",
  "EK 2.3.A.1 states that the nonpolar hydrophobic fatty acid regions face each other within the interior of the membrane, which is what keeps them out of the aqueous environment on either side."),
 ("polar and hydrophilic, so it is compatible",
  "EK 2.3.A.1 calls the phosphate regions polar and hydrophilic and orients them toward the aqueous environment. The rejected option attaches that orientation to the chemical character EK 2.3.A.1 assigns to the fatty acid regions instead."),
 ("hydrophilic, hydrophobic, or both",
  "EK 2.3.A.2 states that embedded proteins can be hydrophilic, with charged and polar side groups, hydrophobic, with nonpolar side groups, or both. Allowing all three is what lets one protein span a membrane."),
 ("Either inside the interior of the protein or exposed to the cytosol",
  "EK 2.3.A.2 i, near verbatim. The rejected first option is the location EK 2.3.A.2 ii assigns to the HYDROPHOBIC regions, which is the confusion this item is built to catch."),
 ("surface that interacts with the fatty acids in the interior of the membrane",
  "EK 2.3.A.2 ii states that hydrophobic regions of proteins make up the protein surface that interacts with the fatty acids in the interior membrane. Exposure to the cytosol and burial inside the protein are EK 2.3.A.2 i's HYDROPHILIC placements."),
 ("Hydrophilic proteins have charged and polar side groups",
  "EK 2.3.A.2 pairs hydrophilic with charged and polar side groups and hydrophobic with nonpolar side groups in one parenthetical. Denying that proteins carry side groups also contradicts EK 1.7.A.2, which gives every amino acid an R group."),
 ("framework of phospholipids embedded with proteins, steroids",
  "EK 2.3.B.1 states that plasma membranes consist of a structural framework of phospholipid molecules embedded with proteins, steroids such as cholesterol in vertebrate animals, glycoproteins, and glycolipids. Nucleic acids and cellulose appear nowhere in that list."),
 ("Cholesterol, in vertebrate animals",
  "EK 2.3.B.1 names steroids, such as cholesterol in vertebrate animals, among the embedded components. Glycolipids and glycoproteins are listed separately in the same sentence and are not steroids."),
 ("can move around the surface of the cell within the membrane",
  "EK 2.3.B.1 ends by stating that ALL of these can move around the surface of the cell within the membrane, as illustrated by the fluid mosaic model. The word all is what rules out confining movement to the proteins."),
 ("Phospholipids",
  "EK 2.3.B.1 states that plasma membranes consist of a structural framework of phospholipid molecules, with the other components embedded in that framework. The rejected options are named in the same sentence as embedded components, or not named at all."),
 ("Glycoproteins and glycolipids",
  "EK 2.3.B.1 lists proteins, steroids, glycoproteins, and glycolipids as embedded in the phospholipid framework, and those last two are the pair whose names carry the carbohydrate prefix. The framework claims nothing further about either."),
 ("Segment 2 and Segment 4",
  "Recomputed in q14 above: exactly two segments carry nonpolar side groups, which EK 2.3.A.2 identifies as hydrophobic, and EK 2.3.A.2 ii puts hydrophobic regions on the surface that interacts with the interior fatty acids."),
 ("Segment 1 and Segment 3",
  "Recomputed in q15 above: exactly two segments carry charged and polar side groups, which EK 2.3.A.2 identifies as hydrophilic, and EK 2.3.A.2 i puts hydrophilic regions inside the protein or exposed to the cytosol."),
 ("moved within the membrane over the course of the measurement",
  "Recomputed in q16 above: the distance rises at every measurement including the last, so movement had not stopped. EK 2.3.B.1 states that the membrane's components can move around the surface of the cell within the membrane."),
 ("About 0.2 micrometers per minute",
  "Recomputed in q17 above by dividing the total distance moved by the total elapsed time. The rejected values are that figure off by a factor of ten, or the total distance and the total time reported as though they were rates."),
 ("Phospholipid, which the framework identifies",
  "Recomputed in q18 above: the phospholipid share is the unique maximum in the table. EK 2.3.B.1 independently calls the phospholipid molecules the structural framework, so data and framework name the same component."),
 ("45 percent",
  "Recomputed in q19 above: the column is checked to sum to 100 first, then the phospholipid share is subtracted. The check also confirms the 25 distractor is the protein share alone."),
 ("no longer be suited to the surface that interacts",
  "EK 2.3.A.2 ii reserves the surface that interacts with the interior fatty acids for hydrophobic regions, and EK 2.3.A.2 identifies hydrophilic regions by exactly the charged and polar side groups described. EK 2.3.A.1 fixes the phospholipids' orientation independently of any one protein."),
 ("polar hydrophilic regions face the water on both sides",
  "EK 2.3.A.1 orients the polar hydrophilic phosphate regions toward the aqueous environment and has the nonpolar hydrophobic fatty acid regions face each other in the interior, and EK 1.5.A.2 iv states that phospholipids group together to form lipid bilayers."),
 ("hydrophobic regions face the fatty acids",
  "EK 2.3.A.2 allows a protein to be both, and its sub-points then fix each kind: ii puts the hydrophobic regions on the surface meeting the interior fatty acids and i puts the hydrophilic regions inside the protein or exposed to the cytosol. EK 2.3.B.1's movement is lateral and does not reverse those placements."),
 ("which is what the fluid mosaic model illustrates",
  "EK 2.3.B.1 states that all of the listed components can move around the surface of the cell within the membrane, as illustrated by the fluid mosaic model. The word all rules out both options confining movement to one class of component."),
 ("fatty acid regions face each other and whose phosphate regions face outward",
  "EK 2.3.A.1 orients the polar hydrophilic phosphate regions toward the aqueous external or internal environment and has the nonpolar hydrophobic fatty acid regions face each other within the interior of the membrane, which is exactly the two-layer arrangement described."),
 ("seen to change position within the membrane over time",
  "EK 2.3.B.1 attaches the fluid mosaic model to the claim that all of the components can move around the surface of the cell within the membrane, so movement is what evidence for it must show. Listing the components tests EK 2.3.B.1's composition clause instead, and a hydrophobic interior tests EK 2.3.A.1."),
 ("Entirely within the interior of the membrane",
  "EK 2.3.A.2 identifies hydrophobic protein regions by their nonpolar side groups and EK 2.3.A.2 ii places those regions on the surface interacting with the interior fatty acids. A surface nonpolar throughout has no region suited to the aqueous cytosol under EK 2.3.A.2 i."),
 ("occupied by the nonpolar hydrophobic fatty acid regions",
  "EK 2.3.A.1 states that the nonpolar hydrophobic fatty acid regions face each other within the interior of the membrane, while the phosphate regions are oriented toward the aqueous environments on either side."),
 ("named as a component of plasma membranes in vertebrate animals",
  "EK 2.3.B.1 names steroids, such as cholesterol in vertebrate animals, among the components embedded in the phospholipid framework, and EK 1.5.A.2 ii makes steroids a class of lipid. The framework itself is the phospholipid layer, not the steroid."),
 ("One end of the molecule is polar and hydrophilic while the other is nonpolar",
  "EK 2.3.A.1 states that phospholipids have both hydrophilic and hydrophobic regions and orients the two in opposite directions. A molecule alike at both ends could not straddle the boundary between the aqueous cytosol and the water-free interior."),
 ("all of which can move within the membrane",
  "EK 2.3.B.1 combines both halves: a structural framework of phospholipid molecules embedded with proteins, steroids, glycoproteins and glycolipids, all of which can move around the surface of the cell within the membrane, as illustrated by the fluid mosaic model."),
]

TABLE_CHECKS = {14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b2_3_mutant")
        mod.TOPIC = b2_3.TOPIC
        mod.QUESTIONS = copy.deepcopy(b2_3.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def third_nonpolar(mod, claims):
        mod.QUESTIONS[13]["table"] = dict(
            headers=b2_3._T_SEGMENTS["headers"],
            rows=[[lab, ("nonpolar" if lab == "Segment 3" else c)]
                  for lab, c in b2_3._T_SEGMENTS["rows"]])

    def side_group_typo(mod, claims):
        mod.QUESTIONS[14]["table"] = dict(
            headers=b2_3._T_SEGMENTS["headers"],
            rows=[[lab, ("slightly polar" if lab == "Segment 1" else c)]
                  for lab, c in b2_3._T_SEGMENTS["rows"]])

    def percentages_do_not_sum(mod, claims):
        mod.QUESTIONS[18]["table"] = dict(
            headers=b2_3._T_COMPOSITION["headers"],
            rows=[[lab, ("40" if lab == "Phospholipid" else v)]
                  for lab, v in b2_3._T_COMPOSITION["rows"]])

    def protein_stops_moving(mod, claims):
        mod.QUESTIONS[15]["table"] = dict(
            headers=b2_3._T_FLUIDITY["headers"],
            rows=[["0", "0.0"], ["10", "2.1"], ["20", "2.1"], ["30", "2.1"]])

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[11].__setitem__("ans", 2))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(9, ("no such phrase", c[9][1])))
    must_fail("a third protein segment made nonpolar", third_nonpolar)
    must_fail("a side group cell outside the framework's two kinds", side_group_typo)
    must_fail("membrane percentages no longer summing to 100", percentages_do_not_sum)
    must_fail("the labelled protein stopped moving after ten minutes", protein_stops_moving)
    must_fail("a backslash macro in a choice",
              lambda m, c: m.QUESTIONS[0]["choices"].__setitem__(2, "It is \\beta hydrophobic throughout."))
    print("all negative controls raised as required.")


import b2_3  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b2_3)
cg.check(b2_3, CLAIMS, table_checks=TABLE_CHECKS)
