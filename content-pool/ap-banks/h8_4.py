# AP CHEMISTRY 8.4 Acid-Base Reactions and Buffers
# CED effective Fall 2024, Unit 8 Acids and Bases.
# Learning objective 8.4.A: explain the relationship among the concentrations of major
# species in a mixture of weak and strong acids and bases. Suggested skill 5.F, calculate,
# estimate, or predict an unknown quantity from known quantities by selecting and
# following a logical computational pathway.
#
# Essential knowledge relied on, in the framework's own words:
#   8.4.A.1  When a strong acid and a strong base are mixed, they react quantitatively in a
#            reaction represented by H+(aq) + OH-(aq) to H2O(l). The pH of the resulting
#            solution may be determined from the concentration of excess reagent.
#   8.4.A.2  When a weak acid and a strong base are mixed, they react quantitatively:
#            HA(aq) + OH-(aq) to A-(aq) + H2O(l). If the weak acid is in excess, then a
#            buffer solution is formed, and the pH can be determined from the
#            Henderson-Hasselbalch equation (see 8.9.A.1). If the strong base is in excess,
#            then the pH can be determined from the moles of excess hydroxide ion and the
#            total volume of solution. If they are equimolar, then the (slightly basic) pH
#            can be determined from A-(aq) + H2O(l) to HA(aq) + OH-(aq).
#   8.4.A.3  When a weak base and a strong acid are mixed they react quantitatively:
#            B(aq) + H3O+(aq) to HB+(aq) + H2O(l), with the three cases mirrored: weak base
#            in excess gives a buffer, strong acid in excess gives a pH from the moles of
#            excess hydronium and the total volume, and equimolar gives a (slightly acidic)
#            pH from HB+(aq) + H2O(l) to B(aq) + H3O+(aq).
#   8.4.A.4  When a weak acid and a weak base are mixed, they react to an equilibrium state:
#            HA(aq) + B(aq) to A-(aq) + HB+(aq).
#
# THE FOUR BUFFER TOPICS, PLANNED TOGETHER BEFORE ANY OF THEM WAS WRITTEN. 8.4, 8.8, 8.9
# and 8.10 all speak about buffers and would collide if each were written on its own, so
# each was given one job and told to leave the others alone:
#
#   8.4  (here)  WHICH CASE A MIXTURE IS. Mole counting on the mixture: is the weak
#                component in excess, is the strong one, or are they equimolar, and what
#                are the major species that result. Where a buffer forms, this topic says
#                so and stops -- it never computes a buffer pH.
#   8.8          THE MECHANISM. A buffer holds a large concentration of BOTH members of a
#                pair; the conjugate acid consumes added base and the conjugate base
#                consumes added acid. Net ionic equations, no arithmetic.
#   8.9          THE ARITHMETIC. pH from pKa and the ratio, and the ratio from pH.
#   8.10         CAPACITY. Scaling both concentrations at a fixed ratio, and the asymmetry
#                between capacity for added acid and for added base.
#
# So no item below contains a logarithm of a concentration ratio, and none compares the
# capacity of two buffers. verify_h8_4.py asserts both of those, which is what keeps the
# separation real rather than merely intended.
#
# ARITHMETIC. Every excess-reagent pH is exact: the leftover moles and the total volume are
# chosen so the resulting concentration is a power of ten.
#
# NOTATION. export_units.py does not typeset Chemistry; every span is hand-written.
TOPIC = ("8.4", "Acid-Base Reactions and Buffers", 8)

_T_MIXTURES = dict(
    headers=["Mixture", "Millimoles of weak acid HA", "Millimoles of NaOH added"],
    rows=[["1", "5.00", "2.00"],
          ["2", "5.00", "5.00"],
          ["3", "5.00", "8.00"]])

_T_STRONG = dict(
    headers=["Trial", "Millimoles of HCl", "Millimoles of NaOH",
             "Total volume after mixing (mL)"],
    rows=[["A", "15.0", "5.00", "100.0"],
          ["B", "5.00", "15.0", "100.0"],
          ["C", "9.00", "9.00", "100.0"]])

