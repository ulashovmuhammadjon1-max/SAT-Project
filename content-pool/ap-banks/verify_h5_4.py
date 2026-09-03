"""Key audit for AP CHEMISTRY 5.4 Elementary Reactions.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Four table items and three stem-data items
are recomputed from their own stimulus.

WHAT THE KEYS REST ON
---------------------
EK 5.4.A.1  The rate law of an elementary reaction can be inferred from the
            stoichiometry of the particles participating in a collision.
            (items 1, 2, 3, 4, 5, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
EK 5.4.A.2  Elementary reactions involving the simultaneous collision of three
            or more particles are rare.  (items 5, 6, 7, 12, 19, 21, 27)

Two items chain outward and say so in their rationale: item 8 and item 23 rest
on 5.4.A.1 TOGETHER WITH 5.2.A.1 and 5.2.A.5, because the point of both is that
the inference is licensed for an elementary step and not for an overall
reaction. That contrast is the whole content of topic 5.4 and cannot be asked
from inside 5.2, where the elementary case does not exist yet.

q16 BELOW PARSES THE STEPS RATHER THAN TRUSTING THE TABLE. It reads the reactant
side of each tabulated elementary step, counts the particles of each species,
and rebuilds the rate-law description in words -- then compares that against the
description the table prints. So a table cell that misdescribed a step would
fail here rather than teach a student the wrong inference.

NEGATIVE CONTROL: ``python3 verify_h5_4.py --selftest``.
"""
import sys

import h_chem_notation as hn
import h5_4 as M

NPART = "Particles that must collide"
NSIDE = "Number of particles on the reactant side"
IMPLIED = "Rate law implied by the particles colliding"
ORDCOL = "Overall order of its rate law"

ORDWORD = {1: "first", 2: "second", 3: "third"}
COUNTWORD = {"one": 1, "two": 2, "three": 3}
TIMESWORD = {2: "twice", 3: "three times", 4: "four times", 9: "nine times"}


def parse_reactants(step):
    """The particle count of each species on the reactant side of a step."""
    left = step.split("gives")[0]
    if ":" in left:
        left = left.split(":", 1)[1]
    counts = {}
    for part in left.split("+"):
        toks = part.split()
        assert toks, f"empty reactant term in {step!r}"
        if len(toks) == 2 and toks[0].isdigit():
            counts[toks[1]] = counts.get(toks[1], 0) + int(toks[0])
        else:
            assert len(toks) == 1, f"cannot read the reactant term {part!r} in {step!r}"
            counts[toks[0]] = counts.get(toks[0], 0) + 1
    return counts


# ------------------------------------------------------------ table questions

def q7(t, item):
    labs = hn.cg.labels(t)
    n = dict(zip(labs, hn.cg.col(t, NPART)))
    for lab in labs:
        assert n[lab] == sum(parse_reactants(lab).values()), \
            f"{lab}: the tabulated particle count disagrees with the step as written"
    rare = [l for l in labs if n[l] >= 3]
    assert len(rare) == 1, f"steps needing three or more particles: {rare}"
    hn.keyed(item, "three particles to collide simultaneously")
    return (f"each tabulated count matches its own step, and exactly one step of the "
            f"{len(labs)} needs three or more particles at once")


def q12(t, item):
    labs = hn.cg.labels(t)
    n = dict(zip(labs, hn.cg.col(t, NSIDE)))
    for lab in labs:
        assert n[lab] == sum(parse_reactants(lab).values()), \
            f"{lab}: the tabulated particle count disagrees with the step as written"
    rare = [l for l in labs if n[l] >= 3]
    assert len(rare) == 1 and rare[0].startswith("P2"), \
        f"proposals needing three or more particles: {rare}"
    hn.keyed(item, "two molecules of NO and one of O2")
    return ("reading each proposal's own reactant side gives the tabulated counts, and "
            "only one proposal requires three particles to meet at once")


def q16(t, item):
    for step, printed in [(r[0], r[1]) for r in t["rows"]]:
        counts = parse_reactants(step)
        rebuilt = " and ".join(f"{ORDWORD[c]} order in {sp}" for sp, c in counts.items())
        assert rebuilt == printed, (
            f"{step!r} implies {rebuilt!r}, but the table prints {printed!r}"
        )
    hn.keyed(item, "All three")
    return (f"rebuilding the rate-law description from each of the {len(t['rows'])} steps' "
            "own reactant particles reproduces exactly what the table prints")


