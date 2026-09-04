"""Key audit for AP CHEMISTRY 5.9 Pre-Equilibrium Approximation.

One ``(anchor, claim)`` per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EK 5.9.A.1  If the first elementary reaction is not rate limiting,
            approximations (such as pre-equilibrium) must be made to determine
            a rate law expression.                             (every item)
EK 5.8.A.1  is the complementary case -- the direct reading this topic cannot
            use.                                    (items 2, 3, 17, 19, 28)
EK 5.4.A.1  supplies the slow step's own rate expression from the particles
            colliding in it.               (items 4, 7, 9, 11, 13, 18, 20, 29)
EK 5.2.A.2/.3  supply the proportionality to concentration and the overall
            order as the sum of the powers.  (items 5, 8, 12, 21, 25, 26)
EK 5.7.A.3  supplies why an intermediate's concentration cannot stand in the
            answer: it is present only while the reaction runs.  (items 6, 15)

THE SUBSTITUTION IS EXACT ARITHMETIC ON EXPONENTS, AND ``derive`` REDOES IT.
Starting from the slow step's own particle counts, each intermediate's exponent
is removed and replaced, through the equilibrium of the fast first step, by the
exponents of the species standing opposite it in that step:

    remove   e powers of the intermediate X, formed c at a time in step 1
    add      e * n / c powers of every species on step 1's LEFT
    subtract e * n / c powers of every OTHER species on step 1's RIGHT

Fractions are exact (``fractions.Fraction``), which is what makes the half-order
and the inverse-order cases come out right rather than nearly right. The derived
law is then written in the module's own notation and must appear verbatim in the
keyed choice, order clause included.

FOUR STRUCTURAL GUARDS RUN OVER EVERY TABULATED MECHANISM, because this topic is
defined by a shape:

  * every elementary step balances in atoms and charge (EK 4.2.A.2);
  * exactly one step is labelled slow, and it is NOT the first -- a slow first
    step is EK 5.8.A.1's case, not this one;
  * the first step is labelled as reaching equilibrium, which is what licenses
    the substitution;
  * the slow step's reactants include an intermediate, which is the reason an
    approximation is needed at all.

NEGATIVE CONTROL: ``python3 verify_h5_9.py --selftest``.
"""
import re
import sys
from fractions import Fraction

import cg_check as cg
import h_check as h
import h_equation as heq

import h5_9

STEPCOL = "Elementary reaction"
RATECOL = "Relative rate"

ORDER_TEXT = {Fraction(1): "one", Fraction(2): "two", Fraction(3): "three",
              Fraction(4): "four", Fraction(3, 2): "three halves",
              Fraction(1, 2): "one half"}
TIMESWORD = {2: "twice", 3: "three times", 4: "four times", 8: "eight times",
             9: "nine times"}

_FIGURE = re.compile(
    r"(?<![a-z])(as shown|shown below|shown above|figure|image|picture|depicted|"
    r"pictured|illustrated|(?:diagram|graph|profile|curve|plot|chart)s?\s+"
    r"(?:above|below))(?![a-z])", re.I)


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, but every mechanism "
                f"here is a table -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every mechanism is carried as a table of steps "
          "with their relative rates.")


# ------------------------------------------------------------ the substitution

def latex_formula(name):
    m = re.search(r"(\d?)([+-])$", name)
    charge = ""
    if m:
        size = m.group(1)
        charge = f"^{{{size}{m.group(2)}}}" if size else f"^{m.group(2)}"
        name = name[:m.start()]
    return re.sub(r"(\d)", r"_\1", name) + charge


def mechanism(table):
    """The tabulated steps and the slow index, with this topic's shape asserted."""
    si, ri = table["headers"].index(STEPCOL), table["headers"].index(RATECOL)
    steps = [r[si] for r in table["rows"]]
    rates = [str(r[ri]).strip().lower() for r in table["rows"]]
    for s in steps:
        assert heq.balanced(s), f"a tabulated step does not balance: {s} -- {heq.report(s)}"
    slow = [i for i, r in enumerate(rates) if r == "slow"]
    assert len(slow) == 1, f"the tabulated relative rates are {rates}; exactly one must be slow"
    assert slow[0] != 0, (
        "the slow step must NOT be the first; a rate-limiting first step is EK 5.8.A.1's "
        "case, which is read off directly and needs no approximation"
    )
    assert "equilibrium" in rates[0], (
        f"the first step must be labelled as reaching equilibrium, not {rates[0]!r}; that "
        "label is what licenses the substitution"
    )
    inter = set(heq.intermediates(steps))
    slow_left, _ = heq.step_species(steps[slow[0]])
    assert inter & set(slow_left), (
        f"the slow step's reactants {sorted(slow_left)} include none of the intermediates "
        f"{sorted(inter)}, so no approximation would be needed"
    )
    return steps, slow[0], inter


