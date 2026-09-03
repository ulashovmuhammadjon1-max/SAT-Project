# AP CHEMISTRY 7.10 Reaction Quotient and Le Chatelier's Principle
# CED effective Fall 2024, Unit 7 Equilibrium.
# Learning objective 7.10.A: explain the relationships between Q, K, and the direction in
# which a reversible reaction will proceed to reach equilibrium. Suggested skill 5.F,
# calculate, estimate, or predict an unknown quantity from known quantities.
#
# Essential knowledge relied on, in the framework's own words:
#   7.10.A.1  A disturbance to a system at equilibrium causes Q to differ from K, thereby
#             taking the system out of equilibrium. The system responds by bringing Q back
#             into agreement with K, thereby establishing a new equilibrium state.
#   7.10.A.2  Some stresses, such as changes in concentration, cause a change in Q only. A
#             change in temperature causes a change in K. In either case, the
#             concentrations or partial pressures redistribute to bring Q and K back into
#             equality.
#
# SCOPE, and it is the reason this topic is not a second copy of 7.9. 7.9 asks which way a
# stressed system moves and what a student would MEASURE. Every item below is about the two
# NUMBERS: what the disturbance does to Q, what it does to K, and which of the two moved.
# The distinction EK 7.10.A.2 draws -- a concentration change moves Q only, a temperature
# change moves K -- is the spine of the topic and is tested from many angles here and from
# none in 7.9. verify_h7_10.py asserts that every rationale in this module names Q or K.
#
# ARITHMETIC. Every quotient below is recomputed in verify_h7_10.py from the stated
# equilibrium concentrations and the stated disturbance alone.
#
# NOTATION. export_units.py does not typeset Chemistry; arrows are written as the word
# "to".
TOPIC = ("7.10", "Reaction Quotient and Le Châtelier’s Principle", 7)

_T_DISTURB = dict(
    headers=["Disturbance", "Does Q change immediately", "Does K change"],
    rows=[["Some reactant is added at constant temperature", "yes", "no"],
          ["Some product is removed at constant temperature", "yes", "no"],
          ["The vessel is warmed", "no", "yes"]])

_T_AFTER = dict(
    headers=["Vessel", "[A] just after the disturbance (M)",
             "[B] just after the disturbance (M)"],
    rows=[["1", "0.50", "0.80"],
          ["2", "0.20", "1.20"],
          ["3", "0.10", "0.40"]])

_T_KTEMP = dict(
    headers=["Temperature in kelvins", "Equilibrium constant"],
    rows=[["300", "4.0"],
          ["400", "6.0"],
          ["500", "10"]])

_T_NO2 = dict(
    headers=["Condition", "[N2O4] (M)", "[NO2] (M)"],
    rows=[["At equilibrium", "0.40", "0.40"],
          ["Just after the volume is halved", "0.80", "0.80"],
          ["Just after the volume is doubled", "0.20", "0.20"]])

