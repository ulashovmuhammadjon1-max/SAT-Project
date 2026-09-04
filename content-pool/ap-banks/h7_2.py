# AP CHEMISTRY 7.2 Direction of Reversible Reactions
# CED effective Fall 2024, Unit 7 Equilibrium.
# Learning objective 7.2.A: explain the relationship between the direction in which a
# reversible reaction proceeds and the relative rates of the forward and reverse
# reactions. Suggested skill 4.D, explain the degree to which a model or representation
# describes the connection between particulate-level properties and macroscopic
# properties.
#
# Essential knowledge relied on, in the framework's own words -- this topic has exactly
# one statement, and every key below is one of its three clauses:
#   7.2.A.1  If the rate of the forward reaction is greater than the reverse reaction,
#            then there is a net conversion of reactants to products. If the rate of the
#            reverse reaction is greater than that of the forward reaction, then there is
#            a net conversion of products to reactants. An equilibrium state is reached
#            when these rates are equal.
#
# SCOPE, and it is what keeps this topic from being a second copy of 7.1. 7.1 owns the
# ESTABLISHED equilibrium -- that no observable change occurs, that both species are
# present, that the state is dynamic -- and asks a rate table only when equilibrium is
# first reached. Every item below is about the UNEQUAL case: which way the composition is
# moving while the two rates differ, and what a measured composition says about which rate
# is larger. 7.7 and 7.10 own the argument from Q against K; no item here names either,
# and verify_h7_2.py asserts that.
#
# THE MISCONCEPTION. "Net conversion of reactants to products" does not mean the reverse
# reaction has stopped; EK 7.1.A.3 has both processes running throughout. Items 7, 18 and
# 24 are built on that, and every rate table below carries a nonzero reverse rate wherever
# any product is present.
#
# THE FIGURE PROBLEM. Rate against time is a graph in the framework and this bank cannot
# show one, so every set of readings is a table. No stem says "shown" or "the graph".
#
# ARITHMETIC. Every direction of net conversion, and every comparison of two rates, is
# recomputed in verify_h7_2.py from the table alone.
#
# NOTATION. export_units.py does not typeset Chemistry; a reaction arrow is written as the
# word "to" so no glyph is left outside a math span.
TOPIC = ("7.2", "Direction of Reversible Reactions", 7)

_T_VESSELS = dict(
    headers=["Vessel", "Rate of the forward reaction (M per s)",
             "Rate of the reverse reaction (M per s)"],
    rows=[["1", "0.060", "0.020"],
          ["2", "0.015", "0.045"],
          ["3", "0.030", "0.030"],
          ["4", "0.048", "0.044"]])

_T_FROM_REACTANTS = dict(
    headers=["Time (s)", "Rate of the forward reaction (M per s)",
             "Rate of the reverse reaction (M per s)"],
    rows=[["0", "0.100", "0"],
          ["20", "0.070", "0.030"],
          ["40", "0.055", "0.045"],
          ["60", "0.050", "0.050"],
          ["80", "0.050", "0.050"]])

_T_FROM_PRODUCTS = dict(
    headers=["Time (s)", "Rate of the forward reaction (M per s)",
             "Rate of the reverse reaction (M per s)"],
    rows=[["0", "0", "0.090"],
          ["15", "0.030", "0.060"],
          ["30", "0.042", "0.048"],
          ["45", "0.045", "0.045"]])

_T_CONC = dict(
    headers=["Time (s)", "[R] (M)", "[P] (M)"],
    rows=[["0", "0.200", "0.400"],
          ["30", "0.240", "0.360"],
          ["60", "0.260", "0.340"],
          ["90", "0.260", "0.340"]])

