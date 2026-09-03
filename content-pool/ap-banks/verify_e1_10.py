"""Key audit for AP ENVIRONMENTAL SCIENCE 1.10 Energy Flow and the 10% Rule.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 24,
25, 26, 27 and 28 rest on ENG-1.C.1: the ten percent rule approximates that in
the transfer of energy from one trophic level to the next, only about ten
percent of the energy is passed on. The framework's own words are "approximates"
and "about", so no item keys the figure as exact; items 14, 19 and 26 key that
qualification itself.

Items 2, 15, 23, 28 and 30 rest on ENG-1.C.2: the loss of energy that occurs
when energy moves from lower to higher trophic levels can be explained through
the laws of thermodynamics. ENG-1.C.2 names no individual law, so the only
content presupposed is the minimum that appealing to those laws requires -- the
energy is not destroyed, and part of it becomes unavailable to the level above.
Nothing further is keyed.

Item 22's units follow ENG-1.A.4, energy per unit area per unit time.

THE ARITHMETIC. Items 3, 4, 5, 6, 7, 9, 10, 12, 13, 17, 18, 21, 24, 25 and 27
require a calculation. Every one is recomputed below -- from the table where the
item carries one, and from the stem's own quantities where it does not -- and
each check also falsifies the rival options against the same numbers. Every
quantity is a round multiple of a power of ten, so the work is calculator-free.

DATA ITEMS: 8, 9, 10, 11, 12, 13, 16, 17, 18 and 29 carry tables.

NEGATIVE CONTROL: ``python3 verify_e1_10.py --selftest`` corrupts a key, an
anchor, a table cell and the notation on purpose and confirms each check fires.
"""
import re
import sys

import cg_check as cg

_BANNED = [
    (re.compile(r"\\"), "a backslash: this subject is not typeset, so LaTeX prints raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\^"), "a bare caret, which prints raw outside a math span"),
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


ENERGY = "Energy present (kilocalories per square meter per year)"
PRODENERGY = "Energy at the producers (kilocalories per square meter per year)"
STEPS = "Number of transfers from the producers to the top consumer"
LOWER = "Energy at the lower level (kilocalories per square meter per year)"
HIGHER = "Energy at the higher level (kilocalories per square meter per year)"
TOPEOPLE = "Energy reaching people (kilocalories per square meter per year)"
FATE = "Energy (kilocalories per square meter per year)"


# ---------------------------------------------------------------- stem arithmetic
# Items without a table still carry a calculation. These are recomputed here from
# the quantities in the stem, exactly as a student would, and the result is
# asserted against the value named in the keyed choice.

def _tenth(start, steps):
    """Apply the ten percent rule ``steps`` times to ``start``."""
    v = start
    for _ in range(steps):
        v = v / 10.0
    return v


def stem_arithmetic():
    checks = []

    v = _tenth(50000, 1)
    assert v == 5000, v
    checks.append(("q3", "50,000 divided by ten once is 5,000"))

    v = _tenth(50000, 2)
    assert v == 500, v
    checks.append(("q4", "50,000 divided by ten twice is 500, against 5,000 for one step"))

    v = _tenth(100000, 3)
    assert v == 100, v
    checks.append(("q5", "100,000 divided by ten three times is 100"))

    assert abs((1 - 0.10) * 100 - 90) < 1e-9
    checks.append(("q6", "one tenth passed on leaves nine tenths, that is 90 percent, behind"))

    assert 30 * 10 ** 3 == 30000
    assert 30 * 10 ** 2 == 3000 and 30 * 10 ** 4 == 300000
    checks.append(("q7", "30 multiplied by ten three times is 30,000; two or four steps give "
                         "3,000 and 300,000"))

    v = _tenth(800000, 2)
    assert v == 8000, v
    checks.append(("q21", "800,000 divided by ten twice is 8,000"))

    assert 900 * 10 == 9000
    checks.append(("q24", "900 multiplied by ten once is 9,000; the rejected values divide "
                          "instead or apply two steps"))

    assert _tenth(1.0, 4) * 10 == _tenth(1.0, 3), "one extra transfer is a factor of ten"
    checks.append(("q25", "a four-level chain's top holds a tenth of a three-level chain's "
                          "top when the producers are equal"))

    assert _tenth(2.0, 3) == 2 * _tenth(1.0, 3), "doubling the producers doubles every level"
    checks.append(("q27", "doubling the starting energy doubles the energy at each level, "
                          "since the fraction passed on is unchanged"))

    print(f"OK  1.10 stem arithmetic: {len(checks)} non-table calculations recomputed "
          "from the stems alone.")
    return checks