def derive(steps, slow, inter):
    """The exponents of the derived rate law, exactly, as Fractions."""
    left1, right1 = heq.step_species(steps[0])
    slow_left, _ = heq.step_species(steps[slow])
    exps = {name: Fraction(n) for name, n in slow_left.items()}
    for x in [n for n in list(exps) if n in inter]:
        assert x in right1, (
            f"the intermediate {x} is not produced by the first step, so the "
            "pre-equilibrium of that step cannot replace it"
        )
        e = exps.pop(x)
        c = right1[x]
        for s, n in left1.items():
            exps[s] = exps.get(s, Fraction(0)) + e * Fraction(n, c)
        for s, n in right1.items():
            if s != x:
                exps[s] = exps.get(s, Fraction(0)) - e * Fraction(n, c)
    surviving = {s: e for s, e in exps.items() if e != 0}
    assert not (set(surviving) & inter), (
        f"an intermediate survives into the derived law: {surviving}"
    )
    # Written order: the fast step's own reactants first, then the rest.
    order = [s for s in left1 if s in surviving]
    order += [s for s in slow_left if s in surviving and s not in order]
    order += [s for s in surviving if s not in order]
    return {s: surviving[s] for s in order}


def _exponent(e):
    return str(e.numerator) if e.denominator == 1 else f"{e.numerator}/{e.denominator}"


def law_text(exps):
    """The derived law in this module's own notation, plus its overall order."""
    num, den = [], []
    for s, e in exps.items():
        piece = f"[\\mathrm{{{latex_formula(s)}}}]"
        mag = abs(e)
        if mag != 1:
            piece += f"^{{{_exponent(mag)}}}"
        (num if e > 0 else den).append(piece)
    body = "k" + "".join(num)
    law = body if not den else "\\frac{" + body + "}{" + "".join(den) + "}"
    total = sum(exps.values(), Fraction(0))
    assert total in ORDER_TEXT, f"an overall order of {total} has no wording here"
    return law, ORDER_TEXT[total]


def law_item(table, item):
    steps, slow, inter = mechanism(table)
    exps = derive(steps, slow, inter)
    law, order = law_text(exps)
    h.shows(item, f"{law} \\), overall order {order}")
    return (f"substituting the intermediate(s) {sorted(inter)} out of the slow step's rate "
            f"expression through the fast equilibrium gives exponents "
            f"{ {s: str(e) for s, e in exps.items()} }, that is {law} , overall order {order}")


def factor_item(table, item, name, multiplier):
    steps, slow, inter = mechanism(table)
    exps = derive(steps, slow, inter)
    power = exps.get(name, Fraction(0))
    assert power.denominator == 1 and power > 0, (
        f"{name} enters the derived law with exponent {power}, which this check cannot phrase"
    )
    factor = multiplier ** int(power)
    h.shows(item, f"{TIMESWORD[factor]} as large")
    return (f"the derived law carries {name} to the power {power}, so multiplying that "
            f"concentration by {multiplier} multiplies the rate by {factor}")


# ---------------------------------------------------------------- table items

def q4(table, item):
    return law_item(table, item)


def q5(table, item):
    return factor_item(table, item, "NO", 2)


def q6(table, item):
    steps, slow, inter = mechanism(table)
    exps = derive(steps, slow, inter)
    assert not (set(exps) & inter), f"an intermediate survives the substitution: {exps}"
    h.shows(item, "equilibrium of the fast step lets its concentration be replaced")
    return (f"the intermediates {sorted(inter)} are absent from the derived law's species "
            f"{sorted(exps)}, which is what the substitution accomplishes")


def q7(table, item):
    return law_item(table, item)


def q8(table, item):
    return factor_item(table, item, "Br2", 2)


def q9(table, item):
    return law_item(table, item)


def q11(table, item):
    return law_item(table, item)


def q12(table, item):
    steps, slow, inter = mechanism(table)
    exps = derive(steps, slow, inter)
    assert exps.get("O2", Fraction(0)) < 0, (
        f"dioxygen enters the derived law with exponent {exps.get('O2')}, not a negative one"
    )
    h.shows(item, "rate falls, because dioxygen appears as a divisor")
    return (f"the substitution leaves dioxygen with exponent {exps['O2']}, a divisor, so a "
            "larger concentration of it corresponds to a smaller rate")


def q13(table, item):
    return law_item(table, item)


def q21(table, item):
    return factor_item(table, item, "O3", 2)


TABLE_CHECKS = {4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 11: q11, 12: q12,
                13: q13, 21: q21}


