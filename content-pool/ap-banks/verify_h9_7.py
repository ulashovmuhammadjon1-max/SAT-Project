"""Key audit for AP CHEMISTRY 9.7 Coupled Reactions.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  9.7.A.1  an external source of energy can make a thermodynamically
           unfavorable process occur -- electrical energy for an electrolytic
           cell or to charge a battery, light for the conversion of carbon
           dioxide to glucose        1, 2, 17, 18, 19, 26, 29, 30
  9.7.A.2  a desired product can be formed by coupling the unfavorable reaction
           that produces it to a favorable one; the individual reactions share
           one or more common intermediates; their SUM has a standard free
           energy change below zero
                   3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 21, 22,
                   23, 24, 25, 27, 28, 30

THE BOUNDARY IS THE THING MOST EASILY GOT WRONG. EK 9.7.A.2 requires the sum to
be BELOW zero, so a pair summing to exactly zero does NOT achieve the outcome.
``verdict_matches_sum`` therefore reads the recomputed sum and the key's verdict
as two separately named booleans and compares them with a strict inequality, and
one item sits deliberately at zero so the boundary is exercised rather than
assumed. A control moves that item off zero and another flips its verdict.

"achieves" and "fails to achieve" share the word "achieve", so the verdict is
read as two independent named substrings rather than by searching for one and
assuming the other -- the same family of own-goal as matching "favored" inside
"unfavored".

SCOPE. EK 9.7.A.1 names the electrolytic cell, so that phrase belongs here; the
cells themselves are 9.8 to 9.11's. ``no_cell_machinery`` asserts that no item
computes a cell potential, names an electrode, or uses Faraday's law.

NEGATIVE CONTROL: ``python3 verify_h9_7.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h9_check as h9

import h9_7

UCOL = "Free energy change of the unfavorable step, kJ/mol"
FCOL = "Free energy change of the favorable step, kJ/mol"

# Explicit lookarounds, never \b. "electrolytic cell" is NOT banned: EK 9.7.A.1
# names it as an example and the topic cannot be written without it.
_OUT_OF_SCOPE = re.compile(
    r"(?<![A-Za-z])(cell potential|standard reduction potential|anode|cathode|electrode|"
    r"faraday|nernst|salt bridge|kinetic control|equilibrium constant)(?![A-Za-z])", re.I)

_VALUE_KJ = re.compile(r"\\\(\s*([+-]?\d+(?:\.\d+)?)\s*\\\)\s*kJ/mol")
# The two steps of a coupling, as written in a stem.
_STEP = re.compile(r"\\\(\s*\\Delta G\^\\circ\s*=\s*([+-]\d+(?:\.\d+)?)\s*\\\)")

# Keys stating a signed sum together with a verdict about the coupling.
SUM_ITEMS = (6, 7)


def no_cell_machinery(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _OUT_OF_SCOPE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: mentions {hit.group(0)!r}, which belongs to 9.8 "
                f"to 9.11 or another topic -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: the electrolytic cell appears only as EK 9.7.A.1's "
          "example; no item computes a cell potential or uses Faraday's law.")


def _verdict(text):
    """Whether the text says the coupling succeeds, fails, or says neither.

    Read as two independent substrings. "fails to achieve" contains "achieve",
    so a check that searched for one phrase and assumed the negation of the
    other would read every failure as a success.
    """
    says_succeeds = "coupling achieves the desired outcome" in text
    says_fails = "coupling fails to achieve the desired outcome" in text
    if says_succeeds == says_fails:
        return None
    return says_succeeds


def _verdict_agrees(item, total, where):
    key_says_succeeds = _verdict(h.keyed(item))
    assert key_says_succeeds is not None, (
        f"{where}: the key states no single verdict about the coupling: {h.keyed(item)!r}"
    )
    # STRICT: EK 9.7.A.2 requires the sum to be BELOW zero, so exactly zero fails.
    sum_is_below_zero = total < 0
    assert sum_is_below_zero == key_says_succeeds, (
        f"{where}: the recomputed sum is {total:+.1f} kJ/mol and the key says the coupling "
        f"{'achieves' if key_says_succeeds else 'fails to achieve'} the outcome, which is "
        f"EK 9.7.A.2's condition backwards"
    )
    return key_says_succeeds


def verdict_matches_sum(module):
    for i in SUM_ITEMS:
        item = module.QUESTIONS[i - 1]
        steps = [float(v) for v in _STEP.findall(item["q"])]
        assert len(steps) == 2, f"{module.TOPIC[0]} q{i}: expected two steps, found {steps}"
        _verdict_agrees(item, sum(steps), f"{module.TOPIC[0]} q{i}")
    print(f"OK  {module.TOPIC[0]} swap guard: {len(SUM_ITEMS)} keys pair a sum below zero "
          "with a coupling that achieves the outcome and a sum above zero with one that "
          "does not.")


# ---------------------------------------------------------------- stem numerics

def coupled_sum(item):
    """EK 9.7.A.2's sum, recomputed from the two steps stated in the stem."""
    steps = [float(v) for v in _STEP.findall(item["q"])]
    assert len(steps) == 2, f"expected two steps in the stem, found {steps}"
    unfavorable = [v for v in steps if v > 0]
    favorable = [v for v in steps if v < 0]
    assert len(unfavorable) == 1 and len(favorable) == 1, (
        f"a coupling needs one unfavorable step and one favorable step: {steps}"
    )
    total = sum(steps)
    token = f"{total:+.1f}"
    h9.shows_signed(item, token)
    flipped = h9.opposite_sign_offered(item, token)
    _verdict_agrees(item, total, "the keyed choice")
    return (f"the two steps {steps} sum to {token} kJ/mol, against {flipped} offered as the "
            f"sign-flipped distractor")


