"""Key audit for AP CHEMISTRY 5.2 Introduction to Rate Law.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Every order, every rate-constant value and
every unit assignment is recomputed here from the item's own data.

HOW THE ORDERS ARE RECOMPUTED
-----------------------------
``order_from`` finds the pair of experiments in which exactly ONE concentration
differs, then takes the ratio of rates against the ratio of that concentration
and solves for the power by logarithms. That is EK 5.2.A.5's own method --
comparing initial rates -- carried out arithmetically rather than asserted, so a
mis-typed table cell or a moved key fails here. It also refuses to run if more
than one concentration differs between the chosen pair, which is the mistake the
method invites and which item 23 is written about.

WHAT THE KEYS REST ON
---------------------
EK 5.2.A.1  Experimental methods can be used to monitor the amounts of reactants
            and/or products over time and to determine the rate.  (items 24, 25)
EK 5.2.A.2  The rate law expresses the rate as proportional to the concentration
            of each reactant raised to a power.  (items 1, 10, 11, 15, 16, 17,
            18, 26, 29, 30)
EK 5.2.A.3  The power of each reactant is the order with respect to it; the sum
            of the powers is the overall order.  (items 2, 3, 9, 18, 22, 27)
EK 5.2.A.4  The proportionality constant is the rate constant; its value is
            temperature dependent and its units reflect the overall reaction
            order.  (items 4, 5, 12, 19, 20, 27, 28, 30)
EK 5.2.A.5  Comparing initial rates is a method to determine the order with
            respect to each reactant.  (items 6, 7, 8, 13, 14, 21, 23, 25)

NOT HERE, ON PURPOSE: integrated rate laws and half-life (5.3), molecularity
(5.4), and rate laws derived from a mechanism (5.8, 5.9). Item 25 keys on the
rate law having to come from data rather than from the coefficients, which is
what EK 5.2.A.1 and 5.2.A.5 together say and what makes 5.4 a separate topic.

NEGATIVE CONTROL: ``python3 verify_h5_2.py --selftest``.
"""
import math
import sys

import h_chem_notation as hn
import h5_2 as M

A = "Initial concentration of A (moles per liter)"
B = "Initial concentration of B (moles per liter)"
RAB = "Initial rate (moles per liter per second)"
X = "Initial concentration of X (moles per liter)"
Y = "Initial concentration of Y (moles per liter)"
A3 = "Initial [A] (moles per liter)"
B3 = "Initial [B] (moles per liter)"
C3 = "Initial [C] (moles per liter)"
KCOL = "Rate constant measured for the same reaction"
TCOL = "Temperature (kelvins)"
UNITS = "Units of the rate constant"

WORD = {0: "Zero order", 1: "First order", 2: "Second order", 3: "Third order",
        4: "Fourth order"}


def order_from(table, target, others, rate_header):
    """The order with respect to ``target``, by EK 5.2.A.5's own method.

    Finds the unique pair of rows differing ONLY in the target concentration and
    solves rate2/rate1 = (c2/c1)**n for n. Raises if no such pair exists or if
    more than one is found, so a table that cannot isolate the reactant fails
    rather than returning a number that means nothing.
    """
    tcol = hn.cg.col(table, target)
    ocols = [hn.cg.col(table, h) for h in others]
    rate = hn.cg.col(table, rate_header)
    pairs = []
    for i in range(len(tcol)):
        for j in range(i + 1, len(tcol)):
            if tcol[i] != tcol[j] and all(c[i] == c[j] for c in ocols):
                pairs.append((i, j))
    assert len(pairs) == 1, (
        f"{target}: {len(pairs)} pairs isolate it; the comparison of initial rates "
        "needs exactly one"
    )
    i, j = pairs[0]
    n = math.log(rate[j] / rate[i]) / math.log(tcol[j] / tcol[i])
    rounded = round(n)
    assert abs(n - rounded) < 1e-9, f"{target}: the order recomputes to {n}, not a whole number"
    return rounded


# ------------------------------------------------------------ table questions

def q7(t, item):
    n = order_from(t, A, [B], RAB)
    hn.keyed(item, WORD[n])
    return f"holding B fixed, the rate ratio against the A ratio gives an order of {n} in A"


def q8(t, item):
    n = order_from(t, B, [A], RAB)
    hn.keyed(item, WORD[n])
    return f"holding A fixed, the rate ratio against the B ratio gives an order of {n} in B"