CLAIMS = [
 ("Approximations such as pre-equilibrium must be made",
  "EK 5.9.A.1, near verbatim: if the first elementary reaction is not rate limiting, approximations such as pre-equilibrium must be made to determine a rate law expression."),
 ("first step that is fast and reversible",
  "EK 5.8.A.1 licenses the direct reading only when each step is irreversible or the first step is rate limiting, and EK 5.9.A.1 takes over exactly when the first elementary reaction is not rate limiting."),
 ("set by the molecularity of that slowest step",
  "EK 5.8.A.1 states that for such mechanisms the rate law is set by the molecularity of the slowest elementary step, which is why EK 5.9.A.1 is written for the other case."),
 (r"k[\mathrm{NO}]^{2}[\mathrm{O_2}] \), overall order three",
  "EK 5.9.A.1's approximation applied to the tabulated steps, with the substitution recomputed exactly in q4."),
 ("four times as large",
  "EK 5.9.A.1's derived law with EK 5.2.A.2's proportionality, recomputed in q5 from the exponent the substitution gives that reactant."),
 ("equilibrium of the fast step lets its concentration be replaced",
  "EK 5.9.A.1 calls for the approximation precisely so a rate law expression can be determined, and EK 5.7.A.3 makes the intermediate present only while the reaction runs. Recomputed in q6, which checks no intermediate survives."),
 (r"k[\mathrm{NO}]^{2}[\mathrm{Br_2}] \), overall order three",
  "EK 5.9.A.1's approximation applied to the tabulated bromine mechanism, recomputed in q7."),
 ("twice as large",
  "EK 5.9.A.1's derived law with EK 5.2.A.2's proportionality, recomputed in q8 from the exponent bromine carries."),
 (r"k[\mathrm{I_2}][\mathrm{H_2}] \), overall order two",
  "EK 5.9.A.1's approximation applied to the tabulated hydrogen iodide mechanism, where two powers of the atom collapse into one power of the molecule. Recomputed in q9."),
 ("does not settle the mechanism",
  "EK 5.9.A.1's approximation can reproduce the law EK 5.4.A.1 would give a single two-particle step, and EK 5.7.A.4 makes detection of an intermediate the further evidence that distinguishes such proposals."),
 (r"\frac{k[\mathrm{O_3}]^{2}}{[\mathrm{O_2}]} \), overall order one",
  "EK 5.9.A.1's approximation applied to the tabulated ozone mechanism, where the species formed alongside the intermediate enters as a divisor. Recomputed exactly in q11."),
 ("rate falls, because dioxygen appears as a divisor",
  "EK 5.9.A.1's substitution gives dioxygen a negative exponent, recomputed in q12, and EK 5.2.A.2 makes the rate follow the law as written."),
 (r"k[\mathrm{Cl_2}]^{1/2}[\mathrm{CHCl_3}] \), overall order three halves",
  "EK 5.9.A.1's approximation where one molecule gives two atoms, so replacing one atom brings in a square root. Recomputed with exact fractions in q13."),
 ("splitting one particle into two, so replacing one of them brings in a square root",
  "EK 5.9.A.1's pre-equilibrium writes the intermediate's concentration from the first step's equilibrium, and an equilibrium making two particles from one leaves the intermediate proportional to a square root."),
 ("present only while the reaction runs",
  "EK 5.7.A.3 makes an intermediate present only while a reaction is occurring, which is why EK 5.9.A.1 requires an approximation to reach a rate law in measurable concentrations."),
 ("species on both sides of the fast first step",
  "EK 5.9.A.1 names pre-equilibrium as the approximation, and treating the first step as an equilibrium relates the intermediate's concentration to the species it stands between."),
 ("The second, because it is the slower of the two",
  "EK 5.8.A.1 identifies the rate-limiting step as the slowest elementary step, and EK 5.9.A.1 is written for the case in which that step is not the first."),
 ("including the intermediate",
  "EK 5.4.A.1 infers an elementary step's rate law from the particles participating in its collision, and for these mechanisms one of those is the intermediate."),
 ("read off its slow step directly, while the second needs an approximation",
  "EK 5.8.A.1 covers the first case and EK 5.9.A.1 the second, and the substitution generally introduces powers the slow step alone does not carry."),
 ("intermediate consumed in the slow step is itself made from several particles",
  "EK 5.9.A.1's approximation replaces the intermediate's concentration with the concentrations that form it, and EK 5.4.A.1 makes those counts the powers."),
 ("four times as large",
  "EK 5.9.A.1's derived law, in which ozone carries two powers, with EK 5.2.A.2's proportionality. Recomputed in q21."),
 ("assumes the fast step stays at equilibrium while the slow step steadily removes",
  "EK 5.9.A.1 calls pre-equilibrium an approximation, and treating as an equilibrium a step that the next one is draining is the assumption that word flags."),
 ("not consistent with the measurement and must be revised or rejected",
  "EK 5.2.A.1 and EK 5.2.A.5 make the measured rate law the authority, and EK 5.9.A.1 makes the approximation a way of predicting one."),
 ("species that appear with it in that first step",
  "EK 5.9.A.1's pre-equilibrium relates the intermediate's concentration to the other species in the equilibrium it takes part in, which are those of the first step."),
 ("Adding that substance slows the reaction down",
  "EK 5.9.A.1's approximation puts a species formed alongside the intermediate into the denominator, and EK 5.2.A.2's proportionality makes a larger concentration of it correspond to a smaller rate."),
 ("counting a denominator power as negative",
  "EK 5.2.A.3 makes the overall order the sum of the powers, and EK 5.9.A.1's approximation is what supplies those powers when the first step is not rate limiting."),
 ("absorbed into the single rate constant",
  "EK 5.9.A.1's substitution multiplies the slow step's rate constant by the equilibrium expression, and the product of two constants is one constant."),
 ("The second, because it is the slowest and therefore rate limiting",
  "EK 5.8.A.1 makes the slowest step the rate-limiting one, and EK 5.9.A.1's approximation is applied to the intermediate in that step's rate expression."),
 ("two particles of A form an intermediate",
  "EK 5.9.A.1's approximation replaces the intermediate's concentration with the concentrations forming it, so an intermediate built from two particles of A carries two powers of A into a slow step already contributing one power of B."),
 ("offered as one example of the approximations",
  "EK 5.9.A.1's wording is approximations (SUCH AS pre-equilibrium) must be made, which presents the method as an instance rather than as the whole class."),
]


