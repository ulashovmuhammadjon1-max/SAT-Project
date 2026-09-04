# AP CHEMISTRY 5.7 Introduction to Reaction Mechanisms
# CED effective Fall 2024, Unit 5 Kinetics.
# Learning objective 5.7.A: identify the components of a reaction mechanism.
# Suggested skill 1.B, describe the components of and quantitative information
# from models and representations.
#
# Essential knowledge relied on, in the framework's own words:
#   5.7.A.1  A reaction mechanism consists of a series of elementary reactions,
#            or steps, that occur in sequence. The components may include
#            reactants, intermediates, products, and catalysts.
#   5.7.A.2  The elementary steps when combined should align with the overall
#            balanced equation of a chemical reaction.
#   5.7.A.3  A reaction intermediate is produced by some elementary steps and
#            consumed by others, such that it is present only while a reaction
#            is occurring.
#   5.7.A.4  Experimental detection of a reaction intermediate is a common way
#            to build evidence in support of one reaction mechanism over an
#            alternative mechanism.
#            Exclusion statement: collection of data pertaining to detection of
#            a reaction intermediate will not be assessed on the AP Exam.
#
# THIS TOPIC IS IDENTIFICATION, NOT RATE. 5.7.A is "identify the components",
# and the components are named in 5.7.A.1. Which step sets the rate law is 5.8,
# and what to do when the first step is not rate limiting is 5.9; nothing here
# keys on either, and no item in this module labels a step fast or slow.
#
# WHY THE ANSWERS ARE COMPUTABLE. Two of the three claims are mechanical.
# 5.7.A.2 says the combined steps must align with the overall equation, which is
# addition and cancellation. 5.7.A.3 defines an intermediate by WHERE it appears
# -- produced by an earlier step and consumed by a later one -- which is a
# search over the steps. h_equation.py does both, so every mechanism in this
# module is resolved by the verifier rather than by the author's memory.
#
# THE EXCLUSION STATEMENT IS OBEYED. 5.7.A.4 is asked as a claim about what
# detecting an intermediate is evidence FOR. No item asks how the detection is
# carried out or what data it produces.
#
# NOTATION. Chemistry is not typeset. The arrow is the word "gives", formulas
# are plain text, and ions are written I-, IO- in the ordinary way. There is no
# mathematics in this topic and so no hand-written span.
TOPIC = ("5.7", "Introduction to Reaction Mechanisms", 5)

_M_NO2CO = dict(
    headers=["Step", "Elementary reaction"],
    rows=[["Step 1", "NO2 + NO2 gives NO3 + NO"],
          ["Step 2", "NO3 + CO gives NO2 + CO2"]])

_M_CFC = dict(
    headers=["Step", "Elementary reaction"],
    rows=[["Step 1", "Cl + O3 gives ClO + O2"],
          ["Step 2", "ClO + O gives Cl + O2"]])

_M_IODIDE = dict(
    headers=["Step", "Elementary reaction"],
    rows=[["Step 1", "H2O2 + I- gives H2O + IO-"],
          ["Step 2", "H2O2 + IO- gives H2O + O2 + I-"]])

_M_NO_O2 = dict(
    headers=["Step", "Elementary reaction"],
    rows=[["Step 1", "2 NO gives N2O2"],
          ["Step 2", "N2O2 + O2 gives 2 NO2"]])

_M_OZONE = dict(
    headers=["Step", "Elementary reaction"],
    rows=[["Step 1", "O3 gives O2 + O"],
          ["Step 2", "O + O3 gives 2 O2"]])

_M_ICL = dict(
    headers=["Step", "Elementary reaction"],
    rows=[["Step 1", "H2 + ICl gives HI + HCl"],
          ["Step 2", "HI + ICl gives I2 + HCl"]])

