"""Key audit for AP CHEMISTRY 4.4 Physical and Chemical Changes.

One ``(anchor, claim)`` per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is ``cg_check.check``; the notation gate is
``h_chem_notation.notation``. Neither can tell whether the chemistry is right.
That is gated by the CLAIMS text below and by the rule in SCIENCE_BRIEF.md that
every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
Items 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23,
26, 27, 28 and 30 rest on EK 4.4.A.1: processes that involve the breaking
and/or formation of chemical bonds are typically classified as chemical
processes, while processes that involve only changes in intermolecular
interactions, such as phase changes, are typically classified as physical
processes.

Items 4, 17, 18, 24, 25 and 29 rest on EK 4.4.A.2: sometimes physical processes
involve the breaking of chemical bonds, the framework's own example being the
dissolution of a salt in water, which breaks ionic bonds and forms ion-dipole
interactions between ions and solvent. No item here keys on "dissolving a salt
is physical" or on "dissolving a salt is chemical" -- the framework says a
plausible argument runs either way, and that is what item 4 keys on.

DATA ITEMS: 3, 10, 12, 15, 16, 25 and 28 carry tables. Each keyed conclusion is
recomputed below from that table alone, and each check also falsifies the
distractors against the same numbers.

NEGATIVE CONTROL: ``python3 verify_h4_4.py --selftest`` corrupts a key, an
anchor, the notation and a table cell on purpose and requires each corruption to
be caught.
"""
import sys

import h_chem_notation as hn
import h4_4 as M

VAP = "Enthalpy of vaporization (kilojoules per mole)"
BOND = "Average enthalpy of the bond inside the molecule (kilojoules per mole)"
BP = "Normal boiling point (degrees Celsius)"
NRG = "Energy required (kilojoules per mole)"
DE = "Energy change (kilojoules per mole)"
ADDED = "Mass added (grams)"
BACK = "Mass of solid recovered after all the water was evaporated (grams)"
M0 = "Mass at the start (grams)"
M1 = "Mass after 30 minutes (grams)"
VAL = "Value (kilojoules per mole)"
HVAP = "Enthalpy of vaporization (kilojoules per mole)"
HCOMB = "Enthalpy of complete combustion (kilojoules per mole)"


def q3(t, item):
    e = dict(zip(hn.cg.labels(t), hn.cg.col(t, NRG)))
    bond = e["Breaking one mole of O-H bonds within the molecules"]
    phase = [v for k, v in e.items() if k != "Breaking one mole of O-H bonds within the molecules"]
    assert bond == max(e.values()), f"the bond value {bond} is not the largest"
    assert all(bond > 10 * p for p in phase), \
        f"the bond value is not an order of magnitude above the phase values {phase}"
    assert bond > sum(phase), "the 'sum of the two phase changes' distractor must not reach it"
    return (f"464 is the largest tabulated value, more than ten times each of {phase} "
            f"and larger than their sum {sum(phase)}")


def q10(t, item):
    labs = hn.cg.labels(t)
    vap = dict(zip(labs, hn.cg.col(t, VAP)))
    bond = dict(zip(labs, hn.cg.col(t, BOND)))
    bp = dict(zip(labs, hn.cg.col(t, BP)))
    for lab in labs:
        assert bond[lab] > 10 * vap[lab], \
            f"{lab}: bond {bond[lab]} is not more than ten times vaporization {vap[lab]}"
    strongest = max(bond, key=bond.get)
    hottest = max(bp, key=bp.get)
    assert strongest != hottest, \
        "'strongest bond also boils highest' must be false, but the same substance holds both"
    assert [bond[l] for l in labs] == sorted((bond[l] for l in labs), reverse=True), \
        "'bond enthalpies increase from HCl to HI' must be false, so the column must fall"
    assert max(bp.values()) < 0, "every boiling point should be below zero degrees Celsius"
    return (f"each internal bond {sorted(bond.values())} exceeds ten times its "
            f"vaporization {sorted(vap.values())}; strongest bond is {strongest} but "
            f"highest boiling point is {hottest}")


