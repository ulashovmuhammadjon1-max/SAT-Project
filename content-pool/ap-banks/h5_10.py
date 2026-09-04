# AP CHEMISTRY 5.10 Multistep Reaction Energy Profile
# CED effective Fall 2024, Unit 5 Kinetics.
# Learning objective 5.10.A: represent the activation energy and overall energy
# change in a multistep reaction with a reaction energy profile. Suggested skill
# 3.B, represent chemical substances or phenomena with appropriate diagrams or
# models.
#
# Essential knowledge relied on, in the framework's own words:
#   5.10.A.1  Knowledge of the energetics of each elementary reaction in a
#             mechanism allows for the construction of an energy profile for a
#             multistep reaction.
#
# ONE ESSENTIAL KNOWLEDGE STATEMENT, AND IT IS AN ASSEMBLY CLAIM. 5.10.A.1 says
# the multistep profile is BUILT OUT OF the profiles of the elementary steps,
# and the pieces come from 5.6: EK 5.6.A.3 makes the activation energy of a step
# the difference between its own starting point and its transition state, and
# the learning objectives for both topics pair that barrier with the overall
# energy change. EK 5.7.A.1 supplies the sequence of steps and EK 5.7.A.3 the
# intermediate that sits between two of them. Every key here is one of those.
#
# THERE ARE NO PICTURES, AND THIS TOPIC IS A PICTURE. Every profile in this
# module is a TABLE of the energy at each named point along the reaction
# coordinate -- reactants, first transition state, intermediate, second
# transition state, products -- in the order they are passed. That is what a
# drawn profile conveys, and unlike a drawing it can be recomputed: each step's
# barrier and each step's energy change are subtractions the verifier redoes.
#
# THE SIGN IS THE DEFECT MOST LIKELY HERE, so every energy-change choice states
# whether energy is released or absorbed as well as the size, and the verifier
# checks the direction word against a SIGNED difference.
#
# WHAT IS NOT HERE. A single elementary step's profile is 5.6 and h5_6.py owns
# it. Identifying the components of a mechanism is 5.7; reading the rate law off
# a slow step is 5.8. How a catalyst changes the profile is 5.11, and no item
# here mentions one.
#
# NOTATION. Chemistry is not typeset. Energies are plain text with their units,
# and every numeric choice carries a clause saying what the number is, so no
# choice is a truncation of another.
TOPIC = ("5.10", "Multistep Reaction Energy Profile", 5)

_P_TWO_A = dict(
    headers=["Point along the reaction coordinate", "Energy (kJ/mol)"],
    rows=[["Reactants", "40"],
          ["First transition state", "150"],
          ["Intermediate", "70"],
          ["Second transition state", "120"],
          ["Products", "20"]])

_P_TWO_B = dict(
    headers=["Point along the reaction coordinate", "Energy (kJ/mol)"],
    rows=[["Reactants", "30"],
          ["First transition state", "90"],
          ["Intermediate", "50"],
          ["Second transition state", "160"],
          ["Products", "40"]])

_P_THREE = dict(
    headers=["Point along the reaction coordinate", "Energy (kJ/mol)"],
    rows=[["Reactants", "20"],
          ["First transition state", "100"],
          ["First intermediate", "60"],
          ["Second transition state", "150"],
          ["Second intermediate", "80"],
          ["Third transition state", "110"],
          ["Products", "30"]])

