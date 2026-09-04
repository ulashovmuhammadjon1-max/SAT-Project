"""Key audit for AP CHEMISTRY 5.8 Reaction Mechanism and Rate Law.

One ``(anchor, claim)`` per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EK 5.8.A.1  For mechanisms in which each elementary step is irreversible, or in
            which the first step is rate limiting, the rate law is set by the
            molecularity of the slowest elementary step.        (every item)
EK 5.4.A.1  supplies what molecularity means for the powers: the rate law of an
            elementary reaction follows from the stoichiometry of the particles
            participating in the collision.
            (items 4, 6, 8, 9, 10, 11, 12, 14, 15, 16, 20, 22, 23, 27, 28)
EK 5.2.A.1/.2/.3  supply the measured rate law as the authority, the
            proportionality to concentration, and the overall order as the sum
            of the powers.               (items 5, 7, 13, 15, 16, 17, 18, 22, 24)
EK 5.9.A.1  is the case the condition excludes -- if the first elementary
            reaction is not rate limiting, an approximation is needed.
            (items 2, 21, 24, 25)

THE RATE LAW IS REBUILT, NOT TRUSTED. ``rate_law`` below reads the reactant side
of the step the table labels slow, counts the particles of each species, and
writes out the law it implies -- ``k[\\mathrm{NO_2}]^{2}`` and the order word
that goes with it. The keyed choice must contain exactly that string. So a key
pointing at the wrong power, or at a species that does not collide in the slow
step, fails here.

THREE STRUCTURAL GUARDS RUN OVER EVERY TABULATED MECHANISM, because 5.8.A.1's
rule is conditional and this bank must not teach it as unconditional:

  * every elementary step must balance in atoms and charge (EK 4.2.A.2);
  * exactly one step is labelled slow, and it must be the FIRST -- the learning
    objective for 5.8 is the first-step-rate-limiting case;
  * the slow step's reactants must contain no intermediate of the mechanism,
    since a rate law in an intermediate's concentration is EK 5.9.A.1's
    pre-equilibrium case and is not read off in this topic's way.

NEGATIVE CONTROL: ``python3 verify_h5_8.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h_equation as heq

import h5_8

STEPCOL = "Elementary reaction"
RATECOL = "Relative rate"

ORDWORD = {1: "first", 2: "second", 3: "third", 4: "fourth"}
TIMESWORD = {1: "unchanged", 2: "twice", 3: "three times", 4: "four times",
             8: "eight times", 9: "nine times", 27: "twenty seven times"}

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


# ------------------------------------------------------- rebuilding a rate law

def latex_formula(name):
    """``NO2`` to ``NO_2``; ``I-`` to ``I^-``. The house spelling inside a span."""
    m = re.search(r"(\d?)([+-])$", name)
    charge = ""
    if m:
        size = m.group(1)
        charge = f"^{{{size}{m.group(2)}}}" if size else f"^{m.group(2)}"
        name = name[:m.start()]
    return re.sub(r"(\d)", r"_\1", name) + charge


def rate_law(step):
    """The rate law the molecularity of ``step`` implies, and its order word."""
    left, _ = heq.step_species(step)
    parts = []
    for name, n in left.items():
        piece = f"[\\mathrm{{{latex_formula(name)}}}]"
        if n > 1:
            piece += f"^{{{n}}}"
        parts.append(piece)
    order = sum(left.values())
    assert order in ORDWORD, f"an overall order of {order} has no word here"
    return "k" + "".join(parts), ORDWORD[order], order


def mechanism(table):
    """The tabulated steps and the index of the slow one, with every guard applied."""
    si, ri = table["headers"].index(STEPCOL), table["headers"].index(RATECOL)
    steps = [r[si] for r in table["rows"]]
    rates = [str(r[ri]).strip().lower() for r in table["rows"]]
    for s in steps:
        assert heq.balanced(s), f"a tabulated step does not balance: {s} -- {heq.report(s)}"
    slow = [i for i, r in enumerate(rates) if r == "slow"]
    assert len(slow) == 1, f"the tabulated relative rates are {rates}; exactly one must be slow"
    assert slow[0] == 0, (
        "the slow step must be the FIRST; a slow step later in the mechanism is EK 5.9.A.1's "
        f"pre-equilibrium case, and the table marks step {slow[0] + 1}"
    )
    return steps, slow[0]


def no_intermediate_in_key(steps, item):
    """EK 5.9.A.1's case must not be keyed here.

    A rate law written in the concentration of an intermediate is what EK
    5.9.A.1 sends to a pre-equilibrium approximation, and it is not something
    EK 5.8.A.1 licenses reading off a slow step. Every mechanism in this module
    forms at least one intermediate and offers a distractor written in it, so
    this is reachable: keying that distractor fires it.
    """
    for name in heq.intermediates(steps):
        token = f"[\\mathrm{{{latex_formula(name)}}}]"
        assert token not in item["choices"][item["ans"]], (
            f"the keyed rate law is written in the intermediate {name}, which is EK "
            f"5.9.A.1's pre-equilibrium case rather than EK 5.8.A.1's"
        )
    return heq.intermediates(steps)


def law_item(table, item):
    steps, slow = mechanism(table)
    inter = no_intermediate_in_key(steps, item)
    law, word, _ = rate_law(steps[slow])
    anchor = f"{law} \\), {word} order overall"
    h.shows(item, anchor)
    return (f"the tabulated slow step {steps[slow]!r} carries the particles that must collide, "
            f"so its molecularity rebuilds the rate law as {law} , {word} order overall, "
            f"naming none of the intermediates {inter}")


def factor_item(table, item, species_name, multiplier):
    """What multiplying one concentration does, from the slow step's own powers."""
    steps, slow = mechanism(table)
    left, _ = heq.step_species(steps[slow])
    power = left.get(species_name, 0)
    factor = multiplier ** power
    h.shows(item, TIMESWORD[factor] if factor != 1 else "It is unchanged")
    return (f"{species_name} appears {power} time(s) in the tabulated slow step, so "
            f"multiplying its concentration by {multiplier} multiplies the rate by {factor}")


