"""Key audit for AP CHEMISTRY 6.2 Energy Diagrams.

One (anchor, claim) per item, in module order.

THE TOPIC IS NAMED AFTER A PICTURE AND THIS BANK HAS NONE, so this file carries
two checks the other unit 6 verifiers do not need, and they are the reason the
module is publishable at all:

``no_deictic_reference``   bans every phrase that POINTS at a drawing -- the
                           diagram above, in the diagram, as shown. The word
                           "diagram" itself cannot be banned here, because the
                           topic is diagrams; what has to be banned is a stem
                           that assumes the student is looking at one.
``diagram_items_are_self_contained``  the positive half, and the one that
                           actually protects the student: any item that speaks
                           of a diagram must either carry a table of the
                           energies it turns on, or state in its own words what
                           is drawn -- which state is higher, what the axis
                           carries, what the scale is. An item with neither is
                           one that silently needs a picture.

WHAT THE KEYS REST ON.

  6.2.A.1  a physical or chemical process can be described with an energy
           diagram that shows the endothermic or exothermic nature of that
           process                        every item
  6.1.A.3  supplies which direction of energy change each word names
                                          3, 4, 5, 11, 13, 15, 19, 20, 22, 25, 30
  6.1.A.2  heating a substance is such a process too              17
  6.1.A.4  a dissolution may go either way                        23
  6.1.A.1  a temperature is an indicator of an energy, not an energy   28
  skill 3.A  correct graphing technique, scale and units      6, 7, 8, 24, 29

THE SIGN, AGAIN. Twelve items supply two energies in a table and ask what the
diagram of that process would look like. Every one of those is recomputed here
by SUBTRACTING the tabulated energies and checking the sign explicitly, never
the magnitude, because products drawn above the reactants for an exothermic
process is the only way this topic can lie.

``direction_items_need_a_same_direction_distractor`` is carried over from
verify_h6_1.py for the same reason it exists there: if the key is the only
choice saying "exothermic", the word alone answers the item and the reasoning
is never tested.

SCOPE. A reaction energy profile with a transition state and an activation
energy is Unit 5's, not this topic's -- EK 6.2.A.1 says nothing about a barrier
between the two states. ``no_other_topic`` bans that vocabulary along with the
neighbouring unit 6 topics', over stems, keyed choices and why text. Distractors
are exempt, because a wrong answer naming an activation energy is a fair wrong
answer.

NEGATIVE CONTROL: ``python3 verify_h6_2.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h6_thermo as h6

import h6_2

INIT = "Energy of the initial state (kJ/mol)"
FIN = "Energy of the final state (kJ/mol)"
BEF = "Energy before (kJ/mol)"
AFT = "Energy after (kJ/mol)"
REACT = "Energy of the reactants (kJ/mol)"
PROD = "Energy of the products (kJ/mol)"

# A reference that POINTS at a drawing. "diagram" on its own is the topic's own
# word and must stay legal; what cannot appear is a stem assuming the student
# can see one.
_DEICTIC = re.compile(
    r"(?<![a-z])(?:diagram|figure|graph|picture|plot|image)s?\s+"
    r"(?:above|below|shown|here|opposite)(?![a-z])|"
    r"(?<![a-z])(?:in|from|on|according to)\s+the\s+(?:energy\s+)?"
    r"(?:diagram|figure|graph|plot|picture)(?![a-z])|"
    r"(?<![a-z])(?:as shown|shown below|shown above|the following)(?![a-z])",
    re.I)

_DIAGRAM = re.compile(r"(?<![A-Za-z])diagrams?(?![A-Za-z])", re.I)
# A stem talking about ONE PARTICULAR transformation, rather than about energy
# diagrams in general. "What does an energy diagram show?" needs no picture and
# no data; "what does the diagram for THIS reaction show?" needs both.
_SPECIFIC = re.compile(
    r"(?<![A-Za-z])(?:this|that|these|those|the same)\s+(?:\w+\s+){0,2}"
    r"(?:reaction|process|transformation|dissolution|change|substance)(?![A-Za-z])", re.I)
# What makes a diagram item self-contained: it says what is drawn, or what the
# axes carry, rather than expecting the student to look.
_DESCRIBES = re.compile(
    r"(?<![A-Za-z])(?:above|below|higher|lower|level with|same height|"
    r"vertical axis|horizontal axis|axes|no units|scale|kJ/mol|"
    r"upward step|downward step|initial state|final state)(?![A-Za-z])", re.I)

_OTHER_TOPIC = [
    (re.compile(r"(?<![A-Za-z])activation energ(?:y|ies)(?![A-Za-z])", re.I),
     "5.6's activation energy"),
    (re.compile(r"(?<![A-Za-z])transition state(?![A-Za-z])", re.I), "5.6's transition state"),
    (re.compile(r"(?<![A-Za-z])reaction coordinate(?![A-Za-z])", re.I),
     "5.6's reaction coordinate"),
    (re.compile(r"(?<![A-Za-z])catalys[a-z]*", re.I), "5.11's catalyst"),
    (re.compile(r"(?<![A-Za-z])specific heat(?![A-Za-z])", re.I), "6.4's specific heat"),
    (re.compile(r"(?<![A-Za-z])calorimet[a-z]*", re.I), "6.4's calorimetry"),
    (re.compile(r"(?<![A-Za-z])enthalp[a-z]*", re.I), "6.5 to 6.9's enthalpy"),
    (re.compile(r"(?<![A-Za-z])Hess(?![A-Za-z])", re.I), "6.9's law"),
]


def _facing(item):
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(x) for x in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def no_deictic_reference(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _DEICTIC.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: points at a drawing with {hit.group(0)!r}, and "
                f"this bank has none -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: the word diagram is used {sum(1 for it in module.QUESTIONS if _DIAGRAM.search(it['q']))} "
          "time(s) in a stem and never to point at one.")


def diagram_items_are_self_contained(module):
    """An item about a diagram must supply what the diagram would show.

    This is the half that protects the student. Banning "the diagram above" only
    stops the stem SAYING there is a picture; it does nothing about a stem that
    quietly needs one. So an item that speaks of the diagram of ONE PARTICULAR
    transformation must carry either a table of the energies or its own
    description of what is drawn.

    Items asking what an energy diagram does in general -- "what does an energy
    diagram of a process show?" -- are exempt, because they need no data and no
    picture. The exemption is narrow on purpose: it requires the ABSENCE of a
    definite referent, so the moment a stem says "this reaction" the
    requirement applies again. The negative control corrupts an item in exactly
    that way.
    """
    n, exempt = 0, 0
    for i, item in enumerate(module.QUESTIONS, 1):
        if not _DIAGRAM.search(item["q"]):
            continue
        if not (_SPECIFIC.search(item["q"]) or item.get("table")
                or _DESCRIBES.search(item["q"])):
            exempt += 1
            continue
        n += 1
        has_table = bool(item.get("table"))
        describes = bool(_DESCRIBES.search(item["q"]))
        assert has_table or describes, (
            f"{module.TOPIC[0]} q{i}: speaks of the diagram of one particular "
            f"transformation but supplies neither a table of energies nor any "
            f"description of what is drawn -- {item['q'][:90]!r}"
        )
    print(f"OK  {module.TOPIC[0]} self-containment: {n} item(s) naming a diagram carry "
          f"either the energies they turn on or their own description of what is drawn; "
          f"{exempt} ask what a diagram does in general and need neither.")


def no_other_topic(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in (item["q"], h.keyed(item), item["why"]):
            for pat, owner in _OTHER_TOPIC:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: a stem, key or why uses {hit.group(0)!r}, "
                    f"which is {owner} -- {text[:70]!r}"
                )
    print(f"OK  {module.TOPIC[0]} scope: no stem, key or why borrows Unit 5's activation "
          "energy, transition state or catalyst, or unit 6's calorimetry, enthalpy or "
          "Hess's law.")


def direction_items_need_a_same_direction_distractor(module):
    n = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        said = h6.stated_direction(h.keyed(item))
        if said is None:
            continue
        n += 1
        same = [k for k, c in enumerate(item["choices"])
                if k != item["ans"] and h6.stated_direction(c) == said]
        assert same, (
            f"{module.TOPIC[0]} q{i}: the key is the only choice that says {said!r}, so "
            "the item can be answered from the word without reading the diagram at all"
        )
    print(f"OK  {module.TOPIC[0]} direction guard: each of the {n} item(s) whose key names "
          "a direction offers a distractor naming the same direction.")


# ------------------------------------------------------------------- helpers

def step(table, label, before, after):
    """The signed step a diagram of this row would be drawn with."""
    return cg.cell(table, label, after) - cg.cell(table, label, before)


def _unique_extreme(values, pick):
    lab = pick(values, key=values.get)
    ties = [k for k, v in values.items() if abs(v - values[lab]) < 1e-12]
    assert ties == [lab], f"the extreme is not unique: {ties} all hold {values[lab]}"
    return lab


def _drawn_down(table, label, before, after):
    """Named boolean: would this row's diagram be drawn as a fall?"""
    return h6.direction(step(table, label, before, after))["exothermic"]


