"""Key audit for AP BIOLOGY 2.6 Facilitated Diffusion.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
The topic has three statements and they carry everything.

EK 2.6.A.1 (facilitated diffusion requires transport or channel proteins to
enable the movement of charged ions) carries items 1, 10, 13 and 24; sub-point i
(membranes may become polarized by the movement of ions) items 3 and 23;
sub-point ii (charged ions, including sodium and potassium, require channel
proteins) items 2, 7, 10 and 21.

EK 2.6.A.2 (facilitated diffusion enables the movement of large polar molecules
with no energy input, and substances move down the concentration gradient)
carries items 4, 5, 12, 18, 19, 20, 21 and 24.

EK 2.6.A.3 (aquaporins transport large quantities of water across membranes)
carries items 6, 11, 15, 16, 26 and 27.

THE CHAIN TO TOPIC 2.5, made explicit because items 8, 9, 25 and 30 depend on
it: EK 2.6.A.2's two clauses -- no energy input, and movement down the
concentration gradient -- are exactly the two clauses EK 2.5.A.2 uses to define
passive transport, and EK 2.5.A.3 defines active transport by the direct input
of energy. So calling facilitated diffusion passive is a chaining of stated
sentences, not a new assertion. Needing a PROTEIN is not what the framework uses
to sort passive from active, and three items are built on exactly that
confusion.

Items 14, 17 and 22 chain to EK 2.4.A.2 (small nonpolar molecules freely pass)
and item 17 and 26 to EK 2.4.A.3 (small polar uncharged molecules pass in small
amounts), which is what lets a cell line with no aquaporins still show some
water movement.

Items 28 and 29 rest on method: what a requirement claim needs, and what
separates a protein-dependent route from free passage. Item 28 is the CED's own
suggested skill area for the neighbouring topic and is used here only as design
reasoning.

DATA ITEMS: 13 to 20 carry tables. Every keyed conclusion is recomputed below
from the table alone.

NEGATIVE CONTROL: ``python3 verify_b2_6.py --selftest`` corrupts a key, an
anchor, three table cells and the notation on purpose and confirms each fails.
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


KRATE = "Rate of potassium ion movement across the membrane (arbitrary units)"
ORATE = "Rate of oxygen movement across the membrane (arbitrary units)"
NAQP = "Aquaporins per cell (thousands)"
WATER = "Water crossing the membrane per minute (arbitrary units)"
GRATE = "Rate of glucose entry by facilitated diffusion (arbitrary units)"
OUT = "Glucose concentration outside the cell (millimolar)"
IN = "Glucose concentration inside the cell (millimolar)"
TIME = "Time (minutes)"


def q13(table, item):
    with_p, without = "Channel proteins present", "Channel proteins absent"
    k = {lab: cg.cell(table, lab, KRATE) for lab in cg.labels(table)}
    o = {lab: cg.cell(table, lab, ORATE) for lab in cg.labels(table)}
    assert k[without] < k[with_p] / 20, f"potassium movement must collapse without channels: {k}"
    assert abs(o[without] - o[with_p]) / o[with_p] < 0.05, f"oxygen movement must be near unchanged: {o}"
    return (f"potassium falls from {k[with_p]:.0f} to {k[without]:.0f} while oxygen goes "
            f"from {o[with_p]:.0f} to {o[without]:.0f}")


def q14(table, item):
    with_p, without = "Channel proteins present", "Channel proteins absent"
    o = {lab: cg.cell(table, lab, ORATE) for lab in cg.labels(table)}
    k = {lab: cg.cell(table, lab, KRATE) for lab in cg.labels(table)}
    assert abs(o[without] - o[with_p]) / o[with_p] < 0.05, f"oxygen must be the unaffected one: {o}"
    assert not abs(k[without] - k[with_p]) / k[with_p] < 0.05, \
        f"potassium must NOT also be unaffected, or the item has two answers: {k}"
    return f"oxygen changes by under five percent while potassium changes by far more"


def _aqua(table):
    return {lab: (cg.cell(table, lab, NAQP), cg.cell(table, lab, WATER))
            for lab in cg.labels(table)}


def q15(table, item):
    pairs = sorted(_aqua(table).values())
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"water movement must rise with aquaporin count: {pairs}"
    assert pairs[0][1] == min(w for _, w in pairs), "the zero-aquaporin row must not be the highest"
    return f"sorted by aquaporin count the water rates are {[w for _, w in pairs]}, strictly rising"


def q16(table, item):
    pairs = [(n, w) for n, w in _aqua(table).values() if n > 0]
    ratios = [w / n for n, w in pairs]
    assert max(ratios) - min(ratios) < 0.5, f"water per aquaporin is not near constant: {ratios}"
    # the doubling and halving distractors must both be false on the same numbers
    ordered = [w / n for n, w in sorted(pairs)]
    assert not all(ordered[i] * 1.8 < ordered[i + 1] for i in range(len(ordered) - 1)), \
        "'roughly doubles at each step' must be false"
    assert not all(ordered[i] > 1.8 * ordered[i + 1] for i in range(len(ordered) - 1)), \
        "'roughly halves at each step' must be false"
    return f"water per thousand aquaporins is {[round(r, 2) for r in ordered]}, all close together"


def q17(table, item):
    a = _aqua(table)
    zero = [lab for lab, (n, w) in a.items() if n == 0]
    assert len(zero) == 1, f"exactly one row should have no aquaporins: {zero}"
    w0 = a[zero[0]][1]
    assert w0 > 0, "the aquaporin-free row must still show some water movement"
    others = [w for lab, (n, w) in a.items() if n > 0]
    assert all(w0 < o / 10 for o in others), f"that movement must be small next to every other row: {w0} vs {others}"
    return f"{zero[0]} has no aquaporins yet moves {w0:.0f}, under a tenth of every other row {others}"


def q18(table, item):
    vals = {lab: cg.cell(table, lab, GRATE) for lab in cg.labels(table)}
    up, treated = "Untreated cells", "Cells with ATP synthesis blocked"
    assert abs(vals[up] - vals[treated]) / vals[up] < 0.05, f"the two rates must be close: {vals}"
    assert vals[treated] > 0, "'stopped entirely' must be false"
    assert vals[treated] < 2 * vals[up], "'more than doubled' must be false"
    return f"{vals[up]:.0f} against {vals[treated]:.0f} is a difference under five percent"


def q19(table, item):
    out = cg.col(table, OUT)
    inn = cg.col(table, IN)
    assert all(out[i] > out[i + 1] for i in range(len(out) - 1)), f"outside must fall: {out}"
    assert all(inn[i] < inn[i + 1] for i in range(len(inn) - 1)), f"inside must rise: {inn}"
    assert out[0] > inn[0], "the gradient must start with more outside than inside"
    return f"outside {out} falls while inside {inn} rises, so net movement runs down the gradient"


def q20(table, item):
    out = cg.col(table, OUT)
    inn = cg.col(table, IN)
    assert out[-1] == inn[-1], f"the last row must be equal on both sides: {out[-1]} and {inn[-1]}"
    assert inn[-1] <= out[-1], "'inside above outside' must be false"
    assert out[-1] > 0, "'outside fell to zero' must be false"
    assert out[0] != inn[0], "'still far apart' must be false only because they started apart"
    return f"the last row records {out[-1]:.0f} on both sides, having started at {out[0]:.0f} and {inn[0]:.0f}"


CLAIMS = [
 ("Transport or channel proteins",
  "EK 2.6.A.1 states that facilitated diffusion requires transport or channel proteins to enable the movement of charged ions across the membrane. EK 2.6.A.2 says in the same statement group that the process happens with no energy input, so the energy option contradicts it."),
 ("Sodium and potassium",
  "EK 2.6.A.1 ii states that charged ions, including sodium and potassium, require channel proteins to move through the membrane. Oxygen, nitrogen and carbon dioxide are EK 2.4.A.2's freely passing small nonpolar molecules and water and ammonia are EK 2.4.A.3's small polar uncharged case."),
 ("The membrane may become polarized",
  "EK 2.6.A.1 i states that membranes may become polarized by the movement of ions across the membrane. Vesicle formation is EK 2.5.B.1 i's endocytosis and nothing in this topic makes a membrane freely permeable."),
 ("with no energy input",
  "EK 2.6.A.2 states that facilitated diffusion enables the movement of large polar molecules through membranes with no energy input. A direct energy input is what EK 2.5.A.3 assigns to active transport instead."),
 ("Down the concentration gradient",
  "EK 2.6.A.2 states that in this type of diffusion substances move down the concentration gradient. Movement up a gradient is EK 2.5.A.3's energy-requiring case."),
 ("transport large quantities of water",
  "EK 2.6.A.3 states that aquaporins transport large quantities of water across membranes. Sodium and potassium are the ions EK 2.6.A.1 ii routes through channel proteins, and the membrane's framework is phospholipid under EK 2.3.B.1."),
 ("nonpolar hydrocarbon tails in the membrane interior prevent",
  "EK 2.4.A.3 states that the nonpolar hydrocarbon tails of phospholipids prevent the movement of ions and polar molecules across the membrane, which is why EK 2.6.A.1 ii routes charged ions through channel proteins. The phosphate regions face the aqueous environments rather than the interior."),
 ("Passive, because it occurs with no energy input",
  "Chaining EK 2.6.A.2 to EK 2.5.A.2: facilitated diffusion has both clauses of the passive definition, no energy input and movement down the concentration gradient. EK 2.5.A.3 makes a direct input of energy, not the use of a protein, what defines the active case."),
 ("Facilitated diffusion needs no energy input and follows the gradient",
  "EK 2.6.A.2 gives facilitated diffusion no energy input and movement down the gradient; EK 2.5.A.3 gives active transport a direct energy input and in some cases movement from low concentration to high. Both use membrane proteins, so protein use cannot separate them."),
 ("movement of charged ions such as sodium and potassium across the membrane will fall sharply",
  "EK 2.6.A.1 ii states that charged ions, including sodium and potassium, require channel proteins to move through the membrane, so blocking those proteins removes the route. EK 2.4.A.2 lets small nonpolar molecules pass freely without it."),
 ("no longer move large quantities of water",
  "EK 2.6.A.3 assigns the transport of large quantities of water to aquaporins, so blocking them removes the high-volume route. EK 2.4.A.3 still lets water pass in small amounts, which is why the prediction concerns quantity rather than total exclusion."),
 ("It will continue, because it occurs with no energy input",
  "EK 2.6.A.2 states that facilitated diffusion enables movement through membranes with no energy input, so losing usable energy does not remove the driver. Movement up a gradient is EK 2.5.A.3's energy-requiring case."),
 ("Potassium ion movement depends on the channel proteins while oxygen movement does not",
  "Recomputed in q13 above: potassium movement collapses to under a twentieth without channel proteins while oxygen changes by under five percent. EK 2.6.A.1 ii requires channel proteins for charged ions and EK 2.4.A.2 lets small nonpolar molecules pass freely."),
 ("Oxygen, because small nonpolar molecules",
  "Recomputed in q14 above: oxygen is the one substance whose rate barely changes, and the check confirms potassium is not also unaffected, so the item has a single answer. EK 2.4.A.2 states that small nonpolar molecules including oxygen freely pass across the membrane."),
 ("increased as the number of aquaporins increased",
  "Recomputed in q15 above: water movement rises at every step as the aquaporin count rises. EK 2.6.A.3 states that aquaporins transport large quantities of water across membranes."),
 ("stays roughly constant, so the total rises in proportion",
  "Recomputed in q16 above: dividing water movement by aquaporin count gives nearly the same value for every line that has aquaporins, and the doubling and halving readings are both checked false on the same numbers."),
 ("small polar uncharged molecule and passes through the membrane in small amounts",
  "Recomputed in q17 above: the aquaporin-free line still moves water, but under a tenth of every other line. EK 2.4.A.3 lets water pass in small amounts and EK 2.6.A.3 makes aquaporins the route for LARGE quantities, not the only route of any kind."),
 ("proceeds without a direct energy input",
  "Recomputed in q18 above: the two rates differ by under five percent, and neither the stopped-entirely nor the more-than-doubled reading survives the same numbers. EK 2.6.A.2 states that facilitated diffusion happens with no energy input."),
 ("from the side where it was more concentrated toward the side where it was less",
  "Recomputed in q19 above: the outside concentration falls while the inside rises from a start with more outside than inside. EK 2.6.A.2 states that in this type of diffusion substances move down the concentration gradient."),
 ("two concentrations have become equal",
  "Recomputed in q20 above: the final row records the same value on both sides, having started far apart, and the outside value is not zero. EK 2.6.A.2 makes movement follow the gradient, so an abolished gradient leaves nothing to drive net movement; passing beyond equality would need EK 2.5.A.3's energy input."),
 ("Charged ions and large polar molecules",
  "EK 2.6.A.1 assigns charged ions to transport or channel proteins and EK 2.6.A.2 assigns large polar molecules to the same process. Small nonpolar molecules cross freely under EK 2.4.A.2 and need no facilitation."),
 ("Carbon dioxide",
  "EK 2.4.A.2 states that small nonpolar molecules including carbon dioxide freely pass across the membrane, so no protein is needed. EK 2.6.A.1 ii and EK 2.6.A.2 place ions and large polar molecules in the facilitated category."),
 ("The movement of ions across the membrane",
  "EK 2.6.A.1 i states that membranes may become polarized by the movement of ions across the membrane, and the framework attaches polarization to no other movement in this topic. Water and small nonpolar molecules carry no charge."),
 ("does not make the process require energy",
  "EK 2.6.A.1 requires transport or channel proteins and EK 2.6.A.2 states in the same group that the process happens with no energy input and down the concentration gradient, so needing a protein and needing energy are separate matters in the framework."),
 ("direct input of energy, and facilitated diffusion occurs with no energy input",
  "EK 2.5.A.3 defines active transport by the direct input of energy and EK 2.6.A.2 states that facilitated diffusion occurs with no energy input and down the concentration gradient. Membrane proteins are used in both, so their presence cannot distinguish them."),
 ("aquaporins are what allow large quantities to cross",
  "EK 2.4.A.3 lets water, as a small polar uncharged molecule, pass through the membrane in small amounts, and EK 2.6.A.3 states that aquaporins transport large quantities of water across membranes. The two statements describe the same substance at two scales."),
 ("Many aquaporins, because the framework assigns the transport of large quantities",
  "EK 2.6.A.3 states that aquaporins transport large quantities of water across membranes. EK 2.6.A.1 ii assigns sodium channels to ions rather than water, and EK 2.4.A.3 makes the hydrophobic interior what restricts polar molecules rather than what speeds them."),
 ("otherwise identical cells lacking it",
  "A requirement claim needs the protein to be the only difference between otherwise identical preparations. Comparing across species or across solutes varies more than one thing at once, and a time course with the protein always present offers no contrast."),
 ("falls sharply when its membrane proteins are blocked",
  "EK 2.6.A.1 makes the protein requirement the distinctive feature of facilitated diffusion, while EK 2.6.A.2 shares no-energy and down-the-gradient movement with the free passage EK 2.4.A.2 grants small nonpolar molecules. Sensitivity to losing energy would point to EK 2.5.A.3's active case instead."),
 ("includes the aquaporin route for water",
  "The four parts come from three statements: EK 2.6.A.1 for the protein requirement, EK 2.6.A.2 for no energy input and movement down the concentration gradient, and EK 2.6.A.3 for aquaporins transporting large quantities of water."),
]

TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b2_6_mutant")
        mod.TOPIC = b2_6.TOPIC
        mod.QUESTIONS = copy.deepcopy(b2_6.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def oxygen_also_blocked(mod, claims):
        mod.QUESTIONS[13]["table"] = dict(
            headers=b2_6._T_CHANNEL["headers"],
            rows=[["Channel proteins present", "320", "95"],
                  ["Channel proteins absent", "2", "3"]])

    def aquaporins_not_proportional(mod, claims):
        mod.QUESTIONS[15]["table"] = dict(
            headers=b2_6._T_AQUA["headers"],
            rows=[["Line 1", "0", "6"], ["Line 2", "20", "118"],
                  ["Line 3", "40", "240"], ["Line 4", "60", "900"]])

    def zero_row_too_big(mod, claims):
        mod.QUESTIONS[16]["table"] = dict(
            headers=b2_6._T_AQUA["headers"],
            rows=[["Line 1", "0", "100"], ["Line 2", "20", "118"],
                  ["Line 3", "40", "240"], ["Line 4", "60", "352"]])

    def energy_matters_after_all(mod, claims):
        mod.QUESTIONS[17]["table"] = dict(
            headers=b2_6._T_ENERGY["headers"],
            rows=[["Untreated cells", "210"], ["Cells with ATP synthesis blocked", "12"]])

    def gradient_overshoots(mod, claims):
        mod.QUESTIONS[19]["table"] = dict(
            headers=b2_6._T_GRAD["headers"],
            rows=[["0", "20", "2"], ["10", "15", "7"], ["20", "12", "10"], ["30", "8", "14"]])

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[4].__setitem__("ans", 1))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(5, ("no such phrase", c[5][1])))
    must_fail("oxygen made to depend on channel proteins too", oxygen_also_blocked)
    must_fail("water movement made to outrun the aquaporin count", aquaporins_not_proportional)
    must_fail("the aquaporin-free line given as much water movement as the rest", zero_row_too_big)
    must_fail("facilitated diffusion made to collapse without ATP", energy_matters_after_all)
    must_fail("the gradient made to overshoot equality", gradient_overshoots)
    must_fail("a backslash macro in a stem",
              lambda m, c: m.QUESTIONS[5].__setitem__("q", "What do aquaporins do to \\rm H_2O?"))
    print("all negative controls raised as required.")


import b2_6  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b2_6)
cg.check(b2_6, CLAIMS, table_checks=TABLE_CHECKS)