QUESTIONS = [

 dict(q="According to the framework, what allows an energy profile for a "
        "multistep reaction to be constructed?",
      choices=[
        "Knowledge of the energetics of each elementary reaction in the "
        "mechanism",
        "Knowledge of the overall balanced equation alone",
        "Knowledge of the rate constant of the overall reaction",
        "Knowledge of the concentration of each reactant at the start",
        "Knowledge of the temperature at which the reaction is run"],
      ans=0,
      why="EK 5.10.A.1, near verbatim: knowledge of the energetics of each "
          "elementary reaction in a mechanism allows for the construction of an "
          "energy profile for a multistep reaction. The overall equation says "
          "nothing about the steps."),

 dict(q="How many maxima does the energy profile of a two-step mechanism have?",
      choices=[
        "Two, one transition state for each elementary step",
        "One, however many steps the mechanism has",
        "Three, one for each of the reactants, the intermediate and the products",
        "Four, two for each step",
        "None, because a multistep profile falls steadily"],
      ans=0,
      why="EK 5.10.A.1 builds the profile from the energetics of each elementary "
          "reaction, and EK 5.6.A.3 gives each elementary reaction one "
          "transition state between its own reactants and products."),

 dict(q="What occupies the low point BETWEEN the two maxima of a two-step "
        "profile?",
      choices=[
        "The reaction intermediate, which the first step forms and the second "
        "consumes",
        "The transition state shared by the two steps",
        "The reactants of the overall reaction",
        "The products of the overall reaction",
        "The catalyst, which is regenerated at that point"],
      ans=0,
      why="EK 5.7.A.3 makes a reaction intermediate a species produced by some "
          "elementary steps and consumed by others, and EK 5.10.A.1 assembles "
          "the profile from those steps, so the finished substance between the "
          "two steps sits in the trough."),

 dict(q="The table gives the energy at each point along the reaction coordinate "
        "of a two-step mechanism, in the order the points are passed. What is "
        "the activation energy of the FIRST step?",
      table=_P_TWO_A,
      choices=[
        "110 kJ/mol, the rise from the reactants to the first transition state",
        "80 kJ/mol, the fall from the first transition state to the intermediate",
        "50 kJ/mol, the rise from the intermediate to the second transition "
        "state",
        "150 kJ/mol, the energy of the first transition state itself",
        "30 kJ/mol, the rise from the reactants to the intermediate"],
      ans=0,
      why="EK 5.6.A.3 makes a step's activation energy the difference between "
          "its own starting point and its transition state, and EK 5.10.A.1 "
          "assembles the multistep profile from exactly those step energetics."),

 dict(q="Using the same tabulated profile, what is the activation energy of the "
        "SECOND step?",
      table=_P_TWO_A,
      choices=[
        "50 kJ/mol, the rise from the intermediate to the second transition "
        "state",
        "110 kJ/mol, the rise from the reactants to the first transition state",
        "100 kJ/mol, the fall from the second transition state to the products",
        "120 kJ/mol, the energy of the second transition state itself",
        "20 kJ/mol, the energy of the products themselves"],
      ans=0,
      why="EK 5.6.A.3 measures a step's activation energy from that step's own "
          "starting point, which for the second step is the intermediate rather "
          "than the original reactants."),

 dict(q="For that same tabulated profile, what is the overall energy change of "
        "the reaction?",
      table=_P_TWO_A,
      choices=[
        "20 kJ/mol is released, so the overall change is negative",
        "20 kJ/mol is absorbed, so the overall change is positive",
        "110 kJ/mol is released, since that is the first activation energy",
        "50 kJ/mol is absorbed, since that is the second activation energy",
        "130 kJ/mol is released, the sum of the two activation energies"],
      ans=0,
      why="The learning objective pairs the activation energy with the overall "
          "energy change, and EK 5.10.A.1's assembled profile makes that change "
          "the difference between its two ends, which are the reactants and the "
          "products of the overall reaction."),

 dict(q="Which step of that tabulated mechanism is the rate-limiting one?",
      table=_P_TWO_A,
      choices=[
        "The first, because its climb from its own starting point is the larger",
        "The second, because it comes after the intermediate is formed",
        "The first, because its transition state lies below the second one",
        "The second, because its products lie lowest of all",
        "Neither, because both steps have the same activation energy"],
      ans=0,
      why="EK 5.8.A.1 makes the rate-limiting step the slowest one, and EK "
          "5.6.A.4 ties a step's rate to the proportion of collisions able to "
          "reach its transition state, so the step with the larger climb from "
          "its own starting point is the slower."),

 dict(q="The table gives the profile of a different two-step mechanism. Which "
        "step is rate limiting here?",
      table=_P_TWO_B,
      choices=[
        "The second, because its climb from the intermediate is the larger",
        "The first, because it is always the first step that limits the rate",
        "The second, because its transition state is reached last",
        "The first, because its climb from the reactants is the larger",
        "Neither, because the two climbs are equal"],
      ans=0,
      why="EK 5.6.A.3 measures each step's barrier from its own starting point, "
          "and EK 5.8.A.1 makes the slowest step the rate-limiting one, so "
          "comparing the two tabulated climbs settles which that is."),

 dict(q="Using that second tabulated profile, what is the overall energy change "
        "of the reaction?",
      table=_P_TWO_B,
      choices=[
        "10 kJ/mol is absorbed, so the overall change is positive",
        "10 kJ/mol is released, so the overall change is negative",
        "110 kJ/mol is absorbed, since that is the larger activation energy",
        "60 kJ/mol is released, since that is the smaller activation energy",
        "120 kJ/mol is absorbed, the sum of the two activation energies"],
      ans=0,
      why="EK 5.10.A.1's assembled profile makes the overall energy change the "
          "difference between the two ends of the whole coordinate, and the "
          "tabulated products lie above the tabulated reactants."),

 dict(q="What is the activation energy of the first step of that second "
        "tabulated mechanism?",
      table=_P_TWO_B,
      choices=[
        "60 kJ/mol, the rise from the reactants to the first transition state",
        "110 kJ/mol, the rise from the intermediate to the second transition "
        "state",
        "40 kJ/mol, the fall from the first transition state to the intermediate",
        "90 kJ/mol, the energy of the first transition state itself",
        "20 kJ/mol, the rise from the reactants to the intermediate"],
      ans=0,
      why="EK 5.6.A.3 makes a step's activation energy the difference between "
          "its own starting point and its transition state, which for the first "
          "step is measured from the reactants."),

 dict(q="The table gives the profile of a three-step mechanism. How many "
        "reaction intermediates does it show?",
      table=_P_THREE,
      choices=[
        "Two, one in each trough between successive transition states",
        "One, the lowest point of the whole profile",
        "Three, one for each elementary step",
        "None, because a profile shows only reactants and products",
        "Four, counting the reactants and the products as well"],
      ans=0,
      why="EK 5.10.A.1 assembles the profile from each elementary reaction, and "
          "EK 5.7.A.3 puts an intermediate between the step that forms it and "
          "the step that consumes it, so a three-step sequence leaves two "
          "troughs."),

 dict(q="Which step of that three-step tabulated mechanism has the largest "
        "activation energy?",
      table=_P_THREE,
      choices=[
        "The second, whose climb from the first intermediate is the largest",
        "The first, whose climb from the reactants is the largest",
        "The third, whose climb from the second intermediate is the largest",
        "All three are equal, since the profile has one overall energy change",
        "It cannot be determined without the rate constants"],
      ans=0,
      why="EK 5.6.A.3 measures each step's barrier from its own starting point, "
          "which for the second and third steps are the intermediates rather "
          "than the reactants, and EK 5.10.A.1 makes those the pieces of the "
          "assembled profile."),

 dict(q="For the same three-step profile, what is the overall energy change of "
        "the reaction?",
      table=_P_THREE,
      choices=[
        "10 kJ/mol is absorbed, so the overall change is positive",
        "10 kJ/mol is released, so the overall change is negative",
        "90 kJ/mol is absorbed, since that is the largest activation energy",
        "130 kJ/mol is released, the total of the three climbs",
        "The overall change cannot be found when there are three steps"],
      ans=0,
      why="EK 5.10.A.1's assembled profile makes the overall change the "
          "difference between its two ends however many steps lie between them, "
          "and the tabulated products stand above the tabulated reactants."),

 dict(q="Why can the profile of a multistep reaction NOT be drawn from the "
        "overall balanced equation alone?",
      choices=[
        "Because the equation says nothing about the energetics of the "
        "individual elementary steps the profile is assembled from",
        "Because a balanced equation contains no energy information of any kind",
        "Because the overall equation gives only the products of the last step",
        "Because a profile requires the temperature, which the equation omits",
        "Because a multistep reaction has no overall balanced equation"],
      ans=0,
      why="EK 5.10.A.1 makes knowledge of the energetics of EACH ELEMENTARY "
          "REACTION what allows the construction, and EK 5.7.A.2 leaves the "
          "overall equation as only the sum of the steps, which the "
          "intermediates cancel out of."),

 dict(q="Two mechanisms with different numbers of steps are proposed for the "
        "same overall reaction. What must their energy profiles have in common?",
      choices=[
        "The same two endpoints, since the reactants and products are the same",
        "The same number of maxima, since the reaction is the same",
        "The same largest activation energy, since the rate is the same",
        "The same number of troughs, since intermediates always pair up",
        "Nothing at all, since the mechanisms differ"],
      ans=0,
      why="EK 5.10.A.1 assembles a profile from a mechanism's own steps, so the "
          "number of maxima follows the mechanism, while EK 5.7.A.2 makes every "
          "acceptable mechanism combine to the same overall equation and "
          "therefore run between the same two ends."),

 dict(q="For a two-step mechanism, how is the activation energy of the second "
        "step measured on the profile?",
      choices=[
        "From the intermediate up to the second transition state",
        "From the reactants up to the second transition state",
        "From the second transition state down to the products",
        "From the first transition state up to the second transition state",
        "From the reactants up to the products"],
      ans=0,
      why="EK 5.6.A.3 makes a step's activation energy the difference between "
          "the reactants OF THAT STEP and its transition state, and the second "
          "step begins from the intermediate under EK 5.7.A.3."),

 dict(q="What is the activation energy of the reverse of the first step of the "
        "first tabulated two-step profile, in which the intermediate returns to "
        "the reactants?",
      table=_P_TWO_A,
      choices=[
        "80 kJ/mol, the climb from the intermediate back to the first "
        "transition state",
        "110 kJ/mol, the climb from the reactants to the first transition state",
        "30 kJ/mol, the difference between the intermediate and the reactants",
        "50 kJ/mol, the climb from the intermediate to the second transition "
        "state",
        "150 kJ/mol, the energy of the first transition state itself"],
      ans=0,
      why="EK 5.6.A.3 names its difference the activation energy FOR THE FORWARD "
          "reaction, so the reverse of a step is the climb from that step's own "
          "products back to the same transition state."),

 dict(q="What does the energy of the intermediate relative to the reactants tell "
        "you?",
      choices=[
        "The energy change of the first elementary step alone",
        "The overall energy change of the whole reaction",
        "The activation energy of the first step",
        "The activation energy of the second step",
        "Nothing, because an intermediate has no defined energy"],
      ans=0,
      why="EK 5.10.A.1 assembles the profile from the energetics of each "
          "elementary reaction, and the first step runs from the reactants to "
          "the intermediate, so that difference is the first step's own energy "
          "change."),

 dict(q="For the first tabulated two-step profile, what is the energy change of "
        "the FIRST step alone?",
      table=_P_TWO_A,
      choices=[
        "30 kJ/mol is absorbed, because the intermediate lies above the "
        "reactants",
        "30 kJ/mol is released, because the intermediate lies below the "
        "reactants",
        "110 kJ/mol is absorbed, since that is the first activation energy",
        "80 kJ/mol is released, since that is the fall to the intermediate",
        "20 kJ/mol is released, since that is the overall change"],
      ans=0,
      why="EK 5.10.A.1 builds the profile from each elementary reaction's own "
          "energetics, and the first step ends at the intermediate, which the "
          "table places above the reactants."),

 dict(q="For that same profile, what is the energy change of the SECOND step "
        "alone?",
      table=_P_TWO_A,
      choices=[
        "50 kJ/mol is released, because the products lie below the intermediate",
        "50 kJ/mol is absorbed, because the products lie above the intermediate",
        "30 kJ/mol is released, since that is the first step's change",
        "100 kJ/mol is absorbed, since that is the fall from the second "
        "transition state",
        "20 kJ/mol is absorbed, since that is the overall change"],
      ans=0,
      why="EK 5.10.A.1 assembles the profile step by step, and the second step "
          "runs from the intermediate to the products, which the table places "
          "lower."),

 dict(q="How do the energy changes of the individual steps relate to the overall "
        "energy change of the reaction?",
      choices=[
        "They add up to it, because the steps run end to end along one "
        "coordinate",
        "They multiply to give it",
        "The overall change is the largest of them",
        "The overall change is the smallest of them",
        "There is no relationship between them"],
      ans=0,
      why="EK 5.10.A.1 assembles one profile from the energetics of the "
          "successive elementary reactions, so the rises and falls of the steps "
          "run consecutively between the same two ends, and their sum is the "
          "distance between those ends."),

 dict(q="Which point on a multistep profile is the highest?",
      choices=[
        "One of the transition states, which one depending on the mechanism",
        "The first transition state, always",
        "The last transition state, always",
        "An intermediate, since intermediates are unstable",
        "The reactants, since energy is used up as the reaction proceeds"],
      ans=0,
      why="EK 5.10.A.1 assembles the profile from separate elementary "
          "reactions, each contributing its own transition state under EK "
          "5.6.A.3, and nothing in the framework fixes which of those stands "
          "highest."),

 dict(q="A student says the rate-limiting step must be the one whose transition "
        "state lies highest above the INTERMEDIATE before it. What is the "
        "correct general statement?",
      choices=[
        "Each step's barrier is measured from its own starting point, whether "
        "that is the reactants or an intermediate",
        "Every barrier is measured from the reactants of the overall reaction",
        "Every barrier is measured from the products of the overall reaction",
        "Every barrier is measured from the lowest point of the whole profile",
        "Barriers cannot be compared between steps of one mechanism"],
      ans=0,
      why="EK 5.6.A.3 defines the activation energy as the difference between "
          "the reactants and the transition state OF THAT ELEMENTARY REACTION, "
          "and EK 5.10.A.1 assembles the multistep profile out of those "
          "individual pieces."),

 dict(q="A two-step mechanism has a first step that absorbs energy and a second "
        "that releases more than the first absorbed. What is the shape of the "
        "profile between its ends?",
      choices=[
        "The intermediate lies above the reactants and the products lie below "
        "them",
        "The intermediate lies below the reactants and the products lie above "
        "them",
        "Both the intermediate and the products lie above the reactants",
        "Both the intermediate and the products lie below the reactants",
        "The intermediate and the products lie at the same energy"],
      ans=0,
      why="EK 5.10.A.1 assembles the profile from the two steps in sequence, so "
          "an uphill first step raises the intermediate above the reactants and "
          "a larger downhill second step carries the products below them."),

 dict(q="What does the framework's phrase energetics of each elementary reaction "
        "refer to?",
      choices=[
        "The activation energy and the energy change of that step",
        "The rate constant and the order of that step",
        "The concentration of each species during that step",
        "The number of particles colliding in that step",
        "The time that step takes to complete"],
      ans=0,
      why="EK 5.10.A.1 makes those energetics what the profile is built from, "
          "and EK 5.6.A.3 with the learning objective for 5.6 names the two "
          "quantities an elementary reaction's profile carries."),

 dict(q="On the profile of a two-step mechanism, which quantity is NOT read from "
        "the two endpoints alone?",
      choices=[
        "The activation energy of either step",
        "The overall energy change of the reaction",
        "Whether the reaction releases energy overall",
        "Whether the products lie above the reactants",
        "The size of the difference between the reactants and the products"],
      ans=0,
      why="EK 5.6.A.3 makes an activation energy a difference involving a "
          "transition state, which lies between the ends, while the overall "
          "change and its direction are properties of the ends themselves."),

 dict(q="Two steps of a mechanism have equal activation energies. What follows "
        "about their transition states on the profile?",
      choices=[
        "They stand equally far above their own starting points, though not "
        "necessarily at the same energy",
        "They must stand at the same energy as one another",
        "They must stand at the same energy as the reactants",
        "One of them must be the highest point of the profile",
        "The two steps must have the same energy change as well"],
      ans=0,
      why="EK 5.6.A.3 makes each activation energy a difference from that step's "
          "own starting point, and EK 5.10.A.1 places those starting points at "
          "different heights along the assembled profile."),

 dict(q="How does the number of elementary steps in a mechanism show itself on "
        "the assembled energy profile?",
      choices=[
        "As the number of maxima, since each step contributes one transition "
        "state",
        "As the number of endpoints, since each step contributes one",
        "As the total height of the profile",
        "As the horizontal length of the reaction coordinate in seconds",
        "It does not show itself at all"],
      ans=0,
      why="EK 5.10.A.1 constructs the multistep profile from each elementary "
          "reaction, and EK 5.6.A.3 gives each elementary reaction a single "
          "transition state along its own stretch of the coordinate."),

 dict(q="If a proposed mechanism is replaced by one with an extra elementary "
        "step, what happens to the overall energy change shown by the profile?",
      choices=[
        "It is unchanged, because the two ends of the profile are the same "
        "reactants and products",
        "It increases, because there is one more step to contribute",
        "It decreases, because the energy is spread over more steps",
        "It becomes zero, because the extra step cancels the others",
        "It cannot be compared between the two mechanisms"],
      ans=0,
      why="EK 5.7.A.2 makes every acceptable mechanism combine to the same "
          "overall balanced equation, and EK 5.10.A.1's assembled profile runs "
          "between the reactants and the products of that equation whatever lies "
          "in between."),

 dict(q="Why is a multistep energy profile more informative about the mechanism "
        "than a single-step profile is?",
      choices=[
        "Because it shows a separate barrier and a separate energy change for "
        "each elementary step, together with the intermediates between them",
        "Because it uses a longer reaction coordinate",
        "Because it shows the concentration of each species at every moment",
        "Because it gives the rate constant of the overall reaction directly",
        "Because a single-step profile has no transition state"],
      ans=0,
      why="EK 5.10.A.1 builds the multistep profile out of the energetics of "
          "each elementary reaction, and EK 5.7.A.3's intermediates appear as "
          "the points between successive steps, none of which a one-step profile "
          "carries."),
]
