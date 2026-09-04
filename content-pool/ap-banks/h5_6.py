# AP CHEMISTRY 5.6 Reaction Energy Profile
# CED effective Fall 2024, Unit 5 Kinetics.
# Learning objective 5.6.A: represent the activation energy and overall energy
# change in an elementary reaction using a reaction energy profile. Suggested
# skill 3.B, represent chemical substances or phenomena with appropriate
# diagrams or models.
#
# Essential knowledge relied on, in the framework's own words:
#   5.6.A.1  Elementary reactions typically involve the breaking of some bonds
#            and the forming of new ones.
#   5.6.A.2  The reaction coordinate is the axis along which the complex set of
#            motions involved in rearranging reactants to form products can be
#            plotted.
#   5.6.A.3  The energy profile gives the energy along the reaction coordinate,
#            which typically proceeds from reactants, through a transition
#            state, to products. The energy difference between the reactants
#            and the transition state is the activation energy for the forward
#            reaction.
#   5.6.A.4  The rate of an elementary reaction is temperature dependent because
#            the proportion of particle collisions that are energetic enough to
#            reach the transition state varies with temperature. The Arrhenius
#            equation relates the temperature dependence of the rate of an
#            elementary reaction to the activation energy needed by molecular
#            collisions to reach the transition state.
#            Exclusion statement: calculations involving the Arrhenius equation
#            will not be assessed on the AP Exam.
#
# THE FIGURE PROBLEM IS AT ITS WORST HERE, AND IS THE REASON THIS MODULE IS
# BUILT OUT OF TABLES. The topic is named after a graph. This bank cannot show
# one, and a stem that says "in the profile above" with nothing behind it is a
# defect this project has already shipped once. So every profile in this module
# is a TABLE OF ENERGIES at named points along the reaction coordinate, and each
# question is asked of those energies. Two quantities are then arithmetic a
# checker can redo: the activation energy is the transition state minus the
# reactants, and the overall energy change is the products minus the reactants.
#
# THE EXCLUSION STATEMENT IS OBEYED. No item computes anything from the
# Arrhenius equation. It is named only where EK 5.6.A.4 names it -- as the
# relationship between the temperature dependence of the rate and the activation
# energy.
#
# WHAT IS NOT HERE. Why only some collisions succeed is 5.5, and h5_5.py owns
# the distribution of collision energies. A profile with more than one maximum
# is a MULTISTEP profile and belongs to 5.10; every profile here is for a single
# elementary reaction, and the one item that mentions the difference says so.
# How a catalyst lowers the activation energy is 5.11.
#
# NOTATION. Chemistry is not typeset. Energies are written as plain text with
# their units, "130 kJ/mol", and every numeric choice carries a short clause
# saying what the number is, so that no choice is a truncation of another.
TOPIC = ("5.6", "Reaction Energy Profile", 5)

_T_P1 = dict(
    headers=["Point along the reaction coordinate", "Energy (kJ/mol)"],
    rows=[["Reactants", "50"],
          ["Transition state", "180"],
          ["Products", "20"]])

_T_P2 = dict(
    headers=["Point along the reaction coordinate", "Energy (kJ/mol)"],
    rows=[["Reactants", "40"],
          ["Transition state", "150"],
          ["Products", "110"]])

_T_COMPARE = dict(
    headers=["Elementary reaction", "Energy of the reactants (kJ/mol)",
             "Energy of the transition state (kJ/mol)",
             "Energy of the products (kJ/mol)"],
    rows=[["R1", "30", "150", "80"],
          ["R2", "30", "95", "80"],
          ["R3", "30", "210", "80"]])

_T_POINTS = dict(
    headers=["Point along the reaction coordinate", "Energy (kJ/mol)"],
    rows=[["Point 1", "25"],
          ["Point 2", "95"],
          ["Point 3", "140"],
          ["Point 4", "60"]])

_T_P5 = dict(
    headers=["Point along the reaction coordinate", "Energy (kJ/mol)"],
    rows=[["Reactants", "20"],
          ["Transition state", "200"],
          ["Products", "120"]])