_T_WEAKBASE = dict(
    headers=["Mixture", "Millimoles of weak base B", "Millimoles of HCl added"],
    rows=[["4", "6.00", "2.00"],
          ["5", "6.00", "6.00"],
          ["6", "6.00", "9.00"]])

QUESTIONS = [

 dict(q="Which equation represents the reaction that occurs when a strong acid and a "
        "strong base are mixed?",
      choices=[
        "H+(aq) + OH-(aq) to H2O(l)",
        "H+(aq) + OH-(aq) to H2(g) + O2(g)",
        "HA(aq) + OH-(aq) to A-(aq) + H2O(l)",
        "B(aq) + H3O+(aq) to HB+(aq) + H2O(l)",
        "HA(aq) + B(aq) to A-(aq) + HB+(aq)"],
      ans=0,
      why="EK 8.4.A.1 gives exactly this equation for a strong acid mixed with a strong "
          "base, and says the two react quantitatively. The other equations belong to EK "
          "8.4.A.2, 8.4.A.3 and 8.4.A.4, which cover a weak component on one side or both."),

 dict(q="After a strong acid and a strong base are mixed and one is left over, how does "
        "the framework say the pH is found?",
      choices=[
        "From the concentration of the reagent present in excess",
        "From the ionization constant of the reagent present in excess",
        "From the average of the two starting pH values",
        "From the total number of moles of both reagents combined",
        "From the volume of the more concentrated of the two solutions"],
      ans=0,
      why="EK 8.4.A.1 states that the pH of the resulting solution may be determined from "
          "the concentration of excess reagent. A strong acid and a strong base have no "
          "ionization constants to use, since both react completely."),

 dict(q="A solution containing 15.0 millimoles of HCl is mixed with one containing 5.00 "
        "millimoles of NaOH, and the total volume is 100.0 mL. What is the pH?",
      choices=["pH = 1.00", "pH = 13.00", "pH = 2.00", "pH = 7.00", "pH = 0.10"],
      ans=0,
      why="The two react one for one under EK 8.4.A.1, leaving 10.0 millimoles of "
          "hydronium in 100.0 mL, which is 0.100 M. The pH is the negative logarithm of "
          "that excess concentration."),

 dict(q="A solution containing 5.00 millimoles of HCl is mixed with one containing 15.0 "
        "millimoles of NaOH, and the total volume is 100.0 mL. What is the pH at 25 "
        "degrees Celsius?",
      choices=["pH = 13.00", "pH = 1.00", "pH = 11.00", "pH = 7.00", "pH = 12.00"],
      ans=0,
      why="EK 8.4.A.1's one-for-one reaction leaves 10.0 millimoles of hydroxide in 100.0 "
          "mL, which is 0.100 M and a pOH of one. EK 8.1.A.3 then gives the pH as the "
          "remainder of fourteen."),

 dict(q="Equal numbers of moles of a strong acid and a strong base are mixed. What is the "
        "pH of the resulting solution at 25 degrees Celsius?",
      choices=[
        "7.00, because neither reagent is left in excess and only water and a spectator "
        "salt remain",
        "7.00, because the salt formed hydrolyses to give a slightly basic solution",
        "Below 7.00, because the acid is always the stronger of the two",
        "Above 7.00, because the conjugate base formed reacts with water",
        "It cannot be determined without the ionization constant of the salt"],
      ans=0,
      why="EK 8.4.A.1 has the two react quantitatively, so equal moles leave no excess "
          "reagent at all. The ions that remain came from a strong acid and a strong base, "
          "so neither reacts further with water; the slightly basic equimolar case belongs "
          "to EK 8.4.A.2, where one component is WEAK."),

 dict(q="Which equation represents the reaction of a weak acid with a strong base?",
      choices=[
        "HA(aq) + OH-(aq) to A-(aq) + H2O(l)",
        "H+(aq) + OH-(aq) to H2O(l)",
        "HA(aq) + H2O(l) to A-(aq) + H3O+(aq)",
        "A-(aq) + H2O(l) to HA(aq) + OH-(aq)",
        "HA(aq) + B(aq) to A-(aq) + HB+(aq)"],
      ans=0,
      why="EK 8.4.A.2 gives this equation and says the two react quantitatively. The third "
          "equation is the weak acid's own ionization from EK 8.3.A.2, and the fourth is "
          "the reaction of its conjugate base at the equimolar point."),

 dict(q="Using the table of weak acid mixtures, which mixture forms a buffer solution?",
      table=_T_MIXTURES,
      choices=["Mixture 1", "Mixture 2", "Mixture 3",
               "Mixtures 2 and 3", "None of the three"],
      ans=0,
      why="EK 8.4.A.2 says a buffer forms when the WEAK ACID is in excess, because both "
          "the un-ionized acid and its conjugate base are then present in quantity. Only "
          "one tabulated mixture has more millimoles of weak acid than of added strong "
          "base."),

 dict(q="Using the same table, which mixture is the equimolar case described by the "
        "framework?",
      table=_T_MIXTURES,
      choices=["Mixture 2", "Mixture 1", "Mixture 3",
               "Mixtures 1 and 3", "None of the three"],
      ans=0,
      why="EK 8.4.A.2 treats the equimolar case separately: the weak acid is exactly "
          "consumed, leaving its conjugate base. Exactly one tabulated mixture has equal "
          "millimoles of the two reagents."),

 dict(q="Using the same table, what are the major species in solution after mixture 2 has "
        "reacted?",
      table=_T_MIXTURES,
      choices=[
        "The conjugate base of the weak acid, together with water and sodium ion",
        "The un-ionized weak acid, together with water and sodium ion",
        "Both the weak acid and its conjugate base in comparable amounts",
        "Excess hydroxide ion, together with the conjugate base",
        "Excess un-ionized weak acid, together with hydronium ion"],
      ans=0,
      why="EK 8.4.A.2's equation converts the weak acid to its conjugate base one for one, "
          "and the tabulated millimoles are equal, so the acid is exactly consumed. "
          "Comparable amounts of both members would be the buffer case, which requires the "
          "acid to be in excess."),

 dict(q="Using the same table, is the solution formed by mixture 2 acidic, neutral or "
        "basic at 25 degrees Celsius?",
      table=_T_MIXTURES,
      choices=[
        "Slightly basic, because the conjugate base reacts with water to give hydroxide "
        "ion",
        "Exactly neutral, because the acid and the base were present in equal amounts",
        "Slightly acidic, because a weak acid was one of the reagents",
        "Strongly basic, because sodium hydroxide is a strong base",
        "Strongly acidic, because the conjugate base is a strong acid"],
      ans=0,
      why="EK 8.4.A.2 says that if the two are equimolar, the slightly basic pH can be "
          "determined from the equilibrium A-(aq) + H2O(l) to HA(aq) + OH-(aq). The "
          "hydroxide has all been consumed by the weak acid, so nothing strongly basic "
          "remains."),

 dict(q="Using the same table, how does the framework say the pH of mixture 3 should be "
        "found?",
      table=_T_MIXTURES,
      choices=[
        "From the moles of excess hydroxide ion and the total volume of solution",
        "From the Henderson-Hasselbalch equation using the ratio of the two species",
        "From the ionization constant of the weak acid and its initial concentration",
        "From the equilibrium of the conjugate base with water alone",
        "From the average of the pH values of the two solutions before mixing"],
      ans=0,
      why="EK 8.4.A.2 gives three cases, and this mixture is the one in which the STRONG "
          "BASE is in excess, for which the framework says the pH can be determined from "
          "the moles of excess hydroxide ion and the total volume of solution."),

 dict(q="Which mixture of a weak acid with a strong base produces a buffer, according to "
        "the framework?",
      choices=[
        "One in which the weak acid is in excess after the reaction",
        "One in which the strong base is in excess after the reaction",
        "One in which the two are present in exactly equal numbers of moles",
        "One in which the strong base is present in twice the moles of the weak acid",
        "Any mixture at all, since a weak acid is always a buffer"],
      ans=0,
      why="EK 8.4.A.2 names the three cases and attaches the buffer to just one of them: "
          "if the weak acid is in excess, then a buffer solution is formed. In the other "
          "two, either excess strong base or the conjugate base alone determines the pH."),

 dict(q="Which equation represents the reaction of a weak base with a strong acid?",
      choices=[
        "B(aq) + H3O+(aq) to HB+(aq) + H2O(l)",
        "HB+(aq) + H2O(l) to B(aq) + H3O+(aq)",
        "B(aq) + H2O(l) to HB+(aq) + OH-(aq)",
        "HA(aq) + OH-(aq) to A-(aq) + H2O(l)",
        "H+(aq) + OH-(aq) to H2O(l)"],
      ans=0,
      why="EK 8.4.A.3 gives this equation for a weak base mixed with a strong acid. The "
          "second equation is what the conjugate acid does at the equimolar point, and the "
          "third is the weak base's own reaction with water from EK 8.3.A.3."),

 dict(q="Using the table of weak base mixtures, which mixture forms a buffer solution?",
      table=_T_WEAKBASE,
      choices=["Mixture 4", "Mixture 5", "Mixture 6",
               "Mixtures 5 and 6", "None of the three"],
      ans=0,
      why="EK 8.4.A.3 says that if the weak base is in excess then a buffer solution is "
          "formed, since both the base and its conjugate acid are present in quantity. "
          "Only one tabulated mixture has more millimoles of weak base than of added "
          "strong acid."),

 dict(q="Using the same table of weak base mixtures, what is true of mixture 5 at 25 "
        "degrees Celsius?",
      table=_T_WEAKBASE,
      choices=[
        "It is slightly acidic, because the conjugate acid formed reacts with water to "
        "give hydronium ion",
        "It is slightly basic, because a weak base was one of the reagents",
        "It is exactly neutral, because the two reagents were present in equal amounts",
        "It is strongly acidic, because hydrochloric acid is a strong acid",
        "It is a buffer, because both members of the pair are present"],
      ans=0,
      why="EK 8.4.A.3 says that if the weak base and strong acid are equimolar, the "
          "slightly acidic pH can be determined from HB+(aq) + H2O(l) to B(aq) + H3O+(aq). "
          "The tabulated millimoles are equal, so the base is exactly consumed and no "
          "strong acid remains."),

 dict(q="Using the same table of weak base mixtures, how should the pH of mixture 6 be "
        "found?",
      table=_T_WEAKBASE,
      choices=[
        "From the moles of excess hydronium ion and the total volume of solution",
        "From the moles of excess hydroxide ion and the total volume of solution",
        "From the base ionization constant and the initial concentration of the base",
        "From the ratio of the conjugate acid to the weak base",
        "From the equilibrium of the conjugate acid with water alone"],
      ans=0,
      why="EK 8.4.A.3 gives three cases, and this is the one in which the STRONG ACID is "
          "in excess, for which the framework says the pH can be determined from the moles "
          "of excess hydronium ion and the total volume of solution."),

 dict(q="Which equation does the framework give for a weak acid mixed with a weak base?",
      choices=[
        "HA(aq) + B(aq) to A-(aq) + HB+(aq)",
        "HA(aq) + OH-(aq) to A-(aq) + H2O(l)",
        "B(aq) + H3O+(aq) to HB+(aq) + H2O(l)",
        "H+(aq) + OH-(aq) to H2O(l)",
        "HA(aq) + B(aq) to HB+(aq) + OH-(aq)"],
      ans=0,
      why="EK 8.4.A.4 gives exactly this equation and says the two react to an equilibrium "
          "state, transferring a proton from the weak acid to the weak base. The other "
          "equations involve a strong reagent on one side."),

 dict(q="How does the framework describe the extent of reaction when a weak acid is mixed "
        "with a weak base, compared with a mixture involving a strong reagent?",
      choices=[
        "They react to an equilibrium state, rather than quantitatively as the other "
        "combinations do",
        "They do not react at all, since neither reagent is strong",
        "They react quantitatively, exactly as a strong acid and a strong base do",
        "They react quantitatively, but only if the two are present in equal amounts",
        "They react to an equilibrium state in which no products are formed"],
      ans=0,
      why="EK 8.4.A.4 says a weak acid and a weak base react TO AN EQUILIBRIUM STATE, "
          "while EK 8.4.A.1, 8.4.A.2 and 8.4.A.3 each use the word quantitatively for the "
          "combinations that include a strong reagent. Reaching an equilibrium is not the "
          "same as not reacting."),

 dict(q="Using the table of strong acid and strong base trials, what is the pH of trial A?",
      table=_T_STRONG,
      choices=["pH = 1.00", "pH = 13.00", "pH = 2.00", "pH = 12.00", "pH = 7.00"],
      ans=0,
      why="EK 8.4.A.1's one-for-one reaction leaves the difference between the two "
          "tabulated millimole figures as excess hydronium, and dividing by the tabulated "
          "total volume gives its concentration. The pH is the negative logarithm of that."),

 dict(q="Using the same table of trials, what is the pH of trial B at 25 degrees Celsius?",
      table=_T_STRONG,
      choices=["pH = 13.00", "pH = 1.00", "pH = 11.00", "pH = 12.00", "pH = 7.00"],
      ans=0,
      why="The tabulated hydroxide exceeds the tabulated hydronium, so the excess is "
          "hydroxide; dividing by the tabulated volume gives its concentration and a pOH, "
          "which EK 8.1.A.3 turns into a pH at this temperature."),

 dict(q="Using the same table of trials, what is true of trial C?",
      table=_T_STRONG,
      choices=[
        "Neither reagent is in excess, so the solution is neutral at 25 degrees Celsius",
        "The acid is in excess, so the solution is acidic",
        "The base is in excess, so the solution is basic",
        "A buffer has formed, since both reagents are present",
        "The pH cannot be determined without an ionization constant"],
      ans=0,
      why="The tabulated millimoles are equal, and EK 8.4.A.1 has the two react "
          "quantitatively, so nothing is left over. Neither ion remaining in solution "
          "reacts further with water, and a buffer requires a WEAK component, which "
          "neither reagent here is."),

 dict(q="A student mixes a weak acid with a strong base and finds that some un-ionized "
        "weak acid remains after the reaction. What must also be present in quantity?",
      choices=[
        "The conjugate base of that weak acid, formed by the reaction",
        "Excess hydroxide ion, left over from the strong base",
        "Undissolved solid, since the weak acid cannot fully dissolve",
        "A second weak acid, formed from the sodium ion",
        "Nothing else, since the weak acid is the only solute"],
      ans=0,
      why="EK 8.4.A.2's equation converts weak acid into its conjugate base one for one, "
          "so hydroxide that reacted has left an equal amount of conjugate base behind. "
          "Hydroxide cannot remain in excess while un-ionized acid also remains, because "
          "the reaction is quantitative."),

 dict(q="Why does the framework call the reaction between a weak acid and a strong base "
        "quantitative even though the acid is weak?",
      choices=[
        "Because the hydroxide ion is a strong enough base to remove the proton "
        "essentially completely",
        "Because the weak acid becomes a strong acid once a base is added",
        "Because the reaction is exothermic and so runs to completion",
        "Because the sodium ion catalyses the proton transfer",
        "Because a weak acid has no equilibrium of its own once mixed"],
      ans=0,
      why="EK 8.4.A.2 states the reaction is quantitative and writes it with a single "
          "outcome, which is why the mole bookkeeping in this topic works. The weakness of "
          "the acid governs its equilibrium with WATER under EK 8.3.A.2, not its reaction "
          "with hydroxide ion."),

 dict(q="A mixture of a weak acid and a strong base has been prepared, and 3.00 millimoles "
        "of weak acid remain un-ionized alongside 2.00 millimoles of its conjugate base. "
        "Which description applies?",
      choices=[
        "A buffer solution, since both members of the conjugate pair are present in "
        "quantity",
        "A solution of a strong base, since sodium hydroxide was added",
        "A neutral solution, since neither species is in large excess",
        "A solution containing only the conjugate base, since the reaction is quantitative",
        "A solution in which no equilibrium exists, since the reaction has finished"],
      ans=0,
      why="EK 8.4.A.2 attaches the buffer to the case in which the weak acid is in excess, "
          "and the two amounts given are exactly what that leaves: some un-ionized acid "
          "together with the conjugate base its reaction produced."),

 dict(q="A solution containing 5.000 millimoles of HCl is mixed with one containing 4.900 "
        "millimoles of NaOH, and the total volume is 100.0 mL. What is the pH?",
      choices=["pH = 3.00", "pH = 2.00", "pH = 1.00", "pH = 11.00", "pH = 4.00"],
      ans=0,
      why="EK 8.4.A.1's one-for-one reaction leaves 0.100 millimole of hydronium in 100.0 "
          "mL, which is 0.00100 M. The pH is the negative logarithm of that excess "
          "concentration, and a small excess gives a pH far from the value the more "
          "concentrated acid alone would give."),

 dict(q="Which of the following pairs of species could NOT be present together in "
        "appreciable amounts in the same solution?",
      choices=[
        "A weak acid and excess hydroxide ion",
        "A weak acid and its conjugate base",
        "A weak base and its conjugate acid",
        "A weak acid and a spectator sodium ion",
        "A conjugate base and a spectator sodium ion"],
      ans=0,
      why="EK 8.4.A.2 makes the reaction of a weak acid with hydroxide quantitative, so "
          "the two cannot coexist in quantity: whichever is in shorter supply is consumed. "
          "A weak acid together with its conjugate base is precisely the buffer that same "
          "statement describes."),

 dict(q="A weak base is mixed with a strong acid so that the weak base is in excess. What "
        "are the major species present after the reaction?",
      choices=[
        "The weak base and its conjugate acid, in comparable amounts",
        "The weak base and excess hydronium ion",
        "The conjugate acid alone, with no weak base remaining",
        "Excess hydronium ion and the chloride ion only",
        "Neither member of the pair, since both are consumed"],
      ans=0,
      why="EK 8.4.A.3 says that if the weak base is in excess a buffer solution is formed, "
          "which means both members of the conjugate pair are present: the base that "
          "remains and the conjugate acid that the reacted portion produced."),

 dict(q="In which of the four mixing cases named by the framework does the reaction NOT go "
        "essentially to completion?",
      choices=[
        "A weak acid mixed with a weak base",
        "A strong acid mixed with a strong base",
        "A weak acid mixed with a strong base",
        "A weak base mixed with a strong acid",
        "None of them, since all four go to completion"],
      ans=0,
      why="EK 8.4.A.1, 8.4.A.2 and 8.4.A.3 all describe their reactions as quantitative, "
          "while EK 8.4.A.4 says a weak acid and a weak base react TO AN EQUILIBRIUM "
          "STATE, which is the one case where appreciable amounts of all four species "
          "remain."),

 dict(q="A solution containing 10.0 millimoles of a strong base is mixed with one "
        "containing 9.00 millimoles of a strong acid, and the total volume is 100.0 mL. "
        "What is the pOH?",
      choices=["pOH = 2.00", "pOH = 1.00", "pOH = 12.00", "pOH = 3.00", "pOH = 7.00"],
      ans=0,
      why="EK 8.4.A.1's one-for-one reaction leaves 1.00 millimole of hydroxide in 100.0 "
          "mL, which is 0.0100 M, and the pOH is the negative logarithm of that excess "
          "concentration."),

 dict(q="Why does the framework treat the equimolar mixture of a weak acid with a strong "
        "base differently from the equimolar mixture of two strong reagents?",
      choices=[
        "Because the conjugate base left behind reacts with water, while the ions left by "
        "two strong reagents do not",
        "Because the weak acid is not completely consumed at the equimolar point",
        "Because the strong base is not completely consumed at the equimolar point",
        "Because the equimolar point of a weak acid mixture leaves excess hydroxide ion",
        "Because a weak acid produces twice as much conjugate base as a strong acid does"],
      ans=0,
      why="EK 8.4.A.2 gives the equimolar case its own equation, A-(aq) + H2O(l) to HA(aq) "
          "+ OH-(aq), and calls the result slightly basic, whereas EK 8.4.A.1 leaves only "
          "spectator ions behind. Both reactions are quantitative, so neither reagent "
          "survives the equimolar point."),

]
