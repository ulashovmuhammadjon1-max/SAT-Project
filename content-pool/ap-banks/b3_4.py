# AP BIOLOGY 3.4 Photosynthesis
# CED effective Fall 2025, Unit 3 Cellular Energetics. Big Idea 2 Energetics.
# Learning objectives 3.4.A (describe the photosynthetic processes and
# structural features of the chloroplast that allow organisms to capture and
# store energy) and 3.4.B (explain how cells capture energy from light and
# transfer it to biological molecules for storage and use).
# Suggested skill 6.B, support a claim with evidence from biological
# principles, concepts, processes, and data.
#
# Essential knowledge, in the framework's own terms:
#   3.4.A.1     photosynthesis uses CARBON DIOXIDE, WATER and LIGHT ENERGY to
#               make CARBOHYDRATES and OXYGEN
#     i.        photosynthetic organisms capture energy from the sun and
#               produce sugars that can be USED or STORED
#     ii.       photosynthesis FIRST EVOLVED IN PROKARYOTIC organisms
#     iii.      evidence supports the claim that prokaryotic (CYANOBACTERIAL)
#               photosynthesis was responsible for an OXYGENATED ATMOSPHERE
#     iv.       prokaryotic photosynthetic pathways were the FOUNDATION of
#               eukaryotic photosynthesis
#   3.4.A.2     STROMA and THYLAKOIDS are found within the chloroplast
#     i.        the stroma is the fluid inside the inner chloroplast membrane
#               and OUTSIDE the thylakoid; CARBON FIXATION (Calvin cycle)
#               occurs in the STROMA
#     ii.       thylakoid membranes hold CHLOROPHYLL pigments organized into
#               TWO PHOTOSYSTEMS, plus electron transport proteins
#     iii.      thylakoids stacked into GRANA; the LIGHT REACTIONS occur there
#   3.4.A.3     the light reactions yield ATP and NADPH, which power production
#               of organic molecules in the Calvin cycle
#   3.4.B.1     ETC reactions occur in CHLOROPLASTS, MITOCHONDRIA and across
#               PROKARYOTIC PLASMA MEMBRANES; in photosynthesis electrons are
#               ultimately transferred to NADP+, reducing it to NADPH IN
#               PHOTOSYSTEM I
#   3.4.B.2     chlorophylls absorb light energy, BOOSTING ELECTRONS to a higher
#               energy level in photosystems I and II; WATER THEN SPLITS,
#               supplying electrons to replace those lost from PHOTOSYSTEM II
#   3.4.B.3     photosystems I and II are embedded in the thylakoid membranes
#               and are CONNECTED BY an ETC
#   3.4.B.4     the proton gradient runs LOW OUTSIDE the thylakoid membrane and
#               HIGH INSIDE the thylakoid
#   3.4.B.5     proton flow back through membrane-bound ATP SYNTHASE by
#               CHEMIOSMOSIS drives ATP formation from ADP and inorganic
#               phosphate; this is PHOTOPHOSPHORYLATION
#   3.4.B.6     the energy in ATP and NADPH powers production of carbohydrates
#               from carbon dioxide in the Calvin cycle, IN THE STROMA
#
# EXCLUSION STATEMENTS OBSERVED. The CED puts beyond scope: memorization of the
# steps of the Calvin cycle, the structures of the molecules and the names of
# the enzymes involved WITH THE EXCEPTION OF ATP SYNTHASE; the full names of
# specific electron carriers; and the specific steps, enzyme names and
# intermediates of these pathways. No item here asks for any of them. ATP
# synthase is named because the CED explicitly exempts it.
#
# BOUNDARY WITH 3.5, HELD DELIBERATELY. Both topics carry an electron transport
# chain, a proton gradient, ATP synthase and chemiosmosis, and a bank that
# asked the same question of each would be asking one question twice. Every
# item here is chloroplast-specific: the DIRECTION of the thylakoid gradient
# (high INSIDE), the name PHOTOPHOSPHORYLATION, reduction of NADP+ at
# PHOTOSYSTEM I, the SPLITTING OF WATER at photosystem II, and grana against
# stroma. Topic 3.5 takes glycolysis, pyruvate, the Krebs cycle, the matrix,
# oxygen as terminal acceptor, the opposite gradient direction, OXIDATIVE
# phosphorylation, cristae and fermentation.
#
# NO FIGURES ANYWHERE. The bank cannot carry images, so no stem refers to a
# graph or a diagram. Where a question needs data it carries a table and asks
# the question of the table.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("3.4", "Photosynthesis", 3)

