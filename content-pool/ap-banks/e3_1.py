# AP ENVIRONMENTAL SCIENCE 3.1 Generalist and Specialist Species
# CED effective Fall 2026, Unit 3 Populations.
# Enduring understanding ERT-3: populations change over time in reaction to a variety of
# factors.
# Learning objective ERT-3.A: identify differences between generalist and specialist
# species. Suggested skill 1.B.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-3.A.1  Specialist species tend to be advantaged in habitats that remain constant,
#              while generalist species tend to be advantaged in habitats that are changing.
# Unit 3 overview, same CED: "Specialist species are advantaged by habitats that remain
# constant, while generalist species tend to be advantaged by habitats that are changing."
#
# THE TOPIC HAS ONE ESSENTIAL KNOWLEDGE STATEMENT AND EVERY KEY HERE RESTS ON IT. The
# statement is a single comparison with two halves and a hedge, and that is the whole
# content: which kind is advantaged in a CONSTANT habitat, which kind is advantaged in a
# CHANGING one, and the fact that both halves say TEND TO BE rather than always are.
#
# THE FRAMEWORK NEVER DEFINES SPECIALIST OR GENERALIST, anywhere in the course. So no item
# here asks a student to sort a species into one of the two from its diet, its range or
# anything else. The two words are used exactly as the framework uses them: as labels on
# counts. Item 5 keys that absence outright.
#
# BOUNDARIES, BOTH DELIBERATE, BECAUSE THREE TOPICS TOUCH THESE TWO WORDS.
#   - ERT-2.A.4 (topic 2.1) gives the ORDER of losses under habitat loss: specialists first,
#     then generalists. That is a different claim, about a shrinking habitat rather than a
#     changing one, and topic 2.1 already carries it. NO ITEM HERE IS ABOUT HABITAT LOSS OR
#     FRAGMENTATION; item 9 exists to mark the line and names the chain.
#   - ERT-2.E.1 (topic 2.3) gives the ISLAND case: limited resources, and invasive
#     generalists outcompeting specialists. Topic 2.3 carries it. No item here is about
#     islands or introductions; item 10 marks that line and names the chain.
# Both boundary items key the DISTINCTION, not the other topic's content.
#
# THE SWAP IS THE HAZARD. Every distractor set that names both kinds contains the reversed
# statement, so the anchors in verify_e3_1.py for items 3, 11, 16, 20 and 21 carry BOTH
# clauses. Half an anchor matches the swap as readily as the key; that defect was found
# once already in verify_e2_1.py and is not repeated here.
#
# NO FIGURES. Every quantitative item carries a table=, recomputed in verify_e3_1.py from
# that table alone.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("3.1", "Generalist and Specialist Species", 3)

_T_HABVAR = dict(
    headers=["Habitat surveyed",
             "Year to year variation in temperature and rainfall (index)",
             "Specialist species present", "Generalist species present"],
    rows=[["Habitat 1", "1", "28", "6"],
          ["Habitat 2", "4", "19", "11"],
          ["Habitat 3", "9", "9", "18"],
          ["Habitat 4", "16", "3", "27"]])

_T_TREND = dict(
    headers=["Period of the record",
             "Years in the period with a marked change in conditions",
             "Specialist species present at the end of the period",
             "Generalist species present at the end of the period"],
    rows=[["Period 1", "1", "24", "8"],
          ["Period 2", "3", "20", "11"],
          ["Period 3", "8", "12", "19"],
          ["Period 4", "14", "5", "26"]])

_T_TWO = dict(
    headers=["Reserve", "Change in mean conditions over thirty years (index)",
             "Change in the number of specialist species",
             "Change in the number of generalist species"],
    rows=[["Reserve held constant by management", "0", "3", "-1"],
          ["Reserve left to fluctuate", "12", "-9", "7"]])

_T_PCT = dict(
    headers=["Site", "Marked changes in conditions recorded over twenty years",
             "Specialists as a percent of the species present"],
    rows=[["Site A", "0", "82"],
          ["Site B", "5", "61"],
          ["Site C", "11", "34"],
          ["Site D", "19", "9"]])

