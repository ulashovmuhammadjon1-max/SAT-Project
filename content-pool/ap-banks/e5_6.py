# AP ENVIRONMENTAL SCIENCE 5.6 Pest Control Methods
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding EIN-2: when humans use natural resources, they alter natural
# systems.
# Learning objective EIN-2.G: describe the benefits and drawbacks of different methods
# of pest control.
# Suggested skill 7.E, make a claim that proposes a solution to an environmental problem
# in an applied context.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-2.G.1  One consequence of using common pest-control methods such as pesticides,
#              herbicides, fungicides, rodenticides, and insecticides is that organisms
#              can become resistant to them through artificial selection. Pest control
#              decreases crop damage by pest and increases crop yields.
#   EIN-2.G.2  Crops can be genetically engineered to increase their resistance to pests
#              and diseases. However, using genetically engineered crops in planting or
#              other ways can lead to loss of genetic diversity of that particular crop.
#
# SCOPE. Four claims and one list. The list is pesticides, herbicides, fungicides,
# rodenticides and insecticides. The claims are: resistance arises through ARTIFICIAL
# SELECTION; pest control decreases crop damage and increases yields; genetic
# engineering can increase a crop's resistance to pests and diseases; and using
# engineered crops can lead to loss of genetic diversity OF THAT PARTICULAR CROP. No key
# here goes further -- the framework names no chemical, no pest species, no year, and
# says nothing about human health effects in this topic.
#
# THE PHRASE THAT IS EASY TO MISREAD. Resistance in EIN-2.G.1 is resistance OF THE PEST
# to the control method; resistance in EIN-2.G.2 is resistance OF THE CROP to pests and
# diseases. Several items turn on keeping those two apart, and the distractors are built
# from swapping them, because that is the mistake a prepared student actually makes.
#
# BOUNDARY WITH 5.14. Integrated pest management, its component methods, and its benefit
# of reduced risk to wildlife, water supplies and human health are STB-1.C and STB-1.D
# in topic 5.14. They appear here only as rejected options, never as a key.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e5_6.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.6", "Pest Control Methods", 5)

_T_RESIST = dict(
    headers=["Generation of the insect population sprayed",
             "Share of the population surviving the standard dose (percent)"],
    rows=[["First", "4"],
          ["Fifth", "17"],
          ["Tenth", "48"],
          ["Fifteenth", "82"]])

_T_YIELD = dict(
    headers=["Treatment of the plot",
             "Share of the crop damaged by the pest (percent)",
             "Crop harvested (tonnes per hectare)"],
    rows=[["No pest control applied", "38", "2.4"],
          ["Pest control applied", "9", "4.8"]])

_T_DOSE = dict(
    headers=["Year of the spraying programme",
             "Dose needed to kill nine tenths of the pest population "
             "(grams per hectare)"],
    rows=[["Year 1", "40"],
          ["Year 4", "90"],
          ["Year 8", "220"],
          ["Year 12", "560"]])

_T_VARIETIES = dict(
    headers=["Period", "Number of distinct varieties of the crop planted in the district",
             "Share of the planted area sown to the single leading variety (percent)"],
    rows=[["Before engineered seed was available", "34", "12"],
          ["Ten years after it became available", "11", "58"],
          ["Twenty years after it became available", "4", "86"]])

_T_GE = dict(
    headers=["Field", "Type of seed sown",
             "Share of plants showing pest damage at harvest (percent)"],
    rows=[["Field 1", "Conventional variety", "31"],
          ["Field 2", "Conventional variety", "27"],
          ["Field 3", "Variety engineered for pest resistance", "6"],
          ["Field 4", "Variety engineered for pest resistance", "8"]])

_T_OUTBREAK = dict(
    headers=["District",
             "Number of distinct varieties of the crop grown",
             "Share of the district's crop lost to a single new disease (percent)"],
    rows=[["District J", "22", "7"],
          ["District K", "9", "24"],
          ["District L", "3", "61"]])

