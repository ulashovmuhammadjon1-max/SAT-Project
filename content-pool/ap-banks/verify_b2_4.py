"""Key audit for AP BIOLOGY 2.4 Membrane Permeability.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
EK 2.4.A.1 (plasma membranes separate the internal from the external
environment; selective permeability results from the membrane having a
hydrophobic interior) carries items 1, 2, 18, 28 and 29.

EK 2.4.A.2 (small nonpolar molecules including nitrogen, oxygen and carbon
dioxide freely pass; hydrophilic substances such as large polar molecules and
ions move through embedded channels and transport proteins) carries items 3, 4,
9, 12, 14, 16, 20, 23 and 30.

EK 2.4.A.3 (the nonpolar hydrocarbon tails prevent the movement of ions and
polar molecules; small polar uncharged molecules like water and ammonia pass in
small amounts) carries items 5, 6, 10, 11, 19, 22, 27 and 30.

EK 2.4.B.1 (cell walls of Bacteria, Archaea, Fungi and plants provide a
structural boundary, a permeability barrier for some substances, and protection
from osmotic lysis) carries items 7, 8, 17, 24 and 25.

Items 15 and 26 rest on method rather than content: what a null hypothesis
asserts, and what a preparation must exclude to test the bilayer alone. Both are
the CED's own suggested skill for this topic, 5.D.

THE THREE-WAY SPLIT IS THE WHOLE TOPIC, and it is where a wrong key would be
easiest to write: FREE passage for small nonpolar molecules (EK 2.4.A.2), SMALL
AMOUNTS for small polar uncharged molecules (EK 2.4.A.3), and PROTEINS for large
polar molecules and ions (EK 2.4.A.2). Every claim below names which of the
three a key comes from.

DATA ITEMS: 9 to 17 carry tables. Each keyed conclusion is recomputed below from
the table alone, and the permeability table's chemical descriptions are checked
against that same three-way split, so a description that does not correspond to
any category the CED names fails rather than ships.

NEGATIVE CONTROL: ``python3 verify_b2_4.py --selftest`` corrupts a key, an
anchor, two table cells and the notation on purpose and confirms each fails.
"""
import re
import sys

import cg_check as cg

_BANNED = [
    (re.compile(r"\\"), "a backslash: Biology is not typeset, so LaTeX would print raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\^"), "a caret exponent: Biology is not typeset, so write it in words"),
    (re.compile(r"\$"), "a dollar sign, which a converter reads as inline math"),
]