def _drawn_up(table, label, before, after):
    return h6.direction(step(table, label, before, after))["endothermic"]


# -------------------------------------------------------------- table items

def q10(table, item):
    steps = {lab: step(table, lab, INIT, FIN) for lab in cg.labels(table)}
    lab = _unique_extreme(steps, min)
    assert _drawn_down(table, lab, INIT, FIN), (
        f"the extreme process {lab} would not be drawn as a fall at all: {steps}")
    assert lab == "Process 1", f"the largest fall is at {lab}: {steps}"
    h.shows(item, "Process 1")
    return (f"the tabulated steps are {steps} kJ/mol, whose unique minimum "
            f"{h6.report(steps[lab])} is at {lab}")


def q11(table, item):
    steps = {lab: step(table, lab, INIT, FIN) for lab in cg.labels(table)}
    up = sorted(lab for lab in steps if _drawn_up(table, lab, INIT, FIN))
    assert up == ["Process 2", "Process 4"], f"the rises recompute as {up}: {steps}"
    h.shows(item, "Process 2 and Process 4")
    return (f"exactly two tabulated processes end above where they began, {up}, so exactly "
            f"two diagrams are drawn with a rise: {steps}")


def q12(table, item):
    steps = {lab: step(table, lab, INIT, FIN) for lab in cg.labels(table)}
    lab = _unique_extreme(steps, max)
    assert _drawn_up(table, lab, INIT, FIN), (
        f"the extreme process {lab} would not be drawn as a rise at all: {steps}")
    assert lab == "Process 4", f"the largest rise is at {lab}: {steps}"
    h.shows(item, "Process 4")
    return (f"the tabulated steps are {steps} kJ/mol, whose unique maximum "
            f"{h6.report(steps[lab])} is at {lab}")


