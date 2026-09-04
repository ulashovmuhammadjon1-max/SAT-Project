"""Key audit for AP CHEMISTRY 6.1 Endothermic and Exothermic Processes.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  6.1.A.1  a temperature change in a system indicates an energy change
                                          1, 13, 22, 30
  6.1.A.2  heating or cooling a substance, a phase change and a chemical
           transformation are all described as endothermic or exothermic
                                          2, 17, 18, 19, 29
  6.1.A.3  the energy of a reacting system decreases (exothermic), increases
           (endothermic) or stays the same, and what the system loses the
           surroundings gain, by heat transfer or by work
                                          3, 4, 5, 6, 10, 11, 12, 14, 15, 16,
                                          20, 21, 27, 28
  6.1.A.4  forming a solution may go either way, on the relative strengths of
           the interactions before and after dissolution
                                          7, 8, 9, 23, 24, 25, 26
  EK 6.5.A.1 supplies the constant temperature of a phase change     22

THE SIGN IS THE WHOLE TOPIC, so nothing here is checked by magnitude.
``process_direction`` inverts the surroundings' temperature change ON PURPOSE
and says so in its name: a solution that WARMS reports a system that LOST
energy. That inversion is the one step a wrong key in this topic would skip, so
it is written once, named, and used by every table check.

``direction_items_need_a_same_direction_distractor`` is the structural guard
against the vocabulary shortcut. If the only choice saying "exothermic" is the
key, a student can answer without following the energy anywhere, and an anchor
that pins only the word would still match a key whose REASON was backwards. The
check asserts that every item whose key states a direction also offers at least
one distractor stating the SAME direction, so the item turns on the reasoning.

SCOPE. Nine topics share unit 6 and they must not write each other's questions,
so ``no_other_topic`` bans the neighbouring vocabulary from every stem, every
KEYED choice and every ``why``: the specific heat capacity and the calorimeter
belong to 6.4, the word enthalpy to 6.5 and 6.6, average kinetic energy and
thermal equilibrium to 6.3, the energy diagram to 6.2, bond energies to 6.7 and
Hess's law to 6.9. Distractors are deliberately NOT scanned -- naming a
calorimeter is a fair wrong answer, and banning it from a distractor would make
the item worse rather than the module tidier.

ARITHMETIC. Every temperature difference and every comparison of interaction
energies is recomputed from the table alone, through ``h6_thermo``, whose own
positive and negative controls run with ``python3 h6_thermo.py``.

NEGATIVE CONTROL: ``python3 verify_h6_1.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h6_thermo as h6

import h6_1

BEFORE_W = "Temperature of the water before (degrees Celsius)"
AFTER_W = "Temperature of the solution after (degrees Celsius)"
BEFORE_M = "Temperature of the mixture before (degrees Celsius)"
AFTER_M = "Temperature of the mixture after (degrees Celsius)"
NEEDED = "Energy needed to separate the original particles (kJ/mol)"
RELEASED = "Energy released as the new interactions form (kJ/mol)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|the plot above|the plot below)(?![a-z])", re.I)

# The neighbouring topics' vocabulary. Scanned over stems, keyed choices and
# ``why`` text only -- see the module docstring for why distractors are exempt.
_OTHER_TOPIC = [
    (re.compile(r"(?<![A-Za-z])specific heat(?![A-Za-z])", re.I), "6.4's specific heat"),
    (re.compile(r"(?<![A-Za-z])heat capacit(?:y|ies)(?![A-Za-z])", re.I), "6.4's heat capacity"),
    (re.compile(r"(?<![A-Za-z])calorimet[a-z]*", re.I), "6.4's calorimetry"),
    (re.compile(r"(?<![A-Za-z])enthalp[a-z]*", re.I), "6.5, 6.6, 6.8 and 6.9's enthalpy"),
    (re.compile(r"(?<![A-Za-z])average kinetic energy(?![A-Za-z])", re.I),
     "6.3's particle-level account"),
    (re.compile(r"(?<![A-Za-z])thermal equilibrium(?![A-Za-z])", re.I), "6.3's equilibrium"),
    (re.compile(r"(?<![A-Za-z])energy diagram(?![A-Za-z])", re.I), "6.2's representation"),
    (re.compile(r"(?<![A-Za-z])bond energ(?:y|ies)(?![A-Za-z])", re.I), "6.7's bond energies"),
    (re.compile(r"(?<![A-Za-z])Hess(?![A-Za-z])", re.I), "6.9's law"),
]


def _facing(item):
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(x) for x in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every measurement is carried as a table and no "
          "item points at a picture.")


def no_other_topic(module):
    """Unit 6's nine topics must not write each other's questions."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in (item["q"], h.keyed(item), item["why"]):
            for pat, owner in _OTHER_TOPIC:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: a stem, key or why uses {hit.group(0)!r}, "
                    f"which is {owner} -- {text[:70]!r}"
                )
    print(f"OK  {module.TOPIC[0]} scope: no stem, key or why borrows the specific heat "
          "capacity, the calorimeter, enthalpy, kinetic energy, the energy diagram, bond "
          "energies or Hess's law.")