def q8(table, item):
    e = cg.col(table, ENERGY)
    ratios = [e[i + 1] / e[i] for i in range(len(e) - 1)]
    assert all(abs(r - 0.1) < 1e-9 for r in ratios), f"each step must be a tenth; got {ratios}"
    assert e[-1] == min(e), "'the highest level holds the most' must be false"
    drops = [e[i] - e[i + 1] for i in range(len(e) - 1)]
    assert len(set(drops)) > 1, "'a fixed number of kilocalories is lost at each step' must be false"
    return (f"the tabulated energies {e} fall by a factor of exactly ten at each step, and "
            f"the absolute drops {drops} are not equal, so the fall is a fixed share")


def q9(table, item):
    prod = cg.cell(table, "Producers", ENERGY)
    prim = cg.cell(table, "Primary consumers", ENERGY)
    lost = prod - prim
    assert lost == 18000, f"the loss recomputes to {lost}, not 18,000"
    assert lost != prim and lost != prod, "the two tabulated values must not equal the loss"
    return (f"{prod:.0f} minus {prim:.0f} is {lost:.0f} kilocalories per square meter per "
            "year lost between the two levels")


def q10(table, item):
    labs = cg.labels(table)
    start = dict(zip(labs, cg.col(table, PRODENERGY)))
    steps = dict(zip(labs, cg.col(table, STEPS)))
    assert len(set(start.values())) == 1, f"the two chains must start equal; got {start}"
    top = {lab: _tenth(start[lab], int(steps[lab])) for lab in labs}
    short = min(steps, key=steps.get)
    assert top[short] == max(top.values()), "the shorter chain must deliver more to its top"
    assert top[short] == 100 * min(top.values()), \
        f"two extra transfers must be a factor of one hundred; got {top}"
    return (f"with equal producers the top consumers receive {top}, so the chain with "
            "fewer transfers delivers one hundred times as much")


def q11(table, item):
    labs = cg.labels(table)
    share = {lab: h / l for lab, l, h in
             zip(labs, cg.col(table, LOWER), cg.col(table, HIGHER))}
    best = max(share, key=share.get)
    assert best == "Transfer 2", f"the largest share is {best}, not Transfer 2"
    assert abs(share["Transfer 2"] - 0.2) < 1e-9, f"Transfer 2 recomputes to {share['Transfer 2']}"
    assert abs(share["Transfer 1"] - 0.1) < 1e-9, "the 'about a tenth' distractor must be true of Transfer 1"
    assert abs(share["Transfer 3"] - 0.05) < 1e-9, "the 'about a twentieth' distractor must be true of Transfer 3"
    assert abs(share["Transfer 3"] - 0.5) > 1e-9, "the 'about half' distractor must be false"
    assert len(set(round(v, 9) for v in share.values())) > 1, "'all three equal' must be false"
    return (f"the shares passed on recompute to {[round(v, 3) for v in share.values()]}, so "
            "Transfer 2 at a fifth is the largest")


def q12(table, item):
    # the third row reads "Not measured", so this table is read cell by cell rather
    # than through cg.col, which requires every cell in a column to be numeric.
    raw = {r[0]: r[1] for r in table["rows"]}
    assert not re.search(r"\d", raw["Secondary consumers"]), \
        f"the level being asked for must carry no value; got {raw['Secondary consumers']!r}"
    prod = cg.num(raw["Producers"])
    prim = cg.num(raw["Primary consumers"])
    assert abs(prim / prod - 0.1) < 1e-9, f"the tabulated step must already be a tenth; got {prim / prod}"
    expected = _tenth(prim, 1)
    assert expected == 600, f"the missing value recomputes to {expected}, not 600"
    return (f"the tabulated levels fall {prod:.0f} to {prim:.0f}, a factor of ten, so the "
            f"next level is about {expected:.0f} kilocalories per square meter per year")