def q13(table, item):
    steps = {lab: step(table, lab, INIT, FIN) for lab in cg.labels(table)}
    flat = sorted(lab for lab, v in steps.items() if h6.direction(v)["neither"])
    assert flat == ["Process 5"], f"the level processes recompute as {flat}: {steps}"
    h.shows(item, "Process 5")
    return (f"exactly one tabulated process ends at the energy it began at, {flat[0]}, so "
            f"exactly one diagram is drawn level: {steps}")


def q14(table, item):
    steps = {lab: step(table, lab, BEF, AFT) for lab in cg.labels(table)}
    lab = _unique_extreme(steps, max)
    assert _drawn_up(table, lab, BEF, AFT), f"{lab} is not drawn as a rise: {steps}"
    assert lab == "Vaporizing", f"the largest rise is at {lab}: {steps}"
    h.shows(item, "Vaporizing")
    return (f"the tabulated steps are {steps} kJ/mol, whose unique maximum "
            f"{h6.report(steps[lab])} is at {lab}")


def q15(table, item):
    steps = {lab: step(table, lab, BEF, AFT) for lab in cg.labels(table)}
    lab = _unique_extreme(steps, min)
    assert _drawn_down(table, lab, BEF, AFT), f"{lab} is not drawn as a fall: {steps}"
    assert lab == "Condensing", f"the largest fall is at {lab}: {steps}"
    h.shows(item, "Condensing")
    return (f"the tabulated steps are {steps} kJ/mol, whose unique minimum "
            f"{h6.report(steps[lab])} is at {lab}")