def _extra_mutations():
    def slow_step_first(mod, cl):
        """The slow label moved to the first step, which is 5.8's case."""
        t = mod.QUESTIONS[3]["table"]
        mod.QUESTIONS[3]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], r[1], "slow" if r[0] == "Step 1" else "fast"] for r in t["rows"]])

    def equilibrium_label_dropped(mod, cl):
        t = mod.QUESTIONS[6]["table"]
        mod.QUESTIONS[6]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], r[1], "fast"] if r[0] == "Step 1" else list(r) for r in t["rows"]])

    def key_power_wrong(mod, cl):
        """The keyed law retyped with the power the slow step alone would give."""
        mod.QUESTIONS[3]["choices"][0] = (
            r"\( \mathrm{rate} = k[\mathrm{NO}]^{3}[\mathrm{O_2}] \), overall order four")
        cl[3] = (r"k[\mathrm{NO}]^{3}[\mathrm{O_2}] \), overall order four", cl[3][1])

    def slow_step_retyped(mod, cl):
        """The slow step retyped so the mechanism loses this topic's shape.

        Note what this control proves and what it does not. Rescaling a step --
        writing ``2 Cl2 gives 4 Cl`` for ``Cl2 gives 2 Cl`` -- does NOT change
        the derived exponents, and should not: the substitution is scale
        invariant. So the mutation that bites is one that stops the slow step
        consuming an intermediate at all, and the shape guard is what catches
        it. The exponent arithmetic itself is controlled by the two mutations
        that retype a KEY away from the derived law.
        """
        t = mod.QUESTIONS[6]["table"]
        mod.QUESTIONS[6]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "NOBr2 + NOBr2 gives 2 NOBr + Br2", r[2]] if r[0] == "Step 2"
                  else list(r) for r in t["rows"]])

    def divisor_turned_factor(mod, cl):
        """The ozone key retyped as a product, hiding the inverse dependence."""
        mod.QUESTIONS[10]["choices"][0] = (
            r"\( \mathrm{rate} = k[\mathrm{O_3}]^{2}[\mathrm{O_2}]^{3} \), overall order four")
        cl[10] = (r"k[\mathrm{O_3}]^{2}[\mathrm{O_2}]^{3} \), overall order four", cl[10][1])

    def factor_key_wrong(mod, cl):
        mod.QUESTIONS[4]["choices"][0] = "It becomes sixteen times as large"
        cl[4] = ("sixteen times as large", cl[4][1])

    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "What does the mechanism shown above require?"
        no_figure_language(mod)

    return [("the slow label moved onto the first step, which is 5.8's case", slow_step_first),
            ("the equilibrium label dropped from the fast first step",
             equilibrium_label_dropped),
            ("the keyed law retyped with the slow step's own powers", key_power_wrong),
            ("the slow step retyped so the mechanism loses this topic's shape",
             slow_step_retyped),
            ("an inverse dependence retyped as a product", divisor_turned_factor),
            ("a concentration-change key moved off its recomputed factor", factor_key_wrong),
            ("a stem pointing at a picture the bank cannot show", figure_language)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    heq.selftest()
    h.selftest(h5_9, CLAIMS, table_checks=TABLE_CHECKS, mutations=_extra_mutations())

heq.selftest()
no_figure_language(h5_9)
h.run(h5_9, CLAIMS, table_checks=TABLE_CHECKS)
