"""Key audit for AP CHEMISTRY 5.1 Reaction Rates.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Seven table items and six stem-data items are
recomputed from their own stimulus and asserted against the keyed choice.

WHAT THE KEYS REST ON
---------------------
EK 5.1.A.1  The kinetics of a chemical reaction is defined as the rate at which
            an amount of reactants is converted to products per unit of time.
            (items 1, 5, 6, 8, 16, 22, 23, 24, 30)
EK 5.1.A.2  The rates of change of reactant and product concentrations are
            determined by the stoichiometry in the balanced chemical equation.
            (items 2, 3, 9, 13, 14, 19, 20, 25, 26, 28)
EK 5.1.A.3  The rate of a reaction is influenced by reactant concentrations,
            temperature, surface area, catalysts, and other environmental
            factors.  (items 4, 7, 10, 11, 12, 15, 17, 18, 21, 27, 29)

WHAT IS DELIBERATELY ABSENT, so that this module does not answer another
topic's question:

  * No key explains WHY a factor changes a rate. Collisions, energy and
    orientation are 5.5; the temperature dependence of an elementary rate is
    5.6; how a catalyst works is 5.11. Items 10, 17 and 18 assert only that
    temperature and catalysts influence the rate, which is what 5.1.A.3 states.
  * No key asserts a reaction ORDER or a rate constant. Item 15 deliberately
    rejects the option that names an order, because establishing one takes the
    comparison of initial rates that belongs to 5.2.

DISTRACTORS ON THE STOICHIOMETRY ITEMS are the two errors 5.1.A.2 invites:
inverting the coefficient ratio, and setting every rate equal. Both are checked
false against the same coefficients in the recomputation.

NEGATIVE CONTROL: ``python3 verify_h5_1.py --selftest``.
"""
import sys

import h_chem_notation as hn
import h5_1 as M

T = "Time (seconds)"
C = "Concentration of N2O5 (moles per liter)"
O2 = "Moles of O2 collected"
TEMP = "Temperature (degrees Celsius)"
DONE = "Time for the reaction to finish (seconds)"
RC = "Coefficient of the reactant monitored"
PC = "Coefficient of the product monitored"
HALF = "Time for half the hydrogen peroxide to decompose (seconds)"

MPLS = "moles per liter per second"


# ------------------------------------------------------------ table questions

def q5(t, item):
    time = hn.cg.col(t, T)
    conc = hn.cg.col(t, C)
    rate = (conc[0] - conc[1]) / (time[1] - time[0])
    hn.keyed(item, f"{rate:.5f} {MPLS}")
    return (f"{conc[0]} falling to {conc[1]} over {time[1] - time[0]:.0f} seconds is "
            f"{rate:.5f} moles per liter per second")


def q6(t, item):
    time = hn.cg.col(t, T)
    conc = hn.cg.col(t, C)
    first = (conc[0] - conc[1]) / (time[1] - time[0])
    last = (conc[-2] - conc[-1]) / (time[-1] - time[-2])
    assert time[1] - time[0] == time[-1] - time[-2], "the two intervals must be equally long"
    assert last < first, f"the later rate {last} is not smaller than the earlier {first}"
    hn.keyed(item, "less N2O5 disappears in the later interval")
    return (f"the first interval loses {conc[0] - conc[1]:.3f} and the last loses "
            f"{conc[-2] - conc[-1]:.3f} over the same {time[1] - time[0]:.0f} seconds")


def q8(t, item):
    time = hn.cg.col(t, T)
    mol = hn.cg.col(t, O2)
    rate = (mol[-1] - mol[0]) / (time[-1] - time[0])
    hn.keyed(item, f"{rate:.5f} moles per second")
    return (f"{mol[-1]} moles collected over {time[-1]:.0f} seconds is {rate:.5f} moles "
            "per second on average")


def q11(t, item):
    labs = hn.cg.labels(t)
    form = {r[0]: r[1] for r in t["rows"]}
    temp = dict(zip(labs, hn.cg.col(t, TEMP)))
    group = [l for l in labs if temp[l] == temp["1"]]
    assert group == ["1", "2", "3"], f"trials sharing trial 1's temperature: {group}"
    assert len({form[l] for l in group}) == len(group), \
        "the trials at one temperature must all use a different form of the solid"
    assert temp["4"] != temp["3"] and form["4"] == form["3"], \
        "the fourth trial must vary temperature at fixed form, not surface area"
    hn.keyed(item, "Trials 1, 2 and 3")
    return ("three trials share one temperature and differ only in the form of the solid, "
            "so only surface area varies among them")


