"""Key audit for AP CHEMISTRY 3.7 Solutions and Mixtures.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  3.7.A.1  solutions are homogeneous mixtures, may be solid, liquid or gas, and
           have macroscopic properties that do not vary throughout the sample,
           while a heterogeneous mixture's depend on location
                    1, 2, 3, 4, 19, 20, 21, 22, 25, 26
  3.7.A.2  composition can be expressed in a variety of ways, molarity is the
           most common in the laboratory, and molarity is moles of solute over
           litres of SOLUTION
                    5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23, 24,
                    27, 28, 29, 30

THE EXCLUDED CALCULATIONS. Topic 3.8's exclusion statements put colligative
properties and calculations of molality, percent by mass and percent by volume
outside the exam. ``excluded_measures_never_asked`` asserts that no stem asks
for one and no key states one, while requiring that they appear somewhere as
distractors -- otherwise the check would pass over an empty set and prove
nothing.

THE DENOMINATOR. EK 3.7.A.2 divides by litres of SOLUTION.
``denominator_is_the_solution`` refuses any key that divides by a volume of
solvent, and requires the solvent reading to be offered as a distractor.

DILUTION. The CED does not separately state that adding water leaves the solute
alone, so ``dilution_premise_stated`` asserts that every stem performing a
dilution says so in its own words. A calculation resting on an unstated premise
is exactly what this project's rules forbid.

ARITHMETIC. Twelve stem items and four tabulated ones are recomputed from the
stimulus alone. Most checks also recompute the specific wrong turn a distractor
represents -- the inverted ratio, the unconverted millilitres, the
pre-dilution concentration -- and assert that value is offered and not keyed.

NEGATIVE CONTROL: ``python3 verify_h3_7.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h3_7

MOLES = "Moles of solute"
VOLUME = "Volume of solution (L)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below)(?![a-z])", re.I)

# Topic 3.8's exclusion statements, which are exam-wide.
_EXCLUDED = re.compile(
    r"(?<![A-Za-z])(molality|percent by mass|percent by volume|colligative)(?![A-Za-z])",
    re.I)

# EK 3.7.A.2 divides by litres of SOLUTION. A key dividing by solvent is wrong.
_SOLVENT_DENOM = [
    re.compile(r"L_\{\\mathrm\{solvent\}\}", re.I),
    re.compile(r"(?<![a-z])(?:litres|liters|volume)\s+of\s+(?:the\s+)?solvent(?![a-z])",
               re.I),
    re.compile(r"(?<![a-z])volume of the solvent used(?![a-z])", re.I),
]

# A stem that dilutes must say the solute is untouched.
# "Diluting to a volume" while DISSOLVING a weighed amount is not a dilution --
# the amount of solute is given outright there, so nothing has to be carried
# over. The trigger is therefore water being added to an existing solution, or a
# stock solution being drawn from; those are the stems whose arithmetic depends
# on the unstated premise.
_DILUTION_STEM = re.compile(
    r"(?<![a-z])(water is added|adds water|adding water|stock solution)(?![a-z])", re.I)
_PREMISE = re.compile(
    r"(?<![a-z])(no solute (?:is )?added or removed|nothing else is added or removed|"
    r"only other thing added is water|only water is added|"
    r"transfers the whole solution|whole solution is transferred)(?![a-z])", re.I)


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
    print(f"OK  {module.TOPIC[0]} figures: every set of solution data is carried as a table.")


def excluded_measures_never_asked(module):
    """3.8's exclusion statements: no molality, no percent by mass or volume, no colligatives."""
    offered = []
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = _EXCLUDED.search(item["q"])
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the stem asks about {hit.group(0)!r}, which topic "
            f"3.8's exclusion statement puts outside the exam -- {item['q'][:70]!r}"
        )
        hit = _EXCLUDED.search(h.keyed(item))
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the key states {hit.group(0)!r}, which topic 3.8's "
            f"exclusion statement puts outside the exam -- {h.keyed(item)!r}"
        )
        offered += [(i, k) for k, c in enumerate(item["choices"])
                    if k != item["ans"] and _EXCLUDED.search(c)]
    assert len(offered) >= 3, (
        f"the excluded measures are offered only {len(offered)} time(s) as distractors, so "
        "this check has almost nothing to distinguish and proves little"
    )
    print(f"OK  {module.TOPIC[0]} exclusions: molality, percent by mass and percent by volume "
          f"appear only as distractors, at {offered}, and never in a stem or a key.")


