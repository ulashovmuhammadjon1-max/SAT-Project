# AP ENVIRONMENTAL SCIENCE 2.3 Island Biogeography
# CED effective Fall 2026, Unit 2 The Living World: Biodiversity.
# Enduring understanding ERT-2: ecosystems have structure and diversity that change over
# time.
# Learning objectives ERT-2.D, describe island biogeography, and ERT-2.E, describe the
# role of island biogeography in evolution. Suggested skill 1.A.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-2.D.1  Island biogeography is the study of the ecological relationships and
#              distribution of organisms on islands, and of these organisms' community
#              structures.
#   ERT-2.D.2  Islands have been colonized in the past by new species arriving from
#              elsewhere.
#   ERT-2.E.1  Many island species have evolved to be specialists versus generalists
#              because of the limited resources, such as food and territory, on most
#              islands. The long-term survival of specialists may be jeopardized if and
#              when invasive species, typically generalists, are introduced and outcompete
#              the specialists.
#
# THIS IS THE ISLAND CASE, AND IT IS DELIBERATELY THE ONE 2.1 LEFT ALONE. Topic 2.1 uses
# only ERT-2.A.4's ordering of losses under habitat loss and says in its own header that
# the island specialist-versus-generalist case is ERT-2.E.1 and belongs here. Which of the
# two kinds is advantaged in a constant or a changing habitat is ERT-3.A.1 and belongs to
# topic 3.1; nothing here reaches into it, and no item here is about habitat fragments.
#
# THE FRAMEWORK NEVER DEFINES SPECIALIST OR GENERALIST, so no item asks a student to sort
# a species into one of the two from its diet or its range. The two words are used here
# only as the framework uses them, as labels on counts.
#
# WHAT ELSE IS NOT ASSERTED. The framework gives no species-area rule, no distance rule
# and no equilibrium between arrival and extinction. Where a table shows species rising
# with area or falling with distance, the keyed conclusion is a reading OF THAT TABLE and
# the claim says so; ERT-2.D.1 supplies only that the distribution of organisms on islands
# is what the field studies.
#
# NAMED CHAIN. EIN-4.A.1 defines an invasive species as one that can live outside its
# normal habitat and is considered invasive when it threatens native species, and
# EIN-4.A.2 states that invasive species are often generalist, r-selected species and may
# therefore outcompete native species for resources. Those belong to unit 9 and are used
# here only where a claim names the chain, in item 29.
#
# ERT-2.E.1's hedges are load-bearing: MANY island species, MOST islands, TYPICALLY
# generalists, MAY be jeopardized IF AND WHEN introduced. Items 8, 9, 10 and 27 turn on
# them and no key anywhere hardens one into a certainty.
#
# NO FIGURES. Every quantitative item carries a table=, recomputed in verify_e2_3.py from
# that table alone.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("2.3", "Island Biogeography", 2)

_T_AREA = dict(
    headers=["Island in one group", "Land area (square kilometres)",
             "Resident bird species recorded"],
    rows=[["Island 1", "4", "6"],
          ["Island 2", "30", "14"],
          ["Island 3", "240", "27"],
          ["Island 4", "1900", "49"]])

_T_DISTANCE = dict(
    headers=["Island surveyed", "Distance from the mainland (kilometres)",
             "Plant species present that also grow on the mainland"],
    rows=[["Island A", "15", "88"],
          ["Island B", "90", "54"],
          ["Island C", "400", "26"],
          ["Island D", "1200", "9"]])

_T_NEW = dict(
    headers=["Years since the island rose from the sea", "Species recorded on the island"],
    rows=[["Five", "3"],
          ["Twenty", "17"],
          ["Fifty", "44"],
          ["One hundred and twenty", "71"]])

_T_INVASION = dict(
    headers=["Stage of the record", "Specialist bird species present",
             "Generalist bird species present"],
    rows=[["Before the introduction", "9", "5"],
          ["Ten years after the introduction", "5", "6"],
          ["Thirty years after the introduction", "2", "7"]])