def direction_items_need_a_same_direction_distractor(module):
    """An item whose key names a direction must not be answerable from the word.

    If every distractor states the opposite direction, the word alone picks the
    key and the item never tests where the energy went -- which is the half of
    EK 6.1.A.3 most easily shipped backwards.
    """
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
            "the item can be answered from the word without following the energy anywhere"
        )
    print(f"OK  {module.TOPIC[0]} direction guard: each of the {n} item(s) whose key names "
          "a direction offers a distractor naming the same direction, so the word alone "
          "cannot pick it.")


# ------------------------------------------------------------------- helpers

def process_direction(delta_t_of_surroundings):
    """The direction of the PROCESS, from the temperature change of what surrounds it.

    The sign is inverted here, once, deliberately, and the inversion is what the
    name says: EK 6.1.A.3 has the energy an exothermic system loses gained by
    the surroundings, and EK 6.1.A.1 makes the surroundings' rising temperature
    the report of that gain. So a solution that WARMS is a process that LOST
    energy, and the process's own change is negative.
    """
    return h6.direction(-delta_t_of_surroundings)


def warming(table, label, before, after):
    """The signed temperature change of the surroundings, recomputed from the table."""
    return cg.cell(table, label, after) - cg.cell(table, label, before)


def net_of_dissolution(table, label):
    """EK 6.1.A.4: energy needed to separate, minus energy released on forming.

    Positive is endothermic -- more was required than was given back.
    """
    return cg.cell(table, label, NEEDED) - cg.cell(table, label, RELEASED)


def _unique_extreme(values, pick):
    """The label with the extreme value, asserted to be the only one holding it."""
    lab = pick(values, key=values.get)
    ties = [k for k, v in values.items() if abs(v - values[lab]) < 1e-12]
    assert ties == [lab], f"the extreme is not unique: {ties} all hold {values[lab]}"
    return lab


# -------------------------------------------------------------- table items

def q10(table, item):
    dts = {lab: warming(table, lab, BEFORE_W, AFTER_W) for lab in cg.labels(table)}
    lab = _unique_extreme(dts, max)
    assert process_direction(dts[lab])["exothermic"], (
        f"the salt with the largest rise, {lab}, does not come out exothermic: {dts}"
    )
    assert lab == "Calcium chloride", f"the largest rise is at {lab}: {dts}"
    h.shows(item, "Calcium chloride")
    return (f"the tabulated temperature changes are {dts}, whose unique maximum "
            f"{dts[lab]:+g} degrees is at {lab} and is a rise, so that system lost the most")