QUESTIONS = [

 dict(q="In a reversible reaction, the rate of the forward reaction is greater than the "
        "rate of the reverse reaction. What is happening to the composition of the "
        "mixture?",
      choices=[
        "There is a net conversion of reactants to products",
        "There is a net conversion of products to reactants",
        "The composition is unchanging, since both reactions are occurring",
        "The reactants are consumed and no product forms until they are gone",
        "The composition changes only if the forward rate is at least twice the reverse "
        "rate"],
      ans=0,
      why="EK 7.2.A.1 states that if the rate of the forward reaction is greater than the "
          "reverse reaction, then there is a net conversion of reactants to products. No "
          "threshold ratio appears in the statement; any excess of one rate over the other "
          "produces net conversion in that direction."),

 dict(q="In a second vessel the rate of the reverse reaction is greater than the rate of "
        "the forward reaction. Which way is the composition moving?",
      choices=[
        "Products are being converted to reactants on balance",
        "Reactants are being converted to products on balance",
        "Neither, because a reverse reaction cannot outrun a forward reaction",
        "Neither, because the vessel must already be at equilibrium",
        "Products are being converted to reactants only until the two rates cross"],
      ans=0,
      why="EK 7.2.A.1 states that if the rate of the reverse reaction is greater than that "
          "of the forward reaction, then there is a net conversion of products to "
          "reactants. Nothing in the framework privileges the forward direction, and a "
          "vessel with unequal rates is by the same statement not at equilibrium."),

 dict(q="According to the framework, what condition on the two rates defines the "
        "equilibrium state?",
      choices=[
        "The forward and reverse rates are equal",
        "The forward and reverse rates are both zero",
        "The forward rate is at its minimum value",
        "The forward rate exceeds the reverse rate by the smallest measurable amount",
        "The reactant and product concentrations are equal"],
      ans=0,
      why="EK 7.2.A.1 ends by saying an equilibrium state is reached when these rates are "
          "equal. Rates of zero would describe a system in which nothing occurs, and the "
          "framework says nothing here about the concentrations matching each other."),

 dict(q="The table reports the two rates measured in four vessels holding the same "
        "reversible reaction. In which vessel is there a net conversion of reactants to "
        "products at the largest rate difference?",
      table=_T_VESSELS,
      choices=["Vessel 1", "Vessel 2", "Vessel 3", "Vessel 4",
               "All four vessels show the same difference"],
      ans=0,
      why="EK 7.2.A.1 makes net conversion of reactants to products the case in which the "
          "forward rate is the greater, so subtracting the tabulated reverse rate from the "
          "tabulated forward rate in each vessel and taking the largest positive difference "
          "identifies it. One vessel's difference is negative, which is the opposite "
          "direction."),

 dict(q="Using the same table of four vessels, in which vessel is there a net conversion "
        "of products to reactants?",
      table=_T_VESSELS,
      choices=["Vessel 2", "Vessel 1", "Vessel 3", "Vessel 4", "No vessel shows this"],
      ans=0,
      why="EK 7.2.A.1 makes net conversion of products to reactants the case in which the "
          "reverse rate is the greater, and exactly one of the tabulated vessels has a "
          "reverse rate above its forward rate."),

 dict(q="Using the same table of four vessels, which vessel has reached an equilibrium "
        "state?",
      table=_T_VESSELS,
      choices=["Vessel 3", "Vessel 1", "Vessel 2", "Vessel 4",
               "None of the four, since some conversion is occurring in each"],
      ans=0,
      why="EK 7.2.A.1 says an equilibrium state is reached when the two rates are equal, "
          "and exactly one tabulated vessel has identical entries in the two rate columns. "
          "A vessel whose rates are merely close is still converting on balance."),

 dict(q="A student looking at the same table says that vessel 1 cannot be running its "
        "reverse reaction at all, because reactants are being converted to products there. "
        "What is wrong with this claim?",
      table=_T_VESSELS,
      choices=[
        "The tabulated reverse rate for that vessel is greater than zero, so the reverse "
        "reaction is occurring",
        "Nothing is wrong, because a net conversion in one direction excludes the other",
        "The claim is wrong because the forward reaction is the one that has stopped",
        "The claim is wrong only because the two rates in that vessel are equal",
        "The reverse rate cannot be measured while a net conversion is occurring"],
      ans=0,
      why="EK 7.2.A.1 speaks of a NET conversion, which is the excess of one rate over the "
          "other rather than the absence of the smaller one, and the table reports a "
          "nonzero rate in both columns for that vessel. EK 7.1.A.3 makes both processes "
          "continue in any case."),

 dict(q="Using the same table of four vessels, which vessel is closest to reaching an "
        "equilibrium state without having got there?",
      table=_T_VESSELS,
      choices=["Vessel 4", "Vessel 1", "Vessel 2", "Vessel 3",
               "Vessels 1 and 2 are equally close"],
      ans=0,
      why="EK 7.2.A.1 makes equality of the two rates the equilibrium condition, so the "
          "vessel with the smallest nonzero gap between the tabulated rates is the closest "
          "to it. The vessel whose rates already agree has reached equilibrium rather than "
          "being close to it, and the two remaining gaps are larger and unequal."),

 dict(q="The table reports the two rates at intervals in a vessel charged with reactants "
        "only. What is the reverse rate at the moment of mixing, and why?",
      table=_T_FROM_REACTANTS,
      choices=[
        "Zero, because no product is present yet for the reverse reaction to consume",
        "Zero, because the reverse reaction begins only after the forward reaction ends",
        "Equal to the forward rate, because the two rates are always equal",
        "At its maximum, because the reverse reaction is fastest at the start",
        "Unmeasurable, because rates cannot be found at the instant of mixing"],
      ans=0,
      why="The tabulated reverse rate at the first reading is zero, and EK 7.2.A.1's whole "
          "comparison is between two processes, of which the reverse one has nothing to act "
          "on until product has formed. The framework never makes the two rates equal "
          "except at equilibrium."),

 dict(q="Using the same table for the vessel charged with reactants only, in which "
        "direction is the net conversion occurring during the first twenty seconds?",
      table=_T_FROM_REACTANTS,
      choices=[
        "Reactants to products, because the tabulated forward rate is the greater",
        "Products to reactants, because the tabulated reverse rate is rising",
        "Neither direction, because the system is already at equilibrium",
        "Products to reactants, because the forward rate is falling",
        "The direction alternates from moment to moment"],
      ans=0,
      why="EK 7.2.A.1 makes the direction of net conversion follow from which rate is "
          "greater, and over that interval the tabulated forward rate is above the reverse "
          "one at every reading. A rate that is rising or falling is not the same as a rate "
          "that is larger."),

 dict(q="Using the same table for the vessel charged with reactants only, at which reading "
        "does net conversion cease?",
      table=_T_FROM_REACTANTS,
      choices=["60 seconds", "20 seconds", "40 seconds", "80 seconds",
               "Net conversion never ceases in a reversible reaction"],
      ans=0,
      why="EK 7.2.A.1 says an equilibrium state is reached when the two rates are equal, "
          "and equal rates mean neither direction outruns the other. The first tabulated "
          "reading at which the two entries agree is where net conversion ends; the "
          "readings before it still show a gap."),

 dict(q="The table reports rates in a vessel charged with PRODUCTS only. In which "
        "direction is the net conversion occurring at the moment of mixing?",
      table=_T_FROM_PRODUCTS,
      choices=[
        "Products to reactants, because only the reverse reaction has anything to consume",
        "Reactants to products, because a reaction always runs in the forward direction",
        "Neither, because a reaction charged with products is already at equilibrium",
        "Products to reactants, and this continues until all the product is gone",
        "The direction cannot be found without the balanced equation"],
      ans=0,
      why="EK 7.2.A.1 makes the greater rate set the direction, and the table reports a "
          "forward rate of zero against a nonzero reverse rate at the first reading. The "
          "conversion stops when the two rates become equal, which the later readings show "
          "happening with product still present."),

 dict(q="Using the same table for the vessel charged with products only, what happens to "
        "the forward rate as time passes?",
      table=_T_FROM_PRODUCTS,
      choices=[
        "It rises from zero and levels off once it matches the reverse rate",
        "It stays at zero, because no reactant was placed in the vessel",
        "It rises without limit, because reactant keeps accumulating",
        "It falls, because the reverse reaction consumes the product",
        "It rises and then falls back to zero"],
      ans=0,
      why="The tabulated forward rate climbs from zero and stops changing at the reading "
          "where the two columns agree, which EK 7.2.A.1 identifies as the equilibrium "
          "state. Reactant is being produced by the reverse reaction, so the forward rate "
          "cannot stay at zero, and it stops rising rather than growing without limit."),

 dict(q="The table reports concentrations measured at intervals in a vessel in which R "
        "and P interconvert. Which rate was the greater during the first thirty seconds?",
      table=_T_CONC,
      choices=[
        "The reverse rate, because the tabulated concentration of P fell while that of R "
        "rose",
        "The forward rate, because the tabulated concentration of R rose",
        "The forward rate, because a reaction proceeds forward unless it is stopped",
        "Neither, because the two concentrations changed by the same amount",
        "The comparison cannot be made from concentrations alone"],
      ans=0,
      why="EK 7.2.A.1 links the direction of net conversion to which rate is greater, so a "
          "measured composition moving from product toward reactant means the reverse rate "
          "was the larger. The two concentrations do change by the same amount here, which "
          "is the stoichiometry rather than a sign that neither rate led."),

 dict(q="Using the same table of concentrations, at which reading has the system reached "
        "an equilibrium state?",
      table=_T_CONC,
      choices=["60 seconds", "30 seconds", "90 seconds", "At the very first reading",
               "The system is at equilibrium throughout, since both species are present"],
      ans=0,
      why="EK 7.2.A.1 makes equal rates the equilibrium condition, and equal rates leave "
          "the composition unchanging. The first tabulated reading after which neither "
          "concentration changes again is the one; earlier readings are still moving, and "
          "the presence of both species proves nothing on its own."),

 dict(q="A vessel holds a reversible reaction whose forward rate is measured as twice the "
        "reverse rate. Is the vessel at equilibrium?",
      choices=[
        "No, because equilibrium requires the two rates to be equal",
        "Yes, because both reactions are occurring at measurable rates",
        "Yes, because a fixed ratio between the rates is what equilibrium means",
        "No, because equilibrium requires both rates to fall to zero",
        "It depends on whether the concentrations are also in a two-to-one ratio"],
      ans=0,
      why="EK 7.2.A.1 says an equilibrium state is reached when these rates are EQUAL. A "
          "forward rate twice the reverse rate is the case the same statement assigns to "
          "net conversion of reactants to products, and the framework nowhere makes the "
          "rates fall to zero."),

 dict(q="Can a system be at equilibrium while the reactant concentration is much larger "
        "than the product concentration?",
      choices=[
        "Yes, because the equilibrium condition is on the two RATES, not on the two "
        "concentrations",
        "No, because equilibrium requires the concentrations to be equal",
        "No, because a large reactant concentration always makes the forward rate the "
        "greater",
        "Yes, but only if the reaction has a one-to-one stoichiometry",
        "Yes, but only while the system is still approaching equilibrium"],
      ans=0,
      why="EK 7.2.A.1 states the equilibrium condition entirely in terms of the forward and "
          "reverse rates being equal, and says nothing at all about the concentrations. EK "
          "7.1.A.2 requires only that both species be present and that their amounts stay "
          "constant."),

 dict(q="A student writes that during a net conversion of reactants to products, the "
        "reverse reaction does not occur. How should this be corrected?",
      choices=[
        "The reverse reaction does occur; it is simply slower than the forward reaction",
        "It should not be corrected, because a net conversion means only one reaction runs",
        "The reverse reaction occurs only after the forward reaction has finished",
        "The forward reaction is the one that does not occur during that period",
        "Both reactions stop during a net conversion and restart at equilibrium"],
      ans=0,
      why="EK 7.2.A.1 speaks of the forward rate being GREATER than the reverse rate, which "
          "presupposes that both are running, and EK 7.1.A.3 has both processes continuing "
          "throughout. A net conversion is the difference between two ongoing processes."),

 dict(q="A vessel is charged with reactants only. Describe how the two rates change as the "
        "system approaches equilibrium.",
      choices=[
        "The forward rate falls and the reverse rate rises until they meet",
        "The forward rate rises and the reverse rate falls until they meet",
        "Both rates fall until they reach zero together",
        "Both rates rise until the reaction is complete",
        "The forward rate falls while the reverse rate stays at zero"],
      ans=0,
      why="With reactants only at the start there is no product for the reverse process to "
          "consume, so its rate begins at zero and climbs as product accumulates while the "
          "forward rate falls. EK 7.2.A.1 says the two meet at the equilibrium state, which "
          "is where the net conversion ends."),

 dict(q="Two vessels hold the same reversible reaction. In vessel J the product "
        "concentration is rising and in vessel L it is falling. What can be said about the "
        "rates in each?",
      choices=[
        "In vessel J the forward rate is the greater; in vessel L the reverse rate is",
        "In vessel J the reverse rate is the greater; in vessel L the forward rate is",
        "In both vessels the forward rate is the greater, since product is present in both",
        "In both vessels the rates are equal, since both are sealed",
        "Nothing can be said, because the rates depend on the temperature"],
      ans=0,
      why="EK 7.2.A.1 ties a net conversion of reactants to products to a larger forward "
          "rate and a net conversion of products to reactants to a larger reverse rate. A "
          "rising product concentration is the first case and a falling one is the second."),

 dict(q="Which measurement on its own would show that a reversible reaction in a sealed "
        "flask still has a net conversion occurring?",
      choices=[
        "The concentration of one species measured at two times, showing a change",
        "The concentration of one species measured once, showing a nonzero value",
        "The temperature of the flask measured at two times, showing no change",
        "The total mass of the sealed flask measured at two times",
        "The presence of both reactant and product in a single sample"],
      ans=0,
      why="A composition that is still changing is exactly what EK 7.2.A.1's unequal rates "
          "produce, and equal rates would leave it fixed. A single reading, the mass of a "
          "sealed flask, and the presence of both species are all consistent with either "
          "case."),

 dict(q="In a vessel the reverse rate exceeds the forward rate. What happens to the "
        "reactant concentration over the next few minutes?",
      choices=[
        "It rises, because products are being converted to reactants on balance",
        "It falls, because the forward reaction is still occurring",
        "It stays constant, because both reactions are occurring",
        "It rises and then falls back to its starting value",
        "It falls until the two rates become equal"],
      ans=0,
      why="EK 7.2.A.1 assigns a larger reverse rate to a net conversion of products to "
          "reactants, so reactant accumulates. The forward reaction is still occurring, but "
          "the net effect is set by which rate is larger."),

 dict(q="Once the forward and reverse rates have become equal, what is the direction of "
        "net conversion?",
      choices=[
        "There is none, since neither process outruns the other",
        "Reactants to products, since the forward reaction is always favoured",
        "Products to reactants, since the reverse reaction is the more recent",
        "It alternates between the two directions",
        "Reactants to products, but at a rate too small to measure"],
      ans=0,
      why="EK 7.2.A.1 makes the direction of net conversion follow from an inequality "
          "between the rates, so equal rates leave no direction, which is why the same "
          "statement calls that condition the equilibrium state."),

 dict(q="A technician reports that in one flask the forward rate is 0.040 M per s and the "
        "reverse rate is 0.040 M per s. What should be concluded?",
      choices=[
        "The flask has reached an equilibrium state",
        "The flask is converting reactants to products at 0.040 M per s",
        "The flask is converting products to reactants at 0.080 M per s",
        "The measurement must be wrong, since two rates cannot be equal",
        "The flask will reach equilibrium once the rates fall to zero"],
      ans=0,
      why="EK 7.2.A.1 says an equilibrium state is reached when these rates are equal, and "
          "the two reported values agree exactly. Neither the sum nor the individual value "
          "is a net rate of conversion, since the two processes cancel."),

 dict(q="Which observation would indicate a net conversion of products to reactants in a "
        "sealed vessel?",
      choices=[
        "The product concentration falls steadily while the reactant concentration rises",
        "The product concentration is smaller than the reactant concentration",
        "The reverse reaction is observed to occur at all",
        "The product concentration stops changing",
        "Both concentrations fall steadily over time"],
      ans=0,
      why="EK 7.2.A.1 defines the direction of net conversion by which rate is greater, and "
          "a composition moving from product toward reactant is what a greater reverse rate "
          "produces. A concentration that is merely smaller, or that has stopped changing, "
          "reports no direction at all."),

 dict(q="Using the table for the vessel charged with reactants only, by how much does the "
        "forward rate exceed the reverse rate at the twenty second reading?",
      table=_T_FROM_REACTANTS,
      choices=["0.040 M per s", "0.070 M per s", "0.030 M per s", "0.100 M per s",
               "0.010 M per s"],
      ans=0,
      why="Subtracting the tabulated reverse rate from the tabulated forward rate at that "
          "reading gives the excess directly, and EK 7.2.A.1 makes that excess the reason "
          "there is a net conversion of reactants to products at that moment. The two "
          "individual rates are the tabulated values themselves, not the difference."),

 dict(q="Using the table for the vessel charged with products only, what is true of the "
        "gap between the two rates as the readings proceed?",
      table=_T_FROM_PRODUCTS,
      choices=[
        "It narrows at every reading and reaches zero",
        "It widens at every reading",
        "It stays the same at every reading",
        "It narrows and then widens again",
        "It cannot be found, because only one rate is tabulated at the start"],
      ans=0,
      why="Subtracting the two tabulated columns at each reading gives a gap that shrinks "
          "monotonically to zero, which is EK 7.2.A.1's approach to the equilibrium state "
          "where the rates are equal. Both columns are tabulated at every reading, "
          "including the first."),

 dict(q="Why does the framework describe the conversion in an unequal-rate system as a NET "
        "conversion rather than simply a conversion?",
      choices=[
        "Because conversion occurs in both directions and the word names the difference "
        "between them",
        "Because only a fraction of the reactant is ever converted",
        "Because the conversion is too slow to observe directly",
        "Because the word distinguishes a chemical change from a physical one",
        "Because the conversion reverses direction periodically"],
      ans=0,
      why="EK 7.2.A.1 compares two rates and calls the outcome of the comparison a net "
          "conversion, and EK 7.1.A.3 has both processes running at once. The word names "
          "the balance between two ongoing conversions, not a partial or slow one."),

 dict(q="A reversible reaction has been charged with a mixture of reactants and products "
        "and its measured composition does not change over an hour. Which comparison of "
        "rates does this support?",
      choices=[
        "The forward and reverse rates are equal",
        "The forward rate is slightly greater than the reverse rate",
        "The reverse rate is slightly greater than the forward rate",
        "Both rates are zero",
        "No comparison is supported, since composition and rate are unrelated"],
      ans=0,
      why="EK 7.2.A.1 makes an unchanging composition the case in which neither rate "
          "exceeds the other, which is the equilibrium condition it states. Rates of zero "
          "are ruled out by EK 7.1.A.3, which has both processes continuing."),

 dict(q="In a reversible reaction the forward rate is 0.090 M per s and the reverse rate "
        "is 0.030 M per s. Which statement describes the system correctly?",
      choices=[
        "Reactants are being converted to products on balance, and the system is not at "
        "equilibrium",
        "Reactants are being converted to products on balance, and the system is at "
        "equilibrium",
        "Products are being converted to reactants on balance, and the system is not at "
        "equilibrium",
        "The system is at equilibrium because both rates are nonzero",
        "The system is at equilibrium because the rates are in a fixed ratio"],
      ans=0,
      why="EK 7.2.A.1 assigns a greater forward rate to a net conversion of reactants to "
          "products, and reserves the equilibrium state for the case in which the two rates "
          "are equal. Both halves of the statement have to be read together, and unequal "
          "rates settle the second half."),

]
