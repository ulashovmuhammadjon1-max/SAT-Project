"""Key audit for AP CHEMISTRY 9.4 Thermodynamic and Kinetic Control.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  9.4.A.1  many thermodynamically favored processes do not occur to any
           measurable extent, or occur at extremely slow rates
                   5, 6, 14, 16, 18, 20, 28, 30
  9.4.A.2  such a process is under "kinetic control"; high activation energy is
           a common reason; failing to proceed at a noticeable rate does NOT
           mean the system is at equilibrium; and where a favored process does
           not occur it is reasonable to conclude kinetic control
                   1, 2, 3, 4, 7, 8, 10, 11, 12, 14, 15, 17, 19, 21, 22, 23,
                   24, 25, 26, 27, 29
  9.3.A.2  borrowed only to read the sign of a free energy value
                   7, 9, 13, 21, 22, 28

THE PRECONDITION GUARD. "Under kinetic control" is defined by EK 9.4.A.2 ONLY
for a process that is thermodynamically favored. A key that called an unfavored
process kinetically controlled would read perfectly well and be wrong, and no
structural check could see it. ``kinetic_from_stem`` therefore reads the sign of
the free energy value out of the stem and whether the key asserts kinetic
control out of the key, as two SEPARATELY NAMED facts, and requires them to
agree. Both directions are negative-controlled: a favored process whose key
denies control, and an unfavored one whose key asserts it.

The tabulated items apply the same two-condition rule row by row, so a row that
shows no change but is not favored cannot be swept into the answer.

SCOPE. Unit 5 owns rate laws, orders, mechanisms, the collision model and
catalysis; 9.1 to 9.3 own entropy, enthalpy and the free energy arithmetic; 9.5
owns the equilibrium constant. ``no_neighbouring_topics`` asserts that none of
them appears -- but it deliberately does NOT ban the bare word "equilibrium",
because EK 9.4.A.2's central warning is about equilibrium and the topic cannot
be written without it.

NEGATIVE CONTROL: ``python3 verify_h9_4.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h9_check as h9

import h9_4

GCOL = "Standard free energy change, kJ/mol"
EACOL = "Activation energy, kJ/mol"
OBSCOL = "Change observed after one hour at 298 K"

# Explicit lookarounds, never \b. "equilibrium" alone is NOT banned: the topic's
# own essential knowledge is about it.
_OUT_OF_SCOPE = re.compile(
    r"(?<![A-Za-z])(rate law|rate constant|reaction order|half-life|collision|arrhenius|"
    r"catalys[et]|catalysts|mechanism|elementary step|intermediate|equilibrium constant|"
    r"entropy|enthalpy)(?![A-Za-z])", re.I)

_VALUE_KJ = re.compile(r"\\\(\s*([+-]\d+(?:\.\d+)?)\s*\\\)\s*kJ/mol")

# The items that quote a free energy value in the stem and key a verdict about
# kinetic control. Listed explicitly so the guard cannot quietly stop covering
# an item that was edited.
STEM_VALUE_ITEMS = (7, 22)


def no_neighbouring_topics(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _OUT_OF_SCOPE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: mentions {hit.group(0)!r}, which belongs to "
                f"Unit 5 or to another Unit 9 topic -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no rate law, order, mechanism, collision model "
          "or catalysis, and no entropy or enthalpy arithmetic.")


def _key_asserts_kinetic_control(key):
    """Whether the key claims kinetic control, denies it, or says neither.

    Two named readings rather than one, because "no, it is not under kinetic
    control" contains the phrase just as an assertion does, and a check that
    only searched for the phrase would read a denial as an assertion -- the
    same shape of own-goal as matching "favored" inside "unfavored".
    """
    mentions_control = "kinetic control" in key.lower()
    opens_with_denial = key.strip().lower().startswith("no,")
    if not mentions_control and not opens_with_denial:
        return None
    return mentions_control and not opens_with_denial


def kinetic_from_stem(item):
    """EK 9.4.A.2's precondition, read from the stem and checked against the key."""
    m = _VALUE_KJ.search(item["q"])
    assert m, f"the stem quotes no free energy value: {item['q'][:70]!r}"
    stem_says_favored = float(m.group(1)) < 0
    key_says_controlled = _key_asserts_kinetic_control(h.keyed(item))
    assert key_says_controlled is not None, (
        f"the key neither asserts nor denies kinetic control: {h.keyed(item)!r}"
    )
    assert stem_says_favored == key_says_controlled, (
        f"the stem quotes {m.group(1)} kJ/mol, so the process is "
        f"{'favored' if stem_says_favored else 'NOT favored'}, but the key "
        f"{'asserts' if key_says_controlled else 'denies'} kinetic control -- EK 9.4.A.2 "
        f"defines it only for a favored process"
    )
    return (f"the stem's {m.group(1)} kJ/mol makes the process "
            f"{'favored' if stem_says_favored else 'unfavored'}, which is the precondition "
            f"EK 9.4.A.2 attaches to kinetic control, and the key agrees")