def style(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        texts = [item["q"], item["why"]] + list(item["choices"])
        t = item.get("table")
        if t:
            texts += [str(h) for h in t["headers"]] + [str(c) for r in t["rows"] for c in r]
        for text in texts:
            for pat, msg in _BANNED:
                hit = pat.search(text)
                assert not hit, f"{module.TOPIC[0]} q{i}: {msg} -- {hit.group(0)!r} in {text[:70]!r}"
    print(f"OK  {module.TOPIC[0]} notation: no typeset markup in "
          f"{len(module.QUESTIONS)} questions.")


DESC = "Chemical description"
RATE = ("Rate of movement across a protein-free artificial phospholipid bilayer "
        "(arbitrary units)")
SOLUTE = ("Mean amount of a large polar solute entering the cells in ten minutes "
          "(arbitrary units)")
OXY = "Mean amount of oxygen entering the cells in ten minutes (arbitrary units)"
BURST = "Percentage of cells that burst in distilled water within twenty minutes"

# EK 2.4.A.2 and EK 2.4.A.3's own three categories. A description outside these fails.
FREE = "small nonpolar"
SMALL_AMOUNTS = "small polar and uncharged"
NEEDS_PROTEIN = {"large polar", "charged"}
CATEGORIES = {FREE, SMALL_AMOUNTS} | NEEDS_PROTEIN


def _described(table):
    j = table["headers"].index(DESC)
    cells = {r[0]: r[j] for r in table["rows"]}
    unknown = set(cells.values()) - CATEGORIES
    assert not unknown, f"chemical descriptions outside the framework's categories: {unknown}"
    return cells


def q9(table, item):
    desc = _described(table)
    rates = dict(zip(cg.labels(table), cg.col(table, RATE)))
    top = max(rates, key=rates.get)
    assert top == "Oxygen", f"the fastest row is {top}"
    assert desc[top] == FREE, f"{top} is described as {desc[top]!r}, not the free-passage category"
    assert desc["Carbon dioxide"] == FREE, \
        "the misdescription distractor requires carbon dioxide to be small and nonpolar in the table"
    return f"rates are {rates}; the maximum {top} is described as {desc[top]!r}"


def q10(table, item):
    desc = _described(table)
    rates = dict(zip(cg.labels(table), cg.col(table, RATE)))
    bottom = min(rates, key=rates.get)
    assert bottom == "Sodium ion", f"the slowest row is {bottom}"
    assert desc[bottom] == "charged", f"{bottom} is described as {desc[bottom]!r}, not charged"
    return f"the minimum rate belongs to {bottom}, which the table describes as {desc[bottom]!r}"


def q11(table, item):
    desc = _described(table)
    rates = dict(zip(cg.labels(table), cg.col(table, RATE)))
    water = rates["Water"]
    free = [r for lab, r in rates.items() if desc[lab] == FREE]
    slow = [r for lab, r in rates.items() if desc[lab] in NEEDS_PROTEIN]
    assert all(water < f for f in free), f"water {water} must be below every free-passage row {free}"
    assert all(water > s for s in slow), f"water {water} must be above every protein-needing row {slow}"
    assert desc["Water"] == SMALL_AMOUNTS, f"water is described as {desc['Water']!r}"
    return f"water {water} sits below {sorted(free)} and above {sorted(slow)}, an intermediate position"


def q12(table, item):
    desc = _described(table)
    rates = dict(zip(cg.labels(table), cg.col(table, RATE)))
    need = sorted(lab for lab in rates if desc[lab] in NEEDS_PROTEIN)
    assert need == ["Glucose", "Sodium ion"], f"protein-needing rows: {need}"
    two_slowest = sorted(rates, key=rates.get)[:2]
    assert sorted(two_slowest) == need, \
        f"the two lowest rates {two_slowest} must be the two protein-needing rows"
    return f"{need} are both described as hydrophilic categories and hold the two lowest rates"


def q13(table, item):
    rates = dict(zip(cg.labels(table), cg.col(table, RATE)))
    ratio = rates["Oxygen"] / rates["Carbon dioxide"]
    assert 1.75 <= ratio <= 2.5, f"the ratio recomputes to {ratio}, not about two"
    return f"{rates['Oxygen']:.0f} over {rates['Carbon dioxide']:.0f} is {ratio:.2f}, about two"


def q14(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, SOLUTE)))
    ok, blocked = vals["Transport proteins functional"], vals["Transport proteins blocked"]
    assert blocked < ok / 10, f"blocking must cut entry by more than tenfold: {blocked} against {ok}"
    return (f"entry falls from {ok:.0f} to {blocked:.0f} when the proteins are blocked, "
            "far too large a gap for a no-effect hypothesis to survive")


def q15(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, SOLUTE)))
    assert len(vals) == 2, "a null hypothesis of no effect needs exactly two treatments to compare"
    assert vals["Transport proteins functional"] != vals["Transport proteins blocked"], \
        "the two treatments must differ, or there would be nothing for the null to be rejected against"
    return ("the table holds one treated and one untreated mean, which is what a hypothesis "
            "of no effect between them is stated about")