# ---------------------------------------------------------------- table items

def q4(table, item):
    return law_item(table, item)


def q5(table, item):
    steps, slow = mechanism(table)
    left, _ = heq.step_species(steps[slow])
    assert "CO" not in left, f"carbon monoxide does appear in the slow step: {left}"
    later = [i for i, s in enumerate(steps) if i != slow and "CO" in heq.step_species(s)[0]]
    assert later, "carbon monoxide must enter in some step, or the item makes no sense"
    h.shows(item, "consumed only in a step that is not rate limiting")
    return (f"the tabulated slow step's reactants are {sorted(left)}, which exclude carbon "
            f"monoxide, and it enters instead at step(s) {[i + 1 for i in later]}")


def q6(table, item):
    return law_item(table, item)


def q8(table, item):
    return law_item(table, item)


def q9(table, item):
    steps, slow = mechanism(table)
    left, _ = heq.step_species(steps[slow])
    assert "I-" in left, f"the iodide ion is not a reactant of the slow step: {left}"
    assert heq.catalysts(steps) == ["I-"], (
        f"the tabulated mechanism's catalysts are {heq.catalysts(steps)}"
    )
    h.shows(item, "one of the particles that must collide in the rate-limiting step")
    return ("the iodide ion is both a reactant of the tabulated slow step and the mechanism's "
            "one catalyst, so it carries a power while its net amount is unchanged")


def q10(table, item):
    return law_item(table, item)


def q11(table, item):
    return law_item(table, item)


def q12(table, item):
    return law_item(table, item)


def q13(table, item):
    return factor_item(table, item, "CHCl3", 2)


def q14(table, item):
    return law_item(table, item)


def q15(table, item):
    return factor_item(table, item, "NO", 2)


TABLE_CHECKS = {4: q4, 5: q5, 6: q6, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12,
                13: q13, 14: q14, 15: q15}


# --------------------------------------------------------------- stem numerics

def n16(item):
    order = 1 + 1
    h.shows(item, f"{ORDWORD[order].capitalize().replace('Second', 'Two')}, the sum of the powers")
    return (f"one particle of each of two reactants in the slow step contributes one power "
            f"each, so the overall order is {order}")


def n21(item):
    law, word, order = rate_law("X gives Y + Z")
    assert (law, order) == ("k[\\mathrm{X}]", 1), (law, order)
    h.shows(item, f"{law} \\), {word} order overall")
    return f"a single particle breaking apart gives {law} , which is {word} order overall"


def n23(item):
    factor = 3 ** 2
    h.shows(item, f"{TIMESWORD[factor]} as large")
    return (f"two colliding particles of one reactant make the slow step second order in it, "
            f"so tripling that concentration multiplies the rate by {factor}")


NUMERIC = {16: n16, 21: n21, 23: n23}


