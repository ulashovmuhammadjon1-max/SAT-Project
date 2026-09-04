"""Key audit for AP CHEMISTRY 6.9 Hess's Law.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  6.9.A.1    many processes break into a series of steps, each with its own
             energy change                                            1
  6.9.B.1    total energy is conserved (first law), so the net thermal energy
             transferred is the sum of the steps' transfers; those transfers are
             the result of potential energy changes among the species; thus, AT
             CONSTANT PRESSURE, the overall enthalpy change is the sum of the
             steps'                                             2, 3, 7, 8
  6.9.B.2 i   reversed: magnitude constant, mathematical sign reversed
                              4, 9, 12, 13, 14, 17, 19, 20, 23, 24, 25, 26, 27,
                              29, 30
  6.9.B.2 ii  multiplied by c: enthalpy change multiplied by c
                                        5, 10, 12, 15, 17, 18, 21, 27, 30
  6.9.B.2 iii added: enthalpy changes added
                              6, 11, 16, 17, 18, 19, 22, 24, 26, 28, 29, 30
  6.6.A.1     negative is heat energy released, positive absorbed -- borrowed
              only to name a direction, and cited where it is used

THE EXCLUSION STATEMENT IS ENFORCED, NOT JUST NOTED. The CED attaches one to
this topic: the concept of state functions will not be assessed. Path
independence is the most natural question anybody would write here, and the
framework has asked for it not to be asked. ``no_excluded`` bans the phrase and
the path-independence question from every stem, every choice and every
rationale, and the negative control corrupts an item on purpose to prove the ban
fires.

THE ALGEBRA IS CHECKED AS WELL AS THE ARITHMETIC, and this is the part a
verifier for this topic must not skip. Getting the number right proves nothing if
the steps combined do not actually add up to the reaction the stem asks about.
``combinations_reach_their_targets`` takes each item's combination, REVERSES and
SCALES the tabulated equations exactly as the combination says, cancels the
species with ``h_equation``, and asserts the remainder is the target equation
printed verbatim in the stem. The enthalpy is then recomputed over the same
combination through ``h6_thermo.hess_sum``, so one description drives both.

WHY ``hess_step`` TAKES ``reversed_`` BY NAME. A caller can get the same number
by passing a negative factor, and then EK 6.9.B.2's two separate rules become
one, and nothing can tell a reversal from a scaling afterwards. ``h6_thermo``
refuses a negative factor for that reason, and its selftest controls it.

THE SIGN IS THE ANSWER. Principle i is a rule about a sign and nothing else, and
a step reversed without its sign reversed gives a plausible number wrong by
twice that step's enthalpy change -- item 26, recomputed here. So every keyed
enthalpy states its direction, ``anchors_carry_the_direction`` requires the
anchor to carry the sign AND the word so it cannot match a sign-flipped key, and
``h6_thermo.agrees`` compares the key's word against the SIGN of the recomputed
value using named booleans. Locating a mistaken value goes through
``h6_thermo.present``, which compares signed values RAW because ``normalize``
drops a leading '+' and keeps '-'.

NEGATIVE CONTROL: ``python3 verify_h6_9.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h_equation as eq
import h6_thermo as h6

import h6_9

STEPCOL = "Reaction"
DHCOL = "Enthalpy change (kJ/mol)"

# Each item's combination of tabulated steps, as (step label, factor, reversed).
# ``factor`` is always positive: EK 6.9.B.2 keeps scaling and reversal as two
# separate rules, and h6_thermo.hess_step refuses to let a reversal hide inside a
# negative factor.
METHANE = [("Step 1", 1, False), ("Step 8", 1, False), ("Step 9", 1, True)]
CARBON_MONOXIDE = [("Step 1", 2, False), ("Step 2", 1, True)]
SULFUR = [("Step 5", 2, False), ("Step 6", 1, False)]

COMBINATIONS = {
    14: [("Step 7", 1, True)],
    15: [("Step 8", 2, False)],
    16: [("Step 3", 1, False), ("Step 4", 1, False)],
    17: CARBON_MONOXIDE,
    18: SULFUR,
    19: METHANE,
    20: METHANE,
    21: SULFUR,
    22: CARBON_MONOXIDE,
    23: [("Step 4", 1, True)],
    24: [("Step 3", 1, True), ("Step 4", 1, True)],
    25: [("Step 1", 1, True)],
    26: METHANE,
    29: METHANE,
}

# The overall reaction each combination must produce, printed VERBATIM in that
# item's stem. Item 23 asks about a single reversed step rather than an overall
# reaction, so it has no target and is checked on its arithmetic alone.
TARGETS = {
    14: "CaO(s) + CO2(g) gives CaCO3(s)",
    15: "4 H2(g) + 2 O2(g) gives 4 H2O(l)",
    16: "N2(g) + 2 O2(g) gives 2 NO2(g)",
    17: "2 C(s) + O2(g) gives 2 CO(g)",
    18: "2 S(s) + 3 O2(g) gives 2 SO3(g)",
    19: "C(s) + 2 H2(g) gives CH4(g)",
    20: "C(s) + 2 H2(g) gives CH4(g)",
    21: "2 S(s) + 3 O2(g) gives 2 SO3(g)",
    22: "2 C(s) + O2(g) gives 2 CO(g)",
    24: "2 NO2(g) gives N2(g) + 2 O2(g)",
    25: "CO2(g) gives C(s) + O2(g)",
    26: "C(s) + 2 H2(g) gives CH4(g)",
    29: "C(s) + 2 H2(g) gives CH4(g)",
}

# Items whose key reports a signed enthalpy with a direction word.
ENTHALPY_ITEMS = (9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 23, 24, 25, 28)

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|picture|image|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|energy diagram)(?![a-z])", re.I)

_OTHER_TOPIC = [
    (re.compile(r"(?<![A-Za-z])bond (?:enthalp(?:y|ies)|energ(?:y|ies))(?![A-Za-z])", re.I),
     "6.7's average bond energies"),
    (re.compile(r"(?<![A-Za-z])enthalp(?:y|ies) of formation(?![A-Za-z])", re.I),
     "6.8's quantity"),
    (re.compile(r"(?<![A-Za-z])specific heat(?![A-Za-z])", re.I), "6.4's specific heat"),
    (re.compile(r"(?<![A-Za-z])calorimet[a-z]*", re.I), "6.4's calorimetry"),
]

# The CED's exclusion statement on THIS topic, which is why it is enforced across
# every string rather than only in stems: "The concept of state functions will
# not be assessed on the AP Exam." Path independence is the same concept in
# ordinary words, so the phrasing a question would actually use is banned too.
_EXCLUDED = [
    (re.compile(r"(?<![A-Za-z])state functions?(?![A-Za-z])", re.I), "a state function"),
    (re.compile(r"(?<![A-Za-z])(?:path independent|independent of the path|"
                r"regardless of the path|whatever path|path taken|"
                r"route taken)(?![A-Za-z])", re.I), "path independence"),
]

_SIGNED_ENTHALPY = re.compile(r"(?<![A-Za-z0-9.])[-+]\d[\d.]*\s*kJ/mol(?![A-Za-z])")
_DIRECTION = re.compile(r"(?<![A-Za-z0-9])(?:exothermic|endothermic)(?![A-Za-z0-9])", re.I)


# ------------------------------------------------------------------- helpers

def _facing(item):
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(x) for x in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def _species_name(term):
    m = re.match(r"^\d+\s+(\S.*)$", term.strip())
    return (m.group(1) if m else term).strip()


def _coefficient(term):
    m = re.match(r"^(\d+)\s+\S", term.strip())
    return int(m.group(1)) if m else 1


def reverse_step(equation):
    """EK 6.9.B.2 i on the EQUATION: the two sides exchanged."""
    left, right = equation.split(" gives ")
    return f"{right.strip()} gives {left.strip()}"


def scale_step(equation, factor):
    """EK 6.9.B.2 ii on the EQUATION: every coefficient multiplied by the factor."""
    assert factor >= 1 and int(factor) == factor, (
        f"a reaction is multiplied by a whole factor of at least one here, not {factor!r}"
    )
    halves = []
    for half in equation.split(" gives "):
        parts = []
        for term in half.split(" + "):
            n = _coefficient(term) * int(factor)
            name = _species_name(term)
            parts.append(name if n == 1 else f"{n} {name}")
        halves.append(" + ".join(parts))
    return " gives ".join(halves)


def _transform_self_check():
    """Positive AND negative controls for the two equation transforms."""
    step = "2 CO(g) + O2(g) gives 2 CO2(g)"
    assert reverse_step(step) == "2 CO2(g) gives 2 CO(g) + O2(g)", reverse_step(step)
    assert reverse_step(reverse_step(step)) == step, "reversing twice must return the original"
    assert eq.atom_balanced(reverse_step(step)), "a reversal must not unbalance an equation"
    assert scale_step(step, 2) == "4 CO(g) + 2 O2(g) gives 4 CO2(g)", scale_step(step, 2)
    assert eq.atom_balanced(scale_step(step, 3)), "a scaling must not unbalance an equation"
    assert scale_step(step, 1) == step, "a factor of one must leave the equation alone"
    # A coefficient of one is written bare, not as "1 X".
    assert scale_step("C(s) + O2(g) gives CO2(g)", 2) == "2 C(s) + 2 O2(g) gives 2 CO2(g)"
    # NEGATIVE CONTROL: the transforms must be distinguishable from doing nothing,
    # or a check built on them would pass while proving nothing.
    assert reverse_step(step) != step, "a reversal that returns its input tests nothing"
    assert scale_step(step, 2) != step, "a scaling that returns its input tests nothing"
    try:
        scale_step(step, -1)
    except AssertionError:
        pass
    else:
        raise AssertionError(
            "NEGATIVE CONTROL FAILED: a negative factor was accepted, which would let a "
            "reversal hide inside EK 6.9.B.2's scaling rule"
        )
    print("OK  6.9 transforms: reversing exchanges the sides and is its own inverse, scaling "
          "multiplies every coefficient, both leave an equation balanced, and neither is a "
          "no-op; a negative factor is refused.")


def step_equation(table, label):
    """One tabulated step's equation, read from the table the student reads."""
    rows = [r for r in table["rows"] if cg.normalize(r[0]) == cg.normalize(label)]
    assert len(rows) == 1, f"row {label!r} appears {len(rows)} times"
    j = [cg.normalize(x) for x in table["headers"]].index(cg.normalize(STEPCOL))
    return str(rows[0][j])


