# AP CHEMISTRY 8.10 Buffer Capacity
# CED effective Fall 2024, Unit 8 Acids and Bases.
# Learning objective 8.10.A: explain the relationship between the buffer capacity of a
# solution and the relative concentrations of the conjugate acid and conjugate base
# components of the solution. Suggested skill 6.G, explain how potential sources of
# experimental error may affect the experimental results.
#
# Essential knowledge relied on, in the framework's own words:
#   8.10.A.1  Increasing the concentration of the buffer components (while keeping the
#             ratio of these concentrations constant) keeps the pH of the buffer the same
#             but increases the capacity of the buffer to neutralize added acid or base.
#   8.10.A.2  When a buffer has more conjugate acid than base, it has a greater buffer
#             capacity for addition of added base than acid. When a buffer has more
#             conjugate base than acid, it has a greater buffer capacity for addition of
#             added acid than base.
#
# THE FOUR BUFFER TOPICS. h8_4.py's header records the split agreed before any of them was
# written, and this module is the CAPACITY entry: scaling both concentrations at a fixed
# ratio, and the asymmetry between capacity for added acid and for added base. 8.4 owns
# deciding which case a mixture is, 8.8 owns the mechanism and its net ionic equations, and
# 8.9 owns the arithmetic -- pH from pKa and the ratio, and the ratio from pH. So no item
# below computes a pH, takes a logarithm, or writes a net ionic equation, and
# verify_h8_10.py asserts that. Where a pH is spoken of here it is only as unchanged or
# changed, never as a number.
#
# THE SWAP THAT MUST NOT SHIP. EK 8.10.A.2 pairs MORE CONJUGATE ACID with a greater
# capacity for added BASE, and more conjugate base with a greater capacity for added ACID.
# Getting that backwards is the single most likely defect in this topic, so every keyed
# choice here states BOTH clauses -- which component is in excess and which addition it
# handles better -- and every anchor in verify_h8_10.py spans both, so a key that is
# half-right cannot pass.
#
# WHY THE ASYMMETRY IS THE RIGHT WAY ROUND, stated so a reader can check it: EK 8.8.A.1
# assigns added base to the CONJUGATE ACID, so the component in excess is the one that has
# more of the work available to it. A buffer rich in the acid form can absorb a great deal
# of added base before running short.
#
# ARITHMETIC. There is none to do beyond comparing concentrations and ratios, and every
# such comparison is recomputed in verify_h8_10.py from the table alone.
#
# NOTATION. export_units.py does not typeset Chemistry; formulas stay plain text.
TOPIC = ("8.10", "Buffer Capacity", 8)

_T_SCALE = dict(
    headers=["Buffer", "[HA] (M)", "[A-] (M)"],
    rows=[["1", "0.10", "0.10"],
          ["2", "1.00", "1.00"],
          ["3", "0.010", "0.010"]])

_T_ASYM = dict(
    headers=["Buffer", "[HA] (M)", "[A-] (M)"],
    rows=[["P", "1.00", "0.10"],
          ["Q", "0.10", "1.00"],
          ["R", "0.50", "0.50"]])

_T_MIXED = dict(
    headers=["Buffer", "[HA] (M)", "[A-] (M)"],
    rows=[["J", "0.20", "0.20"],
          ["K", "0.020", "0.020"],
          ["L", "0.40", "0.10"],
          ["M", "0.10", "0.40"]])