def q9(t, item):
    total = order_from(t, A, [B], RAB) + order_from(t, B, [A], RAB)
    hn.keyed(item, WORD[total])
    return f"the two separately recomputed powers sum to an overall order of {total}"


def q10(t, item):
    na, nb = order_from(t, A, [B], RAB), order_from(t, B, [A], RAB)
    assert (na, nb) == (1, 2), f"the recomputed powers are {na} and {nb}"
    hn.keyed(item, r"k[\mathrm{A}][\mathrm{B}]^{2}")
    return f"the recomputed powers, {na} on A and {nb} on B, are the exponents in the keyed law"


def q11(t, item):
    na, nb = order_from(t, A, [B], RAB), order_from(t, B, [A], RAB)
    a, b, r = hn.cg.col(t, A), hn.cg.col(t, B), hn.cg.col(t, RAB)
    ks = [r[i] / (a[i] ** na * b[i] ** nb) for i in range(len(r))]
    assert max(ks) - min(ks) < 1e-9, f"the constant is not the same in every row: {ks}"
    hn.keyed(item, f"{ks[0]:.1f}")
    return (f"dividing each measured rate by its own concentration factors gives {ks[0]:.1f} "
            f"in all {len(ks)} experiments")


def q13(t, item):
    n = order_from(t, Y, [X], RAB)
    hn.keyed(item, WORD[n])
    return f"holding X fixed, doubling Y leaves the rate unchanged, an order of {n} in Y"


def q14(t, item):
    n = order_from(t, X, [Y], RAB)
    hn.keyed(item, WORD[n])
    return f"holding Y fixed, the rate ratio against the X ratio gives an order of {n} in X"


def q15(t, item):
    nx, ny = order_from(t, X, [Y], RAB), order_from(t, Y, [X], RAB)
    assert (nx, ny) == (2, 0), f"the recomputed powers are {nx} and {ny}"
    hn.keyed(item, r"k[\mathrm{X}]^{2} \), second order overall")
    return (f"a power of {ny} on Y removes it from the expression, leaving the power of "
            f"{nx} on X as the whole rate law")


def q16(t, item):
    nx, ny = order_from(t, X, [Y], RAB), order_from(t, Y, [X], RAB)
    x, y, r = hn.cg.col(t, X), hn.cg.col(t, Y), hn.cg.col(t, RAB)
    ks = [r[i] / (x[i] ** nx * y[i] ** ny) for i in range(len(r))]
    assert max(ks) - min(ks) < 1e-9, f"the constant is not the same in every row: {ks}"
    hn.keyed(item, f"{ks[0]:.2f}")
    return (f"dividing each measured rate by the concentration factors gives {ks[0]:.2f} in "
            "every experiment")


def q20(t, item):
    temp = hn.cg.col(t, TCOL)
    k = hn.cg.col(t, KCOL)
    assert temp == sorted(temp), "the temperature column should be in increasing order"
    assert k == sorted(k), f"the rate constant does not rise with temperature: {k}"
    assert max(k) > 3 * min(k), "the change should be far too large to call scatter"
    hn.keyed(item, "rises as the temperature rises")
    return (f"over {temp[0]:.0f} to {temp[-1]:.0f} kelvins the constant moves from {k[0]} to "
            f"{k[-1]}, a factor of {k[-1] / k[0]:.1f}")


def q21(t, item):
    n = order_from(t, C3, [A3, B3], RAB)
    hn.keyed(item, WORD[n])
    return f"holding A and B fixed, doubling C multiplies the rate fourfold, an order of {n}"


def q22(t, item):
    total = (order_from(t, A3, [B3, C3], RAB) + order_from(t, B3, [A3, C3], RAB)
             + order_from(t, C3, [A3, B3], RAB))
    hn.keyed(item, WORD[total])
    return f"the three separately recomputed powers sum to an overall order of {total}"


def q23(t, item):
    labs = hn.cg.labels(t)
    b = dict(zip(labs, hn.cg.col(t, B3)))
    a = dict(zip(labs, hn.cg.col(t, A3)))
    c = dict(zip(labs, hn.cg.col(t, C3)))
    pairs = [(p, q) for i, p in enumerate(labs) for q in labs[i + 1:]
             if b[p] != b[q] and a[p] == a[q] and c[p] == c[q]]
    assert pairs == [("1", "3")], f"pairs isolating B: {pairs}"
    hn.keyed(item, "first and third experiments")
    return ("exactly one pair of experiments differs in B alone, which is the only "
            "comparison that isolates its order")


