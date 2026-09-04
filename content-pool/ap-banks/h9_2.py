# AP CHEMISTRY 9.2 Absolute Entropy and Entropy Change
# CED effective Fall 2024, Unit 9 Thermodynamics and Electrochemistry.
# Learning objective 9.2.A: calculate the standard entropy change for a chemical or
# physical process based on the absolute entropies (standard molar entropies) of the
# species involved in the process.
# Suggested skill 5.F, calculate or predict an unknown quantity from known quantities by
# selecting and following a logical computational pathway and attending to precision.
#
# Essential knowledge relied on, in the framework's own words:
#   9.2.A.1  The entropy change for a process can be calculated from the absolute
#            entropies of the species involved before and after the process occurs.
#            EQN: (standard entropy change of reaction) = (sum of standard entropies of
#            the products) - (sum of standard entropies of the reactants)
#
# SCOPE. This topic is that one equation. Enthalpy, free energy and thermodynamic
# favorability all belong to 9.3 and beyond, and verify_h9_2.py asserts that none of
# them appears here -- a topic that quietly does the next topic's work is not the topic
# the student selected. The qualitative sign rules stay 9.1's, and where an item checks
# a computed sign against them it says so.
#
# ARITHMETIC. Every value below is recomputed in verify_h9_2.py from the tabulated
# absolute entropies and the equation parsed out of the stem -- the verifier is never
# told the answer. The recomputed value must appear in the KEYED choice with its sign,
# and a sign-flipped distractor must exist, so an item cannot pass by offering only
# wrong magnitudes.
#
# WHY EVERY NUMERIC CHOICE CARRIES AN EXPLICIT SIGN INSIDE A MATH SPAN. cg_check's
# containment test normalizes choice text, which strips a leading plus and lets
# "198.1 J/(mol K)" read as contained in "-198.1 J/(mol K)". Written as
# \( +198.1 \) and \( -198.1 \) the comparison keeps the sign, and h9_check.shows_signed
# matches the raw token rather than the normalized one.
#
# NO FIGURES. Every stimulus is a table of absolute entropies.
TOPIC = ("9.2", "Absolute Entropy and Entropy Change", 9)

_SCOL = "Standard molar entropy, J/(mol K)"

_T_S1 = dict(
    headers=["Species", _SCOL],
    rows=[["N2(g)", "191.6"],
          ["H2(g)", "130.7"],
          ["NH3(g)", "192.8"],
          ["O2(g)", "205.0"],
          ["H2O(l)", "69.9"],
          ["H2O(g)", "188.8"]])

_T_S2 = dict(
    headers=["Species", _SCOL],
    rows=[["C(s)", "5.7"],
          ["H2(g)", "130.7"],
          ["CO(g)", "197.7"],
          ["CO2(g)", "213.8"],
          ["O2(g)", "205.0"],
          ["CH4(g)", "186.3"],
          ["H2O(g)", "188.8"]])

_T_S3 = dict(
    headers=["Species", _SCOL],
    rows=[["CaCO3(s)", "92.9"],
          ["CaO(s)", "39.8"],
          ["CO2(g)", "213.8"],
          ["Na(s)", "51.3"],
          ["Cl2(g)", "223.1"],
          ["NaCl(s)", "72.1"]])

_T_RXN = dict(
    headers=["Process", "Standard entropy change, J/(mol K)"],
    rows=[["1", "-198.1"],
          ["2", "+118.9"],
          ["3", "-88.8"],
          ["4", "+160.7"]])