def q11(table, item):
    dts = {lab: warming(table, lab, BEFORE_W, AFTER_W) for lab in cg.labels(table)}
    lab = _unique_extreme(dts, min)
    assert process_direction(dts[lab])["endothermic"], (
        f"the salt with the largest fall, {lab}, does not come out endothermic: {dts}"
    )
    assert lab == "Ammonium nitrate", f"the largest fall is at {lab}: {dts}"
    h.shows(item, "Ammonium nitrate")
    return (f"the tabulated temperature changes are {dts}, whose unique minimum "
            f"{dts[lab]:+g} degrees is at {lab} and is a fall, so that system gained the most")


def q12(table, item):
    dts = {lab: warming(table, lab, BEFORE_W, AFTER_W) for lab in cg.labels(table)}
    exo = sorted(lab for lab, dt in dts.items() if process_direction(dt)["exothermic"])
    assert exo == ["Calcium chloride", "Lithium chloride"], (
        f"the exothermic dissolutions recompute as {exo}: {dts}"
    )
    h.shows(item, "Calcium chloride and lithium chloride")
    return (f"exactly two tabulated solutions warmed, {exo}, so exactly two dissolutions "
            f"are exothermic under EK 6.1.A.3: {dts}")


def q13(table, item):
    dts = {lab: warming(table, lab, BEFORE_W, AFTER_W) for lab in cg.labels(table)}
    endo = {lab: dt for lab, dt in dts.items() if process_direction(dt)["endothermic"]}
    assert len(endo) >= 2, f"there must be several endothermic rows to choose among: {endo}"
    sizes = {lab: abs(dt) for lab, dt in endo.items()}
    lab = _unique_extreme(sizes, min)
    assert lab == "Sodium chloride", f"the smallest endothermic change is at {lab}: {sizes}"
    h.shows(item, "Sodium chloride")
    return (f"the endothermic rows change by {sizes} degrees, whose unique smallest "
            f"magnitude is at {lab}")


def q14(table, item):
    dts = {lab: warming(table, lab, BEFORE_M, AFTER_M) for lab in cg.labels(table)}
    lab = _unique_extreme(dts, min)
    assert process_direction(dts[lab])["endothermic"], (
        f"the mixture with the largest fall, {lab}, does not come out endothermic: {dts}"
    )
    assert lab == "Mixture X", f"the largest fall is at {lab}: {dts}"
    h.shows(item, "Mixture X")
    return (f"the tabulated changes are {dts}, whose unique minimum {dts[lab]:+g} degrees "
            f"is at {lab}, the largest transfer from the surroundings into the system")


def q15(table, item):
    dts = {lab: warming(table, lab, BEFORE_M, AFTER_M) for lab in cg.labels(table)}
    lab = _unique_extreme(dts, max)
    assert process_direction(dts[lab])["exothermic"], (
        f"the mixture with the largest rise, {lab}, does not come out exothermic: {dts}"
    )
    assert lab == "Mixture Z", f"the largest rise is at {lab}: {dts}"
    h.shows(item, "Mixture Z")
    return (f"the tabulated changes are {dts}, whose unique maximum {dts[lab]:+g} degrees "
            f"is at {lab}, the largest release to the surroundings")


def q16(table, item):
    dts = {lab: warming(table, lab, BEFORE_M, AFTER_M) for lab in cg.labels(table)}
    flat = sorted(lab for lab, dt in dts.items() if process_direction(dt)["neither"])
    assert flat == ["Mixture Y"], f"the mixtures showing no change recompute as {flat}: {dts}"
    h.shows(item, "Mixture Y")
    return (f"exactly one tabulated mixture ended at the temperature it started, {flat[0]}, "
            f"which is EK 6.1.A.3's third possibility: {dts}")


def q24(table, item):
    nets = {lab: net_of_dissolution(table, lab) for lab in cg.labels(table)}
    lab = _unique_extreme(nets, min)
    assert h6.direction(nets[lab])["exothermic"], (
        f"the extreme system {lab} does not come out exothermic: {nets}"
    )
    assert lab == "System P", f"the largest net release is at {lab}: {nets}"
    h.shows(item, "System P")
    return (f"needed minus released recomputes as {nets} kJ/mol, whose unique minimum "
            f"{h6.report(nets[lab])} is at {lab}")


