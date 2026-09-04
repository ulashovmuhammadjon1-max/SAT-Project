"""Key audit for AP CHEMISTRY 3.6 Deviation from Ideal Gas Law.

One (anchor, claim) per item, in module order.

THE WHOLE TOPIC IS ONE SENTENCE. EK 3.6.A.1 says the ideal gas law does not
explain the actual behavior of real gases; that deviations may result from
interparticle attractions among gas molecules, particularly at conditions close
to those resulting in condensation; and that deviations may also arise from
particle volumes, particularly at extremely high pressures. Every key here is
one of those three clauses, applied.

THREE THINGS THE VERIFIER ENFORCES, all of them about not saying more than the
sentence says.

``pairing_runs_the_frameworks_way`` parses every key that names a cause together
with a condition and checks the association: attractions with CONDENSATION,
particle volumes with EXTREMELY HIGH PRESSURE. It reads each pair out of the
key's own text into a named variable rather than building two tuples and
comparing them positionally -- the mistake that made an earlier verifier in this
bank reject a correct key.

``direction_claim_only_when_disowned`` refuses any key asserting that a real gas
exerts less (or more) pressure than the equation predicts. EK 3.6.A.1 names
causes and conditions and stops; it never states the DIRECTION of the departure.
One item asks which claim goes beyond the framework, and its key is that claim,
so the check permits the sentence in a key only where the stem frames it as
unsupported -- and asserts the directional claim appears somewhere, so it cannot
pass over an empty set.

``hedge_kept`` refuses any key asserting that a real gas ALWAYS deviates. The
framework's word is may.

TWO HALF-SWAPS. Items 11 and 14 each keep a distractor with the right verdict
and the wrong reason, so ``swap_anchors_carry_both_clauses`` requires those
anchors to name both the verdict and the reason and proves the ambiguity by
locating the one-clause distractor.

ARITHMETIC. Eight tabulated items are recomputed from their tables alone,
including the four corner cases of high-or-low pressure crossed with near-or-far
from condensation.

NEGATIVE CONTROL: ``python3 verify_h3_6.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h3_6

GASTEMP = "Temperature of the gas (K)"
BOIL = "Boiling point of the substance (K)"
PRESS = "Pressure (atm)"
MARGIN = "Kelvins above the boiling point"
BP = "Boiling point (K)"
PARTVOL = "Volume occupied by the particles in one mole (mL)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|curve above|curve below)(?![a-z])", re.I)

# 3.5 owns the distribution, 3.7 owns molarity, 3.13 owns Beer-Lambert.
_OTHER_TOPIC = re.compile(
    r"(?<![A-Za-z])(Maxwell-Boltzmann|kinetic molecular theory|molarity|"
    r"Beer-Lambert|molar absorptivity)(?![A-Za-z])", re.I)

# The two causes and the two conditions, read out of a key's own words.
_ATTR_COND = re.compile(
    r"(?<![a-z])(?:interparticle\s+)?attractions?(?![a-z])"
    r"(?:.{0,120}?)(?<![a-z])(condensation|extremely high pressures?)(?![a-z])",
    re.I | re.S)
_VOL_COND = re.compile(
    r"(?<![a-z])particle volumes?(?![a-z])"
    r"(?:.{0,120}?)(?<![a-z])(condensation|extremely high pressures?)(?![a-z])",
    re.I | re.S)

# The directional claim EK 3.6.A.1 does not make.
_DIRECTION = [
    re.compile(r"(?<![a-z])(?:lower|higher|greater|less|larger|smaller)\s+"
               r"(?:pressure\s+|volume\s+)?than\s+(?:the\s+)?"
               r"(?:ideal|predicted|ideal gas law)", re.I),
    re.compile(r"(?<![a-z])predicts?\s+a\s+(?:pressure|volume)\s+"
               r"(?:lower|higher|greater|smaller|larger)(?![a-z])", re.I),
]
_DISOWNED = re.compile(
    r"(?<![a-z])(goes beyond|beyond what|not supported|does not state|"
    r"never states|unsupported)(?![a-z])", re.I)

_ALWAYS_DEVIATES = re.compile(r"(?<![a-z])always\s+deviates?(?![a-z])", re.I)


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
    print(f"OK  {module.TOPIC[0]} figures: every set of conditions is carried as a table.")


def no_other_topic(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _OTHER_TOPIC.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: uses {hit.group(0)!r}, which belongs to another "
                f"topic -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: the topic stays on EK 3.6.A.1's two causes.")


def pairing_runs_the_frameworks_way(module):
    """Attractions go with condensation; particle volumes go with extremely high pressure.

    Read as named booleans out of each key's own text. An earlier verifier in
    this bank built one tuple ordered (acid, base) and another ordered
    (base, acid) and compared index 0 with index 0 -- it rejected a correct key
    because two lists that read as parallel were not. Nothing is indexed here.
    """
    checked = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = h.keyed(item)

        attr = _ATTR_COND.search(key)
        vol = _VOL_COND.search(key)
        if not attr and not vol:
            continue

        if attr:
            condition = attr.group(1).lower()
            attractions_go_with_condensation = condition.startswith("condensation")
            assert attractions_go_with_condensation, (
                f"{module.TOPIC[0]} q{i}: the key pairs interparticle attractions with "
                f"{condition!r}, but EK 3.6.A.1 attaches them to conditions close to those "
                f"resulting in condensation -- {key!r}"
            )
        if vol:
            condition = vol.group(1).lower()
            volumes_go_with_high_pressure = condition.startswith("extremely high")
            assert volumes_go_with_high_pressure, (
                f"{module.TOPIC[0]} q{i}: the key pairs particle volumes with {condition!r}, "
                f"but EK 3.6.A.1 attaches them to extremely high pressures -- {key!r}"
            )
        checked.append(i)

    assert len(checked) >= 2, (
        f"only {len(checked)} key(s) pair a cause with a condition, so this check has almost "
        "nothing to read and proves little"
    )
    print(f"OK  {module.TOPIC[0]} pairing: item(s) {checked} pair a cause with a condition "
          "and every pairing runs the framework's way.")


def direction_claim_only_when_disowned(module):
    """EK 3.6.A.1 names causes and conditions; it never says which way a measurement goes."""
    present, keyed_disowned = [], []
    for i, item in enumerate(module.QUESTIONS, 1):
        for k, choice in enumerate(item["choices"]):
            if not any(p.search(choice) for p in _DIRECTION):
                continue
            present.append((i, k))
            if k != item["ans"]:
                continue
            assert _DISOWNED.search(item["q"]), (
                f"{module.TOPIC[0]} q{i}: the key states which way a real gas departs from "
                f"the ideal value ({choice!r}), but the stem does not frame that claim as "
                f"going beyond the framework -- stem {item['q'][:80]!r}"
            )
            keyed_disowned.append(i)
    assert len(present) >= 2, (
        f"the directional claim appears only {len(present)} time(s) in the module, so this "
        "check has almost nothing to distinguish and proves little"
    )
    print(f"OK  {module.TOPIC[0]} direction guard: the directional claim appears at "
          f"{present}, keyed only at item(s) {keyed_disowned}, where the stem asks what goes "
          "beyond the framework.")


def hedge_kept(module):
    """EK 3.6.A.1's word is MAY. No key may promise that a real gas always deviates."""
    offered = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for k, choice in enumerate(item["choices"]):
            if not _ALWAYS_DEVIATES.search(choice):
                continue
            assert k != item["ans"], (
                f"{module.TOPIC[0]} q{i}: the key promises that a real gas always deviates, "
                f"but EK 3.6.A.1 says deviations MAY result -- {choice!r}"
            )
            offered.append((i, k))
    assert offered, (
        "the always-deviates over-claim is offered nowhere, so this check ran over an empty "
        "set and proves nothing"
    )
    print(f"OK  {module.TOPIC[0]} hedge: the always-deviates over-claim is offered at "
          f"{offered} and keyed nowhere.")


