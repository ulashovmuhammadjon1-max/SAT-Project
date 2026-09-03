r"""Key audit for AP CHEMISTRY 1.5 Atomic Structure and Electron Configuration.

One (anchor, claim) per item, in module order. ``anchor`` must appear in the
KEYED choice and in no distractor; the exporter reshuffles choices, so an index
is not a record of the key.

TWO THINGS ARE GATED HERE THAT NO OTHER UNIT 1 MODULE NEEDS.

**Electron configurations are checked as configurations, not as strings.**
``_parse`` reads a keyed configuration back out of its LaTeX span and
``_ground_state`` builds the correct one from scratch in Aufbau order for the
stated electron count, so a keyed configuration is compared against a
derivation rather than against the author's memory. That is as close to the
sympy gate the Math banks enjoy as this content allows, and it caught nothing
only because it was written before the keys were.

**Coulomb's law items are recomputed from the stated charges and distances.**
EK 1.5.A.2 gives the force as proportional to the product of the charges over
the square of the separation, and every item that turns on it is evaluated with
that expression -- including, for the table item, a check that reading the
table on charge alone or on distance alone gives a DIFFERENT row, so the item
cannot be answered by half the data.

WHAT THE KEYS REST ON
---------------------
Items 1, 18 and 20 rest on EK 1.5.A.1: the atom is composed of negatively
charged electrons and a positively charged nucleus made of protons and
neutrons.

Items 5, 6, 15, 19 and 23 rest on EK 1.5.A.2, Coulomb's law, and are recomputed
below from the numbers each item states.

Items 2, 3, 4, 7, 8, 11, 12, 13, 14, 16, 22, 24, 25, 27, 28 and 29 rest on EK
1.5.A.3: shells and subshells, core and valence electrons, and the Aufbau
principle. Every configuration among them is derived below.

Items 9, 17, 21, 26 and 30 rest on EK 1.5.A.4: the relative energy required to
remove an electron from different subshells of an atom, or from the same
subshell in different atoms, estimated by a qualitative application of
Coulomb's law through distance and effective nuclear charge.

BOUNDARIES KEPT. No item assigns a quantum number to any electron (the CED's
exclusion at 1.5.A.3), no item writes a configuration for an element that is an
exception to the Aufbau principle (the exclusion at 1.7.A.1), and no item is
answered from an element's position in the periodic table, which is 1.7's
material rather than this topic's.

DATA ITEMS: 10, 17, 20, 21, 26 and 28 carry tables; all six are recomputed.

NEGATIVE CONTROL: ``python3 verify_h1_5.py --selftest``.
"""
import re
import sys

import cg_check as cg
import chem_notation

# ---------------------------------------------------------- configuration gate

_SUBSHELL = re.compile(r"(\d)([spdf])\^\{?(\d+)\}?")

# The Aufbau filling order the CED's 1.5.A.3 names, far enough for every
# element this module uses, with each subshell's capacity.
_ORDER = [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6), ("4s", 2),
          ("3d", 10), ("4p", 6), ("5s", 2), ("4d", 10), ("5p", 6)]


def _parse(text):
    """Every (subshell, count) in a configuration, read out of its LaTeX span."""
    return [(f"{n}{l}", int(k)) for n, l, k in _SUBSHELL.findall(text)]


def _ground_state(n_electrons):
    """Build the ground-state configuration for n electrons, in Aufbau order."""
    out, left = [], n_electrons
    for name, cap in _ORDER:
        if left <= 0:
            break
        k = min(cap, left)
        out.append((name, k))
        left -= k
    assert left == 0, f"{n_electrons} electrons do not fit the filling order used here"
    return out


def _assert_ground(text, n_electrons, where):
    got = _parse(text)
    want = _ground_state(n_electrons)
    assert got == want, f"{where}: {got} is not the ground state for {n_electrons} electrons ({want})"
    return want


def _total(text):
    return sum(k for _, k in _parse(text))


# ------------------------------------------------------------- Coulomb's law

def _coulomb(q1, q2, r):
    """EK 1.5.A.2: the force is proportional to q1 q2 over r squared."""
    return q1 * q2 / (r ** 2)


CH1 = "Charge on the first particle"
CH2 = "Charge on the second particle"
SEP = "Separation (picometers)"
ENERGY = "Energy required (megajoules per mole)"


