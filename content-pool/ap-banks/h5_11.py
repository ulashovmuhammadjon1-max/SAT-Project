# AP CHEMISTRY 5.11 Catalysis
# CED effective Fall 2024, Unit 5 Kinetics.
# Learning objective 5.11.A: explain the relationship between the effect of a
# catalyst on a reaction and changes in the reaction mechanism. Suggested skill
# 6.E, provide reasoning to justify a claim using connections between
# particulate and macroscopic scales or levels.
#
# Essential knowledge relied on, in the framework's own words:
#   5.11.A.1  In order for a catalyst to increase the rate of a reaction, the
#             addition of the catalyst must increase the number of effective
#             collisions and/or provide a reaction path with a lower activation
#             energy relative to the original reaction coordinate.
#   5.11.A.2  In a reaction mechanism containing a catalyst, the net
#             concentration of the catalyst is constant. However, the catalyst
#             will frequently be consumed in the rate-determining step of the
#             reaction, only to be regenerated in a subsequent step in the
#             mechanism.
#   5.11.A.3  Some catalysts accelerate a reaction by binding to the
#             reactant(s). The reactants are either oriented more favorably or
#             react with lower activation energy. There is often a new reaction
#             intermediate in which the catalyst is bound to the reactant(s).
#             Many enzymes function in this manner.
#   5.11.A.4  Some catalysts involve covalent bonding between the catalyst and
#             the reactant(s). An example is acid-base catalysis, in which a
#             reactant or intermediate either gains or loses a proton. This
#             introduces a new reaction intermediate and new elementary
#             reactions involving that intermediate.
#   5.11.A.5  In surface catalysis, a reactant or intermediate binds to, or
#             forms a covalent bond with, the surface. This introduces
#             elementary reactions involving these new bound reaction
#             intermediate(s).
#
# THE LEARNING OBJECTIVE IS THE SPINE: the effect of a catalyst is EXPLAINED
# THROUGH THE MECHANISM. Every one of the five essential knowledge statements
# says something about what the catalyst does to the sequence of elementary
# steps -- it is consumed and regenerated within it, or it adds a new
# intermediate and new steps to it. So the module keeps returning to the
# mechanism rather than treating a catalyst as a substance that simply makes
# things faster.
#
# WHAT THE FRAMEWORK DOES NOT SAY, AND THIS MODULE DOES NOT CLAIM. 5.11.A.1
# gives two routes, "increase the number of effective collisions AND/OR provide
# a reaction path with a lower activation energy", so no item here asserts that
# lowering the barrier is the only mechanism. 5.11.A.3 says MANY enzymes
# function by binding, not all, and no key here says otherwise.
#
# NO PICTURES. Where a catalyzed and an uncatalyzed path are compared, the
# comparison is a table of activation energies and endpoint energies, and the
# question is asked of the table. Mechanisms are tables of elementary steps, as
# in h5_7.py and h5_8.py.
#
# NOTATION. Chemistry is not typeset. Formulas are plain text, the arrow is the
# word "gives", ions are written H3O+ in the ordinary way, and a surface site is
# written M, as a mechanism for surface catalysis conventionally does.
TOPIC = ("5.11", "Catalysis", 5)

_M_OZONE = dict(
    headers=["Step", "Elementary reaction"],
    rows=[["Step 1", "Cl + O3 gives ClO + O2"],
          ["Step 2", "ClO + O gives Cl + O2"]])

_M_ACID = dict(
    headers=["Step", "Elementary reaction"],
    rows=[["Step 1", "HCOOH + H3O+ gives HCOOH2+ + H2O"],
          ["Step 2", "HCOOH2+ gives CO + H3O+"]])

_M_SURFACE = dict(
    headers=["Step", "Elementary reaction"],
    rows=[["Step 1", "H2 + 2 M gives 2 MH"],
          ["Step 2", "C2H4 + 2 MH gives C2H6 + 2 M"]])

