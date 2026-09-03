"""Key audit for AP CHEMISTRY 5.3 Concentration Changes Over Time.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Nine table items and seven stem-data items
are recomputed here.

HOW "WHICH PLOT IS LINEAR" IS RECOMPUTED WITHOUT A PLOT
------------------------------------------------------
The framework states 5.3.A.1 to 5.3.A.3 in terms of graphs and this bank cannot
carry a figure, so each of those items is a table giving the concentration, its
natural log and its reciprocal at EVENLY SPACED times. Against evenly spaced
times a plot is a straight line exactly when the column's successive differences
are constant, so ``linear_columns`` below computes those differences and reports
which single column has them. It asserts the times are evenly spaced first --
without that the differences say nothing, and asserting it is what keeps the
substitute for a graph honest.

The tolerance is RELATIVE and deliberately tight (2 percent of the mean step).
The natural-log columns are printed to three decimals, so a genuinely linear
column varies in its last digit; a column that is not linear here is off by tens
of percent, so nothing sits near the line.

WHAT THE KEYS REST ON
---------------------
EK 5.3.A.1  The order can be inferred from concentration versus time data.
            (items 1, 24, 27, 29)
EK 5.3.A.2  First order gives a linear plot of the natural log.  (items 2, 5,
            20, 22)
EK 5.3.A.3  Second order gives a linear plot of the reciprocal.  (items 3, 8,
            21, 22, 24)
EK 5.3.A.4  The slopes give the rate constant; the three printed equations.
            (items 4, 6, 9, 10, 11, 19, 20, 21, 22, 25, 28)
EK 5.3.A.5  Half-life is a critical parameter for first order reactions because
            it is constant, and t(1/2) = 0.693/k.  (items 7, 12, 13, 14, 15, 16,
            18, 23, 26, 30)
EK 5.3.A.6  Radioactive decay illustrates first order kinetics.  (items 17, 18)

ON ITEM 30. The framework attaches CONSTANCY of the half-life to first order
reactions and gives that as the reason the parameter matters. The key says only
that -- that the successive halvings take equal times for the first order case
-- and does not assert any formula for a second order half-life, which the CED
does not give.

NEGATIVE CONTROL: ``python3 verify_h5_3.py --selftest``.
"""
import sys

import h_chem_notation as hn
import h5_3 as M

TIME = "Time (seconds)"
LN = "Natural log of the concentration"
RECIP = "Reciprocal of the concentration (liters per mole)"
CONC = {"_T_FIRST": "Concentration of A (moles per liter)",
        "_T_SECOND": "Concentration of B (moles per liter)",
        "_T_ZEROTH": "Concentration of D (moles per liter)"}
FRAC = "Fraction of the sample remaining"
NHALF = "Number of half-lives elapsed"

WORD = {0: "Zero order", 1: "First order", 2: "Second order"}
FRACWORD = {2: "One half", 4: "One quarter", 8: "One eighth", 16: "One sixteenth"}


def _steps(values):
    return [values[i + 1] - values[i] for i in range(len(values) - 1)]


def _is_linear(values, rel=0.02):
    d = _steps(values)
    scale = sum(abs(x) for x in d) / len(d)
    return scale > 0 and (max(d) - min(d)) <= rel * scale


def linear_columns(table, conc_header):
    """Which of the three columns is a straight line against evenly spaced time.

    Returns the single header whose successive differences are constant. Fails
    if the times are not evenly spaced, or if none or more than one column
    qualifies -- either of which would make the item's key unsupportable.
    """
    t = hn.cg.col(table, TIME)
    dt = _steps(t)
    assert max(dt) == min(dt), f"the times are not evenly spaced: {t}"
    hits = [h for h in (conc_header, LN, RECIP) if _is_linear(hn.cg.col(table, h))]
    assert len(hits) == 1, f"{len(hits)} columns are linear ({hits}); exactly one must be"
    return hits[0]


def _order_of(table, conc_header):
    which = linear_columns(table, conc_header)
    return {conc_header: 0, LN: 1, RECIP: 2}[which]


# ------------------------------------------------------------ table questions

def q5(t, item):
    n = _order_of(t, CONC["_T_FIRST"])
    hn.keyed(item, WORD[n])
    return (f"of the three columns only the natural log has constant successive "
            f"differences, which is order {n}")