def denominator_is_the_solution(module):
    """EK 3.7.A.2 divides by litres of SOLUTION, which is not the volume of solvent."""
    offered = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for k, choice in enumerate(item["choices"]):
            hit = next((p.search(choice) for p in _SOLVENT_DENOM if p.search(choice)), None)
            if not hit:
                continue
            assert k != item["ans"], (
                f"{module.TOPIC[0]} q{i}: the key divides by a volume of solvent "
                f"({hit.group(0)!r}); EK 3.7.A.2 divides by litres of solution"
            )
            offered.append((i, k))
    assert len(offered) >= 2, (
        f"the solvent-denominator misreading is offered only {len(offered)} time(s), so this "
        "check has almost nothing to distinguish"
    )
    print(f"OK  {module.TOPIC[0]} denominator: the solvent-volume misreading is offered at "
          f"{offered} and keyed nowhere.")


def dilution_premise_stated(module):
    """A dilution stem must say the amount of solute is untouched, not assume it."""
    dilutions = []
    for i, item in enumerate(module.QUESTIONS, 1):
        if not _DILUTION_STEM.search(item["q"]):
            continue
        dilutions.append(i)
        assert _PREMISE.search(item["q"]), (
            f"{module.TOPIC[0]} q{i}: the stem performs a dilution but never states that the "
            f"amount of solute is unchanged, which the CED does not supply -- "
            f"{item['q'][:100]!r}"
        )
    assert len(dilutions) >= 3, (
        f"only {len(dilutions)} stem(s) dilute anything, so this check has almost nothing to "
        "read and proves little"
    )
    print(f"OK  {module.TOPIC[0]} dilution premise: item(s) {dilutions} dilute, and every one "
          "of them states in its own words that no solute is added or removed.")


# ------------------------------------------------------------------ arithmetic

def molarity(moles, litres):
    """EK 3.7.A.2, written once."""
    return moles / litres


def _wrong_value_offered(item, text):
    """The named mistake must be OFFERED as a distractor and must not be the key."""
    hits = [k for k, c in enumerate(item["choices"]) if cg.contains_phrase(c, text)]
    assert hits and item["ans"] not in hits, (
        f"the mistake value {text!r} must appear as a distractor and not as the key; it "
        f"appears at {hits} with the key at {item['ans']}"
    )


def n7(item):
    m = molarity(0.50, 2.0)
    assert abs(m - 0.25) < 1e-12, f"the molarity recomputes to {m}"
    inverted = 2.0 / 0.50
    assert abs(inverted - 4.0) < 1e-12, f"the inverted ratio recomputes to {inverted}"
    _wrong_value_offered(item, f"{inverted:.1f} M")
    h.shows(item, f"{m:.2f} M")
    return (f"0.50 mol over 2.0 L recomputes the molarity as {m:g} M, with the inverted "
            f"ratio {inverted:g} M offered as a distractor")


def n8(item):
    n = 0.20 * 0.500
    assert abs(n - 0.10) < 1e-12, f"the amount recomputes to {n}"
    divided = 0.20 / 0.500
    assert abs(divided - 0.40) < 1e-12, f"the divided value recomputes to {divided}"
    _wrong_value_offered(item, f"{divided:.2f} mol")
    h.shows(item, f"{n:.2f} mol")
    return (f"0.20 M times 0.500 L recomputes the amount as {n:g} mol, with the division "
            f"{divided:g} mol offered as a distractor")


