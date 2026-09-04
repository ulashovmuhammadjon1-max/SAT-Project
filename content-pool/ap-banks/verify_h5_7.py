"""Key audit for AP CHEMISTRY 5.7 Introduction to Reaction Mechanisms.

One ``(anchor, claim)`` per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EK 5.7.A.1  A mechanism is a series of elementary reactions occurring in
            sequence; the components may include reactants, intermediates,
            products and catalysts.        (items 1, 2, 9, 12, 20, 22, 26)
EK 5.7.A.2  The elementary steps when combined should align with the overall
            balanced equation.       (items 3, 7, 10, 14, 17, 19, 21, 24, 27,
            28, 29)
EK 5.7.A.3  A reaction intermediate is produced by some elementary steps and
            consumed by others, so it is present only while a reaction is
            occurring.   (items 4, 5, 6, 8, 11, 13, 17, 18, 19, 23, 25, 30)
EK 5.7.A.4  Detecting an intermediate is a common way to build evidence in
            support of one mechanism over an alternative.  (items 15, 16, 29, 30)
EK 5.11.A.2 supplies the catalyst's pattern -- consumed in one step and
            regenerated in a subsequent one.        (items 9, 12, 18, 22)

EVERY MECHANISM IS RESOLVED, NOT REMEMBERED. ``h_equation`` adds the tabulated
steps, cancels what appears on both sides, and reports the overall equation, the
intermediates and the catalysts. So each "which species is the intermediate"
key is checked against a search over the steps themselves, and each "what is the
overall equation" key against the actual sum. Both helpers are negative-
controlled inside ``h_equation.selftest()``, which runs first: a species that
survives into the overall equation must NOT be reported as an intermediate, and
a wrong overall equation must NOT be reported as aligning.

Every tabulated step is also required to balance in atoms and charge, under EK
4.2.A.2, so a mistyped step fails here rather than teaching a student a
mechanism that loses an atom.

THE EXCLUSION STATEMENT. EK 5.7.A.4's exclusion rules out collection of data
pertaining to the detection of an intermediate, so ``no_detection_procedure``
asserts no stem asks how a detection is carried out or what it measures.

NEGATIVE CONTROL: ``python3 verify_h5_7.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h_equation as heq

import h5_7

STEPCOL = "Elementary reaction"

_FIGURE = re.compile(
    r"(?<![a-z])(as shown|shown below|shown above|figure|image|picture|depicted|"
    r"pictured|illustrated|(?:diagram|graph|profile|curve|plot|chart)s?\s+"
    r"(?:above|below))(?![a-z])", re.I)

# EK 5.7.A.4's exclusion statement: the DETECTION PROCEDURE and its data are out
# of scope. These are the words a procedural item would have to use.
_PROCEDURE = re.compile(
    r"(?<![a-z])(spectrometer|spectrophotometer|absorbance|apparatus|"
    r"burette|calibration|instrument|readings taken|collect the data|"
    r"collection of data)(?![a-z])", re.I)


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, but every mechanism "
                f"here is a table of steps -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every mechanism is carried as a table of "
          "elementary steps.")


def no_detection_procedure(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _PROCEDURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: mentions {hit.group(0)!r}, which EK 5.7.A.4's "
                f"exclusion statement puts out of scope -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item asks how an intermediate is detected, as "
          "EK 5.7.A.4's exclusion statement requires.")


def mechanism(table):
    """The tabulated steps, in row order, each checked to balance."""
    steps = [r[table["headers"].index(STEPCOL)] for r in table["rows"]]
    for s in steps:
        assert heq.balanced(s), f"a tabulated elementary step does not balance: {s} -- {heq.report(s)}"
    return steps


def _fmt(side):
    return " + ".join(f"{n if n > 1 else ''} {name}".strip() for name, n in sorted(side.items()))


def one_intermediate(table, item, expected):
    steps = mechanism(table)
    found = heq.intermediates(steps)
    assert found == [expected], (
        f"reading the tabulated steps gives intermediates {found}, not [{expected!r}]"
    )
    h.shows(item, expected)
    return (f"searching the {len(steps)} tabulated steps for a species produced by an earlier "
            f"step and consumed by a later one gives {found}")


def one_catalyst(table, item, expected, anchor=None):
    steps = mechanism(table)
    found = heq.catalysts(steps)
    assert found == [expected], (
        f"reading the tabulated steps gives catalysts {found}, not [{expected!r}]"
    )
    h.shows(item, anchor or expected)
    return (f"searching the {len(steps)} tabulated steps for a species consumed by an earlier "
            f"step and regenerated by a later one gives {found}")


def overall_is(table, item, equation):
    steps = mechanism(table)
    assert heq.aligns_with(steps, equation), (
        f"the tabulated steps combine to {heq.mechanism_overall(steps)}, which is not "
        f"{equation!r}"
    )
    also = [i for i, c in enumerate(item["choices"])
            if i != item["ans"] and " gives " in c and _aligns(steps, c)]
    assert not also, f"choice(s) {also} also align with the tabulated steps"
    h.shows(item, equation)
    left, right = heq.mechanism_overall(steps)
    return (f"adding the {len(steps)} tabulated steps and cancelling what appears on both "
            f"sides leaves {_fmt(left)} giving {_fmt(right)}")


def _aligns(steps, candidate):
    try:
        return heq.aligns_with(steps, candidate)
    except AssertionError:
        return False


# ---------------------------------------------------------------- table items

def q6(table, item):
    return one_intermediate(table, item, "NO3")


def q7(table, item):
    return overall_is(table, item, "NO2 + CO gives NO + CO2")


def q8(table, item):
    return one_intermediate(table, item, "ClO")


def q9(table, item):
    return one_catalyst(table, item, "Cl")


def q10(table, item):
    return overall_is(table, item, "O3 + O gives 2 O2")


def q11(table, item):
    return one_intermediate(table, item, "IO-")


def q12(table, item):
    return one_catalyst(table, item, "I-",
                        anchor="consumed in the first step and regenerated in the second")


def q13(table, item):
    return one_intermediate(table, item, "N2O2")


def q14(table, item):
    steps = mechanism(table)
    stated = "2 O3 gives 3 O2"
    assert heq.aligns_with(steps, stated), (
        f"the tabulated steps combine to {heq.mechanism_overall(steps)}, not {stated!r}"
    )
    assert heq.intermediates(steps) == ["O"], heq.intermediates(steps)
    h.shows(item, "adding the steps and cancelling the intermediate leaves")
    return (f"adding the {len(steps)} tabulated steps and cancelling the single intermediate "
            f"{heq.intermediates(steps)} reproduces the stated overall equation exactly")


def q24(table, item):
    steps = mechanism(table)
    stated = "H2 + ICl gives I2 + HCl"
    assert not heq.aligns_with(steps, stated), (
        "the stated overall equation was supposed NOT to align with the tabulated steps"
    )
    left, right = heq.mechanism_overall(steps)
    assert left.get("ICl") == 2 and right.get("HCl") == 2, (
        f"the combined steps give {left} giving {right}, so the keyed reason is wrong"
    )
    h.shows(item, "requires two ICl and produces two HCl")
    return (f"the tabulated steps combine to {_fmt(left)} giving {_fmt(right)}, which the "
            f"stated equation {stated!r} does not match")


def q25(table, item):
    return one_intermediate(table, item, "HI")


TABLE_CHECKS = {6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13,
                14: q14, 24: q24, 25: q25}


CLAIMS = [
 ("series of elementary reactions, or steps, that occur in sequence",
  "EK 5.7.A.1, near verbatim: a reaction mechanism consists of a series of elementary reactions, or steps, that occur in sequence."),
 ("Reactants, intermediates, products and catalysts",
  "EK 5.7.A.1 lists exactly those four as the components a mechanism may include; a transition state is a point on EK 5.6.A.3's energy profile instead."),
 ("Align with the overall balanced equation of the reaction",
  "EK 5.7.A.2, verbatim in substance: the elementary steps when combined should align with the overall balanced equation of a chemical reaction."),
 ("produced by some elementary steps and consumed by others",
  "EK 5.7.A.3, near verbatim. The highest-energy arrangement is EK 5.6.A.3's transition state and a species that is not used up is EK 5.11.A.2's catalyst."),
 ("steps that produce it are matched by steps that consume it",
  "EK 5.7.A.3 draws the transience from the matched production and consumption: produced by some elementary steps and consumed by others, SUCH THAT it is present only while a reaction is occurring."),
 ("NO3",
  "EK 5.7.A.3's definition applied to the tabulated steps and recomputed in q6, which also checks the intermediate is unique."),
 ("NO2 + CO gives NO + CO2",
  "EK 5.7.A.2's alignment, recomputed in q7 by adding the tabulated steps and cancelling; no other offered equation aligns."),
 ("ClO",
  "EK 5.7.A.3's definition applied to the tabulated ozone steps, recomputed in q8."),
 ("Cl",
  "EK 5.7.A.1 lists catalysts among a mechanism's components and EK 5.11.A.2 has one consumed in a step and regenerated later. Recomputed in q9 as the unique such species."),
 ("O3 + O gives 2 O2",
  "EK 5.7.A.2's alignment for the tabulated ozone steps, recomputed in q10."),
 ("IO-",
  "EK 5.7.A.3's definition applied to the tabulated peroxide steps, recomputed in q11."),
 ("consumed in the first step and regenerated in the second",
  "EK 5.11.A.2's catalyst pattern, with EK 5.7.A.1 listing catalysts among a mechanism's components. Recomputed in q12 as the unique such species."),
 ("N2O2",
  "EK 5.7.A.3's definition applied to the tabulated nitrogen dioxide steps, recomputed in q13."),
 ("adding the steps and cancelling the intermediate leaves",
  "EK 5.7.A.2's alignment, recomputed in q14 against the overall equation stated in the stem, together with the single intermediate that cancels."),
 ("build evidence in support of one reaction mechanism over an alternative",
  "EK 5.7.A.4, verbatim in substance. The overall equation is known independently under EK 5.7.A.2."),
 ("evidence in support of that mechanism over the alternatives",
  "EK 5.7.A.4's own word is evidence rather than proof: detection is a common way to BUILD EVIDENCE IN SUPPORT OF one mechanism over an alternative."),
 ("consumed again by a later step",
  "EK 5.7.A.3 has the intermediate consumed by later steps so that it is present only while the reaction runs, and EK 5.7.A.2 makes the overall equation what survives the combination."),
 ("produced before it is consumed, while the catalyst is consumed before it is regenerated",
  "EK 5.7.A.3 defines the intermediate by production then consumption and EK 5.11.A.2 has the catalyst consumed then regenerated, which is the same pattern in the opposite order."),
 ("not fully consumed by the later steps",
  "EK 5.7.A.3 requires an intermediate to be present only while a reaction is occurring, and EK 5.7.A.2 makes the overall equation what the combined steps leave behind."),
 ("occur in sequence, one after another",
  "EK 5.7.A.1 states that a mechanism consists of a series of elementary reactions, or steps, that occur in sequence."),
 ("align with the overall balanced equation once the species appearing on both sides have cancelled",
  "EK 5.7.A.2 imposes exactly this, and EK 5.7.A.3's intermediates are the species expected to appear in more than one step and cancel."),
 ("catalyst, consumed early and regenerated later",
  "EK 5.11.A.2 has a catalyst frequently consumed in one step and regenerated in a subsequent one, and EK 5.7.A.1 lists catalysts among a mechanism's components."),
 ("intermediate, since it is produced by one step and consumed by another",
  "EK 5.7.A.3 defines a reaction intermediate as a species produced by some elementary steps and consumed by others, which is the position described."),
 ("requires two ICl and produces two HCl",
  "EK 5.7.A.2's alignment test, recomputed in q24, which finds the combined steps demand two of one reactant where the stated equation writes one."),
 ("HI",
  "EK 5.7.A.3's definition applied to the tabulated steps, recomputed in q25."),
 ("reactants, intermediates, products and a catalyst all at once",
  "EK 5.7.A.1 says the components MAY INCLUDE those four, which places no restriction against a mechanism holding all of them."),
 ("requires the combined steps to align with the overall balanced equation",
  "EK 5.7.A.2 states that requirement, so a proposal failing it describes a different reaction from the one observed."),
 ("The reactants of the overall equation",
  "EK 5.7.A.2's alignment puts the overall equation's reactants on the left of the combined steps, while EK 5.7.A.3's intermediates cancel out of that combination."),
 ("evidence such as a detected intermediate is what distinguishes them",
  "EK 5.7.A.2 imposes only alignment with the overall equation, and EK 5.7.A.4 makes detection of an intermediate a common way to build evidence for one mechanism over an alternative."),
 ("Every proposal so far is incomplete",
  "EK 5.7.A.3 makes an intermediate a species present only while a reaction occurs and EK 5.7.A.4 makes its detection evidence bearing on which mechanism is right, so a species no proposal contains counts against all of them."),
]


def _extra_mutations():
    def step_unbalanced(mod, cl):
        """A tabulated step retyped so it loses an atom."""
        t = mod.QUESTIONS[5]["table"]
        mod.QUESTIONS[5]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "NO2 + NO2 gives NO3 + N"] if r[0] == "Step 1" else list(r)
                  for r in t["rows"]])

    def intermediate_removed(mod, cl):
        """The second step retyped so nothing is consumed after being produced."""
        t = mod.QUESTIONS[7]["table"]
        mod.QUESTIONS[7]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "Cl + O gives ClO"] if r[0] == "Step 2" else list(r)
                  for r in t["rows"]])

    def catalyst_becomes_intermediate(mod, cl):
        """The catalyst's two appearances swapped, so the key names the wrong role."""
        t = mod.QUESTIONS[8]["table"]
        mod.QUESTIONS[8]["table"] = dict(
            headers=t["headers"],
            rows=[["Step 1", "ClO + O gives Cl + O2"],
                  ["Step 2", "Cl + O3 gives ClO + O2"]])

    def overall_key_wrong(mod, cl):
        """The overall-equation key moved to an equation the steps do not give."""
        mod.QUESTIONS[6]["choices"][0] = "NO2 + CO gives NO2 + CO2"
        cl[6] = ("NO2 + CO gives NO2 + CO2", cl[6][1])

    def alignment_broken(mod, cl):
        """A step retyped so the mechanism no longer sums to the stated equation."""
        t = mod.QUESTIONS[13]["table"]
        mod.QUESTIONS[13]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "O + O2 gives O3"] if r[0] == "Step 2" else list(r)
                  for r in t["rows"]])

    def procedure_creeps_in(mod, cl):
        mod.QUESTIONS[14]["q"] = ("What absorbance is recorded when the intermediate is "
                                  "detected?")
        no_detection_procedure(mod)

    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the mechanism shown above, what is a step?"
        no_figure_language(mod)

    return [("a tabulated elementary step retyped so it loses an atom", step_unbalanced),
            ("the second step retyped so no intermediate remains", intermediate_removed),
            ("a catalyst's two appearances swapped, so its role changes",
             catalyst_becomes_intermediate),
            ("the overall-equation key moved off the sum of the steps", overall_key_wrong),
            ("a step retyped so the mechanism stops aligning with the stated equation",
             alignment_broken),
            ("an item asking how a detection is carried out, which is excluded",
             procedure_creeps_in),
            ("a stem pointing at a picture the bank cannot show", figure_language)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    heq.selftest()
    h.selftest(h5_7, CLAIMS, table_checks=TABLE_CHECKS, mutations=_extra_mutations())

heq.selftest()
no_figure_language(h5_7)
no_detection_procedure(h5_7)
h.run(h5_7, CLAIMS, table_checks=TABLE_CHECKS)