def q12(t, item):
    before = [r[1] for r in t["rows"]]
    after = [r[2] for r in t["rows"]]
    changed = [lab for lab, b, a in zip(hn.cg.labels(t), before, after) if b != a]
    assert changed == ["Synthesis of ammonia"], f"rows whose substances change: {changed}"
    de = dict(zip(hn.cg.labels(t), hn.cg.col(t, DE)))
    assert all(v != 0 for v in de.values()), "'every row has a nonzero change' is true, not a reason"
    assert de["Sublimation of dry ice"] < 30, "the dry-ice distractor's own arithmetic must hold"
    assert max(de, key=de.get) == "Boiling of ethanol", \
        "the ethanol distractor's own arithmetic must hold"
    return ("exactly one row, the ammonia synthesis, lists different substances before "
            "and after; the two energy-based distractors are arithmetically true and "
            "still do not identify a chemical process")


def q15(t, item):
    labs = hn.cg.labels(t)
    added = dict(zip(labs, hn.cg.col(t, ADDED)))
    back = dict(zip(labs, hn.cg.col(t, BACK)))
    lost = [lab for lab in labs if back[lab] < added[lab]]
    assert lost == ["3"], f"trials recovering less than was added: {lost}"
    assert all(back[lab] == added[lab] for lab in labs if lab != "3"), \
        "the sucrose and salt trials must return exactly what was added"
    return (f"trial 3 returns {back['3']} grams of the {added['3']} added while trials 1 "
            "and 2 return every gram, so only trial 3 shows the solid became something else")


def q16(t, item):
    labs = hn.cg.labels(t)
    start = dict(zip(labs, hn.cg.col(t, M0)))
    end = dict(zip(labs, hn.cg.col(t, M1)))
    assert all(start[l] == end[l] for l in labs), "both flasks should hold their mass"
    assert len(set(end.values())) == 1, "the two flasks should not be distinguishable by mass"
    return (f"both flasks read {sorted(start.values())} at the start and the same at the "
            "end, so the mass column separates them not at all")


def q25(t, item):
    v = dict(zip(hn.cg.labels(t), hn.cg.col(t, VAL)))
    sep = v["Energy to separate the ions from the crystal"]
    hyd = v["Energy released when the separated ions are hydrated"]
    net = v["Net energy change on dissolving the crystal in water"]
    assert abs(sep + hyd - net) < 1e-9, f"{sep} plus {hyd} is {sep + hyd}, not the stated net {net}"
    assert abs(net) < 0.01 * sep, "the net should be tiny beside the two steps it comes from"
    assert net > 0, "'releases far more than it absorbs' must be false on a positive net"
    return (f"{sep} plus {hyd} equals the tabulated net {net}, under one percent of the "
            "separation step, so the two steps very nearly cancel")


def q28(t, item):
    labs = hn.cg.labels(t)
    vap = dict(zip(labs, hn.cg.col(t, HVAP)))
    comb = dict(zip(labs, hn.cg.col(t, HCOMB)))
    ratios = {lab: abs(comb[lab]) / vap[lab] for lab in labs}
    assert all(r > 100 for r in ratios.values()), f"ratios are {ratios}"
    assert all(comb[lab] < 0 for lab in labs), "every combustion value should be negative"
    up_vap = [vap[l] for l in labs] == sorted(vap[l] for l in labs)
    up_comb = [abs(comb[l]) for l in labs] == sorted(abs(comb[l]) for l in labs)
    assert up_vap and up_comb, \
        "'the two columns trend in opposite directions' must be false, so both must rise"
    assert abs(comb["Heptane"]) > vap["Heptane"], \
        "'vaporizing heptane releases more than burning it' must be false"
    return (f"combustion over vaporization is {[round(r) for r in ratios.values()]}, every "
            "one above a hundred, and both columns rise together rather than opposing")


TABLE_CHECKS = {3: q3, 10: q10, 12: q12, 15: q15, 16: q16, 25: q25, 28: q28}

