"""Key audit for AP ENVIRONMENTAL SCIENCE 1.8 Primary Productivity.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1, 20, 28 and 29 rest on ENG-1.A.1: primary productivity is the rate at
which solar energy is converted into organic compounds via photosynthesis over a
unit of time.

Items 2 and 25 rest on ENG-1.A.2: gross primary productivity is the total rate
of photosynthesis in a given area.

Items 3, 5, 6, 7, 8, 15, 17, 18, 23, 24, 25 and 30 rest on ENG-1.A.3: net
primary productivity is the rate of energy storage by photosynthesizers in a
given area, after subtracting the energy lost to respiration.

Items 4, 13, 14, 19, 20 and 28 rest on ENG-1.A.4: productivity is measured in
units of energy per unit area per unit time.

Items 9, 10, 11, 12, 16, 21, 22, 26 and 27 rest on ENG-1.A.5: most red light is
absorbed in the upper one meter of water, blue light only penetrates deeper than
one hundred meters in the clearest water, and this affects photosynthesis in
aquatic ecosystems, whose photosynthesizers have adapted mechanisms to address
the lack of visible light.

THE ARITHMETIC. Items 5, 6, 7, 13, 14, 15 and 17 require a subtraction, a ratio
or a product. Every one is recomputed below from its own table, and each check
also falsifies the rival options against the same numbers. All the quantities are
round enough to be handled without a calculator.

DATA ITEMS: 5, 6, 7, 12, 13, 14, 15, 16, 17 and 21 carry tables.

NEGATIVE CONTROL: ``python3 verify_e1_8.py --selftest`` corrupts a key, an
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


GPP = "Gross primary productivity (kilocalories per square meter per year)"
RESP = "Energy lost to respiration (kilocalories per square meter per year)"
VALUE = "Value (kilocalories per square meter per year)"
RED = "Percent of surface red light still present"
BLUE = "Percent of surface blue light still present"
NPP = "Net primary productivity (kilocalories per square meter per year)"
AREA = "Area of the Earth covered (millions of square kilometers)"
STARTE = "Energy in plant tissue at the start of the year (kilocalories per square meter)"
ENDE = "Energy in plant tissue at the end of the year (kilocalories per square meter)"
BEST = "Depth at which it is most abundant (meters)"


def q5(table, item):
    labs = cg.labels(table)
    net = {lab: g - r for lab, g, r in zip(labs, cg.col(table, GPP), cg.col(table, RESP))}
    best = max(net, key=net.get)
    assert best == "Ecosystem 2", f"the largest net productivity is {best}, not Ecosystem 2"
    assert net["Ecosystem 2"] == 4000, f"Ecosystem 2 recomputes to {net['Ecosystem 2']}"
    assert net["Ecosystem 1"] == 3000 and net["Ecosystem 3"] == 800 and net["Ecosystem 4"] == 600, \
        f"the three distractor values must be the true nets of their own rows; got {net}"
    assert cg.cell(table, "Ecosystem 1", GPP) == 9000, \
        "the 'nine thousand' distractor must be Ecosystem 1's GROSS figure, not its net"
    return (f"subtracting respiration from gross gives {net}, so Ecosystem 2 at 4,000 "
            "kilocalories per square meter per year is the largest net value")


def q6(table, item):
    labs = cg.labels(table)
    share = {lab: r / g for lab, g, r in zip(labs, cg.col(table, GPP), cg.col(table, RESP))}
    worst = max(share, key=share.get)
    assert worst == "Ecosystem 1", f"the largest respired share is {worst}, not Ecosystem 1"
    assert abs(share["Ecosystem 1"] - 2 / 3) < 1e-9, f"Ecosystem 1 recomputes to {share['Ecosystem 1']}"
    assert abs(share["Ecosystem 2"] - 1 / 5) < 1e-9, "the one-fifth distractor must state Ecosystem 2's true share"
    assert abs(share["Ecosystem 3"] - 1 / 10) > 1e-9, \
        "the one-tenth distractor must be false for Ecosystem 3"
    assert abs(share["Ecosystem 4"] - 3 / 4) > 1e-9, \
        "the three-quarters distractor must be false for Ecosystem 4"
    assert len(set(round(v, 9) for v in share.values())) > 1, "'all four lose the same share' must be false"
    return (f"the respired shares recompute to {[round(v, 3) for v in share.values()]}, so "
            "Ecosystem 1 loses two thirds, the largest share")


def q7(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, VALUE)))
    gross = v["Gross primary productivity"]
    resp = v["Energy lost to respiration by the producers"]
    net = gross - resp
    assert net == 5000, f"net recomputes to {net}, not 5,000"
    assert gross + resp == 10000, "the 'ten thousand' distractor must be the sum, not the difference"
    assert resp == 2500 and gross == 7500, "the two remaining distractors must be the tabulated values themselves"
    return (f"{gross:.0f} minus {resp:.0f} is {net:.0f} kilocalories per square meter per "
            "year; the sum 10,000 and the two tabulated values are the rival options")


def q12(table, item):
    depth = [cg.num(r[0]) for r in table["rows"]]
    red = cg.col(table, RED)
    blue = cg.col(table, BLUE)
    assert red[depth.index(10)] == 0, "red light must be gone by ten meters"
    assert blue[-1] > 0, "blue light must still be measurable at the deepest row"
    assert blue[-1] < blue[0], "blue light must also decline with depth"
    assert red[-1] != red[0], "'red light is as strong at one hundred meters as at one' must be false"
    assert blue[depth.index(1)] > 50, "'neither color is present below one meter' must be false"
    return (f"red light reads {red} percent with depth and blue light {blue}, so red is gone "
            "within a few meters while blue persists to one hundred")


def q13(table, item):
    labs = cg.labels(table)
    rate = dict(zip(labs, cg.col(table, NPP)))
    area = dict(zip(labs, cg.col(table, AREA)))
    ocean = "Open ocean"
    assert rate[ocean] == min(rate.values()) or rate[ocean] < 0.2 * max(rate.values()), \
        "the open ocean must have a low rate per square meter"
    assert area[ocean] == max(area.values()), "the open ocean must cover the largest area"
    assert rate[ocean] != max(rate.values()), "'the open ocean has the highest rate' must be false"
    assert rate[ocean] != rate["Tropical rainforest"], \
        "'the open ocean matches rainforest per square meter' must be false"
    return (f"the open ocean's rate of {rate[ocean]:.0f} sits far below rainforest's "
            f"{rate['Tropical rainforest']:.0f}, yet its area {area[ocean]:.0f} is the "
            "largest of the three")


def q14(table, item):
    labs = cg.labels(table)
    rate = dict(zip(labs, cg.col(table, NPP)))
    area = dict(zip(labs, cg.col(table, AREA)))
    total = {lab: rate[lab] * area[lab] for lab in labs}
    best = max(total, key=total.get)
    assert best == "Open ocean", f"the largest total is {best}, not the open ocean"
    assert total["Open ocean"] > total["Tropical rainforest"], \
        "the ocean total must beat the rainforest total for the key to hold"
    assert total["Desert"] < total["Open ocean"], "'desert delivers the largest total' must be false"
    assert len(set(total.values())) == len(total), "'all three totals are equal' must be false"
    return (f"rate times area gives {[round(v) for v in total.values()]} in the table's own "
            "units, so the open ocean delivers the largest total despite the lowest rate")


def q15(table, item):
    gross = cg.col(table, GPP)
    resp = cg.col(table, RESP)
    net = [g - r for g, r in zip(gross, resp)]
    assert len(set(gross)) == 1, f"gross productivity must be constant; got {gross}"
    assert all(resp[i + 1] > resp[i] for i in range(len(resp) - 1)), f"respiration must rise; got {resp}"
    assert all(net[i + 1] < net[i] for i in range(len(net) - 1)), f"net must fall; got {net}"
    return (f"gross stays at {gross[0]:.0f} while respiration rises {resp}, so the net "
            f"recomputes to {net}, falling each year")


def q16(table, item):
    prod = cg.col(table, NPP)
    assert all(prod[i + 1] < prod[i] for i in range(len(prod) - 1)), \
        f"productivity must fall with depth; got {prod}"
    assert prod[-1] == min(prod), "'the deepest band is the most productive' must be false"
    assert prod[0] == max(prod), "'the shallowest band is the least productive' must be false"
    assert prod[0] > 100 * prod[-1], "the fall must be steep, not marginal"
    return (f"net productivity falls {prod} kilocalories per square meter per year from the "
            "surface band to the deepest")


def q17(table, item):
    labs = cg.labels(table)
    gain = {lab: e - s for lab, s, e in zip(labs, cg.col(table, STARTE), cg.col(table, ENDE))}
    assert gain["Plot 1"] > gain["Plot 2"], f"Plot 1 must gain more; got {gain}"
    assert all(v > 0 for v in gain.values()), "both plots must gain energy over the year"
    assert cg.cell(table, "Plot 1", STARTE) == cg.cell(table, "Plot 2", STARTE), \
        "the two plots must start equal, so 'same start means same productivity' is the tempting error"
    assert gain["Plot 1"] != gain["Plot 2"], "'the two had the same productivity' must be false"
    return (f"the plots gain {gain['Plot 1']:.0f} and {gain['Plot 2']:.0f} kilocalories per "
            "square meter over the year from an equal start")


def q21(table, item):
    rows = {r[0]: (cg.num(r[1]), r[2]) for r in table["rows"]}
    deep = max(rows, key=lambda k: rows[k][0])
    shallow = min(rows, key=lambda k: rows[k][0])
    assert rows[deep][1] == "Blue", f"the deeper alga must absorb blue best; got {rows[deep][1]}"
    assert rows[shallow][1] == "Red", f"the shallower alga must absorb red best; got {rows[shallow][1]}"
    assert rows[deep][0] > 10 * rows[shallow][0], "the two depths must differ substantially"
    return (f"the alga at {rows[deep][0]:.0f} meters absorbs blue best and the one at "
            f"{rows[shallow][0]:.0f} meter absorbs red best, matching the colors that reach "
            "those depths")


CLAIMS = [
 ("converted into organic compounds by photosynthesis",
  "ENG-1.A.1, near verbatim: primary productivity is the rate at which solar energy (sunlight) is converted into organic compounds via photosynthesis over a unit of time. It is a rate, not a standing quantity."),
 ("total rate of photosynthesis",
  "ENG-1.A.2, near verbatim: gross primary productivity is the total rate of photosynthesis in a given area. The subtraction of respiration belongs to ENG-1.A.3, not to the gross figure."),
 ("rate of energy storage by photosynthesizers",
  "ENG-1.A.3, near verbatim: net primary productivity is the rate of energy storage by photosynthesizers in a given area, after subtracting the energy lost to respiration."),
 ("per unit area per unit time",
  "ENG-1.A.4, near verbatim: productivity is measured in units of energy per unit area per unit time. Each rejected option drops the energy, the area or the time."),
 ("four thousand kilocalories",
  "Recomputed in q5 above: each ecosystem's net figure is its gross column less its respiration column, and the largest of those differences is 4,000. The 'nine thousand' option is one row's GROSS figure, which ENG-1.A.3 excludes."),
 ("two thirds",
  "Recomputed in q6 above: the share of gross productivity lost is respiration divided by gross, and the largest of those ratios is two thirds. The two remaining fractions are checked false for the rows they name."),
 ("Five thousand kilocalories",
  "Recomputed in q7 above: ENG-1.A.3 subtracts the energy lost to respiration from the gross rate, giving 5,000. The sum, 10,000, and the two tabulated values themselves are the rival options."),
 ("smaller than gross primary productivity",
  "ENG-1.A.3 obtains the net figure by subtracting the energy lost to respiration from the gross rate of ENG-1.A.2, so any respiration at all makes the net figure the smaller of the two."),
 ("absorbed in the upper one meter",
  "ENG-1.A.5, near verbatim: most red light is absorbed in the upper one meter of water, which is exactly what distinguishes it from blue light in the same sentence."),
 ("only in the clearest water",
  "ENG-1.A.5, near verbatim: blue light only penetrates deeper than one hundred meters in the clearest water. Both the depth and the qualification about clarity are part of the claim."),
 ("adapted mechanisms to address the lack of visible light",
  "ENG-1.A.5, near verbatim: this affects photosynthesis in aquatic ecosystems, whose photosynthesizers have adapted mechanisms to address the lack of visible light."),
 ("Red light is essentially gone",
  "Recomputed in q12 above: the red column reaches zero by ten meters while the blue column is still measurable at one hundred. ENG-1.A.5 states both halves of that contrast."),
 ("by far the largest area",
  "Recomputed in q13 above: the open ocean holds the low rate per square meter and the largest tabulated area. ENG-1.A.4 makes productivity a rate per unit area, so a rate and a whole-biome total are different quantities."),
 ("large enough to outweigh",
  "Recomputed in q14 above: multiplying each tabulated rate by its tabulated area makes the open ocean's total the largest of the three. ENG-1.A.4 requires the area as well as the rate to reach a total."),
 ("fell each year, because respiration rose",
  "Recomputed in q15 above: gross productivity is constant across the three years while respiration rises, so the difference required by ENG-1.A.3 shrinks each year."),
 ("falls steeply with depth",
  "Recomputed in q16 above: net productivity falls at every step down the depth column. ENG-1.A.5 states that light is absorbed with depth in water and that this affects photosynthesis in aquatic ecosystems."),
 ("gained more energy over the year",
  "Recomputed in q17 above: both plots start equal and one gains far more energy in plant tissue. ENG-1.A.3 makes net primary productivity the rate of energy storage by photosynthesizers after respiration is subtracted."),
 ("not added to it",
  "ENG-1.A.3 states that net primary productivity is the rate of energy storage AFTER SUBTRACTING the energy lost to respiration, so the student has reversed the operation."),
 ("Kilocalories per square meter per year",
  "ENG-1.A.4 states that productivity is measured in units of energy per unit area per unit time and gives kilocalories per square meter per year as its own example. Each rejected option drops one of the three parts."),
 ("not a standing amount",
  "ENG-1.A.1 defines primary productivity as a RATE over a unit of time and ENG-1.A.4 requires units of energy per unit area per unit time, so a quantity with no time in it is a different measurement."),
 ("penetrates deeper into water",
  "Recomputed in q21 above: the alga most abundant at depth is the one whose pigments absorb blue best, and blue is the color ENG-1.A.5 says penetrates far deeper than red. ENG-1.A.5 also attributes adapted mechanisms to aquatic photosynthesizers."),
 ("progressively absorbed with depth",
  "ENG-1.A.5 states that most red light is absorbed in the upper one meter and that blue light reaches beyond one hundred meters only in the clearest water, then attributes the difficulty of aquatic photosynthesis to that lack of visible light."),
 ("reduced by the same subtraction",
  "ENG-1.A.3 makes the net figure the gross rate less the energy lost to respiration, so raising the first term while holding the second constant raises the difference."),
 ("energy stored in the plot's plant tissue",
  "ENG-1.A.3 defines net primary productivity as the rate of energy storage by photosynthesizers after respiration is subtracted, so the energy that has actually accumulated in plant tissue over a known period is the quantity sought."),
 ("Gross measures the total rate of photosynthesis",
  "ENG-1.A.2 defines gross primary productivity as the total rate of photosynthesis in a given area and ENG-1.A.3 defines net primary productivity as the rate of energy storage after subtracting the energy lost to respiration."),
 ("greater depth in the clearer lake",
  "ENG-1.A.5 states that blue light penetrates deeper than one hundred meters only in the CLEAREST water, which makes clarity the condition on how far light reaches and so on the depth at which photosynthesis is possible."),
 ("still present there",
  "ENG-1.A.5 attributes adapted mechanisms specifically to the lack of visible light, so the evidence bearing on it is a feature that lets an organism use the light that remains. Size, salinity tolerance and reproductive rate address other problems."),
 ("rate of energy conversion or storage",
  "ENG-1.A.4 states that productivity is measured in units of energy per unit area per unit time, and the reported value carries exactly those three parts, so it is a productivity figure rather than a standing total."),
 ("defined as the rate at which sunlight is converted",
  "ENG-1.A.1 defines primary productivity as the rate at which solar energy (sunlight) is converted into organic compounds via photosynthesis over a unit of time, so sunlight is the input the definition itself names."),
 ("loses more of its gross productivity",
  "ENG-1.A.3 makes stored energy the gross rate less the energy lost to respiration, so with the gross figures equal the difference in storage must come from the size of that subtraction."),
]

TABLE_CHECKS = {5: q5, 6: q6, 7: q7, 12: q12, 13: q13, 14: q14,
                15: q15, 16: q16, 17: q17, 21: q21}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("e1_8_mutant")
        mod.TOPIC = e1_8.TOPIC
        mod.QUESTIONS = copy.deepcopy(e1_8.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[1]["ans"] = 2

    def break_anchor(mod, claims):
        claims[8] = ("no such phrase anywhere in the module", claims[8][1])

    def corrupt_arithmetic(mod, claims):
        # change one respiration figure so the keyed net value is no longer 5,000
        mod.QUESTIONS[6]["table"] = dict(
            headers=e1_8._T_ONEPLOT["headers"],
            rows=[[k, ("3000" if k.startswith("Energy lost") else v)]
                  for k, v in e1_8._T_ONEPLOT["rows"]])

    def corrupt_table(mod, claims):
        # let respiration fall instead of rise, so net no longer declines
        mod.QUESTIONS[14]["table"] = dict(
            headers=e1_8._T_YEARS["headers"],
            rows=[[y, g, r] for (y, g, _), r in
                  zip(e1_8._T_YEARS["rows"], ["4500", "3000", "2000"])])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[3]["choices"][1] = mod.QUESTIONS[3]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[17]["why"] = "It just is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[24]["why"] = ("Choice E is wrong because the framework says so and "
                                    "the rest of the reasoning follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[3]["choices"][4] = "Area per unit time, written \\frac{m}{yr}"
        style(mod)

    def slash_units_slip_in(mod, claims):
        mod.QUESTIONS[18]["choices"][0] = "Kilocalories per 1/2 square meter per year."
        style(mod)

    print("negative controls:")
    must_fail("a backslash macro in a choice", latex_slips_in)
    must_fail("a slash fraction in a choice", slash_units_slip_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer in the keyed choice", break_anchor)
    must_fail("a table value changed so the keyed arithmetic is wrong", corrupt_arithmetic)
    must_fail("a table trend reversed so the keyed conclusion is false", corrupt_table)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a why reduced below the minimum", thin_why)
    must_fail("a why naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import e1_8  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(e1_8)
cg.check(e1_8, CLAIMS, table_checks=TABLE_CHECKS)
