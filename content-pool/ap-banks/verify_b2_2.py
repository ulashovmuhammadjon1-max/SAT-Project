"""Key audit for AP BIOLOGY 2.2 Cell Size.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
EK 2.2.A.1 (surface area to volume ratios affect the ability to obtain nutrients,
eliminate waste, acquire or dissipate thermal energy and otherwise exchange
chemicals and energy) carries item 1, and its illustrative examples carry item 9.

EK 2.2.A.2 (the plasma membrane's surface area must be large enough to
adequately exchange materials) carries items 2, 23 and 30, with its sub-points:
i (the ratio can restrict cell size and shape; smaller cells have a higher ratio
and more efficient exchange) items 3, 10, 13, 14, 15 and 26;
ii (as cells increase in volume the ratio decreases and the demand for internal
resources increases) items 4, 12, 17, 22 and 28;
iii (more complex structures, for example membrane folds) items 5 and 24;
iv (as organisms increase in size the ratio decreases, affecting heat exchange;
smaller masses exchange proportionally more heat) items 6, 7, 20, 21 and 25;
v (typically the smaller the organism, the higher the metabolic rate per unit
body mass) items 8, 18 and 19.

Item 27 is an experimental-design item and rests on isolating one variable, not
on a content sentence.

THE GEOMETRY IS RECOMPUTED, NOT TRUSTED. Every surface area and volume printed
in the two tables is recomputed here from the side lengths in the same row, so a
mistyped cell fails rather than ships. Items 11, 16, 17 and 29 are arithmetic
questions whose keys are recomputed in ``check_geometry`` from the formulas the
stems themselves supply -- the CED prints those formulas on the exam's formula
sheet and this bank writes them out in words rather than leaving them recalled.

NEGATIVE CONTROL: ``python3 verify_b2_2.py --selftest`` corrupts a key, an
anchor, a tabulated surface area, a trend and the notation on purpose and
confirms each check fails.
"""
import math
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


SIDE = "Length of one side (micrometers)"
SA = "Surface area (square micrometers)"
VOL = "Volume (cubic micrometers)"
DIMS = "Length, width and height (micrometers)"
MASS_A = "Body mass (grams)"
MRATE = "Metabolic rate per gram of body mass (arbitrary units)"
MASS_S = "Mass (grams)"
HEAT = "Heat lost per gram per minute (arbitrary units)"


def _cube_ratios(table):
    """Recompute each cube's surface area, volume and ratio from its side length."""
    out = {}
    for lab in cg.labels(table):
        s = cg.cell(table, lab, SIDE)
        sa, vol = 6 * s * s, s ** 3
        assert sa == cg.cell(table, lab, SA), \
            f"{lab}: tabulated surface area {cg.cell(table, lab, SA)} but six times side squared is {sa}"
        assert vol == cg.cell(table, lab, VOL), \
            f"{lab}: tabulated volume {cg.cell(table, lab, VOL)} but side cubed is {vol}"
        out[lab] = sa / vol
    return out


def q10(table, item):
    r = _cube_ratios(table)
    top = max(r, key=r.get)
    assert top == "Cube A", f"the largest ratio belongs to {top}"
    assert len(set(r.values())) == len(r), "'all four the same' must be false"
    return f"ratios recomputed from the side lengths are {r}; the unique maximum is {top}"


def q11(table, item):
    r = _cube_ratios(table)
    hits = [lab for lab in cg.labels(table) if cg.cell(table, lab, SIDE) == 3]
    assert len(hits) == 1, f"the stem's 3 micrometer cube matched {hits}"
    assert r[hits[0]] == 2, f"the ratio recomputes to {r[hits[0]]}"
    return f"{hits[0]}: 54 over 27 is {r[hits[0]]:.0f}, so the ratio is 2 to 1"


def q12(table, item):
    r = _cube_ratios(table)
    pairs = sorted((cg.cell(table, lab, SIDE), r[lab]) for lab in cg.labels(table))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the ratio must fall as side length rises: {pairs}"
    return f"sorted by side length the ratios are {[round(v, 2) for _, v in pairs]}, strictly falling"


