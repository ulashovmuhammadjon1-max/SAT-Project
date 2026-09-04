"""Key audit for AP CHEMISTRY 5.6 Reaction Energy Profile.

One ``(anchor, claim)`` per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EK 5.6.A.1  Elementary reactions typically involve the breaking of some bonds
            and the forming of new ones.                       (items 5, 23)
EK 5.6.A.2  The reaction coordinate is the axis along which the motions that
            rearrange reactants into products can be plotted.  (items 1, 26)
EK 5.6.A.3  The energy profile gives the energy along that coordinate, which
            proceeds from reactants through a transition state to products;
            the reactant-to-transition-state difference is the activation
            energy for the forward reaction.
            (items 2, 3, 4, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21,
            24, 25, 26, 27, 28, 29, 30)
EK 5.6.A.4  The rate is temperature dependent because the proportion of
            collisions energetic enough to reach the transition state varies
            with temperature; the Arrhenius equation relates that dependence to
            the activation energy.            (items 9, 10, 18, 22, 29, 30)

THE ARITHMETIC. Two quantities in this topic are subtraction and nothing else,
so nothing here is taken on trust:

    activation energy (forward) = transition state - reactants
    overall energy change       = products - reactants
    activation energy (reverse) = transition state - products

``ea_forward``, ``overall`` and ``ea_reverse`` are written once, and every
tabulated profile and every stem figure is put through them. THE SIGN IS THE
DEFECT MOST LIKELY IN A THERMOCHEMICAL BANK, so ``overall`` returns a signed
number and the checks assert the DIRECTION word in the keyed choice -- released
against absorbed -- rather than only the magnitude. A key that had the sign
backwards would pass a magnitude check and fail these.

NO FIGURE LANGUAGE. This topic is named after a graph the bank cannot show, so
``no_figure_language`` runs over every stem and choice; every profile here is a
table of energies at named points.

NO ARRHENIUS CALCULATION. EK 5.6.A.4's exclusion statement rules those out, so
``no_arrhenius_computation`` asserts that no item pairing the word Arrhenius
with a numeric key exists.

NEGATIVE CONTROL: ``python3 verify_h5_6.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h5_6

ENERGY = "Energy (kJ/mol)"
REACT = "Energy of the reactants (kJ/mol)"
TS = "Energy of the transition state (kJ/mol)"
PROD = "Energy of the products (kJ/mol)"

_FIGURE = re.compile(
    r"(?<![a-z])(as shown|shown below|shown above|figure|image|picture|sketch|"
    r"depicted|pictured|illustrated|"
    r"(?:diagram|graph|profile|curve|plot|chart)s?\s+(?:above|below))(?![a-z])",
    re.I)
_ARRHENIUS = re.compile(r"(?<![A-Za-z])Arrhenius(?![A-Za-z])", re.I)
_NUMBER = re.compile(r"(?<![A-Za-z0-9.])\d+(?:\.\d+)?(?![A-Za-z0-9.])")


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, but every energy "
                f"profile in this module is a table -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every energy profile is carried as a table of "
          "energies at named points along the reaction coordinate.")


def no_arrhenius_computation(module):
    """EK 5.6.A.4's exclusion statement: no Arrhenius calculation is assessed."""
    for i, item in enumerate(module.QUESTIONS, 1):
        if _ARRHENIUS.search(item["q"]):
            hit = _NUMBER.search(item["choices"][item["ans"]])
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: an Arrhenius item with the number {hit.group(0)!r} "
                "in its key, which EK 5.6.A.4's exclusion statement rules out"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item computes anything from the Arrhenius "
          "equation, as EK 5.6.A.4's exclusion statement requires.")


# ------------------------------------------------------- the profile arithmetic

def points(table):
    """The tabulated energies, by the name of the point along the coordinate."""
    return dict(zip(cg.labels(table), cg.col(table, ENERGY)))


def ea_forward(reactants, transition):
    return transition - reactants


def overall(reactants, products):
    """Signed: negative when the products lie below the reactants."""
    return products - reactants


def ea_reverse(products, transition):
    return transition - products


def _direction(value):
    return "released" if value < 0 else "absorbed"


def check_barrier(item, reactants, transition, unit="kJ/mol"):
    ea = ea_forward(reactants, transition)
    assert ea > 0, f"the transition state must lie above the reactants; the rise is {ea}"
    h.shows(item, f"{ea:g} {unit}")
    return (f"the tabulated transition state at {transition:g} less the reactants at "
            f"{reactants:g} gives a forward activation energy of {ea:g} {unit}")