def step_enthalpy(table, label):
    """One tabulated step's enthalpy change, read from the same row."""
    return cg.cell(table, label, DHCOL)


def transformed(table, combination):
    """Each step's equation after EK 6.9.B.2 i and ii have been applied to it."""
    out = []
    for label, factor, reversed_ in combination:
        equation = scale_step(step_equation(table, label), factor)
        out.append(reverse_step(equation) if reversed_ else equation)
    return out


def hess_total(table, combination):
    """EK 6.9.B.2 iii over the same combination, through h6_thermo."""
    return h6.hess_sum([(step_enthalpy(table, label), factor, reversed_)
                        for label, factor, reversed_ in combination])


def _close(a, b, tol=1e-9):
    return abs(a - b) < tol


def signed(value):
    return "0 kJ/mol" if value == 0 else f"{value:+g} kJ/mol"


def key_shows(item, value_text, what):
    assert h6.present(h.keyed(item), value_text), (
        f"the recomputed {what} {value_text!r} is not in the keyed choice {h.keyed(item)!r}"
    )
    also = [k for k, c in enumerate(item["choices"])
            if k != item["ans"] and h6.present(c, value_text)]
    assert not also, (
        f"the recomputed {what} {value_text!r} also appears in choice(s) {also} -- "
        f"{item['choices']}"
    )
    return value_text


