# AP CHEMISTRY 8.7 pH and pKa
# CED effective Fall 2024, Unit 8 Acids and Bases.
# Learning objective 8.7.A: explain the relationship between the predominant form of a
# weak acid or base in solution at a given pH and the pKa of the conjugate acid or the pKb
# of the conjugate base. Suggested skill 2.D, make observations or collect data from
# representations of laboratory setups or results, while attending to precision where
# appropriate.
#
# Essential knowledge relied on, in the framework's own words:
#   8.7.A.1  The protonation state of an acid or base (i.e., the relative concentrations of
#            HA and A-) can be predicted by comparing the pH of a solution to the pKa of
#            the acid in that solution. When solution pH < acid pKa, the acid form has a
#            higher concentration than the base form. When solution pH > acid pKa, the base
#            form has a higher concentration than the acid form.
#   8.7.A.2  Acid-base indicators are substances that exhibit different properties (such as
#            color) in their protonated versus deprotonated state, making that property
#            respond to the pH of a solution.
#   8.7.A.3  To ensure accurate results in a titration experiment, acid-base indicators
#            should be selected that have a pKa close to the pH at the equivalence point.
#
# SCOPE, and this module is the other half of a boundary already drawn. h8_5.py (Acid-Base
# Titrations) deliberately contains NO item that selects an indicator, and its verifier
# asserts that, because EK 8.7.A.3 belongs here. So indicator selection is this module's,
# and it is used properly: every equivalence pH is supplied in the stem rather than
# assumed.
#
# THE OTHER BOUNDARY IS WITH 8.9. h8_4.py's header records the four-way split of the
# buffer material: 8.9 owns the ARITHMETIC -- pH from pKa and the ratio, and the ratio from
# pH. This module stops at the QUALITATIVE comparison EK 8.7.A.1 states: which form has the
# higher concentration. No item below takes a logarithm, names the Henderson-Hasselbalch
# equation, or is handed two concentrations; verify_h8_7.py asserts all three.
#
# WHAT THE FRAMEWORK DOES NOT SAY, and the error this module exists to prevent: the
# comparison is pH against pKa, NOT pH against 7. A solution at pH 5 is acidic, and an acid
# of pKa 3 sitting in it is nonetheless mostly DEPROTONATED. Items 16, 22 and 23 turn on
# that, and every tabulated row is chosen so the pH-against-7 rule would give the wrong
# answer at least once.
#
# ARITHMETIC. Every comparison of a pH with a pKa, and every choice of the indicator whose
# pKa lies closest to a stated equivalence pH, is recomputed in verify_h8_7.py from the
# table or the stem alone.
#
# NOTATION. export_units.py does not typeset Chemistry; formulas stay plain text (HA, A-).
TOPIC = ("8.7", "pH and pKa", 8)

_T_ACIDS = dict(
    headers=["Acid", "pKa of the acid", "pH of the solution it is dissolved in"],
    rows=[["HJ", "4.0", "6.0"],
          ["HL", "7.0", "6.0"],
          ["HM", "6.0", "6.0"],
          ["HN", "3.0", "5.0"]])

_T_INDICATORS = dict(
    headers=["Indicator", "pKa of the indicator", "Colour of the protonated form",
             "Colour of the deprotonated form"],
    rows=[["W", "3.5", "red", "yellow"],
          ["X", "5.0", "colourless", "pink"],
          ["Y", "8.9", "colourless", "blue"],
          ["Z", "10.5", "yellow", "green"]])