_T_PATHS = dict(
    headers=["Path", "Activation energy (kJ/mol)",
             "Energy of the reactants (kJ/mol)", "Energy of the products (kJ/mol)"],
    rows=[["Without the catalyst", "150", "50", "20"],
          ["With the catalyst", "90", "50", "20"]])

QUESTIONS = [

 dict(q="According to the framework, what must the addition of a catalyst do if "
        "it is to increase the rate of a reaction?",
      choices=[
        "Increase the number of effective collisions and/or provide a reaction "
        "path with a lower activation energy",
        "Increase the concentration of the reactants",
        "Raise the temperature at which the reaction is carried out",
        "Lower the energy of the products relative to the reactants",
        "Remove one of the products as it is formed"],
      ans=0,
      why="EK 5.11.A.1, near verbatim: the addition of the catalyst must "
          "increase the number of effective collisions and/or provide a reaction "
          "path with a lower activation energy relative to the original reaction "
          "coordinate."),

 dict(q="In a reaction mechanism containing a catalyst, what does the framework "
        "say about the catalyst's net concentration?",
      choices=[
        "It is constant",
        "It falls steadily as the reaction proceeds",
        "It rises steadily as the reaction proceeds",
        "It falls to zero before the reaction is complete",
        "It doubles each time the rate-determining step occurs"],
      ans=0,
      why="EK 5.11.A.2, verbatim in substance: in a reaction mechanism "
          "containing a catalyst, the net concentration of the catalyst is "
          "constant, even though individual steps consume and regenerate it."),

 dict(q="Where does the framework say a catalyst is frequently consumed, and "
        "where is it regenerated?",
      choices=[
        "Consumed in the rate-determining step and regenerated in a subsequent "
        "step",
        "Consumed in the last step and regenerated in the first",
        "Consumed and regenerated within the same single elementary step",
        "Consumed in every step and never regenerated",
        "Neither consumed nor regenerated at any point"],
      ans=0,
      why="EK 5.11.A.2 states that the catalyst will frequently be consumed in "
          "the rate-determining step of the reaction, only to be regenerated in "
          "a subsequent step in the mechanism."),

 dict(q="How does the framework say many enzymes accelerate a reaction?",
      choices=[
        "By binding to the reactants",
        "By raising the temperature of the surrounding solution",
        "By increasing the concentration of the reactants",
        "By lowering the energy of the products",
        "By removing an intermediate from the mixture"],
      ans=0,
      why="EK 5.11.A.3 says some catalysts accelerate a reaction by binding to "
          "the reactants and adds that many enzymes function in this manner. The "
          "framework says many, not all."),

 dict(q="When a catalyst binds to the reactants, what does the framework say "
        "happens to them?",
      choices=[
        "They are either oriented more favorably or react with lower activation "
        "energy",
        "They are converted directly into products without any further step",
        "They are held apart so that they cannot collide",
        "They are raised to a higher energy than the transition state",
        "They exchange atoms with the catalyst permanently"],
      ans=0,
      why="EK 5.11.A.3, near verbatim: the reactants are either oriented more "
          "favorably or react with lower activation energy. Both routes appear "
          "in EK 5.11.A.1's pair as well."),

 dict(q="What does the framework say often appears in a mechanism when a "
        "catalyst binds to the reactants?",
      choices=[
        "A new reaction intermediate in which the catalyst is bound to the "
        "reactants",
        "A second transition state with no intermediate between the steps",
        "A new product that the uncatalyzed reaction does not form",
        "A new reactant supplied by the catalyst",
        "An elementary step with no reactants at all"],
      ans=0,
      why="EK 5.11.A.3 states that there is often a new reaction intermediate in "
          "which the catalyst is bound to the reactants, which is one of the "
          "changes to the mechanism the learning objective asks about."),

 dict(q="What happens in acid-base catalysis, the example the framework gives of "
        "catalysis involving covalent bonding?",
      choices=[
        "A reactant or intermediate either gains or loses a proton",
        "A reactant is oxidized while the catalyst is reduced",
        "The catalyst dissolves the reactants in a new solvent",
        "The catalyst raises the concentration of the reactant",
        "A reactant is adsorbed onto a metal surface"],
      ans=0,
      why="EK 5.11.A.4 names acid-base catalysis as an example of catalysis "
          "involving covalent bonding between catalyst and reactant, in which a "
          "reactant or intermediate either gains or loses a proton. Adsorption "
          "onto a surface is EK 5.11.A.5's case."),

 dict(q="What does acid-base catalysis introduce into the mechanism, according "
        "to the framework?",
      choices=[
        "A new reaction intermediate and new elementary reactions involving that "
        "intermediate",
        "A single elementary reaction replacing all the others",
        "A new product that is not formed without the catalyst",
        "A transition state with no activation energy",
        "A step in which no bonds are broken or formed"],
      ans=0,
      why="EK 5.11.A.4 states that this introduces a new reaction intermediate "
          "and new elementary reactions involving that intermediate, which is "
          "exactly the change to the mechanism the learning objective asks a "
          "student to explain."),

 dict(q="What happens in surface catalysis, according to the framework?",
      choices=[
        "A reactant or intermediate binds to, or forms a covalent bond with, the "
        "surface",
        "The surface increases the temperature of the reacting mixture",
        "The surface supplies electrons that are consumed by the reactants",
        "The surface removes the products as fast as they are formed",
        "The surface raises the concentration of the catalyst in solution"],
      ans=0,
      why="EK 5.11.A.5, near verbatim: in surface catalysis, a reactant or "
          "intermediate binds to, or forms a covalent bond with, the surface."),

 dict(q="What does surface catalysis introduce into the mechanism?",
      choices=[
        "Elementary reactions involving new bound reaction intermediates",
        "A single elementary reaction with no intermediates",
        "An extra product formed only on the surface",
        "A reaction path with no transition state",
        "A change in the overall balanced equation of the reaction"],
      ans=0,
      why="EK 5.11.A.5 states that this introduces elementary reactions "
          "involving these new bound reaction intermediates, which is a change "
          "to the mechanism rather than to the overall equation."),

 dict(q="The table gives a two-step mechanism for the destruction of ozone. "
        "Which species acts as the catalyst?",
      table=_M_OZONE,
      choices=[
        "Cl, the chlorine atom",
        "ClO, the chlorine monoxide radical",
        "O3, ozone",
        "O2, dioxygen",
        "O, the oxygen atom"],
      ans=0,
      why="EK 5.11.A.2 has a catalyst consumed in one step and regenerated in a "
          "subsequent step, leaving its net concentration constant, which is "
          "what the two tabulated steps do to exactly one species."),

 dict(q="In that same tabulated mechanism, which species is the reaction "
        "intermediate rather than the catalyst?",
      table=_M_OZONE,
      choices=[
        "ClO, the chlorine monoxide radical",
        "Cl, the chlorine atom",
        "O3, ozone",
        "O2, dioxygen",
        "O, the oxygen atom"],
      ans=0,
      why="EK 5.7.A.3 makes an intermediate a species produced by an earlier "
          "step and consumed by a later one, which is the mirror image of EK "
          "5.11.A.2's catalyst, consumed first and regenerated afterwards."),

 dict(q="The table gives a two-step mechanism for the decomposition of formic "
        "acid in acid solution. Which species is the catalyst?",
      table=_M_ACID,
      choices=[
        "H3O+, the hydronium ion",
        "HCOOH2+, the protonated acid",
        "HCOOH, formic acid",
        "H2O, water",
        "CO, carbon monoxide"],
      ans=0,
      why="EK 5.11.A.2 has the catalyst consumed in one step and regenerated in "
          "a subsequent one with its net concentration unchanged, and EK 5.11.A.4 "
          "makes the gain of a proton by a reactant the characteristic move of "
          "acid-base catalysis."),

 dict(q="Which kind of catalysis does that formic acid mechanism illustrate?",
      table=_M_ACID,
      choices=[
        "Acid-base catalysis, in which a reactant gains a proton",
        "Surface catalysis, in which a reactant binds to a solid",
        "Enzyme catalysis, in which a protein binds the reactants",
        "Catalysis by an increase in the number of collisions alone",
        "Catalysis in which the catalyst is permanently consumed"],
      ans=0,
      why="EK 5.11.A.4 gives acid-base catalysis as its example, in which a "
          "reactant or intermediate either gains or loses a proton, introducing "
          "a new intermediate and new elementary reactions, which is what the "
          "tabulated steps show."),

 dict(q="The table gives a two-step mechanism for the addition of hydrogen to "
        "ethene on a metal surface, where M is a site on that surface. Which "
        "species acts as the catalyst?",
      table=_M_SURFACE,
      choices=[
        "M, a site on the metal surface",
        "MH, a hydrogen atom bound to the surface",
        "H2, dihydrogen",
        "C2H4, ethene",
        "C2H6, ethane"],
      ans=0,
      why="EK 5.11.A.2 has the catalyst consumed in one step and regenerated in "
          "a subsequent one, and EK 5.11.A.5 has the reactant bind to the "
          "surface, so the surface sites are used and freed again."),

 dict(q="In that surface mechanism, what does the species written MH represent?",
      table=_M_SURFACE,
      choices=[
        "A bound reaction intermediate, a hydrogen atom held on a surface site",
        "The catalyst itself, before any reaction has occurred",
        "A product of the overall reaction",
        "A reactant of the overall reaction",
        "A transition state between the two elementary steps"],
      ans=0,
      why="EK 5.11.A.5 says surface catalysis introduces elementary reactions "
          "involving new BOUND reaction intermediates, and EK 5.7.A.3 makes an "
          "intermediate a species produced by one step and consumed by another."),

 dict(q="The table compares the same reaction carried out with and without a "
        "catalyst. What has the catalyst changed?",
      table=_T_PATHS,
      choices=[
        "The activation energy, while leaving the reactant and product energies "
        "unchanged",
        "The energies of the reactants and the products, while leaving the "
        "activation energy unchanged",
        "Both the activation energy and the overall energy change",
        "Neither the activation energy nor the overall energy change",
        "The overall energy change only"],
      ans=0,
      why="EK 5.11.A.1 has the catalyst provide a reaction path with a lower "
          "activation energy RELATIVE TO THE ORIGINAL REACTION COORDINATE, that "
          "is a different route between the same two ends, which is what the "
          "tabulated energies show."),

 dict(q="Using the same table, by how much has the catalyst lowered the "
        "activation energy?",
      table=_T_PATHS,
      choices=[
        "60 kJ/mol, the difference between the two tabulated barriers",
        "30 kJ/mol, the difference between the reactants and the products",
        "90 kJ/mol, the barrier of the catalyzed path itself",
        "150 kJ/mol, the barrier of the uncatalyzed path itself",
        "240 kJ/mol, the sum of the two tabulated barriers"],
      ans=0,
      why="EK 5.11.A.1 makes the catalyst's contribution a lower activation "
          "energy relative to the original coordinate, so subtracting the two "
          "tabulated barriers gives the amount by which it has been lowered."),

 dict(q="Why does a catalyst not appear in the overall balanced equation of the "
        "reaction it speeds up?",
      choices=[
        "Because it is regenerated as fast as it is consumed, so it cancels when "
        "the steps are combined",
        "Because it takes no part in any elementary step",
        "Because it is present in too small an amount to write down",
        "Because the overall equation lists only substances that change phase",
        "Because it is a product rather than a reactant"],
      ans=0,
      why="EK 5.11.A.2 keeps the catalyst's net concentration constant by having "
          "it consumed and then regenerated, and EK 5.7.A.2 makes the overall "
          "equation what the combined steps leave, so anything consumed and "
          "reformed cancels out of it."),

 dict(q="What distinguishes a catalyst from a reaction intermediate in a "
        "mechanism?",
      choices=[
        "A catalyst is present before the reaction begins and is consumed before "
        "being regenerated; an intermediate is made first and consumed after",
        "A catalyst appears in the overall equation and an intermediate does not",
        "An intermediate appears in the overall equation and a catalyst does not",
        "A catalyst takes part in only one step and an intermediate in all of "
        "them",
        "There is no difference, since neither survives the reaction"],
      ans=0,
      why="EK 5.11.A.2 has the catalyst consumed in a step and regenerated "
          "afterwards while its net concentration stays constant, and EK 5.7.A.3 "
          "has the intermediate produced by some steps and consumed by others, "
          "so it exists only while the reaction runs."),

 dict(q="Why does a reaction path with a lower activation energy proceed faster "
        "at a given temperature?",
      choices=[
        "Because a larger proportion of collisions carries enough energy to "
        "reach the lower transition state",
        "Because the particles collide more often when the barrier is lower",
        "Because the products become more stable when the barrier is lower",
        "Because the reactants are at a higher energy on the new path",
        "Because a lower barrier means no collision is required at all"],
      ans=0,
      why="EK 5.11.A.1 offers the lower-activation-energy path as one route to a "
          "faster reaction, and EK 5.6.A.4 explains a rate through the "
          "proportion of collisions energetic enough to reach the transition "
          "state."),

 dict(q="Is a catalyst used up over the course of the reaction it catalyzes?",
      choices=[
        "No, because its net concentration is constant even though steps consume "
        "and regenerate it",
        "Yes, because it is consumed in the rate-determining step",
        "Yes, because it becomes part of one of the products",
        "No, because it never takes part in any elementary step",
        "It depends on whether the reaction releases energy"],
      ans=0,
      why="EK 5.11.A.2 states that the net concentration of the catalyst is "
          "constant, while also allowing that it is frequently consumed in the "
          "rate-determining step and regenerated in a subsequent step."),

 dict(q="Can the concentration of a catalyst appear in the rate law of a "
        "catalyzed reaction?",
      choices=[
        "Yes, because the catalyst is frequently consumed in the rate-determining "
        "step, whose molecularity sets the rate law",
        "No, because a catalyst is not used up overall",
        "No, because a rate law may contain only the reactants of the overall "
        "equation",
        "Yes, but only if the catalyst appears in the overall balanced equation",
        "Only if the catalyst is a solid"],
      ans=0,
      why="EK 5.11.A.2 has the catalyst frequently consumed in the "
          "rate-determining step, and EK 5.8.A.1 makes the rate law the "
          "molecularity of that step, so a particle colliding there carries a "
          "power whatever happens to it later."),

 dict(q="The framework offers a second route by which a catalyst may increase a "
        "rate, besides lowering the activation energy. What is it?",
      choices=[
        "Increasing the number of effective collisions",
        "Increasing the total number of particles present",
        "Increasing the energy released by the reaction",
        "Increasing the concentration of the products",
        "Increasing the number of elementary steps"],
      ans=0,
      why="EK 5.11.A.1 pairs the two with AND/OR: the addition of the catalyst "
          "must increase the number of effective collisions and/or provide a "
          "reaction path with a lower activation energy."),

 dict(q="Which statement about enzymes does the framework support?",
      choices=[
        "Many of them accelerate a reaction by binding to the reactants",
        "All of them accelerate a reaction by binding to the reactants",
        "None of them forms an intermediate with the reactants",
        "They increase the rate without changing the mechanism",
        "They are consumed permanently by the reactions they speed up"],
      ans=0,
      why="EK 5.11.A.3 says some catalysts accelerate a reaction by binding to "
          "the reactants, that there is often a new intermediate in which the "
          "catalyst is bound, and that MANY enzymes function in this manner. The "
          "hedge is the framework's own."),

 dict(q="How does the framework connect the effect of a catalyst to the reaction "
        "mechanism?",
      choices=[
        "The catalyst adds new elementary reactions and new intermediates, "
        "giving a different path between the same reactants and products",
        "The catalyst removes the slowest elementary step from the mechanism",
        "The catalyst changes the products the mechanism forms",
        "The catalyst leaves the mechanism unchanged and acts only on the "
        "temperature",
        "The catalyst makes the mechanism a single elementary step"],
      ans=0,
      why="EK 5.11.A.4 and EK 5.11.A.5 each say the catalyst introduces a new "
          "intermediate and new elementary reactions, and EK 5.11.A.1 makes the "
          "new path an alternative relative to the original reaction "
          "coordinate."),

 dict(q="A catalyst is consumed in the rate-determining step of a mechanism. "
        "What must happen later if it is to remain a catalyst?",
      choices=[
        "It must be regenerated in a subsequent step, so that its net "
        "concentration is unchanged",
        "It must be replaced by adding more of it as the reaction proceeds",
        "It must be converted into one of the products",
        "It must leave the reaction mixture as a gas",
        "Nothing further is required, since a catalyst may be consumed"],
      ans=0,
      why="EK 5.11.A.2 states both halves: the net concentration of the catalyst "
          "is constant, and it will frequently be consumed in the "
          "rate-determining step only to be regenerated in a subsequent step."),

 dict(q="Does adding a catalyst change the products a reaction forms?",
      choices=[
        "No, because it provides an alternative path relative to the original "
        "reaction coordinate, which runs between the same two ends",
        "Yes, because a new intermediate means a new product",
        "Yes, because the catalyst is incorporated into the products",
        "No, because a catalyst does not take part in any elementary step",
        "It depends on how much catalyst is added"],
      ans=0,
      why="EK 5.11.A.1 describes the catalyzed path as one with a lower "
          "activation energy RELATIVE TO THE ORIGINAL REACTION COORDINATE, that "
          "is an alternative route for the same reaction, and EK 5.11.A.2 leaves "
          "the catalyst's net concentration unchanged so it cancels out of the "
          "overall equation."),

 dict(q="Two paths for one reaction are available at the same temperature, one "
        "with an activation energy of 150 kJ/mol and one with 90 kJ/mol. Which "
        "carries the greater share of the reaction, and why?",
      choices=[
        "The 90 kJ/mol path, because a larger proportion of collisions can reach "
        "its transition state",
        "The 150 kJ/mol path, because more energy is available along it",
        "The two carry equal shares, because the reactants and products are the "
        "same",
        "Neither, because two paths cannot exist at once",
        "It cannot be judged without the overall energy change"],
      ans=0,
      why="EK 5.11.A.1 makes a lower activation energy a route to a faster "
          "reaction, and EK 5.6.A.4 ties the rate to the proportion of "
          "collisions energetic enough to reach the transition state, which is "
          "larger for the lower barrier."),

 dict(q="Why does the framework ask a student to explain a catalyst's effect "
        "through the mechanism rather than simply to state that it speeds the "
        "reaction up?",
      choices=[
        "Because each way a catalyst works is a change to the elementary steps: "
        "a new bound intermediate, a proton transferred, or a surface site "
        "occupied and freed",
        "Because a catalyst has no effect on the observed rate at all",
        "Because the mechanism determines the products the reaction forms",
        "Because the overall balanced equation cannot be written for a "
        "catalyzed reaction",
        "Because the rate of a catalyzed reaction cannot be measured"],
      ans=0,
      why="The learning objective for 5.11 asks for the relationship between the "
          "effect of a catalyst and CHANGES IN THE REACTION MECHANISM, and EK "
          "5.11.A.3, 5.11.A.4 and 5.11.A.5 each describe that effect as a new "
          "intermediate and new elementary reactions."),
]