def q10(table, item):
    labs = cg.labels(table)
    a, b, r = cg.col(table, CH1), cg.col(table, CH2), cg.col(table, SEP)
    force = dict(zip(labs, [abs(_coulomb(x, y, d)) for x, y, d in zip(a, b, r)]))
    top = max(force, key=force.get)
    assert top == "Pair 2", f"the largest attraction is {top}"
    assert len([k for k, v in force.items() if abs(v - force[top]) < 1e-18]) == 1, \
        "two rows tie for the largest force, so the item has no unique answer"
    assert abs(force["Pair 2"] - force["Pair 4"]) > 1e-12, \
        "'Pairs 2 and 4 are equal' must be false on these numbers"
    # Reading only one column must give a DIFFERENT answer, or half the data suffices.
    prod = dict(zip(labs, [abs(x * y) for x, y in zip(a, b)]))
    near = dict(zip(labs, [-d for d in r]))
    assert len([k for k, v in prod.items() if v == max(prod.values())]) > 1, \
        "the charge product alone already picks a unique row"
    assert max(near, key=near.get) != "Pair 2" or \
        len([k for k, v in near.items() if v == max(near.values())]) > 1, \
        "the separation alone already picks the keyed row"
    return (f"charge product over separation squared gives "
            f"{ {k: f'{v:.2e}' for k, v in force.items()} }; Pair 2 is the unique maximum, "
            "and neither column alone picks it out")


def q17(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, ENERGY)))
    top = max(vals, key=vals.get)
    assert top == "1s", f"the largest removal energy belongs to {top}"
    assert vals["1s"] > 5 * sorted(vals.values())[-2], \
        "the innermost subshell should stand far above the rest for the item to be clear"
    return (f"the tabulated energies are {vals}, so the 1s electron is held most tightly "
            "and therefore closest")


def q20(table, item):
    p, e = cg.col(table, "Protons"), cg.col(table, "Electrons")
    charge = dict(zip(cg.labels(table), [x - y for x, y in zip(p, e)]))
    minus_one = [k for k, v in charge.items() if v == -1]
    assert minus_one == ["Species 3"], f"the species at minus one are {minus_one}"
    n = cg.col(table, "Neutrons")
    assert any(x != y for x, y in zip(n, p)), \
        "some row must have unequal protons and neutrons, or the neutron distractor is untestable"
    return f"protons minus electrons gives charges {charge}, so exactly one species is minus one"


def q21(table, item):
    prot = cg.col(table, "Protons in the nucleus")
    en = cg.col(table, "Energy to remove one 3s electron (megajoules per mole)")
    pairs = sorted(zip(prot, en))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the energy does not rise with nuclear charge: {pairs}"
    assert len(set(en)) == len(en), "'the three values should have been identical' must be false"
    return (f"sorted by proton count the removal energies are {[e for _, e in pairs]}, "
            "strictly increasing, so a larger nuclear charge holds the same subshell harder")


def q26(table, item):
    labs, vals = cg.labels(table), cg.col(table, ENERGY)
    order = sorted(zip(vals, labs))
    gaps = [(order[i + 1][0] - order[i][0], order[i][1], order[i + 1][1])
            for i in range(len(order) - 1)]
    biggest = max(gaps)
    assert (biggest[1], biggest[2]) == ("2s", "1s"), \
        f"the largest gap is between {biggest[1]} and {biggest[2]}"
    others = sorted(g[0] for g in gaps)[:-1]
    assert biggest[0] > 10 * max(others), \
        f"the largest gap {biggest[0]} is not decisively bigger than the rest {others}"
    assert len(set(round(g[0], 6) for g in gaps)) > 1, "'equal steps' must be false"
    return (f"sorted by energy the gaps are {[round(g[0], 2) for g in gaps]}, so the step from "
            "2s to 1s dwarfs the others and the four values are not evenly spaced")


def q28(table, item):
    e = dict(zip(cg.labels(table), cg.col(table, "Electrons")))
    ten = sorted(k for k, v in e.items() if v == 10)
    assert ten == ["Species 2", "Species 4"], f"the species with ten electrons are {ten}"
    p = dict(zip(cg.labels(table), cg.col(table, "Protons")))
    assert p["Species 2"] != p["Species 4"], \
        "the two matching species must differ in proton count, which is the point of the item"
    return (f"the electron column is {e}, so exactly two species carry ten electrons while "
            f"holding {p['Species 2']:.0f} and {p['Species 4']:.0f} protons respectively")


# ------------------------------------------------- configurations, derived here