def q16(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, OXY)))
    ok, blocked = vals["Transport proteins functional"], vals["Transport proteins blocked"]
    assert abs(ok - blocked) / ok < 0.05, f"the two oxygen means must be close: {ok} against {blocked}"
    return (f"oxygen entry is {ok:.0f} against {blocked:.0f}, a difference under five percent, "
            "so a no-effect hypothesis survives this test")


def q17(table, item):
    j = table["headers"].index("Treatment of the cell wall")
    treat = {r[0]: r[j] for r in table["rows"]}
    burst = {lab: cg.cell(table, lab, BURST) for lab in cg.labels(table)}
    intact = [lab for lab, t in treat.items() if t == "wall left intact"]
    removed = [lab for lab, t in treat.items() if t == "wall enzymatically removed"]
    assert len(intact) == 1 and len(removed) == 1, f"one of each treatment expected: {treat}"
    assert burst[removed[0]] > 10 * burst[intact[0]], \
        f"removing the wall must raise bursting sharply: {burst}"
    return (f"{burst[intact[0]]:.0f} percent burst with the wall intact against "
            f"{burst[removed[0]]:.0f} percent with it removed")


CLAIMS = [
 ("separates the internal environment of the cell",
  "EK 2.4.A.1 opens by stating that plasma membranes separate the internal environment of the cell from the external environment. The rejected options are functions the framework assigns to ribosomes, nucleic acids and lysosomes in EK 2.1.A.1, EK 1.6.A.1 and EK 2.1.A.6."),
 ("having a hydrophobic interior",
  "EK 2.4.A.1 states that selective permeability is the result of the plasma membrane having a hydrophobic interior. A hydrophilic interior is the opposite claim, and the cell wall is a separate barrier under EK 2.4.B.1."),
 ("Small nonpolar molecules such as nitrogen, oxygen and carbon dioxide",
  "EK 2.4.A.2 states that small nonpolar molecules, including nitrogen, oxygen, and carbon dioxide, freely pass across the membrane. Large polar molecules and ions are in the second half of that same statement as substances routed through proteins."),
 ("Through embedded channels and transport proteins",
  "EK 2.4.A.2 states that hydrophilic substances, such as large polar molecules and ions, move across the membrane through embedded channels and transport proteins. EK 2.4.A.3 explicitly denies the direct route for them."),
 ("nonpolar hydrocarbon tails of the phospholipids",
  "EK 2.4.A.3 states that the nonpolar hydrocarbon tails of phospholipids prevent the movement of ions and polar molecules across the membrane. The embedded transport proteins of EK 2.4.A.2 permit rather than prevent."),
 ("pass through the membrane in small amounts",
  "EK 2.4.A.3 states that small polar, uncharged molecules, like water or ammonia, pass through the membrane in small amounts. That is a third case, between EK 2.4.A.2's free passage and EK 2.4.A.3's prevention."),
 ("Bacteria, Archaea, Fungi and plants",
  "EK 2.4.B.1 names the cell walls of Bacteria, Archaea, Fungi, and plants. Animals are not on that list, so options adding them or extending the list to all organisms overstate it."),
 ("structural boundary, a permeability barrier for some substances, and protection from osmotic lysis",
  "EK 2.4.B.1, near verbatim. The hydrophobic interior belongs to the plasma membrane under EK 2.4.A.1 and the channels to its embedded proteins under EK 2.4.A.2."),
 ("Oxygen, which is small and nonpolar",
  "Recomputed in q9 above: the largest tabulated rate belongs to a row the table itself describes as small and nonpolar, which is the category EK 2.4.A.2 says freely passes. The check also confirms the final option misdescribes a row the table calls small and nonpolar."),
 ("The sodium ion",
  "Recomputed in q10 above: the smallest tabulated rate belongs to the row described as charged. EK 2.4.A.3 states that the nonpolar hydrocarbon tails prevent the movement of ions across the membrane."),
 ("Below the small nonpolar molecules but above the large polar molecule",
  "Recomputed in q11 above: water's rate is below every row described as small and nonpolar and above every row described as large polar or charged. EK 2.4.A.3 gives small polar uncharged molecules passage in small amounts, which is exactly that intermediate position."),
 ("Glucose and the sodium ion",
  "Recomputed in q12 above: the two rows described as large polar and as charged are also the two lowest rates. EK 2.4.A.2 routes hydrophilic substances such as those through embedded channels and transport proteins."),
 ("About twice as fast",
  "Recomputed in q13 above from the two tabulated rates. Both rows are described as small and nonpolar, which is why EK 2.4.A.2 puts them far above the other three even though they differ from each other."),
 ("It should be rejected, because entry fell",
  "Recomputed in q14 above: blocking the proteins cuts entry by more than tenfold, in the direction the mechanism predicts, so the no-effect hypothesis does not survive. EK 2.4.A.2 routes large polar solutes through embedded channels and transport proteins."),
 ("no effect on the amount of solute entering",
  "A null hypothesis is the statement of no effect, which data are then used to reject or fail to reject; asserting an increase or a decrease states the alternative instead. The last rejected option asserts a mechanism EK 2.4.A.3 denies for a polar solute. Suggested skill 5.D is the CED's own framing."),
 ("crossing the membrane without transport proteins",
  "Recomputed in q16 above: the two oxygen means differ by under five percent, so the no-effect hypothesis survives. EK 2.4.A.2 states that small nonpolar molecules including oxygen freely pass across the membrane, so blocking transport proteins should not change oxygen entry."),
 ("protects cells from bursting",
  "Recomputed in q17 above: far more cells burst with the wall removed than with it intact. EK 2.4.B.1 names protection from osmotic lysis among the roles of the cell wall."),
 ("cross it even less readily than before",
  "EK 2.4.A.1 makes the hydrophobic interior the source of selective permeability and EK 2.4.A.3 makes the nonpolar hydrocarbon tails what prevents ions and polar molecules from moving, so strengthening that interior sharpens the exclusion rather than removing it."),
 ("nonpolar hydrocarbon tails, which prevent the movement of ions",
  "EK 2.4.A.3 states that the nonpolar hydrocarbon tails of phospholipids prevent the movement of ions and polar molecules, and EK 2.3.A.1 places those tails facing each other in the interior. The phosphate regions face the aqueous environments instead."),
 ("small nonpolar molecule, and the framework says such molecules freely pass",
  "EK 2.4.A.2 states that small nonpolar molecules, including nitrogen, oxygen, and carbon dioxide, freely pass across the membrane. Small polar uncharged molecules are the separate case EK 2.4.A.3 limits to small amounts."),
 ("selectively permeable",
  "EK 2.4.A.1 names the property selective permeability rather than impermeability, and EK 2.4.A.2 supplies both halves of the selection: free passage for small nonpolar molecules and embedded channels and transport proteins for hydrophilic substances."),
 ("small polar, uncharged molecule that passes through the membrane in small amounts",
  "EK 2.4.A.3 places water and ammonia in a category of their own, passing in small amounts, distinct from EK 2.4.A.2's freely passing small nonpolar molecules and from the ions and polar molecules the hydrocarbon tails prevent."),
 ("Glucose is a large polar molecule and so needs embedded proteins",
  "EK 2.4.A.2 divides the cases by size and polarity rather than by charge: small nonpolar molecules freely pass, while hydrophilic substances such as large polar molecules move through embedded channels and transport proteins."),
 ("The cell wall",
  "EK 2.4.B.1 states that cell walls provide a structural boundary as well as a permeability barrier for some substances to the internal or external cellular environments. The rejected structures are internal components from EK 2.1.A.1 to EK 2.1.A.5."),
 ("more likely to burst, because the wall's protection",
  "EK 2.4.B.1 names protection from osmotic lysis among the roles of the cell walls of Bacteria, Archaea, Fungi, and plants, so removing the wall removes that protection. Nothing in EK 2.4.A.1 to EK 2.4.A.3 makes the membrane's own properties depend on the wall."),
 ("artificial bilayer made only of phospholipids",
  "The claim under test is about the bilayer alone, so the preparation must exclude the embedded channels and transport proteins EK 2.4.A.2 names as the alternative route. A living membrane confounds the two routes and a cell wall is a different barrier under EK 2.4.B.1."),
 ("in small amounts, as a small polar uncharged molecule",
  "EK 2.4.A.3 names ammonia alongside water as a small polar, uncharged molecule that passes through the membrane in small amounts. It is neither in EK 2.4.A.2's free-passage category nor among the ions that statement routes through proteins."),
 ("fatty acid regions of the phospholipids, which face each other",
  "EK 2.4.A.1 attributes selective permeability to the hydrophobic interior and EK 2.4.A.3 calls the excluding structures the nonpolar hydrocarbon tails of phospholipids, which EK 2.3.A.1 places facing each other within the interior of the membrane."),
 ("Selective permeability",
  "EK 2.4.A.1 names selective permeability as the property resulting from the membrane's hydrophobic interior, and the three behaviours described are the three cases EK 2.4.A.2 and EK 2.4.A.3 lay out. Osmotic lysis and structural boundary formation belong to EK 2.4.B.1."),
 ("Small nonpolar molecules pass freely; small polar uncharged molecules pass in small amounts",
  "The three-way sort comes straight from two statements: EK 2.4.A.2 gives free passage to small nonpolar molecules and embedded channels and transport proteins to hydrophilic substances such as large polar molecules and ions, and EK 2.4.A.3 gives small polar uncharged molecules passage in small amounts."),
]