def q16(table, item):
    steps = {lab: step(table, lab, BEF, AFT) for lab in cg.labels(table)}
    target = h6.opposite(steps["Melting"])
    mirrors = sorted(lab for lab, v in steps.items()
                     if lab != "Melting" and abs(v - target) < 1e-12)
    assert mirrors == ["Freezing"], (
        f"the mirror of melting's {steps['Melting']:+g} kJ/mol recomputes as {mirrors}: {steps}"
    )
    assert h6.direction(steps["Melting"])["endothermic"] and \
        h6.direction(target)["exothermic"], (
        "the mirror must run the opposite way, or it is not a mirror at all"
    )
    h.shows(item, "Freezing")
    return (f"melting's tabulated step is {steps['Melting']:+g} kJ/mol, and exactly one "
            f"other row holds its negative, {mirrors[0]} at {target:+g}")


def q17(table, item):
    steps = {lab: step(table, lab, BEF, AFT) for lab in cg.labels(table)}
    phase_changes = {"Melting", "Freezing", "Vaporizing", "Condensing"}
    others = sorted(set(steps) - phase_changes)
    assert others == ["Warming the liquid"], (
        f"the tabulated rows that are not changes of state are {others}"
    )
    lab = others[0]
    assert _drawn_up(table, lab, BEF, AFT), (
        f"{lab} is not drawn as a rise, so it cannot be the keyed answer: {steps}"
    )
    h.shows(item, "Warming the liquid")
    return (f"exactly one tabulated row is not a change of state, {lab}, and its step "
            f"{h6.report(steps[lab])} is a rise")


def q18(table, item):
    steps = {lab: step(table, lab, REACT, PROD) for lab in cg.labels(table)}
    lab = _unique_extreme(steps, min)
    assert _drawn_down(table, lab, REACT, PROD), f"{lab} is not drawn as a fall: {steps}"
    assert lab == "Reaction D", f"the largest fall is at {lab}: {steps}"
    h.shows(item, "Reaction D")
    return (f"products minus reactants recomputes as {steps} kJ/mol, whose unique minimum "
            f"{h6.report(steps[lab])} is at {lab}")


def q19(table, item):
    steps = {lab: step(table, lab, REACT, PROD) for lab in cg.labels(table)}
    up = sorted(lab for lab in steps if _drawn_up(table, lab, REACT, PROD))
    assert up == ["Reaction B"], f"the rises recompute as {up}: {steps}"
    h.shows(item, "Reaction B")
    return (f"exactly one tabulated reaction has its products above its reactants, {up[0]}: "
            f"{steps}")


def q20(table, item):
    steps = {lab: step(table, lab, REACT, PROD) for lab in cg.labels(table)}
    flat = sorted(lab for lab, v in steps.items() if h6.direction(v)["neither"])
    assert flat == ["Reaction C"], f"the level reactions recompute as {flat}: {steps}"
    h.shows(item, "Reaction C")
    return (f"exactly one tabulated reaction has its products at the reactants' energy, "
            f"{flat[0]}: {steps}")


def q21(table, item):
    steps = {lab: step(table, lab, REACT, PROD) for lab in cg.labels(table)}
    falls = {lab: abs(v) for lab, v in steps.items()
             if _drawn_down(table, lab, REACT, PROD)}
    assert len(falls) >= 2, f"there must be several falls to choose among: {falls}"
    lab = _unique_extreme(falls, min)
    assert lab == "Reaction E", f"the shallowest fall is at {lab}: {falls}"
    h.shows(item, "Reaction E")
    return (f"the tabulated falls are {falls} kJ/mol deep, whose unique smallest is at "
            f"{lab}")


TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17,
                18: q18, 19: q19, 20: q20, 21: q21}


# ------------------------------------------------- the stated-drawing items