QUESTIONS = [

 dict(q="How does the framework define the reaction coordinate?",
      choices=[
        "The axis along which the complex set of motions that rearrange "
        "reactants into products can be plotted",
        "The axis along which the time elapsed since mixing is plotted",
        "The axis along which the concentration of the reactants is plotted",
        "The axis along which the temperature of the reacting mixture is "
        "plotted",
        "The axis along which the number of collisions per second is plotted"],
      ans=0,
      why="EK 5.6.A.2, near verbatim: the reaction coordinate is the axis along "
          "which the complex set of motions involved in rearranging reactants "
          "to form products can be plotted. It is a coordinate of rearrangement, "
          "not of clock time."),

 dict(q="What does the framework say an energy profile gives?",
      choices=[
        "The energy along the reaction coordinate",
        "The rate constant at each temperature",
        "The concentration of each species at each moment",
        "The number of particles present at each energy",
        "The order of the reaction with respect to each reactant"],
      ans=0,
      why="EK 5.6.A.3, verbatim in substance: the energy profile gives the "
          "energy along the reaction coordinate. A distribution of particle "
          "energies is EK 5.5.A.3's curve, which is a different representation."),

 dict(q="In what order does an energy profile typically proceed?",
      choices=[
        "From reactants, through a transition state, to products",
        "From products, through an intermediate, to reactants",
        "From reactants, through a catalyst, to products",
        "From the transition state, through the reactants, to the products",
        "From reactants directly to products with nothing in between"],
      ans=0,
      why="EK 5.6.A.3 states that the reaction coordinate typically proceeds "
          "from reactants, through a transition state, to products. An "
          "intermediate belongs to a mechanism of more than one step, which is "
          "EK 5.7.A.3's material."),

 dict(q="Which energy difference does the framework identify as the activation "
        "energy for the forward reaction?",
      choices=[
        "The difference between the reactants and the transition state",
        "The difference between the reactants and the products",
        "The difference between the transition state and the products",
        "The difference between the products and the highest point after them",
        "The total energy of the reactants alone"],
      ans=0,
      why="EK 5.6.A.3, near verbatim: the energy difference between the "
          "reactants and the transition state is the activation energy for the "
          "forward reaction. The reactant-to-product difference is the overall "
          "energy change instead."),

 dict(q="What does the framework say elementary reactions typically involve?",
      choices=[
        "The breaking of some bonds and the forming of new ones",
        "The breaking of every bond in every reactant",
        "The forming of new bonds with no bonds broken",
        "A change in the nuclei of the atoms taking part",
        "The transfer of whole atoms with no bonds affected"],
      ans=0,
      why="EK 5.6.A.1, verbatim in substance: elementary reactions typically "
          "involve the breaking of some bonds and the forming of new ones. The "
          "word is SOME, not all."),

 dict(q="The table gives the energy at three points along the reaction "
        "coordinate of an elementary reaction. What is the activation energy "
        "for the forward reaction?",
      table=_T_P1,
      choices=[
        "130 kJ/mol, the rise from the reactants to the transition state",
        "160 kJ/mol, the fall from the transition state to the products",
        "30 kJ/mol, the difference between the reactants and the products",
        "180 kJ/mol, the energy of the transition state itself",
        "50 kJ/mol, the energy of the reactants themselves"],
      ans=0,
      why="EK 5.6.A.3 makes the activation energy for the forward reaction the "
          "energy difference between the reactants and the transition state, "
          "which the tabulated energies fix by subtraction."),

 dict(q="Using the same tabulated energies, what is the overall energy change "
        "for that elementary reaction?",
      table=_T_P1,
      choices=[
        "30 kJ/mol is released, so the overall change is negative",
        "30 kJ/mol is absorbed, so the overall change is positive",
        "130 kJ/mol is released, since that is the activation energy",
        "160 kJ/mol is absorbed, since that is the fall to the products",
        "180 kJ/mol is released, since that is the highest tabulated energy"],
      ans=0,
      why="The learning objective pairs the activation energy with the overall "
          "energy change, and EK 5.6.A.3's profile makes that change the "
          "difference between the products and the reactants; the products lie "
          "below the reactants, so energy leaves the system."),

 dict(q="For the same elementary reaction, what is the activation energy of the "
        "REVERSE reaction, in which the products are converted back to the "
        "reactants?",
      table=_T_P1,
      choices=[
        "160 kJ/mol, the climb from the products up to the transition state",
        "130 kJ/mol, the climb from the reactants up to the transition state",
        "30 kJ/mol, the difference between the reactants and the products",
        "20 kJ/mol, the energy of the products themselves",
        "180 kJ/mol, the energy of the transition state itself"],
      ans=0,
      why="EK 5.6.A.3 calls the reactant-to-transition-state difference the "
          "activation energy FOR THE FORWARD REACTION, which marks the reverse "
          "as the mirrored climb from the products to the same transition "
          "state."),

 dict(q="Why is the rate of an elementary reaction temperature dependent?",
      choices=[
        "Because the proportion of particle collisions energetic enough to "
        "reach the transition state varies with temperature",
        "Because the activation energy itself falls as the temperature rises",
        "Because the products become more stable as the temperature rises",
        "Because the reaction coordinate lengthens as the temperature rises",
        "Because the number of particles in the sample increases with "
        "temperature"],
      ans=0,
      why="EK 5.6.A.4, near verbatim: the rate of an elementary reaction is "
          "temperature dependent because the proportion of particle collisions "
          "that are energetic enough to reach the transition state varies with "
          "temperature. The requirement stays put; the proportion meeting it "
          "changes."),

 dict(q="What does the framework say the Arrhenius equation relates?",
      choices=[
        "The temperature dependence of the rate of an elementary reaction to "
        "the activation energy needed to reach the transition state",
        "The concentration of a reactant to the rate of the reaction",
        "The overall energy change of a reaction to its rate constant",
        "The number of elementary steps in a mechanism to the overall rate law",
        "The pressure of a gaseous reactant to the position of its transition "
        "state"],
      ans=0,
      why="EK 5.6.A.4 states exactly this relationship. Tying rate to "
          "concentration is EK 5.2.A.1's rate law, a different relationship "
          "entirely."),

 dict(q="The table gives the energies at three points along the reaction "
        "coordinate of a different elementary reaction. What is its activation "
        "energy in the forward direction?",
      table=_T_P2,
      choices=[
        "110 kJ/mol, the rise from the reactants to the transition state",
        "70 kJ/mol, the difference between the products and the reactants",
        "40 kJ/mol, the fall from the transition state to the products",
        "150 kJ/mol, the energy of the transition state itself",
        "260 kJ/mol, the sum of the reactant and product energies"],
      ans=0,
      why="EK 5.6.A.3 makes the activation energy for the forward reaction the "
          "energy difference between the reactants and the transition state, "
          "which subtraction of the tabulated energies gives directly."),

 dict(q="For that same reaction, what does the relationship between the "
        "reactant and product energies say about the overall energy change?",
      table=_T_P2,
      choices=[
        "70 kJ/mol is absorbed, because the products lie above the reactants",
        "70 kJ/mol is released, because the products lie below the reactants",
        "110 kJ/mol is absorbed, because that is the activation energy",
        "40 kJ/mol is released, because that is the drop to the products",
        "The overall change is zero, because a transition state lies between "
        "them"],
      ans=0,
      why="The learning objective covers the overall energy change as well as "
          "the activation energy, and EK 5.6.A.3's profile places the products "
          "above the reactants here, so the system finishes with more energy "
          "than it started with."),

 dict(q="The table gives the energies of the reactants, the transition state "
        "and the products for three elementary reactions. Which has the "
        "greatest activation energy in the forward direction?",
      table=_T_COMPARE,
      choices=[
        "R3",
        "R1",
        "R2",
        "All three are equal, because their overall energy changes are equal",
        "It cannot be determined from the tabulated energies"],
      ans=0,
      why="EK 5.6.A.3 makes the activation energy the difference between the "
          "reactants and the transition state, so subtracting the two tabulated "
          "columns for each reaction ranks them; the equal overall changes are "
          "irrelevant to that difference."),

 dict(q="Those three elementary reactions have the same reactant energy and the "
        "same product energy. What follows about their overall energy changes?",
      table=_T_COMPARE,
      choices=[
        "All three overall energy changes are equal, even though the activation "
        "energies differ",
        "The reaction with the largest activation energy has the largest "
        "overall energy change",
        "The reaction with the smallest activation energy has the largest "
        "overall energy change",
        "The overall energy changes cannot be compared without knowing the "
        "temperature",
        "All three overall energy changes are zero"],
      ans=0,
      why="EK 5.6.A.3 defines the two quantities by different pairs of points: "
          "the activation energy uses the transition state and the overall "
          "change uses the products, so equal reactant and product energies fix "
          "one while leaving the other free."),

 dict(q="An elementary reaction has its products at a higher energy than its "
        "reactants. What does the profile show about the process?",
      choices=[
        "The system finishes with more energy than it began with, so the "
        "process absorbs energy overall",
        "The system finishes with less energy than it began with, so the "
        "process releases energy overall",
        "The system finishes with the same energy, since a transition state "
        "returns it",
        "The activation energy must be zero",
        "The reaction cannot occur at any temperature"],
      ans=0,
      why="EK 5.6.A.3's profile gives the energy along the coordinate and the "
          "learning objective names the overall energy change as the difference "
          "the profile represents, which is positive when the products lie "
          "higher."),

 dict(q="Which point on a reaction energy profile for an elementary reaction "
        "carries the highest energy?",
      choices=[
        "The transition state",
        "The reactants",
        "The products",
        "Whichever end of the profile lies higher",
        "A point midway along the reaction coordinate"],
      ans=0,
      why="EK 5.6.A.3 has the coordinate proceed from reactants, through a "
          "transition state, to products, and makes the reactant to transition "
          "state difference an activation energy that must be supplied, so the "
          "transition state stands above both ends."),

 dict(q="The table gives the energy at four points along the reaction "
        "coordinate of an elementary reaction, in the order they are passed. "
        "Which point is the transition state?",
      table=_T_POINTS,
      choices=[
        "Point 3",
        "Point 1",
        "Point 2",
        "Point 4",
        "There is no transition state among the tabulated points"],
      ans=0,
      why="EK 5.6.A.3 places the transition state between the reactants and the "
          "products and makes the climb to it the activation energy, so it is "
          "the point of greatest energy among those tabulated."),

 dict(q="Raising the temperature of a sample increases the rate of an "
        "elementary reaction. What has changed?",
      choices=[
        "The proportion of collisions with enough energy to reach the "
        "transition state, not the height of the transition state",
        "The height of the transition state, not the proportion of collisions "
        "reaching it",
        "The overall energy change of the reaction",
        "The identity of the products the reaction forms",
        "The position of the reactants along the reaction coordinate"],
      ans=0,
      why="EK 5.6.A.4 attributes the temperature dependence to the proportion "
          "of particle collisions that are energetic enough to reach the "
          "transition state, which locates the change in the collisions rather "
          "than in the energy requirement."),

 dict(q="An elementary reaction releases energy overall. How do its forward and "
        "reverse activation energies compare?",
      choices=[
        "The reverse activation energy is the larger, because the products "
        "start lower and must climb farther to the same transition state",
        "The forward activation energy is the larger, because the forward "
        "reaction is the one that occurs",
        "The two are equal, because they share a transition state",
        "The reverse activation energy is zero, because the reverse reaction "
        "does not occur",
        "The comparison depends on the temperature"],
      ans=0,
      why="EK 5.6.A.3 measures the forward activation energy from the reactants "
          "to the transition state, and a reaction that releases energy has its "
          "products below its reactants, so the climb from the products to the "
          "same transition state is the longer one."),

 dict(q="An elementary reaction has a forward activation energy of 90 kJ/mol "
        "and releases 40 kJ/mol overall. What is the activation energy of the "
        "reverse reaction?",
      choices=[
        "130 kJ/mol, the forward barrier plus the energy released",
        "50 kJ/mol, the forward barrier minus the energy released",
        "90 kJ/mol, the same as the forward barrier",
        "40 kJ/mol, the energy released",
        "3600 kJ/mol, the product of the two figures"],
      ans=0,
      why="EK 5.6.A.3's profile places the transition state 90 kJ/mol above the "
          "reactants and, since energy is released, the products 40 kJ/mol "
          "below them, so the products stand that much farther below the same "
          "transition state."),

 dict(q="An elementary reaction has a forward activation energy of 75 kJ/mol "
        "and a reverse activation energy of 120 kJ/mol. What is its overall "
        "energy change?",
      choices=[
        "45 kJ/mol is released, because the products lie below the reactants",
        "45 kJ/mol is absorbed, because the products lie above the reactants",
        "195 kJ/mol is released, the sum of the two barriers",
        "75 kJ/mol is absorbed, the forward barrier",
        "The overall energy change cannot be found from two activation "
        "energies"],
      ans=0,
      why="EK 5.6.A.3 measures both barriers from the same transition state, so "
          "the reactants stand 75 kJ/mol below it and the products 120 kJ/mol "
          "below it, which puts the products lower than the reactants."),

 dict(q="Two elementary reactions are carried out at the same temperature. One "
        "has an activation energy of 60 kJ/mol and the other 140 kJ/mol. Which "
        "is expected to be faster, and why?",
      choices=[
        "The one with the 60 kJ/mol barrier, because a larger proportion of "
        "collisions carries enough energy to reach its transition state",
        "The one with the 140 kJ/mol barrier, because more energy is available "
        "to it",
        "They proceed at the same rate, because they are at the same "
        "temperature",
        "The one with the 140 kJ/mol barrier, because a higher transition state "
        "is reached sooner",
        "Neither can proceed, because both barriers exceed the energy of an "
        "ordinary collision"],
      ans=0,
      why="EK 5.6.A.4 ties the rate to the proportion of collisions energetic "
          "enough to reach the transition state, and EK 5.5.A.2 makes only a "
          "small fraction of collisions sufficiently energetic, so a lower "
          "requirement is met by more of them at a given temperature."),

 dict(q="What happens to the bonds in the reactants as the system climbs toward "
        "the transition state?",
      choices=[
        "Some of them are being broken while new ones are beginning to form, "
        "which is why energy must be supplied to get there",
        "All of them are broken before any new bond begins to form",
        "None of them changes until the products have been reached",
        "They are replaced by nuclei of different elements",
        "They lengthen but never break at any point"],
      ans=0,
      why="EK 5.6.A.1 says elementary reactions typically involve the breaking "
          "of some bonds and the forming of new ones, and EK 5.6.A.3 makes the "
          "rise to the transition state the activation energy that must be "
          "supplied for that rearrangement."),

 dict(q="The table gives the energies at three points for an elementary "
        "reaction that absorbs energy. What is its forward activation energy?",
      table=_T_P5,
      choices=[
        "180 kJ/mol, the rise from the reactants to the transition state",
        "100 kJ/mol, the difference between the products and the reactants",
        "80 kJ/mol, the fall from the transition state to the products",
        "200 kJ/mol, the energy of the transition state itself",
        "20 kJ/mol, the energy of the reactants themselves"],
      ans=0,
      why="EK 5.6.A.3 makes the forward activation energy the difference "
          "between the reactants and the transition state, which subtraction of "
          "the tabulated energies gives whether the overall change is positive "
          "or negative."),

 dict(q="For that same reaction, what is the reverse activation energy, and how "
        "does it compare with the forward one?",
      table=_T_P5,
      choices=[
        "80 kJ/mol, smaller than the forward barrier because the products lie "
        "above the reactants",
        "80 kJ/mol, larger than the forward barrier because the products lie "
        "below the reactants",
        "180 kJ/mol, equal to the forward barrier because they share a "
        "transition state",
        "280 kJ/mol, the sum of the two tabulated differences",
        "100 kJ/mol, the difference between the products and the reactants"],
      ans=0,
      why="EK 5.6.A.3's forward barrier runs from the reactants to the "
          "transition state, so the reverse runs from the products to the same "
          "point; products lying above the reactants make that climb the "
          "shorter of the two."),

 dict(q="Why does the profile of the reverse reaction pass through the same "
        "highest point as the forward one?",
      choices=[
        "Because the same rearrangement of the same particles is being traced "
        "in the opposite direction along the reaction coordinate",
        "Because activation energies are always equal in the two directions",
        "Because the reverse reaction has no transition state of its own",
        "Because the products of the forward reaction have no energy",
        "Because the reaction coordinate is measured in units of time"],
      ans=0,
      why="EK 5.6.A.2 makes the coordinate an axis of the motions that rearrange "
          "reactants into products, and EK 5.6.A.3 places one transition state "
          "along it, so reversing the direction of travel does not create a "
          "different summit."),

 dict(q="How many maxima does the energy profile of a single elementary "
        "reaction have?",
      choices=[
        "One, the transition state it passes through",
        "Two, one for the reactants and one for the products",
        "As many as there are bonds broken during the reaction",
        "None, because the energy falls steadily from reactants to products",
        "One for every particle that takes part in the collision"],
      ans=0,
      why="EK 5.6.A.3 has the coordinate proceed from reactants, through A "
          "transition state, to products. A profile with more than one maximum "
          "belongs to a mechanism of several elementary steps, which is EK "
          "5.10.A.1's material."),

 dict(q="Which pair of quantities does the learning objective for this topic "
        "ask a student to represent with a reaction energy profile?",
      choices=[
        "The activation energy and the overall energy change",
        "The rate constant and the order of the reaction",
        "The concentration of each reactant and the time",
        "The number of collisions and their orientations",
        "The equilibrium constant and the reaction quotient"],
      ans=0,
      why="The learning objective for 5.6 names exactly those two, and EK "
          "5.6.A.3 supplies the definition of the first as the reactant to "
          "transition state difference while the profile's endpoints supply the "
          "second."),

 dict(q="A student claims that lowering the temperature changes the activation "
        "energy of an elementary reaction. What is the framework's position?",
      choices=[
        "Temperature changes the proportion of collisions that meet the "
        "activation energy, which is a property of the profile itself",
        "Temperature changes the activation energy in direct proportion to the "
        "change in kelvins",
        "Temperature changes the activation energy only for reactions that "
        "release energy",
        "Temperature has no effect on the rate of an elementary reaction at all",
        "Temperature changes the overall energy change rather than the rate"],
      ans=0,
      why="EK 5.6.A.4 locates the temperature dependence in the proportion of "
          "particle collisions energetic enough to reach the transition state, "
          "while EK 5.6.A.3 fixes the activation energy as a difference between "
          "two points on the profile."),

 dict(q="Why can an elementary reaction that releases energy overall still be "
        "slow at room temperature?",
      choices=[
        "Because the rate depends on the climb to the transition state, which "
        "can be high however far the products fall below the reactants",
        "Because a reaction that releases energy must always be slow",
        "Because the overall energy change and the activation energy are the "
        "same quantity measured twice",
        "Because energy released by the reaction is used to break the products "
        "apart again",
        "Because the reaction coordinate is longer for reactions that release "
        "energy"],
      ans=0,
      why="EK 5.6.A.3 defines the activation energy and the overall change by "
          "different pairs of points on the profile, and EK 5.6.A.4 ties the "
          "rate to the collisions able to meet the activation energy alone."),
]