def q25(table, item):
    nets = {lab: net_of_dissolution(table, lab) for lab in cg.labels(table)}
    lab = _unique_extreme(nets, max)
    assert h6.direction(nets[lab])["endothermic"], (
        f"the extreme system {lab} does not come out endothermic: {nets}"
    )
    assert lab == "System Q", f"the largest net requirement is at {lab}: {nets}"
    h.shows(item, "System Q")
    return (f"needed minus released recomputes as {nets} kJ/mol, whose unique maximum "
            f"{h6.report(nets[lab])} is at {lab}")


def q26(table, item):
    nets = {lab: net_of_dissolution(table, lab) for lab in cg.labels(table)}
    flat = sorted(lab for lab, v in nets.items() if h6.direction(v)["neither"])
    assert flat == ["System R"], f"the systems with no net change recompute as {flat}: {nets}"
    h.shows(item, "System R")
    return (f"exactly one tabulated system has its two energies equal, {flat[0]}, so "
            f"neither an increase nor a decrease is left: {nets}")


TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16,
                24: q24, 25: q25, 26: q26}


# ------------------------------------------------- the stated-observation items

def _observation(item, warmed, measured_on, what):
    """The key's direction word must follow from the observation the stem states.

    ``warmed`` is the sign of the temperature change the stem reports, taken
    from the stem and nowhere else. ``measured_on`` says WHOSE temperature that
    is -- ``"system"`` or ``"surroundings"`` -- and it has to be said, because
    the inference runs opposite ways for the two and there is no way to tell
    from the number.

    The first version of this helper assumed every reported temperature
    belonged to the surroundings and promptly rejected item 29, whose stem
    says in as many words "taking the water as the system". The key was right
    and the CHECK was inverted -- the same shape as the (acid, base) against
    (base, acid) comparison this project already shipped. Naming the side is
    the fix; a bare sign cannot carry it.
    """
    assert warmed != 0, "the stem must report a temperature change in one direction"
    assert measured_on in ("system", "surroundings"), measured_on
    measured_on_the_system = measured_on == "system"
    d = (h6.direction(warmed) if measured_on_the_system
         else process_direction(warmed))
    signed = -1.0 if d["exothermic"] else 1.0
    assert h6.agrees(signed, h.keyed(item)), (
        f"the stem reports that {what}, measured on the {measured_on}, so EK 6.1.A.3 "
        f"makes the process {h6.word(signed)}, but the keyed choice says "
        f"{h6.stated_direction(h.keyed(item))!r}: {h.keyed(item)!r}"
    )
    gained = warmed > 0
    return (f"the stem reports that {what}, so the {measured_on} "
            f"{'gained' if gained else 'lost'} energy and the process is "
            f"{h6.word(signed)}")


def n18(item):
    return _observation(item, +1.0, "surroundings", "the window pane became warmer")


def n19(item):
    return _observation(item, -1.0, "surroundings", "the skin felt cool")


def n23(item):
    return _observation(item, -1.0, "surroundings",
                        "the water in the cold pack became cold")


def n29(item):
    # The stem names the water as the system in as many words, so the sign is
    # read the other way round from the three items above.
    return _observation(item, +1.0, "system", "the water on the hotplate was warmed")


NUMERIC = {18: n18, 19: n19, 23: n23, 29: n29}