def q6(t, item):
    assert _order_of(t, CONC["_T_FIRST"]) == 1, "this table must be the first order one"
    ln = hn.cg.col(t, LN)
    dt = _steps(hn.cg.col(t, TIME))[0]
    k = -sum(_steps(ln)) / len(_steps(ln)) / dt
    assert abs(k - 0.0693) < 5e-5, f"the rate constant recomputes to {k}"
    hn.keyed(item, "0.0693 per second")
    return (f"the natural log falls {abs(sum(_steps(ln)) / len(_steps(ln))):.3f} every "
            f"{dt:.0f} seconds, so the rate constant is {k:.4f} per second")


def q7(t, item):
    c = hn.cg.col(t, CONC["_T_FIRST"])
    dt = _steps(hn.cg.col(t, TIME))[0]
    ratios = [c[i + 1] / c[i] for i in range(len(c) - 1)]
    assert all(abs(r - 0.5) < 0.01 for r in ratios), \
        f"the concentration does not halve over each interval: {ratios}"
    hn.keyed(item, f"{dt:.0f} seconds")
    return (f"each successive tabulated concentration is half the one before it, and the "
            f"tabulated times are {dt:.0f} seconds apart")


def q8(t, item):
    n = _order_of(t, CONC["_T_SECOND"])
    hn.keyed(item, WORD[n])
    return (f"of the three columns only the reciprocal has constant successive "
            f"differences, which is order {n}")


def q9(t, item):
    assert _order_of(t, CONC["_T_SECOND"]) == 2, "this table must be the second order one"
    r = hn.cg.col(t, RECIP)
    dt = _steps(hn.cg.col(t, TIME))[0]
    k = sum(_steps(r)) / len(_steps(r)) / dt
    assert abs(k - 0.0200) < 1e-6, f"the rate constant recomputes to {k}"
    hn.keyed(item, "0.0200 liters per mole per second")
    return (f"the reciprocal rises {sum(_steps(r)) / len(_steps(r)):.2f} every {dt:.0f} "
            f"seconds, so the rate constant is {k:.4f}")


def q10(t, item):
    n = _order_of(t, CONC["_T_ZEROTH"])
    hn.keyed(item, WORD[n])
    return (f"of the three columns only the concentration itself has constant successive "
            f"differences, which is order {n}")


def q11(t, item):
    assert _order_of(t, CONC["_T_ZEROTH"]) == 0, "this table must be the zeroth order one"
    c = hn.cg.col(t, CONC["_T_ZEROTH"])
    dt = _steps(hn.cg.col(t, TIME))[0]
    k = -sum(_steps(c)) / len(_steps(c)) / dt
    assert abs(k - 0.00500) < 1e-9, f"the rate constant recomputes to {k}"
    hn.keyed(item, "0.00500 moles per liter per second")
    return (f"the concentration falls {abs(sum(_steps(c)) / len(_steps(c))):.3f} every "
            f"{dt:.0f} seconds, so the rate constant is {k:.5f}")


def q22(t, item):
    plot = {r[0]: r[1].strip().lower() for r in t["rows"]}
    order = {}
    for lab, text in plot.items():
        if "natural log" in text:
            order[lab] = 1
        elif "reciprocal" in text:
            order[lab] = 2
        else:
            order[lab] = 0
    assert order == {"R1": 1, "R2": 2, "R3": 0}, f"the tabulated orders come out {order}"
    hn.keyed(item, "R1 is first order, R2 is second order, and R3 is zero order")
    return ("mapping each tabulated linear plot onto the framework's three cases gives "
            "first, second and zero order in that row order")


def q26(t, item):
    n = dict(zip(hn.cg.labels(t), [r[1].strip().lower() for r in t["rows"]]))
    match = [k for k, v in n.items() if v == "one sixteenth"]
    assert match == ["4"], f"rows reporting one sixteenth remaining: {match}"
    for lab, frac in n.items():
        expected = FRACWORD[2 ** int(lab)].lower()
        assert frac == expected, f"after {lab} half-lives the table says {frac}, not {expected}"
    hn.keyed(item, "Four half-lives")
    return ("every tabulated fraction is one half raised to the number of half-lives in "
            "its own row, and one sixteenth sits against four")


TABLE_CHECKS = {5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11,
                22: q22, 26: q26}


# --------------------------------------------------------- stem-data questions

def a12(item):
    t = 0.693 / 0.0231
    assert abs(t - 30.0) < 0.05, f"the half-life recomputes to {t}"
    hn.keyed(item, "30. seconds")
    return f"0.693 divided by the given rate constant is {t:.1f} seconds"


