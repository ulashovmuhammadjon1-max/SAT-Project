"""Key audit for AP CHEMISTRY 6.3 Heat Transfer and Thermal Equilibrium.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  6.3.A.1  the particles in a warmer body have a greater AVERAGE kinetic energy
                                    1, 9, 10, 12, 14, 15, 17, 23, 24, 26, 29
  6.3.A.2  collisions between particles in thermal contact can transfer energy,
           and that process is called heat transfer, heat exchange, or transfer
           of energy as heat        2, 3, 8, 22, 25, 26, 30
  6.3.A.3  eventually thermal equilibrium is reached AS THE PARTICLES CONTINUE
           TO COLLIDE, and there the average kinetic energy of both bodies is
           the same and hence their temperatures are
                                    4, 5, 6, 7, 11, 13, 16, 18, 19, 20, 21, 27,
                                    28, 29, 30

THE AVERAGE-VERSUS-TOTAL TRAP, and the check built for it. EK 6.3.A.3 equates
the AVERAGE kinetic energy of the two bodies, and hence their temperatures. It
does not equate their totals, and a large cool body can hold far more energy in
total than a small warm one. ``equilibrium_keys_equate_an_average`` asserts that
any keyed choice on an equilibrium item that asserts an equality is asserting it
of the average kinetic energy or of the temperature, and never of a total. The
distractor sitting beside the key on item 6 is the total-energy version, so an
off-by-one key there ships the error.

THE DIRECTION, AND WHY ITS KEYS CARRY TWO CLAUSES. No single CED sentence says
energy runs from warm to cold; it follows from EK 6.3.A.1 giving the warmer body
the greater average and EK 6.3.A.3 requiring the two to finish equal. So the
keys that name a direction name that reason too, and
``direction_keys_state_both_clauses`` checks the pairing is not inverted -- with
named booleans, never two tuples read in parallel, which is how a checker in
this project rejected a correct key.

SCOPE. 6.1 owns the words endothermic and exothermic, and ``no_other_topic``
bans BOTH from every stem, key and why here, because those two topics would
otherwise write the same question. 6.4 owns q = mc(delta T), the specific heat
capacity and the calorimeter, so nothing here computes a final temperature or a
quantity of energy; the final temperatures in the third table are measured
values and the questions asked of them are about direction and about what
equilibrium means.

ARITHMETIC. Every temperature comparison is recomputed from the table alone, and
item 20's claim that each measured final temperature lies BETWEEN the two
starting values is checked for all five trials rather than asserted.

NEGATIVE CONTROL: ``python3 verify_h6_3.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h6_thermo as h6

import h6_3

T1 = "Temperature of body 1 (degrees Celsius)"
T2 = "Temperature of body 2 (degrees Celsius)"
TEMP = "Temperature (degrees Celsius)"
BLOCK = "Initial temperature of the metal block (degrees Celsius)"
WATER = "Initial temperature of the water (degrees Celsius)"
FINAL = "Final temperature of both (degrees Celsius)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below)(?![a-z])", re.I)

_OTHER_TOPIC = [
    (re.compile(r"(?<![A-Za-z0-9])exothermic(?![A-Za-z0-9])", re.I), "6.1's word"),
    (re.compile(r"(?<![A-Za-z0-9])endothermic(?![A-Za-z0-9])", re.I), "6.1's word"),
    (re.compile(r"(?<![A-Za-z])energy diagram(?![A-Za-z])", re.I), "6.2's representation"),
    (re.compile(r"(?<![A-Za-z])specific heat(?![A-Za-z])", re.I), "6.4's specific heat"),
    (re.compile(r"(?<![A-Za-z])heat capacit(?:y|ies)(?![A-Za-z])", re.I), "6.4's heat capacity"),
    (re.compile(r"(?<![A-Za-z])calorimet[a-z]*", re.I), "6.4's calorimetry"),
    (re.compile(r"(?<![A-Za-z])enthalp[a-z]*", re.I), "6.5 to 6.9's enthalpy"),
    (re.compile(r"(?<![A-Za-z])Hess(?![A-Za-z])", re.I), "6.9's law"),
]

_EQUILIBRIUM = re.compile(r"(?<![A-Za-z])thermal equilibrium(?![A-Za-z])", re.I)
_EQUALITY = re.compile(r"(?<![A-Za-z])(?:the same|equal|match(?:ed|es)?)(?![A-Za-z])", re.I)
_AVERAGE_KE = re.compile(r"(?<![A-Za-z])average kinetic energ(?:y|ies)(?![A-Za-z])", re.I)
_TEMPERATURE = re.compile(r"(?<![A-Za-z])temperatures?(?![A-Za-z])", re.I)
_TOTAL = re.compile(
    r"(?<![A-Za-z])total (?:energy|amount of energy|energies)(?![A-Za-z])|"
    r"(?<![A-Za-z])(?:energy|energies) (?:each body holds|in total)(?![A-Za-z])", re.I)


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
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in (item["q"], h.keyed(item), item["why"]):
            for pat, owner in _OTHER_TOPIC:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: a stem, key or why uses {hit.group(0)!r}, "
                    f"which is {owner} -- {text[:70]!r}"
                )
    print(f"OK  {module.TOPIC[0]} scope: the words endothermic and exothermic, which are "
          "6.1's, appear in no stem, key or why, and neither do 6.2's diagram or 6.4's "
          "calorimetry.")


def equilibrium_keys_equate_an_average(module):
    """EK 6.3.A.3 equates an AVERAGE, never a total.

    A large cool body holds more energy in total than a small warm one, so a key
    that equated totals at thermal equilibrium would be false as well as
    off-framework. Item 6's neighbouring distractor is exactly that sentence.
    """
    n = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        if not (_EQUILIBRIUM.search(item["q"]) or _EQUILIBRIUM.search(h.keyed(item))):
            continue
        key = h.keyed(item)
        n += 1
        hit = _TOTAL.search(key)
        equates_a_total = bool(hit) and bool(_EQUALITY.search(key))
        assert not equates_a_total, (
            f"{module.TOPIC[0]} q{i}: the keyed choice equates {hit.group(0)!r} at "
            f"thermal equilibrium, but EK 6.3.A.3 equates the average kinetic energy and "
            f"hence the temperature -- {key!r}"
        )
        if _EQUALITY.search(key):
            assert _AVERAGE_KE.search(key) or _TEMPERATURE.search(key), (
                f"{module.TOPIC[0]} q{i}: the keyed choice asserts an equality at thermal "
                f"equilibrium without saying it is of the average kinetic energy or of "
                f"the temperature -- {key!r}"
            )
    print(f"OK  {module.TOPIC[0]} average guard: each of the {n} equilibrium item(s) keys "
          "an equality of the average kinetic energy or of the temperature, never of a "
          "total.")


# Items whose key pairs a comparison of the two bodies with a direction of
# transfer. Listed explicitly so the guard cannot quietly stop covering one.
DIRECTION_ITEMS = (9, 28)

_WARMER_SOURCE = re.compile(
    r"from the warmer to the cooler|from body 1 to body 2", re.I)
_COOLER_SOURCE = re.compile(
    r"from the cooler to the warmer|from body 2 to body 1", re.I)
_GREATER_IS_SOURCE = re.compile(
    r"warmer body's particles have the greater average kinetic energy|"
    r"body 1 is warmer", re.I)


def direction_keys_state_both_clauses(module):
    """A direction key must name the transfer AND the comparison behind it.

    Named booleans, not two tuples read in parallel: the body with the greater
    average kinetic energy and the body the energy leaves are the SAME body, and
    a check that lined the two up by position rather than by name is how this
    project rejected a correct key once already.
    """
    for i in DIRECTION_ITEMS:
        key = h.keyed(module.QUESTIONS[i - 1])
        leaves_the_greater = bool(_WARMER_SOURCE.search(key))
        leaves_the_lesser = bool(_COOLER_SOURCE.search(key))
        names_the_comparison = bool(_GREATER_IS_SOURCE.search(key))
        assert leaves_the_greater or leaves_the_lesser, (
            f"{module.TOPIC[0]} q{i}: the keyed choice names no direction of transfer "
            f"at all -- {key!r}"
        )
        assert not (leaves_the_greater and leaves_the_lesser), (
            f"{module.TOPIC[0]} q{i}: the keyed choice names both directions -- {key!r}"
        )
        assert names_the_comparison, (
            f"{module.TOPIC[0]} q{i}: the keyed choice names a direction without saying "
            f"which body has the greater average kinetic energy, so a key that reached "
            f"the right answer by the wrong route would pass -- {key!r}"
        )
        assert leaves_the_greater, (
            f"{module.TOPIC[0]} q{i}: the keyed choice sends the energy INTO the body "
            f"with the greater average kinetic energy, which EK 6.3.A.1 with EK 6.3.A.3 "
            f"forbids -- {key!r}"
        )
    print(f"OK  {module.TOPIC[0]} direction guard: {len(DIRECTION_ITEMS)} direction key(s), "
          "each naming the body with the greater average kinetic energy AND sending the "
          "transfer away from it.")


# ------------------------------------------------------------------- helpers

def gap(table, label, a, b):
    """The signed difference between two tabulated temperatures."""
    return cg.cell(table, label, a) - cg.cell(table, label, b)


def _unique_extreme(values, pick):
    lab = pick(values, key=values.get)
    ties = [k for k, v in values.items() if abs(v - values[lab]) < 1e-12]
    assert ties == [lab], f"the extreme is not unique: {ties} all hold {values[lab]}"
    return lab


# -------------------------------------------------------------- table items

def q10(table, item):
    gaps = {lab: abs(gap(table, lab, T1, T2)) for lab in cg.labels(table)}
    lab = _unique_extreme(gaps, max)
    assert lab == "Pair 1", f"the widest tabulated gap is at {lab}: {gaps}"
    h.shows(item, "Pair 1")
    return (f"the tabulated temperature gaps are {gaps} degrees, whose unique maximum is "
            f"at {lab}, which EK 6.3.A.1 makes the widest gap in average kinetic energy")


def q11(table, item):
    gaps = {lab: gap(table, lab, T1, T2) for lab in cg.labels(table)}
    level = sorted(lab for lab, v in gaps.items() if h6.direction(v)["neither"])
    assert level == ["Pair 3"], f"the pairs already at one temperature are {level}: {gaps}"
    h.shows(item, "Pair 3")
    return (f"exactly one tabulated pair starts at a single temperature, {level[0]}, so "
            f"exactly one is already at thermal equilibrium: {gaps}")


def q12(table, item):
    gaps = {lab: gap(table, lab, T1, T2) for lab in cg.labels(table)}
    # Body 1 rises where it is the COOLER of the two, so where the signed gap is
    # negative. The sign is the whole content of the item.
    rising = {lab: abs(v) for lab, v in gaps.items() if h6.direction(v)["exothermic"]}
    assert set(rising) == {"Pair 2", "Pair 5"}, (
        f"the pairs in which body 1 starts colder recompute as {sorted(rising)}: {gaps}"
    )
    lab = _unique_extreme(rising, max)
    assert lab == "Pair 2", f"the widest such gap is at {lab}: {rising}"
    h.shows(item, "Pair 2")
    return (f"body 1 starts colder in {sorted(rising)}, with gaps {rising} degrees, whose "
            f"unique maximum is at {lab}")


def q13(table, item):
    gaps = {lab: abs(gap(table, lab, T1, T2)) for lab in cg.labels(table)}
    unequal = {lab: v for lab, v in gaps.items() if v > 0}
    assert len(unequal) == 4, f"four tabulated pairs must start unequal: {gaps}"
    lab = _unique_extreme(unequal, min)
    assert lab == "Pair 5", f"the narrowest nonzero gap is at {lab}: {unequal}"
    h.shows(item, "Pair 5")
    return (f"among the tabulated pairs that start apart, the gaps are {unequal} degrees, "
            f"whose unique smallest is at {lab}")


def q14(table, item):
    temps = {lab: cg.cell(table, lab, TEMP) for lab in cg.labels(table)}
    lab = _unique_extreme(temps, max)
    assert lab == "Sample K", f"the highest tabulated temperature is at {lab}: {temps}"
    h.shows(item, "Sample K")
    return (f"the tabulated temperatures are {temps}, whose unique maximum is at {lab}, "
            "which EK 6.3.A.1 makes the greatest average kinetic energy")


def q15(table, item):
    temps = {lab: cg.cell(table, lab, TEMP) for lab in cg.labels(table)}
    lab = _unique_extreme(temps, min)
    assert lab == "Sample M", f"the lowest tabulated temperature is at {lab}: {temps}"
    h.shows(item, "Sample M")
    return (f"the tabulated temperatures are {temps}, whose unique minimum is at {lab}, "
            "which EK 6.3.A.1 makes the smallest average kinetic energy")


def q16(table, item):
    temps = {lab: cg.cell(table, lab, TEMP) for lab in cg.labels(table)}
    groups = {}
    for lab, t in temps.items():
        groups.setdefault(t, []).append(lab)
    shared = sorted(sorted(g) for g in groups.values() if len(g) > 1)
    assert shared == [["Sample L", "Sample P"]], (
        f"the tabulated samples grouped by temperature are {groups}"
    )
    h.shows(item, "Sample L and Sample P")
    return (f"grouping the tabulated temperatures gives {groups}, with exactly one pair "
            "sharing a value and so, under EK 6.3.A.3, one average kinetic energy")


def q17(table, item):
    gaps = {lab: gap(table, lab, BLOCK, WATER) for lab in cg.labels(table)}
    # Energy enters the block where the block starts COLDER, so where the signed
    # gap is negative.
    into_block = sorted(lab for lab, v in gaps.items() if h6.direction(v)["exothermic"])
    assert into_block == ["Trial 5"], (
        f"the trials in which the block starts colder recompute as {into_block}: {gaps}"
    )
    assert cg.cell(table, "Trial 5", FINAL) > cg.cell(table, "Trial 5", BLOCK), (
        "the measured final temperature must be above the block's starting value, or the "
        "block did not gain energy at all"
    )
    h.shows(item, "Trial 5")
    return (f"exactly one tabulated trial starts with the block below the water, "
            f"{into_block[0]}, and its measured final temperature is above the block's "
            f"start: {gaps}")


def q18(table, item):
    gaps = {lab: gap(table, lab, BLOCK, WATER) for lab in cg.labels(table)}
    level = sorted(lab for lab, v in gaps.items() if h6.direction(v)["neither"])
    assert level == ["Trial 3"], f"the trials starting at one temperature are {level}: {gaps}"
    h.shows(item, "Trial 3")
    return (f"exactly one tabulated trial starts with block and water at one temperature, "
            f"{level[0]}, so exactly one has nothing to transfer on balance: {gaps}")


def q19(table, item):
    falls = {lab: cg.cell(table, lab, BLOCK) - cg.cell(table, lab, FINAL)
             for lab in cg.labels(table)}
    lab = _unique_extreme(falls, max)
    assert falls[lab] > 0, f"the extreme trial {lab} does not cool the block at all: {falls}"
    assert lab == "Trial 1", f"the largest fall in the block is at {lab}: {falls}"
    h.shows(item, "Trial 1")
    return (f"the block's tabulated fall in each trial is {falls} degrees, whose unique "
            f"maximum is at {lab}")


def q20(table, item):
    between = {}
    for lab in cg.labels(table):
        b, w, f = (cg.cell(table, lab, BLOCK), cg.cell(table, lab, WATER),
                   cg.cell(table, lab, FINAL))
        assert min(b, w) <= f <= max(b, w), (
            f"{lab}'s measured final temperature {f} does not lie between its starting "
            f"values {b} and {w}, so the item's premise is false of the table it is "
            f"asked of"
        )
        between[lab] = (min(b, w), f, max(b, w))
    h.shows(item, "so the warmer falls and the cooler rises until the two meet")
    return (f"every tabulated final temperature lies between that trial's two starting "
            f"values: {between}")


TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16,
                17: q17, 18: q18, 19: q19, 20: q20}

NUMERIC = {}


CLAIMS = [
 ("They have a greater average kinetic energy",
  "EK 6.3.A.1, verbatim in substance: the particles in a warmer body have a greater average kinetic energy than those in a cooler body."),
 ("The transfer of energy",
  "EK 6.3.A.2 states that collisions between particles in thermal contact can result in the transfer of energy; it is energy that crosses, not matter."),
 ("Heat transfer, heat exchange, and transfer of energy as heat",
  "EK 6.3.A.2 gives the process exactly these three names, in these words. No other term in the choices is one the framework attaches to it here."),
 ("Thermal equilibrium",
  "EK 6.3.A.3 states that eventually thermal equilibrium is reached as the particles continue to collide."),
 ("The average kinetic energy of their particles, and hence their temperatures",
  "EK 6.3.A.3, verbatim in substance: at thermal equilibrium the average kinetic energy of both bodies is the same, and hence their temperatures are the same."),
 ("what the framework equates is the average kinetic energy of the particles, and hence the temperatures",
  "EK 6.3.A.3 equates an average, and a body of many more particles can hold far more energy in total at the same average, so the totals are not made equal by reaching equilibrium."),
 ("No, the particles continue to collide",
  "EK 6.3.A.3 says thermal equilibrium is reached AS THE PARTICLES CONTINUE TO COLLIDE, so equilibrium is the absence of a net transfer rather than of collisions."),
 ("Through collisions between the particles of the two bodies",
  "EK 6.3.A.2 makes collisions between particles in thermal contact the mechanism of the transfer, which is the particulate account suggested skill 6.E asks for."),
 ("From the warmer to the cooler, because the warmer body's particles have the greater average kinetic energy and the two must finish equal",
  "EK 6.3.A.1 gives the warmer body the greater average and EK 6.3.A.3 requires the two to end the same, so the greater must fall. Both clauses are in the key because the swap is what this topic is exposed to."),
 ("Pair 1",
  "EK 6.3.A.1 ties a wider temperature gap to a wider gap in average kinetic energy. q10 recomputes every tabulated gap and checks the maximum is unique."),
 ("Pair 3",
  "EK 6.3.A.3 makes equal temperatures the mark of equal averages, which is thermal equilibrium. q11 recomputes every gap and checks exactly one is zero."),
 ("Pair 2",
  "EK 6.3.A.1 with EK 6.3.A.3 send the transfer away from the greater average, so body 1 rises where it starts colder. q12 recomputes the SIGN of every gap and checks the widest such case is unique."),
 ("Pair 5",
  "EK 6.3.A.3 has the two temperatures finish the same, so the narrowest starting gap needs the smallest change. q13 recomputes the gaps and excludes the pair that starts equal."),
 ("Sample K",
  "EK 6.3.A.1 makes the warmer body's average the greater. q14 recomputes the tabulated temperatures and checks the maximum is unique."),
 ("Sample M",
  "The same statement read downward. q15 checks the minimum is unique."),
 ("Sample L and Sample P",
  "EK 6.3.A.3 pairs equal averages with equal temperatures. q16 groups the tabulated temperatures and checks exactly one pair shares a value."),
 ("Trial 5",
  "EK 6.3.A.1 with EK 6.3.A.3 send the transfer into whichever body starts colder. q17 recomputes the sign of every tabulated gap, finds exactly one trial with the block below the water, and checks its measured final temperature really is above the block's start."),
 ("Trial 3",
  "EK 6.3.A.3 makes equal temperatures the condition of equilibrium. q18 recomputes every gap and checks exactly one trial starts level."),
 ("Trial 1",
  "EK 6.3.A.3 has both bodies finish at one temperature, so the block's fall is its start less the measured final. q19 recomputes every fall and checks the maximum is unique and really a fall."),
 ("so the warmer falls and the cooler rises until the two meet",
  "EK 6.3.A.1 with EK 6.3.A.3. q20 checks the premise against the table itself: every measured final temperature is verified to lie between that trial's two starting values."),
 ("there is no net transfer, because their average kinetic energies are already equal",
  "EK 6.3.A.3 describes equilibrium as equal averages while the particles continue to collide, so the collisions persist and the net transfer does not."),
 ("The framework uses heat for the transfer of energy between bodies, not for something a body contains",
  "EK 6.3.A.2 attaches heat transfer, heat exchange and transfer of energy as heat to the PROCESS by which colliding particles pass energy, so the word names a transfer rather than a store."),
 ("Their average kinetic energy is the greater of the two",
  "EK 6.3.A.1 states exactly this comparison, and it is of the average rather than of the number of particles or of any total."),
 ("They are the same, because equal temperatures go with equal average kinetic energies",
  "EK 6.3.A.3 pairs the same average kinetic energy with the same temperature, and EK 6.3.A.1 makes any difference in average show up as a difference in temperature."),
 ("closer together than they were, but not yet the same",
  "EK 6.3.A.2 transfers energy while the bodies are in contact and EK 6.3.A.3 has that transfer carry the two averages together over many collisions, so an interrupted contact leaves them partway."),
 ("passed energy from the block's particles to the water's until the two average kinetic energies matched",
  "EK 6.3.A.2 supplies the collisions, EK 6.3.A.1 makes the hotter block the body with the greater average, and EK 6.3.A.3 supplies the endpoint."),
 ("through repeated collisions, which take time to bring the two averages together",
  "EK 6.3.A.3 says equilibrium is reached EVENTUALLY, as the particles CONTINUE to collide, so it arrives over the course of many of the transfers EK 6.3.A.2 describes."),
 ("Body 1 is warmer, and energy will pass from body 1 to body 2",
  "EK 6.3.A.1 makes the greater average kinetic energy the mark of the warmer body, and EK 6.3.A.3 requires the two averages to finish equal, so body 1's must fall."),
 ("A thermometer reading is macroscopic, the average kinetic energy of the particles is particulate, and the framework ties one to the other",
  "EK 6.3.A.1 and EK 6.3.A.3 both state that link directly, which is the particulate-to-macroscopic connection suggested skill 6.E names."),
 ("continuing until the two average kinetic energies are the same",
  "EK 6.3.A.2 supplies the collisions and EK 6.3.A.3 the endpoint, which is the same AVERAGE kinetic energy in both bodies and hence the same temperature, not the same total."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, how do the particles compare?"
        no_figure_language(mod)

    def sixone_word_creeps_in(mod, cl):
        mod.QUESTIONS[0]["q"] = (
            "Is the warming of a cooler body by a warmer one an endothermic change for it?")
        no_other_topic(mod)

    def key_equates_totals(mod, cl):
        # Item 6's own neighbouring distractor, promoted to the key. It reads
        # perfectly well and it is false: a large cool body holds more energy in
        # total than a small warm one at the same temperature.
        mod.QUESTIONS[5]["ans"] = 1
        cl[5] = ("thermal equilibrium means the two bodies hold equal total energy", cl[5][1])
        equilibrium_keys_equate_an_average(mod)

    def direction_key_reversed(mod, cl):
        # The key moved to the choice that gives the warmer body the greater
        # average and then sends the energy the WRONG way. The choices are
        # untouched, so they stay distinct and the new anchor matches only the
        # new key; only the direction guard can reject it.
        mod.QUESTIONS[8]["ans"] = 1
        cl[8] = ("From the cooler to the warmer, because the warmer body's particles have "
                 "the greater average kinetic energy", cl[8][1])
        direction_keys_state_both_clauses(mod)

    def direction_key_drops_its_reason(mod, cl):
        ch = list(mod.QUESTIONS[27]["choices"])
        ch[0] = "Energy will pass from body 1 to body 2"
        mod.QUESTIONS[27]["choices"] = ch
        cl[27] = ("Energy will pass from body 1 to body 2", cl[27][1])
        direction_keys_state_both_clauses(mod)

    def contact_gap_moved(mod, cl):
        mod.QUESTIONS[9]["table"] = dict(
            headers=h6_3._T_CONTACT["headers"],
            rows=[["Pair 1", "85", "20"], ["Pair 2", "15", "140"],
                  ["Pair 3", "30", "30"], ["Pair 4", "5", "-10"],
                  ["Pair 5", "60", "62"]])

    def contact_signs_flipped(mod, cl):
        # The two columns exchanged. Every gap keeps its size and every one
        # changes sign, so a check that compared magnitudes would see nothing
        # while the keyed pair for "body 1 becomes warmer" becomes false.
        mod.QUESTIONS[11]["table"] = dict(
            headers=h6_3._T_CONTACT["headers"],
            rows=[[lab, b, a] for lab, a, b in h6_3._T_CONTACT["rows"]])

    def second_shared_temperature(mod, cl):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h6_3._T_KE["headers"],
            rows=[["Sample K", "120"], ["Sample L", "25"], ["Sample M", "-40"],
                  ["Sample N", "120"], ["Sample P", "25"]])

    def block_already_warmer(mod, cl):
        # The one trial in which the block starts colder turned round, so no
        # trial keys the answer any more.
        mod.QUESTIONS[16]["table"] = dict(
            headers=h6_3._T_EQUIL["headers"],
            rows=[["Trial 1", "95", "20", "28"], ["Trial 2", "80", "20", "24"],
                  ["Trial 3", "20", "20", "20"], ["Trial 4", "60", "55", "56"],
                  ["Trial 5", "50", "45", "46"]])

    def final_outside_the_starting_range(mod, cl):
        # A measured final temperature put OUTSIDE its trial's two starting
        # values. The item's whole premise is that this never happens, and
        # nothing but q20's per-row check looks at it.
        mod.QUESTIONS[19]["table"] = dict(
            headers=h6_3._T_EQUIL["headers"],
            rows=[["Trial 1", "95", "20", "28"], ["Trial 2", "80", "20", "24"],
                  ["Trial 3", "20", "20", "20"], ["Trial 4", "60", "55", "72"],
                  ["Trial 5", "10", "45", "41"]])

    return [("a stem referring to a diagram the bank cannot show", figure_language),
            ("a stem borrowing 6.1's word endothermic", sixone_word_creeps_in),
            ("a key equating the two bodies' TOTAL energies at thermal equilibrium",
             key_equates_totals),
            ("a direction key sending the energy into the greater average kinetic energy",
             direction_key_reversed),
            ("a direction key that names a direction without naming the comparison behind it",
             direction_key_drops_its_reason),
            ("the widest tabulated temperature gap moved off the keyed pair", contact_gap_moved),
            ("the two tabulated temperature columns exchanged, which flips every sign and "
             "preserves every magnitude", contact_signs_flipped),
            ("a second tabulated pair of samples made to share a temperature",
             second_shared_temperature),
            ("the one tabulated trial with the block starting colder turned round",
             block_already_warmer),
            ("a measured final temperature put outside its trial's two starting values",
             final_outside_the_starting_range)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h6.selftest()
    h.selftest(h6_3, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h6_3)
no_other_topic(h6_3)
equilibrium_keys_equate_an_average(h6_3)
direction_keys_state_both_clauses(h6_3)
h.run(h6_3, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
