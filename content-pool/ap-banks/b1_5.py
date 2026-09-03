# AP BIOLOGY 1.5 Lipids
# CED effective Fall 2025, Unit 1 Chemistry of Life. Big Idea 4 Systems Interactions.
# Learning objective 1.5.A: describe the structure and function of lipids.
# Suggested skill 6.E, predict the causes or effects of a change in, or disruption to,
# one or more components in a biological system.
#
# Essential knowledge relied on, in the framework's own words:
#   1.5.A.1    Lipids are typically nonpolar, hydrophobic molecules whose structure and
#              function are derived from the way their subcomponents are assembled.
#              Fatty acids can be described as either saturated or unsaturated.
#     i.       Saturated fatty acids contain only single bonds between carbon atoms.
#     ii.      Unsaturated fatty acids contain at least one double bond between carbon
#              atoms, which causes the carbon chain to kink.
#     iii.     The more double bonds in a fatty acid tail, the more unsaturated the
#              lipid becomes.
#     iv.      The more unsaturated a lipid is, the more liquid it is at room
#              temperature.
#   1.5.A.2    Lipids provide a variety of functions for living organisms. Some
#              examples of lipids are fats, steroids including cholesterol, and
#              phospholipids.
#     i.       Fats provide energy storage and support cell function. In some cases,
#              they can also provide insulation to help keep mammals warm.
#     ii.      Steroids are hormones that support physiological functions including
#              growth and development, energy metabolism, and homeostasis.
#     iii.     Cholesterol provides essential structural stability to animal cell
#              membranes.
#     iv.      Phospholipids group together to form the lipid bilayers found in plasma
#              and cell membranes.
#
# ON THE DATA. Every table is labelled hypothetical in the stem, and every keyed
# conclusion is recoverable from the table alone and recomputed in verify_b1_5.py. No
# item asks for a remembered melting point or a remembered fatty acid name; the CED
# prints none.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("1.5", "Lipids", 1)

_T_FATTY = dict(
    headers=["Lipid", "Number of carbon to carbon double bonds in each fatty acid tail"],
    rows=[["Lipid 1", "0"],
          ["Lipid 2", "1"],
          ["Lipid 3", "3"],
          ["Lipid 4", "6"]])

_T_MELT = dict(
    headers=["Lipid (hypothetical)",
             "Number of carbon to carbon double bonds in each fatty acid tail",
             "Melting point (degrees Celsius)"],
    rows=[["Lipid P", "0", "63"],
          ["Lipid Q", "1", "13"],
          ["Lipid R", "2", "-5"],
          ["Lipid S", "3", "-11"]])

_T_CHOL = dict(
    headers=["Membrane preparation (hypothetical)",
             "Cholesterol as a percentage of the membrane lipid",
             "Force needed to rupture the membrane (arbitrary units)"],
    rows=[["Preparation 1", "0", "12"],
          ["Preparation 2", "10", "19"],
          ["Preparation 3", "20", "27"],
          ["Preparation 4", "30", "34"]])

_T_STEROID = dict(
    headers=["Group (hypothetical)", "Steroid hormone supplied (units per day)",
             "Mean gain in body length over eight weeks (millimeters)"],
    rows=[["Group 1", "0", "4"],
          ["Group 2", "2", "11"],
          ["Group 3", "4", "19"],
          ["Group 4", "8", "26"]])