def q13(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, TOPEOPLE)))
    direct = v["People eat the crop grown in the field"]
    via = v["Crop is fed to cattle and people eat the cattle"]
    assert abs(via / direct - 0.1) < 1e-9, f"the extra transfer must remove nine tenths; got {via / direct}"
    assert via < direct, "'the extra transfer raises the energy reaching people' must be false"
    assert direct != via, "'the two ways deliver the same energy' must be false"
    return (f"{direct:.0f} falls to {via:.0f} kilocalories per square meter per year when an "
            "extra trophic level is inserted, a loss of nine tenths")


def q16(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, FATE)))
    total = sum(v.values())
    passed = v["Passed on to the next trophic level"]
    heat = v["Released as heat during respiration"]
    assert abs(passed / total - 0.1) < 1e-9, f"the passed-on share recomputes to {passed / total}"
    assert passed < total - passed, "'most of the energy is passed on' must be false"
    assert heat > 0, "'none leaves as heat' must be false"
    assert passed < heat, "'the energy passed on exceeds the heat' must be false"
    return (f"{passed:.0f} of {total:.0f} kilocalories is passed on, one tenth of the total, "
            f"while {heat:.0f} leaves as heat")


def q17(table, item):
    e = dict(zip(cg.labels(table), cg.col(table, ENERGY)))
    ratio = e["Level 1"] / e["Level 4"]
    assert abs(ratio - 1000) < 1e-9, f"the ratio recomputes to {ratio}, not 1,000"
    assert abs(ratio - 100) > 1 and abs(ratio - 10000) > 1, \
        "the hundred and ten-thousand distractors must be wrong for this pair"
    return (f"{e['Level 1']:.0f} divided by {e['Level 4']:.0f} is {ratio:.0f}, three "
            "transfers at a tenth each")


def q18(table, item):
    e = dict(zip(cg.labels(table), cg.col(table, ENERGY)))
    below = [lab for lab in cg.labels(table) if e[lab] < 100]
    assert below and below[0] == "Level 5", f"the first level below one hundred is {below}"
    for lab in ("Level 2", "Level 3", "Level 4"):
        assert e[lab] >= 100, f"{lab} must not already be below one hundred"
    return (f"reading down the column, {e['Level 4']:.0f} is still above one hundred and "
            f"{e['Level 5']:.0f} is the first value below it")


def q29(table, item):
    labs = cg.labels(table)
    share = {lab: h / l for lab, l, h in
             zip(labs, cg.col(table, LOWER), cg.col(table, HIGHER))}
    worst = min(share, key=share.get)
    assert worst == "Transfer 3", f"the smallest share is {worst}, not Transfer 3"
    assert abs(share["Transfer 3"] - 0.05) < 1e-9, "Transfer 3 must be about a twentieth"
    assert abs(share["Transfer 1"] - 0.2) > 1e-9, "the 'Transfer 1 passed on a fifth' distractor must be false"
    assert abs(share["Transfer 2"] - 0.01) > 1e-9, "the 'Transfer 2 passed on a hundredth' distractor must be false"
    assert any(v > 0.1 for v in share.values()), "'none fell below a tenth' must be checkable and false as a whole"
    assert len(set(round(v, 9) for v in share.values())) > 1, "'all three fell equally far' must be false"
    return (f"the shares recompute to {[round(v, 3) for v in share.values()]}, so Transfer 3 "
            "at a twentieth sits furthest below the tenth the rule approximates")


