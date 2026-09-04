# AP CHEMISTRY 6.5 Energy of Phase Changes
# CED effective Fall 2024, Unit 6 Thermochemistry.
# Learning objective 6.5.A: explain changes in the heat q absorbed or released by a system
# undergoing a phase transition based on the amount of the substance in moles and the molar
# enthalpy of the phase transition. Suggested skill 1.B, describe the components of and
# quantitative information from models and representations that illustrate both
# particulate-level and macroscopic-level properties.
#
# Essential knowledge relied on, in the framework's own words:
#   6.5.A.1  Energy must be transferred to a system to cause a substance to melt (or boil).
#            The energy of the system therefore increases as the system undergoes a
#            solid-to-liquid (or liquid-to-gas) phase transition. Likewise, a system
#            releases energy when it freezes (or condenses). The energy of the system
#            decreases as the system undergoes a liquid-to-solid (or gas-to-liquid) phase
#            transition. The temperature of a pure substance remains constant during a
#            phase change.
#   6.5.A.2  The energy absorbed during a phase change is equal to the energy released
#            during a complementary phase change in the opposite direction. For example,
#            the molar enthalpy of condensation of a substance is equal to the negative of
#            its molar enthalpy of vaporization. Similarly, the molar enthalpy of fusion
#            can be used to calculate the energy absorbed when melting a substance and the
#            energy released when freezing a substance.
#
# THE ARITHMETIC THE LEARNING OBJECTIVE ASKS FOR is the amount in moles times the molar
# enthalpy of the transition, and every quantitative item below is exactly that, in one
# step, with the numbers chosen so no calculator is needed. verify_h6_5.py recomputes each
# one from the stimulus alone.
#
# THE TWO SIGNS THAT DECIDE EVERY ANSWER HERE, and the two ways to get them backwards:
#
#   the DIRECTION of the transition   melting and boiling take energy IN and raise the
#                                     energy of the system; freezing and condensing give
#                                     energy OUT and lower it. EK 6.5.A.1 states all four
#                                     clauses, and every keyed choice that reports an
#                                     amount of energy says which way it went as well as
#                                     how much.
#   the COMPLEMENT of a transition    EK 6.5.A.2 makes the molar enthalpy of condensation
#                                     the NEGATIVE of the molar enthalpy of vaporization,
#                                     not a second, independent number and not the same
#                                     number. Item 8 and item 19 are built on that, and
#                                     the keys say "the negative of" rather than leaving a
#                                     bare magnitude to be read either way.
#
# THE CONSTANT TEMPERATURE IS THE OTHER HALF OF EK 6.5.A.1 AND IS EASILY LOST. Energy goes
# in while the thermometer stands still, which is not a contradiction and is the point of
# items 5, 6, 20 and 21. verify_h6_5.py asserts that each of those keys states the
# constancy and that none of them has the temperature rising or falling during the change.
#
# SCOPE. 6.4 owns q = mc(delta T), the specific heat capacity and the calorimeter, and NO
# item here warms a substance without changing its state. 6.6 owns the molar enthalpy of
# REACTION and 6.8 the standard enthalpies of formation, so nothing here is a chemical
# change. 6.1 owns the observation-to-energy link and already carries the single item
# making the logical point that a constant temperature does not mean no transfer; this
# module does not repeat it, and asks instead where the energy goes and what a heating
# experiment shows.
#
# NOTATION. export_units.py does not typeset Chemistry. Molar enthalpies are written in
# plain text as "40.7 kJ/mol", and a negative value is written in words as "the negative
# of", never as a bare minus sign that could be read as a dash.
TOPIC = ("6.5", "Energy of Phase Changes", 6)

_T_PHASE = dict(
    headers=["Substance", "Molar enthalpy of fusion (kJ/mol)",
             "Molar enthalpy of vaporization (kJ/mol)"],
    rows=[["Water", "6.01", "40.7"],
          ["Ethanol", "4.93", "38.6"],
          ["Ammonia", "5.65", "23.4"],
          ["Methane", "0.94", "8.17"],
          ["Mercury", "2.29", "59.1"]])