QUESTIONS = [

 dict(q="How does the course framework characterize lipids as a class?",
      choices=[
        "They are typically nonpolar, hydrophobic molecules.",
        "They are typically polar, hydrophilic molecules.",
        "They are typically charged molecules that dissolve readily in water.",
        "They are polymers assembled from a single repeating monomer.",
        "They are typically nonpolar but dissolve in water more readily than sugars do."],
      ans=0,
      why="EK 1.5.A.1 opens by stating that lipids are typically nonpolar, hydrophobic "
          "molecules whose structure and function are derived from the way their "
          "subcomponents are assembled. Polar, hydrophilic and charged all describe the "
          "opposite property, and the framework does not describe lipids as polymers of "
          "one repeating monomer."),

 dict(q="What distinguishes a saturated fatty acid, according to the course framework?",
      choices=[
        "It contains only single bonds between its carbon atoms.",
        "It contains at least one double bond between its carbon atoms.",
        "It contains no carbon atoms at all.",
        "It contains a phosphate group in place of one carbon chain.",
        "It contains only double bonds between its carbon atoms."],
      ans=0,
      why="EK 1.5.A.1 i states that saturated fatty acids contain only single bonds "
          "between carbon atoms. Having at least one double bond is the definition EK "
          "1.5.A.1 ii gives for unsaturated, so the two options are the two halves of the "
          "same distinction."),

 dict(q="An unsaturated fatty acid contains at least one double bond between carbon "
        "atoms. What consequence does the course framework attach to that double bond?",
      choices=[
        "It causes the carbon chain to kink.",
        "It causes the carbon chain to become perfectly straight.",
        "It causes the fatty acid to become polar.",
        "It causes the fatty acid to lose its hydrophobic character.",
        "It causes the fatty acid to become a steroid."],
      ans=0,
      why="EK 1.5.A.1 ii states that unsaturated fatty acids contain at least one double "
          "bond between carbon atoms, which causes the carbon chain to kink. The "
          "framework attaches no change of polarity, no loss of hydrophobicity and no "
          "change of class to that double bond."),

 dict(q="Two fatty acid tails differ only in the number of carbon to carbon double bonds "
        "they contain. Which statement follows from the course framework?",
      choices=[
        "The tail with more double bonds belongs to the more unsaturated lipid.",
        "The tail with more double bonds belongs to the more saturated lipid.",
        "The number of double bonds has no bearing on how unsaturated a lipid is.",
        "The tail with more double bonds contains fewer carbon atoms.",
        "The tail with more double bonds is the one described as saturated."],
      ans=0,
      why="EK 1.5.A.1 iii states that the more double bonds in a fatty acid tail, the "
          "more unsaturated the lipid becomes. Saturated is defined in EK 1.5.A.1 i by "
          "the absence of such bonds, so the two rejected saturation readings invert the "
          "framework's own relation."),

 dict(q="How does the degree of unsaturation of a lipid relate to its physical state at "
        "room temperature?",
      choices=[
        "The more unsaturated the lipid, the more liquid it is at room temperature.",
        "The more unsaturated the lipid, the more solid it is at room temperature.",
        "Unsaturation has no relationship to physical state at room temperature.",
        "Only fully saturated lipids can be liquid at room temperature.",
        "Every lipid is a solid at room temperature regardless of unsaturation."],
      ans=0,
      why="EK 1.5.A.1 iv states that the more unsaturated a lipid is, the more liquid it "
          "is at room temperature. That is a direct statement of the relation, so the "
          "reversed and the no-relation options both contradict it."),

 dict(q="The table records the number of carbon to carbon double bonds in the fatty acid "
        "tails of four lipids. Which lipid is the most unsaturated?",
      table=_T_FATTY,
      choices=["Lipid 4", "Lipid 1", "Lipid 2", "Lipid 3",
               "The table gives no basis for ranking them."],
      ans=0,
      why="EK 1.5.A.1 iii makes the count of carbon to carbon double bonds the measure of "
          "how unsaturated a lipid is, so the largest count in the table is the most "
          "unsaturated. The table therefore does supply exactly what the ranking needs."),

 dict(q="Among the same four lipids, which one is built from saturated fatty acids?",
      table=_T_FATTY,
      choices=["Lipid 1", "Lipid 2", "Lipid 3", "Lipid 4",
               "All four are built from saturated fatty acids."],
      ans=0,
      why="EK 1.5.A.1 i defines a saturated fatty acid as containing only single bonds "
          "between carbon atoms, which means a count of zero carbon to carbon double "
          "bonds. Exactly one row of the table records zero, so the option covering all "
          "four is false."),

 dict(q="Which lipids in the table have fatty acid tails whose carbon chains are kinked?",
      table=_T_FATTY,
      choices=[
        "Lipid 2, Lipid 3 and Lipid 4",
        "Lipid 1 only",
        "Lipid 4 only",
        "Lipid 1 and Lipid 2 only",
        "None of them, because kinks are caused by single bonds"],
      ans=0,
      why="EK 1.5.A.1 ii attaches the kink to the presence of at least one carbon to "
          "carbon double bond, so every tail with a nonzero count is kinked and the tail "
          "with zero is not. Three rows of the table record a nonzero count."),

 dict(q="If the four lipids in the table are compared at the same room temperature, which "
        "one is expected to be the most liquid?",
      table=_T_FATTY,
      choices=["Lipid 4", "Lipid 1", "Lipid 2", "Lipid 3",
               "All four are expected to be equally liquid."],
      ans=0,
      why="Chaining EK 1.5.A.1 iii to EK 1.5.A.1 iv: more double bonds means more "
          "unsaturated, and more unsaturated means more liquid at room temperature. The "
          "largest count in the table therefore gives the most liquid lipid."),

 dict(q="The table gives measured melting points for four hypothetical lipids alongside "
        "the number of double bonds in their tails. Taking room temperature as 22 degrees "
        "Celsius, which lipids are liquid at room temperature?",
      table=_T_MELT,
      choices=[
        "Lipid Q, Lipid R and Lipid S",
        "Lipid P only",
        "Lipid P and Lipid Q only",
        "Lipid S only",
        "All four lipids"],
      ans=0,
      why="A lipid is liquid above its melting point, so the answer is every row whose "
          "melting point is below 22 degrees. Three of the four qualify, and the "
          "remaining one melts far above room temperature."),

 dict(q="What relationship between the two numerical columns of the melting point table "
        "is shown by the data?",
      table=_T_MELT,
      choices=[
        "As the number of double bonds rises, the melting point falls.",
        "As the number of double bonds rises, the melting point also rises.",
        "The melting point is the same for every number of double bonds.",
        "The melting point rises and then falls as double bonds are added.",
        "The two columns show no consistent relationship."],
      ans=0,
      why="The melting points fall monotonically as the double bond count rises across "
          "the four rows. That is the quantitative form of EK 1.5.A.1 iv, since a lower "
          "melting point is what makes a lipid more liquid at a given room temperature."),

 dict(q="A fifth lipid of the same family carries four carbon to carbon double bonds in "
        "each tail. Based on the pattern in the melting point table, what is the best "
        "prediction for its melting point?",
      table=_T_MELT,
      choices=[
        "Lower than the melting point of any lipid in the table",
        "Higher than the melting point of any lipid in the table",
        "Between the two highest melting points in the table",
        "Exactly equal to the melting point of the lipid with three double bonds",
        "Impossible to predict, because melting point does not depend on double bonds"],
      ans=0,
      why="Every additional double bond in the table is accompanied by a lower melting "
          "point, and the new lipid carries more double bonds than any row shown. EK "
          "1.5.A.1 iii and iv are what make the extrapolation reasonable rather than "
          "arbitrary."),

 dict(q="Which functions does the course framework assign to fats?",
      choices=[
        "Energy storage and support of cell function, and in some cases insulation that "
        "helps keep mammals warm",
        "Formation of the lipid bilayer of the plasma membrane",
        "Acting as hormones that support growth and development",
        "Providing structural stability to animal cell membranes",
        "Encoding and transmitting hereditary information"],
      ans=0,
      why="EK 1.5.A.2 i states that fats provide energy storage and support cell function "
          "and can in some cases provide insulation to help keep mammals warm. The other "
          "options are the functions the same statement assigns to phospholipids in iv, "
          "to steroids in ii and to cholesterol in iii."),

 dict(q="Steroids are described in the course framework as which of the following?",
      choices=[
        "Hormones that support growth and development, energy metabolism, and "
        "homeostasis",
        "Structural molecules that group together into bilayers",
        "Long-term energy stores that also insulate mammals",
        "Nonpolar chains whose kinks determine how liquid a lipid is",
        "Molecules that carry hereditary information between generations"],
      ans=0,
      why="EK 1.5.A.2 ii states that steroids are hormones that support physiological "
          "functions including growth and development, energy metabolism, and "
          "homeostasis. Bilayer formation belongs to phospholipids under EK 1.5.A.2 iv "
          "and energy storage to fats under EK 1.5.A.2 i."),

 dict(q="What role does the course framework assign specifically to cholesterol?",
      choices=[
        "It provides essential structural stability to animal cell membranes.",
        "It provides the main long-term energy store of animal cells.",
        "It forms the lipid bilayer of the plasma membrane on its own.",
        "It is the monomer from which all other lipids are assembled.",
        "It carries the phosphate group that makes a phospholipid polar."],
      ans=0,
      why="EK 1.5.A.2 iii states that cholesterol provides essential structural stability "
          "to animal cell membranes. EK 1.5.A.2 iv assigns bilayer formation to "
          "phospholipids rather than to cholesterol, and the framework names no lipid "
          "monomer of the kind the fourth option describes."),

 dict(q="Which lipids does the course framework identify as grouping together to form the "
        "lipid bilayers of plasma and cell membranes?",
      choices=["Phospholipids", "Steroids", "Fats", "Saturated fatty acids alone",
               "Cholesterol alone"],
      ans=0,
      why="EK 1.5.A.2 iv states that phospholipids group together to form the lipid "
          "bilayers found in plasma and cell membranes. Cholesterol is assigned the "
          "different role of providing structural stability in EK 1.5.A.2 iii, and fats "
          "and steroids are assigned energy storage and hormone roles."),

 dict(q="A physician wishes to describe a lipid that acts as a chemical messenger "
        "supporting growth. Which of the lipid examples named in the course framework "
        "fits that description?",
      choices=["A steroid", "A fat", "A phospholipid",
               "A saturated fatty acid", "An unsaturated fatty acid"],
      ans=0,
      why="EK 1.5.A.2 ii is the only sub-point that describes a lipid as a hormone, and "
          "it names growth and development among the physiological functions steroids "
          "support. Fats and phospholipids are given storage and membrane roles instead."),

 dict(q="A membrane preparation is found to consist of two facing layers of lipid "
        "molecules. Which lipid example named in the course framework accounts for that "
        "arrangement?",
      choices=["Phospholipids, which group together into the two facing layers of a "
               "bilayer",
               "Steroid hormones, which act as chemical messengers",
               "Stored fats, which provide energy and insulation",
               "Free fatty acids released from a fat",
               "Cholesterol, which stabilizes the membrane it sits in"],
      ans=0,
      why="EK 1.5.A.2 iv states that phospholipids group together to form the lipid "
          "bilayers found in plasma and cell membranes, which is the two-layer "
          "arrangement described. No other sub-point of EK 1.5.A.2 assigns a bilayer to "
          "any other lipid."),

 dict(q="A population of cells is grown so that its membrane lipids contain far fewer "
        "carbon to carbon double bonds than usual. Which prediction follows most directly "
        "from the course framework?",
      choices=[
        "Those lipids will be less liquid at room temperature than the usual ones.",
        "Those lipids will be more liquid at room temperature than the usual ones.",
        "Those lipids will become polar and dissolve in the surrounding water.",
        "Those lipids will stop forming a bilayer and act as hormones instead.",
        "Those lipids will be unchanged, because double bond number affects only "
        "colour."],
      ans=0,
      why="EK 1.5.A.1 iii ties the number of double bonds to how unsaturated a lipid is "
          "and EK 1.5.A.1 iv ties unsaturation to how liquid it is at room temperature, "
          "so fewer double bonds gives a less liquid lipid. Nothing in EK 1.5.A.1 makes a "
          "double bond change a lipid's polarity or its class."),

 dict(q="According to the course framework, the structure and function of a lipid are "
        "derived from what?",
      choices=[
        "The way its subcomponents are assembled",
        "The number of separate lipid molecules present in the cell",
        "The temperature at which the lipid was first synthesized",
        "The sequence of nucleotides in the gene that produced it",
        "The number of hydrogen bonds it forms with surrounding water"],
      ans=0,
      why="EK 1.5.A.1 states that lipids are typically nonpolar, hydrophobic molecules "
          "whose structure and function are derived from the way their subcomponents are "
          "assembled. The framework attributes lipid function to that assembly rather "
          "than to abundance, temperature of synthesis or hydrogen bonding with water."),

 dict(q="Four hypothetical membrane preparations differing only in cholesterol content "
        "were tested for the force needed to rupture them, with the results in the table. "
        "Which conclusion is best supported?",
      table=_T_CHOL,
      choices=[
        "Membranes with more cholesterol withstood a greater rupturing force.",
        "Membranes with more cholesterol withstood a smaller rupturing force.",
        "Cholesterol content had no measurable effect on rupturing force.",
        "The preparation with no cholesterol withstood the greatest force.",
        "The rupturing force reached its maximum at an intermediate cholesterol "
        "content."],
      ans=0,
      why="The rupturing force rises at every step as cholesterol content rises across "
          "the four preparations. That is the pattern EK 1.5.A.2 iii describes when it "
          "says cholesterol provides essential structural stability to animal cell "
          "membranes."),

 dict(q="Using the same rupture data, how many times as great was the force needed for "
        "the preparation containing 20 percent cholesterol compared with the preparation "
        "containing none?",
      table=_T_CHOL,
      choices=["About twice as great", "About half as great", "About four times as great",
               "About ten times as great", "Almost exactly the same"],
      ans=0,
      why="The two tabulated forces are 27 and 12 arbitrary units, and dividing the first "
          "by the second gives a value near two. The comparison is what turns the "
          "qualitative claim of EK 1.5.A.2 iii into a reading off the data."),

 dict(q="Four groups of a hypothetical animal received different daily amounts of a "
        "steroid hormone, and their mean gain in body length was recorded, as shown in "
        "the table. Which conclusion is best supported?",
      table=_T_STEROID,
      choices=[
        "Body length gain increased as the amount of steroid supplied increased.",
        "Body length gain decreased as the amount of steroid supplied increased.",
        "The steroid had no measurable effect on body length gain.",
        "Only the group receiving no steroid gained any body length.",
        "Body length gain was greatest at the intermediate amounts supplied."],
      ans=0,
      why="The mean gain rises at every step as the supplied amount rises across the four "
          "groups. EK 1.5.A.2 ii names growth and development among the physiological "
          "functions that steroids, acting as hormones, support."),

 dict(q="In the same steroid experiment, which group serves as the control?",
      table=_T_STEROID,
      choices=["Group 1", "Group 2", "Group 3", "Group 4",
               "The experiment contains no control group."],
      ans=0,
      why="A control receives none of the treatment whose effect is being measured, and "
          "exactly one group in the table was supplied zero units per day. That group is "
          "the baseline against which the other three gains are judged."),

 dict(q="A student claims that a lipid becomes polar when its fatty acid tails contain "
        "double bonds. Which correction is best supported by the course framework?",
      choices=[
        "Lipids are typically nonpolar and hydrophobic; a double bond kinks the chain "
        "rather than making it polar.",
        "Lipids are typically polar, so the student has the class backwards but the "
        "double bond right.",
        "A double bond removes the kink from the chain and leaves polarity unchanged.",
        "Double bonds cannot occur between carbon atoms in a lipid at all.",
        "A double bond converts a fatty acid into a steroid hormone."],
      ans=0,
      why="EK 1.5.A.1 describes lipids as typically nonpolar and hydrophobic, and EK "
          "1.5.A.1 ii attaches the double bond to a kink in the carbon chain and to "
          "nothing else. The framework nowhere makes a double bond a source of polarity."),

 dict(q="Which element does the course framework require for building phospholipids that "
        "it does not require for building a carbohydrate?",
      choices=["Phosphorus", "Carbon", "Hydrogen", "Oxygen", "Sulfur"],
      ans=0,
      why="EK 1.2.A.1 ii states that phosphorus is used in the building of phospholipids, "
          "which it identifies as a type of lipid, while carbon, hydrogen and oxygen are "
          "the elements EK 1.2.A.1 names for biological molecules generally. Sulfur is "
          "assigned to proteins in EK 1.2.A.1 i."),

 dict(q="Which comparison of two lipid functions named in the course framework is "
        "accurate?",
      choices=[
        "Fats store energy, whereas phospholipids form the bilayer of a membrane.",
        "Fats form the bilayer of a membrane, whereas phospholipids store energy.",
        "Fats act as hormones, whereas steroids store energy.",
        "Cholesterol stores energy, whereas fats stabilize animal cell membranes.",
        "Steroids form the bilayer of a membrane, whereas cholesterol acts as a "
        "hormone."],
      ans=0,
      why="EK 1.5.A.2 i assigns energy storage and support of cell function to fats, and "
          "EK 1.5.A.2 iv assigns the formation of lipid bilayers to phospholipids. Every "
          "rejected option swaps a function onto a lipid the framework assigns a "
          "different one."),

 dict(q="A mammal living in a cold climate carries a thick layer of fat beneath its skin. "
        "Which function named in the course framework does that layer most directly "
        "illustrate?",
      choices=[
        "Insulation that helps keep the mammal warm",
        "Formation of the lipid bilayer of its cell membranes",
        "Action as a hormone regulating its growth",
        "Provision of structural stability to its cell membranes",
        "Storage of the animal's hereditary information"],
      ans=0,
      why="EK 1.5.A.2 i states that fats can in some cases provide insulation to help keep "
          "mammals warm, alongside their energy storage role. The other options belong to "
          "phospholipids, steroids and cholesterol under the other sub-points of EK "
          "1.5.A.2."),

 dict(q="Two lipids contain the same number of carbon atoms per tail, but one tail "
        "contains only single bonds between carbons and the other contains three double "
        "bonds. Which pair of predictions follows from the course framework?",
      choices=[
        "The tail with only single bonds is unkinked and the lipid it belongs to is less "
        "liquid at room temperature.",
        "The tail with only single bonds is kinked and the lipid it belongs to is more "
        "liquid at room temperature.",
        "Both tails are kinked, and both lipids are equally liquid at room temperature.",
        "Neither tail is kinked, and the lipid with three double bonds is the more solid "
        "of the two.",
        "The tail with three double bonds is unkinked and belongs to the more saturated "
        "lipid."],
      ans=0,
      why="EK 1.5.A.1 i makes a tail with only single bonds saturated, EK 1.5.A.1 ii "
          "confines the kink to tails carrying a double bond, and EK 1.5.A.1 iii and iv "
          "make the more unsaturated lipid the more liquid one. The three statements "
          "together fix both halves of the prediction."),

 dict(q="Which of the following would be the strongest evidence that a purified lipid "
        "sample is highly unsaturated, given only the course framework's own criteria?",
      choices=[
        "Its fatty acid tails carry many carbon to carbon double bonds and it is liquid "
        "at room temperature.",
        "Its fatty acid tails carry no carbon to carbon double bonds and it is solid at "
        "room temperature.",
        "It dissolves readily in water at room temperature.",
        "It contains phosphorus as well as carbon, hydrogen and oxygen.",
        "It forms a bilayer when it is placed in water."],
      ans=0,
      why="EK 1.5.A.1 iii makes the double bond count the measure of unsaturation and EK "
          "1.5.A.1 iv predicts that a more unsaturated lipid is more liquid at room "
          "temperature, so the two observations agree. Solubility in water contradicts "
          "the hydrophobic character of EK 1.5.A.1, and phosphorus and bilayer formation "
          "identify a phospholipid under EK 1.2.A.1 ii and EK 1.5.A.2 iv without "
          "reporting saturation."),
]