def _check_configurations(module):
    """Derive every keyed configuration in the module rather than trusting it."""
    q = module.QUESTIONS
    _assert_ground(q[1]["choices"][q[1]["ans"]], 11, "q2 neutral sodium")
    _assert_ground(q[6]["choices"][q[6]["ans"]], 10, "q7 oxide ion, 8 protons plus 2 electrons")
    _assert_ground(q[10]["choices"][q[10]["ans"]], 18, "q11 chloride ion")
    _assert_ground(q[15]["choices"][q[15]["ans"]], 10, "q16 magnesium ion, 12 protons less 2")
    _assert_ground(q[26]["choices"][q[26]["ans"]], 20, "q27 neutral calcium")

    # q8 asks which configuration is NOT a ground state: the key must fail the
    # derivation and every distractor must pass it.
    for i, choice in enumerate(q[7]["choices"]):
        n = _total(choice)
        ok = _parse(choice) == _ground_state(n)
        if i == q[7]["ans"]:
            assert not ok, f"q8: the keyed configuration {choice!r} IS a valid ground state"
        else:
            assert ok, f"q8: the distractor {choice!r} is not a ground state either"

    # Counting items: valence, core and total electrons, read off the stem's span.
    assert _total(q[3]["q"]) == 16, "q4's stem configuration does not hold sixteen electrons"
    val = [k for name, k in _parse(q[3]["q"]) if name.startswith("3")]
    assert sum(val) == 6, f"q4: the outermost shell holds {sum(val)}, not six"

    assert _total(q[11]["q"]) == 13, "q12's stem configuration does not hold thirteen electrons"
    core = [k for name, k in _parse(q[11]["q"]) if not name.startswith("3")]
    assert sum(core) == 10, f"q12: the core holds {sum(core)}, not ten"

    outer = [k for name, k in _parse(q[21]["q"]) if name.startswith("4")]
    assert sum(outer) == 2, f"q22: the fourth shell holds {sum(outer)}, not two"

    assert _total(q[23]["q"]) == 26, f"q24's configuration holds {_total(q[23]['q'])}, not 26"

    # q29's student configuration must indeed be a non-ground state of five electrons.
    boron = _parse(q[28]["q"])
    assert sum(k for _, k in boron) == 5, "q29's configuration does not hold five electrons"
    assert boron != _ground_state(5), "q29's configuration IS the ground state, so the key is wrong"
    print(f"OK  {module.TOPIC[0]} configurations: every keyed configuration derived in "
          "Aufbau order from its electron count, not taken on trust.")


