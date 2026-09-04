# AP CHEMISTRY 9.1 Introduction to Entropy
# CED effective Fall 2024, Unit 9 Thermodynamics and Electrochemistry.
# Learning objective 9.1.A: identify the sign and relative magnitude of the entropy
# change associated with chemical or physical processes.
# Suggested skill 6.C, support a claim with evidence from representations or models at
# the particulate level.
#
# Essential knowledge relied on, in the framework's own words:
#   9.1.A.1  Entropy increases when matter becomes more dispersed. For example, the
#            phase change from solid to liquid or from liquid to gas results in a
#            dispersal of matter as the individual particles become freer to move and
#            generally occupy a larger volume. Similarly, for a gas, the entropy
#            increases when there is an increase in volume (at constant temperature),
#            and the gas molecules are able to move within a larger space. For reactions
#            involving gas-phase reactants or products, the entropy generally increases
#            when the total number of moles of gas-phase products is greater than the
#            total number of moles of gas-phase reactants.
#   9.1.A.2  Entropy increases when energy is dispersed. According to kinetic molecular
#            theory (KMT), the distribution of kinetic energy among the particles of a
#            gas broadens as the temperature increases. As a result, the entropy of the
#            system increases with an increase in temperature.
#
# SCOPE. This topic identifies the SIGN and the relative magnitude only. The arithmetic
# of absolute entropies belongs to 9.2 and every energy quantity belongs to 9.3 and
# beyond, so no item here states a value in J/(mol K) or in kJ/mol -- verify_h9_1.py
# asserts that, because a topic that quietly does the next topic's arithmetic is not
# the topic the student selected.
#
# ARITHMETIC. Every gas-mole claim is recomputed in verify_h9_1.py by parsing the
# equation out of the stem itself and counting the moles of gas on each side. A key
# that says "positive" over an equation whose gas moles fall is rejected there.
#
# NO FIGURES. This bank cannot carry images; nothing below refers to one.
#
# NOTATION. export_units.py does not typeset Chemistry. This topic needs no math spans.
TOPIC = ("9.1", "Introduction to Entropy", 9)

_T_GASMOLES = dict(
    headers=["Reaction", "Total moles of gas-phase reactants",
             "Total moles of gas-phase products"],
    rows=[["W", "2", "4"],
          ["X", "3", "2"],
          ["Y", "1", "1"],
          ["Z", "4", "7"]])

_T_PHASES = dict(
    headers=["Process", "State before", "State after"],
    rows=[["1", "solid", "liquid"],
          ["2", "gas", "liquid"],
          ["3", "liquid", "gas"],
          ["4", "gas", "solid"]])

