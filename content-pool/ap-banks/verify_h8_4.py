"""Key audit for AP CHEMISTRY 8.4 Acid-Base Reactions and Buffers.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  8.4.A.1  strong + strong react quantitatively; pH from the EXCESS reagent
                                                 1, 2, 3, 4, 5, 19, 20, 21, 25, 29
  8.4.A.2  weak acid + strong base: weak in excess gives a buffer, strong in
           excess gives a pH from excess hydroxide and total volume, equimolar
           gives a slightly basic pH from the conjugate base with water
                                                 6, 7, 8, 9, 10, 11, 12, 22, 23,
                                                 24, 26, 30
  8.4.A.3  weak base + strong acid, the same three cases mirrored
                                                 13, 14, 15, 16, 27
  8.4.A.4  weak + weak react TO AN EQUILIBRIUM STATE, not quantitatively
                                                 17, 18, 28

THE SEPARATION FROM 8.8, 8.9 AND 8.10, checked rather than intended. Four topics
in this unit speak about buffers, and they were planned together before any was
written: 8.4 decides WHICH CASE a mixture is, 8.8 gives the mechanism, 8.9 the
Henderson-Hasselbalch arithmetic, 8.10 the capacity. Two checks below enforce
this module's half of that bargain:

  ``no_buffer_arithmetic``  no item here takes a logarithm of a concentration
                            ratio or invokes the Henderson-Hasselbalch equation
                            in a KEY -- that is 8.9's work
  ``no_capacity_language``  no item here compares how much acid or base a buffer
                            can absorb -- that is 8.10's work

Without those, four topics on one idea produce four copies of the same thirty
questions, which is the failure SOCIAL_DEDUPE.md records for the Government
banks.

ARITHMETIC. Every excess-reagent pH is recomputed from the millimoles and the
total volume through ``excess_ph``, written once.

NEGATIVE CONTROL: ``python3 verify_h8_4.py --selftest``.
"""
import math
import re
import sys

import cg_check as cg
import h_check as h

import h8_4

HA_MM = "Millimoles of weak acid HA"
NAOH_MM = "Millimoles of NaOH added"
B_MM = "Millimoles of weak base B"
HCL_MM = "Millimoles of HCl added"
ACID_MM = "Millimoles of HCl"
BASE_MM = "Millimoles of NaOH"
VOL = "Total volume after mixing (mL)"

# 8.9 owns the Henderson-Hasselbalch arithmetic and 8.10 owns capacity.
# Explicit lookarounds, never \b beside a letter run.
_HH = re.compile(r"henderson|(?<![A-Za-z])p\s*K_?a\s*\+|\\log|(?<![A-Za-z])log(?![A-Za-z])",
                 re.I)
_CAPACITY = re.compile(r"(?<![A-Za-z])(?:capacit(?:y|ies)|neutraliz\w*|absorb\w*)(?![A-Za-z])",
                       re.I)


def no_buffer_arithmetic(module):
    """No KEY here may compute a buffer pH -- that is topic 8.9's material."""
    for i, item in enumerate(module.QUESTIONS, 1):
        keyed = h.keyed(item)
        hit = _HH.search(keyed)
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the keyed choice invokes the buffer arithmetic "
            f"({hit.group(0)!r}), which belongs to 8.9 -- {keyed[:60]!r}"
        )
    print(f"OK  {module.TOPIC[0]} scope: no keyed choice computes a buffer pH, which is "
          "8.9's material.")


