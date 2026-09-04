"""Key audit for AP CHEMISTRY 5.10 Multistep Reaction Energy Profile.

One ``(anchor, claim)`` per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EK 5.10.A.1  Knowledge of the energetics of each elementary reaction in a
             mechanism allows for the construction of an energy profile for a
             multistep reaction.                                (every item)
EK 5.6.A.3   supplies each step's activation energy as the difference between
             ITS OWN starting point and its transition state.
             (items 2, 4, 5, 7, 8, 10, 12, 16, 17, 22, 23, 26, 27, 28)
EK 5.7.A.1/.2/.3  supply the sequence of steps, the alignment with the overall
             equation, and the intermediate between two steps.
             (items 3, 11, 14, 15, 29, 30)
EK 5.6.A.4 / EK 5.8.A.1  supply which step limits the rate. (items 7, 8, 12)

THE PROFILE IS A TABLE, AND THE TABLE IS RECOMPUTED. Every profile here is the
energy at each named point along the coordinate, in the order the points are
passed. From that, three quantities are subtraction and nothing else:

    activation energy of step i = its transition state - the minimum before it
    energy change of step i     = the minimum after it - the minimum before it
    overall energy change       = the last point - the first point

``profile`` reads the tabulated points, checks that maxima and minima alternate
starting and ending at a minimum, and returns those three lists. So an item
asking which step is rate limiting is settled by comparing recomputed barriers,
not by the author's memory of the picture.

THE SIGN IS THE LIKELIEST DEFECT, so every energy-change check asserts the
DIRECTION word -- released against absorbed -- from a signed difference, and
requires the swapped-direction option to be present among the distractors. A key
with the sign backwards passes a magnitude check and fails this one.

NO FIGURE LANGUAGE, and NO CATALYST: how a catalyst changes a profile is 5.11's
material, so ``no_catalyst`` keeps it out of this module's stems and keys.

NEGATIVE CONTROL: ``python3 verify_h5_10.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h5_10

ENERGY = "Energy (kJ/mol)"

_FIGURE = re.compile(
    r"(?<![a-z])(as shown|shown below|shown above|figure|image|picture|sketch|"
    r"depicted|pictured|illustrated|"
    r"(?:diagram|graph|profile|curve|plot|chart)s?\s+(?:above|below))(?![a-z])",
    re.I)
_CATALYST = re.compile(r"(?<![A-Za-z])catalys(?:t|ts|is|ed|e|ing)(?![A-Za-z])", re.I)


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, but every profile here "
                f"is a table of energies -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every profile is carried as a table of energies "
          "at named points along the reaction coordinate.")


def no_catalyst(module):
    """5.11 owns the catalyst; a key here must not depend on one."""
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = _CATALYST.search(item["choices"][item["ans"]])
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the key turns on {hit.group(0)!r}, which is EK "
            f"5.11.A.1's material rather than this topic's"
        )
    print(f"OK  {module.TOPIC[0]} scope: no key turns on a catalyst, which belongs to 5.11.")


# --------------------------------------------------------- the profile arithmetic

def profile(table):
    """The tabulated points as ``(labels, energies, barriers, step changes)``.

    The points must alternate minimum, maximum, minimum, ... and both end on a
    minimum, which is what an assembled multistep profile looks like under EK
    5.10.A.1. A table that did not alternate would make "the barrier of step i"
    meaningless, so it is asserted rather than assumed.
    """
    labels = cg.labels(table)
    energies = cg.col(table, ENERGY)
    assert len(energies) % 2 == 1 and len(energies) >= 5, (
        f"a multistep profile needs an odd number of points, at least five: {labels}"
    )
    for i in range(1, len(energies) - 1):
        if i % 2:
            assert energies[i] > energies[i - 1] and energies[i] > energies[i + 1], (
                f"{labels[i]} at {energies[i]} is not a maximum between its neighbours"
            )
        else:
            assert energies[i] < energies[i - 1] and energies[i] < energies[i + 1], (
                f"{labels[i]} at {energies[i]} is not a minimum between its neighbours"
            )
    minima = energies[0::2]
    maxima = energies[1::2]
    barriers = [maxima[i] - minima[i] for i in range(len(maxima))]
    changes = [minima[i + 1] - minima[i] for i in range(len(maxima))]
    return labels, energies, barriers, changes


def _direction(value):
    return "released" if value < 0 else "absorbed"


def show_energy(item, value, unit="kJ/mol"):
    """A signed energy change: magnitude AND direction, with the swap required."""
    assert value != 0, "a zero change has no direction to state"
    word = _direction(value)
    h.shows(item, f"{abs(value):g} {unit} is {word}")
    other = "absorbed" if word == "released" else "released"
    swapped = [i for i, c in enumerate(item["choices"])
               if i != item["ans"] and cg.contains_phrase(c, f"{abs(value):g} {unit} is {other}")]
    assert swapped, (
        "the swapped-direction distractor is missing; an item about the sign of an energy "
        "change must offer the wrong sign as an option"
    )
    return word


def barrier_item(table, item, step):
    labels, energies, barriers, _ = profile(table)
    assert 1 <= step <= len(barriers), f"step {step} is out of range for {labels}"
    ea = barriers[step - 1]
    h.shows(item, f"{ea:g} kJ/mol")
    return (f"the tabulated {labels[2 * step - 1]} at {energies[2 * step - 1]:g} less the "
            f"{labels[2 * step - 2]} at {energies[2 * step - 2]:g} gives a barrier of "
            f"{ea:g} kJ/mol; the barriers of the steps are {barriers}")


def overall_item(table, item):
    labels, energies, _, changes = profile(table)
    value = energies[-1] - energies[0]
    word = show_energy(item, value)
    return (f"the tabulated {labels[-1]} at {energies[-1]:g} less the {labels[0]} at "
            f"{energies[0]:g} gives {value:+g} kJ/mol, so energy is {word}; the step "
            f"changes {changes} sum to the same figure")


def limiting_item(table, item, step, anchor):
    labels, _, barriers, _ = profile(table)
    biggest = max(range(len(barriers)), key=lambda i: barriers[i]) + 1
    assert barriers.count(max(barriers)) == 1, (
        f"the barriers {barriers} are tied, so no step is uniquely rate limiting"
    )
    assert biggest == step, f"the largest tabulated barrier belongs to step {biggest}"
    h.shows(item, anchor)
    return (f"the barriers recomputed from each step's own starting point are {barriers}, "
            f"whose single largest belongs to step {biggest}")


def step_change_item(table, item, step):
    labels, energies, _, changes = profile(table)
    value = changes[step - 1]
    word = show_energy(item, value)
    return (f"the tabulated minimum after step {step} less the minimum before it gives "
            f"{value:+g} kJ/mol, so energy is {word}; the step changes are {changes}")


# ---------------------------------------------------------------- table items

def q4(table, item):
    return barrier_item(table, item, 1)


def q5(table, item):
    return barrier_item(table, item, 2)


def q6(table, item):
    return overall_item(table, item)


def q7(table, item):
    return limiting_item(table, item, 1, "first, because its climb from its own starting point")


def q8(table, item):
    return limiting_item(table, item, 2, "second, because its climb from the intermediate")


def q9(table, item):
    return overall_item(table, item)


def q10(table, item):
    return barrier_item(table, item, 1)


def q11(table, item):
    labels, energies, barriers, _ = profile(table)
    troughs = [labels[i] for i in range(2, len(labels) - 1, 2)]
    assert len(troughs) == len(barriers) - 1 == 2, (
        f"the tabulated profile shows troughs {troughs} against {len(barriers)} steps"
    )
    h.shows(item, "Two, one in each trough")
    return (f"the tabulated points alternate, leaving {len(troughs)} troughs {troughs} between "
            f"{len(barriers)} transition states")


def q12(table, item):
    return limiting_item(table, item, 2, "second, whose climb from the first intermediate")


def q13(table, item):
    return overall_item(table, item)


def q17(table, item):
    labels, energies, barriers, _ = profile(table)
    reverse = energies[1] - energies[2]
    assert reverse != barriers[0], "the forward and reverse barriers must differ here"
    h.shows(item, f"{reverse:g} kJ/mol")
    return (f"the tabulated first transition state at {energies[1]:g} less the intermediate at "
            f"{energies[2]:g} gives a reverse barrier of {reverse:g} kJ/mol, against "
            f"{barriers[0]:g} forward")


def q19(table, item):
    return step_change_item(table, item, 1)


def q20(table, item):
    return step_change_item(table, item, 2)


TABLE_CHECKS = {4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11,
                12: q12, 13: q13, 17: q17, 19: q19, 20: q20}


CLAIMS = [
 ("energetics of each elementary reaction in the mechanism",
  "EK 5.10.A.1, near verbatim: knowledge of the energetics of each elementary reaction in a mechanism allows for the construction of an energy profile for a multistep reaction."),
 ("Two, one transition state for each elementary step",
  "EK 5.10.A.1 builds the profile from each elementary reaction, and EK 5.6.A.3 gives each one transition state between its own ends."),
 ("reaction intermediate, which the first step forms and the second consumes",
  "EK 5.7.A.3 makes an intermediate a species produced by some steps and consumed by others, and EK 5.10.A.1 assembles the profile from those steps in sequence."),
 ("110 kJ/mol",
  "EK 5.6.A.3's activation energy measured from the step's own starting point, recomputed in q4 from the tabulated profile."),
 ("50 kJ/mol",
  "EK 5.6.A.3's activation energy for the SECOND step, which starts from the intermediate under EK 5.7.A.3. Recomputed in q5."),
 ("20 kJ/mol is released",
  "The learning objective's overall energy change, recomputed with its sign in q6, which also requires the swapped-direction distractor to be present."),
 ("first, because its climb from its own starting point",
  "EK 5.6.A.3 measures each barrier from its own starting point and EK 5.8.A.1 makes the slowest step rate limiting. Recomputed in q7, which checks the largest barrier is unique."),
 ("second, because its climb from the intermediate",
  "The same comparison on a second tabulated profile, recomputed in q8, where the later step carries the larger barrier."),
 ("10 kJ/mol is absorbed",
  "EK 5.10.A.1's assembled profile makes the overall change the difference between its ends; recomputed with its sign in q9."),
 ("60 kJ/mol",
  "EK 5.6.A.3's activation energy for the first step of the second tabulated profile, recomputed in q10."),
 ("Two, one in each trough",
  "EK 5.7.A.3's intermediates appear as the troughs between successive transition states; counted from the tabulated points in q11."),
 ("second, whose climb from the first intermediate",
  "EK 5.6.A.3's barriers measured from each step's own starting point, recomputed and compared across three steps in q12."),
 ("10 kJ/mol is absorbed",
  "EK 5.10.A.1's assembled profile runs between the same two ends however many steps lie between; recomputed with its sign in q13."),
 ("says nothing about the energetics of the individual elementary steps",
  "EK 5.10.A.1 makes knowledge of each elementary reaction's energetics what allows the construction, and EK 5.7.A.2 leaves the overall equation as only the sum of the steps."),
 ("same two endpoints",
  "EK 5.7.A.2 makes every acceptable mechanism combine to the same overall equation, so EK 5.10.A.1's assembled profiles share their ends while differing in what lies between."),
 ("From the intermediate up to the second transition state",
  "EK 5.6.A.3 makes a step's activation energy the difference between the reactants OF THAT STEP and its transition state, and the second step begins at EK 5.7.A.3's intermediate."),
 ("80 kJ/mol",
  "EK 5.6.A.3 names its difference the activation energy for the FORWARD reaction, so the reverse of a step is the climb from that step's own products back to the same transition state. Recomputed in q17."),
 ("energy change of the first elementary step alone",
  "EK 5.10.A.1 assembles the profile from each elementary reaction, and the first step runs from the reactants to the intermediate."),
 ("30 kJ/mol is absorbed",
  "The first step's own energy change, recomputed with its sign in q19."),
 ("50 kJ/mol is released",
  "The second step's own energy change, recomputed with its sign in q20."),
 ("They add up to it",
  "EK 5.10.A.1 assembles one profile from successive elementary reactions, so their rises and falls run end to end between the same two points."),
 ("One of the transition states, which one depending on the mechanism",
  "EK 5.10.A.1 builds the profile from separate elementary reactions, each contributing a transition state under EK 5.6.A.3, and nothing fixes which stands highest."),
 ("measured from its own starting point, whether that is the reactants or an intermediate",
  "EK 5.6.A.3 defines the activation energy as a difference from the reactants OF THAT ELEMENTARY REACTION, and EK 5.10.A.1 assembles the profile out of those pieces."),
 ("intermediate lies above the reactants and the products lie below",
  "EK 5.10.A.1 assembles the profile in sequence, so an uphill first step raises the intermediate and a larger downhill second step carries the products below the start."),
 ("activation energy and the energy change of that step",
  "EK 5.10.A.1 makes those energetics what the profile is built from, and EK 5.6.A.3 with topic 5.6's learning objective names the two quantities an elementary reaction's profile carries."),
 ("activation energy of either step",
  "EK 5.6.A.3 makes an activation energy a difference involving a transition state, which lies between the ends, while the overall change is a property of the ends alone."),
 ("equally far above their own starting points",
  "EK 5.6.A.3 makes each activation energy a difference from that step's own starting point, and EK 5.10.A.1 places those starting points at different heights."),
 ("As the number of maxima",
  "EK 5.10.A.1 constructs the profile from each elementary reaction and EK 5.6.A.3 gives each one a single transition state."),
 ("unchanged, because the two ends of the profile are the same",
  "EK 5.7.A.2 makes every acceptable mechanism combine to the same overall equation, and EK 5.10.A.1's profile runs between that equation's two ends."),
 ("separate barrier and a separate energy change for each elementary step",
  "EK 5.10.A.1 builds the multistep profile out of the energetics of each elementary reaction, and EK 5.7.A.3's intermediates appear between them."),
]


def _extra_mutations():
    def sign_flipped(mod, cl):
        """The tabulated products raised above the reactants while the key still says released."""
        t = mod.QUESTIONS[5]["table"]
        mod.QUESTIONS[5]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "60"] if r[0] == "Products" else list(r) for r in t["rows"]])

    def swap_option_removed(mod, cl):
        mod.QUESTIONS[5]["choices"][1] = "The overall change cannot be found from the table"

    def barrier_key_wrong(mod, cl):
        """The keyed barrier measured from the wrong starting point."""
        mod.QUESTIONS[4]["choices"][0] = (
            "80 kJ/mol, the rise from the intermediate to the second transition state")
        cl[4] = ("80 kJ/mol", cl[4][1])

    def profile_not_alternating(mod, cl):
        """A tabulated intermediate raised above its neighbouring maximum."""
        t = mod.QUESTIONS[3]["table"]
        mod.QUESTIONS[3]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "160"] if r[0] == "Intermediate" else list(r) for r in t["rows"]])

    def barriers_tied(mod, cl):
        """The two tabulated barriers made equal, so no step is uniquely limiting."""
        t = mod.QUESTIONS[6]["table"]
        mod.QUESTIONS[6]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "180"] if r[0] == "Second transition state" else list(r)
                  for r in t["rows"]])

    def catalyst_creeps_in(mod, cl):
        mod.QUESTIONS[1]["choices"][mod.QUESTIONS[1]["ans"]] = (
            "Two, unless a catalyst provides a path with fewer maxima")
        cl[1] = ("unless a catalyst provides a path", cl[1][1])
        no_catalyst(mod)

    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "What does the profile above allow you to construct?"
        no_figure_language(mod)

    return [("the tabulated products moved above the reactants, so the keyed direction is wrong",
             sign_flipped),
            ("the swapped-direction option removed from a sign item", swap_option_removed),
            ("a barrier keyed from the wrong starting point", barrier_key_wrong),
            ("a tabulated intermediate raised above its neighbouring maximum",
             profile_not_alternating),
            ("two barriers tied, so no step is uniquely rate limiting", barriers_tied),
            ("a key turning on a catalyst, which is 5.11's material", catalyst_creeps_in),
            ("a stem pointing at a profile the bank cannot show", figure_language)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h5_10, CLAIMS, table_checks=TABLE_CHECKS, mutations=_extra_mutations())

no_figure_language(h5_10)
no_catalyst(h5_10)
h.run(h5_10, CLAIMS, table_checks=TABLE_CHECKS)
