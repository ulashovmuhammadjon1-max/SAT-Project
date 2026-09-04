# AP CHEMISTRY 7.5 Magnitude of the Equilibrium Constant
# CED effective Fall 2024, Unit 7 Equilibrium.
# Learning objective 7.5.A: explain the relationship between very large or very small
# values of K and the relative concentrations of chemical species at equilibrium.
# Suggested skill 6.D, provide reasoning to justify a claim using chemical principles or
# laws, or using mathematical justification.
#
# Essential knowledge relied on, in the framework's own words -- one statement, two
# clauses, and every key below is one of them or the learning objective that frames them:
#   7.5.A.1  Some equilibrium reactions have very large K values and proceed essentially
#            to completion. Others have very small K values and barely proceed at all.
#
# SCOPE, agreed with the neighbouring modules. h7_6.py's header records that "7.5 owns
# what a large or small K says about the extent of reaction". 7.4 owns getting a NUMBER
# for K out of equilibrium measurements and 7.7 owns getting concentrations out of a K, so
# no item below asks for "the value of Kc" and none solves for an equilibrium
# concentration. verify_h7_5.py asserts both. Where a composition appears, what is
# recomputed from it is the RATIO of product to reactant -- the "relative concentrations"
# of the learning objective -- and the item asks whether K is large or small, not what it
# is.
#
# WHAT THE FRAMEWORK DOES NOT SAY, and where this module stops. EK 7.5.A.1 describes only
# the two extremes. It does not give a rule for a K near one, so the items that raise that
# case key on the honest answer: neither clause of the statement applies, and appreciable
# amounts of both species are present. It also says nothing about RATE -- "proceeds
# essentially to completion" is a statement about how far, not how fast -- and item 10
# turns on exactly that, with EK 9.4.A.1 supplying the separate point that a favoured
# process may not occur at a measurable rate.
#
# THE OTHER THING IT DOES NOT SAY: that a large K leaves NO reactant. EK 7.1.A.2 has
# reactants and products simultaneously present at any equilibrium, so "essentially to
# completion" means a very small but nonzero amount remains. Items 15 and 26 are built on
# that, because a bank that taught "large K means the reactant is gone" would contradict
# the topic three pages earlier.
#
# ARITHMETIC. Every ordering of constants and every product-to-reactant ratio is
# recomputed in verify_h7_5.py from the tabulated values alone, with the scientific
# notation parsed out of the hand-written spans rather than restated.
#
# NOTATION. export_units.py does not typeset Chemistry, so every \( ... \) span below is
# hand-written; a formula in prose stays plain text.
TOPIC = ("7.5", "Magnitude of the Equilibrium Constant", 7)

_T_K = dict(
    headers=["Reaction", "Equilibrium constant at 298 K"],
    rows=[["I", "\\( 1 \\times 10^{15} \\)"],
          ["II", "\\( 1 \\times 10^{-12} \\)"],
          ["III", "\\( 2.0 \\)"],
          ["IV", "\\( 1 \\times 10^{6} \\)"]])

_T_TWO = dict(
    headers=["Reaction", "Equilibrium constant at 500 K"],
    rows=[["J", "\\( 1 \\times 10^{-4} \\)"],
          ["L", "\\( 1 \\times 10^{-10} \\)"]])

_T_COMPS = dict(
    headers=["Mixture", "[A] at equilibrium (M)", "[B] at equilibrium (M)"],
    rows=[["P", "0.0010", "0.9990"],
          ["R", "0.9990", "0.0010"],
          ["S", "0.5000", "0.5000"]])