TABLE_CHECKS = {9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b2_4_mutant")
        mod.TOPIC = b2_4.TOPIC
        mod.QUESTIONS = copy.deepcopy(b2_4.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def water_beats_oxygen(mod, claims):
        mod.QUESTIONS[10]["table"] = dict(
            headers=b2_4._T_PERM["headers"],
            rows=[[lab, d, ("20,000" if lab == "Water" else r)]
                  for lab, d, r in b2_4._T_PERM["rows"]])

    def description_typo(mod, claims):
        mod.QUESTIONS[8]["table"] = dict(
            headers=b2_4._T_PERM["headers"],
            rows=[[lab, ("smallish nonpolar" if lab == "Oxygen" else d), r]
                  for lab, d, r in b2_4._T_PERM["rows"]])

    def oxygen_effect_invented(mod, claims):
        mod.QUESTIONS[15]["table"] = dict(
            headers=b2_4._T_NULL_OXYGEN["headers"],
            rows=[["Transport proteins functional", "96"],
                  ["Transport proteins blocked", "11"]])

    def wall_makes_no_difference(mod, claims):
        mod.QUESTIONS[16]["table"] = dict(
            headers=b2_4._T_WALL["headers"],
            rows=[["Preparation 1", "wall left intact", "2"],
                  ["Preparation 2", "wall enzymatically removed", "3"]])

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[5].__setitem__("ans", 1))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(6, ("no such phrase", c[6][1])))
    must_fail("water given a faster rate than the small nonpolar molecules", water_beats_oxygen)
    must_fail("a chemical description outside the framework's categories", description_typo)
    must_fail("blocking transport proteins made to change oxygen entry", oxygen_effect_invented)
    must_fail("removing the cell wall made to change nothing", wall_makes_no_difference)
    must_fail("a backslash macro in a why",
              lambda m, c: m.QUESTIONS[2].__setitem__(
                  "why", "EK 2.4.A.2 names \\ce{O2} among the small nonpolar molecules that pass freely."))
    print("all negative controls raised as required.")


import b2_4  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b2_4)
cg.check(b2_4, CLAIMS, table_checks=TABLE_CHECKS)