SWAP_ITEMS = {
    11: ("polar gas", "interactions between polar molecules are typically greater"),
    14: ("Interparticle attractions", "conditions close to those resulting in condensation"),
}


def swap_anchors_carry_both_clauses(module, claims):
    for i, (clause_a, clause_b) in sorted(SWAP_ITEMS.items()):
        anchor = claims[i - 1][0]
        item = module.QUESTIONS[i - 1]
        has_a = cg.contains_phrase(anchor, clause_a)
        has_b = cg.contains_phrase(anchor, clause_b)
        assert has_a and has_b, (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} must name both the verdict "
            f"{clause_a!r} and the reason {clause_b!r}; it carries "
            f"{'only the verdict' if has_a else 'only the reason' if has_b else 'neither'}"
        )
        half = [k for k, c in enumerate(item["choices"])
                if k != item["ans"]
                and cg.contains_phrase(c, clause_a) != cg.contains_phrase(c, clause_b)]
        assert half, (
            f"{module.TOPIC[0]} q{i}: no distractor carries exactly one of the two clauses, "
            "so this item is not the half-swap case the check is for"
        )
    print(f"OK  {module.TOPIC[0]} swap guard: {len(SWAP_ITEMS)} anchor(s) carry the verdict "
          "and the reason together, each with a half-swapped distractor present.")


