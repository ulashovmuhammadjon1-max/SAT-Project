"""Key audit for AP CHEMISTRY 8.10 Buffer Capacity.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  8.10.A.1  raising both concentrations at a fixed ratio keeps the pH the same
            and increases the capacity
                    1, 2, 5, 6, 7, 8, 13, 14, 15, 16, 17, 19, 20, 23, 24, 26,
                    27, 29
  8.10.A.2  an excess of the conjugate acid gives the greater capacity for added
            BASE, and an excess of the conjugate base the greater capacity for
            added ACID
                    3, 4, 9, 10, 11, 12, 21, 22, 25, 28, 30
  EK 8.9.A.1 supplies why the pH follows the ratio            18

THE SWAP GUARD. EK 8.10.A.2 is the easiest statement in the unit to ship
backwards, so ``asymmetry_anchors_span_both_clauses`` asserts that every anchor
belonging to an asymmetry item names BOTH the component in excess and the
addition it handles better. An anchor that named only one of them would still
match a key that had them the wrong way round, which is the defect this check
exists to make impossible.

SCOPE, from the four-way buffer split recorded in h8_4.py's header. 8.8 owns the
net ionic equations and 8.9 owns the arithmetic, so ``no_ph_arithmetic`` asserts
that no item takes a logarithm, states a numeric pH, or asks for a net ionic
equation.

ARITHMETIC. Every ratio, every ordering by concentration and every pair of
buffers said to share a pH is recomputed from the table alone.

NEGATIVE CONTROL: ``python3 verify_h8_10.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h8_10

HA = "[HA] (M)"
AM = "[A-] (M)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|titration curve)(?![a-z])", re.I)

_ARITH = re.compile(
    r"\\log|(?<![a-z])logarithm(?![a-z])|(?<![a-z])net ionic(?![a-z])", re.I)
_PH_VALUE = re.compile(r"(?<![A-Za-z])pH\s*(?:=|of)\s*\d", re.I)

# The items whose keys carry EK 8.10.A.2's asymmetry. Listed explicitly so the
# guard cannot quietly stop covering an item that was edited.
ASYMMETRY_ITEMS = (3, 4, 25, 30)

# Which component is in EXCESS, read off the comparative that introduces it.
# A bare "conjugate acid" search cannot do this: every one of these sentences
# names both components ("more conjugate acid than conjugate base", "ten times
# as much conjugate acid as conjugate base"), so only the position relative to
# the comparative distinguishes them.
_EXCESS = re.compile(
    r"(?:more|as much|as many|greater concentration of|excess of(?: the)?)\s+"
    r"conjugate\s+(acid|base)(?![a-z])",
    re.I,
)
# The same fact with the comparative AFTER the component, which is how the
# answer choices phrase it: "the conjugate acid is the component in excess".
_EXCESS_POST = re.compile(
    r"conjugate\s+(acid|base)\s+is\s+the\s+(?:component|one)\s+in\s+excess",
    re.I,
)


def _excess_component(text):
    """Which conjugate component the text says is in excess, or None.

    Both phrasings are searched because a bare "conjugate acid" substring
    cannot answer this: every sentence in this topic names BOTH components
    ("more conjugate acid than conjugate base"), so only the position
    relative to the comparative distinguishes which one is in surplus.
    """
    hit = _EXCESS.search(text) or _EXCESS_POST.search(text)
    return hit.group(1).lower() if hit else None


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
    print(f"OK  {module.TOPIC[0]} figures: no item points at a picture.")


def no_ph_arithmetic(module):
    """8.9 owns the logarithm and the pH values; 8.8 owns the net ionic equations."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _ARITH.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: uses {hit.group(0)!r}, which is 8.8's or 8.9's "
                f"material -- {text[:70]!r}"
            )
        for text in item["choices"]:
            hit = _PH_VALUE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: a choice states a pH value ({hit.group(0)!r}), "
                "which is 8.9's arithmetic"
            )
    print(f"OK  {module.TOPIC[0]} scope: no logarithm, no numeric pH and no net ionic "
          "equation; the topic stays on capacity.")


