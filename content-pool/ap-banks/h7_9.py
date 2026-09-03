# AP CHEMISTRY 7.9 Introduction to Le Chatelier's Principle
# CED effective Fall 2024, Unit 7 Equilibrium. The CED prints the title with an accented
# "Chatelier"; TOPIC below carries the title exactly as CHEMISTRY_topics.json records it.
# Learning objective 7.9.A: identify the response of a system at equilibrium to an
# external stress, using Le Chatelier's principle. Suggested skill 6.F, explain the
# connection between experimental results and chemical concepts, processes, or theories.
#
# Essential knowledge relied on, in the framework's own words:
#   7.9.A.1  Le Chatelier's principle can be used to predict the response of a system to
#            stresses such as addition or removal of a chemical species, change in
#            temperature, change in volume/pressure of a gas-phase system, or dilution of
#            a reaction system.
#   7.9.A.2  Le Chatelier's principle can be used to predict the effect that a stress will
#            have on experimentally measurable properties such as pH, temperature, and
#            color of a solution.
#
# SCOPE, and this matters because 7.10 is the very next topic. 7.10 owns the MECHANISM --
# that a disturbance makes Q differ from K, that a concentration change moves Q only while
# a temperature change moves K, and that the system responds by bringing the two back into
# agreement. Nothing below argues from Q. Every item here names one of the four stresses
# in EK 7.9.A.1 and asks for the direction of the response or for its effect on one of the
# three measurable properties named in EK 7.9.A.2.
#
# COLOURS AND pH VALUES ARE SUPPLIED IN THE STEM, never assumed from memory of a
# particular indicator or complex ion, so no key rests on a fact the CED does not state.
#
# NOTATION. export_units.py does not typeset Chemistry; reaction arrows are written as the
# word "to" so no glyph is left outside a math span.
TOPIC = ("7.9", "Introduction to Le Châtelier’s Principle", 7)

_T_GASCOUNT = dict(
    headers=["Reaction", "Equation", "Moles of gas on the reactant side",
             "Moles of gas on the product side"],
    rows=[["1", "N2(g) + 3 H2(g) to 2 NH3(g)", "4", "2"],
          ["2", "H2(g) + I2(g) to 2 HI(g)", "2", "2"],
          ["3", "N2O4(g) to 2 NO2(g)", "1", "2"]])

_T_COLOUR = dict(
    headers=["Trial", "Change made to the flask", "Colour after the change"],
    rows=[["1", "Some FeSCN2+ removed", "paler red"],
          ["2", "Some SCN- added", "deeper red"],
          ["3", "Water added to dilute the solution", "paler red"]])

_T_TEMP = dict(
    headers=["Flask", "Temperature of the water bath in degrees Celsius",
             "Colour of the equilibrium mixture"],
    rows=[["Cold bath", "5", "pink"],
          ["Room temperature", "25", "purple"],
          ["Hot bath", "80", "blue"]])