def q21(t, item):
    labs = hn.cg.labels(t)
    order = dict(zip(labs, hn.cg.col(t, ORDCOL)))
    for lab in labs:
        word = lab.split()[0].lower()
        assert COUNTWORD[word] == order[lab], \
            f"{lab}: {COUNTWORD[word]} particles but a tabulated order of {order[lab]}"
    rare = [l for l in labs if order[l] >= 3]
    assert len(rare) == 1, f"entries at order three or above: {rare}"
    hn.keyed(item, "three-particle entry")
    return ("every tabulated order equals its own particle count, and exactly one entry "
            "reaches the three-particle case the framework calls rare")


TABLE_CHECKS = {7: q7, 12: q12, 16: q16, 21: q21}


# --------------------------------------------------------- stem-data questions

def a17(item):
    factor = 3 ** 1
    hn.keyed(item, f"{TIMESWORD[factor]} as large")
    return f"one power of the concentration turns a tripling into a factor of {factor}"


def a18(item):
    factor = 2 ** 2
    hn.keyed(item, f"{TIMESWORD[factor]} as large")
    return f"two colliding particles of Y make the step second order, so doubling gives {factor}"


def a29(item):
    factor = 2 * 2
    hn.keyed(item, f"{TIMESWORD[factor]} the first")
    return f"one power on each reactant turns two doublings into a factor of {factor}"


ARITH = {17: a17, 18: a18, 29: a29}