CLAIMS = [
 ("molecularity of the slowest elementary step",
  "EK 5.8.A.1, near verbatim: the rate law of the reaction is set by the molecularity of the slowest elementary step. EK 5.2.A.1 keeps the overall equation's coefficients out of a rate law."),
 ("each elementary step is irreversible, or when the first step is rate limiting",
  "EK 5.8.A.1 states the rule under exactly those two conditions, and EK 5.9.A.1 covers the case they exclude."),
 ("The rate-limiting step",
  "EK 5.8.A.1 names the slowest elementary step the rate-limiting step in its own parenthesis."),
 (r"k[\mathrm{NO_2}]^{2} \), second order overall",
  "EK 5.8.A.1's molecularity of the slow step, with EK 5.4.A.1 counting the particles that collide in it. Rebuilt from the tabulated slow step in q4."),
 ("consumed only in a step that is not rate limiting",
  "EK 5.8.A.1 makes the rate law depend on the slowest step alone. Recomputed in q5, which checks carbon monoxide is absent from the slow step and present in a later one."),
 (r"k[\mathrm{NO_2}][\mathrm{F_2}] \), second order overall",
  "EK 5.8.A.1 with EK 5.4.A.1's one power for each colliding particle, rebuilt from the tabulated slow step in q6."),
 ("powers need not match the coefficients of the overall equation",
  "EK 5.8.A.1 ties the rate law to the slow step, and EK 5.2.A.1 makes an overall reaction's powers a matter for measurement rather than for reading off coefficients."),
 (r"k[\mathrm{H_2O_2}][\mathrm{I^-}] \), second order overall",
  "EK 5.8.A.1 with EK 5.4.A.1's particle counts, rebuilt from the tabulated slow step in q8."),
 ("one of the particles that must collide in the rate-limiting step",
  "EK 5.8.A.1 sources the powers in the slow step's molecularity. Recomputed in q9, which confirms the species is both a reactant of that step and the mechanism's only catalyst."),
 (r"k[\mathrm{O_3}] \), first order overall",
  "EK 5.8.A.1 with EK 5.4.A.1's single power for a single participating particle, rebuilt in q10."),
 (r"k[\mathrm{NO}][\mathrm{Br_2}] \), second order overall",
  "EK 5.8.A.1 with EK 5.4.A.1's one power for each of two different colliding particles, rebuilt in q11."),
 (r"k[\mathrm{Cl_2}] \), first order overall",
  "EK 5.8.A.1 makes the slowest step decisive however many steps follow, rebuilt from the tabulated slow step in q12."),
 ("chloroform enters only after the rate-limiting step",
  "EK 5.8.A.1 sources the powers in the slow step alone and EK 5.2.A.2 makes the rate depend on the concentrations appearing in the law. Recomputed in q13 from the slow step's own powers."),
 (r"k[\mathrm{NO}]^{2} \), second order overall",
  "EK 5.8.A.1 with EK 5.4.A.1's two powers for two colliding particles of one species, rebuilt in q14."),
 ("four times as large",
  "EK 5.8.A.1's rate law with EK 5.2.A.2's proportionality, recomputed in q15 from the power the tabulated slow step gives that species."),
 ("Two, the sum of the powers",
  "EK 5.8.A.1's molecularity with EK 5.4.A.1's counting and EK 5.2.A.3's sum of the powers, recomputed in n16."),
 ("no faster than its slowest step",
  "EK 5.8.A.1 sets the rate law by the molecularity of the SLOWEST elementary step, which is the framework's own way of saying that later steps do not limit the rate."),
 ("not consistent with the measurement and must be revised or rejected",
  "EK 5.2.A.1 and EK 5.2.A.5 make the measured rate law the authority, and EK 5.8.A.1 makes a first-step-limited mechanism predict one."),
 ("By measuring the rate law",
  "EK 5.8.A.1 makes the rate law a consequence of the slowest step, so different slow steps predict different laws, and EK 5.2.A.5 makes the law measurable."),
 ("Only the species that collide in the first step",
  "EK 5.8.A.1 sets the rate law by the molecularity of the slowest step, which for a first-step-limited mechanism is the particles colliding in it under EK 5.4.A.1."),
 (r"k[\mathrm{X}] \), first order overall",
  "EK 5.8.A.1 with EK 5.4.A.1's single power for a single participating particle, rebuilt in n21."),
 ("first step is reversible and not rate limiting needs an approximation",
  "EK 5.8.A.1 states its rule conditionally, and EK 5.9.A.1 says that if the first elementary reaction is not rate limiting, approximations such as pre-equilibrium must be made."),
 ("nine times as large",
  "EK 5.8.A.1's rate law with EK 5.4.A.1's squared concentration and EK 5.2.A.2's proportionality, recomputed in n23."),
 ("How many particles must come together",
  "EK 5.8.A.1 sets the rate law by the molecularity of the slow step, and EK 5.4.A.1 makes that the stoichiometry of the particles participating in a collision."),
 ("present only while the reaction runs",
  "EK 5.7.A.3 makes an intermediate present only while a reaction occurs, and EK 5.2.A.1 writes a rate law in reactant concentrations, so such a mechanism needs EK 5.9.A.1's approximation."),
 ("FIRST step to be rate limiting",
  "EK 5.8.A.1 attaches that condition explicitly, and EK 5.9.A.1 sends the remaining case to an approximation such as pre-equilibrium."),
 ("wherever that step falls",
  "EK 5.8.A.1 offers two sufficient conditions, and under the irreversible-steps condition the slowest step sets the law without any requirement that it be the first."),
 ("double the rate in the first case and quadruple it in the second",
  "EK 5.8.A.1 makes each candidate slow step predict its own law through EK 5.4.A.1's particle counts, and EK 5.2.A.2 turns different powers into different responses to a doubling."),
 ("Which particles must collide in the rate-limiting step",
  "EK 5.8.A.1 makes the rate law the molecularity of the slow step and EK 5.4.A.1 makes that molecularity a count of participating particles."),
 ("more than one mechanism can have a slowest step of the same molecularity",
  "EK 5.8.A.1 fixes the law from the slow step but not the converse, and EK 5.7.A.4 makes detection of an intermediate a common way to build evidence for one mechanism over an alternative."),
]


