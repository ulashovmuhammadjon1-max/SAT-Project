# AP BIOLOGY 3.1 Enzymes
# CED effective Fall 2025, Unit 3 Cellular Energetics. Big Idea 2 Energetics.
# Learning objective 3.1.A, explain how enzymes affect the rate of biological
# reactions. Suggested skills 1.B (explain biological concepts and processes)
# and 3.C (identify experimental procedures that align with the question,
# including identifying dependent and independent variables, identifying
# appropriate controls, and justifying appropriate controls).
#
# Essential knowledge, in the framework's own terms:
#   3.1.A.1  The structure and function of enzymes contribute to the regulation
#            of biological processes. Enzymes are proteins that are biological
#            catalysts that facilitate chemical reactions in cells by lowering
#            the activation energy.
#   3.1.A.2  For an enzyme-mediated chemical reaction to occur, the shape and
#            charge of the substrate must be compatible with the active site of
#            the enzyme. This is illustrated by the enzyme-substrate complex
#            model.
#
# BOUNDARY WITH 3.2, HELD DELIBERATELY. Temperature, pH, denaturation,
# inhibitors and the relative concentrations of substrate and product are all
# essential knowledge of topic 3.2, not of this one, and no key in this module
# rests on them. What is left to 3.1 is what the two statements above actually
# say -- catalysis by lowering activation energy, and compatibility of shape
# and charge with the active site -- worked through the topic's own second
# suggested skill, 3.C, which is why a third of the module is experimental
# design. That skill belongs to this topic in the CED and to no other in
# Unit 3.
#
# Tables are labelled HYPOTHETICAL and every keyed conclusion is recoverable
# from the table itself.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("3.1", "Enzymes", 3)

_T_RATE = dict(
    headers=["Tube (hypothetical)", "Enzyme added (micrograms)",
             "Substrate converted in five minutes (micromoles)"],
    rows=[["Tube 1", "0", "0"],
          ["Tube 2", "5", "20"],
          ["Tube 3", "10", "40"],
          ["Tube 4", "20", "80"]])

_T_EA = dict(
    headers=["Reaction (hypothetical)",
             "Activation energy with no enzyme present (kilojoules per mole)",
             "Activation energy with the enzyme present (kilojoules per mole)"],
    rows=[["Reaction W", "75", "30"],
          ["Reaction X", "60", "24"],
          ["Reaction Y", "90", "36"],
          ["Reaction Z", "45", "18"]])

_T_SPEC = dict(
    headers=["Enzyme (hypothetical)",
             "Product formed with substrate A (micromoles)",
             "Product formed with substrate B (micromoles)",
             "Product formed with substrate C (micromoles)"],
    rows=[["Enzyme 1", "45", "0", "0"],
          ["Enzyme 2", "0", "38", "0"],
          ["Enzyme 3", "0", "0", "52"]])