def a13(item):
    k = 0.693 / 20.0
    # 0.03465 exactly; the choice prints it to three significant figures, so the
    # tolerance has to admit that rounding and nothing wider.
    assert abs(k - 0.0347) < 1e-4, f"the rate constant recomputes to {k}"
    hn.keyed(item, "0.0347 per second")
    return f"0.693 divided by the given half-life is {k:.4f} per second"


def a15(item):
    frac = 2 ** 3
    hn.keyed(item, FRACWORD[frac])
    return f"three successive halvings leave one part in {frac}"


def a16(item):
    n = 4                       # halvings needed to reach one sixteenth
    assert 2 ** n == 16, "four halvings must be what reaches one sixteenth"
    total = n * 25
    hn.keyed(item, f"{total:.0f} seconds")
    return f"{n} halvings at 25 seconds each is {total:.0f} seconds"


def a18(item):
    n = 24 // 8
    left = 40.0 / 2 ** n
    hn.keyed(item, f"{left:.1f} grams")
    return f"24 days is {n} half-lives of 8 days, leaving {left:.1f} of the 40. grams"


def a25(item):
    c = 0.600 - 0.0100 * 40.0
    hn.keyed(item, f"{c:.3f} moles per liter")
    return f"0.600 less 0.0100 times 40. seconds is {c:.3f} moles per liter"


def a28(item):
    k = (2.58 - 1.20) / 60.0
    assert abs(k - 0.0230) < 1e-6, f"the rate constant recomputes to {k}"
    hn.keyed(item, "0.0230 per second")
    return f"a fall of 1.38 in the natural log over 60. seconds is {k:.4f} per second"


ARITH = {12: a12, 13: a13, 15: a15, 16: a16, 18: a18, 25: a25, 28: a28}

