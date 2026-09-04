# AP ENVIRONMENTAL SCIENCE 5.14 Integrated Pest Management
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding STB-1: humans can mitigate their impact on land and water
# resources through sustainable use.
# Learning objectives STB-1.C, describe integrated pest management; STB-1.D, describe the
# benefits and drawbacks of integrated pest management (IPM).
# Suggested skill 7.D, use data and evidence to support a potential solution.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-1.C.1  Integrated pest management (IPM) is a combination of methods used to
#              effectively control pest species while minimizing the disruption to the
#              environment. These methods include biological, physical, and limited
#              chemical methods such as biocontrol, intercropping, crop rotation, and
#              natural predators of the pests.
#   STB-1.D.1  The use of integrated pest management (IPM) reduces the risk that
#              pesticides pose to wildlife, water supplies, and human health.
#   STB-1.D.2  Integrated pest management (IPM) minimizes disruptions to the environment
#              and threats to human health but can be complex and expensive.
#
# SCOPE. Three statements: a definition with three categories of method and four named
# examples, one claim about what the approach reduces the risk to, and one claim that
# pairs two benefits with two drawbacks. The framework names no pest, no crop, no
# chemical, no country and no figure, and gives no number anywhere, so every quantitative
# item here prints its data in a table and the arithmetic is recomputed in
# verify_e5_14.py from that table alone.
#
# TWO WORDS THAT MUST NOT BE STRENGTHENED.
#   * STB-1.C.1 says LIMITED CHEMICAL methods, not no chemical methods. IPM restricts
#     chemical control; it does not forbid it. One item keys that directly.
#   * STB-1.C.1 says EFFECTIVELY CONTROL pest species, not eliminate them, and STB-1.D.2
#     says IPM CAN BE complex and expensive, not that it always is. One item keys both
#     hedges.
#
# BOUNDARY WITH 5.6. Pesticides, herbicides, fungicides, rodenticides and insecticides,
# resistance arising through ARTIFICIAL SELECTION, the yield benefit of pest control, and
# genetically engineered crops are all EIN-2.G in topic 5.6. None of them is keyed here;
# they appear only as rejected options and in one item that separates the two topics.
#
# BOUNDARY WITH 5.17. STB-1.G.2 names IPM among the methods for protecting forests from
# pathogens and insects. That statement belongs to topic 5.17 and is not keyed here.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e5_14.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.14", "Integrated Pest Management", 5)

_T_COMPARE = dict(
    headers=["Measure taken over one season",
             "Field under conventional spraying",
             "Field under integrated pest management"],
    rows=[["Pesticide applied (kilograms per hectare)", "12", "3"],
          ["Crop lost to the pest (percent)", "9", "8"],
          ["Cost of pest control (currency units per hectare)", "60", "95"],
          ["Hours of monitoring and planning (per hectare)", "2", "14"]])

_T_STREAM = dict(
    headers=["Year of the record",
             "Pesticide in the stream draining the sprayed fields "
             "(micrograms per litre)",
             "Pesticide in the stream draining the managed fields "
             "(micrograms per litre)"],
    rows=[["Year 1", "20", "18"],
          ["Year 4", "24", "9"],
          ["Year 8", "27", "3"]])

_T_WILDLIFE = dict(
    headers=["Group counted on the farmland",
             "Fields under conventional spraying",
             "Fields under integrated pest management"],
    rows=[["Predatory beetles (per square meter)", "4", "19"],
          ["Wild bee species recorded", "7", "23"],
          ["Farmland bird pairs per hundred hectares", "5", "12"]])

_T_ROTATION = dict(
    headers=["Management of the field",
             "Seasons the same crop is grown in succession",
             "Pest larvae in the soil (per square meter)"],
    rows=[["The same crop every season", "6", "320"],
          ["The same crop for three seasons, then a break", "3", "150"],
          ["A different crop every season", "1", "40"]])

_T_INTERCROP = dict(
    headers=["Planting arrangement",
             "Crop rows damaged by the pest (percent)"],
    rows=[["A single crop across the whole field", "31"],
          ["Two crops in alternating strips", "17"],
          ["Three crops intercropped in the same beds", "9"]])

_T_BIOCONTROL = dict(
    headers=["Stage of the orchard record",
             "Predatory mites released (thousands per hectare)",
             "Pest mites on the leaves (per leaf)"],
    rows=[["Before release", "0", "46"],
          ["One month after release", "20", "18"],
          ["Three months after release", "20", "5"]])

