r"""AP CHEMISTRY 3.9 Separation of Solutions and Mixtures.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.9.A: explain the results of a separation experiment based
on intermolecular interactions.
Suggested skill 2.C, identify experimental procedures that are aligned to the
question.

Essential knowledge relied on, in the framework's own words:

  3.9.A.1  The components of a liquid solution cannot be separated by
           filtration. They can, however, be separated using processes that take
           advantage of differences in the intermolecular interactions of the
           components.
             i. Chromatography (paper, thin-layer, and column) separates
                chemical species by taking advantage of the differential
                strength of intermolecular interactions between and among the
                components of the solution (the mobile phase) and with the
                surface components of the stationary phase. The resulting
                chromatogram can be used to infer the relative polarities of
                components in a mixture.
            ii. [NOT PRESENT IN THIS SOURCE -- see below]

A HOLE IN THE SOURCE, AND WHAT IS DONE ABOUT IT. EK 3.9.A.1 has a second
sub-point and its text is NOT in the CED PDF's text layer: the page ends at a
bare "ii." and the next page opens topic 3.10. This is the same situation
SCIENCE_RESUME.md records for the Biology CED's exocytosis sub-point, and it
gets the same treatment: **nothing here keys a second separation method.** A
guess would probably be right and would still be a guess, which is precisely
what this project's rules forbid. verify_h3_9.py asserts that no key names
distillation, evaporation, crystallisation or centrifugation as a method the
framework offers; those words appear only as distractors, where they are wrong
for reasons that do not depend on the missing sub-point.

THE DIRECTION OF TRAVEL IS SUPPLIED BY THE STEM. EK 3.9.A.1 says chromatography
exploits the DIFFERENTIAL STRENGTH of intermolecular interactions and that the
chromatogram can be used to infer relative polarities. It does not state which
way round the distances run -- that a species held more strongly by the
stationary phase travels a shorter distance. So every item whose key depends on
that convention SAYS SO IN ITS OWN STEM, and verify_h3_9.py asserts it. The
question then tests the reasoning rather than a fact the source does not carry.

WHERE POLARITY ENTERS, IT IS CITED. EK 3.9.A.1 sanctions inferring RELATIVE
polarities from a chromatogram; EK 3.1.A.2 supplies why a polar species is held
harder by a polar surface, since interactions between polar molecules are
typically greater than those between nonpolar molecules of comparable size.
Both are named in the rationales that use them.

NO FIGURES. Every chromatogram is a table of distances.

ARITHMETIC. Every distance comparison a key asserts is recomputed in
verify_h3_9.py from the table alone.

NOTATION. Plain prose; no math spans are needed in this module.
"""
TOPIC = ("3.9", "Separation of Solutions and Mixtures", 3)

# One chromatogram, given as distances rather than as a picture. Ratios to the
# solvent front recompute to 0.25, 0.75 and 0.50.
_T_CHROM = dict(
    headers=["Component", "Distance travelled by the component (cm)",
             "Distance travelled by the solvent front (cm)"],
    rows=[["Component 1", "2.0", "8.0"],
          ["Component 2", "6.0", "8.0"],
          ["Component 3", "4.0", "8.0"]])

# The same mixture run twice, once on a polar stationary phase and once on a
# nonpolar one.
_T_TWO = dict(
    headers=["Component", "Distance on the polar stationary phase (cm)",
             "Distance on the nonpolar stationary phase (cm)"],
    rows=[["Component X", "1.0", "7.0"],
          ["Component Y", "7.0", "1.0"],
          ["Component Z", "4.0", "4.0"]])