def _extra_mutations():
    def slow_step_moved(mod, cl):
        """The slow label moved to the second step, which is 5.9's case."""
        t = mod.QUESTIONS[3]["table"]
        mod.QUESTIONS[3]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], r[1], "fast" if r[2] == "slow" else "slow"] for r in t["rows"]])

    def power_wrong(mod, cl):
        """The keyed rate law retyped with the wrong power."""
        mod.QUESTIONS[3]["choices"][0] = (
            r"\( \mathrm{rate} = k[\mathrm{NO_2}]^{3} \), third order overall")
        cl[3] = (r"k[\mathrm{NO_2}]^{3} \), third order overall", cl[3][1])

    def slow_step_species_changed(mod, cl):
        """A tabulated slow step retyped, so the rebuilt law no longer matches the key."""
        t = mod.QUESTIONS[5]["table"]
        mod.QUESTIONS[5]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "NO2 + NO2 gives N2O4", r[2]] if r[0] == "Step 1" else list(r)
                  for r in t["rows"]])

    def two_slow_steps(mod, cl):
        t = mod.QUESTIONS[11]["table"]
        mod.QUESTIONS[11]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], r[1], "slow"] if r[0] == "Step 2" else list(r) for r in t["rows"]])

    def key_written_in_an_intermediate(mod, cl):
        """The key moved to the rate law written in the mechanism's intermediate."""
        mod.QUESTIONS[3]["ans"] = 2
        cl[3] = (r"k[\mathrm{NO_3}][\mathrm{CO}] \), second order overall", cl[3][1])

    def factor_key_wrong(mod, cl):
        """The doubling key moved off the factor the slow step's powers give."""
        mod.QUESTIONS[14]["choices"][0] = "It becomes sixteen times as large"
        cl[14] = ("sixteen times as large", cl[14][1])

    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "What sets the rate law in the mechanism shown above?"
        no_figure_language(mod)

    return [("the slow label moved off the first step", slow_step_moved),
            ("the keyed rate law retyped with the wrong power", power_wrong),
            ("a tabulated slow step retyped so the rebuilt law changes",
             slow_step_species_changed),
            ("two steps both labelled slow", two_slow_steps),
            ("a key written in the concentration of an intermediate, which is 5.9's case",
             key_written_in_an_intermediate),
            ("a concentration-change key moved off its recomputed factor", factor_key_wrong),
            ("a stem pointing at a picture the bank cannot show", figure_language)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    heq.selftest()
    h.selftest(h5_8, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

heq.selftest()
no_figure_language(h5_8)
h.run(h5_8, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