QUESTIONS = [

 dict(q="What does the framework say a reaction mechanism consists of?",
      choices=[
        "A series of elementary reactions, or steps, that occur in sequence",
        "A single elementary reaction repeated many times",
        "A list of the substances present at equilibrium",
        "A table of the rate measured at several concentrations",
        "The set of collisions that fail to produce products"],
      ans=0,
      why="EK 5.7.A.1, near verbatim: a reaction mechanism consists of a series "
          "of elementary reactions, or steps, that occur in sequence. A rate "
          "table is EK 5.2.A.5's method for finding a rate law, not a "
          "mechanism."),

 dict(q="Which components does the framework say a mechanism may include?",
      choices=[
        "Reactants, intermediates, products and catalysts",
        "Reactants and products only",
        "Intermediates and catalysts only",
        "Reactants, products and transition states only",
        "Whichever substances are present in the largest amounts"],
      ans=0,
      why="EK 5.7.A.1 lists exactly those four as the components a mechanism may "
          "include. A transition state is a point on an energy profile under EK "
          "5.6.A.3 rather than a component of a mechanism."),

 dict(q="What must the elementary steps of a mechanism do when they are "
        "combined?",
      choices=[
        "Align with the overall balanced equation of the reaction",
        "Reduce to a single elementary reaction",
        "Produce more product than the overall equation shows",
        "Contain the same number of steps as there are reactants",
        "Leave every intermediate in the final equation"],
      ans=0,
      why="EK 5.7.A.2, verbatim in substance: the elementary steps when combined "
          "should align with the overall balanced equation of a chemical "
          "reaction. EK 5.7.A.3's intermediates are exactly what does NOT "
          "survive that combination."),

 dict(q="How does the framework define a reaction intermediate?",
      choices=[
        "A species produced by some elementary steps and consumed by others",
        "A species that is present before the reaction starts and after it ends",
        "A species that appears on both sides of the overall balanced equation",
        "The highest-energy arrangement the reacting particles pass through",
        "A species that speeds the reaction up without taking part in it"],
      ans=0,
      why="EK 5.7.A.3, near verbatim. The highest-energy arrangement is EK "
          "5.6.A.3's transition state, and a species that speeds a reaction "
          "without being used up is EK 5.11.A.2's catalyst."),

 dict(q="Why is a reaction intermediate present only while the reaction is "
        "occurring?",
      choices=[
        "Because the steps that produce it are matched by steps that consume "
        "it, so none of it is left when the reaction is over",
        "Because it decomposes on contact with air",
        "Because it is always a gas and escapes from the container",
        "Because it is destroyed by the catalyst before the reaction finishes",
        "Because it is never actually formed in measurable amounts at all"],
      ans=0,
      why="EK 5.7.A.3 defines an intermediate as produced by some elementary "
          "steps and consumed by others, SUCH THAT it is present only while a "
          "reaction is occurring; the framework draws the transience from the "
          "matched production and consumption."),

 dict(q="The table gives a two-step mechanism. Which species is the reaction "
        "intermediate?",
      table=_M_NO2CO,
      choices=["NO3", "NO2", "CO", "CO2", "NO"],
      ans=0,
      why="EK 5.7.A.3 makes an intermediate the species produced by one "
          "elementary step and consumed by another. Reading the two tabulated "
          "steps for a species appearing first as a product and then as a "
          "reactant is what identifies it."),

 dict(q="For that same tabulated mechanism, what is the overall balanced "
        "equation the steps combine to give?",
      table=_M_NO2CO,
      choices=[
        "NO2 + CO gives NO + CO2",
        "2 NO2 + CO gives NO3 + NO + CO2",
        "NO2 + NO3 + CO gives NO + NO2 + CO2",
        "2 NO2 + 2 CO gives 2 NO + 2 CO2",
        "NO3 + CO gives NO2 + CO2"],
      ans=0,
      why="EK 5.7.A.2 requires the combined steps to align with the overall "
          "balanced equation, which means adding the two steps and cancelling "
          "whatever appears on both sides, namely the intermediate and the "
          "species regenerated."),

 dict(q="The table gives a two-step mechanism proposed for the destruction of "
        "ozone. Which species is the reaction intermediate?",
      table=_M_CFC,
      choices=["ClO", "Cl", "O3", "O2", "O"],
      ans=0,
      why="EK 5.7.A.3 makes an intermediate the species produced by an earlier "
          "elementary step and consumed by a later one, which is settled by "
          "reading where each tabulated species appears."),

 dict(q="In that same tabulated mechanism, which species is consumed in the "
        "first step and regenerated in the second?",
      table=_M_CFC,
      choices=["Cl", "ClO", "O3", "O2", "O"],
      ans=0,
      why="EK 5.7.A.1 lists catalysts among the components of a mechanism, and "
          "EK 5.11.A.2 describes a catalyst as frequently consumed in one step "
          "and regenerated in a subsequent one, which is what the tabulated "
          "steps show for this species."),

 dict(q="What overall balanced equation do the two tabulated ozone steps combine "
        "to give?",
      table=_M_CFC,
      choices=[
        "O3 + O gives 2 O2",
        "Cl + O3 gives ClO + O2",
        "O3 gives O2 + O",
        "2 O3 gives 3 O2",
        "ClO + O3 gives Cl + 2 O2"],
      ans=0,
      why="EK 5.7.A.2 has the combined steps align with the overall equation. "
          "Adding the two tabulated steps and cancelling the species that "
          "appear on both sides leaves only what enters and leaves the whole "
          "sequence."),

 dict(q="The table gives a two-step mechanism for the decomposition of hydrogen "
        "peroxide. Which species is the reaction intermediate?",
      table=_M_IODIDE,
      choices=["IO-", "I-", "H2O2", "H2O", "O2"],
      ans=0,
      why="EK 5.7.A.3 makes an intermediate the species produced by one step "
          "and consumed by another, and only one tabulated species is formed "
          "before it is used."),

 dict(q="In that same peroxide mechanism, what is true of the iodide ion, I-?",
      table=_M_IODIDE,
      choices=[
        "It is consumed in the first step and regenerated in the second, so its "
        "net amount is unchanged",
        "It is produced in the first step and consumed in the second, so it is "
        "the intermediate",
        "It appears on the left of the overall equation as a reactant",
        "It appears on the right of the overall equation as a product",
        "It takes no part in either tabulated step"],
      ans=0,
      why="EK 5.7.A.1 lists catalysts among a mechanism's components and EK "
          "5.11.A.2 has the catalyst consumed in one step and regenerated in a "
          "later one, leaving its net concentration constant; the tabulated "
          "steps place I- on the left of the first and the right of the second."),

 dict(q="The table gives a two-step mechanism proposed for the formation of "
        "nitrogen dioxide. Which species is the reaction intermediate?",
      table=_M_NO_O2,
      choices=["N2O2", "NO", "O2", "NO2", "There is no intermediate"],
      ans=0,
      why="EK 5.7.A.3 makes an intermediate the species produced by an earlier "
          "step and consumed by a later one, so the species formed in the first "
          "tabulated step and used in the second is the one."),

 dict(q="A student proposes the tabulated two-step mechanism for the overall "
        "reaction 2 O3 gives 3 O2. Do the steps align with that overall "
        "equation?",
      table=_M_OZONE,
      choices=[
        "Yes, because adding the steps and cancelling the intermediate leaves "
        "exactly that equation",
        "No, because the first step alone does not give that equation",
        "No, because an intermediate remains after the steps are added",
        "Yes, but only because both steps involve oxygen",
        "It cannot be judged without knowing which step is slower"],
      ans=0,
      why="EK 5.7.A.2 requires the elementary steps when combined to align with "
          "the overall balanced equation, which is settled by adding the two "
          "tabulated steps and cancelling any species appearing on both sides."),

 dict(q="What does the framework say experimental detection of a reaction "
        "intermediate is commonly used for?",
      choices=[
        "To build evidence in support of one reaction mechanism over an "
        "alternative mechanism",
        "To measure the rate constant of the overall reaction",
        "To determine the temperature at which the reaction is fastest",
        "To establish the overall balanced equation of the reaction",
        "To find the concentration of the catalyst"],
      ans=0,
      why="EK 5.7.A.4, verbatim in substance. Detection discriminates between "
          "proposed mechanisms; the overall equation is known independently "
          "under EK 5.7.A.2."),

 dict(q="A species predicted by one proposed mechanism, and by no other, is "
        "detected during a reaction. What does the framework let a chemist "
        "conclude?",
      choices=[
        "The detection is evidence in support of that mechanism over the "
        "alternatives",
        "The mechanism has been proved correct beyond further question",
        "Every alternative mechanism has been shown to be impossible",
        "The reaction must proceed in a single elementary step",
        "Nothing at all, since intermediates are never detectable"],
      ans=0,
      why="EK 5.7.A.4 describes detection as a common way to BUILD EVIDENCE IN "
          "SUPPORT OF one mechanism over an alternative. The framework's word is "
          "evidence, not proof."),

 dict(q="How does a reaction intermediate differ from a product of the overall "
        "reaction?",
      choices=[
        "The intermediate is consumed again by a later step, so it does not "
        "survive to appear in the overall equation",
        "The intermediate is always formed in the last step rather than the "
        "first",
        "The intermediate carries a charge while a product never does",
        "The intermediate is always a gas while a product never is",
        "There is no difference; the words name the same thing"],
      ans=0,
      why="EK 5.7.A.3 has an intermediate produced by some steps and consumed by "
          "others, so it is present only while the reaction runs, and EK 5.7.A.2 "
          "makes the combined steps align with an overall equation from which it "
          "has therefore cancelled."),

 dict(q="How does a reaction intermediate differ from a catalyst in a "
        "mechanism?",
      choices=[
        "The intermediate is produced before it is consumed, while the catalyst "
        "is consumed before it is regenerated",
        "The intermediate appears in the overall equation while the catalyst "
        "does not",
        "The catalyst appears in the overall equation while the intermediate "
        "does not",
        "The intermediate takes part in only one step while the catalyst takes "
        "part in all of them",
        "There is no difference, since neither survives the reaction"],
      ans=0,
      why="EK 5.7.A.3 defines the intermediate by production followed by "
          "consumption, and EK 5.11.A.2 has the catalyst consumed in a step and "
          "regenerated afterwards, which is the same pattern in the opposite "
          "order; EK 5.7.A.2 keeps both out of the overall equation."),

 dict(q="Why can a species that appears in the overall balanced equation not be "
        "a reaction intermediate?",
      choices=[
        "Because it was not fully consumed by the later steps, so it is present "
        "when the reaction is over",
        "Because the overall equation lists only catalysts",
        "Because an intermediate must always carry a charge",
        "Because a species in the overall equation cannot appear in any step",
        "Because the overall equation is written before the mechanism is "
        "proposed"],
      ans=0,
      why="EK 5.7.A.3 requires an intermediate to be present only while a "
          "reaction is occurring, and EK 5.7.A.2 makes the overall equation what "
          "the combined steps leave, so anything surviving into it was not "
          "consumed again."),

 dict(q="What does the framework say about the order in which the elementary "
        "steps of a mechanism occur?",
      choices=[
        "They occur in sequence, one after another",
        "They occur simultaneously in a single collision",
        "They occur in whichever order the reactants happen to meet",
        "They occur in the order of increasing activation energy",
        "The order is not defined for any mechanism"],
      ans=0,
      why="EK 5.7.A.1 states that a mechanism consists of a series of elementary "
          "reactions, or steps, that occur in sequence. A single simultaneous "
          "event would be one elementary reaction rather than a mechanism."),

 dict(q="A proposed mechanism has three elementary steps. What does the "
        "framework require of the three steps taken together?",
      choices=[
        "That they align with the overall balanced equation once the species "
        "appearing on both sides have cancelled",
        "That each step contain the same number of atoms as the others",
        "That the first step be the one with the smallest activation energy",
        "That every step produce at least one intermediate",
        "That no species appear in more than one step"],
      ans=0,
      why="EK 5.7.A.2 is exactly this requirement, and EK 5.7.A.3's "
          "intermediates are the species that cancel, so a species appearing in "
          "more than one step is expected rather than forbidden."),

 dict(q="In a proposed mechanism, a species is written on the left of step 1 "
        "and on the right of step 3, and it does not appear in the overall "
        "equation. What is it?",
      choices=[
        "A catalyst, consumed early and regenerated later",
        "An intermediate, produced early and consumed later",
        "A product of the overall reaction",
        "A reactant of the overall reaction",
        "The transition state of the mechanism"],
      ans=0,
      why="EK 5.11.A.2 has a catalyst frequently consumed in one step and "
          "regenerated in a subsequent one, and EK 5.7.A.1 lists catalysts among "
          "a mechanism's components; EK 5.7.A.3's intermediate shows the "
          "opposite order."),

 dict(q="A species is written on the right of step 1 and on the left of step 2 "
        "of a proposed mechanism, and it does not appear in the overall "
        "equation. What is it?",
      choices=[
        "An intermediate, since it is produced by one step and consumed by "
        "another",
        "A catalyst, since it survives the reaction unchanged",
        "A reactant, since it is present before the second step",
        "A product, since it is formed by the first step",
        "A transition state, since it lies between the two steps"],
      ans=0,
      why="EK 5.7.A.3 defines a reaction intermediate as a species produced by "
          "some elementary steps and consumed by others, which is exactly the "
          "position described."),

 dict(q="A chemist writes the overall equation H2 + ICl gives I2 + HCl and "
        "offers the tabulated mechanism for it. Do the steps align with that "
        "overall equation?",
      table=_M_ICL,
      choices=[
        "No, because combining the steps requires two ICl and produces two HCl",
        "Yes, because both steps are balanced on their own",
        "Yes, because the intermediate cancels between the two steps",
        "No, because the two steps produce different intermediates",
        "It cannot be judged, because a mechanism never has to match an overall "
        "equation"],
      ans=0,
      why="EK 5.7.A.2 requires the combined steps to align with the overall "
          "balanced equation, so adding the tabulated steps and cancelling the "
          "species common to both sides is what the stated equation must be "
          "compared against."),

 dict(q="For that same tabulated mechanism, which species is the reaction "
        "intermediate?",
      table=_M_ICL,
      choices=["HI", "ICl", "H2", "HCl", "I2"],
      ans=0,
      why="EK 5.7.A.3 makes an intermediate the species produced by an earlier "
          "elementary step and consumed by a later one, which is settled by "
          "reading the two tabulated steps."),

 dict(q="Which statement about the components of a mechanism is consistent with "
        "the framework?",
      choices=[
        "A single mechanism may contain reactants, intermediates, products and "
        "a catalyst all at once",
        "A mechanism may contain either intermediates or a catalyst, but never "
        "both",
        "A mechanism contains only the substances written in the overall "
        "equation",
        "A mechanism contains no products until its final step is complete",
        "A mechanism contains exactly one component of each kind"],
      ans=0,
      why="EK 5.7.A.1 says the components MAY INCLUDE reactants, intermediates, "
          "products, and catalysts, which places no restriction against a "
          "mechanism holding all four."),

 dict(q="Why does a proposed mechanism whose steps do not combine to the known "
        "overall equation have to be rejected?",
      choices=[
        "Because the framework requires the combined steps to align with the "
        "overall balanced equation of the reaction",
        "Because a mechanism may never contain more than two steps",
        "Because such a mechanism would have to contain a catalyst",
        "Because the overall equation is derived from the mechanism rather than "
        "measured",
        "Because the steps would then have to occur simultaneously"],
      ans=0,
      why="EK 5.7.A.2 states that the elementary steps when combined should "
          "align with the overall balanced equation, so a proposal failing that "
          "test describes a different reaction from the one observed."),

 dict(q="Which species must appear on the left of the combined steps of a "
        "correct mechanism?",
      choices=[
        "The reactants of the overall equation",
        "The intermediates of the mechanism",
        "The products of the overall equation",
        "The catalysts of the mechanism only",
        "Every species that appears anywhere in the mechanism"],
      ans=0,
      why="EK 5.7.A.2 requires the combined steps to align with the overall "
          "balanced equation, whose left side holds the reactants; EK 5.7.A.3's "
          "intermediates cancel out of that combination entirely."),

 dict(q="Two chemists propose mechanisms with different numbers of elementary "
        "steps for the same overall reaction. What does the framework say about "
        "this?",
      choices=[
        "Both remain possible so long as each set of steps combines to the "
        "overall equation, and evidence such as a detected intermediate is what "
        "distinguishes them",
        "The proposal with fewer steps is correct by definition",
        "The proposal with more steps is correct by definition",
        "Neither can be correct, since a mechanism has a fixed number of steps",
        "The overall equation determines how many steps the mechanism has"],
      ans=0,
      why="EK 5.7.A.2 imposes only that the combined steps align with the "
          "overall equation, and EK 5.7.A.4 makes experimental detection of an "
          "intermediate a common way to build evidence for one mechanism over "
          "an alternative."),

 dict(q="A species is detected during a reaction that appears in NO proposed "
        "mechanism. What does this suggest under the framework?",
      choices=[
        "Every proposal so far is incomplete, since a mechanism's steps should "
        "account for the species present while the reaction runs",
        "The detection must be an error, since only proposed species can exist",
        "The overall balanced equation must be wrong",
        "The reaction must be a single elementary step after all",
        "The detected species must be a catalyst"],
      ans=0,
      why="EK 5.7.A.3 makes an intermediate a species present only while a "
          "reaction is occurring and EK 5.7.A.4 makes its detection evidence "
          "bearing on which mechanism is right, so a species no proposal "
          "contains is evidence against all of them."),
]
