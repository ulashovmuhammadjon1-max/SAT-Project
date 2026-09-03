# AP ENVIRONMENTAL SCIENCE 5.8 Impacts of Overfishing
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding EIN-2: when humans use natural resources, they alter natural
# systems.
# Learning objective EIN-2.J: describe causes of and problems related to overfishing.
# Suggested skill 7.B, describe potential responses or approaches to environmental
# problems.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-2.J.1  Overfishing has led to the extreme scarcity of some fish species, which
#              can lessen biodiversity in aquatic systems and harm people who depend on
#              fishing for food and commerce.
#
# SCOPE, AND WHERE THE CAUSES COME FROM. The learning objective asks for CAUSES as well
# as problems, but EIN-2.J.1 states only problems: extreme scarcity of SOME species,
# lessened biodiversity in aquatic systems, and harm to PEOPLE WHO DEPEND ON FISHING FOR
# FOOD AND COMMERCE. Every item about a cause therefore CHAINS to a framework statement
# that supplies one, and the chain is written out in the claim:
#
#   taking more than the stock replaces -> STB-1.A.2: sustainable yield is the amount of
#                                          a renewable resource that can be taken WITHOUT
#                                          REDUCING THE AVAILABLE SUPPLY. Taking above it
#                                          reduces the supply.
#   why many independent fishers do it  -> EIN-2.A.1: individuals use shared resources in
#                                          their own self-interest rather than in keeping
#                                          with the common good, thereby depleting them.
#
# Nothing else is asserted. In particular no key here names a fish species, a fishing
# gear, a fishery, a quota system or a country, because the framework names none of
# those; and the framework's word is SOME species, not all, so no key says every species
# in a fished system becomes scarce.
#
# BOUNDARY WITH 5.1 AND 5.16. The decision structure of a shared resource is EIN-2.A.1 in
# topic 5.1 and is used here only as a named chain, never as the thing being tested.
# Aquaculture, its efficiency and its escapes and disease are STB-1.F in topic 5.16 and
# appear here only as rejected options.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e5_8.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.8", "Impacts of Overfishing", 5)

_T_STOCK = dict(
    headers=["Decade of the record",
             "Adult fish remaining in the stock (thousand tonnes)",
             "Fish landed by the fleet in the decade (thousand tonnes)"],
    rows=[["First", "900", "120"],
          ["Second", "620", "180"],
          ["Third", "310", "210"],
          ["Fourth", "60", "70"]])

_T_EFFORT = dict(
    headers=["Year of the record", "Days at sea worked by the fleet (thousands)",
             "Fish landed (thousand tonnes)"],
    rows=[["Year 1", "20", "100"],
          ["Year 8", "40", "120"],
          ["Year 16", "60", "90"],
          ["Year 24", "80", "40"]])

_T_SPECIES = dict(
    headers=["Area of the sea surveyed",
             "Fishing pressure applied over twenty years (relative units)",
             "Fish species recorded in the survey"],
    rows=[["Area 1", "1", "44"],
          ["Area 2", "4", "31"],
          ["Area 3", "9", "17"],
          ["Area 4", "16", "8"]])

_T_COMMUNITY = dict(
    headers=["Period", "Fish landed at the port (thousand tonnes)",
             "People employed in fishing and processing at the port"],
    rows=[["Before the decline", "58", "2,400"],
          ["Ten years into the decline", "26", "1,100"],
          ["Twenty years into the decline", "7", "300"]])

_T_YIELD = dict(
    headers=["Management rule applied to the stock",
             "Fish taken each year (thousand tonnes)",
             "Stock remaining after twelve years (thousand tonnes)"],
    rows=[["Take held at the amount the stock replaces", "40", "500"],
          ["Take set above the amount the stock replaces", "90", "70"]])

_T_RECOVERY = dict(
    headers=["Years after the fishery was closed",
             "Adult fish in the stock (thousand tonnes)"],
    rows=[["At closure", "60"],
          ["Five", "140"],
          ["Ten", "290"],
          ["Fifteen", "460"]])