QUESTIONS = [

 dict(q="What does the framework say about separating the components of a liquid solution by "
        "filtration?",
      choices=[
        "They cannot be separated by filtration",
        "They can be separated by filtration if the filter paper is fine enough",
        "They can be separated by filtration only when the solution is cooled",
        "They can be separated by filtration only when the solvent is water",
        "The framework says nothing about filtration"],
      ans=0,
      why="EK 3.9.A.1 opens by stating that the components of a liquid solution cannot be "
          "separated by filtration. The claim is unqualified, so no detail of the apparatus "
          "or the conditions rescues the method."),

 dict(q="What kind of processes does the framework say CAN separate the components of a "
        "liquid solution?",
      choices=[
        "Processes that take advantage of differences in the intermolecular interactions of "
        "the components",
        "Processes that take advantage of differences in the molar masses of the components",
        "Processes that take advantage of differences in the colours of the components",
        "Processes that take advantage of the size of the pores in a filter",
        "Processes that take advantage of differences in the covalent bonds within each "
        "component"],
      ans=0,
      why="EK 3.9.A.1 says they can be separated using processes that take advantage of "
          "differences in the intermolecular interactions of the components. The forces "
          "inside each molecule hold that molecule together and are not what distinguishes "
          "one component's behaviour from another's here."),

 dict(q="Which three forms of chromatography does the framework name?",
      choices=[
        "Paper, thin-layer, and column",
        "Paper, distillation, and evaporation",
        "Column, centrifugation, and filtration",
        "Thin-layer, crystallisation, and filtration",
        "Paper, column, and filtration"],
      ans=0,
      why="EK 3.9.A.1's first sub-point lists chromatography as paper, thin-layer, and "
          "column. Filtration is the one method the same statement rules out for a liquid "
          "solution, so it cannot appear on a list of chromatographic forms."),

 dict(q="What does the framework say chromatography takes advantage of in order to separate "
        "chemical species?",
      choices=[
        "The differential strength of intermolecular interactions",
        "The differential strength of covalent bonds within each species",
        "Differences in the mass of each species",
        "Differences in the colour of each species",
        "Differences in the boiling point of each species"],
      ans=0,
      why="EK 3.9.A.1's first sub-point says chromatography separates chemical species by "
          "taking advantage of the differential strength of intermolecular interactions. The "
          "word differential matters: it is the difference between species that does the "
          "separating."),

 dict(q="In the framework's description of chromatography, which part of the system is the "
        "mobile phase?",
      choices=[
        "The components of the solution",
        "The surface components of the stationary phase",
        "The paper or the column itself",
        "The container holding the apparatus",
        "The atmosphere above the apparatus"],
      ans=0,
      why="EK 3.9.A.1's first sub-point names the components of the solution as the mobile "
          "phase in a parenthesis, and sets them against the surface components of the "
          "stationary phase."),

 dict(q="With what does the framework say the mobile phase interacts, besides itself?",
      choices=[
        "The surface components of the stationary phase",
        "The interior of the stationary phase, below its surface",
        "The walls of the room in which the experiment is performed",
        "The covalent bonds inside the stationary phase",
        "Nothing; the mobile phase interacts only with itself"],
      ans=0,
      why="EK 3.9.A.1's first sub-point names interactions between and among the components "
          "of the solution AND with the surface components of the stationary phase. It is "
          "the surface that the sentence specifies."),

 dict(q="What does the framework say the resulting chromatogram can be used to infer?",
      choices=[
        "The relative polarities of components in a mixture",
        "The absolute molar mass of each component",
        "The exact concentration of each component in moles per litre",
        "The boiling point of each component",
        "The number of covalent bonds in each component"],
      ans=0,
      why="EK 3.9.A.1's first sub-point says the resulting chromatogram can be used to infer "
          "the relative polarities of components in a mixture. It is a comparison among the "
          "components rather than a measured value for any one of them."),

 dict(q="A student proposes to separate the components of a liquid solution by pouring it "
        "through filter paper. What does the framework say about that plan?",
      choices=[
        "It will not separate them, because the components of a liquid solution cannot be "
        "separated by filtration",
        "It will separate them, provided the filter paper is fine enough",
        "It will separate them, provided the solution is first cooled",
        "It will separate them only if one component is coloured",
        "It will separate them only if the solvent is nonpolar"],
      ans=0,
      why="EK 3.9.A.1's opening sentence rules the method out for this kind of sample "
          "outright, which is exactly the judgement suggested skill 2.C asks for: deciding "
          "whether a proposed procedure is aligned to the question being asked."),

 dict(q="A chemist wants to know which of two dissolved substances is the more polar. Which "
        "procedure is aligned to that question, according to the framework?",
      choices=[
        "Paper chromatography, since the resulting chromatogram can be used to infer relative "
        "polarities",
        "Filtration, since the more polar substance is held back by the filter",
        "Weighing the residue left after evaporation, since polarity follows mass",
        "Measuring the total volume of the solution before and after mixing",
        "Counting the number of components visible to the eye"],
      ans=0,
      why="EK 3.9.A.1's first sub-point ends by saying the resulting chromatogram can be used "
          "to infer the relative polarities of components in a mixture, so a chromatographic "
          "procedure is the one aligned to a question about relative polarity. The same "
          "statement's opening sentence rules filtration out for a liquid solution."),

 dict(q="The table reports how far each component of a mixture travelled on one plate. Which "
        "component interacts most strongly with the stationary phase? In this experiment a "
        "component that interacts more strongly with the stationary phase travels a shorter "
        "distance.",
      table=_T_CHROM,
      choices=[
        "Component 1",
        "Component 2",
        "Component 3",
        "All three interact equally strongly",
        "It cannot be decided from distances alone"],
      ans=0,
      why="EK 3.9.A.1's first sub-point makes the differential strength of intermolecular "
          "interactions the basis of the separation, and the stem supplies the convention "
          "linking a stronger interaction to a shorter distance. The tabulated distances then "
          "settle it directly."),

 dict(q="Using the same tabulated plate, which component interacts LEAST strongly with the "
        "stationary phase? A component that interacts more strongly with the stationary phase "
        "travels a shorter distance in this experiment.",
      table=_T_CHROM,
      choices=[
        "Component 2",
        "Component 1",
        "Component 3",
        "All three interact equally strongly",
        "It cannot be decided from distances alone"],
      ans=0,
      why="The same convention read the other way: the component carried furthest by the "
          "mobile phase is the one the stationary phase holds least. EK 3.9.A.1 makes that "
          "difference in interaction strength the whole mechanism of the separation."),

 dict(q="The stationary phase used for the tabulated plate is polar. Which component is the "
        "LEAST polar? A component that interacts more strongly with the stationary phase "
        "travels a shorter distance in this experiment.",
      table=_T_CHROM,
      choices=[
        "Component 2",
        "Component 1",
        "Component 3",
        "All three are equally polar",
        "Polarity cannot be inferred from a chromatogram"],
      ans=0,
      why="EK 3.9.A.1's first sub-point says the chromatogram can be used to infer the "
          "relative polarities of components, and EK 3.1.A.2 supplies the link: interactions "
          "between polar molecules are typically greater than those between nonpolar "
          "molecules of comparable size, so a polar surface holds a polar species harder. "
          "With the stem's convention, the component carried furthest is the least polar."),

 dict(q="For how many of the tabulated components did the component travel more than half as "
        "far as the solvent front?",
      table=_T_CHROM,
      choices=[
        "Exactly one",
        "Exactly two",
        "All three",
        "None of them",
        "It cannot be decided without the identity of the solvent"],
      ans=0,
      why="Each tabulated component distance is compared with the tabulated solvent front "
          "distance for that run, and the framework's differential-strength account is what "
          "makes those ratios differ from one another in the first place."),

 dict(q="The same mixture was run on two plates, one with a polar stationary phase and one "
        "with a nonpolar stationary phase. Which component interacts most strongly with the "
        "POLAR stationary phase? A component that interacts more strongly with the stationary "
        "phase travels a shorter distance.",
      table=_T_TWO,
      choices=[
        "Component X",
        "Component Y",
        "Component Z",
        "All three interact equally strongly with it",
        "It cannot be decided without running a third plate"],
      ans=0,
      why="EK 3.9.A.1 makes the differential strength of intermolecular interactions with the "
          "surface components of the stationary phase the basis of the separation, and the "
          "stem supplies the convention. The shortest tabulated distance on the polar plate "
          "identifies the component that surface holds hardest."),

 dict(q="Which tabulated component behaved the same way on both plates? A component that "
        "interacts more strongly with the stationary phase travels a shorter distance.",
      table=_T_TWO,
      choices=[
        "Component Z",
        "Component X",
        "Component Y",
        "All three behaved the same way on both",
        "None of them behaved the same way on both"],
      ans=0,
      why="EK 3.9.A.1 attributes the separation to differences in interaction strength, so a "
          "component that travels the same distance on a polar and a nonpolar surface is one "
          "the two surfaces hold about equally. The tabulated distances identify it."),

 dict(q="Which two tabulated components exchanged their positions between the polar plate and "
        "the nonpolar plate? A component that interacts more strongly with the stationary "
        "phase travels a shorter distance.",
      table=_T_TWO,
      choices=[
        "Components X and Y",
        "Components X and Z",
        "Components Y and Z",
        "All three exchanged positions",
        "No two of them exchanged positions"],
      ans=0,
      why="EK 3.9.A.1's differential-strength account allows one surface to hold a species "
          "that another barely holds, and the tabulated distances show exactly one pair whose "
          "two readings are each other's exchanged between the two plates."),

 dict(q="Taking the polar plate as the guide, which tabulated component is the LEAST polar? A "
        "component that interacts more strongly with the stationary phase travels a shorter "
        "distance.",
      table=_T_TWO,
      choices=[
        "Component Y",
        "Component X",
        "Component Z",
        "All three are equally polar",
        "Polarity cannot be inferred from these data"],
      ans=0,
      why="EK 3.9.A.1's first sub-point sanctions inferring relative polarities from a "
          "chromatogram, and EK 3.1.A.2 makes a polar surface hold a polar species harder "
          "than a nonpolar one of comparable size. Under the stem's convention, the component "
          "carried furthest on the polar plate is held least by it."),

 dict(q="Which interactions does the framework name as relevant to a chromatographic "
        "separation?",
      choices=[
        "Those between and among the components of the solution, and those with the surface "
        "components of the stationary phase",
        "Only those among the components of the solution",
        "Only those with the surface components of the stationary phase",
        "Only the covalent bonds within each component",
        "Only the interactions between the apparatus and the surrounding air"],
      ans=0,
      why="EK 3.9.A.1's first sub-point names both: interactions between and among the "
          "components of the solution, which it calls the mobile phase, and interactions with "
          "the surface components of the stationary phase. Dropping either half loses part of "
          "what the sentence attributes the separation to."),

 dict(q="The framework says chromatography exploits the DIFFERENTIAL strength of "
        "intermolecular interactions. What does that word require?",
      choices=[
        "That the components differ from one another in how strongly they interact",
        "That the interactions are stronger than covalent bonds",
        "That every component interacts equally strongly",
        "That the interactions change over the course of the experiment",
        "That the interactions be measured in absolute units before the run"],
      ans=0,
      why="EK 3.9.A.1's first sub-point attributes the separation to the DIFFERENTIAL "
          "strength of the interactions, which is a comparison between species. Interactions "
          "of equal strength would give every component the same behaviour and so no "
          "separation at all."),

 dict(q="Two components of a mixture happen to interact identically with both the mobile "
        "phase and the stationary phase. What does the framework's account predict?",
      choices=[
        "They will not be separated from each other",
        "They will be separated, but only slowly",
        "They will be separated, since every mixture separates eventually",
        "They will be separated if the plate is made longer",
        "They will be separated if the stationary phase is made polar"],
      ans=0,
      why="EK 3.9.A.1's first sub-point makes the DIFFERENTIAL strength of the interactions "
          "the thing chromatography takes advantage of, so where there is no difference there "
          "is nothing for the method to exploit. Lengthening the plate multiplies a "
          "difference of zero."),

 dict(q="Which of these is NOT one of the three forms of chromatography the framework names?",
      choices=[
        "Gas chromatography",
        "Paper chromatography",
        "Thin-layer chromatography",
        "Column chromatography",
        "The framework names all four of these"],
      ans=0,
      why="EK 3.9.A.1's first sub-point gives the list in a parenthesis as paper, thin-layer, "
          "and column. Other separations exist in a laboratory, but the framework's list has "
          "three entries and this one is not among them."),

 dict(q="What does the framework say the stationary phase contributes to the separation?",
      choices=[
        "Its surface components, which interact with the species being separated",
        "Its total mass, which holds the plate steady",
        "Its colour, which makes the components visible",
        "Its temperature, which drives the components upward",
        "Its thickness, which filters the larger components out"],
      ans=0,
      why="EK 3.9.A.1's first sub-point names interactions with the SURFACE COMPONENTS of the "
          "stationary phase. Filtering by size is the mechanism the same statement's opening "
          "sentence rules out for a liquid solution."),

 dict(q="A chemist asks which of two dyes is held more strongly by a polar surface. Which "
        "procedure is aligned to that question?",
      choices=[
        "Running a chromatogram with a polar stationary phase and comparing how far each dye "
        "travels",
        "Filtering the dye solution and weighing what remains on the paper",
        "Measuring the volume of dye solution used",
        "Comparing the two dyes by eye without any separation",
        "Measuring how long the solution takes to be prepared"],
      ans=0,
      why="EK 3.9.A.1's first sub-point makes interaction with the surface components of the "
          "stationary phase the basis of the separation and the chromatogram the record of "
          "it, so a chromatographic run on the surface in question is the procedure aligned "
          "to the question, which is what suggested skill 2.C asks a student to identify."),

 dict(q="A mixture of one polar and one nonpolar substance is run on a polar stationary "
        "phase. Which travels further? A component that interacts more strongly with the "
        "stationary phase travels a shorter distance.",
      choices=[
        "The nonpolar substance, since a polar surface holds a polar substance more strongly",
        "The polar substance, since a polar surface holds a polar substance more strongly",
        "The nonpolar substance, since a polar surface holds a nonpolar substance more "
        "strongly",
        "The polar substance, since polar substances always move faster",
        "Neither, since polarity has no effect on a chromatographic run"],
      ans=0,
      why="EK 3.1.A.2 makes interactions between polar molecules typically greater than those "
          "between nonpolar molecules of comparable size, so a polar surface holds the polar "
          "component harder; EK 3.9.A.1 makes that difference the basis of the separation, "
          "and the stem's convention turns the stronger hold into the shorter distance."),

 dict(q="Which of these does the framework explicitly rule out as a way of separating the "
        "components of a liquid solution?",
      choices=[
        "Filtration",
        "Paper chromatography",
        "Thin-layer chromatography",
        "Column chromatography",
        "Any process exploiting differences in intermolecular interactions"],
      ans=0,
      why="EK 3.9.A.1's opening sentence names filtration and says the components of a liquid "
          "solution cannot be separated by it. The four rejected options are each either a "
          "form of chromatography the same statement lists or the general description it "
          "gives of what does work."),

 dict(q="The framework says a chromatogram can be used to infer the RELATIVE polarities of "
        "components. What does that word limit?",
      choices=[
        "The chromatogram ranks the components against one another rather than giving an "
        "absolute polarity for any of them",
        "The chromatogram gives an absolute polarity for each component in standard units",
        "The chromatogram applies only to components that are all polar",
        "The chromatogram applies only to components that are all nonpolar",
        "The chromatogram gives the polarity of the stationary phase rather than of the "
        "components"],
      ans=0,
      why="EK 3.9.A.1's first sub-point speaks of the RELATIVE polarities of components in a "
          "mixture. A run compares the species with each other on one plate, which is enough "
          "to order them and not enough to fix a value for any one of them."),

 dict(q="Two components of a mixture end up at different places after a chromatographic run. "
        "What does the framework give as the basis of that outcome?",
      choices=[
        "Differences in the strength of their intermolecular interactions with the mobile and "
        "stationary phases",
        "Differences in the strength of the covalent bonds within each of them",
        "Differences in their masses, with the heavier one left behind",
        "Differences in their colours, which the plate sorts",
        "Differences in the time at which each was added to the plate"],
      ans=0,
      why="EK 3.9.A.1's first sub-point attributes the separation to the differential strength "
          "of intermolecular interactions between and among the components of the solution "
          "and with the surface components of the stationary phase. Intramolecular bonds and "
          "masses are not what the sentence names."),

 dict(q="The framework's claim that filtration cannot separate the components is made about "
        "which kind of sample?",
      choices=[
        "A liquid solution",
        "Any mixture whatsoever",
        "A mixture of two solids",
        "A mixture of two gases",
        "A pure substance"],
      ans=0,
      why="EK 3.9.A.1 begins with the components of a LIQUID SOLUTION, and EK 3.7.A.1 makes a "
          "solution a homogeneous mixture whose macroscopic properties do not vary throughout "
          "the sample. A pure substance has no components to separate in the first place."),

 dict(q="Which question could a chromatogram answer, according to the framework?",
      choices=[
        "Which component of a mixture is the more polar",
        "What the molar mass of each component is",
        "How many moles of each component are present",
        "What the boiling point of the solvent is",
        "Whether the mixture is a pure substance"],
      ans=0,
      why="EK 3.9.A.1's first sub-point says the resulting chromatogram can be used to infer "
          "the relative polarities of components in a mixture, and that is the only inference "
          "the sentence sanctions. Amounts and molar masses need other measurements "
          "altogether."),

 dict(q="Which statement puts together what EK 3.9.A.1 says about separating a liquid "
        "solution?",
      choices=[
        "Its components cannot be separated by filtration, but they can be separated by "
        "processes that exploit differences in their intermolecular interactions",
        "Its components can be separated by filtration, and by no other means",
        "Its components cannot be separated by any method at all",
        "Its components can be separated only by processes that break covalent bonds",
        "Its components can be separated by any process whatever, since a solution is "
        "uniform"],
      ans=0,
      why="EK 3.9.A.1 has two halves and this option carries both: the method it rules out "
          "and the general description of the methods that work. Each rejected option keeps "
          "one half and contradicts the other."),
]