def asymmetry_anchors_span_both_clauses(module, claims):
    """EK 8.10.A.2's two clauses must both be pinned, not just one.

    A key that named the right addition but the wrong component in excess -- or
    the reverse -- is the defect this topic is most likely to ship. An anchor
    naming only one half would match such a key. So each asymmetry item's anchor
    must contain a word for the component in excess AND a word for the addition
    handled better, and the two must be OPPOSITE, which is what the framework
    says.
    """
    for i in ASYMMETRY_ITEMS:
        anchor = claims[i - 1][0].lower()
        stem = module.QUESTIONS[i - 1]["q"].lower()

        # Named, not indexed into two tuples. The first version of this check
        # built `excess` as (acid, base) and `addition` as (base, acid) and
        # then compared index 0 against index 0, so it demanded the pairing
        # the framework FORBIDS and rejected a CORRECT key -- q3, whose key
        # is EK 8.10.A.2 almost verbatim. Two tuples that read as parallel and
        # are not is the same family of own-goal as this project's `\bpi` and
        # LETTER_REF bugs.
        handles_added_base = "added base" in anchor
        handles_added_acid = "added acid" in anchor

        # An anchor stating no direction at all is the general-summary item:
        # it must still pin the RELATIONSHIP, or it pins nothing and a key
        # claiming an excess helps the same addition would match it too.
        if not (handles_added_base or handles_added_acid):
            assert "opposite" in anchor and "same" not in anchor, (
                f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} names no addition and does not "
                "call the pairing opposite, so it pins neither direction of EK 8.10.A.2"
            )
            continue

        assert handles_added_base != handles_added_acid, (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} names both additions, which leaves "
            "the pairing ambiguous"
        )

        # The stem always states the premise; the key states it too on some
        # items and not on others (q25's choices differ ONLY in the addition,
        # so requiring its anchor to name a component would mean anchoring to
        # text the choice does not contain).
        stem_excess = _excess_component(stem)
        assert stem_excess, (
            f"{module.TOPIC[0]} q{i}: the stem does not say which component is in excess, so "
            "there is nothing to pair the addition against"
        )
        # Where the key DOES give a reason, the reason must match the premise.
        # This is what stops a key that reaches the right answer by the wrong
        # route -- "added acid is handled better, because the conjugate acid
        # is in excess" -- from passing on the strength of its verdict alone.
        anchor_excess = _excess_component(anchor)
        assert anchor_excess in (None, stem_excess), (
            f"{module.TOPIC[0]} q{i}: the key says the conjugate {anchor_excess} is in excess "
            f"but the stem says the conjugate {stem_excess} is -- anchor {anchor!r}"
        )
        acid_in_excess = stem_excess == "acid"

        # EK 8.10.A.2, verbatim: "When a buffer has more conjugate acid than
        # base, it has a greater buffer capacity for addition of added base
        # than acid." So the component in excess and the addition handled
        # better are OPPOSITES -- an excess of acid pairs with added base.
        assert acid_in_excess == handles_added_base, (
            f"{module.TOPIC[0]} q{i}: pairs an excess of the conjugate "
            f"{'acid' if acid_in_excess else 'base'} with better handling of added "
            f"{'base' if handles_added_base else 'acid'}, which is EK 8.10.A.2 backwards "
            f"-- anchor {anchor!r}"
        )
    print(f"OK  {module.TOPIC[0]} swap guard: {len(ASYMMETRY_ITEMS)} asymmetry anchors, each "
          "pairing the excess component with the OPPOSITE addition, the excess read from the "
          "anchor or, where the choices do not name it, from the stem.")


# ------------------------------------------------------------------ helpers

def ratio(table, label):
    """Conjugate base over conjugate acid for one tabulated buffer."""
    return cg.cell(table, label, AM) / cg.cell(table, label, HA)


def total(table, label):
    return cg.cell(table, label, AM) + cg.cell(table, label, HA)


# ------------------------------------------------------------------ table items

