# AP CHEMISTRY 5.4 Elementary Reactions
# CED effective Fall 2024, Unit 5 Kinetics.
# Learning objective 5.4.A: represent an elementary reaction as a rate law
# expression using stoichiometry. Suggested skill 5.E, determine a balanced
# chemical equation for a given chemical phenomenon.
#
# Essential knowledge relied on, in the framework's own words:
#   5.4.A.1  The rate law of an elementary reaction can be inferred from the
#            stoichiometry of the particles participating in a collision.
#   5.4.A.2  Elementary reactions involving the simultaneous collision of three
#            or more particles are rare.
#
# THE ONE MOVE THIS TOPIC OWNS. For an OVERALL reaction the powers in the rate
# law must be measured -- that is 5.2.A.1 and 5.2.A.5, and h5_2.py keys an item
# on exactly that. 5.4.A.1 carves out the single exception: for an ELEMENTARY
# reaction, and only there, the powers follow from the particles that collide.
# Every item in this module turns on that exception or on 5.4.A.2's rarity
# claim, and every stem that asks for a rate law SAYS the step is elementary.
#
# WHAT IS NOT HERE. A mechanism is a SEQUENCE of elementary steps; identifying
# the rate law of a whole mechanism is 5.8 and 5.9, and the components of a
# mechanism are 5.7. Nothing in this module involves more than one step, so no
# key here is a 5.7, 5.8 or 5.9 key wearing a different stem.
#
# ON THE WORD "MOLECULARITY". The CED prints it once, in 5.8.A.1, and it prints
# no name at all for a one-, two- or three-particle step. So this module counts
# particles in words rather than using terms the framework does not define.
#
# NOTATION. Chemistry is not typeset. Every rate law is a hand-written
# \( ... \) span, and each rate-law choice states the overall order it implies
# so that no choice is a truncation of another -- a bare shorter law would be a
# substring of a longer one, which the shared structural check rejects.
TOPIC = ("5.4", "Elementary Reactions", 5)

_T_STEPS = dict(
    headers=["Elementary step", "Particles that must collide"],
    rows=[["S1: A gives products", "1"],
          ["S2: A + B gives products", "2"],
          ["S3: 2 A gives products", "2"],
          ["S4: A + B + C gives products", "3"]])

_T_PROPOSED = dict(
    headers=["Proposed elementary step", "Number of particles on the reactant side"],
    rows=[["P1: NO + O3 gives NO2 + O2", "2"],
          ["P2: 2 NO + O2 gives 2 NO2", "3"],
          ["P3: O3 gives O2 + O", "1"],
          ["P4: NO2 + NO2 gives NO3 + NO", "2"]])

_T_MATCH = dict(
    headers=["Elementary step", "Rate law implied by the particles colliding"],
    rows=[["2 NOBr gives products", "second order in NOBr"],
          ["N2O5 gives products", "first order in N2O5"],
          ["H2 + I2 gives products", "first order in H2 and first order in I2"]])

_T_ORDERS = dict(
    headers=["Elementary step", "Overall order of its rate law"],
    rows=[["One particle", "1"],
          ["Two particles", "2"],
          ["Three particles", "3"]])

