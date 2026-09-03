"""Key audit for AP BIOLOGY 3.1 Enzymes.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the choice shuffle ``export_units.py`` applies on export. The claim
names the essential knowledge statement or the science practice the key rests
on.

WHAT THE KEYS REST ON
---------------------
  3.1.A.1  the structure and function of enzymes contribute to the regulation
           of biological processes; enzymes are PROTEINS that are BIOLOGICAL
           CATALYSTS facilitating chemical reactions in cells by LOWERING THE
           ACTIVATION ENERGY
  3.1.A.2  for an enzyme-mediated chemical reaction to occur, the SHAPE AND
           CHARGE of the substrate must be COMPATIBLE WITH THE ACTIVE SITE;
           illustrated by the ENZYME-SUBSTRATE COMPLEX model

Ten items rest on the topic's second suggested skill, 3.C -- identify
experimental procedures that align with the question, including identifying
dependent and independent variables, identifying appropriate controls, and
justifying appropriate controls. That skill is attached to this topic in the
CED and to no other topic in Unit 3, which is why it carries a third of the
module.

NOTHING HERE RESTS ON TOPIC 3.2. Temperature, pH, denaturation, inhibitors and
the relative concentrations of substrate and product are essential knowledge of
3.2 and no key in this file uses them. Item 16 goes as far as the word
CATALYST in EK 3.1.A.1 warrants -- a catalyst lowers a barrier and is not
turned into product -- and no further.

Items 12, 13, 14, 15 and 26 carry tables. Every number is HYPOTHETICAL and the
stem says so; each keyed conclusion is recomputed below from the table alone,
and the distractors are shown false against the same numbers.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b3_1

RATE = b3_1._T_RATE
EA = b3_1._T_EA
SPEC = b3_1._T_SPEC

H_ENZ = "Enzyme added (micrograms)"
H_CONV = "Substrate converted in five minutes (micromoles)"
H_NOENZ = "Activation energy with no enzyme present (kilojoules per mole)"
H_WITHENZ = "Activation energy with the enzyme present (kilojoules per mole)"
SUBSTRATES = ["Product formed with substrate A (micromoles)",
              "Product formed with substrate B (micromoles)",
              "Product formed with substrate C (micromoles)"]


def q12(table, item):
    enz = cg.col(table, H_ENZ)
    conv = cg.col(table, H_CONV)
    pairs = sorted(zip(enz, conv))
    assert pairs[0][0] == 0 and pairs[0][1] == 0, \
        "the zero-enzyme tube must convert nothing"
    assert all(b[1] > a[1] for a, b in zip(pairs, pairs[1:])), \
        "conversion must rise as enzyme rises"
    ratios = {round(c / e, 6) for e, c in pairs if e > 0}
    assert len(ratios) == 1, f"conversion per microgram of enzyme is not constant: {ratios}"
    assert conv[enz.index(0.0)] != max(conv), \
        "'the zero-enzyme tube converted the most' must be false"
    return (f"the zero-enzyme tube converts 0 and the rest convert {ratios.pop():.0f} micromoles per "
            f"microgram of enzyme, so conversion rises in step with enzyme added")


def q13(table, item):
    enz = cg.col(table, H_ENZ)
    conv = cg.col(table, H_CONV)
    zeros = [i for i, e in enumerate(enz) if e == 0]
    assert len(zeros) == 1, f"exactly one tube may set the independent variable to zero; got {zeros}"
    i = zeros[0]
    assert enz[i] != max(enz), "'the tube with the most enzyme' must not be the control"
    assert conv[i] != max(conv), "'the tube that converted the most' must not be the control"
    assert enz[i] != sorted(enz)[len(enz) // 2], \
        "'the tube with an intermediate amount' must not be the control"
    return (f"exactly one of the {len(enz)} tubes receives no enzyme, and it is neither the "
            f"highest-dose nor the highest-yield nor an intermediate-dose tube")


def q14(table, item):
    labs = cg.labels(table)
    without = dict(zip(labs, cg.col(table, H_NOENZ)))
    with_ = dict(zip(labs, cg.col(table, H_WITHENZ)))
    assert all(with_[k] < without[k] for k in labs), \
        f"every with-enzyme value must be below its without-enzyme value: {without} vs {with_}"
    hi = max(labs, key=lambda k: without[k])
    lo = min(labs, key=lambda k: with_[k])
    assert hi != lo, "'the highest barrier without enzyme becomes the lowest with enzyme' must be false"
    return (f"all {len(labs)} reactions fall from {list(without.values())} to {list(with_.values())} "
            f"kilojoules per mole, so the enzyme lowers every barrier listed")


def q26(table, item):
    labs = cg.labels(table)
    without = dict(zip(labs, cg.col(table, H_NOENZ)))
    with_ = dict(zip(labs, cg.col(table, H_WITHENZ)))
    fracs = {k: with_[k] / without[k] for k in labs}
    assert len(set(round(f, 6) for f in fracs.values())) == 1, \
        f"the proportional reduction is not the same in every reaction: {fracs}"
    drops = {k: without[k] - with_[k] for k in labs}
    assert len(set(drops.values())) > 1, \
        "the absolute reductions must differ, or the item has no distinction to make"
    f = next(iter(fracs.values()))
    return (f"each reaction retains the same fraction {f:.2f} of its barrier, a reduction of "
            f"{100 * (1 - f):.0f} percent, while the absolute drops {sorted(drops.values())} differ")


def q15(table, item):
    labs = cg.labels(table)
    grid = {lab: [cg.cell(table, lab, h) for h in SUBSTRATES] for lab in labs}
    for lab, row in grid.items():
        hits = [v for v in row if v > 0]
        assert len(hits) == 1, f"{lab} must form product with exactly one substrate; got {row}"
    for j, h in enumerate(SUBSTRATES):
        colvals = [grid[lab][j] for lab in labs]
        assert len([v for v in colvals if v > 0]) == 1, \
            f"substrate {h!r} must be acted on by exactly one enzyme; got {colvals}"
    assert len({tuple(r) for r in grid.values()}) == len(labs), \
        "'the enzymes are interchangeable' must be false"
    return (f"each of the {len(labs)} enzymes yields product with exactly one substrate and each "
            f"substrate is used by exactly one enzyme, so the grid is one-to-one")


CLAIMS = [
 ("lowering the activation energy the reaction must overcome",
  "EK 3.1.A.1 states that enzymes are biological catalysts that facilitate chemical reactions in cells by lowering the activation energy. Lowering a barrier is not supplying energy, heating the surroundings, or changing the products."),
 ("Proteins",
  "EK 3.1.A.1 states directly that enzymes are proteins that are biological catalysts. That identity is what makes an active site a consequence of the molecule's amino acid sequence."),
 ("shape and its charge must both be compatible",
  "EK 3.1.A.2 names both properties: the shape AND charge of the substrate must be compatible with the active site of the enzyme. The compatibility required is with the active site, not with the whole molecule."),
 ("enzyme-substrate complex model",
  "EK 3.1.A.2 names the enzyme-substrate complex model as the illustration of the compatibility requirement. The other named models describe membranes, organelle origins, proton gradients and nucleic acid structure."),
 ("compatible in shape and charge with the enzyme's active site",
  "EK 3.1.A.2 makes compatibility of shape and charge with the active site the condition for an enzyme-mediated reaction, so specificity follows from that condition rather than from availability or chance."),
 ("charge compatibility has been lost",
  "EK 3.1.A.2 requires both the shape and the charge of the substrate to be compatible with the active site. Preserving one requirement while destroying the other leaves the pair incompatible and the reaction unable to proceed as before."),
 ("depends on which enzymes it has available",
  "EK 3.1.A.1 opens by stating that the structure and function of enzymes contribute to the regulation of biological processes. An uncatalyzed reaction is too slow to matter, so controlling which enzyme is present is how the process is controlled."),
 ("amount of enzyme added to each tube",
  "Skill 3.C asks students to identify dependent and independent variables. The independent variable is the one the investigator sets, here the enzyme dose; time, volume and temperature are held constant and product formed is measured."),
 ("amount of product formed in each tube",
  "Skill 3.C asks students to identify dependent and independent variables. The dependent variable is the measured outcome that may respond to the treatment, which in this design is the product formed."),
 ("except that no enzyme is added",
  "Skill 3.C asks for an appropriate control and for its justification. The claim under test is that the enzyme is responsible, so the control must differ from the treatment in the enzyme and in nothing else."),
 ("would have happened anyway would be credited to the enzyme",
  "Skill 3.C asks students to justify a control rather than merely name one. EK 3.1.A.1 makes the enzyme a catalyst of a reaction that can also proceed slowly on its own, so the untreated tube measures the part of the result the enzyme did not cause."),
 ("rises with the amount of enzyme",
  "Recomputed in q12 above: nothing converts without enzyme and conversion per microgram is constant across the dosed tubes. That is EK 3.1.A.1's catalysis claim shown as data, which skill 4.B asks students to describe."),
 ("to which no enzyme was added",
  "Recomputed in q13 above: exactly one tube sets the independent variable to zero and it is neither the highest-dose, the highest-yield, nor an intermediate-dose tube. Skill 3.C asks students to identify appropriate controls."),
 ("lowers the activation energy of every reaction listed",
  "Recomputed in q14 above: every with-enzyme value lies below its matching without-enzyme value. That is EK 3.1.A.1's statement that enzymes facilitate reactions by lowering the activation energy, shown as measurements."),
 ("only one of the substrates offered",
  "Recomputed in q15 above: each enzyme yields product with exactly one substrate and each substrate is used by exactly one enzyme. That is EK 3.1.A.2's compatibility requirement expressed as data."),
 ("while the enzyme, a catalyst, remained able to act",
  "EK 3.1.A.1 calls enzymes biological catalysts, and a catalyst lowers a reaction's activation energy without being turned into the product. Exhaustion of substrate explains the same observation without contradicting that description."),
 ("occur fast enough to be useful",
  "EK 3.1.A.1 describes enzymes as catalysts that facilitate reactions by lowering the activation energy, which is a claim about the rate at which a reaction proceeds and not about whether it is possible at all."),
 ("each catalyzes its own reaction",
  "EK 3.1.A.2 requires compatibility between substrate and active site for a reaction to occur, and EK 3.1.A.1 makes each enzyme the catalyst of its own reaction. One substrate compatible with two different active sites is exactly what the observation reports."),
 ("occupies an enzyme's active site",
  "EK 3.1.A.2 introduces the enzyme-substrate complex model as the illustration of substrate and active site compatibility, so the complex is enzyme and substrate joined at that site, not the product, the barrier or a denatured protein."),
 ("much faster with the protein present",
  "Skill 6.B asks for evidence connected to the claim. EK 3.1.A.1 defines an enzyme by its effect on reaction rate, so the supporting evidence is a rate comparison against a mixture differing only in the protein."),
 ("Two variables change at once",
  "Skill 3.C requires procedures aligned with the question asked. When treatment and substrate differ together, either one accounts for the outcome, so the design cannot answer the question it was built to answer."),
 ("alters the region of the substrate that fits into the active site",
  "EK 3.1.A.2 makes compatibility of the substrate's shape and charge with the active site the condition for the reaction. Only an alteration at the region that must fit the site removes that compatibility."),
 ("creates an active site with a particular shape and charge",
  "EK 3.1.A.1 pairs structure with function, and EK 3.1.A.2 supplies the link: the substrate's shape and charge must be compatible with the active site, and the active site is a feature of the protein's structure."),
 ("also speeds up closely related reactions",
  "Skill 3.C asks for procedures aligned to the question. EK 3.1.A.2's compatibility requirement predicts that a genuine enzyme acts on some related molecules and not others, so testing the range of substrates is the informative follow-up."),
 ("eliminates the activation energy of a reaction entirely",
  "EK 3.1.A.1 says enzymes LOWER the activation energy; it does not say they abolish it. The other four statements restate EK 3.1.A.1 and EK 3.1.A.2 directly and are therefore supported."),
 ("the same fraction in every one of the four reactions",
  "Recomputed in q26 above: each with-enzyme value is the same fraction of its without-enzyme value while the absolute drops differ. Skill 5.A asks for exactly this kind of ratio calculation."),
 ("the difference between the tubes",
  "Skill 3.C's justification of a control is this reasoning. EK 3.1.A.1 makes the enzyme a catalyst of a reaction that can also proceed uncatalyzed, so the control measures the background and the enzyme's contribution is what remains."),
 ("rapidly only in the cell that makes the enzyme",
  "EK 3.1.A.1 makes the enzyme the reason a reaction proceeds fast enough to matter, and makes that the mechanism by which enzymes contribute to the regulation of biological processes. Which enzymes a cell has is what separates the two cells."),
 ("leaves the reaction rate the same as in a mixture without it",
  "EK 3.1.A.1 defines an enzyme by its effect on the rate at which a reaction proceeds, so a protein that leaves the rate unchanged fails the defining test. The other observations are all compatible with the protein being the enzyme."),
 ("compatible with their active sites",
  "EK 3.1.A.1 gives the identity and the mechanism -- protein catalysts lowering activation energy inside cells -- and EK 3.1.A.2 gives the condition, compatibility of the substrate's shape and charge with the active site."),
]

cg.check(b3_1, CLAIMS, table_checks={12: q12, 13: q13, 14: q14, 15: q15, 26: q26})