QUESTIONS = [

 dict(q="How does the course framework define integrated pest management?",
      choices=[
        "A combination of methods used to effectively control pest species while "
        "minimizing the disruption to the environment",
        "A single method used to eliminate pest species regardless of the disruption to "
        "the environment",
        "A combination of methods used to increase the number of pest species on a farm",
        "A programme of spraying one chemical repeatedly until the pest population "
        "disappears",
        "A rule that no crop may be protected from pests by any means whatever"],
      ans=0,
      why="STB-1.C.1 states that IPM is A COMBINATION OF METHODS used to EFFECTIVELY CONTROL "
          "pest species WHILE MINIMIZING THE DISRUPTION TO THE ENVIRONMENT. The rejected options "
          "reduce it to one method, drop the environmental condition, or reverse the aim."),

 dict(q="Which three categories of method does the framework say integrated pest management "
        "draws on?",
      choices=[
        "Biological, physical, and limited chemical methods",
        "Biological, physical, and unlimited chemical methods",
        "Chemical methods only, applied at a reduced dose",
        "Biological methods only, with no physical or chemical component",
        "Mechanical, financial, and legal methods"],
      ans=0,
      why="STB-1.C.1 states that the methods include BIOLOGICAL, PHYSICAL, AND LIMITED CHEMICAL "
          "methods. The rejected options remove the limit on the chemical component, drop two of "
          "the three categories, or substitute categories the statement never names."),

 dict(q="What does the framework's word LIMITED establish about the chemical part of "
        "integrated pest management?",
      choices=[
        "Chemical methods remain part of the approach but are restricted rather than "
        "excluded",
        "Chemical methods are excluded from the approach altogether",
        "Chemical methods are the only part of the approach that is permitted",
        "Chemical methods may be used without restriction once other methods have failed",
        "Chemical methods are restricted to crops that carry no pest at all"],
      ans=0,
      why="STB-1.C.1 lists LIMITED CHEMICAL methods alongside biological and physical ones, so "
          "the chemical component is inside the approach and bounded. Reading the word as a ban, "
          "or ignoring it, both depart from the statement."),

 dict(q="Which set of examples does the framework give for the methods used in integrated "
        "pest management?",
      choices=[
        "Biocontrol, intercropping, crop rotation, and natural predators of the pests",
        "Blanket spraying, soil fumigation, seed coating, and aerial dusting",
        "Contour plowing, terracing, windbreaks, and strip cropping",
        "Biocontrol, blanket spraying, terracing, and aerial dusting",
        "Clearcutting, prescribed burning, reforestation, and wood reuse"],
      ans=0,
      why="STB-1.C.1 names biocontrol, intercropping, crop rotation, and natural predators of "
          "the pests. Contour plowing, terracing, windbreaks and strip cropping are the soil "
          "conservation methods of STB-1.E.1, and prescribed burning and reforestation are "
          "STB-1.G, all in other topics."),

 dict(q="Which of the following is NOT one of the examples the framework names for integrated "
        "pest management?",
      choices=[
        "Blanket spraying of a broad-spectrum insecticide across the whole field",
        "Biocontrol",
        "Intercropping",
        "Crop rotation",
        "Natural predators of the pests"],
      ans=0,
      why="STB-1.C.1's four named examples are biocontrol, intercropping, crop rotation, and "
          "natural predators of the pests. Spraying a whole field with a broad-spectrum chemical "
          "is neither limited nor among the examples, and it is the practice EIN-2.G.1 associates "
          "with resistance in topic 5.6."),

 dict(q="According to the framework, what does the use of integrated pest management reduce?",
      choices=[
        "The risk that pesticides pose to wildlife, water supplies, and human health",
        "The risk that pesticides pose to crop yields, farm profits, and machinery",
        "The number of pest species that exist in the world",
        "The amount of rainfall a farming district receives",
        "The genetic diversity of the crop being grown"],
      ans=0,
      why="STB-1.D.1 states that the use of IPM reduces THE RISK THAT PESTICIDES POSE TO "
          "WILDLIFE, WATER SUPPLIES, AND HUMAN HEALTH. Loss of a crop's genetic diversity belongs "
          "to EIN-2.G.2 in topic 5.6, and the other options name nothing the statement mentions."),

 dict(q="Which three things does the framework name as being at risk from pesticides?",
      choices=[
        "Wildlife, water supplies, and human health",
        "Wildlife, farm income, and machinery",
        "Water supplies, soil texture, and air pressure",
        "Human health, crop variety names, and market prices",
        "Wildlife, water supplies, and the genetic diversity of the crop"],
      ans=0,
      why="STB-1.D.1 names wildlife, water supplies, and human health as what pesticides put at "
          "risk. The last rejected option swaps the third item for the loss of crop genetic "
          "diversity, which EIN-2.G.2 attaches to engineered crops in a different topic."),

 dict(q="Which drawbacks does the framework attach to integrated pest management?",
      choices=[
        "It can be complex and expensive",
        "It can be simple and cheap",
        "It always increases the crop lost to pests",
        "It always requires more pesticide than conventional control",
        "The framework attaches no drawbacks to it"],
      ans=0,
      why="STB-1.D.2 states that IPM minimizes disruptions to the environment and threats to "
          "human health BUT CAN BE COMPLEX AND EXPENSIVE. The framework does record drawbacks, "
          "so the last option is wrong on its face, and it names neither crop loss nor extra "
          "pesticide among them."),

 dict(q="Which benefits does the same statement pair with those drawbacks?",
      choices=[
        "It minimizes disruptions to the environment and threats to human health",
        "It minimizes disruptions to the environment but raises threats to human health",
        "It minimizes threats to human health but raises disruptions to the environment",
        "It minimizes the cost of pest control and the labour it requires",
        "It minimizes the number of crops a farm must grow"],
      ans=0,
      why="STB-1.D.2 states that IPM MINIMIZES DISRUPTIONS TO THE ENVIRONMENT AND THREATS TO "
          "HUMAN HEALTH, and only then adds the drawbacks. Two rejected options reverse one of "
          "the two benefits, and the statement's own drawbacks are cost and complexity rather "
          "than benefits."),

 dict(q="Two neighbouring fields of the same crop were managed differently for one season. "
        "Which reading of the values matches the framework's account?",
      table=_T_COMPARE,
      choices=[
        "The managed field used far less pesticide and lost about as little crop, but cost "
        "more and took far more planning.",
        "The managed field used far less pesticide and lost about as little crop, and also "
        "cost less and took less planning.",
        "The managed field used more pesticide than the sprayed field and lost more crop.",
        "The two fields used the same amount of pesticide and cost the same to protect.",
        "The managed field lost so much more crop that the pest was not controlled at all."],
      ans=0,
      why="The managed field applies 3 kilograms per hectare against 12, loses 8 percent of the "
          "crop against 9, costs 95 currency units against 60, and takes 14 hours of planning "
          "against 2. STB-1.C.1 has IPM effectively controlling the pest, and STB-1.D.2 warns "
          "that it can be complex and expensive."),

 dict(q="Using the same two fields, how much pesticide did the sprayed field use compared with "
        "the managed field?",
      table=_T_COMPARE,
      choices=[
        "Four times as much",
        "Three times as much",
        "Nine times as much",
        "Fifteen times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated applications gives 12 divided by 3, which is 4. The "
          "rejected values quote the managed field's application alone, take the difference "
          "rather than the ratio, add the two, or deny that they differ."),

 dict(q="Using the same two fields, how much more did pest control cost on the managed field?",
      table=_T_COMPARE,
      choices=[
        "35 currency units per hectare more",
        "95 currency units per hectare more",
        "155 currency units per hectare more",
        "60 currency units per hectare more",
        "9 currency units per hectare more"],
      ans=0,
      why="Subtracting the two tabulated costs gives 95 minus 60, which is 35 currency units per "
          "hectare. The rejected values quote one field's cost alone, add the two, or take the "
          "difference in pesticide applied. STB-1.D.2 warns that IPM can be expensive."),

 dict(q="Two streams draining differently managed farmland were sampled over eight years. What "
        "do the values show?",
      table=_T_STREAM,
      choices=[
        "Pesticide in the stream draining the managed fields fell while pesticide in the "
        "stream draining the sprayed fields rose.",
        "Pesticide in the stream draining the managed fields rose while pesticide in the "
        "stream draining the sprayed fields fell.",
        "Pesticide rose in both streams across the eight years.",
        "Pesticide fell in both streams across the eight years.",
        "Pesticide in the two streams stayed level across the eight years."],
      ans=0,
      why="The sprayed stream runs 20, 24 and 27 micrograms per litre while the managed stream "
          "runs 18, 9 and 3. STB-1.D.1 states that the use of IPM reduces the risk pesticides "
          "pose to water supplies, and a falling concentration in the water leaving the fields "
          "is that reduction measured."),

 dict(q="Using the same two streams, how much lower was the pesticide concentration in the "
        "managed stream than in the sprayed stream in the final year?",
      table=_T_STREAM,
      choices=[
        "24 micrograms per litre lower",
        "27 micrograms per litre lower",
        "30 micrograms per litre lower",
        "15 micrograms per litre lower",
        "3 micrograms per litre lower"],
      ans=0,
      why="Subtracting the two tabulated concentrations gives 27 minus 3, which is 24 micrograms "
          "per litre. The rejected values quote the sprayed stream alone, add the two, take an "
          "earlier year, or quote the managed stream alone."),

 dict(q="Three groups of animals were counted on farmland under the two regimes. Which "
        "conclusion is best supported?",
      table=_T_WILDLIFE,
      choices=[
        "Every group counted was more numerous on the managed fields than on the sprayed "
        "fields.",
        "Every group counted was less numerous on the managed fields than on the sprayed "
        "fields.",
        "The beetles were more numerous on the managed fields but the birds were more "
        "numerous on the sprayed fields.",
        "The three groups were equally numerous under the two regimes.",
        "Counts of animals on farmland say nothing about the risk pesticides pose to "
        "wildlife."],
      ans=0,
      why="Beetles read 19 against 4, bee species 23 against 7, and bird pairs 12 against 5, so "
          "the managed fields lead on all three. STB-1.D.1 states that the use of IPM reduces "
          "the risk pesticides pose to wildlife."),

 dict(q="Using the same counts, how many more wild bee species were recorded on the managed "
        "fields?",
      table=_T_WILDLIFE,
      choices=[
        "16 more species",
        "23 more species",
        "30 more species",
        "15 more species",
        "7 more species"],
      ans=0,
      why="Subtracting the two tabulated counts gives 23 minus 7, which is 16 species. The "
          "rejected values quote the managed fields alone, add the two, give the difference in "
          "the beetle row, or quote the sprayed fields alone."),

 dict(q="Three fields differing only in how often the crop is changed were sampled for pest "
        "larvae. What relationship do the values show?",
      table=_T_ROTATION,
      choices=[
        "The longer the same crop is grown in succession, the more pest larvae are found in "
        "the soil.",
        "The longer the same crop is grown in succession, the fewer pest larvae are found in "
        "the soil.",
        "The number of larvae is the same however often the crop is changed.",
        "The field that changes crop every season holds the most larvae of the three.",
        "Changing the crop raises the number of larvae in the first season and lowers it "
        "afterwards."],
      ans=0,
      why="Six seasons of the same crop carry 320 larvae per square meter, three seasons carry "
          "150, and a different crop every season carries 40. STB-1.C.1 names crop rotation "
          "among the methods that make up integrated pest management."),

 dict(q="Using the same three fields, how many times as many larvae does the unchanged field "
        "hold as the field whose crop changes every season?",
      table=_T_ROTATION,
      choices=[
        "Eight times as many",
        "Four times as many",
        "Three times as many",
        "Two times as many",
        "The same number"],
      ans=0,
      why="Dividing the two tabulated counts gives 320 divided by 40, which is 8. The rejected "
          "values come from the middle field, from the column counting seasons, or from denying "
          "that the fields differ."),

 dict(q="Three planting arrangements were compared for pest damage in one season. Which "
        "conclusion do the values support?",
      table=_T_INTERCROP,
      choices=[
        "Mixing more crops into the same ground went with less of the crop being damaged.",
        "Mixing more crops into the same ground went with more of the crop being damaged.",
        "The three arrangements suffered the same share of damage.",
        "The single-crop field suffered the least damage of the three.",
        "Damage depends only on the size of the field, not on how it is planted."],
      ans=0,
      why="Damage runs 31 percent under a single crop, 17 percent under two crops in strips and "
          "9 percent under three crops intercropped. STB-1.C.1 names intercropping among the "
          "methods that make up integrated pest management."),

 dict(q="Using the same arrangements, how much less of the crop was damaged under the most "
        "mixed planting than under the single crop?",
      table=_T_INTERCROP,
      choices=[
        "22 percentage points less",
        "31 percentage points less",
        "40 percentage points less",
        "14 percentage points less",
        "9 percentage points less"],
      ans=0,
      why="Subtracting the two tabulated shares gives 31 minus 9, which is 22 percentage points. "
          "The rejected values quote the single crop alone, add the two, compare the wrong pair "
          "of arrangements, or quote the most mixed planting alone."),

 dict(q="Predatory mites were released into an orchard and the pest mites on the leaves were "
        "counted. What do the values support?",
      table=_T_BIOCONTROL,
      choices=[
        "The pest fell steadily after the predators were released, which is the outcome the "
        "framework's biocontrol method aims at.",
        "The pest rose steadily after the predators were released, which is the outcome the "
        "framework's biocontrol method aims at.",
        "The pest was highest three months after the release and lowest before it.",
        "The number of predators released fell as the pest fell.",
        "The framework names no method that uses one organism against another."],
      ans=0,
      why="Pest mites run 46 per leaf before the release, 18 after a month and 5 after three "
          "months, while the predators released stay at 20 thousand per hectare. STB-1.C.1 names "
          "biocontrol and natural predators of the pests among the methods of integrated pest "
          "management."),

 dict(q="A student writes that integrated pest management forbids the use of any chemical "
        "control. Which correction is required?",
      choices=[
        "The framework includes limited chemical methods among the approach's own methods",
        "The framework excludes chemical methods entirely, and the student is correct",
        "The framework includes chemical methods with no limit placed on them",
        "The framework includes chemical methods only where biological methods have failed",
        "The framework says nothing at all about chemical methods"],
      ans=0,
      why="STB-1.C.1 lists biological, physical, AND LIMITED CHEMICAL methods, so a bounded "
          "chemical component is part of the approach rather than outside it. The statement "
          "attaches no sequence in which the methods must be tried."),

 dict(q="A second student writes that the framework presents integrated pest management as "
        "simpler and cheaper than conventional control. Which correction is required?",
      choices=[
        "The framework says it can be complex and expensive",
        "The framework says it is always simple and cheap, and the student is correct",
        "The framework says it is always complex and expensive, without qualification",
        "The framework compares its cost with conventional control and finds them equal",
        "The framework makes no statement about its complexity or its cost"],
      ans=0,
      why="STB-1.D.2 states that IPM minimizes disruptions to the environment and threats to "
          "human health BUT CAN BE COMPLEX AND EXPENSIVE. The word can is a hedge, so the "
          "framework neither promises cheapness nor asserts that every scheme is costly."),

 dict(q="Which observation would most directly show that a change of practice had reduced the "
        "risk the framework attaches to water supplies?",
      choices=[
        "Less pesticide in the water drawn from the stream that supplies the district",
        "Fewer pest insects on the leaves of the crop",
        "A larger harvest from the same area of land",
        "More hours spent monitoring the fields each week",
        "A higher price paid for the crop at market"],
      ans=0,
      why="STB-1.D.1 names water supplies among the three things pesticides put at risk, so the "
          "evidence is a fall in pesticide in the water actually used. Pest counts, yield, labour "
          "and price measure other things, some of which the framework never mentions."),

 dict(q="Which comparison would best test whether integrated pest management controls a pest "
        "as effectively as conventional spraying?",
      choices=[
        "Two neighbouring fields of the same crop and soil, one managed each way, with the "
        "crop lost to the pest measured on both",
        "One field managed under integrated pest management, with the crop lost to the pest "
        "measured and no other field involved",
        "One field sprayed in a wet season compared with another field managed in a dry "
        "season",
        "One field of one crop compared with another field of a different crop on different "
        "soil",
        "A survey asking growers which approach they believe controls pests better"],
      ans=0,
      why="A comparison isolates the approach only when the crop, the soil and the season are "
          "matched and the outcome is measured on both. Each rejected design supplies no "
          "comparison, lets the weather or the crop vary alongside the treatment, or collects "
          "opinion in place of measurement."),

 dict(q="A grower whose fields drain into a stream used for drinking water wants to control a "
        "pest with the least risk to that supply. Which approach does the framework support?",
      choices=[
        "Combining biological, physical and limited chemical methods, since the framework "
        "says that use reduces the risk pesticides pose to water supplies",
        "Increasing the dose of a single chemical, since a stronger dose finishes the pest "
        "sooner",
        "Leaving the pest entirely uncontrolled, since the framework prefers no intervention",
        "Switching to a chemical applied by air, since less of it touches the ground",
        "Growing the same crop every season so that the pest becomes predictable"],
      ans=0,
      why="STB-1.C.1 defines IPM as a combination of biological, physical and limited chemical "
          "methods, and STB-1.D.1 states that its use reduces the risk pesticides pose to water "
          "supplies. Nothing in the framework recommends leaving a pest uncontrolled, and crop "
          "rotation is one of its own named methods rather than growing one crop repeatedly."),

 dict(q="Which of the following belongs to the framework's separate topic on pest control "
        "methods rather than to this one?",
      choices=[
        "That organisms can become resistant to a control method through artificial "
        "selection",
        "That the approach combines biological, physical and limited chemical methods",
        "That the approach reduces the risk pesticides pose to wildlife and water supplies",
        "That the approach minimizes disruptions to the environment and threats to human "
        "health",
        "That the approach can be complex and expensive"],
      ans=0,
      why="Resistance arising through artificial selection is EIN-2.G.1 in topic 5.6, a statement "
          "about the consequence of common pest-control chemicals. Every rejected option is "
          "quoted from STB-1.C.1, STB-1.D.1 or STB-1.D.2, which are this topic's own statements."),

 dict(q="Which pair of the framework's own words limits how strongly its claims about this "
        "approach may be stated?",
      choices=[
        "That the methods EFFECTIVELY CONTROL pest species, and that the approach CAN BE "
        "complex and expensive",
        "That the methods ELIMINATE pest species, and that the approach IS ALWAYS complex "
        "and expensive",
        "That the methods effectively control pest species, and that the approach is always "
        "cheap",
        "That the methods eliminate pest species, and that the approach is always cheap",
        "The framework uses no hedged wording in either statement"],
      ans=0,
      why="STB-1.C.1 says the methods EFFECTIVELY CONTROL pest species rather than remove them, "
          "and STB-1.D.2 says the approach CAN BE complex and expensive rather than that it "
          "always is. Both are hedges, and strengthening either goes past the framework."),

 dict(q="How do the framework's three statements on this topic stand in relation to one "
        "another?",
      choices=[
        "The first says what the approach is, the second says what its use reduces the risk "
        "to, and the third pairs its benefits with its drawbacks",
        "The first pairs benefits with drawbacks, the second says what the approach is, and "
        "the third says what its use reduces the risk to",
        "All three define the approach, and none of them names a benefit or a drawback",
        "All three name drawbacks, and none of them defines the approach",
        "The three statements describe three unrelated approaches"],
      ans=0,
      why="STB-1.C.1 defines the approach and lists its methods, STB-1.D.1 names wildlife, water "
          "supplies and human health as what its use reduces the risk to, and STB-1.D.2 sets the "
          "two benefits against complexity and cost. The swap of the definition and the "
          "cost-benefit statement is the error worth guarding against."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Integrated pest management combines biological, physical and limited chemical "
        "methods, such as biocontrol, intercropping, crop rotation and natural predators, to "
        "control pests with little disruption to the environment; it reduces the risk "
        "pesticides pose to wildlife, water supplies and human health, but can be complex "
        "and expensive.",
        "Integrated pest management bans every chemical method and eliminates pest species "
        "entirely, at no cost and with no complexity.",
        "Integrated pest management combines chemical methods only, and raises the risk "
        "pesticides pose to wildlife and to water supplies.",
        "Integrated pest management is a soil conservation programme built from contour "
        "plowing, terracing and windbreaks.",
        "Integrated pest management reduces the genetic diversity of the crop and offers no "
        "benefit to human health."],
      ans=0,
      why="The keyed summary carries STB-1.C.1's definition, categories and examples, STB-1.D.1's "
          "three protected things, and STB-1.D.2's benefits and drawbacks. Each rejected summary "
          "bans the chemical component, reverses a direction, or substitutes the soil "
          "conservation methods of STB-1.E.1 or the crop diversity claim of EIN-2.G.2."),
]
