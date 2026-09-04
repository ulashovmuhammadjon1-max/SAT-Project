# AP CHEMISTRY 8.11 pH and Solubility
# CED effective Fall 2024, Unit 8 Acids and Bases.
# Learning objective 8.11.A: identify the qualitative effect of changes in pH on the
# solubility of a salt. Suggested skill 2.D, make observations or collect data from
# representations of laboratory setups or results, while attending to precision where
# appropriate.
#
# Essential knowledge relied on, in the framework's own words:
#   8.11.A.1  The solubility of a salt is pH sensitive when one of the constituent ions is
#             a weak acid, a weak base, or the hydroxide ion. These effects can be
#             understood qualitatively using Le Chatelier's principle.
#             Exclusion Statement: Computations of solubility as a function of pH will not
#             be assessed on the AP Exam.
#
# Supporting statements used where the framework's own reasoning needs them:
#   EK 7.9.A.1   Le Chatelier's principle predicts the response of a system to stresses
#                such as the addition or removal of a chemical species -- which is the
#                reasoning EK 8.11.A.1 itself points at.
#   EK 7.10.A.2  A change in concentration causes a change in Q only; a change in
#                temperature causes a change in K. This is why a pH change moves the
#                solubility without moving Ksp.
#   EK 7.11.A.1  The dissolution of a salt is a reversible process whose extent is
#                described by Ksp -- the equilibrium EK 8.11.A.1's Le Chatelier argument
#                is applied to.
#   EK 7.12.A.1  The common-ion effect, understood qualitatively using Le Chatelier's
#                principle. It is the reason a hydroxide salt is LESS soluble at high pH.
#   EK 8.2.A.1   The strong acids are HCl, HBr, HI, HClO4, H2SO4 and HNO3. An acid outside
#                that list is a weak acid, which is how a student decides whether a given
#                anion is the conjugate base of a weak acid.
#   EK 8.6.A.1   i. the strong acids have very weak conjugate bases; iv. common weak bases
#                include nitrogenous bases such as ammonia as well as carboxylate ions.
#                Part i is why chloride and nitrate salts are NOT pH sensitive.
#
# THE EXCLUSION IS THE SHAPE OF THIS TOPIC. EK 8.11.A.1's exclusion statement bars
# computations of solubility as a function of pH, and the learning objective asks only for
# the QUALITATIVE effect. So not one item below computes a molar solubility, a Ksp, or a
# pH; verify_h8_11.py asserts that no stem, choice or why asks for one. The arithmetic
# that does appear is the reading of measured laboratory data -- comparing two numbers a
# table already carries -- which is suggested skill 2.D and not a computation of solubility
# from a pH.
#
# SCOPE LEFT BY THE NEIGHBOURS. 7.11 owns Ksp and molar solubility, and 7.12 owns the
# common-ion effect, so no item here computes either. 8.5 owns titration curves and 8.10
# owns buffer capacity; neither appears. Where a hydroxide salt is made less soluble by
# added hydroxide the item says plainly that the same observation is the common-ion effect
# of EK 7.12.A.1, rather than pretending the two topics are unrelated.
#
# THE SWAP THAT MUST NOT SHIP. The whole topic is a DIRECTION -- more soluble or less --
# and writing one backwards is the single likeliest defect. Every keyed choice that states
# a direction states the REASON in the same breath, and verify_h8_11.py predicts the
# direction independently from the species added and the kind of ion involved, then
# requires the anchor to carry both clauses so a half-right key cannot match.
#
# THE FIGURE PROBLEM. This bank carries no images, so no item points at one. Laboratory
# results appear as tables of what was measured or observed.
#
# NOTATION. export_units.py does not typeset Chemistry; formulas stay plain text.
TOPIC = ("8.11", "pH and Solubility", 8)

# Measured molar solubilities, the kind of result suggested skill 2.D asks students to read.
_T_MEASURED = dict(
    headers=["Salt", "Molar solubility at pH 2.0 (M)", "Molar solubility at pH 7.0 (M)"],
    rows=[["Salt Q", "0.045", "0.00030"],
          ["Salt R", "0.000018", "0.000018"],
          ["Salt S", "0.012", "0.00060"],
          ["Salt T", "0.0021", "0.0021"]])