QUESTIONS = [

 dict(q="What does the course framework say overfishing has led to?",
      choices=[
        "The extreme scarcity of some fish species",
        "The extinction of every fish species in the ocean",
        "A rise in the abundance of every fish species that is caught",
        "A permanent increase in the number of people employed in fishing",
        "The complete replacement of wild fisheries by fish farms"],
      ans=0,
      why="EIN-2.J.1 states that overfishing has led to the extreme scarcity of SOME fish "
          "species. The framework's word is some rather than all, and it claims scarcity "
          "rather than global extinction or a rise in abundance."),

 dict(q="Which two further consequences does the framework attach to that scarcity?",
      choices=[
        "It can lessen biodiversity in aquatic systems and harm people who depend on "
        "fishing for food and commerce.",
        "It can raise biodiversity in aquatic systems and harm people who depend on "
        "fishing for food and commerce.",
        "It can lessen biodiversity in aquatic systems and benefit people who depend on "
        "fishing for food and commerce.",
        "It can raise biodiversity in aquatic systems and benefit people who depend on "
        "fishing for food and commerce.",
        "It has no consequences beyond the scarcity of the species themselves."],
      ans=0,
      why="EIN-2.J.1 states that the extreme scarcity of some fish species can lessen "
          "biodiversity in aquatic systems and harm people who depend on fishing for food and "
          "commerce. Each rejected option reverses one or both directions, or denies that the "
          "framework names anything further."),

 dict(q="A stock was monitored over four decades while it was fished. What do the values "
        "show?",
      table=_T_STOCK,
      choices=[
        "The stock remaining fell in every decade, and in the last decade the catch was "
        "larger than what was left.",
        "The stock remaining rose in every decade, and the catch fell throughout.",
        "The stock remaining was unchanged while the catch rose.",
        "The catch fell in every decade while the stock remaining rose.",
        "The catch and the stock remaining were equal in every decade."],
      ans=0,
      why="The stock runs 900, 620, 310 and 60 thousand tonnes while the catch runs 120, 180, "
          "210 and 70, so the stock falls without a reversal and the final catch of 70 exceeds "
          "the 60 left. EIN-2.J.1 records the extreme scarcity of some fish species as the "
          "result of overfishing."),

 dict(q="Using the same record, how much of the stock was lost between the first and the "
        "fourth decade?",
      table=_T_STOCK,
      choices=[
        "840 thousand tonnes",
        "900 thousand tonnes",
        "590 thousand tonnes",
        "250 thousand tonnes",
        "960 thousand tonnes"],
      ans=0,
      why="Subtracting the two tabulated stock values gives 900 minus 60, which is 840 thousand "
          "tonnes. The rejected values quote the opening stock alone, pair the wrong decades, "
          "or add the first and last rather than differencing them."),

 dict(q="A fleet's effort and landings were recorded over twenty-four years. What does the "
        "pattern show?",
      table=_T_EFFORT,
      choices=[
        "Effort rose throughout, but landings rose and then fell, so more work was "
        "producing less fish by the end.",
        "Effort rose throughout and landings rose throughout, so more work was producing "
        "more fish by the end.",
        "Effort fell throughout while landings rose throughout.",
        "Effort and landings were both unchanged across the record.",
        "Landings were highest in the year of greatest effort."],
      ans=0,
      why="Days at sea run 20, 40, 60 and 80 thousand while landings run 100, 120, 90 and 40 "
          "thousand tonnes, so effort rises without a reversal while landings peak and then "
          "fall to below their starting value. EIN-2.J.1 records the extreme scarcity of some "
          "fish species as the result of overfishing."),

 dict(q="Using the same record, what happened to the fish landed for each thousand days at "
        "sea between the first year and the last?",
      table=_T_EFFORT,
      choices=[
        "It fell from 5 thousand tonnes per thousand days to 0.5 thousand tonnes per "
        "thousand days.",
        "It rose from 0.5 thousand tonnes per thousand days to 5 thousand tonnes per "
        "thousand days.",
        "It stayed at 5 thousand tonnes per thousand days throughout.",
        "It fell from 5 thousand tonnes per thousand days to 3 thousand tonnes per "
        "thousand days.",
        "It cannot be worked out, because the table reports no effort."],
      ans=0,
      why="Dividing landings by days at sea gives 100 over 20, which is 5, in the first year "
          "and 40 over 80, which is 0.5, in the last, a fall of a factor of ten. That falling "
          "return for the same work is the extreme scarcity EIN-2.J.1 describes, measured "
          "against effort."),

 dict(q="Four areas of sea were surveyed after twenty years of different fishing pressure. "
        "What do the values show?",
      table=_T_SPECIES,
      choices=[
        "Areas under heavier fishing pressure recorded fewer fish species.",
        "Areas under heavier fishing pressure recorded more fish species.",
        "All four areas recorded the same number of fish species.",
        "The area under the heaviest pressure recorded the most species.",
        "Fishing pressure and species number cannot be compared across areas."],
      ans=0,
      why="Pressure runs 1, 4, 9 and 16 relative units while species recorded run 44, 31, 17 "
          "and 8, moving in opposite directions with no reversal. EIN-2.J.1 states that the "
          "extreme scarcity of some fish species can lessen biodiversity in aquatic systems."),

 dict(q="Using the same survey, how many more species were recorded in the least fished area "
        "than in the most heavily fished one?",
      table=_T_SPECIES,
      choices=[
        "36 more species",
        "44 more species",
        "27 more species",
        "9 more species",
        "52 more species"],
      ans=0,
      why="Subtracting the two tabulated counts gives 44 minus 8, which is 36 species. The "
          "rejected values quote the largest count alone, pair the wrong areas, or add the two "
          "counts rather than differencing them."),

 dict(q="A fishing port recorded its landings and its employment through a long decline. "
        "Which conclusion does the framework support?",
      table=_T_COMMUNITY,
      choices=[
        "Falling landings were accompanied by falling employment, which is the harm to "
        "people dependent on fishing that the framework names.",
        "Falling landings were accompanied by rising employment, so no harm to dependent "
        "people occurred.",
        "Landings fell but employment was unchanged, so the framework's claim about people "
        "does not apply.",
        "Employment fell but landings were unchanged, so the cause must lie outside "
        "the fishery.",
        "Neither landings nor employment changed over the period recorded."],
      ans=0,
      why="Landings run 58, 26 and 7 thousand tonnes while employment runs 2,400, 1,100 and 300 "
          "people, both falling without a reversal. EIN-2.J.1 states that the scarcity brought "
          "on by overfishing can harm people who depend on fishing for food and commerce."),

 dict(q="Using the same port record, how many jobs in fishing and processing were lost "
        "across the twenty years?",
      table=_T_COMMUNITY,
      choices=[
        "2,100 jobs",
        "2,400 jobs",
        "1,300 jobs",
        "800 jobs",
        "2,700 jobs"],
      ans=0,
      why="Subtracting the two tabulated employment counts gives 2,400 minus 300, which is "
          "2,100 jobs. The rejected values quote the opening count alone, pair the wrong "
          "periods, or add the first and last rather than differencing them."),

 dict(q="Which framework statement supplies the standard against which a catch counts as "
        "too large?",
      choices=[
        "Sustainable yield is the amount of a renewable resource that can be taken without "
        "reducing the available supply.",
        "Aquaculture is highly efficient, requires only small areas of water, and requires "
        "little fuel.",
        "Eutrophication occurs when a body of water is enriched in nutrients.",
        "A rain shadow is a region of land made drier because higher ground blocks "
        "precipitation.",
        "Impervious surfaces do not allow water to reach the soil, leading to flooding."],
      ans=0,
      why="STB-1.A.2 defines sustainable yield as the amount of a renewable resource that can "
          "be taken WITHOUT REDUCING THE AVAILABLE SUPPLY, so a catch that reduces the supply "
          "is above that amount. The rejected statements are STB-1.F.1, STB-3.F.1, ENG-2.B.2 "
          "and EIN-2.M.3, none of which concerns how much may be taken."),

 dict(q="Two stocks of the same species were managed under different rules for twelve years. "
        "What does the comparison show?",
      table=_T_YIELD,
      choices=[
        "The stock fished at the amount it replaces was left far larger than the stock "
        "fished above that amount.",
        "The stock fished above the amount it replaces was left far larger than the stock "
        "fished at that amount.",
        "The two stocks were left the same size after twelve years.",
        "Both stocks were reduced to nothing after twelve years.",
        "The stock fished above the amount it replaces yielded no fish at all."],
      ans=0,
      why="The stock held to its replacement rate is left with 500 thousand tonnes against 70 "
          "for the stock fished above it, on takes of 40 and 90 thousand tonnes a year. "
          "STB-1.A.2 makes the sustainable yield the amount that can be taken without reducing "
          "the available supply."),

 dict(q="Using the same two rules, how much larger is the stock left under the sustainable "
        "rule after twelve years?",
      table=_T_YIELD,
      choices=[
        "Larger by 430 thousand tonnes",
        "Larger by 500 thousand tonnes",
        "Larger by 70 thousand tonnes",
        "Larger by 50 thousand tonnes",
        "Larger by 570 thousand tonnes"],
      ans=0,
      why="Subtracting the two tabulated remaining stocks gives 500 minus 70, which is 430 "
          "thousand tonnes. The rejected values quote one remaining stock alone, use the "
          "difference in annual takes, or add the two remaining stocks."),

 dict(q="Why do many independent boats fishing one open stock tend to take more than the "
        "stock can replace, according to the framework's own account of shared resources?",
      choices=[
        "Each boat gains the whole value of what it lands while the cost of the reduced "
        "stock falls on every boat, so self-interest points away from the common good.",
        "Each boat bears the whole cost of the reduced stock, so restraint is the "
        "obvious choice.",
        "Each boat is unaware that other boats are fishing the same stock.",
        "Each boat is legally required to land as much fish as it can.",
        "Each boat gains nothing from landing more fish, so the outcome must have "
        "another cause."],
      ans=0,
      why="EIN-2.A.1 states that individuals will use shared resources in their own "
          "self-interest rather than in keeping with the common good, thereby depleting the "
          "resources, and the division of the cost across all users is what makes that so. The "
          "rejected options concentrate the cost on one user or replace the incentive with "
          "ignorance or a legal duty."),

 dict(q="A stock was measured for fifteen years after its fishery was closed. What do the "
        "values show?",
      table=_T_RECOVERY,
      choices=[
        "The stock grew in every interval after the closure, though it had not returned "
        "to a large size within five years.",
        "The stock fell in every interval after the closure.",
        "The stock was unchanged in every interval after the closure.",
        "The stock returned to its original size within five years of the closure.",
        "The stock grew and then fell back to its size at closure."],
      ans=0,
      why="The stock runs 60, 140, 290 and 460 thousand tonnes at closure and after five, ten "
          "and fifteen years, rising without a reversal and still below its final value at the "
          "five-year mark. EIN-2.J.1 records the scarcity that follows overfishing, and this is "
          "what removing the pressure does to it."),

 dict(q="Using the same recovery record, how many times as large was the stock after fifteen "
        "years as at the moment of closure?",
      table=_T_RECOVERY,
      choices=[
        "About eight times as large",
        "About two times as large",
        "About five times as large",
        "About fifteen times as large",
        "The same size"],
      ans=0,
      why="Dividing the two tabulated stocks gives 460 divided by 60, which is about 7.7 and "
          "rounds to about eight. The rejected values come from earlier points in the same "
          "record, from the number of years, or from denying that the stock changed."),

 dict(q="Which of the following is the clearest sign that a fishery is being overfished in "
        "the sense the framework describes?",
      choices=[
        "The same fishing effort lands less fish year after year while the stock "
        "keeps falling.",
        "The same fishing effort lands more fish year after year while the stock "
        "keeps rising.",
        "The number of boats in the fleet has fallen while landings have risen.",
        "The price of fish at market has risen while landings have risen.",
        "The number of fish farms in the region has risen."],
      ans=0,
      why="EIN-2.J.1 ties overfishing to the extreme scarcity of some fish species, and "
          "STB-1.A.2 makes the sustainable amount the one that can be taken without reducing "
          "the available supply, so a falling stock alongside a falling return for the same "
          "work is the diagnostic pair. Fish farming is STB-1.F, a different topic."),

 dict(q="A report says that because only three of the twenty species in a bay have become "
        "scarce, overfishing cannot be responsible. How does the framework bear on "
        "that reasoning?",
      choices=[
        "It undercuts the reasoning, because the framework says overfishing has led to the "
        "extreme scarcity of SOME fish species rather than all of them.",
        "It supports the reasoning, because the framework says overfishing makes every "
        "species scarce at once.",
        "It supports the reasoning, because the framework says overfishing cannot affect "
        "species number.",
        "It undercuts the reasoning, because the framework says overfishing always drives "
        "species to extinction.",
        "It is silent on the reasoning, because the framework does not discuss scarcity."],
      ans=0,
      why="EIN-2.J.1 says overfishing has led to the extreme scarcity of SOME fish species, so "
          "a mixed picture across a bay is exactly what the framework describes rather than "
          "evidence against it. The framework claims scarcity, not extinction of all species."),

 dict(q="A coastal town's food supply and its main export both come from one fishery. Which "
        "part of the framework's statement applies most directly to that town?",
      choices=[
        "The harm to people who depend on fishing for food and commerce",
        "The lessening of biodiversity in aquatic systems",
        "The extreme scarcity of some fish species considered on its own",
        "The definition of sustainable yield",
        "The description of aquaculture as efficient and low in fuel use"],
      ans=0,
      why="EIN-2.J.1 names harm to PEOPLE WHO DEPEND ON FISHING FOR FOOD AND COMMERCE, and the "
          "town depends on the fishery for both. The other options name the framework's other "
          "consequences or belong to STB-1.A.2 and STB-1.F.1."),

 dict(q="Which measurement would show most directly the effect on biodiversity that the "
        "framework names?",
      choices=[
        "The number of fish species recorded in repeated surveys of the same area",
        "The total mass of fish landed by the fleet each year",
        "The price paid for fish at the dockside each year",
        "The number of days the fleet spends at sea each year",
        "The average length of the boats in the fleet"],
      ans=0,
      why="EIN-2.J.1 says the scarcity can LESSEN BIODIVERSITY IN AQUATIC SYSTEMS, and a count "
          "of species present in repeated surveys is the direct measure of that. Landings, "
          "price, effort and boat size each measure the fishery rather than the diversity of "
          "the system."),

 dict(q="Using the survey of four sea areas, what is the ratio of species recorded in the "
        "least fished area to species recorded in the most heavily fished area?",
      table=_T_SPECIES,
      choices=[
        "About eleven to two",
        "About two to eleven",
        "About one to one",
        "About sixteen to one",
        "About three to one"],
      ans=0,
      why="The two tabulated counts are 44 and 8 species, and 44 to 8 reduces to 11 to 2. The "
          "rejected values invert the ratio, use the fishing pressure column, or deny that the "
          "two areas differ."),

 dict(q="Which response to overfishing follows most directly from the framework's own "
        "definition of a sustainable take?",
      choices=[
        "Limit the annual catch to an amount the stock can replace, so the available "
        "supply is not reduced.",
        "Raise the annual catch so that more fish are landed before the stock declines "
        "further.",
        "Leave the annual catch unregulated so that each boat can decide for itself.",
        "Move the fleet to a second stock and fish it at the same rate as the first.",
        "Increase the number of days each boat spends at sea."],
      ans=0,
      why="STB-1.A.2 defines sustainable yield as the amount of a renewable resource that can "
          "be taken without reducing the available supply, so holding the catch at that amount "
          "is what the definition prescribes. Each rejected option raises the take, moves it, "
          "or leaves it to the self-interested choice EIN-2.A.1 describes."),

 dict(q="Which pair of measurements would best test whether a stock is being taken above the "
        "amount it can replace?",
      choices=[
        "The mass taken from the stock each year, and the mass of the stock remaining at "
        "the end of each year",
        "The mass taken from the stock each year, and the price of fish that year",
        "The mass of the stock remaining, and the number of fish farms in the region",
        "The number of boats in the fleet, and the average age of their crews",
        "The water temperature at the fishing grounds, and the depth of the water there"],
      ans=0,
      why="STB-1.A.2 defines the sustainable amount as the one that does not reduce the "
          "available supply, so the test compares what is taken with what remains from year to "
          "year. Price, fish farms, crew age and water conditions leave one side of that "
          "comparison unmeasured."),

 dict(q="Using the four-decade stock record, in which decade did the catch first exceed the "
        "stock left at the end of the decade?",
      table=_T_STOCK,
      choices=[
        "The fourth decade, when 70 thousand tonnes were landed and 60 thousand "
        "tonnes remained",
        "The first decade, when 120 thousand tonnes were landed and 900 thousand "
        "tonnes remained",
        "The second decade, when 180 thousand tonnes were landed and 620 thousand "
        "tonnes remained",
        "The third decade, when 210 thousand tonnes were landed and 310 thousand "
        "tonnes remained",
        "In no decade did the catch exceed the stock remaining"],
      ans=0,
      why="Comparing the two columns decade by decade, the catch stays below the stock "
          "remaining in the first three decades and exceeds it only in the fourth, 70 against "
          "60 thousand tonnes. EIN-2.J.1 records extreme scarcity as the outcome of "
          "overfishing, and this is that point reached."),

 dict(q="A minister argues that landings from the national fleet have never been higher, so "
        "the stock must be healthy. Which reading of the effort record answers that "
        "argument?",
      table=_T_EFFORT,
      choices=[
        "Landings must be read against the effort that produced them, and here effort "
        "quadrupled while landings ended below their starting value.",
        "Landings must be read on their own, and here they ended above their "
        "starting value.",
        "Effort must be read on its own, and here it fell across the record.",
        "Landings and effort tell the same story, since both rose steadily "
        "across the record.",
        "Neither landings nor effort can indicate anything about the state of a stock."],
      ans=0,
      why="Days at sea rise from 20 to 80 thousand while landings fall from 100 to 40 thousand "
          "tonnes, so four times the work produces less than half the fish. That falling return "
          "for rising effort is the scarcity EIN-2.J.1 describes, which a raw landings total "
          "conceals."),

 dict(q="What does the framework's statement imply about a fishing community after the "
        "species it targets has become extremely scarce?",
      choices=[
        "The community can be harmed in both its food supply and its commerce.",
        "The community is harmed in its commerce but never in its food supply.",
        "The community is harmed in its food supply but never in its commerce.",
        "The community is unaffected, because the framework restricts the harm to "
        "the ecosystem.",
        "The community benefits, because scarce fish command a higher price."],
      ans=0,
      why="EIN-2.J.1 names harm to people who depend on fishing FOR FOOD AND COMMERCE, which "
          "covers both. The framework does not restrict the harm to one of the two, nor confine "
          "the consequences to the ecosystem."),

 dict(q="Which of the following correctly distinguishes the ecological consequence the "
        "framework names from the human one?",
      choices=[
        "The ecological consequence is lessened biodiversity in aquatic systems; the human "
        "one is harm to people who depend on fishing for food and commerce.",
        "The ecological consequence is harm to people who fish; the human one is lessened "
        "biodiversity in aquatic systems.",
        "Both consequences the framework names are ecological.",
        "Both consequences the framework names are human.",
        "The framework names one consequence only."],
      ans=0,
      why="EIN-2.J.1 puts lessened biodiversity in aquatic systems and harm to people who "
          "depend on fishing for food and commerce side by side, one about the system and one "
          "about the people. The rejected options swap them or collapse the pair."),

 dict(q="Using the port record, what fraction of its original employment did the port retain "
        "after twenty years?",
      table=_T_COMMUNITY,
      choices=[
        "One eighth of it",
        "One half of it",
        "One quarter of it",
        "Three quarters of it",
        "All of it"],
      ans=0,
      why="Dividing the two tabulated employment counts gives 300 over 2,400, which is one "
          "eighth. The rejected fractions correspond to other pairs of periods or deny that "
          "employment changed."),

 dict(q="Which observation would most weaken a claim that a particular stock's decline was "
        "caused by overfishing rather than by something else?",
      choices=[
        "The stock declined by the same amount in a neighbouring area where no fishing "
        "was permitted.",
        "The stock declined in the years when the fleet worked the most days at sea.",
        "The number of species recorded in the area fell as the stock declined.",
        "The port's employment fell as the stock declined.",
        "The stock recovered after the fishery was closed."],
      ans=0,
      why="If an unfished area declined by the same amount, the fishing is not doing the work "
          "the claim assigns it. The other four observations are consistent with the claim: "
          "EIN-2.J.1 links overfishing to scarcity, lessened biodiversity and harm to dependent "
          "people, and a recovery after closure points the same way."),

 dict(q="Which summary states this topic exactly as the framework does?",
      choices=[
        "Overfishing has made some fish species extremely scarce, which can lessen aquatic "
        "biodiversity and harm people who depend on fishing for food and commerce.",
        "Overfishing has made every fish species extinct, which has raised aquatic "
        "biodiversity and benefited fishing communities.",
        "Overfishing has made some fish species extremely scarce, with no consequence for "
        "aquatic systems or for people.",
        "Overfishing has raised the abundance of some fish species, which has lessened "
        "aquatic biodiversity.",
        "Overfishing affects only the fish and never the communities that catch them."],
      ans=0,
      why="EIN-2.J.1 states that overfishing has led to the extreme scarcity of some fish "
          "species, which can lessen biodiversity in aquatic systems and harm people who depend "
          "on fishing for food and commerce. Each rejected summary reverses a direction, drops "
          "a consequence, or strengthens scarcity into extinction."),
]
