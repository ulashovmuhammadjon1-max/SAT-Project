# AP CHEMISTRY 4.7 Types of Chemical Reactions
# CED effective Fall 2024, Unit 4 Chemical Reactions.
# Learning objective 4.7.A: identify a reaction as acid-base,
# oxidation-reduction, or precipitation. Suggested skill 1.B, describe the
# components of and quantitative information from models and representations.
#
# Essential knowledge relied on, in the framework's own words:
#   4.7.A.1  Acid-base reactions involve transfer of one or more protons (H+
#            ions) between chemical species.
#   4.7.A.2  Oxidation-reduction (redox) reactions involve transfer of one or
#            more electrons between chemical species, as indicated by changes in
#            oxidation numbers of the involved species. Combustion is an
#            important subclass of oxidation-reduction reactions, in which a
#            species reacts with oxygen gas. In the case of hydrocarbons, carbon
#            dioxide and water are products of complete combustion.
#   4.7.A.3  In a redox reaction, electrons are transferred from the species
#            that is oxidized to the species that is reduced.
#   4.7.A.4  Oxidation numbers may be assigned to each of the atoms in the
#            reactants and products; this is often an effective way to identify
#            the oxidized and reduced species in a redox reaction.
#   4.7.A.5  Precipitation reactions frequently involve mixing ions in aqueous
#            solution to produce an insoluble or sparingly soluble ionic
#            compound. All sodium, potassium, ammonium, and nitrate salts are
#            soluble in water.
#
# TWO EXCLUSION STATEMENTS ARE OBEYED HERE, DELIBERATELY:
#   * "The meaning of the terms 'reducing agent' and 'oxidizing agent' will not
#     be assessed on the AP Exam." Neither phrase appears anywhere in this
#     module -- not in a stem, a choice or a rationale. Items ask which species
#     is oxidized and which is reduced, which 4.7.A.3 and 4.7.A.4 do state.
#   * "Rote memorization of 'solubility rules' other than those implied in
#     4.7.A.5 will not be assessed." So the ONLY solubility fact any key rests
#     on is that all sodium, potassium, ammonium and nitrate salts are soluble.
#     Where an item needs a compound to be insoluble, the stem SAYS a solid
#     appeared -- that is an observation, not a rule to be recalled.
#
# ON ASSIGNING OXIDATION NUMBERS. 4.7.A.4 says they may be assigned; it does not
# print the conventions. So an item needing a convention beyond "an element in
# its standard form is zero" or "a monatomic ion equals its charge" states the
# convention in its own stem, and the verifier recomputes from it.
#
# Topic 4.8 handles Bronsted-Lowry conjugate pairs and topic 4.9 handles balanced
# half-reactions; this module stays on CLASSIFICATION and oxidation numbers.
#
# NOTATION. Chemistry is not typeset; formulas and charges stay plain text.
TOPIC = ("4.7", "Types of Chemical Reactions", 4)

_T_ONUMBERS = dict(
    headers=["Element", "Oxidation number in the reactants",
             "Oxidation number in the products"],
    rows=[["Zn", "0", "+2"],
          ["Cu", "+2", "0"],
          ["S", "+6", "+6"],
          ["O", "-2", "-2"]])

_T_THREE = dict(
    headers=["Reaction", "Observation reported"],
    rows=[["I", "A gas is released and no oxidation number changes",
           ],
          ["II", "A yellow solid settles out of a clear mixture"],
          ["III", "A strip of metal disappears and a different metal coats the "
                  "beaker"]])

_T_SOLUBLE = dict(
    headers=["Solution mixed", "Ions present before mixing"],
    rows=[["Potassium iodide with lead(II) nitrate",
           "K+, I-, Pb2+, NO3-"],
          ["Sodium chloride with potassium nitrate",
           "Na+, Cl-, K+, NO3-"]])

_T_COMBUST = dict(
    headers=["Fuel burned in excess oxygen", "Products detected"],
    rows=[["Methane, CH4", "CO2 and H2O"],
          ["Ethane, C2H6", "CO2 and H2O"],
          ["Octane, C8H18", "CO2 and H2O"]])