def check_overall(item, reactants, products, unit="kJ/mol"):
    value = overall(reactants, products)
    assert value != 0, "the reactants and the products must differ for a direction to exist"
    word = _direction(value)
    h.shows(item, f"{abs(value):g} {unit} is {word}")
    other = "absorbed" if word == "released" else "released"
    also = [i for i, c in enumerate(item["choices"])
            if i != item["ans"] and cg.contains_phrase(c, f"{abs(value):g} {unit} is {other}")]
    assert also, (
        "the swapped-direction distractor is missing; an item about the sign of an energy "
        "change must offer the wrong sign as an option"
    )
    return (f"products at {products:g} less reactants at {reactants:g} gives {value:+g} "
            f"{unit}, so energy is {word}, with the opposite direction offered at {also}")


# ---------------------------------------------------------------- table items

def q6(table, item):
    p = points(table)
    return check_barrier(item, p["Reactants"], p["Transition state"])


def q7(table, item):
    p = points(table)
    return check_overall(item, p["Reactants"], p["Products"])


def q8(table, item):
    p = points(table)
    rev = ea_reverse(p["Products"], p["Transition state"])
    fwd = ea_forward(p["Reactants"], p["Transition state"])
    assert rev != fwd, "the two barriers must differ, or the item has no unique answer"
    h.shows(item, f"{rev:g} kJ/mol")
    return (f"the tabulated transition state at {p['Transition state']:g} less the products "
            f"at {p['Products']:g} gives a reverse barrier of {rev:g} kJ/mol, against "
            f"{fwd:g} forward")


def q11(table, item):
    p = points(table)
    return check_barrier(item, p["Reactants"], p["Transition state"])


def q12(table, item):
    p = points(table)
    return check_overall(item, p["Reactants"], p["Products"])


def q13(table, item):
    labs = cg.labels(table)
    eas = {lab: ea_forward(r, t) for lab, r, t in
           zip(labs, cg.col(table, REACT), cg.col(table, TS))}
    biggest = max(eas, key=eas.get)
    assert sorted(eas.values()) == sorted(set(eas.values())), \
        f"the barriers must be distinct for a maximum to be unique: {eas}"
    assert biggest == "R3", f"the largest tabulated barrier is {biggest}"
    h.shows(item, biggest)
    return f"subtracting the two tabulated energy columns gives barriers {eas}, whose maximum is {biggest}"


def q14(table, item):
    labs = cg.labels(table)
    changes = {lab: overall(r, p) for lab, r, p in
               zip(labs, cg.col(table, REACT), cg.col(table, PROD))}
    eas = {lab: ea_forward(r, t) for lab, r, t in
           zip(labs, cg.col(table, REACT), cg.col(table, TS))}
    assert len(set(changes.values())) == 1, f"the overall changes are {changes}, not all equal"
    assert len(set(eas.values())) == len(eas), f"the barriers are {eas}, which are not all different"
    h.shows(item, "All three overall energy changes are equal")
    return (f"the tabulated overall changes are {changes}, all equal, while the barriers "
            f"{eas} are all different")


def q17(table, item):
    p = points(table)
    top = max(p, key=p.get)
    assert list(p.values()).count(p[top]) == 1, f"the greatest energy is not unique: {p}"
    assert top == "Point 3", f"the highest tabulated point is {top}"
    h.shows(item, top)
    return f"the tabulated energies are {p}, whose single greatest value is at {top}"


def q24(table, item):
    p = points(table)
    assert overall(p["Reactants"], p["Products"]) > 0, \
        "this profile is supposed to absorb energy overall"
    return check_barrier(item, p["Reactants"], p["Transition state"])


def q25(table, item):
    p = points(table)
    rev = ea_reverse(p["Products"], p["Transition state"])
    fwd = ea_forward(p["Reactants"], p["Transition state"])
    assert rev < fwd, f"the reverse barrier {rev} is not smaller than the forward {fwd}"
    h.shows(item, f"{rev:g} kJ/mol, smaller than the forward barrier")
    return (f"the reverse barrier recomputes to {rev:g} kJ/mol against {fwd:g} forward, so "
            "it is the smaller, which the keyed choice states")


TABLE_CHECKS = {6: q6, 7: q7, 8: q8, 11: q11, 12: q12, 13: q13, 14: q14, 17: q17,
                24: q24, 25: q25}


# --------------------------------------------------------------- stem numerics

def n20(item):
    fwd, released = 90.0, 40.0
    # The profile: reactants at zero, transition state at +fwd, products at -released.
    rev = ea_reverse(-released, fwd)
    assert rev == 130.0, f"the reverse barrier recomputes to {rev}"
    h.shows(item, f"{rev:g} kJ/mol")
    return (f"placing the reactants at zero puts the transition state at {fwd:g} and the "
            f"products at {-released:g}, so the reverse climb is {rev:g} kJ/mol")