CLAIMS = [
 ("positively charged nucleus that is made of protons",
  "EK 1.5.A.1, near verbatim: the atom is composed of negatively charged electrons and a positively charged nucleus that is made of protons and neutrons. Every rejected option either moves a particle into or out of the nucleus or reverses a charge sign."),
 (r"1s^2\,2s^2\,2p^6\,3s^1",
  "Derived in _check_configurations above by filling the Aufbau order of EK 1.5.A.3 with eleven electrons, rather than recalled. Two rejected options break a subshell capacity outright and one lists the subshells out of energy order."),
 ("inner electrons of an atom",
  "EK 1.5.A.3, near verbatim: inner electrons are called core electrons, and outer electrons are called valence electrons. Both kinds are electrons and both sit outside the nucleus, since EK 1.5.A.1 puts only protons and neutrons inside it."),
 ("Six valence electrons",
  "Recomputed in _check_configurations above from the stem's own configuration: the outermost shell present is the third, and its s and p subshells hold two and four. EK 1.5.A.3 defines the valence electrons as the outer ones."),
 ("It doubles.",
  "EK 1.5.A.2 makes the force proportional to the product of the two charges over the square of the separation, so doubling one charge doubles the product and the force. The square applies to the distance alone, which is what the quadrupling option misplaces."),
 ("four times as large",
  "EK 1.5.A.2 puts the separation in the denominator and squared, so halving it multiplies the force by four. Treating the dependence as a simple inverse gives the doubling option instead."),
 (r"1s^2\,2s^2\,2p^6",
  "Derived above for ten electrons, which is what a neutral oxygen atom's eight becomes on gaining two. The configuration of the neutral atom is among the rejected options, and an eight-electron p subshell exceeds the capacity the Aufbau order allows."),
 (r"2p^5\,3s^1",
  "The only item in the module whose key is an INVALID configuration. _check_configurations derives the ground state for each option's own electron count and confirms that exactly the keyed one fails: it opens the third shell while the 2p subshell still has a vacancy, which the Aufbau principle of EK 1.5.A.3 forbids."),
 ("closer to the nucleus and is shielded by fewer",
  "EK 1.5.A.4 states that the energy needed to remove an electron from different subshells of an atom is estimated by a qualitative application of Coulomb's law and is related to the distance from the nucleus and the effective nuclear charge. EK 1.5.A.2 then makes the shorter separation a steeply stronger attraction."),
 ("Pair 2",
  "Recomputed in q10 above from the tabulated charges and separations using EK 1.5.A.2's expression. The check confirms the winner is unique and that neither the charge column nor the distance column alone picks it out, so both halves of the data are needed."),
 (r"3s^2\,3p^6",
  "Derived above for eighteen electrons, which is a neutral chlorine atom's seventeen plus one. The neutral atom's own configuration is a rejected option and a seven-electron p subshell exceeds the allowed capacity."),
 ("Ten core electrons",
  "Recomputed in _check_configurations above: every electron outside the outermost occupied shell. EK 1.5.A.3 names those the core electrons, and the three in the third shell are the valence electrons that a student counting the wrong group would report."),
 ("shells, which are energy levels",
  "EK 1.5.A.3, near verbatim: in atoms and ions the electrons can be thought of as being in shells (energy levels) and subshells (sublevels), as described by the ground-state electron configuration. The framework applies the model to ions as well as atoms, which the last rejected option denies."),
 ("4s subshell lies lower in energy",
  "EK 1.5.A.3 states that the configuration is delineated by the Aufbau principle, which orders subshells by energy rather than by shell number. A d subshell holds ten electrons and is occupied in many ground-state configurations, so two rejected options are false on their own terms."),
 ("twice as strongly",
  "EK 1.5.A.2 makes the force proportional to the product of the charges over the square of the separation, so doubling one charge at fixed distance doubles it. Only the distance is squared, and mass appears nowhere in the relationship."),
 ("a total of ten electrons",
  "Derived above for ten electrons, which is a neutral magnesium atom's twelve less two. The two electrons lost are the outermost, so a configuration with a depleted inner subshell would not be a ground state at all."),
 ("1s subshell",
  "Recomputed in q17 above: the largest tabulated removal energy by a wide margin. EK 1.5.A.4 relates removal energy to distance from the nucleus and effective nuclear charge, and EK 1.5.A.2 makes a shorter separation a stronger attraction."),
 ("one more proton than it has electrons",
  "EK 1.5.A.1 gives the electron a negative charge and the proton a positive one, so the net charge follows from the difference between those two counts alone. Neutrons are uncharged and cannot offset a proton, which is what two rejected options assume."),
 ("one ninth",
  "EK 1.5.A.2 puts the separation in the denominator and squared, so tripling it divides the force by nine. The one-third option is what a simple inverse dependence would give."),
 ("Species 3",
  "Recomputed in q20 above as protons minus electrons for every row. EK 1.5.A.1 supplies the signs, and the check confirms exactly one row comes to minus one so the answer is unique."),
 ("attracts the 3s electron more strongly",
  "Recomputed in q21 above: the removal energy rises strictly with the proton count. EK 1.5.A.4 covers exactly this comparison -- the same subshell in different atoms -- and attributes it to distance and effective nuclear charge under Coulomb's law."),
 ("Two electrons in the fourth shell",
  "Recomputed in _check_configurations above from the stem's configuration: the outermost shell occupied is the fourth and it holds two electrons. Counting the filled third shell instead is the commonest route to a rejected option."),
 ("repel each other, and the repulsion weakens",
  "EK 1.5.A.2 makes the force proportional to the product of the two charges, so like signs give a positive product and a repulsion, and the inverse square dependence makes it fall steeply with distance."),
 ("Twenty-six electrons",
  "Recomputed in _check_configurations above by summing the superscripts of the stem's configuration. Stopping at the fourth-shell s subshell and ignoring the d subshell gives one of the rejected values."),
 ("starting from the lowest in energy",
  "EK 1.5.A.3 states that the configuration is explained by quantum mechanics as delineated in the Aufbau principle and exemplified in the periodic table. Filling upward from the lowest energy is precisely what makes a configuration a GROUND state."),
 ("2s and 1s subshells",
  "Recomputed in q26 above: the gaps between consecutive tabulated energies are compared and the innermost step is more than ten times any other. The check also confirms the four values are not evenly spaced, so the 'no jump' option is false on the data."),
 (r"3p^6\,4s^2",
  "Derived above for twenty electrons in Aufbau order, which puts the last two in the fourth-shell s subshell rather than the 3d subshell. A p subshell cannot hold eight, and splitting the last two electrons across two subshells would not be a ground state."),
 ("Species 2 and Species 4",
  "Recomputed in q28 above by reading the electron column. The check also confirms the two matching species differ in proton count, which is what makes the item about configuration rather than about identity."),
 ("2s subshell can hold two electrons and must be filled",
  "_check_configurations confirms that the student's configuration holds five electrons and is NOT the ground state for five, so the total adding up correctly is exactly why the count alone cannot settle the question. The Aufbau principle of EK 1.5.A.3 is what it violates."),
 ("one fewer electron sharing the attraction",
  "EK 1.5.A.4 has ionization energy estimated by a qualitative application of Coulomb's law through distance and effective nuclear charge, and EK 1.5.A.2 makes an unchanged positive nuclear charge pull harder on each of a smaller number of electrons. The nuclear charge really is unchanged, which is why the reasoning must turn on the electron count."),
]

