"""Key audit for AP BIOLOGY 3.4 Photosynthesis.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the shuffle ``export_units.py`` applies on export.

WHAT THE KEYS REST ON
---------------------
Every key traces to an essential knowledge statement of topic 3.4, listed at
the head of ``b3_4.py`` and cited by code in each claim below. The two that do
the most work, because they are the two most often stated backwards, are:

  3.4.B.1  electrons are ultimately transferred to NADP+, reducing it to
           NADPH, IN PHOTOSYSTEM I  -- not photosystem II
  3.4.B.4  the gradient runs LOW OUTSIDE the thylakoid membrane and HIGH
           INSIDE the thylakoid -- the OPPOSITE sense to the mitochondrial
           gradient of EK 3.5.A.3.ii, which is why item 29 keys the reversed
           statement as the unsupported one

EXCLUSION STATEMENTS OBSERVED. The CED puts beyond scope the steps of the
Calvin cycle, the structures of the molecules, the names of the enzymes
involved WITH THE EXCEPTION OF ATP SYNTHASE, the full names of the specific
electron carriers, and the specific steps and intermediates of these pathways.
No item asks for any of them. ATP synthase is named in items 15 and 22 because
the exclusion statement explicitly exempts it.

BOUNDARY WITH 3.5. Both topics carry an electron transport chain, a proton
gradient, ATP synthase and chemiosmosis. Every item here is
chloroplast-specific -- the direction of the thylakoid gradient, the name
photophosphorylation, NADP+ reduced at photosystem I, water split at
photosystem II, grana against stroma -- and topic 3.5 takes glycolysis,
pyruvate, the Krebs cycle, the matrix, oxygen as terminal acceptor, the
opposite gradient sense, oxidative phosphorylation, cristae and fermentation.

NO FIGURES. The bank cannot carry images and no stem here refers to one. Items
17, 18, 19 and 20 carry tables instead; every number is HYPOTHETICAL and the
stem says so, each keyed conclusion is recomputed below from the table alone,
and the distractors are shown false against the same numbers.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b3_4

LIGHT = b3_4._T_LIGHT
WAVE = b3_4._T_WAVE
PROTON = b3_4._T_PROTON
FRACTION = b3_4._T_FRACTION

H_INT = "Light intensity (arbitrary units)"
H_O2 = "Oxygen released (hypothetical, micromoles per hour)"
H_NM = "Wavelength of light supplied (nanometers)"
H_IN = "Proton concentration inside the thylakoid (hypothetical, nanomolar)"
H_STROMA = "Proton concentration in the stroma (hypothetical, nanomolar)"
H_ATP = "ATP formed in the light (hypothetical, arbitrary units)"
H_CARB = "Carbohydrate formed from carbon dioxide (hypothetical, arbitrary units)"


def q17(table, item):
    inten = cg.col(table, H_INT)
    o2 = cg.col(table, H_O2)
    assert all(b > a for a, b in zip(inten, inten[1:])), "intensity must increase down the table"
    assert all(b >= a for a, b in zip(o2, o2[1:])), f"oxygen release must never fall: {o2}"
    assert o2[-1] == o2[-2], "the series must end on a plateau, or 'levels off' is unsupported"
    assert o2[1] > o2[0], "the series must rise before it flattens"
    assert inten[0] == 0 and o2[0] == 0, "the dark point must show no oxygen release"
    assert o2[-1] > o2[0], "'the same at every intensity' and 'falls steadily' must both be false"
    return (f"oxygen release runs {o2} against intensities {inten}, rising and then holding at "
            f"{o2[-1]:.0f}, so it neither rises without limit nor stays constant")


def q18(table, item):
    nm = cg.col(table, H_NM)
    o2 = cg.col(table, H_O2)
    assert min(o2) > 0, "every wavelength must give a measurable rate"
    assert max(o2) >= 5 * min(o2), f"the spread must be large enough to call it selective: {o2}"
    i_max = o2.index(max(o2))
    assert o2.count(max(o2)) == 1, "the best wavelength must be unique"
    assert nm[i_max] != max(nm), "'only the longest wavelength' must be false"
    assert i_max != len(nm) // 2, "'the wavelength in the middle of the range' must be false"
    assert not all(b >= a for a, b in zip(o2, o2[1:])), "the series must not be monotonic"
    return (f"rates run {o2} across wavelengths {nm}, a {max(o2) / min(o2):.0f}-fold spread peaking "
            f"at {nm[i_max]:.0f} nanometers, which is neither the longest nor the middle wavelength")


def q19(table, item):
    labs = cg.labels(table)
    inside = dict(zip(labs, cg.col(table, H_IN)))
    stroma = dict(zip(labs, cg.col(table, H_STROMA)))
    dark = [k for k in labs if "dark" in k.lower()]
    assert len(dark) == 1, f"exactly one row must be the dark control; got {dark}"
    d = dark[0]
    assert inside[d] == stroma[d], "in darkness the two regions must be equal"
    lit = [k for k in labs if k != d]
    assert lit, "there must be illuminated rows to compare"
    for k in lit:
        assert inside[k] > stroma[k], f"{k}: protons must be higher inside the thylakoid"
        assert inside[k] > inside[d], f"{k}: the inside must rise above its dark value"
        assert stroma[k] < stroma[d], f"{k}: the stroma must fall below its dark value"
    assert len(set(inside.values())) > 1, "'equal in every condition' must be false"
    return (f"in darkness both regions sit at {inside[d]:.0f} nanomolar; under light the thylakoid "
            f"interior reaches {max(inside[k] for k in lit):.0f} while the stroma falls to "
            f"{min(stroma[k] for k in lit):.0f}")


def q20(table, item):
    labs = cg.labels(table)
    atp = dict(zip(labs, cg.col(table, H_ATP)))
    carb = dict(zip(labs, cg.col(table, H_CARB)))
    thy = [k for k in labs if "thylakoid" in k.lower() and "stroma" not in k.lower()]
    stro = [k for k in labs if "stroma" in k.lower() and "thylakoid" not in k.lower()]
    both = [k for k in labs if "thylakoid" in k.lower() and "stroma" in k.lower()]
    assert len(thy) == len(stro) == len(both) == 1, \
        f"the table must hold one thylakoid, one stroma and one combined row; got {labs}"
    t, s, b = thy[0], stro[0], both[0]
    assert atp[t] >= 10 * atp[s], "ATP formation must depend on the thylakoid material"
    assert carb[b] >= 10 * carb[t] and carb[b] >= 10 * carb[s], \
        "carbohydrate formation must require both materials together"
    assert atp[b] >= 0.8 * atp[t], "combining must not abolish ATP formation"
    assert carb[t] < atp[t] and carb[s] < atp[t], \
        "'either material alone supports both processes' must be false"
    return (f"ATP runs {atp[t]:.0f} for thylakoid alone against {atp[s]:.0f} for stroma alone, while "
            f"carbohydrate reaches {carb[b]:.0f} only when the two are combined "
            f"({carb[t]:.0f} and {carb[s]:.0f} apart)")


CLAIMS = [
 ("make carbohydrates and oxygen",
  "EK 3.4.A.1 states that photosynthesis is the series of reactions that use carbon dioxide, water, and light energy to make carbohydrates and oxygen. The distractors reverse the reaction or drop a required input."),
 ("Prokaryotic organisms",
  "EK 3.4.A.1.ii states that photosynthesis first evolved in prokaryotic organisms, and EK 3.4.A.1.iv makes those pathways the foundation of the eukaryotic version, placing the eukaryotic form later."),
 ("production of an oxygenated atmosphere",
  "EK 3.4.A.1.iii states that scientific evidence supports the claim that prokaryotic, cyanobacterial photosynthesis was responsible for the production of an oxygenated atmosphere."),
 ("foundation on which the eukaryotic version rests",
  "EK 3.4.A.1.iv states that prokaryotic photosynthetic pathways were the foundation of eukaryotic photosynthesis, and EK 3.4.A.1.ii places the prokaryotic version first in time."),
 ("outside the thylakoid, and carbon fixation occurs there",
  "EK 3.4.A.2.i states that the stroma is the fluid within the inner chloroplast membrane and outside the thylakoid, and that the carbon fixation reactions of the Calvin cycle occur in the stroma."),
 ("organized into two photosystems",
  "EK 3.4.A.2.ii states that the thylakoid membranes contain chlorophyll pigments organized into two photosystems, as well as electron transport proteins. Both the number and the transport proteins are part of the statement."),
 ("thylakoids, where the light reactions occur",
  "EK 3.4.A.2.iii states that thylakoids are organized in stacks called grana and that the light reactions occur in the grana. EK 3.4.A.2.i puts carbon fixation in the stroma instead."),
 ("ATP and NADPH",
  "EK 3.4.A.3 states that the light reactions yield ATP and NADPH, which power the production of organic molecules in the Calvin cycle. ADP and inorganic phosphate are what ATP is made FROM, per EK 3.4.B.5."),
 ("chloroplasts, in mitochondria, and across prokaryotic plasma membranes",
  "EK 3.4.B.1 states that electron transport chain reactions occur in chloroplasts, in mitochondria, and across prokaryotic plasma membranes. The chain is confined to none of the three."),
 ("reducing it to NADPH, in photosystem I",
  "EK 3.4.B.1 states that electrons passing through the thylakoid membrane are picked up and ultimately transferred to NADP+, reducing it to NADPH, in photosystem I. Naming photosystem II here is the standard reversal."),
 ("splitting of water",
  "EK 3.4.B.2 states that water then splits, supplying electrons to replace those lost from photosystem II. That splitting is also the origin of the oxygen EK 3.4.A.1 names as a product."),
 ("boosted to a higher energy level",
  "EK 3.4.B.2 states that during photosynthesis chlorophylls absorb energy from light, boosting electrons to a higher energy level in photosystems I and II."),
 ("transfer of electrons through an electron transport chain",
  "EK 3.4.B.3 states that photosystems I and II are embedded in the thylakoid membranes and are connected by the transfer of electrons through an electron transport chain."),
 ("The inside of the thylakoid",
  "EK 3.4.B.4 states that the membrane separates a region of low proton concentration outside the thylakoid membrane from a region of high proton concentration inside the thylakoid membrane."),
 ("Photophosphorylation",
  "EK 3.4.B.5 states that the flow of protons back through membrane-bound ATP synthase by chemiosmosis drives the formation of ATP from ADP and inorganic phosphate, and names this photophosphorylation."),
 ("ATP and NADPH, in the stroma",
  "EK 3.4.B.6 states that the energy captured in the light reactions and transferred to ATP and NADPH powers the production of carbohydrates from carbon dioxide in the Calvin cycle, and that this occurs in the stroma."),
 ("up to a point and then levels off",
  "Recomputed in q17 above. EK 3.4.A.1 makes light energy an input and oxygen an output, so oxygen release reports the process; skill 4.B asks students to describe the trend, which rises and then flattens."),
 ("some wavelengths far more effectively than others",
  "Recomputed in q18 above. EK 3.4.A.2.ii places chlorophyll pigments in the thylakoid membranes and EK 3.4.B.2 makes their absorption of light the step that boosts electrons, so a several-fold variation at constant intensity reports wavelength-dependent absorption."),
 ("builds up protons inside the thylakoid relative to the stroma",
  "Recomputed in q19 above. EK 3.4.B.4 places low proton concentration outside the thylakoid membrane and high concentration inside it, and EK 3.4.B.2 makes light the trigger for the electron flow that establishes the gradient."),
 ("carbohydrate formation requires both materials together",
  "Recomputed in q20 above. EK 3.4.A.2.iii and EK 3.4.A.3 place the light reactions and ATP formation in the thylakoid-containing grana, while EK 3.4.B.6 places carbohydrate production in the stroma and makes it depend on ATP and NADPH from the light reactions."),
 ("not replaced and oxygen release stops",
  "EK 3.4.B.2 makes the splitting of water the source of the electrons replacing those lost from photosystem II, and EK 3.4.A.1 lists oxygen among the products. Skill 6.E asks for the effect of disrupting one component of a system."),
 ("gradient collapses and ATP formation by chemiosmosis falls",
  "EK 3.4.B.5 makes the return flow of protons through ATP synthase by chemiosmosis the step that drives ATP formation, and EK 3.4.B.4 makes that flow depend on a gradient across the thylakoid membrane."),
 ("supplies the carbon that carbohydrate is built from",
  "EK 3.4.A.1 names carbon dioxide among the inputs and EK 3.4.B.6 describes carbohydrate production as a conversion of carbon dioxide powered by ATP and NADPH. Without the carbon source there is nothing for that energy to build."),
 ("NADP+ is reduced in photosystem I",
  "EK 3.4.B.1 places the transfer of electrons to NADP+, reducing it to NADPH, in photosystem I. Water splitting belongs to photosystem II under EK 3.4.B.2 and carbohydrate assembly to the stroma under EK 3.4.B.6."),
 ("Carbon dioxide",
  "EK 3.4.A.1 names carbon dioxide as an input and carbohydrate as a product, and EK 3.4.B.6 describes the production of carbohydrates FROM CARBON DIOXIDE. ATP and NADPH carry energy rather than carbon."),
 ("Use them in biological processes or store them",
  "EK 3.4.A.1.i states that photosynthetic organisms capture energy from the sun and produce sugars that can be used in biological processes or stored. Both fates are named in the statement."),
 ("first evolved in prokaryotes, so early prokaryotes were the available source",
  "Skill 6.B asks that a claim be supported with evidence from biological processes. EK 3.4.A.1 makes oxygen a product, EK 3.4.A.1.ii places the first photosynthesis in prokaryotes, and EK 3.4.A.1.iii states the conclusion those two support."),
 ("Grana with the light reactions and stroma with carbon fixation",
  "EK 3.4.A.2.iii places the light reactions in the grana and EK 3.4.A.2.i places the carbon fixation reactions of the Calvin cycle in the stroma, so the two sets of reactions occupy different regions of one organelle."),
 ("higher in the stroma than inside the thylakoid",
  "EK 3.4.B.4 states the gradient in the opposite sense: low outside the thylakoid membrane and high inside it. The other four options restate EK 3.4.B.3, EK 3.4.B.2, EK 3.4.A.3 and EK 3.4.A.2.i directly."),
 ("supply the ATP and NADPH that the Calvin cycle uses",
  "EK 3.4.A.3 and EK 3.4.B.6 both state the dependence in this direction: the light reactions yield ATP and NADPH, and that energy powers production of carbohydrates from carbon dioxide in the stroma."),
]

cg.check(b3_4, CLAIMS, table_checks={17: q17, 18: q18, 19: q19, 20: q20})