CLAIMS = [
 ("order of the reaction with respect to that reactant",
  "EK 5.3.A.1: the order of a reaction can be inferred from a graph of concentration of reactant versus time. Energy, product identity and temperature are not read off such data."),
 ("natural log of the reactant concentration",
  "EK 5.3.A.2, near verbatim: for a first order reaction a plot of the natural log of the reactant concentration as a function of time will be linear."),
 ("reciprocal of the reactant concentration",
  "EK 5.3.A.3, near verbatim: for a second order reaction a plot of the reciprocal of the concentration of that reactant versus time will be linear."),
 ("the concentration itself falling linearly with time",
  "EK 5.3.A.4 prints the zeroth order relationship as the difference of the concentrations equalling the negative of the rate constant times the time, which is a straight line in the concentration itself."),
 ("First order",
  "Recomputed in q5 above: of the three tabulated columns only the natural log has constant successive differences against evenly spaced times, which EK 5.3.A.2 assigns to first order."),
 ("0.0693 per second",
  "Recomputed in q6 above. EK 5.3.A.4 makes the slope of the natural log against time the negative of the rate constant."),
 ("10 seconds",
  "Recomputed in q7 above: every tabulated concentration is half the one before it, at a fixed spacing in time, which is the constancy EK 5.3.A.5 attributes to a first order half-life."),
 ("Second order",
  "Recomputed in q8 above: only the reciprocal column has constant successive differences, which EK 5.3.A.3 assigns to second order."),
 ("0.0200 liters per mole per second",
  "Recomputed in q9 above. EK 5.3.A.4 makes the slope of the reciprocal against time the rate constant itself, with no negative sign."),
 ("Zero order",
  "Recomputed in q10 above: only the concentration column itself has constant successive differences, which is the zeroth order equation of EK 5.3.A.4."),
 ("0.00500 moles per liter per second",
  "Recomputed in q11 above. EK 5.3.A.4's zeroth order relationship makes the concentration fall by the rate constant times the elapsed time."),
 ("30. seconds",
  "Recomputed in a12. EK 5.3.A.5 relates the half-life of a first order reaction to its rate constant as 0.693 divided by that constant."),
 ("0.0347 per second",
  "Recomputed in a13. EK 5.3.A.5's relation rearranges to make the rate constant the ratio of 0.693 to the half-life."),
 ("half-life is constant and fixed by the rate constant alone",
  "EK 5.3.A.5, near verbatim: half-life is a critical parameter for first order reactions BECAUSE the half-life is constant and related to the rate constant by the equation given."),
 ("One eighth",
  "Recomputed in a15. EK 5.3.A.5 makes the half-life of a first order reaction constant, so each successive half-life leaves half of what was present at its start."),
 ("100 seconds",
  "Recomputed in a16. A constant half-life means the time to reach a fraction is the number of successive halvings that produce it, each taking the same interval."),
 ("Radioactive decay",
  "EK 5.3.A.6, near verbatim: radioactive decay processes provide an important illustration of first order kinetics."),
 ("5.0 grams",
  "Recomputed in a18. EK 5.3.A.6 makes radioactive decay a first order process and EK 5.3.A.5 makes its half-life constant, so each interval of one half-life halves what remains."),
 ("the reciprocal rising linearly with time",
  "EK 5.3.A.4 prints the second order relationship as the difference of the reciprocals equalling the rate constant times the time."),
 ("rate constant for the reaction",
  "EK 5.3.A.4 gives the first order relationship as the difference of the natural logs equalling the negative of the rate constant times the time, so the magnitude of that slope is the constant."),
 ("The rate constant for the reaction",
  "EK 5.3.A.4 gives the second order relationship with no negative sign, so the slope of the reciprocal against time is the rate constant itself."),
 ("R1 is first order, R2 is second order, and R3 is zero order",
  "Recomputed in q22 above. EK 5.3.A.2 assigns the linear natural log plot to first order, EK 5.3.A.3 assigns the linear reciprocal plot to second order, and EK 5.3.A.4's zeroth order equation makes the concentration itself linear."),
 ("They are equal",
  "EK 5.3.A.5 states that for a first order reaction the half-life is constant and related to the rate constant by 0.693 divided by it. The starting concentration does not appear in that relationship."),
 ("second order with respect to that reactant",
  "EK 5.3.A.3 states that a linear plot of the reciprocal of the concentration versus time is what a second order dependence produces, which is exactly the observation described."),
 ("0.200 moles per liter",
  "Recomputed in a25 from EK 5.3.A.4's zeroth order equation: the concentration falls from its starting value by the rate constant multiplied by the elapsed time."),
 ("Four half-lives",
  "Recomputed in q26 above: every tabulated fraction is one half raised to that row's number of half-lives, which is the constancy EK 5.3.A.5 attributes to a first order process."),
 ("concentration of the monitored reactant at known times",
  "EK 5.3.A.1 has the order inferred from concentration versus time data, and each equation in EK 5.3.A.4 relates a concentration at time t to the concentration at time zero."),
 ("0.0230 per second",
  "Recomputed in a28 from EK 5.3.A.4's first order equation: the rate constant is the fall in the natural log divided by the elapsed time."),
 ("differs between zeroth, first and second order reactions",
  "EK 5.3.A.1 has the order inferred from a graph of concentration versus time, and EK 5.3.A.2 to 5.3.A.4 supply three different functions of concentration, exactly one of which is linear for each order."),
 ("Only the first order reaction takes the same time for each successive halving",
  "EK 5.3.A.5 attaches the CONSTANCY of the half-life to first order reactions and gives it as the reason the parameter matters there. Nothing here asserts any formula for a second order half-life, which the framework does not print."),
]


def _wreck_ln_column(mod, cl):
    """Module-specific control: break the constancy the first-order key rests on."""
    t = mod.QUESTIONS[4]["table"]
    mod.QUESTIONS[4]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], r[1], "-1.100", r[3]] if r[0] == "20" else list(r)
              for r in t["rows"]])


def _wreck_spacing(mod, cl):
    """Module-specific control: make the times unevenly spaced.

    The differences of a column only stand in for a slope when the times are
    evenly spaced, so the check asserts that first; this control is what proves
    that assertion is not decoration.
    """
    t = mod.QUESTIONS[7]["table"]
    mod.QUESTIONS[7]["table"] = dict(
        headers=t["headers"],
        rows=[["70", r[1], r[2], r[3]] if r[0] == "50" else list(r)
              for r in t["rows"]])


def _wreck_decay_table(mod, cl):
    """Module-specific control: mislabel a fraction in the half-life table."""
    t = mod.QUESTIONS[25]["table"]
    mod.QUESTIONS[25]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "one twelfth"] if r[0] == "3" else list(r) for r in t["rows"]])


def _wreck_stem_key(mod, cl):
    """Module-specific control: key a half-life item to the wrong value."""
    mod.QUESTIONS[11]["choices"][0] = "45. seconds"


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH,
                extra=[("a natural-log cell corrupted", _wreck_ln_column),
                       ("the times made unevenly spaced", _wreck_spacing),
                       ("a half-life fraction mislabelled", _wreck_decay_table),
                       ("a key moved off its recomputed half-life", _wreck_stem_key)])

hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