NUMERIC = {7: kinetic_from_stem, 22: kinetic_from_stem}


# ------------------------------------------------------------------ table items

def _rows(table):
    """Each row as (free energy change, the rest of the row), by label."""
    values = cg.col(table, GCOL)
    return {lab: (v, row) for lab, v, row in zip(cg.labels(table), values, table["rows"])}


def _observation(table, label):
    return str(dict(zip(cg.labels(table), table["rows"]))[label][2]).strip().lower()


def q8(table, item):
    favored = {lab for lab, (v, _) in _rows(table).items() if v < 0}
    stalled = {lab for lab in cg.labels(table)
               if _observation(table, lab) == "none detectable"}
    controlled = sorted(favored & stalled)
    assert controlled == ["1", "4"], (
        f"the rows meeting BOTH of EK 9.4.A.2's conditions are {controlled}"
    )
    assert sorted(stalled) != controlled, (
        "at least one tabulated row must show no change WITHOUT being favored, or the "
        "item does not test the precondition at all"
    )
    h.shows(item, "Processes 1 and 4")
    return (f"the tabulated rows that are favored are {sorted(favored)} and those showing "
            f"no change are {sorted(stalled)}, whose intersection is {controlled}")


def q9(table, item):
    moving = [lab for lab, (v, _) in _rows(table).items()
              if v < 0 and _observation(table, lab) == "substantial"]
    assert moving == ["2"], f"the favored rows showing substantial change are {moving}"
    h.shows(item, "Process 2")
    return (f"exactly one tabulated row pairs a free energy change below zero with a "
            f"substantial observed change: {moving[0]}")


def _unfavored(table):
    return sorted(lab for lab, (v, _) in _rows(table).items() if v > 0)


def q10(table, item):
    unfavored = _unfavored(table)
    assert unfavored == ["3"], f"the tabulated rows above zero are {unfavored}"
    assert _observation(table, "3") == "none detectable", (
        "the unfavored row must be one that shows no change, or there is nothing for "
        "thermodynamics to explain"
    )
    h.shows(item, "Process 3")
    return (f"exactly one tabulated row has a free energy change above zero, {unfavored[0]}, "
            f"and it is one of the rows showing no change")


def q11(table, item):
    unfavored = _unfavored(table)
    assert unfavored == ["3"], f"the tabulated rows above zero are {unfavored}"
    h.shows(item, "Process 3, because kinetic control is defined only for a favored process")
    return (f"the only tabulated row excluded by EK 9.4.A.2's favorability precondition is "
            f"{unfavored[0]}, whatever its activation energy might be")