CLAIMS = [
 ("attractions between whole Br2 molecules",
  "EK 4.4.A.1: a process involving only changes in intermolecular interactions, such as a phase change, is typically classified as physical. Br2 is present before and after, so the Br-Br bond survives and only attractions between molecules were overcome."),
 ("within the reactant molecules are broken",
  "EK 4.4.A.1: processes involving the breaking and/or formation of chemical bonds are typically classified as chemical. Combustion breaks C-H and O=O bonds and forms C=O and O-H bonds, so the substances afterward are not those present before."),
 ("464 kilojoules per mole",
  "Recomputed in q3 above. EK 4.4.A.1 separates changes in intermolecular interactions from the breaking of chemical bonds, and the tabulated value for the bond inside the molecule is an order of magnitude above either phase-change value."),
 ("plausible argument can be made either way",
  "EK 4.4.A.2, near verbatim: plausible arguments could be made for the dissolution of a salt in water as either a physical or a chemical process, because it involves breaking of ionic bonds and the formation of ion-dipole interactions between ions and solvent."),
 ("London dispersion forces holding the I2 molecules",
  "EK 4.4.A.1 makes a process physical when only intermolecular interactions change. Intact I2 molecules are stated to be present in the solution, so the I-I bond was never broken."),
 ("bonds inside the molecules remain intact",
  "EK 4.4.A.1 names phase changes as involving only changes in intermolecular interactions. Sublimation leaves CO2 as CO2, so the C=O bonds survive and only the attractions holding molecules in the solid are overcome."),
 ("inside the water molecules were broken",
  "EK 4.4.A.1: chemical when chemical bonds are broken and/or formed. Water molecules do not survive electrolysis; O-H bonds are broken and the atoms are assembled into H2 and O2, which are different substances."),
 ("divided into smaller crystals",
  "EK 4.4.A.1 reserves the chemical classification for the breaking or forming of chemical bonds. Grinding produces smaller pieces of the same lattice, so no ionic bond is broken and the substance is unchanged."),
 ("a new O-H bond is formed on a water molecule",
  "EK 4.4.A.1 makes bond breaking and forming the criterion. Essentially no HCl molecules remain, so the H-Cl bond was broken and the proton now sits on a water molecule in a new O-H bond."),
 ("less than a tenth",
  "Recomputed in q10 above. EK 4.4.A.1 distinguishes intermolecular interactions from chemical bonds, and the tabulated vaporization enthalpies are under a tenth of the internal bond enthalpies of the same molecules."),
 ("stays intact",
  "EK 4.4.A.1 names phase changes as changes in intermolecular interactions only. Condensation re-forms attractions between whole molecules and releases energy, while every O-H bond inside a water molecule is untouched."),
 ("synthesis of ammonia",
  "Recomputed in q12 above. EK 4.4.A.1 makes different substances before and after the mark of a chemical process, and exactly one tabulated row shows that."),
 ("Liquid mercury freezing",
  "EK 4.4.A.1 offers phase changes as its example of processes involving only changes in intermolecular interactions. Each rejected option names a process producing a substance that was not present at the start."),
 ("color change alone is not sufficient",
  "EK 4.4.A.1 defines the categories by bond interactions, not by any single macroscopic observation. A colored species can appear because bonds formed or merely because a colored solute dissolved, so the observation does not settle the classification."),
 ("recovered mass is smaller than the mass added",
  "Recomputed in q15 above. EK 4.4.A.1 makes the survival of the original substance the test, and only the heated carbonate trial fails to return the mass it was given."),
 ("Nothing can be concluded from mass alone",
  "Recomputed in q16 above: both sealed flasks hold the same mass throughout. Atoms are conserved whether or not bonds break, so a mass reading is silent on the classification EK 4.4.A.1 asks for."),
 ("also breaks the ionic bonds of the lattice",
  "EK 4.4.A.1 makes the sucrose case physical because only intermolecular interactions change, and EK 4.4.A.2 makes the salt case arguable precisely because ionic bonds are broken and ion-dipole interactions with solvent are formed."),
 ("partial negative end of a polar water molecule",
  "EK 4.4.A.2 names the interaction formed between ions and solvent on dissolution as an ion-dipole interaction. A whole charge on the ion and a permanent dipole on the water molecule are exactly what that interaction requires."),
 ("only the burning is a chemical process",
  "EK 4.4.A.1 makes bond breaking the criterion. Evaporation leaves ethanol molecules intact in the vapor; combustion converts them to carbon dioxide and water, which requires bonds inside the molecules to be broken."),
 ("added mass and the different properties",
  "EK 4.4.A.1 makes the formation of chemical bonds a chemical process. Mass gained from the air together with properties unlike copper's identifies a new compound containing oxygen."),
 ("same mass and melting point",
  "EK 4.4.A.1 turns on whether the original substance survives. Recovering the same mass with the same characteristic properties shows the solute was unchanged; a different mass or melting point points to bonds broken or formed."),
 ("separates the ions from their fixed positions",
  "The substance is sodium chloride before and after; only the mobility of the ions changes, which is what makes the melt conduct. EK 4.4.A.1 classifies a phase change as physical."),
 ("new insoluble solid",
  "EK 4.4.A.1 makes the formation of chemical bonds a chemical process. Ions that were free in solution become bound together in an insoluble ionic solid, while the spectator ions remain in solution unchanged."),
 ("exceeded the energy released in forming ion-dipole",
  "EK 4.4.A.2 identifies the two energy terms in dissolving a salt: breaking ionic bonds costs energy and forming ion-dipole interactions with the solvent releases it. A net cooling means the first term is the larger."),
 ("nearly cancels the energy needed",
  "Recomputed in q25 above: the two tabulated steps of EK 4.4.A.2 sum to the tabulated net, which is under one percent of either, so a small net change is consistent with a great deal of bond breaking and forming."),
 ("typically classified as physical",
  "EK 4.4.A.1, near verbatim: processes that involve only changes in intermolecular interactions, such as phase changes, are typically classified as physical processes. The hedge is the framework's own and does not depend on the substance."),
 ("both substances survive unaltered",
  "EK 4.4.A.1 makes a process physical when only intermolecular interactions change. Both liquids are recovered with their original properties, so no bond within a pentane or hexane molecule was broken in either step."),
 ("more than a hundred times its vaporization",
  "Recomputed in q28 above. EK 4.4.A.1 separates intermolecular changes from bond breaking, and the tabulated combustion enthalpies exceed the vaporization enthalpies of the same alkanes by a factor above a hundred."),
 ("breaks ionic bonds while still being",
  "EK 4.4.A.2 states that sometimes physical processes involve the breaking of chemical bonds, and gives the dissolution of a salt in water as its example. None of the rejected processes is treated as physical by the framework."),
 ("re-formed when the gases cool",
  "EK 4.4.A.1 classifies by whether chemical bonds are broken or formed, not by whether the starting material reappears. NH3 and HCl detected in the hot region show the bond holding the proton to chloride was broken, and re-forming it on cooling is a second bond-forming step."),
]


def _wreck_table(mod, cl):
    """Module-specific control: make trial 3 return every gram it was given."""
    t = mod.QUESTIONS[14]["table"]
    mod.QUESTIONS[14]["table"] = dict(
        headers=t["headers"],
        rows=[list(r[:3]) + ["10.0"] if r[0] == "3" else list(r) for r in t["rows"]])


def _wreck_lattice(mod, cl):
    """Module-specific control: break the sum that q25's key rests on."""
    t = mod.QUESTIONS[24]["table"]
    mod.QUESTIONS[24]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "-600"] if r[0].startswith("Energy released") else list(r)
              for r in t["rows"]])


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS,
                extra=[("a recovered-mass cell corrupted", _wreck_table),
                       ("a hydration-energy cell corrupted", _wreck_lattice)])

hn.audit(M, CLAIMS, TABLE_CHECKS)