def q12(t, item):
    labs = hn.cg.labels(t)
    form = {r[0]: r[1] for r in t["rows"]}
    temp = dict(zip(labs, hn.cg.col(t, TEMP)))
    done = dict(zip(labs, hn.cg.col(t, DONE)))
    pairs = [(a, b) for i, a in enumerate(labs) for b in labs[i + 1:]
             if form[a] == form[b] and temp[a] != temp[b]]
    assert pairs == [("3", "4")], f"pairs differing only in temperature: {pairs}"
    ratio = done["3"] / done["4"]
    assert 2.5 < ratio < 3.5, f"the completion times differ by a factor of {ratio}, not about three"
    hn.keyed(item, "Trials 3 and 4")
    return (f"one pair shares a form and differs in temperature, and the warmer finished in "
            f"{done['4']:.0f} against {done['3']:.0f} seconds, a factor of {ratio:.1f}")


def q14(t, item):
    labs = hn.cg.labels(t)
    r = dict(zip(labs, hn.cg.col(t, RC)))
    p = dict(zip(labs, hn.cg.col(t, PC)))
    doubles = [l for l in labs if p[l] == 2 * r[l]]
    assert doubles == ["2 N2O5 gives 4 NO2 + O2"], f"rows with a product to reactant ratio of two: {doubles}"
    assert any(p[l] < r[l] for l in labs), \
        "'a product coefficient always exceeds the reactant coefficient' must be false"
    hn.keyed(item, "the coefficients are two and four")
    return ("exactly one tabulated equation has its product coefficient at twice its "
            "reactant coefficient, and another has it smaller")


def q18(t, item):
    labs = hn.cg.labels(t)
    cat = {r[0]: r[1] for r in t["rows"]}
    time = dict(zip(labs, hn.cg.col(t, HALF)))
    none = [l for l in labs if cat[l].strip().lower() == "none"]
    assert len(none) == 1, f"rows with no catalyst: {none}"
    withcat = [l for l in labs if l not in none]
    assert all(time[l] < time[none[0]] for l in withcat), \
        "every catalyzed trial must be faster than the uncatalyzed one"
    assert len({time[l] for l in withcat}) == len(withcat), \
        "'the catalysts influenced it equally' must be false, so their times must differ"
    hn.keyed(item, "the two catalysts did not influence it equally")
    return (f"the uncatalyzed trial takes {time[none[0]]:.0f} seconds against "
            f"{sorted(time[l] for l in withcat)} for the catalyzed ones, which also differ "
            "from each other")


TABLE_CHECKS = {5: q5, 6: q6, 8: q8, 11: q11, 12: q12, 14: q14, 18: q18}


# --------------------------------------------------------- stem-data questions

def a2(item):
    rate = 0.080 * (2 / 4)
    hn.keyed(item, f"{rate:.3f} {MPLS}")
    return f"two N2O5 per four NO2 makes the reactant rate {rate:.3f} moles per liter per second"


def a3(item):
    rate = 0.30 * (2 / 3)
    hn.keyed(item, f"{rate:.2f} {MPLS}")
    return f"two NH3 per three H2 makes the ammonia rate {rate:.2f} moles per liter per second"


def a19(item):
    rate = 0.25 * (6 / 5)
    hn.keyed(item, f"{rate:.2f} {MPLS}")
    return f"six H2O per five O2 makes the water rate {rate:.2f} moles per liter per second"


def a22(item):
    rate = (0.500 - 0.350) / 50
    hn.keyed(item, f"{rate:.4f} {MPLS}")
    return f"a fall of 0.150 over 50 seconds is {rate:.4f} moles per liter per second"


def a23(item):
    first, second = 0.20 / 10, 0.60 / 60
    assert first > second, "the first reaction should have the larger average rate"
    factor = first / second
    assert abs(factor - 2) < 1e-9, f"the factor recomputes to {factor}, not two"
    hn.keyed(item, "The first, by a factor of two")
    return (f"{first} against {second} moles per liter per second is a ratio of "
            f"{factor:.0f} in favour of the first")