QUESTIONS = [

 dict(q="A system at equilibrium is disturbed. According to the course framework, what "
        "has the disturbance done, and what does the system then do?",
      choices=[
        "It has made Q differ from K, and the system responds by bringing Q back into "
        "agreement with K",
        "It has made K differ from Q, and the system responds by returning K to its "
        "former value",
        "It has set both Q and K to new values that can never agree again",
        "It has left Q and K equal, so the system does nothing at all",
        "It has destroyed the equilibrium permanently, so no new equilibrium state is "
        "reached"],
      ans=0,
      why="EK 7.10.A.1 states it in these terms: a disturbance causes Q to differ from K, "
          "taking the system out of equilibrium, and the system responds by bringing Q "
          "back into agreement with K, thereby establishing a new equilibrium state."),

 dict(q="For A(g) to B(g) with an equilibrium constant of 4.0, a vessel sits at "
        "equilibrium with 0.20 M A and 0.80 M B. Enough A is injected to raise its "
        "concentration to 0.50 M at constant temperature. What is Q immediately "
        "afterwards?",
      choices=["Q = 1.6", "Q = 4.0", "Q = 0.63", "Q = 2.5", "Q = 6.3"],
      ans=0,
      why="EK 7.10.A.2 makes a change in concentration a change in Q only. Immediately "
          "after the injection the concentration of B is still 0.80 M, so Q is 0.80 "
          "divided by 0.50, which is 1.6, while K stays at 4.0."),

 dict(q="In that same vessel, immediately after the injection of A, in which direction "
        "does the system proceed and why?",
      choices=[
        "Forward, because Q now lies below K and must rise to meet it",
        "In reverse, because Q now lies below K and must fall to meet it",
        "Forward, because Q now lies above K and must fall to meet it",
        "In reverse, because K has fallen below Q as a result of the injection",
        "Neither way, because the injection changed Q and K by the same factor"],
      ans=0,
      why="EK 7.10.A.1 has the system respond by bringing Q back into agreement with K. "
          "Q is 1.6 and K is 4.0, so Q must rise, and it rises when product terms grow "
          "and reactant terms shrink, which is net forward reaction. EK 7.10.A.2 keeps K "
          "fixed because the temperature did not change."),

 dict(q="Using the same reaction and constant of 4.0, vessel 2 in the table lists the "
        "concentrations just after a disturbance. What is Q there, and what follows?",
      table=_T_AFTER,
      choices=[
        "Q is 6.0, which is above K, so the system proceeds in reverse",
        "Q is 6.0, which is above K, so the system proceeds forward",
        "Q is 0.17, which is below K, so the system proceeds forward",
        "Q is 4.0, so the system is still at equilibrium",
        "Q is 1.4, which is below K, so the system proceeds in reverse"],
      ans=0,
      why="Q is 1.20 divided by 0.20, which is 6.0. EK 7.10.A.1 has the system bring Q "
          "back to K, and lowering Q from 6.0 to 4.0 requires the product term to shrink "
          "and the reactant term to grow, which is net reverse reaction."),

 dict(q="Vessel 3 in the same table is examined for the same reaction with a constant of "
        "4.0. What is true of vessel 3 just after its disturbance?",
      table=_T_AFTER,
      choices=[
        "Q equals K, so the disturbance did not take the system out of equilibrium",
        "Q is above K, so the system must proceed in reverse",
        "Q is below K, so the system must proceed forward",
        "Q cannot be computed until the system has settled again",
        "Q is undefined because both concentrations changed at once"],
      ans=0,
      why="Q is 0.40 divided by 0.10, which is 4.0, exactly the constant. EK 7.10.A.1 "
          "makes a disturbance a matter of whether Q has been made to DIFFER from K, and "
          "here it has not, so no net change follows even though both concentrations "
          "moved."),

 dict(q="Which statement correctly distinguishes the effect of a concentration change "
        "from the effect of a temperature change?",
      choices=[
        "A concentration change moves Q only, while a temperature change moves K",
        "A concentration change moves K only, while a temperature change moves Q",
        "Both kinds of change move K and leave Q untouched",
        "Both kinds of change move Q and leave K untouched",
        "Neither kind of change moves Q or K once equilibrium has been reached"],
      ans=0,
      why="EK 7.10.A.2 states it directly: some stresses, such as changes in "
          "concentration, cause a change in Q only, and a change in temperature causes a "
          "change in K. That asymmetry is why heating a system is a different kind of "
          "disturbance from adding a reagent."),

 dict(q="Using the table of disturbances, which row is the one for which the equilibrium "
        "constant itself takes a new value?",
      table=_T_DISTURB,
      choices=[
        "The row in which the vessel is warmed",
        "The row in which some reactant is added at constant temperature",
        "The row in which some product is removed at constant temperature",
        "Every row, since any disturbance changes the constant",
        "No row, since the constant can never change"],
      ans=0,
      why="EK 7.10.A.2 assigns a change in K to a change in temperature and a change in Q "
          "alone to a change in concentration, which is exactly how the table is filled "
          "in. The constant does change, but only with temperature."),

 dict(q="Using the same table, what do all three rows have in common once the system has "
        "settled again?",
      table=_T_DISTURB,
      choices=[
        "The concentrations have redistributed so that Q and K are equal once more",
        "The concentrations have returned to the values they had before the disturbance",
        "The value of K has returned to the value it had before the disturbance",
        "The value of Q has returned to the value it had before the disturbance",
        "Both Q and K have been left at whatever values the disturbance produced"],
      ans=0,
      why="EK 7.10.A.2 closes with exactly this: in either case, the concentrations or "
          "partial pressures redistribute to bring Q and K back into equality. What Q "
          "settles at is whatever K then is, which after a temperature change is a new "
          "number."),

 dict(q="The table lists the equilibrium constant for one reaction at three temperatures. "
        "A vessel sits at equilibrium at 300 K and is then heated to 500 K. Immediately "
        "after the heating, before any reaction occurs, what is the relationship between "
        "Q and K?",
      table=_T_KTEMP,
      choices=[
        "Q is 4.0 and K is 10, so Q lies below K",
        "Q is 10 and K is 4.0, so Q lies above K",
        "Q and K are both 10, so the system is still at equilibrium",
        "Q and K are both 4.0, so the system is still at equilibrium",
        "Q is 6.0 and K is 10, since Q takes the value at the midpoint temperature"],
      ans=0,
      why="At equilibrium at 300 K, Q equals the tabulated constant there. EK 7.10.A.2 "
          "makes a temperature change a change in K, and the concentrations have not yet "
          "moved, so Q is still the old value while K is the value tabulated at the new "
          "temperature."),

 dict(q="Using that same table, in which direction does the vessel proceed after being "
        "heated from 300 K to 500 K?",
      table=_T_KTEMP,
      choices=[
        "Forward, because Q must rise from 4.0 to the new constant of 10",
        "In reverse, because Q must fall from 10 to the new constant of 4.0",
        "Forward, because K must fall to meet the unchanged Q",
        "In reverse, because heating always favours the reactants",
        "Neither way, because both Q and K changed by the same factor"],
      ans=0,
      why="EK 7.10.A.1 has the system respond by bringing Q back into agreement with K. "
          "The tabulated constant is larger at the higher temperature, so Q must rise, "
          "which requires product terms to grow and reactant terms to shrink."),

 dict(q="A student claims that adding more reactant to a system at equilibrium raises the "
        "value of the equilibrium constant. What is wrong with the claim?",
      choices=[
        "Adding reactant lowers Q and leaves K alone, and the system then reacts to bring "
        "Q back up to K",
        "Adding reactant raises Q and leaves K alone, and the system then reacts to bring "
        "Q back down to K",
        "Adding reactant lowers both Q and K, so the two remain equal throughout",
        "Adding reactant is not a disturbance, so neither Q nor K is affected in any way",
        "Adding reactant raises K and lowers Q, which is why a new equilibrium is reached"],
      ans=0,
      why="EK 7.10.A.2 assigns a concentration change to Q alone; only a temperature "
          "change moves K. A larger reactant term in the denominator makes Q smaller, and "
          "EK 7.10.A.1 then has the system react forward until Q equals the unchanged K."),

 dict(q="For N2O4(g) to 2 NO2(g), a vessel at equilibrium holds the concentrations in the "
        "first row of the table. Using those values, what is the equilibrium constant?",
      table=_T_NO2,
      choices=["K = 0.40", "K = 1.0", "K = 0.16", "K = 2.5", "K = 0.80"],
      ans=0,
      why="The product carries a coefficient of two, so its concentration is squared: the "
          "square of 0.40 divided by 0.40 is 0.40. That value of K is what the later rows "
          "of the table are compared against under EK 7.10.A.1."),

 dict(q="Using the second row of that same table, the volume of the vessel is suddenly "
        "halved, which doubles both concentrations. What is Q immediately afterwards?",
      table=_T_NO2,
      choices=["Q = 0.80", "Q = 0.40", "Q = 1.6", "Q = 0.20", "Q = 1.0"],
      ans=0,
      why="Immediately after the compression the concentrations are those in the second "
          "row, so Q is the square of 0.80 divided by 0.80, which is 0.80. EK 7.10.A.2 "
          "makes this a change in Q only, since the temperature has not changed."),

 dict(q="Following that compression, in which direction does the N2O4 and NO2 system "
        "proceed, and what does that say about the moles of gas?",
      table=_T_NO2,
      choices=[
        "In reverse, because Q rose above K, and the reverse direction has fewer moles of "
        "gas",
        "Forward, because Q rose above K, and the forward direction has fewer moles of gas",
        "In reverse, because Q fell below K, and the reverse direction has more moles of "
        "gas",
        "Forward, because K rose above Q when the vessel was compressed",
        "Neither way, because compression changes Q and K by the same factor"],
      ans=0,
      why="Q rises from 0.40 to 0.80 while K stays at 0.40, so EK 7.10.A.1 has the system "
          "lower Q, which is net reverse reaction. The reverse direction converts two "
          "moles of NO2 into one of N2O4, which is the connection between the arithmetic "
          "of Q and the count of gas particles."),

 dict(q="Using the third row of the same table, the vessel is instead expanded so that "
        "both concentrations are halved. What is Q immediately afterwards, and what "
        "follows?",
      table=_T_NO2,
      choices=[
        "Q is 0.20, below K, so the system proceeds forward",
        "Q is 0.20, below K, so the system proceeds in reverse",
        "Q is 0.10, below K, so the system proceeds forward",
        "Q is 0.40, so the system remains at equilibrium",
        "Q is 0.80, above K, so the system proceeds in reverse"],
      ans=0,
      why="Q is the square of 0.20 divided by 0.20, which is 0.20, against a constant of "
          "0.40. EK 7.10.A.1 then has the system raise Q, which is net forward reaction "
          "toward the side carrying more moles of gas."),

 dict(q="Why does a change in concentration leave the equilibrium constant untouched?",
      choices=[
        "Because the constant is fixed by the temperature, and the framework assigns a "
        "change in it only to a change in temperature",
        "Because the constant is fixed by the initial amounts, which a later addition "
        "cannot alter",
        "Because the constant is an average of every value Q has taken during the "
        "reaction",
        "Because the constant applies only to systems that have never been disturbed",
        "Because the constant is recalculated after each disturbance and happens to come "
        "out the same"],
      ans=0,
      why="EK 7.10.A.2 states that changes in concentration cause a change in Q only, "
          "while a change in temperature causes a change in K. The constant belongs to "
          "the reaction at a temperature, so it is not touched by how much material "
          "happens to be present."),

 dict(q="Immediately after a disturbance, a system has Q greater than K. Which pair of "
        "changes will occur as the system settles?",
      choices=[
        "The product terms fall and the reactant terms rise, until Q has fallen to K",
        "The product terms rise and the reactant terms fall, until Q has risen to K",
        "The product terms and the reactant terms both fall, until K has risen to Q",
        "K falls until it equals the new value of Q, and the concentrations stay put",
        "Nothing changes, because a system cannot have Q greater than K"],
      ans=0,
      why="EK 7.10.A.1 has the system bring Q back into agreement with K, and EK 7.10.A.2 "
          "says the concentrations redistribute to do it. Lowering a quotient whose "
          "numerator is the product term requires that term to shrink and the "
          "denominator to grow."),

 dict(q="A gas-phase system at equilibrium is compressed. For which kind of equation does "
        "the compression leave Q equal to K?",
      choices=[
        "One with the same number of moles of gas on both sides",
        "One with more moles of gas among the products",
        "One with more moles of gas among the reactants",
        "One in which at least one species is a pure solid",
        "One with a very large equilibrium constant"],
      ans=0,
      why="Compressing multiplies every gas concentration by the same factor, and that "
          "factor cancels out of the quotient exactly when the numerator and the "
          "denominator carry the same total power. EK 7.10.A.1 makes the absence of a "
          "difference between Q and K the reason nothing then happens."),

 dict(q="For H2(g) + I2(g) to 2 HI(g) with a constant of 4.0, a vessel sits at "
        "equilibrium with 0.50 M H2, 0.50 M I2 and 1.00 M HI. The volume is halved, "
        "doubling every concentration. What is Q immediately afterwards?",
      choices=["Q = 4.0", "Q = 8.0", "Q = 2.0", "Q = 16", "Q = 1.0"],
      ans=0,
      why="Doubling every concentration gives 1.00, 1.00 and 2.00, so Q is the square of "
          "2.00 divided by the product of 1.00 and 1.00, which is 4.0. The doubling "
          "cancels because both sides carry two moles of gas, so Q has not been made to "
          "differ from K at all."),

 dict(q="A vessel at equilibrium is cooled, and the equilibrium constant for the reaction "
        "is larger at the lower temperature. Which sequence describes what happens?",
      choices=[
        "K rises above the unchanged Q, and the system reacts forward until Q has risen "
        "to the new K",
        "Q rises above the unchanged K, and the system reacts in reverse until Q has "
        "fallen to K",
        "K falls below the unchanged Q, and the system reacts in reverse until Q has "
        "fallen to the new K",
        "Both Q and K fall together, so the system is never taken out of equilibrium",
        "Neither Q nor K changes, because cooling only slows the reaction down"],
      ans=0,
      why="EK 7.10.A.2 makes a temperature change a change in K, with the concentrations "
          "and therefore Q momentarily unchanged. If the new K exceeds Q, EK 7.10.A.1 has "
          "the system raise Q to meet it, which is net forward reaction."),

 dict(q="Which of the following describes the state of a system in the instant after a "
        "reactant has been added at constant temperature?",
      choices=[
        "It is no longer at equilibrium, because Q has been made to differ from K",
        "It is still at equilibrium, because the constant has not changed",
        "It is still at equilibrium, because the addition was made slowly",
        "It has no defined value of Q until the new equilibrium is reached",
        "It has no defined value of K until the new equilibrium is reached"],
      ans=0,
      why="EK 7.10.A.1 identifies being out of equilibrium with Q differing from K, not "
          "with K changing. Q is defined for any set of concentrations, at equilibrium or "
          "not, and K is defined by the temperature."),

 dict(q="For A(g) to B(g) with a constant of 4.0, a vessel at equilibrium holds 0.20 M A "
        "and 0.80 M B. Enough B is removed to bring it to 0.40 M at constant temperature. "
        "What is Q immediately afterwards?",
      choices=["Q = 2.0", "Q = 4.0", "Q = 0.50", "Q = 1.0", "Q = 8.0"],
      ans=0,
      why="Removing product lowers only the numerator, so Q is 0.40 divided by 0.20, "
          "which is 2.0, while EK 7.10.A.2 leaves K at 4.0 because the temperature is "
          "unchanged."),

 dict(q="Continuing from that removal of B, what is the composition doing as the system "
        "settles?",
      choices=[
        "More B is being formed and A is being consumed, which raises Q toward 4.0",
        "More A is being formed and B is being consumed, which lowers Q toward 4.0",
        "Both A and B are being consumed, which leaves Q where the removal put it",
        "K is falling toward the value of Q produced by the removal",
        "Nothing is happening, because removing a species cannot disturb an equilibrium"],
      ans=0,
      why="Q stands at 2.0 against a constant of 4.0, so EK 7.10.A.1 has the system raise "
          "Q, which requires the product term in the numerator to grow and the reactant "
          "term in the denominator to shrink."),

 dict(q="Which single quantity tells a chemist both whether a system is at equilibrium "
        "and, if it is not, which way it will go?",
      choices=[
        "The comparison of Q with K",
        "The value of Q on its own",
        "The value of K on its own",
        "The total pressure inside the vessel",
        "The rate constant of the forward reaction"],
      ans=0,
      why="EK 7.10.A.1 makes the difference between Q and K the definition of being out "
          "of equilibrium and makes the response the closing of that difference. Neither "
          "number alone carries the comparison, and a rate constant describes speed "
          "rather than direction of net change."),

 dict(q="A reaction has a very large equilibrium constant, and a vessel is charged so "
        "that Q is larger still. What happens?",
      choices=[
        "The system proceeds in reverse until Q has fallen to K",
        "The system proceeds forward, since a large constant always favours products",
        "The system does nothing, since both Q and K are large numbers",
        "The constant increases to match the larger value of Q",
        "The system cannot be prepared in that state at all"],
      ans=0,
      why="EK 7.10.A.1 makes the direction depend on the COMPARISON of Q with K rather "
          "than on the size of either. A quotient above the constant is lowered by net "
          "reverse reaction, however large the constant happens to be."),

 dict(q="Two disturbances are applied in turn to one vessel: first some product is added, "
        "and later the vessel is warmed. Which description of the two is correct?",
      choices=[
        "The first moved Q only; the second moved K",
        "The first moved K only; the second moved Q",
        "Both moved Q only, since the vessel was sealed throughout",
        "Both moved K only, since the same reaction was involved",
        "Neither moved Q or K, since the two disturbances cancel"],
      ans=0,
      why="EK 7.10.A.2 assigns a change in concentration to Q alone and a change in "
          "temperature to K. Adding product is the first kind and warming is the second, "
          "so the two disturbances act on different quantities."),

 dict(q="After a disturbance and the response to it, how do the final concentrations "
        "compare with those before the disturbance, when the temperature was never "
        "changed?",
      choices=[
        "They are generally different, but they satisfy the same value of K",
        "They are identical, because the system returns to exactly where it began",
        "They are generally different, and they satisfy a new value of K",
        "They cannot be compared, because Q is undefined between the two states",
        "They are identical only if the disturbance was an addition rather than a removal"],
      ans=0,
      why="EK 7.10.A.1 calls the result a NEW equilibrium state, so the concentrations "
          "need not return to their former values. EK 7.10.A.2 keeps K fixed when the "
          "temperature is fixed, so the new concentrations satisfy the same constant."),

 dict(q="A vessel is at equilibrium and a catalyst is introduced at constant temperature. "
        "What happens to Q and to K?",
      choices=[
        "Neither changes, so no net reaction follows",
        "Q rises while K stays put, so net forward reaction follows",
        "K rises while Q stays put, so net forward reaction follows",
        "Both rise together, so the system stays at equilibrium at new concentrations",
        "Q falls while K stays put, so net reverse reaction follows"],
      ans=0,
      why="EK 7.10.A.2 attaches a change in Q to a change in concentration and a change "
          "in K to a change in temperature. A catalyst changes neither the concentrations "
          "at the moment it is added nor the temperature, so Q and K remain equal and EK "
          "7.10.A.1 gives no disturbance to respond to."),

 dict(q="For A(g) to B(g) with a constant of 4.0, vessel 1 in the table lists the "
        "concentrations just after a disturbance. What is Q there?",
      table=_T_AFTER,
      choices=["Q = 1.6", "Q = 0.63", "Q = 4.0", "Q = 2.5", "Q = 0.40"],
      ans=0,
      why="Q is 0.80 divided by 0.50, which is 1.6. EK 7.10.A.2 makes that a change in Q "
          "produced by a concentration change, with K left at 4.0 by the unchanged "
          "temperature."),

 dict(q="Why is it wrong to say that a system responds to a disturbance by returning K to "
        "its original value?",
      choices=[
        "Because K did not move in the first place unless the temperature changed, and "
        "what the system moves is Q",
        "Because K moves in response to every disturbance and can never be returned",
        "Because K is a rate rather than a ratio, so it is not the sort of thing that "
        "returns",
        "Because K is defined only at the original equilibrium and has no value afterwards",
        "Because K and Q are the same quantity under two different names"],
      ans=0,
      why="EK 7.10.A.2 says a concentration change moves Q only, so there is nothing for "
          "K to return from; and where a temperature change did move K, EK 7.10.A.1 has "
          "the system bring Q to the NEW K rather than restoring the old one."),

]