def q27(t, item):
    order = {r[0].strip().lower(): r[1] for r in t["rows"]}
    assert "zero" in order, f"the table has no zero-order row: {list(order)}"
    assert order["zero"] == "moles per liter per second", \
        f"the zero-order units are tabulated as {order['zero']!r}"
    assert len(set(order.values())) == len(order), \
        "'a rate constant always carries the same units' must be false"
    hn.keyed(item, "Zero order, with the rate constant carrying moles per liter per second")
    return ("the table pairs a zero overall order with units identical to those of a rate, "
            "and gives a different set of units to each of the other orders")


TABLE_CHECKS = {7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 13: q13, 14: q14,
                15: q15, 16: q16, 20: q20, 21: q21, 22: q22, 23: q23, 27: q27}


# --------------------------------------------------------- stem-data questions

def a2(item):
    hn.keyed(item, WORD[2])
    return "the exponent written on the A concentration in the printed rate law is two"


def a3(item):
    hn.keyed(item, WORD[2 + 1])
    return "the printed exponents two and one sum to an overall order of three"


def a17(item):
    factor = 2 ** 2
    hn.keyed(item, f"{'four' if factor == 4 else factor} times as large")
    return f"doubling a concentration that enters squared multiplies the rate by {factor}"


def a26(item):
    factor = 3 ** 2
    hn.keyed(item, str(factor))
    return f"tripling a concentration that enters squared multiplies the rate by {factor}"


def a29(item):
    factor = 2 * 2
    hn.keyed(item, f"{'four' if factor == 4 else factor} times as large")
    return f"two independent doublings, each contributing a factor of two, give {factor}"


ARITH = {2: a2, 3: a3, 17: a17, 26: a26, 29: a29}