CLAIMS = [
 ("stoichiometry of the particles participating in the collision",
  "EK 5.4.A.1, near verbatim: the rate law of an elementary reaction can be inferred from the stoichiometry of the particles participating in a collision. Measurement is how an overall reaction's powers are found, under EK 5.2.A.5."),
 (r"k[\mathrm{A}] \), first order overall",
  "EK 5.4.A.1 infers the rate law from the participating particles. One particle of A is the whole reactant side, so its concentration enters to the first power."),
 (r"k[\mathrm{A}][\mathrm{B}] \), second order overall",
  "EK 5.4.A.1 infers the rate law from the colliding particles: one of each reactant, so each concentration enters to the first power."),
 (r"k[\mathrm{A}]^{2} \), second order overall",
  "EK 5.4.A.1 infers the rate law from the stoichiometry of the colliding particles. Two particles of A must meet, so its concentration enters twice."),
 (r"k[\mathrm{A}]^{2}[\mathrm{B}] \), third order",
  "EK 5.4.A.1 makes two particles of A and one of B give a squared and a first power respectively. EK 5.4.A.2 adds that a step needing three particles at once is rare."),
 ("They are rare",
  "EK 5.4.A.2, verbatim in substance: elementary reactions involving the simultaneous collision of three or more particles are rare. The framework calls them rare rather than impossible."),
 ("three particles to collide simultaneously",
  "Recomputed in q7 above, including a check that each tabulated count matches its own step. EK 5.4.A.2 is what makes that step the rare one."),
 ("particles that actually collide",
  "EK 5.4.A.1 licenses the inference only for an elementary reaction, where the stoichiometry IS the collision, while EK 5.2.A.1 and 5.2.A.5 make an overall reaction's powers a matter for experiment."),
 (r"k[\mathrm{O_3}] \), first order overall",
  "EK 5.4.A.1 infers the rate law from the particles participating in the collision, which are the step's reactants. One ozone molecule is the whole reactant side and products do not enter."),
 (r"k[\mathrm{NO}][\mathrm{O_3}] \), second order overall",
  "EK 5.4.A.1 infers the rate law from the colliding particles, one molecule of each reactant, so each concentration enters to the first power."),
 ("They are equal",
  "EK 5.4.A.1 makes each participating particle contribute one power of its own concentration, and EK 5.2.A.3 makes the overall order the sum of the powers, so the two counts coincide."),
 ("two molecules of NO and one of O2",
  "Recomputed in q12 above. EK 5.4.A.2 states that elementary reactions involving the simultaneous collision of three or more particles are rare, and only one tabulated proposal needs such a collision."),
 ("one particle of each of the two reactants collides",
  "EK 5.4.A.1 makes the rate law of an elementary step follow from the colliding particles, so a step is consistent with a measured rate law when its particle counts match the measured powers."),
 (r"k[\mathrm{NOBr}]^{2} \), second order overall",
  "EK 5.4.A.1 infers the rate law from the colliding particles: two NOBr molecules must meet, so that concentration enters twice, and the products take no part in the collision."),
 ("Only the reactants of the step appear in it",
  "EK 5.4.A.1 infers the rate law from the stoichiometry of the particles PARTICIPATING IN A COLLISION, and the particles that collide to start a step are its reactants."),
 ("All three",
  "Recomputed in q16 above by rebuilding each row's rate-law description from its own step. EK 5.4.A.1 licenses exactly that inference for an elementary reaction."),
 ("three times as large",
  "Recomputed in a17. EK 5.4.A.1 gives the step one power of the concentration of X and EK 5.2.A.2 makes the rate proportional to that concentration raised to its power."),
 ("four times as large",
  "Recomputed in a18. EK 5.4.A.1 makes a step needing two particles of Y second order in Y, so doubling that concentration multiplies the rate by two squared."),
 ("requires three particles to collide at once",
  "EK 5.4.A.1 makes the overall order of an elementary step equal the number of colliding particles, so a third order step needs three at once, and EK 5.4.A.2 calls such steps rare."),
 (r"k[\mathrm{Cl}][\mathrm{CH_4}] \), second order overall",
  "EK 5.4.A.1 infers the rate law from the colliding particles, one chlorine atom and one methane molecule. A subscript inside a chemical formula is not a power in a rate law."),
 ("three-particle entry",
  "Recomputed in q21 above, including a check that each tabulated order equals its own particle count. EK 5.4.A.2 makes the three-particle case the rare one."),
 ("formed by the collision rather than taking part in it",
  "EK 5.4.A.1 infers the rate law from the particles PARTICIPATING IN A COLLISION, and the products are what the collision makes rather than what must meet for it to occur."),
 ("cannot be a single elementary step",
  "EK 5.4.A.1 makes an elementary step's powers follow from its colliding particles, so a measured rate law disagreeing with those counts rules the reaction out as one step; EK 5.2.A.1 makes the measurement the authority."),
 (r"k[\mathrm{NO_2}]^{2} \), second order overall",
  "EK 5.4.A.1 infers the rate law from the colliding particles. Two molecules of NO2 must meet whether the step is written with a coefficient of two or as a sum of two identical species."),
 ("half order overall",
  "EK 5.4.A.1 makes the powers counts of colliding particles, and a collision involves a whole number of particles, so a fractional power cannot arise from counting participants in one collision."),
 ("matching their particle counts",
  "EK 5.4.A.1 makes the rate law of an elementary step follow from the stoichiometry of the participating particles, so a one-particle step carries one power and a two-particle step carries two."),
 (r"k[\mathrm{A}]^{3} \), and the framework calls such steps rare",
  "EK 5.4.A.1 makes three colliding particles of A give three powers of its concentration, and EK 5.4.A.2 states that such simultaneous three-particle steps are rare rather than impossible."),
 ("How many particles of each species must meet",
  "EK 5.4.A.1 infers the rate law from that stoichiometry and the rate law's powers are counts of participating particles, so the phrase refers to how many of each species take part in the one collision."),
 ("four times the first",
  "Recomputed in a29. EK 5.4.A.1 gives the step one power on each reactant and EK 5.2.A.2 makes the rate proportional to the product of the concentration factors."),
 ("without further measurement",
  "EK 5.4.A.1 is exactly this permission: for an elementary reaction the rate law can be inferred from the stoichiometry of the colliding particles, without the experiments EK 5.2.A.5 requires for an overall reaction."),
]


def _wreck_count(mod, cl):
    """Module-specific control: mistype a particle count against its own step."""
    t = mod.QUESTIONS[6]["table"]
    mod.QUESTIONS[6]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "2"] if r[0].startswith("S4") else list(r) for r in t["rows"]])


def _wreck_description(mod, cl):
    """Module-specific control: misdescribe a step's implied rate law."""
    t = mod.QUESTIONS[15]["table"]
    mod.QUESTIONS[15]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "first order in NOBr"] if r[0].startswith("2 NOBr") else list(r)
              for r in t["rows"]])


def _wreck_order_column(mod, cl):
    """Module-specific control: break the order-equals-particles pairing."""
    t = mod.QUESTIONS[20]["table"]
    mod.QUESTIONS[20]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "1"] if r[0].startswith("Three") else list(r) for r in t["rows"]])


def _wreck_stem_key(mod, cl):
    """Module-specific control: key a concentration-change item to the wrong factor."""
    mod.QUESTIONS[16]["choices"][0] = "nine times as large"


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH,
                extra=[("a particle-count cell corrupted", _wreck_count),
                       ("a rate-law description corrupted", _wreck_description),
                       ("an overall-order cell corrupted", _wreck_order_column),
                       ("a key moved off its recomputed factor", _wreck_stem_key)])

hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