def no_capacity_language(module):
    """No item here may compare buffer capacity -- that is topic 8.10's material."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _CAPACITY.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to buffer capacity ({hit.group(0)!r}), "
                f"which belongs to 8.10 -- {text[:60]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item compares buffer capacity, which is "
          "8.10's material.")


def excess_ph(acid_mmol, base_mmol, volume_ml):
    """EK 8.4.A.1: the two react one for one; the pH follows from what is left.

    Returns (pH, which reagent is in excess).
    """
    net = acid_mmol - base_mmol
    if abs(net) < 1e-12:
        return 7.0, "neither"
    conc = abs(net) / volume_ml          # millimoles per millilitre is molarity
    if net > 0:
        return -math.log10(conc), "acid"
    return 14.0 + math.log10(conc), "base"


# ------------------------------------------------------------------ table items

def q7(table, item):
    acid = dict(zip(cg.labels(table), cg.col(table, HA_MM)))
    base = dict(zip(cg.labels(table), cg.col(table, NAOH_MM)))
    buffers = [lab for lab in acid if acid[lab] > base[lab]]
    assert buffers == ["1"], f"tabulated mixtures with the weak acid in excess: {buffers}"
    h.shows(item, "Mixture 1")
    return (f"comparing {acid} with {base}, exactly one mixture leaves the weak acid in "
            "excess, which is the buffer case")


def q8(table, item):
    acid = dict(zip(cg.labels(table), cg.col(table, HA_MM)))
    base = dict(zip(cg.labels(table), cg.col(table, NAOH_MM)))
    equal = [lab for lab in acid if abs(acid[lab] - base[lab]) < 1e-12]
    assert equal == ["2"], f"tabulated equimolar mixtures: {equal}"
    h.shows(item, "Mixture 2")
    return f"exactly one tabulated mixture has equal millimoles of the two reagents: {equal}"


def q9(table, item):
    acid = cg.cell(table, "2", HA_MM)
    base = cg.cell(table, "2", NAOH_MM)
    left = acid - base
    assert abs(left) < 1e-12, f"mixture 2 leaves {left} millimoles of weak acid"
    h.shows(item, "conjugate base of the weak acid")
    return (f"the tabulated {acid:g} millimoles of weak acid are exactly consumed by "
            f"{base:g} millimoles of hydroxide, leaving none")


def q10(table, item):
    acid = cg.cell(table, "2", HA_MM)
    base = cg.cell(table, "2", NAOH_MM)
    assert abs(acid - base) < 1e-12, "this item must sit at the equimolar point"
    h.shows(item, "Slightly basic")
    return (f"the tabulated {acid:g} and {base:g} millimoles are equal, which is the case "
            "EK 8.4.A.2 calls slightly basic")


def q11(table, item):
    acid = cg.cell(table, "3", HA_MM)
    base = cg.cell(table, "3", NAOH_MM)
    assert base > acid, f"mixture 3 must have the strong base in excess: {base} against {acid}"
    h.shows(item, "moles of excess hydroxide ion")
    return (f"the tabulated {base:g} millimoles of hydroxide exceed the {acid:g} of weak "
            "acid, leaving strong base in excess")


def q14(table, item):
    base = dict(zip(cg.labels(table), cg.col(table, B_MM)))
    acid = dict(zip(cg.labels(table), cg.col(table, HCL_MM)))
    buffers = [lab for lab in base if base[lab] > acid[lab]]
    assert buffers == ["4"], f"tabulated mixtures with the weak base in excess: {buffers}"
    h.shows(item, "Mixture 4")
    return (f"comparing {base} with {acid}, exactly one mixture leaves the weak base in "
            "excess, which is the buffer case")


def q15(table, item):
    base = cg.cell(table, "5", B_MM)
    acid = cg.cell(table, "5", HCL_MM)
    assert abs(base - acid) < 1e-12, f"mixture 5 must be equimolar: {base} against {acid}"
    h.shows(item, "slightly acidic")
    return (f"the tabulated {base:g} and {acid:g} millimoles are equal, which is the case "
            "EK 8.4.A.3 calls slightly acidic")


def q16(table, item):
    base = cg.cell(table, "6", B_MM)
    acid = cg.cell(table, "6", HCL_MM)
    assert acid > base, f"mixture 6 must have the strong acid in excess: {acid} against {base}"
    h.shows(item, "moles of excess hydronium ion")
    return (f"the tabulated {acid:g} millimoles of strong acid exceed the {base:g} of weak "
            "base, leaving strong acid in excess")


def q19(table, item):
    ph, who = excess_ph(cg.cell(table, "A", ACID_MM), cg.cell(table, "A", BASE_MM),
                        cg.cell(table, "A", VOL))
    assert who == "acid" and abs(ph - 1.0) < 1e-9, f"trial A gives pH {ph} with {who} in excess"
    h.shows(item, "1.00")
    return f"the tabulated millimoles and volume recompute trial A's pH as {ph:g}"


def q20(table, item):
    ph, who = excess_ph(cg.cell(table, "B", ACID_MM), cg.cell(table, "B", BASE_MM),
                        cg.cell(table, "B", VOL))
    assert who == "base" and abs(ph - 13.0) < 1e-9, f"trial B gives pH {ph} with {who} in excess"
    h.shows(item, "13.00")
    return f"the tabulated millimoles and volume recompute trial B's pH as {ph:g}"


def q21(table, item):
    ph, who = excess_ph(cg.cell(table, "C", ACID_MM), cg.cell(table, "C", BASE_MM),
                        cg.cell(table, "C", VOL))
    assert who == "neither", f"trial C leaves {who} in excess"
    h.shows(item, "Neither reagent is in excess")
    return f"the tabulated millimoles for trial C are equal, so nothing is left over"


TABLE_CHECKS = {7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 14: q14, 15: q15, 16: q16,
                19: q19, 20: q20, 21: q21}


# ---------------------------------------------------------------- stem numerics

def n3(item):
    ph, who = excess_ph(15.0, 5.00, 100.0)
    assert who == "acid" and abs(ph - 1.0) < 1e-9, f"recomputed pH {ph} with {who} in excess"
    h.shows(item, "1.00")
    return f"10.0 millimoles of excess hydronium in 100.0 mL recomputes the pH as {ph:g}"


def n4(item):
    ph, who = excess_ph(5.00, 15.0, 100.0)
    assert who == "base" and abs(ph - 13.0) < 1e-9, f"recomputed pH {ph} with {who} in excess"
    h.shows(item, "13.00")
    return f"10.0 millimoles of excess hydroxide in 100.0 mL recomputes the pH as {ph:g}"


def n25(item):
    ph, who = excess_ph(5.000, 4.900, 100.0)
    assert who == "acid" and abs(ph - 3.0) < 1e-9, f"recomputed pH {ph} with {who} in excess"
    h.shows(item, "3.00")
    return f"0.100 millimole of excess hydronium in 100.0 mL recomputes the pH as {ph:g}"


def n29(item):
    ph, who = excess_ph(9.00, 10.0, 100.0)
    poh = 14.0 - ph
    assert who == "base" and abs(poh - 2.0) < 1e-9, f"recomputed pOH {poh} with {who} in excess"
    h.shows(item, "2.00")
    return f"1.00 millimole of excess hydroxide in 100.0 mL recomputes the pOH as {poh:g}"


NUMERIC = {3: n3, 4: n4, 25: n25, 29: n29}


CLAIMS = [
 ("H+(aq) + OH-(aq) to H2O(l)",
  "EK 8.4.A.1 gives this equation for a strong acid mixed with a strong base and says they react quantitatively."),
 ("concentration of the reagent present in excess",
  "EK 8.4.A.1, verbatim in substance: the pH of the resulting solution may be determined from the concentration of excess reagent. Neither reagent has an ionization constant to use, since both react completely."),
 ("1.00",
  "EK 8.4.A.1's one-for-one reaction with the acid in excess. Recomputed in n3 from the millimoles and the total volume."),
 ("13.00",
  "EK 8.4.A.1 with the base in excess, converted to a pH through EK 8.1.A.3. Recomputed in n4."),
 ("neither reagent is left in excess",
  "EK 8.4.A.1's quantitative reaction leaves nothing over at equal moles, and the spectator ions of a strong acid and a strong base do not react further with water. The slightly basic equimolar case belongs to EK 8.4.A.2, where one component is weak."),
 ("HA(aq) + OH-(aq) to A-(aq) + H2O(l)",
  "EK 8.4.A.2's equation for a weak acid mixed with a strong base, which the framework also calls quantitative."),
 ("Mixture 1",
  "EK 8.4.A.2 attaches the buffer to the case in which the WEAK ACID is in excess. The tabulated millimoles are compared in q7 and exactly one mixture qualifies."),
 ("Mixture 2",
  "EK 8.4.A.2 treats the equimolar case separately. The tabulated millimoles are compared in q8 and exactly one pair is equal."),
 ("conjugate base of the weak acid",
  "EK 8.4.A.2's equation converts the weak acid to its conjugate base one for one, and q9 recomputes that the tabulated equimolar mixture leaves no un-ionized acid at all."),
 ("Slightly basic",
  "EK 8.4.A.2 says that if the two are equimolar, the slightly basic pH follows from A-(aq) + H2O(l) to HA(aq) + OH-(aq). The equimolar condition is recomputed in q10."),
 ("moles of excess hydroxide ion",
  "EK 8.4.A.2, verbatim in substance: if the strong base is in excess, the pH can be determined from the moles of excess hydroxide ion and the total volume of solution. The excess is recomputed in q11."),
 ("weak acid is in excess after the reaction",
  "EK 8.4.A.2 names three cases and attaches the buffer to exactly one of them, the case in which the weak acid is in excess."),
 ("B(aq) + H3O+(aq) to HB+(aq) + H2O(l)",
  "EK 8.4.A.3's equation for a weak base mixed with a strong acid."),
 ("Mixture 4",
  "EK 8.4.A.3 attaches the buffer to the case in which the weak base is in excess. The tabulated millimoles are compared in q14."),
 ("slightly acidic",
  "EK 8.4.A.3 says the equimolar case gives a slightly acidic pH from HB+(aq) + H2O(l) to B(aq) + H3O+(aq). The equimolar condition is recomputed in q15."),
 ("moles of excess hydronium ion",
  "EK 8.4.A.3, verbatim in substance: if the strong acid is in excess, the pH can be determined from the moles of excess hydronium ion and the total volume. Recomputed in q16."),
 ("HA(aq) + B(aq) to A-(aq) + HB+(aq)",
  "EK 8.4.A.4's equation for a weak acid mixed with a weak base, a proton transfer between two weak partners."),
 ("rather than quantitatively as the other",
  "EK 8.4.A.4 uses that phrase, while EK 8.4.A.1, 8.4.A.2 and 8.4.A.3 each say quantitatively for the combinations containing a strong reagent."),
 ("1.00",
  "EK 8.4.A.1 applied to tabulated millimoles and a tabulated volume. Recomputed in q19."),
 ("13.00",
  "EK 8.4.A.1 with the tabulated hydroxide in excess. Recomputed in q20."),
 ("Neither reagent is in excess",
  "EK 8.4.A.1's quantitative reaction on equal tabulated millimoles. Recomputed in q21; a buffer would require a weak component, which neither tabulated reagent is."),
 ("conjugate base of that weak acid, formed by the reaction",
  "EK 8.4.A.2's equation produces one conjugate base for every hydroxide consumed, so remaining un-ionized acid must be accompanied by the conjugate base already made. The reaction is quantitative, so hydroxide cannot remain alongside it."),
 ("strong enough base to remove the proton essentially completely",
  "EK 8.4.A.2 describes the reaction as quantitative, which is what licenses the mole bookkeeping of this topic. The weakness of the acid governs its equilibrium with water under EK 8.3.A.2, a different reaction."),
 ("both members of the conjugate pair are present in quantity",
  "EK 8.4.A.2 attaches the buffer to the weak-acid-in-excess case, and the amounts given are exactly what that case leaves behind."),
 ("3.00",
  "EK 8.4.A.1 with a small excess, so the pH is far from that of the acid alone. Recomputed in n25."),
 ("weak acid and excess hydroxide ion",
  "EK 8.4.A.2 makes their reaction quantitative, so whichever is in shorter supply is consumed and the two cannot coexist in quantity. A weak acid with its conjugate base is the buffer that same statement describes."),
 ("weak base and its conjugate acid, in comparable amounts",
  "EK 8.4.A.3 says a buffer forms when the weak base is in excess, which means both the remaining base and the conjugate acid produced by the reacted portion are present."),
 ("weak acid mixed with a weak base",
  "EK 8.4.A.4 alone says the reaction reaches an equilibrium state; the other three statements each use the word quantitatively."),
 ("2.00",
  "EK 8.4.A.1 with the base in excess, reported as a pOH. Recomputed in n29."),
 ("conjugate base left behind reacts with water",
  "EK 8.4.A.2 gives the equimolar case its own equation and calls the result slightly basic, while EK 8.4.A.1 leaves only spectator ions. Both reactions are quantitative, so no reagent survives the equimolar point in either case."),
]


def _extra_mutations():
    def corrupt_table(mod, cl):
        mod.QUESTIONS[6]["table"] = dict(
            headers=h8_4._T_MIXTURES["headers"],
            rows=[[lab, a, ("9.00" if lab == "1" else b)]
                  for lab, a, b in h8_4._T_MIXTURES["rows"]])

    def corrupt_numeric(mod, cl):
        ch = list(mod.QUESTIONS[2]["choices"])
        ch[0] = "pH = 1.30"
        mod.QUESTIONS[2]["choices"] = ch
        cl[2] = ("1.30", cl[2][1])

    def buffer_arithmetic_creeps_in(mod, cl):
        ch = list(mod.QUESTIONS[0]["choices"])
        ch[0] = "Use the Henderson-Hasselbalch equation on the ratio of the two species"
        mod.QUESTIONS[0]["choices"] = ch
        cl[0] = ("Henderson-Hasselbalch equation", cl[0][1])
        no_buffer_arithmetic(mod)

    def capacity_language_creeps_in(mod, cl):
        mod.QUESTIONS[5]["q"] = ("Which mixture has the greater buffer capacity for added "
                                 "base?")
        no_capacity_language(mod)

    return [("a tabulated millimole figure corrupted so the buffer case changes", corrupt_table),
            ("a recomputed excess pH no longer in the keyed choice", corrupt_numeric),
            ("a key invoking the Henderson-Hasselbalch equation, which is 8.9's material",
             buffer_arithmetic_creeps_in),
            ("an item comparing buffer capacity, which is 8.10's material",
             capacity_language_creeps_in)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h8_4, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_buffer_arithmetic(h8_4)
no_capacity_language(h8_4)
h.run(h8_4, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