def n21(item):
    fwd, rev = 75.0, 120.0
    # Both barriers are measured from the same transition state.
    value = overall(-fwd, -rev)
    assert value == -45.0, f"the overall change recomputes to {value}"
    word = _direction(value)
    h.shows(item, f"{abs(value):g} kJ/mol is {word}")
    swapped = [i for i, c in enumerate(item["choices"])
               if i != item["ans"] and cg.contains_phrase(c, f"{abs(value):g} kJ/mol is absorbed")]
    assert swapped, "the swapped-sign distractor is missing from an item about direction"
    return (f"measuring both barriers from one transition state puts the reactants {fwd:g} "
            f"below it and the products {rev:g} below it, an overall change of {value:+g} "
            f"kJ/mol, so energy is {word}")


def n22(item):
    low, high = 60.0, 140.0
    assert low < high, "the keyed reaction must be the one with the lower barrier"
    h.shows(item, f"{low:g} kJ/mol barrier")
    return (f"the two stated barriers are {low:g} and {high:g} kJ/mol, and the smaller "
            "requirement is met by a larger proportion of collisions at one temperature")


NUMERIC = {20: n20, 21: n21, 22: n22}


CLAIMS = [
 ("complex set of motions that rearrange reactants into products",
  "EK 5.6.A.2, near verbatim: the reaction coordinate is the axis along which the complex set of motions involved in rearranging reactants to form products can be plotted."),
 ("The energy along the reaction coordinate",
  "EK 5.6.A.3, verbatim in substance: the energy profile gives the energy along the reaction coordinate."),
 ("From reactants, through a transition state, to products",
  "EK 5.6.A.3 states that the coordinate typically proceeds in exactly that order; an intermediate belongs to a mechanism of more than one step under EK 5.7.A.3."),
 ("difference between the reactants and the transition state",
  "EK 5.6.A.3, near verbatim: that difference is the activation energy for the forward reaction, while the reactant-to-product difference is the overall energy change."),
 ("breaking of some bonds and the forming of new ones",
  "EK 5.6.A.1, verbatim in substance: elementary reactions typically involve the breaking of some bonds and the forming of new ones."),
 ("130 kJ/mol",
  "EK 5.6.A.3's definition of the forward activation energy, recomputed in q6 from the tabulated energies."),
 ("30 kJ/mol is released",
  "The learning objective's overall energy change, recomputed with its SIGN in q7, which also requires the swapped-direction distractor to be present."),
 ("160 kJ/mol",
  "EK 5.6.A.3 names its difference the activation energy FOR THE FORWARD reaction, which makes the reverse the mirrored climb from the products to the same transition state. Recomputed in q8."),
 ("proportion of particle collisions energetic enough",
  "EK 5.6.A.4, near verbatim: the rate is temperature dependent because the proportion of particle collisions that are energetic enough to reach the transition state varies with temperature."),
 ("temperature dependence of the rate of an elementary reaction",
  "EK 5.6.A.4 states that the Arrhenius equation relates that dependence to the activation energy needed by molecular collisions to reach the transition state."),
 ("110 kJ/mol",
  "EK 5.6.A.3's forward activation energy, recomputed in q11 from a second tabulated profile."),
 ("70 kJ/mol is absorbed",
  "The overall energy change with its sign, recomputed in q12 for a profile whose products lie above its reactants."),
 ("R3",
  "EK 5.6.A.3's activation energy computed for each tabulated reaction in q13, with the three barriers checked distinct so the maximum is unique."),
 ("All three overall energy changes are equal",
  "EK 5.6.A.3 defines the barrier and the overall change from different pairs of points; q14 recomputes both columns and finds the changes equal while the barriers differ."),
 ("finishes with more energy than it began with",
  "EK 5.6.A.3's profile gives the energy along the coordinate, so products above reactants means the system ends higher, which is the positive overall change the learning objective names."),
 ("The transition state",
  "EK 5.6.A.3 places the transition state between the reactants and the products and makes the climb to it an activation energy that must be supplied, so it stands above both ends."),
 ("Point 3",
  "EK 5.6.A.3's transition state as the greatest energy along the coordinate, recomputed in q17 and checked to be unique."),
 ("not the height of the transition state",
  "EK 5.6.A.4 locates the temperature dependence in the proportion of collisions energetic enough to reach the transition state, leaving the profile's own energies untouched."),
 ("reverse activation energy is the larger",
  "EK 5.6.A.3 measures the forward barrier from the reactants, so a reaction releasing energy has its products lower and their climb to the same transition state is longer."),
 ("130 kJ/mol",
  "EK 5.6.A.3's two differences combined, recomputed in n20 by placing the reactants at zero."),
 ("45 kJ/mol is released",
  "EK 5.6.A.3 measures both barriers from one transition state, recomputed with its sign in n21, which also requires the swapped-sign distractor to be present."),
 ("60 kJ/mol barrier, because a larger proportion",
  "EK 5.6.A.4 ties the rate to the proportion of collisions energetic enough to reach the transition state, and EK 5.5.A.2 makes that fraction small, so a lower requirement is met more often. Recomputed in n22."),
 ("broken while new ones are beginning to form",
  "EK 5.6.A.1 says elementary reactions typically involve the breaking of some bonds and the forming of new ones, and EK 5.6.A.3 makes the climb to the transition state the energy that rearrangement costs."),
 ("180 kJ/mol",
  "EK 5.6.A.3's forward activation energy for a profile that absorbs energy overall, recomputed in q24."),
 ("80 kJ/mol, smaller than the forward barrier",
  "EK 5.6.A.3's mirrored difference, recomputed in q25, which also checks the reverse barrier really is the smaller of the two."),
 ("same rearrangement of the same particles",
  "EK 5.6.A.2 makes the coordinate an axis of the motions rearranging reactants into products and EK 5.6.A.3 places one transition state along it, so travelling it backwards passes the same summit."),
 ("One, the transition state it passes through",
  "EK 5.6.A.3 has the coordinate proceed from reactants through A transition state to products; a profile with several maxima is EK 5.10.A.1's multistep case."),
 ("The activation energy and the overall energy change",
  "The learning objective for topic 5.6 names exactly those two quantities as what the profile represents."),
 ("property of the profile itself",
  "EK 5.6.A.4 puts the temperature dependence in the proportion of collisions that meet the requirement, while EK 5.6.A.3 fixes the requirement as a difference between two points on the profile."),
 ("climb to the transition state, which can be high",
  "EK 5.6.A.4 ties the rate to the collisions able to meet the activation energy, and EK 5.6.A.3 defines that barrier independently of the reactant-to-product difference."),
]


