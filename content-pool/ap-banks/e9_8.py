# AP ENVIRONMENTAL SCIENCE 9.8 Invasive Species
# CED effective Fall 2026, Unit 9 Global Change.
# Enduring understanding EIN-4: The health of a species is closely tied to its ecosystem,
# and minor environmental changes can have a large impact.
# Learning objective EIN-4.A: explain the environmental problems associated with invasive
# species and strategies to control them. Suggested skill 7.E, make a claim that proposes
# a solution to an environmental problem in an applied context.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-4.A.1  Invasive species are species that can live, and sometimes thrive, outside
#              of their normal habitat. Invasive species can sometimes be beneficial, but
#              they are considered invasive when they threaten native species.
#   EIN-4.A.2  Invasive species are often generalist, r-selected species and therefore may
#              outcompete native species for resources.
#   EIN-4.A.3  Invasive species can be controlled through a variety of human interventions.
#
# EIN-4.A.3 NAMES NO INTERVENTION. It says only that invasive species can be controlled
# through a variety of human interventions, and the framework supplies no list of them
# anywhere in this unit. So NO KEY HERE NAMES A CONTROL METHOD -- not trapping, not
# biological control, not herbicide. Item 8 keys exactly that absence, and the data item
# 25 reads the effect of an unnamed intervention from its own record rather than crediting
# a method the framework never states.
#
# THE CRITERION IS THE THREAT TO NATIVE SPECIES, NOT THE MOVE ITSELF. EIN-4.A.1 defines an
# invasive species as one that can live and sometimes thrive outside its normal habitat,
# then makes the label turn on whether it threatens native species, and allows outright
# that such a species can sometimes be beneficial. Items 9, 10, 12, 13, 20, 27, 28 and 29
# all turn on keeping those three clauses apart: living elsewhere is not the criterion,
# being beneficial does not exempt a species from it, and a species can be both beneficial
# and a threat at once.
#
# THE HEDGES ARE KEPT. EIN-4.A.2 says OFTEN generalist and r-selected and MAY outcompete,
# so item 6 keys the hedges rather than hardening either into a rule.
#
# NO FIGURES ARE REFERENCED. Every record is supplied as a table.
#
# BOUNDARIES. What r-selected and generalist mean, and which native species are most
# adversely affected, are ERT-3.A and ERT-3.B (topics 3.1 and 3.2); the island case, where
# introduced generalists outcompete island specialists, is ERT-2.E.1 (topic 2.3). No key
# here defines either category or restates the island case, and no item is set on an
# island. HIPPCO, which lists invasive species among the causes of biodiversity loss, is
# EIN-4.C.1 (topic 9.10).
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("9.8", "Invasive Species", 9)

_T_RANGE = dict(
    headers=["Introduced species",
             "Survival in the new range (percent of individuals in the first year)",
             "Population after twenty years, as a multiple of the number released"],
    rows=[["Species 1", "94", "310"],
          ["Species 2", "71", "58"],
          ["Species 3", "44", "6"],
          ["Species 4", "12", "0.3"]])

_T_INTRODUCED = dict(
    headers=["Introduced species",
             "Percent change in the introduced population over ten years",
             "Percent change in the native species sharing its resources"],
    rows=[["Species 1", "820", "-64"],
          ["Species 2", "410", "-38"],
          ["Species 3", "60", "-9"],
          ["Species 4", "15", "3"]])

_T_TRAITS = dict(
    headers=["Introduced species", "Number of different food types it eats",
             "Offspring produced in a year", "Age at first reproduction (months)"],
    rows=[["Species A", "18", "2,400", "3"],
          ["Species B", "14", "900", "6"],
          ["Species C", "3", "40", "36"],
          ["Species D", "2", "12", "60"]])

_T_RESOURCE = dict(
    headers=["Site", "Density of the introduced species (individuals per hectare)",
             "Share of the shared food taken by the introduced species (percent)",
             "Density of the native species (individuals per hectare)"],
    rows=[["Site 1", "5", "12", "88"],
          ["Site 2", "22", "37", "54"],
          ["Site 3", "51", "68", "26"],
          ["Site 4", "84", "89", "7"]])