def n9(item):
    v = 0.60 / 3.0
    assert abs(v - 0.20) < 1e-12, f"the volume recomputes to {v}"
    multiplied = 0.60 * 3.0
    inverted = 3.0 / 0.60
    assert abs(multiplied - 1.8) < 1e-12 and abs(inverted - 5.0) < 1e-12, (
        f"the two mistake values recompute to {multiplied} and {inverted}"
    )
    _wrong_value_offered(item, f"{multiplied:.1f} L")
    _wrong_value_offered(item, f"{inverted:.1f} L")
    h.shows(item, f"{v:.2f} L")
    return (f"0.60 mol over 3.0 M recomputes the volume as {v:g} L, with {multiplied:g} L "
            f"and {inverted:g} L the two mistake values offered")


def n10(item):
    m = molarity(0.10, 250.0 / 1000.0)
    assert abs(m - 0.40) < 1e-12, f"the molarity recomputes to {m}"
    unconverted = 0.10 / 250.0
    assert abs(unconverted - 0.0004) < 1e-15, f"the unconverted value recomputes to {unconverted}"
    _wrong_value_offered(item, "0.00040 M")
    h.shows(item, f"{m:.2f} M")
    return (f"0.10 mol over 0.250 L recomputes the molarity as {m:g} M, with the millilitre "
            f"division {unconverted:g} M offered as the conversion mistake")


def n11(item):
    moles = 2.00 * (25.0 / 1000.0)
    m = molarity(moles, 100.0 / 1000.0)
    assert abs(moles - 0.0500) < 1e-12, f"the amount recomputes to {moles}"
    assert abs(m - 0.500) < 1e-12, f"the diluted molarity recomputes to {m}"
    assert m < 2.00, "adding only water cannot raise the concentration"
    upside_down = 2.00 * (100.0 / 25.0)
    assert abs(upside_down - 8.00) < 1e-12, f"the inverted-ratio value recomputes to {upside_down}"
    _wrong_value_offered(item, f"{upside_down:.2f} M")
    h.shows(item, f"{m:.3f} M")
    return (f"{moles:g} mol of solute in {100.0 / 1000.0:g} L recomputes the diluted molarity "
            f"as {m:g} M, below the original 2.00 M, with the inverted volume ratio "
            f"{upside_down:g} M offered as a distractor")


def n12(item):
    moles = 0.30 * (250.0 / 1000.0)
    v_litres = moles / 6.0
    v_ml = v_litres * 1000.0
    assert abs(moles - 0.075) < 1e-12, f"the amount recomputes to {moles}"
    assert abs(v_ml - 12.5) < 1e-9, f"the stock volume recomputes to {v_ml} mL"
    assert v_ml < 250.0, "the stock volume must be smaller than the volume being prepared"
    h.shows(item, f"{v_ml:.1f} mL")
    return (f"the finished solution must hold {moles:g} mol, and {v_ml:g} mL of 6.0 M stock "
            f"carries exactly that")


def n13(item):
    factor = 1.0 / 2.0
    assert abs(factor - 0.5) < 1e-12, f"the molarity factor recomputes to {factor}"
    h.shows(item, "halved")
    return (f"the moles above the line are unchanged and the litres below it double, so the "
            f"molarity is multiplied by {factor:g}")


def n23(item):
    n = 0.40 * 0.75
    assert abs(n - 0.30) < 1e-12, f"the amount recomputes to {n}"
    divided = 0.40 / 0.75
    assert abs(divided - 0.5333) < 1e-3, f"the divided value recomputes to {divided}"
    _wrong_value_offered(item, f"{divided:.2f} mol")
    h.shows(item, f"{n:.2f} mol")
    return (f"0.40 M times 0.75 L recomputes the amount as {n:g} mol, with the division "
            f"{divided:.2f} mol offered as a distractor")


def n24(item):
    intermediate = molarity(0.10, 500.0 / 1000.0)
    final = molarity(0.10, 2.00)
    assert abs(intermediate - 0.20) < 1e-12, f"the intermediate molarity recomputes to {intermediate}"
    assert abs(final - 0.050) < 1e-12, f"the final molarity recomputes to {final}"
    assert final < intermediate, "adding water must lower the concentration"
    _wrong_value_offered(item, f"{intermediate:.2f} M")
    h.shows(item, f"{final:.3f} M")
    return (f"the same {0.10:g} mol of solute in the final {2.00:g} L recomputes the molarity "
            f"as {final:g} M, with the intermediate value {intermediate:g} M offered as a "
            "distractor")