def mistake(item, value_text, origin):
    assert not h6.present(h.keyed(item), value_text), (
        f"the mistaken value {value_text!r} ({origin}) appears in the KEYED choice, so the "
        f"item has two defensible answers -- {h.keyed(item)!r}"
    )
    hits = [k for k, c in enumerate(item["choices"])
            if k != item["ans"] and h6.present(c, value_text)]
    assert len(hits) == 1, (
        f"the recomputed mistake {value_text!r} ({origin}) appears in {len(hits)} "
        f"distractor(s); exactly one must carry it -- choices {item['choices']}"
    )
    return value_text


# --------------------------------------------------------------- module gates

def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every step is carried in a table with its own "
          "equation and enthalpy change, and no item points at a picture.")


def no_other_topic(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in (item["q"], h.keyed(item), item["why"]):
            for pat, owner in _OTHER_TOPIC:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: a stem, key or why uses {hit.group(0)!r}, "
                    f"which is {owner} -- {text[:70]!r}"
                )
    print(f"OK  {module.TOPIC[0]} scope: no stem, key or why reaches an enthalpy by 6.7's "
          "bond energies or 6.8's formation route, or borrows 6.4's calorimetry.")


def no_excluded(module):
    """The CED's exclusion statement on this topic, enforced across every string."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            for pat, what in _EXCLUDED:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: uses {hit.group(0)!r}, which is {what}. The "
                    "CED's exclusion statement on 6.9 says the concept of state functions "
                    "will not be assessed, so it does not belong even in a distractor -- "
                    f"{text[:70]!r}"
                )
    print(f"OK  {module.TOPIC[0]} exclusions: neither state functions nor path independence -- "
          "the same excluded concept in ordinary words -- appears in any stem, choice or why.")


def steps_are_balanced(module):
    """Every tabulated step is a real, balanced equation."""
    table = h6_9._T_STEPS
    labels = cg.labels(table)
    for label in labels:
        equation = step_equation(table, label)
        assert eq.atom_balanced(equation), (
            f"{module.TOPIC[0]}: tabulated {label} does not conserve atoms -- "
            f"{eq.report(equation)}"
        )
        assert eq.charge_balanced(equation), (
            f"{module.TOPIC[0]}: tabulated {label} does not conserve charge -- "
            f"{eq.report(equation)}"
        )
    print(f"OK  {module.TOPIC[0]} steps: all {len(labels)} tabulated step(s) are atom- and "
          "charge-balanced from the formulas as written.")


def combinations_reach_their_targets(module):
    """The steps a check combines really do add up to the reaction in the stem.

    This is the half of a Hess's law item that arithmetic alone cannot cover. The
    tabulated equations are reversed and scaled exactly as the item's combination
    says, the species are cancelled, and what is left must be the target equation
    -- which must also appear verbatim in that item's stem, and balance.
    """
    table = h6_9._T_STEPS
    for i, target in sorted(TARGETS.items()):
        stem = module.QUESTIONS[i - 1]["q"]
        assert target in stem, (
            f"{module.TOPIC[0]} q{i}: the check uses the overall reaction {target!r}, which "
            f"does not appear in the stem the student reads -- {stem[:90]!r}"
        )
        assert eq.atom_balanced(target) and eq.charge_balanced(target), (
            f"{module.TOPIC[0]} q{i}: {target!r} is not balanced -- {eq.report(target)}"
        )
        steps = transformed(table, COMBINATIONS[i])
        assert eq.aligns_with(steps, target), (
            f"{module.TOPIC[0]} q{i}: the combination {COMBINATIONS[i]} adds to "
            f"{eq.mechanism_overall(steps)}, not to {target!r}"
        )
    print(f"OK  {module.TOPIC[0]} algebra: all {len(TARGETS)} combination(s) of tabulated "
          "steps, reversed and scaled as stated, cancel down to exactly the overall reaction "
          "printed in their own stems.")


def enthalpy_keys_state_a_direction(module):
    for i in ENTHALPY_ITEMS:
        key = h.keyed(module.QUESTIONS[i - 1])
        assert _SIGNED_ENTHALPY.search(key), (
            f"{module.TOPIC[0]} q{i}: listed as an enthalpy item but the keyed choice reports "
            f"no signed value in kJ/mol -- {key!r}"
        )
        assert _DIRECTION.search(key), (
            f"{module.TOPIC[0]} q{i}: the keyed choice reports an enthalpy change without "
            f"saying whether it is exothermic or endothermic -- {key!r}"
        )
    print(f"OK  {module.TOPIC[0]} sign guard: each of the {len(ENTHALPY_ITEMS)} key(s) "
          "reporting an enthalpy change states its direction as well as its number.")


def anchors_carry_the_direction(module, claims):
    for i in ENTHALPY_ITEMS:
        anchor = claims[i - 1][0]
        assert _SIGNED_ENTHALPY.search(anchor), (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} carries no signed value, so it "
            "could not tell a sign-flipped key from the right one"
        )
        assert _DIRECTION.search(anchor), (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} names a value without its "
            "direction, so it would still match a key with the sign reversed"
        )
    print(f"OK  {module.TOPIC[0]} anchor guard: every enthalpy anchor carries the sign AND "
          "exothermic or endothermic.")


# -------------------------------------------------------------- table items

def _hess_item(table, item, i, expected, wrong):
    """Recompute one combination's enthalpy change and check the key against it."""
    total = hess_total(table, COMBINATIONS[i])
    assert _close(total, expected), f"the combination recomputes to {total}, not {expected}"
    key_shows(item, signed(total), "overall enthalpy change")
    assert h6.agrees(total, h.keyed(item)), (
        f"the combination recomputes to {h6.report(total)}, but the keyed choice says "
        f"{h6.stated_direction(h.keyed(item))!r}: {h.keyed(item)!r}"
    )
    for value, origin in wrong:
        mistake(item, signed(value), origin)
    return (f"the tabulated steps {COMBINATIONS[i]}, reversed and scaled as stated, sum to "
            f"{h6.report(total)}, with {len(wrong)} mistaken route(s) each recomputed into one "
            "distractor")