QUESTIONS = [

 dict(q="What does the framework say about equilibrium reactions with very large values of "
        "K?",
      choices=[
        "They proceed essentially to completion",
        "They proceed only until half the reactant has been consumed",
        "They reach equilibrium more quickly than other reactions",
        "They release more energy than reactions with small values",
        "They never reach equilibrium at all"],
      ans=0,
      why="EK 7.5.A.1 states that some equilibrium reactions have very large K values and "
          "proceed essentially to completion. The statement is about how FAR the reaction "
          "goes; nothing in it concerns how quickly equilibrium is reached or how much "
          "energy is involved."),

 dict(q="What does the framework say about equilibrium reactions with very small values of "
        "K?",
      choices=[
        "They barely proceed at all",
        "They proceed to completion but very slowly",
        "They cannot reach equilibrium",
        "They consume all of the reactant but produce little product",
        "They proceed further than reactions with large values"],
      ans=0,
      why="EK 7.5.A.1 states that reactions with very small K values barely proceed at all. "
          "Barely proceeding is a statement about extent, so a reaction that went to "
          "completion slowly would be described by the other clause of the same sentence."),

 dict(q="At equilibrium in a reaction with a very large value of K, which species are "
        "present in the greater concentrations?",
      choices=[
        "The products, since the reaction has proceeded nearly to completion",
        "The reactants, since a large constant means the reactants are favoured",
        "Both are present in equal concentrations",
        "The reactants, but only if the reaction is exothermic",
        "Neither, since a large constant means the reaction goes to a solid"],
      ans=0,
      why="EK 7.5.A.1 pairs a very large K with proceeding essentially to completion, and "
          "a reaction that has nearly finished has converted nearly all its reactant, so "
          "the products dominate the equilibrium mixture. Learning objective 7.5.A is "
          "exactly this link between the size of K and the relative concentrations."),

 dict(q="At equilibrium in a reaction with a very small value of K, what does the "
        "equilibrium mixture mostly contain?",
      choices=[
        "Reactants, since the reaction has barely proceeded",
        "Products, since the reaction has barely proceeded",
        "Equal amounts of reactants and products",
        "Only reactants, with no product at all",
        "Whichever species was placed in the vessel second"],
      ans=0,
      why="EK 7.5.A.1 says such reactions barely proceed at all, so little reactant has "
          "been converted and the mixture is mostly what was put in. EK 7.1.A.2 keeps some "
          "product present all the same, which is why 'only reactants' overstates it."),

 dict(q="The table gives equilibrium constants for four reactions at the same temperature. "
        "Which reaction proceeds essentially to completion?",
      table=_T_K,
      choices=["Reaction I", "Reaction II", "Reaction III", "Reaction IV",
               "Reactions I and IV equally"],
      ans=0,
      why="EK 7.5.A.1 attaches proceeding essentially to completion to a very large K, and "
          "the tabulated constants have a single largest value, many orders of magnitude "
          "above the next. The reaction with a constant near one is neither of the two "
          "cases the statement describes."),

 dict(q="Using the same table of four constants, which reaction barely proceeds at all?",
      table=_T_K,
      choices=["Reaction II", "Reaction I", "Reaction III", "Reaction IV",
               "None of them, since all four have positive constants"],
      ans=0,
      why="EK 7.5.A.1 attaches barely proceeding to a very small K, and one tabulated "
          "constant is far below the others and far below one. Every equilibrium constant "
          "is a positive number, so being positive distinguishes nothing."),

 dict(q="Using the same table of four constants, in which reaction's equilibrium mixture "
        "is the ratio of products to reactants smallest?",
      table=_T_K,
      choices=["Reaction II", "Reaction I", "Reaction III", "Reaction IV",
               "The ratio is the same in all four"],
      ans=0,
      why="Learning objective 7.5.A links the size of the constant to the relative "
          "concentrations at equilibrium, so the smallest tabulated constant belongs to the "
          "mixture with the least product relative to reactant. The four tabulated values "
          "are all different, so no two mixtures can share the ratio."),

 dict(q="Using the same table of four constants, what does the framework's statement allow "
        "you to say about the reaction whose constant is close to one?",
      table=_T_K,
      choices=[
        "Neither clause applies, so appreciable amounts of both reactants and products are "
        "present",
        "It proceeds essentially to completion, like the reaction with the largest constant",
        "It barely proceeds at all, like the reaction with the smallest constant",
        "It has not yet reached equilibrium",
        "Its constant must have been measured incorrectly"],
      ans=0,
      why="EK 7.5.A.1 describes only VERY LARGE and VERY SMALL constants, and a tabulated "
          "value close to one is neither. What remains is EK 7.1.A.2's general statement "
          "that reactants and products are both present, in this case in comparable "
          "amounts."),

 dict(q="The table gives constants for two reactions run under the same conditions. "
        "Starting from the same concentration of reactant, which reaction ends with more "
        "product at equilibrium?",
      table=_T_TWO,
      choices=["Reaction J", "Reaction L", "Both end with the same amount",
               "Neither, because both constants are less than one",
               "The comparison cannot be made from constants alone"],
      ans=0,
      why="Learning objective 7.5.A links the magnitude of K to the relative "
          "concentrations at equilibrium, and the larger of the two tabulated constants "
          "belongs to the mixture with more product. A negative exponent that is larger in "
          "SIZE makes the number smaller, which is the trap in the comparison."),

 dict(q="A student concludes from a very large equilibrium constant that the reaction must "
        "be fast. Why is that conclusion unwarranted?",
      choices=[
        "The constant describes how far the reaction proceeds, not how quickly",
        "It is warranted, because a large constant means a large forward rate",
        "The constant describes how quickly the reaction proceeds, not how far",
        "A large constant means the reaction is slow, not fast",
        "The constant says nothing about the reaction at all"],
      ans=0,
      why="EK 7.5.A.1 speaks of reactions proceeding essentially to completion or barely "
          "proceeding at all, which are statements of extent. EK 9.4.A.1 makes the point "
          "separately that many favoured processes do not occur at a measurable rate, so "
          "extent and rate are independent questions."),

 dict(q="The table reports the equilibrium composition of three mixtures of the reaction "
        "A(g) to B(g). Which mixture came from the reaction with the largest constant?",
      table=_T_COMPS,
      choices=["Mixture P", "Mixture R", "Mixture S", "Mixtures P and S equally",
               "The mixture cannot be identified from composition"],
      ans=0,
      why="Learning objective 7.5.A links the magnitude of the constant to the relative "
          "concentrations, so the mixture with the most product relative to reactant "
          "belongs to the largest constant. Comparing the tabulated ratios of the two "
          "columns identifies a single mixture."),

 dict(q="Using the same table of three equilibrium mixtures, which mixture belongs to a "
        "reaction that barely proceeds at all?",
      table=_T_COMPS,
      choices=["Mixture R", "Mixture P", "Mixture S", "Mixtures R and S equally",
               "None, since every mixture contains some product"],
      ans=0,
      why="EK 7.5.A.1 attaches barely proceeding to a very small constant, and the "
          "tabulated mixture whose product concentration is a thousandth of its reactant "
          "concentration is that case. Some product is present in every equilibrium "
          "mixture under EK 7.1.A.2, so its presence does not settle the question."),

 dict(q="Using the same table of three equilibrium mixtures, which one is described by "
        "NEITHER clause of the framework's statement about very large and very small "
        "constants?",
      table=_T_COMPS,
      choices=["Mixture S", "Mixture P", "Mixture R", "All three are described by one of "
               "the clauses", "None of the three is described by either clause"],
      ans=0,
      why="EK 7.5.A.1 describes only very large and very small constants. The tabulated "
          "mixture whose two concentrations are equal has a product-to-reactant ratio of "
          "one, which is neither extreme, while the other two are far from one in opposite "
          "directions."),

 dict(q="A reaction has an equilibrium constant of \\( 1 \\times 10^{-20} \\). What will a "
        "chemist observe on mixing the reactants and waiting for equilibrium?",
      choices=[
        "Almost no product, because the reaction barely proceeds",
        "Almost no reactant, because the reaction goes nearly to completion",
        "Equal amounts of reactant and product",
        "No reaction at all, since the constant is smaller than one",
        "A steady change in composition that never settles"],
      ans=0,
      why="EK 7.5.A.1 says a very small constant means the reaction barely proceeds at "
          "all, so very little product forms. A constant of that size is not zero, so a "
          "trace of product does form and the system does reach equilibrium under EK "
          "7.1.A.2."),

 dict(q="A reaction has an equilibrium constant of \\( 1 \\times 10^{20} \\). What is true "
        "of the equilibrium mixture?",
      choices=[
        "It is almost entirely product, with only a trace of reactant left",
        "It is almost entirely reactant, with only a trace of product formed",
        "It contains the two species in comparable amounts",
        "It contains no reactant whatsoever",
        "It cannot be described without knowing the starting amounts"],
      ans=0,
      why="EK 7.5.A.1 pairs a very large constant with proceeding essentially to "
          "completion. EK 7.1.A.2 keeps both species present at any equilibrium, so the "
          "reactant is reduced to a trace rather than eliminated."),

 dict(q="Does 'proceeds essentially to completion' mean that no reactant remains at "
        "equilibrium?",
      choices=[
        "No, a very small amount of reactant remains, since both species are present at "
        "equilibrium",
        "Yes, the reactant is entirely consumed when the constant is very large",
        "Yes, but only for reactions with a single reactant",
        "No, exactly half the reactant remains at equilibrium",
        "No, and the amount remaining is the same for every reaction with a large constant"],
      ans=0,
      why="EK 7.5.A.1 chooses the word ESSENTIALLY, and EK 7.1.A.2 states that reactants "
          "and products are simultaneously present at equilibrium with their "
          "concentrations constant. A constant of any finite size therefore leaves some "
          "reactant, however little."),

 dict(q="Two reactions are carried out under identical conditions and one has a constant a "
        "million times the other. How do their equilibrium mixtures compare?",
      choices=[
        "The one with the larger constant has proceeded further toward products",
        "The one with the larger constant has proceeded less far toward products",
        "The two mixtures are identical, since the conditions were identical",
        "The one with the larger constant reached equilibrium a million times sooner",
        "No comparison can be made without the starting concentrations"],
      ans=0,
      why="Learning objective 7.5.A ties the magnitude of the constant to the relative "
          "concentrations at equilibrium, and EK 7.5.A.1's two clauses put large constants "
          "at the completion end of that scale. A ratio of constants says nothing about "
          "time, which EK 9.4.A.1 treats separately."),

 dict(q="A reaction with a very small equilibrium constant is left for several hours and "
        "its composition stops changing, with almost all of the reactant still present. "
        "Has the system reached equilibrium?",
      choices=[
        "Yes, because the concentrations have become constant",
        "No, because most of the reactant is still unreacted",
        "No, because a very small constant means equilibrium is never reached",
        "Yes, but only if some product can be detected",
        "It cannot be decided without measuring the rates"],
      ans=0,
      why="EK 7.1.A.2 makes constancy of the concentrations the signature of equilibrium, "
          "and EK 7.5.A.1 explains why so little product is there: the reaction barely "
          "proceeds. Little conversion and no conversion look similar but only the second "
          "would be inconsistent with equilibrium."),

 dict(q="Which pair of statements about a reaction is consistent with the framework?",
      choices=[
        "The constant is very large, and at equilibrium the products predominate",
        "The constant is very large, and at equilibrium the reactants predominate",
        "The constant is very small, and at equilibrium the products predominate",
        "The constant is very small, and at equilibrium neither species is present",
        "The constant is very large, and at equilibrium nothing has reacted"],
      ans=0,
      why="EK 7.5.A.1 links a very large constant with proceeding essentially to "
          "completion, which leaves a mixture dominated by products, and learning "
          "objective 7.5.A is precisely that relationship between the value of K and the "
          "relative concentrations."),

 dict(q="A chemist wants to choose a reaction that will convert nearly all of a starting "
        "material into a desired product in one step. What should the chemist look for?",
      choices=[
        "A reaction with a very large equilibrium constant",
        "A reaction with a very small equilibrium constant",
        "A reaction with an equilibrium constant close to one",
        "A reaction whose equilibrium constant has not been measured",
        "A reaction with the largest possible number of products"],
      ans=0,
      why="EK 7.5.A.1 says reactions with very large K values proceed essentially to "
          "completion, which is exactly the conversion of nearly all the starting material "
          "the chemist wants. A constant near one would leave much of the starting "
          "material behind."),

 dict(q="Which of the following equilibrium constants belongs to the reaction that "
        "proceeds furthest toward products?",
      choices=["\\( 5 \\times 10^{8} \\)", "\\( 5 \\times 10^{-8} \\)",
               "\\( 5 \\times 10^{-3} \\)", "\\( 8 \\times 10^{-5} \\)",
               "\\( 3 \\times 10^{-1} \\)"],
      ans=0,
      why="EK 7.5.A.1 puts the largest constant at the completion end, and only one of "
          "these values is greater than one at all; the rest have negative exponents and "
          "are therefore fractions. A large digit in front of a negative power of ten does "
          "not make the number large."),

 dict(q="Which of the following equilibrium constants belongs to the reaction that barely "
        "proceeds?",
      choices=["\\( 2 \\times 10^{-16} \\)", "\\( 2 \\times 10^{16} \\)",
               "\\( 2 \\times 10^{2} \\)", "\\( 9 \\times 10^{4} \\)",
               "\\( 6 \\times 10^{1} \\)"],
      ans=0,
      why="EK 7.5.A.1 attaches barely proceeding to a very small constant, and only one of "
          "these values is far below one. The remaining values are all greater than one and "
          "belong to reactions that have proceeded appreciably or nearly completely."),

 dict(q="An equilibrium mixture is found to contain a thousand times as much product as "
        "reactant. What does this indicate about the constant?",
      choices=[
        "It is much greater than one",
        "It is much less than one",
        "It is equal to one",
        "It is negative",
        "It cannot be related to the composition at all"],
      ans=0,
      why="Learning objective 7.5.A links the value of K to the relative concentrations at "
          "equilibrium, with products over reactants in the expression of EK 7.3.A.1, so a "
          "mixture rich in product corresponds to a large constant. An equilibrium constant "
          "is a ratio of positive concentrations and can never be negative."),

 dict(q="An equilibrium mixture is found to contain a thousand times as much reactant as "
        "product. Which description from the framework fits this reaction?",
      choices=[
        "It barely proceeds, so its constant is very small",
        "It proceeds essentially to completion, so its constant is very large",
        "It has an equilibrium constant close to one",
        "It has not yet reached equilibrium",
        "It has a constant that depends on how much reactant was used"],
      ans=0,
      why="EK 7.5.A.1's second clause covers exactly this case: reactions with very small K "
          "values barely proceed at all, leaving most of the reactant unconverted. EK "
          "7.4.A.1 makes the constant independent of how the vessel was charged."),

 dict(q="Two reactions have constants of \\( 1 \\times 10^{-3} \\) and \\( 1 \\times "
        "10^{-9} \\). Which statement compares them correctly?",
      choices=[
        "Both barely proceed, but the first proceeds further than the second",
        "Both barely proceed, but the second proceeds further than the first",
        "The first proceeds essentially to completion and the second barely proceeds",
        "Both proceed essentially to completion",
        "The two proceed to the same extent, since both constants are less than one"],
      ans=0,
      why="Both constants are far below one, so EK 7.5.A.1's second clause covers both, and "
          "learning objective 7.5.A makes the larger of two constants the one whose "
          "equilibrium mixture holds relatively more product. A million-fold difference "
          "between them is not nothing."),

 dict(q="A reaction has a constant of \\( 1 \\times 10^{12} \\). What fraction of the "
        "reactant is left at equilibrium?",
      choices=[
        "A very small but nonzero fraction",
        "Exactly none, since the reaction is complete",
        "About half, since the reaction is reversible",
        "The same fraction as for any reaction with a constant above one",
        "A fraction that cannot be smaller than one part in a hundred"],
      ans=0,
      why="EK 7.5.A.1's phrase is 'essentially to completion', and EK 7.1.A.2 requires "
          "reactants and products to be simultaneously present at equilibrium, so a very "
          "small amount of reactant remains. How small depends on the reaction and the "
          "conditions, so no universal fraction can be quoted."),

 dict(q="What is the relationship the framework draws between the size of K and the "
        "composition of the equilibrium mixture?",
      choices=[
        "A larger constant corresponds to a mixture richer in products",
        "A larger constant corresponds to a mixture richer in reactants",
        "The size of the constant fixes the total amount of material present",
        "The size of the constant fixes how long equilibrium takes to reach",
        "There is no relationship, since the constant is fixed by temperature alone"],
      ans=0,
      why="Learning objective 7.5.A is stated as the relationship between very large or "
          "very small values of K and the relative concentrations at equilibrium, and EK "
          "7.5.A.1 gives the two ends of it. Temperature fixes the VALUE of the constant "
          "for a given reaction, which is a separate matter from what the value then tells "
          "you."),

 dict(q="A reaction is described as barely proceeding at all. Which observation is "
        "consistent with that description?",
      choices=[
        "After equilibrium is reached, only a trace of product can be detected",
        "After equilibrium is reached, no reactant can be detected",
        "The reaction takes several days to reach equilibrium",
        "The reaction releases very little heat",
        "The reaction produces a solid rather than a gas"],
      ans=0,
      why="EK 7.5.A.1 uses 'barely proceed at all' to describe how far a reaction with a "
          "very small constant goes, so the observable consequence is a mixture holding "
          "almost none of the product. Time taken, heat released and the state of the "
          "product are not what the statement is about."),

 dict(q="Which question can be answered from the value of an equilibrium constant alone?",
      choices=[
        "Whether the equilibrium mixture holds mostly products or mostly reactants",
        "How long the reaction will take to reach equilibrium",
        "How much heat the reaction will release",
        "Whether the reaction requires a catalyst",
        "How many steps the reaction mechanism contains"],
      ans=0,
      why="Learning objective 7.5.A makes the relative concentrations at equilibrium the "
          "thing the magnitude of K reports. EK 9.4.A.1 separates extent from rate, and "
          "nothing in EK 7.5.A.1 concerns heat, catalysts or mechanisms."),

 dict(q="Summarise what a very large equilibrium constant and a very small one have in "
        "common, according to the framework.",
      choices=[
        "Both describe systems that reach equilibrium with both species present",
        "Both describe systems in which one species is completely absent",
        "Both describe systems that never reach equilibrium",
        "Both describe systems whose composition keeps changing",
        "Both describe systems in which the forward reaction has stopped"],
      ans=0,
      why="EK 7.5.A.1 distinguishes the two cases by how far the reaction proceeds, but EK "
          "7.1.A.2 applies to both alike: reactants and products are simultaneously present "
          "and their concentrations remain constant once equilibrium is reached."),

]