def a26(item):
    rate = 0.24 * (1 / 4)
    hn.keyed(item, f"{rate:.3f} {MPLS}")
    return f"one O2 per four NO2 makes the oxygen rate {rate:.3f} moles per liter per second"


ARITH = {2: a2, 3: a3, 19: a19, 22: a22, 23: a23, 26: a26}

CLAIMS = [
 ("converted to products per unit of time",
  "EK 5.1.A.1, near verbatim: the kinetics of a chemical reaction is defined as the rate at which an amount of reactants is converted to products per unit of time. Total yield and energy change are different quantities."),
 ("0.040 moles per liter per second",
  "Recomputed in a2. EK 5.1.A.2 makes the rates of change determined by the stoichiometry, and four NO2 appear per two N2O5 consumed."),
 ("0.20 moles per liter per second",
  "Recomputed in a3. EK 5.1.A.2 ties the several rates of one reaction to the coefficients: two NH3 form per three H2 consumed."),
 ("surface area of a solid reactant",
  "EK 5.1.A.3 lists reactant concentrations, temperature, surface area, catalysts and other environmental factors as influences on the rate. Only one of the five options appears on that list."),
 ("0.00080 moles per liter per second",
  "Recomputed in q5 above from the table's first interval. EK 5.1.A.1 makes a rate an amount converted per unit of time, so an average rate is the concentration change over the interval length."),
 ("less N2O5 disappears in the later interval",
  "Recomputed in q6 above. The two intervals are equally long, so under EK 5.1.A.1 comparing their rates is comparing their concentration changes, and the later change is smaller."),
 ("surface area is one of the factors",
  "EK 5.1.A.3 names surface area among the influences on rate. Grinding changes the exposed area without changing how much reactant is present, so it does not change the eventual yield."),
 ("0.00060 moles per second",
  "Recomputed in q8 above. EK 5.1.A.1 defines the rate as an amount converted per unit of time, so the average is the amount collected over the elapsed time."),
 ("twice as fast as oxygen appears",
  "EK 5.1.A.2 makes the rates determined by the stoichiometry: two peroxide molecules are consumed and two water molecules formed for every one oxygen molecule."),
 ("temperature is one of the factors",
  "EK 5.1.A.3 lists temperature among the influences on the rate of a reaction. It governs how fast the conversion happens, not how much product the mixture can make."),
 ("Trials 1, 2 and 3",
  "Recomputed in q11 above from the table's own temperature column. EK 5.1.A.3 names surface area and temperature as separate influences, so isolating one requires the other to be held constant."),
 ("Trials 3 and 4",
  "Recomputed in q12 above. EK 5.1.A.3 names temperature among the influences, and the only tabulated pair sharing a form of the solid differs in temperature alone."),
 ("B disappears twice as fast as A does",
  "EK 5.1.A.2 makes the rates of change of reactant and product concentrations determined by the stoichiometry, so each rate stands to the others in the ratio of the coefficients."),
 ("the coefficients are two and four",
  "Recomputed in q14 above. EK 5.1.A.2 makes the ratio of two rates the ratio of the two coefficients, and the table supplies both for each equation."),
 ("Reactant concentration influences the rate",
  "EK 5.1.A.3 names reactant concentrations among the factors that influence the rate. Naming an ORDER would require the quantitative initial-rate comparison of topic 5.2, which this observation does not supply."),
 ("how much conversion occurs in a given interval",
  "EK 5.1.A.1 defines kinetics as the rate at which an amount of reactants is converted to products per unit of time, so the quantity is a change divided by the interval in which it happened."),
 ("catalysts are named among the factors",
  "EK 5.1.A.3 lists catalysts among the factors that influence the rate of a reaction. Not being consumed says nothing about whether a species affects the speed."),
 ("the two catalysts did not influence it equally",
  "Recomputed in q18 above. EK 5.1.A.3 names catalysts among the influences on rate; every catalyzed trial is faster than the uncatalyzed one and the two catalyzed times differ from each other."),
 ("0.30 moles per liter per second",
  "Recomputed in a19. EK 5.1.A.2 makes the rates determined by the coefficients: six water molecules form per five oxygen molecules consumed."),
 ("agrees with the rate of formation of B",
  "EK 5.1.A.2 makes the several rates of one reaction unequal and fixed by the coefficients. Dividing each by its own coefficient gives a single number describing the reaction rather than one species."),
 ("wider beaker",
  "EK 5.1.A.3 names reactant concentrations, temperature, surface area and catalysts. For a reaction between two dissolved species, changing the shape of the vessel alters none of them."),
 ("0.0030 moles per liter per second",
  "Recomputed in a22. EK 5.1.A.1 makes the average rate the concentration change divided by the time taken."),
 ("The first, by a factor of two",
  "Recomputed in a23. EK 5.1.A.1 makes each average rate its own change over its own interval, and the two quotients are then compared directly."),
 ("Energy released and rate are separate questions",
  "EK 5.1.A.1 defines the rate as an amount converted per unit of time, and EK 5.1.A.3 lists what influences it. The energy change of a reaction appears on neither statement."),
 ("The rate for O2",
  "EK 5.1.A.2 makes the rates stand in the ratio of the coefficients, so the species with the smallest coefficient changes concentration most slowly. In this equation that is the oxygen."),
 ("0.060 moles per liter per second",
  "Recomputed in a26. EK 5.1.A.2 makes the rates determined by the stoichiometry: one oxygen molecule forms per four nitrogen dioxide molecules."),
 ("same reactant concentrations and the same physical form",
  "EK 5.1.A.3 names several separate influences on rate, so attributing an observed difference to temperature requires every other named factor to be held constant across the trials."),
 ("divided by its own coefficient",
  "EK 5.1.A.2 makes the rates of change determined by the stoichiometry in the balanced equation, so dividing each measured rate by that species' coefficient yields one value common to them all."),
 ("many smaller pieces of the same total mass",
  "EK 5.1.A.3 names surface area as a factor influencing the rate. Dividing a fixed mass increases the exposed area while leaving the amount of reactant unchanged."),
 ("fallen to zero there",
  "EK 5.1.A.1 defines the rate as the amount converted per unit of time. A concentration that is no longer changing means no further amount is converted in each interval."),
]