def q14(table, item):
    raw = step_enthalpy(table, "Step 7")
    return _hess_item(table, item, 14, -178.0, [
        (raw, "the tabulated sign carried across unchanged"),
        (2 * -178.0, "the reversed value also doubled"),
        (2 * raw, "the sign kept and the value doubled"),
        (-178.0 / 2, "the reversed value halved")])


def q15(table, item):
    raw = step_enthalpy(table, "Step 8")
    return _hess_item(table, item, 15, -1144.0, [
        (raw, "the factor left off"),
        (1144.0, "the sign reversed for no reason"),
        (4 * raw, "the factor applied twice"),
        (-raw, "the factor left off and the sign reversed")])


def q16(table, item):
    a = step_enthalpy(table, "Step 3")
    b = step_enthalpy(table, "Step 4")
    return _hess_item(table, item, 16, 66.0, [
        (-66.0, "the sign of the sum reversed"),
        (abs(a) + abs(b), "the magnitudes added instead of the signed values"),
        (-(abs(a) + abs(b)), "the magnitudes added and the sign reversed"),
        (a, "the first step reported alone")])


def q17(table, item):
    one = step_enthalpy(table, "Step 1")
    two = step_enthalpy(table, "Step 2")
    return _hess_item(table, item, 17, -222.0, [
        (222.0, "the sign of the total reversed"),
        (2 * one + two, "the second step added without being reversed"),
        (one + two, "neither the factor nor the reversal applied"),
        (two, "the second step reported alone")])


def q18(table, item):
    five = step_enthalpy(table, "Step 5")
    six = step_enthalpy(table, "Step 6")
    return _hess_item(table, item, 18, -792.0, [
        (792.0, "the sign of the total reversed"),
        (five + six, "the factor left off"),
        (2 * five + 2 * six, "the factor applied to both steps"),
        (2 * five, "the doubled step reported alone")])


def q19(table, item):
    one = step_enthalpy(table, "Step 1")
    eight = step_enthalpy(table, "Step 8")
    nine = step_enthalpy(table, "Step 9")
    return _hess_item(table, item, 19, -75.0, [
        (75.0, "the sign of the total reversed"),
        (one + eight + nine, "the third step added without being reversed"),
        (one + eight, "the third step left out altogether"),
        (-(one + eight + nine), "the third step not reversed and the total then negated")])


def q20(table, item):
    reversed_steps = [label for label, _f, r in COMBINATIONS[20] if r]
    assert len(reversed_steps) == 1, (
        f"exactly one step must be reversed for this item to have one answer; "
        f"{reversed_steps} are"
    )
    h.shows(item, reversed_steps[0])
    # The item is only meaningful if the combination it names is the right one,
    # which combinations_reach_their_targets has already established.
    return (f"of the steps combined to reach the stated overall reaction, {reversed_steps} "
            f"is the only one written backwards, out of {len(COMBINATIONS[20])} used")


def q21(table, item):
    scaled = [(label, f) for label, f, _r in COMBINATIONS[21] if f != 1]
    assert len(scaled) == 1, (
        f"exactly one step must be multiplied for this item to have one answer; {scaled} are"
    )
    label, factor = scaled[0]
    assert factor == 2, f"the stem asks which step is multiplied by two, but the factor is "\
                        f"{factor}"
    h.shows(item, label)
    return (f"of the steps combined to reach the stated overall reaction, {label} is the only "
            f"one multiplied, and its factor is {factor}")


_PHASE_TAIL = re.compile(r"\((?:s|l|g|aq)\)$")


def _phase_labelled(steps, bare):
    """The species as the TABLE writes it, given the phase-free name eq returns.

    ``h_equation.step_species`` strips phase labels, so cancellation is computed
    on bare names; the choice a student reads carries the label, and this is what
    ties the two together rather than a hardcoded string in this file.
    """
    hits = {_species_name(term)
            for step in steps
            for half in step.split(" gives ")
            for term in half.split(" + ")
            if _PHASE_TAIL.sub("", _species_name(term)) == bare}
    assert len(hits) == 1, f"{bare!r} is written {sorted(hits)} in the tabulated steps"
    return hits.pop()


def q22(table, item):
    steps = transformed(table, COMBINATIONS[22])
    left, right = {}, {}
    for step in steps:
        ls, rs = eq.step_species(step)
        for name, n in ls.items():
            left[name] = left.get(name, 0) + n
        for name, n in rs.items():
            right[name] = right.get(name, 0) + n
    net_l, net_r = eq.mechanism_overall(steps)
    gone = sorted(name for name in set(left) & set(right)
                  if name not in net_l and name not in net_r)
    assert gone == ["CO2"], (
        f"the species that cancel entirely are {gone}, from left {left} and right {right}"
    )
    # Oxygen is on both sides too and does NOT vanish; that is the distractor
    # this item exists to separate, so it is asserted rather than assumed.
    assert "O2" in left and "O2" in right, (left, right)
    assert "O2" in net_l or "O2" in net_r, (
        "oxygen must survive into the overall reaction, or the item has two defensible answers"
    )
    labelled = _phase_labelled(steps, gone[0])
    h.shows(item, labelled)
    return (f"combining the stated steps puts {dict(sorted(left.items()))} on the left and "
            f"{dict(sorted(right.items()))} on the right, of which only {labelled} cancels "
            "entirely; oxygen appears on both sides but survives")


def q23(table, item):
    raw = step_enthalpy(table, "Step 4")
    return _hess_item(table, item, 23, 114.0, [
        (raw, "the tabulated sign carried across unchanged"),
        (2 * 114.0, "the reversed value also doubled"),
        (2 * raw, "the sign kept and the value doubled"),
        (114.0 / 2, "the reversed value halved")])


