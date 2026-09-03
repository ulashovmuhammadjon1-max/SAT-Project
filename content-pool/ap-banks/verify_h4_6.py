"""Key audit for AP CHEMISTRY 4.6 Introduction to Titration.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Nine stem-data items and five table items are
recomputed from their own stimulus and asserted against the keyed choice.

WHAT THE KEYS REST ON
---------------------
Topic 4.6 has exactly ONE essential knowledge statement, 4.6.A.1, and every key
in this module traces to a clause of it:

  "titrations may be used to determine the amount of an analyte in solution"
      -- items 9, 11, 21, 24, 26, 28
  "the titrant has a known concentration of a species that reacts specifically
   and quantitatively with the analyte"
      -- items 3, 4, 21, 26
  "the equivalence point ... occurs when the analyte is totally consumed by the
   reacting species in the titrant"
      -- items 1, 5, 6, 10, 13, 14, 16, 17, 18, 22, 23, 25, 27, 29
  "the equivalence point is often indicated by a change in a property (such as
   color) ... this observable event is called the endpoint"
      -- items 2, 7, 8, 12, 15, 19, 20, 30

Items 18 and 29 also lean on EK 4.5.A.2, that the coefficients of a balanced
equation give the proportionality of the amounts -- which is what makes a one to
two titration reach its equivalence point at a different delivered amount than a
one to one titration. That is a chain across two topics, not a repeat of either.

NOT ASSESSED HERE: the pH at the equivalence point, acid and base strength, and
how an indicator's own equilibrium sets its transition range. Those belong to
Unit 8. A pH column in a table here is only a measured property whose sharp
change locates the equivalence point, which is what 4.6.A.1 says such a change
does.

NEGATIVE CONTROL: ``python3 verify_h4_6.py --selftest`` corrupts a key, an
anchor, the notation, a table cell and a stem-recomputed value on purpose and
requires each corruption to be caught.
"""
import sys

import h_chem_notation as hn
import h4_6 as M

PH = "Measured pH"
VNAOH = "Volume of 0.100 M NaOH added (milliliters)"
VBA = "Volume of 0.050 M Ba(OH)2 added (milliliters)"
COND = "Conductivity of the mixture (arbitrary units)"
VEND = "Volume of 0.150 M titrant at the endpoint (milliliters)"
VACID = "Volume of acid (milliliters)"
CACID = "Concentration of acid (moles per liter)"


# ------------------------------------------------------------ table questions

def q7(t, item):
    v = hn.cg.col(t, VNAOH)
    ph = hn.cg.col(t, PH)
    assert ph == sorted(ph), "'the pH stops rising' must be false, so the column must rise throughout"
    steep = {}
    for i in range(1, len(v) - 1):
        steep[v[i]] = (ph[i + 1] - ph[i - 1]) / (v[i + 1] - v[i - 1])
    sharpest = max(steep, key=steep.get)
    assert sharpest == 25.0, f"the sharpest change sits at {sharpest} mL, not 25.0"
    early = (ph[1] - ph[0]) / (v[1] - v[0])
    assert early < steep[sharpest], \
        "'the earliest readings change fastest per milliliter' must be false"
    hn.keyed(item, "25.0 mL")
    return (f"across the readings bracketing 25.0 mL the pH moves {steep[25.0]:.1f} units "
            f"per milliliter against {early:.2f} over the first interval")


def q12(t, item):
    v = hn.cg.col(t, VBA)
    c = hn.cg.col(t, COND)
    lowest = v[c.index(min(c))]
    assert lowest == 15.0, f"the minimum conductivity sits at {lowest} mL"
    after = [c[i] for i in range(len(v)) if v[i] > lowest]
    assert after == sorted(after) and after[0] > min(c), \
        "conductivity must rise again once the analyte is consumed"
    assert c[0] == max(c), "the starting reading should be the largest, as one distractor claims"
    hn.keyed(item, "15.0 mL")
    return (f"conductivity falls from {c[0]} to its minimum {min(c)} at 15.0 mL and then "
            "rises again as excess titrant accumulates")