_T_CONTROL = dict(
    headers=["Stage of one control programme", "Years of intervention completed",
             "Area still occupied by the introduced species (hectares)",
             "Native species recorded in that area"],
    rows=[["Stage 1", "1", "9,400", "12"],
          ["Stage 2", "3", "6,100", "17"],
          ["Stage 3", "6", "2,800", "24"],
          ["Stage 4", "10", "700", "31"]])

_T_BENEFIT = dict(
    headers=["Introduced species", "Crop it pollinates (tonnes each year)",
             "Percent change in the native species sharing its habitat"],
    rows=[["Species P", "4,200", "1"],
          ["Species Q", "3,100", "-52"],
          ["Species R", "0", "-47"],
          ["Species S", "0", "3"]])

QUESTIONS = [

 dict(q="What does the framework say invasive species are?",
      choices=[
        "Species that can live, and sometimes thrive, outside of their normal habitat.",
        "Species that can live only within their normal habitat.",
        "Species that have been bred by people for economic return.",
        "Species that are threatened with extinction in their normal habitat.",
        "Species that occupy the largest territories in an ecosystem."],
      ans=0,
      why="EIN-4.A.1 states that invasive species are species that can live, and sometimes "
          "thrive, outside of their normal habitat, which is where the definition begins."),

 dict(q="When does the framework say such a species is considered invasive?",
      choices=[
        "When it threatens native species.",
        "As soon as it is found outside its normal habitat, whatever else happens.",
        "Only when it produces no benefit of any kind.",
        "Only when it is the most abundant species present.",
        "Only when it has been introduced deliberately rather than by accident."],
      ans=0,
      why="EIN-4.A.1 states that invasive species can sometimes be beneficial, but that "
          "they are considered invasive when they threaten native species, which makes the "
          "threat the criterion rather than the move or the abundance."),

 dict(q="What does the framework allow that an invasive species can sometimes be?",
      choices=[
        "Beneficial.",
        "Native to the habitat it has entered.",
        "Incapable of living outside its normal habitat.",
        "Immune to every human intervention.",
        "The only species present in an ecosystem."],
      ans=0,
      why="EIN-4.A.1 states outright that invasive species can sometimes be beneficial, "
          "before adding that they are considered invasive when they threaten native "
          "species."),

 dict(q="What kind of species does the framework say invasive species often are?",
      choices=[
        "Generalist, r-selected species.",
        "Specialist, K-selected species.",
        "Species with the largest territorial requirements in the ecosystem.",
        "Species that have been domesticated for economic return.",
        "Species found only in polar regions."],
      ans=0,
      why="EIN-4.A.2 states that invasive species are often generalist, r-selected "
          "species, which is the pairing the keyed option gives and the reverse of the "
          "pairing in the rejected one."),

 dict(q="What does the framework say may follow from invasive species being of that kind?",
      choices=[
        "They may outcompete native species for resources.",
        "They may be outcompeted by native species for resources.",
        "They may be unable to reproduce in the new habitat.",
        "They may raise the number of native species present.",
        "They may become dependent on a single native species for food."],
      ans=0,
      why="EIN-4.A.2 states that invasive species are often generalist, r-selected species "
          "and therefore may outcompete native species for resources, which puts the "
          "competitive advantage on the introduced side."),

 dict(q="EIN-4.A.2 says invasive species are OFTEN generalist and r-selected and that they "
        "MAY outcompete native species. What does that wording establish?",
      choices=[
        "A tendency and a possibility rather than a rule holding in every case.",
        "A rule that holds without exception for every invasive species.",
        "A claim the framework treats as unlikely.",
        "A claim about native species rather than about introduced ones.",
        "A claim that applies only where the two kinds of species eat the same food."],
      ans=0,
      why="The hedges OFTEN and MAY in EIN-4.A.2 mark the profile as usual rather than "
          "universal and the outcompeting as possible rather than certain, so neither is a "
          "rule and neither is dismissed."),

 dict(q="What does the framework say about controlling invasive species?",
      choices=[
        "They can be controlled through a variety of human interventions.",
        "They cannot be controlled once they are established.",
        "They can be controlled only by removing the native species that compete with "
        "them.",
        "They control themselves once resources run short.",
        "They can be controlled only in their normal habitat."],
      ans=0,
      why="EIN-4.A.3 states that invasive species can be controlled through a variety of "
          "human interventions, which is the whole of what the framework says about "
          "control in this topic."),

 dict(q="Which of those human interventions does the framework itself name?",
      choices=[
        "None; it refers to a variety of human interventions and names no particular one.",
        "Trapping and hunting, which it names as the two available methods.",
        "The release of a predator of the introduced species.",
        "The application of chemicals to the affected area.",
        "The removal of the native species that compete with the introduced one."],
      ans=0,
      why="EIN-4.A.3 states only that invasive species can be controlled through a variety "
          "of human interventions. It lists none of them, so no particular method can be "
          "keyed to the framework in this topic."),

 dict(q="A student writes that any species found living outside its normal habitat is "
        "invasive. What is the clearest correction from the framework?",
      choices=[
        "The framework reserves the label for species that threaten native species.",
        "The framework applies the label to every species found outside its normal "
        "habitat, so the student is right.",
        "The framework applies the label only to species that produce no benefit.",
        "The framework applies the label only to species introduced on purpose.",
        "The framework gives no criterion for the label at all."],
      ans=0,
      why="EIN-4.A.1 opens with the ability to live outside the normal habitat but then "
          "makes the label turn on threatening native species, so living elsewhere is the "
          "setting rather than the criterion."),

 dict(q="A student writes that an invasive species can never do any good. What is the "
        "clearest correction from the framework?",
      choices=[
        "The framework states that invasive species can sometimes be beneficial.",
        "The framework states that invasive species are never beneficial, so the student "
        "is right.",
        "The framework states that invasive species are beneficial in every case.",
        "The framework makes no statement about whether they can be beneficial.",
        "The framework states that only native species can be beneficial."],
      ans=0,
      why="EIN-4.A.1 states that invasive species can sometimes be beneficial, so a claim "
          "that they never are contradicts the statement, while a claim that they always "
          "are overshoots the word SOMETIMES."),

 dict(q="Which of these does the framework NOT claim in this topic?",
      choices=[
        "An invasive species cannot be controlled once it is established.",
        "Invasive species can live, and sometimes thrive, outside their normal habitat.",
        "Invasive species are considered invasive when they threaten native species.",
        "Invasive species are often generalist, r-selected species.",
        "Invasive species can be controlled through a variety of human interventions."],
      ans=0,
      why="EIN-4.A.3 states the opposite of the keyed option, that invasive species can be "
          "controlled through a variety of human interventions, and the other three "
          "rejected options restate EIN-4.A.1 and EIN-4.A.2."),

 dict(q="A plant carried to a new region spreads widely there, and after twenty years no "
        "native population has declined. What does the framework's criterion give?",
      choices=[
        "It is living outside its normal habitat, but the criterion for calling it "
        "invasive, a threat to native species, has not been met.",
        "It is invasive, because it is living outside its normal habitat.",
        "It is invasive, because it has spread widely.",
        "It is not living outside its normal habitat, since it has established itself "
        "there.",
        "The framework offers no way to judge the case."],
      ans=0,
      why="EIN-4.A.1 makes threatening native species the condition under which a species "
          "is considered invasive, and this account reports the spread without that "
          "threat."),

 dict(q="An introduced beetle pollinates a valuable crop and, over the same years, drives "
        "a native beetle to the edge of extinction. What does the framework's criterion "
        "give?",
      choices=[
        "It is considered invasive, because it threatens a native species, and the benefit "
        "it brings does not exempt it.",
        "It is not considered invasive, because the benefit it brings exempts it.",
        "It is not considered invasive, because a species can be either beneficial or "
        "invasive but not both.",
        "It is considered invasive only if the crop it pollinates is a native plant.",
        "The framework treats the two effects as cancelling one another out."],
      ans=0,
      why="EIN-4.A.1 allows that invasive species can sometimes be beneficial and still "
          "makes them considered invasive when they threaten native species, so the two "
          "clauses stand together rather than cancelling."),

 dict(q="Why does the framework connect the profile it attributes to invasive species with "
        "their effect on natives?",
      choices=[
        "Because it says they are often generalist and r-selected and therefore may "
        "outcompete native species for resources.",
        "Because it says they are often specialist and K-selected and therefore need less "
        "food than natives.",
        "Because it says they always eat the same food as the native species.",
        "Because it says they cannot reproduce unless native species are removed first.",
        "Because it says the profile makes them easier for people to control."],
      ans=0,
      why="EIN-4.A.2 states the profile and the consequence in one sentence, joined by "
          "THEREFORE: invasive species are often generalist, r-selected species and "
          "therefore may outcompete native species for resources."),

 dict(q="Which evidence would show most directly that an introduced species meets the "
        "framework's criterion for being invasive?",
      choices=[
        "Records showing native species declining alongside the spread of the introduced "
        "species.",
        "Records showing the introduced species surviving its first winter.",
        "Records showing the introduced species eating more than one kind of food.",
        "Records showing the introduced species producing many offspring each year.",
        "Records showing the value of the crop the introduced species pollinates."],
      ans=0,
      why="EIN-4.A.1 makes the threat to native species the condition under which a species "
          "is considered invasive, so evidence of that threat is what bears on the "
          "criterion, rather than evidence of survival, diet or benefit."),

 dict(q="Which observations would test EIN-4.A.3's claim most directly?",
      choices=[
        "Records of the area an introduced species occupies before and during a programme "
        "of human intervention.",
        "Records of the number of food types the introduced species eats.",
        "Records of the offspring the introduced species produces each year.",
        "Records of how far the introduced species travelled from its normal habitat.",
        "Records of the crop the introduced species pollinates."],
      ans=0,
      why="EIN-4.A.3 asserts that invasive species can be controlled through human "
          "interventions, so the evidence bearing on it follows what an intervention does "
          "to the species rather than describing its diet, its reproduction or its "
          "origin."),

 dict(q="Four introduced species were followed in their new ranges. What does the record "
        "establish?",
      table=_T_RANGE,
      choices=[
        "Some merely persisted in the new range while others multiplied many times over.",
        "Every one of the four multiplied many times over in the new range.",
        "Every one of the four fell below the number released.",
        "The species with the lowest first year survival multiplied the most.",
        "First year survival and the eventual population are unrelated in this record."],
      ans=0,
      why="Sorting the species by first year survival leaves the eventual multiple "
          "strictly increasing, and the column runs from well below one to several "
          "hundred. EIN-4.A.1 states that invasive species can live, and sometimes thrive, "
          "outside of their normal habitat."),

 dict(q="Which of those four introduced species thrived most in its new range?",
      table=_T_RANGE,
      choices=[
        "Species 1, whose population reached the largest multiple of the number released.",
        "Species 4, whose population fell below the number released.",
        "Species 3, whose first year survival was the second lowest.",
        "Species 2, whose first year survival was the second highest.",
        "All four thrived to the same extent."],
      ans=0,
      why="The largest entry in the multiple column belongs to one species alone, and it "
          "is also the species with the highest first year survival. EIN-4.A.1 distinguishes "
          "living outside the normal habitat from thriving there."),

 dict(q="Four introduced species were recorded alongside the native species sharing their "
        "resources. What does the record establish?",
      table=_T_INTRODUCED,
      choices=[
        "The introduced species that grew most are the ones alongside the largest native "
        "declines.",
        "The introduced species that grew most are the ones alongside the largest native "
        "increases.",
        "Growth in the introduced species and change in the native species are unrelated "
        "here.",
        "Every native species in the record declined.",
        "Every native species in the record increased."],
      ans=0,
      why="Sorting the introduced species by their growth leaves the change in the native "
          "species strictly falling. EIN-4.A.2 states that invasive species may outcompete "
          "native species for resources."),

 dict(q="By the framework's criterion, which of those four introduced species would NOT be "
        "considered invasive on this record?",
      table=_T_INTRODUCED,
      choices=[
        "Species 4, the only one alongside which the native species did not decline.",
        "Species 1, alongside which the native species declined most.",
        "Species 2, alongside which the native species declined second most.",
        "Species 3, whose own growth was the second smallest.",
        "All four would be considered invasive, since all four grew."],
      ans=0,
      why="EIN-4.A.1 makes a species considered invasive when it threatens native species, "
          "and exactly one row of this record shows no decline in the native species "
          "sharing its resources."),

 dict(q="Four introduced species were measured for diet, offspring and age at first "
        "reproduction. What does the record establish?",
      table=_T_TRAITS,
      choices=[
        "The species eating the widest range of foods also produce the most offspring and "
        "breed youngest.",
        "The species eating the widest range of foods produce the fewest offspring and "
        "breed latest.",
        "Diet, offspring and age at first reproduction vary independently in this record.",
        "Every one of the four eats the same number of food types.",
        "Every one of the four first reproduces at the same age."],
      ans=0,
      why="Sorting the species by the number of food types they eat leaves the offspring "
          "count rising and the age at first reproduction falling. EIN-4.A.2 states that "
          "invasive species are often generalist, r-selected species."),

 dict(q="Which of those four best fits the profile the framework says invasive species "
        "often carry?",
      table=_T_TRAITS,
      choices=[
        "Species A, which eats the widest range of foods, produces the most offspring and "
        "breeds youngest.",
        "Species D, which eats the narrowest range of foods, produces the fewest offspring "
        "and breeds latest.",
        "Species B, which stands second on all three measures.",
        "Species C, which stands third on all three measures.",
        "None of the four, because the framework gives no profile."],
      ans=0,
      why="EIN-4.A.2 states that invasive species are often generalist, r-selected "
          "species, and one row of this record leads on the breadth of diet and on the "
          "reproductive measures at once."),

 dict(q="Four sites were recorded for the density of an introduced species, the share of "
        "the shared food it takes and the density of the native species. What does the "
        "record establish?",
      table=_T_RESOURCE,
      choices=[
        "Where the introduced species is denser it takes a larger share of the food and "
        "the native species is scarcer.",
        "Where the introduced species is denser it takes a smaller share of the food and "
        "the native species is commoner.",
        "The density of the introduced species and the share of food it takes are "
        "unrelated here.",
        "The native species is at the same density at all four sites.",
        "The introduced species takes the same share of the food at all four sites."],
      ans=0,
      why="Sorting the sites by the density of the introduced species leaves the share of "
          "food it takes rising and the native density falling. EIN-4.A.2 states that "
          "invasive species may outcompete native species for resources."),

 dict(q="At which of those four sites is the native species scarcest?",
      table=_T_RESOURCE,
      choices=[
        "Site 4, where the introduced species is densest and takes the largest share of "
        "the food.",
        "Site 1, where the introduced species is least dense and takes the smallest share "
        "of the food.",
        "Site 2, where the introduced species stands second from the bottom on both "
        "measures.",
        "Site 3, where the introduced species stands third on both measures.",
        "The native species is equally scarce at all four sites."],
      ans=0,
      why="The smallest native density, the largest introduced density and the largest "
          "share of food taken all fall in the same row, which is the pattern EIN-4.A.2's "
          "outcompeting for resources describes."),

 dict(q="One control programme was recorded at four stages. What does the record "
        "establish?",
      table=_T_CONTROL,
      choices=[
        "As the intervention continued the area occupied by the introduced species fell "
        "and the native species recorded rose.",
        "As the intervention continued the area occupied by the introduced species rose "
        "and the native species recorded fell.",
        "The area occupied fell while the native species recorded stayed the same.",
        "The native species recorded rose while the area occupied stayed the same.",
        "Neither the area occupied nor the native species recorded changed."],
      ans=0,
      why="Reading down the columns in stage order, the area occupied falls at every stage "
          "and the native count rises at every stage. EIN-4.A.3 states that invasive "
          "species can be controlled through a variety of human interventions, and this "
          "record follows one such programme without naming its method."),

 dict(q="Across that same programme, by how much did the area occupied by the introduced "
        "species fall?",
      table=_T_CONTROL,
      choices=[
        "By 8,700 hectares.",
        "By 700 hectares.",
        "By 9,400 hectares.",
        "By 3,300 hectares.",
        "By 2,100 hectares."],
      ans=0,
      why="The first and last entries in the area column are subtracted. EIN-4.A.3 states "
          "that invasive species can be controlled through human interventions, and this "
          "is the size of the reduction the record reports."),

 dict(q="Four introduced species were recorded for a crop they pollinate and for the "
        "native species sharing their habitat. What does the record establish?",
      table=_T_BENEFIT,
      choices=[
        "One of the four brings a benefit and is nevertheless accompanied by a heavy "
        "decline in the native species.",
        "Every species bringing a benefit is accompanied by a rise in the native species.",
        "Every species bringing no benefit is accompanied by a rise in the native species.",
        "All four bring a benefit of some size.",
        "All four are accompanied by a decline in the native species."],
      ans=0,
      why="Two rows of the record pollinate a crop and two do not, and the decline in "
          "native species does not follow that split. EIN-4.A.1 states that invasive "
          "species can sometimes be beneficial but are considered invasive when they "
          "threaten native species, so the two properties are separate."),

 dict(q="Which of those four species brings a benefit and would still be considered "
        "invasive on the framework's criterion?",
      table=_T_BENEFIT,
      choices=[
        "Species Q, which pollinates a crop and is accompanied by a heavy native decline.",
        "Species P, which pollinates a crop and is accompanied by no native decline.",
        "Species R, which pollinates no crop and is accompanied by a heavy native decline.",
        "Species S, which pollinates no crop and is accompanied by no native decline.",
        "None of the four, because a species that brings a benefit is never considered "
        "invasive."],
      ans=0,
      why="EIN-4.A.1 makes the threat to native species the criterion and allows that an "
          "invasive species can sometimes be beneficial, so the species meeting both "
          "descriptions is the one that pollinates a crop and is accompanied by a fall in "
          "the native species."),

 dict(q="And which of those four brings no benefit and would not be considered invasive on "
        "that criterion either?",
      table=_T_BENEFIT,
      choices=[
        "Species S, which pollinates no crop and is accompanied by no native decline.",
        "Species P, which pollinates the largest crop of the four.",
        "Species Q, which pollinates a crop and is accompanied by a heavy native decline.",
        "Species R, which pollinates no crop and is accompanied by a heavy native decline.",
        "None of the four, because every introduced species threatens native species."],
      ans=0,
      why="EIN-4.A.1 ties the label to threatening native species, so a row with no crop "
          "pollinated and no fall in the native species meets neither the benefit nor the "
          "criterion."),

 dict(q="Which single sentence collects what this topic's three statements assert and "
        "nothing further?",
      choices=[
        "Invasive species can live, and sometimes thrive, outside their normal habitat; "
        "they can sometimes be beneficial but are considered invasive when they threaten "
        "native species; they are often generalist, r-selected species and may therefore "
        "outcompete natives for resources; and they can be controlled through a variety of "
        "human interventions.",
        "Invasive species can live only within their normal habitat; they are never "
        "beneficial; they are often specialist, K-selected species; and they cannot be "
        "controlled once established.",
        "Invasive species are any species found outside their normal habitat, whatever "
        "their effect, and the framework names the interventions used to control them.",
        "Invasive species are considered invasive when they bring no benefit, and the "
        "framework says nothing about how they compete with native species.",
        "Invasive species always outcompete native species for resources, and no human "
        "intervention has any effect on them."],
      ans=0,
      why="EIN-4.A.1 supplies the definition, the possible benefit and the criterion, "
          "EIN-4.A.2 the usual profile and the possible outcompeting, and EIN-4.A.3 the "
          "control through a variety of human interventions. No statement names an "
          "intervention or hardens either hedge into a rule."),
]