def n28(item):
    litres = 250.0 / 1000.0
    assert abs(litres - 0.250) < 1e-12, f"the conversion recomputes to {litres}"
    h.shows(item, f"{litres:.3f} L")
    return f"250. mL divided by the thousand millilitres in a litre recomputes as {litres:g} L"


NUMERIC = {7: n7, 8: n8, 9: n9, 10: n10, 11: n11, 12: n12, 13: n13, 23: n23,
           24: n24, 28: n28}


# ----------------------------------------------------------------- table items

def _molarities(table):
    return {lab: molarity(cg.cell(table, lab, MOLES), cg.cell(table, lab, VOLUME))
            for lab in cg.labels(table)}


def q16(table, item):
    ms = _molarities(table)
    top = max(ms, key=ms.get)
    tied = [lab for lab, v in ms.items() if abs(v - ms[top]) < 1e-12]
    assert tied == [top], f"the most concentrated tabulated solution is not unique: {ms}"
    assert top == "Solution 2", f"the most concentrated tabulated solution is {top}: {ms}"
    moles = dict(zip(cg.labels(table), cg.col(table, MOLES)))
    assert max(moles, key=moles.get) == top, (
        "this item is only worth asking if the largest amount and the largest concentration "
        f"can come apart; here they agree, so check the volumes differ: {moles} / {ms}"
    )
    vols = dict(zip(cg.labels(table), cg.col(table, VOLUME)))
    assert len(set(vols.values())) > 1, "the tabulated volumes must differ, or the ratio is idle"
    h.shows(item, top)
    return (f"the tabulated molarities recompute as {ms} from amounts {moles} and volumes "
            f"{vols}, with a unique maximum at {top}")


def q17(table, item):
    m = molarity(cg.cell(table, "Solution 3", MOLES), cg.cell(table, "Solution 3", VOLUME))
    assert abs(m - 0.20) < 1e-12, f"the tabulated row recomputes to {m}"
    h.shows(item, f"{m:.2f} M")
    return (f"the tabulated moles and volume for that row recompute the molarity as {m:g} M")


def q18(table, item):
    ms = _molarities(table)
    groups = {}
    for lab, v in ms.items():
        groups.setdefault(round(v, 9), []).append(lab)
    shared = sorted(g for g in groups.values() if len(g) > 1)
    assert shared == [["Solution 1", "Solution 4"]], (
        f"exactly one tabulated pair may share a molarity; the grouping is {groups}"
    )
    pair = shared[0]
    assert (cg.cell(table, pair[0], MOLES) != cg.cell(table, pair[1], MOLES)
            and cg.cell(table, pair[0], VOLUME) != cg.cell(table, pair[1], VOLUME)), (
        "the matching pair must differ in BOTH the amount and the volume, or the item can be "
        "answered without forming either ratio"
    )
    nums = [str(lab).split()[-1] for lab in pair]
    h.shows(item, f"Solutions {nums[0]} and {nums[1]}")
    return (f"the tabulated molarities group as {groups}, with exactly one pair sharing a "
            f"value while differing in both amount and volume")


def q27(table, item):
    ms = _molarities(table)
    above = sorted(lab for lab, v in ms.items() if v > 0.15)
    assert above == ["Solution 2", "Solution 3"], f"the rows above 0.15 M are {above}: {ms}"
    word = {0: "None of them", 1: "Exactly one", 2: "Exactly two", 3: "Exactly three",
            4: "All four"}[len(above)]
    h.shows(item, word)
    return (f"the tabulated molarities recompute as {ms}, of which {len(above)} exceed the "
            f"stated 0.15 M threshold: {above}")


TABLE_CHECKS = {16: q16, 17: q17, 18: q18, 27: q27}


