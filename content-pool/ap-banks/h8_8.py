# AP CHEMISTRY 8.8 Properties of Buffers
# CED effective Fall 2024, Unit 8 Acids and Bases.
# Learning objective 8.8.A: explain the relationship between the ability of a buffer to
# stabilize pH and the reactions that occur when an acid or a base is added to a buffered
# solution. Suggested skill 6.D, provide reasoning to justify a claim using chemical
# principles or laws, or using mathematical justification.
#
# Essential knowledge relied on, in the framework's own words -- this topic has exactly one
# statement, and every key below is one of its three clauses:
#   8.8.A.1  A buffer solution contains a large concentration of both members in a
#            conjugate acid-base pair. The conjugate acid reacts with added base and the
#            conjugate base reacts with added acid. These reactions are responsible for the
#            ability of a buffer to stabilize pH.
#
# THE FOUR BUFFER TOPICS. h8_4.py's header records the split that was agreed before any of
# them was written, and this module is the second entry in it:
#
#   8.4   WHICH CASE A MIXTURE IS. Mole counting on a mixture of a weak component with a
#         strong one. Where a buffer forms, 8.4 says so and stops.
#   8.8   (here) THE MECHANISM. A buffer holds a large concentration of BOTH members of a
#         pair; the conjugate acid consumes added base and the conjugate base consumes
#         added acid. Net ionic equations, no arithmetic.
#   8.9   THE ARITHMETIC. pH from pKa and the ratio, and the ratio from pH.
#   8.10  CAPACITY. Scaling both concentrations at a fixed ratio, and the asymmetry between
#         capacity for added acid and for added base.
#
# So no item below computes a pH, takes a logarithm, counts moles to decide what a mixture
# is, or compares the capacity of two buffers. verify_h8_8.py asserts all four, which is
# what keeps the separation real rather than merely intended.
#
# WHY A STRONG ACID AND ITS SALT IS NOT A BUFFER, and why that is a CED argument rather
# than a remembered rule: EK 8.8.A.1 requires that the conjugate base REACT with added
# acid, and EK 8.6.A.1.i states that the strong acids have very weak conjugate bases. A
# species that does not take a proton back cannot do the job the statement assigns it.
# Items 7 and 23 are built on exactly that pair of statements.
#
# NOTATION. export_units.py does not typeset Chemistry. Formulas stay plain text
# (CH3COOH, CH3COO-, NH3, NH4+, H3O+, OH-) and a reaction arrow is written as the word
# "to" so no glyph is left outside a math span.
TOPIC = ("8.8", "Properties of Buffers", 8)

_T_MIXTURES = dict(
    headers=["Solution", "What was dissolved in the water"],
    rows=[["1", "equal amounts of CH3COOH and CH3COONa"],
          ["2", "equal amounts of HCl and NaCl"],
          ["3", "equal amounts of NH3 and NH4Cl"],
          ["4", "CH3COOH and nothing else"],
          ["5", "equal amounts of NaOH and NaCl"]])

_T_EQUATIONS = dict(
    headers=["Equation", "Net ionic equation a student wrote"],
    rows=[["P", "CH3COO- + H3O+ to CH3COOH + H2O"],
          ["Q", "CH3COOH + OH- to CH3COO- + H2O"],
          ["R", "CH3COOH + H3O+ to CH3COOH2+ + H2O"],
          ["S", "Na+ + OH- to NaOH"]])

_T_ADDITIONS = dict(
    headers=["Trial", "What was added to an acetic acid buffer"],
    rows=[["1", "a small amount of strong acid"],
          ["2", "a small amount of strong base"]])

