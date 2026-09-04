"""Key audit for AP CHEMISTRY 2.6 Resonance and Formal Charge.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Fourteen stem-arithmetic items and seven
table items -- twenty-one of the thirty -- are recomputed here from the item's
own stimulus.

WHAT THE KEYS REST ON
---------------------
EK 2.6.A.1  Where more than one EQUIVALENT Lewis structure can be constructed,
            resonance must be included as a refinement; in many such cases the
            refinement is needed for qualitatively accurate predictions of
            molecular structure and properties.        (items 1, 2, 14, 22)
EK 2.6.A.2  The octet rule and formal charge can be used as criteria for
            determining which of several possible valid Lewis diagrams provides
            the best model.       (items 4, 8, 14, and every formal-charge item)
EK 2.6.A.3  As with any model there are limitations to the Lewis structure
            model, particularly for an odd number of valence electrons.
                                       (items 6, 10, 16, 18, 25, 27, 30)

THE DEFINITION OF FORMAL CHARGE IS NOT IN THE CED, and this module does not
pretend otherwise. EK 2.6.A.2 names formal charge as a criterion and unit 2's
own page tells students to practise calculating it, but no sentence in the
framework states the arithmetic. So every calculating item STATES THE RULE IN
ITS OWN STEM, and ``rule_stated_in_the_stem`` asserts that all thirteen of them
do. The key then rests on arithmetic the item supplied, which is a thing a
verifier can check, rather than on a definition recalled from a textbook.

THE SAME MOVE FOR THE RANKING ITEM. EK 2.6.A.2 licenses formal charge as a
criterion but never says which way the comparison runs, so item 12 states its
comparison ("closest to zero") in the stem and asks the student to carry it out.

ITEM 21 CHECKS ITSELF TWICE. The three formal charges are recomputed and added,
AND the sum is compared against the overall charge the stem states for the ion,
which is a constraint the item's own numbers either satisfy or fail. A stem
whose electron counts did not describe a real diagram of that ion would fail
here rather than teach a student to add wrong numbers.

SCOPE. ``no_geometry_or_hybridization`` keeps EK 2.7.A.2's geometry and bond
angles and EK 2.7.A.3's hybridization inside topic 2.7.

NEGATIVE CONTROL: ``python3 verify_h2_6.py --selftest``.
"""
import re
import sys

import h_chem_notation as hn
import h2_6 as M

FORMULA = "Formula"
CHARGE = "Overall charge"
NONZERO = "Number of atoms carrying a nonzero formal charge"
LARGEST = "Largest formal charge magnitude on any one atom"

# Group valence-electron counts, read off the periodic table the AP Chemistry
# exam supplies. EK 1.5.A.3 is what makes these the electrons a Lewis diagram
# displays; nothing here is a remembered molecular structure.
VALENCE = {"H": 1, "C": 4, "N": 5, "O": 6, "F": 7, "Si": 4, "P": 5, "S": 6,
           "Cl": 7, "Se": 6, "Br": 7, "I": 7}

ELEMENT_NAME = {"hydrogen": "H", "carbon": "C", "nitrogen": "N", "oxygen": "O",
                "fluorine": "F", "phosphorus": "P", "sulfur": "S",
                "chlorine": "Cl", "bromine": "Br", "iodine": "I"}

COUNTWORD = {0: "None of them", 1: "Exactly one", 2: "Exactly two",
             3: "Exactly three", 4: "All four"}

_ATOM = re.compile(r"([A-Z][a-z]?)(\d*)")
# The stems phrase the same fact three ways ("has", "with", and a bare "gives an
# oxygen atom 6 electrons"), so the verb is optional here. It was NOT optional in
# the first draft, and the check crashed rather than passing silently -- which is
# the failure mode to prefer, but the pattern still had to be widened.
_ATOM_IN_STEM = re.compile(
    r"([a-z]+) atom (?:has |with )?(\d+) electrons in lone pairs and (\d+) "
    r"electrons in bonds")
_FORM_IN_STEM = re.compile(r"formula is ([A-Z][A-Za-z0-9]*)(?![A-Za-z0-9])")
_CHARGE_IN_STEM = re.compile(r"overall charge of (\d)([+-])(?![0-9])")
_NEUTRAL = re.compile(r"(?<![a-z])neutral overall(?![a-z])")
_THE_RULE = re.compile(
    r"minus half the number of electrons it shares in bonds")

cg = hn.cg


