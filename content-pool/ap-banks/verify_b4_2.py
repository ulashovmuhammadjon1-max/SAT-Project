"""Key audit for AP BIOLOGY 4.2 Introduction to Signal Transduction.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the shuffle ``export_units.py`` applies on export.

WHAT THE KEYS REST ON
---------------------
  4.2.A.1      pathways LINK SIGNAL RECEPTIONS WITH CELLULAR RESPONSES
  4.2.A.2      many pathways include PROTEIN MODIFICATIONS and PHOSPHORYLATION
               CASCADES
  4.2.B.1      signaling begins with recognition of a chemical messenger, a
               LIGAND, by a RECEPTOR PROTEIN in a TARGET CELL
  4.2.B.1.i    the LIGAND-BINDING DOMAIN recognizes a SPECIFIC messenger, a
               PEPTIDE (PROTEIN) or a SMALL MOLECULE
  4.2.B.1.ii   G PROTEIN-COUPLED RECEPTORS are the CED's named eukaryotic
               example of a receptor protein
  4.2.B.1.iii  receptors may be ON THE SURFACE or IN THE CYTOPLASM OR NUCLEUS
  4.2.B.2      cascades RELAY signals from receptors to cell targets, OFTEN
               AMPLIFYING them; responses could include CELL GROWTH, SECRETION
               OF MOLECULES, or GENE EXPRESSION
  4.2.B.2.i    after binding, the INTRACELLULAR DOMAIN CHANGES SHAPE
  4.2.B.2.ii   ENZYMES and SECOND MESSENGERS such as CYCLIC AMP relay and
               amplify the intracellular signal
  4.2.B.2.iii  HORMONES travel LONG DISTANCES IN THE BLOODSTREAM
  4.2.B.2.iv   ligand binding OPENS OR CLOSES a LIGAND-GATED CHANNEL

BOUNDARY WITH 4.1 AND 4.3. Topic 4.1 owns the mode and distance of
communication and no key here rests on that distinction -- items 12 and 25 are
keyed to EK 4.2.B.2.iii's placement of hormones INSIDE a transduction pathway,
not to their range. Topic 4.3 owns what a pathway's output does to the cell and
what mutations or chemicals do to a pathway, so this module carries no mutation
item and no inhibitor item at all. The topic's suggested skill is 1.A,
DESCRIBE, and the module is written to it.

Items 15, 16, 17 and 18 carry tables. Every number is HYPOTHETICAL and the stem
says so; each keyed conclusion is recomputed below from the table alone, and
the distractors are shown false against the same numbers. No stem refers to a
figure.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b4_2

AMPLIFY = b4_2._T_AMPLIFY
BINDING = b4_2._T_BINDING
LOCATION = b4_2._T_LOCATION
CHANNEL = b4_2._T_CHANNEL

H_COUNT = "Activated molecules present at that stage (hypothetical)"
H_P = "Sites occupied by ligand P (hypothetical, percent)"
H_Q = "Sites occupied by ligand Q (hypothetical, percent)"
H_M = "Receptor for messenger M detected (hypothetical, units)"
H_N = "Receptor for messenger N detected (hypothetical, units)"
H_LIG = "Ligand supplied (hypothetical, micromolar)"
H_FLOW = "Ion flow through the channel (hypothetical, arbitrary units)"

BOUND = 50   # percent of sites; the table leaves a wide gap either side
PRESENT = 30  # units; likewise


def q15(table, item):
    labs = cg.labels(table)
    n = cg.col(table, H_COUNT)
    assert all(b >= a for a, b in zip(n, n[1:])), f"the counts must never fall: {n}"
    assert n[-1] >= 1000 * n[0], f"the cascade must amplify substantially: {n[0]} to {n[-1]}"
    assert n.index(max(n)) == len(n) - 1, "the largest count must be at the last stage, not at ligand binding"
    assert len(set(n)) > 1, "'the same at every stage' must be false"
    ligand_stage = [i for i, lab in enumerate(labs) if "ligand" in lab.lower()]
    assert ligand_stage and n[ligand_stage[0]] == min(n), \
        "'the largest number is where ligand binds' must be false"
    return (f"activated molecules run {n} from ligand binding to the last stage, a "
            f"{n[-1] / n[0]:.0f}-fold increase along the cascade")


def q16(table, item):
    labs = cg.labels(table)
    p = dict(zip(labs, cg.col(table, H_P)))
    q = dict(zip(labs, cg.col(table, H_Q)))
    for k in labs:
        assert not (p[k] >= BOUND and q[k] >= BOUND), f"{k} must not bind both messengers"
        for v in (p[k], q[k]):
            assert v >= BOUND or v <= BOUND / 5, f"{k} must bind clearly or not at all, not marginally"
    binds_p = [k for k in labs if p[k] >= BOUND]
    binds_q = [k for k in labs if q[k] >= BOUND]
    assert len(binds_p) == 1 and len(binds_q) == 1 and binds_p != binds_q, \
        f"each messenger must have exactly one distinct partner; got P {binds_p}, Q {binds_q}"
    neither = [k for k in labs if p[k] < BOUND and q[k] < BOUND]
    assert neither, "'every receptor recognizes every messenger' must be false"
    assert len({(p[k], q[k]) for k in labs}) == len(labs), "'the receptors are interchangeable' must be false"
    return (f"ligand P is bound only by {binds_p[0]} and ligand Q only by {binds_q[0]}, while "
            f"{neither[0]} binds neither above {BOUND} percent")


def q17(table, item):
    labs = cg.labels(table)
    m = dict(zip(labs, cg.col(table, H_M)))
    n = dict(zip(labs, cg.col(table, H_N)))
    surface = [k for k in labs if "membrane" in k.lower()]
    assert len(surface) == 1, f"exactly one fraction must be the cell surface; got {labs}"
    s = surface[0]
    inside = [k for k in labs if k != s]
    assert m[s] >= PRESENT and all(m[k] < PRESENT for k in inside), \
        f"messenger M's receptor must sit at the surface and nowhere else: {m}"
    assert n[s] < PRESENT and any(n[k] >= PRESENT for k in inside), \
        f"messenger N's receptor must sit inside the cell and not at the surface: {n}"
    return (f"the receptor for M reads {m[s]:.0f} at the plasma membrane against "
            f"{[m[k] for k in inside]} inside, while the receptor for N reads {n[s]:.0f} at the "
            f"membrane against {[n[k] for k in inside]} inside")


def q18(table, item):
    lig = cg.col(table, H_LIG)
    flow = cg.col(table, H_FLOW)
    assert all(b > a for a, b in zip(lig, lig[1:])), f"ligand supplied must increase down the table: {lig}"
    assert all(b > a for a, b in zip(flow, flow[1:])), f"ion flow must rise with ligand: {flow}"
    assert lig[0] == 0, "the first row must supply no ligand"
    assert flow[0] == min(flow), "'flow is greatest with no ligand' must be false"
    assert flow[-1] >= 10 * flow[0], f"the rise must be substantial: {flow[0]} to {flow[-1]}"
    return (f"ion flow rises {flow} as ligand supplied rises {lig}, a {flow[-1] / flow[0]:.0f}-fold "
            f"increase from the no-ligand condition")


CLAIMS = [
 ("links the reception of a signal to a cellular response",
  "EK 4.2.A.1 states that signal transduction pathways link signal receptions with cellular responses. Reception at one end and response at the other are what the pathway connects."),
 ("including phosphorylation cascades",
  "EK 4.2.A.2 states that many signal transduction pathways include protein modifications and involve phosphorylation cascades."),
 ("A ligand",
  "EK 4.2.B.1 states that signaling begins with the recognition of a chemical messenger, a ligand, by a receptor protein in a target cell. A second messenger acts later and inside the cell, under EK 4.2.B.2.ii."),
 ("ligand-binding domain, which recognizes a specific",
  "EK 4.2.B.1.i states that the ligand-binding domain of a receptor recognizes a specific chemical messenger. The intracellular domain acts later, changing shape after binding, under EK 4.2.B.2.i."),
 ("A peptide, meaning a protein, or a small molecule",
  "EK 4.2.B.1.i states that the specific chemical messenger a ligand-binding domain recognizes can be a peptide, glossed in the framework as a protein, or a small molecule."),
 ("G protein-coupled receptors",
  "EK 4.2.B.1.ii names G protein-coupled receptors as an example of a receptor protein in eukaryotes. The other structures listed are introduced elsewhere in the framework for other purposes."),
 ("On the cell surface, or in the cytoplasm or nucleus",
  "EK 4.2.B.1.iii states that receptors may be located on the surface of a target cell or in the cytoplasm or nucleus of the target cell. All three locations are named in that one sentence."),
 ("relay the signal onward and often amplify it",
  "EK 4.2.B.2 states that signaling cascades relay signals from receptors to cell targets, often amplifying the incoming signals, resulting in the appropriate responses by the cell."),
 ("secretion of molecules, or gene expression",
  "EK 4.2.B.2 states that responses could include cell growth, secretion of molecules, or gene expression, naming all three together."),
 ("changes shape, initiating transduction",
  "EK 4.2.B.2.i states that after the ligand binds, the intracellular domain of a receptor protein changes shape, initiating transduction of the signal."),
 ("relay and amplify the intracellular signal",
  "EK 4.2.B.2.ii states that enzymes and second messengers such as cyclic AMP relay and amplify the intracellular signal. Both jobs are named in that sentence."),
 ("travel long distances in the bloodstream",
  "EK 4.2.B.2.iii states that hormones are an example of a signaling messenger that can travel long distances in the bloodstream. Second messengers, receptors, enzymes and channels are separate components in the same statements."),
 ("caused to open or to close",
  "EK 4.2.B.2.iv states that the binding of ligands to ligand-gated channels can cause the channel to open or close. Both directions are part of the statement."),
 ("much larger number of activated molecules inside the cell",
  "EK 4.2.B.2 states that cascades often amplify the incoming signals, and EK 4.2.B.2.ii assigns that amplification to enzymes and second messengers acting inside the cell rather than to any change in the signal molecule itself."),
 ("grows at successive stages, so the signal is amplified",
  "Recomputed in q15 above. EK 4.2.B.2 states that cascades often amplify the incoming signals and EK 4.2.B.2.ii names what does the amplifying; a rising count from stage to stage is that statement as data."),
 ("recognizes a specific messenger rather than any messenger",
  "Recomputed in q16 above. EK 4.2.B.1.i states that the ligand-binding domain of a receptor recognizes a SPECIFIC chemical messenger, and each receptor in the table binds at most one of the two offered."),
 ("found at the cell surface and the other's inside the cell",
  "Recomputed in q17 above. EK 4.2.B.1.iii states that receptors may be located on the surface of a target cell or in the cytoplasm or nucleus, so both distributions in the table are ones the framework allows."),
 ("rises as ligand is supplied, so binding of the ligand opens",
  "Recomputed in q18 above. EK 4.2.B.2.iv states that the binding of ligands to ligand-gated channels can cause the channel to open or close, and rising flow with rising ligand is the opening case."),
 ("receptors may be located in the nucleus of a target cell",
  "EK 4.2.B.1.iii states that receptors may be located on the surface of a target cell or in the cytoplasm or nucleus of the target cell, so a nuclear location is one of the three the framework names."),
 ("released molecule is the ligand and the recognizing protein is the receptor",
  "EK 4.2.B.1 states that signaling begins with the recognition of a chemical messenger, a ligand, by a receptor protein in a target cell, which assigns each name to one of the two molecules."),
 ("recognized by a receptor, a cascade relays the signal, and the cell responds",
  "EK 4.2.B.1 places recognition of the ligand by the receptor first, EK 4.2.B.2 puts the relaying cascade between receptor and cell target, and EK 4.2.A.1 makes linking reception to response the pathway's function."),
 ("has a receptor whose binding domain recognizes that messenger",
  "EK 4.2.B.1 makes signaling begin with recognition by a receptor protein in a TARGET cell, and EK 4.2.B.1.i makes the ligand-binding domain recognize a specific messenger. A cell without the matching receptor is not a target."),
 ("carrying and enlarging the signal it has started",
  "EK 4.2.B.2.i puts the shape change of the receptor's intracellular domain at the start of transduction, and EK 4.2.B.2.ii has enzymes and second messengers such as cyclic AMP relay and amplify the intracellular signal that follows."),
 ("passes the signal to the next",
  "EK 4.2.B.2 states that signaling cascades relay signals from receptors to cell targets, resulting in the appropriate responses by the cell. Relaying is passing the signal along that route."),
 ("A hormone",
  "EK 4.2.B.2.iii states that hormones are an example of a signaling messenger that can travel long distances in the bloodstream. The other four terms name components acting at or inside the target cell."),
 ("allows a ligand to be a peptide as well as a small molecule",
  "EK 4.2.B.1.i states that the specific chemical messenger recognized by a ligand-binding domain can be a peptide, glossed in the framework as a protein, or a small molecule."),
 ("A G protein-coupled receptor",
  "EK 4.2.B.1.ii names G protein-coupled receptors as an example of a receptor protein in eukaryotes, and EK 4.2.B.1 makes the receptor the component that recognizes the external messenger."),
 ("Gene expression",
  "EK 4.2.B.2 lists cell growth, secretion of molecules and gene expression as possible responses. Beginning to make a protein not previously made is the third of those; recognition and relay are earlier steps rather than responses."),
 ("located in the plasma membrane of its target cell",
  "EK 4.2.B.1.iii allows receptors on the surface or in the cytoplasm or nucleus, so a plasma membrane location is not universal. The other four options restate EK 4.2.B.1.i, EK 4.2.B.2, EK 4.2.B.2.ii and EK 4.2.B.2.iv."),
 ("relaying and amplifying cascade, and a cellular response",
  "EK 4.2.B.1 gives the messenger and the receptor, EK 4.2.B.2 gives the relaying and often amplifying cascade and the response, and EK 4.2.A.1 states that the pathway links reception to response."),
]

cg.check(b4_2, CLAIMS, table_checks={15: q15, 16: q16, 17: q17, 18: q18})