def _wreck_decomp(mod, cl):
    """Module-specific control: make the later interval lose more, not less."""
    t = mod.QUESTIONS[5]["table"]
    mod.QUESTIONS[5]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "0.050"] if r[0] == "400" else list(r) for r in t["rows"]])


def _wreck_factors(mod, cl):
    """Module-specific control: remove the one temperature contrast in the table.

    Setting trial 4 to a DIFFERENT non-25 temperature does not work -- the check
    asks whether a pair differs in temperature at fixed form, and 35 differs
    just as 45 does. The corruption has to remove the contrast, which is what
    running the control taught.
    """
    t = mod.QUESTIONS[11]["table"]
    mod.QUESTIONS[11]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], r[1], "25", r[3]] if r[0] == "4" else list(r) for r in t["rows"]])


def _wreck_timing(mod, cl):
    """Module-specific control: flatten the timing difference q12's key quotes."""
    t = mod.QUESTIONS[11]["table"]
    mod.QUESTIONS[11]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], r[1], r[2], "60"] if r[0] == "4" else list(r) for r in t["rows"]])


def _wreck_catalyst(mod, cl):
    """Module-specific control: make the two catalyzed trials identical."""
    t = mod.QUESTIONS[17]["table"]
    mod.QUESTIONS[17]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], r[1], "35"] if r[0] == "C" else list(r) for r in t["rows"]])


def _wreck_stem_number(mod, cl):
    """Module-specific control: key a stoichiometric ratio to the inverted value."""
    mod.QUESTIONS[1]["choices"][0] = "0.160 moles per liter per second"


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH,
                extra=[("a concentration cell corrupted", _wreck_decomp),
                       ("a temperature cell corrupted", _wreck_factors),
                       ("a completion-time cell corrupted", _wreck_timing),
                       ("a catalyst timing cell corrupted", _wreck_catalyst),
                       ("a key inverted against its coefficients", _wreck_stem_number)])

hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
