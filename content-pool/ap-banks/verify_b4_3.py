"""Key audit for AP BIOLOGY 4.3 Signal Transduction Pathways.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the shuffle ``export_units.py`` applies on export.

WHAT THE KEYS REST ON
---------------------
  4.3.A.1  signal transduction may result in CHANGES IN GENE EXPRESSIONS AND
           CELL FUNCTION, which may ALTER PHENOTYPE or result in PROGRAMMED
           CELL DEATH (APOPTOSIS)
  4.3.B.1  MUTATIONS IN ANY DOMAIN of the receptor protein OR IN ANY COMPONENT
           of the pathway may affect the DOWNSTREAM components by altering the
           subsequent transduction of the signal
  4.3.B.2  CHEMICALS interacting with ANY COMPONENT may ACTIVATE OR INHIBIT the
           pathway

Six items name one of the CED's own illustrative examples, and each of those
keys is a classification of the example under one of the three statements
above, never a mechanism the CED does not print for it:

  under EK 4.3.A.1  quorum sensing -- chemical messengers used by microbes to
                    regulate specific pathways in response to population
                    density; epinephrine stimulation of glycogen breakdown
  under EK 4.3.B.1  cytokines regulating gene expression for cell replication
                    and division; yeast mating pheromones triggering mating
                    gene expression; ethylene changing enzyme production and
                    allowing fruit to ripen; HOX genes regulating animal body
                    plans

QUORUM SENSING IS ASKED TWICE ACROSS THE BANK, ON PURPOSE AND DIFFERENTLY. The
CED lists it under EK 4.1.B.1 as short-distance communication by a local
regulator and again under EK 4.3.A.1 as regulation of specific pathways in
response to population density. Module b4_1 item 7 asks how far the signal
travels; item 8 here asks what the pathway's output regulates. Neither key
answers the other question.

BOUNDARY WITH 4.2. The components themselves -- ligand, binding domain, G
protein-coupled receptors, receptor location, intracellular domain, second
messengers, amplification, ligand-gated channels -- are essential knowledge of
4.2 and no key here merely names one. This module is about what a pathway
produces and what happens when it is changed, which is what skill 6.C asks a
student to reason about.

Items 13 to 17 carry tables. Every number is HYPOTHETICAL and the stem says so;
each keyed conclusion is recomputed below from the table alone, and the
distractors are shown false against the same numbers. No stem refers to a
figure.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b4_3

LINES = b4_3._T_LINES
DRUG = b4_3._T_DRUG
EXPRESSION = b4_3._T_EXPRESSION
APOPTOSIS = b4_3._T_APOPTOSIS

STEPS = ["Ligand bound by the receptor (percent of normal)",
         "Relay component activated (percent of normal)",
         "Final response measured (percent of normal)"]
H_LIG = "Ligand supplied (1 means yes, 0 means no)"
H_RESP = "Response measured (hypothetical, arbitrary units)"
H_OFF = "Expression without the signal (hypothetical, arbitrary units)"
H_ON = "Expression with the signal (hypothetical, arbitrary units)"
H_ALIVE = "Cells still alive after two days (hypothetical, percent)"
H_DEAD = "Cells that underwent programmed cell death (hypothetical, percent)"

FAILED = 50   # percent of normal; the table leaves a wide gap either side
INTACT = 80


def _lines(table):
    """For each mutant, the index of the first step that has failed.

    Requires the clean shape the keyed readings assume: every step before the
    first failure is intact and every step from it onward has failed, which is
    what EK 4.3.B.1's "affect the DOWNSTREAM components" predicts.
    """
    labs = cg.labels(table)
    grid = {lab: [cg.cell(table, lab, h) for h in STEPS] for lab in labs}
    normal = [lab for lab in labs if "normal" in lab.lower()]
    assert len(normal) == 1, f"exactly one normal control row is required; got {labs}"
    n = normal[0]
    assert all(v >= INTACT for v in grid[n]), f"the control must be intact at every step: {grid[n]}"
    firsts = {}
    for lab in labs:
        if lab == n:
            continue
        row = grid[lab]
        failed = [i for i, v in enumerate(row) if v <= FAILED]
        assert failed, f"{lab} must fail somewhere; got {row}"
        first = failed[0]
        assert failed == list(range(first, len(row))), \
            f"{lab} must fail from its first failure onward, not intermittently: {row}"
        assert all(row[i] >= INTACT for i in range(first)), \
            f"{lab} must be intact at every step before its first failure: {row}"
        firsts[lab] = first
    assert len(set(firsts.values())) == len(firsts), \
        f"each mutant must break at a different step; got {firsts}"
    return n, grid, firsts


def q13(table, item):
    n, grid, firsts = _lines(table)
    at_receptor = [k for k, i in firsts.items() if i == 0]
    assert len(at_receptor) == 1, f"exactly one line may fail at ligand binding; got {at_receptor}"
    k = at_receptor[0]
    assert all(v <= FAILED for v in grid[k]), "a binding failure must carry through every later step"
    return (f"{k} reads {grid[k]} against the control's {grid[n]}, failing at the binding step and "
            f"at everything after it, while the other lines bind normally")


def q14(table, item):
    n, grid, firsts = _lines(table)
    last = len(STEPS) - 1
    downstream = [k for k, i in firsts.items() if i == last]
    assert len(downstream) == 1, f"exactly one line may fail only at the last step; got {downstream}"
    k = downstream[0]
    assert grid[k][0] >= INTACT and grid[k][1] >= INTACT, \
        "the downstream mutant must bind and relay normally"
    assert grid[k][last] <= FAILED, "the downstream mutant's response must have failed"
    return (f"{k} reads {grid[k]}: binding and relay are within {INTACT} percent of normal while the "
            f"response has fallen to {grid[k][last]:.0f} percent")


def q15(table, item):
    labs = cg.labels(table)
    lig = dict(zip(labs, cg.col(table, H_LIG)))
    resp = dict(zip(labs, cg.col(table, H_RESP)))
    base_off = [k for k in labs if "no drug" in k.lower() and lig[k] == 0]
    base_on = [k for k in labs if "no drug" in k.lower() and lig[k] == 1]
    assert len(base_off) == 1 and len(base_on) == 1, f"two untreated controls are required; got {labs}"
    off, on = base_off[0], base_on[0]
    assert resp[on] >= 10 * resp[off], \
        f"the messenger must produce a clear response without any drug: {resp[off]} to {resp[on]}"
    drugged = [k for k in labs if "drug" in k.lower() and "no drug" not in k.lower()]
    assert len(drugged) == 2, f"exactly two drug rows are required; got {drugged}"
    activators = [k for k in drugged if lig[k] == 0 and resp[k] >= 0.8 * resp[on]]
    inhibitors = [k for k in drugged if lig[k] == 1 and resp[k] <= 0.2 * resp[on]]
    assert len(activators) == 1, f"exactly one drug may act without the messenger; got {activators}"
    assert len(inhibitors) == 1, f"exactly one drug may block despite the messenger; got {inhibitors}"
    assert activators[0] != inhibitors[0], "the two drugs must be different rows"
    return (f"without any drug the response runs {resp[off]:.0f} to {resp[on]:.0f}; one drug reaches "
            f"{resp[activators[0]]:.0f} with no messenger and the other falls to "
            f"{resp[inhibitors[0]]:.0f} with the messenger present")


def q16(table, item):
    labs = cg.labels(table)
    off = dict(zip(labs, cg.col(table, H_OFF)))
    on = dict(zip(labs, cg.col(table, H_ON)))
    up = [k for k in labs if on[k] >= 10 * off[k]]
    down = [k for k in labs if on[k] <= 0.1 * off[k]]
    same = [k for k in labs if 0.9 * off[k] <= on[k] <= 1.1 * off[k]]
    assert len(up) == 1 and len(down) == 1 and len(same) == 1, \
        f"the table must show one gene up, one down and one unchanged; got {up}, {down}, {same}"
    assert len({up[0], down[0], same[0]}) == 3, "the three genes must be distinct rows"
    changes = {round(on[k] - off[k], 6) for k in labs}
    assert len(changes) == len(labs), "'every gene changes by the same amount' must be false"
    return (f"{up[0]} rises from {off[up[0]]:.0f} to {on[up[0]]:.0f}, {down[0]} falls from "
            f"{off[down[0]]:.0f} to {on[down[0]]:.0f}, and {same[0]} is effectively unmoved")


def q17(table, item):
    labs = cg.labels(table)
    alive = dict(zip(labs, cg.col(table, H_ALIVE)))
    dead = dict(zip(labs, cg.col(table, H_DEAD)))
    for k in labs:
        assert alive[k] + dead[k] == 100, f"{k}: the two percentages must account for the culture"
    supplied = [k for k in labs if "withheld" not in k.lower()]
    withheld = [k for k in labs if "withheld" in k.lower() and "drug" not in k.lower()]
    rescued = [k for k in labs if "withheld" in k.lower() and "drug" in k.lower()]
    assert len(supplied) == len(withheld) == len(rescued) == 1, \
        f"one supplied, one withheld and one rescued condition are required; got {labs}"
    s, w, r = supplied[0], withheld[0], rescued[0]
    assert dead[w] >= 10 * dead[s], f"withholding the signal must raise cell death: {dead[s]} to {dead[w]}"
    assert dead[r] <= 2 * dead[s], f"switching the pathway on must restore survival: {dead[r]}"
    assert dead[w] > dead[r], "'switching the pathway on triggers cell death' must be false"
    assert len(set(dead.values())) > 1, "'the same rate in all three conditions' must be false"
    return (f"programmed cell death runs {dead[s]:.0f} percent with the signal, {dead[w]:.0f} percent "
            f"without it, and {dead[r]:.0f} percent when a drug switches the pathway on instead")


CLAIMS = [
 ("Changes in gene expression and in cell function",
  "EK 4.3.A.1 states that signal transduction may result in changes in gene expressions and cell function. A change in which genes are expressed is not a change in the sequence of the genome."),
 ("An altered phenotype, or programmed cell death",
  "EK 4.3.A.1 states that those changes may alter phenotype or result in programmed cell death, which the framework names apoptosis. Both outcomes are given in the one sentence."),
 ("Programmed cell death",
  "EK 4.3.A.1 glosses apoptosis in parentheses as programmed cell death, one of the outcomes signal transduction may produce."),
 ("Any domain of the receptor protein",
  "EK 4.3.B.1 states that mutations in ANY DOMAIN of the receptor protein may affect the downstream components by altering the subsequent transduction of the signal."),
 ("any component of the signaling pathway",
  "EK 4.3.B.1 extends the same claim beyond the receptor: mutations in any component of the signaling pathway may affect the downstream components by altering the subsequent transduction."),
 ("Activate the pathway or inhibit it",
  "EK 4.3.B.2 states that chemicals that interact with any component of the signaling pathway may activate or inhibit the pathway. Both directions are named."),
 ("change in cell function",
  "The CED lists epinephrine stimulation of glycogen breakdown in mammals as an illustrative example of EK 4.3.A.1, which covers signal transduction resulting in changes in gene expression and cell function."),
 ("regulating specific pathways in response to population density",
  "The CED lists microbes using chemical messengers to regulate specific pathways in response to population density, quorum sensing, as an illustrative example of EK 4.3.A.1 and its account of the responses a pathway elicits."),
 ("pathway regulates gene expression",
  "The CED lists cytokines regulating gene expression to allow for cell replication and division as an illustrative example under EK 4.3.B.1, and EK 4.3.A.1 makes changes in gene expression a result of signal transduction."),
 ("may result in changes in gene expression",
  "The CED lists mating pheromones in yeast triggering mating gene expression among the illustrative examples for EK 4.3.B.1, and EK 4.3.A.1 states that signal transduction may result in changes in gene expressions."),
 ("altering the phenotype",
  "The CED lists ethylene levels changing the production of different enzymes and allowing fruits to ripen among the illustrative examples for EK 4.3.B.1, and EK 4.3.A.1 makes altered phenotype one of the possible outcomes."),
 ("shaping the phenotype of a developing organism",
  "The CED lists HOX genes regulating animal body plans during embryonic development among the illustrative examples for EK 4.3.B.1, and EK 4.3.A.1 makes an altered phenotype an outcome of changed gene expression."),
 ("already reduced along with everything downstream",
  "Recomputed in q13 above. EK 4.3.B.1 makes a mutation affect the components DOWNSTREAM of it, so the earliest step that departs from normal locates the lesion, and only one line fails at binding."),
 ("both normal but the response is not",
  "Recomputed in q14 above. EK 4.3.B.1 leaves the steps before a lesion intact, so a line binding and relaying normally while failing to respond has its lesion after the relay."),
 ("activates the pathway without the ligand and the other inhibits it",
  "Recomputed in q15 above. EK 4.3.B.2 states that chemicals interacting with any component of a pathway may activate or inhibit it, and the table shows one of each against the untreated controls."),
 ("raises expression of one gene, lowers another",
  "Recomputed in q16 above. EK 4.3.A.1 states that signal transduction may result in changes in gene expressions without requiring every gene to move in the same direction."),
 ("triggers programmed cell death, and switching the pathway on prevents it",
  "Recomputed in q17 above. EK 4.3.A.1 makes programmed cell death one outcome of signal transduction, and EK 4.3.B.2 allows a chemical to activate a pathway; the drug substituting for the missing signal is what shows the pathway carries the effect."),
 ("downstream of the receptor is not activated by that messenger",
  "EK 4.3.B.1 states that mutations in any domain of the receptor protein may affect the downstream components by altering the subsequent transduction of the signal. A signal never received cannot be transduced."),
 ("interacted with a component of the pathway and activated it",
  "EK 4.3.B.2 states that chemicals interacting with any component of the signaling pathway may activate or inhibit the pathway, and a response appearing with no messenger present is the activating case."),
 ("inhibiting a component of the pathway downstream of the receptor",
  "EK 4.3.B.2 allows a chemical to interact with ANY component, and EK 4.3.B.1 makes a change at one point affect what lies below it. Binding that is still normal places the block after the receptor."),
 ("while the pathway can still be switched on downstream",
  "Skill 6.C asks for reasoning that connects evidence to a claim. EK 4.3.B.1 makes a lesion affect everything downstream of it, so separating a receptor lesion from a later one requires measurement at more than one point."),
 ("The cells undergo programmed cell death",
  "EK 4.3.A.1 states that signal transduction may result in changes in gene expression and cell function which may alter phenotype or result in programmed cell death, the framework's apoptosis."),
 ("changed gene expression and cell function, altering the phenotype",
  "EK 4.3.A.1 states that signal transduction may result in changes in gene expressions and cell function, which may alter phenotype. Identical genotypes diverging in phenotype after a signal is that case exactly."),
 ("passes the signal to those downstream of it",
  "EK 4.3.B.1 states that a mutation in any component may affect the downstream components by altering the subsequent transduction, and EK 4.2.B.2 makes the cascade a relay from receptor to cell targets."),
 ("whether the response appears without the messenger",
  "EK 4.3.B.2 states that chemicals interacting with a pathway may activate or inhibit it, so the discriminating test is what the response does in the presence and in the absence of the messenger."),
 ("the framework names altered phenotype as a possible outcome",
  "Skill 6.C asks for reasoning connecting evidence to a theory, and EK 4.3.A.1 supplies the chain: transduction changes gene expression and cell function, and those changes may alter phenotype."),
 ("activity of a component downstream of the receptor",
  "EK 4.3.B.1 makes a lesion affect the components downstream of it while leaving earlier steps intact, so only measurements at two or more points can locate it. The final response alone is lowered by a lesion anywhere."),
 ("Both responses downstream of that component are affected",
  "EK 4.3.B.1 states that a mutation in any component may affect the DOWNSTREAM components by altering the subsequent transduction, and both branches lie downstream of the disabled component."),
 ("Only a mutation in the ligand-binding domain",
  "EK 4.3.B.1 extends the effect to mutations in ANY domain of the receptor and in ANY component of the pathway, so no such restriction exists. The other four options restate EK 4.3.A.1, EK 4.3.B.2 and EK 4.3.B.1."),
 ("a change anywhere in the pathway can alter that output",
  "EK 4.3.A.1 gives the range of outputs, EK 4.3.B.1 makes a mutation anywhere in the pathway alter the downstream transduction, and EK 4.3.B.2 adds chemicals that may activate or inhibit it."),
]

cg.check(b4_3, CLAIMS, table_checks={13: q13, 14: q14, 15: q15, 16: q16, 17: q17})