QUESTIONS = [

 dict(q="Increasing the concentration of both buffer components while keeping their ratio "
        "constant has what effect on the pH of the buffer?",
      choices=[
        "The pH stays the same",
        "The pH rises",
        "The pH falls",
        "The pH moves toward 7",
        "The pH becomes equal to the pKa of the acid"],
      ans=0,
      why="EK 8.10.A.1 states that increasing the concentration of the buffer components "
          "while keeping the ratio of those concentrations constant keeps the pH of the "
          "buffer the same. The pH is set by the ratio under EK 8.9.A.1, and the ratio is "
          "what has been held fixed."),

 dict(q="A chemist doubles the concentration of both buffer components, leaving the ratio "
        "between them unchanged. What happens to the buffer's capacity?",
      choices=[
        "It increases the capacity to neutralize added acid or base",
        "It decreases the capacity to neutralize added acid or base",
        "It leaves the capacity unchanged",
        "It increases the capacity for added acid but decreases it for added base",
        "It increases the capacity only if the ratio is one"],
      ans=0,
      why="EK 8.10.A.1 states that the same change increases the capacity of the buffer to "
          "neutralize added acid or base. More of each component is present, so more of "
          "each addition can be consumed before either runs short."),

 dict(q="A buffer contains more conjugate acid than conjugate base. Which addition does it "
        "handle better, and why?",
      choices=[
        "Added base, because the conjugate acid is the component in excess and it is what "
        "reacts with added base",
        "Added acid, because the conjugate acid is the component in excess and it is what "
        "reacts with added acid",
        "Added acid, because an acidic buffer resists acid better",
        "Added base, because the conjugate base is the component in excess",
        "Neither, because the capacities are always equal"],
      ans=0,
      why="EK 8.10.A.2 states that when a buffer has more conjugate acid than base, it has "
          "a greater buffer capacity for addition of added base than acid, and EK 8.8.A.1 "
          "explains why: the conjugate acid is the component that reacts with added base, "
          "so having more of it means more added base can be absorbed."),

 dict(q="A buffer contains more conjugate base than conjugate acid. Which addition does it "
        "handle better, and why?",
      choices=[
        "Added acid, because the conjugate base is the component in excess and it is what "
        "reacts with added acid",
        "Added base, because the conjugate base is the component in excess and it is what "
        "reacts with added base",
        "Added base, because a basic buffer resists base better",
        "Added acid, because the conjugate acid is the component in excess",
        "Neither, because capacity depends only on the total concentration"],
      ans=0,
      why="EK 8.10.A.2 states that when a buffer has more conjugate base than acid, it has "
          "a greater buffer capacity for addition of added acid than base, and EK 8.8.A.1 "
          "assigns added acid to the conjugate base. The mirror of the statement about a "
          "buffer rich in the acid form."),

 dict(q="The table gives three buffers made from the same conjugate pair. What is true of "
        "their pH values?",
      table=_T_SCALE,
      choices=[
        "All three have the same pH, because all three have the same ratio",
        "The most concentrated has the highest pH",
        "The most dilute has the highest pH",
        "All three have the same pH, because all three are buffers",
        "The pH values cannot be compared without the pKa"],
      ans=0,
      why="EK 8.10.A.1 makes concentration irrelevant to pH as long as the ratio is held "
          "constant, and dividing the two tabulated columns gives the same ratio in every "
          "row. Being a buffer is not on its own enough; two buffers of different ratios "
          "would differ in pH."),

 dict(q="Using the same table of three buffers, which has the greatest capacity to "
        "neutralize added acid or base?",
      table=_T_SCALE,
      choices=["Buffer 2", "Buffer 1", "Buffer 3", "All three are equal",
               "The one with the smallest concentrations"],
      ans=0,
      why="EK 8.10.A.1 ties greater capacity to greater concentration of the components at "
          "a fixed ratio, and one tabulated row has both concentrations larger than in the "
          "others. Capacity is about how much of an addition can be consumed, which is a "
          "question about amount rather than about ratio."),

 dict(q="Using the same table of three buffers, which has the smallest capacity?",
      table=_T_SCALE,
      choices=["Buffer 3", "Buffer 1", "Buffer 2", "All three are equal",
               "The one with the largest concentrations"],
      ans=0,
      why="EK 8.10.A.1 makes capacity rise with the concentration of the components, so the "
          "row with the smallest tabulated concentrations has the least of it. Its pH is "
          "the same as the others, which is exactly what makes capacity a separate "
          "property."),

 dict(q="Using the same table of three buffers, why do buffers of such different "
        "concentrations share a pH?",
      table=_T_SCALE,
      choices=[
        "The ratio of the two components is the same in all three",
        "The total concentration is the same in all three",
        "All buffers have the same pH regardless of composition",
        "The pH depends on the volume, which is not stated",
        "The two components neutralize each other completely in all three"],
      ans=0,
      why="EK 8.9.A.1 makes the pH depend on the pKa and the concentration RATIO, and EK "
          "8.10.A.1 says that holding that ratio constant while raising the concentrations "
          "keeps the pH the same. Dividing the tabulated columns row by row gives one "
          "value throughout."),

 dict(q="The table gives three buffers made from the same conjugate pair. Which has the "
        "greatest capacity for added BASE?",
      table=_T_ASYM,
      choices=["Buffer P", "Buffer Q", "Buffer R", "All three are equal",
               "The one with the most conjugate base"],
      ans=0,
      why="EK 8.10.A.2 gives the greater capacity for added base to the buffer with more "
          "conjugate acid than base, and one tabulated row has its acid concentration "
          "above its base concentration by the largest factor. The component that reacts "
          "with added base is the conjugate ACID, under EK 8.8.A.1."),

 dict(q="Using the same three buffers, which has the greatest capacity for added ACID?",
      table=_T_ASYM,
      choices=["Buffer Q", "Buffer P", "Buffer R", "All three are equal",
               "The one with the most conjugate acid"],
      ans=0,
      why="EK 8.10.A.2 gives the greater capacity for added acid to the buffer with more "
          "conjugate base than acid, and one tabulated row has its base concentration above "
          "its acid concentration. Added acid is consumed by the conjugate BASE under EK "
          "8.8.A.1, so that is the component whose amount matters here."),

 dict(q="Using the same three buffers, in which one are the capacities for added acid and "
        "for added base most nearly equal?",
      table=_T_ASYM,
      choices=["Buffer R", "Buffer P", "Buffer Q", "None of them",
               "The buffer whose concentrations are the largest"],
      ans=0,
      why="EK 8.10.A.2's two clauses describe buffers with an EXCESS of one component; "
          "neither applies to a buffer whose two tabulated concentrations are equal, and "
          "with equal amounts of each component neither addition is favoured over the "
          "other."),

 dict(q="Using the same three buffers, which two have pH values on opposite sides of the "
        "pKa of the acid?",
      table=_T_ASYM,
      choices=["Buffers P and Q", "Buffers P and R", "Buffers Q and R",
               "No two of them", "All three, since they differ in concentration"],
      ans=0,
      why="EK 8.9.A.1's equation puts the pH above the pKa when the base form is in excess "
          "and below it when the acid form is, so the two tabulated rows with opposite "
          "excesses sit on opposite sides. The row with equal tabulated concentrations sits "
          "at the pKa itself."),

 dict(q="A student doubles the concentration of both components of a buffer, keeping the "
        "ratio unchanged. What should be expected?",
      choices=[
        "The same pH and a greater capacity",
        "A higher pH and a greater capacity",
        "The same pH and the same capacity",
        "A lower pH and a greater capacity",
        "The same pH and a smaller capacity"],
      ans=0,
      why="EK 8.10.A.1 states in one sentence that increasing the concentration of the "
          "components while keeping the ratio constant keeps the pH the same but increases "
          "the capacity. Both halves have to be right for the prediction to match the "
          "framework."),

 dict(q="A student dilutes a buffer by adding water, which lowers both component "
        "concentrations by the same factor. What should be expected?",
      choices=[
        "The same pH and a smaller capacity",
        "The same pH and a greater capacity",
        "A higher pH and a smaller capacity",
        "A lower pH and a smaller capacity",
        "A change in pH that cannot be predicted"],
      ans=0,
      why="Dilution divides both concentrations by the same factor, so the ratio is "
          "unchanged and EK 8.10.A.1's statement applies in reverse: the pH is the same and "
          "the capacity, which rises with concentration, falls."),

 dict(q="Which change to a buffer would increase its capacity WITHOUT changing its pH?",
      choices=[
        "Dissolving more of both components in the same ratio",
        "Dissolving more of the conjugate acid only",
        "Dissolving more of the conjugate base only",
        "Adding water to the solution",
        "Adding a strong acid to the solution"],
      ans=0,
      why="EK 8.10.A.1 names exactly this change: raising the concentration of the "
          "components while keeping the ratio constant keeps the pH the same but increases "
          "the capacity. Adding one component alone changes the ratio and so, under EK "
          "8.9.A.1, changes the pH."),

 dict(q="Which change to a buffer would alter its pH?",
      choices=[
        "Changing the ratio of conjugate base to conjugate acid",
        "Raising both component concentrations by the same factor",
        "Lowering both component concentrations by the same factor",
        "Transferring the buffer to a larger flask",
        "Stirring the buffer for longer"],
      ans=0,
      why="EK 8.9.A.1 makes the pH depend on the pKa and the RATIO, and EK 8.10.A.1 says "
          "that scaling both concentrations together leaves the pH alone. Only a change to "
          "the ratio moves it."),

 dict(q="A student intends to prepare a buffer but weighs out half as much of each "
        "component as the procedure specifies, dissolving both in the intended volume. What "
        "is the effect on the result?",
      choices=[
        "The pH is as intended but the capacity is lower than intended",
        "The pH is lower than intended and the capacity is as intended",
        "The pH is higher than intended and the capacity is as intended",
        "Both the pH and the capacity are as intended",
        "The pH is as intended and the capacity is higher than intended"],
      ans=0,
      why="Halving both components preserves the ratio, so EK 8.9.A.1 leaves the pH where "
          "it was, while EK 8.10.A.1 ties the capacity to the concentration of the "
          "components and so lowers it. This is the kind of preparation error suggested "
          "skill 6.G asks students to reason about."),

 dict(q="A different student weighs out the correct amount of the conjugate acid but half "
        "the intended amount of the conjugate base. What is the effect on the result?",
      choices=[
        "The pH is lower than intended, because the ratio of base to acid has fallen",
        "The pH is higher than intended, because the ratio of base to acid has fallen",
        "The pH is as intended, because both components are still present",
        "The pH is as intended, because only concentrations were changed",
        "The pH cannot be predicted without the identity of the acid"],
      ans=0,
      why="EK 8.9.A.1's equation makes the pH rise and fall with the base-to-acid ratio, "
          "and this error lowers that ratio. EK 8.10.A.1's protection applies only when the "
          "ratio is held CONSTANT, which is exactly what this error fails to do."),

 dict(q="Why does a more concentrated buffer neutralize more added acid before its pH "
        "shifts appreciably?",
      choices=[
        "It holds more conjugate base, which is the component that consumes added acid",
        "It holds more conjugate acid, which is the component that consumes added acid",
        "It has a higher pH to begin with",
        "It reacts more quickly with the added acid",
        "Its pKa is larger"],
      ans=0,
      why="EK 8.8.A.1 assigns added acid to the conjugate base, and EK 8.10.A.1 ties "
          "capacity to the concentration of the components. More of the consuming species "
          "means more of the addition can be absorbed; the pH and the pKa are unchanged by "
          "the scaling."),

 dict(q="Two buffers have the same pH, but one was made at ten times the concentration of "
        "the other. A large amount of strong base is added to each. What is expected?",
      choices=[
        "The pH of the more concentrated buffer changes less",
        "The pH of the more dilute buffer changes less",
        "The two pH values change by the same amount",
        "Neither pH changes, since both are buffers",
        "The more concentrated buffer changes pH in the opposite direction"],
      ans=0,
      why="EK 8.10.A.1 gives the more concentrated buffer the greater capacity to "
          "neutralize added acid or base, which is precisely the ability to absorb a large "
          "addition with little change. Equal pH values say nothing about capacity, which "
          "is what makes them separate properties."),

 dict(q="The table gives four buffers made from the same conjugate pair. Which has the "
        "greatest capacity for added acid?",
      table=_T_MIXED,
      choices=["Buffer M", "Buffer J", "Buffer K", "Buffer L",
               "Buffers J and K equally"],
      ans=0,
      why="EK 8.10.A.2 gives the greater capacity for added acid to the buffer richest in "
          "the conjugate base, since EK 8.8.A.1 makes that the component consuming added "
          "acid. Comparing the tabulated base concentrations identifies a single largest "
          "value."),

 dict(q="Using the same four buffers, which has the greatest capacity for added base?",
      table=_T_MIXED,
      choices=["Buffer L", "Buffer J", "Buffer K", "Buffer M",
               "Buffers L and M equally"],
      ans=0,
      why="EK 8.10.A.2 gives the greater capacity for added base to the buffer richest in "
          "the conjugate acid, since EK 8.8.A.1 makes that the component consuming added "
          "base. Comparing the tabulated acid concentrations identifies a single largest "
          "value."),

 dict(q="Using the same four buffers, which two share a pH?",
      table=_T_MIXED,
      choices=["Buffers J and K", "Buffers J and L", "Buffers K and M",
               "Buffers L and M", "No two of them share a pH"],
      ans=0,
      why="EK 8.9.A.1 makes the pH follow from the ratio, and EK 8.10.A.1 says that scaling "
          "both concentrations leaves it unchanged. Exactly two tabulated rows have the "
          "same base-to-acid ratio, and they differ only in concentration."),

 dict(q="Using the same four buffers, which one has the same pH as buffer J but a "
        "smaller capacity?",
      table=_T_MIXED,
      choices=["Buffer K", "Buffer L", "Buffer M", "Buffer J has no equal in pH",
               "Every other buffer has the same pH as buffer J"],
      ans=0,
      why="EK 8.10.A.1 describes exactly this situation: two buffers of the same ratio share "
          "a pH while the more dilute of them has the smaller capacity. Exactly one "
          "tabulated row has the same base-to-acid ratio as buffer J, and its "
          "concentrations are lower."),

 dict(q="A buffer contains ten times as much conjugate acid as conjugate base. How do its "
        "two capacities compare?",
      choices=[
        "Its capacity for added base is the greater",
        "Its capacity for added acid is the greater",
        "The two capacities are equal",
        "The greater capacity is for added acid, since the buffer is acidic",
        "Neither capacity can be assessed without the pKa"],
      ans=0,
      why="EK 8.10.A.2 states that when a buffer has more conjugate acid than base, it has "
          "a greater buffer capacity for addition of added base than acid. The component in "
          "excess is the one that consumes added base under EK 8.8.A.1, which is why the "
          "asymmetry runs this way and not the other."),

 dict(q="Does increasing the concentration of both buffer components change the pKa of the "
        "acid?",
      choices=[
        "No, and the pH is unchanged as well because the ratio is unchanged",
        "Yes, and the pH rises with it",
        "Yes, but the pH stays the same",
        "No, but the pH falls because the solution is more concentrated",
        "No, but the pH rises because more base is present"],
      ans=0,
      why="A pKa is a property of the acid rather than of the solution, and EK 8.10.A.1 "
          "states that scaling both concentrations at a fixed ratio keeps the pH of the "
          "buffer the same. What changes is the capacity, which is the point of the "
          "statement."),

 dict(q="What does the framework mean by the capacity of a buffer?",
      choices=[
        "Its ability to neutralize added acid or base",
        "The pH it holds the solution at",
        "The volume of solution that was prepared",
        "The difference between its pH and the pKa of its acid",
        "The speed with which it responds to an addition"],
      ans=0,
      why="EK 8.10.A.1 speaks of the capacity of the buffer TO NEUTRALIZE ADDED ACID OR "
          "BASE, which is the amount of an addition it can absorb. The pH it holds is a "
          "separate property, fixed by the ratio under EK 8.9.A.1."),

 dict(q="A buffer is prepared with equal concentrations of the two components. How do its "
        "capacities for added acid and added base compare?",
      choices=[
        "They are the same, since neither component is in excess",
        "The capacity for added acid is greater",
        "The capacity for added base is greater",
        "Neither capacity exists until an addition is made",
        "The comparison depends on the pKa of the acid"],
      ans=0,
      why="EK 8.10.A.2 states its asymmetry for buffers with MORE of one component than the "
          "other, and neither of its two clauses applies when the amounts are equal. Equal "
          "amounts of the two consuming species leave neither addition better handled."),

 dict(q="A technician reports that a buffer holds the intended pH but is exhausted by a "
        "smaller addition of acid than expected. Which preparation error would explain "
        "this?",
      choices=[
        "Both components were made more dilute than intended, in the correct ratio",
        "The conjugate base was made more concentrated than intended",
        "The conjugate acid was made more concentrated than intended",
        "The wrong acid was used, with a different pKa",
        "The solution was prepared in too small a flask"],
      ans=0,
      why="EK 8.10.A.1 pairs an unchanged ratio with an unchanged pH and ties the capacity "
          "to the concentration, so an error that scales both components down leaves the pH "
          "right and the capacity low. An error in the ratio or in the identity of the acid "
          "would have moved the pH as well, under EK 8.9.A.1."),

 dict(q="Summarise the two things the framework says about buffer capacity.",
      choices=[
        "Capacity rises with the concentration of the components at a fixed ratio, and an "
        "excess of one component gives the greater capacity for the opposite addition",
        "Capacity rises with the concentration of the components at a fixed ratio, and an "
        "excess of one component gives the greater capacity for the same addition",
        "Capacity depends only on the ratio of the two components",
        "Capacity depends only on the pKa of the acid",
        "Capacity rises as the buffer is diluted, and is unaffected by the ratio"],
      ans=0,
      why="EK 8.10.A.1 gives the first statement and EK 8.10.A.2 the second: more conjugate "
          "acid means a greater capacity for added BASE, and more conjugate base means a "
          "greater capacity for added ACID. Each excess protects against the addition it "
          "reacts with, which is the opposite of itself."),

]