def q13(table, item):
    r = _cube_ratios(table)
    top = max(r, key=r.get)
    assert top == "Cube A", f"the most efficient exchanger by ratio is {top}"
    assert len(set(r.values())) > 1, "'all four equally efficient' must be false"
    return f"the largest recomputed ratio is {top}'s, {r[top]:.0f} to 1, and the four differ"


def _box_ratios(table):
    """Recompute each box's surface area and volume from its own dimensions."""
    j = table["headers"].index(DIMS)
    out = {}
    for row in table["rows"]:
        lab = row[0]
        l, w, h = (float(x) for x in row[j].split(" by "))
        sa = 2 * l * h + 2 * l * w + 2 * w * h
        vol = l * w * h
        assert sa == cg.cell(table, lab, SA), \
            f"{lab}: tabulated surface area {cg.cell(table, lab, SA)} but the dimensions give {sa}"
        assert vol == cg.cell(table, lab, VOL), \
            f"{lab}: tabulated volume {cg.cell(table, lab, VOL)} but the dimensions give {vol}"
        out[lab] = sa / vol
    return out


def q14(table, item):
    r = _box_ratios(table)
    vols = set(cg.col(table, VOL))
    assert len(vols) == 1, f"the three models must enclose equal volumes; got {vols}"
    top = max(r, key=r.get)
    assert top == "Model 3", f"the largest ratio belongs to {top}"
    assert len(set(r.values())) == len(r), "'all three the same ratio' must be false"
    return f"volumes are all {vols.pop():.0f}; recomputed ratios {r} differ, with the maximum at {top}"


def q15(table, item):
    r = _box_ratios(table)
    cube = [lab for lab in cg.labels(table)
            if len(set(table["rows"][cg.labels(table).index(lab)][1].split(" by "))) == 1]
    assert cube, "one model must be a cube for the flattening comparison to mean anything"
    flat = [lab for lab in r if lab not in cube]
    assert all(r[f] > r[cube[0]] for f in flat), \
        f"the flattened and elongated models must exceed the cube: {r}"
    assert len(set(cg.col(table, VOL))) == 1, "volume must be held constant"
    return (f"at a constant volume the cube {cube[0]} has ratio {r[cube[0]]:.2f} and the "
            f"flattened models {[round(r[f], 2) for f in flat]}, all larger")


def q18(table, item):
    pairs = sorted(zip(cg.col(table, MASS_A), cg.col(table, MRATE)))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"rate per gram must fall as mass rises: {pairs}"
    return f"sorted by body mass the rates per gram are {[r for _, r in pairs]}, strictly falling"


def q19(table, item):
    pairs = sorted(zip(cg.col(table, MASS_A), cg.col(table, MRATE)))
    ratio = pairs[0][1] / pairs[-1][1]
    assert 11 <= ratio <= 13, f"the ratio recomputes to {ratio}, not about twelve"
    assert abs(pairs[0][1] - 60) < 5, "the sixty distractor must be the lightest animal's own rate"
    return f"{pairs[0][1]:.0f} over {pairs[-1][1]:.0f} is {ratio:.1f}, about twelve"


def q20(table, item):
    pairs = sorted(zip(cg.col(table, MASS_S), cg.col(table, HEAT)))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"heat lost per gram must fall as mass rises: {pairs}"
    assert pairs[-1][1] == min(h for _, h in pairs), "the heaviest sphere must lose the least per gram"
    return f"sorted by mass the heat losses per gram are {[h for _, h in pairs]}, strictly falling"


def q21(table, item):
    pairs = sorted(zip(cg.col(table, MASS_S), cg.col(table, HEAT)))
    assert 125 > max(m for m, _ in pairs), "the predicted sphere must be heavier than every row"
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        "the trend must be monotone for the extrapolation to be the keyed one"
    return (f"the table runs to {max(m for m, _ in pairs):.0f} grams with a falling trend "
            f"whose minimum is {min(h for _, h in pairs):.0f}, so 125 grams extrapolates below it")


