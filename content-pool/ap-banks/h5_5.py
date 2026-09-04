# AP CHEMISTRY 5.5 Collision Model
# CED effective Fall 2024, Unit 5 Kinetics.
# Learning objective 5.5.A: explain the relationship between the rate of an
# elementary reaction and the frequency, energy, and orientation of particle
# collisions. Suggested skill 6.E, provide reasoning to justify a claim using
# connections between particulate and macroscopic scales or levels.
#
# Essential knowledge relied on, in the framework's own words:
#   5.5.A.1  For an elementary reaction to successfully produce products,
#            reactants must successfully collide to initiate bond-breaking and
#            bond-making events.
#   5.5.A.2  In most reactions, only a small fraction of the collisions leads to
#            a reaction. Successful collisions have both sufficient energy to
#            overcome the activation energy requirements and orientations that
#            allow the bonds to rearrange in the required manner.
#   5.5.A.3  The Maxwell-Boltzmann distribution curve describes the distribution
#            of particle energies; this distribution can be used to gain a
#            qualitative estimate of the fraction of collisions with sufficient
#            energy to lead to a reaction, and also how that fraction depends on
#            temperature.
#
# THE THREE WORDS IN THE LEARNING OBJECTIVE ARE THE SPINE: frequency, energy and
# orientation. 5.5.A.1 supplies frequency (a collision has to happen at all),
# and 5.5.A.2 supplies the other two as the joint condition for a collision to
# succeed. Every item here sits on one of those three or on 5.5.A.3's
# distribution.
#
# WHERE THIS TOPIC STOPS. The reaction energy profile, the transition state and
# the Arrhenius equation are 5.6 -- and the CED excludes Arrhenius CALCULATIONS
# outright, so no item here computes anything from it or names it as a formula.
# How a catalyst changes the number of effective collisions is 5.11. Nothing
# here keys on either.
#
# NO CURVE, SO NO "AS THE GRAPH SHOWS". 5.5.A.3 is stated in terms of a curve
# and this bank cannot carry one, so every distribution item is a TABLE of the
# fraction of collisions above the energy requirement at stated temperatures,
# and the question is asked of that table. The framework itself calls the
# estimate QUALITATIVE, so no key here computes a fraction from a temperature.
#
# NOTATION. Chemistry is not typeset; this module needs almost no math, and what
# it needs is written in prose.
TOPIC = ("5.5", "Collision Model", 5)

_T_FRACTION = dict(
    headers=["Temperature (kelvins)",
             "Fraction of collisions with energy above the requirement"],
    rows=[["300", "0.0001"],
          ["350", "0.0012"],
          ["400", "0.0080"],
          ["450", "0.0330"]])

_T_COLLISIONS = dict(
    headers=["Collision", "Energy compared with the requirement",
             "Orientation of the colliding particles",
             "Did products form?"],
    rows=[["C1", "Above", "Allows the bonds to rearrange", "Yes"],
          ["C2", "Above", "Does not allow the bonds to rearrange", "No"],
          ["C3", "Below", "Allows the bonds to rearrange", "No"],
          ["C4", "Below", "Does not allow the bonds to rearrange", "No"]])

_T_COUNTS = dict(
    headers=["Sample", "Collisions per second in the vessel",
             "Fraction of those collisions that lead to products"],
    rows=[["Sample 1", "1.0 trillion", "0.000010"],
          ["Sample 2", "2.0 trillion", "0.000010"],
          ["Sample 3", "1.0 trillion", "0.000040"]])

_T_TWOTEMPS = dict(
    headers=["Property of the sample", "At 300 kelvins", "At 400 kelvins"],
    rows=[["Average kinetic energy of the particles", "Lower", "Higher"],
          ["Fraction of particles with very high energy", "Smaller", "Larger"],
          ["Total number of particles", "Same", "Same"]])