# ----------------------------------------------------------------- table items

def _unique_extreme(mapping, want_max, what):
    pick = (max if want_max else min)(mapping, key=mapping.get)
    tied = [k for k, v in mapping.items() if abs(v - mapping[pick]) < 1e-12]
    assert tied == [pick], f"the {what} is not unique: {tied} in {mapping}"
    return pick


def q9(table, item):
    margins = {lab: cg.cell(table, lab, GASTEMP) - cg.cell(table, lab, BOIL)
               for lab in cg.labels(table)}
    for lab, m in margins.items():
        assert m > 0, f"{lab} is tabulated below its boiling point ({m} K), so it is not a gas"
    closest = _unique_extreme(margins, False, "sample nearest its boiling point")
    assert closest == "Sample 2", f"the nearest tabulated sample is {closest}: {margins}"
    h.shows(item, closest)
    return (f"the tabulated gaps between gas temperature and boiling point are {margins}, "
            f"whose unique minimum is at {closest}")


def q10(table, item):
    press = dict(zip(cg.labels(table), cg.col(table, PRESS)))
    top = _unique_extreme(press, True, "highest tabulated pressure")
    assert top == "Sample L", f"the highest tabulated pressure is at {top}: {press}"
    h.shows(item, top)
    return (f"the tabulated pressures are {press}, whose unique maximum is at {top}, the "
            "condition EK 3.6.A.1 attaches to particle volume")


def _corners(table):
    press = dict(zip(cg.labels(table), cg.col(table, PRESS)))
    margin = dict(zip(cg.labels(table), cg.col(table, MARGIN)))
    hi, lo = max(press.values()), min(press.values())
    assert hi > lo, f"the tabulated pressures must differ: {press}"
    far, near = max(margin.values()), min(margin.values())
    assert far > near, f"the tabulated margins must differ: {margin}"
    return press, margin, hi, lo, far, near


def _corner(table, high_pressure, near_condensation):
    press, margin, hi, lo, far, near = _corners(table)
    want_p = hi if high_pressure else lo
    want_m = near if near_condensation else far
    hits = [lab for lab in press
            if abs(press[lab] - want_p) < 1e-12 and abs(margin[lab] - want_m) < 1e-12]
    assert len(hits) == 1, (
        f"exactly one tabulated row must sit at pressure {want_p} with margin {want_m}; "
        f"{hits} do, from {press} and {margin}"
    )
    return hits[0], press, margin