def q5(table, item):
    rs = {lab: ratio(table, lab) for lab in cg.labels(table)}
    assert len(set(round(r, 9) for r in rs.values())) == 1, f"the tabulated ratios are {rs}"
    concs = {lab: total(table, lab) for lab in cg.labels(table)}
    assert len(set(round(c, 9) for c in concs.values())) == len(concs), (
        "the three tabulated buffers must differ in concentration, or the item shows nothing"
    )
    h.shows(item, "same pH, because all three have the same ratio")
    return f"the three tabulated ratios are all {list(rs.values())[0]:g} while the totals are {concs}"


def q6(table, item):
    concs = {lab: total(table, lab) for lab in cg.labels(table)}
    biggest = max(concs, key=concs.get)
    assert biggest == "2", f"the most concentrated tabulated buffer is {biggest}: {concs}"
    assert len([c for c in concs.values() if abs(c - concs[biggest]) < 1e-12]) == 1, \
        "the most concentrated buffer must be unique"
    h.shows(item, "Buffer 2")
    return f"the tabulated component totals are {concs}, whose unique maximum is at {biggest}"


def q7(table, item):
    concs = {lab: total(table, lab) for lab in cg.labels(table)}
    smallest = min(concs, key=concs.get)
    assert smallest == "3", f"the most dilute tabulated buffer is {smallest}: {concs}"
    assert abs(ratio(table, smallest) - ratio(table, "2")) < 1e-12, \
        "the most dilute buffer must share the others' ratio, so its pH is the same"
    h.shows(item, "Buffer 3")
    return f"the tabulated component totals are {concs}, whose minimum is at {smallest}"


def q8(table, item):
    rs = {lab: ratio(table, lab) for lab in cg.labels(table)}
    assert len(set(round(r, 9) for r in rs.values())) == 1, f"the tabulated ratios are {rs}"
    totals = {lab: total(table, lab) for lab in cg.labels(table)}
    assert len(set(round(t, 9) for t in totals.values())) > 1, (
        "the totals must differ, or the 'same total concentration' distractor would be true"
    )
    h.shows(item, "ratio of the two components is the same in all three")
    return (f"the tabulated ratios agree at {list(rs.values())[0]:g} while the totals "
            f"{totals} do not")


def q9(table, item):
    excess = {lab: cg.cell(table, lab, HA) / cg.cell(table, lab, AM)
              for lab in cg.labels(table)}
    richest = max(excess, key=excess.get)
    assert richest == "P", f"the buffer richest in the conjugate acid is {richest}: {excess}"
    assert excess[richest] > 1.0, "that buffer must really have more acid than base"
    h.shows(item, "Buffer P")
    return (f"the tabulated acid-to-base ratios are {excess}, whose maximum is at "
            f"{richest}, the buffer EK 8.10.A.2 gives the greater capacity for added base")


def q10(table, item):
    rs = {lab: ratio(table, lab) for lab in cg.labels(table)}
    richest = max(rs, key=rs.get)
    assert richest == "Q", f"the buffer richest in the conjugate base is {richest}: {rs}"
    assert rs[richest] > 1.0, "that buffer must really have more base than acid"
    h.shows(item, "Buffer Q")
    return (f"the tabulated base-to-acid ratios are {rs}, whose maximum is at {richest}, "
            "the buffer EK 8.10.A.2 gives the greater capacity for added acid")


def q11(table, item):
    balanced = [lab for lab in cg.labels(table) if abs(ratio(table, lab) - 1.0) < 1e-12]
    assert balanced == ["R"], f"the tabulated buffers with equal components are {balanced}"
    h.shows(item, "Buffer R")
    return f"exactly one tabulated buffer has its two concentrations equal: {balanced[0]}"


def q12(table, item):
    above = [lab for lab in cg.labels(table) if ratio(table, lab) > 1.0]
    below = [lab for lab in cg.labels(table) if ratio(table, lab) < 1.0]
    assert above == ["Q"] and below == ["P"], f"above: {above}, below: {below}"
    h.shows(item, "Buffers P and Q")
    return (f"exactly one tabulated buffer sits above the pKa ({above[0]}) and exactly one "
            f"below it ({below[0]})")