def _drawing(item, final_above_initial, what):
    """The key's direction word must follow from the drawing the stem describes.

    The stem says which state is drawn higher; EK 6.1.A.3 fixes what that means.
    The comparison is between two named booleans, never two tuples read in
    parallel.
    """
    signed = 1.0 if final_above_initial else -1.0
    assert h6.agrees(signed, h.keyed(item)), (
        f"the stem describes {what}, which EK 6.1.A.3 makes {h6.word(signed)}, but the "
        f"keyed choice says {h6.stated_direction(h.keyed(item))!r}: {h.keyed(item)!r}"
    )
    return (f"the stem describes {what}, so the energy of the system "
            f"{'rose' if final_above_initial else 'fell'} and the process is "
            f"{h6.word(signed)}")


def n22(item):
    return _drawing(item, False, "an exothermic reaction, whose products belong below")


def n23(item):
    return _drawing(item, True, "a solution drawn above the separate solid and water")


def n25(item):
    return _drawing(item, False, "a final state drawn below the initial state")


def n30(item):
    return _drawing(item, True, "a final state drawn above the initial state")


NUMERIC = {22: n22, 23: n23, 25: n25, 30: n30}


CLAIMS = [
 ("The endothermic or exothermic nature of that process",
  "EK 6.2.A.1, verbatim in substance: a physical or chemical process can be described with an energy diagram that shows the endothermic or exothermic nature of that process."),
 ("Both physical processes and chemical processes",
  "EK 6.2.A.1 opens with a physical OR chemical process, naming both kinds and restricting the representation to neither."),
 ("Lower than the reactants, because the energy of the system decreases in an exothermic process",
  "EK 6.1.A.3 makes an exothermic reaction one in which the energy of the system decreases, and EK 6.2.A.1 has the diagram show exactly that nature, so both clauses are in the key together."),
 ("Higher than the reactants, because the energy of the system increases in an endothermic process",
  "EK 6.1.A.3's mirror clause with EK 6.2.A.1, again with the direction and the height stated together so a half-right key cannot pass."),
 ("A process in which the energy of the system does not change",
  "EK 6.1.A.3 lists remaining the same as one of the three outcomes, and EK 6.2.A.1 has the relative heights of the two states report which outcome occurred."),
 ("Energy, in an energy unit such as kJ/mol",
  "EK 6.2.A.1 calls the representation an energy diagram, and suggested skill 3.A asks for appropriate graphing with correct scale and units."),
 ("not drawn to the same scale, so their energy changes cannot be compared by eye",
  "Suggested skill 3.A asks for correct scale, and EK 6.2.A.1 puts the size of the change into the height of the step, so unequal scales report a comparison that is not there."),
 ("The size of the energy change, which can no longer be read from the drawing",
  "Suggested skill 3.A asks for correct units; without them the step has no value attached, while the relative position of the states still reports the direction EK 6.2.A.1 names."),
 ("Whether the process is endothermic or exothermic",
  "EK 6.2.A.1 names exactly this as what the diagram shows, and it is carried by which state is drawn higher, which survives the loss of the numbers."),
 ("Process 1",
  "EK 6.2.A.1 with EK 6.1.A.3: the deepest downward step is the largest fall in the energy of the system. q10 subtracts the tabulated energies and checks the minimum is unique and really a fall."),
 ("Process 2 and Process 4",
  "EK 6.1.A.3 makes a rise the endothermic case. q11 recomputes the sign of every tabulated step and checks that exactly two rise."),
 ("Process 4",
  "The same statements read upward. q12 checks the maximum is unique and really a rise."),
 ("Process 5",
  "EK 6.1.A.3's third outcome, drawn level. q13 recomputes every step and checks exactly one is zero."),
 ("Vaporizing",
  "EK 6.2.A.1 applies to physical processes too. q14 subtracts the tabulated energies for each and checks the largest rise is unique."),
 ("Condensing",
  "The same table read downward. q15 checks the largest fall is unique and really a fall."),
 ("Freezing",
  "EK 6.2.A.1 makes the step between the two states the whole content of the diagram. q16 negates melting's recomputed step and checks exactly one other row holds that value, running the opposite way."),
 ("Warming the liquid",
  "EK 6.1.A.2 names the heating of a substance alongside phase changes. q17 checks that exactly one tabulated row is not a change of state and that its recomputed step really is a rise."),
 ("Reaction D",
  "EK 6.2.A.1 draws the energy change as the step from reactants to products. q18 subtracts the tabulated energies and checks the deepest fall is unique."),
 ("Reaction B",
  "EK 6.1.A.3 makes an increase in the system's energy endothermic. q19 recomputes every step and checks exactly one rises."),
 ("Reaction C",
  "EK 6.1.A.3 allows the energy to remain the same. q20 recomputes every step and checks exactly one is level."),
 ("Reaction E",
  "EK 6.2.A.1 puts the size of the change into the height of the step. q21 recomputes the depth of every fall and checks the smallest is unique."),
 ("The one with the products below, because the energy of the system decreases in an exothermic reaction",
  "EK 6.1.A.3 with EK 6.2.A.1. n22 checks the key's direction word against the drawing the stem describes."),
 ("An endothermic dissolution, in which the energy of the system increases",
  "EK 6.1.A.4 allows either direction for forming a solution and EK 6.1.A.3 makes a rise endothermic. n23 checks the direction word against the height the stem states."),
 ("The two axes have been exchanged; the energy belongs on the vertical axis",
  "EK 6.2.A.1 makes the endothermic or exothermic nature visible as the relative HEIGHT of the two states, which requires energy to run up the page, and skill 3.A asks for correct axes."),
 ("The process is exothermic, so energy passes from the system to the surroundings",
  "EK 6.2.A.1 covers physical processes, EK 6.1.A.3 makes a fall exothermic and sends the lost energy to the surroundings. n25 checks the direction against the drawing the stem describes."),
 ("The relative heights of the initial and final states",
  "EK 6.2.A.1 says the diagram shows the endothermic or exothermic nature, which is a matter of whether the energy rose or fell, so it is the two states' positions relative to each other that carry it."),
 ("the endothermic or exothermic nature depends on the difference between the two states",
  "EK 6.1.A.3 settles the direction by whether the energy of the system rose or fell, which is a difference; nothing in EK 6.2.A.1 requires an absolute height."),
 ("the axis must carry an energy, and a temperature is a different quantity",
  "EK 6.2.A.1 calls for an energy diagram, and EK 6.1.A.1 makes a temperature change an indicator of an energy change rather than the energy itself."),
 ("Which reaction changes the energy of the system by the greater amount",
  "EK 6.2.A.1 puts the direction, and with a scale the size, of the energy change into the step, and skill 3.A makes a shared correct scale what allows two steps to be compared."),
 ("Both represent endothermic processes, in which the energy of the system increases",
  "EK 6.2.A.1 covers a physical or a chemical process with the same representation, and EK 6.1.A.3 makes a rise in the system's energy the endothermic case. n30 checks the direction against the height the stem states."),
]