def q8(item):
    """The boundary case: a sum of exactly zero does NOT satisfy EK 9.7.A.2."""
    steps = [float(v) for v in _STEP.findall(item["q"])]
    assert len(steps) == 2, f"expected two steps in the stem, found {steps}"
    total = sum(steps)
    assert abs(total) < 1e-12, f"the two steps sum to {total:+g}, not to exactly zero"
    assert not (total < 0), "a sum of zero is not below zero, which is what the item turns on"
    assert "\\( 0.0 \\)" in h.keyed(item), (
        f"the key must state the recomputed sum of zero: {h.keyed(item)!r}"
    )
    h.shows(item, "which is not below zero")
    return (f"the two steps {steps} sum to exactly {total:+.1f} kJ/mol, which is not below "
            f"zero, so EK 9.7.A.2's strict condition is not met")


def q22(item):
    """Exactly one offered favorable step is too small to carry the coupling."""
    unfavorable = float(_STEP.search(item["q"]).group(1))
    assert unfavorable > 0, f"the stem's step must be unfavorable: {unfavorable:+g}"
    sums = {}
    for k, choice in enumerate(item["choices"]):
        m = _VALUE_KJ.search(choice)
        assert m, f"choice {k} states no value: {choice!r}"
        sums[k] = unfavorable + float(m.group(1))
    failing = [k for k, v in sums.items() if v >= 0]
    assert failing == [item["ans"]], (
        f"the offered steps that leave the sum at or above zero are {failing}, and the key "
        f"is {item['ans']}: recomputed sums {sums}"
    )
    h9.shows_signed(item, f"{float(_VALUE_KJ.search(h.keyed(item)).group(1)):+.1f}")
    return (f"adding the stem's {unfavorable:+g} kJ/mol to each offered step gives {sums}, "
            f"of which exactly one is not below zero")


_TWO_STEPS = re.compile(r"the step (.+?) is unfavorable and the step (.+?) is favorable",
                        re.I)
_STEPS_RESTATED = re.compile(r"steps, (.+?) and (.+?), what", re.I)


def _shared_intermediate(first, second):
    """The species produced by the first step and consumed by the second."""
    _, products_of_first = h9.species_terms(first)
    reactants_of_second, _ = h9.species_terms(second)
    shared = sorted({sp for _, sp in products_of_first}
                    & {sp for _, sp in reactants_of_second})
    return shared