def q12(table, item):
    favored = {lab: cg.cell(table, lab, EACOL)
               for lab, (v, _) in _rows(table).items() if v < 0}
    hardest = max(favored, key=favored.get)
    assert hardest == "W", f"the favored row with the largest activation energy is {hardest}"
    assert len([v for v in favored.values() if abs(v - favored[hardest]) < 1e-12]) == 1, (
        f"that activation energy must be unique among the favored rows: {favored}"
    )
    assert "Y" not in favored, (
        "the row named in the tied distractor must be unfavored, or the distractor would "
        "be defensible"
    )
    h.shows(item, "Reaction W")
    return (f"among the tabulated rows that are favored, the activation energies are "
            f"{favored}, whose unique maximum is at {hardest}")


def q13(table, item):
    unfavored = _unfavored(table)
    assert unfavored == ["Y"], f"the tabulated rows above zero are {unfavored}"
    h.shows(item, "Reaction Y")
    return f"exactly one tabulated reaction has a free energy change above zero: {unfavored[0]}"


def q14(table, item):
    values = {lab: v for lab, (v, _) in _rows(table).items()}
    groups = {}
    for lab, v in values.items():
        groups.setdefault(round(v, 9), []).append(lab)
    shared = sorted(g for g in groups.values() if len(g) > 1)
    assert shared == [["W", "X"]], (
        f"exactly one pair of tabulated reactions must share a free energy change: {groups}"
    )
    ea = {lab: cg.cell(table, lab, EACOL) for lab in shared[0]}
    assert len(set(ea.values())) == len(ea), (
        f"the sharing pair must differ in activation energy, or nothing accounts for the "
        f"difference in behaviour: {ea}"
    )
    h.shows(item, "activation energies differ")
    return (f"the tabulated free energy changes group as {groups}, with one shared pair "
            f"whose activation energies {ea} differ")


TABLE_CHECKS = {8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14}