def check_geometry(module):
    """Items 11, 16, 17 and 29: recompute the arithmetic the stems ask for."""
    # item 16, sphere of radius 3
    r = 3.0
    sa = 4 * math.pi * r ** 2
    vol = (4.0 / 3.0) * math.pi * r ** 3
    assert abs(sa / vol - 1.0) < 1e-12, f"sphere ratio recomputes to {sa / vol}"
    assert module.QUESTIONS[15]["choices"][module.QUESTIONS[15]["ans"]] == "1 to 1", \
        "item 16's key must be the recomputed 1 to 1"

    # item 17, doubling every side of a cube
    s = 5.0
    before = (6 * s * s) / s ** 3
    after = (6 * (2 * s) ** 2) / (2 * s) ** 3
    assert abs((6 * (2 * s) ** 2) / (6 * s * s) - 4) < 1e-12, "surface area must go up fourfold"
    assert abs(((2 * s) ** 3) / s ** 3 - 8) < 1e-12, "volume must go up eightfold"
    assert abs(after / before - 0.5) < 1e-12, f"the ratio must halve; got {after / before}"

    # item 29, cube of side 4
    s4 = 4.0
    ratio4 = (6 * s4 * s4) / s4 ** 3
    assert abs(ratio4 - 1.5) < 1e-12, f"the side-4 cube ratio recomputes to {ratio4}"
    assert module.QUESTIONS[28]["choices"][module.QUESTIONS[28]["ans"]] == "1.5 to 1", \
        "item 29's key must be the recomputed 1.5 to 1"
    # the 6 to 1 distractor must be the ratio at a side of one, not at a side of four
    assert abs((6 * 1 * 1) / 1 ** 3 - 6) < 1e-12, "the 6 to 1 distractor must be the side-1 ratio"
    print(f"OK  {module.TOPIC[0]} geometry: sphere of radius 3 gives 1 to 1, cube of side 4 "
          f"gives 1.5 to 1, doubling a side quarters nothing and halves the ratio.")