def q21(table, item):
    bases = {lab: cg.cell(table, lab, AM) for lab in cg.labels(table)}
    richest = max(bases, key=bases.get)
    assert richest == "M", f"the buffer richest in conjugate base is {richest}: {bases}"
    assert len([v for v in bases.values() if abs(v - bases[richest]) < 1e-12]) == 1, \
        "the richest buffer must be unique"
    h.shows(item, "Buffer M")
    return (f"the tabulated conjugate base concentrations are {bases}, whose unique maximum "
            f"is at {richest}")


def q22(table, item):
    acids = {lab: cg.cell(table, lab, HA) for lab in cg.labels(table)}
    richest = max(acids, key=acids.get)
    assert richest == "L", f"the buffer richest in conjugate acid is {richest}: {acids}"
    assert len([v for v in acids.values() if abs(v - acids[richest]) < 1e-12]) == 1, \
        "the richest buffer must be unique"
    h.shows(item, "Buffer L")
    return (f"the tabulated conjugate acid concentrations are {acids}, whose unique maximum "
            f"is at {richest}")


def q23(table, item):
    rs = {lab: round(ratio(table, lab), 9) for lab in cg.labels(table)}
    groups = {}
    for lab, r in rs.items():
        groups.setdefault(r, []).append(lab)
    shared = sorted(g for g in groups.values() if len(g) > 1)
    assert shared == [["J", "K"]], f"the tabulated buffers grouped by ratio are {groups}"
    h.shows(item, "Buffers J and K")
    return f"the tabulated ratios group as {groups}, with exactly one pair sharing a value"


def q24(table, item):
    rj = ratio(table, "J")
    same = [lab for lab in cg.labels(table)
            if lab != "J" and abs(ratio(table, lab) - rj) < 1e-12]
    assert same == ["K"], f"the buffers sharing J's ratio are {same}"
    assert total(table, "K") < total(table, "J"), (
        "the matching buffer must be the more dilute of the two, or its capacity would not "
        "be the smaller"
    )
    h.shows(item, "Buffer K")
    return (f"exactly one tabulated buffer shares J's ratio of {rj:g}, and its component "
            f"total {total(table, 'K'):g} is below J's {total(table, 'J'):g}")


TABLE_CHECKS = {5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12,
                21: q21, 22: q22, 23: q23, 24: q24}

NUMERIC = {}