def q24(table, item):
    a = step_enthalpy(table, "Step 3")
    b = step_enthalpy(table, "Step 4")
    return _hess_item(table, item, 24, -66.0, [
        (66.0, "neither step reversed"),
        (-(abs(a) + abs(b)), "the magnitudes added instead of the signed values"),
        (abs(a) + abs(b), "the magnitudes added and the sign reversed"),
        (-a, "one reversed step reported alone")])


def q25(table, item):
    raw = step_enthalpy(table, "Step 1")
    return _hess_item(table, item, 25, 394.0, [
        (raw, "the tabulated sign carried across unchanged"),
        (2 * 394.0, "the reversed value also doubled"),
        (2 * raw, "the sign kept and the value doubled"),
        (394.0 / 2, "the reversed value halved")])


def q26(table, item):
    correct = hess_total(table, COMBINATIONS[26])
    assert _close(correct, -75.0), correct
    reversed_steps = [label for label, _f, r in COMBINATIONS[26] if r]
    assert len(reversed_steps) == 1, reversed_steps
    slipped = step_enthalpy(table, reversed_steps[0])
    # The same combination with EK 6.9.B.2 i not applied to the one reversed step.
    wrong = sum(h6.hess_step(step_enthalpy(table, label), factor=f, reversed_=False)
                for label, f, _r in COMBINATIONS[26])
    gap = abs(wrong - correct)
    assert _close(gap, 2 * abs(slipped)), (
        f"the gap recomputes to {gap}, not twice the slipped step's {abs(slipped)}"
    )
    h.shows(item, f"By {gap:g} kJ/mol, which is twice that step's enthalpy change")
    others = sum(step_enthalpy(table, label) for label, _f, r in COMBINATIONS[26] if not r)
    mistake(item, f"By {abs(slipped):g} kJ/mol", "the step's own enthalpy change")
    mistake(item, f"By {abs(others):g} kJ/mol", "the other two steps' sum")
    mistake(item, f"By {abs(correct):g} kJ/mol", "the size of the correct answer")
    return (f"the correct total is {h6.report(correct)} and the slipped one "
            f"{h6.report(wrong)}, a gap of {gap:g} kJ/mol, which is twice the "
            f"{abs(slipped):g} kJ/mol of the step that should have been reversed")


def q29(table, item):
    n = sum(1 for _label, _f, r in COMBINATIONS[29] if r)
    assert n == 1, f"{n} of the steps used are reversed"
    word = {0: "None of them", 1: "Exactly one", 2: "Exactly two", 3: "All three"}[n]
    h.shows(item, word)
    return (f"of the {len(COMBINATIONS[29])} tabulated steps combined to reach the stated "
            f"overall reaction, {n} is written backwards")


TABLE_CHECKS = {14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21,
                22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 29: q29}


# ------------------------------------------------------------- stem numerics

def _stem_values(item, expected_count):
    hits = re.findall(r"(?<![A-Za-z0-9.])([-+]\d+(?:\.\d+)?)\s*kJ/mol", item["q"])
    values = [float(x) for x in hits]
    assert len(values) == expected_count, (
        f"the stem states {values}, not {expected_count} value(s) -- {item['q'][:80]!r}"
    )
    return values


def n9(item):
    (given,) = _stem_values(item, 1)
    total = h6.hess_sum([(given, 1, True)])
    assert _close(total, -given), total
    key_shows(item, signed(total), "reversed enthalpy change")
    assert h6.agrees(total, h.keyed(item)), h6.report(total)
    mistake(item, signed(given), "the sign carried across unchanged")
    mistake(item, signed(2 * total), "the reversed value also doubled")
    mistake(item, signed(2 * given), "the sign kept and the value doubled")
    mistake(item, "0 kJ/mol", "the reversal taken to cancel the enthalpy change")
    return (f"EK 6.9.B.2 i on the stated {given:+g} kJ/mol gives {h6.report(total)}, with "
            "four mistaken routes each recomputed into one distractor")


def n10(item):
    (given,) = _stem_values(item, 1)
    total = h6.hess_sum([(given, 3, False)])
    assert _close(total, 3 * given), total
    key_shows(item, signed(total), "multiplied enthalpy change")
    assert h6.agrees(total, h.keyed(item)), h6.report(total)
    mistake(item, signed(given), "the factor left off")
    mistake(item, signed(-total), "the sign reversed as well as the value multiplied")
    mistake(item, signed(given / 3), "divided by the factor instead of multiplied")
    mistake(item, signed(-given), "the sign reversed and the factor left off")
    return (f"EK 6.9.B.2 ii on the stated {given:+g} kJ/mol with a factor of three gives "
            f"{h6.report(total)}, with four mistaken routes each in one distractor")


def n11(item):
    a, b = _stem_values(item, 2)
    total = h6.hess_sum([(a, 1, False), (b, 1, False)])
    assert _close(total, a + b), total
    key_shows(item, signed(total), "overall enthalpy change")
    assert h6.agrees(total, h.keyed(item)), h6.report(total)
    mistake(item, signed(-total), "the sign of the sum reversed")
    mistake(item, signed(-(abs(a) + abs(b))), "the magnitudes added instead of the signed "
                                              "values")
    mistake(item, signed(abs(a) + abs(b)), "the magnitudes added and the sign reversed")
    mistake(item, signed(a), "the first step reported alone")
    return (f"EK 6.9.B.2 iii on the stated {a:+g} and {b:+g} kJ/mol gives {h6.report(total)}, "
            "with four mistaken routes each in one distractor")


def n12(item):
    (given,) = _stem_values(item, 1)
    total = h6.hess_sum([(given, 2, True)])
    assert _close(total, -2 * given), total
    key_shows(item, signed(total), "contribution")
    assert h6.agrees(total, h.keyed(item)), h6.report(total)
    # The two principles act on different parts of the number, so applying them
    # in the other order must give the same contribution. Named, not assumed.
    scale_then_reverse = -(2 * given)
    reverse_then_scale = 2 * (-given)
    assert _close(scale_then_reverse, reverse_then_scale) and _close(total, scale_then_reverse)
    mistake(item, signed(-total), "the reversal left out")
    mistake(item, signed(-given), "the factor left out")
    mistake(item, signed(given), "neither principle applied")
    mistake(item, signed(2 * total), "the factor applied twice")
    return (f"EK 6.9.B.2 i and ii on the stated {given:+g} kJ/mol give {h6.report(total)}, the "
            "same either way round, with four mistaken routes each in one distractor")