QUESTIONS = [

 dict(q="What does the framework say can be predicted by comparing the pH of a solution "
        "with the pKa of an acid dissolved in it?",
      choices=[
        "The protonation state of the acid, meaning the relative concentrations of HA and "
        "A-",
        "The total concentration of acid that was dissolved",
        "The rate at which the acid ionizes",
        "The temperature at which the solution was prepared",
        "The volume of base needed to reach the equivalence point"],
      ans=0,
      why="EK 8.7.A.1 states that the protonation state of an acid or base, meaning the "
          "relative concentrations of HA and A-, can be predicted by comparing the pH of a "
          "solution to the pKa of the acid in that solution. The comparison gives which "
          "form dominates, not how much acid there is in total."),

 dict(q="When the pH of a solution is LOWER than the pKa of an acid in it, which form has "
        "the higher concentration?",
      choices=[
        "The acid form",
        "The base form",
        "The two forms are present in equal concentrations",
        "Whichever form was added to the solution first",
        "Neither, since both are fully converted to water"],
      ans=0,
      why="EK 8.7.A.1 states that when solution pH is less than the acid pKa, the acid form "
          "has a higher concentration than the base form. The comparison is with the pKa, "
          "and nothing about the order of addition enters it."),

 dict(q="When the pH of a solution is HIGHER than the pKa of an acid in it, which form has "
        "the higher concentration?",
      choices=[
        "The base form",
        "The acid form",
        "The two forms are present in equal concentrations",
        "Whichever form is more soluble",
        "Neither, since a high pH destroys both forms"],
      ans=0,
      why="EK 8.7.A.1 states that when solution pH is greater than the acid pKa, the base "
          "form has a higher concentration than the acid form. Raising the pH strips "
          "protons from the acid form, which is what shifts the balance toward the "
          "conjugate base."),

 dict(q="What is true when the pH of a solution is exactly equal to the pKa of an acid in "
        "it?",
      choices=[
        "The two members of the conjugate pair are present in equal concentrations",
        "The acid form is present in twice the concentration of the base form",
        "The base form is present in twice the concentration of the acid form",
        "Neither form is present, since they neutralize each other",
        "The solution is neutral, with a pH of 7.00"],
      ans=0,
      why="EK 8.5.A.3 states that pH equals pKa when the conjugate acid and base have equal "
          "concentrations, which is the boundary between the two cases EK 8.7.A.1 "
          "describes. Equality of the pair says nothing about the pH being 7.00."),

 dict(q="The table gives four acids, each dissolved in a solution of the stated pH. For "
        "which acid is the base form the more concentrated?",
      table=_T_ACIDS,
      choices=["Acid HJ", "Acid HL", "Acid HM", "Acid HN",
               "For none of them, since every solution listed is acidic"],
      ans=0,
      why="EK 8.7.A.1 makes the base form the more concentrated when the solution pH is "
          "greater than the acid pKa, and comparing the two tabulated columns row by row "
          "identifies which rows satisfy that. Whether the solution is acidic on the "
          "seven-point scale is a different comparison and settles nothing here."),

 dict(q="Using the same table of four acids, for which acid is the ACID form the more "
        "concentrated?",
      table=_T_ACIDS,
      choices=["Acid HL", "Acid HJ", "Acid HM", "Acid HN",
               "For all four, since each is an acid"],
      ans=0,
      why="EK 8.7.A.1 makes the acid form the more concentrated when the solution pH is "
          "less than the acid pKa, and exactly one tabulated row has its pH below its pKa. "
          "Being an acid does not make the protonated form dominant; the comparison does."),

 dict(q="Using the same table of four acids, for which acid are the two forms present in "
        "equal concentrations?",
      table=_T_ACIDS,
      choices=["Acid HM", "Acid HJ", "Acid HL", "Acid HN",
               "For none of them, since equality is impossible"],
      ans=0,
      why="EK 8.5.A.3 puts equal concentrations of the conjugate pair exactly where pH "
          "equals pKa, which is the boundary between EK 8.7.A.1's two cases. One tabulated "
          "row has the two numbers identical."),

 dict(q="Using the same table of four acids, which acid is dissolved in an ACIDIC solution "
        "and is nonetheless mostly deprotonated?",
      table=_T_ACIDS,
      choices=["Acid HN", "Acid HJ", "Acid HL", "Acid HM",
               "No acid can be mostly deprotonated in an acidic solution"],
      ans=0,
      why="EK 8.7.A.1's comparison is between the pH and the pKa, not between the pH and "
          "seven, so a solution below pH 7 can still sit above a low pKa and leave the base "
          "form dominant. Exactly one tabulated row has a pH below seven and above its own "
          "pKa."),

 dict(q="What does the framework say an acid-base indicator is?",
      choices=[
        "A substance whose properties, such as colour, differ between its protonated and "
        "deprotonated states",
        "A substance that neutralizes any acid it is added to",
        "A substance whose pKa is always exactly 7",
        "A substance that changes the pH of the solution it is added to",
        "A substance that measures the total concentration of acid present"],
      ans=0,
      why="EK 8.7.A.2 states that acid-base indicators are substances that exhibit "
          "different properties, such as colour, in their protonated versus deprotonated "
          "state. An indicator reports the pH rather than setting it or neutralizing "
          "anything."),

 dict(q="Why does the colour of an indicator respond to the pH of a solution?",
      choices=[
        "Because pH fixes which of its two states predominates, and the two states differ "
        "in colour",
        "Because pH changes the wavelength of light the solution transmits directly",
        "Because the indicator reacts with the solvent to form a coloured product",
        "Because the indicator's concentration rises as the pH rises",
        "Because the indicator decomposes at low pH"],
      ans=0,
      why="EK 8.7.A.2 attaches the colour to the protonated versus deprotonated STATE, and "
          "EK 8.7.A.1 makes the pH relative to the indicator's own pKa decide which state "
          "predominates. Putting those two statements together is the whole mechanism."),

 dict(q="According to the framework, how should an indicator be selected for a titration "
        "experiment?",
      choices=[
        "Choose one whose pKa is close to the pH at the equivalence point",
        "Choose one whose pKa is close to the pH of the analyte before titration begins",
        "Choose one whose pKa is as far as possible from the equivalence pH",
        "Choose one whose pKa is exactly 7 in every titration",
        "Choose one whose colour matches the colour of the analyte"],
      ans=0,
      why="EK 8.7.A.3 states that to ensure accurate results in a titration experiment, "
          "acid-base indicators should be selected that have a pKa close to the pH at the "
          "equivalence point. A pKa fixed at seven would only suit the titrations whose "
          "equivalence pH happens to be seven."),

 dict(q="The table lists four indicators. A titration has its equivalence point at pH 9.0. "
        "Which indicator should be chosen?",
      table=_T_INDICATORS,
      choices=["Indicator Y", "Indicator W", "Indicator X", "Indicator Z",
               "Any of the four, since all change colour eventually"],
      ans=0,
      why="EK 8.7.A.3 asks for the indicator whose pKa is closest to the equivalence pH, so "
          "subtracting the stated equivalence pH from each tabulated pKa and taking the "
          "smallest difference in size settles it. An indicator that changes colour at the "
          "wrong pH changes it at the wrong volume of titrant."),

 dict(q="Using the same table of indicators, which should be chosen for a titration whose "
        "equivalence point falls at pH 5.2?",
      table=_T_INDICATORS,
      choices=["Indicator X", "Indicator W", "Indicator Y", "Indicator Z",
               "None of them, since none has a pKa of exactly 5.2"],
      ans=0,
      why="EK 8.7.A.3 asks only that the pKa be CLOSE to the equivalence pH, not equal to "
          "it, and the tabulated pKa values give a single closest match. Requiring exact "
          "equality would leave almost every titration without an indicator."),

 dict(q="Using the same table of indicators, what colour will indicator X show in a "
        "solution at pH 2.0?",
      table=_T_INDICATORS,
      choices=[
        "Its protonated colour, because the solution pH is below its pKa",
        "Its deprotonated colour, because the solution pH is below its pKa",
        "Its protonated colour, because the solution pH is above its pKa",
        "A mixture of both colours, because the pH is far from its pKa",
        "No colour at all, because indicators only work near their pKa"],
      ans=0,
      why="EK 8.7.A.1 makes the acid form the more concentrated when the solution pH is "
          "below the pKa, and EK 8.7.A.2 attaches the colour to that state. The stated pH "
          "is well below this indicator's tabulated pKa."),

 dict(q="Using the same table of indicators, what colour will indicator W show in a "
        "solution at pH 6.0?",
      table=_T_INDICATORS,
      choices=[
        "Yellow, because the solution pH is above its pKa and the deprotonated form "
        "predominates",
        "Red, because the solution pH is above its pKa and the protonated form predominates",
        "Red, because the solution pH is below its pKa",
        "Yellow, because every indicator is yellow above pH 5",
        "A colour between the two, because the pH is exactly at its pKa"],
      ans=0,
      why="The stated pH is above this indicator's tabulated pKa, so EK 8.7.A.1 makes the "
          "deprotonated form the more concentrated, and EK 8.7.A.2 attaches the "
          "corresponding tabulated colour to that state."),

 dict(q="A weak acid with a pKa of 5.0 is dissolved in a solution held at pH 3.0. Which "
        "form predominates?",
      choices=[
        "The protonated form, because the pH is below the pKa",
        "The deprotonated form, because the pH is below the pKa",
        "The protonated form, because the pH is below 7",
        "The deprotonated form, because the solution is acidic",
        "Neither, since the two are always present in equal amounts"],
      ans=0,
      why="EK 8.7.A.1 makes the acid form the more concentrated when the solution pH is "
          "less than the acid pKa. The reason has to be the comparison with the pKa: the "
          "same solution would leave an acid of pKa 2.0 mostly deprotonated, so being below "
          "seven settles nothing on its own."),

 dict(q="A weak acid with a pKa of 4.0 is dissolved in a solution held at pH 6.0. Which "
        "form predominates?",
      choices=[
        "The deprotonated form, because the pH is above the pKa",
        "The protonated form, because the pH is below 7",
        "The protonated form, because the pH is above the pKa",
        "The deprotonated form, because the pH is below 7",
        "The two are equal, because the difference is only two pH units"],
      ans=0,
      why="EK 8.7.A.1 makes the base form the more concentrated when the solution pH is "
          "greater than the acid pKa, and the stated pH exceeds the stated pKa. The "
          "solution is acidic on the seven-point scale, which is exactly why the "
          "seven-point comparison is the wrong one to make."),

 dict(q="Two weak acids, one of pKa 4.0 and one of pKa 8.0, are dissolved in the same "
        "solution at pH 6.0. Which is more fully deprotonated?",
      choices=[
        "The one with the pKa of 4.0, since the solution pH is above it",
        "The one with the pKa of 8.0, since the solution pH is below it",
        "Both are equally deprotonated, since both are in the same solution",
        "Neither is deprotonated, since the solution is acidic",
        "The comparison requires the concentrations of the two acids"],
      ans=0,
      why="EK 8.7.A.1 is applied to each acid separately against the same pH: the acid "
          "whose pKa lies below the solution pH has its base form predominant, while the "
          "one whose pKa lies above it has its acid form predominant. Total concentration "
          "does not enter the comparison."),

 dict(q="Which comparison determines the protonation state of a weak acid in solution?",
      choices=[
        "The solution pH against the pKa of that acid",
        "The solution pH against 7.00",
        "The solution pH against the pOH of the solution",
        "The pKa of the acid against 7.00",
        "The concentration of the acid against the concentration of the solvent"],
      ans=0,
      why="EK 8.7.A.1 states the rule in terms of solution pH against acid pKa in both of "
          "its clauses. Comparing with seven answers a different question -- whether the "
          "solution is acidic or basic -- which does not fix which form of a given acid "
          "predominates."),

 dict(q="A student says that in any solution with a pH below 7, every weak acid present is "
        "mostly protonated. What is wrong with this?",
      choices=[
        "An acid whose pKa is below the solution pH is mostly deprotonated even in an "
        "acidic solution",
        "Nothing is wrong; a pH below 7 does keep every weak acid protonated",
        "The claim fails only for polyprotic acids",
        "The claim fails only at temperatures other than 25 degrees Celsius",
        "The claim fails because weak acids do not have a protonation state"],
      ans=0,
      why="EK 8.7.A.1 makes the comparison one between pH and pKa, so an acid of pKa 3.0 "
          "sitting in a solution at pH 5.0 has its base form predominant even though the "
          "solution is acidic. The tabulated acids in this topic include exactly that "
          "case."),

 dict(q="Why does an indicator chosen with a pKa far from the equivalence pH give an "
        "inaccurate titration result?",
      choices=[
        "Its colour changes at a volume of titrant either well before or well after the "
        "equivalence point",
        "Its colour change is too faint to see at any pH",
        "It reacts with the analyte and consumes some of it entirely",
        "It shifts the equivalence point to its own pKa",
        "It changes colour twice, once at each end of the titration"],
      ans=0,
      why="EK 8.7.A.2 has the colour change track the indicator's own protonation state, "
          "which under EK 8.7.A.1 flips as the pH passes the indicator's pKa. EK 8.7.A.3 "
          "therefore asks for a pKa close to the equivalence pH, so that the flip coincides "
          "with the point the experiment is trying to locate."),

 dict(q="A titration of a weak acid with a strong base has its equivalence point at a "
        "basic pH. What kind of indicator does the framework's rule call for?",
      choices=[
        "One whose pKa is above 7, close to that basic equivalence pH",
        "One whose pKa is below 7, since the analyte was an acid",
        "One whose pKa is exactly 7, since that is neutral",
        "One whose pKa is as far as possible from the equivalence pH",
        "Any indicator, since the equivalence point is reached regardless"],
      ans=0,
      why="EK 8.5.A.4 puts the equivalence point of a weak acid titration on the basic "
          "side, and EK 8.7.A.3 asks for an indicator whose pKa is close to the pH at the "
          "equivalence point. The identity of the analyte enters only through where its "
          "equivalence pH falls."),

 dict(q="A titration of a weak base with a strong acid has its equivalence point at an "
        "acidic pH. What kind of indicator does the framework's rule call for?",
      choices=[
        "One whose pKa is below 7, close to that acidic equivalence pH",
        "One whose pKa is above 7, since the analyte was a base",
        "One whose pKa is exactly 7, since that is neutral",
        "One whose colour change is the most vivid available",
        "One whose pKa matches the pH of the analyte before any titrant is added"],
      ans=0,
      why="EK 8.5.A.4 puts the equivalence point of a weak base titration on the acidic "
          "side, and EK 8.7.A.3 asks for a pKa close to that pH. Vividness of colour is not "
          "the criterion the framework gives."),

 dict(q="Using the table of indicators, which one would be the WORST choice for a titration "
        "whose equivalence point falls at pH 3.5?",
      table=_T_INDICATORS,
      choices=["Indicator Z", "Indicator W", "Indicator X", "Indicator Y",
               "They would all perform equally"],
      ans=0,
      why="EK 8.7.A.3 asks for a pKa close to the equivalence pH, so the worst choice is "
          "the tabulated indicator whose pKa is furthest from the stated value. Subtracting "
          "the stated pH from each tabulated pKa identifies a single largest difference."),

 dict(q="An indicator is placed in a solution whose pH happens to equal the indicator's own "
        "pKa. What is observed?",
      choices=[
        "Both forms are present in comparable amounts, so an intermediate colour appears",
        "Only the protonated colour, since the pH has not yet passed the pKa",
        "Only the deprotonated colour, since the pH has reached the pKa",
        "No colour, since the two forms cancel",
        "The colour of whichever form was added to the bottle"],
      ans=0,
      why="EK 8.5.A.3 makes the two members of a conjugate pair equal in concentration when "
          "pH equals pKa, and EK 8.7.A.2 gives each form its own colour, so both colours "
          "are present at once. That is the middle of the range over which an indicator "
          "changes."),

 dict(q="The framework says an indicator exhibits different PROPERTIES in its two states, "
        "giving colour as an example. What does the word 'such as' allow?",
      choices=[
        "That a property other than colour could serve, as long as it differs between the "
        "two states",
        "That colour is the only property that can ever be used",
        "That the property must be one the student can measure without instruments",
        "That the property must change continuously rather than between two states",
        "That the indicator must be coloured in both of its states"],
      ans=0,
      why="EK 8.7.A.2 says indicators exhibit different properties SUCH AS colour in their "
          "protonated versus deprotonated state, making that property respond to pH. The "
          "example is illustrative, and the requirement is that the property differ between "
          "the states."),

 dict(q="Using the table of indicators, what colour will indicator Z show in a solution at "
        "pH 12.0?",
      table=_T_INDICATORS,
      choices=[
        "Green, because the pH is above its pKa so the deprotonated form predominates",
        "Yellow, because the pH is above its pKa so the protonated form predominates",
        "Yellow, because the pH is below its pKa",
        "Green, because every solution above pH 10 is green",
        "Colourless, because the indicator is destroyed at high pH"],
      ans=0,
      why="The stated pH is above this indicator's tabulated pKa, so EK 8.7.A.1 makes the "
          "deprotonated form the more concentrated and EK 8.7.A.2 attaches the tabulated "
          "deprotonated colour to it."),

 dict(q="How does knowing the pKa of a weak base's conjugate acid help predict the base's "
        "protonation state?",
      choices=[
        "The same comparison applies: the pH of the solution is compared with that pKa",
        "The pKa of the conjugate acid is irrelevant to a base",
        "The base's protonation state depends only on its concentration",
        "The comparison must be made with the pKb rather than with any pH",
        "A base has no protonation state to predict"],
      ans=0,
      why="Learning objective 8.7.A is stated for the predominant form of a weak acid OR "
          "BASE, in relation to the pKa of the conjugate acid or the pKb of the conjugate "
          "base, and EK 8.7.A.1 gives the comparison in terms of solution pH against acid "
          "pKa. The conjugate acid of the base is the acid in that comparison."),

 dict(q="Two indicators are available for a titration whose equivalence point falls at pH "
        "7.0: one with a pKa of 6.8 and one with a pKa of 9.0. Which should be used, and "
        "why?",
      choices=[
        "The one with the pKa of 6.8, because it is the closer to the equivalence pH",
        "The one with the pKa of 9.0, because a higher pKa gives a sharper change",
        "Either one, because both are within a few units of the equivalence pH",
        "The one with the pKa of 9.0, because the equivalence point of a titration is "
        "always basic",
        "Neither, because an indicator must have a pKa of exactly 7.0 for a neutral "
        "equivalence point"],
      ans=0,
      why="EK 8.7.A.3 asks for the indicator whose pKa is closest to the equivalence pH, "
          "and the two stated values differ from 7.0 by 0.2 and 2.0. EK 8.5.A.4 makes a "
          "neutral equivalence pH the case for a strong acid with a strong base, so it is "
          "not true that every equivalence point is basic."),

 dict(q="Summarise what fixes which form of a weak acid predominates in a solution.",
      choices=[
        "Where the solution pH sits relative to that acid's pKa",
        "Where the solution pH sits relative to 7.00",
        "How much of the acid was dissolved",
        "How long the solution has been standing",
        "Whether the acid or the conjugate base was added first"],
      ans=0,
      why="EK 8.7.A.1 gives both of its clauses in terms of solution pH against acid pKa, "
          "and nothing in the statement refers to the amount dissolved, the age of the "
          "solution or the order of addition."),

]