def q15(table, item):
    lab, press, margin = _corner(table, True, True)
    assert lab == "Sample Q", f"the both-causes corner is {lab}"
    h.shows(item, lab)
    return (f"the tabulated pressures {press} and margins {margin} put exactly one row at the "
            f"highest pressure AND the smallest margin, namely {lab}")


def q17(table, item):
    lab, press, margin = _corner(table, False, False)
    assert lab == "Sample P", f"the neither-cause corner is {lab}"
    h.shows(item, lab)
    return (f"the tabulated pressures {press} and margins {margin} put exactly one row at the "
            f"lowest pressure AND the largest margin, namely {lab}")


def q18(table, item):
    lab, press, margin = _corner(table, True, False)
    assert lab == "Sample S", f"the volume-only corner is {lab}"
    h.shows(item, lab)
    return (f"the tabulated pressures {press} and margins {margin} put exactly one row at the "
            f"highest pressure while still far from condensation, namely {lab}")


def q19(table, item):
    lab, press, margin = _corner(table, False, True)
    assert lab == "Sample R", f"the attraction-only corner is {lab}"
    h.shows(item, lab)
    return (f"the tabulated pressures {press} and margins {margin} put exactly one row near "
            f"condensation while still at the lowest pressure, namely {lab}")


def q21(table, item):
    bps = dict(zip(cg.labels(table), cg.col(table, BP)))
    top = _unique_extreme(bps, True, "highest tabulated boiling point")
    assert top == "Gas E", f"the highest tabulated boiling point is at {top}: {bps}"
    h.shows(item, top)
    return (f"the tabulated boiling points are {bps}; at one shared temperature the highest "
            f"of them, {top}, sits closest to condensing")


def q22(table, item):
    vols = dict(zip(cg.labels(table), cg.col(table, PARTVOL)))
    top = _unique_extreme(vols, True, "largest tabulated particle volume")
    assert top == "Gas V", f"the largest tabulated particle volume is at {top}: {vols}"
    h.shows(item, top)
    return (f"the tabulated particle volumes are {vols}, whose unique maximum is at {top}, "
            "the cause EK 3.6.A.1 attaches to extremely high pressure")


TABLE_CHECKS = {9: q9, 10: q10, 15: q15, 17: q17, 18: q18, 19: q19, 21: q21, 22: q22}

NUMERIC = {}


