"""Key audit for AP BIOLOGY 3.5 Cellular Respiration.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the shuffle ``export_units.py`` applies on export.

WHAT THE KEYS REST ON
---------------------
Every key traces to an essential knowledge statement of topic 3.5, listed at
the head of ``b3_5.py`` and cited by code in the claims below. The three most
often stated backwards, and therefore the three the distractors deliberately
offer in reverse, are:

  3.5.A.3.ii  the gradient runs HIGH OUTSIDE the inner mitochondrial membrane
              and LOW INSIDE it -- the OPPOSITE sense to the thylakoid gradient
              of EK 3.4.B.4
  3.5.B.5     the pH inside the MATRIX is HIGHER than in the intermembrane
              space, which is the same fact stated in pH terms
  3.5.B.2     pyruvate travels FROM THE CYTOSOL TO THE MITOCHONDRION, not the
              other way

EXCLUSION STATEMENTS OBSERVED. The CED puts beyond scope memorization of the
steps of glycolysis and the Krebs cycle, the structures of the molecules and
the names of the enzymes involved, the full names of the specific electron
carriers, and the specific steps and intermediates of these pathways. No item
asks for any of them. ATP synthase is named because EK 3.5.A.3.iii names it and
the parallel exclusion statement in topic 3.4 exempts it explicitly.

BOUNDARY WITH 3.4. Both topics carry an electron transport chain, a proton
gradient, ATP synthase and chemiosmosis. Every item here is
mitochondrion-specific: the reversed gradient, OXIDATIVE phosphorylation,
oxygen as terminal acceptor, glycolysis, pyruvate, the Krebs cycle, the matrix,
the folding of the inner membrane, decoupling to heat, and fermentation. Item
10 is about the FOLDING named in EK 3.5.A.3.ii, not about compartmentalization,
which is topic 2.9.

NO FIGURES. The topic's suggested skill is 4.A, construct a graph; the bank
cannot carry one, so items 21 to 25 carry tables and ask the skill 4.B question
of them instead. Every number is HYPOTHETICAL and the stem says so, each keyed
conclusion is recomputed below from the table alone, and the distractors are
shown false against the same numbers.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b3_5

MITO = b3_5._T_MITO
YEAST = b3_5._T_YEAST
PH = b3_5._T_PH

H_O2 = "Oxygen consumed (hypothetical, micromoles per minute)"
H_ATP = "ATP formed (hypothetical, micromoles per minute)"
H_GLU = "Glucose consumed (hypothetical, millimoles)"
H_CO2 = "Carbon dioxide released (hypothetical, millimoles)"
H_ETOH = "Ethanol produced (hypothetical, millimoles)"
H_RUN = "pH while electron transport is running (hypothetical)"
H_BLOCK = "pH after electron transport is blocked (hypothetical)"


def _mito(table):
    labs = cg.labels(table)
    o2 = dict(zip(labs, cg.col(table, H_O2)))
    atp = dict(zip(labs, cg.col(table, H_ATP)))
    base = [k for k in labs if "no addition" in k.lower()]
    assert len(base) == 1, f"exactly one untreated row is required; got {base}"
    b = base[0]
    agents = [k for k in labs if k != b]
    assert len(agents) == 2, f"exactly two agents are required; got {agents}"
    blocker = [k for k in agents if o2[k] < o2[b] and atp[k] < atp[b]]
    uncoupler = [k for k in agents if o2[k] > o2[b] and atp[k] < atp[b]]
    assert len(blocker) == 1, f"exactly one agent may lower both measures; got {blocker}"
    assert len(uncoupler) == 1, f"exactly one agent may raise oxygen use while ATP falls; got {uncoupler}"
    assert blocker[0] != uncoupler[0], "the two agents must be different rows"
    assert atp[b] == max(atp.values()), "the untreated row must show the highest ATP formation"
    return b, blocker[0], uncoupler[0], o2, atp


def q21(table, item):
    b, blocker, uncoupler, o2, atp = _mito(table)
    assert o2[blocker] <= 0.2 * o2[b], \
        f"the blocker must nearly stop oxygen consumption: {o2[blocker]} against {o2[b]}"
    assert atp[blocker] <= 0.2 * atp[b], "the blocker must nearly stop ATP formation"
    assert o2[uncoupler] > o2[b], "'oxygen consumption occurs under every condition' must not describe both agents alike"
    return (f"{blocker} drops oxygen use from {o2[b]:.0f} to {o2[blocker]:.0f} and ATP from "
            f"{atp[b]:.0f} to {atp[blocker]:.0f}, while {uncoupler} raises oxygen use to {o2[uncoupler]:.0f}")


def q22(table, item):
    b, blocker, uncoupler, o2, atp = _mito(table)
    assert atp[uncoupler] <= 0.2 * atp[b], \
        f"ATP must collapse under the uncoupler: {atp[uncoupler]} against {atp[b]}"
    assert o2[uncoupler] >= 1.2 * o2[b], \
        f"electron transport must be running faster, not slower: {o2[uncoupler]} against {o2[b]}"
    return (f"{uncoupler} raises oxygen consumption from {o2[b]:.0f} to {o2[uncoupler]:.0f} while ATP "
            f"falls from {atp[b]:.0f} to {atp[uncoupler]:.0f}, which is transport running without ATP formation")


def _yeast(table):
    labs = cg.labels(table)
    glu = dict(zip(labs, cg.col(table, H_GLU)))
    co2 = dict(zip(labs, cg.col(table, H_CO2)))
    etoh = dict(zip(labs, cg.col(table, H_ETOH)))
    with_o2 = [k for k in labs if "no oxygen" not in k.lower()]
    without = [k for k in labs if "no oxygen" in k.lower()]
    assert len(with_o2) == 1 and len(without) == 1, f"one aerated and one anaerobic culture required; got {labs}"
    return with_o2[0], without[0], glu, co2, etoh


def q23(table, item):
    a, n, glu, co2, etoh = _yeast(table)
    assert etoh[n] > 0 and etoh[a] == 0, \
        f"ethanol must appear only without oxygen: {etoh}"
    assert glu[a] == glu[n], "the two cultures must consume equal glucose, or the comparison is confounded"
    assert co2[a] > co2[n], "'the aerated culture releases the most carbon dioxide' must be a true premise"
    return (f"both cultures consume {glu[a]:.0f} millimoles of glucose, but ethanol appears only in the "
            f"culture with no oxygen ({etoh[n]:.0f} against {etoh[a]:.0f})")


def q24(table, item):
    a, n, glu, co2, etoh = _yeast(table)
    assert glu[a] == glu[n], "glucose consumption must be equal for a per-glucose comparison"
    assert co2[a] >= 3 * co2[n], \
        f"the aerated culture must release far more carbon dioxide: {co2[a]} against {co2[n]}"
    assert co2[n] > 0, "the anaerobic culture must still release some carbon dioxide"
    assert etoh[a] == 0, "the aerated culture must produce no ethanol"
    return (f"from equal glucose of {glu[a]:.0f} millimoles, the aerated culture releases {co2[a]:.0f} "
            f"millimoles of carbon dioxide against {co2[n]:.0f} without oxygen, a "
            f"{co2[a] / co2[n]:.0f}-fold difference")


def q25(table, item):
    labs = cg.labels(table)
    run = dict(zip(labs, cg.col(table, H_RUN)))
    blocked = dict(zip(labs, cg.col(table, H_BLOCK)))
    mat = [k for k in labs if "matrix" in k.lower()]
    ims = [k for k in labs if "intermembrane" in k.lower()]
    assert len(mat) == 1 and len(ims) == 1, f"one matrix and one intermembrane row required; got {labs}"
    m, i = mat[0], ims[0]
    assert run[m] > run[i], f"while running, the matrix pH must exceed the intermembrane pH: {run}"
    assert blocked[m] == blocked[i], f"blocking transport must abolish the difference: {blocked}"
    assert abs(run[m] - run[i]) > abs(blocked[m] - blocked[i]), \
        "'blocking makes the difference larger' must be false"
    return (f"while transport runs the matrix sits at pH {run[m]} against {run[i]} in the intermembrane "
            f"space; blocked, both read {blocked[m]}, so the difference depends on transport")


CLAIMS = [
 ("energy from biological macromolecules to synthesize ATP",
  "EK 3.5.A.1 states that cellular respiration uses energy from biological macromolecules to synthesize ATP. The reverse direction and the light-driven synthesis belong to other processes in the framework."),
 ("characteristic of all forms of life",
  "EK 3.5.A.1 states that respiration and fermentation are characteristic of all forms of life, the same kind of universality EK 3.3.B.1 records for conserved core metabolic pathways."),
 ("coordinated enzyme-catalyzed reactions",
  "EK 3.5.A.2 states that aerobic cellular respiration in eukaryotes involves a series of coordinated enzyme-catalyzed reactions that capture energy from biological macromolecules, which is also why EK 3.3.A.3 calls energy pathways sequential."),
 ("oxidation and reduction reactions that establish an electrochemical gradient",
  "EK 3.5.A.3 states that the ETC transfers electrons in a series of oxidation-reduction reactions that establish an electrochemical gradient across membranes."),
 ("Oxygen",
  "EK 3.5.A.3.i states that electrons delivered by NADH and FADH2 are passed to a series of electron acceptors as they move toward the terminal electron acceptor, oxygen."),
 ("molecules other than oxygen as the terminal electron acceptor",
  "EK 3.5.A.3.i states that aerobic prokaryotes use oxygen as a terminal electron acceptor while anaerobic prokaryotes use other molecules. What they lack is oxygen at the end of the chain, not the chain."),
 ("NADH and FADH2",
  "EK 3.5.A.3.i and EK 3.5.B.4 both name NADH and FADH2 as the carriers delivering electrons extracted in glycolysis and the Krebs cycle to the electron transport chain. NADPH belongs to photosynthesis under EK 3.4.B.1."),
 ("Outside the inner mitochondrial membrane",
  "EK 3.5.A.3.ii states that the membrane separates a region of high proton concentration outside the membrane from a region of low proton concentration inside it, the opposite sense to the thylakoid gradient of EK 3.4.B.4."),
 ("matrix is higher than the pH in the intermembrane space",
  "EK 3.5.B.5 states that the pH inside the mitochondrial matrix is higher than in the intermembrane space, which is EK 3.5.A.3.ii's gradient restated, since a higher proton concentration means a lower pH."),
 ("increased surface area allows more ATP",
  "EK 3.5.A.3.ii states that the folding of the inner membrane increases the surface area, which allows for more ATP to be synthesized, tying the structural feature directly to the yield."),
 ("The plasma membrane",
  "EK 3.5.A.3.ii states that in prokaryotes the passage of electrons is accompanied by the movement of protons across the plasma membrane. EK 2.10.A.2 denies prokaryotes the internal membrane-bound organelles the other options name."),
 ("Oxidative phosphorylation",
  "EK 3.5.A.3.iii states that the flow of protons back through membrane-bound ATP synthase by chemiosmosis drives ATP formation from ADP and inorganic phosphate, and names this oxidative phosphorylation in aerobic cellular respiration."),
 ("endothermic organisms can use it to regulate body temperature",
  "EK 3.5.A.3.iv states that decoupling oxidative phosphorylation from electron transport generates heat, and that this heat can be used by endothermic organisms to regulate body temperature."),
 ("ATP, NADH, and pyruvate",
  "EK 3.5.B.1 states that glycolysis releases the energy in glucose molecules to form ATP from ADP and inorganic phosphate, NADH from NAD+, and pyruvate."),
 ("from the cytosol to the mitochondrion",
  "EK 3.5.B.2 states that pyruvate is transported from the cytosol to the mitochondrion where oxidation occurs. That transport is what places glycolysis outside the organelle and the Krebs cycle inside it."),
 ("The matrix",
  "EK 3.5.B.3 states that the Krebs cycle takes place in the mitochondrial matrix. EK 3.5.B.4 places the electron transport chain in the inner membrane instead."),
 ("Carbon dioxide",
  "EK 3.5.B.2 and EK 3.5.B.3 both state that carbon dioxide is released during the Krebs cycle. Oxygen is consumed as the terminal electron acceptor under EK 3.5.A.3.i rather than released."),
 ("NAD+ is reduced to NADH and FAD is reduced to FADH2",
  "EK 3.5.B.2 states that the Krebs cycle releases electrons, reducing NAD+ to NADH and FAD to FADH2. Those reduced carriers then deliver the electrons to the chain under EK 3.5.B.4."),
 ("chain in the inner mitochondrial membrane",
  "EK 3.5.B.4 states that electrons extracted in glycolysis and Krebs cycle reactions are transferred by NADH and FADH2 to the electron transport chain in the inner mitochondrial membrane."),
 ("without oxygen and produces organic molecules such as alcohol and lactic acid",
  "EK 3.5.B.6 states that fermentation allows glycolysis to proceed in the absence of oxygen and produces organic molecules such as alcohol and lactic acid."),
 ("lowers both oxygen consumption and ATP formation",
  "Recomputed in q21 above. EK 3.5.A.3.i makes oxygen the terminal acceptor, so a block on the chain stops oxygen being consumed, and EK 3.5.A.3.iii makes ATP formation depend on the gradient the chain builds."),
 ("collapses, and heat is produced instead",
  "Recomputed in q22 above. EK 3.5.A.3.iv states that decoupling oxidative phosphorylation from electron transport generates heat, and the data signature is transport continuing while ATP formation collapses."),
 ("without oxygen, because it is the one producing ethanol",
  "Recomputed in q23 above. EK 3.5.B.6 states that fermentation allows glycolysis to proceed in the absence of oxygen and produces organic molecules such as alcohol, and ethanol appears only in the anaerobic culture."),
 ("Krebs cycle, which releases carbon dioxide from organic intermediates",
  "Recomputed in q24 above. EK 3.5.B.2 and EK 3.5.B.3 place the release of carbon dioxide in the Krebs cycle, EK 3.5.B.6 limits the oxygen-free culture to glycolysis, and EK 3.5.B.1 makes the product of glycolysis pyruvate rather than carbon dioxide."),
 ("matrix is less acidic than the intermembrane space",
  "Recomputed in q25 above. EK 3.5.B.5 states that the pH inside the mitochondrial matrix is higher than in the intermembrane space, and EK 3.5.A.3.ii makes electron transport the cause of the gradient."),
 ("The cytosol",
  "EK 3.5.B.2 states that pyruvate is transported from the cytosol to the mitochondrion, placing the pathway that makes pyruvate outside the organelle. EK 3.5.B.3 puts the Krebs cycle in the matrix and EK 3.5.B.4 the chain in the inner membrane."),
 ("supported by fermentation",
  "EK 3.5.B.6 states that fermentation allows glycolysis to proceed in the absence of oxygen and produces organic molecules such as lactic acid, and EK 3.5.A.3.i makes oxygen the terminal acceptor the chain requires."),
 ("appears as heat and less as ATP",
  "EK 3.5.A.3.iv states that decoupling oxidative phosphorylation from electron transport generates heat and that endothermic organisms can use it to regulate body temperature, so more decoupling sends more of the same electron flow to heat."),
 ("higher inside the inner mitochondrial membrane than outside it",
  "EK 3.5.A.3.ii states the gradient in the opposite sense, high outside the membrane and low inside, and EK 3.5.B.5 says the same in pH terms. The other four options restate EK 3.5.B.3, EK 3.5.A.3.i, EK 3.5.B.6 and EK 3.5.B.4."),
 ("carriers deliver to the chain, which builds the gradient",
  "EK 3.5.B.4 states that electrons extracted in glycolysis and Krebs cycle reactions are transferred by NADH and FADH2 to the chain, EK 3.5.A.3.ii makes the chain build the gradient, and EK 3.5.A.3.iii makes proton return through ATP synthase form the ATP."),
]

cg.check(b3_5, CLAIMS, table_checks={21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