QUESTIONS = [

 dict(q="What does the framework say a buffer solution contains?",
      choices=[
        "A large concentration of both members of a conjugate acid-base pair",
        "A large concentration of one member of a conjugate acid-base pair",
        "A strong acid and a strong base in equal amounts",
        "A weak acid and a weak base that are not conjugates of each other",
        "A salt whose ions are both spectators"],
      ans=0,
      why="EK 8.8.A.1 opens by stating that a buffer solution contains a large "
          "concentration of both members in a conjugate acid-base pair. Both members are "
          "needed because the same statement gives each of them a job, and neither can do "
          "the other's."),

 dict(q="Which component of a buffer reacts when a base is added to it?",
      choices=["The conjugate acid", "The conjugate base", "Both members equally",
               "Neither, since a buffer prevents any reaction",
               "The spectator ion from the salt"],
      ans=0,
      why="EK 8.8.A.1 states that the conjugate acid reacts with added base and the "
          "conjugate base reacts with added acid. A base needs something to take its proton "
          "from, and that is the acid member of the pair."),

 dict(q="Which component of a buffer reacts when an acid is added to it?",
      choices=["The conjugate base", "The conjugate acid", "Both members equally",
               "The water, which absorbs the added acid",
               "The spectator ion from the salt"],
      ans=0,
      why="EK 8.8.A.1 states that the conjugate base reacts with added acid, the mirror of "
          "its statement about added base. The added acid donates a proton, and the base "
          "member of the pair is what accepts it."),

 dict(q="What does the framework say these two reactions are responsible for?",
      choices=[
        "The ability of the buffer to stabilize pH",
        "The ability of the buffer to raise pH",
        "The ability of the buffer to conduct electricity",
        "The ability of the buffer to dissolve additional solute",
        "The ability of the buffer to reach equilibrium more quickly"],
      ans=0,
      why="EK 8.8.A.1 closes by saying these reactions are responsible for the ability of a "
          "buffer to stabilize pH. Stabilizing is holding a value against a disturbance, "
          "which is what consuming the added acid or base achieves."),

 dict(q="The table describes five solutions. Which two of them are buffers?",
      table=_T_MIXTURES,
      choices=["Solutions 1 and 3", "Solutions 1 and 2", "Solutions 2 and 5",
               "Solutions 3 and 4", "Solutions 4 and 5"],
      ans=0,
      why="EK 8.8.A.1 requires a large concentration of BOTH members of a conjugate "
          "acid-base pair, and exactly two of the tabulated solutions were made by "
          "dissolving a weak acid or base together with a salt supplying its conjugate "
          "partner."),

 dict(q="Using the same table of solutions, why is the solution containing only CH3COOH "
        "not a buffer?",
      table=_T_MIXTURES,
      choices=[
        "Only one member of the conjugate pair is present in large concentration",
        "Acetic acid is too weak to act as a buffer component",
        "Acetic acid has no conjugate base",
        "A buffer must contain a salt of a strong acid",
        "A buffer must contain equal volumes of two solutions"],
      ans=0,
      why="EK 8.8.A.1 requires a large concentration of both members of the pair, and a "
          "weak acid dissolved alone supplies its conjugate base only in the trace amount "
          "its own ionization produces. Acetic acid certainly has a conjugate base; what it "
          "lacks alone is enough of it."),

 dict(q="Using the same table of solutions, why is the solution containing HCl and NaCl "
        "not a buffer, even though it contains an acid and its conjugate base?",
      table=_T_MIXTURES,
      choices=[
        "Chloride ion is the very weak conjugate base of a strong acid and does not take a "
        "proton back from added acid",
        "Chloride ion is not the conjugate base of hydrochloric acid",
        "Sodium ion neutralizes the chloride ion",
        "Hydrochloric acid is too concentrated to be buffered",
        "The two substances are present in equal amounts, which cancels the effect"],
      ans=0,
      why="EK 8.8.A.1 requires the conjugate base to REACT with added acid, and EK "
          "8.6.A.1.i states that the strong acids have very weak conjugate bases. A species "
          "with no appetite for a proton cannot perform the reaction the statement assigns "
          "to it, so the pair fails the requirement even though it is a conjugate pair."),

 dict(q="The table lists four net ionic equations. Which one represents what happens when "
        "acid is added to an acetic acid buffer?",
      table=_T_EQUATIONS,
      choices=["Equation P", "Equation Q", "Equation R", "Equation S",
               "None of them, since a buffer does not react with added acid"],
      ans=0,
      why="EK 8.8.A.1 says the conjugate base reacts with added acid, so the correct "
          "equation must consume hydronium ion and produce the conjugate acid. Exactly one "
          "tabulated equation has the acetate ion on the reactant side with hydronium."),

 dict(q="Using the same four equations, which one represents what happens when base is "
        "added to an acetic acid buffer?",
      table=_T_EQUATIONS,
      choices=["Equation Q", "Equation P", "Equation R", "Equation S",
               "None of them, since a buffer does not react with added base"],
      ans=0,
      why="EK 8.8.A.1 says the conjugate acid reacts with added base, so the correct "
          "equation must consume hydroxide ion and produce the conjugate base. Exactly one "
          "tabulated equation has the un-ionized acid on the reactant side with hydroxide."),

 dict(q="Using the same four equations, which one does NOT represent a buffer reaction at "
        "all?",
      table=_T_EQUATIONS,
      choices=["Equation S", "Equation P", "Equation Q", "Equation R",
               "All four represent buffer reactions"],
      ans=0,
      why="EK 8.8.A.1 assigns the buffering reactions to the two members of the conjugate "
          "pair, and one tabulated equation involves only a spectator ion combining with "
          "hydroxide. A spectator takes no part in the proton transfer the statement "
          "describes."),

 dict(q="Why does adding a small amount of strong acid to a buffer lower the pH far less "
        "than adding the same amount to pure water?",
      choices=[
        "The added hydronium is consumed by the conjugate base already present",
        "The added hydronium is diluted by the larger volume of the buffer",
        "The added hydronium reacts with the spectator ions",
        "The buffer prevents the strong acid from ionizing",
        "The buffer raises the temperature, which offsets the change"],
      ans=0,
      why="EK 8.8.A.1 states that the conjugate base reacts with added acid, and that these "
          "reactions are responsible for the buffer's ability to stabilize pH. Pure water "
          "has no such species waiting, so the added hydronium remains."),

 dict(q="Why does adding a small amount of strong base to a buffer raise the pH far less "
        "than adding the same amount to pure water?",
      choices=[
        "The added hydroxide is consumed by the conjugate acid already present",
        "The added hydroxide is consumed by the conjugate base already present",
        "The added hydroxide cannot dissolve in a buffered solution",
        "The buffer converts the strong base into a weak one before it dissolves",
        "The buffer has a lower pH to begin with, so the change is smaller"],
      ans=0,
      why="EK 8.8.A.1 states that the conjugate acid reacts with added base. The conjugate "
          "BASE has no proton to give and is the member that handles added acid instead, so "
          "swapping the two roles inverts the statement."),

 dict(q="Is a solution of a weak acid alone a buffer?",
      choices=[
        "No, because only one member of the pair is present in large concentration",
        "Yes, because a weak acid ionizes only slightly",
        "Yes, because any acid resists a change in pH",
        "No, because a weak acid does not react with added base",
        "It depends only on the concentration of the weak acid"],
      ans=0,
      why="EK 8.8.A.1 requires a large concentration of both members of the conjugate pair. "
          "A weak acid does react with added base, which is half of the mechanism; what is "
          "missing is a large concentration of the conjugate base to handle added acid."),

 dict(q="Is a solution of the sodium salt of a weak acid, dissolved alone, a buffer?",
      choices=[
        "No, because the conjugate acid is not present in large concentration",
        "Yes, because the salt supplies both members of the pair",
        "Yes, because the salt is fully dissociated",
        "No, because a salt cannot take part in proton transfer",
        "No, because the sodium ion interferes"],
      ans=0,
      why="EK 8.8.A.1 requires both members in large concentration, and the salt supplies "
          "only the conjugate base. That base does react with added acid, but nothing is "
          "present in quantity to consume added base."),

 dict(q="Which pair of substances, dissolved together, would make a buffer?",
      choices=[
        "A weak acid and a salt containing its conjugate base",
        "A strong acid and a salt containing its conjugate base",
        "A strong acid and a strong base",
        "Two weak acids that are not conjugates of each other",
        "A weak acid and a salt containing an unrelated anion"],
      ans=0,
      why="EK 8.8.A.1 requires a large concentration of both members of ONE conjugate "
          "acid-base pair. A strong acid's conjugate base is very weak under EK 8.6.A.1.i "
          "and will not react with added acid, and unrelated species are not a conjugate "
          "pair at all."),

 dict(q="An ammonia buffer contains NH3 and NH4+. Which of these is the conjugate acid?",
      choices=["NH4+", "NH3", "Both, since the pair is symmetric",
               "Neither, since ammonia is a base", "The chloride ion that accompanies it"],
      ans=0,
      why="A conjugate acid is the species holding the extra proton, and EK 8.8.A.1 assigns "
          "the conjugate acid the job of reacting with added base. Ammonia is the base "
          "member of this pair under EK 8.6.A.1.iv, which names nitrogenous bases such as "
          "ammonia among the common weak bases."),

 dict(q="In an ammonia buffer, which species reacts when a small amount of strong acid is "
        "added?",
      choices=["NH3, which accepts the added proton", "NH4+, which accepts the added proton",
               "NH4+, which donates a proton to the added acid",
               "The chloride ion, which accepts the added proton",
               "Neither species, since ammonia is already a base"],
      ans=0,
      why="EK 8.8.A.1 states that the conjugate base reacts with added acid, and in this "
          "pair ammonia is the base member. The ammonium ion is the conjugate acid and "
          "handles added base instead."),

 dict(q="In an ammonia buffer, which species reacts when a small amount of strong base is "
        "added?",
      choices=["NH4+, which gives up a proton to the added base",
               "NH3, which gives up a proton to the added base",
               "NH3, which accepts a proton from the added base",
               "The chloride ion, which gives up a proton",
               "Neither species, since the added base is already basic"],
      ans=0,
      why="EK 8.8.A.1 states that the conjugate acid reacts with added base, and the "
          "ammonium ion is the acid member of this pair. Ammonia has no proton to spare in "
          "this reaction; that is what makes it the base member."),

 dict(q="The table describes two additions made to an acetic acid buffer. In which trial "
        "does the acetate ion react?",
      table=_T_ADDITIONS,
      choices=["Trial 1", "Trial 2", "Both trials", "Neither trial",
               "It cannot be decided without the concentrations"],
      ans=0,
      why="EK 8.8.A.1 assigns added acid to the conjugate base of the pair, and the acetate "
          "ion is the conjugate base of acetic acid. Exactly one of the tabulated trials "
          "adds acid."),

 dict(q="Using the same table of additions, in which trial does the un-ionized acetic acid "
        "react?",
      table=_T_ADDITIONS,
      choices=["Trial 2", "Trial 1", "Both trials", "Neither trial",
               "It cannot be decided without the pH of the buffer"],
      ans=0,
      why="EK 8.8.A.1 assigns added base to the conjugate acid of the pair, and the "
          "un-ionized acid is that member. Exactly one of the tabulated trials adds base, "
          "and being an acid is what makes the molecule react with base rather than with "
          "acid."),

 dict(q="Why does the framework specify a LARGE concentration of each member rather than "
        "merely a detectable amount?",
      choices=[
        "Each member must be plentiful enough to consume the acid or base that is added",
        "A small concentration would make the solution too dilute to measure",
        "A large concentration is needed for the salt to dissolve",
        "A large concentration keeps the two members from reacting with each other",
        "A large concentration is what makes the pH neutral"],
      ans=0,
      why="EK 8.8.A.1 pairs the requirement of a large concentration of both members with "
          "the reactions that consume added acid and added base. A trace of a species can "
          "consume only a trace of what is added, so the stabilization the statement "
          "describes would not follow."),

 dict(q="Which of the following is a conjugate acid-base pair suitable for a buffer?",
      choices=["HF and F-", "HCl and Cl-", "HF and Cl-", "NaOH and Na+", "H3O+ and OH-"],
      ans=0,
      why="EK 8.8.A.1 requires both members of ONE conjugate pair, and EK 8.6.A.1.i makes "
          "the conjugate base of a strong acid very weak, so it cannot react with added "
          "acid. Species from different acids are not a conjugate pair, and hydroxide is "
          "not the conjugate base of hydronium."),

 dict(q="A student proposes making a buffer from hydrochloric acid and sodium chloride "
        "because the two contain a conjugate pair. What does the framework say is wrong "
        "with the proposal?",
      choices=[
        "The conjugate base of a strong acid is very weak and will not react with added "
        "acid",
        "The conjugate base of a strong acid is very strong and will react too violently",
        "Sodium chloride does not dissolve well enough to supply the ion",
        "Hydrochloric acid is a gas and cannot be part of a solution",
        "Nothing is wrong; the proposal would work"],
      ans=0,
      why="EK 8.8.A.1 requires the conjugate base to react with added acid, and EK "
          "8.6.A.1.i states that the strong acids have very weak conjugate bases stabilized "
          "by electronegativity, inductive effects or resonance. Half the mechanism is "
          "therefore unavailable."),

 dict(q="What happens to the composition of a buffer when a small amount of strong acid is "
        "added?",
      choices=[
        "Some of the conjugate base is converted into the conjugate acid",
        "Some of the conjugate acid is converted into the conjugate base",
        "Both members are consumed in equal amounts",
        "Neither member changes, since the buffer prevents reaction",
        "The spectator ions are converted into the conjugate base"],
      ans=0,
      why="EK 8.8.A.1 has the conjugate base react with added acid, and a base that accepts "
          "a proton becomes its own conjugate acid. The total amount of the pair is "
          "unchanged; what changes is how it is divided between the two forms."),

 dict(q="What happens to the composition of a buffer when a small amount of strong base is "
        "added?",
      choices=[
        "Some of the conjugate acid is converted into the conjugate base",
        "Some of the conjugate base is converted into the conjugate acid",
        "Both members are produced in equal amounts",
        "The conjugate acid is destroyed and nothing takes its place",
        "The buffer is converted entirely into water"],
      ans=0,
      why="EK 8.8.A.1 has the conjugate acid react with added base, and an acid that gives "
          "up its proton becomes its own conjugate base. This is the mirror of what added "
          "acid does, which is why both members have to be present."),

 dict(q="If a solution contained a large concentration of the conjugate acid but almost "
        "none of the conjugate base, what would it fail to do?",
      choices=[
        "It would fail to stabilize the pH against added acid",
        "It would fail to stabilize the pH against added base",
        "It would fail to conduct electricity",
        "It would fail to dissolve the conjugate acid",
        "It would fail in both directions equally"],
      ans=0,
      why="EK 8.8.A.1 assigns added acid to the conjugate BASE, so a solution short of that "
          "member has nothing to consume added hydronium. It would still handle added base, "
          "because the member it does have is the one the statement assigns that job."),

 dict(q="Two solutions are prepared: one holds a weak acid together with its conjugate base "
        "and the other holds the same weak acid alone. A small amount of strong acid is "
        "added to each. What is expected?",
      choices=[
        "The pH of the first changes far less than the pH of the second",
        "The pH of the second changes far less than the pH of the first",
        "The two pH values change by the same amount",
        "Neither pH changes, since both solutions contain a weak acid",
        "Both pH values rise"],
      ans=0,
      why="EK 8.8.A.1 makes the reaction of the conjugate base with added acid responsible "
          "for stabilizing pH, and only the first solution holds that species in quantity. "
          "Both solutions become more acidic, so neither pH rises."),

 dict(q="Why does the framework require BOTH reactions to be available in a buffer?",
      choices=[
        "Because a disturbance may be an addition of acid or of base, and a different "
        "member handles each",
        "Because the two reactions occur simultaneously at all times",
        "Because one reaction reverses the other and the two cancel",
        "Because the two members react with each other rather than with what is added",
        "Because a buffer must be able to change the pH in both directions"],
      ans=0,
      why="EK 8.8.A.1 assigns added base to the conjugate acid and added acid to the "
          "conjugate base, two distinct jobs done by two distinct species. A buffer "
          "stabilizes pH rather than changing it, and the two members do not consume each "
          "other."),

 dict(q="Which statement about what a buffer does is supported by the framework?",
      choices=[
        "It stabilizes the pH, resisting large changes rather than preventing any change",
        "It fixes the pH permanently, so no addition can change it",
        "It returns the pH to exactly 7 after any addition",
        "It converts any strong acid added into a weak acid before it dissolves",
        "It removes added acid and base from the solution entirely"],
      ans=0,
      why="EK 8.8.A.1's own word is STABILIZE, and the mechanism it gives is consumption of "
          "the added species by a member of the pair, which converts a large pH change into "
          "a small one. Nothing in the statement makes the change zero or fixes the pH at a "
          "particular value."),

 dict(q="Summarise the mechanism the framework gives for a buffer's ability to stabilize "
        "pH.",
      choices=[
        "Both members of a conjugate pair are present in quantity, and each consumes one "
        "kind of addition",
        "One member of a conjugate pair is present in quantity and consumes both kinds of "
        "addition",
        "The two members react with each other, keeping the pH fixed",
        "A spectator ion absorbs whatever is added",
        "The solvent itself neutralizes whatever is added"],
      ans=0,
      why="EK 8.8.A.1 states all three parts in one sentence: a large concentration of both "
          "members of a conjugate acid-base pair, the conjugate acid reacting with added "
          "base, the conjugate base reacting with added acid, and those reactions being "
          "responsible for the stabilization."),

]
