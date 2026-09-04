"""Key audit for AP ENVIRONMENTAL SCIENCE 2.4 Ecological Tolerance.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
ERT-2.F.1  Ecological tolerance refers to the range of conditions, such as
           temperature, salinity, flow rate, and sunlight, that an organism can
           endure before injury or death results.
                     -- items 1, 2, 3, 4, 7, 8 to 18, 21, 22, 23, 24, 26, 28,
                        29, 30
ERT-2.F.2  Ecological tolerance can apply to individuals and to species.
                     -- items 5, 6, 19, 20, 25, 29, 30

The statement has four moving parts and every key uses one: it is a RANGE, not
a value; the conditions are exemplified by temperature, salinity, flow rate and
sunlight; the end of the range is marked by INJURY OR DEATH; and it applies to
individuals as well as to species.

WHAT IS DELIBERATELY NOT ASKED. The framework gives no optimal range, no zone
of stress, no law of the minimum, and no comparison between one species' range
and another's. Item 27 keys exactly that absence. Where a table shows one
species enduring a wider range than another, the keyed conclusion is arithmetic
ON THAT TABLE -- a subtraction of two printed limits, or a test of whether a
stated condition falls between them -- and never a prediction of a limit the
table does not print.

DATA ITEMS: 8 to 22 carry tables. Every keyed conclusion is recomputed below
from that table alone, read by column header rather than by index.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Two of these tables survive a
column reversal because a reversed pair of limit columns is still a pair of
limits; e_check then flattens them, and the checks below fail on the flattened
table because each one needs the limits to differ. ``python3 verify_e2_4.py
--selftest`` is the same run; the controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e2_4

TLO = "Lowest water temperature endured without injury (degrees Celsius)"
THI = "Highest water temperature endured without injury (degrees Celsius)"
SLO = "Lowest salinity endured (parts per thousand)"
SHI = "Highest salinity endured (parts per thousand)"
FLO = "Lowest flow rate endured (centimetres per second)"
FHI = "Highest flow rate endured (centimetres per second)"
NLO = "Lowest daily sunlight endured (hours)"
NHI = "Highest daily sunlight endured (hours)"
INDLIM = "Highest water temperature it endured without injury (degrees Celsius)"
TANK = "Water temperature held in the tank (degrees Celsius)"
SURV = "Percent of the fish surviving thirty days"


def _widths(table, lo, hi):
    """{row label: upper limit less lower limit}, with the pair sane."""
    labs = cg.labels(table)
    low = cg.col(table, lo)
    high = cg.col(table, hi)
    out = {}
    for lab, a, b in zip(labs, low, high):
        assert b >= a, f"{lab}: the upper limit {b} is below the lower limit {a}"
        out[lab] = b - a
    return out


def _endures(table, lo, hi, value):
    """Row labels whose printed range contains ``value``."""
    labs = cg.labels(table)
    low = cg.col(table, lo)
    high = cg.col(table, hi)
    return [lab for lab, a, b in zip(labs, low, high) if a <= value <= b]


def q8(table, item):
    w = _widths(table, TLO, THI)
    widest = max(w, key=w.get)
    assert widest == "Fish 3", f"Fish 3 must endure the widest range; got {widest}"
    assert len(set(w.values())) == len(w), "'all four are the same width' must be false"
    return f"the four temperature ranges are {w}, and the widest belongs to {widest}"


def q9(table, item):
    w = _widths(table, TLO, THI)
    lo = dict(zip(cg.labels(table), cg.col(table, TLO)))
    hi = dict(zip(cg.labels(table), cg.col(table, THI)))
    assert w["Fish 1"] == 22, f"the first species' range must be 22 degrees; got {w['Fish 1']}"
    assert hi["Fish 1"] != 22 and lo["Fish 1"] != 22, \
        "the width must not coincide with either printed limit"
    return (f"the first species runs {lo['Fish 1']:.0f} to {hi['Fish 1']:.0f} degrees "
            f"Celsius, a width of {w['Fish 1']:.0f}")


def q10(table, item):
    who = _endures(table, TLO, THI, 30)
    assert who == ["Fish 3"], f"exactly Fish 3 must endure 30 degrees; got {who}"
    return (f"exactly one of the four species has 30 degrees Celsius between its printed "
            f"limits, and it is {who[0]}")


def q11(table, item):
    w = _widths(table, TLO, THI)
    narrowest = min(w, key=w.get)
    assert narrowest == "Fish 2", f"Fish 2 must endure the narrowest range; got {narrowest}"
    assert len(set(w.values())) == len(w), "the four widths must all differ"
    return f"the four temperature ranges are {w}, and the narrowest belongs to {narrowest}"


def q12(table, item):
    w = _widths(table, SLO, SHI)
    widest = max(w, key=w.get)
    assert widest == "Estuary species 2", \
        f"the second estuary species must endure the widest range; got {widest}"
    assert len(set(w.values())) == len(w), "'all four are the same width' must be false"
    return f"the four salinity ranges are {w}, and the widest belongs to {widest}"


def q13(table, item):
    both = [lab for lab in _endures(table, SLO, SHI, 5)
            if lab in _endures(table, SLO, SHI, 32)]
    assert both == ["Estuary species 2"], \
        f"exactly the second estuary species must endure both salinities; got {both}"
    assert len(both) != len(table["rows"]), "'every one of the four' must be false"
    return (f"exactly one of the four species has both 5 and 32 parts per thousand between "
            f"its printed limits, and it is {both[0]}")


def q14(table, item):
    w = _widths(table, SLO, SHI)
    lo = dict(zip(cg.labels(table), cg.col(table, SLO)))
    hi = dict(zip(cg.labels(table), cg.col(table, SHI)))
    key = "Estuary species 3"
    assert w[key] == 11, f"the third species' range must be 11; got {w[key]}"
    assert hi[key] != 11 and lo[key] != 11, \
        "the width must not coincide with either printed limit"
    return (f"the third species runs {lo[key]:.0f} to {hi[key]:.0f} parts per thousand, a "
            f"width of {w[key]:.0f}")


def q15(table, item):
    w = _widths(table, FLO, FHI)
    narrowest = min(w, key=w.get)
    assert narrowest == "Insect 2", f"Insect 2 must endure the narrowest range; got {narrowest}"
    assert len(set(w.values())) == len(w), "'all four are the same width' must be false"
    return f"the four flow rate ranges are {w}, and the narrowest belongs to {narrowest}"


def q16(table, item):
    who = _endures(table, FLO, FHI, 100)
    assert who == ["Insect 4"], f"exactly Insect 4 must endure 100; got {who}"
    return (f"exactly one of the four insects has 100 centimetres per second between its "
            f"printed limits, and it is {who[0]}")


def q17(table, item):
    w = _widths(table, NLO, NHI)
    widest = max(w, key=w.get)
    assert widest == "Plant 3", f"Plant 3 must endure the widest range; got {widest}"
    assert len(set(w.values())) == len(w), "'all four are the same width' must be false"
    return f"the four sunlight ranges are {w}, and the widest belongs to {widest}"


def q18(table, item):
    who = _endures(table, NLO, NHI, 10)
    assert who == ["Plant 2", "Plant 3"], \
        f"exactly the second and third plants must endure 10 hours; got {who}"
    return (f"exactly two of the four plants have 10 hours between their printed limits, "
            f"and they are {who}")


def q19(table, item):
    lims = cg.col(table, INDLIM)
    assert len(set(lims)) > 1, f"the individuals' limits must not all be equal; got {lims}"
    assert len(lims) == 5, f"five individuals must be tabulated; got {len(lims)}"
    return (f"the five individual upper limits read {lims} degrees Celsius, which are not "
            "all the same value")


def q20(table, item):
    lims = cg.col(table, INDLIM)
    spread = max(lims) - min(lims)
    assert spread == 6, f"the spread must be 6 degrees; got {spread}"
    assert spread != max(lims), "the spread must not coincide with the largest limit"
    return (f"the highest individual limit is {max(lims):.0f} and the lowest {min(lims):.0f} "
            f"degrees Celsius, a spread of {spread:.0f}")


def q21(table, item):
    pct = cg.col(table, SURV)
    assert pct[0] == 0 and pct[-1] == 0, \
        f"survival must be nil at both ends of the series; got {pct}"
    assert max(pct) == 100, f"survival must reach 100 percent somewhere; got {pct}"
    top = [i for i, v in enumerate(pct) if v == 100]
    assert all(0 < i < len(pct) - 1 for i in top), \
        "complete survival must occur only away from the two ends"
    assert len(set(pct)) > 1, "'survival was the same at every temperature' must be false"
    return (f"survival reads {pct} percent across the series, nil at both ends and complete "
            "only in the middle")


def q22(table, item):
    temps = cg.col(table, TANK)
    pct = cg.col(table, SURV)
    full = [t for t, v in zip(temps, pct) if v == 100]
    assert full == [14, 20], f"complete survival must occur at 14 and 20 only; got {full}"
    assert len(full) != len(temps), "'at every temperature tested' must be false"
    return f"the rows recording 100 percent surviving are those held at {full} degrees Celsius"


CLAIMS = [
 ("before injury or death results",
  "ERT-2.F.1, near verbatim: ecological tolerance refers to the range of conditions that an organism can endure before injury or death results. It is a range with an end at each side, not a single best value."),
 ("flow rate and sunlight",
  "ERT-2.F.1 names temperature, salinity, flow rate, and sunlight as its examples of the conditions ecological tolerance ranges over. Every rejected set replaces at least one of the four."),
 ("Soil nitrogen content",
  "ERT-2.F.1 gives temperature, salinity, flow rate and sunlight as its examples, and soil nitrogen content is not among them."),
 ("Injury or death",
  "ERT-2.F.1 defines the range as what an organism can endure BEFORE INJURY OR DEATH RESULTS, so injury or death is the framework's own marker for the end of the range and it names no other."),
 ("Individuals and species alike",
  "ERT-2.F.2, near verbatim: ecological tolerance can apply to individuals and to species. Both levels are named and neither is excluded."),
 ("a property of a single individual as well",
  "ERT-2.F.2 states that ecological tolerance can apply to individuals and to species, so restricting it to the species level drops half of what the statement says."),
 ("a range, which needs a limit at each end",
  "ERT-2.F.1 defines ecological tolerance as a RANGE of conditions, and a range is fixed by two endpoints, so one reading names neither end. Temperature is in fact one of the four example conditions."),
 ("Fish 3",
  "Recomputed in q8 above: the four temperature ranges are 22, 6, 29 and 7 degrees, and the widest belongs to the species whose limits are 2 and 31. ERT-2.F.1 makes ecological tolerance the range between two limits."),
 ("Twenty-two degrees Celsius",
  "Recomputed in q9 above: 26 less 4 is 22, and 22 is neither of the two printed limits, so the rejected values are the limits themselves rather than the width."),
 ("Fish 3",
  "Recomputed in q10 above: exactly one of the four species has 30 degrees Celsius between its printed limits. ERT-2.F.1 makes injury the result of passing either end of the range."),
 ("Fish 2",
  "Recomputed in q11 above: the four ranges are 22, 6, 29 and 7 degrees, and the narrowest belongs to the species whose limits are 12 and 18. Both limits are printed for every species, so the comparison is available."),
 ("Estuary species 2",
  "Recomputed in q12 above: the four salinity ranges are 12, 31, 11 and 10 parts per thousand, and the widest belongs to the species whose limits are 3 and 34. ERT-2.F.1 names salinity among its example conditions."),
 ("Estuary species 2",
  "Recomputed in q13 above: exactly one species has both 5 and 32 parts per thousand between its printed limits. ERT-2.F.1 makes injury or death the result of passing either end."),
 ("Eleven parts per thousand",
  "Recomputed in q14 above: 36 less 25 is 11, and 11 is neither of the printed limits. ERT-2.F.1's definition makes the width of the range the quantity of interest."),
 ("Insect 2",
  "Recomputed in q15 above: the four flow rate ranges are 75, 15, 30 and 60 centimetres per second, and the narrowest belongs to the insect whose limits are 40 and 55. ERT-2.F.1 names flow rate among its examples."),
 ("Insect 4",
  "Recomputed in q16 above: exactly one insect has 100 centimetres per second between its printed limits. ERT-2.F.1 sets injury as the consequence of passing either end."),
 ("Plant 3",
  "Recomputed in q17 above: the four sunlight ranges are 3, 9, 12 and 6 hours, and the widest belongs to the plant whose limits are 1 and 13. ERT-2.F.1 names sunlight among its example conditions."),
 ("second and the third plant",
  "Recomputed in q18 above: exactly two of the four plants have 10 hours between their printed limits, and they are the ones reaching 11 and 13 hours. The plants reaching only 4 and only 9 hours do not."),
 ("can differ in the temperature they endure",
  "Recomputed in q19 above: the five individual limits are 24, 27, 25, 30 and 26 degrees Celsius, which are not all equal. ERT-2.F.2 states that ecological tolerance can apply to individuals as well as to species, which is what makes a per individual limit a measurement at all."),
 ("Six degrees Celsius",
  "Recomputed in q20 above: 30 less 24 is 6. ERT-2.F.2 allows tolerance to be a property of an individual, so a spread between individuals is a reportable quantity."),
 ("middle band of temperatures and reaches zero at both",
  "Recomputed in q21 above: survival reads 0, 55, 100, 100, 60 and 0 percent as the water warms, nil at both ends and complete only in the middle. ERT-2.F.1 makes tolerance a range bounded at each end by injury or death."),
 ("At 14 and at 20 degrees Celsius",
  "Recomputed in q22 above: exactly two rows record 100 percent surviving and they are the two middle temperatures. The coldest and warmest rows record none surviving, which ERT-2.F.1 identifies as the outcome beyond the range."),
 ("lowest and the highest salinity at which individuals survive",
  "ERT-2.F.1 defines ecological tolerance as the RANGE of conditions endured before injury or death, so a report of it must name both ends. A growth maximum, an average, a count of sites and a single day's reading each name something else."),
 ("rates at which injury first appears at the slow end",
  "ERT-2.F.1 makes ecological tolerance a range ending in injury or death, so a direct test has to locate both endpoints. None of the rejected studies locates either."),
 ("so two individuals may have different limits",
  "ERT-2.F.2 states that ecological tolerance can apply to individuals and to species, so a difference between two individuals is an ordinary result rather than an error or a sign of two species."),
 ("bounded at both ends",
  "The passage names a temperature below which the larvae die and one above which they are damaged, which is the shape ERT-2.F.1 gives ecological tolerance: a range whose ends are marked by injury or death. No growth maximum is stated and no upper limit is denied."),
 ("endures a range of the same width",
  "ERT-2.F.1 supplies the range, the example conditions and the endpoint of injury or death, and ERT-2.F.2 supplies the individual level. Neither statement compares the widths of different species' ranges, so equal width is an addition rather than a reading."),
 ("narrow ecological tolerance for flow rate",
  "ERT-2.F.1 names flow rate among the conditions ecological tolerance ranges over and bounds the range by injury or death. Narrow is an ordinary description of the size of that range; the condition tolerated here is current speed rather than salt, and the tolerance belongs to the organism."),
 ("the same range can be reported for one fish or for the species",
  "ERT-2.F.1 supplies the range and the injury or death that marks its ends, and ERT-2.F.2 supplies both levels of application. Each rejected account drops one end of the range, replaces injury with movement or growth rate, forbids the individual level, or adds an evolutionary claim."),
 ("such as temperature, salinity, flow rate and sunlight",
  "ERT-2.F.1 supplies the range, the four example conditions and the injury or death that ends it, and ERT-2.F.2 supplies the two levels it can apply to, so the keyed summary is exactly the two statements and no more."),
]

TABLE_CHECKS = {8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15,
                16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e2_4, CLAIMS, TABLE_CHECKS)