# ----------------------------------------------------------------- helpers

def atoms(formula):
    """{symbol: count} for a plain-text formula such as ClO2."""
    parsed = _ATOM.findall(formula)
    rebuilt = "".join(sym + digits for sym, digits in parsed)
    assert rebuilt == formula, (
        f"the formula {formula!r} did not parse cleanly; it rebuilds as {rebuilt!r}"
    )
    out = {}
    for sym, digits in parsed:
        assert sym in VALENCE, f"no valence-electron count recorded for {sym!r}"
        out[sym] = out.get(sym, 0) + (int(digits) if digits else 1)
    return out


def valence_total(formula, charge):
    return sum(VALENCE[s] * n for s, n in atoms(formula).items()) - charge


def read_charge(text):
    hit = _CHARGE_IN_STEM.search(text)
    if hit:
        return int(hit.group(1)) * (1 if hit.group(2) == "+" else -1)
    assert _NEUTRAL.search(text), f"neither a charge nor 'neutral overall': {text[:80]!r}"
    return 0


def formal_charges(stem):
    """[(element name, formal charge)] for every atom the stem describes."""
    hits = _ATOM_IN_STEM.findall(stem)
    assert hits, f"the stem describes no atom this check can read: {stem[:80]!r}"
    out = []
    for name, lone, bonds in hits:
        sym = ELEMENT_NAME.get(name)
        assert sym, f"unrecognized element name {name!r} in the stem"
        lone, bonds = int(lone), int(bonds)
        assert bonds % 2 == 0, f"{bonds} bonding electrons does not halve evenly"
        out.append((name, VALENCE[sym] - lone - bonds // 2))
    return out


def signed(value):
    return f"{value:+d}" if value else "0"


# --------------------------------------------------------- stem-numeric checks

def one_atom(item):
    """The keyed formal charge is the one the stem's own numbers give."""
    charges = formal_charges(item["q"])
    assert len(charges) == 1, (
        f"the stem describes {len(charges)} atoms; this check expects exactly one"
    )
    name, fc = charges[0]
    assert _THE_RULE.search(item["q"]), "the stem does not state the formal-charge rule"
    hn.keyed(item, f"formal charge of {signed(fc)}")
    return (f"the stem's own numbers give the {name} a formal charge of {signed(fc)} under "
            "the rule the stem itself states")


def a21(item):
    """Add the stem's formal charges, and check the total against the ion's charge."""
    stem = item["q"]
    assert _THE_RULE.search(stem), "the stem does not state the formal-charge rule"
    charges = formal_charges(stem)
    assert len(charges) >= 3, f"the stem describes only {len(charges)} atoms"
    total = sum(fc for _, fc in charges)
    formula = _FORM_IN_STEM.search(stem)
    assert formula, "the stem states no formula to check the sum against"
    counted = len(charges)
    assert counted == sum(atoms(formula.group(1)).values()), (
        f"the stem describes {counted} atoms but the formula {formula.group(1)} has "
        f"{sum(atoms(formula.group(1)).values())}"
    )
    overall = read_charge(stem)
    assert total == overall, (
        f"the formal charges sum to {total} but the stem gives the species an overall "
        f"charge of {overall}; the stem's own numbers do not describe a diagram of it"
    )
    hn.keyed(item, f"sum of {signed(total)}")
    return (f"the three atoms carry {', '.join(signed(fc) for _, fc in charges)}, summing "
            f"to {signed(total)}, which equals the ion's own overall charge")


def a25(item):
    """The species really does bring an odd number of valence electrons."""
    stem = item["q"]
    formula = _FORM_IN_STEM.search(stem)
    assert formula, f"the stem states no formula: {stem[:80]!r}"
    total = valence_total(formula.group(1), read_charge(stem))
    assert total % 2 == 1, (
        f"{formula.group(1)} brings {total} valence electrons, which is EVEN, so the stem's "
        "premise and the keyed conclusion both fail"
    )
    hn.keyed(item, "At least one electron must be left unpaired")
    return (f"{formula.group(1)} brings {total} valence electrons, an odd total, so the "
            "electrons cannot all be arranged in pairs")


ARITH = {3: one_atom, 5: one_atom, 7: one_atom, 9: one_atom, 11: one_atom,
         13: one_atom, 15: one_atom, 17: one_atom, 19: one_atom, 21: a21,
         23: one_atom, 25: a25, 26: one_atom, 29: one_atom}

RULE_ITEMS = sorted(i for i, fn in ARITH.items() if fn in (one_atom, a21))


# ------------------------------------------------------------ table questions

def _parity(table):
    """[(label, total valence electrons)] for each tabulated species."""
    heads = list(table["headers"])
    fi, ci = heads.index(FORMULA), heads.index(CHARGE)
    out = []
    for row in table["rows"]:
        charge = str(row[ci]).strip()
        if charge.lower() == "neutral":
            signed_charge = 0
        else:
            m = re.fullmatch(r"(\d)([+-])", charge)
            assert m, f"cannot read the tabulated charge {charge!r}"
            signed_charge = int(m.group(1)) * (1 if m.group(2) == "+" else -1)
        out.append((str(row[0]), valence_total(str(row[fi]), signed_charge)))
    return out


def _the_one_odd(table, item):
    rows = _parity(table)
    odd = [lab for lab, n in rows if n % 2 == 1]
    assert len(odd) == 1, (
        f"{len(odd)} tabulated species have an odd valence-electron count: {odd}; the item "
        "needs exactly one"
    )
    hn.keyed(item, odd[0])
    return (f"the tabulated totals are {', '.join(str(n) for _, n in rows)}, and only "
            f"{odd[0]} is odd")


def q6(t, item):
    return _the_one_odd(t, item)


def q16(t, item):
    return _the_one_odd(t, item)


def q27(t, item):
    rows = _parity(t)
    odd = [lab for lab, n in rows if n % 2 == 1]
    hn.keyed(item, COUNTWORD[len(odd)])
    return (f"the tabulated totals are {', '.join(str(n) for _, n in rows)}, of which "
            f"{len(odd)} are odd, namely {', '.join(odd) or 'none'}")


def _candidates(table):
    return list(zip(cg.labels(table), cg.col(table, NONZERO), cg.col(table, LARGEST)))


def q12(t, item):
    rows = _candidates(t)
    best = min(rows, key=lambda r: (r[1], r[2]))
    others = [r for r in rows if r[0] != best[0]]
    assert all(r[1] > best[1] and r[2] > best[2] for r in others), (
        "the preferred diagram does not win on BOTH tabulated columns, so 'closest to "
        "zero' does not pick it out unambiguously"
    )
    hn.keyed(item, best[0])
    return (f"{best[0]} carries {best[1]:g} atoms with nonzero formal charge and a largest "
            f"magnitude of {best[2]:g}, the smallest value in both columns")


def q20(t, item):
    rows = _candidates(t)
    by_size = sorted(rows, key=lambda r: -r[2])
    assert by_size[0][2] > by_size[1][2], "two diagrams tie for the largest single charge"
    by_count = max(rows, key=lambda r: r[1])
    assert by_count[0] != by_size[0][0], (
        "the diagram with the most charged atoms is also the one with the largest single "
        "charge, so the rejected reasoning would reach the keyed answer"
    )
    hn.keyed(item, by_size[0][0])
    return (f"{by_size[0][0]} carries the largest single magnitude at {by_size[0][2]:g}, "
            f"while the most charged atoms belong to {by_count[0]} instead")


def q24(t, item):
    rows = _candidates(t)
    by_count = sorted(rows, key=lambda r: -r[1])
    assert by_count[0][1] > by_count[1][1], "two diagrams tie for the most charged atoms"
    by_size = max(rows, key=lambda r: r[2])
    assert by_size[0] != by_count[0][0], (
        "the diagram with the most charged atoms is also the one with the largest single "
        "charge, so the rejected reasoning would reach the keyed answer"
    )
    hn.keyed(item, by_count[0][0])
    return (f"{by_count[0][0]} spreads nonzero formal charge over {by_count[0][1]:g} atoms, "
            f"more than any other, while the largest single charge is {by_size[0]}'s")


def q28(t, item):
    rows = _candidates(t)
    heavy = [r[0] for r in rows if r[2] >= 2]
    hn.keyed(item, COUNTWORD[len(heavy)])
    return (f"{len(heavy)} of the {len(rows)} tabulated diagrams reach a formal charge "
            f"magnitude of two or more, namely {', '.join(heavy) or 'none'}")


TABLE_CHECKS = {6: q6, 12: q12, 16: q16, 20: q20, 24: q24, 27: q27, 28: q28}


# ------------------------------------------------------- module-specific gates

_TOPIC_2_7 = re.compile(
    r"(?<![a-z])(?:molecular geometry|VSEPR|hybridi[sz]ed|hybridi[sz]ation|"
    r"hybrid orbitals?|sigma bonds?|pi bonds?|trigonal|tetrahedral|octahedral)(?![a-z])",
    re.I)

_FIGURE = re.compile(
    r"(?<![a-z])(?:diagram shown|shown above|shown below|the figure|the picture|"
    r"pictured|as drawn above)(?![a-z])", re.I)


def rule_stated_in_the_stem(module):
    """Every calculating item supplies the formal-charge rule the CED does not."""
    code = module.TOPIC[0]
    for i in RULE_ITEMS:
        stem = module.QUESTIONS[i - 1]["q"]
        assert _THE_RULE.search(stem), (
            f"{code} q{i}: asks for a formal charge without stating the rule in its own "
            f"stem, which would key the answer to a definition the CED never prints -- "
            f"{stem[:70]!r}"
        )
    stated = sum(1 for item in module.QUESTIONS if _THE_RULE.search(item["q"]))
    assert stated == len(RULE_ITEMS), (
        f"{code}: {stated} stems state the formal-charge rule but {len(RULE_ITEMS)} items "
        "are checked against it; the two sets must agree"
    )
    print(f"OK  {code} honesty: all {len(RULE_ITEMS)} calculating item(s) state the "
          "formal-charge rule in their own stem, since the CED never defines it.")


def no_geometry_or_hybridization(module):
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            hit = _TOPIC_2_7.search(text)
            assert not hit, (
                f"{code} q{i}: mentions {hit.group(0)!r}, which is EK 2.7.A.2 and 2.7.A.3's "
                f"material and belongs to topic 2.7 -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: no item touches molecular geometry or hybridization, which "
          "topic 2.7 owns.")


def no_figure_language(module):
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{code} q{i}: refers to {hit.group(0)!r}, but this bank cannot show a "
                f"Lewis diagram -- {text[:70]!r}"
            )
    print(f"OK  {code} figures: every candidate diagram is described by its numbers, never "
          "by a picture.")


CLAIMS = [
 ("resonance be included as a refinement",
  "EK 2.6.A.1, verbatim: in cases where more than one equivalent Lewis structure can be constructed, resonance must be included as a refinement to the Lewis structure."),
 ("qualitatively accurate predictions of molecular structure",
  "EK 2.6.A.1 gives this reason in its own words: in many such cases this refinement is needed to provide qualitatively accurate predictions of molecular structure and properties."),
 ("formal charge of +1",
  "EK 2.6.A.2 makes formal charge a criterion among valid Lewis diagrams. Recomputed from the stem's own numbers under the rule the stem itself states."),
 ("octet rule and formal charge",
  "EK 2.6.A.2, verbatim: the octet rule and formal charge can be used as criteria for determining which of several possible valid Lewis diagrams provides the best model."),
 ("formal charge of 0",
  "EK 2.6.A.2 makes formal charge a criterion among valid diagrams. Recomputed from the stem's own numbers; forgetting to halve the bonding electrons gives a rejected value."),
 ("Nitrogen monoxide",
  "EK 2.6.A.3 names an odd valence-electron count as where the Lewis model's limitations particularly show. Recomputed in q6 by summing each tabulated formula, which finds exactly one odd total."),
 ("formal charge of -1",
  "EK 2.6.A.2 makes formal charge a criterion among valid diagrams. Recomputed from the stem's own numbers; a sign error gives the mirror-image rejected value."),
 ("best model for predicting molecular structure and properties",
  "EK 2.6.A.2 states the purpose in exactly those words: the criteria determine which of several possible VALID diagrams provides the best model."),
 ("formal charge of 0",
  "EK 2.6.A.2 makes formal charge a criterion among valid diagrams. Recomputed from the stem's own numbers for a carbon atom with four bonds and no lone pair."),
 ("limitations, particularly for species with an odd number of valence electrons",
  "EK 2.6.A.3, verbatim in substance: as with any model there are limitations to the use of the Lewis structure model, particularly in cases with an odd number of valence electrons."),
 ("formal charge of +1",
  "EK 2.6.A.2 makes formal charge a criterion among valid diagrams. Recomputed from the stem's own numbers for sulfur, whose six valence electrons the arithmetic starts from."),
 ("Diagram 1",
  "EK 2.6.A.2 licenses formal charge as a criterion and the stem states which way the comparison runs. Recomputed in q12, which asserts the winning diagram is smallest in BOTH tabulated columns, so the comparison is unambiguous."),
 ("formal charge of +1",
  "EK 2.6.A.2 makes formal charge a criterion among valid diagrams. Recomputed from the stem's own numbers for an oxygen holding one lone pair and three bonds' worth of shared electrons."),
 ("octet rule and formal charge, used as criteria to select the better diagram",
  "EK 2.6.A.1 conditions resonance on more than one EQUIVALENT structure, so it does not reach nonequivalent diagrams; EK 2.6.A.2 supplies the criteria for that case, and LO 2.6.A puts the two side by side."),
 ("formal charge of 0",
  "EK 2.6.A.2 makes formal charge a criterion among valid diagrams. Recomputed from the stem's own numbers for a nitrogen with one lone pair and three bonds."),
 ("Nitrogen dioxide",
  "EK 2.6.A.3 names an odd valence-electron count as the limiting case. Recomputed in q16 by summing each tabulated formula, which finds exactly one odd total."),
 ("formal charge of +3",
  "EK 2.6.A.2 makes formal charge a criterion among valid diagrams. Recomputed from the stem's own numbers for chlorine, whose seven valence electrons the arithmetic starts from."),
 ("expected of models generally",
  "EK 2.6.A.3 opens with 'as with any model', which places the Lewis model among models in general while still naming the odd-electron case as where its limitations particularly show."),
 ("formal charge of -1",
  "EK 2.6.A.2 makes formal charge a criterion among valid diagrams. Recomputed from the stem's own numbers for a carbon holding one lone pair."),
 ("Diagram 4",
  "Recomputed in q20 from the tabulated largest-magnitude column, with a check that the diagram carrying the most charged atoms is a DIFFERENT one, so the rejected reasoning cannot reach the key."),
 ("sum of -1",
  "EK 2.6.A.2 makes formal charge a criterion among valid diagrams. Recomputed in a21 atom by atom and added, and the total is checked against the overall charge the stem gives the ion."),
 ("needed in every case where equivalent structures exist",
  "EK 2.6.A.1 makes the INCLUSION of resonance unconditional but hedges its necessity for accurate prediction with 'in many such cases', so a universal claim about the prediction goes beyond the sentence."),
 ("formal charge of -1",
  "EK 2.6.A.2 makes formal charge a criterion among valid diagrams. Recomputed from the stem's own numbers for a nitrogen with two lone pairs and two bonds."),
 ("Diagram 3",
  "Recomputed in q24 from the tabulated count of atoms carrying nonzero formal charge, with a check that the largest single charge belongs to a DIFFERENT diagram."),
 ("At least one electron must be left unpaired",
  "Summing the valence electrons of the stem's own formula gives an odd total, which cannot divide entirely into pairs. EK 2.6.A.3 names exactly this case as where the Lewis model's limitations particularly show."),
 ("formal charge of 0",
  "EK 2.6.A.2 makes formal charge a criterion among valid diagrams. Recomputed from the stem's own numbers for phosphorus, which shares nitrogen's column and so its valence count."),
 ("Exactly two",
  "EK 2.6.A.3 makes the odd valence-electron count the limiting case. Recomputed in q27 by summing each tabulated formula and counting the odd totals."),
 ("Exactly two",
  "Recomputed in q28 from the tabulated largest-magnitude column against the threshold the stem states. EK 2.6.A.2 is what makes formal charge worth measuring across candidates."),
 ("formal charge of -2",
  "EK 2.6.A.2 makes formal charge a criterion among valid diagrams. Recomputed from the stem's own numbers for a carbon holding two lone pairs."),
 ("applies without limitation to every species",
  "EK 2.6.A.3 states that there are limitations to the use of the Lewis structure model, so a claim of none contradicts it; EK 2.6.A.1 and EK 2.6.A.2 supply the remaining rejected statements."),
]


# ------------------------------------------------------------ negative controls

def _swap(mod, i, old, new):
    before = mod.QUESTIONS[i - 1]["q"]
    after = before.replace(old, new)
    assert after != before, f"the control's replacement {old!r} did not match q{i}'s stem"
    mod.QUESTIONS[i - 1]["q"] = after


def _retable(mod, i, label, **cells):
    t = mod.QUESTIONS[i - 1]["table"]
    heads = list(t["headers"])
    rows = []
    for row in t["rows"]:
        row = list(row)
        if str(row[0]) == label:
            for header, value in cells.items():
                row[heads.index(header)] = value
        rows.append(row)
    mod.QUESTIONS[i - 1]["table"] = dict(headers=heads, rows=rows)


def _lone_pairs_change(mod, cl):
    """Change a stated lone-pair count under a keyed formal charge."""
    _swap(mod, 3, "has 0 electrons in lone pairs", "has 2 electrons in lone pairs")


def _element_changes(mod, cl):
    """Change the element under a keyed formal charge, leaving the key behind."""
    _swap(mod, 11, "A sulfur atom", "A carbon atom")


def _rule_removed(mod, cl):
    """Delete the stated rule, so the item would key to an undocumented definition."""
    before = mod.QUESTIONS[8]["q"]
    after = before.replace(
        "minus half the number of electrons it shares in bonds, ", "")
    assert after != before, "the control's replacement did not match the stem"
    mod.QUESTIONS[8]["q"] = after
    rule_stated_in_the_stem(mod)


def _sum_stops_matching_the_charge(mod, cl):
    """Break the cross-check: the formal charges no longer add to the ion's charge."""
    _swap(mod, 21, "the other oxygen atom has 6 electrons",
          "the other oxygen atom has 4 electrons")


def _parity_premise_fails(mod, cl):
    """Make the odd-electron item's own species even, so its premise is false."""
    _swap(mod, 25, "formula is NO2", "formula is SO2")


def _second_odd_species(mod, cl):
    """Give the parity table a second odd species, so the item has two answers."""
    _retable(mod, 6, "Water", **{FORMULA: "OH"})


def _parity_count_changes(mod, cl):
    """Change how many tabulated species are odd."""
    _retable(mod, 27, "Chlorine dioxide", **{FORMULA: "SO2"})


def _two_diagrams_tie_for_best(mod, cl):
    """Make a second diagram carry no formal charge, so 'closest to zero' is ambiguous."""
    _retable(mod, 12, "Diagram 2", **{NONZERO: "0", LARGEST: "0"})


def _largest_charge_ties(mod, cl):
    """Give two diagrams the same largest single formal charge."""
    _retable(mod, 20, "Diagram 3", **{LARGEST: "3"})


def _same_diagram_wins_both_columns(mod, cl):
    """Let one diagram carry both the most charged atoms and the largest single charge.

    This is the control that matters for q24: if Diagram 3 also carried the biggest
    single charge, the rejected reasoning would arrive at the keyed answer and the
    item would no longer distinguish the two columns. Raising ITS magnitude is what
    creates that collapse; lowering some other row's would not.
    """
    _retable(mod, 24, "Diagram 3", **{LARGEST: "4"})


def _threshold_count_changes(mod, cl):
    """Change how many diagrams reach a magnitude of two."""
    _retable(mod, 28, "Diagram 3", **{LARGEST: "1"})


def _geometry_creeps_in(mod, cl):
    mod.QUESTIONS[0]["q"] = "Which molecular geometry does the resonance refinement predict?"
    no_geometry_or_hybridization(mod)


def _figure_language(mod, cl):
    mod.QUESTIONS[1]["q"] = "In the diagram shown above, why is the refinement needed?"
    no_figure_language(mod)


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH, extra=[
        ("a stated lone-pair count changed under a keyed formal charge",
         _lone_pairs_change),
        ("the element changed under a keyed formal charge", _element_changes),
        ("the formal-charge rule deleted from a calculating stem", _rule_removed),
        ("the summed formal charges no longer matching the ion's own charge",
         _sum_stops_matching_the_charge),
        ("the odd-electron item given a species with an even count", _parity_premise_fails),
        ("a second odd species added to the parity table", _second_odd_species),
        ("the parity table's count of odd species changed", _parity_count_changes),
        ("a second diagram made to carry no formal charge, so the best is ambiguous",
         _two_diagrams_tie_for_best),
        ("two diagrams tied for the largest single formal charge", _largest_charge_ties),
        ("one diagram made to win both tabulated columns, collapsing the distinction",
         _same_diagram_wins_both_columns),
        ("the count of diagrams reaching magnitude two changed", _threshold_count_changes),
        ("molecular geometry, which is topic 2.7's, moved into a stem", _geometry_creeps_in),
        ("a stem pointing at a drawn diagram the bank cannot show", _figure_language),
    ])

rule_stated_in_the_stem(M)
no_geometry_or_hybridization(M)
no_figure_language(M)
hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