_T_LIGHT = dict(
    headers=["Light intensity (arbitrary units)",
             "Oxygen released (hypothetical, micromoles per hour)"],
    rows=[["0", "0"],
          ["20", "12"],
          ["40", "24"],
          ["60", "33"],
          ["80", "36"],
          ["100", "36"]])

_T_WAVE = dict(
    headers=["Wavelength of light supplied (nanometers)",
             "Oxygen released (hypothetical, micromoles per hour)"],
    rows=[["450", "30"],
          ["500", "8"],
          ["550", "3"],
          ["600", "10"],
          ["675", "28"]])

_T_PROTON = dict(
    headers=["Condition of the chloroplast sample",
             "Proton concentration inside the thylakoid (hypothetical, nanomolar)",
             "Proton concentration in the stroma (hypothetical, nanomolar)"],
    rows=[["Held in darkness", "100", "100"],
          ["Illuminated for thirty seconds", "900", "80"],
          ["Illuminated for two minutes", "2,500", "70"]])

_T_FRACTION = dict(
    headers=["Chloroplast material supplied",
             "ATP formed in the light (hypothetical, arbitrary units)",
             "Carbohydrate formed from carbon dioxide (hypothetical, arbitrary units)"],
    rows=[["Thylakoid material alone", "85", "2"],
          ["Stroma material alone", "3", "4"],
          ["Thylakoid and stroma material together", "82", "70"]])