QUESTIONS = [

 dict(q="What does the framework say must happen for a substance to melt or to boil?",
      choices=[
        "Energy must be transferred to the system",
        "Energy must be transferred from the system",
        "The pressure on the system must be raised",
        "The system must be brought into contact with a second substance",
        "The mass of the system must be increased"],
      ans=0,
      why="EK 6.5.A.1 opens by stating that energy must be transferred to a system to cause "
          "a substance to melt or boil, which is why both transitions are ones the system "
          "cannot make on its own."),

 dict(q="What happens to the energy of a system as it undergoes a solid-to-liquid phase "
        "transition?",
      choices=[
        "It increases",
        "It decreases",
        "It stays the same, since the temperature does",
        "It first increases and then decreases",
        "It depends on which substance is melting"],
      ans=0,
      why="EK 6.5.A.1 states that the energy of the system therefore increases as the "
          "system undergoes a solid-to-liquid phase transition, since energy has to be "
          "transferred in for the melting to occur."),

 dict(q="What does the framework say a system does when it freezes or condenses?",
      choices=[
        "It releases energy",
        "It absorbs energy",
        "It neither releases nor absorbs energy",
        "It releases energy only if it is cooled below its freezing point",
        "It absorbs energy from the substance around it"],
      ans=0,
      why="EK 6.5.A.1 states that a system releases energy when it freezes or condenses, "
          "which is the mirror of the transfer into the system that melting and boiling "
          "require."),

 dict(q="What happens to the energy of a system as it undergoes a gas-to-liquid phase "
        "transition?",
      choices=[
        "It decreases",
        "It increases",
        "It stays the same, since the temperature does",
        "It first decreases and then increases",
        "It depends on how quickly the change occurs"],
      ans=0,
      why="EK 6.5.A.1 states that the energy of the system decreases as the system "
          "undergoes a liquid-to-solid or gas-to-liquid phase transition, because the "
          "system has released energy."),

 dict(q="What does the framework say about the temperature of a pure substance while it is "
        "changing state?",
      choices=[
        "It remains constant",
        "It rises steadily",
        "It falls steadily",
        "It rises while the substance melts and falls while it freezes",
        "It changes at a rate set by the molar enthalpy of the transition"],
      ans=0,
      why="EK 6.5.A.1 closes by stating that the temperature of a pure substance remains "
          "constant during a phase change, even though energy is being transferred "
          "throughout."),

 dict(q="Energy is transferred steadily into a pure solid that is melting at its melting "
        "point. Where is that energy going, if not into raising the temperature?",
      choices=[
        "Into the phase change itself, which increases the energy of the system without "
        "changing its temperature",
        "Into the surroundings, which is why the temperature of the sample holds still",
        "Nowhere, since a melting substance absorbs no energy",
        "Into raising the pressure of the sample instead",
        "Into increasing the mass of the liquid formed"],
      ans=0,
      why="EK 6.5.A.1 states both halves in one statement: energy must be transferred to "
          "the system for it to melt, and the energy of the system therefore increases, "
          "while the temperature of a pure substance remains constant during the change."),

 dict(q="How does the energy absorbed during a phase change compare with the energy "
        "released during the complementary change in the opposite direction?",
      choices=[
        "They are equal",
        "The energy released is always the larger",
        "The energy absorbed is always the larger",
        "They are unrelated quantities",
        "The energy released is always half of the energy absorbed"],
      ans=0,
      why="EK 6.5.A.2 states that the energy absorbed during a phase change is equal to the "
          "energy released during a complementary phase change in the opposite direction."),

 dict(q="How is the molar enthalpy of condensation of a substance related to its molar "
        "enthalpy of vaporization?",
      choices=[
        "It is the negative of the molar enthalpy of vaporization",
        "It is the same as the molar enthalpy of vaporization",
        "It is the negative of the molar enthalpy of fusion",
        "It is the sum of the molar enthalpies of fusion and vaporization",
        "It is a separate quantity with no fixed relation to the others"],
      ans=0,
      why="EK 6.5.A.2 gives this as its own example: the molar enthalpy of condensation of "
          "a substance is equal to the negative of its molar enthalpy of vaporization, "
          "which is what makes the two transitions complementary."),

 dict(q="For which two calculations does the framework say the molar enthalpy of fusion "
        "can be used?",
      choices=[
        "The energy absorbed when melting a substance and the energy released when "
        "freezing it",
        "The energy absorbed when melting a substance and the energy absorbed when boiling "
        "it",
        "The energy released when freezing a substance and the energy released when "
        "condensing it",
        "The energy absorbed when boiling a substance and the energy released when "
        "condensing it",
        "The energy needed to raise the temperature of a solid and of a liquid"],
      ans=0,
      why="EK 6.5.A.2 states that the molar enthalpy of fusion can be used to calculate the "
          "energy absorbed when melting a substance and the energy released when freezing a "
          "substance, which is its complementary rule applied to one pair."),

 dict(q="On which two quantities does the learning objective say the heat absorbed or "
        "released in a phase transition depends?",
      choices=[
        "The amount of the substance in moles and the molar enthalpy of the transition",
        "The mass of the substance and its specific heat capacity",
        "The temperature of the substance and the time taken",
        "The amount of the substance in moles and the temperature change",
        "The molar enthalpy of the transition and the pressure"],
      ans=0,
      why="Learning objective 6.5.A names exactly these two, the amount of the substance in "
          "moles and the molar enthalpy of the phase transition, which multiply to give the "
          "heat q for the change."),

 dict(q="The molar enthalpy of vaporization of a substance is 40.7 kJ/mol. How much energy "
        "is involved when 3.00 mol of the liquid is completely vaporized?",
      choices=[
        "122.1 kJ absorbed",
        "122.1 kJ released",
        "40.7 kJ absorbed",
        "13.6 kJ absorbed",
        "43.7 kJ absorbed"],
      ans=0,
      why="Learning objective 6.5.A multiplies the amount in moles by the molar enthalpy of "
          "the transition, and EK 6.5.A.1 has energy transferred INTO a system that is "
          "boiling, so the sample takes the energy in."),

 dict(q="The molar enthalpy of vaporization of a substance is 44.0 kJ/mol. How much energy "
        "is involved when 0.250 mol of its vapour condenses?",
      choices=[
        "11.0 kJ released",
        "11.0 kJ absorbed",
        "44.0 kJ released",
        "176 kJ released",
        "0.250 kJ released"],
      ans=0,
      why="EK 6.5.A.2 makes the molar enthalpy of condensation the negative of the molar "
          "enthalpy of vaporization, and EK 6.5.A.1 has a condensing system release energy, "
          "so the amount in moles times that value is given out."),

 dict(q="The molar enthalpy of fusion of a substance is 6.01 kJ/mol. If 24.04 kJ are "
        "absorbed and the sample melts completely, how much of the substance was there?",
      choices=[
        "4.00 mol",
        "0.250 mol",
        "144 mol",
        "18.0 mol",
        "6.01 mol"],
      ans=0,
      why="Learning objective 6.5.A makes the heat the amount in moles times the molar "
          "enthalpy of the transition, so dividing the energy absorbed by the molar "
          "enthalpy of fusion returns the amount that melted."),

 dict(q="The molar enthalpies of fusion and of vaporization of five substances have been "
        "measured. For which substance does vaporizing one mole take the most energy?",
      table=_T_PHASE,
      choices=[
        "Mercury",
        "Water",
        "Ethanol",
        "Ammonia",
        "Methane"],
      ans=0,
      why="Learning objective 6.5.A makes the energy for one mole the molar enthalpy of the "
          "transition itself, and EK 6.5.A.1 has boiling take energy in, so the largest "
          "tabulated enthalpy of vaporization is the answer."),

 dict(q="Among those same five substances, for which does melting one mole take the least "
        "energy?",
      table=_T_PHASE,
      choices=[
        "Methane",
        "Mercury",
        "Ethanol",
        "Ammonia",
        "Water"],
      ans=0,
      why="The energy for one mole is the molar enthalpy of the transition, so the smallest "
          "tabulated enthalpy of fusion marks the substance that melts on the least energy "
          "per mole."),

 dict(q="For which of those five substances is the molar enthalpy of vaporization the "
        "smallest multiple of the molar enthalpy of fusion?",
      table=_T_PHASE,
      choices=[
        "Ammonia",
        "Water",
        "Ethanol",
        "Methane",
        "Mercury"],
      ans=0,
      why="Dividing each tabulated enthalpy of vaporization by the same substance's "
          "enthalpy of fusion compares the two transitions within one substance, and the "
          "smallest of those five ratios is the answer."),

 dict(q="How much energy is involved when 2.00 mol of water freezes completely?",
      table=_T_PHASE,
      choices=[
        "12.02 kJ released",
        "12.02 kJ absorbed",
        "81.4 kJ released",
        "6.01 kJ released",
        "3.01 kJ released"],
      ans=0,
      why="EK 6.5.A.2 lets the molar enthalpy of fusion give the energy released when "
          "freezing, and EK 6.5.A.1 has a freezing system release energy, so the amount in "
          "moles times the tabulated enthalpy of fusion is given out."),

 dict(q="How much energy is involved when 0.500 mol of ethanol is completely vaporized?",
      table=_T_PHASE,
      choices=[
        "19.3 kJ absorbed",
        "19.3 kJ released",
        "38.6 kJ absorbed",
        "2.47 kJ absorbed",
        "77.2 kJ absorbed"],
      ans=0,
      why="Learning objective 6.5.A multiplies the amount in moles by the tabulated molar "
          "enthalpy of vaporization, and EK 6.5.A.1 has a boiling system take energy in."),

 dict(q="What is the molar enthalpy of condensation of ammonia?",
      table=_T_PHASE,
      choices=[
        "The negative of 23.4 kJ/mol",
        "The same as 23.4 kJ/mol",
        "The negative of 5.65 kJ/mol",
        "The negative of 29.05 kJ/mol",
        "Zero, because the energy absorbed on vaporizing is returned on condensing"],
      ans=0,
      why="EK 6.5.A.2 states that the molar enthalpy of condensation of a substance is "
          "equal to the negative of its molar enthalpy of vaporization, which for this "
          "substance is the tabulated value for vaporization with its sign reversed."),

 dict(q="A steady heater warms a sample of a pure substance from solid, through liquid, to "
        "gas. During which stages does the thermometer reading hold still?",
      choices=[
        "While the sample melts and while it boils, since the temperature of a pure "
        "substance remains constant during a phase change",
        "While the solid warms and while the liquid warms, since a substance takes up "
        "energy only when changing state",
        "At no stage, since energy is being supplied throughout",
        "Only while the sample melts, since boiling always raises the temperature",
        "Only while the sample boils, since melting always raises the temperature"],
      ans=0,
      why="EK 6.5.A.1 states that the temperature of a pure substance remains constant "
          "during a phase change, so the two stages at which the sample is changing state "
          "are the two at which the reading does not move."),

 dict(q="A pure substance is melting, and the framework says its temperature stays where it "
        "is. Does its energy stay where it is too?",
      choices=[
        "No; the temperature remains constant but the energy of the system increases, "
        "because energy must be transferred in for it to melt",
        "Yes; a constant temperature means a constant energy",
        "No; the temperature remains constant but the energy of the system decreases",
        "Yes, but only while some solid is still present",
        "It cannot be decided without knowing the molar enthalpy of fusion"],
      ans=0,
      why="EK 6.5.A.1 states both things about the same interval: energy must be "
          "transferred to the system for it to melt, so the energy of the system increases, "
          "and the temperature of a pure substance remains constant during the change."),

 dict(q="What is the sign of the molar enthalpy of fusion of a substance, and why?",
      choices=[
        "Positive, because energy must be transferred to the system for it to melt",
        "Negative, because energy must be transferred to the system for it to melt",
        "Positive, because the system releases energy as it melts",
        "Negative, because the system releases energy as it melts",
        "It has no sign, because a molar enthalpy is a magnitude only"],
      ans=0,
      why="EK 6.5.A.1 has energy transferred INTO a melting system, so its energy "
          "increases, and EK 6.5.A.2's example makes the complementary transition the "
          "negative one, which leaves melting as the positive member of the pair."),

 dict(q="What is the sign of the molar enthalpy of freezing of a substance, and why?",
      choices=[
        "Negative, because the system releases energy as it freezes",
        "Positive, because the system releases energy as it freezes",
        "Negative, because energy must be transferred to the system for it to freeze",
        "Positive, because energy must be transferred to the system for it to freeze",
        "It has no sign, because freezing and melting are the same process"],
      ans=0,
      why="EK 6.5.A.1 states that a system releases energy when it freezes and that its "
          "energy decreases, and EK 6.5.A.2 makes the freezing value the negative of the "
          "melting one."),

 dict(q="A student calculates the energy needed to melt a sample by multiplying the amount "
        "in moles by the substance's molar enthalpy of vaporization. What is wrong?",
      choices=[
        "The molar enthalpy of fusion is the one that belongs to melting",
        "The amount should have been taken in grams rather than in moles",
        "The two enthalpies should have been added together instead",
        "Nothing, since the two molar enthalpies of a substance are equal",
        "The result should have been divided by the molar enthalpy of fusion"],
      ans=0,
      why="EK 6.5.A.2 attaches the molar enthalpy of fusion to melting and freezing and the "
          "molar enthalpy of vaporization to boiling and condensing, and learning objective "
          "6.5.A pairs the amount in moles with the enthalpy OF THE TRANSITION taking "
          "place."),

 dict(q="Why can one molar enthalpy of fusion serve for both melting and freezing?",
      choices=[
        "Because the energy absorbed in a phase change equals the energy released in the "
        "complementary change in the opposite direction",
        "Because melting and freezing transfer energy in the same direction",
        "Because the temperature is constant during both changes",
        "Because a molar enthalpy does not depend on which substance is involved",
        "Because freezing is not a phase change at all"],
      ans=0,
      why="EK 6.5.A.2 states that the energy absorbed during a phase change is equal to the "
          "energy released during the complementary phase change in the opposite direction, "
          "and names the fusion pair as its second example."),

 dict(q="A 0.500 mol sample of a substance releases 20.4 kJ as it freezes completely. What "
        "is the substance's molar enthalpy of fusion?",
      choices=[
        "40.8 kJ/mol",
        "10.2 kJ/mol",
        "20.4 kJ/mol",
        "0.0245 kJ/mol",
        "20.9 kJ/mol"],
      ans=0,
      why="EK 6.5.A.2 makes the energy released on freezing equal to the energy absorbed on "
          "melting the same amount, so dividing the energy by the amount in moles returns "
          "the molar enthalpy of fusion."),

 dict(q="Which pair of phase transitions absorbs energy?",
      choices=[
        "Melting and vaporizing",
        "Freezing and condensing",
        "Melting and condensing",
        "Freezing and vaporizing",
        "Neither pair, since a phase change transfers no energy"],
      ans=0,
      why="EK 6.5.A.1 states that energy must be transferred to a system to cause a "
          "substance to melt or boil, and that the system RELEASES energy when it freezes "
          "or condenses, which separates the four transitions into two pairs."),

 dict(q="A 1.00 mol sample and a 3.00 mol sample of the same substance are each completely "
        "vaporized. How do the energies absorbed compare?",
      choices=[
        "The larger sample absorbs three times as much, since the heat is the amount in "
        "moles times the molar enthalpy",
        "The two absorb the same, since the molar enthalpy is a property of the substance",
        "The larger sample absorbs three times as much, since its molar enthalpy is three "
        "times as large",
        "The larger sample absorbs nine times as much",
        "The smaller sample absorbs the more, since it vaporizes sooner"],
      ans=0,
      why="Learning objective 6.5.A makes the heat the amount in moles times the molar "
          "enthalpy of the transition, so tripling the amount triples the heat while the "
          "molar enthalpy, a property of the substance, does not change."),

 dict(q="Sample 1 is 2.00 mol of a substance whose molar enthalpy of vaporization is 30.0 "
        "kJ/mol. Sample 2 is 3.00 mol of a substance whose molar enthalpy of vaporization "
        "is 20.0 kJ/mol. Which sample absorbs more energy on being completely vaporized?",
      choices=[
        "Neither; each absorbs 60.0 kJ",
        "Sample 1, because its molar enthalpy of vaporization is the larger",
        "Sample 2, because it contains the greater amount in moles",
        "Sample 1, because it absorbs 90.0 kJ against sample 2's 40.0 kJ",
        "It cannot be decided without knowing the masses of the two samples"],
      ans=0,
      why="Learning objective 6.5.A makes the heat the product of the amount in moles and "
          "the molar enthalpy of the transition, and the two products are the same here, so "
          "neither the larger amount nor the larger enthalpy settles it on its own."),

 dict(q="The molar enthalpy of vaporization of a substance is 25.0 kJ/mol. How much energy "
        "is involved when 2.00 mol of its vapour condenses completely?",
      choices=[
        "50.0 kJ released",
        "50.0 kJ absorbed",
        "25.0 kJ released",
        "12.5 kJ released",
        "27.0 kJ released"],
      ans=0,
      why="EK 6.5.A.2 makes the molar enthalpy of condensation the negative of the molar "
          "enthalpy of vaporization, and EK 6.5.A.1 has a condensing system release energy, "
          "so the amount in moles times that value leaves the system."),
]