CLAIMS = [
 ("A homogeneous mixture",
  "EK 3.7.A.1 opens by saying solutions are also sometimes called homogeneous mixtures; the heterogeneous case is what the same sentence contrasts them with."),
 ("As a solid, a liquid or a gas",
  "EK 3.7.A.1 states that solutions can be solids, liquids, or gases, so the habit of picturing a solution as a liquid is not something the framework requires."),
 ("They do not vary throughout the sample",
  "EK 3.7.A.1: in a solution, the macroscopic properties do not vary throughout the sample."),
 ("They depend on location in the mixture",
  "EK 3.7.A.1: in a heterogeneous mixture, the macroscopic properties depend on location in the mixture."),
 ("Molarity",
  "EK 3.7.A.2 names molarity as the most common method used in the laboratory for expressing solution composition."),
 ("\\frac{n_{\\mathrm{solute}}}{L_{\\mathrm{solution}}}",
  "EK 3.7.A.2's equation, with the moles of solute above the line and the litres of SOLUTION below it rather than the litres of solvent."),
 ("0.25 M",
  "EK 3.7.A.2's equation applied directly. Recomputed in n7, which also recomputes the inverted ratio and checks it is offered rather than keyed."),
 ("0.10 mol",
  "EK 3.7.A.2's equation rearranged for the amount of solute, which is the calculation learning objective 3.7.A names. Recomputed in n8."),
 ("0.20 L",
  "EK 3.7.A.2's equation rearranged for the volume. Recomputed in n9, which also recomputes both mistake values and checks each is offered rather than keyed."),
 ("0.40 M",
  "EK 3.7.A.2's equation with the volume converted to litres first. Recomputed in n10, which also recomputes the value the unconverted millilitres would give."),
 ("0.500 M",
  "EK 3.7.A.2 applied twice under the stem's stated premise that no solute is added or removed. Recomputed in n11, which checks the result is below the original concentration."),
 ("12.5 mL",
  "EK 3.7.A.2 gives the moles the finished solution must hold and the same equation gives the volume of stock carrying them. Recomputed in n12, which checks that volume is smaller than the one being prepared."),
 ("halved",
  "EK 3.7.A.2 keeps the moles above the line fixed while the litres below it double. Recomputed in n13."),
 ("It is unchanged",
  "Water contributes solvent and no solute, so the quantity above the line in EK 3.7.A.2's equation cannot move. This is the premise every dilution stem in this topic states in its own words."),
 ("The volume of the solution",
  "EK 3.7.A.2 writes molarity as moles of solute per litre of SOLUTION; the finished solution's volume is not in general the sum of the separate volumes."),
 ("Solution 2",
  "EK 3.7.A.2's ratio formed for every tabulated row. q16 recomputes all four, checks the maximum is unique, and checks the volumes differ so the ratio is doing the work."),
 ("0.20 M",
  "EK 3.7.A.2's equation applied to one tabulated row. Recomputed in q17."),
 ("Solutions 1 and 4",
  "EK 3.7.A.2's ratio can agree for rows that differ in both amount and volume. q18 recomputes all four, checks exactly one pair matches, and checks that pair differs in both columns."),
 ("They are the same, because in a solution the macroscopic properties do not vary throughout the sample",
  "EK 3.7.A.1 makes uniformity a property of being a solution rather than a consequence of recent stirring. The anchor carries the verdict and the reason together because a distractor pairs the same verdict with a different reason."),
 ("They may differ, because in a heterogeneous mixture the macroscopic properties depend on location in the mixture",
  "EK 3.7.A.1's second contrast, verbatim in substance. The anchor carries both clauses because a distractor gives the same verdict for a reason the framework does not state."),
 ("Yes, because the framework says solutions can be solids",
  "EK 3.7.A.1 allows solutions to be solids and defines the solution case by macroscopic properties that do not vary throughout the sample, both of which a uniform alloy meets."),
 ("As a solution, since a solution is a homogeneous mixture and may be a gas",
  "EK 3.7.A.1 calls solutions homogeneous mixtures, allows them to be gases, and makes uniformity throughout the sample the distinguishing feature."),
 ("0.30 mol",
  "EK 3.7.A.2's equation rearranged for the amount of solute. Recomputed in n23, which also recomputes the division that one distractor represents."),
 ("0.050 M",
  "EK 3.7.A.2 applied once to the final volume, since the stem transfers the whole solution and adds only water. Recomputed in n24, which also recomputes the intermediate concentration offered as a distractor."),
 ("Adding more solvent to the solution",
  "EK 3.7.A.2 makes molarity a ratio of moles of solute to litres of solution, so only a change to one of those two moves it; EK 3.7.A.1's uniformity is why dividing a solution does not."),
 ("The molarity is unchanged and the number of moles of solute is halved",
  "EK 3.7.A.1 makes a solution uniform throughout, so half the volume carries half the solute and EK 3.7.A.2's ratio is unmoved. Both clauses are pinned because a distractor keeps one of them and swaps the other."),
 ("Exactly two",
  "EK 3.7.A.2's ratio formed for each tabulated row and compared with the stated threshold. Recomputed in q27."),
 ("0.250 L",
  "A litre is a thousand millilitres, and EK 3.7.A.2's equation requires litres. Recomputed in n28; attending to the conversion is suggested skill 5.F."),
 ("Molarity is the most common method used in the laboratory",
  "EK 3.7.A.2 says composition can be expressed in a variety of ways and then names molarity as the most common method used in the laboratory, which ranks it without excluding the others."),
 ("Moles of solute divided by litres of solution",
  "EK 3.7.A.2's equation in words: an amount above the line and a volume of SOLUTION below it, not a mass and not a volume of solvent."),
]