QUESTIONS = [

 dict(q="Which group of methods does the course framework name as common pest-control "
        "methods?",
      choices=[
        "Pesticides, herbicides, fungicides, rodenticides, and insecticides",
        "Terracing, contour plowing, strip cropping, and windbreaks",
        "Drip, flood, furrow, and spray systems",
        "Feedlots, rotational grazing, and free-range grazing",
        "Reforestation, prescribed burning, and the removal of affected trees"],
      ans=0,
      why="EIN-2.G.1 names pesticides, herbicides, fungicides, rodenticides, and insecticides "
          "as common pest-control methods. The rejected groups are the soil conservation "
          "methods of STB-1.E.1, the irrigation types of EIN-2.E.2, the meat production methods "
          "of EIN-2.H.1, and the forestry methods of STB-1.G."),

 dict(q="According to the framework, by what process can organisms become resistant to a "
        "pest-control method?",
      choices=[
        "Artificial selection",
        "Genetic engineering of the pest by the grower",
        "The direct transfer of resistance from the crop to the pest",
        "A rise in the mutation rate caused by the crop itself",
        "The framework does not say how resistance arises"],
      ans=0,
      why="EIN-2.G.1 states that one consequence of using common pest-control methods is that "
          "organisms can become resistant to them through artificial selection. The framework "
          "gives that process by name, so the last option is wrong on its face."),

 dict(q="What two benefits does the framework attribute to pest control?",
      choices=[
        "It decreases crop damage by pests and increases crop yields.",
        "It increases crop damage by pests and decreases crop yields.",
        "It decreases crop damage by pests but has no effect on crop yields.",
        "It increases crop yields but has no effect on crop damage by pests.",
        "It removes the need for irrigation and for fertilizer."],
      ans=0,
      why="EIN-2.G.1 ends by stating that pest control decreases crop damage by pest and "
          "increases crop yields. Each rejected option reverses one of the two effects, drops "
          "one, or substitutes benefits the framework does not claim."),

 dict(q="An insect population is sprayed with the same chemical at the same dose over many "
        "generations. What do the survival values show?",
      table=_T_RESIST,
      choices=[
        "A rising share of the population survives the same dose from one generation to "
        "the next.",
        "A falling share of the population survives the same dose from one generation to "
        "the next.",
        "The same share of the population survives in every generation recorded.",
        "The share surviving rose and then fell back to its starting level.",
        "The share surviving cannot be compared between generations."],
      ans=0,
      why="The tabulated shares are 4, 17, 48 and 82 percent, rising with no reversal. "
          "EIN-2.G.1 states that organisms can become resistant to common pest-control methods "
          "through artificial selection, and a rising survival share under a fixed dose is what "
          "that resistance looks like in the field."),

 dict(q="Using the same insect record, by how many percentage points did the share surviving "
        "rise between the first and the fifteenth generation?",
      table=_T_RESIST,
      choices=[
        "78 percentage points",
        "82 percentage points",
        "65 percentage points",
        "34 percentage points",
        "86 percentage points"],
      ans=0,
      why="Subtracting the two tabulated shares gives 82 minus 4, which is 78 percentage "
          "points. The rejected values quote the final share alone, pair the wrong generations, "
          "or add the first and last rather than differencing them."),

 dict(q="Why is artificial selection the right description of what happens to a sprayed pest "
        "population, rather than the chemical teaching the pests to survive?",
      choices=[
        "The spraying removes the individuals that cannot survive it and leaves those that "
        "can to reproduce, so the surviving share grows generation by generation.",
        "The spraying alters each individual pest during its own lifetime so that it and "
        "its offspring survive.",
        "The spraying causes the crop to pass a resistance trait to the pests that feed "
        "on it.",
        "The spraying has no effect on which pests reproduce, so any change must come from "
        "the weather.",
        "The spraying reduces the number of generations the pest produces each year."],
      ans=0,
      why="EIN-2.G.1 attributes resistance to ARTIFICIAL SELECTION, which is selection carried "
          "out by human action on which individuals survive to reproduce. The rejected options "
          "describe change within an individual's lifetime, transfer from the crop, or no "
          "selection at all."),

 dict(q="Two plots of the same crop and soil were compared over one season. What do the two "
        "columns show together?",
      table=_T_YIELD,
      choices=[
        "The plot receiving pest control suffered less damage and produced more crop than "
        "the untreated plot.",
        "The plot receiving pest control suffered more damage and produced less crop than "
        "the untreated plot.",
        "The two plots suffered the same damage but differed in the crop produced.",
        "The two plots produced the same crop but differed in the damage suffered.",
        "The plot receiving pest control suffered less damage but produced less crop than "
        "the untreated plot."],
      ans=0,
      why="The treated plot reads 9 percent damage against 38, and 4.8 tonnes per hectare "
          "against 2.4. EIN-2.G.1 states that pest control decreases crop damage by pest and "
          "increases crop yields, and both tabulated columns move that way."),

 dict(q="Using the same two plots, how many times as much crop did the treated plot produce "
        "as the untreated one?",
      table=_T_YIELD,
      choices=[
        "Twice as much",
        "Four times as much",
        "Nine times as much",
        "Half as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated yields gives 4.8 divided by 2.4, which is 2. The rejected "
          "values invert the ratio, use the damage column, or deny that the two differ."),

 dict(q="From the same comparison, by how many percentage points was the share of the crop "
        "damaged reduced?",
      table=_T_YIELD,
      choices=[
        "A reduction of 29 percentage points",
        "A reduction of 38 percentage points",
        "A reduction of 9 percentage points",
        "A reduction of 47 percentage points",
        "A reduction of 24 percentage points"],
      ans=0,
      why="Subtracting the two tabulated damage shares gives 38 minus 9, which is 29 percentage "
          "points. The rejected values quote one of the two shares alone or add them instead of "
          "differencing them."),

 dict(q="What does the framework say genetic engineering can do for a crop?",
      choices=[
        "Increase the crop's resistance to pests and diseases",
        "Increase the pests' resistance to the chemicals sprayed on the crop",
        "Remove the need for any water to be applied to the crop",
        "Guarantee that the crop can never be damaged by any organism",
        "Raise the number of distinct varieties of the crop being planted"],
      ans=0,
      why="EIN-2.G.2 states that crops can be genetically engineered to increase their "
          "resistance to pests and diseases. The second option describes the resistance of "
          "EIN-2.G.1, which belongs to the pest rather than to the crop, and the last reverses "
          "the diversity consequence the same statement gives."),

 dict(q="What drawback does the framework attach to the use of genetically engineered crops?",
      choices=[
        "It can lead to loss of genetic diversity of that particular crop.",
        "It can lead to loss of every crop species grown in the region.",
        "It always raises the amount of pesticide a grower must apply.",
        "It makes the crop unable to reproduce under any conditions.",
        "It has no drawback, according to the framework."],
      ans=0,
      why="EIN-2.G.2 states that using genetically engineered crops in planting or other ways "
          "can lead to loss of genetic diversity of THAT PARTICULAR CROP, which is narrower "
          "than every species in a region. The framework does record a drawback, so the last "
          "option is wrong on its face."),

 dict(q="A district's planting record was compiled before and after engineered seed became "
        "available. What do the values show?",
      table=_T_VARIETIES,
      choices=[
        "The number of distinct varieties fell while the share of the area sown to one "
        "leading variety rose.",
        "The number of distinct varieties rose while the share of the area sown to one "
        "leading variety fell.",
        "Both the number of varieties and the share sown to one leading variety rose.",
        "Both the number of varieties and the share sown to one leading variety fell.",
        "Neither value changed across the three periods recorded."],
      ans=0,
      why="Varieties fall from 34 to 11 to 4 while the share sown to the leading variety rises "
          "from 12 to 58 to 86 percent. EIN-2.G.2 states that using genetically engineered "
          "crops can lead to loss of genetic diversity of that particular crop, and both "
          "columns are measures of that loss."),

 dict(q="Using the same district record, how many distinct varieties were lost over the "
        "twenty years?",
      table=_T_VARIETIES,
      choices=[
        "30 varieties",
        "34 varieties",
        "23 varieties",
        "7 varieties",
        "38 varieties"],
      ans=0,
      why="Subtracting the two tabulated counts gives 34 minus 4, which is 30 varieties. The "
          "rejected values quote the opening count alone, pair the wrong periods, or add the "
          "first and last counts rather than differencing them."),

 dict(q="Four fields were sown with two kinds of seed and the pest damage at harvest was "
        "recorded. Which conclusion is best supported?",
      table=_T_GE,
      choices=[
        "The fields sown with the engineered variety showed much less pest damage than "
        "those sown with the conventional variety.",
        "The fields sown with the engineered variety showed much more pest damage than "
        "those sown with the conventional variety.",
        "All four fields showed about the same pest damage.",
        "The engineered variety showed no pest damage at all in either field.",
        "Only one of the two engineered fields showed less damage than the conventional "
        "fields."],
      ans=0,
      why="The engineered fields read 6 and 8 percent damage against 31 and 27 for the "
          "conventional fields, so both engineered fields fall well below both conventional "
          "ones and neither is at zero. EIN-2.G.2 states that crops can be genetically "
          "engineered to increase their resistance to pests and diseases."),

 dict(q="A grower says that spraying more often will keep the same chemical working "
        "indefinitely. Which framework statement bears against that plan?",
      choices=[
        "Organisms can become resistant to common pest-control methods through "
        "artificial selection.",
        "Pest control decreases crop damage by pest and increases crop yields.",
        "Crops can be genetically engineered to increase their resistance to pests "
        "and diseases.",
        "Using genetically engineered crops can lead to loss of genetic diversity of "
        "that crop.",
        "Integrated pest management reduces the risk that pesticides pose to wildlife."],
      ans=0,
      why="EIN-2.G.1 names resistance through artificial selection as a consequence of USING "
          "the control method, so applying it more often is the pressure that produces the "
          "problem rather than a way round it. The other statements are real framework claims "
          "but none of them speaks to how long one chemical keeps working."),

 dict(q="The dose needed to kill nine tenths of a pest population was recorded through a "
        "spraying programme. What does the record show?",
      table=_T_DOSE,
      choices=[
        "The dose needed rose in every interval, so the same effect required more "
        "chemical over time.",
        "The dose needed fell in every interval, so the same effect required less "
        "chemical over time.",
        "The dose needed was unchanged throughout the programme.",
        "The dose needed rose and then returned to its starting level.",
        "The dose needed cannot be compared between years."],
      ans=0,
      why="The tabulated doses are 40, 90, 220 and 560 grams per hectare, rising with no "
          "reversal. EIN-2.G.1 attributes resistance to common pest-control methods to "
          "artificial selection, and a rising dose for the same kill is that resistance "
          "measured a second way."),

 dict(q="Using the same dose record, how many times as much chemical was needed in the "
        "twelfth year as in the first?",
      table=_T_DOSE,
      choices=[
        "Fourteen times as much",
        "Four times as much",
        "Twenty times as much",
        "Six times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated doses gives 560 divided by 40, which is 14. The rejected "
          "values come from other pairs of years or deny that the dose changed."),

 dict(q="Which of the following correctly separates the two kinds of resistance the framework "
        "discusses in this topic?",
      choices=[
        "The pest becomes resistant to the control method, while the engineered crop is "
        "made resistant to the pest.",
        "The crop becomes resistant to the control method, while the engineered pest is "
        "made resistant to the crop.",
        "Both statements concern the pest's resistance to the crop.",
        "Both statements concern the crop's resistance to the chemical sprayed on it.",
        "The framework describes only one kind of resistance."],
      ans=0,
      why="EIN-2.G.1 makes the resistance a property the ORGANISM acquires to the control "
          "method, and EIN-2.G.2 makes the resistance a property engineered into the CROP "
          "against pests and diseases. The two are different traits in different organisms."),

 dict(q="Three districts growing the same crop met the same new disease. What relationship do "
        "the values show?",
      table=_T_OUTBREAK,
      choices=[
        "Districts growing fewer distinct varieties lost a larger share of the crop to "
        "the disease.",
        "Districts growing fewer distinct varieties lost a smaller share of the crop to "
        "the disease.",
        "The share lost was the same in all three districts.",
        "The district growing the most varieties lost the largest share of the crop.",
        "The number of varieties grown cannot be compared with the share of the crop lost."],
      ans=0,
      why="Varieties run 22, 9 and 3 while the share lost runs 7, 24 and 61 percent, moving in "
          "opposite directions with no reversal. EIN-2.G.2 names loss of genetic diversity of a "
          "particular crop as a consequence of using engineered crops, and these data show why "
          "that loss matters."),

 dict(q="Using the same three districts, how much larger was the share lost in the district "
        "growing the fewest varieties than in the district growing the most?",
      table=_T_OUTBREAK,
      choices=[
        "54 percentage points larger",
        "61 percentage points larger",
        "37 percentage points larger",
        "17 percentage points larger",
        "68 percentage points larger"],
      ans=0,
      why="Subtracting gives 61 minus 7, which is 54 percentage points. The rejected values "
          "quote the largest loss alone, pair the wrong districts, or add the two shares "
          "rather than differencing them."),

 dict(q="Which observation would be the clearest evidence that a pest population has become "
        "resistant in the way the framework describes?",
      choices=[
        "A larger share of the pest population survives the same application of the same "
        "chemical than survived it several generations earlier.",
        "The pest population has grown larger because the weather was warmer this year.",
        "The crop has produced a higher yield than it did in the previous season.",
        "The grower has switched from one chemical to a second chemical.",
        "The number of distinct varieties of the crop planted has fallen."],
      ans=0,
      why="EIN-2.G.1 makes resistance a change in the organisms' ability to survive the control "
          "method, so the diagnostic comparison holds the chemical and the dose fixed and "
          "watches survival over generations. Warmer weather, a higher yield, a change of "
          "chemical and a fall in crop varieties each measure something else."),

 dict(q="A seed company argues that because its engineered variety resists the main pest, a "
        "district that plants only that variety faces no risk from pests or disease. Which "
        "framework statement undercuts the argument?",
      choices=[
        "Using genetically engineered crops can lead to loss of genetic diversity of "
        "that particular crop.",
        "Pest control decreases crop damage by pest and increases crop yields.",
        "Crops can be genetically engineered to increase their resistance to pests "
        "and diseases.",
        "Common pest-control methods include herbicides, fungicides and rodenticides.",
        "Approximately 70 percent of human freshwater consumption is used for agriculture."],
      ans=0,
      why="EIN-2.G.2 concedes the engineered resistance and then adds that planting engineered "
          "crops can lead to loss of genetic diversity of that particular crop, which is the "
          "cost of planting one variety everywhere. The other statements either support the "
          "company's case or belong to different topics."),

 dict(q="Which of the following is the best statement of what the framework counts as a "
        "benefit and what it counts as a drawback of chemical pest control?",
      choices=[
        "The benefit is less crop damage and a larger harvest; the drawback is that the "
        "target organisms can become resistant.",
        "The benefit is that target organisms become resistant; the drawback is less "
        "crop damage.",
        "The benefit is a larger harvest; the drawback is that the crop loses its "
        "genetic diversity.",
        "The benefit is resistance in the crop; the drawback is a smaller harvest.",
        "The framework records a benefit but no drawback for chemical pest control."],
      ans=0,
      why="EIN-2.G.1 gives both sides in one statement: resistance through artificial selection "
          "is the consequence, and decreased crop damage with increased yields is the benefit. "
          "Loss of genetic diversity belongs to engineered crops in EIN-2.G.2 rather than "
          "to chemicals."),

 dict(q="Which combination of measurements would test both halves of the framework's claim "
        "about chemical pest control at once?",
      choices=[
        "The crop harvested per hectare with and without treatment, and the share of the "
        "pest population surviving the treatment over successive generations",
        "The crop harvested per hectare with and without treatment, and the number of "
        "workers employed on the farm",
        "The share of the pest population surviving over generations, and the price of "
        "the chemical",
        "The number of crop varieties planted, and the depth of the water table beneath "
        "the field",
        "The rainfall in the district, and the number of hours of sunshine in the season"],
      ans=0,
      why="EIN-2.G.1 claims a benefit, less damage and higher yields, and a consequence, "
          "resistance through artificial selection, so testing both needs a yield comparison "
          "and a survival trend. Each rejected pair measures at most one of the two."),

 dict(q="A regional programme wants to keep the yield benefit of pest control while slowing "
        "the process the framework warns of. Which measurement should it track to know "
        "whether the process is advancing?",
      choices=[
        "The dose of the chemical needed to achieve the same reduction in the pest "
        "population each year",
        "The total mass of crop harvested from the district each year",
        "The number of farms in the district that own spraying equipment",
        "The share of the district's land under irrigation",
        "The number of days each year on which spraying is permitted by law"],
      ans=0,
      why="EIN-2.G.1 names resistance through artificial selection as the process at issue, and "
          "a rising dose for the same effect is that resistance measured directly. Total "
          "harvest, equipment ownership, irrigated area and permitted days each leave the "
          "resistance unmeasured."),

 dict(q="Which statement about the relationship between the two essential knowledge "
        "statements in this topic is accurate?",
      choices=[
        "Each pairs a benefit with a drawback, one for chemical control and one for "
        "engineered crops.",
        "Each lists only benefits, one for chemical control and one for engineered crops.",
        "Each lists only drawbacks, one for chemical control and one for engineered crops.",
        "The first lists benefits only and the second lists drawbacks only.",
        "The two describe the same method under different names."],
      ans=0,
      why="EIN-2.G.1 pairs resistance through artificial selection with decreased crop damage "
          "and increased yields, and EIN-2.G.2 pairs engineered resistance to pests and "
          "diseases with loss of genetic diversity of that crop. Both statements carry one of "
          "each, which is what the learning objective's phrase benefits and drawbacks asks for."),

 dict(q="A student writes that the framework says engineered crops raise the genetic diversity "
        "of the crop. Which correction is required?",
      choices=[
        "The framework says their use can lead to LOSS of genetic diversity of that "
        "particular crop.",
        "The framework says their use has no effect on the genetic diversity of the crop.",
        "The framework says their use raises the genetic diversity of the pest instead.",
        "The framework makes no statement about genetic diversity in this topic.",
        "The framework says their use raises the genetic diversity of every crop in "
        "the region."],
      ans=0,
      why="EIN-2.G.2 states that using genetically engineered crops in planting or other ways "
          "can lead to LOSS of genetic diversity of that particular crop, so the direction in "
          "the student's sentence is reversed. The framework does address diversity here, and "
          "it limits the claim to the one crop."),

 dict(q="Using the record of survival across generations, in which interval did the share "
        "surviving grow by the largest number of percentage points?",
      table=_T_RESIST,
      choices=[
        "Between the tenth and the fifteenth generation, by 34 percentage points",
        "Between the fifth and the tenth generation, by 31 percentage points",
        "Between the first and the fifth generation, by 13 percentage points",
        "Between the first and the fifth generation, by 34 percentage points",
        "The three intervals show equal growth"],
      ans=0,
      why="The three interval rises are 13, 31 and 34 percentage points, so the largest is the "
          "last one, between the tenth and the fifteenth generation. Two rejected options "
          "report a smaller interval correctly but do not answer which is largest, one attaches "
          "the wrong rise to an interval, and one denies that the rises differ."),

 dict(q="Which of the following applications of the framework to a new case is sound?",
      choices=[
        "A weed population that survives a herbicide more often each year is showing the "
        "resistance the framework attributes to artificial selection.",
        "A weed population that survives a herbicide more often each year is showing the "
        "engineered resistance the framework attributes to crops.",
        "A crop bred to resist a fungus is showing resistance acquired through "
        "artificial selection by the fungus.",
        "A district that plants more varieties each year is showing the loss of genetic "
        "diversity the framework describes.",
        "A grower who applies no pest control at all should expect less crop damage than "
        "one who does."],
      ans=0,
      why="EIN-2.G.1 names herbicides among the common pest-control methods and attributes "
          "resistance in the target organisms to artificial selection, which is exactly the "
          "weed case. The rejected applications swap the two kinds of resistance, reverse the "
          "diversity claim, or reverse the benefit of pest control."),

 dict(q="Which summary states this topic without adding to the framework?",
      choices=[
        "Chemical control cuts damage and raises yields but selects for resistant "
        "organisms, and engineered crops resist pests and diseases but can narrow the "
        "genetic diversity of that crop.",
        "Chemical control cuts damage and raises yields with no consequence, and "
        "engineered crops resist pests with no consequence.",
        "Chemical control raises damage and lowers yields, and engineered crops widen the "
        "genetic diversity of that crop.",
        "Chemical control selects for resistant organisms and lowers yields, and "
        "engineered crops have no effect on pests.",
        "Neither chemical control nor engineered crops has any effect on crop damage."],
      ans=0,
      why="EIN-2.G.1 supplies the resistance consequence together with the decreased damage and "
          "increased yields, and EIN-2.G.2 supplies engineered resistance together with the "
          "loss of genetic diversity of that particular crop. The keyed summary carries all "
          "four claims and the rejected summaries drop or reverse at least one."),
]