QUESTIONS = [
 dict(q="According to the framework, how does an enzyme increase the rate of a chemical reaction in a cell?",
   choices=[
     "By lowering the activation energy the reaction must overcome",
     "By adding energy to the reactants until they break apart",
     "By raising the temperature of the surrounding cytosol",
     "By converting the reactants into a different set of products than would otherwise form",
     "By removing the need for the reactants to come into contact"],
   ans=0,
   why="EK 3.1.A.1 states that enzymes are biological catalysts that facilitate chemical reactions in cells by lowering the activation energy. Lowering a barrier is not the same as supplying energy or heating the surroundings."),

 dict(q="What class of macromolecule does the framework identify enzymes as belonging to?",
   choices=[
     "Proteins",
     "Nucleic acids",
     "Carbohydrates",
     "Phospholipids",
     "Steroids"],
   ans=0,
   why="EK 3.1.A.1 states outright that enzymes are proteins that are biological catalysts. That identity is what makes an enzyme's shape, and therefore its active site, a consequence of its amino acid sequence."),

 dict(q="For an enzyme-mediated reaction to occur, what must be true of the substrate in relation to the enzyme?",
   choices=[
     "Its shape and its charge must both be compatible with the active site",
     "Its shape alone must match the active site, regardless of charge",
     "Its charge alone must match the active site, regardless of shape",
     "It must be larger than the enzyme that acts on it",
     "It must carry the same net charge as the whole enzyme molecule"],
   ans=0,
   why="EK 3.1.A.2 names both properties: for an enzyme-mediated chemical reaction to occur, the shape and charge of the substrate must be compatible with the active site of the enzyme. Compatibility is with the active site, not with the molecule as a whole."),

 dict(q="Which model does the framework use to illustrate the requirement that a substrate be compatible with an enzyme's active site?",
   choices=[
     "The enzyme-substrate complex model",
     "The fluid mosaic model",
     "The endosymbiotic model",
     "The chemiosmotic model",
     "The double helix model"],
   ans=0,
   why="EK 3.1.A.2 names the enzyme-substrate complex model as the illustration of that compatibility requirement. The other models named describe membranes, organelle origins, proton gradients and nucleic acid structure."),

 dict(q="An enzyme acts on one molecule in a cell and leaves a closely related molecule untouched. Which explanation is supported by the framework?",
   choices=[
     "Only one of the two molecules is compatible in shape and charge with the enzyme's active site",
     "Only one of the two molecules is present in the cell at any given moment",
     "Enzymes act at random and the untouched molecule was simply missed",
     "The untouched molecule has already had its activation energy lowered",
     "The enzyme can only act on the larger of any two molecules it encounters"],
   ans=0,
   why="EK 3.1.A.2 makes compatibility of shape and charge with the active site the condition for an enzyme-mediated reaction. Specificity follows from that condition rather than from availability or chance."),

 dict(q="A mutation replaces an amino acid in an enzyme's active site with one carrying the opposite electric charge. The substrate's shape still fits the site. What is the most reasonable prediction?",
   choices=[
     "The reaction slows or stops because charge compatibility has been lost",
     "The reaction is unaffected because only shape matters for binding",
     "The reaction speeds up because opposite charges attract every substrate",
     "The enzyme now acts on every substrate in the cell equally well",
     "The enzyme becomes a nucleic acid rather than a protein"],
   ans=0,
   why="EK 3.1.A.2 requires the shape AND the charge of the substrate to be compatible with the active site. Preserving one requirement while destroying the other leaves the pairing incompatible, which is why the reaction cannot proceed as before."),

 dict(q="Why does the framework describe enzymes as contributing to the regulation of biological processes rather than merely to their speed?",
   choices=[
     "Because which reactions a cell can run quickly depends on which enzymes it has available",
     "Because enzymes decide the order in which a cell's genes are copied",
     "Because enzymes supply the raw materials that biological processes consume",
     "Because enzymes prevent all uncatalyzed reactions from ever occurring",
     "Because enzymes replace the need for a cell to obtain energy"],
   ans=0,
   why="EK 3.1.A.1 opens by stating that the structure and function of enzymes contribute to the regulation of biological processes. A reaction with no available enzyme proceeds too slowly to matter, so controlling the enzyme is controlling the process."),

 dict(q="A student investigates how the amount of an enzyme affects the amount of product formed in a fixed time. Which is the independent variable?",
   choices=[
     "The amount of enzyme added to each tube",
     "The amount of product formed in each tube",
     "The length of time each tube is allowed to react",
     "The volume of solution in each tube",
     "The temperature at which the tubes are held"],
   ans=0,
   why="Skill 3.C asks students to identify dependent and independent variables. The independent variable is the one the investigator sets, here the enzyme amount; product formed is what is measured, and time, volume and temperature are held constant."),

 dict(q="In the same investigation, which quantity is the dependent variable?",
   choices=[
     "The amount of product formed in each tube",
     "The amount of enzyme added to each tube",
     "The identity of the substrate used",
     "The number of tubes prepared",
     "The size of the pipette used to fill the tubes"],
   ans=0,
   why="Skill 3.C asks students to identify dependent and independent variables. The dependent variable is the measured outcome that may respond to the treatment, which here is the amount of product formed."),

 dict(q="An investigator wants to show that the conversion of a substrate in a reaction mixture is due to the enzyme rather than to the substrate breaking down on its own. Which control is appropriate?",
   choices=[
     "A tube identical in every respect except that no enzyme is added",
     "A tube containing enzyme but no substrate",
     "A tube containing twice as much enzyme as the experimental tubes",
     "A tube containing a completely different enzyme and a different substrate",
     "A tube left out of the experiment entirely and not measured"],
   ans=0,
   why="Skill 3.C asks for appropriate controls and for a justification of them. The claim under test is that the enzyme is responsible, so the control must differ from the treatment in the enzyme alone and in nothing else."),

 dict(q="Why is a tube containing substrate but no enzyme the right comparison for an enzyme experiment, rather than simply reporting the treated tube's result?",
   choices=[
     "Without it, any conversion that would have happened anyway would be credited to the enzyme",
     "Without it, the treated tube cannot be measured accurately",
     "Without it, the enzyme cannot bind its substrate",
     "Without it, the experiment would have no independent variable",
     "Without it, the reaction would consume all of its activation energy"],
   ans=0,
   why="Skill 3.C asks students to JUSTIFY a control, not just name one. EK 3.1.A.1 makes the enzyme a catalyst of a reaction that can proceed uncatalyzed but slowly, so the untreated tube measures how much of the result the enzyme is not responsible for."),

 dict(q="Data from four reaction tubes are shown. Which conclusion do these results support?",
   table=_T_RATE,
   choices=[
     "No substrate is converted without enzyme, and the amount converted rises with the amount of enzyme",
     "Substrate is converted at the same rate whether or not enzyme is present",
     "The amount converted falls as more enzyme is added",
     "The tube with no enzyme converted more substrate than any other tube",
     "The amount converted is unrelated to the amount of enzyme added"],
   ans=0,
   why="The zero-enzyme tube converts nothing and the converted amount rises in step with enzyme added, which is EK 3.1.A.1's catalysis claim shown as data. Skill 4.B asks students to describe exactly this kind of relationship between variables."),

 dict(q="Using the same four tubes, which of them serves as the control for the investigation?",
   table=_T_RATE,
   choices=[
     "The tube to which no enzyme was added",
     "The tube to which the most enzyme was added",
     "The tube that converted the most substrate",
     "The tube to which an intermediate amount of enzyme was added",
     "Every tube serves equally as a control for the others"],
   ans=0,
   why="Skill 3.C asks students to identify appropriate controls. The control sets the independent variable to zero while everything else is unchanged, which in this table is the single tube receiving no enzyme."),

 dict(q="Activation energies were measured for four reactions with and without their enzymes, with the results shown. What do the data show?",
   table=_T_EA,
   choices=[
     "The enzyme lowers the activation energy of every reaction listed",
     "The enzyme raises the activation energy of every reaction listed",
     "The enzyme lowers the activation energy of some reactions and raises it for others",
     "The activation energy is unchanged by the presence of the enzyme",
     "The reaction with the highest activation energy without enzyme has the lowest with enzyme"],
   ans=0,
   why="Every value in the with-enzyme column is below the matching value in the without-enzyme column, which is EK 3.1.A.1's statement that enzymes facilitate reactions by lowering the activation energy shown as measurements."),

 dict(q="Three enzymes were each offered three substrates, with the results shown. Which property of enzymes do these results best illustrate?",
   table=_T_SPEC,
   choices=[
     "Each enzyme forms product with only one of the substrates offered",
     "Each enzyme forms product with every substrate offered",
     "The three enzymes are interchangeable with one another",
     "Product formation depends only on how much substrate is present",
     "Each substrate is acted on by all three enzymes to the same extent"],
   ans=0,
   why="Each row shows a single nonzero entry, so each enzyme acted on exactly one substrate. That is EK 3.1.A.2's compatibility requirement expressed as data: a substrate whose shape and charge do not suit the active site yields no product."),

 dict(q="A student concludes from an enzyme experiment that the enzyme was consumed by the reaction, because product stopped forming after several minutes. Which is the better explanation given how the framework describes enzymes?",
   choices=[
     "The available substrate was used up, while the enzyme, a catalyst, remained able to act",
     "The enzyme was permanently converted into product molecules",
     "The activation energy of the reaction increased as the reaction proceeded",
     "The substrate lost the ability to be recognized by any enzyme",
     "The enzyme became a nucleic acid once it had acted several times"],
   ans=0,
   why="EK 3.1.A.1 calls enzymes biological catalysts, and a catalyst lowers the activation energy of a reaction without being turned into its product. Exhaustion of substrate accounts for the same observation without contradicting that description."),

 dict(q="A cell needs to run a reaction that would otherwise proceed far too slowly to be useful. Which statement best describes what supplying the appropriate enzyme accomplishes?",
   choices=[
     "It makes a reaction that was already possible occur fast enough to be useful",
     "It makes a reaction possible that could not otherwise occur under any conditions",
     "It supplies the energy that the reaction was previously missing",
     "It changes which products the reaction forms",
     "It removes the substrate's requirement for a compatible partner"],
   ans=0,
   why="EK 3.1.A.1 describes enzymes as catalysts that facilitate reactions by lowering the activation energy, which is a statement about the rate at which a reaction proceeds rather than about whether it can occur at all."),

 dict(q="Two different enzymes in a cell act on the same substrate but form different products. What does the framework's account of enzyme action imply about them?",
   choices=[
     "Each has an active site the substrate is compatible with, and each catalyzes its own reaction",
     "One of the two enzymes must be inactive at all times",
     "The substrate must change its shape before either enzyme can act",
     "The two enzymes must have identical amino acid sequences",
     "Only the enzyme with the larger active site can act on the substrate"],
   ans=0,
   why="EK 3.1.A.2 requires compatibility between substrate and active site for a reaction to occur, and EK 3.1.A.1 makes each enzyme the catalyst of its own reaction. Compatibility with two different active sites is possible and is what the observation reports."),

 dict(q="Which of these is the best statement of what an enzyme-substrate complex is?",
   choices=[
     "The association formed when a compatible substrate occupies an enzyme's active site",
     "The product molecule that leaves the enzyme after the reaction",
     "The whole set of enzymes a cell produces at one time",
     "A protein that has lost its shape and can no longer act",
     "The energy barrier that must be overcome for a reaction to occur"],
   ans=0,
   why="EK 3.1.A.2 introduces the enzyme-substrate complex model as the illustration of substrate and active site compatibility, so the complex is the enzyme and the substrate joined at that site rather than the product, the barrier or the enzyme collection."),

 dict(q="An investigator claims that a purified protein is an enzyme for a particular reaction. Which result would most directly support that claim?",
   choices=[
     "The reaction proceeds much faster with the protein present than in an otherwise identical mixture without it",
     "The protein has a molecular mass typical of enzymes",
     "The protein is found in the same organelle as the substrate",
     "The reaction proceeds slowly whether or not the protein is present",
     "The protein binds tightly to many unrelated molecules"],
   ans=0,
   why="Skill 6.B asks for evidence connected to the claim. EK 3.1.A.1 defines an enzyme by what it does to reaction rate, so the supporting evidence is a rate comparison against a control differing only in the protein."),

 dict(q="A student sets up two tubes to test an enzyme, but adds a different substrate to each as well as a different amount of enzyme. What is the flaw in this design?",
   choices=[
     "Two variables change at once, so a difference in the results cannot be assigned to either one",
     "Two tubes are too few to run any experiment",
     "The student has failed to identify a dependent variable",
     "Enzymes cannot be tested in tubes at all",
     "The substrates would each need their own enzyme in the same tube"],
   ans=0,
   why="Skill 3.C requires procedures aligned with the question being asked. When treatment and substrate differ together, the outcome is consistent with either cause, so the design cannot answer the question it was built for."),

 dict(q="Which change to a substrate molecule would be most likely to prevent an enzyme from acting on it?",
   choices=[
     "A change that alters the region of the substrate that fits into the active site",
     "A change to a part of the substrate far from the active site that alters neither shape nor charge there",
     "A change that leaves the substrate's shape and charge exactly as they were",
     "A change that makes the substrate more abundant in the cell",
     "A change that moves the substrate into a different part of the same compartment"],
   ans=0,
   why="EK 3.1.A.2 makes compatibility of the substrate's shape and charge with the active site the condition for the reaction. Only an alteration at the region that must fit the site removes that compatibility."),

 dict(q="How does the framework connect an enzyme's structure to what it does?",
   choices=[
     "Its structure creates an active site with a particular shape and charge, which determines what it acts on",
     "Its structure determines how much energy it releases when it acts",
     "Its structure determines which organelle the cell will build next",
     "Its structure has no bearing on function, only its abundance does",
     "Its structure changes the products of any reaction it encounters"],
   ans=0,
   why="EK 3.1.A.1 opens with the structure AND function of enzymes, and EK 3.1.A.2 supplies the link: the shape and charge of the substrate must be compatible with the active site, and the active site is a feature of the protein's structure."),

 dict(q="Which of these would be the most informative next experiment for an investigator who has shown that a reaction runs faster with a certain protein present?",
   choices=[
     "Testing whether the same protein also speeds up closely related reactions",
     "Measuring how many tubes can be prepared in one afternoon",
     "Weighing the empty tubes before the reagents are added",
     "Recording the color of the reagent bottles used",
     "Counting how many students performed the procedure"],
   ans=0,
   why="Skill 3.C asks for procedures aligned to the question. EK 3.1.A.2's compatibility requirement predicts that a genuine enzyme will act on some related molecules and not others, so testing the range of substrates is the informative follow-up."),

 dict(q="Which statement about enzymes and activation energy is NOT supported by the framework?",
   choices=[
     "An enzyme eliminates the activation energy of a reaction entirely",
     "An enzyme lowers the activation energy of the reaction it catalyzes",
     "An enzyme is a protein",
     "An enzyme facilitates chemical reactions in cells",
     "An enzyme's active site must be compatible with its substrate"],
   ans=0,
   why="EK 3.1.A.1 says enzymes lower the activation energy; it does not say they abolish it, and the other four statements restate EK 3.1.A.1 and EK 3.1.A.2 directly."),

 dict(q="Using the measured activation energies, by what fraction does the enzyme reduce the barrier in these four reactions?",
   table=_T_EA,
   choices=[
     "By the same fraction in every one of the four reactions",
     "By a larger fraction in the reaction with the highest barrier",
     "By a larger fraction in the reaction with the lowest barrier",
     "By a fraction that cannot be determined from the values given",
     "By no measurable fraction in any of the four reactions"],
   ans=0,
   why="Dividing each with-enzyme value by its matching without-enzyme value gives the same ratio in all four rows, so the proportional reduction is identical even though the absolute reductions differ. Skill 5.A calls for exactly this kind of ratio calculation."),

 dict(q="Suppose an investigator repeats an enzyme assay and finds that the tube with no enzyme also converts a small amount of substrate. What does that result tell the investigator?",
   choices=[
     "Some conversion occurs without the enzyme, so the enzyme's contribution is the difference between the tubes",
     "The experiment must be discarded because a control may never show any result",
     "The enzyme is not a catalyst after all",
     "The substrate has been contaminated with product and no conclusion is possible",
     "The activation energy of the uncatalyzed reaction must be zero"],
   ans=0,
   why="Skill 3.C's justification of a control is exactly this reasoning: EK 3.1.A.1 makes the enzyme a catalyst of a reaction that can also proceed slowly on its own, so the control measures the background and the enzyme's effect is what remains."),

 dict(q="Two cells contain the same substrate, but only one of them makes the enzyme for a particular reaction. What follows about that reaction in the two cells?",
   choices=[
     "It proceeds rapidly only in the cell that makes the enzyme",
     "It proceeds rapidly in both cells because the substrate is present in both",
     "It proceeds rapidly only in the cell that lacks the enzyme",
     "It cannot occur in either cell without an additional substrate",
     "It occurs at the same rate in both cells regardless of the enzyme"],
   ans=0,
   why="EK 3.1.A.1 makes the enzyme the reason a reaction runs fast enough to matter and makes that the mechanism by which enzymes contribute to the regulation of biological processes. Which enzymes a cell has is therefore what distinguishes the two cells."),

 dict(q="Which observation would most strongly suggest that a protein is NOT the enzyme for a reaction under study?",
   choices=[
     "Adding the protein leaves the reaction rate the same as in a mixture without it",
     "Adding the protein leaves some substrate unconverted after five minutes",
     "The protein binds its substrate before the reaction occurs",
     "The protein is present in the cell in small amounts",
     "The reaction has a high activation energy when the protein is absent"],
   ans=0,
   why="EK 3.1.A.1 defines an enzyme by its effect on the rate at which a reaction proceeds. A protein that leaves the rate unchanged has failed the only test that defines the category; the other observations are all compatible with the protein being the enzyme."),

 dict(q="Taken together, what do the framework's two statements about enzymes assert?",
   choices=[
     "That enzymes are protein catalysts that lower activation energy, and that they act only on substrates compatible with their active sites",
     "That enzymes are nucleic acids that raise activation energy, and that they act on any substrate",
     "That enzymes supply energy to reactions and are consumed in doing so",
     "That enzymes determine the products of every reaction in a cell",
     "That enzymes work only outside cells and never inside them"],
   ans=0,
   why="EK 3.1.A.1 gives the identity and the mechanism, protein catalysts that lower activation energy inside cells, and EK 3.1.A.2 gives the condition, compatibility of the substrate's shape and charge with the active site."),
]