def q13(item):
    m = _TWO_STEPS.search(item["q"])
    assert m, f"the stem does not state two steps: {item['q'][:70]!r}"
    shared = _shared_intermediate(m.group(1), m.group(2))
    assert len(shared) == 1, f"expected exactly one common intermediate, found {shared}"
    h.shows(item, shared[0])
    return (f"the species produced by the first step and consumed by the second is "
            f"{shared[0]}, so it cancels when the two are added")


def q14(item):
    m = _STEPS_RESTATED.search(item["q"])
    assert m, f"the stem does not restate the two steps: {item['q'][:70]!r}"
    first, second = m.group(1), m.group(2)
    shared = _shared_intermediate(first, second)
    assert len(shared) == 1, f"expected exactly one common intermediate, found {shared}"
    reactants_of_first, products_of_first = h9.species_terms(first)
    reactants_of_second, products_of_second = h9.species_terms(second)
    left = sorted(sp for _, sp in reactants_of_first + reactants_of_second
                  if sp not in shared)
    right = sorted(sp for _, sp in products_of_first + products_of_second
                   if sp not in shared)
    overall = " + ".join(left) + " gives " + " + ".join(right)
    keyed_reactants, keyed_products = h9.species_terms(h.keyed(item))
    assert sorted(sp for _, sp in keyed_reactants) == left, (
        f"the keyed overall reaction has reactants "
        f"{sorted(sp for _, sp in keyed_reactants)}, not {left}"
    )
    assert sorted(sp for _, sp in keyed_products) == right, (
        f"the keyed overall reaction has products "
        f"{sorted(sp for _, sp in keyed_products)}, not {right}"
    )
    return (f"cancelling the common intermediate {shared[0]} from the sum of the two steps "
            f"gives {overall}, which is the keyed equation")


def q30(item):
    """The missing step, recomputed as the overall change less the one that is given."""
    values = [float(x) for x in _STEP.findall(item["q"])]
    assert len(values) == 2, f"expected two values in the stem, found {values}"
    unfavorable, overall = values
    assert unfavorable > 0, f"the first value stated must be the unfavorable step: {unfavorable:+g}"
    assert overall < 0, f"the overall change must lie below zero: {overall:+g}"
    favorable = overall - unfavorable
    token = f"{favorable:+.1f}"
    h9.shows_signed(item, token)
    h9.opposite_sign_offered(item, token)
    assert abs((unfavorable + favorable) - overall) < 1e-9, \
        "the recomputed step must add with the unfavorable one to give the stated overall"
    return (f"the overall {overall:+g} kJ/mol less the unfavorable {unfavorable:+g} kJ/mol "
            f"recomputes the favorable step as {token} kJ/mol")


NUMERIC = {6: coupled_sum, 7: coupled_sum, 8: q8, 13: q13, 14: q14, 22: q22, 30: q30}


# ------------------------------------------------------------------ table items

def _sums(table):
    return {lab: cg.cell(table, lab, UCOL) + cg.cell(table, lab, FCOL)
            for lab in cg.labels(table)}


def q9(table, item):
    sums = _sums(table)
    working = sorted(lab for lab, v in sums.items() if v < 0)
    assert working == ["Pair 1", "Pair 4"], f"the tabulated sums below zero are {working}"
    assert any(abs(v) < 1e-12 for v in sums.values()), (
        "the table must include a pair summing to exactly zero, or the item does not test "
        "that EK 9.7.A.2's condition is a strict inequality"
    )
    h.shows(item, "Pairs 1 and 4")
    return (f"the tabulated sums are {sums}, of which exactly {working} lie below zero and "
            f"one sits at the boundary")


def q10(table, item):
    sums = _sums(table)
    failing = sorted(lab for lab, v in sums.items() if v > 0)
    assert failing == ["Pair 2"], f"the tabulated sums above zero are {failing}"
    assert cg.cell(table, failing[0], FCOL) < 0, (
        "the failing pair's second step must itself be favorable, or the item's premise is "
        "false"
    )
    h.shows(item, "Pair 2")
    return (f"the tabulated sums are {sums}, of which exactly one is above zero even though "
            f"its favorable step is genuinely favorable")