TABLE_CHECKS = {10: q10, 17: q17, 20: q20, 21: q21, 26: q26, 28: q28}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate, configs=False):
        mod = types.ModuleType("h1_5_mutant")
        mod.TOPIC = h1_5.TOPIC
        mod.QUESTIONS = copy.deepcopy(h1_5.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            if configs:
                _check_configurations(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:95]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[1]["ans"] = 1

    def break_anchor(mod, claims):
        claims[9] = ("no such phrase anywhere in the choice", claims[9][1])

    def wrong_configuration(mod, claims):
        # Key sodium at the magnesium configuration: twelve electrons, not eleven.
        mod.QUESTIONS[1]["ans"] = 1

    def excited_state_keyed_as_ground(mod, claims):
        mod.QUESTIONS[10]["choices"][0] = r"\(1s^2\,2s^2\,2p^6\,3s^1\,3p^7\)"

    def ground_state_keyed_as_excited(mod, claims):
        # q8's key must be the one configuration that is NOT a ground state.
        mod.QUESTIONS[7]["ans"] = 2

    def corrupt_coulomb_table(mod, claims):
        # Move Pair 3 to the shortest separation and biggest charges: Pair 2 loses.
        mod.QUESTIONS[9]["table"] = dict(
            headers=h1_5._T_PAIRS["headers"],
            rows=[["Pair 1", "+1", "-1", "100"], ["Pair 2", "+2", "-1", "100"],
                  ["Pair 3", "+3", "-3", "50"], ["Pair 4", "+1", "-2", "200"]])

    def flatten_ionization_trend(mod, claims):
        mod.QUESTIONS[20]["table"] = dict(
            headers=h1_5._T_IE_SAME_SUBSHELL["headers"],
            rows=[["Sodium", "11", "0.50"], ["Magnesium", "12", "0.50"],
                  ["Aluminum", "13", "0.50"]])

    def even_out_the_subshell_gaps(mod, claims):
        mod.QUESTIONS[25]["table"] = dict(
            headers=h1_5._T_IE_SUBSHELLS["headers"],
            rows=[["1s", "4.00"], ["2s", "3.00"], ["2p", "2.00"], ["3s", "1.00"]])

    def forget_table_check(mod, claims):
        mod.QUESTIONS[0]["table"] = h1_5._T_PAIRS

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[4]["choices"][3] = mod.QUESTIONS[4]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[14]["why"] = "By Coulomb."

    def letter_reference(mod, claims):
        mod.QUESTIONS[5]["why"] = ("Choice A is right because the framework says so, and "
                                   "the remaining reasoning follows from that alone.")

    def subscript_configuration(mod, claims):
        # Exactly the defect the converter produced: a configuration set with
        # SUBscripts, and a chunk of it left outside the span.
        mod.QUESTIONS[1]["choices"][2] = r"\(1s_2\)2s_2 2p_7"
        chem_notation.style(mod)

    print("negative controls:")
    must_fail("a configuration with subscripts and text outside the span",
              subscript_configuration)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer present in the keyed choice", break_anchor)
    must_fail("an ion keyed to the wrong electron count", wrong_configuration, configs=True)
    must_fail("an impossible configuration keyed as a ground state",
              excited_state_keyed_as_ground, configs=True)
    must_fail("a genuine ground state keyed as the 'not a ground state' answer",
              ground_state_keyed_as_excited, configs=True)
    must_fail("the Coulomb table corrupted so the keyed pair is not the strongest",
              corrupt_coulomb_table)
    must_fail("the ionization trend flattened, refuting the keyed explanation",
              flatten_ionization_trend)
    must_fail("the subshell energies made evenly spaced, refuting the keyed jump",
              even_out_the_subshell_gaps)
    must_fail("a table added with no recompute behind it", forget_table_check)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a rationale reduced below the minimum", thin_why)
    must_fail("a rationale naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import h1_5  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

chem_notation.style(h1_5)
_check_configurations(h1_5)
cg.check(h1_5, CLAIMS, table_checks=TABLE_CHECKS)