def n27(item):
    """The order of the two principles cannot matter, recomputed rather than asserted."""
    for value in (-250.0, -60.0, 45.0, 120.0):
        for factor in (2, 3, 5):
            both = h6.hess_step(value, factor=factor, reversed_=True)
            reverse_then_scale = factor * (-value)
            scale_then_reverse = -(factor * value)
            assert _close(both, reverse_then_scale) and _close(both, scale_then_reverse), (
                value, factor, both, reverse_then_scale, scale_then_reverse
            )
            # NEGATIVE CONTROL on the check itself: an order that genuinely
            # differed would have to be visible here, so a wrong composition is
            # computed and required to disagree.
            wrong = factor * value
            assert not _close(both, wrong), (
                "a comparison that cannot separate the reversed contribution from the "
                "unreversed one proves nothing"
            )
    h.shows(item, "No, the contribution comes out the same either way")
    return ("reversing then scaling and scaling then reversing were computed for twelve "
            "value and factor pairs and agree in every one, while the unreversed "
            "contribution differs in every one")


def n28(item):
    a, b, c = _stem_values(item, 3)
    total = h6.hess_sum([(a, 1, False), (b, 1, False), (c, 1, False)])
    assert _close(total, a + b + c), total
    key_shows(item, signed(total), "overall enthalpy change")
    assert h6.agrees(total, h.keyed(item)), h6.report(total)
    mistake(item, signed(-total), "the sign of the sum reversed")
    mistake(item, signed(abs(a) + abs(b) + abs(c)), "the magnitudes added instead of the "
                                                    "signed values")
    mistake(item, signed(-(abs(a) + abs(b) + abs(c))), "the magnitudes added and the sign "
                                                       "reversed")
    mistake(item, signed(b), "the largest step reported alone")
    return (f"EK 6.9.B.2 iii on the stated {a:+g}, {b:+g} and {c:+g} kJ/mol gives "
            f"{h6.report(total)}, with four mistaken routes each in one distractor")


def n30(item):
    """The combination the stem describes, computed for a sample pair."""
    first, second = -300.0, 40.0
    total = h6.hess_sum([(first, 1, True), (second, 3, False)])
    assert _close(total, -first + 3 * second), total
    assert _close(h6.hess_step(first, reversed_=True), -first)
    assert _close(h6.hess_step(second, factor=3), 3 * second)
    h.shows(item, "the reversed step's enthalpy change changes sign, the multiplied step's is "
                  "tripled, and the two are then added")
    return (f"for a sample pair the three principles give {-first:+g} from the reversed step "
            f"and {3 * second:+g} from the tripled one, summing to {total:+g} kJ/mol")


NUMERIC = {9: n9, 10: n10, 11: n11, 12: n12, 27: n27, 28: n28, 30: n30}