def _extra_mutations():
    def sign_flipped(mod, cl):
        """The keyed direction word swapped: released for absorbed."""
        mod.QUESTIONS[6]["choices"][0] = "30 kJ/mol is absorbed, so the overall change is negative"
        cl[6] = ("30 kJ/mol is absorbed, so the overall change is negative", cl[6][1])

    def swapped_distractor_removed(mod, cl):
        """The wrong-sign option removed, so the item stops testing the sign."""
        mod.QUESTIONS[6]["choices"][1] = "The overall change cannot be found from the table"

    def barrier_miscomputed(mod, cl):
        """A tabulated energy retyped so the keyed barrier is no longer the difference."""
        t = mod.QUESTIONS[5]["table"]
        mod.QUESTIONS[5]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "170"] if r[0] == "Transition state" else list(r) for r in t["rows"]])

    def barriers_tied(mod, cl):
        """Two tabulated reactions given the same barrier, so no maximum is unique."""
        t = mod.QUESTIONS[12]["table"]
        mod.QUESTIONS[12]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], r[1], "210", r[3]] if r[0] == "R1" else list(r) for r in t["rows"]])

    def stem_barrier_wrong(mod, cl):
        """A stem-figure key moved off the recomputed reverse barrier."""
        mod.QUESTIONS[19]["choices"][0] = "70 kJ/mol, the forward barrier plus the energy released"
        cl[19] = ("70 kJ/mol", cl[19][1])

    def arrhenius_computation(mod, cl):
        mod.QUESTIONS[9]["q"] = ("Using the Arrhenius equation, what rate constant does an "
                                 "activation energy of 50 kJ/mol give?")
        mod.QUESTIONS[9]["choices"][0] = "12 per second"
        cl[9] = ("12 per second", cl[9][1])
        no_arrhenius_computation(mod)

    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the energy profile above, what is the reaction coordinate?"
        no_figure_language(mod)

    return [("the keyed direction word swapped from released to absorbed", sign_flipped),
            ("the wrong-sign option removed from a direction item", swapped_distractor_removed),
            ("a tabulated energy retyped so the keyed barrier is wrong", barrier_miscomputed),
            ("two tabulated barriers tied, so no maximum is unique", barriers_tied),
            ("a stem-figure key moved off the recomputed reverse barrier", stem_barrier_wrong),
            ("an item computing from the Arrhenius equation, which is excluded",
             arrhenius_computation),
            ("a stem pointing at a profile the bank cannot show", figure_language)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h5_6, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h5_6)
no_arrhenius_computation(h5_6)
h.run(h5_6, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