CLAIMS = [
 ("does not explain the actual behavior of real gases",
  "EK 3.6.A.1's opening sentence, verbatim. It states a limitation without saying which way a measurement will miss."),
 ("Interparticle attractions among gas molecules, and particle volumes",
  "EK 3.6.A.1 names exactly those two sources of deviation and no property of the container or of the apparatus."),
 ("At conditions close to those resulting in condensation",
  "EK 3.6.A.1 attaches the attraction cause to conditions that are close to those resulting in condensation; extremely high pressure is the OTHER cause's condition."),
 ("At extremely high pressures",
  "EK 3.6.A.1 says deviations may also arise from particle volumes, particularly at extremely high pressures."),
 ("Interparticle attractions among gas molecules",
  "EK 3.6.A.1 ties that cause to conditions close to those resulting in condensation, which is the situation the stem describes."),
 ("The volumes of the particles themselves",
  "EK 3.6.A.1 attaches particle volume to extremely high pressures, and the described sample is far from the conditions the same sentence gives the other cause."),
 ("The volumes of the particles themselves",
  "EK 3.6.A.1 names particle volumes as one of its two sources; the rejected options are quantities the ideal gas law already contains or never mentions."),
 ("a second source, separate from interparticle attractions",
  "EK 3.6.A.1 introduces attractions first and adds particle volumes with the word also, attaching a different range of conditions to each, so they cannot be one cause renamed."),
 ("Sample 2",
  "EK 3.6.A.1 ties the attraction cause to nearness to condensation. q9 recomputes each tabulated gap between gas temperature and boiling point and checks the minimum is unique."),
 ("Sample L",
  "EK 3.6.A.1 attaches particle volume to extremely high pressures. q10 recomputes the tabulated pressures and checks the maximum is unique."),
 ("The polar gas, because interactions between polar molecules are typically greater than those between nonpolar molecules of comparable size",
  "EK 3.6.A.1 makes interparticle attractions a source of deviation and EK 3.1.A.2 makes interactions between polar molecules typically greater than those between nonpolar molecules of comparable size. The anchor carries both the verdict and the reason because a half-swapped distractor is present."),
 ("The gas whose particles occupy more space",
  "EK 3.6.A.1 names particle VOLUMES as the cause and both samples sit at the extremely high pressure the sentence attaches to it, so more of that volume is more of that cause."),
 ("Neither named source is in its stated range",
  "EK 3.6.A.1 gives each of its two causes a range of conditions, and the described sample falls outside both -- the particulate-to-macroscopic justification suggested skill 6.E asks for."),
 ("Interparticle attractions are a named source of deviation, and the framework ties them to conditions close to those resulting in condensation",
  "EK 3.6.A.1 names that cause and attaches it to conditions close to those resulting in condensation. The anchor carries both clauses because a distractor names the framework's OTHER cause under the same condition."),
 ("Sample Q",
  "EK 3.6.A.1's two causes need extremely high pressure and nearness to condensation. q15 recomputes both tabulated columns and checks exactly one row meets both."),
 ("names a possible source rather than guaranteeing a deviation",
  "EK 3.6.A.1 uses may in both causal sentences, which names where deviations can come from without promising that a given sample will show one."),
 ("Sample P",
  "Neither cause is in range where the pressure is lowest and the margin above the boiling point is largest. q17 recomputes both tabulated columns and checks exactly one row is that corner."),
 ("Sample S",
  "EK 3.6.A.1's particle-volume cause needs extremely high pressure while its attraction cause needs nearness to condensation. q18 recomputes the corner where the first holds and the second does not."),
 ("Sample R",
  "The mirrored corner of the same two conditions. q19 recomputes the row near condensation at the lowest tabulated pressure."),
 ("properties of the particles themselves",
  "EK 3.6.A.1 names interparticle attractions among gas molecules and particle volumes, both of which belong to the particles rather than to the apparatus."),
 ("Gas E",
  "EK 3.6.A.1 ties the attraction cause to nearness to condensation, and at one shared temperature the highest boiling point is closest to condensing. q21 recomputes the tabulated maximum."),
 ("Gas V",
  "EK 3.6.A.1 attaches particle volume to extremely high pressure, which all three tabulated samples share. q22 recomputes the largest tabulated particle volume."),
 ("Extremely low pressure",
  "EK 3.6.A.1 names extremely high pressures and nearness to condensation and attaches nothing to the low-pressure end, which is where neither cause is in its stated range."),
 ("Attractive forces acting between separate gas molecules",
  "EK 3.6.A.1's phrase is among gas molecules, which places the forces between one molecule and another; the forces inside a molecule are topic 2.2's intramolecular ones."),
 ("Raising the pressure toward extremely high values",
  "EK 3.6.A.1 attaches particle volume to extremely high pressures, so moving toward that condition moves the sample into the range where the framework expects that cause to show."),
 ("Bringing the conditions closer to those that would produce condensation",
  "EK 3.6.A.1 attaches interparticle attractions to conditions close to those resulting in condensation, so approaching them brings that cause into its stated range."),
 ("attaches a different range of conditions to each of them",
  "EK 3.6.A.1 gives attractions the near-condensation range and particle volumes the extremely-high-pressure range, and two causes with different ranges are distinguishable by observation."),
 ("interparticle attractions may cause deviations near conditions producing condensation, and particle volumes may cause deviations at extremely high pressures",
  "EK 3.6.A.1's three parts in one statement: the limitation, then each cause with its own conditions. The pairing check reads both associations out of this key."),
 ("Interparticle attractions with conditions producing condensation, and particle volumes with extremely high pressures",
  "EK 3.6.A.1's two associations, stated in full because exchanging the two conditions keeps every word and makes the statement false."),
 ("relied on to exert less pressure than the ideal gas law predicts",
  "EK 3.6.A.1 names two causes and the conditions under which each matters and stops there; it never says which way a measured quantity departs from the equation's value. The four rejected statements are each part of what the sentence does assert."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[8]["q"] = "In the diagram above, which sample is nearest condensing?"
        no_figure_language(mod)

    def other_topic(mod, cl):
        mod.QUESTIONS[0]["q"] = (mod.QUESTIONS[0]["q"]
                                 + " Use the Maxwell-Boltzmann distribution to decide.")
        no_other_topic(mod)

    def pairing_swapped_in_the_summary(mod, cl):
        ch = list(mod.QUESTIONS[27]["choices"])
        ch[0] = ("The ideal gas law does not explain real gas behavior; interparticle "
                 "attractions may cause deviations at extremely high pressures, and particle "
                 "volumes may cause deviations near conditions producing condensation")
        mod.QUESTIONS[27]["choices"] = ch
        cl[27] = ("interparticle attractions may cause deviations at extremely high pressures",
                  cl[27][1])
        pairing_runs_the_frameworks_way(mod)

    def pairing_swapped_by_moving_the_key(mod, cl):
        mod.QUESTIONS[28]["ans"] = 1
        cl[28] = ("Interparticle attractions with extremely high pressures, and particle "
                  "volumes with conditions producing condensation", cl[28][1])
        pairing_runs_the_frameworks_way(mod)

    def no_key_pairs_anything(mod, cl):
        # A control on the CONTROL: with no key naming a cause beside a
        # condition, the pairing check would read nothing and pass.
        for item in mod.QUESTIONS:
            ch = list(item["choices"])
            ch[item["ans"]] = "An unrelated statement about the apparatus"
            item["choices"] = ch
        pairing_runs_the_frameworks_way(mod)

    def direction_claim_keyed(mod, cl):
        mod.QUESTIONS[0]["ans"] = 2
        cl[0] = ("always predicts a pressure lower than the measured one", cl[0][1])
        direction_claim_only_when_disowned(mod)

    def direction_stem_no_longer_disowns(mod, cl):
        # Same keyed choice at item 30, but the stem now asks which claim the
        # framework MAKES, which turns a correct item into the assertion the
        # framework withholds.
        mod.QUESTIONS[29]["q"] = ("Which claim about deviation from the ideal gas law does "
                                  "the framework establish?")
        direction_claim_only_when_disowned(mod)

    def direction_claim_removed_everywhere(mod, cl):
        for item in mod.QUESTIONS:
            item["choices"] = [
                c.replace("predicts a pressure lower than the measured one",
                          "applies to every gas equally")
                 .replace("less pressure than the ideal gas law predicts",
                          "a pressure the framework does not specify")
                for c in item["choices"]]
        direction_claim_only_when_disowned(mod)

    def always_deviates_keyed(mod, cl):
        mod.QUESTIONS[15]["ans"] = 1
        cl[15] = ("always deviates from the ideal gas law by a fixed amount", cl[15][1])
        hedge_kept(mod)

    def always_deviates_removed(mod, cl):
        for item in mod.QUESTIONS:
            item["choices"] = [c.replace("always deviates", "may deviate")
                               for c in item["choices"]]
        hedge_kept(mod)

    def polar_anchor_halved(mod, cl):
        cl[10] = ("The polar gas", cl[10][1])
        swap_anchors_carry_both_clauses(mod, cl)

    def attraction_anchor_halved(mod, cl):
        cl[13] = ("conditions close to those resulting in condensation", cl[13][1])
        swap_anchors_carry_both_clauses(mod, cl)

    def condensation_table_ties(mod, cl):
        mod.QUESTIONS[8]["table"] = dict(
            headers=h3_6._T_COND["headers"],
            rows=[["Sample 1", "400", "390"], ["Sample 2", "250", "240"],
                  ["Sample 3", "600", "90"]])

    def sample_below_its_boiling_point(mod, cl):
        # A tabulated "gas" colder than its own boiling point is not a gas.
        mod.QUESTIONS[8]["table"] = dict(
            headers=h3_6._T_COND["headers"],
            rows=[["Sample 1", "400", "100"], ["Sample 2", "230", "240"],
                  ["Sample 3", "600", "90"]])

    def corner_table_loses_a_corner(mod, cl):
        # Two rows at the high-pressure, near-condensation corner: the item no
        # longer has a single answer.
        mod.QUESTIONS[14]["table"] = dict(
            headers=h3_6._T_BOTH["headers"],
            rows=[["Sample P", "1.0", "300"], ["Sample Q", "900", "5"],
                  ["Sample R", "900", "5"], ["Sample S", "900", "300"]])

    def corner_table_pressures_exchanged(mod, cl):
        # The pressure column reversed: the volume-only corner moves off the
        # keyed row.
        mod.QUESTIONS[17]["table"] = dict(
            headers=h3_6._T_BOTH["headers"],
            rows=[["Sample P", "900", "300"], ["Sample Q", "1.0", "5"],
                  ["Sample R", "900", "5"], ["Sample S", "1.0", "300"]])

    def boiling_points_tied(mod, cl):
        mod.QUESTIONS[20]["table"] = dict(
            headers=h3_6._T_BP["headers"],
            rows=[["Gas D", "240"], ["Gas E", "240"], ["Gas F", "85"]])

    def particle_volumes_changed(mod, cl):
        mod.QUESTIONS[21]["table"] = dict(
            headers=h3_6._T_SIZE["headers"],
            rows=[["Gas T", "80"], ["Gas U", "32"], ["Gas V", "64"]])

    return [
        ("a stem referring to a diagram the bank cannot show", figure_language),
        ("another topic's material creeping in", other_topic),
        ("the summary key with its two conditions exchanged", pairing_swapped_in_the_summary),
        ("the pairing item keyed to its swapped distractor", pairing_swapped_by_moving_the_key),
        ("every key replaced, so the pairing check would read nothing", no_key_pairs_anything),
        ("the directional over-claim promoted to a key under an ordinary stem",
         direction_claim_keyed),
        ("the disowning stem rewritten to assert the directional claim instead",
         direction_stem_no_longer_disowns),
        ("the directional claim removed everywhere, so that guard would run over an empty set",
         direction_claim_removed_everywhere),
        ("the always-deviates over-claim promoted to a key", always_deviates_keyed),
        ("the always-deviates over-claim removed everywhere, so the hedge check would be idle",
         always_deviates_removed),
        ("the polar-gas anchor cut to the verdict only", polar_anchor_halved),
        ("the attraction anchor cut to the reason only", attraction_anchor_halved),
        ("two tabulated samples tied for nearest to condensation", condensation_table_ties),
        ("a tabulated sample placed below its own boiling point",
         sample_below_its_boiling_point),
        ("two tabulated rows sharing the both-causes corner", corner_table_loses_a_corner),
        ("the corner table's pressure column reversed", corner_table_pressures_exchanged),
        ("two tabulated gases tied for the highest boiling point", boiling_points_tied),
        ("the tabulated particle volumes changed under the key", particle_volumes_changed),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h3_6, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h3_6)
no_other_topic(h3_6)
pairing_runs_the_frameworks_way(h3_6)
direction_claim_only_when_disowned(h3_6)
hedge_kept(h3_6)
swap_anchors_carry_both_clauses(h3_6, CLAIMS)
h.run(h3_6, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
