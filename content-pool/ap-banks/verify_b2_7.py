"""Key audit for AP BIOLOGY 2.7 Tonicity and Osmoregulation.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
EK 2.7.A.1 (external environments can be hypotonic, hypertonic or isotonic;
water moves from hypotonic to hypertonic regions; water moves by osmosis from
high water potential to low water potential) carries items 1, 2, 3, 15, 16, 17,
18, 20, 26, 27 and 30, and its illustrative examples carry item 10.

The water potential equation printed with EK 2.7.A.1, water potential is the sum
of the pressure potential and the solute potential, carries items 5, 6, 14, 15,
23 and 25.

EK 2.7.B.1 (growth and homeostasis are maintained by the constant movement of
molecules across membranes) carries items 9 and part of 28.

EK 2.7.B.2 (osmoregulation maintains water balance and lets organisms control
their internal solute composition and water potential; water moves from low to
high solute concentration) carries items 4, 8, 19, 21, 22, 29 and 30, and the
solute potential equation printed with it carries items 6, 7, 11, 12, 13, 24
and 25.

Item 27 chains to EK 2.4.B.1, which names protection from osmotic lysis among
the roles of the cell walls of Bacteria, Archaea, Fungi and plants -- an animal
cell has none, which is why the risk applies to it.

EVERY NUMBER IS RECOMPUTED, NOTHING RECALLED. Both equations are written out in
words in the stems that need them, and the arithmetic below rederives every
keyed value from the table's own inputs using the pressure constant 0.0831 liter
bars per mole per Kelvin and the Kelvin conversion of Celsius plus 273. Item 13
is checked to round to the keyed value, item 14 to equal its own solute
potential once the pressure potential is zero, and item 15's direction to follow
from the two recomputed water potentials rather than from the concentrations.

DATA ITEMS: 11 to 22 carry tables.

NEGATIVE CONTROL: ``python3 verify_b2_7.py --selftest`` corrupts a key, an
anchor, three table cells and the notation on purpose and confirms each fails.
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


ION = "Ionization constant of the solute"
CONC = "Molar concentration (moles per liter)"
TEMP = "Temperature (degrees Celsius)"
INSIDE = "Solute concentration inside the cell (millimolar)"
OUTSIDE = "Solute concentration of the surrounding solution (millimolar)"
EXT = "Solute concentration of the solution (millimolar)"
CONTR = "Contractions of the contractile vacuole per minute"

R = 0.0831  # liter bars per mole per Kelvin, as printed with EK 2.7.B.2
KELVIN_OFFSET = 273


def _solute_potential(table, lab):
    """The CED's own equation, rebuilt from this row's inputs."""
    i = cg.cell(table, lab, ION)
    c = cg.cell(table, lab, CONC)
    t_kelvin = cg.cell(table, lab, TEMP) + KELVIN_OFFSET
    return -i * c * R * t_kelvin


def _all_potentials(table):
    return {lab: _solute_potential(table, lab) for lab in cg.labels(table)}


def q11(table, item):
    # the keyed reasoning ("same temperature, so the product decides") assumes this
    assert len(set(cg.col(table, TEMP))) == 1, \
        f"the rows must share a temperature for the product to decide: {cg.col(table, TEMP)}"
    psi = _all_potentials(table)
    lowest = min(psi, key=psi.get)
    assert lowest == "Solution 4", f"the most negative solute potential is {lowest}"
    assert list(psi.values()).count(psi[lowest]) == 1, "the minimum must be unique"
    assert len(set(round(v, 6) for v in psi.values())) > 1, "'all four the same' must be false"
    return f"solute potentials recompute to {[round(v, 3) for v in psi.values()]}; the minimum is {lowest}"


def q12(table, item):
    assert len(set(cg.col(table, TEMP))) == 1, \
        f"the rows must share a temperature for the product to decide: {cg.col(table, TEMP)}"
    psi = _all_potentials(table)
    labs = list(psi)
    equal = sorted({tuple(sorted((a, b))) for a in labs for b in labs
                    if a != b and abs(psi[a] - psi[b]) < 1e-9})
    assert equal == [("Solution 1", "Solution 2")], f"equal pairs: {equal}"
    return (f"exactly one pair shares a solute potential, {equal[0]}, both at "
            f"{psi['Solution 1']:.3f} bars")


def q13(table, item):
    hits = [lab for lab in cg.labels(table)
            if cg.cell(table, lab, CONC) == 0.5 and cg.cell(table, lab, ION) == 1]
    assert len(hits) == 1, f"the stem's row matched {hits}"
    v = _solute_potential(table, hits[0])
    assert abs(v - (-12.5)) < 0.1, f"the solute potential recomputes to {v}, not about negative 12.5"
    assert v < 0, "the minus sign in the equation makes every real solute potential negative"
    return f"{hits[0]}: negative 1 times 0.5 times {R} times 300 is {v:.3f} bars"


def q14(table, item):
    hits = [lab for lab in cg.labels(table)
            if cg.cell(table, lab, ION) == 1 and cg.cell(table, lab, CONC) == 0.2]
    assert len(hits) == 1, f"the stem's row matched {hits}"
    solute = _solute_potential(table, hits[0])
    water = 0.0 + solute            # pressure potential is zero in an open beaker
    assert abs(water - (-5.0)) < 0.1, f"the water potential recomputes to {water}"
    assert water == solute, "with a pressure potential of zero the two must be identical"
    return f"{hits[0]}: pressure potential 0 plus solute potential {solute:.3f} is {water:.3f} bars"


def q15(table, item):
    first = [lab for lab in cg.labels(table)
             if cg.cell(table, lab, ION) == 1 and cg.cell(table, lab, CONC) == 0.2][0]
    second = [lab for lab in cg.labels(table)
              if cg.cell(table, lab, ION) == 2 and cg.cell(table, lab, CONC) == 0.3][0]
    wp = {lab: 0.0 + _solute_potential(table, lab) for lab in (first, second)}
    assert wp[first] > wp[second], f"the first solution must hold the higher water potential: {wp}"
    assert wp[first] != wp[second], "'the two water potentials are equal' must be false"
    return (f"{first} at {wp[first]:.3f} bars is above {second} at {wp[second]:.3f} bars, so water "
            "moves from the first to the second")


def _tonicity(table):
    return {lab: (cg.cell(table, lab, INSIDE), cg.cell(table, lab, OUTSIDE))
            for lab in cg.labels(table)}


def q16(table, item):
    t = _tonicity(table)
    hypo = sorted(lab for lab, (i, o) in t.items() if o < i)
    assert hypo == ["Cell A"], f"cells in a hypotonic solution: {hypo}"
    return f"exactly one row has a lower outside than inside concentration, {hypo[0]}: {t[hypo[0]]}"


def q17(table, item):
    t = _tonicity(table)
    hyper = sorted(lab for lab, (i, o) in t.items() if o > i)
    assert hyper == ["Cell B"], f"cells in a hypertonic solution: {hyper}"
    return f"exactly one row has a higher outside than inside concentration, {hyper[0]}: {t[hyper[0]]}"


def q18(table, item):
    t = _tonicity(table)
    iso = sorted(lab for lab, (i, o) in t.items() if o == i)
    assert iso == ["Cell C"], f"cells in an isotonic solution: {iso}"
    assert len(t) == 3 and len({("hypo" if o < i else "hyper" if o > i else "iso")
                                for i, o in t.values()}) == 3, \
        "the three rows should illustrate the three relations EK 2.7.A.1 names"
    return f"exactly one row records equal concentrations, {iso[0]}, and the three rows cover all three relations"


def q19(table, item):
    t = _tonicity(table)
    gains = sorted(lab for lab, (i, o) in t.items() if i > o)
    assert gains == ["Cell A"], f"cells that gain water: {gains}"
    return f"water moves toward the more concentrated side, so only {gains[0]} takes water in: {t[gains[0]]}"


def q20(table, item):
    t = _tonicity(table)
    loses = sorted(lab for lab, (i, o) in t.items() if o > i)
    assert loses == ["Cell B"], f"cells that lose water: {loses}"
    return f"water moves toward the more concentrated side, so only {loses[0]} loses water: {t[loses[0]]}"


def q21(table, item):
    pairs = sorted(zip(cg.col(table, EXT), cg.col(table, CONTR)))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"contractions must fall as the external concentration rises: {pairs}"
    return f"sorted by external concentration the contraction rates are {[c for _, c in pairs]}, strictly falling"


def q22(table, item):
    pairs = sorted(zip(cg.col(table, EXT), cg.col(table, CONTR)))
    assert 250 > max(c for c, _ in pairs), "the predicted solution must be more concentrated than every row"
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        "the trend must be monotone for the extrapolation to be the keyed one"
    return (f"the table runs to {max(c for c, _ in pairs):.0f} millimolar with a falling trend whose "
            f"minimum is {min(c for _, c in pairs):.0f}, so 250 millimolar extrapolates below it")


CLAIMS = [
 ("Hypotonic, hypertonic and isotonic",
  "EK 2.7.A.1 states that external environments can be hypotonic, hypertonic, or isotonic to internal environments of cells. The rejected sets belong to EK 2.3.A.2, EK 2.5, EK 1.5.A.1 and EK 1.4.A.1."),
 ("From hypotonic regions to hypertonic regions",
  "EK 2.7.A.1 states that movement of water can also be described as moving from hypotonic to hypertonic regions. The framework gives no direction fixed relative to the cell, only relative to the tonicity of the two regions."),
 ("From regions of high water potential to regions of low water potential",
  "EK 2.7.A.1 states that water moves by osmosis from regions of high water potential to regions of low water potential. The rejected option comparing a pressure potential with a solute potential compares two different quantities."),
 ("From regions of low solute concentration to regions of high solute",
  "EK 2.7.B.2 states that water moves from regions of low osmolarity or solute concentration to regions of high osmolarity or solute concentration, which is the same movement EK 2.7.A.1 calls hypotonic to hypertonic."),
 ("pressure potential and the solute potential, added together",
  "The equation printed with EK 2.7.A.1 gives water potential as the sum of the pressure potential and the solute potential. The other quantities named are inputs to the separate solute potential equation printed with EK 2.7.B.2."),
 ("pressure potential of the solution",
  "The equation printed with EK 2.7.B.2 takes the ionization constant, the molar concentration, the pressure constant and the Kelvin temperature. The pressure potential belongs to the water potential equation of EK 2.7.A.1, where it is ADDED to the solute potential rather than multiplied into it."),
 ("300 Kelvin",
  "The equation printed with EK 2.7.B.2 defines the Kelvin temperature as the Celsius temperature plus 273. Using the Celsius value unchanged, or subtracting rather than adding, are the two slips the distractors are built from."),
 ("maintains water balance and allows organisms to control their internal solute",
  "EK 2.7.B.2, near verbatim. Preventing all water movement would contradict EK 2.7.B.1's constant movement of molecules across membranes."),
 ("constant movement of molecules across membranes",
  "EK 2.7.B.1 states that growth and homeostasis are maintained by the constant movement of molecules across membranes. Removing every gradient would remove what EK 2.5.A.1 says selective permeability establishes."),
 ("contractile vacuole in protists and the central vacuole in plant cells",
  "These are the two illustrative examples printed with EK 2.7.A.1. The rejected pairs are organelles from EK 2.1.A.1 to EK 2.1.A.8, which the framework attaches to topic 2.1."),
 ("Solution 4",
  "Recomputed in q11 above from each row's own ionization constant, concentration and temperature through the equation printed with EK 2.7.B.2. Lowest means most negative, and the minimum is unique."),
 ("Solution 1 and Solution 2",
  "Recomputed in q12 above: exactly one pair of rows shares a solute potential, because a solute that dissociates into two particles at half the concentration gives the same product as one that does not dissociate."),
 ("About negative 12.5 bars",
  "Recomputed in q13 above from the row the stem identifies. The positive option ignores the minus sign the equation printed with EK 2.7.B.2 begins with, which is what makes every real solute potential negative."),
 ("About negative 5.0 bars",
  "Recomputed in q14 above: with the pressure potential zero, the water potential equation printed with EK 2.7.A.1 reduces to the solute potential alone, and the check confirms the two are identical. The stem supplies the pressure potential, so the cannot-be-determined option is false."),
 ("From the first solution to the second",
  "Recomputed in q15 above: both water potentials are rederived from the table and the first is the less negative, so it is the higher. EK 2.7.A.1 sends water from high water potential to low."),
 ("Cell A",
  "Recomputed in q16 above: exactly one row records a lower outside than inside solute concentration, which is what makes the external environment hypotonic under EK 2.7.A.1."),
 ("Cell B",
  "Recomputed in q17 above: exactly one row records a higher outside than inside solute concentration, which is what makes the external environment hypertonic under EK 2.7.A.1."),
 ("Cell C",
  "Recomputed in q18 above: exactly one row records equal concentrations, and the check confirms the three rows cover the three relations EK 2.7.A.1 names."),
 ("Cell A",
  "Recomputed in q19 above: exactly one row has the more concentrated side inside, and EK 2.7.B.2 sends water from low solute concentration to high."),
 ("Cell B",
  "Recomputed in q20 above: exactly one row has the more concentrated side outside, and EK 2.7.A.1 sends water from hypotonic toward hypertonic regions."),
 ("more dilute the surrounding solution, the more often",
  "Recomputed in q21 above: contractions fall at every step as the external concentration rises. EK 2.7.B.2 sends water toward the more concentrated region, so a dilute environment sends more water in for the contractile vacuole EK 2.7.A.1 names to expel."),
 ("Fewer contractions per minute than in any of the three solutions",
  "Recomputed in q22 above: the trend is monotone and the new solution is more concentrated than every tabulated row, so the extrapolation runs below the lowest value. EK 2.7.B.2 is why the trend continues rather than reversing."),
 ("no physical pressure applied to the solution beyond the surroundings",
  "The equation printed with EK 2.7.A.1 makes water potential the sum of the pressure potential and the solute potential, so a pressure potential of zero leaves the solute potential as the whole value. The solute potential is not itself zero unless there is no solute."),
 ("equation begins with a minus sign",
  "The equation printed with EK 2.7.B.2 takes the negative of a product of four quantities, each positive for a real solution, so the result is zero without solute and negative with it. None of the individual inputs is negative."),
 ("falls, because a larger concentration makes the solute potential more negative",
  "The equation printed with EK 2.7.B.2 makes the solute potential proportional to the molar concentration with a minus sign in front, and the equation printed with EK 2.7.A.1 adds that to a pressure potential of zero in an open beaker."),
 ("Water leaves the cell, because water moves toward the region of higher solute",
  "EK 2.7.B.2 sends water from regions of low solute concentration to regions of high, and EK 2.7.A.1 describes the same movement as hypotonic toward hypertonic, so a hypertonic exterior draws water out."),
 ("may undergo osmotic lysis",
  "EK 2.7.A.1 sends water from hypotonic toward hypertonic regions, so a hypotonic exterior drives water in, and EK 2.4.B.1 names protection from osmotic lysis among the roles of the cell walls of Bacteria, Archaea, Fungi and plants -- which an animal cell does not have."),
 ("no difference in water potential to drive net movement",
  "EK 2.7.A.1 drives osmosis by a difference in water potential and EK 2.7.B.2 by a difference in solute concentration, so equal concentrations leave no net direction. EK 2.7.B.1's constant movement of molecules across membranes rules out the claim that movement stops altogether."),
 ("expel less water, because less water now enters",
  "EK 2.7.B.2 sends water toward the more concentrated region, so narrowing the difference reduces the inward flow, and the same statement makes osmoregulation the maintenance of water balance. EK 2.7.A.1 offers the contractile vacuole of protists as its illustrative example."),
 ("from hypotonic to hypertonic regions, from low solute concentration to high",
  "EK 2.7.A.1 supplies the tonicity and the water potential descriptions and EK 2.7.B.2 the solute concentration description, and all three name the same movement, toward the more concentrated and lower water potential side. Each rejected option reverses one or two of the three."),
]

TABLE_CHECKS = {11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17,
                18: q18, 19: q19, 20: q20, 21: q21, 22: q22}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b2_7_mutant")
        mod.TOPIC = b2_7.TOPIC
        mod.QUESTIONS = copy.deepcopy(b2_7.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def concentration_changed(mod, claims):
        mod.QUESTIONS[12]["table"] = dict(
            headers=b2_7._T_WATERPOT["headers"],
            rows=[[lab, i, ("0.4" if lab == "Solution 3" else c), t]
                  for lab, i, c, t in b2_7._T_WATERPOT["rows"]])

    def equal_pair_broken(mod, claims):
        mod.QUESTIONS[11]["table"] = dict(
            headers=b2_7._T_WATERPOT["headers"],
            rows=[[lab, i, ("0.15" if lab == "Solution 2" else c), t]
                  for lab, i, c, t in b2_7._T_WATERPOT["rows"]])

    def temperature_differs(mod, claims):
        mod.QUESTIONS[10]["table"] = dict(
            headers=b2_7._T_WATERPOT["headers"],
            rows=[[lab, i, c, ("127" if lab == "Solution 3" else t)]
                  for lab, i, c, t in b2_7._T_WATERPOT["rows"]])

    def tonicity_duplicated(mod, claims):
        mod.QUESTIONS[15]["table"] = dict(
            headers=b2_7._T_TONICITY["headers"],
            rows=[["Cell A", "300", "150"], ["Cell B", "300", "100"], ["Cell C", "300", "300"]])

    def contraction_trend_broken(mod, claims):
        mod.QUESTIONS[20]["table"] = dict(
            headers=b2_7._T_CONTRACTILE["headers"],
            rows=[["Solution P", "5", "22"], ["Solution Q", "50", "11"],
                  ["Solution R", "150", "18"]])

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[2].__setitem__("ans", 1))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(9, ("no such phrase", c[9][1])))
    must_fail("a concentration changed so the keyed value is wrong", concentration_changed)
    must_fail("the equal-potential pair broken", equal_pair_broken)
    must_fail("one solution moved to a different temperature", temperature_differs)
    must_fail("a second cell made hypotonic, giving the item two answers", tonicity_duplicated)
    must_fail("the contraction trend made non-monotone", contraction_trend_broken)
    must_fail("a backslash macro in a stem",
              lambda m, c: m.QUESTIONS[4].__setitem__("q", "What is \\Psi equal to?"))
    print("all negative controls raised as required.")


import b2_7  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b2_7)
cg.check(b2_7, CLAIMS, table_checks=TABLE_CHECKS)