CLAIMS = [
 ("broken down into a series of steps, each with its own energy change",
  "EK 6.9.A.1: many processes can be broken down into a series of steps, and each step in the series has its own energy change."),
 ("The sum of the enthalpy changes of the individual steps",
  "EK 6.9.B.1's conclusion, verbatim in substance: at constant pressure the enthalpy change of the overall process equals the sum of the steps'."),
 ("Because total energy is conserved, which is the first law of thermodynamics",
  "EK 6.9.B.1 names that as the reason the net thermal energy transferred equals the sum of the transfers in each step."),
 ("stays constant in magnitude but its mathematical sign is reversed",
  "EK 6.9.B.2 i, verbatim in substance. Both halves are the rule: the magnitude is untouched and only the sign moves."),
 ("It is multiplied by the same factor c",
  "EK 6.9.B.2 ii: when a reaction is multiplied by a factor c, the enthalpy change is multiplied by the same factor c, and nothing in the rule touches the sign."),
 ("They are added to obtain the net enthalpy change of the overall reaction",
  "EK 6.9.B.2 iii, verbatim in substance: adding reactions adds their individual enthalpy changes."),
 ("Potential energy changes among the species in the reaction sequence",
  "EK 6.9.B.1 says the thermal energy transfers are the result of exactly that."),
 ("At constant pressure",
  "EK 6.9.B.1 attaches that condition to its conclusion in so many words."),
 ("+250 kJ/mol, so the reverse reaction is endothermic",
  "EK 6.9.B.2 i on the stated value, with EK 6.6.A.1 reading the positive result as heat energy absorbed. n9 recomputes it and four mistaken routes."),
 ("+360 kJ/mol, so it is endothermic",
  "EK 6.9.B.2 ii on the stated value with a factor of three; the sign is untouched. n10 recomputes it and four mistaken routes."),
 ("-140 kJ/mol, so the overall process is exothermic",
  "EK 6.9.B.2 iii adds the stated enthalpy changes with their signs, so a positive step subtracts from a negative one. n11 recomputes it."),
 ("+600 kJ/mol, so its contribution is endothermic",
  "EK 6.9.B.2 i and ii both act: the sign is reversed and the magnitude doubled. n12 recomputes it and checks the two orders agree."),
 ("Reversing a reaction reverses the mathematical sign of its enthalpy change",
  "EK 6.9.B.2 i is a rule about the sign and only the sign, so carrying the tabulated value across unchanged reports heat flowing the wrong way."),
 ("-178 kJ/mol, so the overall reaction is exothermic",
  "EK 6.9.B.2 i on one tabulated step. q14 recomputes it from the table, and combinations_reach_their_targets checks the reversed step really is the overall reaction in the stem."),
 ("-1144 kJ/mol, so the overall reaction is exothermic",
  "EK 6.9.B.2 ii on one tabulated step. q15 recomputes it and checks the doubled equation cancels down to the stem's overall reaction."),
 ("+66 kJ/mol, so the overall reaction is endothermic",
  "EK 6.9.B.2 iii on two tabulated steps added as written. q16 recomputes it and four mistaken routes."),
 ("-222 kJ/mol, so the overall reaction is exothermic",
  "All three principles at once: one step doubled, another reversed, and the two added. q17 recomputes the total and the algebra is checked separately."),
 ("-792 kJ/mol, so the overall reaction is exothermic",
  "EK 6.9.B.2 ii on one of two tabulated steps, then iii. q18 recomputes it and four mistaken routes."),
 ("-75 kJ/mol, so the overall reaction is exothermic",
  "Three tabulated steps with one reversed. q19 recomputes the total, and the combination is checked to cancel down to the overall reaction in the stem."),
 ("Step 9",
  "EK 6.9.B.2 i has to be applied to whichever step has its substances on the wrong sides. q20 reads which step the verified combination reverses."),
 ("Step 5",
  "EK 6.9.B.2 ii is applied so the cancelling species appear in equal amounts. q21 reads which step the verified combination multiplies, and by what factor."),
 ("CO2(g)",
  "EK 6.9.B.2 iii adds the reactions, so a species produced and consumed in equal amount leaves nothing behind. q22 cancels the combined steps and checks oxygen survives."),
 ("+114 kJ/mol, so the reverse step is endothermic",
  "EK 6.9.B.2 i on one tabulated step, keeping the magnitude and reversing the sign. q23 recomputes it and four mistaken routes."),
 ("-66 kJ/mol, so the overall reaction is exothermic",
  "EK 6.9.B.2 i applied to both tabulated steps before iii adds them. q24 recomputes it and checks the pair cancels down to the stem's overall reaction."),
 ("+394 kJ/mol, so the overall reaction is endothermic",
  "EK 6.9.B.2 i on one tabulated step, with EK 6.6.A.1 reading the positive result as heat energy absorbed. q25 recomputes it."),
 ("1782 kJ/mol, which is twice that step's enthalpy change",
  "EK 6.9.B.2 i replaces a value by its negative, so using the value itself shifts the total by twice it. q26 recomputes the correct and the slipped total and the gap between them."),
 ("No, the contribution comes out the same either way",
  "EK 6.9.B.2 i changes only the sign and ii scales only the magnitude, so neither undoes the other. n27 computes both orders for twelve value and factor pairs."),
 ("+100 kJ/mol, so the overall process is endothermic",
  "EK 6.9.B.2 iii adds the three stated enthalpy changes with their signs. n28 recomputes it and four mistaken routes."),
 ("Exactly one",
  "EK 6.9.B.2 i is needed only for a step whose substances are on the wrong sides. q29 counts the reversals in the combination whose algebra has been verified."),
 ("the reversed step's enthalpy change changes sign, the multiplied step's is tripled, and the two are then added",
  "EK 6.9.B.2's three principles used once each. n30 computes the described combination for a sample pair through h6_thermo."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the energy diagram above, what happens to a process?"
        no_figure_language(mod)

    def formation_route_creeps_in(mod, cl):
        mod.QUESTIONS[1]["q"] = "What is the sum of the enthalpies of formation of the steps?"
        no_other_topic(mod)

    def excluded_state_function(mod, cl):
        ch = list(mod.QUESTIONS[1]["choices"])
        ch[4] = "The enthalpy of the first step, since enthalpy is a state function"
        mod.QUESTIONS[1]["choices"] = ch
        no_excluded(mod)

    def excluded_path_independence(mod, cl):
        # The same excluded concept written in ordinary words, which is how it
        # would actually reach a student. A ban on the technical phrase alone
        # would miss this, so the ban covers both.
        mod.QUESTIONS[2]["why"] = (
            "EK 6.9.B.1 makes the overall enthalpy change independent of the path taken "
            "between the same reactants and products, which is why the steps may be chosen "
            "freely.")
        no_excluded(mod)

    def tabulated_step_unbalanced(mod, cl):
        saved = h6_9._T_STEPS["rows"]
        h6_9._T_STEPS = dict(
            headers=_T_HEADERS,
            rows=[[lab, ("2 CO(g) + O2(g) gives 3 CO2(g)" if lab == "Step 2" else e), v]
                  for lab, e, v in saved])
        try:
            steps_are_balanced(mod)
        finally:
            h6_9._T_STEPS = dict(headers=_T_HEADERS, rows=saved)

    def combination_does_not_reach_its_target(mod, cl):
        # The arithmetic would still come out to a plausible number; only the
        # ALGEBRA can reject this, which is the half a Hess's law verifier is
        # most likely to skip.
        COMBINATIONS[17] = [("Step 1", 1, False), ("Step 2", 1, True)]
        try:
            combinations_reach_their_targets(mod)
        finally:
            COMBINATIONS[17] = CARBON_MONOXIDE

    def reversal_dropped_from_a_combination(mod, cl):
        COMBINATIONS[19] = [("Step 1", 1, False), ("Step 8", 1, False), ("Step 9", 1, False)]
        try:
            combinations_reach_their_targets(mod)
        finally:
            COMBINATIONS[19] = METHANE

    def target_edited_out_of_a_stem(mod, cl):
        mod.QUESTIONS[18]["q"] = (
            "For the formation of methane from its elements, what is the enthalpy change "
            "from the tabulated steps?")
        combinations_reach_their_targets(mod)

    def enthalpy_key_loses_its_direction(mod, cl):
        ch = list(mod.QUESTIONS[13]["choices"])
        ch[0] = "-178 kJ/mol"
        mod.QUESTIONS[13]["choices"] = ch
        cl[13] = ("-178 kJ/mol", cl[13][1])
        enthalpy_keys_state_a_direction(mod)

    def anchor_loses_its_direction(mod, cl):
        cl[14] = ("-1144 kJ/mol", cl[14][1])
        anchors_carry_the_direction(mod, cl)

    def key_moved_to_the_unreversed_value(mod, cl):
        # The classic defect: EK 6.9.B.2 i not applied, so the tabulated sign is
        # carried across. The magnitude is right and only the sign is wrong.
        mod.QUESTIONS[13]["ans"] = 1
        cl[13] = ("+178 kJ/mol, so the overall reaction is endothermic", cl[13][1])

    def direction_word_alone_reversed(mod, cl):
        # The NUMBER is left exactly right and only the direction word flipped,
        # so every earlier guard passes and only the comparison of the key's word
        # against the SIGN of the recomputed value can reject it. The wording
        # after the number differs from the reversed distractor's, or the
        # containment check would fire first and the control would prove nothing.
        ch = list(mod.QUESTIONS[16]["choices"])
        ch[0] = "-222 kJ/mol, and the overall reaction is endothermic"
        mod.QUESTIONS[16]["choices"] = ch
        cl[16] = ("-222 kJ/mol, and the overall reaction is endothermic", cl[16][1])

    def tabulated_enthalpy_changed(mod, cl):
        mod.QUESTIONS[18]["table"] = dict(
            headers=_T_HEADERS,
            rows=[[lab, e, ("-800" if lab == "Step 9" else v)]
                  for lab, e, v in h6_9._T_STEPS["rows"]])

    def tabulated_sign_flipped(mod, cl):
        mod.QUESTIONS[15]["table"] = dict(
            headers=_T_HEADERS,
            rows=[[lab, e, ("-180" if lab == "Step 3" else v)]
                  for lab, e, v in h6_9._T_STEPS["rows"]])

    def unreversed_distractor_removed(mod, cl):
        # The distractor carrying the not-reversed value replaced. The key is
        # still right and every choice still distinct -- the item has simply
        # stopped testing the one error it exists to test.
        ch = list(mod.QUESTIONS[24]["choices"])
        ch[1] = "-500 kJ/mol, so the overall reaction is exothermic"
        mod.QUESTIONS[24]["choices"] = ch

    def stem_value_edited(mod, cl):
        mod.QUESTIONS[8]["q"] = mod.QUESTIONS[8]["q"].replace("-250 kJ/mol", "-260 kJ/mol")

    def three_stem_values_reduced_to_two(mod, cl):
        mod.QUESTIONS[27]["q"] = mod.QUESTIONS[27]["q"].replace(
            "-100 kJ/mol, +250 kJ/mol and -50 kJ/mol", "+250 kJ/mol and -50 kJ/mol")

    def which_step_reversed_key_moved(mod, cl):
        mod.QUESTIONS[19]["ans"] = 1
        cl[19] = ("Step 1", cl[19][1])

    def scaled_step_key_moved(mod, cl):
        mod.QUESTIONS[20]["ans"] = 1
        cl[20] = ("Step 6", cl[20][1])

    def cancelling_species_key_moved(mod, cl):
        mod.QUESTIONS[21]["ans"] = 3
        cl[21] = ("O2(g)", cl[21][1])

    def reversal_count_key_moved(mod, cl):
        mod.QUESTIONS[28]["ans"] = 2
        cl[28] = ("Exactly two", cl[28][1])

    def slipped_step_gap_key_moved(mod, cl):
        mod.QUESTIONS[25]["ans"] = 1
        cl[25] = ("891 kJ/mol, which is that step's enthalpy change", cl[25][1])

    return [
        ("a stem referring to an energy diagram the bank cannot show", figure_language),
        ("a stem borrowing 6.8's enthalpies of formation", formation_route_creeps_in),
        ("the CED's excluded state-function concept used as a distractor",
         excluded_state_function),
        ("the same excluded concept written as path independence in a rationale",
         excluded_path_independence),
        ("a tabulated step that does not conserve atoms", tabulated_step_unbalanced),
        ("a combination whose steps do not add up to the overall reaction in the stem",
         combination_does_not_reach_its_target),
        ("a reversal dropped from a combination, leaving the algebra wrong",
         reversal_dropped_from_a_combination),
        ("the overall reaction removed from a stem while the check keeps using it",
         target_edited_out_of_a_stem),
        ("a key reporting an enthalpy change with no direction",
         enthalpy_key_loses_its_direction),
        ("an anchor cut back to a bare value while the key keeps its direction",
         anchor_loses_its_direction),
        ("a key moved to the value with EK 6.9.B.2 i not applied",
         key_moved_to_the_unreversed_value),
        ("a keyed direction word flipped with its number left right",
         direction_word_alone_reversed),
        ("a tabulated enthalpy change edited under a keyed total", tabulated_enthalpy_changed),
        ("a tabulated enthalpy's sign flipped with its magnitude untouched",
         tabulated_sign_flipped),
        ("the not-reversed distractor replaced, so the item stops testing it",
         unreversed_distractor_removed),
        ("a stem's stated enthalpy edited under an untouched key", stem_value_edited),
        ("a stated enthalpy dropped from a three-step stem", three_stem_values_reduced_to_two),
        ("the which-step-is-reversed item keyed to a step used as written",
         which_step_reversed_key_moved),
        ("the which-step-is-multiplied item keyed to the unscaled step", scaled_step_key_moved),
        ("the cancelling-species item keyed to the species that survives",
         cancelling_species_key_moved),
        ("the reversal-count item keyed to the wrong count", reversal_count_key_moved),
        ("the slipped-sign item keyed to a single step's enthalpy change",
         slipped_step_gap_key_moved),
    ]


_T_HEADERS = h6_9._T_STEPS["headers"]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h6.selftest()
    eq.selftest()
    h.selftest(h6_9, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

_transform_self_check()
no_figure_language(h6_9)
no_other_topic(h6_9)
no_excluded(h6_9)
steps_are_balanced(h6_9)
combinations_reach_their_targets(h6_9)
enthalpy_keys_state_a_direction(h6_9)
anchors_carry_the_direction(h6_9, CLAIMS)
h.run(h6_9, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