def q11(table, item):
    sums = _sums(table)
    boundary = sorted(lab for lab, v in sums.items() if abs(v) < 1e-12)
    assert boundary == ["Pair 3"], f"the tabulated sums equal to zero are {boundary}"
    h.shows(item, "Pair 3")
    return f"exactly one tabulated pair sums to zero: {boundary[0]}"


def q12(table, item):
    sums = _sums(table)
    best = min(sums, key=sums.get)
    assert best == "Pair 4", f"the most negative tabulated sum is at {best}: {sums}"
    assert len([v for v in sums.values() if abs(v - sums[best]) < 1e-12]) == 1, (
        f"the most negative sum must be unique: {sums}"
    )
    biggest_favorable = min(sums, key=lambda lab: cg.cell(table, lab, FCOL))
    assert biggest_favorable != best, (
        "the pair with the largest favorable step must NOT be the keyed pair, or the item "
        "can be answered by reading one column alone"
    )
    h.shows(item, "Pair 4")
    return (f"the tabulated sums are {sums}, whose unique minimum is at {best}, which is "
            f"not the pair with the largest favorable step ({biggest_favorable})")


TABLE_CHECKS = {9: q9, 10: q10, 11: q11, 12: q12}


CLAIMS = [
 ("Make a thermodynamically unfavorable process occur",
  "EK 9.7.A.1 opens by saying an external source of energy can be used to make a thermodynamically unfavorable process occur."),
 ("Electrical energy driving an electrolytic cell or charging a battery, and light",
  "EK 9.7.A.1 lists exactly these two examples: electrical energy for an electrolytic cell or to charge a battery, and light for the conversion of carbon dioxide to glucose."),
 ("The conversion of ATP to ADP",
  "EK 9.7.A.2 names this as its example of a favorable reaction coupled to an unfavorable one in biological systems."),
 ("Its standard free energy change is below zero",
  "EK 9.7.A.2 says the sum of the individual reactions produces an overall reaction that achieves the desired outcome and has a standard free energy change below zero."),
 ("One or more common intermediates",
  "EK 9.7.A.2 states that in the coupled system the individual reactions share one or more common intermediates, which is what makes their sum a single reaction."),
 ("-20.0 kJ/mol, so the coupling achieves the desired outcome",
  "EK 9.7.A.2 makes the overall change the sum of the two steps. Recomputed in coupled_sum, which also checks the verdict matches the recomputed sign."),
 ("+35.0 kJ/mol, so the coupling fails to achieve the desired outcome",
  "EK 9.7.A.2 requires the SUM to lie below zero, and a favorable step too small to outweigh the unfavorable one leaves it above. Recomputed in coupled_sum."),
 ("which is not below zero",
  "EK 9.7.A.2's condition is a strict inequality, so a sum of exactly zero does not achieve the outcome. q8 recomputes the sum and checks it is exactly zero and not below it."),
 ("Pairs 1 and 4",
  "EK 9.7.A.2 applied to four tabulated pairs. q9 recomputes every sum and also checks the table contains a pair at exactly zero, so the strict inequality is really tested."),
 ("Pair 2",
  "EK 9.7.A.2 requires the sum to be below zero. q10 recomputes the sums and checks the failing pair's second step is itself genuinely favorable."),
 ("Pair 3",
  "A sum of exactly zero is not below zero. q11 recomputes which tabulated pair sits on the boundary."),
 ("Pair 4",
  "EK 9.7.A.2 makes the overall change the sum of the two steps. q12 recomputes every sum, checks the minimum is unique, and checks it is not simply the pair with the largest favorable step."),
 ("R(aq)",
  "EK 9.7.A.2 says the individual reactions share one or more common intermediates. q13 parses both steps and finds the species produced by the first and consumed by the second."),
 ("P(s) + Q(aq) gives S(aq) + T(g)",
  "EK 9.7.A.2 says the sum of the individual reactions produces the overall reaction, and the shared intermediate cancels. q14 builds that sum from the two steps in the stem and compares it with the key."),
 ("adding them gives a single overall reaction producing the desired product",
  "EK 9.7.A.2 pairs the shared intermediate with the claim that the SUM produces an overall reaction achieving the desired outcome."),
 ("unfavorable step keeps its own positive value and it is the sum that lies below zero",
  "EK 9.7.A.2 places its condition on the sum of the individual reactions, not on either reaction taken alone, and the desired product still forms because the overall reaction is what occurs."),
 ("An external source of energy making a thermodynamically unfavorable process occur",
  "EK 9.7.A.1 lists light driving the conversion of carbon dioxide to glucose as its second example of exactly that; the shared-intermediate mechanism is EK 9.7.A.2's separate route."),
 ("An external source of energy making a thermodynamically unfavorable process occur",
  "EK 9.7.A.1 lists electrical energy driving an electrolytic cell or charging a battery as its first example of exactly that."),
 ("Waiting long enough for the process to occur of its own accord",
  "EK 9.7.A.1 names external energy sources and EK 9.7.A.2 names coupling, and neither statement suggests time alone brings an unfavorable process about."),
 ("Couple that reaction to a favorable one with which it shares an intermediate",
  "EK 9.7.A.2 says a desired product can be formed by coupling the unfavorable reaction that produces it to a favorable reaction sharing one or more common intermediates."),
 ("favorable enough that the two sum to a value below zero",
  "EK 9.7.A.2's condition is on the sum, so the size of the favorable reaction matters as well as its sign; an exactly opposite value would leave the sum at zero."),
 ("-50.0",
  "EK 9.7.A.2 requires the sum to lie below zero, so the favorable step must exceed the unfavorable one in size. q22 recomputes the sum for every offered step and checks exactly one fails."),
 ("overall sum that is below zero, not the unfavorable reaction itself",
  "EK 9.7.A.2 places its condition on the sum of the individual reactions; each keeps its own value and the outcome is achieved through the overall reaction."),
 ("must share a common intermediate and must sum to a value below zero",
  "EK 9.7.A.2 sets both conditions, and sharing a container is not among them."),
 ("It is the favorable reaction to which an unfavorable one is coupled",
  "EK 9.7.A.2 offers the conversion of ATP to ADP while describing the coupling of an unfavorable reaction that produces a desired product TO a favorable reaction."),
 ("comes from outside the chemical system rather than from another reaction within it",
  "EK 9.7.A.1 speaks of an EXTERNAL source of energy while EK 9.7.A.2 describes a second reaction inside the system sharing a common intermediate."),
 ("An overall reaction that achieves the desired outcome",
  "EK 9.7.A.2's own words for what the sum produces; whether it then proceeds at a measurable rate is EK 9.4.A.2's separate question."),
 ("A thermodynamically unfavorable process driven by an external source of energy",
  "EK 9.7.A.1 names charging a battery among its examples of electrical energy used from outside to make a thermodynamically unfavorable process occur."),
 ("Supplying energy from outside the system, or coupling to a favorable reaction within it",
  "EK 9.7.A.1 gives the first route and EK 9.7.A.2 the second, and those two statements are the whole content of the topic."),
 ("-90.0",
  "EK 9.7.A.2 makes the overall reaction the sum of the individual reactions, so the favorable step is the overall change less the unfavorable one. Recomputed in q30 from the two values in the stem."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, what does the energy source do?"
        h9.no_figure_language(mod)

    def cell_machinery_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = (
            mod.QUESTIONS[0]["why"] + " The cathode is where it happens.")
        no_cell_machinery(mod)

    def verdict_flipped_on_a_sum(mod, cl):
        ch = list(mod.QUESTIONS[5]["choices"])
        ch[0] = "\\( -20.0 \\) kJ/mol, so the coupling fails to achieve the desired outcome"
        mod.QUESTIONS[5]["choices"] = ch
        verdict_matches_sum(mod)

    def verdict_flipped_the_other_way(mod, cl):
        ch = list(mod.QUESTIONS[6]["choices"])
        ch[0] = "\\( +35.0 \\) kJ/mol, so the coupling achieves the desired outcome"
        mod.QUESTIONS[6]["choices"] = ch
        verdict_matches_sum(mod)

    def a_step_changed_in_a_stem(mod, cl):
        mod.QUESTIONS[5]["q"] = mod.QUESTIONS[5]["q"].replace("-50.0", "-70.0")

    def boundary_item_moved_off_zero(mod, cl):
        # The item that exists to test the strict inequality no longer sums to
        # zero, so it tests nothing about the boundary and q8 must refuse it.
        mod.QUESTIONS[7]["q"] = mod.QUESTIONS[7]["q"].replace("-40.0", "-45.0")

    def boundary_row_removed_from_table(mod, cl):
        mod.QUESTIONS[8]["table"] = dict(
            headers=h9_7._T_COUPLE["headers"],
            rows=[["Pair 1", "+45.0", "-70.0"], ["Pair 2", "+90.0", "-30.0"],
                  ["Pair 3", "+15.0", "-25.0"], ["Pair 4", "+20.0", "-55.0"]])

    def failing_pair_given_an_unfavorable_second_step(mod, cl):
        mod.QUESTIONS[9]["table"] = dict(
            headers=h9_7._T_COUPLE["headers"],
            rows=[["Pair 1", "+45.0", "-70.0"], ["Pair 2", "+90.0", "+30.0"],
                  ["Pair 3", "+15.0", "-15.0"], ["Pair 4", "+20.0", "-55.0"]])

    def best_pair_also_has_the_largest_favorable_step(mod, cl):
        # Pair 4 given the largest favorable step as well, so the item could be
        # answered by reading one column and the check that forbids that fires.
        mod.QUESTIONS[11]["table"] = dict(
            headers=h9_7._T_COUPLE["headers"],
            rows=[["Pair 1", "+45.0", "-60.0"], ["Pair 2", "+90.0", "-30.0"],
                  ["Pair 3", "+15.0", "-15.0"], ["Pair 4", "+20.0", "-75.0"]])

    def intermediate_no_longer_shared(mod, cl):
        mod.QUESTIONS[12]["q"] = (
            "In a coupled system, the step P(s) + Q(aq) gives R(aq) is unfavorable and the "
            "step U(aq) gives S(aq) + T(g) is favorable. Which species is the common "
            "intermediate?")

    def overall_reaction_keeps_the_intermediate(mod, cl):
        ch = list(mod.QUESTIONS[13]["choices"])
        ch[0] = "P(s) + Q(aq) gives S(aq) + R(aq)"
        mod.QUESTIONS[13]["choices"] = ch
        cl[13] = ("P(s) + Q(aq) gives S(aq) + R(aq)", cl[13][1])

    def overall_change_altered(mod, cl):
        mod.QUESTIONS[29]["q"] = mod.QUESTIONS[29]["q"].replace("-15.0", "-35.0")

    def two_offered_steps_fail(mod, cl):
        ch = list(mod.QUESTIONS[21]["choices"])
        ch[1] = "\\( -40.0 \\) kJ/mol"
        mod.QUESTIONS[21]["choices"] = ch

    return [
        ("a stem pointing at a figure the bank cannot show", figure_language),
        ("a why naming a cathode, which is 9.8's material", cell_machinery_creeps_in),
        ("a sum below zero keyed as a coupling that fails", verdict_flipped_on_a_sum),
        ("a sum above zero keyed as a coupling that succeeds",
         verdict_flipped_the_other_way),
        ("a step changed in a stem while the key stands", a_step_changed_in_a_stem),
        ("the boundary item moved off exactly zero, so the strict inequality goes untested",
         boundary_item_moved_off_zero),
        ("the tabulated pair at exactly zero replaced, so the boundary goes untested",
         boundary_row_removed_from_table),
        ("the failing pair given a second step that is not favorable at all",
         failing_pair_given_an_unfavorable_second_step),
        ("the keyed pair given the largest favorable step, so one column would answer it",
         best_pair_also_has_the_largest_favorable_step),
        ("the two steps in a stem no longer sharing an intermediate",
         intermediate_no_longer_shared),
        ("an overall reaction that keeps the intermediate instead of cancelling it",
         overall_reaction_keeps_the_intermediate),
        ("a second offered step that also leaves the sum above zero", two_offered_steps_fail),
        ("the overall change altered in a stem while the keyed step stands",
         overall_change_altered),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h9_7, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h9.no_figure_language(h9_7)
no_cell_machinery(h9_7)
verdict_matches_sum(h9_7)
h.run(h9_7, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