_T_MNO = dict(
    headers=["Species", "Oxidation number of the manganese atom"],
    rows=[["MnO4-", "+7"],
          ["MnO2", "+4"],
          ["Mn2+", "+2"],
          ["Mn metal", "0"]])

QUESTIONS = [

 dict(q="Hydrochloric acid is mixed with sodium hydroxide solution and the "
        "products are sodium chloride solution and water. Which classification "
        "of this reaction is correct, and on what grounds?",
      choices=[
        "Acid-base, because a proton is transferred from the acid to the "
        "hydroxide ion",
        "Oxidation-reduction, because electrons move from the sodium to the "
        "chlorine",
        "Precipitation, because a new ionic compound, sodium chloride, is "
        "formed",
        "Oxidation-reduction, because the oxidation number of hydrogen falls "
        "from positive one to zero",
        "Acid-base, because the two solutions have different concentrations of "
        "dissolved ions"],
      ans=0,
      why="EK 4.7.A.1 defines acid-base reactions as involving the transfer of "
          "one or more protons between chemical species, which is what the "
          "hydroxide ion accepts here. No oxidation number changes, and EK "
          "4.7.A.5 makes all sodium salts soluble, so nothing precipitates."),

 dict(q="A strip of zinc is placed in copper(II) sulfate solution. The blue color "
        "fades, the zinc strip loses mass, and a reddish solid coats it. Which "
        "classification is correct?",
      choices=[
        "Oxidation-reduction, because electrons are transferred from the zinc to "
        "the copper(II) ions",
        "Acid-base, because the sulfate ion accepts a proton from the zinc",
        "Precipitation, because a solid appears where there was none before",
        "Oxidation-reduction, because the sulfate ion is converted into sulfur "
        "dioxide gas",
        "Acid-base, because the solution becomes less acidic as the color fades"],
      ans=0,
      why="EK 4.7.A.2 defines redox reactions as involving transfer of one or "
          "more electrons, and EK 4.7.A.3 has the electrons travel from the "
          "species oxidized to the species reduced. Zinc metal becomes zinc "
          "ions and copper(II) ions become copper metal."),

 dict(q="Solutions of silver nitrate and sodium chloride are mixed and a white "
        "solid appears immediately. Which classification is correct, and which "
        "compound is the solid?",
      choices=[
        "Precipitation, and the solid is silver chloride, because sodium and "
        "nitrate salts are soluble",
        "Precipitation, and the solid is sodium nitrate, because it is the other "
        "pairing of the four ions",
        "Oxidation-reduction, and the solid is silver metal, because silver ions "
        "gain electrons from chloride",
        "Acid-base, and the solid is silver hydroxide, because water donates a "
        "proton to the silver ion",
        "Precipitation, and the solid could be either silver chloride or sodium "
        "nitrate, since neither can be ruled out"],
      ans=0,
      why="EK 4.7.A.5 states that all sodium, potassium, ammonium and nitrate "
          "salts are soluble in water, so sodium nitrate stays dissolved. The "
          "only other pairing available from the four ions present is the "
          "silver and chloride combination."),

 dict(q="Propane burns completely in excess oxygen. How is this reaction "
        "classified, and what are its products?",
      choices=[
        "A subclass of oxidation-reduction called combustion, giving carbon "
        "dioxide and water",
        "An acid-base reaction, giving carbon dioxide and water",
        "A precipitation reaction, giving solid carbon and water vapor",
        "A subclass of oxidation-reduction called combustion, giving carbon "
        "monoxide and hydrogen gas",
        "A reaction of no assigned class, because propane contains no ions"],
      ans=0,
      why="EK 4.7.A.2 names combustion as an important subclass of "
          "oxidation-reduction reactions, in which a species reacts with oxygen "
          "gas, and states that carbon dioxide and water are the products of "
          "complete combustion of a hydrocarbon."),

 dict(q="In a redox reaction, in which direction do the electrons travel?",
      choices=[
        "From the species that is oxidized to the species that is reduced",
        "From the species that is reduced to the species that is oxidized",
        "From the more concentrated solution to the more dilute one",
        "From every species present toward the solvent surrounding them",
        "From the solid phase to the aqueous phase, whichever species are "
        "involved"],
      ans=0,
      why="EK 4.7.A.3, near verbatim: in a redox reaction, electrons are "
          "transferred from the species that is oxidized to the species that is "
          "reduced."),

 dict(q="Which of the following is the defining feature of an acid-base "
        "reaction?",
      choices=[
        "One or more protons are transferred between chemical species",
        "One or more electrons are transferred between chemical species",
        "An insoluble ionic compound forms from ions in solution",
        "A gas is released from the reaction mixture",
        "The temperature of the mixture rises measurably"],
      ans=0,
      why="EK 4.7.A.1, near verbatim: acid-base reactions involve transfer of "
          "one or more protons, that is H+ ions, between chemical species. "
          "Electron transfer defines the redox class under EK 4.7.A.2 and an "
          "insoluble product defines precipitation under EK 4.7.A.5."),

 dict(q="Sulfur trioxide, SO3, is a neutral molecule. Taking each oxygen atom to "
        "carry an oxidation number of negative two and requiring the oxidation "
        "numbers of all atoms to sum to the overall charge, what is the "
        "oxidation number of the sulfur atom?",
      choices=["+6", "+3", "+2", "-2", "0"],
      ans=0,
      why="EK 4.7.A.4 states that oxidation numbers may be assigned to each of "
          "the atoms. Three oxygen atoms at negative two total negative six, and "
          "the molecule is neutral, so the sulfur must carry the balancing "
          "positive value."),

 dict(q="The table gives the oxidation numbers of four elements before and after "
        "a reaction. Which species is oxidized?",
      table=_T_ONUMBERS,
      choices=[
        "Zinc, because its oxidation number increases",
        "Copper, because its oxidation number changes by two units",
        "Sulfur, because it holds the largest oxidation number in the table",
        "Oxygen, because it carries a negative oxidation number throughout",
        "None of them, because two elements change and two do not"],
      ans=0,
      why="EK 4.7.A.4 makes oxidation numbers the way to identify the oxidized "
          "and reduced species, and EK 4.7.A.3 has electrons leave the species "
          "that is oxidized. Losing electrons raises an oxidation number, and "
          "only one element in the table rises."),

 dict(q="Two solutions are mixed and the table lists the ions each pair supplies. "
        "In which mixture would no precipitate be expected, and why?",
      table=_T_SOLUBLE,
      choices=[
        "The sodium chloride with potassium nitrate mixture, because every "
        "possible pairing is a sodium, potassium or nitrate salt",
        "The potassium iodide with lead(II) nitrate mixture, because potassium "
        "salts are soluble",
        "Both mixtures, because ions in solution do not combine with one another",
        "Neither mixture, because mixing any two ionic solutions produces a solid",
        "The sodium chloride with potassium nitrate mixture, because it contains "
        "no metal ion with a charge greater than one"],
      ans=0,
      why="EK 4.7.A.5 states that all sodium, potassium, ammonium and nitrate "
          "salts are soluble in water. Every pairing available in that mixture "
          "falls under that statement, so nothing available can come out of "
          "solution."),

 dict(q="Magnesium metal is dropped into hydrochloric acid. Bubbles of hydrogen "
        "gas form and the magnesium dissolves. Which pair of classifications "
        "best describes what has happened?",
      choices=[
        "Oxidation-reduction, because magnesium atoms lose electrons and "
        "hydrogen ions gain them",
        "Precipitation only, because a new compound of magnesium is formed in "
        "the beaker",
        "Acid-base only, because an acid is one of the reactants",
        "Oxidation-reduction, because the chloride ion is converted to chlorine "
        "gas",
        "Neither class applies, because one reactant is a solid and the other a "
        "solution"],
      ans=0,
      why="EK 4.7.A.2 defines redox by the transfer of electrons, indicated by "
          "changes in oxidation numbers. Magnesium goes from zero to positive "
          "two and hydrogen from positive one to zero in H2, so electrons have "
          "moved between them."),

 dict(q="Which statement about combustion is consistent with the course "
        "framework?",
      choices=[
        "It is a subclass of oxidation-reduction in which a species reacts with "
        "oxygen gas",
        "It is a subclass of acid-base reactions in which a species releases "
        "protons to oxygen",
        "It is a class separate from oxidation-reduction because no ions are "
        "involved",
        "It is a subclass of precipitation because solid soot is always among "
        "the products",
        "It is a physical process, because the fuel changes phase as it burns"],
      ans=0,
      why="EK 4.7.A.2, near verbatim: combustion is an important subclass of "
          "oxidation-reduction reactions, in which a species reacts with oxygen "
          "gas."),

 dict(q="The table reports what was detected when three different hydrocarbons "
        "were burned in excess oxygen. What generalization do these results "
        "support?",
      table=_T_COMBUST,
      choices=[
        "Complete combustion of a hydrocarbon gives carbon dioxide and water, "
        "whatever the size of the molecule",
        "Larger hydrocarbons give different products from smaller ones, because "
        "they contain more carbon atoms",
        "Hydrocarbons burn to give hydrogen gas, which then reacts with the "
        "excess oxygen",
        "The products depend on whether the fuel is a gas or a liquid before "
        "burning",
        "No generalization is possible, because each fuel has a different "
        "formula"],
      ans=0,
      why="EK 4.7.A.2 states that in the case of hydrocarbons, carbon dioxide "
          "and water are the products of complete combustion. Every row of the "
          "table reports that same pair regardless of the fuel."),

 dict(q="Ammonia gas and hydrogen chloride gas meet and form a white solid, "
        "ammonium chloride. Which classification of this reaction is correct?",
      choices=[
        "Acid-base, because a proton passes from the hydrogen chloride to the "
        "ammonia",
        "Oxidation-reduction, because the nitrogen atom gains an electron from "
        "the chlorine",
        "Precipitation, because two aqueous solutions were mixed to give an "
        "insoluble ionic compound",
        "Combustion, because a gas reacts to give a solid product",
        "Oxidation-reduction, because the oxidation number of chlorine changes "
        "from zero to negative one"],
      ans=0,
      why="EK 4.7.A.1 defines acid-base reactions as the transfer of one or more "
          "protons between chemical species, which is exactly what forms the "
          "ammonium ion here. EK 4.7.A.5's precipitation class requires ions "
          "mixed in aqueous solution, and no solution is involved."),

 dict(q="Which of the following reactions is NOT an oxidation-reduction reaction?",
      choices=[
        "Nitric acid reacting with potassium hydroxide to give potassium nitrate "
        "and water",
        "Iron reacting with oxygen to give iron(III) oxide",
        "Methane burning in oxygen to give carbon dioxide and water",
        "Chlorine gas reacting with sodium metal to give sodium chloride",
        "Copper metal reacting with silver ions to give copper(II) ions and "
        "silver metal"],
      ans=0,
      why="EK 4.7.A.2 makes changes in oxidation number the indicator of "
          "electron transfer. In the neutralization every element keeps the "
          "oxidation number it began with, so only protons move, which EK "
          "4.7.A.1 makes an acid-base reaction."),

 dict(q="A student assigns an oxidation number of zero to the chlorine atoms in "
        "Cl2 and negative one to the chloride ion in NaCl. Which reasoning "
        "supports those assignments?",
      choices=[
        "An element in its standard form is assigned zero, and a monatomic ion "
        "is assigned its own charge",
        "Any atom bonded to another atom of the same element is assigned "
        "negative one",
        "Chlorine is always assigned negative one, so Cl2 must be an exception "
        "with no rule behind it",
        "An atom in a molecule is assigned the number of bonds it forms",
        "The oxidation number of any halogen equals the group number of the "
        "element"],
      ans=0,
      why="EK 4.7.A.4 states that oxidation numbers may be assigned to each of "
          "the atoms in the reactants and products. The two assignments the "
          "student makes are the two least ambiguous cases: an uncombined "
          "element, and an ion whose whole charge is its oxidation number."),

 dict(q="In the reaction 2 Na + Cl2 → 2 NaCl, which species is reduced and by "
        "what evidence?",
      choices=[
        "Chlorine, because each chlorine atom goes from an oxidation number of "
        "zero to negative one",
        "Sodium, because each sodium atom goes from zero to positive one",
        "Chlorine, because it is the more electronegative of the two elements",
        "Sodium, because it is a metal and metals gain electrons in ionic "
        "compounds",
        "Neither, because the product is a neutral compound overall"],
      ans=0,
      why="EK 4.7.A.4 makes changes in oxidation number the way to identify the "
          "reduced species, and EK 4.7.A.3 has electrons arrive at the species "
          "that is reduced. Gaining electrons lowers an oxidation number, and "
          "chlorine's falls."),

 dict(q="The table gives the oxidation number of manganese in four species. Which "
        "conversion represents manganese being reduced by the largest number of "
        "units?",
      table=_T_MNO,
      choices=[
        "MnO4- becoming Mn metal, a fall of seven units",
        "MnO4- becoming Mn2+, a fall of five units",
        "MnO2 becoming Mn2+, a fall of two units",
        "Mn metal becoming Mn2+, a rise of two units",
        "MnO2 becoming MnO4-, a rise of three units"],
      ans=0,
      why="EK 4.7.A.4 makes oxidation numbers the way to identify oxidation and "
          "reduction, and reduction is the fall. Comparing the tabulated values "
          "shows which pair of species is separated by the largest decrease."),

 dict(q="Calcium carbonate reacts with hydrochloric acid to give calcium "
        "chloride, water and carbon dioxide gas. What justifies calling this an "
        "acid-base reaction?",
      choices=[
        "Protons from the acid are transferred to the carbonate ion, which then "
        "breaks up into water and carbon dioxide",
        "Electrons are transferred from the carbonate ion to the hydrogen ions, "
        "releasing gas",
        "An insoluble calcium compound forms and settles out of the mixture",
        "The carbon atom changes its oxidation number from positive four to zero",
        "The reaction releases a gas, and every gas-releasing reaction is "
        "acid-base"],
      ans=0,
      why="EK 4.7.A.1 defines acid-base reactions as the transfer of one or more "
          "protons between chemical species. Calcium keeps its charge, carbon "
          "stays at the same oxidation number, and the calcium chloride formed "
          "remains dissolved."),

 dict(q="Which observation on its own would be strongest evidence that a "
        "precipitation reaction has occurred?",
      choices=[
        "A solid appears after two clear aqueous solutions of ionic compounds "
        "are combined",
        "The temperature of the mixture rises by several degrees",
        "A gas is released steadily from the mixture",
        "The mixture conducts electricity better than either solution did alone",
        "The color of the mixture is different from the color of either "
        "solution"],
      ans=0,
      why="EK 4.7.A.5 states that precipitation reactions frequently involve "
          "mixing ions in aqueous solution to produce an insoluble or sparingly "
          "soluble ionic compound. The appearance of that solid is the "
          "observation the class is named for."),

 dict(q="Potassium iodide solution is added to lead(II) nitrate solution and a "
        "bright yellow solid forms. Which ions remain dissolved in the mixture "
        "afterward?",
      choices=[
        "Potassium ions and nitrate ions, because all potassium and nitrate "
        "salts are soluble",
        "Lead(II) ions and iodide ions, because they are the ions that reacted",
        "Potassium ions only, because nitrate ions are consumed in forming the "
        "solid",
        "No ions at all, because a precipitation reaction removes every ion from "
        "solution",
        "Lead(II) ions and nitrate ions, because both carry the same sign of "
        "charge"],
      ans=0,
      why="EK 4.7.A.5 states that all sodium, potassium, ammonium and nitrate "
          "salts are soluble in water, so the pairing of those two ions cannot "
          "come out of solution. The yellow solid must therefore be the other "
          "pairing available."),

 dict(q="Which of the following statements correctly relates oxidation numbers to "
        "electron transfer?",
      choices=[
        "A rise in oxidation number accompanies the loss of electrons and a fall "
        "accompanies their gain",
        "A rise in oxidation number accompanies the gain of electrons and a fall "
        "accompanies their loss",
        "Oxidation numbers change only when a reaction produces a gas",
        "Oxidation numbers are unrelated to electron transfer and only track "
        "charge on whole ions",
        "Every atom in a redox reaction changes its oxidation number by the same "
        "amount"],
      ans=0,
      why="EK 4.7.A.2 says the transfer of electrons is indicated by changes in "
          "oxidation numbers, and EK 4.7.A.3 sends electrons from the oxidized "
          "species to the reduced one. Losing negative charge raises the "
          "assigned number and gaining it lowers the number."),

 dict(q="The table lists three reactions with one observation each. Which "
        "reaction is best classified as a precipitation reaction?",
      table=_T_THREE,
      choices=[
        "Reaction II, because a solid separates from a mixture that was clear "
        "beforehand",
        "Reaction I, because releasing a gas removes material from the solution",
        "Reaction III, because a solid metal appears on the beaker",
        "Reaction I and Reaction III together, because both involve a change of "
        "phase",
        "None of them, because an observation can never distinguish the three "
        "classes"],
      ans=0,
      why="EK 4.7.A.5 makes the production of an insoluble ionic compound from "
          "ions in solution the mark of precipitation. The metal coating in the "
          "third row accompanies an oxidation number change, which EK 4.7.A.2 "
          "makes a redox reaction instead."),

 dict(q="In the reaction 2 Fe2O3 + 3 C → 4 Fe + 3 CO2, taking oxygen as negative "
        "two and requiring the oxidation numbers in a neutral compound to sum to "
        "zero, which species is oxidized?",
      choices=[
        "Carbon, whose oxidation number rises from zero to positive four",
        "Iron, whose oxidation number rises from zero to positive three",
        "Oxygen, whose oxidation number rises from negative two to zero",
        "Carbon, whose oxidation number falls from positive four to zero",
        "Iron, whose oxidation number falls from positive three to zero"],
      ans=0,
      why="EK 4.7.A.4 makes oxidation numbers the way to identify the oxidized "
          "species. Elemental carbon starts at zero and the carbon in carbon "
          "dioxide balances two oxygens at negative two, so it rises; the iron "
          "moves the opposite way."),

 dict(q="Why can a reaction be classified as acid-base even though no substance "
        "in it is called an acid on its label?",
      choices=[
        "Because the classification depends on whether a proton is transferred, "
        "not on what a container says",
        "Because any reaction that produces water is classified as acid-base by "
        "convention",
        "Because a reaction with no solid product and no gas must be acid-base "
        "by elimination",
        "Because all reactions in aqueous solution are acid-base reactions",
        "Because acid-base is the default class for any reaction whose products "
        "are unknown"],
      ans=0,
      why="EK 4.7.A.1 defines the class by the transfer of one or more protons "
          "between chemical species. The definition is about what happens to a "
          "proton, so it applies wherever that transfer occurs."),

 dict(q="A student writes that in the reaction Cu + 2 Ag+ → Cu2+ + 2 Ag, two "
        "electrons leave each copper atom and one electron arrives at each "
        "silver ion. Is this consistent with the framework, and why?",
      choices=[
        "Yes, because electrons pass from the species that is oxidized to the "
        "species that is reduced and the totals on each side match",
        "No, because the number of electrons lost by one atom must equal the "
        "number gained by one atom",
        "No, because electrons cannot be transferred between a solid and an ion "
        "in solution",
        "Yes, but only because copper and silver are both metals",
        "No, because the copper is reduced and the silver ions are oxidized"],
      ans=0,
      why="EK 4.7.A.3 has electrons transferred from the species oxidized to the "
          "species reduced. Copper rises from zero to positive two while each "
          "silver falls from positive one to zero, and two silver ions account "
          "for the two electrons one copper atom releases."),

 dict(q="Ammonium sulfate solution is mixed with sodium hydroxide solution. Which "
        "prediction about a precipitate is best supported by the framework?",
      choices=[
        "No precipitate of an ammonium or sodium compound can form, because all "
        "such salts are soluble",
        "Ammonium hydroxide will precipitate, because it is the pairing of the "
        "two ions not already combined",
        "Sodium sulfate will precipitate, because sulfate carries a charge of "
        "negative two",
        "Both possible new compounds will precipitate, because two ionic "
        "solutions were mixed",
        "A precipitate is certain, because every mixture of ionic solutions "
        "produces one"],
      ans=0,
      why="EK 4.7.A.5 states that all sodium, potassium, ammonium and nitrate "
          "salts are soluble in water. Both new pairings available here are an "
          "ammonium salt or a sodium salt, so that statement rules each of them "
          "out as a solid."),

 dict(q="Hydrogen gas burns in oxygen to give water. Which classification and "
        "justification are correct?",
      choices=[
        "Oxidation-reduction, because hydrogen rises from zero to positive one "
        "and oxygen falls from zero to negative two",
        "Acid-base, because hydrogen ions are transferred to oxygen atoms",
        "Precipitation, because liquid water separates from the gas mixture",
        "Oxidation-reduction, because hydrogen falls from positive one to zero "
        "as the water forms",
        "No class applies, because both reactants are elements rather than "
        "compounds"],
      ans=0,
      why="EK 4.7.A.2 makes combustion a subclass of oxidation-reduction and "
          "makes changes in oxidation number the indicator of electron "
          "transfer. Both elements start uncombined at zero and end with "
          "opposite signs in water."),

 dict(q="Which single question is most useful for deciding whether a reaction "
        "belongs to the oxidation-reduction class?",
      choices=[
        "Does any element have a different oxidation number in the products "
        "than in the reactants?",
        "Does the reaction release energy to its surroundings?",
        "Are all of the reactants dissolved in water at the start?",
        "Does the reaction produce more moles of product than of reactant?",
        "Is one of the reactants a compound containing hydrogen?"],
      ans=0,
      why="EK 4.7.A.2 states that redox reactions involve transfer of one or "
          "more electrons between chemical species, as indicated by changes in "
          "oxidation numbers, and EK 4.7.A.4 makes assigning those numbers an "
          "effective way to identify what was oxidized and reduced."),

 dict(q="A reaction mixture releases a gas, its temperature rises, and no element "
        "changes oxidation number. Which classification is best supported?",
      choices=[
        "Acid-base, since a proton transfer can release a gas without any "
        "element changing oxidation number",
        "Oxidation-reduction, since the release of energy shows that electrons "
        "have moved",
        "Precipitation, since a gas leaving the mixture is a phase separating "
        "from solution",
        "Combustion, since a gas is produced and energy is released",
        "None of the three, since a reaction releasing a gas belongs to a fourth "
        "class"],
      ans=0,
      why="EK 4.7.A.2 makes a change in oxidation number the indicator of "
          "electron transfer, so its absence rules the redox class out, and EK "
          "4.7.A.5 requires an insoluble solid for precipitation. EK 4.7.A.1's "
          "proton transfer is what remains, and carbonates release carbon "
          "dioxide on receiving protons."),

 dict(q="Two students classify the reaction of solid copper(II) oxide with "
        "sulfuric acid, which gives copper(II) sulfate solution and water. One "
        "calls it acid-base and the other calls it oxidation-reduction. Who is "
        "right, and why?",
      choices=[
        "The first, because protons move from the acid to the oxide ion while "
        "copper stays at positive two throughout",
        "The second, because a solid is converted into dissolved ions, which "
        "requires electron transfer",
        "The second, because copper falls from positive two to zero as the solid "
        "dissolves",
        "The first, because any reaction involving a metal oxide is classified "
        "as acid-base by convention",
        "Neither, because the reaction produces a solution rather than a solid "
        "or a gas"],
      ans=0,
      why="EK 4.7.A.1 defines acid-base by proton transfer and EK 4.7.A.2 "
          "requires a change in oxidation number for redox. The copper is "
          "positive two on both sides and the oxide ion accepts protons to "
          "become water, so only protons have moved."),
]