def q15(t, item):
    labs = hn.cg.labels(t)
    ends = dict(zip(labs, hn.cg.col(t, VEND)))
    keep = [ends[l] for l in labs if l != "3"]
    assert max(keep) - min(keep) < 0.3, f"the three retained trials disagree: {keep}"
    gap = ends["3"] - sum(keep) / len(keep)
    assert gap > 13.0, f"trial 3 differs from the others by only {gap}"
    assert ends["1"] != max(ends.values()), \
        "'trial 1 is the largest of the first three' must not make it the outlier"
    hn.keyed(item, "Trial 3")
    return (f"trials 1, 2 and 4 span {min(keep)} to {max(keep)} millilitres while trial 3 "
            f"sits {gap:.1f} millilitres away from their mean")


def q18(t, item):
    labs = hn.cg.labels(t)
    vol = dict(zip(labs, hn.cg.col(t, VACID)))
    con = dict(zip(labs, hn.cg.col(t, CACID)))
    mol = {l: vol[l] * con[l] for l in labs}
    assert mol["1"] == mol["2"], f"the two flasks should hold equal amounts of acid: {mol}"
    protons = {"1": 1, "2": 2}
    base = {l: mol[l] * protons[l] for l in labs}
    assert base["2"] == 2 * base["1"], \
        f"flask 2 should require twice the base of flask 1: {base}"
    hn.keyed(item, "twice the volume of flask 1")
    return (f"both flasks hold {mol['1']} millimoles of acid, but H2SO4 needs two hydroxide "
            f"ions each, so the base required is {base['1']} against {base['2']} millimoles")


def q20(t, item):
    v = hn.cg.col(t, "Volume of titrant added (milliliters)")
    colors = [r[1] for r in t["rows"]]
    colored = [v[i] for i, c in enumerate(colors) if "colorless" not in c.lower()]
    assert colored, "no row records a color at all"
    first = min(colored)
    assert first == 17.60, f"the first colored reading is at {first} mL"
    assert max(x for i, x in enumerate(v) if "colorless" in colors[i].lower()) < first, \
        "every colorless reading must precede the first colored one"
    hn.keyed(item, "17.60 mL")
    return (f"the flask is colorless through {max(x for i, x in enumerate(v) if 'colorless' in colors[i].lower())} "
            f"millilitres and first holds a permanent color at {first}")


TABLE_CHECKS = {7: q7, 12: q12, 15: q15, 18: q18, 20: q20}


# --------------------------------------------------------- stem-data questions

def a5(item):
    mol = 0.100 * 20.0          # millimoles of base delivered
    c = mol / 25.0
    hn.keyed(item, f"{c:.4f} M")
    return f"0.100 M times 20.0 mL is {mol} millimoles, over 25.0 mL of sample is {c:.4f} M"


def a6(item):
    acid = 0.100 * 10.0
    base = 2 * acid
    v = base / 0.200
    hn.keyed(item, f"{v:.1f} mL")
    return f"{acid} millimoles of H2SO4 needs {base} millimoles of NaOH, which is {v:.1f} mL"


def a10(item):
    mol = 0.250 * 16.0
    hn.keyed(item, f"{mol:.2f} millimoles")
    return f"0.250 M times 16.0 mL is {mol:.2f} millimoles of acid, matched one to one"


def a13(item):
    n = 0.0020 * 5
    hn.keyed(item, f"{n:.3f} mol")
    return f"five iron(II) per permanganate makes the analyte amount {n:.3f} mol"


def a14(item):
    mol = 0.500 * 0.0200        # moles of base
    mass = mol * 60.0
    hn.keyed(item, f"{mass:.3f} g")
    return f"{mol} mol of base matches {mol} mol of acid, which at 60.0 g/mol is {mass:.3f} g"


def a17(item):
    base = 0.200 * 10.0
    acid = 2 * base
    hn.keyed(item, f"{acid:.2f} millimoles")
    return f"{base} millimoles of Ca(OH)2 needs two HCl each, or {acid:.2f} millimoles"


def a22(item):
    mol = 0.0500 * 30.0
    c = mol / 15.0
    hn.keyed(item, f"{c:.3f} M")
    return f"0.0500 M times 30.0 mL is {mol} millimoles, over 15.0 mL is {c:.3f} M"


def a25(item):
    mass = 0.00400 * 100.0
    hn.keyed(item, f"{mass:.3f} g")
    return f"0.00400 mol of acid at 100. g/mol has a mass of {mass:.3f} g"


