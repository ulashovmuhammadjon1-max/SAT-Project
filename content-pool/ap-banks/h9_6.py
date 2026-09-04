# AP CHEMISTRY 9.6 Free Energy of Dissolution
# CED effective Fall 2024, Unit 9 Thermodynamics and Electrochemistry.
# Learning objective 9.6.A: explain the relationship between the solubility of a salt and
# changes in the enthalpy and entropy that occur in the dissolution process.
# Suggested skill 4.D, explain the degree to which a model or representation describes
# the connection between particulate-level properties and macroscopic properties.
#
# Essential knowledge relied on, in the framework's own words:
#   9.6.A.1  The free energy change for dissolution of a substance reflects a number of
#            factors: the breaking of the intermolecular interactions that hold the solid
#            together, the reorganization of the solvent around the dissolved species,
#            and the interaction of the dissolved species with the solvent. It is
#            possible to estimate the sign and relative magnitude of the enthalpic and
#            entropic contributions to each of these factors. However, making predictions
#            for the total change in free energy of dissolution can be challenging due to
#            the cancellations among the free energies associated with the three factors
#            cited.
#
# WHERE THE SIGNS OF THE SEPARATE CONTRIBUTIONS COME FROM, since EK 9.6.A.1 licenses
# estimating them but does not list them. Each is traced to a statement elsewhere in the
# framework rather than to memory:
#   EK 6.7.A.2  energy is REQUIRED to break bonds and RELEASED when bonds form, so
#               pulling the solid apart is an endothermic contribution and the new
#               attractions between the dissolved species and the solvent are exothermic.
#   EK 4.4.A.2  names the two halves for a salt specifically: dissolution "involves
#               breaking of ionic bonds, and the formation of ion-dipole interactions
#               between ions and solvent".
#   EK 9.1.A.1  entropy increases when matter becomes more dispersed, so breaking up the
#               ordered solid raises the entropy while holding solvent molecules in place
#               around a dissolved species lowers it.
#   EK 9.3.A.5  supplies the arithmetic wherever an enthalpy and an entropy change are
#               combined at a temperature.
#
# SCOPE. 7.11 and 7.12 own the solubility product and the common-ion effect, and no item
# here computes one; verify_h9_6.py asserts that. The point of this topic is the
# CANCELLATION -- three contributions of hundreds of kilojoules per mole summing to a few
# -- which is what makes the total hard to predict and is why the framework says so.
#
# NO FIGURES. Every stimulus is a table.
TOPIC = ("9.6", "Free Energy of Dissolution", 9)

_T_FACTORS = dict(
    headers=["Factor", "Contribution to the enthalpy change, kJ/mol",
             "Contribution to the free energy change, kJ/mol"],
    rows=[["Breaking the interactions that hold the solid together", "+780.0", "+765.0"],
          ["Reorganizing the solvent around the dissolved species", "-30.0", "-16.0"],
          ["Interaction of the dissolved species with the solvent", "-755.0", "-751.0"]])

_T_SALTS = dict(
    headers=["Salt", "Enthalpy change of dissolution, kJ/mol",
             "Entropy change of dissolution, J/(mol K)"],
    rows=[["Salt A", "+25.0", "+100.0"],
          ["Salt B", "-10.0", "-50.0"],
          ["Salt C", "+30.0", "-20.0"],
          ["Salt D", "-20.0", "+40.0"]])