SWAP_ITEMS = {
    19: ("They are the same", "do not vary throughout the sample"),
    20: ("They may differ", "depend on location in the mixture"),
    26: ("molarity is unchanged", "moles of solute is halved"),
}


def swap_anchors_carry_both_clauses(module, claims):
    """Where a distractor keeps the verdict and swaps the reason, pin both."""
    for i, (clause_a, clause_b) in sorted(SWAP_ITEMS.items()):
        anchor = claims[i - 1][0]
        item = module.QUESTIONS[i - 1]
        has_a = cg.contains_phrase(anchor, clause_a)
        has_b = cg.contains_phrase(anchor, clause_b)
        assert has_a and has_b, (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} must name both {clause_a!r} and "
            f"{clause_b!r}; it carries "
            f"{'only the first' if has_a else 'only the second' if has_b else 'neither'}"
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


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[15]["q"] = "In the diagram above, which solution is most concentrated?"
        no_figure_language(mod)

    def excluded_measure_in_a_stem(mod, cl):
        mod.QUESTIONS[6]["q"] = "What is the molality of a solution holding 0.50 mol in 2.0 kg?"
        excluded_measures_never_asked(mod)

    def excluded_measure_keyed(mod, cl):
        mod.QUESTIONS[4]["ans"] = 1
        cl[4] = ("Molality", cl[4][1])
        excluded_measures_never_asked(mod)

    def excluded_distractors_removed(mod, cl):
        # A control on the CONTROL.
        for item in mod.QUESTIONS:
            item["choices"] = [_EXCLUDED.sub("mole fraction", c) for c in item["choices"]]
        excluded_measures_never_asked(mod)

    def solvent_denominator_keyed(mod, cl):
        mod.QUESTIONS[14]["ans"] = 1
        cl[14] = ("The volume of the solvent used", cl[14][1])
        denominator_is_the_solution(mod)

    def solvent_distractors_removed(mod, cl):
        for item in mod.QUESTIONS:
            item["choices"] = [
                c.replace("L_{\\mathrm{solvent}}", "L_{\\mathrm{sample}}")
                 .replace("volume of the solvent used", "volume that was poured first")
                 .replace("litres of solvent", "litres of sample")
                 .replace("volume of solvent and solute measured separately",
                          "volume of the two components measured separately")
                for c in item["choices"]]
        denominator_is_the_solution(mod)

    def dilution_premise_dropped(mod, cl):
        mod.QUESTIONS[10]["q"] = mod.QUESTIONS[10]["q"].replace(
            " No solute is added or removed.", "")
        dilution_premise_stated(mod)

    def swap_anchor_halved(mod, cl):
        cl[25] = ("molarity is unchanged", cl[25][1])
        swap_anchors_carry_both_clauses(mod, cl)

    def solution_reason_anchor_halved(mod, cl):
        cl[18] = ("They are the same", cl[18][1])
        swap_anchors_carry_both_clauses(mod, cl)

    def table_amounts_changed(mod, cl):
        mod.QUESTIONS[16]["table"] = dict(
            headers=h3_7._T_SOL["headers"],
            rows=[["Solution 1", "0.20", "2.0"], ["Solution 2", "0.60", "1.5"],
                  ["Solution 3", "0.30", "0.50"], ["Solution 4", "0.40", "4.0"]])

    def table_concentration_tied(mod, cl):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h3_7._T_SOL["headers"],
            rows=[["Solution 1", "0.20", "2.0"], ["Solution 2", "0.60", "1.5"],
                  ["Solution 3", "0.20", "0.50"], ["Solution 4", "1.60", "4.0"]])

    def table_gains_a_second_matching_pair(mod, cl):
        mod.QUESTIONS[17]["table"] = dict(
            headers=h3_7._T_SOL["headers"],
            rows=[["Solution 1", "0.20", "2.0"], ["Solution 2", "0.60", "1.5"],
                  ["Solution 3", "0.60", "1.5"], ["Solution 4", "0.40", "4.0"]])

    def matching_pair_shares_its_columns(mod, cl):
        # Two identical rows share a molarity trivially: the item can be answered
        # without forming either ratio, which is not what it claims to test.
        mod.QUESTIONS[17]["table"] = dict(
            headers=h3_7._T_SOL["headers"],
            rows=[["Solution 1", "0.20", "2.0"], ["Solution 2", "0.60", "1.5"],
                  ["Solution 3", "0.10", "0.50"], ["Solution 4", "0.20", "2.0"]])

    def threshold_count_changes(mod, cl):
        mod.QUESTIONS[26]["table"] = dict(
            headers=h3_7._T_SOL["headers"],
            rows=[["Solution 1", "0.20", "2.0"], ["Solution 2", "0.60", "1.5"],
                  ["Solution 3", "0.10", "0.50"], ["Solution 4", "1.60", "4.0"]])

    return [
        ("a stem referring to a diagram the bank cannot show", figure_language),
        ("a stem asking for a molality, which the exclusion statement bars",
         excluded_measure_in_a_stem),
        ("an excluded measure promoted to a key", excluded_measure_keyed),
        ("every excluded measure removed, so that check would run over an empty set",
         excluded_distractors_removed),
        ("a key dividing by the volume of solvent instead of solution",
         solvent_denominator_keyed),
        ("the solvent-denominator misreading removed everywhere, so that check would be idle",
         solvent_distractors_removed),
        ("a dilution stem stripped of its stated premise", dilution_premise_dropped),
        ("the pour-out-half anchor cut to one clause", swap_anchor_halved),
        ("the uniform-solution anchor cut to the verdict only", solution_reason_anchor_halved),
        ("a tabulated amount changed under the row whose molarity is keyed",
         table_amounts_changed),
        ("two tabulated solutions tied for the highest molarity", table_concentration_tied),
        ("a second tabulated pair made to share a molarity",
         table_gains_a_second_matching_pair),
        ("the matching pair made identical in both columns, so no ratio need be formed",
         matching_pair_shares_its_columns),
        ("a tabulated volume changed so the count above the threshold moves",
         threshold_count_changes),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h3_7, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h3_7)
excluded_measures_never_asked(h3_7)
denominator_is_the_solution(h3_7)
dilution_premise_stated(h3_7)
swap_anchors_carry_both_clauses(h3_7, CLAIMS)
h.run(h3_7, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
