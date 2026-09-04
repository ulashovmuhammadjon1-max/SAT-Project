# AP ENVIRONMENTAL SCIENCE 3.2 K-Selected r-Selected Species
# CED effective Fall 2026, Unit 3 Populations.
# Enduring understanding ERT-3: populations change over time in reaction to a variety of
# factors.
# Learning objective ERT-3.B: identify differences between K- and r-selected species.
# Suggested skill 5.A, describe patterns or trends in data.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-3.B.1  K-selected species tend to be large, have few offspring per reproduction
#              event, live in stable environments, expend significant energy for each
#              offspring, mature after many years of extended youth and parental care, have
#              long life spans and life expectancy, and reproduce more than once in their
#              lifetime. Competition for resources in K-selected species' habitats is
#              usually relatively high.
#   ERT-3.B.2  r-selected species tend to be small, have many offspring, expend or invest
#              minimal energy for each offspring, mature early, have short life spans, and
#              may reproduce only once in their lifetime. Competition for resources in
#              r-selected species' habitats is typically relatively low.
#   ERT-3.B.3  Biotic potential refers to the maximum reproductive rate of a population in
#              ideal conditions.
#   ERT-3.B.4  Many species have reproductive strategies that are not uniquely r-selected or
#              K-selected, or they change in different conditions at different times.
#   ERT-3.B.5  K-selected species are typically more adversely affected by invasive species
#              than r-selected species, which are minimally affected by invasive species.
#              Most invasive species are r-selected species.
#
# THE TWO PROFILES ARE MIRROR IMAGES, WHICH MAKES THE SWAP THE STANDING HAZARD. Every
# distractor set that names both kinds contains the reversed statement, so the anchors in
# verify_e3_2.py for items 5, 6, 7, 8, 9, 15, 20 and 22 carry BOTH clauses -- which kind and
# which trait. Half an anchor matches the swap as readily as the key; that defect was found
# once already in verify_e2_1.py.
#
# ERT-3.B.4 IS NOT AN AFTERTHOUGHT AND IS KEYED TWICE. Many species are not uniquely one or
# the other, and a species' strategy can change in different conditions at different times.
# So no key here says a species must be one kind or the other, and items 13, 14, 28 and 29
# turn on exactly that.
#
# WHAT IS DELIBERATELY NOT ASKED. The framework gives no formula for biotic potential, no
# survivorship curve (that is ERT-3.C in topic 3.3) and no carrying capacity (ERT-3.D in
# topic 3.4). ERT-3.B.5 is stated with TYPICALLY and MOST, and no key hardens either.
#
# NO FIGURES. Every quantitative item carries a table=, recomputed in verify_e3_2.py from
# that table alone.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("3.2", "K-Selected r-Selected Species", 3)

_T_TRAITS = dict(
    headers=["Species", "Adult mass (kilograms)", "Offspring per reproduction event",
             "Age at maturity (years)", "Typical life span (years)"],
    rows=[["Species 1", "1200", "1", "6", "40"],
          ["Species 2", "0.02", "3000", "0.2", "1"],
          ["Species 3", "300", "2", "4", "28"],
          ["Species 4", "0.5", "400", "0.5", "2"]])

_T_COMPETITION = dict(
    headers=["Habitat surveyed", "Competition for resources (index)",
             "Species with the K-selected profile present",
             "Species with the r-selected profile present"],
    rows=[["Habitat 1", "9", "14", "3"],
          ["Habitat 2", "6", "10", "6"],
          ["Habitat 3", "3", "5", "12"],
          ["Habitat 4", "1", "2", "19"]])

_T_INVASIVE = dict(
    headers=["Native species", "Reproductive strategy recorded for it",
             "Percent decline in its numbers after the invasive species arrived"],
    rows=[["Native 1", "K-selected", "62"],
          ["Native 2", "K-selected", "48"],
          ["Native 3", "r-selected", "6"],
          ["Native 4", "r-selected", "3"]])

_T_INVORIGIN = dict(
    headers=["Survey of invasive species in one region",
             "Number classified as r-selected", "Number classified as K-selected"],
    rows=[["Survey 1", "41", "6"],
          ["Survey 2", "33", "4"],
          ["Survey 3", "27", "3"]])