QUESTIONS = [

 dict(q="For an elementary reaction, where do the powers in the rate law come "
        "from?",
      choices=[
        "From the stoichiometry of the particles participating in the collision",
        "From measurements of how the rate changes when a concentration is "
        "doubled",
        "From the coefficients of the overall balanced equation for the whole "
        "reaction",
        "From the temperature at which the reaction is carried out",
        "From the number of products the step forms"],
      ans=0,
      why="EK 5.4.A.1, near verbatim: the rate law of an elementary reaction can "
          "be inferred from the stoichiometry of the particles participating in "
          "a collision. Measurement is how an overall reaction's powers are "
          "found; an elementary step is the case where they can be read off."),

 dict(q="An elementary step is written as A → products. What is its rate law?",
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{A}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k \), zero order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}]^{3} \), third order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}]^{2} \) divided by a concentration, "
        "first order overall"],
      ans=0,
      why="EK 5.4.A.1 lets the rate law be inferred from the stoichiometry of "
          "the particles taking part. One particle of A appears on the reactant "
          "side, so its concentration enters to the first power."),

 dict(q="An elementary step is written as A + B → products. What is its rate law?",
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{A}][\mathrm{B}] \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{B}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}]^{2}[\mathrm{B}]^{2} \), fourth order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{A}]^{2} \), second order overall"],
      ans=0,
      why="EK 5.4.A.1 infers the rate law from the particles participating in "
          "the collision. One particle of each reactant collides, so each "
          "concentration enters to the first power."),

 dict(q="An elementary step is written as 2 A → products. What is its rate law?",
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{A}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}] \), first order overall",
        r"\( \mathrm{rate} = 2k[\mathrm{A}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}]^{3} \), third order overall",
        r"\( \mathrm{rate} = k \), zero order overall"],
      ans=0,
      why="EK 5.4.A.1 infers the rate law from the stoichiometry of the "
          "colliding particles. Two particles of A must meet, so the "
          "concentration of A enters twice, that is squared."),

 dict(q="An elementary step is written as 2 A + B → products. What is its rate "
        "law?",
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{A}]^{2}[\mathrm{B}] \), third order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{A}][\mathrm{B}] \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}][\mathrm{B}]^{2} \), third order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{A}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{B}] \), first order overall"],
      ans=0,
      why="EK 5.4.A.1 infers the rate law from the particles that must collide: "
          "two of A and one of B, so A enters squared and B to the first power. "
          "EK 5.4.A.2 adds that such three-particle steps are rare."),

 dict(q="What does the course framework say about elementary reactions requiring "
        "three or more particles to collide at once?",
      choices=[
        "They are rare",
        "They are the most common kind of elementary reaction",
        "They cannot be written as elementary reactions at all",
        "They always have a rate law of overall order two",
        "They occur only at temperatures below room temperature"],
      ans=0,
      why="EK 5.4.A.2, near verbatim: elementary reactions involving the "
          "simultaneous collision of three or more particles are rare. The "
          "framework calls them rare rather than impossible."),

 dict(q="The table lists four elementary steps with the number of particles that "
        "must collide in each. Which step does the framework describe as rare?",
      table=_T_STEPS,
      choices=[
        "The step requiring three particles to collide simultaneously",
        "The step requiring only one particle, because a single particle cannot "
        "collide with anything",
        "Both steps requiring two particles, because a collision of two is "
        "already unlikely",
        "None of them, because every elementary step is equally likely",
        "All of them, because a simultaneous collision is always rare"],
      ans=0,
      why="EK 5.4.A.2 states that elementary reactions involving the "
          "simultaneous collision of three or more particles are rare. The "
          "table's particle counts identify which step that is."),

 dict(q="Why can the rate law of an overall reaction NOT generally be written "
        "down from its balanced equation, while the rate law of an elementary "
        "step can?",
      choices=[
        "Because the elementary step describes the particles that actually "
        "collide, while the overall equation only sums a sequence of such steps",
        "Because the coefficients of an overall equation are never whole numbers",
        "Because the rate law of an overall reaction has no powers at all",
        "Because an overall equation gives no information about which "
        "substances react",
        "Because an elementary step is always the fastest part of a reaction"],
      ans=0,
      why="EK 5.4.A.1 permits the inference only for an elementary reaction, "
          "where the stoichiometry IS the collision. EK 5.2.A.1 and 5.2.A.5 make "
          "the powers of an overall reaction a matter for experiment."),

 dict(q="An elementary step is written as O3 → O2 + O. What is its rate law?",
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{O_3}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{O_3}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{O_2}][\mathrm{O}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{O_3}][\mathrm{O_2}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k \), zero order overall"],
      ans=0,
      why="EK 5.4.A.1 infers the rate law from the stoichiometry of the "
          "particles participating, and the participating particles are the "
          "reactants. One ozone molecule is the whole reactant side, and the "
          "products do not enter a rate law."),

 dict(q="An elementary step is written as NO + O3 → NO2 + O2. What is its rate "
        "law?",
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{NO}][\mathrm{O_3}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{NO}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{NO}]^{2}[\mathrm{O_3}] \), third order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{NO_2}][\mathrm{O_2}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{O_3}]^{2} \), second order overall"],
      ans=0,
      why="EK 5.4.A.1 infers the rate law from the particles that collide, which "
          "are one molecule of each reactant, so each concentration enters to "
          "the first power and the products do not appear."),

 dict(q="For an elementary step, what is the relationship between the number of "
        "particles that must collide and the overall order of its rate law?",
      choices=[
        "They are equal, because each colliding particle contributes one power "
        "of its own concentration",
        "The overall order is one less than the number of particles",
        "The overall order is twice the number of particles",
        "The overall order is always one, whatever the number of particles",
        "There is no relationship between them"],
      ans=0,
      why="EK 5.4.A.1 infers the rate law from the stoichiometry of the "
          "colliding particles, and EK 5.2.A.3 makes the overall order the sum "
          "of the powers. Each participating particle contributes one power, so "
          "the two counts coincide."),

 dict(q="The table lists four proposed elementary steps with the number of "
        "particles on the reactant side of each. Which proposal should be "
        "regarded as the least likely to be a genuine elementary step?",
      table=_T_PROPOSED,
      choices=[
        "The step requiring two molecules of NO and one of O2 to meet at the "
        "same moment",
        "The step in which one ozone molecule falls apart on its own",
        "The step in which a molecule of NO meets a molecule of ozone",
        "The step in which two molecules of NO2 meet",
        "All four are equally likely, because each is balanced"],
      ans=0,
      why="EK 5.4.A.2 states that elementary reactions involving the "
          "simultaneous collision of three or more particles are rare, and the "
          "table's particle counts identify the one proposal that requires such "
          "a collision."),

 dict(q="A single elementary step is proposed to explain a reaction whose "
        "measured rate law is first order in one reactant and first order in a "
        "second reactant. Which step is consistent with that measurement?",
      choices=[
        "A step in which one particle of each of the two reactants collides",
        "A step in which two particles of the first reactant collide with one of "
        "the second",
        "A step in which one particle of the first reactant falls apart on its "
        "own",
        "A step in which two particles of the second reactant collide",
        "No step is consistent, because a measured rate law cannot match an "
        "elementary step"],
      ans=0,
      why="EK 5.4.A.1 makes the rate law of an elementary step follow from the "
          "particles that collide, so a step is consistent with a measured rate "
          "law when the particle counts match the measured powers."),

 dict(q="An elementary step is written as 2 NOBr → 2 NO + Br2. What is its rate "
        "law?",
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{NOBr}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{NOBr}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{NO}]^{2}[\mathrm{Br_2}] \), third order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{NOBr}]^{2}[\mathrm{Br_2}] \), third order "
        "overall",
        r"\( \mathrm{rate} = 2k[\mathrm{NOBr}] \), first order overall"],
      ans=0,
      why="EK 5.4.A.1 infers the rate law from the colliding particles. Two "
          "NOBr molecules must meet, so that concentration enters twice; the "
          "products play no part in the collision that starts the step."),

 dict(q="Which statement about the rate law of an elementary step is correct?",
      choices=[
        "Only the reactants of the step appear in it, each raised to the number "
        "of its particles in the collision",
        "Both the reactants and the products of the step appear in it",
        "Only the products of the step appear in it",
        "Neither the reactants nor the products appear in it, since the rate "
        "constant carries all the information",
        "The reactants appear in it raised to the number of products the step "
        "forms"],
      ans=0,
      why="EK 5.4.A.1 infers the rate law from the stoichiometry of the "
          "particles PARTICIPATING IN A COLLISION, and the particles that "
          "collide to start a step are its reactants."),

 dict(q="The table pairs three elementary steps with the rate law each implies. "
        "Which pairing does the framework support?",
      table=_T_MATCH,
      choices=[
        "All three, because in each row the powers match the particles that must "
        "collide",
        "Only the first, because it is the only step with a coefficient greater "
        "than one",
        "Only the second, because it is the only step with a single reactant",
        "Only the third, because it is the only step with two different "
        "reactants",
        "None of them, because a rate law can never be written from a chemical "
        "equation"],
      ans=0,
      why="EK 5.4.A.1 allows the rate law of an elementary reaction to be "
          "inferred from the stoichiometry of the particles participating, and "
          "each tabulated row states powers that match its own step's reactant "
          "particles."),

 dict(q="An elementary step involving one particle of X has a rate law "
        r"\( \mathrm{rate} = k[\mathrm{X}] \). If the concentration of X is tripled, "
        "what happens to the rate of that step?",
      choices=[
        "It becomes three times as large",
        "It becomes nine times as large",
        "It is unchanged",
        "It becomes one third as large",
        "It becomes twenty seven times as large"],
      ans=0,
      why="EK 5.4.A.1 gives the step a rate law with one power of the "
          "concentration of X, and EK 5.2.A.2 makes the rate proportional to "
          "that concentration raised to its power."),

 dict(q="An elementary step requires two particles of Y to collide. If the "
        "concentration of Y is doubled, what happens to the rate of that step?",
      choices=[
        "It becomes four times as large",
        "It becomes twice as large",
        "It is unchanged",
        "It becomes eight times as large",
        "It becomes half as large"],
      ans=0,
      why="EK 5.4.A.1 makes the rate law of the step second order in Y, because "
          "two particles of Y participate, and EK 5.2.A.2 makes the rate "
          "proportional to that concentration squared."),

 dict(q="A chemist proposes a single elementary step to explain a reaction whose "
        "measured rate law is third order overall. What does the framework imply "
        "about this proposal?",
      choices=[
        "It requires three particles to collide at once, which the framework "
        "calls rare",
        "It is impossible, because a rate law cannot be third order overall",
        "It is the most likely explanation, because a higher order means a "
        "faster reaction",
        "It requires only two particles to collide, because the third power "
        "comes from the rate constant",
        "It cannot be evaluated without knowing the temperature"],
      ans=0,
      why="EK 5.4.A.1 makes the overall order of an elementary step equal to the "
          "number of colliding particles, so a third order step needs three at "
          "once, and EK 5.4.A.2 calls such steps rare."),

 dict(q="An elementary step is written as Cl + CH4 → HCl + CH3. What is its rate "
        "law?",
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{Cl}][\mathrm{CH_4}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{Cl}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{CH_4}]^{4} \), fourth order overall",
        r"\( \mathrm{rate} = k[\mathrm{HCl}][\mathrm{CH_3}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{Cl}]^{2}[\mathrm{CH_4}] \), third order "
        "overall"],
      ans=0,
      why="EK 5.4.A.1 infers the rate law from the particles that collide, which "
          "here is one chlorine atom and one methane molecule, so each "
          "concentration enters once. The subscript in a formula is not a power "
          "in a rate law."),

 dict(q="The table gives the overall order of the rate law implied by an "
        "elementary step with one, two or three colliding particles. Which "
        "entry corresponds to the kind of step the framework calls rare?",
      table=_T_ORDERS,
      choices=[
        "The three-particle entry, whose overall order is three",
        "The one-particle entry, whose overall order is one",
        "The two-particle entry, whose overall order is two",
        "Every entry, since all three orders are equally rare",
        "No entry, since rarity is unrelated to the number of particles"],
      ans=0,
      why="EK 5.4.A.2 states that elementary reactions involving the "
          "simultaneous collision of three or more particles are rare, and EK "
          "5.4.A.1 makes the overall order equal the number of colliding "
          "particles, so the table pairs the two."),

 dict(q="Why do the products of an elementary step not appear in its rate law?",
      choices=[
        "Because the rate law is inferred from the particles that collide, and "
        "the products are formed by the collision rather than taking part in it",
        "Because the products are always present in negligible amounts",
        "Because the products are consumed again as soon as they are formed",
        "Because a rate law may contain at most two concentration factors",
        "Because the products are the same substances as the reactants"],
      ans=0,
      why="EK 5.4.A.1 infers the rate law from the stoichiometry of the "
          "particles PARTICIPATING IN A COLLISION. The products are what the "
          "collision makes, so they are not among the particles whose meeting "
          "the rate depends on."),

 dict(q="An overall reaction 2 A + B → C is found by experiment to have the rate "
        r"law \( \mathrm{rate} = k[\mathrm{A}] \). What does this show?",
      choices=[
        "The overall reaction cannot be a single elementary step, because the "
        "powers do not match its reactant particles",
        "The experiment must be in error, because a rate law always matches the "
        "balanced equation",
        "The reaction is elementary and B is a product rather than a reactant",
        "The reaction is elementary but the rate constant absorbs the missing "
        "powers",
        "Nothing, because a measured rate law carries no information about "
        "elementary steps"],
      ans=0,
      why="EK 5.4.A.1 makes the powers of an ELEMENTARY step follow from its "
          "colliding particles, so a measured rate law that disagrees with those "
          "particle counts rules the reaction out as a single step. EK 5.2.A.1 "
          "makes the measurement itself the authority."),

 dict(q="An elementary step is written as NO2 + NO2 → NO3 + NO. What is its rate "
        "law?",
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{NO_2}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{NO_2}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{NO_3}][\mathrm{NO}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{NO_2}]^{4} \), fourth order overall",
        r"\( \mathrm{rate} = k \), zero order overall"],
      ans=0,
      why="EK 5.4.A.1 infers the rate law from the colliding particles. Two "
          "molecules of NO2 must meet, whether the step is written with a "
          "coefficient of two or as a sum of two identical species, so that "
          "concentration enters twice."),

 dict(q="Which of the following rate laws could NOT have been inferred from a "
        "single elementary step?",
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{A}]^{1/2} \), half order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}][\mathrm{B}] \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}]^{2}[\mathrm{B}] \), third order "
        "overall"],
      ans=0,
      why="EK 5.4.A.1 makes the powers the counts of colliding particles, and a "
          "collision involves a whole number of particles. A fractional power "
          "therefore cannot come from counting participants in one collision."),

 dict(q="Two elementary steps are compared: one in which a single molecule breaks "
        "apart, and one in which two molecules must meet. Which statement about "
        "their rate laws is correct?",
      choices=[
        "The first is first order overall and the second is second order "
        "overall, matching their particle counts",
        "Both are first order overall, because each step is a single event",
        "Both are second order overall, because every collision involves two "
        "bodies",
        "The first is second order overall and the second is first order "
        "overall",
        "Neither has an order, because an order applies only to overall "
        "reactions"],
      ans=0,
      why="EK 5.4.A.1 makes the rate law of an elementary step follow from the "
          "stoichiometry of the particles participating, so a one-particle step "
          "carries one power and a two-particle step carries two."),

 dict(q="A step is written as A + A + A → products. Which pair of statements is "
        "correct?",
      choices=[
        r"Its rate law is \( \mathrm{rate} = k[\mathrm{A}]^{3} \), and the "
        "framework calls such steps rare",
        r"Its rate law is \( \mathrm{rate} = k[\mathrm{A}] \), and the framework "
        "calls such steps common",
        r"Its rate law is \( \mathrm{rate} = 3k[\mathrm{A}] \), and the "
        "framework calls such steps rare",
        r"Its rate law is \( \mathrm{rate} = k[\mathrm{A}]^{3} \), and the "
        "framework calls such steps the most common kind",
        "It cannot be written as an elementary step at all, so it has no rate "
        "law"],
      ans=0,
      why="EK 5.4.A.1 makes three colliding particles of A give three powers of "
          "its concentration, and EK 5.4.A.2 states that elementary reactions "
          "involving the simultaneous collision of three or more particles are "
          "rare rather than impossible."),

 dict(q="What does the framework mean by the stoichiometry of the particles "
        "participating in a collision?",
      choices=[
        "How many particles of each species must meet for that single step to "
        "occur",
        "The masses of the particles that meet during the step",
        "The total number of atoms present on both sides of the step",
        "The proportion of collisions that lead to a reaction",
        "The order in which the products of the step are formed"],
      ans=0,
      why="EK 5.4.A.1 infers the rate law from that stoichiometry, and the rate "
          "law's powers are counts of the participating particles, so the phrase "
          "refers to how many of each species take part in the one collision."),

 dict(q="An elementary step involving one molecule of P and one molecule of Q is "
        "carried out twice, once with both concentrations at their original "
        "values and once with both doubled. How do the rates compare?",
      choices=[
        "The second rate is four times the first, because each doubling "
        "contributes one factor of two",
        "The second rate is twice the first, because the two effects are "
        "averaged",
        "The second rate equals the first, because both concentrations changed "
        "in the same way",
        "The second rate is eight times the first, because the step is third "
        "order",
        "The comparison cannot be made without the value of the rate constant"],
      ans=0,
      why="EK 5.4.A.1 gives the step a rate law first order in each reactant, "
          "and EK 5.2.A.2 makes the rate proportional to the product of the "
          "concentration factors, so two independent doublings multiply."),

 dict(q="Why is it useful to know the rate law of each elementary step in a "
        "proposed sequence?",
      choices=[
        "Because each step's rate law follows from its own colliding particles "
        "and can be written without further measurement",
        "Because the rate law of a step tells you how much product the whole "
        "reaction will make",
        "Because a step's rate law fixes the temperature at which the reaction "
        "occurs",
        "Because the rate law of a step gives the energy released by that step",
        "Because every step in a sequence must have the same rate law"],
      ans=0,
      why="EK 5.4.A.1 is exactly this permission: for an elementary reaction the "
          "rate law can be inferred from the stoichiometry of the particles "
          "participating in the collision, without the experiments EK 5.2.A.5 "
          "requires for an overall reaction."),
]