CLAIMS = [
 ("under kinetic control",
  "EK 9.4.A.2: processes that are thermodynamically favored but do not proceed at a measurable rate are under kinetic control. The same statement denies that such a process is at equilibrium."),
 ("A high activation energy",
  "EK 9.4.A.2 states that high activation energy is a common reason for a process to be under kinetic control; a positive free energy change would make the process unfavored, a different situation."),
 ("failing to proceed at a noticeable rate does not mean the system is at equilibrium",
  "EK 9.4.A.2 says this in so many words, so an unchanging composition is not by itself evidence of equilibrium."),
 ("That the process is under kinetic control",
  "EK 9.4.A.2's closing sentence licenses exactly this inference for a process known to be favored that does not occur at a measurable rate."),
 ("Many do not occur to any measurable extent, or occur at extremely slow rates",
  "EK 9.4.A.1, verbatim in substance, and the reason the topic exists at all."),
 ("a favored process may still occur at an extremely slow rate",
  "EK 9.4.A.1 separates favorability from speed, so the size of the free energy change settles whether a process is downhill and nothing about how fast it goes."),
 ("thermodynamically favored and under kinetic control",
  "EK 9.4.A.2's inference applied to a value below zero. kinetic_from_stem reads the sign out of the stem and checks the key asserts control only because the process is favored."),
 ("Processes 1 and 4",
  "EK 9.4.A.2 requires BOTH conditions. q8 recomputes which tabulated rows are favored and which show no change and takes the intersection, checking the two sets differ so the precondition is really tested."),
 ("Process 2",
  "EK 9.3.A.2 marks a favored process by a value below zero. q9 recomputes which tabulated row pairs that with a substantial observed change."),
 ("Process 3",
  "Exactly one tabulated row is above zero, so its lack of change needs no appeal to kinetics. q10 recomputes which row that is and checks it is one of those showing no change."),
 ("Process 3, because kinetic control is defined only for a favored process",
  "EK 9.4.A.2's definition excludes an unfavored process regardless of its activation energy. q11 recomputes which tabulated row is excluded."),
 ("Reaction W",
  "EK 9.4.A.2 names high activation energy as the common reason and restricts kinetic control to favored processes. q12 recomputes the activation energies of the favored rows only."),
 ("Reaction Y",
  "EK 9.3.A.2 marks an unfavored process by a value above zero. q13 recomputes which tabulated reaction that is."),
 ("activation energies differ",
  "EK 9.4.A.1 lets two equally favored processes differ entirely in whether they are observed and EK 9.4.A.2 names the reason. q14 finds the tabulated pair sharing a free energy change and checks their activation energies differ."),
 ("favored process held up by a high activation energy",
  "EK 9.4.A.2 denies that an unchanging mixture is at equilibrium and names high activation energy as the common alternative explanation."),
 ("Many thermodynamically favored processes occur at extremely slow rates",
  "EK 9.4.A.1 makes slowness no evidence at all about favorability, which is precisely what the student's inference assumes."),
 ("That it is thermodynamically favored",
  "EK 9.4.A.2 builds favorability into the definition of kinetic control; the activation energy enters as the common explanation rather than as a prior requirement."),
 ("It may occur at a rate too slow to measure",
  "EK 9.4.A.1 says many favored processes do not occur to any measurable extent or occur at extremely slow rates, and EK 9.4.A.2 gives that case a name rather than excluding it."),
 ("A high activation energy commonly holds such a reaction up",
  "Learning objective 9.4.A asks for the explanation in terms of kinetics and EK 9.4.A.2 supplies it directly."),
 ("thermodynamically favored, and whether it proceeds at a measurable rate",
  "EK 9.4.A.1 and EK 9.4.A.2 exist because the two questions come apart, and neither answer settles the other."),
 ("below zero, because kinetic control is defined for a favored process",
  "EK 9.4.A.2 restricts kinetic control to favored processes and EK 9.3.A.2 makes a favored process one whose standard free energy change is below zero."),
 ("not thermodynamically favored in the first place",
  "EK 9.4.A.2's precondition fails for a value above zero, so the absence of change is explained without kinetics. kinetic_from_stem reads the sign from the stem and checks the key denies control."),
 ("seen to proceed at a measurable rate",
  "EK 9.4.A.2 makes failing to proceed at a measurable rate one of the two conditions, so a favored process observed to proceed fails it."),
 ("Reaction J only, since kinetic control requires a favored process",
  "EK 9.4.A.2's two conditions taken together: only the favored reaction meets both, and the inference is licensed without measuring any activation energy."),
 ("asks what a favored process does NOT tell you",
  "Learning objective 9.4.A takes a thermodynamically favored reaction as its premise, so the free energy idea has to come first; nothing in the topic computes one quantity from the other."),
 ("A process under kinetic control",
  "EK 9.4.A.2 names exactly this combination -- favored, not proceeding at a measurable rate, commonly held up by a high activation energy -- and forbids calling the unchanging system an equilibrium."),
 ("still thermodynamically favored to change",
  "EK 9.4.A.2 reserves kinetic control for favored processes and denies that an unchanging system is thereby at equilibrium, so the tendency to change persists in one case and not the other."),
 ("standard free energy change above zero",
  "A value above zero contradicts the premise that the reaction is favored, which EK 9.3.A.2 ties to a value below zero; every other option is language EK 9.4.A.1 or 9.4.A.2 uses for this situation."),
 ("Kinetic control may be concluded; equilibrium may not be",
  "EK 9.4.A.2 licenses the first conclusion in exactly this case and denies the second in the same statement."),
 ("says whether a process is downhill, not whether it will be seen to happen",
  "EK 9.4.A.1 and EK 9.4.A.2 together separate favorability from observation, and nothing in the topic lets kinetics make an unfavored process favored."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the figure above, what is the process called?"
        h9.no_figure_language(mod)

    def unit_five_creeps_in(mod, cl):
        mod.QUESTIONS[1]["why"] = (
            mod.QUESTIONS[1]["why"] + " A catalyst would lower it.")
        no_neighbouring_topics(mod)

    def favored_process_denied_control(mod, cl):
        # The stem's value turned negative, so the process IS favored and EK
        # 9.4.A.2's inference applies -- but the key still denies kinetic
        # control. Confirmed to violate the precondition guard and nothing else.
        mod.QUESTIONS[21]["q"] = mod.QUESTIONS[21]["q"].replace("+130.0", "-130.0")

    def unfavored_process_keyed_as_controlled(mod, cl):
        # The mirror: the value turned positive while the key still calls the
        # process favored and under kinetic control.
        mod.QUESTIONS[6]["q"] = mod.QUESTIONS[6]["q"].replace("-210.0", "+210.0")

    def stalled_rows_all_favored(mod, cl):
        # The unfavored row made to CHANGE, so every row that shows no change is
        # now also favored. The keyed pair is still right, which is the point:
        # the item no longer tests EK 9.4.A.2's precondition, because nothing in
        # the table is excluded by it. Confirmed to leave the intersection
        # assertion satisfied and to violate only the one that exists to catch
        # this, which would otherwise never run.
        mod.QUESTIONS[7]["table"] = dict(
            headers=h9_4._T_OBS["headers"],
            rows=[["1", "-210.0", "none detectable"], ["2", "-95.0", "substantial"],
                  ["3", "+130.0", "substantial"], ["4", "-58.0", "none detectable"]])

    def observation_changed(mod, cl):
        mod.QUESTIONS[7]["table"] = dict(
            headers=h9_4._T_OBS["headers"],
            rows=[["1", "-210.0", "substantial"], ["2", "-95.0", "substantial"],
                  ["3", "+130.0", "none detectable"], ["4", "-58.0", "none detectable"]])

    def activation_energy_maximum_moved(mod, cl):
        mod.QUESTIONS[11]["table"] = dict(
            headers=h9_4._T_EA["headers"],
            rows=[["W", "-150.0", "25.0"], ["X", "-150.0", "35.0"],
                  ["Y", "+80.0", "40.0"], ["Z", "-20.0", "30.0"]])

    def unfavored_row_given_the_largest_barrier(mod, cl):
        # The tied distractor becomes defensible: the unfavored row now carries
        # the largest activation energy in the table.
        # Y made FAVORED but with a smaller barrier than W, so the maximum is
        # still W and still unique -- the only assertion left to fail is the one
        # that keeps the tied distractor indefensible.
        mod.QUESTIONS[11]["table"] = dict(
            headers=h9_4._T_EA["headers"],
            rows=[["W", "-150.0", "250.0"], ["X", "-150.0", "35.0"],
                  ["Y", "-80.0", "40.0"], ["Z", "-20.0", "30.0"]])

    def shared_pair_broken(mod, cl):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h9_4._T_EA["headers"],
            rows=[["W", "-150.0", "250.0"], ["X", "-120.0", "35.0"],
                  ["Y", "+80.0", "40.0"], ["Z", "-20.0", "30.0"]])

    def shared_pair_given_equal_barriers(mod, cl):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h9_4._T_EA["headers"],
            rows=[["W", "-150.0", "35.0"], ["X", "-150.0", "35.0"],
                  ["Y", "+80.0", "40.0"], ["Z", "-20.0", "30.0"]])

    return [
        ("a stem pointing at a figure the bank cannot show", figure_language),
        ("a why reaching into catalysis, which is Unit 5's material", unit_five_creeps_in),
        ("a favored process whose key denies kinetic control",
         favored_process_denied_control),
        ("an unfavored process whose key asserts kinetic control",
         unfavored_process_keyed_as_controlled),
        ("every stalled tabulated row made favored, so the precondition is untested",
         stalled_rows_all_favored),
        ("a tabulated observation changed so the keyed pair is wrong", observation_changed),
        ("the largest tabulated activation energy moved off the keyed reaction",
         activation_energy_maximum_moved),
        ("the tied distractor made defensible by turning its reaction favored",
         unfavored_row_given_the_largest_barrier),
        ("the tabulated pair sharing a free energy change broken apart",
         shared_pair_broken),
        ("the sharing pair given equal activation energies, so nothing explains the "
         "difference", shared_pair_given_equal_barriers),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h9_4, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h9.no_figure_language(h9_4)
no_neighbouring_topics(h9_4)
h.run(h9_4, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