QUESTIONS = [

 dict(q="What must happen before an elementary reaction can produce products?",
      choices=[
        "The reactant particles must collide successfully so that bond-breaking "
        "and bond-making can begin",
        "The reactant particles must be separated from one another by the "
        "solvent",
        "The products must first be formed and then rearranged into reactants",
        "The temperature of the mixture must reach the boiling point of the "
        "reactants",
        "A catalyst must be present, since no collision leads to products "
        "without one"],
      ans=0,
      why="EK 5.5.A.1, near verbatim: for an elementary reaction to successfully "
          "produce products, reactants must successfully collide to initiate "
          "bond-breaking and bond-making events."),

 dict(q="According to the course framework, which two conditions must a "
        "successful collision meet?",
      choices=[
        "Sufficient energy to overcome the activation energy requirement, and an "
        "orientation that allows the bonds to rearrange",
        "Sufficient energy to overcome the activation energy requirement, and a "
        "sufficiently low temperature",
        "An orientation that allows the bonds to rearrange, and equal masses for "
        "the two particles",
        "A high concentration of both reactants, and the presence of a catalyst",
        "A collision between exactly three particles, and a low pressure in the "
        "vessel"],
      ans=0,
      why="EK 5.5.A.2, near verbatim: successful collisions have BOTH sufficient "
          "energy to overcome the activation energy requirements AND "
          "orientations that allow the bonds to rearrange in the required "
          "manner."),

 dict(q="What proportion of the collisions in a typical reaction mixture actually "
        "leads to a reaction?",
      choices=[
        "Only a small fraction of them",
        "All of them, since every collision transfers energy",
        "Exactly half of them, since half are correctly oriented",
        "None of them unless a catalyst is present",
        "All of those between particles of different substances"],
      ans=0,
      why="EK 5.5.A.2, near verbatim: in most reactions, only a small fraction "
          "of the collisions leads to a reaction, because a collision must meet "
          "both the energy and the orientation condition."),

 dict(q="What does the Maxwell-Boltzmann distribution curve describe?",
      choices=[
        "The distribution of particle energies in a sample",
        "The distribution of particle masses in a sample",
        "The number of products formed per unit of time",
        "The path a particle follows between collisions",
        "The proportion of a sample that has already reacted"],
      ans=0,
      why="EK 5.5.A.3, near verbatim: the Maxwell-Boltzmann distribution curve "
          "describes the distribution of particle energies, and can be used to "
          "estimate qualitatively the fraction of collisions with sufficient "
          "energy to lead to a reaction."),

 dict(q="The table gives the fraction of collisions carrying energy above the "
        "requirement at four temperatures. What does the trend show?",
      table=_T_FRACTION,
      choices=[
        "The fraction with sufficient energy grows as the temperature rises",
        "The fraction with sufficient energy shrinks as the temperature rises",
        "The fraction with sufficient energy is unaffected by temperature",
        "The fraction with sufficient energy reaches one at the highest "
        "temperature listed",
        "The fraction with sufficient energy is the same as the fraction with "
        "the correct orientation"],
      ans=0,
      why="EK 5.5.A.3 states that the distribution of particle energies can be "
          "used to estimate how the fraction of collisions with sufficient "
          "energy depends on temperature, and the tabulated fractions rise as "
          "the temperature does."),

 dict(q="The table records four collisions with the energy and the orientation of "
        "each. Which condition do the framework's two requirements together "
        "explain about these results?",
      table=_T_COLLISIONS,
      choices=[
        "Products formed only in the collision that met the energy requirement "
        "and the orientation requirement at the same time",
        "Products formed in every collision that met the energy requirement, "
        "whatever the orientation",
        "Products formed in every collision that met the orientation "
        "requirement, whatever the energy",
        "Products formed in every collision recorded, because a collision "
        "occurred in each case",
        "Products formed only in the collisions that met neither requirement"],
      ans=0,
      why="EK 5.5.A.2 requires BOTH sufficient energy and a suitable "
          "orientation, so a collision meeting one condition and failing the "
          "other produces nothing, which is what the tabulated outcomes show."),

 dict(q="Two molecules collide with far more than the energy the reaction "
        "requires, and yet no products are formed. What is the most likely "
        "explanation?",
      choices=[
        "The particles were oriented so that the bonds could not rearrange in "
        "the required manner",
        "The particles carried too much energy, which prevented a reaction",
        "The particles did not actually touch during the collision",
        "The reaction had already reached its maximum possible yield",
        "The collision occurred at too low a temperature for the energy to "
        "matter"],
      ans=0,
      why="EK 5.5.A.2 makes energy and orientation two separate conditions that "
          "must both be met. Excess energy does not repair an orientation that "
          "does not allow the bonds to rearrange in the required manner."),

 dict(q="Why does raising the concentration of a reactant raise the rate of an "
        "elementary reaction?",
      choices=[
        "More particles in the same volume make collisions between reactants "
        "more frequent",
        "More particles in the same volume give each collision more energy",
        "More particles in the same volume improve the orientation of each "
        "collision",
        "More particles in the same volume lower the energy the reaction "
        "requires",
        "More particles in the same volume raise the temperature of the sample"],
      ans=0,
      why="EK 5.5.A.1 makes a collision necessary before an elementary reaction "
          "can produce products, so anything that makes collisions more frequent "
          "gives more chances for one to succeed. EK 5.5.A.2's two conditions "
          "concern which collisions succeed, and neither is altered by crowding."),

 dict(q="The table gives the number of collisions per second and the fraction of "
        "them that lead to products for three samples. Which comparison isolates "
        "the effect of collision frequency alone?",
      table=_T_COUNTS,
      choices=[
        "The first and second samples, which share the same successful fraction "
        "but differ in collisions per second",
        "The first and third samples, which share the same collisions per second "
        "but differ in the successful fraction",
        "The second and third samples, which differ in both quantities at once",
        "All three samples together, because each records a different "
        "combination",
        "None of them, because collision frequency cannot be separated from the "
        "successful fraction"],
      ans=0,
      why="EK 5.5.A.1 makes collisions necessary and EK 5.5.A.2 makes only a "
          "small fraction of them successful, so the two quantities are "
          "independent. Isolating one requires a pair of samples in which the "
          "other is held fixed."),

 dict(q="Using the same table of collision counts, which comparison isolates the "
        "effect of the fraction of collisions that succeed?",
      table=_T_COUNTS,
      choices=[
        "The first and third samples, which share the same collisions per second",
        "The first and second samples, which share the same successful fraction",
        "The second and third samples, which share neither quantity",
        "Any pair, because the two quantities always change together",
        "No pair, because the successful fraction is the same in all three "
        "samples"],
      ans=0,
      why="EK 5.5.A.2 makes the successful fraction a separate quantity from the "
          "number of collisions, so the comparison that isolates it is the one "
          "in which the collision count is held fixed."),

 dict(q="How does the Maxwell-Boltzmann distribution change when a sample is "
        "warmed?",
      choices=[
        "A larger fraction of the particles carries high energy",
        "A larger fraction of the particles carries low energy",
        "The total number of particles increases",
        "Every particle ends up with exactly the same energy",
        "The distribution disappears, because all particles react"],
      ans=0,
      why="EK 5.5.A.3 states that the distribution describes particle energies "
          "and can be used to estimate how the fraction of collisions with "
          "sufficient energy depends on temperature. That fraction growing with "
          "temperature is a shift of the distribution toward higher energies."),

 dict(q="The table compares three properties of one sample at two temperatures. "
        "Which row explains why the reaction runs faster at the higher "
        "temperature?",
      table=_T_TWOTEMPS,
      choices=[
        "The row reporting a larger fraction of particles with very high energy "
        "at the higher temperature",
        "The row reporting the same total number of particles at both "
        "temperatures",
        "The row reporting a higher average kinetic energy, because an average "
        "alone determines whether each collision succeeds",
        "None of the rows, because temperature does not affect a reaction rate",
        "All three rows equally, because each differs between the two "
        "temperatures"],
      ans=0,
      why="EK 5.5.A.2 requires a collision to carry sufficient energy to "
          "overcome the activation energy requirement, and EK 5.5.A.3 makes the "
          "fraction of collisions meeting that requirement the quantity the "
          "distribution estimates."),

 dict(q="A student says that because the average energy of the particles is below "
        "what the reaction requires, no reaction can occur at all. What is wrong "
        "with this reasoning?",
      choices=[
        "The energies are distributed, so some particles carry far more than the "
        "average and their collisions can succeed",
        "The average energy of a sample is always above what a reaction requires",
        "Energy plays no part in whether a collision succeeds",
        "The reaction requires no energy at all if the orientation is correct",
        "The average energy of a sample cannot be measured, so the claim is "
        "untestable"],
      ans=0,
      why="EK 5.5.A.3 states that the Maxwell-Boltzmann curve describes the "
          "DISTRIBUTION of particle energies and is used to estimate the "
          "fraction with sufficient energy. A distribution has particles on both "
          "sides of its average."),

 dict(q="Which description matches what the framework calls a successful "
        "collision?",
      choices=[
        "One that initiates the bond-breaking and bond-making events leading to "
        "products",
        "One in which the two particles rebound without any change",
        "One in which the two particles stick together permanently without "
        "reacting",
        "One in which the particles exchange energy but not atoms",
        "One that occurs between particles of the same substance"],
      ans=0,
      why="EK 5.5.A.1 states that reactants must successfully collide to "
          "initiate bond-breaking and bond-making events for an elementary "
          "reaction to produce products, which is what makes a collision "
          "successful."),

 dict(q="Why does the framework describe the estimate obtained from the "
        "Maxwell-Boltzmann distribution as qualitative?",
      choices=[
        "Because the distribution shows how the fraction with sufficient energy "
        "compares between conditions rather than yielding a numerical rate",
        "Because the distribution applies only to samples that are not reacting",
        "Because particle energies cannot be measured at all",
        "Because the distribution changes shape unpredictably from moment to "
        "moment",
        "Because the fraction with sufficient energy is always exactly one half"],
      ans=0,
      why="EK 5.5.A.3 says the distribution can be used to gain a QUALITATIVE "
          "estimate of the fraction of collisions with sufficient energy and of "
          "how that fraction depends on temperature, which is a comparison "
          "rather than a computed value."),

 dict(q="Two reaction mixtures are prepared identically except that one is "
        "stirred vigorously and one is left still, and both are at the same "
        "temperature and concentration. Which statement about the fraction of "
        "collisions that succeed is best supported?",
      choices=[
        "It is essentially the same in both, because the energy and orientation "
        "conditions do not depend on stirring",
        "It is larger in the stirred mixture, because stirring adds energy to "
        "every collision",
        "It is smaller in the stirred mixture, because stirring disturbs the "
        "orientation of the particles",
        "It is zero in the still mixture, because particles must be stirred in "
        "order to collide",
        "It cannot be compared, because stirring changes the identity of the "
        "reactants"],
      ans=0,
      why="EK 5.5.A.2 makes the success of a collision depend on its energy "
          "relative to the requirement and on the orientation of the particles. "
          "Neither is set by whether the vessel is stirred, though stirring can "
          "bring reactants into contact in a heterogeneous mixture."),

 dict(q="Which of the following is NOT one of the three factors the learning "
        "objective connects to the rate of an elementary reaction?",
      choices=[
        "The mass of the products formed",
        "The frequency of particle collisions",
        "The energy of particle collisions",
        "The orientation of particle collisions",
        "None of them, because all four are named"],
      ans=0,
      why="Learning objective 5.5.A names the frequency, energy and orientation "
          "of particle collisions. The mass of product formed is an outcome of "
          "the reaction rather than a property of the collisions that produce it."),

 dict(q="At a fixed temperature, a reaction between two gases is carried out at "
        "two different pressures. Which quantity does the higher pressure change "
        "most directly?",
      choices=[
        "The frequency with which reactant particles collide",
        "The fraction of collisions with sufficient energy",
        "The fraction of collisions with a suitable orientation",
        "The energy the reaction requires in order to occur",
        "The identity of the products formed"],
      ans=0,
      why="EK 5.5.A.1 makes collisions necessary before products can form, and "
          "compressing a gas puts more particles in each unit of volume. EK "
          "5.5.A.2's two conditions are properties of an individual collision "
          "and are not changed by crowding at fixed temperature."),

 dict(q="Which statement about energy and orientation is consistent with the "
        "framework?",
      choices=[
        "Both must be satisfied in the same collision for products to form",
        "Either one on its own is enough for products to form",
        "Orientation matters only when the energy requirement is not met",
        "Energy matters only for collisions between particles of the same "
        "substance",
        "The two conditions are two names for the same requirement"],
      ans=0,
      why="EK 5.5.A.2 states that successful collisions have BOTH sufficient "
          "energy to overcome the activation energy requirements AND "
          "orientations that allow the bonds to rearrange in the required "
          "manner."),

 dict(q="Using the table of fractions above the energy requirement, by roughly "
        "what factor does that fraction change between the lowest and the "
        "highest temperature listed?",
      table=_T_FRACTION,
      choices=[
        "It grows by a factor of a few hundred",
        "It grows by a factor of about two",
        "It falls by a factor of a few hundred",
        "It is unchanged, since the temperatures differ by only 150 kelvins",
        "It grows by a factor of about ten thousand"],
      ans=0,
      why="EK 5.5.A.3 makes the temperature dependence of the fraction with "
          "sufficient energy something the distribution can be used to estimate, "
          "and the ratio of the largest to the smallest tabulated fraction "
          "measures how steep that dependence is over this range."),

 dict(q="A reaction between two large molecules is found to succeed in a far "
        "smaller fraction of its collisions than a reaction between two atoms at "
        "the same temperature. Which explanation is most consistent with the "
        "framework?",
      choices=[
        "Large molecules can meet in many ways, and few of those orientations "
        "allow the bonds to rearrange in the required manner",
        "Large molecules move too slowly for any of their collisions to carry "
        "sufficient energy",
        "Large molecules collide less often, which lowers the fraction that "
        "succeed",
        "Large molecules require no activation energy, so their collisions are "
        "not counted",
        "Large molecules always react on the first collision, so the fraction "
        "should be larger"],
      ans=0,
      why="EK 5.5.A.2 makes an orientation allowing the bonds to rearrange one "
          "of the two conditions for success. How often a collision meets that "
          "condition is a property of the particles, separate from how often "
          "they collide."),

 dict(q="What does the framework mean by sufficient energy in a collision?",
      choices=[
        "Enough energy to overcome the activation energy requirement of the "
        "reaction",
        "Enough energy to break every bond in both particles at once",
        "Enough energy to raise the temperature of the whole sample",
        "Enough energy to move the particles at the average speed of the sample",
        "Enough energy to keep the particles together permanently"],
      ans=0,
      why="EK 5.5.A.2 states that successful collisions have sufficient energy "
          "to overcome the activation energy requirements, so the standard the "
          "energy is compared against is that requirement and nothing else."),

 dict(q="Two samples of the same reaction mixture are held at 300 kelvins and 400 "
        "kelvins. Which pair of statements is correct?",
      choices=[
        "Collisions are both more frequent and more often energetic enough at "
        "the higher temperature",
        "Collisions are more frequent at the higher temperature but less often "
        "energetic enough",
        "Collisions are less frequent at the higher temperature but more often "
        "energetic enough",
        "Collisions are equally frequent at both temperatures and equally often "
        "energetic enough",
        "Collisions are more frequent at the higher temperature and the "
        "orientation requirement disappears"],
      ans=0,
      why="EK 5.5.A.3 makes the fraction of collisions with sufficient energy "
          "grow with temperature, and faster-moving particles meet more often, "
          "so both the frequency named in learning objective 5.5.A and that "
          "fraction move the same way."),

 dict(q="A student proposes that a reaction is slow because its particles hardly "
        "ever collide. Which observation would count against that proposal?",
      choices=[
        "The particles are calculated to collide many billions of times per "
        "second in the mixture",
        "The reaction produces very little product over an hour",
        "The reaction runs faster when the mixture is warmed",
        "The reaction involves two different substances",
        "The mixture contains a solvent as well as the reactants"],
      ans=0,
      why="EK 5.5.A.1 makes collisions necessary but EK 5.5.A.2 makes only a "
          "small fraction of them successful. A very large collision count with "
          "a slow reaction points at the energy or orientation conditions rather "
          "than at a shortage of collisions."),

 dict(q="Which change would raise the fraction of collisions that carry "
        "sufficient energy, without changing how often the particles collide "
        "very much?",
      choices=[
        "Warming the mixture while holding the amounts and the volume fixed",
        "Adding more of one reactant at the same temperature",
        "Pouring the mixture into a wider vessel at the same temperature",
        "Stirring the mixture more vigorously at the same temperature",
        "Waiting longer at the same temperature"],
      ans=0,
      why="EK 5.5.A.3 makes the fraction of collisions with sufficient energy "
          "depend on temperature, and it is the only listed change that alters "
          "the distribution of particle energies rather than the crowding of the "
          "particles."),

 dict(q="In a mixture at a single temperature, do all particles carry the same "
        "energy?",
      choices=[
        "No, the energies are distributed over a range, which is what the "
        "Maxwell-Boltzmann curve describes",
        "Yes, temperature fixes the energy of every particle exactly",
        "Yes, but only in a gas; in a liquid the energies differ",
        "No, but the differences are too small to affect any collision",
        "No, and the distribution is the same at every temperature"],
      ans=0,
      why="EK 5.5.A.3 states that the Maxwell-Boltzmann distribution curve "
          "describes the distribution of particle energies, and a distribution "
          "over a range is what makes a fraction with sufficient energy a "
          "meaningful quantity at all."),

 dict(q="Which statement best connects the particulate picture of collisions to "
        "the macroscopic rate of an elementary reaction?",
      choices=[
        "The rate reflects how often collisions occur multiplied by the fraction "
        "of them that meet both conditions for success",
        "The rate reflects only how often collisions occur, since every "
        "collision that happens leads to products",
        "The rate reflects only the fraction of successful collisions, since the "
        "number of collisions is fixed",
        "The rate reflects the total energy of the sample divided by the number "
        "of particles",
        "The rate reflects the number of products formed by each successful "
        "collision"],
      ans=0,
      why="EK 5.5.A.1 makes a collision necessary and EK 5.5.A.2 makes only a "
          "small fraction of collisions successful, so both the count and the "
          "fraction bear on how quickly products appear."),

 dict(q="A reaction between two gases is run at a fixed temperature in a vessel "
        "whose volume is then halved. What happens to the fraction of collisions "
        "that succeed?",
      choices=[
        "It stays essentially the same, because neither the energy distribution "
        "nor the orientation requirement has changed",
        "It doubles, because the particles are twice as crowded",
        "It halves, because the particles have less room to orient themselves",
        "It rises to one, because every collision must now succeed",
        "It falls to zero, because the particles can no longer move"],
      ans=0,
      why="EK 5.5.A.2 makes success depend on a collision's energy relative to "
          "the requirement and on its orientation, and EK 5.5.A.3 ties the "
          "energy distribution to temperature. Compressing at fixed temperature "
          "changes how often particles meet, not how often a meeting succeeds."),

 dict(q="Which sequence correctly describes what happens in a successful "
        "collision?",
      choices=[
        "The particles meet with enough energy and in a suitable orientation, "
        "and bond-breaking and bond-making then begin",
        "Bonds break first, and the particles then collide to form the new bonds",
        "The particles meet, then wait until the temperature rises, and only "
        "then react",
        "The products form first and the reactants are consumed afterward",
        "The particles exchange energy without touching, and products appear "
        "elsewhere in the vessel"],
      ans=0,
      why="EK 5.5.A.1 states that reactants must successfully collide TO "
          "INITIATE bond-breaking and bond-making events, and EK 5.5.A.2 gives "
          "the two conditions the collision must meet for that to happen."),

 dict(q="Why is the fraction of successful collisions a more useful quantity than "
        "the number of collisions when comparing two different reactions at the "
        "same temperature and concentration?",
      choices=[
        "Because the number of collisions is set mainly by crowding and speed, "
        "while the fraction reflects the energy and orientation each reaction "
        "requires",
        "Because the number of collisions cannot be estimated for any reaction",
        "Because the fraction of successful collisions is the same for every "
        "reaction",
        "Because the number of collisions does not affect the rate at all",
        "Because the fraction of successful collisions is always close to one"],
      ans=0,
      why="EK 5.5.A.2 attaches the two success conditions to the reaction itself "
          "through its activation energy requirement and the rearrangement its "
          "bonds need, while EK 5.5.A.1 makes the collision count a matter of "
          "the particles meeting at all."),
]