def _extra_mutations():
    def deictic_creeps_in(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, what does the step represent?"
        no_deictic_reference(mod)

    def diagram_item_left_empty(mod, cl):
        # The stem still says "diagram" but no longer says anything about what
        # is drawn, and it carries no table. Nothing in the deictic ban would
        # catch it, because it points at nothing -- it just silently needs a
        # picture, which is the defect this project already shipped.
        mod.QUESTIONS[2]["q"] = "What does the energy diagram for this reaction represent?"
        diagram_items_are_self_contained(mod)

    def activation_energy_creeps_in(mod, cl):
        mod.QUESTIONS[0]["q"] = (
            "What does an energy diagram show about the activation energy of a process?")
        no_other_topic(mod)

    def direction_word_alone_answers_it(mod, cl):
        # Both other exothermic choices turned endothermic. Every choice stays
        # distinct and the anchor still matches only the key.
        ch = list(mod.QUESTIONS[2]["choices"])
        ch[1] = ("Higher than the reactants, because an endothermic process stores the "
                 "released energy in the products")
        ch[2] = ("Higher than the reactants, because the energy of the system decreases "
                 "in an endothermic process")
        mod.QUESTIONS[2]["choices"] = ch
        direction_items_need_a_same_direction_distractor(mod)

    def drawing_key_swapped(mod, cl):
        # The key moved to the choice calling a solution drawn HIGHER exothermic.
        # Choices untouched, so they stay distinct and the new anchor is unique;
        # only n23's direction comparison can reject it.
        mod.QUESTIONS[22]["ans"] = 1
        cl[22] = ("An exothermic dissolution, in which the energy of the system increases",
                  cl[22][1])

    def states_maximum_moved(mod, cl):
        mod.QUESTIONS[9]["table"] = dict(
            headers=h6_2._T_STATES["headers"],
            rows=[["Process 1", "0", "-198"], ["Process 2", "0", "57"],
                  ["Process 3", "0", "-250"], ["Process 4", "0", "180"],
                  ["Process 5", "0", "0"]])

    def states_signs_flipped(mod, cl):
        # Every step negated. Every magnitude is preserved, so ONLY the sign
        # check can reject it -- the exact defect of drawing an exothermic
        # process with its products on top.
        mod.QUESTIONS[10]["table"] = dict(
            headers=h6_2._T_STATES["headers"],
            rows=[["Process 1", "0", "198"], ["Process 2", "0", "-57"],
                  ["Process 3", "0", "92"], ["Process 4", "0", "-180"],
                  ["Process 5", "0", "0"]])

    def mirror_made_ambiguous(mod, cl):
        # A second row given melting's exact negative, so the mirror is no
        # longer unique even though the keyed row still is one.
        mod.QUESTIONS[15]["table"] = dict(
            headers=h6_2._T_PHYSICAL["headers"],
            rows=[["Melting", "0", "9.5"], ["Freezing", "0", "-9.5"],
                  ["Vaporizing", "0", "31.0"], ["Condensing", "0", "-9.5"],
                  ["Warming the liquid", "0", "5.2"]])

    def non_phase_row_made_a_fall(mod, cl):
        # The one row that is not a change of state turned into a fall, so the
        # key's "upward step" is false while the row is still the only
        # non-phase-change one.
        mod.QUESTIONS[16]["table"] = dict(
            headers=h6_2._T_PHYSICAL["headers"],
            rows=[["Melting", "0", "9.5"], ["Freezing", "0", "-9.5"],
                  ["Vaporizing", "0", "31.0"], ["Condensing", "0", "-31.0"],
                  ["Warming the liquid", "0", "-5.2"]])

    def level_reaction_given_a_step(mod, cl):
        mod.QUESTIONS[19]["table"] = dict(
            headers=h6_2._T_TWO["headers"],
            rows=[["Reaction A", "120", "28"], ["Reaction B", "75", "166"],
                  ["Reaction C", "40", "31"], ["Reaction D", "210", "95"],
                  ["Reaction E", "60", "12"]])

    def second_rise_added(mod, cl):
        mod.QUESTIONS[18]["table"] = dict(
            headers=h6_2._T_TWO["headers"],
            rows=[["Reaction A", "120", "228"], ["Reaction B", "75", "166"],
                  ["Reaction C", "40", "40"], ["Reaction D", "210", "95"],
                  ["Reaction E", "60", "12"]])

    return [("a stem pointing at a diagram the bank cannot show", deictic_creeps_in),
            ("a diagram item left with neither a table nor a description of what is drawn",
             diagram_item_left_empty),
            ("a stem borrowing Unit 5's activation energy", activation_energy_creeps_in),
            ("an item where the direction word alone picks the key",
             direction_word_alone_answers_it),
            ("a key calling a solution drawn HIGHER an exothermic dissolution",
             drawing_key_swapped),
            ("the tabulated deepest fall moved off the keyed process", states_maximum_moved),
            ("every tabulated step negated, which changes nothing but the sign",
             states_signs_flipped),
            ("a second tabulated row given melting's exact negative, so the mirror is not "
             "unique", mirror_made_ambiguous),
            ("the one tabulated row that is not a change of state turned into a fall",
             non_phase_row_made_a_fall),
            ("the tabulated level reaction given a step", level_reaction_given_a_step),
            ("a second tabulated reaction made to rise, so the keyed one is not the only "
             "one", second_rise_added)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h6.selftest()
    h.selftest(h6_2, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_deictic_reference(h6_2)
diagram_items_are_self_contained(h6_2)
no_other_topic(h6_2)
direction_items_need_a_same_direction_distractor(h6_2)
h.run(h6_2, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