_T_HYDROXIDE = dict(
    headers=["pH of the solution", "Measured molar solubility of the hydroxide salt (M)"],
    rows=[["9.0", "0.010"],
          ["10.0", "0.00010"],
          ["11.0", "0.0000010"]])

_T_ANIONS = dict(
    headers=["Salt", "Anion released when the salt dissolves"],
    rows=[["Salt W", "carbonate ion, the conjugate base of a weak acid"],
          ["Salt X", "chloride ion, the very weak conjugate base of a strong acid"],
          ["Salt Y", "hydroxide ion"],
          ["Salt Z", "nitrate ion, the very weak conjugate base of a strong acid"]])

_T_BEAKERS = dict(
    headers=["Beaker", "Contents", "Observation after stirring"],
    rows=[["Beaker 1", "excess solid calcium fluoride in water at pH 7.0",
           "a small amount of solid dissolves"],
          ["Beaker 2", "excess solid calcium fluoride in a solution at pH 2.0",
           "a much larger amount of solid dissolves"],
          ["Beaker 3", "excess solid silver chloride in water at pH 7.0",
           "a very small amount of solid dissolves"],
          ["Beaker 4", "excess solid silver chloride in a solution at pH 2.0",
           "a very small amount of solid dissolves"]])

QUESTIONS = [

 dict(q="According to the course framework, what makes the solubility of a salt sensitive "
        "to the pH of the solution?",
      choices=[
        "One of the ions the salt is made of is a weak acid, a weak base, or the hydroxide "
        "ion",
        "One of the ions the salt is made of is the very weak conjugate base of a strong "
        "acid",
        "The salt contains a metal ion drawn from group I or group II",
        "The salt dissolves by absorbing energy from its surroundings",
        "The salt has a solubility-product constant larger than one"],
      ans=0,
      why="EK 8.11.A.1 states that the solubility of a salt is pH sensitive when one of the "
          "constituent ions is a weak acid, a weak base, or the hydroxide ion. An ion that "
          "is none of those three has no appreciable reaction with hydronium or hydroxide, "
          "so changing the pH does not remove it from the solution."),

 dict(q="In what way does the framework say the effect of pH on the solubility of a salt "
        "can be understood?",
      choices=[
        "Qualitatively, using Le Chatelier's principle",
        "Quantitatively, by computing the molar solubility at each pH",
        "By comparing the solubility-product constants of two different salts",
        "By measuring the enthalpy change of the dissolution",
        "Only by direct experiment, since no general principle applies"],
      ans=0,
      why="EK 8.11.A.1 says these effects can be understood qualitatively using Le "
          "Chatelier's principle, and EK 7.9.A.1 makes that principle the tool for "
          "predicting a system's response to the addition or removal of a species. The "
          "exclusion statement attached to EK 8.11.A.1 rules out the quantitative route."),

 dict(q="Which of the following does the exclusion statement attached to this topic place "
        "outside the scope of the AP Exam?",
      choices=[
        "Computation of the solubility of a salt as a function of pH",
        "Identification of the qualitative effect of a pH change on the solubility of a salt",
        "Identification of which ions a salt releases as it dissolves",
        "Prediction of whether a salt dissolves more readily in acid than in pure water",
        "Comparison of measured solubilities of one salt at two different pH values"],
      ans=0,
      why="The exclusion statement attached to EK 8.11.A.1 says computations of solubility "
          "as a function of pH will not be assessed, while learning objective 8.11.A asks "
          "precisely for the qualitative effect. Reading and comparing measured results is "
          "suggested skill 2.D and stays in scope."),

 dict(q="Excess solid calcium carbonate sits in contact with its saturated solution. Nitric "
        "acid is added, lowering the pH. What is observed, and why?",
      choices=[
        "More of the solid dissolves, because hydronium ion removes carbonate ion from the "
        "solution",
        "Less of the solid dissolves, because hydronium ion removes carbonate ion from the "
        "solution",
        "More of the solid dissolves, because nitrate ion is an ion common to the salt",
        "Less of the solid dissolves, because nitrate ion is an ion common to the salt",
        "Nothing changes, because the solubility-product constant is fixed at a given "
        "temperature"],
      ans=0,
      why="Carbonic acid is not among the strong acids EK 8.2.A.1 lists, so carbonate ion "
          "is the conjugate base of a weak acid and is itself a weak base, which is one of "
          "the three cases EK 8.11.A.1 names. Protonating carbonate lowers its "
          "concentration, and EK 7.9.A.1's principle shifts the dissolution equilibrium to "
          "replace it. Nitrate is an ion of neither the solid nor the equilibrium."),

 dict(q="Why does removing a dissolved anion by protonating it increase the amount of a "
        "salt that dissolves?",
      choices=[
        "Lowering the concentration of a dissolved product shifts the dissolution "
        "equilibrium toward dissolving more solid",
        "Lowering the concentration of a dissolved product raises the solubility-product "
        "constant of the salt",
        "Protonating the anion supplies the energy the lattice needs in order to break apart",
        "The conjugate acid formed is itself a solid, so the solution has more room for the "
        "salt",
        "The protonated anion returns to the crystal and carries more of it into solution"],
      ans=0,
      why="EK 7.11.A.1 makes dissolution a reversible process, and EK 7.9.A.1 says the "
          "removal of a species is a stress the system responds to. Removing one of the "
          "dissolved ions therefore drives more solid into solution, which is the "
          "qualitative Le Chatelier argument EK 8.11.A.1 points at."),

 dict(q="Excess solid magnesium hydroxide is stirred into a solution and hydrochloric acid "
        "is then added. What happens to the amount of solid that dissolves?",
      choices=[
        "It rises, because hydronium ion consumes the hydroxide ion the solid releases",
        "It falls, because hydronium ion consumes the hydroxide ion the solid releases",
        "It rises, because chloride ion is an ion common to magnesium hydroxide",
        "It falls, because chloride ion is an ion common to magnesium hydroxide",
        "It is unchanged, because magnesium ion does not react with hydronium ion"],
      ans=0,
      why="EK 8.11.A.1 names the hydroxide ion as one of the three constituent ions that "
          "make a salt's solubility pH sensitive. Added hydronium ion neutralizes the "
          "hydroxide ion released by the solid, and under EK 7.9.A.1 the dissolution "
          "equilibrium responds to that removal by dissolving more solid. Chloride is not "
          "an ion of this salt."),

 dict(q="Solid sodium hydroxide is added instead to the same magnesium hydroxide mixture, "
        "raising the pH sharply. What happens to the amount of solid that dissolves?",
      choices=[
        "It falls, because the added hydroxide ion is an ion the solid itself releases",
        "It rises, because the added hydroxide ion is an ion the solid itself releases",
        "It falls, because sodium ion precipitates the magnesium ion",
        "It rises, because a more basic solution dissolves more of any solid",
        "It is unchanged, because only an acid can alter a solubility"],
      ans=0,
      why="Raising the pH raises the concentration of hydroxide ion, which EK 8.11.A.1 "
          "names as a constituent ion of this salt. EK 7.12.A.1 makes that the common-ion "
          "effect: a salt is less soluble in a solution already containing one of its own "
          "ions, and the same Le Chatelier reasoning covers both statements."),

 dict(q="Excess solid silver chloride is stirred into water, and the pH is then lowered to "
        "2.0. What is expected?",
      choices=[
        "No appreciable change, because chloride ion is the very weak conjugate base of a "
        "strong acid",
        "A large increase, because chloride ion is the very weak conjugate base of a strong "
        "acid",
        "A large increase, because every salt dissolves more readily in acid",
        "A large decrease, because hydronium ion is an ion common to silver chloride",
        "A large decrease, because silver ion reacts with hydronium ion"],
      ans=0,
      why="EK 8.2.A.1 lists HCl among the strong acids and EK 8.6.A.1 says the strong acids "
          "have very weak conjugate bases, so chloride ion is not a weak base and is not "
          "protonated to any appreciable extent. None of the three cases in EK 8.11.A.1 "
          "applies, so the pH does not move this solubility."),

 dict(q="A sparingly soluble salt releases a cation that is itself a weak acid. Sodium "
        "hydroxide solution is added, raising the pH. What is expected?",
      choices=[
        "More of the solid dissolves, because hydroxide ion removes the cation by "
        "deprotonating it",
        "Less of the solid dissolves, because hydroxide ion removes the cation by "
        "deprotonating it",
        "More of the solid dissolves, because sodium ion is an ion common to the salt",
        "No change at all, because only the anion of a salt can be pH sensitive",
        "No change at all, because a cation cannot act as an acid"],
      ans=0,
      why="EK 8.11.A.1 says the solubility is pH sensitive when one of the CONSTITUENT ions "
          "is a weak acid, a weak base, or the hydroxide ion, and a cation counts. "
          "Deprotonating the cation lowers its concentration, and EK 7.9.A.1's principle "
          "then shifts the dissolution equilibrium toward more dissolving."),

 dict(q="Which of these salts would have a solubility that rises as the pH of the solution "
        "is lowered?",
      choices=[
        "Calcium fluoride, since fluoride ion is the conjugate base of a weak acid",
        "Silver chloride, since chloride ion is the conjugate base of a weak acid",
        "Potassium nitrate, since nitrate ion is the conjugate base of a weak acid",
        "Sodium bromide, since bromide ion is the conjugate base of a weak acid",
        "Potassium iodide, since iodide ion is the conjugate base of a weak acid"],
      ans=0,
      why="EK 8.2.A.1's list of strong acids contains HCl, HBr, HI and HNO3 but not HF, so "
          "fluoride is the only one of these anions that is the conjugate base of a weak "
          "acid. EK 8.11.A.1 then makes that salt, and only that salt, pH sensitive."),

 dict(q="Which of these salts would have a solubility essentially unaffected by a change in "
        "pH?",
      choices=[
        "Silver bromide, whose two ions are neither weak acids nor weak bases",
        "Calcium carbonate, whose anion is the conjugate base of a weak acid",
        "Magnesium hydroxide, whose anion is the hydroxide ion",
        "Calcium fluoride, whose anion is the conjugate base of a weak acid",
        "Iron(III) hydroxide, whose anion is the hydroxide ion"],
      ans=0,
      why="HBr appears in EK 8.2.A.1's list of strong acids, so bromide ion is a very weak "
          "conjugate base under EK 8.6.A.1 and is not protonated appreciably. EK 8.11.A.1's "
          "three cases are a weak acid, a weak base and the hydroxide ion, and none of them "
          "covers this salt, while each of the others is covered by one of them."),

 dict(q="Excess solid calcium fluoride is placed in water and the solution is then "
        "acidified. Which species accounts for the change in how much solid dissolves?",
      choices=[
        "Hydronium ion, which converts fluoride ion into hydrofluoric acid",
        "Hydroxide ion, which converts fluoride ion into hydrofluoric acid",
        "Calcium ion, which is removed from solution as the pH falls",
        "Water, which dissolves more of any solid once acid has been added",
        "Fluoride ion, which is supplied by the acid as a common ion"],
      ans=0,
      why="Hydrofluoric acid is absent from EK 8.2.A.1's list of strong acids, so fluoride "
          "ion is the conjugate base of a weak acid and reacts with hydronium ion. That "
          "removal is the stress EK 7.9.A.1 describes, and EK 8.11.A.1 makes it the reason "
          "this solubility is pH sensitive."),

 dict(q="A sparingly soluble salt of a carboxylate ion is stirred into water. Would its "
        "solubility be pH sensitive?",
      choices=[
        "Yes, because a carboxylate ion is a weak base",
        "No, because a carboxylate ion is a very weak conjugate base",
        "Yes, because a carboxylate ion is the hydroxide ion in disguise",
        "No, because only inorganic ions respond to a change in pH",
        "Yes, because every organic salt is more soluble in base"],
      ans=0,
      why="EK 8.6.A.1 names carboxylate ions among the common weak bases, and EK 8.11.A.1 "
          "makes a salt pH sensitive when one of its constituent ions is a weak base. "
          "Lowering the pH protonates the carboxylate and drives more of the solid into "
          "solution."),

 dict(q="When the pH of a solution is changed at constant temperature, what happens to the "
        "solubility-product constant of a salt sitting in it?",
      choices=[
        "The constant is unchanged, while the amount of salt that dissolves may change",
        "The constant falls, which is why less of the salt dissolves",
        "The constant rises, which is why more of the salt dissolves",
        "The constant and the amount that dissolves both change together",
        "The constant becomes undefined once the solution is no longer neutral"],
      ans=0,
      why="EK 7.10.A.2 says a change in concentration alters Q only, while a change in "
          "temperature is what alters K. A pH change is a concentration change, so under EK "
          "7.11.A.1 the constant describing the extent of dissolution stays put and it is "
          "the position of the equilibrium, and so the amount dissolved, that moves."),

 dict(q="The table reports the molar solubility of four salts measured at two pH values. "
        "For which salts is the solubility pH sensitive?",
      table=_T_MEASURED,
      choices=["Salts Q and S", "Salts R and T", "Salts Q and R", "Salts S and T",
               "All four salts"],
      ans=0,
      why="EK 8.11.A.1 calls a solubility pH sensitive when it responds to a change in pH, "
          "and exactly two of the tabulated salts have different measured solubilities in "
          "the two solutions. The other two read the same at both pH values, which is what "
          "a salt with no weakly acidic or basic ion does."),

 dict(q="Using the same measurements, which salt shows the largest proportional increase on "
        "going from the neutral solution to the acidic one?",
      table=_T_MEASURED,
      choices=["Salt Q", "Salt S", "Salt R", "Salt T",
               "Salts Q and S increase by the same proportion"],
      ans=0,
      why="Dividing each salt's tabulated acidic solubility by its tabulated neutral "
          "solubility gives the factor by which the pH change moved it, and one row gives a "
          "far larger factor than any other. Suggested skill 2.D asks exactly this of "
          "measured laboratory results."),

 dict(q="Using the same measurements, by roughly what factor does the solubility of salt S "
        "rise between the two solutions?",
      table=_T_MEASURED,
      choices=["About 20 times", "About 150 times", "About 75 times", "About 4 times",
               "It does not rise at all"],
      ans=0,
      why="The two tabulated values for that salt differ by a factor a student can read "
          "straight off the table, which is the observation suggested skill 2.D asks for. "
          "EK 8.11.A.1 supplies the reason a factor of this size appears at all: one of the "
          "salt's ions is being removed by the acid."),

 dict(q="Using the same measurements, what do the two readings for salt R suggest about the "
        "ions it releases?",
      table=_T_MEASURED,
      choices=[
        "Neither ion is a weak acid, a weak base, or the hydroxide ion",
        "One ion is a weak base, which the acid protonates",
        "One ion is the hydroxide ion, which the acid neutralizes",
        "One ion is a weak acid, which the acid suppresses",
        "Both ions are weak bases, which cancel each other out"],
      ans=0,
      why="The two tabulated readings for that salt are identical, so lowering the pH "
          "removed neither of its ions. EK 8.11.A.1 makes a solubility pH sensitive exactly "
          "when one constituent ion is a weak acid, a weak base or the hydroxide ion, so a "
          "salt that does not respond has none of the three."),

 dict(q="The table reports the measured molar solubility of one hydroxide salt in three "
        "solutions. What does the trend show?",
      table=_T_HYDROXIDE,
      choices=[
        "The solubility falls as the pH rises",
        "The solubility rises as the pH rises",
        "The solubility is unchanged across the three solutions",
        "The solubility rises and then falls as the pH rises",
        "The solubility falls and then rises as the pH rises"],
      ans=0,
      why="Reading the tabulated pairs in order of increasing pH shows each measured "
          "solubility smaller than the one before it. EK 8.11.A.1 names the hydroxide ion "
          "as a constituent ion that makes a solubility pH sensitive, and EK 7.12.A.1 gives "
          "the direction: more of a salt's own ion in solution means less of it dissolves."),

 dict(q="Using the same three solutions, in which one does the greatest amount of the "
        "hydroxide salt dissolve?",
      table=_T_HYDROXIDE,
      choices=["The least basic of the three solutions", "The most basic of the three "
               "solutions", "The solution of intermediate pH", "All three dissolve equal "
               "amounts", "It cannot be told from measurements of this kind"],
      ans=0,
      why="The largest tabulated solubility sits beside the lowest tabulated pH. That is "
          "what EK 8.11.A.1 predicts for a salt releasing hydroxide ion, since the solution "
          "with the least hydroxide already in it is the one that can accept the most from "
          "the solid."),

 dict(q="What accounts for the trend in the three measured solubilities of the hydroxide "
        "salt?",
      table=_T_HYDROXIDE,
      choices=[
        "Raising the pH adds an ion the solid itself releases, so less of the solid can "
        "dissolve",
        "Raising the pH adds an ion the solid itself releases, so more of the solid can "
        "dissolve",
        "Raising the pH lowers the solubility-product constant of the salt",
        "Raising the pH converts the metal ion into a soluble acid",
        "Raising the pH cools the solution, which reduces every solubility"],
      ans=0,
      why="EK 8.11.A.1 makes a hydroxide salt pH sensitive because hydroxide is one of its "
          "constituent ions, and EK 7.12.A.1 gives the common-ion argument in Le "
          "Chatelier's terms. EK 7.10.A.2 rules out any change in the constant itself, "
          "since only the temperature moves that."),

 dict(q="The table names the anion each of four salts releases. Which salts have a "
        "solubility the framework calls pH sensitive?",
      table=_T_ANIONS,
      choices=["Salts W and Y", "Salts X and Z", "Salts W and X", "Salts Y and Z",
               "All four of them"],
      ans=0,
      why="EK 8.11.A.1's three cases are a weak acid, a weak base and the hydroxide ion. "
          "Exactly two of the tabulated anions fall under one of them, the conjugate base "
          "of a weak acid being itself a weak base. The other two are described as very "
          "weak conjugate bases, which EK 8.6.A.1 attaches to the strong acids."),

 dict(q="Using the same four salts, which pair would show almost no change in solubility "
        "when the pH is lowered?",
      table=_T_ANIONS,
      choices=["Salts X and Z", "Salts W and Y", "Salts W and Z", "Salts X and Y",
               "No pair, since every salt responds to acid"],
      ans=0,
      why="The two tabulated anions described as very weak conjugate bases of strong acids "
          "are not protonated appreciably, so acid removes neither of them. EK 8.11.A.1 "
          "makes a solubility pH sensitive only in its three named cases, and neither of "
          "these salts falls into one."),

 dict(q="Using the same four salts, which of them would become MORE soluble as the pH is "
        "raised?",
      table=_T_ANIONS,
      choices=[
        "None of them, since none releases an ion that added base could remove",
        "The salt releasing carbonate ion, since base removes carbonate",
        "The salt releasing hydroxide ion, since base removes hydroxide",
        "The two salts releasing very weak conjugate bases",
        "All four of them, since base dissolves any salt"],
      ans=0,
      why="Added hydroxide removes a constituent ion only where that ion is a weak ACID, "
          "which EK 8.11.A.1 lists as its first case, and none of the tabulated anions is "
          "one. For the salt releasing hydroxide ion the added base is a common ion under "
          "EK 7.12.A.1 and reduces the solubility instead."),

 dict(q="The table records what was observed in four beakers. Which pair of beakers "
        "demonstrates that a solubility is pH sensitive?",
      table=_T_BEAKERS,
      choices=["Beakers 1 and 2", "Beakers 3 and 4", "Beakers 1 and 3", "Beakers 2 and 4",
               "No pair demonstrates it"],
      ans=0,
      why="A demonstration needs two beakers holding the same solid at two different pH "
          "values, and only one such pair shows different observations. EK 8.11.A.1 defines "
          "a pH-sensitive solubility as one that responds to that change, so a pair "
          "recording the same observation twice demonstrates the opposite."),

 dict(q="Using the same four beakers, what accounts for the contrast between the two pairs "
        "of results?",
      table=_T_BEAKERS,
      choices=[
        "Fluoride ion is the conjugate base of a weak acid while chloride ion is not",
        "Chloride ion is the conjugate base of a weak acid while fluoride ion is not",
        "Calcium ion reacts with hydronium ion while silver ion does not",
        "The silver salt was stirred for less time than the calcium salt",
        "The calcium salt has the larger solubility-product constant"],
      ans=0,
      why="EK 8.2.A.1 lists HCl among the strong acids and omits HF, so acid protonates one "
          "of these anions and not the other. EK 8.11.A.1 then predicts a pH-sensitive "
          "solubility for one solid and none for the other, which is the pattern the "
          "observations record."),

 dict(q="A student concludes from one experiment that adding acid increases the solubility "
        "of any salt. What is wrong with the conclusion?",
      choices=[
        "It holds only where a constituent ion is a weak base or the hydroxide ion",
        "It holds only where a constituent ion is the conjugate base of a strong acid",
        "It holds only where the salt has a large solubility-product constant",
        "It is wrong in every case, since acid always reduces a solubility",
        "It is wrong in every case, since a solubility cannot depend on the pH"],
      ans=0,
      why="EK 8.11.A.1 restricts the effect to salts one of whose constituent ions is a "
          "weak acid, a weak base or the hydroxide ion, and EK 8.6.A.1 says the conjugate "
          "bases of the strong acids are very weak. Generalising from one salt to all salts "
          "ignores the condition the framework attaches."),

 dict(q="Limestone is largely calcium carbonate, and rainwater made acidic dissolves it "
        "over long periods. Which reasoning explains that observation?",
      choices=[
        "Hydronium ion protonates carbonate ion, so the dissolution equilibrium shifts "
        "toward dissolving",
        "Hydronium ion is an ion common to calcium carbonate, so the dissolution "
        "equilibrium shifts toward dissolving",
        "Acidic water raises the solubility-product constant of calcium carbonate",
        "Acidic water is at a higher temperature than neutral rainwater",
        "Calcium ion is protonated by the acid and leaves the crystal"],
      ans=0,
      why="Carbonic acid is not among the strong acids EK 8.2.A.1 lists, so carbonate is "
          "the conjugate base of a weak acid and is protonated by hydronium. EK 8.11.A.1 "
          "names that as a pH-sensitive case, and EK 7.9.A.1 supplies the shift once the "
          "carbonate concentration falls."),

 dict(q="A hydroxide salt is made less soluble by the addition of sodium hydroxide. Which "
        "description of that observation is accurate?",
      choices=[
        "It is a pH effect and a common-ion effect at once, since hydroxide is both",
        "It is a pH effect but not a common-ion effect, since sodium is not in the salt",
        "It is a common-ion effect but not a pH effect, since the constant is unchanged",
        "It is neither, since a solubility responds only to temperature",
        "It is a common-ion effect only when the added base is a strong base"],
      ans=0,
      why="EK 8.11.A.1 names the hydroxide ion as a constituent ion that makes a solubility "
          "pH sensitive, and EK 7.12.A.1 defines the common-ion effect as the reduction "
          "produced by an ion already present in the salt. Added hydroxide answers to both "
          "descriptions, and both rest on the same Le Chatelier argument."),

 dict(q="Which pairing of a constituent ion with the pH change that increases a salt's "
        "solubility is correct?",
      choices=[
        "A weakly basic anion with a decrease in pH, and a weakly acidic cation with an "
        "increase in pH",
        "A weakly basic anion with an increase in pH, and a weakly acidic cation with a "
        "decrease in pH",
        "Both a weakly basic anion and a weakly acidic cation with a decrease in pH",
        "Both a weakly basic anion and a weakly acidic cation with an increase in pH",
        "Neither ion, since only the hydroxide ion makes a solubility pH sensitive"],
      ans=0,
      why="EK 8.11.A.1 makes a salt pH sensitive when a constituent ion is a weak acid, a "
          "weak base or the hydroxide ion, and EK 7.9.A.1 supplies the direction in each "
          "case: added hydronium removes a weakly basic anion, while added hydroxide "
          "removes a weakly acidic cation. Each ion is dissolved by the addition it reacts "
          "with, which is the opposite of itself."),

]