QUESTIONS = [

 dict(q="Which change does the course framework associate with an increase in entropy?",
      choices=[
        "Matter becoming more dispersed, as when particles become freer to move",
        "Matter becoming more concentrated into a smaller region of space",
        "Energy becoming confined to a smaller number of particles",
        "A fall in the number of particles that are free to move about",
        "A fall in the temperature of a sample of gas"],
      ans=0,
      why="EK 9.1.A.1 opens by stating that entropy increases when matter becomes more "
          "dispersed, and gives the phase change from solid to liquid or from liquid to "
          "gas as the example, because the individual particles become freer to move. "
          "Concentrating matter or confining energy is the reverse of both statements."),

 dict(q="A sample of ice melts to liquid water at constant pressure. What is the sign of "
        "the entropy change of the water, and why?",
      choices=[
        "Positive, because the particles become freer to move and generally occupy a "
        "larger volume",
        "Negative, because the sample absorbs energy from its surroundings as it melts",
        "Negative, because liquid water is denser than the ice it came from",
        "Zero, because the chemical identity of the substance does not change",
        "Positive, because the temperature of the sample rises while it is melting"],
      ans=0,
      why="EK 9.1.A.1 names the phase change from solid to liquid as a dispersal of "
          "matter in which the individual particles become freer to move and generally "
          "occupy a larger volume. Absorbing energy is not the framework's criterion, and "
          "the temperature of a pure substance does not rise while it melts."),

 dict(q="Steam condenses to liquid water at constant temperature. What is the sign of the "
        "entropy change of the water?",
      choices=[
        "Negative, because the matter present becomes less dispersed",
        "Positive, because energy is released to the surroundings during condensation",
        "Positive, because a given mass of liquid contains more molecules than the gas",
        "Zero, because condensation is a physical change rather than a chemical one",
        "Negative, because the number of water molecules falls as the steam condenses"],
      ans=0,
      why="EK 9.1.A.1 makes entropy increase when matter becomes more dispersed, so the "
          "reverse change, in which a gas collapses into a liquid of far smaller volume, "
          "lowers the entropy. The number of water molecules is unchanged by a phase "
          "change."),

 dict(q="A fixed amount of gas expands into a larger container while the temperature is "
        "held constant. What happens to the entropy of the gas?",
      choices=[
        "It increases, because the gas molecules are able to move within a larger space",
        "It decreases, because the gas becomes more dilute than it was",
        "It is unchanged, because the temperature has not changed",
        "It is unchanged, because no energy has entered or left the gas",
        "It decreases, because the molecules collide with one another less often"],
      ans=0,
      why="EK 9.1.A.1 says that for a gas the entropy increases when there is an increase "
          "in volume at constant temperature, and gives the reason directly: the gas "
          "molecules are able to move within a larger space. Constant temperature is what "
          "isolates the volume effect rather than cancelling it."),

 dict(q="A fixed amount of gas is compressed into a smaller container while the "
        "temperature is held constant. What is the sign of the entropy change?",
      choices=[
        "Negative, because the molecules are confined to a smaller space",
        "Positive, because the molecules collide more often in the smaller container",
        "Positive, because compressing a gas raises its pressure",
        "Zero, because the temperature of the gas does not change",
        "Zero, because the number of gas molecules does not change"],
      ans=0,
      why="EK 9.1.A.1 ties the entropy of a gas to the space its molecules can move "
          "within, so reducing the volume at constant temperature reduces the dispersal "
          "of matter. Collision frequency and pressure are not the framework's criterion."),

 dict(q="The temperature of a sample of gas is raised at constant volume. What happens to "
        "its entropy, and what does kinetic molecular theory say about why?",
      choices=[
        "It increases, because the distribution of kinetic energy among the particles "
        "broadens",
        "It decreases, because the particles move too quickly to remain dispersed",
        "It is unchanged, because the volume available to the particles is fixed",
        "It increases, because the particles come to occupy a larger volume",
        "It is unchanged, because the number of particles present is fixed"],
      ans=0,
      why="EK 9.1.A.2 states that entropy increases when energy is dispersed, and that "
          "according to kinetic molecular theory the distribution of kinetic energy among "
          "the particles of a gas broadens as the temperature increases, so the entropy "
          "of the system increases with temperature. The volume is fixed here, so the "
          "dispersal is of energy rather than of matter."),

 dict(q="Two identical sealed samples of neon are held at 300 K and at 600 K. Which "
        "sample has the greater entropy?",
      choices=[
        "The sample at 600 K, because entropy increases with increasing temperature",
        "The sample at 300 K, because slower particles are arranged more randomly",
        "Neither, because the two samples contain the same substance",
        "Neither, because entropy depends only on the volume available",
        "The sample at 300 K, because energy is less dispersed at the lower temperature"],
      ans=0,
      why="EK 9.1.A.2 concludes that the entropy of the system increases with an increase "
          "in temperature, because the distribution of kinetic energy broadens. Energy "
          "genuinely is less dispersed at 300 K, but that is a reason for the colder "
          "sample to have the SMALLER entropy."),

 dict(q="For the reaction 2 NH3(g) gives N2(g) + 3 H2(g), what is the sign of the entropy "
        "change, and why?",
      choices=[
        "Positive, because the total moles of gas-phase products exceed the total moles "
        "of gas-phase reactants",
        "Negative, because a compound is broken into two elements",
        "Negative, because nitrogen and hydrogen are more stable than ammonia",
        "Zero, because the same atoms are present before and after the reaction",
        "Positive, because the reaction absorbs energy from its surroundings"],
      ans=0,
      why="EK 9.1.A.1 ends with the rule for reactions involving gas-phase species: the "
          "entropy generally increases when the total number of moles of gas-phase "
          "products is greater than the total number of moles of gas-phase reactants. "
          "Conservation of atoms holds in every reaction and so distinguishes nothing."),

 dict(q="For the reaction N2(g) + 3 H2(g) gives 2 NH3(g), what is the sign of the entropy "
        "change?",
      choices=[
        "Negative, because four moles of gas are replaced by two moles of gas",
        "Positive, because ammonia molecules are larger than hydrogen molecules",
        "Positive, because a new substance is formed that was not there before",
        "Zero, because the number of atoms is conserved in the reaction",
        "Negative, because ammonia is a gas at ordinary temperatures"],
      ans=0,
      why="EK 9.1.A.1's gas-mole rule runs in both directions: the entropy generally "
          "increases when the moles of gas-phase products exceed the moles of gas-phase "
          "reactants, so it falls when the reverse holds. Molecular size is not the "
          "framework's criterion."),

 dict(q="For the reaction CaCO3(s) gives CaO(s) + CO2(g), what is the sign of the entropy "
        "change?",
      choices=[
        "Positive, because a gas is produced where there was none among the reactants",
        "Negative, because a solid is among the products",
        "Negative, because the reaction must be heated strongly before it will occur",
        "Zero, because one mole of solid becomes one mole of solid",
        "Positive, because the reaction absorbs energy from its surroundings"],
      ans=0,
      why="EK 9.1.A.1's rule compares the total moles of gas-phase products with the "
          "total moles of gas-phase reactants, and here it rises from none to one, which "
          "is the dispersal of matter the statement describes. Whether a reaction absorbs "
          "energy is a separate question from its entropy change."),

 dict(q="For the reaction 2 CO(g) + O2(g) gives 2 CO2(g), what is the sign of the entropy "
        "change?",
      choices=[
        "Negative, because three moles of gas become two moles of gas",
        "Positive, because carbon dioxide molecules are larger than carbon monoxide "
        "molecules",
        "Positive, because the reaction releases energy to its surroundings",
        "Zero, because every species in the reaction is a gas",
        "Negative, because oxygen is entirely consumed by the reaction"],
      ans=0,
      why="EK 9.1.A.1's gas-mole rule counts moles rather than molecular sizes or "
          "identities, and the total moles of gas-phase products here is smaller than the "
          "total moles of gas-phase reactants. That every species is a gas is what makes "
          "the rule applicable, not what makes the change zero."),

 dict(q="For the reaction H2(g) + Cl2(g) gives 2 HCl(g), what does the framework's rule "
        "about moles of gas predict?",
      choices=[
        "It predicts no increase, because the total moles of gas are the same on both "
        "sides",
        "It predicts a large increase, because the product is a compound",
        "It predicts a large decrease, because two reactants become one product",
        "It predicts an increase, because hydrogen chloride is a gas",
        "The rule cannot be applied, because no gases take part in the reaction"],
      ans=0,
      why="EK 9.1.A.1 makes the entropy generally increase when the moles of gas-phase "
          "products exceed the moles of gas-phase reactants, and here the two totals are "
          "equal, so the rule predicts no increase on that ground. Counting SUBSTANCES "
          "rather than moles of gas is the error the other options make."),

 dict(q="The table gives the total moles of gas-phase reactants and products for four "
        "reactions. For which reaction does the framework's gas-mole rule predict the "
        "largest increase in entropy?",
      table=_T_GASMOLES,
      choices=["Reaction Z", "Reaction W", "Reaction X", "Reaction Y",
               "Reactions W and Z equally"],
      ans=0,
      why="EK 9.1.A.1 makes the entropy generally increase when the total moles of "
          "gas-phase products exceed the total moles of gas-phase reactants, so the "
          "largest increase belongs to the tabulated reaction with the largest surplus of "
          "gas-phase product moles."),

 dict(q="Using the same table of gas-mole totals, for which reaction does the rule "
        "predict a decrease in entropy?",
      table=_T_GASMOLES,
      choices=["Reaction X", "Reaction W", "Reaction Y", "Reaction Z",
               "None of the four reactions"],
      ans=0,
      why="EK 9.1.A.1's rule predicts a decrease where the total moles of gas-phase "
          "products fall short of the total moles of gas-phase reactants, and exactly one "
          "tabulated row does that."),

 dict(q="Using the tabulated gas-mole totals once more, for which reaction does the rule "
        "predict neither an increase nor a decrease?",
      table=_T_GASMOLES,
      choices=[
        "Reaction Y, because the total moles of gas are equal on the two sides",
        "Reaction W, because it forms more moles of gas than it consumes",
        "Reaction X, because it consumes more moles of gas than it forms",
        "Reaction Z, because it forms the greatest number of moles of gas",
        "None of them, because the rule decides every case"],
      ans=0,
      why="EK 9.1.A.1's rule turns on a comparison of two totals, so it predicts a "
          "direction only where they differ. Exactly one tabulated reaction has them "
          "equal, and for that one the rule is silent rather than predicting zero for "
          "some other reason."),

 dict(q="Solid carbon dioxide sublimes directly to carbon dioxide gas. What is the sign "
        "of the entropy change of the carbon dioxide?",
      choices=[
        "Positive, because the particles become far freer to move as the solid becomes a "
        "gas",
        "Negative, because the visible solid disappears from the container",
        "Zero, because the substance is chemically the same before and after",
        "Negative, because sublimation absorbs energy from the surroundings",
        "Positive, because sublimation skips the liquid state entirely"],
      ans=0,
      why="EK 9.1.A.1 explains the phase changes toward the gas state as a dispersal of "
          "matter in which the individual particles become freer to move and generally "
          "occupy a larger volume, which is exactly what sublimation does in one step."),

 dict(q="Water vapour deposits directly as frost on a cold surface. What is the sign of "
        "the entropy change of the water?",
      choices=[
        "Negative, because matter that was dispersed as a gas becomes a fixed solid",
        "Positive, because the frost occupies a larger volume than the vapour did",
        "Positive, because energy leaves the water during deposition",
        "Zero, because no chemical bonds are broken or formed",
        "Negative, because the temperature of the cold surface falls further"],
      ans=0,
      why="EK 9.1.A.1 makes entropy increase when matter becomes more dispersed and the "
          "particles become freer to move, so a change that fixes gas particles into a "
          "solid runs the other way. A gas occupies a far larger volume than the solid it "
          "deposits as."),

 dict(q="Liquid bromine vaporizes at its boiling point. Which statement best explains the "
        "sign of the entropy change of the bromine?",
      choices=[
        "The entropy increases, because the particles in the gas are freer to move and "
        "occupy a much larger volume",
        "The entropy decreases, because gas particles are farther apart and interact less",
        "The entropy is unchanged, because the temperature stays constant while it boils",
        "The entropy decreases, because energy is absorbed from the surroundings",
        "The entropy increases, because the mass of the sample rises as it vaporizes"],
      ans=0,
      why="EK 9.1.A.1 names the phase change from liquid to gas as a dispersal of matter "
          "in which the individual particles become freer to move and generally occupy a "
          "larger volume. Mass is conserved in a phase change, and a constant temperature "
          "does not prevent the dispersal of matter."),

 dict(q="Which pair of changes does the framework name as the two circumstances in which "
        "entropy increases?",
      choices=[
        "Matter becoming more dispersed and energy becoming more dispersed",
        "Matter becoming more dispersed and the temperature falling",
        "Energy becoming more concentrated and the volume decreasing",
        "The number of particles falling and the temperature rising",
        "Energy becoming more dispersed and the pressure rising"],
      ans=0,
      why="EK 9.1.A.1 opens with the dispersal of matter and EK 9.1.A.2 opens with the "
          "dispersal of energy, and those two sentences are the whole of the framework's "
          "account of when entropy increases in this topic."),

 dict(q="A student claims that the entropy of a gas cannot change unless its volume "
        "changes. What is wrong with the claim?",
      choices=[
        "Entropy also increases with temperature, because the distribution of kinetic "
        "energy broadens",
        "Nothing is wrong: volume is the only quantity entropy depends on",
        "Entropy depends only on how many particles are present in the sample",
        "Entropy can change only during a chemical reaction, never a physical one",
        "Entropy also falls as temperature rises, because faster particles collide more"],
      ans=0,
      why="EK 9.1.A.2 gives a second route to higher entropy that has nothing to do with "
          "volume: the distribution of kinetic energy among the particles of a gas "
          "broadens as the temperature increases, so the entropy of the system increases "
          "with temperature."),

 dict(q="For the reaction 2 H2O2(l) gives 2 H2O(l) + O2(g), what is the sign of the "
        "entropy change?",
      choices=[
        "Positive, because a gas is formed from liquids alone",
        "Negative, because hydrogen peroxide is broken into simpler substances",
        "Zero, because the same atoms appear on both sides of the equation",
        "Negative, because oxygen gas escapes from the open container",
        "Positive, because the reaction gives out energy as heat"],
      ans=0,
      why="EK 9.1.A.1's rule compares the total moles of gas-phase products with the "
          "total moles of gas-phase reactants, and here that total rises from none to "
          "one, which is the dispersal of matter the statement describes."),

 dict(q="Reaction P converts 1 mole of gas into 3 moles of gas, and reaction Q converts 1 "
        "mole of gas into 2 moles of gas. Which has the greater increase in entropy on the "
        "framework's gas-mole rule?",
      choices=[
        "Reaction P, because it produces the greater increase in the moles of gas",
        "Reaction Q, because it produces the smaller number of moles of gas",
        "The two increases are equal, because both reactions produce more gas",
        "Reaction Q, because a smaller change in moles is always the larger entropy change",
        "The rule cannot compare two different reactions with one another"],
      ans=0,
      why="Learning objective 9.1.A asks for the relative magnitude as well as the sign, "
          "and EK 9.1.A.1 ties the increase to the surplus of gas-phase product moles "
          "over gas-phase reactant moles, which is larger for the reaction that gains two "
          "moles than for the one that gains one."),

 dict(q="Which of these changes disperses ENERGY rather than matter?",
      choices=[
        "Heating a sealed sample of argon from 250 K to 400 K",
        "Allowing a gas to expand into an evacuated bulb",
        "Melting a block of ice at its melting point",
        "Boiling a beaker of water at its boiling point",
        "Letting a solid sublime into a large empty container"],
      ans=0,
      why="EK 9.1.A.2 attributes the temperature effect to the broadening distribution of "
          "kinetic energy among the particles, which is a dispersal of energy. The other "
          "changes move matter into a larger volume, which is EK 9.1.A.1's route."),

 dict(q="Which of these changes disperses MATTER rather than energy?",
      choices=[
        "Allowing a gas to expand from a small bulb into a much larger one at constant "
        "temperature",
        "Warming a sealed flask of nitrogen from 300 K to 500 K",
        "Cooling a sealed flask of nitrogen from 500 K to 300 K",
        "Raising the temperature of a block of copper",
        "Broadening the range of kinetic energies in a gas by heating it"],
      ans=0,
      why="EK 9.1.A.1 attributes the volume effect to the gas molecules being able to "
          "move within a larger space, which is a dispersal of matter, while every "
          "temperature change listed is EK 9.1.A.2's dispersal of energy."),

 dict(q="According to kinetic molecular theory, what happens to the distribution of "
        "kinetic energy among the particles of a gas as the temperature rises, and what "
        "follows for the entropy?",
      choices=[
        "It broadens, and the entropy of the gas therefore increases",
        "It narrows, and the entropy of the gas therefore decreases",
        "It broadens, but the entropy of the gas is unaffected by it",
        "It stays as it was, because only the average kinetic energy changes",
        "It narrows, but the entropy of the gas increases in spite of that"],
      ans=0,
      why="EK 9.1.A.2 states both halves in one sentence: the distribution of kinetic "
          "energy among the particles of a gas broadens as the temperature increases, and "
          "as a result the entropy of the system increases with an increase in "
          "temperature."),

 dict(q="The table lists four physical changes by the state of the substance before and "
        "after. For which processes is the entropy change of the substance positive?",
      table=_T_PHASES,
      choices=[
        "Processes 1 and 3, because in each the matter present becomes more dispersed",
        "Processes 2 and 4, because in each the matter present becomes more dispersed",
        "Process 3 only, because only a gas counts as dispersed matter",
        "Process 1 only, because melting is the only change that frees the particles",
        "All four, because every phase change frees the particles to some degree"],
      ans=0,
      why="EK 9.1.A.1 makes the entropy increase when matter becomes more dispersed, and "
          "names the change from solid to liquid and the change from liquid to gas as "
          "exactly those cases. The tabulated changes toward the solid state run the "
          "other way."),

 dict(q="Using the same table of state changes, for which processes does the entropy of "
        "the substance decrease?",
      table=_T_PHASES,
      choices=[
        "Processes 2 and 4, because in each the matter present becomes less dispersed",
        "Processes 1 and 3, because in each the matter present becomes less dispersed",
        "Process 4 only, because only a solid counts as ordered",
        "Process 2 only, because only condensation removes a gas",
        "None of them, because entropy never decreases in a physical change"],
      ans=0,
      why="EK 9.1.A.1's criterion is the dispersal of matter, so the tabulated changes "
          "that take a substance toward the solid state lower the entropy. Entropy of a "
          "SYSTEM certainly can fall, which is why the framework asks for a sign at all."),

 dict(q="One mole of argon occupies 1.0 L and a second mole of argon at the same "
        "temperature occupies 10.0 L. Which sample has the greater entropy?",
      choices=[
        "The 10.0 L sample, because its particles can move within a larger space",
        "The 1.0 L sample, because its particles collide with one another more often",
        "Neither, because both samples hold the same amount of argon",
        "Neither, because the two samples are at the same temperature",
        "The 1.0 L sample, because a higher pressure disperses matter further"],
      ans=0,
      why="EK 9.1.A.1 states that for a gas the entropy increases when there is an "
          "increase in volume at constant temperature, because the gas molecules are able "
          "to move within a larger space. Equal amounts and equal temperatures are what "
          "leave volume as the only difference."),

 dict(q="For the reaction 2 KClO3(s) gives 2 KCl(s) + 3 O2(g), what is the sign of the "
        "entropy change?",
      choices=[
        "Positive, because three moles of gas appear where the reactants contained none",
        "Negative, because two moles of solid are consumed by the reaction",
        "Negative, because the reaction must be heated before it will proceed",
        "Zero, because two moles of solid become two moles of solid",
        "Positive, because the products are simpler substances than the reactant"],
      ans=0,
      why="EK 9.1.A.1's rule compares the total moles of gas-phase products with the "
          "total moles of gas-phase reactants, and that total rises here from none to "
          "three. Simplicity of the products is not the framework's criterion."),

 dict(q="Which of these would NOT, by itself, increase the entropy of a sample of gas?",
      choices=[
        "Compressing the sample into a smaller volume at constant temperature",
        "Allowing the sample to expand at constant temperature",
        "Raising the temperature of the sample",
        "Allowing the sample to expand into an evacuated space",
        "Broadening the distribution of kinetic energies of its particles by heating it"],
      ans=0,
      why="EK 9.1.A.1 raises the entropy of a gas when its volume increases and EK "
          "9.1.A.2 raises it when the temperature increases, so the one change listed "
          "that reduces the space available to the molecules is the one that lowers the "
          "entropy instead."),

]