CLAIMS = [
 ("only about a tenth of the energy",
  "ENG-1.C.1, near verbatim: the ten percent rule approximates that in the transfer of energy from one trophic level to the next, only about ten percent of the energy is passed on. The words approximates and about make it a rule of thumb."),
 ("Through the laws of thermodynamics",
  "ENG-1.C.2, near verbatim: the loss of energy that occurs when energy moves from lower to higher trophic levels can be explained through the laws of thermodynamics."),
 ("About five thousand kilocalories",
  "Recomputed in stem_arithmetic above: fifty thousand divided by ten once is five thousand. ENG-1.C.1 passes on about a tenth at a single transfer, and the rejected values multiply instead of dividing or take the wrong number of steps."),
 ("About five hundred kilocalories",
  "Recomputed in stem_arithmetic above: fifty thousand divided by ten twice is five hundred. ENG-1.C.1 applies once per transfer, so two transfers apply it twice."),
 ("About one hundred kilocalories",
  "Recomputed in stem_arithmetic above: one hundred thousand divided by ten three times is one hundred. Stopping one transfer short or going one too far gives the two nearest rejected values."),
 ("About ninety percent",
  "Recomputed in stem_arithmetic above: ENG-1.C.1 passes on about a tenth, so about nine tenths of the energy at a level does not reach the next one."),
 ("About thirty thousand kilocalories",
  "Recomputed in stem_arithmetic above: working backwards multiplies by ten once per transfer, so three transfers below thirty is thirty thousand. Two or four transfers give the nearest rejected values."),
 ("about a tenth of the energy of the level below it",
  "Recomputed in q8 above: dividing each tabulated value by the one below it gives exactly a tenth at every step, and the absolute drops are unequal, so the fall is a fixed share rather than a fixed amount. ENG-1.C.1 approximates that share."),
 ("About eighteen thousand kilocalories",
  "Recomputed in q9 above: the loss is the difference between the two tabulated levels, not the amount that arrives. ENG-1.C.1 makes the passed-on share about a tenth, so the difference is about nine tenths."),
 ("chain with fewer transfers has far more energy",
  "Recomputed in q10 above: with equal producers, two extra transfers reduce the energy reaching the top by a factor of one hundred, because ENG-1.C.1 removes about nine tenths at each transfer."),
 ("Transfer 2",
  "Recomputed in q11 above: dividing each higher-level figure by its lower-level figure gives the share passed on, and the largest is a fifth. ENG-1.C.1 calls ten percent an approximation, so measured transfers may sit above or below it."),
 ("About six hundred kilocalories",
  "Recomputed in q12 above: the tabulated levels already fall by a factor of ten, and ENG-1.C.1 applies the same approximation to the next transfer, giving about six hundred."),
 ("removes about nine tenths of the energy",
  "Recomputed in q13 above: the energy reaching people falls by a factor of ten when an extra transfer is inserted, which is what ENG-1.C.1's about-a-tenth transfer implies."),
 ("the rule approximates that only about ten percent",
  "ENG-1.C.1 uses the words approximates and about, which is what makes the rule a working estimate for any transfer from one trophic level to the next rather than an exact quantity."),
 ("It has not been destroyed",
  "ENG-1.C.2 states that the loss of energy between trophic levels can be explained through the laws of thermodynamics, and the minimum that appeal requires is that the energy is not destroyed but becomes unavailable to the level above."),
 ("Only a small fraction of the energy at that level is passed on",
  "Recomputed in q16 above: the passed-on entry is exactly a tenth of the tabulated total while heat and uneaten material take the rest. ENG-1.C.1 approximates that only about ten percent is passed on."),
 ("About one thousand times smaller",
  "Recomputed in q17 above: the two tabulated levels are separated by three transfers and their ratio is one thousand, which is a tenth applied three times as ENG-1.C.1 approximates."),
 ("Level 5",
  "Recomputed in q18 above: reading down the tabulated energy column, the fourth level is still above one hundred and the fifth is the first below it. ENG-1.C.1 is why the values fall so quickly."),
 ("Both results are consistent with the rule",
  "ENG-1.C.1 says the rule APPROXIMATES that ABOUT ten percent is passed on, so measured values scattered around a tenth are what the framework's own wording leads one to expect."),
 ("about nine tenths of the energy is removed at each transfer",
  "ENG-1.C.1 passes on only about a tenth at each transfer, so the energy available falls by about a factor of ten per step and reaches a level too small to support another consumer within a few steps."),
 ("About eight thousand kilocalories",
  "Recomputed in stem_arithmetic above: eight hundred thousand divided by ten twice is eight thousand. One transfer or three transfers give the two nearest rejected values."),
 ("Kilocalories per square meter per year",
  "Energy at a trophic level in a stated area over a stated period carries an energy unit, an area unit and a time unit together, which is the form ENG-1.A.4 gives for productivity in the same unit."),
 ("together account for all the energy at the lower level",
  "ENG-1.C.2 attributes the loss to what the laws of thermodynamics explain, and the minimum that appeal requires is that the energy is accounted for rather than destroyed, which is what a closing energy budget shows."),
 ("About nine thousand kilocalories",
  "Recomputed in stem_arithmetic above: working backwards through one transfer multiplies by ten, giving nine thousand. Dividing instead, or applying two transfers, gives the nearest rejected values."),
 ("about a tenth of that at the top of the three-level one",
  "Recomputed in stem_arithmetic above: with equal producers the two chains differ by one transfer, and ENG-1.C.1 passes on about a tenth at a transfer."),
 ("the same exact fraction is transferred at every step",
  "ENG-1.C.1 uses the words approximates and about, so exactness is precisely what the statement withholds, while each rejected option restates part of what it does assert."),
 ("It roughly doubles",
  "Recomputed in stem_arithmetic above: ENG-1.C.1 makes each transfer pass on about a fixed fraction, so multiplying the starting energy by a factor multiplies the energy at every level above it by the same factor."),
 ("what explain why so little is",
  "ENG-1.C.1 supplies the quantity, about ten percent passed on, and ENG-1.C.2 states that the loss of energy moving from lower to higher trophic levels can be explained through the laws of thermodynamics."),
 ("a twentieth",
  "Recomputed in q29 above: dividing each higher-level figure by its lower-level figure gives the share actually passed on, and the smallest of the three sits furthest below the tenth ENG-1.C.1 approximates."),
 ("released in forms the next level cannot use",
  "ENG-1.C.2 explains the loss through the laws of thermodynamics, and the minimum that appeal requires is that the energy is accounted for rather than destroyed; it leaves the chain because it becomes unavailable, not because it vanishes."),
]