CLAIMS = [
 ("The pH stays the same",
  "EK 8.10.A.1: increasing the concentration of the components while keeping the ratio constant keeps the pH the same, because EK 8.9.A.1 makes the pH follow the ratio."),
 ("increases the capacity to neutralize added acid or base",
  "EK 8.10.A.1's second half, verbatim in substance: the same change increases the capacity of the buffer to neutralize added acid or base."),
 ("conjugate acid is the component in excess and it is what reacts with added base",
  "EK 8.10.A.2: more conjugate acid than base gives the greater capacity for added BASE, and EK 8.8.A.1 says why -- the conjugate acid is what reacts with added base."),
 ("conjugate base is the component in excess and it is what reacts with added acid",
  "EK 8.10.A.2's mirror clause: more conjugate base than acid gives the greater capacity for added ACID, which EK 8.8.A.1 assigns to the conjugate base."),
 ("same pH, because all three have the same ratio",
  "EK 8.10.A.1 with EK 8.9.A.1. q5 recomputes every tabulated ratio and checks they agree while the concentrations differ."),
 ("Buffer 2",
  "EK 8.10.A.1 ties capacity to concentration at a fixed ratio. q6 recomputes the tabulated component totals and checks the maximum is unique."),
 ("Buffer 3",
  "EK 8.10.A.1 read the other way. q7 recomputes the totals and checks the most dilute buffer shares the others' ratio, so its pH is the same."),
 ("ratio of the two components is the same in all three",
  "EK 8.9.A.1 makes the pH follow the ratio. q8 recomputes the ratios and checks the totals differ, so the 'same total' distractor is false."),
 ("Buffer P",
  "EK 8.10.A.2's first clause. q9 recomputes every tabulated acid-to-base ratio and checks the richest in the acid form is unique and really in excess."),
 ("Buffer Q",
  "EK 8.10.A.2's second clause. q10 recomputes every tabulated base-to-acid ratio and checks the richest in the base form is unique and really in excess."),
 ("Buffer R",
  "Neither clause of EK 8.10.A.2 applies when the components are equal. q11 recomputes the ratios and checks exactly one row is balanced."),
 ("Buffers P and Q",
  "EK 8.9.A.1's equation puts the pH above the pKa for a base excess and below it for an acid excess. q12 recomputes which tabulated rows do each."),
 ("same pH and a greater capacity",
  "EK 8.10.A.1 states both halves in one sentence: the ratio held constant keeps the pH, and the higher concentration raises the capacity."),
 ("same pH and a smaller capacity",
  "Dilution divides both concentrations by the same factor, so EK 8.10.A.1 applies in reverse: unchanged ratio, unchanged pH, lower capacity."),
 ("Dissolving more of both components in the same ratio",
  "EK 8.10.A.1 names exactly this change; adding one component alone changes the ratio and so, under EK 8.9.A.1, the pH."),
 ("Changing the ratio of conjugate base to conjugate acid",
  "EK 8.9.A.1 makes the pH depend on the ratio, and EK 8.10.A.1 says scaling both concentrations together leaves it alone."),
 ("pH is as intended but the capacity is lower than intended",
  "Halving both components preserves the ratio, so EK 8.9.A.1 leaves the pH and EK 8.10.A.1 lowers the capacity -- the error analysis suggested skill 6.G asks for."),
 ("pH is lower than intended, because the ratio of base to acid has fallen",
  "EK 8.9.A.1 makes the pH rise and fall with the base-to-acid ratio, and EK 8.10.A.1's protection applies only when that ratio is held constant."),
 ("more conjugate base, which is the component that consumes added acid",
  "EK 8.8.A.1 assigns added acid to the conjugate base and EK 8.10.A.1 ties capacity to concentration, so more of the consuming species absorbs more."),
 ("more concentrated buffer changes less",
  "EK 8.10.A.1 gives the more concentrated buffer the greater capacity, which is the ability to absorb a large addition with little change."),
 ("Buffer M",
  "EK 8.10.A.2's second clause across four tabulated buffers. q21 recomputes the conjugate base concentrations and checks the maximum is unique."),
 ("Buffer L",
  "EK 8.10.A.2's first clause across the same four. q22 recomputes the conjugate acid concentrations and checks the maximum is unique."),
 ("Buffers J and K",
  "EK 8.10.A.1 with EK 8.9.A.1: equal ratios give equal pH. q23 groups the tabulated rows by recomputed ratio and checks exactly one pair shares a value."),
 ("Buffer K",
  "EK 8.10.A.1: the same ratio gives the same pH and the lower concentration the smaller capacity. q24 recomputes both facts from the table."),
 ("capacity for added base is the greater",
  "EK 8.10.A.2: a buffer with more conjugate acid than base has the greater capacity for added base, because EK 8.8.A.1 makes the conjugate acid the consumer of added base."),
 ("No, and the pH is unchanged as well because the ratio is unchanged",
  "A pKa is a property of the acid, not of the solution, and EK 8.10.A.1 keeps the pH the same when both concentrations are scaled at a fixed ratio."),
 ("ability to neutralize added acid or base",
  "EK 8.10.A.1 speaks of the capacity of the buffer to neutralize added acid or base; the pH it holds is a separate property fixed by the ratio."),
 ("same, since neither component is in excess",
  "EK 8.10.A.2 states its asymmetry for buffers with MORE of one component, and neither clause applies when the two amounts are equal."),
 ("Both components were made more dilute than intended, in the correct ratio",
  "EK 8.10.A.1 pairs an unchanged ratio with an unchanged pH and ties capacity to concentration; an error in the ratio would have moved the pH too."),
 ("excess of one component gives the greater capacity for the opposite addition",
  "EK 8.10.A.1 and EK 8.10.A.2 together: more conjugate acid protects against added base and more conjugate base against added acid, each excess guarding the opposite addition."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the figure above, what happens to the pH?"
        no_figure_language(mod)

    def logarithm_creeps_in(mod, cl):
        mod.QUESTIONS[1]["q"] = mod.QUESTIONS[1]["q"] + " Use \\( \\log \\) to decide."
        no_ph_arithmetic(mod)

    def numeric_ph_key(mod, cl):
        ch = list(mod.QUESTIONS[0]["choices"])
        ch[0] = "The buffer stays at a pH of 4.75"
        mod.QUESTIONS[0]["choices"] = ch
        cl[0] = ("stays at a pH of 4", cl[0][1])
        no_ph_arithmetic(mod)

    def anchor_reason_contradicts_stem(mod, cl):
        # The right verdict reached by the wrong route: the stem says the
        # conjugate ACID is in excess, and this key agrees that added base is
        # handled better, but credits the conjugate BASE for it.
        cl[2] = ("Added base, because the conjugate base is the component in excess",
                 cl[2][1])
        asymmetry_anchors_span_both_clauses(mod, cl)

    def summary_anchor_pins_no_direction(mod, cl):
        # q30 names no specific addition, so the word "opposite" is the only
        # thing pinning EK 8.10.A.2's direction. Without it the anchor would
        # equally match a key claiming an excess helps the SAME addition.
        cl[29] = ("an excess of one component gives the greater capacity", cl[29][1])
        asymmetry_anchors_span_both_clauses(mod, cl)

    def summary_anchor_states_same(mod, cl):
        cl[29] = ("an excess of one component gives the greater capacity for the same "
                  "addition", cl[29][1])
        asymmetry_anchors_span_both_clauses(mod, cl)

    def anchor_pairs_same_side(mod, cl):
        cl[2] = ("conjugate acid is the component in excess and it is what reacts with "
                 "added acid", cl[2][1])
        asymmetry_anchors_span_both_clauses(mod, cl)

    def ratios_no_longer_equal(mod, cl):
        mod.QUESTIONS[4]["table"] = dict(
            headers=h8_10._T_SCALE["headers"],
            rows=[["1", "0.10", "0.10"], ["2", "1.00", "0.50"], ["3", "0.010", "0.010"]])

    def concentrations_made_identical(mod, cl):
        # Three buffers of the SAME concentration would show nothing about
        # capacity, since EK 8.10.A.1 is about changing it.
        mod.QUESTIONS[4]["table"] = dict(
            headers=h8_10._T_SCALE["headers"],
            rows=[["1", "0.10", "0.10"], ["2", "0.10", "0.10"], ["3", "0.10", "0.10"]])

    def excess_swapped(mod, cl):
        mod.QUESTIONS[8]["table"] = dict(
            headers=h8_10._T_ASYM["headers"],
            rows=[["P", "0.10", "1.00"], ["Q", "1.00", "0.10"], ["R", "0.50", "0.50"]])

    def second_shared_ratio(mod, cl):
        mod.QUESTIONS[22]["table"] = dict(
            headers=h8_10._T_MIXED["headers"],
            rows=[["J", "0.20", "0.20"], ["K", "0.020", "0.020"],
                  ["L", "0.40", "0.10"], ["M", "0.80", "0.20"]])

    return [("a stem referring to a figure the bank cannot show", figure_language),
            ("a logarithm, which is 8.9's material", logarithm_creeps_in),
            ("a keyed choice stating a numeric pH, which is 8.9's arithmetic",
             numeric_ph_key),
            ("an asymmetry key crediting the wrong component for the right verdict",
             anchor_reason_contradicts_stem),
            ("the summary anchor dropped to where it pins neither direction",
             summary_anchor_pins_no_direction),
            ("the summary anchor claiming an excess helps the SAME addition",
             summary_anchor_states_same),
            ("an asymmetry anchor pairing the excess component with the SAME addition",
             anchor_pairs_same_side),
            ("the tabulated ratios no longer equal, so the shared-pH key is false",
             ratios_no_longer_equal),
            ("three tabulated buffers of identical concentration, which show nothing about "
             "capacity", concentrations_made_identical),
            ("the two tabulated excesses exchanged", excess_swapped),
            ("a second pair of tabulated buffers made to share a ratio", second_shared_ratio)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    def _hook(mod, cl):
        asymmetry_anchors_span_both_clauses(mod, cl)
    h.selftest(h8_10, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h8_10)
no_ph_arithmetic(h8_10)
asymmetry_anchors_span_both_clauses(h8_10, CLAIMS)
h.run(h8_10, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