def a27(item):
    acid = 0.0800 * 25.0
    base = 2 * acid
    v = base / 0.100
    hn.keyed(item, f"{v:.1f} mL")
    return f"{acid} millimoles of a diprotic acid needs {base} millimoles of base, or {v:.1f} mL"


ARITH = {5: a5, 6: a6, 10: a10, 13: a13, 14: a14, 17: a17, 22: a22, 25: a25, 27: a27}

CLAIMS = [
 ("totally consumed by the reacting species",
  "EK 4.6.A.1, near verbatim: the equivalence point of the titration occurs when the analyte is totally consumed by the reacting species in the titrant. Equal volumes and equal concentrations appear nowhere in that definition."),
 ("endpoint of the titration",
  "EK 4.6.A.1: the equivalence point is often indicated by a change in a property, such as color, and that observable event is called the endpoint of the titration."),
 ("known concentration",
  "EK 4.6.A.1, near verbatim: the titrant has a known concentration of a species that reacts specifically and quantitatively with the analyte. The unknown amount is the analyte's, not the titrant's."),
 ("measure the analyte together with whatever else",
  "EK 4.6.A.1 requires the titrant to react specifically with the analyte. The analyte amount is computed from the amount of titrant delivered, so titrant consumed by any other species would be miscounted as analyte."),
 ("0.0800 M",
  "Recomputed in a5. EK 4.6.A.1 makes the equivalence point the total consumption of the analyte, so the delivered base amount equals the acid amount in a one to one reaction."),
 ("10.0 mL",
  "Recomputed in a6. EK 4.6.A.1 puts the equivalence point at total consumption of the analyte, and the balanced equation requires two moles of base per mole of sulfuric acid."),
 ("25.0 mL",
  "Recomputed in q7 above from the tabulated pH readings. EK 4.6.A.1 states that the equivalence point is often indicated by a change in a property, and the sharpest change in the table brackets that volume."),
 ("may be reached slightly before or after",
  "EK 4.6.A.1 defines the equivalence point as a condition of the mixture and the endpoint as the observable event indicating it. They are separate, so an indicator changing early or late shifts the reading away from the true value."),
 ("amount of the analyte present",
  "EK 4.6.A.1 opens by stating that titrations may be used to determine the amount of an analyte in solution. Rate belongs to Unit 5 and is not what a delivered volume measures."),
 ("4.00 millimoles",
  "Recomputed in a10. EK 4.6.A.1 makes the analyte totally consumed at the equivalence point, and a one to one reaction makes the analyte amount equal to the titrant amount delivered."),
 ("changes the concentration of the analyte but not the amount",
  "EK 4.6.A.1 puts the equivalence point where the analyte is totally consumed, which depends on how much analyte is present. Adding solvent neither adds nor removes analyte."),
 ("15.0 mL",
  "Recomputed in q12 above. EK 4.6.A.1 states that the equivalence point is often indicated by a property change; ions are removed from solution until the analyte is consumed, so the conductivity minimum marks it."),
 ("0.010 mol",
  "Recomputed in a13. EK 4.6.A.1 makes the equivalence point the total consumption of the analyte by the reacting species in the titrant, and the balanced equation puts five iron(II) with each permanganate."),
 ("0.600 g",
  "Recomputed in a14. EK 4.6.A.1 lets the delivered titrant fix the analyte amount; the stated molar mass then converts that amount to a mass."),
 ("Trial 3",
  "Recomputed in q15 above. EK 4.6.A.1 makes the delivered volume the measurement of the analyte amount, so identical samples must require the same volume; three trials agree closely and one does not."),
 ("related to the analyte amount by the coefficients alone",
  "EK 4.6.A.1 makes the equivalence point the total consumption of the analyte, and the learning objective states the assumption that the titration reaction goes to completion. With nothing of either left unreacted, only the coefficients connect the two amounts."),
 ("4.00 millimoles",
  "Recomputed in a17. EK 4.6.A.1 places the equivalence point at total consumption of the analyte, and the balanced equation requires two moles of acid per mole of calcium hydroxide."),
 ("twice the volume of flask 1",
  "Recomputed in q18 above from the table's own volumes and concentrations. The two flasks hold equal amounts of acid, but EK 4.5.A.2's coefficients require two hydroxide ions per H2SO4 and one per HCl."),
 ("Continuing to add titrant past",
  "EK 4.6.A.1 makes the delivered volume the measure of the analyte amount. Titrant added after the analyte has been totally consumed is still counted, so the computed amount comes out too large."),
 ("17.60 mL",
  "Recomputed in q20 above. EK 4.6.A.1 calls the observable property change the endpoint, and the first tabulated reading holding a permanent color is that observation."),
 ("concentration has been determined accurately",
  "EK 4.6.A.1 requires the titrant to have a known concentration. The analyte amount follows from that concentration times the delivered volume, so an error in it passes straight into the result."),
 ("0.100 M",
  "Recomputed in a22. EK 4.6.A.1 puts the equivalence point at total consumption of the analyte, so the delivered base amount is the acid amount in a one to one reaction."),
 ("amount of titrant delivered is twice the amount of analyte",
  "EK 4.6.A.1 makes the equivalence point the total consumption of the analyte by the reacting species in the titrant, and a mole ratio is a statement about amounts. Volumes, concentrations and masses stand in that ratio only by coincidence."),
 ("identity of the indicator",
  "EK 4.6.A.1 makes the computation rest on the titrant's known concentration, the delivered volume, the reaction stoichiometry and the sample volume. The indicator only makes the endpoint visible."),
 ("0.400 g",
  "Recomputed in a25. EK 4.6.A.1 lets the delivered titrant fix the analyte amount, and the stated molar mass converts it to the mass of pure acid present in the impure sample."),
 ("reacts with analyte throughout the flask",
  "EK 4.6.A.1 requires the titrant to react quantitatively with the analyte for the delivered volume to measure it. Titrant sitting unmixed in a local excess has been delivered without yet meeting analyte."),
 ("40.0 mL",
  "Recomputed in a27. EK 4.6.A.1 places the equivalence point at total consumption of the analyte, and removing both protons requires two hydroxide ions per acid molecule."),
 ("delivered half the volume",
  "EK 4.6.A.1 makes the equivalence point the total consumption of the analyte, which is a property of the sample rather than of the titrant. Doubling the titrant concentration halves the volume needed to deliver the same amount."),
 ("set how much titrant is needed",
  "EK 4.6.A.1 defines the equivalence point as the analyte being totally consumed by the reacting species in the titrant, and EK 4.5.A.2 makes the coefficients the proportionality between amounts."),
 ("extra titrant is counted as having reacted",
  "EK 4.6.A.1 separates the equivalence point from the endpoint that signals it. Every millilitre delivered up to the endpoint is treated as having reacted with analyte, so a late endpoint inflates the reported amount."),
]