_T_INVADER = dict(
    headers=["Introduced species", "Islands in the group it has reached",
             "Native specialist species lost from those islands"],
    rows=[["Introduced species 1", "7", "12"],
          ["Introduced species 2", "4", "5"],
          ["Introduced species 3", "1", "0"]])

_T_RESOURCE = dict(
    headers=["Island holding the same native bird", "Area of fruiting forest (hectares)",
             "Territory one breeding pair requires (hectares)",
             "Breeding pairs the island supports"],
    rows=[["Island W", "40", "20", "2"],
          ["Island X", "200", "20", "10"],
          ["Island Y", "900", "20", "45"],
          ["Island Z", "1400", "20", "70"]])

_T_ENDEMIC = dict(
    headers=["Island group", "Distance from the nearest continent (kilometres)",
             "Percent of its plant species found nowhere else"],
    rows=[["Group 1", "40", "6"],
          ["Group 2", "300", "24"],
          ["Group 3", "1100", "51"],
          ["Group 4", "3400", "78"]])

QUESTIONS = [

 dict(q="What does the course framework say island biogeography is the study of?",
      choices=[
        "The ecological relationships and distribution of organisms on islands, and of "
        "those organisms' community structures.",
        "The rock types and mineral composition from which islands are built.",
        "The routes taken by ships and aircraft between islands and continents.",
        "The rate at which sea level rises and falls around islands.",
        "The weather systems that form over warm ocean water near islands."],
      ans=0,
      why="ERT-2.D.1 states that island biogeography is the study of the ecological "
          "relationships and distribution of organisms on islands, and of these organisms' "
          "community structures. Every rejected option names something other than the "
          "organisms."),

 dict(q="A revision note lists four things island biogeography studies. Which one is not "
        "part of the framework's definition?",
      choices=[
        "The mineral composition of the rock the island is built from.",
        "The ecological relationships among the organisms living on the island.",
        "The distribution of organisms on the island.",
        "The community structures those organisms form.",
        "The organisms present on the island rather than on the mainland."],
      ans=0,
      why="ERT-2.D.1 names ecological relationships, distribution of organisms on islands "
          "and those organisms' community structures. The geology of the island itself is "
          "not among the three things the definition covers."),

 dict(q="What does the framework say about how islands came to hold the species they now "
        "have?",
      choices=[
        "They have been colonized in the past by new species arriving from elsewhere.",
        "Their species have all been present since the islands first formed.",
        "Their species were all placed there deliberately by people.",
        "Their species arrived only after the islands were joined to a continent.",
        "Their species are the survivors of an older continent that broke apart."],
      ans=0,
      why="ERT-2.D.2 states that islands have been colonized in the past by new species "
          "arriving from elsewhere, so an island community is something that was assembled "
          "by arrivals rather than fixed from the island's origin."),

 dict(q="Why does the framework say many island species have evolved to be specialists "
        "versus generalists?",
      choices=[
        "Because resources such as food and territory are limited on most islands.",
        "Because islands are warmer than the nearest mainland.",
        "Because islands receive more rainfall than the nearest mainland.",
        "Because island populations are larger than mainland populations.",
        "Because islands are free of predators of every kind."],
      ans=0,
      why="ERT-2.E.1 states that many island species have evolved to be specialists versus "
          "generalists because of the limited resources, such as food and territory, on "
          "most islands. Limited resources are the reason the framework gives."),

 dict(q="Which two limited resources does the framework name as examples in that "
        "statement?",
      choices=["Food and territory", "Sunlight and rainfall", "Oxygen and fresh water",
               "Soil depth and salinity", "Shelter and temperature"],
      ans=0,
      why="ERT-2.E.1 gives food and territory as its two examples of the limited resources "
          "on most islands. The other pairs name conditions the statement does not list."),

 dict(q="According to the framework, what is typically true of the invasive species "
        "introduced to islands, and what do they do to the specialists?",
      choices=[
        "They are typically generalists, and they outcompete the specialists.",
        "They are typically specialists, and they outcompete the generalists.",
        "They are typically generalists, and they are outcompeted by the specialists.",
        "They are typically specialists, and they are outcompeted by the generalists.",
        "They are typically generalists, and they have no effect on either group."],
      ans=0,
      why="ERT-2.E.1 states that invasive species, typically generalists, are introduced "
          "and outcompete the specialists. Each rejected option swaps which kind the "
          "invader is, or reverses which kind loses the competition, or denies that any "
          "competition follows."),

 dict(q="Whose long-term survival does ERT-2.E.1 say may be jeopardized by an "
        "introduction?",
      choices=[
        "That of the island's specialists.",
        "That of the island's generalists.",
        "That of the introduced species itself.",
        "That of every species on the island without distinction.",
        "That of the mainland populations the introduced species came from."],
      ans=0,
      why="ERT-2.E.1 states that the long-term survival of specialists may be jeopardized "
          "if and when invasive species are introduced and outcompete them. The statement "
          "names one group at risk and it is not the generalists."),

 dict(q="ERT-2.E.1 says the specialists' survival MAY be jeopardized IF AND WHEN invasive "
        "species are introduced. What does that wording establish?",
      choices=[
        "That the risk depends on an introduction taking place and is not certain even "
        "then.",
        "That every island will eventually lose all of its specialists.",
        "That specialists are already extinct wherever an introduction has occurred.",
        "That an introduction is guaranteed to happen on every island in time.",
        "That specialists are at no risk at all until the introduced species outnumbers "
        "them."],
      ans=0,
      why="ERT-2.E.1 is written with may and with if and when, which make the outcome "
          "conditional on an introduction and uncertain even where one occurs. Nothing in "
          "the statement promises the loss, and nothing promises the introduction."),

 dict(q="The framework says resources are limited on MOST islands. What does that word "
        "settle?",
      choices=[
        "That the claim holds for most islands but is not asserted of every island.",
        "That the claim holds for every island without exception.",
        "That the claim holds only for islands smaller than a stated area.",
        "That the claim holds only for islands that have never been colonized.",
        "That the claim holds for continents as readily as for islands."],
      ans=0,
      why="ERT-2.E.1 says the limited resources are found on most islands, which asserts a "
          "prevailing pattern rather than a universal rule and leaves room for islands "
          "where resources are not limiting."),

 dict(q="The framework says MANY island species have evolved to be specialists versus "
        "generalists. What does that word settle?",
      choices=[
        "That the pattern is common among island species without covering all of them.",
        "That every species on every island is a specialist.",
        "That only one species on each island is a specialist.",
        "That island species become specialists within a single generation.",
        "That mainland species never specialise at all."],
      ans=0,
      why="ERT-2.E.1 says many island species have evolved this way, which is a statement "
          "about how common the pattern is. It neither covers every island species nor "
          "makes any claim about mainland ones."),

 dict(q="Four islands of one group differ in size. What does the table establish about the "
        "resident birds?",
      table=_T_AREA,
      choices=[
        "More bird species are recorded on the larger islands than on the smaller ones.",
        "More bird species are recorded on the smaller islands than on the larger ones.",
        "The same number of bird species is recorded on every island.",
        "Bird species were recorded only on the two largest islands.",
        "The smallest island holds the most bird species of the four."],
      ans=0,
      why="Ordered by land area the species counts run 6, 14, 27 and 49, rising at every "
          "step. ERT-2.D.1 makes the distribution of organisms on islands the subject "
          "matter of island biogeography, and this record is one such distribution."),

 dict(q="Using the same island group, how many more bird species were recorded on the "
        "largest island than on the smallest?",
      table=_T_AREA,
      choices=["Forty-three", "Six", "Twenty-seven", "Fifty-five", "Nineteen"],
      ans=0,
      why="The largest island records 49 species and the smallest records 6, and 49 less 6 "
          "is 43. The count is taken from the record rather than from any rule about area."),

 dict(q="Four islands lie at different distances from one mainland. What does the table "
        "establish?",
      table=_T_DISTANCE,
      choices=[
        "Islands further from the mainland share fewer plant species with it.",
        "Islands further from the mainland share more plant species with it.",
        "Every island shares the same number of plant species with the mainland.",
        "Distance from the mainland and shared plant species are unrelated here.",
        "The island furthest from the mainland shares the most plant species with it."],
      ans=0,
      why="Ordered by distance the shared species counts run 88, 54, 26 and 9, falling at "
          "every step. ERT-2.D.2 states that islands have been colonized by species "
          "arriving from elsewhere, and this record measures how much of one island flora "
          "is shared with a possible source."),

 dict(q="Which of the four islands in that survey shares the fewest plant species with the "
        "mainland?",
      table=_T_DISTANCE,
      choices=["Island D", "Island A", "Island B", "Island C",
               "The record does not allow a comparison"],
      ans=0,
      why="The shared species counts are 88, 54, 26 and 9, and the smallest of those "
          "belongs to the island lying furthest out. The comparison is a direct reading of "
          "one column."),

 dict(q="A new volcanic island rose from the sea and has been surveyed repeatedly since. "
        "What does the table establish?",
      table=_T_NEW,
      choices=[
        "The number of species recorded on the island rose at every survey.",
        "The number of species recorded on the island fell at every survey.",
        "The island held the same number of species at every survey.",
        "The island held its full complement of species within five years.",
        "The island lost species after the fiftieth year."],
      ans=0,
      why="The counts run 3, 17, 44 and 71 as the years pass, rising at every survey. "
          "ERT-2.D.2 states that islands have been colonized in the past by new species "
          "arriving from elsewhere, and an island that began bare can only have gained them "
          "that way."),

 dict(q="Using the same volcanic island, how many more species were recorded at fifty years "
        "than at five years?",
      table=_T_NEW,
      choices=["Forty-one", "Fourteen", "Forty-seven", "Twenty-seven", "Three"],
      ans=0,
      why="The survey at fifty years records 44 species and the survey at five years "
          "records 3, and 44 less 3 is 41. The figure is a difference between two entries "
          "in one column."),

 dict(q="A generalist bird was introduced to an island holding both specialist and "
        "generalist natives. What do the two right hand columns establish?",
      table=_T_INVASION,
      choices=[
        "The specialist count fell at both later stages while the generalist count rose.",
        "The generalist count fell at both later stages while the specialist count rose.",
        "Both counts fell at both later stages.",
        "Both counts rose at both later stages.",
        "Neither count changed after the introduction."],
      ans=0,
      why="The specialists run 9, 5 and 2 while the generalists run 5, 6 and 7, so one "
          "column falls throughout and the other rises throughout. ERT-2.E.1 states that "
          "introduced invasive species, typically generalists, outcompete the specialists "
          "and may jeopardize their long-term survival."),

 dict(q="On that same island, what share of the specialist species present before the "
        "introduction was still present thirty years later?",
      table=_T_INVASION,
      choices=[
        "Two of the original nine",
        "Seven of the original nine",
        "Five of the original nine",
        "All nine of the original nine",
        "Two of an original five"],
      ans=0,
      why="The record opens with 9 specialist species and closes with 2, so 2 of the "
          "original 9 remain. The generalist column opens at 5 and is a different "
          "measurement, which is what the rejected counts confuse it with."),

 dict(q="Three species were introduced to one island group and have spread through it to "
        "different extents. What does the table establish?",
      table=_T_INVADER,
      choices=[
        "The introduced species reaching the most islands is associated with the most "
        "native specialists lost.",
        "The introduced species reaching the most islands is associated with the fewest "
        "native specialists lost.",
        "All three introduced species are associated with the same number of losses.",
        "No native specialists were lost from any island in the group.",
        "The introduced species that reached only one island caused the largest loss."],
      ans=0,
      why="Ordered by islands reached, the specialists lost run 0, 5 and 12, rising with "
          "the spread. ERT-2.E.1 attaches the jeopardy specifically to the arrival of "
          "introduced species that outcompete the specialists."),

 dict(q="One native bird needs a fixed area of fruiting forest for each breeding pair. "
        "What relationship do the columns hold on every island in the table?",
      table=_T_RESOURCE,
      choices=[
        "The pairs supported equal the forest area divided by the territory one pair "
        "requires.",
        "The pairs supported equal the forest area multiplied by the territory one pair "
        "requires.",
        "The pairs supported equal the territory one pair requires divided by the forest "
        "area.",
        "The pairs supported are the same on every island regardless of forest area.",
        "The pairs supported fall as the forest area rises."],
      ans=0,
      why="Forty hectares over twenty gives two pairs, two hundred gives ten, nine hundred "
          "gives forty-five and fourteen hundred gives seventy, so one relation holds "
          "across all four rows. ERT-2.E.1 names territory as one of the limited resources "
          "on most islands, and this is what limiting by territory looks like in numbers."),

 dict(q="Which island in that record supports the fewest breeding pairs of the native "
        "bird?",
      table=_T_RESOURCE,
      choices=["Island W", "Island X", "Island Y", "Island Z",
               "All four support the same number"],
      ans=0,
      why="The pairs supported run 2, 10, 45 and 70, and the smallest belongs to the island "
          "with the least fruiting forest. ERT-2.E.1 names territory among the limited "
          "resources that shape island populations."),

 dict(q="Four island groups lie at different distances from the nearest continent. What "
        "does the table establish?",
      table=_T_ENDEMIC,
      choices=[
        "The more distant groups hold a larger percent of plant species found nowhere else.",
        "The more distant groups hold a smaller percent of plant species found nowhere "
        "else.",
        "Every group holds the same percent of plant species found nowhere else.",
        "None of the four groups holds any plant species found nowhere else.",
        "The group nearest the continent holds the largest percent found nowhere else."],
      ans=0,
      why="Ordered by distance the percentages run 6, 24, 51 and 78, rising at every step. "
          "ERT-2.D.1 makes the distribution of organisms on islands the subject of island "
          "biogeography, and ERT-2.D.2 supplies arrival from elsewhere as how island floras "
          "are assembled."),

 dict(q="Which island group in that survey holds the largest percent of plant species found "
        "nowhere else?",
      table=_T_ENDEMIC,
      choices=["Group 4", "Group 1", "Group 2", "Group 3",
               "The survey does not report that quantity"],
      ans=0,
      why="The percentages recorded are 6, 24, 51 and 78, and the largest of those belongs "
          "to the group lying furthest from any continent. The comparison is a direct "
          "reading of one column."),

 dict(q="A researcher claims that an introduced generalist, rather than a change in the "
        "weather, drove a decline in one island's specialists. Which observation would most "
        "directly support the claim?",
      choices=[
        "Specialist numbers on a nearby island of similar size, where the generalist was "
        "never introduced, held steady over the same years.",
        "The introduced generalist is also common on the mainland it came from.",
        "The island's total rainfall was measured every year of the study.",
        "The specialists on the island had been named and described before the "
        "introduction.",
        "The introduced generalist reached the island on a ship rather than by flying."],
      ans=0,
      why="ERT-2.E.1 attributes the jeopardy to the introduced competitor, so the evidence "
          "must separate the introduction from everything else that changed over the same "
          "period. An island without the introduction but with the same weather does that; "
          "none of the rejected observations does."),

 dict(q="Which account of an island community stays within what ERT-2.D.2 asserts?",
      choices=[
        "Its species arrived from elsewhere over time, so the community was assembled "
        "rather than fixed when the island formed.",
        "Its species have been present unchanged since the island first formed.",
        "Its species arrive only when people carry them there deliberately.",
        "Its species arrived all at once during a single colonisation event.",
        "Its species are those of the nearest mainland, unchanged in every respect."],
      ans=0,
      why="ERT-2.D.2 states that islands have been colonized in the past by new species "
          "arriving from elsewhere. It says arrival happened; it does not say the arrivals "
          "were human-assisted, simultaneous, or identical to the mainland stock."),

 dict(q="What does the framework's definition include that a bare list of the species "
        "living on an island would leave out?",
      choices=[
        "The ecological relationships among the organisms and the community structures they "
        "form.",
        "The date on which each species was first named by a scientist.",
        "The depth of the water separating the island from its neighbours.",
        "The number of people living on the island at the time of the survey.",
        "The age of the volcanic rock underlying the island."],
      ans=0,
      why="ERT-2.D.1 names three things: ecological relationships, distribution of "
          "organisms, and those organisms' community structures. A list of species covers "
          "the second only, so the first and third are what it leaves out."),

 dict(q="A student concludes from ERT-2.E.1 that an introduced species harms every native "
        "species on an island equally. Why is that more than the framework says?",
      choices=[
        "The statement puts the specialists, not every native species, at risk from the "
        "introduced generalists.",
        "The statement puts the generalists, not the specialists, at risk from the "
        "introduced species.",
        "The statement says introduced species never affect natives at all.",
        "The statement applies only to plants and not to animals.",
        "The statement applies only to islands that have never been colonized before."],
      ans=0,
      why="ERT-2.E.1 names the long-term survival of specialists as what may be jeopardized "
          "when introduced invasive species, typically generalists, outcompete them. It "
          "makes no equivalent claim about the natives that are themselves generalists."),

 dict(q="A team protecting a bird that lives on one island only and feeds on one plant "
        "only asks which risk the framework identifies for it. What should they be told?",
      choices=[
        "The arrival of an introduced generalist that outcompetes it.",
        "The arrival of an introduced specialist that shares its single food plant.",
        "A rise in the number of generalist natives already on the island.",
        "The loss of the island's connection to the mainland.",
        "An increase in the island's total land area."],
      ans=0,
      why="ERT-2.E.1 states that the long-term survival of specialists may be jeopardized "
          "if and when invasive species, typically generalists, are introduced and "
          "outcompete the specialists. That is the one risk the statement names."),

 dict(q="Elsewhere the framework states that invasive species are often generalist, "
        "r-selected species and may therefore outcompete native species for resources. How "
        "does that sit alongside ERT-2.E.1?",
      choices=[
        "Both say the introduced competitor is typically a generalist and that the native "
        "specialists lose the competition.",
        "The two disagree, because one calls the invader a generalist and the other calls "
        "it a specialist.",
        "The two disagree, because one says the natives win the competition.",
        "They describe different processes, because only one of them involves competition "
        "for resources.",
        "They describe different processes, because only one of them concerns species "
        "introduced from elsewhere."],
      ans=0,
      why="EIN-4.A.2 states that invasive species are often generalist, r-selected species "
          "and may therefore outcompete native species for resources, and ERT-2.E.1 states "
          "that invasive species, typically generalists, are introduced and outcompete the "
          "specialists. Both name the invader as usually a generalist and the native as the "
          "one outcompeted."),

 dict(q="Which single sentence collects what this topic's three statements assert and "
        "nothing further?",
      choices=[
        "Island biogeography studies the relationships, distribution and community "
        "structures of island organisms; islands were colonized from elsewhere; and limited "
        "resources have made many island species specialists that introduced generalists "
        "may outcompete.",
        "Island biogeography studies island geology; islands were colonized from elsewhere; "
        "and limited resources have made many island species generalists.",
        "Island biogeography studies the relationships, distribution and community "
        "structures of island organisms; islands have never been colonized; and abundant "
        "resources have made many island species specialists.",
        "Island biogeography studies the relationships, distribution and community "
        "structures of island organisms; islands were colonized from elsewhere; and every "
        "island species is certain to be lost once an introduction occurs.",
        "Island biogeography studies the relationships, distribution and community "
        "structures of island organisms; islands were colonized from elsewhere; and "
        "introduced specialists outcompete the resident generalists."],
      ans=0,
      why="ERT-2.D.1 supplies the subject matter, ERT-2.D.2 the colonisation from "
          "elsewhere, and ERT-2.E.1 the limited resources, the specialisation and the "
          "introduced generalists that may outcompete the specialists. Each rejected "
          "summary changes the subject matter, denies colonisation, reverses which kind is "
          "advantaged, or hardens may into certainty."),
]