QUESTIONS = [

 dict(q="The reaction N2(g) + 3 H2(g) to 2 NH3(g) is at equilibrium in a rigid vessel. "
        "Additional H2(g) is injected without changing the temperature. In which "
        "direction does the system respond?",
      choices=[
        "Toward the products, consuming some of the added H2(g)",
        "Toward the reactants, producing more H2(g) than was added",
        "There is no response, because the vessel is rigid",
        "There is no response, because only a change in temperature is a stress",
        "Toward the reactants, because the added gas raises the total pressure"],
      ans=0,
      why="EK 7.9.A.1 names addition of a chemical species as a stress and has the "
          "principle predict the response. Adding a reactant is relieved by consuming "
          "some of it, which is a shift toward the products. A rigid vessel does not "
          "prevent a concentration change, and temperature is only one of the four "
          "stresses the framework lists."),

 dict(q="Ammonia is continuously removed from an equilibrium mixture of N2(g), H2(g) and "
        "NH3(g) at constant temperature. What does the system do?",
      choices=[
        "It shifts toward the products, forming more NH3(g)",
        "It shifts toward the reactants, forming more N2(g) and H2(g)",
        "It remains exactly as it was, because removal is not a stress",
        "It stops reacting altogether once ammonia is withdrawn",
        "It shifts toward the products only if the vessel is also cooled"],
      ans=0,
      why="EK 7.9.A.1 names removal of a chemical species as a stress. Removing a product "
          "is relieved by making more of it, which is a shift toward the products. "
          "Removal and addition are both listed, so removal is a stress in its own "
          "right."),

 dict(q="An equilibrium mixture for the exothermic reaction 2 SO2(g) + O2(g) to "
        "2 SO3(g) is heated. How does the position of the equilibrium respond?",
      choices=[
        "It shifts toward the reactants, because heating an exothermic reaction favours "
        "the side that absorbs energy",
        "It shifts toward the products, because heating always speeds the forward "
        "reaction more than the reverse",
        "It does not shift, because a temperature change alters only the rate and not "
        "the position",
        "It shifts toward the products, because heat is a product of an exothermic "
        "reaction",
        "It shifts toward whichever side has fewer moles of gas, whatever the sign of "
        "the enthalpy change"],
      ans=0,
      why="EK 7.9.A.1 names a change in temperature as a stress. An exothermic reaction "
          "releases energy as it goes forward, so supplying energy is relieved by the "
          "reverse direction, which absorbs it. Heating changes where the equilibrium "
          "lies, not only how fast it is reached."),

 dict(q="The endothermic reaction CaCO3(s) to CaO(s) + CO2(g) is at equilibrium in a "
        "closed vessel. The vessel is cooled. What happens to the amount of CO2(g)?",
      choices=[
        "It decreases, because cooling favours the direction that releases energy",
        "It increases, because cooling always favours the formation of a gas",
        "It is unchanged, because two of the three species are solids",
        "It increases, because a lower temperature increases the solubility of the gas",
        "It is unchanged, because cooling changes only the rate of reaction"],
      ans=0,
      why="EK 7.9.A.1 names a change in temperature as a stress. The forward direction "
          "here absorbs energy, so removing energy is relieved by the reverse direction, "
          "which consumes CO2. The presence of solids does not exempt the system from a "
          "temperature stress."),

 dict(q="An equilibrium mixture of N2O4(g) and NO2(g) in a cylinder is compressed to half "
        "its volume at constant temperature. The equation is N2O4(g) to 2 NO2(g). Which "
        "response does Le Chatelier's principle predict?",
      choices=[
        "A shift toward N2O4(g), the side with fewer moles of gas",
        "A shift toward NO2(g), the side with more moles of gas",
        "No shift, because the number of molecules in the cylinder cannot change",
        "A shift toward NO2(g), because compression always favours the products",
        "No shift, because the temperature was held constant"],
      ans=0,
      why="EK 7.9.A.1 names a change in volume or pressure of a gas-phase system as a "
          "stress. Compression raises the pressure, and the system relieves that by "
          "moving toward the side with fewer moles of gas, which is the single mole of "
          "N2O4 rather than the two moles of NO2."),

 dict(q="Using the table, which reaction is UNAFFECTED in position by compressing the "
        "vessel at constant temperature?",
      table=_T_GASCOUNT,
      choices=["Reaction 2", "Reaction 1", "Reaction 3", "Reactions 1 and 3",
               "All three reactions"],
      ans=0,
      why="EK 7.9.A.1 makes a volume or pressure change a stress for a gas-phase system, "
          "and a system relieves compression by moving toward fewer moles of gas. The "
          "tabulated counts are equal on the two sides for one of the three reactions, "
          "so that one has no side to move toward."),

 dict(q="Using the same table, which reaction shifts toward its PRODUCTS when the vessel "
        "is expanded at constant temperature?",
      table=_T_GASCOUNT,
      choices=["Reaction 3", "Reaction 1", "Reaction 2", "Reactions 1 and 2",
               "None of the three reactions"],
      ans=0,
      why="Expansion lowers the pressure, and EK 7.9.A.1 makes that a stress relieved by "
          "moving toward the side with MORE moles of gas. The tabulated counts show one "
          "reaction whose product side carries more moles of gas than its reactant side."),

 dict(q="A saturated aqueous equilibrium is diluted by adding pure water at constant "
        "temperature. Which stress from the course framework has been applied?",
      choices=[
        "Dilution of a reaction system",
        "A change in the volume of a gas-phase system",
        "A change in the temperature of the system",
        "The addition of a catalyst to the system",
        "The removal of a chemical species from the system"],
      ans=0,
      why="EK 7.9.A.1 lists four kinds of stress, and dilution of a reaction system is "
          "one of them, named separately from a change in the volume of a gas-phase "
          "system. A catalyst is not among the stresses the framework names."),

 dict(q="A flask holds the equilibrium Fe3+(aq) + SCN-(aq) to FeSCN2+(aq), in which the "
        "product is deep red and the reactants are nearly colourless. Solid KSCN is "
        "dissolved in the flask at constant temperature. What is observed?",
      choices=[
        "The red colour deepens, because the system shifts toward the product",
        "The red colour fades, because the system shifts toward the reactants",
        "The colour is unchanged, because a solid was added rather than a solution",
        "The red colour fades, because the added ion is a spectator",
        "The colour is unchanged, because only temperature affects colour"],
      ans=0,
      why="EK 7.9.A.1 names addition of a chemical species as a stress and EK 7.9.A.2 "
          "makes colour of a solution a measurable property the principle can be used to "
          "predict. Adding a reactant is relieved by forming more product, and the stem "
          "states that the product is the coloured species."),

 dict(q="In the same red-coloured system, silver nitrate solution is added, which removes "
        "SCN-(aq) by precipitating AgSCN(s). What happens to the colour?",
      choices=[
        "It fades, because removing a reactant shifts the system toward the reactants",
        "It deepens, because removing a reactant shifts the system toward the product",
        "It is unchanged, because a precipitate leaves the solution phase",
        "It deepens, because the precipitate itself is deep red",
        "It fades, because the system stops reacting once a precipitate forms"],
      ans=0,
      why="EK 7.9.A.1 names removal of a chemical species as a stress; precipitating one "
          "of the reactants removes it from solution. The system relieves that by "
          "reforming the removed species, which consumes the coloured product, and EK "
          "7.9.A.2 makes the fading colour the measurable consequence."),

 dict(q="The table records three changes made to the same red equilibrium and the colour "
        "observed after each. Which trial is the one in which a PRODUCT was removed?",
      table=_T_COLOUR,
      choices=["Trial 1", "Trial 2", "Trial 3", "Trials 1 and 3", "None of the trials"],
      ans=0,
      why="EK 7.9.A.1 names removal of a chemical species as a stress. Only one tabulated "
          "change removes the coloured product itself, and the recorded colour after it "
          "is paler, which is what removing the coloured species produces."),

 dict(q="In the same table, trial 3 dilutes the solution and the colour becomes paler. "
        "What is the best explanation?",
      table=_T_COLOUR,
      choices=[
        "Dilution is a stress under the framework, and it lowers the concentration of "
        "the coloured product",
        "Dilution is not a stress, so the paler colour must come from a temperature "
        "change",
        "Dilution destroys the coloured product, which cannot re-form once water is "
        "added",
        "Dilution raises the concentration of every species, which masks the colour",
        "Dilution changes the identity of the coloured species from red to colourless"],
      ans=0,
      why="EK 7.9.A.1 lists dilution of a reaction system as one of the four stresses, "
          "and EK 7.9.A.2 makes colour a property the principle can be used to predict. "
          "Adding water lowers every concentration, including that of the species the "
          "stem identifies as coloured."),

 dict(q="An aqueous solution of the weak acid CH3COOH is at equilibrium with H3O+(aq) and "
        "CH3COO-(aq). Solid sodium acetate is dissolved in it at constant temperature. "
        "What happens to the pH?",
      choices=[
        "It rises, because the system shifts toward the un-ionized acid and consumes "
        "hydronium ion",
        "It falls, because the system shifts toward the ions and produces more hydronium "
        "ion",
        "It is unchanged, because sodium acetate is neither an acid nor a base",
        "It falls, because adding any solid to a solution lowers the pH",
        "It is unchanged, because only a temperature change can alter the pH"],
      ans=0,
      why="EK 7.9.A.1 names addition of a chemical species as a stress, and EK 7.9.A.2 "
          "names pH as a measurable property whose response the principle predicts. "
          "Adding the acetate ion, a product of the ionization, is relieved by the "
          "reverse direction, which removes hydronium ion and so raises the pH."),

 dict(q="Hydrochloric acid is added to that same acetic acid equilibrium at constant "
        "temperature. Which prediction follows from Le Chatelier's principle?",
      choices=[
        "The proportion of the acid present as CH3COO- falls, because added hydronium "
        "ion pushes the system toward the un-ionized acid",
        "The proportion of the acid present as CH3COO- rises, because a stronger acid "
        "drives the weaker one to ionize further",
        "The proportion of the acid present as CH3COO- is unchanged, because "
        "hydrochloric acid is a different substance",
        "The acetic acid is destroyed, because a strong acid decomposes a weak one",
        "The pH rises, because two acids in the same flask partly cancel"],
      ans=0,
      why="EK 7.9.A.1 names addition of a chemical species as a stress, and hydronium ion "
          "is a product of the ionization already present in the equilibrium. Adding it "
          "is relieved by the reverse direction, which converts acetate back to the "
          "un-ionized acid."),

 dict(q="The table lists the colour of one cobalt equilibrium mixture in three water "
        "baths. Which conclusion about the forward reaction, the one that produces the "
        "blue species, does the framework support?",
      table=_T_TEMP,
      choices=[
        "It is endothermic, because raising the temperature moves the mixture toward the "
        "blue species",
        "It is exothermic, because raising the temperature moves the mixture toward the "
        "blue species",
        "It is endothermic, because the colour at room temperature lies between the "
        "other two",
        "Its enthalpy change cannot be inferred from a colour change of any kind",
        "It is exothermic, because cooling the mixture leaves it pink rather than "
        "colourless"],
      ans=0,
      why="EK 7.9.A.1 names a change in temperature as a stress and EK 7.9.A.2 names "
          "colour as a measurable property. Supplying energy is relieved by the direction "
          "that absorbs energy, so the direction favoured by heating is the endothermic "
          "one, and the tabulated colours put the blue species at the hot end."),

 dict(q="Using the same three water baths, what would be observed if the flask were moved "
        "from the hot bath back to the cold bath?",
      table=_T_TEMP,
      choices=[
        "The mixture would return toward pink, as the system shifts back to the species "
        "favoured at low temperature",
        "The mixture would stay blue, because a colour change caused by heating cannot "
        "be reversed",
        "The mixture would turn colourless, because both coloured species decompose on "
        "cooling",
        "The mixture would deepen in blue, because cooling always favours the product",
        "No prediction is possible, because Le Chatelier's principle applies only to "
        "gases"],
      ans=0,
      why="EK 7.9.A.1 makes a change in temperature a stress in either direction, so "
          "removing energy is relieved by the direction that releases it, returning the "
          "mixture toward the colour tabulated for the cold bath. The principle is not "
          "restricted to gas-phase systems; the framework lists dilution of a reaction "
          "system among the stresses."),

 dict(q="Argon, which takes no part in the reaction, is pumped into a RIGID vessel "
        "holding an equilibrium mixture of gases at constant temperature. What does Le "
        "Chatelier's principle predict?",
      choices=[
        "No shift, because the concentrations of the reacting gases are unchanged",
        "A shift toward the side with fewer moles of gas, because the total pressure has "
        "risen",
        "A shift toward the side with more moles of gas, because the vessel now holds "
        "more particles",
        "A shift toward the products, because argon acts as a catalyst",
        "A shift toward the reactants, because argon dilutes the products"],
      ans=0,
      why="EK 7.9.A.1 names a change in volume or pressure of a gas-phase system as a "
          "stress. In a rigid vessel the volume is fixed and the added gas takes no part "
          "in the reaction, so the amount of each reacting gas in that fixed volume is "
          "exactly what it was and there is nothing for the system to relieve."),

 dict(q="An equilibrium mixture of H2(g), I2(g) and HI(g) is transferred to a vessel of "
        "twice the volume at constant temperature. The equation is H2(g) + I2(g) to "
        "2 HI(g). What is the response?",
      choices=[
        "No shift, because the two sides of the equation carry equal moles of gas",
        "A shift toward HI(g), because expansion always favours the products",
        "A shift toward H2(g) and I2(g), because expansion always favours the reactants",
        "A shift toward HI(g), because the concentration of HI(g) fell on expansion",
        "No shift, because a change in volume is not a stress under the framework"],
      ans=0,
      why="EK 7.9.A.1 makes a change in the volume of a gas-phase system a stress, but "
          "the relief available is a move toward the side with a different number of "
          "moles of gas. Here both sides carry two moles, so neither direction relieves "
          "the change and the position does not move."),

 dict(q="A reaction is exothermic in the forward direction and is at equilibrium in an "
        "insulated flask. A small amount of reactant is added. What happens to the "
        "temperature of the mixture?",
      choices=[
        "It rises, because the shift toward the products releases energy",
        "It falls, because the shift toward the products absorbs energy",
        "It is unchanged, because only a heater can change the temperature",
        "It falls, because adding cold reactant always cools the mixture",
        "It rises, because every chemical change releases energy"],
      ans=0,
      why="EK 7.9.A.1 names addition of a chemical species as a stress, and the response "
          "to added reactant is a shift toward the products. EK 7.9.A.2 names temperature "
          "as a measurable property the principle can be used to predict, and a forward "
          "shift in an exothermic reaction releases energy into an insulated flask."),

 dict(q="Which of the following is NOT one of the stresses that the course framework says "
        "Le Chatelier's principle can be used to respond to?",
      choices=[
        "Adding a catalyst to the reaction vessel",
        "Adding a chemical species that appears in the equation",
        "Changing the temperature of the system",
        "Changing the volume of a gas-phase system",
        "Diluting the reaction system"],
      ans=0,
      why="EK 7.9.A.1 names addition or removal of a chemical species, change in "
          "temperature, change in volume or pressure of a gas-phase system, and dilution "
          "of a reaction system. A catalyst is not on that list, and adding one does not "
          "move the position of an equilibrium."),

 dict(q="Which three experimentally measurable properties does the framework give as "
        "examples of what Le Chatelier's principle can be used to predict the effect of a "
        "stress on?",
      choices=[
        "pH, temperature, and colour of a solution",
        "pH, density, and viscosity of a solution",
        "Rate constant, activation energy, and half-life",
        "Colour of a solution, molar mass, and boiling point",
        "Temperature, electrical resistance, and refractive index"],
      ans=0,
      why="EK 7.9.A.2 names exactly these three: the principle can be used to predict the "
          "effect that a stress will have on experimentally measurable properties such as "
          "pH, temperature, and colour of a solution."),

 dict(q="An aqueous equilibrium between a pale species and an intensely coloured species "
        "is diluted with water. The equation converts two dissolved ions into one "
        "dissolved ion. Which way does the system respond to the dilution?",
      choices=[
        "Toward the two separate ions, the side with more dissolved particles",
        "Toward the single ion, the side with fewer dissolved particles",
        "It does not respond, because dilution lowers every concentration equally",
        "Toward the single ion, because the added water is itself a reactant",
        "It does not respond, because dilution is not listed as a stress"],
      ans=0,
      why="EK 7.9.A.1 lists dilution of a reaction system as a stress. Dilution lowers "
          "every concentration, and the side made of more dissolved particles is affected "
          "more strongly by the change, so the system relieves the dilution by moving "
          "toward that side."),

 dict(q="A student says that removing a product from an equilibrium mixture must "
        "eventually stop the reaction, since the product is being taken away. What is "
        "wrong with that reasoning?",
      choices=[
        "Removing product is a stress that the system relieves by making more product, "
        "so the forward reaction continues",
        "Removing product cannot be done, because a product is always in the same phase "
        "as its reactants",
        "Removing product is not a stress under the framework, so nothing at all happens",
        "Removing product shifts the system toward the reactants until no reactant is "
        "left",
        "Removing product raises the temperature, which is what keeps the reaction going"],
      ans=0,
      why="EK 7.9.A.1 names removal of a chemical species as a stress, and the response "
          "to removing a product is a shift toward the products. Continuous removal "
          "therefore keeps the forward reaction running rather than halting it."),

 dict(q="Nitrogen dioxide is a brown gas and dinitrogen tetroxide is colourless, and the "
        "two are at equilibrium in a syringe. The plunger is pushed in quickly, halving "
        "the volume. After the mixture settles, what colour is observed compared with the "
        "colour before the plunger moved?",
      choices=[
        "Paler than at first, because the system shifts toward the colourless species "
        "with fewer moles of gas",
        "Darker than at first, because the system shifts toward the brown species with "
        "more moles of gas",
        "Exactly the same, because the number of molecules in the syringe cannot change",
        "Colourless, because compression converts all of the brown gas",
        "Darker than at first, because compression cannot change the position of an "
        "equilibrium"],
      ans=0,
      why="EK 7.9.A.1 makes compression of a gas-phase system a stress, relieved by "
          "moving toward the side with fewer moles of gas, which the stem identifies as "
          "the colourless species. EK 7.9.A.2 names colour as the measurable property "
          "that reports the shift, and the settled colour is compared after the shift, "
          "not at the instant of compression."),

 dict(q="Why does adding more solid CaCO3 to the equilibrium CaCO3(s) to CaO(s) + CO2(g) "
        "produce no shift?",
      choices=[
        "Because a pure solid has a concentration that does not depend on how much of it "
        "is present",
        "Because a solid cannot take part in a reversible reaction at all",
        "Because adding a reactant is not one of the stresses the framework names",
        "Because the added solid reacts immediately with the CO2 already present",
        "Because the shift produced is too small to be measured in practice"],
      ans=0,
      why="EK 7.9.A.1 makes addition of a chemical species a stress, but a stress must "
          "change something the equilibrium responds to. Piling up more of a pure solid "
          "leaves its concentration exactly as it was, so there is nothing to relieve. "
          "The solid does take part in the reaction; the equation is written with it."),

 dict(q="An endothermic aqueous reaction is at equilibrium in a beaker standing in a "
        "water bath. The bath is warmed. Which pair of changes is predicted?",
      choices=[
        "A shift toward the products, and an increase in the equilibrium amount of "
        "product",
        "A shift toward the reactants, and a decrease in the equilibrium amount of "
        "product",
        "A shift toward the products, and no change in the equilibrium amount of product",
        "No shift, and an increase in the equilibrium amount of product",
        "No shift, and no change in the equilibrium amount of product"],
      ans=0,
      why="EK 7.9.A.1 names a change in temperature as a stress. An endothermic forward "
          "reaction absorbs energy, so supplying energy is relieved by going forward, "
          "which leaves more product present once the system settles again."),

 dict(q="A gas-phase equilibrium is disturbed and the system responds. Which statement "
        "best describes what the response accomplishes?",
      choices=[
        "It partially offsets the change that was imposed, without undoing it entirely",
        "It restores every concentration exactly to its value before the disturbance",
        "It amplifies the change that was imposed, moving the system further from where "
        "it began",
        "It leaves every concentration where the disturbance put it and changes only the "
        "rate",
        "It converts all of the reactants into products regardless of the disturbance"],
      ans=0,
      why="EK 7.9.A.1 has the principle predict the RESPONSE of a system to a stress. The "
          "response moves the system so as to counter the imposed change in part: adding "
          "a reactant leaves more of that reactant present than before, even though some "
          "of the added amount is consumed."),

 dict(q="Two identical flasks hold the same aqueous equilibrium at the same temperature. "
        "Water is added to one of them only. Which comparison is correct after both have "
        "settled?",
      choices=[
        "The diluted flask has lower concentrations of every species than the other flask",
        "The diluted flask has the same concentration of every species as the other flask",
        "The diluted flask has higher concentrations of every species than the other flask",
        "The two flasks now hold different equilibrium constants",
        "The diluted flask is no longer at equilibrium and never will be again"],
      ans=0,
      why="EK 7.9.A.1 names dilution of a reaction system as a stress; adding solvent "
          "lowers every concentration, and the shift that follows only partly offsets "
          "that. The equilibrium constant is fixed by temperature, which both flasks "
          "share, and a disturbed system re-establishes equilibrium."),

 dict(q="Which experimental observation would be the clearest evidence that a stress has "
        "moved the position of an equilibrium rather than merely changed how fast it is "
        "reached?",
      choices=[
        "The colour of the settled mixture is different from its colour before the stress",
        "The mixture reaches its final colour more quickly than it did before",
        "The mixture bubbles vigorously for a few seconds after the stress",
        "The flask feels warm to the touch while the stress is being applied",
        "The mixture becomes cloudy and then clears again within a minute"],
      ans=0,
      why="EK 7.9.A.2 names colour of a solution as an experimentally measurable property "
          "whose change the principle predicts. A difference in the SETTLED colour "
          "reports a different equilibrium composition, whereas reaching the same final "
          "state sooner is a statement about rate alone."),

 dict(q="A reaction that produces a gas from dissolved reactants is at equilibrium in a "
        "sealed flask. Some of the gas above the solution is pumped out at constant "
        "temperature. What is predicted?",
      choices=[
        "The system shifts toward the gas, replacing part of what was removed",
        "The system shifts away from the gas, since less gas is now present to react",
        "Nothing changes, because a gas above a solution is not part of the equilibrium",
        "The system stops at once, because a sealed flask cannot be disturbed",
        "The dissolved reactants are converted entirely into gas"],
      ans=0,
      why="EK 7.9.A.1 names removal of a chemical species as a stress, and removing a "
          "product is relieved by producing more of it. The response replaces part of "
          "what was taken, not all of it, and it does not run to completion."),

]