CLAIMS = [
 ("proportional to the concentration of each reactant raised to a power",
  "EK 5.2.A.2, near verbatim: the rate law expresses the rate of a reaction as proportional to the concentration of each reactant raised to a power."),
 ("Second order",
  "Recomputed in a2. EK 5.2.A.3 states that the power of each reactant in the rate law is the order of the reaction with respect to that reactant."),
 ("Third order",
  "Recomputed in a3. EK 5.2.A.3 states that the sum of the powers of the reactant concentrations in the rate law is the overall order of the reaction."),
 ("rate constant, whose value is temperature dependent",
  "EK 5.2.A.4, near verbatim: the proportionality constant in the rate law is called the rate constant, and the value of this constant is temperature dependent."),
 ("units reflect the overall reaction order",
  "EK 5.2.A.4 states that the units of the rate constant reflect the overall reaction order. The rate itself always carries concentration per time, so the constant must carry whatever the concentration factors leave over."),
 ("initial rates of runs that differ in one reactant concentration at a time",
  "EK 5.2.A.5, near verbatim: comparing initial rates of a reaction is a method to determine the order with respect to each reactant."),
 ("First order",
  "Recomputed in q7 above by EK 5.2.A.5's method: the one pair of experiments holding B fixed gives the power on A directly."),
 ("Second order",
  "Recomputed in q8 above by the same method, using the pair that holds A fixed while B changes."),
 ("Third order",
  "Recomputed in q9 above. EK 5.2.A.3 makes the overall order the sum of the powers, each obtained from its own paired comparison."),
 (r"k[\mathrm{A}][\mathrm{B}]^{2}",
  "Recomputed in q10 above. EK 5.2.A.2 makes the rate proportional to each concentration raised to a power, and the two powers come from the table's paired comparisons."),
 ("2.0",
  "Recomputed in q11 above: dividing each measured rate by its own concentration factors gives the same constant in every experiment, which is what EK 5.2.A.2's proportionality asserts."),
 ("Liters squared per mole squared per second",
  "EK 5.2.A.4 states that the units of the rate constant reflect the overall reaction order. A rate carries concentration per time and three concentration factors appear, so the constant must cancel three of them."),
 ("Zero order",
  "Recomputed in q13 above. EK 5.2.A.5's comparison holds X fixed while Y doubles, and the measured rate does not move, which is a power of zero."),
 ("Second order",
  "Recomputed in q14 above. Holding Y fixed while X doubles multiplies the rate fourfold, and four is two raised to the recomputed power."),
 (r"k[\mathrm{X}]^{2} \), second order overall",
  "Recomputed in q15 above. A power of zero removes a reactant from the expression, because any concentration raised to zero is one, so the rate law names only the other reactant."),
 ("0.40",
  "Recomputed in q16 above: dividing each measured rate by its concentration factors gives the same value in every experiment."),
 ("four times as large",
  "Recomputed in a17. EK 5.2.A.2 makes the rate proportional to the concentration raised to its power, and EK 5.2.A.3 makes that power the order."),
 ("leaves the rate unchanged",
  "EK 5.2.A.3 makes the power the order with respect to that reactant and EK 5.2.A.2 makes the rate proportional to the concentration raised to it. A concentration raised to the power zero is one, so the factor drops out; the reactant is still consumed."),
 ("Reciprocal seconds",
  "EK 5.2.A.4 states that the units reflect the overall reaction order. A rate carries concentration per time and one concentration factor appears in the rate law, so the two concentrations cancel."),
 ("rises as the temperature rises",
  "Recomputed in q20 above. EK 5.2.A.4 states that the value of the rate constant is temperature dependent, and the table holds the reaction fixed while varying only temperature."),
 ("Second order",
  "Recomputed in q21 above by EK 5.2.A.5's method: the one pair holding A and B fixed shows the rate rising fourfold as C doubles."),
 ("Third order",
  "Recomputed in q22 above. EK 5.2.A.3 makes the overall order the sum of the three separately recomputed powers."),
 ("first and third experiments",
  "Recomputed in q23 above. EK 5.2.A.5 determines each order by comparing initial rates, which is informative only when a single concentration differs between the two runs."),
 ("Monitor the amounts of reactants or products over time",
  "EK 5.2.A.1 states that experimental methods can be used to monitor the amounts of reactants and/or products of a reaction over time and to determine the rate, which every later step depends on."),
 ("powers must be found from experimental data",
  "EK 5.2.A.1 has the rate determined experimentally and EK 5.2.A.5 makes comparing initial rates the method for finding each order. Neither licenses reading the powers off the coefficients of an overall equation."),
 ("9",
  "Recomputed in a26. EK 5.2.A.2 makes the rate proportional to each concentration raised to its power, so multiplying a concentration multiplies the rate by that factor raised to the power."),
 ("Zero order, with the rate constant carrying moles per liter per second",
  "Recomputed in q27 above. EK 5.2.A.3 makes a rate insensitive to every concentration an overall order of zero, and EK 5.2.A.4 then gives its constant the units of a rate."),
 ("same value in both",
  "EK 5.2.A.4 states that the value of the rate constant is temperature dependent. Concentration enters through the separate concentration factors of EK 5.2.A.2, not through the constant."),
 ("four times as large",
  "Recomputed in a29. EK 5.2.A.2 makes the rate proportional to the product of the concentration factors, so doubling two of them multiplies the product by their product."),
 ("constant of proportionality is needed",
  "EK 5.2.A.2 makes the rate proportional to concentrations raised to powers, and EK 5.2.A.4 names that constant of proportionality the rate constant and gives it units set by the overall order."),
]


def _wreck_rate_cell(mod, cl):
    """Module-specific control: change an initial rate so the order shifts."""
    t = mod.QUESTIONS[6]["table"]
    mod.QUESTIONS[6]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], r[1], r[2], "0.0080"] if r[0] == "2" else list(r) for r in t["rows"]])


def _wreck_isolation(mod, cl):
    """Module-specific control: vary two concentrations at once in the B pair."""
    t = mod.QUESTIONS[22]["table"]
    mod.QUESTIONS[22]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "0.20", r[2], r[3], r[4]] if r[0] == "3" else list(r)
              for r in t["rows"]])


def _wreck_k_temperature(mod, cl):
    """Module-specific control: flatten the temperature dependence."""
    t = mod.QUESTIONS[19]["table"]
    mod.QUESTIONS[19]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "0.0012"] for r in t["rows"]])


def _wreck_stem_key(mod, cl):
    """Module-specific control: key a printed rate law to the wrong exponent."""
    mod.QUESTIONS[1]["choices"][0] = "Sixth order"


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH,
                extra=[("an initial-rate cell corrupted", _wreck_rate_cell),
                       ("a table no longer isolating one reactant", _wreck_isolation),
                       ("the temperature dependence flattened", _wreck_k_temperature),
                       ("a key moved off its printed exponent", _wreck_stem_key)])

hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