QUESTIONS = [
 dict(q="Which set of inputs and outputs does the framework give for photosynthesis?",
   choices=[
     "Carbon dioxide, water and light energy are used to make carbohydrates and oxygen",
     "Carbohydrates and oxygen are used to make carbon dioxide, water and light energy",
     "Carbon dioxide and oxygen are used to make water and light energy",
     "Water and carbohydrates are used to make carbon dioxide and light energy",
     "Light energy alone is used to make carbohydrates, with no other input"],
   ans=0,
   why="EK 3.4.A.1 states that photosynthesis is the series of reactions that use carbon dioxide, water, and light energy to make carbohydrates and oxygen. The other options reverse the reaction or drop a required input."),

 dict(q="In which kind of organism does the framework say photosynthesis first evolved?",
   choices=[
     "Prokaryotic organisms",
     "Eukaryotic algae",
     "Flowering plants",
     "Multicellular fungi",
     "Animals that later lost the ability"],
   ans=0,
   why="EK 3.4.A.1.ii states that photosynthesis first evolved in prokaryotic organisms. EK 3.4.A.1.iv adds that those prokaryotic pathways were the foundation of eukaryotic photosynthesis, which places the eukaryotic version later."),

 dict(q="What large-scale change to the planet does the framework attribute to prokaryotic photosynthesis?",
   choices=[
     "The production of an oxygenated atmosphere",
     "The formation of the first continents",
     "The removal of all carbon dioxide from the atmosphere",
     "The origin of the eukaryotic nucleus",
     "The appearance of liquid water on the surface"],
   ans=0,
   why="EK 3.4.A.1.iii states that scientific evidence supports the claim that prokaryotic, cyanobacterial photosynthesis was responsible for the production of an oxygenated atmosphere."),

 dict(q="How does the framework relate prokaryotic photosynthesis to the photosynthesis carried out by eukaryotes?",
   choices=[
     "The prokaryotic pathways were the foundation on which the eukaryotic version rests",
     "The two arose independently and share no pathways",
     "The eukaryotic version came first and was later transferred to prokaryotes",
     "Only eukaryotes have ever carried out photosynthesis",
     "The two use entirely different inputs and produce entirely different outputs"],
   ans=0,
   why="EK 3.4.A.1.iv states that prokaryotic photosynthetic pathways were the foundation of eukaryotic photosynthesis, and EK 3.4.A.1.ii places the prokaryotic version first in time."),

 dict(q="Where within the chloroplast is the stroma, and what occurs there?",
   choices=[
     "It is the fluid inside the inner chloroplast membrane and outside the thylakoid, and carbon fixation occurs there",
     "It is the space inside the thylakoid, and carbon fixation occurs there",
     "It is the fluid outside the chloroplast in the cytosol, and the light reactions occur there",
     "It is the stack of thylakoid membranes, and carbon fixation occurs there",
     "It is the outer membrane of the chloroplast, and the light reactions occur there"],
   ans=0,
   why="EK 3.4.A.2.i states that the stroma is the fluid within the inner chloroplast membrane and outside the thylakoid, and that the carbon fixation reactions of the Calvin cycle occur in the stroma."),

 dict(q="What does the framework say the thylakoid membranes contain?",
   choices=[
     "Chlorophyll pigments organized into two photosystems, along with electron transport proteins",
     "Chlorophyll pigments organized into a single photosystem and no transport proteins",
     "Carbon fixation enzymes and no pigments",
     "The chloroplast's supply of carbohydrate and nothing else",
     "Only the proteins that transport carbon dioxide into the chloroplast"],
   ans=0,
   why="EK 3.4.A.2.ii states that the thylakoid membranes contain chlorophyll pigments organized into two photosystems, as well as electron transport proteins."),

 dict(q="What are grana, and which reactions does the framework place in them?",
   choices=[
     "Stacks of thylakoids, where the light reactions occur",
     "Stacks of thylakoids, where carbon fixation occurs",
     "Regions of the stroma, where the light reactions occur",
     "Folds of the outer chloroplast membrane, where carbon fixation occurs",
     "Pores in the inner chloroplast membrane, where carbon dioxide enters"],
   ans=0,
   why="EK 3.4.A.2.iii states that thylakoids are organized in stacks called grana and that the light reactions of photosynthesis occur in the grana. Carbon fixation is placed in the stroma by EK 3.4.A.2.i."),

 dict(q="Which two energy-carrying products do the light reactions yield in eukaryotes, according to the framework?",
   choices=[
     "ATP and NADPH",
     "ATP and carbon dioxide",
     "NADPH and carbohydrate",
     "Oxygen and water",
     "ADP and inorganic phosphate"],
   ans=0,
   why="EK 3.4.A.3 states that the light reactions capture energy present in light to yield ATP and NADPH, which power the production of organic molecules in the Calvin cycle. ADP and inorganic phosphate are the reactants ATP is made from, per EK 3.4.B.5."),

 dict(q="In which locations does the framework say electron transport chain reactions occur?",
   choices=[
     "In chloroplasts, in mitochondria, and across prokaryotic plasma membranes",
     "In chloroplasts only",
     "In mitochondria only",
     "Across prokaryotic plasma membranes only",
     "In the nucleus of every eukaryotic cell"],
   ans=0,
   why="EK 3.4.B.1 states that electron transport chain reactions occur in chloroplasts, in mitochondria, and across prokaryotic plasma membranes. The chain is not confined to any one of the three."),

 dict(q="In photosynthesis, what happens to the electrons that pass through the thylakoid membrane, and where?",
   choices=[
     "They are ultimately transferred to NADP+, reducing it to NADPH, in photosystem I",
     "They are ultimately transferred within photosystem II to NADP+, which is reduced to NADPH",
     "They are ultimately transferred to oxygen, forming water, in photosystem I",
     "They are ultimately transferred to carbon dioxide, forming carbohydrate, in the grana",
     "They are returned unchanged to the chlorophyll that released them"],
   ans=0,
   why="EK 3.4.B.1 states that electrons passing through the thylakoid membrane are picked up and ultimately transferred to NADP+, reducing it to NADPH, in photosystem I."),

 dict(q="Where do the electrons that replace those lost from photosystem II come from?",
   choices=[
     "From the splitting of water",
     "From the splitting of carbon dioxide",
     "From the breakdown of carbohydrate in the stroma",
     "From NADPH returning its electrons to the membrane",
     "From ATP synthase as protons flow through it"],
   ans=0,
   why="EK 3.4.B.2 states that water then splits, supplying electrons to replace those lost from photosystem II. That is also the source of the oxygen named as a product in EK 3.4.A.1."),

 dict(q="What does the framework say happens when chlorophylls absorb energy from light?",
   choices=[
     "Electrons are boosted to a higher energy level in photosystems I and II",
     "Electrons are removed from carbon dioxide and passed to water",
     "Protons are pumped directly out of the chloroplast into the cytosol",
     "Carbohydrate is formed immediately without any further reactions",
     "The chlorophyll molecule is permanently destroyed"],
   ans=0,
   why="EK 3.4.B.2 states that during photosynthesis chlorophylls absorb energy from light, boosting electrons to a higher energy level in photosystems I and II."),

 dict(q="How are photosystems I and II related to one another in the thylakoid membrane?",
   choices=[
     "They are connected by the transfer of electrons through an electron transport chain",
     "They are connected by the transfer of carbon dioxide through the stroma",
     "They operate in separate organelles and are never connected",
     "They are two names for the same structure",
     "They are connected only when the chloroplast is in darkness"],
   ans=0,
   why="EK 3.4.B.3 states that photosystems I and II are embedded in the thylakoid membranes of chloroplasts and are connected by the transfer of electrons through an electron transport chain."),

 dict(q="Which side of the thylakoid membrane holds the higher concentration of protons once the electron transport chain has been running?",
   choices=[
     "The inside of the thylakoid",
     "The stroma, outside the thylakoid",
     "The cytosol outside the chloroplast",
     "The space between the two chloroplast membranes",
     "Both sides equally, since protons distribute evenly"],
   ans=0,
   why="EK 3.4.B.4 states that the membrane separates a region of low proton concentration outside the thylakoid membrane from a region of high proton concentration inside the thylakoid membrane."),

 dict(q="What is the name the framework gives to the formation of ATP that is driven by protons flowing back through ATP synthase in the chloroplast?",
   choices=[
     "Photophosphorylation",
     "Carbon fixation",
     "Denaturation",
     "Endosymbiosis",
     "Glycolysis"],
   ans=0,
   why="EK 3.4.B.5 states that the flow of protons back through membrane-bound ATP synthase by chemiosmosis drives the formation of ATP from ADP and inorganic phosphate, and that this is known as photophosphorylation."),

 dict(q="What powers the production of carbohydrates from carbon dioxide, and in which part of the chloroplast does it occur?",
   choices=[
     "The energy carried by ATP and NADPH, in the stroma",
     "The energy carried by ATP and NADPH, inside the thylakoid",
     "Light absorbed directly by carbon dioxide, in the stroma",
     "The proton gradient acting directly on carbon dioxide, in the grana",
     "Oxygen released by the splitting of water, in the stroma"],
   ans=0,
   why="EK 3.4.B.6 states that the energy captured in the light reactions and transferred to ATP and NADPH powers the production of carbohydrates from carbon dioxide in the Calvin cycle, and that this occurs in the stroma of the chloroplast."),

 dict(q="Oxygen release was measured from a plant tissue at a series of light intensities, with the results shown. Which conclusion do the data support?",
   table=_T_LIGHT,
   choices=[
     "Oxygen release rises with light intensity up to a point and then levels off",
     "Oxygen release rises without limit as light intensity rises",
     "Oxygen release falls steadily as light intensity rises",
     "Oxygen release is the same at every light intensity tested",
     "Oxygen is released at the same rate in the dark as in the brightest light"],
   ans=0,
   why="EK 3.4.A.1 makes light energy an input and oxygen an output of photosynthesis, so oxygen release reports the process. Skill 4.B asks students to describe the trend, which in this series rises and then flattens."),

 dict(q="Oxygen release was measured with light of several wavelengths at equal intensity, with the results shown. Which claim do the data support?",
   table=_T_WAVE,
   choices=[
     "The pigments involved capture some wavelengths far more effectively than others",
     "The pigments involved capture every wavelength equally well",
     "The pigments involved capture only the longest wavelength supplied",
     "Wavelength has no bearing on how much oxygen is released",
     "The highest rate occurs at the wavelength in the middle of the range tested"],
   ans=0,
   why="EK 3.4.A.2.ii places chlorophyll pigments in the thylakoid membranes and EK 3.4.B.2 makes their absorption of light the step that boosts electrons. A rate that varies several-fold with wavelength at constant intensity is evidence that absorption is wavelength-dependent."),

 dict(q="Proton concentrations were measured in chloroplasts held in darkness and after illumination, with the results shown. Which statement do the data support?",
   table=_T_PROTON,
   choices=[
     "Illumination builds up protons inside the thylakoid relative to the stroma",
     "Illumination builds up protons in the stroma relative to the inside of the thylakoid",
     "Illumination removes the difference in proton concentration between the two regions",
     "The proton concentrations are equal in every condition tested",
     "Protons accumulate inside the thylakoid only when the sample is kept in darkness"],
   ans=0,
   why="EK 3.4.B.4 places low proton concentration outside the thylakoid membrane and high proton concentration inside the thylakoid, and EK 3.4.B.2 makes light the trigger for the electron flow that establishes it. The measurements show the two regions equal in darkness and diverging in light."),

 dict(q="Chloroplast material was separated and supplied to reaction mixtures, with the results shown. Which conclusion is best supported?",
   table=_T_FRACTION,
   choices=[
     "ATP formation in the light requires the thylakoid material, while carbohydrate formation requires both materials together",
     "Carbohydrate formation requires the thylakoid material alone",
     "ATP formation in the light requires the stroma material alone",
     "Either material alone supports both processes equally well",
     "Neither process occurs when the two materials are combined"],
   ans=0,
   why="EK 3.4.A.2.iii and EK 3.4.A.3 place the light reactions and ATP formation in the thylakoid-containing grana, while EK 3.4.B.6 places carbohydrate production in the stroma and makes it depend on ATP and NADPH from the light reactions."),

 dict(q="A chemical prevents water from splitting in an illuminated chloroplast. What is the most reasonable prediction?",
   choices=[
     "Electrons lost from photosystem II are not replaced and oxygen release stops",
     "Electrons lost from photosystem II are replaced from carbon dioxide instead",
     "The rate of oxygen release rises because water is no longer consumed",
     "Carbon fixation continues at full rate because it does not involve the thylakoid",
     "Protons accumulate faster inside the thylakoid than before"],
   ans=0,
   why="EK 3.4.B.2 makes the splitting of water the source of the electrons that replace those lost from photosystem II, and EK 3.4.A.1 lists oxygen among the products. Skill 6.E asks for the effect of disrupting one component of the system."),

 dict(q="A treatment makes the thylakoid membrane freely permeable to protons while leaving the electron transport chain intact. What is the most reasonable prediction?",
   choices=[
     "The proton gradient collapses and ATP formation by chemiosmosis falls sharply",
     "The proton gradient becomes steeper and ATP formation rises",
     "Electron transport stops immediately but ATP formation continues",
     "Carbon dioxide can no longer enter the chloroplast",
     "Chlorophyll can no longer absorb light of any wavelength"],
   ans=0,
   why="EK 3.4.B.5 makes the flow of protons back through ATP synthase by chemiosmosis the step that drives ATP formation, and EK 3.4.B.4 makes that flow depend on a gradient across the thylakoid membrane. A leaky membrane removes the gradient the mechanism requires."),

 dict(q="An illuminated chloroplast is supplied with light and water but no carbon dioxide. What is the most reasonable prediction about carbohydrate production?",
   choices=[
     "It stops, because carbon dioxide supplies the carbon that carbohydrate is built from",
     "It continues, because ATP and NADPH alone are enough to build carbohydrate",
     "It rises, because no carbon dioxide is competing with water for the light reactions",
     "It continues, because carbohydrate is built from the oxygen released by water splitting",
     "It stops, because chlorophyll cannot absorb light without carbon dioxide"],
   ans=0,
   why="EK 3.4.A.1 names carbon dioxide among the inputs and EK 3.4.B.6 makes carbohydrate production a conversion of carbon dioxide powered by ATP and NADPH. Without the carbon source the powering molecules have nothing to build from."),

 dict(q="An inhibitor blocks photosystem I specifically. Which product of the light reactions is most directly affected?",
   choices=[
     "NADPH, because NADP+ is reduced in photosystem I",
     "Oxygen, because water splits in photosystem I",
     "Carbohydrate, because it is assembled in photosystem I",
     "Carbon dioxide, because it is taken up in photosystem I",
     "Chlorophyll, because it is synthesized in photosystem I"],
   ans=0,
   why="EK 3.4.B.1 places the transfer of electrons to NADP+, reducing it to NADPH, in photosystem I. The splitting of water belongs to photosystem II under EK 3.4.B.2, and carbohydrate is assembled in the stroma under EK 3.4.B.6."),

 dict(q="Which molecule supplies the carbon atoms that end up in the carbohydrate a plant makes?",
   choices=[
     "Carbon dioxide",
     "Water",
     "Oxygen",
     "ATP",
     "NADPH"],
   ans=0,
   why="EK 3.4.A.1 names carbon dioxide as an input and carbohydrate as a product, and EK 3.4.B.6 describes the production of carbohydrates FROM CARBON DIOXIDE in the Calvin cycle. ATP and NADPH supply energy rather than carbon."),

 dict(q="What does the framework say photosynthetic organisms do with the sugars they produce?",
   choices=[
     "Use them in biological processes or store them",
     "Release all of them into the surroundings immediately",
     "Convert all of them back into carbon dioxide within the chloroplast",
     "Use them only to build more chlorophyll",
     "Store them only, since they cannot be used directly"],
   ans=0,
   why="EK 3.4.A.1.i states that photosynthetic organisms capture energy from the sun and produce sugars that can be used in biological processes or stored. Both fates are named."),

 dict(q="An investigator claims that the oxygen in the early atmosphere came from photosynthetic prokaryotes. Which reasoning connects that claim to the framework?",
   choices=[
     "Photosynthesis releases oxygen and first evolved in prokaryotes, so early prokaryotes were the available source",
     "Oxygen is required for photosynthesis, so more prokaryotes meant more oxygen consumed",
     "Prokaryotes lack chloroplasts, so the oxygen must have come from elsewhere",
     "Eukaryotic photosynthesis evolved first, so eukaryotes were the source",
     "Oxygen is a product of the Calvin cycle, which occurs only in prokaryotes"],
   ans=0,
   why="Skill 6.B asks that a claim be supported with evidence from biological processes. EK 3.4.A.1 makes oxygen a product of photosynthesis, EK 3.4.A.1.ii places the first photosynthesis in prokaryotes, and EK 3.4.A.1.iii states the conclusion those two support."),

 dict(q="Which pairing of chloroplast region with the reactions occurring there is correct?",
   choices=[
     "Grana with the light reactions and stroma with carbon fixation",
     "Grana with carbon fixation and stroma with the light reactions",
     "Grana with both sets of reactions and stroma with neither",
     "Stroma with both sets of reactions and grana with neither",
     "Grana with carbon fixation and the outer membrane with the light reactions"],
   ans=0,
   why="EK 3.4.A.2.iii places the light reactions in the grana and EK 3.4.A.2.i places the carbon fixation reactions of the Calvin cycle in the stroma. The two sets of reactions occupy different regions of the same organelle."),

 dict(q="Which statement about photosynthesis is NOT supported by the framework?",
   choices=[
     "The proton concentration is higher in the stroma than inside the thylakoid",
     "Photosystems I and II are connected by an electron transport chain",
     "Water splitting replaces electrons lost from photosystem II",
     "The light reactions yield ATP and NADPH",
     "Carbon fixation occurs in the stroma"],
   ans=0,
   why="EK 3.4.B.4 states the gradient in the opposite direction, low outside the thylakoid membrane and high inside it. The other four statements restate EK 3.4.B.3, EK 3.4.B.2, EK 3.4.A.3 and EK 3.4.A.2.i directly."),

 dict(q="Taken together, how do the light reactions and the Calvin cycle depend on one another in a chloroplast?",
   choices=[
     "The light reactions supply the ATP and NADPH that the Calvin cycle uses to build carbohydrate from carbon dioxide",
     "The Calvin cycle supplies the ATP and NADPH that the light reactions use to split water",
     "The two sets of reactions occur in different organelles and do not interact",
     "The light reactions build carbohydrate and the Calvin cycle releases oxygen",
     "Both sets of reactions occur inside the thylakoid and use the same inputs"],
   ans=0,
   why="EK 3.4.A.3 and EK 3.4.B.6 both state the dependence in this direction: the light reactions yield ATP and NADPH, and that energy powers the production of carbohydrates from carbon dioxide in the Calvin cycle in the stroma."),
]