_T_BIOTIC = dict(
    headers=["Population",
             "Maximum offspring per female per year under ideal conditions",
             "Offspring per female per year recorded in the field"],
    rows=[["Population 1", "900", "120"],
          ["Population 2", "14", "5"],
          ["Population 3", "2", "1"]])

_T_MIXED = dict(
    headers=["Species", "Offspring per reproduction event",
             "Energy invested per offspring (relative units)", "Age at maturity (years)"],
    rows=[["Species X", "250", "1", "5"],
          ["Species Y", "2", "90", "1"]])

_T_CHANGE = dict(
    headers=["Condition the same species was kept under",
             "Offspring per reproduction event",
             "Energy invested per offspring (relative units)"],
    rows=[["Crowded, with resources scarce", "3", "70"],
          ["Uncrowded, with resources abundant", "40", "6"]])

QUESTIONS = [

 dict(q="Which set of tendencies does the framework attach to K-selected species?",
      choices=[
        "Large, few offspring per reproduction event, significant energy expended for each "
        "offspring, and long life spans.",
        "Small, many offspring per reproduction event, minimal energy expended for each "
        "offspring, and short life spans.",
        "Large, many offspring per reproduction event, minimal energy expended for each "
        "offspring, and long life spans.",
        "Small, few offspring per reproduction event, significant energy expended for each "
        "offspring, and short life spans.",
        "Large, few offspring per reproduction event, minimal energy expended for each "
        "offspring, and short life spans."],
      ans=0,
      why="ERT-3.B.1 states that K-selected species tend to be large, have few offspring per "
          "reproduction event, expend significant energy for each offspring and have long "
          "life spans. Each rejected set exchanges at least one of those four for its "
          "opposite."),

 dict(q="Which set of tendencies does the framework attach to r-selected species?",
      choices=[
        "Small, many offspring, minimal energy invested for each offspring, and short life "
        "spans.",
        "Large, few offspring, significant energy invested for each offspring, and long life "
        "spans.",
        "Small, few offspring, minimal energy invested for each offspring, and long life "
        "spans.",
        "Large, many offspring, minimal energy invested for each offspring, and long life "
        "spans.",
        "Small, many offspring, significant energy invested for each offspring, and long "
        "life spans."],
      ans=0,
      why="ERT-3.B.2 states that r-selected species tend to be small, have many offspring, "
          "expend or invest minimal energy for each offspring and have short life spans. "
          "Each rejected set exchanges at least one of those four for its opposite."),

 dict(q="What does the framework say about competition for resources in the habitats of "
        "K-selected species?",
      choices=[
        "It is usually relatively high.",
        "It is usually relatively low.",
        "It is absent altogether.",
        "It varies with no usual level.",
        "It is higher only where the habitat is unstable."],
      ans=0,
      why="ERT-3.B.1 closes by stating that competition for resources in K-selected species' "
          "habitats is usually relatively high. The word usually makes it a prevailing "
          "level rather than a rule."),

 dict(q="What does the framework say about competition for resources in the habitats of "
        "r-selected species?",
      choices=[
        "It is typically relatively low.",
        "It is typically relatively high.",
        "It is absent altogether.",
        "It is the same as in K-selected species' habitats.",
        "It is low only where the habitat is stable."],
      ans=0,
      why="ERT-3.B.2 closes by stating that competition for resources in r-selected species' "
          "habitats is typically relatively low, which is the opposite of the level "
          "ERT-3.B.1 gives for K-selected habitats."),

 dict(q="How do the two strategies differ in the number of offspring produced per "
        "reproduction event?",
      choices=[
        "K-selected species tend to have few offspring and r-selected species many.",
        "K-selected species tend to have many offspring and r-selected species few.",
        "Both tend to have few offspring per reproduction event.",
        "Both tend to have many offspring per reproduction event.",
        "The framework makes no claim about offspring number for either kind."],
      ans=0,
      why="ERT-3.B.1 gives K-selected species few offspring per reproduction event and "
          "ERT-3.B.2 gives r-selected species many. The rejected options exchange the two, "
          "collapse them together, or deny that the framework addresses offspring number."),

 dict(q="How do the two strategies differ in the energy spent on each offspring?",
      choices=[
        "K-selected species expend significant energy for each offspring and r-selected "
        "species minimal energy.",
        "K-selected species expend minimal energy for each offspring and r-selected species "
        "significant energy.",
        "Both expend significant energy for each offspring.",
        "Both expend minimal energy for each offspring.",
        "The framework makes no claim about energy per offspring for either kind."],
      ans=0,
      why="ERT-3.B.1 has K-selected species expend significant energy for each offspring and "
          "ERT-3.B.2 has r-selected species expend or invest minimal energy for each. The "
          "rejected options exchange or collapse the two."),

 dict(q="How do the two strategies differ in the age at which individuals mature?",
      choices=[
        "K-selected species mature after many years of extended youth and parental care, "
        "while r-selected species mature early.",
        "K-selected species mature early, while r-selected species mature after many years "
        "of extended youth and parental care.",
        "Both mature early in life.",
        "Both mature only after many years of parental care.",
        "The framework makes no claim about the age of maturity for either kind."],
      ans=0,
      why="ERT-3.B.1 has K-selected species mature after many years of extended youth and "
          "parental care and ERT-3.B.2 has r-selected species mature early. The rejected "
          "options exchange or collapse the two."),

 dict(q="How do the two strategies differ in life span?",
      choices=[
        "K-selected species tend to have long life spans and r-selected species short ones.",
        "K-selected species tend to have short life spans and r-selected species long ones.",
        "Both tend to have long life spans.",
        "Both tend to have short life spans.",
        "The framework makes no claim about life span for either kind."],
      ans=0,
      why="ERT-3.B.1 gives K-selected species long life spans and life expectancy and "
          "ERT-3.B.2 gives r-selected species short life spans. The rejected options "
          "exchange or collapse the two."),

 dict(q="How do the two strategies differ in how often an individual reproduces during its "
        "lifetime?",
      choices=[
        "K-selected species reproduce more than once, while r-selected species may reproduce "
        "only once.",
        "K-selected species may reproduce only once, while r-selected species reproduce more "
        "than once.",
        "Both reproduce exactly once in a lifetime.",
        "Both reproduce more than once in a lifetime.",
        "The framework makes no claim about how often either kind reproduces."],
      ans=0,
      why="ERT-3.B.1 states that K-selected species reproduce more than once in their "
          "lifetime and ERT-3.B.2 states that r-selected species may reproduce only once. "
          "The rejected options exchange or collapse the two."),

 dict(q="What kind of environment does the framework say K-selected species live in?",
      choices=[
        "Stable environments.",
        "Environments that change from year to year.",
        "Environments with no competition for resources.",
        "Environments that have recently been disturbed.",
        "Environments where no other species is present."],
      ans=0,
      why="ERT-3.B.1 states outright that K-selected species live in stable environments, "
          "and it separately gives their habitats a usually high level of competition for "
          "resources."),

 dict(q="What does the framework say biotic potential refers to?",
      choices=[
        "The maximum reproductive rate of a population in ideal conditions.",
        "The number of offspring a population actually produces in the field.",
        "The largest population an environment can support.",
        "The proportion of offspring that reach maturity.",
        "The rate at which a population loses individuals to predators."],
      ans=0,
      why="ERT-3.B.3 states that biotic potential refers to the maximum reproductive rate of "
          "a population in ideal conditions. It is a maximum under ideal conditions rather "
          "than an observed rate or an environmental limit."),

 dict(q="ERT-3.B.3 defines biotic potential under IDEAL CONDITIONS. What follows from that "
        "phrase?",
      choices=[
        "A population in the field will generally reproduce at less than its biotic "
        "potential.",
        "A population in the field will generally reproduce faster than its biotic "
        "potential.",
        "Biotic potential can only be measured in the field.",
        "Biotic potential is the same for every population.",
        "Biotic potential changes with the number of predators present."],
      ans=0,
      why="ERT-3.B.3 makes biotic potential a MAXIMUM reached under IDEAL conditions, so a "
          "population meeting conditions less than ideal cannot exceed it and will in "
          "general fall short of it."),

 dict(q="What does the framework say about species whose reproductive strategies do not fit "
        "either category cleanly?",
      choices=[
        "Many species have strategies that are not uniquely r-selected or K-selected.",
        "Every species is either uniquely r-selected or uniquely K-selected.",
        "Only invasive species fail to fit one of the two categories.",
        "Only species living on islands fail to fit one of the two categories.",
        "Species that do not fit either category have no reproductive strategy."],
      ans=0,
      why="ERT-3.B.4 states that many species have reproductive strategies that are not "
          "uniquely r-selected or K-selected. The categories are therefore not a partition "
          "of all species, and the exception is not confined to any one group."),

 dict(q="What else does ERT-3.B.4 say a species' reproductive strategy may do?",
      choices=[
        "Change in different conditions at different times.",
        "Remain fixed from the moment the species arises.",
        "Change only when the species becomes invasive.",
        "Change only in response to a rise in predation.",
        "Change only once during a species' existence."],
      ans=0,
      why="ERT-3.B.4 states that many species have strategies that are not uniquely "
          "r-selected or K-selected, OR that they change in different conditions at "
          "different times. The second clause allows one species' strategy to differ between "
          "occasions."),

 dict(q="Which kind of species does the framework say is typically more adversely affected "
        "by invasive species?",
      choices=[
        "K-selected species, while r-selected species are minimally affected.",
        "r-selected species, while K-selected species are minimally affected.",
        "Both kinds equally.",
        "Neither kind, because invasive species affect only plants.",
        "K-selected species, and r-selected species are affected almost as much."],
      ans=0,
      why="ERT-3.B.5 states that K-selected species are typically more adversely affected by "
          "invasive species than r-selected species, which are minimally affected. The "
          "rejected options exchange the two kinds, level them, or deny the difference."),

 dict(q="What does the framework say about the reproductive strategy of invasive species "
        "themselves?",
      choices=[
        "Most invasive species are r-selected species.",
        "Most invasive species are K-selected species.",
        "Invasive species are equally divided between the two strategies.",
        "Invasive species have no reproductive strategy of either kind.",
        "Every invasive species is r-selected without exception."],
      ans=0,
      why="ERT-3.B.5 states that most invasive species are r-selected species. The word most "
          "makes it a majority rather than a rule without exceptions."),

 dict(q="Four species were measured for size, offspring number, age at maturity and life "
        "span. Which two carry the profile the framework gives K-selected species?",
      table=_T_TRAITS,
      choices=[
        "The first and the third species",
        "The second and the fourth species",
        "The first and the second species",
        "The third and the fourth species",
        "All four species carry it"],
      ans=0,
      why="Two of the four are heavy, produce one or two offspring per event, mature after "
          "several years and live for decades, while the other two are light, produce "
          "hundreds or thousands of offspring, mature within a year and live a year or two. "
          "ERT-3.B.1 gives K-selected species the first of those profiles."),

 dict(q="Which of those four species fits the r-selected profile most completely?",
      table=_T_TRAITS,
      choices=["Species 2", "Species 1", "Species 3", "Species 4",
               "None of the four fits it"],
      ans=0,
      why="One species is the lightest, produces the most offspring per event, matures "
          "earliest and lives the shortest life of the four. ERT-3.B.2 gives r-selected "
          "species exactly that combination of small size, many offspring, early maturity "
          "and a short life span."),

 dict(q="In that record, how many times as many offspring per reproduction event does the "
        "most fecund species produce as the least fecund one?",
      table=_T_TRAITS,
      choices=["Three thousand times", "Three hundred times", "Thirty times",
               "Four hundred times", "Twice"],
      ans=0,
      why="The largest offspring count in the record is 3,000 and the smallest is 1, so the "
          "ratio is 3,000. The rejected values are other entries in the same column or "
          "ratios between other pairs of rows."),

 dict(q="Four habitats were scored for competition and for the two kinds of species present. "
        "What do the two right hand columns establish?",
      table=_T_COMPETITION,
      choices=[
        "Species with the K-selected profile are commoner where competition is higher, and "
        "species with the r-selected profile where it is lower.",
        "Species with the r-selected profile are commoner where competition is higher, and "
        "species with the K-selected profile where it is lower.",
        "Both kinds are commoner where competition is higher.",
        "Both kinds are commoner where competition is lower.",
        "Neither kind varies with the level of competition."],
      ans=0,
      why="Ordered by the competition index the K-profile counts run 2, 5, 10 and 14 while "
          "the r-profile counts run 19, 12, 6 and 3. ERT-3.B.1 gives K-selected species' "
          "habitats a usually high level of competition and ERT-3.B.2 gives r-selected "
          "species' habitats a typically low one."),

 dict(q="Which of those habitats holds the most species with the r-selected profile?",
      table=_T_COMPETITION,
      choices=["Habitat 4", "Habitat 1", "Habitat 2", "Habitat 3",
               "All four hold the same number"],
      ans=0,
      why="The r-profile counts are 3, 6, 12 and 19, and the largest belongs to the habitat "
          "with the lowest competition index. ERT-3.B.2 states that competition in "
          "r-selected species' habitats is typically relatively low."),

 dict(q="Four native species of known strategy were followed after an invasive species "
        "arrived. What does the record establish?",
      table=_T_INVASIVE,
      choices=[
        "The K-selected natives declined far more than the r-selected natives.",
        "The r-selected natives declined far more than the K-selected natives.",
        "The two strategies declined by about the same amount.",
        "Neither strategy declined at all.",
        "Only the r-selected natives declined."],
      ans=0,
      why="The two K-selected natives fell by 62 and 48 percent while the two r-selected "
          "natives fell by 6 and 3 percent. ERT-3.B.5 states that K-selected species are "
          "typically more adversely affected by invasive species than r-selected species, "
          "which are minimally affected."),

 dict(q="In that record, by how many percentage points does the largest decline exceed the "
        "smallest?",
      table=_T_INVASIVE,
      choices=["59 points", "62 points", "56 points", "45 points", "3 points"],
      ans=0,
      why="The largest decline recorded is 62 percent and the smallest is 3 percent, and 62 "
          "less 3 is 59. The rejected values are the endpoints themselves or differences "
          "between other pairs of rows."),

 dict(q="Three surveys classified the invasive species found in one region. What does the "
        "record establish?",
      table=_T_INVORIGIN,
      choices=[
        "In every survey most of the invasive species were r-selected.",
        "In every survey most of the invasive species were K-selected.",
        "The two strategies were equally represented in every survey.",
        "No invasive species in any survey was r-selected.",
        "Only the first survey found any r-selected invasive species."],
      ans=0,
      why="The surveys record 41 against 6, 33 against 4 and 27 against 3, so the "
          "r-selected classification is the majority in each. ERT-3.B.5 states that most "
          "invasive species are r-selected species."),

 dict(q="Taking those three surveys together, how do the two classifications compare in "
        "total?",
      table=_T_INVORIGIN,
      choices=[
        "101 r-selected against 13 K-selected",
        "13 r-selected against 101 K-selected",
        "57 r-selected against 57 K-selected",
        "41 r-selected against 6 K-selected",
        "The totals cannot be formed from the record"],
      ans=0,
      why="Adding the columns gives 41 plus 33 plus 27, which is 101, and 6 plus 4 plus 3, "
          "which is 13. The rejected options reverse the two totals, level them, or give "
          "one survey's figures instead of the totals."),

 dict(q="Three populations were measured for their maximum reproductive rate under ideal "
        "conditions and for the rate actually recorded in the field. What does the record "
        "establish?",
      table=_T_BIOTIC,
      choices=[
        "Every population reproduced more slowly in the field than its ideal maximum.",
        "Every population reproduced faster in the field than its ideal maximum.",
        "The field rate and the ideal maximum were equal in every population.",
        "Only the largest population fell short of its ideal maximum.",
        "The record does not report a field rate for any population."],
      ans=0,
      why="The ideal maxima are 900, 14 and 2 offspring per female per year and the field "
          "rates 120, 5 and 1, so each field rate is the smaller of its pair. ERT-3.B.3 "
          "makes biotic potential the MAXIMUM reproductive rate under IDEAL conditions, "
          "which conditions in the field do not meet."),

 dict(q="Which of those three populations has the highest biotic potential as the framework "
        "defines it?",
      table=_T_BIOTIC,
      choices=["Population 1", "Population 2", "Population 3",
               "All three have the same biotic potential",
               "The record does not report biotic potential"],
      ans=0,
      why="ERT-3.B.3 defines biotic potential as the maximum reproductive rate under ideal "
          "conditions, which is the first of the two columns, and the largest entry there is "
          "900 offspring per female per year. The field column is a different quantity."),

 dict(q="Two species were measured for offspring number, energy invested per offspring and "
        "age at maturity. What does the record establish?",
      table=_T_MIXED,
      choices=[
        "Neither species carries a wholly r-selected or a wholly K-selected set of traits.",
        "Both species carry a wholly r-selected set of traits.",
        "Both species carry a wholly K-selected set of traits.",
        "One species is wholly r-selected and the other wholly K-selected.",
        "Neither species' traits were recorded."],
      ans=0,
      why="One species produces 250 offspring and invests almost nothing in each, which are "
          "r-selected tendencies, yet matures only after five years, which is a K-selected "
          "one; the other pairs two offspring and heavy investment with maturity within a "
          "year. ERT-3.B.4 states that many species have reproductive strategies that are "
          "not uniquely r-selected or K-selected."),

 dict(q="One species was kept under two sets of conditions and its reproduction measured "
        "under each. What does the record establish?",
      table=_T_CHANGE,
      choices=[
        "The same species produced few, heavily provisioned offspring under one set of "
        "conditions and many, lightly provisioned ones under the other.",
        "The same species produced many, heavily provisioned offspring under both sets of "
        "conditions.",
        "The same species produced few, lightly provisioned offspring under both sets of "
        "conditions.",
        "The species produced the same number of offspring under both sets of conditions.",
        "The species did not reproduce under either set of conditions."],
      ans=0,
      why="Under crowded, resource-poor conditions the species produced 3 offspring with 70 "
          "units invested in each, and under uncrowded, resource-rich conditions 40 "
          "offspring with 6 units each. ERT-3.B.4 states that reproductive strategies may "
          "change in different conditions at different times."),

 dict(q="Which single sentence collects what this topic's statements assert and nothing "
        "further?",
      choices=[
        "K-selected species tend to be large, slow to mature, long-lived and few in "
        "offspring in stable, competitive habitats, r-selected species the reverse in "
        "less competitive ones; biotic potential is the ideal-conditions maximum; many "
        "species fit neither category cleanly; and invasive species, mostly r-selected, "
        "affect K-selected natives more.",
        "K-selected species tend to be small, quick to mature and many in offspring, "
        "r-selected species the reverse; biotic potential is the rate recorded in the "
        "field; every species fits one category; and invasive species affect r-selected "
        "natives more.",
        "K-selected species tend to be large, slow to mature, long-lived and few in "
        "offspring in stable, competitive habitats, r-selected species the reverse; biotic "
        "potential is the ideal-conditions maximum; every species fits one of the two "
        "categories exactly; and invasive species affect both kinds equally.",
        "K-selected species tend to be large, slow to mature, long-lived and few in "
        "offspring, r-selected species the reverse; biotic potential is the largest "
        "population a habitat can hold; many species fit neither category cleanly; and most "
        "invasive species are K-selected.",
        "K-selected species tend to be large, slow to mature, long-lived and few in "
        "offspring in stable, competitive habitats, r-selected species the reverse in less "
        "competitive ones; biotic potential is the ideal-conditions maximum; many species "
        "fit neither category cleanly; and invasive species, mostly K-selected, affect "
        "r-selected natives more."],
      ans=0,
      why="ERT-3.B.1 and ERT-3.B.2 supply the two mirrored profiles and their competition "
          "levels, ERT-3.B.3 supplies the ideal-conditions maximum, ERT-3.B.4 supplies the "
          "species that fit neither, and ERT-3.B.5 supplies both the greater harm to "
          "K-selected natives and the r-selected majority among invaders. Each rejected "
          "summary swaps a profile, redefines biotic potential, makes the categories "
          "exhaustive, or reverses one half of the invasive-species claim."),
]