CLAIMS = [
 ("Obtain necessary nutrients, eliminate waste products",
  "EK 2.2.A.1, near verbatim: surface area to volume ratios affect the ability of a biological system to obtain necessary nutrients, eliminate waste products, acquire or dissipate thermal energy, and otherwise exchange chemicals and energy with the environment. The rejected options are organelle functions from EK 2.1.A.1, EK 2.1.A.4 and EK 2.1.A.7 i."),
 ("large enough to adequately exchange materials",
  "EK 2.2.A.2 states that the surface area of the plasma membrane must be large enough to adequately exchange materials. Surface area and volume are measured in different units, so equating them is not a claim the framework makes."),
 ("higher surface area to volume ratio and exchange materials with the environment",
  "EK 2.2.A.2 i states that smaller cells typically have a higher surface area to volume ratio as well as a more efficient exchange of materials with the environment than do larger cells. The two halves are asserted together, so the options splitting them contradict the sentence."),
 ("ratio decreases and the demand for internal resources increases",
  "EK 2.2.A.2 ii, near verbatim. The two quantities move in opposite directions, which is what makes large size a problem for exchange."),
 ("Membrane folds",
  "EK 2.2.A.2 iii states that more complex cellular structures, for example membrane folds, are necessary to adequately exchange materials with the environment. The rejected options are Unit 1 molecular structures and the ribosome of EK 2.1.A.1, none offered as an exchange structure."),
 ("rate of heat exchange with the environment",
  "EK 2.2.A.2 iv states that as organisms increase in size their surface area to volume ratio decreases, affecting properties like rate of heat exchange with the environment. The framework makes none of the rejected molecular features a function of body size."),
 ("Smaller amounts of mass exchange proportionally more heat",
  "EK 2.2.A.2 iv, near verbatim: smaller amounts of mass exchange proportionally more heat with the ambient environment than do larger masses, and as mass increases both the ratio and the rate of heat exchange decrease."),
 ("the smaller the organism, the higher the metabolic rate",
  "EK 2.2.A.2 v states that typically the smaller the organism, the higher the metabolic rate per unit body mass. The framework attaches the relationship to size rather than to diet."),
 ("Root hairs",
  "The illustrative examples printed with EK 2.2.A.1 are root hairs, guard cells and gut epithelial cells, together with cilia and stomata. Lysosomes and the Golgi are organelles under EK 2.1.A.6 and EK 2.1.A.4."),
 ("Cube A",
  "Recomputed in q10 above. Each row's surface area and volume are first rederived from its own side length, then divided; the smallest cube gives the largest ratio, as EK 2.2.A.2 i states in general terms."),
 ("2 to 1",
  "Recomputed in q11 above from the row the stem names. The inverted option is volume over surface area and the 6 to 1 option is the smallest cube's ratio in the same table."),
 ("It decreases as the side length increases",
  "Recomputed in q12 above: the ratio computed for each row falls strictly as the side length rises. That is the arithmetic behind EK 2.2.A.2 ii."),
 ("Cube A",
  "Recomputed in q13 above. EK 2.2.A.2 i ties a higher surface area to volume ratio to a more efficient exchange of materials, and the recomputed ratios differ, so the equal-efficiency option is false."),
 ("Model 3",
  "Recomputed in q14 above: the three volumes are checked equal and each surface area is rederived from its own dimensions, so the largest surface area is the largest ratio. EK 2.2.A.2 i is what makes shape as well as size relevant."),
 ("raises its surface area to volume ratio without changing its volume",
  "Recomputed in q15 above: at a constant volume the cube's ratio is the smallest and both flattened models exceed it. EK 2.2.A.2 i states that the surface area to volume ratio can restrict cell size and shape."),
 ("1 to 1",
  "Recomputed in check_geometry above from the two formulas the stem supplies: dividing four pi r squared by four thirds pi r cubed leaves three over the radius, which is 1 at a radius of 3 micrometers. The 3 to 1 option is that expression with the radius left out."),
 ("multiplied by four, volume by eight, and the ratio is halved",
  "Recomputed in check_geometry above: a cube's surface area goes with the square of the side and its volume with the cube, so doubling the side multiplies them by four and by eight and halves the ratio. EK 2.2.A.2 ii states that relation qualitatively."),
 ("the smaller the animal, the higher its metabolic rate",
  "Recomputed in q18 above: ranking the rows by body mass gives the reverse of the ranking by metabolic rate per gram, which is EK 2.2.A.2 v."),
 ("About twelve times as great",
  "Recomputed in q19 above from the lightest and heaviest rows. The check also confirms the sixty option is the lightest animal's own rate rather than a ratio."),
 ("As mass increased, the heat lost per gram per minute decreased",
  "Recomputed in q20 above: heat lost per gram falls at every step as mass rises. EK 2.2.A.2 iv states that as mass increases both the ratio and the rate of heat exchange decrease."),
 ("Lower than the value recorded for any sphere",
  "Recomputed in q21 above: the trend is monotone and the new sphere is heavier than every tabulated row, so the extrapolation runs below the smallest value. EK 2.2.A.2 iv supplies the reason the trend continues."),
 ("ratio falls, and its demand for internal resources rises",
  "EK 2.2.A.2 ii states that as cells increase in volume the surface area to volume ratio decreases and the demand for internal resources increases. Those are the two halves of one sentence."),
 ("has not kept pace with its volume",
  "EK 2.2.A.2 requires the membrane's surface area to be large enough to adequately exchange materials, and EK 2.2.A.2 ii has the ratio falling and the demand rising as volume grows. Under EK 2.2.A.2 i larger cells have the LOWER ratio, which is why the option giving them a higher one is false."),
 ("Adding folds to its plasma membrane",
  "EK 2.2.A.2 iii names membrane folds as an example of the more complex cellular structures necessary to adequately exchange materials. Scaling every side up raises volume faster than surface area under EK 2.2.A.2 ii, and a sphere holds the least surface area for a given volume."),
 ("smaller animal will lose proportionally more heat",
  "EK 2.2.A.2 iv states that smaller amounts of mass exchange proportionally more heat with the ambient environment than do larger masses, and that as mass increases both the ratio and the rate of heat exchange decrease."),
 ("long thin cell has the greater surface area to volume ratio",
  "EK 2.2.A.2 i states that the surface area to volume ratio can restrict cell size and shape and ties a higher ratio to more efficient exchange. This topic's own equal-volume box models, recomputed in q14 and q15, show that equal volumes do not force equal ratios."),
 ("cut to several different side lengths in the same solution",
  "The claim under test is about the effect of size, so size must be the only difference between treatments while material, solution and time are held constant, and the outcome must be scaled to each object's own size. A single object supplies no comparison and computing ratios alone tests no exchange."),
 ("volume grows faster than surface area",
  "Having more membrane in total is consistent with having less membrane per unit of volume, which is what the ratio measures. EK 2.2.A.2 ii states that as cells increase in volume the surface area to volume ratio decreases, and the cube arithmetic recomputed in q12 shows why."),
 ("1.5 to 1",
  "Recomputed in check_geometry above from the two formulas the stem supplies: six times the side squared over the side cubed is six over the side, which is 1.5 at a side of 4 micrometers. The 6 to 1 option is that expression with the side length left out, which holds only at a side of 1."),
 ("membrane must stay large enough relative to the interior",
  "EK 2.2.A.2 i states that the surface area to volume ratio can restrict cell size and shape, and EK 2.2.A.2 requires the plasma membrane's surface area to be large enough to adequately exchange materials. Comparing a volume with an area as if they were the same kind of quantity is not a claim the framework makes."),
]

TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15,
                18: q18, 19: q19, 20: q20, 21: q21}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b2_2_mutant")
        mod.TOPIC = b2_2.TOPIC
        mod.QUESTIONS = copy.deepcopy(b2_2.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            check_geometry(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def mistyped_surface_area(mod, claims):
        mod.QUESTIONS[9]["table"] = dict(
            headers=b2_2._T_CUBES["headers"],
            rows=[[lab, s, ("60" if lab == "Cube C" else sa), v]
                  for lab, s, sa, v in b2_2._T_CUBES["rows"]])

    def boxes_unequal_volume(mod, claims):
        mod.QUESTIONS[13]["table"] = dict(
            headers=b2_2._T_BOXES["headers"],
            rows=[["Model 1", "4 by 4 by 4", "96", "64"],
                  ["Model 2", "8 by 8 by 2", "288", "128"],
                  ["Model 3", "16 by 4 by 1", "168", "64"]])

    def heat_trend_broken(mod, claims):
        mod.QUESTIONS[19]["table"] = dict(
            headers=b2_2._T_HEAT["headers"],
            rows=[[lab, m, ("45" if lab == "Sphere 4" else h)]
                  for lab, m, h in b2_2._T_HEAT["rows"]])

    def wrong_sphere_key(mod, claims):
        mod.QUESTIONS[15]["ans"] = 1

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[4].__setitem__("ans", 2))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(6, ("no such phrase", c[6][1])))
    must_fail("a tabulated surface area that no longer matches its side length",
              mistyped_surface_area)
    must_fail("the equal-volume premise of the shape item broken", boxes_unequal_volume)
    must_fail("a heat value altered so the trend is no longer monotone", heat_trend_broken)
    must_fail("the sphere ratio item keyed to 3 to 1", wrong_sphere_key)
    must_fail("a caret exponent in a stem",
              lambda m, c: m.QUESTIONS[16].__setitem__("q", "What happens to 6s^2 when the side doubles?"))
    print("all negative controls raised as required.")


import b2_2  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b2_2)
check_geometry(b2_2)
cg.check(b2_2, CLAIMS, table_checks=TABLE_CHECKS)