_T_SWITCH = dict(
    headers=["Stage of the record for one wetland",
             "Years per decade in which the water level varied by more than a metre",
             "Specialist species present", "Generalist species present"],
    rows=[["Before the river was regulated", "7", "12", "21"],
          ["After the river was regulated", "1", "25", "10"]])

_T_PAIRED = dict(
    headers=["Pair of neighbouring habitats",
             "Specialist species in the constant habitat",
             "Specialist species in the changing habitat",
             "Generalist species in the constant habitat",
             "Generalist species in the changing habitat"],
    rows=[["Pair 1", "23", "8", "5", "17"],
          ["Pair 2", "31", "12", "7", "22"],
          ["Pair 3", "17", "6", "4", "14"]])

QUESTIONS = [

 dict(q="In habitats that remain constant, which kind of species does the framework say "
        "tends to be advantaged?",
      choices=["Specialist species", "Generalist species",
               "Both kinds to exactly the same degree", "Neither kind",
               "Only the species with the largest territories"],
      ans=0,
      why="ERT-3.A.1 states that specialist species tend to be advantaged in habitats that "
          "remain constant. The framework attaches that half of the comparison to "
          "constancy."),

 dict(q="In habitats that are changing, which kind of species does the framework say tends "
        "to be advantaged?",
      choices=["Generalist species", "Specialist species",
               "Both kinds to exactly the same degree", "Neither kind",
               "Only the species that reproduce most slowly"],
      ans=0,
      why="ERT-3.A.1 states that generalist species tend to be advantaged in habitats that "
          "are changing. The framework attaches that half of the comparison to change."),

 dict(q="Which statement reproduces the framework's comparison in full?",
      choices=[
        "Specialists tend to be advantaged where habitats remain constant, and generalists "
        "where habitats are changing.",
        "Generalists tend to be advantaged where habitats remain constant, and specialists "
        "where habitats are changing.",
        "Specialists tend to be advantaged in every habitat, whether constant or changing.",
        "Generalists tend to be advantaged in every habitat, whether constant or changing.",
        "Neither kind is advantaged by the constancy or the variability of a habitat."],
      ans=0,
      why="ERT-3.A.1 pairs specialists with habitats that remain constant and generalists "
          "with habitats that are changing. The rejected options exchange the two kinds, or "
          "give one kind the advantage everywhere, or deny that habitat constancy matters."),

 dict(q="ERT-3.A.1 says each kind TENDS TO BE advantaged. What does that wording establish?",
      choices=[
        "That the advantage is a tendency, so an individual case may run the other way.",
        "That the advantage holds in every case without exception.",
        "That the advantage appears only after several generations.",
        "That the advantage applies to plants but not to animals.",
        "That the framework is unsure whether habitats differ in constancy."],
      ans=0,
      why="The statement is written twice with tend to be, which asserts a prevailing "
          "pattern rather than a rule without exceptions. A single habitat running the "
          "other way is therefore consistent with it."),

 dict(q="What does the framework supply about the terms specialist and generalist "
        "themselves?",
      choices=[
        "It uses both terms without defining either of them.",
        "It defines a specialist by the number of food types it takes.",
        "It defines a generalist by the size of its geographic range.",
        "It defines both terms by the number of offspring each produces.",
        "It defines a specialist as any species found in only one habitat."],
      ans=0,
      why="ERT-3.A.1 states which kind tends to be advantaged in which habitat and supplies "
          "no definition of either kind. Each rejected option states a definition the "
          "framework does not give anywhere in the course."),

 dict(q="A habitat that has been stable for a long time begins to vary sharply from year to "
        "year. Which shift does the framework's comparison lead you to expect?",
      choices=[
        "A shift toward generalist species being the advantaged kind.",
        "A shift toward specialist species being the advantaged kind.",
        "No change in which kind is advantaged.",
        "A shift toward both kinds being equally advantaged.",
        "A shift toward neither kind being able to persist."],
      ans=0,
      why="ERT-3.A.1 attaches the generalists' advantage to habitats that are changing, so "
          "a habitat that becomes variable moves from the half of the comparison that "
          "favours specialists to the half that favours generalists."),

 dict(q="A forest has held nearly the same temperature and rainfall for centuries. Which "
        "kind of species does the framework's comparison favour there?",
      choices=[
        "Specialist species, because the habitat remains constant.",
        "Generalist species, because the habitat remains constant.",
        "Specialist species, because the habitat is changing.",
        "Generalist species, because the habitat is changing.",
        "Neither kind, because the framework makes no prediction from constancy."],
      ans=0,
      why="ERT-3.A.1 pairs the specialists' advantage with habitats that remain constant. "
          "The rejected options either swap the kind, misdescribe the habitat, or deny that "
          "the framework connects the two."),

 dict(q="Does the framework claim that specialist species disappear from every habitat that "
        "changes?",
      choices=[
        "No, it claims only that generalists tend to be the advantaged kind there.",
        "Yes, it states that specialists disappear whenever a habitat changes.",
        "Yes, but only where the change lasts more than one generation.",
        "No, because the framework makes no claim about changing habitats at all.",
        "No, because the framework claims that specialists are advantaged by change."],
      ans=0,
      why="ERT-3.A.1 speaks of which kind tends to be advantaged and says nothing about "
          "disappearance. It does address changing habitats, and it puts the generalists "
          "rather than the specialists at an advantage in them."),

 dict(q="How does this topic's claim differ from the framework's separate statement that "
        "loss of habitat brings a loss of specialist species and then of generalist "
        "species?",
      choices=[
        "This topic is about which kind is favoured as a habitat stays constant or changes, "
        "while that statement is about the order of losses as a habitat shrinks.",
        "This topic is about the order of losses as a habitat shrinks, while that statement "
        "is about which kind is favoured as a habitat changes.",
        "The two make the same claim in different words.",
        "This topic concerns plants and that statement concerns animals.",
        "This topic concerns a single generation and that statement concerns geological "
        "time."],
      ans=0,
      why="ERT-3.A.1 compares constant habitats with changing ones and says which kind each "
          "favours. ERT-2.A.4, a separate statement belonging to the biodiversity unit, "
          "gives the sequence in which the two kinds are lost as habitat is lost. The "
          "variable is different in each: constancy in one, extent in the other."),

 dict(q="How does this topic's claim differ from the framework's separate statement about "
        "invasive species on islands outcompeting the specialists there?",
      choices=[
        "This topic compares constant habitats with changing ones, while that statement "
        "concerns species introduced to islands with limited resources.",
        "This topic concerns species introduced to islands, while that statement compares "
        "constant habitats with changing ones.",
        "The two make the same claim in different words.",
        "This topic applies only to islands and that statement applies only to continents.",
        "This topic concerns competition and that statement concerns habitat constancy."],
      ans=0,
      why="ERT-3.A.1 is a comparison between habitats that remain constant and habitats "
          "that are changing. ERT-2.E.1, a separate statement in the biodiversity unit, "
          "concerns island species, the limited resources on most islands, and introduced "
          "generalists outcompeting specialists. Neither statement is the other."),

 dict(q="Four habitats differing in how much their conditions vary were surveyed. What do "
        "the two right hand columns establish?",
      table=_T_HABVAR,
      choices=[
        "As the year to year variation rises, the specialist count falls and the generalist "
        "count rises.",
        "As the year to year variation rises, the generalist count falls and the specialist "
        "count rises.",
        "Both counts fall as the year to year variation rises.",
        "Both counts rise as the year to year variation rises.",
        "Neither count changes with the year to year variation."],
      ans=0,
      why="Ordered by variation the specialists run 28, 19, 9 and 3 while the generalists "
          "run 6, 11, 18 and 27, so one column falls throughout and the other rises "
          "throughout. ERT-3.A.1 puts the specialists' advantage in constant habitats and "
          "the generalists' in changing ones."),

 dict(q="In which of those four habitats do specialists outnumber generalists by the "
        "largest margin?",
      table=_T_HABVAR,
      choices=["Habitat 1", "Habitat 2", "Habitat 3", "Habitat 4",
               "Specialists never outnumber generalists in the record"],
      ans=0,
      why="The margins are 28 less 6, 19 less 11, 9 less 18 and 3 less 27, which are 22, 8, "
          "minus 9 and minus 24. The largest belongs to the habitat whose conditions vary "
          "least, which is the half of ERT-3.A.1's comparison that favours specialists."),

 dict(q="In which of those habitats do the generalists outnumber the specialists by more "
        "than a factor of two?",
      table=_T_HABVAR,
      choices=["In Habitat 4 alone", "In Habitat 3 alone", "In Habitat 1 alone",
               "In every one of the four habitats", "In none of the four habitats"],
      ans=0,
      why="The generalist and specialist counts are 6 against 28, 11 against 19, 18 against "
          "9 and 27 against 3. Only the last pair exceeds a factor of two, and that habitat "
          "is the most variable of the four, which is where ERT-3.A.1 places the "
          "generalists' advantage."),

 dict(q="Which of those four habitats holds the fewest specialist species?",
      table=_T_HABVAR,
      choices=["Habitat 4", "Habitat 1", "Habitat 2", "Habitat 3",
               "All four hold the same number of specialists"],
      ans=0,
      why="The specialist counts are 28, 19, 9 and 3, and the smallest belongs to the "
          "habitat whose conditions vary most. ERT-3.A.1 places the specialists' advantage "
          "in habitats that remain constant."),

 dict(q="One region was recorded over four successive periods that differed in how often "
        "conditions changed markedly. What does the record establish?",
      table=_T_TREND,
      choices=[
        "The periods with more marked changes ended with fewer specialists and more "
        "generalists.",
        "The periods with more marked changes ended with more specialists and fewer "
        "generalists.",
        "The periods with more marked changes ended with fewer of both kinds.",
        "The periods with more marked changes ended with more of both kinds.",
        "The number of marked changes had no bearing on either count."],
      ans=0,
      why="Ordered by the number of marked changes the specialists run 24, 20, 12 and 5 "
          "while the generalists run 8, 11, 19 and 26. ERT-3.A.1 places the generalists' "
          "advantage in habitats that are changing and the specialists' in habitats that "
          "remain constant."),

 dict(q="By how many species did the specialist count in that region change between the "
        "first period and the fourth?",
      table=_T_TREND,
      choices=["It fell by 19", "It rose by 19", "It fell by 5", "It fell by 24",
               "It did not change"],
      ans=0,
      why="The specialist count stands at 24 at the end of the first period and 5 at the "
          "end of the fourth, and 24 less 5 is 19. The rejected values reverse the "
          "direction or name one of the two endpoints."),

 dict(q="Two reserves were followed for thirty years, one held to constant conditions by "
        "management and one left to fluctuate. What does the record establish?",
      table=_T_TWO,
      choices=[
        "The reserve held constant gained specialists and lost generalists, while the "
        "fluctuating reserve lost specialists and gained generalists.",
        "The reserve held constant lost specialists and gained generalists, while the "
        "fluctuating reserve gained specialists and lost generalists.",
        "Both reserves gained specialists and lost generalists.",
        "Both reserves lost specialists and gained generalists.",
        "Neither reserve changed in either count."],
      ans=0,
      why="The constant reserve records a gain of 3 specialists and a loss of 1 generalist, "
          "and the fluctuating reserve a loss of 9 specialists and a gain of 7 generalists. "
          "ERT-3.A.1 puts the specialists' advantage in habitats that remain constant and "
          "the generalists' in habitats that are changing."),

 dict(q="Which of those two reserves lost specialist species over the thirty years?",
      table=_T_TWO,
      choices=[
        "The reserve left to fluctuate",
        "The reserve held constant by management",
        "Both reserves lost specialists",
        "Neither reserve lost specialists",
        "The record does not report specialists"],
      ans=0,
      why="One reserve records a change of minus 9 specialists and the other a change of "
          "plus 3, so only one of the two lost any. The reserve that lost them is the one "
          "whose conditions changed, which is the half of ERT-3.A.1's comparison that "
          "favours generalists."),

 dict(q="Four sites were scored for how often their conditions changed markedly and for the "
        "share of their species that are specialists. What does the record establish?",
      table=_T_PCT,
      choices=[
        "The specialist share is smaller at the sites where conditions changed more often.",
        "The specialist share is larger at the sites where conditions changed more often.",
        "The specialist share is the same at all four sites.",
        "The specialist share and the frequency of change are unrelated across the sites.",
        "The site with the most frequent change has the largest specialist share."],
      ans=0,
      why="Ordered by the number of marked changes the specialist shares run 82, 61, 34 and "
          "9 percent, falling at every step. ERT-3.A.1 places the specialists' advantage in "
          "habitats that remain constant."),

 dict(q="Which of those four sites carries the largest specialist share of its species?",
      table=_T_PCT,
      choices=["Site A", "Site B", "Site C", "Site D",
               "The shares are equal at all four sites"],
      ans=0,
      why="The shares recorded are 82, 61, 34 and 9 percent, and the largest belongs to the "
          "site at which no marked change was recorded in twenty years. ERT-3.A.1 pairs "
          "constancy with the specialists' advantage."),

 dict(q="By how many percentage points does the specialist share fall between the least and "
        "the most frequently disturbed of those sites?",
      table=_T_PCT,
      choices=["73 points", "82 points", "9 points", "48 points", "27 points"],
      ans=0,
      why="The specialist share runs from 82 percent at the site with no marked change to 9 "
          "percent at the site with nineteen, and 82 less 9 is 73. The rejected values are "
          "the endpoints themselves or differences between other pairs of sites."),

 dict(q="A wetland was surveyed before and after the river feeding it was regulated so that "
        "its water level varied far less. What does the record establish?",
      table=_T_SWITCH,
      choices=[
        "As the water level steadied, the specialist count rose and the generalist count "
        "fell.",
        "As the water level steadied, the generalist count rose and the specialist count "
        "fell.",
        "As the water level steadied, both counts rose.",
        "As the water level steadied, both counts fell.",
        "The water level steadied and neither count changed."],
      ans=0,
      why="Years of large water level variation fall from 7 to 1 per decade, the "
          "specialists rise from 12 to 25 and the generalists fall from 21 to 10. ERT-3.A.1 "
          "puts the specialists' advantage in habitats that remain constant and the "
          "generalists' in habitats that are changing."),

 dict(q="Three pairs of neighbouring habitats were surveyed, one constant and one changing "
        "in each pair. What holds across all three pairs?",
      table=_T_PAIRED,
      choices=[
        "The constant habitat of each pair holds more specialists and the changing habitat "
        "holds more generalists.",
        "The constant habitat of each pair holds more generalists and the changing habitat "
        "holds more specialists.",
        "The constant habitat of each pair holds more of both kinds.",
        "The changing habitat of each pair holds more of both kinds.",
        "The pattern differs from one pair to the next."],
      ans=0,
      why="In every pair the specialist count is higher in the constant habitat and the "
          "generalist count is higher in the changing one. ERT-3.A.1 makes exactly that "
          "pairing, and the record repeats it three times over."),

 dict(q="In which of those three pairs is the difference in specialist numbers between the "
        "constant and the changing habitat largest?",
      table=_T_PAIRED,
      choices=["Pair 2", "Pair 1", "Pair 3", "The three differences are equal",
               "The record does not report specialists"],
      ans=0,
      why="The differences are 23 less 8, 31 less 12 and 17 less 6, which are 15, 19 and 11 "
          "species. The largest is unique and belongs to the second pair."),

 dict(q="Which study design would test ERT-3.A.1's comparison most directly?",
      choices=[
        "Counting specialists and generalists in habitats that differ in how constant their "
        "conditions are, and comparing the two counts across that gradient.",
        "Counting specialists and generalists in a single habitat once.",
        "Recording how many food types each species in one habitat takes.",
        "Measuring the total area of every habitat in the region.",
        "Counting how many species in the region are found nowhere else."],
      ans=0,
      why="The statement is a comparison between constant and changing habitats, so the "
          "test needs both kinds of habitat and both kinds of species counted across them. "
          "A single site, a diet survey, an area measurement and an endemism count each "
          "leave out one half of the comparison or the comparison itself."),

 dict(q="A reserve manager wants to favour the specialist species already present. Which "
        "management aim follows from ERT-3.A.1?",
      choices=[
        "Keeping the reserve's conditions as constant as possible from year to year.",
        "Making the reserve's conditions vary as much as possible from year to year.",
        "Enlarging the reserve without regard to its conditions.",
        "Introducing further species from outside the reserve.",
        "Nothing follows, because the statement makes no connection between constancy and "
        "either kind."],
      ans=0,
      why="ERT-3.A.1 states that specialist species tend to be advantaged in habitats that "
          "remain constant, so constancy is the condition the statement associates with the "
          "specialists' advantage. Area and introductions are not part of this statement."),

 dict(q="A student concludes that generalists are simply better competitors than "
        "specialists everywhere. Why does that go beyond the framework?",
      choices=[
        "Because the statement gives the generalists their advantage only where habitats "
        "are changing.",
        "Because the statement gives the generalists their advantage only where habitats "
        "remain constant.",
        "Because the statement says nothing about generalists at all.",
        "Because the statement says specialists always outcompete generalists.",
        "Because the statement applies only to habitats that no longer exist."],
      ans=0,
      why="ERT-3.A.1 is a conditional comparison: generalists tend to be advantaged where "
          "habitats are changing, and specialists where they remain constant. An unqualified "
          "advantage in every habitat is not what either half of the statement says."),

 dict(q="A region's climate is becoming markedly more variable from year to year. Which "
        "expectation does the framework support?",
      choices=[
        "The generalist species there tend to be the advantaged kind under the new "
        "conditions.",
        "The specialist species there tend to be the advantaged kind under the new "
        "conditions.",
        "Both kinds tend to be advantaged equally under the new conditions.",
        "Neither kind can persist under the new conditions.",
        "The framework makes no expectation from a change in variability."],
      ans=0,
      why="ERT-3.A.1 attaches the generalists' advantage to habitats that are changing, and "
          "a climate becoming more variable is such a habitat. The statement offers no "
          "prediction of extinction and does not treat the two kinds alike."),

 dict(q="Which observation would count AGAINST the tendency ERT-3.A.1 describes?",
      choices=[
        "Specialists increasing and generalists declining in a habitat that has become far "
        "more variable.",
        "Specialists increasing and generalists declining in a habitat whose conditions have "
        "held steady.",
        "Generalists increasing and specialists declining in a habitat that has become far "
        "more variable.",
        "Both kinds increasing in a habitat whose total area has grown.",
        "Both kinds declining in a habitat whose total area has shrunk."],
      ans=0,
      why="ERT-3.A.1 expects the generalists to be the advantaged kind where a habitat is "
          "changing, so the observation running against it is the opposite result in "
          "exactly that setting. Two of the rejected options match the statement rather than "
          "contradicting it, and two concern area, which the statement does not mention."),

 dict(q="Which single sentence states what this topic asserts and nothing further?",
      choices=[
        "Specialists tend to be advantaged where habitats remain constant and generalists "
        "where habitats are changing, and the framework defines neither kind.",
        "Specialists tend to be advantaged where habitats are changing and generalists where "
        "habitats remain constant, and the framework defines both kinds.",
        "Specialists are always advantaged over generalists, whatever the habitat, and the "
        "framework defines neither kind.",
        "Generalists are always advantaged over specialists, whatever the habitat, and the "
        "framework defines both kinds by their diets.",
        "Specialists tend to be advantaged where habitats remain constant and generalists "
        "where habitats are changing, and the framework defines a specialist as a species "
        "with one food source."],
      ans=0,
      why="ERT-3.A.1 supplies the two halves of the comparison and the hedge, and supplies "
          "no definition of either kind anywhere in the course. Each rejected summary "
          "exchanges the two halves, hardens the tendency into an absolute, or adds a "
          "definition the framework does not give."),
]