QUESTIONS = [

 dict(q="According to the course framework, how is the standard entropy change for a "
        "process obtained from the absolute entropies of the species involved?",
      choices=[
        "By subtracting the sum of the reactant entropies from the sum of the product "
        "entropies",
        "By subtracting the sum of the product entropies from the sum of the reactant "
        "entropies",
        "By adding together the absolute entropies of every species on both sides",
        "By dividing the sum of the product entropies by the sum of the reactant "
        "entropies",
        "By taking the difference between the largest and the smallest entropy present"],
      ans=0,
      why="EK 9.2.A.1 gives the entropy change of a reaction as the sum of the standard "
          "entropies of the products less the sum of the standard entropies of the "
          "reactants, so the order of the subtraction is fixed by the framework and is "
          "not a matter of choice."),

 dict(q="For the reaction N2(g) + 3 H2(g) gives 2 NH3(g), what is the standard entropy "
        "change from the tabulated absolute entropies?",
      table=_T_S1,
      choices=["\\( -198.1 \\) J/(mol K), a decrease", "\\( +198.1 \\) J/(mol K), an increase",
               "\\( +63.3 \\) J/(mol K), an increase", "\\( -390.9 \\) J/(mol K), a decrease",
               "\\( +969.3 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1 subtracts the coefficient-weighted sum of the tabulated reactant "
          "entropies from that of the products, and every coefficient in the equation "
          "must be applied. Dropping the coefficient of three on hydrogen gives a "
          "positive value instead, and adding the two sums gives a value near a thousand."),

 dict(q="For the reaction 2 NH3(g) gives N2(g) + 3 H2(g), what is the standard entropy "
        "change from the same tabulated entropies?",
      table=_T_S1,
      choices=["\\( +198.1 \\) J/(mol K), an increase", "\\( -198.1 \\) J/(mol K), a decrease",
               "\\( -63.3 \\) J/(mol K), a decrease", "\\( +390.9 \\) J/(mol K), an increase",
               "\\( +969.3 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1's subtraction runs products minus reactants, so reversing which "
          "species are the products reverses the sign of the result while leaving its "
          "magnitude alone. This is the same reaction as the synthesis written backwards."),

 dict(q="For the reaction 2 H2(g) + O2(g) gives 2 H2O(l), what is the standard entropy "
        "change from the tabulated absolute entropies?",
      table=_T_S1,
      choices=["\\( -326.6 \\) J/(mol K), a decrease", "\\( +326.6 \\) J/(mol K), an increase",
               "\\( -195.9 \\) J/(mol K), a decrease", "\\( -396.5 \\) J/(mol K), a decrease",
               "\\( +606.2 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1 requires the tabulated entropy of each species to be multiplied by "
          "its coefficient before the sums are subtracted, and the row for liquid water "
          "must be used rather than the row for the vapour. Dropping either coefficient "
          "gives one of the other values."),

 dict(q="For the reaction 2 H2(g) + O2(g) gives 2 H2O(g), what is the standard entropy "
        "change from the same table?",
      table=_T_S1,
      choices=["\\( -88.8 \\) J/(mol K), a decrease", "\\( +88.8 \\) J/(mol K), an increase",
               "\\( -277.6 \\) J/(mol K), a decrease", "\\( +41.9 \\) J/(mol K), an increase",
               "\\( +844.0 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1 is applied exactly as for the reaction forming liquid water, but "
          "the row for gaseous water is the one that belongs in the product sum. Using "
          "the wrong phase is the error the table is arranged to expose."),

 dict(q="Forming gaseous water rather than liquid water from hydrogen and oxygen gives a "
        "less negative standard entropy change. Which tabulated fact accounts for that?",
      table=_T_S1,
      choices=[
        "The absolute entropy of gaseous water is larger than that of liquid water",
        "The absolute entropy of liquid water is larger than that of gaseous water",
        "Oxygen has a smaller absolute entropy than hydrogen has",
        "Two moles of water are formed in each of the two reactions",
        "Hydrogen has the smallest absolute entropy in the table"],
      ans=0,
      why="EK 9.2.A.1 makes the product sum the only part of the calculation that "
          "differs between the two reactions, and the tabulated entropy of the vapour is "
          "the larger, so the product sum is larger and the difference less negative. "
          "That two moles form in each case is true but identical on both sides of the "
          "comparison and so explains nothing."),

 dict(q="For the reaction H2O(l) gives H2O(g), what is the standard entropy change from "
        "the tabulated absolute entropies?",
      table=_T_S1,
      choices=["\\( +118.9 \\) J/(mol K), an increase", "\\( -118.9 \\) J/(mol K), a decrease",
               "\\( +258.7 \\) J/(mol K), an increase", "\\( +69.9 \\) J/(mol K), an increase",
               "\\( +188.8 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1 applies to a physical process as it does to a chemical one: the "
          "absolute entropy of the vapour less that of the liquid. The two tabulated "
          "entropies themselves are offered as values, and neither is the difference."),

 dict(q="Which species in the table has the largest standard molar entropy?",
      table=_T_S1,
      choices=["O2(g)", "NH3(g)", "N2(g)", "H2O(g)", "H2O(l)"],
      ans=0,
      why="EK 9.2.A.1 calls these absolute entropies, and reading the largest value out "
          "of the table is the first step in every calculation that uses them. The "
          "answer is settled by the tabulated numbers rather than by any general rule "
          "about which gas should be largest."),

 dict(q="Which species in the table has the smallest standard molar entropy, and what "
        "does that agree with?",
      table=_T_S1,
      choices=[
        "H2O(l), which agrees with a liquid holding its matter less dispersed than a gas",
        "H2(g), which agrees with the lightest molecule being the least dispersed",
        "N2(g), which agrees with nitrogen being unreactive",
        "H2O(g), which agrees with water being a small molecule",
        "NH3(g), which agrees with ammonia having the fewest atoms"],
      ans=0,
      why="The smallest tabulated value belongs to the only liquid in the table, and EK "
          "9.1.A.1 makes matter in a liquid less dispersed than the same matter as a gas. "
          "Molecular mass and reactivity are not what the tabulated ordering follows."),

 dict(q="For the reaction C(s) + O2(g) gives CO2(g), what is the standard entropy change "
        "from the tabulated absolute entropies?",
      table=_T_S2,
      choices=["\\( +3.1 \\) J/(mol K), an increase", "\\( -3.1 \\) J/(mol K), a decrease",
               "\\( +8.8 \\) J/(mol K), an increase", "\\( +213.8 \\) J/(mol K), an increase",
               "\\( +424.5 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1 includes every species, the solid among them: a solid has a small "
          "but non-zero absolute entropy and leaving it out of the reactant sum gives a "
          "different answer. One mole of gas becomes one mole of gas here, so the change "
          "is small."),

 dict(q="For the reaction 2 CO(g) + O2(g) gives 2 CO2(g), what is the standard entropy "
        "change from the same table?",
      table=_T_S2,
      choices=["\\( -172.8 \\) J/(mol K), a decrease", "\\( +172.8 \\) J/(mol K), an increase",
               "\\( -386.6 \\) J/(mol K), a decrease", "\\( +24.9 \\) J/(mol K), an increase",
               "\\( +1028.0 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1's sums are coefficient-weighted, so both the carbon monoxide and "
          "the carbon dioxide entries are doubled before the subtraction. Three moles of "
          "gas become two, so a negative result also agrees with EK 9.1.A.1."),

 dict(q="For the reaction CH4(g) + 2 O2(g) gives CO2(g) + 2 H2O(g), what is the standard "
        "entropy change from the tabulated entropies?",
      table=_T_S2,
      choices=["\\( -4.9 \\) J/(mol K), a decrease", "\\( +4.9 \\) J/(mol K), an increase",
               "\\( +200.1 \\) J/(mol K), an increase", "\\( -193.7 \\) J/(mol K), a decrease",
               "\\( +1187.7 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1 is applied with the coefficient of two on both the oxygen and the "
          "water vapour. Three moles of gas become three moles of gas, so the result is "
          "small, and a large value in either direction signals a dropped coefficient."),

 dict(q="For the reaction C(s) + CO2(g) gives 2 CO(g), what is the standard entropy "
        "change from the same tabulated entropies?",
      table=_T_S2,
      choices=["\\( +175.9 \\) J/(mol K), an increase", "\\( -175.9 \\) J/(mol K), a decrease",
               "\\( -21.8 \\) J/(mol K), a decrease", "\\( +181.6 \\) J/(mol K), an increase",
               "\\( +614.9 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1 doubles the tabulated entropy of carbon monoxide before subtracting "
          "the reactant sum, which includes the small entropy of the solid. One mole of "
          "gas becomes two, so a positive result also agrees with EK 9.1.A.1."),

 dict(q="For the reaction CaCO3(s) gives CaO(s) + CO2(g), what is the standard entropy "
        "change from the tabulated absolute entropies?",
      table=_T_S3,
      choices=["\\( +160.7 \\) J/(mol K), an increase", "\\( -160.7 \\) J/(mol K), a decrease",
               "\\( +120.9 \\) J/(mol K), an increase", "\\( -53.1 \\) J/(mol K), a decrease",
               "\\( +346.5 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1 sums both products before subtracting the single reactant, so the "
          "solid oxide belongs in the product sum alongside the carbon dioxide. Leaving "
          "either product out gives one of the other values."),

 dict(q="For the reaction 2 Na(s) + Cl2(g) gives 2 NaCl(s), what is the standard entropy "
        "change from the same table?",
      table=_T_S3,
      choices=["\\( -181.5 \\) J/(mol K), a decrease", "\\( +181.5 \\) J/(mol K), an increase",
               "\\( -130.2 \\) J/(mol K), a decrease", "\\( -253.6 \\) J/(mol K), a decrease",
               "\\( +469.9 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1 doubles both the sodium and the sodium chloride entries before the "
          "subtraction. A mole of gas is consumed and no gas is produced, so a negative "
          "result also agrees with EK 9.1.A.1's rule about moles of gas."),

 dict(q="A student uses the tabulated absolute entropies for the reaction N2(g) + 3 H2(g) "
        "gives 2 NH3(g), and obtains \\( +63.3 \\) J/(mol K). Which mistake produces that "
        "value?",
      table=_T_S1,
      choices=[
        "The coefficient of three on hydrogen was not applied to its absolute entropy",
        "The coefficient of two on ammonia was not applied to its absolute entropy",
        "The reactant sum was subtracted from the product sum in the wrong order",
        "The two sums were added together instead of being subtracted",
        "The absolute entropy of a gaseous element was treated as zero"],
      ans=0,
      why="EK 9.2.A.1's sums are coefficient-weighted, and using one mole of hydrogen "
          "instead of three reproduces the student's value exactly, while each of the "
          "other named mistakes reproduces a different value. Working backwards from a "
          "wrong answer to the step that produced it is the diagnosis the calculation "
          "supports."),

 dict(q="A second student uses the same tabulated entropies for the reaction N2(g) + 3 "
        "H2(g) gives 2 NH3(g), and obtains \\( +198.1 \\) J/(mol K). Which mistake "
        "produces that value?",
      table=_T_S1,
      choices=[
        "The reactant sum and the product sum were subtracted in the wrong order",
        "The coefficient of three on hydrogen was left out of the reactant sum",
        "The coefficient of two on ammonia was left out of the product sum",
        "The two sums were added rather than subtracted",
        "The absolute entropy of ammonia was read from the wrong row"],
      ans=0,
      why="EK 9.2.A.1 fixes the order as products less reactants, so exchanging the two "
          "sums returns a value of the same magnitude with the opposite sign, which is "
          "exactly what the student reported. Each other named mistake changes the "
          "magnitude as well."),

 dict(q="What must be known about every species taking part before the framework's "
        "entropy equation can be applied?",
      choices=[
        "Its absolute entropy, that is, its standard molar entropy",
        "Only the change in its entropy during the process",
        "Only its molar mass and its physical state",
        "Its entropy measured relative to that of a chosen reference substance",
        "Only whether it is a solid, a liquid or a gas"],
      ans=0,
      why="EK 9.2.A.1 says the entropy change for a process can be calculated from the "
          "absolute entropies of the species involved before and after the process "
          "occurs, and the learning objective names those absolute entropies as the "
          "standard molar entropies. Knowing the state alone gives a sign at best, which "
          "is EK 9.1.A.1's business rather than this calculation."),

 dict(q="For the reaction CaCO3(s) gives CaO(s) + CO2(g), is the computed sign consistent "
        "with the rule about moles of gas?",
      table=_T_S3,
      choices=[
        "Yes, the computed change is positive and the reaction produces gas where there "
        "was none",
        "No, the computed change is negative although the reaction produces a gas",
        "Yes, the computed change is negative and the reaction produces a gas",
        "No, the rule about moles of gas applies only to reactions with no solids",
        "The two cannot be compared, because one is a calculation and one is a rule"],
      ans=0,
      why="EK 9.2.A.1's calculation and EK 9.1.A.1's qualitative rule are two routes to "
          "the same sign, and here both give an increase: the tabulated product sum "
          "exceeds the reactant sum, and the moles of gas rise from none to one. Agreement "
          "between the two is the check the framework's ordering of the topics invites."),

 dict(q="Which reaction has the larger increase in entropy on the tabulated absolute "
        "entropies, C(s) + O2(g) gives CO2(g), or C(s) + CO2(g) gives 2 CO(g)?",
      table=_T_S2,
      choices=[
        "C(s) + CO2(g) gives 2 CO(g)",
        "C(s) + O2(g) gives CO2(g)",
        "The two increases are equal in size",
        "Neither, because both computed changes are negative",
        "The comparison cannot be made from absolute entropies alone"],
      ans=0,
      why="EK 9.2.A.1 gives both changes from the same tabulated entropies, and the "
          "reaction that turns one mole of gas into two has much the larger increase. "
          "The other keeps the moles of gas the same, which EK 9.1.A.1 already suggests "
          "will leave the change small."),

 dict(q="The table lists the standard entropy change computed for four processes. Which "
        "process has the largest increase in entropy?",
      table=_T_RXN,
      choices=["Process 4", "Process 2", "Process 1", "Process 3",
               "Processes 2 and 4 equally"],
      ans=0,
      why="EK 9.2.A.1's quantity is signed, so the largest increase is the largest "
          "positive value in the table rather than the largest magnitude. The most "
          "negative entry is the largest magnitude and is a decrease."),

 dict(q="Using the same table of computed entropy changes, which process has the largest "
        "DECREASE in entropy?",
      table=_T_RXN,
      choices=["Process 1", "Process 3", "Process 2", "Process 4",
               "Processes 1 and 3 equally"],
      ans=0,
      why="A decrease is a negative value under EK 9.2.A.1's signed convention, and the "
          "largest decrease is the most negative tabulated entry rather than the smallest "
          "number in absolute size."),

 dict(q="Using the tabulated entropy changes once more, for which processes has the "
        "matter present become more dispersed?",
      table=_T_RXN,
      choices=["Processes 2 and 4", "Processes 1 and 3", "Process 4 only",
               "Process 2 only", "All four processes"],
      ans=0,
      why="EK 9.1.A.1 ties a rise in entropy to matter becoming more dispersed, and EK "
          "9.2.A.1 supplies the signed value that says whether the entropy rose. The two "
          "tabulated positive entries are the processes for which it did."),

 dict(q="For the reaction 2 H2O(g) gives 2 H2O(l), what is the standard entropy change "
        "from the tabulated absolute entropies?",
      table=_T_S1,
      choices=["\\( -237.8 \\) J/(mol K), a decrease", "\\( +237.8 \\) J/(mol K), an increase",
               "\\( -118.9 \\) J/(mol K), a decrease", "\\( +118.9 \\) J/(mol K), an increase",
               "\\( +517.4 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1 applies to the condensation of two moles, so the single-mole "
          "difference between the two tabulated water entries must be doubled. Leaving "
          "the coefficient out halves the magnitude, and reversing the subtraction "
          "reverses the sign."),

 dict(q="For the reaction C(s) + 2 H2(g) gives CH4(g), what is the standard entropy "
        "change from the tabulated entropies?",
      table=_T_S2,
      choices=["\\( -80.8 \\) J/(mol K), a decrease", "\\( +80.8 \\) J/(mol K), an increase",
               "\\( +49.9 \\) J/(mol K), an increase", "\\( -75.1 \\) J/(mol K), a decrease",
               "\\( +453.4 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1 doubles the hydrogen entry and includes the small entropy of the "
          "solid carbon in the reactant sum. Two moles of gas become one, so a negative "
          "result also agrees with EK 9.1.A.1."),

 dict(q="Why does the framework's equation take the product sum minus the reactant sum "
        "rather than the other way round?",
      choices=[
        "Because the entropy change is the entropy after the process less the entropy "
        "before it",
        "Because the products always have larger absolute entropies than the reactants",
        "Because reactant entropies are taken as negative by convention",
        "Because the sign of an entropy change is a matter of convention only",
        "Because only the products are present once the process is complete"],
      ans=0,
      why="EK 9.2.A.1 describes the calculation as using the absolute entropies of the "
          "species involved before and after the process occurs, so the subtraction is "
          "the after-state less the before-state. Products do not always have the larger "
          "sum, as the reactions with a falling number of moles of gas show."),

 dict(q="For the reaction 2 CaO(s) + 2 CO2(g) gives 2 CaCO3(s), what is the standard "
        "entropy change from the tabulated entropies?",
      table=_T_S3,
      choices=["\\( -321.4 \\) J/(mol K), a decrease", "\\( +321.4 \\) J/(mol K), an increase",
               "\\( -160.7 \\) J/(mol K), a decrease", "\\( +160.7 \\) J/(mol K), an increase",
               "\\( +693.0 \\) J/(mol K), an increase"],
      ans=0,
      why="EK 9.2.A.1's sums are coefficient-weighted, so every entry is doubled and the "
          "result is twice that for the single-mole reaction written in the other "
          "direction. Forgetting the coefficients halves the magnitude."),

 dict(q="Which comparison of the tabulated absolute entropies agrees with the statement "
        "that entropy increases when matter becomes more dispersed?",
      table=_T_S1,
      choices=[
        "Gaseous water has a larger absolute entropy than liquid water",
        "Liquid water has a larger absolute entropy than gaseous water",
        "Hydrogen has a larger absolute entropy than oxygen",
        "Ammonia has a smaller absolute entropy than liquid water",
        "Nitrogen has a larger absolute entropy than oxygen"],
      ans=0,
      why="EK 9.1.A.1 makes matter in the gas state more dispersed than the same matter "
          "as a liquid, and the tabulated absolute entropies bear that out for the two "
          "water rows. Each of the other comparisons contradicts the table itself."),

 dict(q="For the reaction 2 NaCl(s) gives 2 Na(s) + Cl2(g), what is the standard entropy "
        "change from the tabulated absolute entropies?",
      table=_T_S3,
      choices=["\\( +181.5 \\) J/(mol K), an increase", "\\( -181.5 \\) J/(mol K), a decrease",
               "\\( +130.2 \\) J/(mol K), an increase", "\\( +253.6 \\) J/(mol K), an increase",
               "\\( -469.9 \\) J/(mol K), a decrease"],
      ans=0,
      why="EK 9.2.A.1 gives the reverse of the formation reaction the same magnitude with "
          "the opposite sign, because exchanging the products and the reactants exchanges "
          "the two sums. A mole of gas now appears where there was none."),

 dict(q="For the reaction 2 Na(s) + Cl2(g) gives 2 NaCl(s), is the computed sign "
        "consistent with the rule about moles of gas?",
      table=_T_S3,
      choices=[
        "Yes, the computed change is negative and a mole of gas is consumed with none "
        "produced",
        "No, the computed change is positive although a mole of gas is consumed",
        "Yes, the computed change is positive and a mole of gas is consumed",
        "No, the rule about moles of gas cannot be applied when solids take part",
        "The rule and the calculation always disagree, since one is qualitative"],
      ans=0,
      why="EK 9.2.A.1's tabulated calculation and EK 9.1.A.1's rule agree here as well: "
          "the product sum falls short of the reactant sum, and the only gas in the "
          "equation is consumed. A reaction with solids in it is still covered by the "
          "rule, which counts only the gas-phase species."),

]
