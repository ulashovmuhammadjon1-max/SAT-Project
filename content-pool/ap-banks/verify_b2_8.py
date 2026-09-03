"""Key audit for AP BIOLOGY 2.8 Mechanisms of Transport.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON, AND WHY HALF OF THEM CHAIN
--------------------------------------------------
This topic has ONE essential knowledge statement. EK 2.8.A.1: metabolic energy
(such as that from ATP) is required for active transport of molecules and ions
across the membrane and to establish and maintain electrochemical gradients;
i, membrane proteins are necessary for active transport; ii, the
sodium-potassium pump and ATPase contribute to the maintenance of the membrane
potential.

Items 1, 2, 5, 6, 7, 13, 15, 16, 17, 18, 27 and 29 rest on the lead sentence.
Items 3, 8, 14, 19, 24 and 29 rest on sub-point i. Items 4, 11, 25 and 28 rest
on sub-point ii.

Thirty questions cannot come from one statement alone, so the rest CHAIN, and
each claim names the chain rather than leaving it implicit:
  item 9 and 23 to EK 2.5.A.2, passive transport takes no direct energy input;
  items 22 and 9 to EK 2.5.A.3, active transport takes one and can run uphill;
  item 12 to EK 2.6.A.1 i, membranes may become polarized by ion movement;
  items 10 and 20 to EK 2.6.A.2, facilitated diffusion uses proteins and NO
    energy -- which is exactly why EK 2.8.A.1 i's protein requirement cannot by
    itself identify active transport, and items 10, 20 and 24 are built on that;
  items 21 and 23 to EK 2.4.A.2, small nonpolar molecules freely pass.
Item 26 rests on design logic: holding the energy supply constant is what turns
a comparison into a test of the protein rather than of the energy.

NOTHING ABOUT THE PUMP'S MECHANISM IS ASSERTED. EK 2.8.A.1 ii says only that the
sodium-potassium pump and ATPase contribute to the maintenance of the membrane
potential, and no item here goes further than that sentence.

DATA ITEMS: 13 to 21 carry tables. Every keyed conclusion is recomputed below
from the table alone. The yes and no columns of the process table are checked
against that two-value vocabulary, so a stray cell fails rather than ships.

NEGATIVE CONTROL: ``python3 verify_b2_8.py --selftest`` corrupts a key, an
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


PUMPED = "Sodium ions pumped out of the cell per minute (arbitrary units)"
POT = "Magnitude of the membrane potential (millivolts)"
OUT = "Sodium concentration outside the cell (millimolar)"
IN = "Sodium concentration inside the cell (millimolar)"
NEEDS_PROTEIN = "Requires a membrane protein"
NEEDS_ENERGY = "Requires a direct input of metabolic energy"

UNTREATED = "Untreated cells"
NO_ATP = "Cells with ATP synthesis blocked"
NO_PUMP = "Cells with the pump proteins removed"


def q13(table, item):
    pumped = {lab: cg.cell(table, lab, PUMPED) for lab in cg.labels(table)}
    pot = {lab: cg.cell(table, lab, POT) for lab in cg.labels(table)}
    for treated in (NO_ATP, NO_PUMP):
        assert pumped[treated] < pumped[UNTREATED] / 5, f"{treated} must cut pumping sharply: {pumped}"
        assert pot[treated] < pot[UNTREATED] / 3, f"{treated} must cut the potential sharply: {pot}"
    return (f"pumping falls from {pumped[UNTREATED]:.0f} to {pumped[NO_ATP]:.0f} and "
            f"{pumped[NO_PUMP]:.0f}, and the potential from {pot[UNTREATED]:.0f} to "
            f"{pot[NO_ATP]:.0f} and {pot[NO_PUMP]:.0f}")


def q14(table, item):
    labs = cg.labels(table)
    assert NO_PUMP in labs and NO_ATP in labs, f"both treatments must be present: {labs}"
    assert "pump proteins removed" in NO_PUMP and "ATP synthesis blocked" in NO_ATP, \
        "the two treatments must differ in which requirement they remove"
    pumped = {lab: cg.cell(table, lab, PUMPED) for lab in labs}
    assert pumped[NO_PUMP] < pumped[UNTREATED] / 5, \
        "removing the proteins must reduce pumping, or it isolates nothing"
    return (f"one treatment removes the proteins and leaves the energy supply, the other "
            f"the reverse; pumping under the protein-free treatment is {pumped[NO_PUMP]:.0f}")


def q15(table, item):
    pumped = {lab: cg.cell(table, lab, PUMPED) for lab in cg.labels(table)}
    ratio = pumped[UNTREATED] / pumped[NO_ATP]
    assert 25 <= ratio <= 35, f"the ratio recomputes to {ratio}, not about thirty"
    return f"{pumped[UNTREATED]:.0f} over {pumped[NO_ATP]:.0f} is {ratio:.0f}, about thirty"


def q16(table, item):
    out, inn = cg.col(table, OUT), cg.col(table, IN)
    gaps = [o - i for o, i in zip(out, inn)]
    assert all(gaps[i] > gaps[i + 1] for i in range(len(gaps) - 1)), f"the gap must shrink: {gaps}"
    assert gaps[-1] == 0, f"the final gap must be zero, not {gaps[-1]}"
    assert all(out[i] > out[i + 1] for i in range(len(out) - 1)), f"outside must fall: {out}"
    assert all(inn[i] < inn[i + 1] for i in range(len(inn) - 1)), f"inside must rise: {inn}"
    assert min(out) > 0 and min(inn) > 0, "'both fell to zero' must be false"
    return f"the gap between the two sides runs {gaps}, shrinking to zero"


def q17(table, item):
    out, inn = cg.col(table, OUT), cg.col(table, IN)
    assert out[0] - inn[0] > 0, "a gradient must already exist at the moment energy was removed"
    assert out[-1] - inn[-1] == 0, "it must be gone by the end"
    return (f"the gradient stood at {out[0] - inn[0]:.0f} millimolar when energy was removed and "
            "reached zero afterwards, which tests maintenance rather than establishment")


def q18(table, item):
    out, inn = cg.col(table, OUT), cg.col(table, IN)
    assert out[0] > inn[0], "the starting state must be a real gradient to be maintained"
    assert out[-1] - inn[-1] < out[0] - inn[0], "the observed course must be a decay, not a growth"
    return (f"the observed course decays from {out[0] - inn[0]:.0f} to {out[-1] - inn[-1]:.0f} "
            "millimolar, so the counterfactual with energy available is the maintained gradient")


def _yesno(table):
    jp = table["headers"].index(NEEDS_PROTEIN)
    je = table["headers"].index(NEEDS_ENERGY)
    out = {}
    for r in table["rows"]:
        assert r[jp] in ("yes", "no") and r[je] in ("yes", "no"), \
            f"the requirement columns must read yes or no; got {r[jp]!r} and {r[je]!r}"
        out[r[0]] = (r[jp], r[je])
    return out


def q19(table, item):
    yn = _yesno(table)
    hits = sorted(lab for lab, v in yn.items() if v == ("yes", "yes"))
    assert hits == ["Process 1"], f"rows needing both a protein and energy: {hits}"
    return f"exactly one row answers yes to both requirements, {hits[0]}"


def q20(table, item):
    yn = _yesno(table)
    hits = sorted(lab for lab, v in yn.items() if v == ("yes", "no"))
    assert hits == ["Process 2"], f"rows needing a protein but no energy: {hits}"
    return f"exactly one row answers yes to the protein and no to the energy, {hits[0]}"


def q21(table, item):
    yn = _yesno(table)
    hits = sorted(lab for lab, v in yn.items() if v == ("no", "no"))
    assert hits == ["Process 3"], f"rows needing neither: {hits}"
    assert len(set(yn.values())) == len(yn), "the three rows must be distinguishable from one another"
    return f"exactly one row answers no to both requirements, {hits[0]}, and no two rows match"


CLAIMS = [
 ("Active transport of molecules and ions across the membrane, and establishing",
  "EK 2.8.A.1, near verbatim: metabolic energy is required for active transport of molecules and ions across the membrane and to establish and maintain electrochemical gradients. EK 2.5.A.2 defines passive transport as happening without such an input."),
 ("ATP",
  "EK 2.8.A.1 gives ATP as its example, in the phrase metabolic energy such as that from ATP. The framework offers no other source for active transport in this statement."),
 ("Membrane proteins are necessary for active transport",
  "EK 2.8.A.1 i, verbatim in substance. EK 2.4.A.3 separately makes the hydrophobic interior what prevents ions and polar molecules from crossing directly, so the no-protein route is closed."),
 ("The sodium-potassium pump and ATPase",
  "EK 2.8.A.1 ii states that the sodium-potassium pump and ATPase contribute to the maintenance of the membrane potential. Aquaporins carry water under EK 2.6.A.3 and the cell wall is a separate barrier under EK 2.4.B.1."),
 ("To maintain that gradient once it exists",
  "EK 2.8.A.1 requires metabolic energy to establish AND maintain electrochemical gradients, both verbs in one clause, so the supply is needed continuously rather than only at the outset."),
 ("energy is required to maintain the gradient as well as to establish it",
  "EK 2.8.A.1 puts establish and maintain in the same clause. The framework says nothing about proteins being consumed, and EK 2.4.A.1 makes the membrane selectively rather than completely impermeable."),
 ("Active transport stops, and existing electrochemical gradients are no longer maintained",
  "EK 2.8.A.1 makes metabolic energy required both for active transport and to establish and maintain electrochemical gradients, so its loss reaches both. EK 2.5.A.2 makes passive transport independent of that input."),
 ("It will stop, because membrane proteins are necessary",
  "EK 2.8.A.1 i states that membrane proteins are necessary for active transport, so an intact energy supply is not sufficient on its own. EK 2.4.A.3 closes the direct route through the hydrophobic interior."),
 ("Active transport needs a direct input of metabolic energy and passive transport does not",
  "EK 2.8.A.1 and EK 2.5.A.3 both require the direct input of energy for active transport, and EK 2.5.A.2 defines passive transport as occurring without it. Selective permeability is common ground under EK 2.5.A.1."),
 ("Active transport requires metabolic energy and facilitated diffusion occurs with no energy input",
  "EK 2.8.A.1 requires metabolic energy for active transport and EK 2.6.A.2 states that facilitated diffusion moves substances with no energy input and down the gradient. Both use proteins, so EK 2.8.A.1 i's protein requirement cannot separate them."),
 ("The sodium-potassium pump",
  "EK 2.8.A.1 ii names the sodium-potassium pump, with ATPase, as contributing to the maintenance of the membrane potential. Aquaporins carry water under EK 2.6.A.3 and the contractile vacuole is an osmoregulation example under EK 2.7.A.1."),
 ("difference established across the membrane by ions",
  "EK 2.6.A.1 i states that membranes may become polarized by the movement of ions across the membrane and EK 2.8.A.1 ii states that the pump and ATPase contribute to maintaining the membrane potential, so both statements concern the same ion-established difference."),
 ("Both the pumping of sodium and the membrane potential depend",
  "Recomputed in q13 above: both columns fall sharply under either treatment. EK 2.8.A.1 requires metabolic energy for active transport, EK 2.8.A.1 i makes membrane proteins necessary, and EK 2.8.A.1 ii ties the pump to the membrane potential."),
 ("pump proteins were removed while ATP synthesis was left intact",
  "Recomputed in q14 above: the two treatments remove different requirements, and the protein-free one still cuts pumping sharply. Isolating EK 2.8.A.1 i means removing the proteins while leaving the energy available; blocking ATP tests EK 2.8.A.1's energy clause instead."),
 ("About thirty times as fast",
  "Recomputed in q15 above from the two tabulated pumping rates. It is the quantitative form of EK 2.8.A.1's claim that metabolic energy is required for active transport."),
 ("difference between the two sides shrank until the concentrations were equal",
  "Recomputed in q16 above: the gap shrinks at every step to exactly zero while the outside falls and the inside rises, and neither concentration reaches zero. EK 2.8.A.1 requires metabolic energy to maintain electrochemical gradients."),
 ("maintaining an electrochemical gradient, and not merely establishing it",
  "Recomputed in q17 above: a gradient already existed when the energy supply was removed and had gone by the end, so the observation bears on maintenance rather than establishment. EK 2.8.A.1 puts both verbs in the same clause."),
 ("would have been maintained rather than decaying to zero",
  "Recomputed in q18 above: the observed course is a decay from a real starting gradient. EK 2.8.A.1's explicit use of the word maintain is what makes the counterfactual prediction available."),
 ("Process 1",
  "Recomputed in q19 above: exactly one row answers yes to both requirements, which is what EK 2.8.A.1 and EK 2.8.A.1 i together demand of active transport."),
 ("Process 2",
  "Recomputed in q20 above: exactly one row answers yes to the protein and no to the energy, which is what EK 2.6.A.1 and EK 2.6.A.2 together describe for facilitated diffusion."),
 ("Process 3",
  "Recomputed in q21 above: exactly one row answers no to both, which is EK 2.4.A.2's free passage of small nonpolar molecules, and the check confirms the three rows are mutually distinguishable."),
 ("accumulates against its concentration gradient, and the accumulation stops",
  "EK 2.5.A.3 gives active transport the direct input of energy and, in some cases, movement from low concentration to high, and EK 2.8.A.1 restates the energy requirement. Crossing through an embedded protein is shared with facilitated diffusion under EK 2.6.A.1."),
 ("movement of a small nonpolar molecule down its concentration gradient",
  "EK 2.4.A.2 lets small nonpolar molecules freely pass and EK 2.5.A.2 makes such movement independent of a direct energy input. The other three listed processes are exactly what EK 2.8.A.1 says metabolic energy is required for."),
 ("Membrane proteins are also necessary for active transport",
  "EK 2.8.A.1 names metabolic energy as required and EK 2.8.A.1 i separately states that membrane proteins are necessary, so the framework names two requirements rather than one. EK 2.6.A.2 shows that a protein without energy gives facilitated diffusion, not active transport."),
 ("Contributing, along with the sodium-potassium pump",
  "EK 2.8.A.1 ii names the sodium-potassium pump and ATPase together as contributing to the maintenance of the membrane potential. Water transport belongs to aquaporins under EK 2.6.A.3 and digestion to lysosomes under EK 2.1.A.6."),
 ("otherwise identical cells without it, both supplied with the same energy source",
  "A requirement claim about the protein needs the protein to be the only difference, with the energy supply held constant. Comparing energy-supplied against energy-deprived cells tests EK 2.8.A.1's energy clause rather than EK 2.8.A.1 i's protein clause."),
 ("spent to build and hold electrochemical gradients",
  "EK 2.8.A.1 states that metabolic energy is required to establish and maintain electrochemical gradients, so in this statement energy is spent on the gradient rather than obtained from it."),
 ("sodium-potassium pump and ATPase, which contribute to maintaining",
  "EK 2.8.A.1 ii names both as contributors to the maintenance of the membrane potential, and EK 2.8.A.1 makes metabolic energy required for active transport and for maintaining electrochemical gradients. Aquaporins carry water under EK 2.6.A.3 and are not tied to the potential."),
 ("direct input of metabolic energy and the presence of membrane proteins",
  "EK 2.8.A.1 requires metabolic energy for active transport and EK 2.8.A.1 i states that membrane proteins are necessary for it, so both requirements come from the same statement group."),
 ("drives active transport and both",
  "The three parts come from one statement and its two sub-points: EK 2.8.A.1 for the energy requirement covering active transport and the establishment and maintenance of electrochemical gradients, EK 2.8.A.1 i for the necessity of membrane proteins, and EK 2.8.A.1 ii for the pump and ATPase contributing to the maintenance of the membrane potential."),
]

TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18,
                19: q19, 20: q20, 21: q21}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b2_8_mutant")
        mod.TOPIC = b2_8.TOPIC
        mod.QUESTIONS = copy.deepcopy(b2_8.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def potential_unaffected(mod, claims):
        mod.QUESTIONS[12]["table"] = dict(
            headers=b2_8._T_PUMP["headers"],
            rows=[["Untreated cells", "240", "70"],
                  ["Cells with ATP synthesis blocked", "8", "68"],
                  ["Cells with the pump proteins removed", "4", "10"]])

    def gradient_never_closes(mod, claims):
        mod.QUESTIONS[15]["table"] = dict(
            headers=b2_8._T_DECAY["headers"],
            rows=[["0", "145", "12"], ["20", "120", "38"], ["40", "95", "62"], ["60", "88", "70"]])

    def no_gradient_to_start(mod, claims):
        mod.QUESTIONS[16]["table"] = dict(
            headers=b2_8._T_DECAY["headers"],
            rows=[["0", "79", "79"], ["20", "79", "79"], ["40", "79", "79"], ["60", "79", "79"]])

    def requirement_cell_typo(mod, claims):
        mod.QUESTIONS[18]["table"] = dict(
            headers=b2_8._T_PROCESSES["headers"],
            rows=[["Process 1", "sometimes", "yes"], ["Process 2", "yes", "no"],
                  ["Process 3", "no", "no"]])

    def two_rows_alike(mod, claims):
        mod.QUESTIONS[19]["table"] = dict(
            headers=b2_8._T_PROCESSES["headers"],
            rows=[["Process 1", "yes", "yes"], ["Process 2", "yes", "no"],
                  ["Process 3", "yes", "no"]])

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[3].__setitem__("ans", 2))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(10, ("no such phrase", c[10][1])))
    must_fail("the membrane potential made insensitive to blocking ATP", potential_unaffected)
    must_fail("the sodium gradient made never to close", gradient_never_closes)
    must_fail("the starting gradient removed, so maintenance is untested", no_gradient_to_start)
    must_fail("a requirement cell outside the yes and no vocabulary", requirement_cell_typo)
    must_fail("two processes given identical requirements", two_rows_alike)
    must_fail("a backslash macro in a choice",
              lambda m, c: m.QUESTIONS[1]["choices"].__setitem__(3, "Heat, at \\Delta T above zero"))
    print("all negative controls raised as required.")


import b2_8  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b2_8)
cg.check(b2_8, CLAIMS, table_checks=TABLE_CHECKS)