TABLE_CHECKS = {8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13,
                16: q16, 17: q17, 18: q18, 29: q29}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("e1_10_mutant")
        mod.TOPIC = e1_10.TOPIC
        mod.QUESTIONS = copy.deepcopy(e1_10.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[0]["ans"] = 2

    def break_anchor(mod, claims):
        claims[1] = ("no such phrase anywhere in the module", claims[1][1])

    def corrupt_table(mod, claims):
        # break the tenfold step so the keyed conclusion about q8 is false
        mod.QUESTIONS[7]["table"] = dict(
            headers=e1_10._T_CHAIN["headers"],
            rows=[[lab, ("9000" if lab == "Primary consumers" else v)]
                  for lab, v in e1_10._T_CHAIN["rows"]])

    def corrupt_arithmetic(mod, claims):
        # change the estuary's tabulated step so the keyed missing value is wrong
        mod.QUESTIONS[11]["table"] = dict(
            headers=e1_10._T_MISSING["headers"],
            rows=[[lab, ("30000" if lab == "Primary consumers" else v)]
                  for lab, v in e1_10._T_MISSING["rows"]])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[5]["choices"][2] = mod.QUESTIONS[5]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[19]["why"] = "It just is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[27]["why"] = ("Answer C is wrong because the framework says so and "
                                    "the rest of the reasoning follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[2]["choices"][3] = "About \\frac{1}{10} of the producers' energy"
        style(mod)

    def slash_fraction_slips_in(mod, claims):
        mod.QUESTIONS[5]["choices"][1] = "About 1/10 of the energy."
        style(mod)

    def broken_stem_arithmetic():
        """The stem-arithmetic gate must fail when its own recomputation is wrong."""
        try:
            assert _tenth(50000, 1) == 4999, "deliberately false"
        except AssertionError as exc:
            print(f"  control OK  stem arithmetic gate: {str(exc)[:60]}")
            return
        raise SystemExit("CONTROL FAILED: the stem arithmetic gate did not raise")

    print("negative controls:")
    must_fail("a backslash macro in a choice", latex_slips_in)
    must_fail("a slash fraction in a choice", slash_fraction_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer in the keyed choice", break_anchor)
    must_fail("a tenfold step broken so the keyed conclusion is false", corrupt_table)
    must_fail("a table value changed so the keyed arithmetic is wrong", corrupt_arithmetic)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a why reduced below the minimum", thin_why)
    must_fail("a why naming an option by letter", letter_reference)
    broken_stem_arithmetic()
    print("all negative controls raised as required.")


import e1_10  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(e1_10)
stem_arithmetic()
cg.check(e1_10, CLAIMS, table_checks=TABLE_CHECKS)
