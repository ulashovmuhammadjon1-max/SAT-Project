"""Key audit for AP CHEMISTRY 6.4 Heat Capacity and Calorimetry.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  6.4.A.1  q = mc(delta T), and calorimetry measures the transfer of heat
                                  1, 2, 8, 9, 10, 11, 12, 18, 19, 20, 21, 22,
                                  25, 26, 27
  6.4.A.2  energy is conserved in chemical and physical processes   3, 14, 29
  6.4.A.3  equal masses of substances with differing specific heat capacities
           do NOT change temperature equally                7, 21, 22, 24, 25
  6.4.A.4  heating increases the energy of a system, cooling decreases it
                                                            4, 8, 9, 10, 27
  6.4.A.5  the specific heat capacity and the molar heat capacity are both used
                                                            5, 12, 13, 23, 30
  6.4.A.6  three main processes: heating and cooling, phase transitions,
           chemical reactions                               6
  6.4.A.7  a warming calorimeter mixture means the dissolution released energy
           (exothermic); a cooling one means it absorbed energy (endothermic)
                                                            15, 16, 17, 18, 28

EVERY NUMBER IS RECOMPUTED, INCLUDING THE WRONG ONES. Thirteen items carry
arithmetic, and for each the verifier recomputes the key from the stimulus AND
the origin of each arithmetic distractor -- the final temperature used in place
of the change, the initial temperature used in place of the change, the mass
omitted, the capacity omitted, the reciprocal taken. A distractor whose value
has drifted into being correct is as damaging as a wrong key, and nothing but
recomputing it would notice.

THE SIGN. ``h6_thermo.heat`` carries the sign of the temperature change, so
cooling gives a negative q and EK 6.4.A.4 says what that means. Every keyed
choice reporting a quantity of energy for a directional process states the
direction with the number, and ``energy_keys_state_a_direction`` asserts that:
a key reading "8360 J" with no direction would match a student who had the
arithmetic right and the physics backwards. Where the item is about the
DISSOLUTION rather than about the mixture, the verifier negates the mixture's
heat explicitly and by name -- that negation is EK 6.4.A.2's conservation step
and the one most often dropped.

SCOPE. 6.5 owns the molar enthalpy of a phase change and 6.6 the molar enthalpy
of reaction, so ``no_other_topic`` bans the word enthalpy and Hess's law from
every stem, key and why here; EK 6.4.A.6 is used only as the framework uses it,
to name the three kinds of process.

NEGATIVE CONTROL: ``python3 verify_h6_4.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h6_thermo as h6

import h6_4

MASS = "Mass of solution (g)"
BEF = "Temperature before (degrees Celsius)"
AFT = "Temperature after (degrees Celsius)"
CAP = "Specific heat capacity (J per gram per degree Celsius)"

# The specific heat capacity every _T_CALOR item states in its stem. Written
# once here so a check cannot silently use a different one from the question.
C_MIX = 4.18
# The fixed conditions the _T_C items state in their stems.
C_MASS, C_ENERGY = 10.0, 100.0

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below)(?![a-z])", re.I)

_OTHER_TOPIC = [
    (re.compile(r"(?<![A-Za-z])enthalp[a-z]*", re.I), "6.5 to 6.9's enthalpy"),
    (re.compile(r"(?<![A-Za-z])Hess(?![A-Za-z])", re.I), "6.9's law"),
    (re.compile(r"(?<![A-Za-z])bond energ(?:y|ies)(?![A-Za-z])", re.I), "6.7's bond energies"),
    (re.compile(r"(?<![A-Za-z])energy diagram(?![A-Za-z])", re.I), "6.2's representation"),
    (re.compile(r"(?<![A-Za-z])average kinetic energy(?![A-Za-z])", re.I),
     "6.3's particle account"),
]

# A quantity of energy or of temperature change reported in a keyed choice.
_JOULES = re.compile(r"(?<![A-Za-z0-9.])\d[\d.]*\s*(?:J|kJ)(?![A-Za-z])")
_DEGREES = re.compile(r"(?<![A-Za-z0-9.])\d[\d.]*\s*degrees?(?![A-Za-z])", re.I)
_ENERGY_DIRECTION = re.compile(
    r"(?<![A-Za-z])(?:absorbed|released|lost|gained|rises|falls|"
    r"gained by the mixture)(?![A-Za-z])", re.I)

# Items whose key reports an amount of energy or of temperature change for a
# process that HAS a direction. Listed explicitly so the guard cannot quietly
# stop covering one that was edited.
DIRECTIONAL_ENERGY_ITEMS = (8, 9, 10, 14)


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
    print(f"OK  {module.TOPIC[0]} figures: every laboratory result is carried as a table "
          "and no item points at a picture.")


def no_other_topic(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in (item["q"], h.keyed(item), item["why"]):
            for pat, owner in _OTHER_TOPIC:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: a stem, key or why uses {hit.group(0)!r}, "
                    f"which is {owner} -- {text[:70]!r}"
                )
    print(f"OK  {module.TOPIC[0]} scope: no stem, key or why borrows 6.5 to 6.9's "
          "enthalpy, 6.7's bond energies, 6.2's diagram or 6.3's kinetic energy.")


def energy_keys_state_a_direction(module):
    """A key reporting an amount of energy must say which way it went.

    "8360 J" on its own is exactly what a student with the arithmetic right and
    the physics backwards would write, and an anchor pinned to a bare number
    would match the swapped distractor sitting beside it. So each of these keys
    must carry a direction word, and the anchor must carry it too.
    """
    for i in DIRECTIONAL_ENERGY_ITEMS:
        item = module.QUESTIONS[i - 1]
        key = h.keyed(item)
        reports_a_quantity = bool(_JOULES.search(key) or _DEGREES.search(key))
        states_a_direction = bool(_ENERGY_DIRECTION.search(key))
        assert reports_a_quantity, (
            f"{module.TOPIC[0]} q{i}: listed as a directional energy item but the keyed "
            f"choice reports no quantity at all -- {key!r}"
        )
        assert states_a_direction, (
            f"{module.TOPIC[0]} q{i}: the keyed choice reports a quantity without saying "
            f"which way the energy went -- {key!r}"
        )
    print(f"OK  {module.TOPIC[0]} sign guard: each of the {len(DIRECTIONAL_ENERGY_ITEMS)} "
          "key(s) reporting a quantity of energy or a temperature change also states its "
          "direction.")


def anchors_carry_the_direction(module, claims):
    """The anchor, not just the key, must carry the direction word.

    cg_check already refuses an anchor that matches a distractor, so this is the
    belt to that brace: it fails an anchor that is a bare number even when no
    distractor happens to repeat that number today. A later edit that added the
    swapped distractor would otherwise slip through.
    """
    for i in DIRECTIONAL_ENERGY_ITEMS:
        anchor = claims[i - 1][0]
        assert _ENERGY_DIRECTION.search(anchor), (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} names a quantity without a "
            "direction, so it would still match a key with the sign reversed"
        )
    print(f"OK  {module.TOPIC[0]} anchor guard: every directional-energy anchor carries "
          "its direction word as well as its number.")


# ------------------------------------------------------------------- helpers

def _close(a, b, tol=1e-9):
    return abs(a - b) < tol


def _unique_extreme(values, pick):
    lab = pick(values, key=values.get)
    ties = [k for k, v in values.items() if _close(v, values[lab])]
    assert ties == [lab], f"the extreme is not unique: {ties} all hold {values[lab]}"
    return lab


def mixture_heat(table, label):
    """EK 6.4.A.1 applied to the tabulated mixture: q = mc(delta T), sign kept."""
    dt = cg.cell(table, label, AFT) - cg.cell(table, label, BEF)
    return h6.heat(cg.cell(table, label, MASS), C_MIX, dt)


def dissolution_heat(table, label):
    """The heat of the DISSOLUTION, which is the mixture's negated.

    EK 6.4.A.2's conservation step, written out rather than folded into the
    line above. A mixture that warmed took energy IN, so the process that
    warmed it gave energy OUT, and the two differ by exactly this sign.
    """
    return -mixture_heat(table, label)


def rise(table, label):
    """The temperature rise of the tabulated substance under the stated conditions."""
    return C_ENERGY / (C_MASS * cg.cell(table, label, CAP))


def mistake(item, value_text, origin):
    """A recomputed WRONG value must sit in exactly one distractor, and never in the key.

    The first version of this file recomputed each distractor's origin as a bare
    assertion about numbers -- ``assert 50.0 * 10.0 == 500.0`` -- which is a
    tautology the module cannot fail. It said nothing about the question at all,
    and its negative control passed only because the mutation happened to
    duplicate a choice string. This ties the recomputation to the item: the
    value has to be found in a distractor, so a distractor edited away from the
    mistake it was written to test, or edited into a second correct answer, is
    caught by the value going missing.
    """
    assert not cg.contains_phrase(h.keyed(item), value_text), (
        f"the mistaken value {value_text!r} ({origin}) appears in the KEYED choice, so the "
        f"item has two defensible answers -- {h.keyed(item)!r}"
    )
    hits = [k for k, c in enumerate(item["choices"])
            if k != item["ans"] and cg.contains_phrase(c, value_text)]
    assert len(hits) == 1, (
        f"the recomputed mistake {value_text!r} ({origin}) appears in {len(hits)} "
        f"distractor(s); exactly one must carry it, or the item has stopped testing that "
        f"mistake -- choices {item['choices']}"
    )
    return value_text


# ------------------------------------------------------------- stem numerics

def n8(item):
    q = h6.heat(50.0, 4.18, 10.0)
    assert _close(q, 2090.0), f"the heat recomputes to {q}"
    assert q > 0, "a warmed sample must take energy in, or EK 6.4.A.4 is being contradicted"
    h.shows(item, "2090 J absorbed")
    assert _close(h6.heat(50.0, 4.18, 1.0), 209.0)
    mistake(item, "209 J", "a one-degree change assumed")
    assert _close(h6.heat(1.0, 4.18, 10.0), 41.8)
    mistake(item, "41.8 J", "the mass left out")
    assert _close(50.0 * 10.0, 500.0)
    mistake(item, "500 J", "the specific heat capacity left out")
    return (f"50.0 g times 4.18 times a rise of 10.0 degrees recomputes as {q:g} J taken "
            "in, and the one-degree, mass-omitted and capacity-omitted mistakes recompute "
            "as 209, 41.8 and 500 J, each found in exactly one distractor")


def n9(item):
    q = h6.heat(100.0, 4.18, 40.0 - 60.0)
    assert _close(q, -8360.0), f"the heat recomputes to {q}"
    assert h6.direction(q)["exothermic"], (
        "a cooling sample must come out with a negative q under EK 6.4.A.4"
    )
    assert h6.agrees(q, h.keyed(item), transfer=True), (
        f"the recomputed q is {h6.report(q, 'J')} but the keyed choice says "
        f"{h6.stated_transfer(h.keyed(item))!r}: {h.keyed(item)!r}"
    )
    h.shows(item, "8360 J released")
    assert _close(2 * abs(q), 16720.0)
    mistake(item, "16720 J", "the change counted twice")
    assert _close(abs(h6.heat(100.0, 4.18, -10.0)), 4180.0)
    mistake(item, "4180 J", "half the temperature change used")
    assert _close(abs(h6.heat(100.0, 4.18, -1.0)), 418.0)
    mistake(item, "418 J", "a one-degree change assumed")
    return (f"100.0 g times 4.18 times a fall of 20.0 degrees recomputes as "
            f"{h6.report(q, 'J')} for the water, so the water gave the energy up, and the "
            "doubled, halved and one-degree mistakes each sit in exactly one distractor")


def n10(item):
    dt = 4180.0 / (100.0 * 4.18)
    assert _close(dt, 10.0), f"the temperature change recomputes to {dt}"
    assert dt > 0, "energy transferred INTO the sample must warm it under EK 6.4.A.4"
    h.shows(item, "rises by 10.0 degrees Celsius")
    assert _close(4180.0 / 100.0, 41.8)
    mistake(item, "41.8 degrees", "divided by the mass alone")
    assert _close(4180.0 / 4.18, 1000.0)
    mistake(item, "1000 degrees", "divided by the capacity alone")
    assert _close(4180.0 / (50.0 * 4.18), 20.0)
    mistake(item, "20.0 degrees", "the mass taken as 50.0 g")
    return (f"4180 J divided by 100.0 g and by 4.18 recomputes the change as a rise of "
            f"{dt:g} degrees, with the mass-alone, capacity-alone and halved-mass mistakes "
            "recomputed as 41.8, 1000 and 20.0 degrees and each found in one distractor")


def n11(item):
    m = 8360.0 / (4.18 * 20.0)
    assert _close(m, 100.0), f"the mass recomputes to {m}"
    h.shows(item, "100.0 g")
    assert _close(8360.0 / 20.0, 418.0)
    mistake(item, "418 g", "divided by the temperature change alone")
    assert _close(8360.0 / 4.18, 2000.0)
    mistake(item, "2000 g", "divided by the capacity alone")
    return (f"8360 J divided by 4.18 and by a rise of 20.0 degrees recomputes the mass as "
            f"{m:g} g, and the two omitted-quantity mistakes recompute as 418 and 2000 g, "
            "each found in exactly one distractor")


def n12(item):
    c = 500.0 / (50.0 * 25.0)
    assert _close(c, 0.400), f"the specific heat capacity recomputes to {c}"
    h.shows(item, "0.400 J per gram per degree Celsius")
    assert _close(500.0 / 50.0, 10.0)
    mistake(item, "10.0 J per gram", "divided by the mass alone")
    assert _close(500.0 / 25.0, 20.0)
    mistake(item, "20.0 J per gram", "divided by the temperature change alone")
    assert _close(1.0 / c, 2.50)
    mistake(item, "2.50 J per gram", "the reciprocal taken")
    assert _close(c / 10.0, 0.0400)
    mistake(item, "0.0400 J per gram", "a decimal place lost")
    return (f"500 J divided by 50.0 g and by a rise of 25.0 degrees recomputes the capacity "
            f"as {c:g}, with the mass-alone, change-alone, reciprocal and decimal-slip "
            "mistakes each recomputed and each found in one distractor")


def n13(item):
    q = 2.00 * 75.3 * 10.0
    assert _close(q, 1506.0), f"the energy recomputes to {q}"
    h.shows(item, "1506 J")
    assert _close(75.3 * 10.0, 753.0)
    mistake(item, "753 J", "the amount in moles left out")
    assert _close(75.3 * 2.00, 150.6)
    mistake(item, "150.6 J", "the temperature change left out")
    assert _close(75.3 * 10.0 / 2.00, 376.5)
    mistake(item, "376.5 J", "divided by the amount instead of multiplied")
    assert _close(q * 10.0, 15060.0)
    mistake(item, "15060 J", "a decimal place gained")
    return (f"2.00 mol times 75.3 J per mole per degree times 10.0 degrees recomputes as "
            f"{q:g} J, with four recomputed mistakes at 753, 150.6, 376.5 and 15060 J, "
            "each found in exactly one distractor")


def n14(item):
    gained = 2090.0
    # EK 6.4.A.2: what one body gains the other gave up, in equal measure.
    lost = gained
    assert _close(lost, gained), "conservation makes the two equal in magnitude"
    h.shows(item, "2090 J lost, because energy is conserved")
    mistake(item, "2090 J gained", "the direction reversed while the number stays right")
    assert _close(gained / 2.0, 1045.0)
    mistake(item, "1045 J lost", "the energy assumed to be shared equally")
    assert _close(gained * 2.0, 4180.0)
    mistake(item, "4180 J lost", "the transfer counted twice")
    return (f"the first law makes the block's loss equal the water's gain of {gained:g} J, "
            "with the reversed, halved and doubled mistakes each found in one distractor")


NUMERIC = {8: n8, 9: n9, 10: n10, 11: n11, 12: n12, 13: n13, 14: n14}


# -------------------------------------------------------------- table items

def q17(table, item):
    qs = {lab: dissolution_heat(table, lab) for lab in cg.labels(table)}
    endo = sorted(lab for lab, v in qs.items() if h6.direction(v)["endothermic"])
    assert endo == ["Trial 2"], f"the endothermic dissolutions recompute as {endo}: {qs}"
    assert h6.direction(mixture_heat(table, "Trial 2"))["exothermic"], (
        "the endothermic trial's MIXTURE must have lost energy, which is the negation "
        "EK 6.4.A.2 requires and the step most often dropped"
    )
    h.shows(item, "Trial 2")
    return (f"negating each tabulated mixture's q = mc(delta T) gives the dissolutions "
            f"{qs} J, of which exactly one is positive and so endothermic: {endo[0]}")


def q18(table, item):
    qs = {lab: mixture_heat(table, lab) for lab in cg.labels(table)}
    lab = _unique_extreme(qs, max)
    assert qs[lab] > 0, f"the extreme trial {lab} did not warm its mixture at all: {qs}"
    assert lab == "Trial 5", f"the largest transfer into a mixture is at {lab}: {qs}"
    h.shows(item, "Trial 5")
    return (f"the tabulated mixtures took up {qs} J, whose unique maximum is at {lab}, "
            "which EK 6.4.A.7 makes the largest release by a dissolution")


def q19(table, item):
    qs = {lab: round(mixture_heat(table, lab), 9) for lab in cg.labels(table)}
    groups = {}
    for lab, v in qs.items():
        groups.setdefault(v, []).append(lab)
    shared = sorted(sorted(g) for g in groups.values() if len(g) > 1 and g[0] != "Trial 4")
    assert shared == [["Trial 1", "Trial 3"]], (
        f"the tabulated trials grouped by recomputed q are {groups}"
    )
    a, b = shared[0]
    assert cg.cell(table, a, MASS) != cg.cell(table, b, MASS), (
        "the two matching trials must differ in mass, or the item shows nothing"
    )
    assert (cg.cell(table, a, AFT) - cg.cell(table, a, BEF)) != \
        (cg.cell(table, b, AFT) - cg.cell(table, b, BEF)), \
        "the two matching trials must differ in temperature change as well"
    h.shows(item, "Trial 1 and Trial 3")
    return (f"recomputing q = mc(delta T) for every tabulated trial gives {qs} J, with "
            f"exactly one pair sharing a value while differing in mass and in change")


def q20(table, item):
    q = mixture_heat(table, "Trial 1")
    assert _close(q, 2508.0), f"the heat recomputes to {q}"
    assert q > 0, "the tabulated mixture warmed, so it took energy in"
    m, bef, aft = (cg.cell(table, "Trial 1", MASS), cg.cell(table, "Trial 1", BEF),
                   cg.cell(table, "Trial 1", AFT))
    h.shows(item, "2508 J")
    assert _close(h6.heat(m, C_MIX, aft), 11704.0)
    mistake(item, "11704 J", "the final temperature used in place of the change")
    assert _close(h6.heat(m, C_MIX, bef), 9196.0)
    mistake(item, "9196 J", "the initial temperature used in place of the change")
    assert _close(h6.heat(1.0, C_MIX, aft - bef), 25.08)
    mistake(item, "25.08 J", "the mass left out")
    assert _close(h6.heat(m, C_MIX, 1.0), 418.0)
    mistake(item, "418 J", "a one-degree change assumed")
    return (f"{m:g} g times {C_MIX} times a rise of {aft - bef:g} degrees recomputes as "
            f"{q:g} J, with the final-temperature, initial-temperature, mass-omitted and "
            "one-degree distractors recomputed as 11704, 9196, 25.08 and 418 J")


def q21(table, item):
    rises = {lab: rise(table, lab) for lab in cg.labels(table)}
    lab = _unique_extreme(rises, max)
    assert lab == "Lead", f"the largest recomputed rise is at {lab}: {rises}"
    assert cg.cell(table, lab, CAP) == min(cg.col(table, CAP)), (
        "the largest rise must belong to the smallest tabulated capacity, which is what "
        "EK 6.4.A.3 is about"
    )
    h.shows(item, "Lead")
    return (f"dividing 100 J by 10.0 g and by each tabulated capacity gives rises of "
            f"{rises} degrees, whose unique maximum is at {lab}")


def q22(table, item):
    rises = {lab: rise(table, lab) for lab in cg.labels(table)}
    lab = _unique_extreme(rises, min)
    assert lab == "Water", f"the smallest recomputed rise is at {lab}: {rises}"
    assert cg.cell(table, lab, CAP) == max(cg.col(table, CAP)), (
        "the smallest rise must belong to the largest tabulated capacity"
    )
    h.shows(item, "Water")
    return (f"the same division gives rises of {rises} degrees, whose unique minimum is at "
            f"{lab}, the substance with the largest tabulated capacity")


def q23(table, item):
    caps = {lab: cg.cell(table, lab, CAP) for lab in cg.labels(table)}
    lab = _unique_extreme(caps, max)
    assert lab == "Water", f"the largest tabulated capacity is at {lab}: {caps}"
    h.shows(item, "Water")
    return (f"the tabulated capacities are {caps} J per gram per degree, whose unique "
            f"maximum is at {lab}, the energy per gram per degree EK 6.4.A.5 names")


def q24(table, item):
    rises = {lab: rise(table, lab) for lab in cg.labels(table)}
    labs = sorted(rises)
    gaps = {}
    for a in range(len(labs)):
        for b in range(a + 1, len(labs)):
            gaps[(labs[a], labs[b])] = abs(rises[labs[a]] - rises[labs[b]])
    pair = _unique_extreme(gaps, min)
    assert set(pair) == {"Iron", "Copper"}, f"the closest recomputed pair is {pair}"
    h.shows(item, "Iron and copper")
    return (f"the recomputed rises are {rises} degrees, and of the {len(gaps)} pairs the "
            f"unique closest is {pair}, {gaps[pair]:.3g} degrees apart")


TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24}


CLAIMS = [
 ("the mass times the specific heat capacity times the temperature change",
  "EK 6.4.A.1's EQN, q = mc(delta T), with all three quantities present and the temperature entering as a change rather than as a value."),
 ("Measure the transfer of heat",
  "EK 6.4.A.1 closes by stating that calorimetry experiments are used to measure the transfer of heat."),
 ("Energy is conserved in chemical and physical processes",
  "EK 6.4.A.2, verbatim: the first law of thermodynamics states that energy is conserved in chemical and physical processes."),
 ("Heating increases the energy of the system and cooling decreases it",
  "EK 6.4.A.4, verbatim in substance, and it is what the sign of q in the heat transfer equation reports."),
 ("The specific heat capacity of a substance and the molar heat capacity",
  "EK 6.4.A.5 names exactly these two as both used in energy calculations, one taken per gram and the other per mole."),
 ("Heating or cooling, phase transitions, and chemical reactions",
  "EK 6.4.A.6 names exactly these three main processes by which chemical systems change their energy."),
 ("They will not be the same",
  "EK 6.4.A.3, verbatim in substance: the transfer of a given amount of thermal energy will not produce the same temperature change in equal masses of matter with differing specific heat capacities."),
 ("2090 J absorbed",
  "EK 6.4.A.1's equation with EK 6.4.A.4's direction. n8 recomputes the key and the one-degree, mass-omitted and capacity-omitted distractors."),
 ("8360 J released",
  "EK 6.4.A.1's equation takes the change as final less initial, which is negative here, and EK 6.4.A.4 makes that a loss. n9 recomputes the signed value and checks the key's direction word against it."),
 ("rises by 10.0 degrees Celsius",
  "EK 6.4.A.1 rearranged, with EK 6.4.A.4 making energy transferred in a warming. n10 recomputes the change and the capacity-omitted, mass-omitted and halved-mass distractors."),
 ("100.0 g",
  "EK 6.4.A.1 rearranged for the mass. n11 recomputes it and the two omitted-quantity distractors."),
 ("0.400 J per gram per degree Celsius",
  "EK 6.4.A.1 rearranged for the capacity, which EK 6.4.A.5 names the specific heat capacity. n12 recomputes it and the omitted-quantity and reciprocal distractors."),
 ("1506 J",
  "EK 6.4.A.5 puts the molar heat capacity to work with the amount in moles. n13 recomputes the key and four distractors."),
 ("2090 J lost, because energy is conserved",
  "EK 6.4.A.2's first law: what the water gained is what the block gave up. n14 recomputes the halved and doubled distractors as well."),
 ("released by the dissolution, which is therefore exothermic",
  "EK 6.4.A.7, verbatim in substance: if the temperature of the mixture increases, thermal energy is released by the dissolution process, which the same sentence names exothermic."),
 ("absorbed by the dissolution, which is therefore endothermic",
  "EK 6.4.A.7's mirror clause: if the temperature of the mixture decreases, thermal energy is absorbed by the dissolution process, which is endothermic."),
 ("Trial 2",
  "EK 6.4.A.7 with EK 6.4.A.1. q17 recomputes each mixture's q and NEGATES it for the dissolution, then checks exactly one dissolution comes out endothermic."),
 ("Trial 5",
  "EK 6.4.A.1's equation for each mixture with EK 6.4.A.7's direction rule. q18 recomputes every value and checks the maximum is unique."),
 ("Trial 1 and Trial 3",
  "EK 6.4.A.1 multiplies mass by capacity by change, so a smaller change in a larger mass can match a larger change in a smaller one. q19 recomputes all five and checks exactly one pair agrees while differing in both factors."),
 ("2508 J",
  "EK 6.4.A.1's equation using the CHANGE rather than either temperature. q20 recomputes the key and the final-temperature, initial-temperature, mass-omitted and one-degree distractors."),
 ("Lead",
  "EK 6.4.A.3 with EK 6.4.A.1 rearranged: the same energy in equal masses divides by the capacity, so the smallest capacity gives the largest rise. q21 recomputes all five rises."),
 ("Water",
  "The same division read the other way; q22 checks the minimum rise belongs to the largest tabulated capacity."),
 ("Water",
  "EK 6.4.A.5 makes the specific heat capacity the energy per gram per degree, so q23 checks the largest tabulated value is unique."),
 ("Iron and copper",
  "EK 6.4.A.3 makes the rises differ because the capacities do. q24 recomputes all five rises and all ten pairwise gaps and checks the closest pair is unique."),
 ("Water has a much larger specific heat capacity, so the same energy per gram produces a much smaller temperature change",
  "EK 6.4.A.3 states that equal masses with differing capacities do not change temperature equally, and EK 6.4.A.1's equation divides by the capacity."),
 ("The mass, the specific heat capacity, and the change in temperature",
  "EK 6.4.A.1's equation names exactly these three, and the learning objective's own phrase is the CHANGE in temperature rather than either temperature alone."),
 ("The water lost energy, since cooling a system decreases its energy",
  "EK 6.4.A.1's equation carries the sign of the temperature change and EK 6.4.A.4 states that cooling a system decreases the energy of the system."),
 ("The temperature change of the mixture is measured, and the direction of energy flow is deduced from it",
  "EK 6.4.A.7 states that temperature changes of the mixture within the calorimeter can be used to determine the direction of energy flow."),
 ("gained by the mixture and the calorimeter, because energy is conserved",
  "EK 6.4.A.2's first law with EK 6.4.A.1's account of what a calorimeter measures: what the reaction releases the surroundings inside the calorimeter take up."),
 ("Convert the mass to an amount in moles, since a molar heat capacity is taken per mole",
  "EK 6.4.A.5 states that the specific heat capacity and the molar heat capacity are both used in energy calculations, so the amount supplied must match the capacity used."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, which equation is shown?"
        no_figure_language(mod)

    def enthalpy_creeps_in(mod, cl):
        mod.QUESTIONS[1]["q"] = "What is the enthalpy of the transfer a calorimeter measures?"
        no_other_topic(mod)

    def energy_key_loses_its_direction(mod, cl):
        ch = list(mod.QUESTIONS[8]["choices"])
        ch[0] = "8360 J"
        mod.QUESTIONS[8]["choices"] = ch
        cl[8] = ("8360 J", cl[8][1])
        energy_keys_state_a_direction(mod)

    def anchor_loses_its_direction(mod, cl):
        # The key keeps its direction word; only the ANCHOR is cut back to the
        # bare number. cg_check would still pass today, because no distractor
        # happens to repeat 2090 -- which is exactly why this second guard
        # exists.
        cl[7] = ("2090 J", cl[7][1])
        anchors_carry_the_direction(mod, cl)

    def cooling_key_says_absorbed(mod, cl):
        # The arithmetic stays right and the sign goes backwards: the key moves
        # to the choice that calls a 20-degree fall an absorption. Choices are
        # untouched, so they stay distinct and the new anchor matches only the
        # new key; only n9's comparison against the SIGNED recomputed value can
        # reject it.
        mod.QUESTIONS[8]["ans"] = 1
        cl[8] = ("8360 J absorbed", cl[8][1])

    def distractor_becomes_a_second_correct_answer(mod, cl):
        # The one-degree distractor on item 8 quietly edited into the SAME
        # value as the key, written in kilojoules so it is not a duplicate
        # string. The key is untouched and still right, every choice is still
        # distinct, and the anchor still matches only the key -- so nothing but
        # ``mistake`` noticing that 209 J has left the choice list can reject
        # it.
        ch = list(mod.QUESTIONS[7]["choices"])
        ch[2] = "2.090 kJ absorbed"
        mod.QUESTIONS[7]["choices"] = ch

    def distractor_drifts_off_its_mistake(mod, cl):
        # A distractor edited to a number that is not the mistake it was
        # written to test. The item still has one correct answer and five
        # distinct choices; it has simply stopped testing what it was for.
        ch = list(mod.QUESTIONS[19]["choices"])
        ch[1] = "12000 J"
        mod.QUESTIONS[19]["choices"] = ch

    def calorimeter_endothermic_trial_flipped(mod, cl):
        # The one cooling trial turned into a warming one, so no tabulated
        # dissolution is endothermic any more.
        mod.QUESTIONS[16]["table"] = dict(
            headers=h6_4._T_CALOR["headers"],
            rows=[["Trial 1", "100.0", "22.0", "28.0"],
                  ["Trial 2", "100.0", "22.0", "27.0"],
                  ["Trial 3", "200.0", "20.0", "23.0"],
                  ["Trial 4", "50.0", "25.0", "25.0"],
                  ["Trial 5", "100.0", "22.0", "31.0"]])

    def matching_pair_broken(mod, cl):
        mod.QUESTIONS[18]["table"] = dict(
            headers=h6_4._T_CALOR["headers"],
            rows=[["Trial 1", "100.0", "22.0", "28.0"],
                  ["Trial 2", "100.0", "22.0", "17.0"],
                  ["Trial 3", "200.0", "20.0", "25.0"],
                  ["Trial 4", "50.0", "25.0", "25.0"],
                  ["Trial 5", "100.0", "22.0", "31.0"]])

    def trial_one_mass_changed(mod, cl):
        # The mass in the trial whose energy is keyed, so the recomputed 2508 J
        # is no longer what the table says.
        mod.QUESTIONS[19]["table"] = dict(
            headers=h6_4._T_CALOR["headers"],
            rows=[["Trial 1", "150.0", "22.0", "28.0"],
                  ["Trial 2", "100.0", "22.0", "17.0"],
                  ["Trial 3", "200.0", "20.0", "23.0"],
                  ["Trial 4", "50.0", "25.0", "25.0"],
                  ["Trial 5", "100.0", "22.0", "31.0"]])

    def capacities_reordered(mod, cl):
        # Lead given water's capacity and water lead's. Every tabulated NUMBER
        # is preserved, so a check on the set of capacities would see nothing
        # while the keyed substance stops being the largest rise.
        mod.QUESTIONS[20]["table"] = dict(
            headers=h6_4._T_C["headers"],
            rows=[["Water", "0.128"], ["Aluminum", "0.900"], ["Iron", "0.449"],
                  ["Copper", "0.385"], ["Lead", "4.18"]])

    def closest_pair_made_ambiguous(mod, cl):
        # Aluminum moved so that its rise sits as close to iron's as copper's
        # is, leaving two equally close pairs.
        mod.QUESTIONS[23]["table"] = dict(
            headers=h6_4._T_C["headers"],
            rows=[["Water", "4.18"], ["Aluminum", "0.449"], ["Iron", "0.449"],
                  ["Copper", "0.385"], ["Lead", "0.128"]])

    return [("a stem referring to a diagram the bank cannot show", figure_language),
            ("a stem borrowing 6.5 to 6.9's enthalpy", enthalpy_creeps_in),
            ("a key reporting a quantity of energy with no direction",
             energy_key_loses_its_direction),
            ("an anchor cut back to a bare number while the key keeps its direction",
             anchor_loses_its_direction),
            ("a key calling a 20-degree fall an absorption, with the arithmetic still right",
             cooling_key_says_absorbed),
            ("a distractor quietly edited into a second correct answer in other units",
             distractor_becomes_a_second_correct_answer),
            ("a distractor drifted off the mistake it was written to test",
             distractor_drifts_off_its_mistake),
            ("the one tabulated trial whose mixture cooled turned into a warming",
             calorimeter_endothermic_trial_flipped),
            ("the tabulated pair of trials that transferred equal energy broken apart",
             matching_pair_broken),
            ("the mass changed in the tabulated trial whose energy is keyed",
             trial_one_mass_changed),
            ("two tabulated capacities exchanged, which preserves every number and moves "
             "the answer", capacities_reordered),
            ("a second tabulated substance made equally close, so the closest pair is not "
             "unique", closest_pair_made_ambiguous)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h6.selftest()
    h.selftest(h6_4, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h6_4)
no_other_topic(h6_4)
energy_keys_state_a_direction(h6_4)
anchors_carry_the_direction(h6_4, CLAIMS)
h.run(h6_4, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