CLAIMS = [
 ("That the energy of the system has changed",
  "EK 6.1.A.1, verbatim in substance: temperature changes in a system indicate energy changes."),
 ("The heating or cooling of a substance, a phase change, or a chemical transformation",
  "EK 6.1.A.2 names all three: energy changes in a system can be described as endothermic and exothermic processes such as the heating or cooling of a substance, phase changes, or chemical transformations."),
 ("It decreases, it increases, or it remains the same",
  "EK 6.1.A.3's opening sentence lists exactly these three outcomes for the energy of a reacting system, and the third is stated as plainly as the other two."),
 ("Exothermic, and the energy lost by the reacting species is gained by the surroundings",
  "EK 6.1.A.3, verbatim in substance, with both clauses in the key because the swap is the defect this topic is most exposed to: a decrease in the system's energy is exothermic, and what the system loses the surroundings gain."),
 ("Endothermic, and the system gains the energy from the surroundings",
  "EK 6.1.A.3's mirror clause, again with both halves stated: an increase in the system's energy is endothermic, and the system gains that energy from the surroundings."),
 ("By heat transfer and by work",
  "EK 6.1.A.3 names both routes in both directions: heat transfer from or work done by the system when exothermic, heat transfer to or work done on it when endothermic."),
 ("Either is possible, and which one occurs depends on the relative strengths of the interactions before and after dissolution",
  "EK 6.1.A.4, verbatim in substance: the formation of a solution may be an exothermic or endothermic process, depending on the relative strengths of the intermolecular or interparticle interactions before and after dissolution."),
 ("release less energy than separating the original particles required, so the dissolution is endothermic",
  "EK 6.1.A.4 makes the comparison of the two decide the direction, and EK 6.1.A.1 reads the cooling of the solution as the system having taken energy from it."),
 ("release more energy than separating the original particles required, so the dissolution is exothermic",
  "EK 6.1.A.4's other outcome, with EK 6.1.A.3 giving the released energy to the surroundings, which is what the warming of the solution reports."),
 ("Calcium chloride",
  "EK 6.1.A.3 with EK 6.1.A.1: the largest rise in the water's temperature is the largest release. q10 recomputes every tabulated change and checks the maximum is unique and really a rise."),
 ("Ammonium nitrate",
  "The same pair of statements read the other way. q11 recomputes every change and checks the minimum is unique and really a fall."),
 ("Calcium chloride and lithium chloride",
  "EK 6.1.A.3 makes a process exothermic when the system loses energy. q12 recomputes the sign of every tabulated change and checks that exactly two are rises."),
 ("Sodium chloride",
  "EK 6.1.A.1 ties the size of the temperature change to the size of the energy change. q13 recomputes the endothermic rows and checks the smallest magnitude among them is unique."),
 ("Mixture X",
  "EK 6.1.A.3 has an endothermic system gain energy from its surroundings. q14 recomputes every tabulated change and checks the largest fall is unique."),
 ("Mixture Z",
  "EK 6.1.A.3 has an exothermic system give energy to its surroundings. q15 recomputes every change and checks the largest rise is unique."),
 ("Mixture Y",
  "EK 6.1.A.3's third possibility, that the energy of the system remains the same. q16 recomputes every change and checks exactly one mixture ended where it began."),
 ("The heating or cooling of a substance and phase changes are also described that way",
  "EK 6.1.A.2 lists those two alongside chemical transformations, so restricting the two words to reactions drops two thirds of the framework's own sentence."),
 ("It is exothermic, because energy has passed from the condensing water to the pane around it",
  "EK 6.1.A.2 counts a phase change among these processes and EK 6.1.A.3 sends an exothermic system's energy to the surroundings. n18 checks the key's direction word against the warming the stem reports."),
 ("It is endothermic, because the evaporating liquid has taken energy from the skin",
  "EK 6.1.A.2 with EK 6.1.A.3's endothermic clause: the system gains energy from the surroundings. n19 checks the direction word against the cooling the stem reports."),
 ("since the framework lists remaining the same alongside decreasing and increasing",
  "EK 6.1.A.3 states three outcomes, not two, so a reaction that leaves the energy of the system unchanged is within the framework's own list."),
 ("work done by the system is a route by which energy reaches the surroundings",
  "EK 6.1.A.3 names the two routes explicitly: heat transfer from OR work done BY the system. Work is in the framework's sentence, not an addition to it."),
 ("the temperature of a pure substance stays constant through a phase change even while energy is transferred",
  "EK 6.1.A.1 says a temperature change indicates an energy change and says nothing about the converse, and EK 6.5.A.1 states that the temperature of a pure substance remains constant during a phase change."),
 ("Endothermic, because the dissolving salt and water take energy from their surroundings",
  "EK 6.1.A.4 allows the formation of a solution to be endothermic and EK 6.1.A.3 has such a system gain energy from its surroundings. n23 checks the direction word against the cooling the stem reports."),
 ("System P",
  "EK 6.1.A.4's comparison made countable. q24 subtracts the tabulated release from the tabulated requirement for every row and checks the largest net release is unique and really negative."),
 ("System Q",
  "The same subtraction read the other way. q25 checks the largest net requirement is unique and really positive, which EK 6.1.A.3 makes an endothermic process."),
 ("System R",
  "EK 6.1.A.4 turns on the relative strengths of the two sets of interactions, so equal amounts leave no change. q26 recomputes every row and checks exactly one is balanced."),
 ("The reacting species",
  "EK 6.1.A.3 writes of the energy lost by the reacting species and names them, in its own parenthesis, as the system; the water that gains that energy is therefore part of the surroundings."),
 ("the energy lost by the reacting species is the energy gained by the surroundings",
  "EK 6.1.A.3 states exactly this for exothermic reactions, so the two descriptions are one transfer counted from the two sides."),
 ("Endothermic, because the water gains energy from its surroundings",
  "EK 6.1.A.2 names the heating of a substance among these processes and EK 6.1.A.3 has a system that gains energy do so from its surroundings. n29 checks the direction against the warming the stem reports."),
 ("Whether the temperature of the solution rises or falls",
  "EK 6.1.A.1 makes a temperature change the indicator of an energy change and EK 6.1.A.3 fixes which direction of transfer each sign reports, so no other observation is needed."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, what does the temperature change show?"
        no_figure_language(mod)

    def other_topic_creeps_in(mod, cl):
        mod.QUESTIONS[0]["q"] = (
            "Using the specific heat of water, what does a temperature change indicate?")
        no_other_topic(mod)

    def enthalpy_creeps_into_a_key(mod, cl):
        ch = list(mod.QUESTIONS[2]["choices"])
        ch[0] = "The enthalpy decreases, increases, or remains the same"
        mod.QUESTIONS[2]["choices"] = ch
        cl[2] = ("enthalpy decreases, increases, or remains the same", cl[2][1])
        no_other_topic(mod)

    def direction_word_alone_answers_it(mod, cl):
        # Both exothermic distractors turned endothermic, so the key becomes the
        # only choice saying "exothermic" and the word alone picks it. Every
        # choice stays distinct and the anchor still matches only the key, so
        # nothing but this guard can reject it.
        ch = list(mod.QUESTIONS[3]["choices"])
        ch[2] = "Endothermic, and the energy is destroyed rather than transferred"
        ch[4] = ("Endothermic, and the surroundings lose an equal amount of energy to the "
                 "system")
        mod.QUESTIONS[3]["choices"] = ch
        direction_items_need_a_same_direction_distractor(mod)

    def observation_key_swapped(mod, cl):
        # The key moved to the choice that calls a WARMING pane endothermic.
        # The choices are untouched, so they stay distinct and the new anchor
        # matches only the new key -- the direction check is the only thing
        # standing between this and a student.
        mod.QUESTIONS[17]["ans"] = 1
        cl[17] = ("It is endothermic, because energy has passed from the condensing water",
                  cl[17][1])

    def system_side_key_swapped(mod, cl):
        # Item 29 is the one that names the WATER as the system, so its sign is
        # read the opposite way to items 18, 19 and 23. This control moves the
        # key to the exothermic choice: if _observation ever loses the
        # measured_on argument and assumes the surroundings again, it will
        # accept this and reject the real key, which is precisely the inverted
        # check this project has already shipped once.
        mod.QUESTIONS[28]["ans"] = 1
        cl[28] = ("Exothermic, because the water gains energy from its surroundings",
                  cl[28][1])

    def dissolving_maximum_moved(mod, cl):
        # Lithium chloride raised above calcium chloride, so the keyed salt is
        # no longer the largest release.
        mod.QUESTIONS[9]["table"] = dict(
            headers=h6_1._T_DISSOLVING["headers"],
            rows=[["Ammonium nitrate", "21.0", "13.4"],
                  ["Calcium chloride", "21.0", "31.6"],
                  ["Potassium bromide", "21.0", "18.2"],
                  ["Lithium chloride", "21.0", "38.0"],
                  ["Sodium chloride", "21.0", "20.8"]])

    def dissolving_maximum_tied(mod, cl):
        # A tie for the largest rise. The keyed salt is still A largest, so a
        # check that took max() without asserting uniqueness would pass.
        mod.QUESTIONS[9]["table"] = dict(
            headers=h6_1._T_DISSOLVING["headers"],
            rows=[["Ammonium nitrate", "21.0", "13.4"],
                  ["Calcium chloride", "21.0", "31.6"],
                  ["Potassium bromide", "21.0", "18.2"],
                  ["Lithium chloride", "21.0", "31.6"],
                  ["Sodium chloride", "21.0", "20.8"]])

    def dissolving_signs_flipped(mod, cl):
        # Every rise turned into a fall of the same size. The magnitudes are
        # untouched, so ONLY the sign check can reject it -- which is the
        # defect this whole topic is exposed to.
        mod.QUESTIONS[11]["table"] = dict(
            headers=h6_1._T_DISSOLVING["headers"],
            rows=[["Ammonium nitrate", "21.0", "28.6"],
                  ["Calcium chloride", "21.0", "10.4"],
                  ["Potassium bromide", "21.0", "23.8"],
                  ["Lithium chloride", "21.0", "14.5"],
                  ["Sodium chloride", "21.0", "21.2"]])

    def flat_mixture_given_a_change(mod, cl):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h6_1._T_REACTIONS["headers"],
            rows=[["Mixture V", "22.0", "20.9"],
                  ["Mixture W", "22.0", "30.4"],
                  ["Mixture X", "22.0", "16.8"],
                  ["Mixture Y", "22.0", "23.6"],
                  ["Mixture Z", "22.0", "34.9"]])

    def interaction_columns_swapped(mod, cl):
        # The two energy columns exchanged. Every magnitude is preserved and
        # every row still differs from the others, so the ONLY thing that
        # changes is which systems are exothermic -- the exact inversion
        # process_direction exists to catch.
        mod.QUESTIONS[23]["table"] = dict(
            headers=h6_1._T_INTERACTIONS["headers"],
            rows=[[lab, rel, need]
                  for lab, need, rel in h6_1._T_INTERACTIONS["rows"]])

    return [("a stem referring to a diagram the bank cannot show", figure_language),
            ("a stem borrowing 6.4's specific heat", other_topic_creeps_in),
            ("a keyed choice borrowing the word enthalpy", enthalpy_creeps_into_a_key),
            ("an item where the direction word alone picks the key",
             direction_word_alone_answers_it),
            ("a key calling a warming pane's condensation endothermic",
             observation_key_swapped),
            ("a key calling the heating of water, named in the stem as the system, "
             "exothermic", system_side_key_swapped),
            ("the tabulated maximum moved off the keyed salt", dissolving_maximum_moved),
            ("the tabulated maximum tied, so the keyed salt is not the unique answer",
             dissolving_maximum_tied),
            ("every tabulated rise turned into a fall of the same size, which changes "
             "nothing but the sign", dissolving_signs_flipped),
            ("the tabulated mixture that showed no change given one",
             flat_mixture_given_a_change),
            ("the two tabulated interaction energies exchanged, which inverts every "
             "direction while preserving every magnitude", interaction_columns_swapped)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h6.selftest()
    h.selftest(h6_1, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h6_1)
no_other_topic(h6_1)
direction_items_need_a_same_direction_distractor(h6_1)
h.run(h6_1, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