QUESTIONS = [

 dict(q="Which three factors does the framework say the free energy change of dissolution "
        "reflects?",
      choices=[
        "Breaking the interactions holding the solid together, reorganizing the solvent "
        "around the dissolved species, and the interaction of the dissolved species with "
        "the solvent",
        "The mass of the solid, the volume of the solvent, and the temperature of the "
        "mixture",
        "The charge on the ions, the size of the ions, and the polarity of the solvent",
        "Breaking the solvent apart, breaking the solid apart, and heating the mixture",
        "The rate of dissolution, the extent of dissolution, and the temperature at which "
        "it occurs"],
      ans=0,
      why="EK 9.6.A.1 names exactly these three: the breaking of the intermolecular "
          "interactions that hold the solid together, the reorganization of the solvent "
          "around the dissolved species, and the interaction of the dissolved species "
          "with the solvent."),

 dict(q="What is the sign of the enthalpic contribution from breaking the interactions "
        "that hold the solid together?",
      choices=[
        "Positive, because energy is required to break the interactions",
        "Negative, because energy is released when the interactions break",
        "Positive, because the solid becomes more dispersed as it breaks up",
        "Negative, because the solid is more stable once it has dissolved",
        "Zero, because breaking interactions neither absorbs nor releases energy"],
      ans=0,
      why="EK 6.7.A.2 makes the energy required to break interactions an amount that has "
          "to be supplied, so this factor is endothermic, and EK 9.6.A.1 invites exactly "
          "this estimate of the sign. Dispersal of matter is an ENTROPIC effect, not an "
          "enthalpic one."),

 dict(q="What is the sign of the enthalpic contribution from the interaction of the "
        "dissolved species with the solvent?",
      choices=[
        "Negative, because energy is released as the new attractions form",
        "Positive, because energy must be supplied to bring the two together",
        "Negative, because the dissolved species becomes more dispersed",
        "Positive, because the solvent must be pushed aside first",
        "Zero, because the dissolved species and the solvent do not interact"],
      ans=0,
      why="EK 6.7.A.2 makes the forming of attractions a release of energy, and EK 4.4.A.2 "
          "names the ion-dipole interactions between ions and solvent that form when a "
          "salt dissolves. EK 9.6.A.1 invites the estimate. Dispersal is again an entropic "
          "matter."),

 dict(q="What is the sign of the entropic contribution from breaking the ordered solid "
        "apart into dissolved species?",
      choices=[
        "Positive, because the matter present becomes more dispersed",
        "Negative, because the matter present becomes more dispersed",
        "Positive, because energy must be supplied to break the solid apart",
        "Negative, because the solid is destroyed in the process",
        "Zero, because the same particles are present before and after"],
      ans=0,
      why="EK 9.1.A.1 makes entropy increase when matter becomes more dispersed, and "
          "particles locked into a solid lattice become free to move through the solution. "
          "The energy required to do it is the ENTHALPIC contribution of EK 6.7.A.2, a "
          "separate matter."),

 dict(q="What is the sign of the entropic contribution from reorganizing the solvent "
        "around the dissolved species?",
      choices=[
        "Negative, because solvent molecules become held in place around the species",
        "Positive, because solvent molecules become held in place around the species",
        "Negative, because energy is released as the solvent reorganizes",
        "Positive, because the solvent spreads out to accommodate the species",
        "Zero, because the solvent is present in the same amount throughout"],
      ans=0,
      why="EK 9.1.A.1 ties entropy to how dispersed the matter is, and solvent molecules "
          "arranged around a dissolved species are less free to move than they were, so "
          "this factor lowers the entropy. Whether energy is released is the enthalpic "
          "question, not the entropic one."),

 dict(q="What does the framework say it IS possible to estimate about the factors in a "
        "dissolution?",
      choices=[
        "The sign and relative magnitude of the enthalpic and entropic contributions to "
        "each factor",
        "The exact value of the free energy change of the whole process",
        "The temperature at which the solid will dissolve completely",
        "The mass of solid that will dissolve in a given volume of solvent",
        "The order in which the three factors occur"],
      ans=0,
      why="EK 9.6.A.1 says it is possible to estimate the sign and relative magnitude of "
          "the enthalpic and entropic contributions to each of the factors, and in the "
          "next sentence says the TOTAL is the challenging part."),

 dict(q="What does the framework say is challenging about the free energy of dissolution, "
        "and why?",
      choices=[
        "Predicting the total change, because of cancellations among the three factors",
        "Predicting the sign of each separate factor, because they are not measurable",
        "Predicting the temperature dependence, because entropy is not defined for "
        "solutions",
        "Predicting the enthalpy change, because bonds break and form at once",
        "Nothing is challenging, since the three factors can be added directly"],
      ans=0,
      why="EK 9.6.A.1 says that making predictions for the total change in free energy of "
          "dissolution can be challenging due to the cancellations among the free energies "
          "associated with the three factors cited, while the separate contributions can "
          "be estimated."),

 dict(q="Why do cancellations among the three factors make the total free energy change "
        "hard to predict?",
      choices=[
        "The total is a small difference between large contributions of opposite sign",
        "The three factors are all of the same sign, so they add to a very large number",
        "The three factors cannot be estimated separately at all",
        "The total depends on the order in which the three factors are considered",
        "The total is always exactly zero, so nothing can be said about it"],
      ans=0,
      why="EK 9.6.A.1 attributes the difficulty to cancellations among the free energies "
          "associated with the three factors: the contributions oppose one another, so the "
          "sum is much smaller than any of them and its sign turns on the balance rather "
          "than on any one factor."),

 dict(q="The table gives the contribution of each factor for the dissolution of one salt. "
        "What is the total free energy change of dissolution?",
      table=_T_FACTORS,
      choices=[
        "\\( -2.0 \\) kJ/mol, so the dissolution is thermodynamically favored",
        "\\( +2.0 \\) kJ/mol, so the dissolution is thermodynamically unfavored",
        "\\( +765.0 \\) kJ/mol, so the dissolution is thermodynamically unfavored",
        "\\( -767.0 \\) kJ/mol, so the dissolution is thermodynamically favored",
        "\\( +1532.0 \\) kJ/mol, so the dissolution is thermodynamically unfavored"],
      ans=0,
      why="EK 9.6.A.1 makes the free energy change of dissolution the combination of the "
          "three factors, so the tabulated contributions are added. EK 9.3.A.2 then reads "
          "a total below zero as thermodynamically favored. Taking one factor alone, or "
          "adding the sizes without their signs, gives the very large values offered."),

 dict(q="Using the same table, which factor makes the largest positive contribution to the "
        "free energy change?",
      table=_T_FACTORS,
      choices=[
        "Breaking the interactions that hold the solid together",
        "Reorganizing the solvent around the dissolved species",
        "Interaction of the dissolved species with the solvent",
        "The three contributions are equal in size",
        "No factor makes a positive contribution"],
      ans=0,
      why="EK 9.6.A.1 invites comparison of the relative magnitudes of the separate "
          "contributions, and exactly one tabulated contribution is above zero. It is the "
          "factor EK 6.7.A.2 makes endothermic, since energy has to be supplied to pull "
          "the solid apart."),

 dict(q="What does the comparison between the tabulated total and the tabulated individual "
        "contributions illustrate?",
      table=_T_FACTORS,
      choices=[
        "The total is far smaller than the separate contributions, because they largely "
        "cancel",
        "The total is larger than any separate contribution, because they add together",
        "The total equals the largest separate contribution, since the others are "
        "negligible",
        "The total is unrelated to the separate contributions",
        "The separate contributions are all small, so the total is small too"],
      ans=0,
      why="EK 9.6.A.1 names cancellations among the free energies associated with the "
          "three factors as the reason predictions are challenging, and the tabulated "
          "figures show it: contributions of hundreds of kilojoules per mole leaving a "
          "total of a few."),

 dict(q="Using the tabulated contributions, what is the total enthalpy change of the "
        "dissolution?",
      table=_T_FACTORS,
      choices=[
        "\\( -5.0 \\) kJ/mol, so the dissolution releases a little energy overall",
        "\\( +5.0 \\) kJ/mol, so the dissolution absorbs a little energy overall",
        "\\( +780.0 \\) kJ/mol, so the dissolution absorbs a great deal of energy",
        "\\( -785.0 \\) kJ/mol, so the dissolution releases a great deal of energy",
        "\\( +1565.0 \\) kJ/mol, so the dissolution absorbs a great deal of energy"],
      ans=0,
      why="EK 9.6.A.1 treats the enthalpic contributions of the three factors as separate "
          "amounts to be combined, so the tabulated enthalpy column is summed with its "
          "signs. EK 6.6.A.1 makes a negative enthalpy change a release of energy. The "
          "cancellation is as sharp here as in the free energy column."),

 dict(q="Is the dissolution described by the tabulated contributions thermodynamically "
        "favored, and by how much?",
      table=_T_FACTORS,
      choices=[
        "Yes, but only by a few kilojoules per mole out of contributions of hundreds",
        "Yes, by hundreds of kilojoules per mole",
        "No, it is unfavored by a few kilojoules per mole",
        "No, it is unfavored by hundreds of kilojoules per mole",
        "It cannot be decided, because the contributions are too large"],
      ans=0,
      why="Summing the tabulated free energy contributions gives a small negative total, "
          "which EK 9.3.A.2 reads as thermodynamically favored, and EK 9.6.A.1's warning "
          "about cancellation is exactly the observation that the margin is tiny beside "
          "the individual terms."),

 dict(q="The table gives the enthalpy and entropy changes for the dissolution of four "
        "salts. What is the free energy change of dissolution for salt A at 300 K?",
      table=_T_SALTS,
      choices=[
        "\\( -5.0 \\) kJ/mol, so the dissolution is thermodynamically favored",
        "\\( +5.0 \\) kJ/mol, so the dissolution is thermodynamically unfavored",
        "\\( +55.0 \\) kJ/mol, so the dissolution is thermodynamically unfavored",
        "\\( -75.0 \\) kJ/mol, so the dissolution is thermodynamically favored",
        "\\( +25.0 \\) kJ/mol, so the dissolution is thermodynamically unfavored"],
      ans=0,
      why="EK 9.3.A.5's equation subtracts the temperature times the entropy change from "
          "the enthalpy change, with the entropy change converted from joules to "
          "kilojoules. Learning objective 9.6.A asks for exactly this link between the two "
          "changes and whether the salt dissolves."),

 dict(q="Using the same table, what is the free energy change of dissolution for salt B at "
        "300 K?",
      table=_T_SALTS,
      choices=[
        "\\( +5.0 \\) kJ/mol, so the dissolution is thermodynamically unfavored",
        "\\( -5.0 \\) kJ/mol, so the dissolution is thermodynamically favored",
        "\\( -25.0 \\) kJ/mol, so the dissolution is thermodynamically favored",
        "\\( +40.0 \\) kJ/mol, so the dissolution is thermodynamically unfavored",
        "\\( -10.0 \\) kJ/mol, so the dissolution is thermodynamically favored"],
      ans=0,
      why="EK 9.3.A.5's equation subtracts a negative entropy term, which adds to the "
          "enthalpy change, so an exothermic dissolution can still come out unfavored when "
          "the entropy change opposes it. That is the balance learning objective 9.6.A "
          "asks the student to weigh."),

 dict(q="Which of the tabulated salts has a dissolution that is thermodynamically favored "
        "at every temperature?",
      table=_T_SALTS,
      choices=["Salt D", "Salt A", "Salt B", "Salt C", "Salts A and D together"],
      ans=0,
      why="EK 9.3.A.6's table places a negative enthalpy change with a positive entropy "
          "change in the row favored at all temperatures, and exactly one tabulated salt "
          "has that pair of signs. For it, no calculation is needed at all."),

 dict(q="One of the tabulated salts has a dissolution that no temperature will make "
        "thermodynamically favored. Which salt is it?",
      table=_T_SALTS,
      choices=["Salt C", "Salt A", "Salt B", "Salt D", "Salts B and C together"],
      ans=0,
      why="EK 9.3.A.6's table places a positive enthalpy change with a negative entropy "
          "change in the row favored at no temperature, and exactly one tabulated salt has "
          "that pair of signs. No amount of heating or cooling will make it dissolve "
          "favorably."),

 dict(q="Which tabulated salts have a dissolution that is thermodynamically favored at 300 "
        "K?",
      table=_T_SALTS,
      choices=["Salts A and D", "Salts B and C", "Salt D alone", "Salt A alone",
               "All four salts"],
      ans=0,
      why="EK 9.3.A.5's equation is applied to each tabulated pair of changes at the stated "
          "temperature, and EK 9.3.A.2 reads a result below zero as favored. Two of the "
          "four come out below zero, and one of those is endothermic."),

 dict(q="The dissolution of salt A absorbs energy and is still favored at 300 K. What "
        "accounts for that?",
      table=_T_SALTS,
      choices=[
        "Its positive entropy change, multiplied by the temperature, outweighs its "
        "enthalpy change",
        "Its enthalpy change is small enough to be ignored altogether",
        "Its entropy change is negative, which favors dissolution",
        "Absorbing energy always makes a process favored",
        "The temperature is too low for the enthalpy change to matter"],
      ans=0,
      why="EK 9.3.A.5's equation lets a positive entropy change, once multiplied by the "
          "temperature, exceed a positive enthalpy change and leave the difference below "
          "zero. EK 9.3.A.4 names the dissolution of a salt as exactly the kind of case "
          "where both must be weighed."),

 dict(q="Which dissolution does the framework name as an example of a process for which "
        "both enthalpy and entropy must be considered?",
      choices=[
        "The dissolution of sodium nitrate",
        "The dissolution of sodium chloride",
        "The dissolution of calcium carbonate",
        "The dissolution of ammonia in water",
        "The dissolution of carbon dioxide in water"],
      ans=0,
      why="EK 9.3.A.4 names the freezing of water and the dissolution of sodium nitrate as "
          "the examples of phenomena for which it is necessary to consider both enthalpy "
          "and entropy to determine whether a process will be thermodynamically favored."),

 dict(q="What relationship does the learning objective for this topic ask a student to "
        "explain?",
      choices=[
        "The relationship between the solubility of a salt and the enthalpy and entropy "
        "changes of dissolution",
        "The relationship between the solubility of a salt and the rate at which it "
        "dissolves",
        "The relationship between the solubility of a salt and the mass of solvent used",
        "The relationship between the enthalpy of dissolution and the temperature of the "
        "solvent",
        "The relationship between the size of the ions and the strength of the solvent"],
      ans=0,
      why="Learning objective 9.6.A asks for the relationship between the solubility of a "
          "salt and the changes in enthalpy and entropy that occur in the dissolution "
          "process, which is why EK 9.6.A.1 separates the enthalpic and entropic "
          "contributions of each factor."),

 dict(q="A salt whose dissolution has a positive enthalpy change and a positive entropy "
        "change becomes more soluble as the temperature rises. Which framework statement "
        "accounts for that?",
      choices=[
        "The temperature multiplies the entropy change, so the free energy change falls as "
        "the temperature rises",
        "The enthalpy change falls as the temperature rises, so dissolution becomes favored",
        "The entropy change reverses sign at high temperature",
        "A positive enthalpy change always makes a process favored",
        "Temperature does not appear in the free energy relationship at all"],
      ans=0,
      why="EK 9.3.A.5's equation multiplies the entropy change by the temperature before "
          "subtracting it, so with both changes positive a higher temperature lowers the "
          "free energy change, which EK 9.3.A.6 records as the favored-at-high-temperature "
          "case."),

 dict(q="Which of the three factors involves the formation of ion-dipole interactions "
        "between ions and solvent?",
      choices=[
        "The interaction of the dissolved species with the solvent",
        "The breaking of the interactions that hold the solid together",
        "The reorganization of the solvent around the dissolved species",
        "None of the three, since ion-dipole interactions are not part of dissolution",
        "All three equally, since ion-dipole interactions occur throughout"],
      ans=0,
      why="EK 4.4.A.2 says the dissolution of a salt in water involves breaking of ionic "
          "bonds and the formation of ion-dipole interactions between ions and solvent, "
          "and EK 9.6.A.1's third factor is precisely the interaction of the dissolved "
          "species with the solvent."),

 dict(q="Which of the three factors involves breaking the ionic bonds of the solid?",
      choices=[
        "The breaking of the interactions that hold the solid together",
        "The interaction of the dissolved species with the solvent",
        "The reorganization of the solvent around the dissolved species",
        "None of the three, since ionic bonds do not break during dissolution",
        "All three, since the solid is present throughout"],
      ans=0,
      why="EK 9.6.A.1's first factor is the breaking of the intermolecular interactions "
          "that hold the solid together, and EK 4.4.A.2 identifies those, for a salt, as "
          "the ionic bonds broken when it dissolves."),

 dict(q="A student predicts the free energy of dissolution from the lattice-breaking term "
        "alone. What is wrong with that approach?",
      choices=[
        "The other two factors are of comparable size and largely cancel the first",
        "The lattice-breaking term is always zero",
        "The lattice-breaking term is entropic rather than enthalpic",
        "Nothing is wrong, since the other factors are negligible",
        "The other two factors always have the same sign as the first"],
      ans=0,
      why="EK 9.6.A.1 lists three factors and attributes the difficulty of predicting the "
          "total to cancellations among the free energies associated with all three, so "
          "keeping only one of them discards most of what determines the answer."),

 dict(q="A student argues that a dissolution which absorbs energy cannot be "
        "thermodynamically favored. What is wrong with the argument?",
      choices=[
        "A sufficiently positive entropy change can outweigh a positive enthalpy change",
        "Nothing is wrong: an endothermic process is never favored",
        "The enthalpy change of dissolution is always negative in fact",
        "Favorability is decided by the rate of dissolution instead",
        "Absorbing energy makes the entropy change negative"],
      ans=0,
      why="EK 9.3.A.4 names the dissolution of sodium nitrate as a case where both "
          "enthalpy and entropy must be weighed, and EK 9.3.A.5's equation lets the "
          "temperature times a positive entropy change exceed a positive enthalpy change."),

 dict(q="Why can the sign of the total free energy change of dissolution be hard to "
        "predict even when the sign of every separate contribution is known?",
      choices=[
        "Because the contributions oppose one another and their relative sizes decide the "
        "outcome",
        "Because the signs of the contributions change as the solid dissolves",
        "Because only one of the three contributions can be estimated at a time",
        "Because the total is not the sum of the separate contributions",
        "Because the signs of the contributions are not really known"],
      ans=0,
      why="EK 9.6.A.1 says the separate signs and relative magnitudes can be estimated but "
          "that predicting the total is challenging due to cancellations, so knowing the "
          "signs alone leaves the outcome resting on magnitudes that nearly match."),

 dict(q="What kind of estimate does the framework say can be made for each factor in a "
        "dissolution?",
      choices=[
        "An estimate of the sign and the relative magnitude",
        "An exact value in kilojoules per mole",
        "An estimate of the sign only, never of the size",
        "An estimate of the size only, never of the sign",
        "An estimate of the temperature at which it vanishes"],
      ans=0,
      why="EK 9.6.A.1 states that it is possible to estimate the sign and relative "
          "magnitude of the enthalpic and entropic contributions to each of the factors, "
          "which is less than an exact value and more than a sign alone."),

 dict(q="How does the tabulated total free energy change compare in size with the largest "
        "single tabulated contribution?",
      table=_T_FACTORS,
      choices=[
        "The total is smaller by a factor of hundreds",
        "The total is larger, because the contributions add",
        "The total is about half the largest contribution",
        "The total is equal to the largest contribution",
        "The total is larger by a factor of about two"],
      ans=0,
      why="Summing the tabulated contributions leaves a total of a few kilojoules per mole "
          "against a largest single contribution of many hundreds, which is the "
          "cancellation EK 9.6.A.1 warns makes prediction of the total challenging."),

 dict(q="What general lesson does the framework's account of dissolution offer about a "
        "process made up of several contributions?",
      choices=[
        "A total made of large opposing contributions can be small and hard to predict",
        "A total is always dominated by its largest contribution",
        "A total can be found from the sign of any one contribution",
        "Contributions of opposite sign cannot occur in the same process",
        "A total is easier to predict than any of its contributions"],
      ans=0,
      why="EK 9.6.A.1 makes exactly this point about dissolution: the separate "
          "contributions can be estimated, yet the total is challenging to predict because "
          "of cancellations among them, so the sum is a small residue of much larger "
          "opposing terms."),

]