def _wreck_table(mod, cl):
    """Module-specific control: move the pH jump q7's key rests on.

    Flattening the 25.0 mL reading alone does NOT work -- the check measures the
    slope ACROSS that volume, from its two neighbours, so the single cell it
    names is not one of its own inputs. The corruption has to move the jump, and
    finding that out is the whole point of running the control.
    """
    t = mod.QUESTIONS[6]["table"]
    moved = {"25.0": "4.4", "26.0": "4.8"}
    mod.QUESTIONS[6]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], moved[r[0]]] if r[0] in moved else list(r) for r in t["rows"]])


def _wreck_color(mod, cl):
    """Module-specific control: colour the flask before the endpoint."""
    t = mod.QUESTIONS[19]["table"]
    mod.QUESTIONS[19]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "Faint permanent pink"] if r[0] == "12.00" else list(r)
              for r in t["rows"]])


def _wreck_stem_number(mod, cl):
    """Module-specific control: change a stem volume so its key no longer follows."""
    mod.QUESTIONS[4]["q"] = mod.QUESTIONS[4]["q"].replace("20.0 mL of the base",
                                                          "30.0 mL of the base")
    mod.QUESTIONS[4]["choices"][0] = "0.120 M"


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH,
                extra=[("a pH cell corrupted", _wreck_table),
                       ("a colour cell corrupted", _wreck_color),
                       ("a stem volume edited away from its key", _wreck_stem_number)])

hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
