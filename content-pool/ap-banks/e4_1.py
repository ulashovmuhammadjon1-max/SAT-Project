# AP ENVIRONMENTAL SCIENCE 4.1 Plate Tectonics
# CED effective Fall 2026, Unit 4 Earth Systems and Resources.
# Enduring understanding ERT-4: Earth's systems interact, resulting in a state of balance
# over time.
# Learning objective ERT-4.A: describe the geological changes and events that occur at
# convergent, divergent, and transform plate boundaries.
# Suggested skill 2.C, explain how environmental concepts and processes represented
# visually relate to broader environmental issues.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-4.A.1  Convergent boundaries can result in the creation of mountains, island arcs,
#              earthquakes, and volcanoes.
#   ERT-4.A.2  Divergent boundaries can result in seafloor spreading, rift valleys,
#              volcanoes, and earthquakes.
#   ERT-4.A.3  Transform boundaries can result in earthquakes.
#   ERT-4.A.4  Maps that show the global distribution of plate boundaries can be used to
#              determine the location of volcanoes, island arcs, earthquakes, hot spots,
#              and faults.
#   ERT-4.A.5  An earthquake occurs when stress overcomes a locked fault, releasing stored
#              energy.
#
# THE THREE LISTS ARE THE WHOLE CONTENT AND THEY OVERLAP DELIBERATELY. Reading them side
# by side is what most of this module asks for:
#   mountains and island arcs      convergent only
#   seafloor spreading, rift valleys   divergent only
#   volcanoes                      convergent and divergent, NOT transform
#   earthquakes                    all three
#   hot spots and faults           named ONLY in ERT-4.A.4's list of what a boundary
#                                  record locates, and attached to no boundary type
#
# CONVERGENT AND DIVERGENT ARE THE OBVIOUS SWAP, so every anchor on an item that
# contrasts them carries BOTH clauses. An anchor naming one list alone matches the swapped
# distractor as well as the key.
#
# NOT KEYED, because the framework does not state it: what drives plate motion, how fast
# plates move, subduction, the depth of an earthquake, a magnitude scale, any named plate,
# fault or mountain range, and the mechanism by which a hot spot forms. ERT-4.A.4 lists hot
# spots among the things a boundary record locates and says nothing else about them.
#
# NO FIGURES. The bank carries no images, so nothing here refers to a picture; where a
# question needs a spatial pattern the counts are tabulated and the question is asked of
# the table.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("4.1", "Plate Tectonics", 4)

_T_BOUNDARY = dict(
    headers=["Boundary", "Relative motion of the two plates",
             "Mountain ranges recorded along it", "Volcanoes recorded along it",
             "Earthquakes recorded in a ten year survey"],
    rows=[["Boundary 1", "The two plates move toward each other", "3", "18", "410"],
          ["Boundary 2", "The two plates move apart", "0", "24", "260"],
          ["Boundary 3", "The two plates slide past each other", "0", "0", "530"]])

_T_SPREAD = dict(
    headers=["Distance from the ridge crest (kilometers)",
             "Age of the seafloor rock (millions of years)"],
    rows=[["0", "0"],
          ["40", "2"],
          ["80", "4"],
          ["120", "6"]])

_T_QUAKE = dict(
    headers=["Fault segment", "Years the segment stayed locked",
             "Stress stored on the segment (units)",
             "Energy released when the segment moved (units)"],
    rows=[["Segment 1", "18", "9", "9"],
          ["Segment 2", "44", "22", "22"],
          ["Segment 3", "96", "48", "48"]])

_T_LOCATE = dict(
    headers=["Kind of feature counted",
             "Number found within one hundred kilometers of a mapped plate boundary",
             "Number found farther than one hundred kilometers from any mapped boundary"],
    rows=[["Volcanoes", "820", "140"],
          ["Island arcs", "31", "0"],
          ["Earthquake epicenters", "9400", "600"]])

QUESTIONS = [

 dict(q="Which geological changes and events does the framework say convergent boundaries "
        "can result in?",
      choices=[
        "The creation of mountains, island arcs, earthquakes, and volcanoes",
        "Seafloor spreading, rift valleys, volcanoes, and earthquakes",
        "Earthquakes, with no other feature named",
        "Hot spots and faults, with no other feature named",
        "Rift valleys and island arcs together, with no volcanoes"],
      ans=0,
      why="ERT-4.A.1 states that convergent boundaries can result in the creation of "
          "mountains, island arcs, earthquakes, and volcanoes. The rejected list of "
          "seafloor spreading and rift valleys belongs to ERT-4.A.2 and divergent "
          "boundaries."),

 dict(q="Which geological changes and events does the framework say divergent boundaries "
        "can result in?",
      choices=[
        "Seafloor spreading, rift valleys, volcanoes, and earthquakes",
        "The creation of mountains, island arcs, earthquakes, and volcanoes",
        "Earthquakes, with no other feature named",
        "Mountains and island arcs, with no volcanoes and no earthquakes",
        "Hot spots alone"],
      ans=0,
      why="ERT-4.A.2 states that divergent boundaries can result in seafloor spreading, "
          "rift valleys, volcanoes, and earthquakes. The rejected list of mountains and "
          "island arcs belongs to ERT-4.A.1 and convergent boundaries."),

 dict(q="What does the framework say transform boundaries can result in?",
      choices=[
        "Earthquakes, and no other feature in that statement",
        "Rift valleys as well as earthquakes",
        "Island arcs as well as earthquakes",
        "Mountains and volcanoes, but no earthquakes",
        "Seafloor spreading as well as earthquakes"],
      ans=0,
      why="ERT-4.A.3 is one clause long: transform boundaries can result in earthquakes. "
          "Rift valleys and seafloor spreading belong to ERT-4.A.2 and island arcs to "
          "ERT-4.A.1, and no statement adds any of them to transform boundaries."),

 dict(q="Which features does the framework attribute to convergent boundaries but not to "
        "divergent ones?",
      choices=[
        "The creation of mountains and island arcs",
        "Seafloor spreading and rift valleys",
        "Volcanoes",
        "Earthquakes",
        "Hot spots"],
      ans=0,
      why="ERT-4.A.1 names mountains and island arcs and ERT-4.A.2 does not. The two lists "
          "share volcanoes and earthquakes, seafloor spreading and rift valleys belong to "
          "the divergent list alone, and hot spots appear only in ERT-4.A.4."),

 dict(q="Which features does the framework attribute to divergent boundaries but not to "
        "convergent ones?",
      choices=[
        "Seafloor spreading and rift valleys",
        "The creation of mountains and island arcs",
        "Volcanoes",
        "Earthquakes",
        "Faults"],
      ans=0,
      why="ERT-4.A.2 names seafloor spreading and rift valleys and ERT-4.A.1 does not. "
          "Mountains and island arcs belong to the convergent list alone, the two lists "
          "share volcanoes and earthquakes, and faults appear only in ERT-4.A.4."),

 dict(q="Which single feature does the framework attribute to convergent and to divergent "
        "boundaries, but not to transform ones?",
      choices=["Volcanoes", "Island arcs", "Rift valleys", "Seafloor spreading",
               "Mountains"],
      ans=0,
      why="Volcanoes appear in both ERT-4.A.1 and ERT-4.A.2, while ERT-4.A.3 names only "
          "earthquakes for transform boundaries. Island arcs and mountains are convergent "
          "alone and rift valleys and seafloor spreading are divergent alone."),

 dict(q="Which single feature does the framework attribute to all three kinds of plate "
        "boundary?",
      choices=["Earthquakes", "Volcanoes", "Mountains", "Rift valleys", "Island arcs"],
      ans=0,
      why="Earthquakes are named in ERT-4.A.1 for convergent boundaries, in ERT-4.A.2 for "
          "divergent ones and in ERT-4.A.3 for transform ones. Volcanoes appear in the "
          "first two statements only, and the remaining features in one statement each."),

 dict(q="According to the framework, when does an earthquake occur?",
      choices=[
        "When stress overcomes a locked fault, releasing stored energy",
        "When a volcano erupts somewhere along a plate boundary",
        "When two plates first come into contact with one another",
        "When stored energy accumulates although no fault is present",
        "When a fault locks after a long period of steady movement"],
      ans=0,
      why="ERT-4.A.5 states that an earthquake occurs when stress overcomes a locked fault, "
          "releasing stored energy. The locking comes first and the release follows, so an "
          "option in which the fault locks at the moment of the earthquake reverses the "
          "order the statement gives."),

 dict(q="In the framework's account of an earthquake, what is released?",
      choices=["Stored energy", "Newly weathered parent material", "Molten rock from a hot "
               "spot", "A length of new seafloor", "Nothing at all is released"],
      ans=0,
      why="ERT-4.A.5 states that the fault gives way releasing stored energy. Weathered "
          "parent material belongs to the soil formation statement, and seafloor spreading "
          "is a separate result of divergent boundaries in ERT-4.A.2."),

 dict(q="In that same account, what does the stress have to overcome?",
      choices=["A locked fault", "A rift valley", "An island arc", "A hot spot",
               "A mountain range"],
      ans=0,
      why="ERT-4.A.5 states that an earthquake occurs when stress overcomes a locked fault. "
          "The rejected options are features named elsewhere in the topic, none of which "
          "that statement puts in the path of the stress."),

 dict(q="What does the framework say can be determined from a record showing the global "
        "distribution of plate boundaries?",
      choices=[
        "The location of volcanoes, island arcs, earthquakes, hot spots, and faults",
        "The date on which the next earthquake will occur",
        "The depth of the ocean at every point on the seafloor",
        "The chemical composition of the rock beneath each plate",
        "The rate at which soil forms on each continent"],
      ans=0,
      why="ERT-4.A.4 states that maps showing the global distribution of plate boundaries "
          "can be used to determine the location of volcanoes, island arcs, earthquakes, "
          "hot spots, and faults. The statement offers a location and not a date, a depth, "
          "a composition or a rate."),

 dict(q="Two of the things ERT-4.A.4 says such a record locates are not attributed by any "
        "other statement to a particular kind of boundary. Which two?",
      choices=[
        "Hot spots and faults",
        "Volcanoes and earthquakes",
        "Island arcs and earthquakes",
        "Mountains and rift valleys",
        "Seafloor spreading and volcanoes"],
      ans=0,
      why="ERT-4.A.1 to ERT-4.A.3 name mountains, island arcs, earthquakes, volcanoes, "
          "seafloor spreading and rift valleys. Hot spots and faults appear only in "
          "ERT-4.A.4's list of what a boundary record locates, with no boundary type "
          "attached to either."),

 dict(q="Each of the three boundary statements says a boundary CAN RESULT IN certain "
        "features. What does that phrasing establish?",
      choices=[
        "The features named are possible results of that kind of boundary rather than ones "
        "present at every boundary of that kind",
        "The features named are present at every boundary of that kind without exception",
        "The features named have never actually been observed at such a boundary",
        "The features named occur only after an earthquake has already happened",
        "The features named are the only features found anywhere on Earth"],
      ans=0,
      why="CAN RESULT IN commits the framework to the connection between a boundary type "
          "and the features it names while stopping short of asserting that every such "
          "boundary carries all of them. Hardening it into every case is stronger than the "
          "statement, and denying the connection is weaker."),

 dict(q="A mountain belt is rising where two plates move toward one another, and volcanoes "
        "and frequent earthquakes lie along it. Which statement covers that case?",
      choices=[
        "Convergent boundaries can result in the creation of mountains, island arcs, "
        "earthquakes, and volcanoes",
        "Divergent boundaries can result in seafloor spreading, rift valleys, volcanoes, "
        "and earthquakes",
        "Transform boundaries can result in earthquakes",
        "An earthquake occurs when stress overcomes a locked fault, releasing stored energy",
        "A record of plate boundaries can be used to locate hot spots and faults"],
      ans=0,
      why="Plates moving toward one another meet at a convergent boundary, and ERT-4.A.1 "
          "names mountains, volcanoes and earthquakes among what such a boundary can "
          "result in. The remaining statements describe a different boundary type, the "
          "mechanism of a single earthquake, or the use of a boundary record."),

 dict(q="A long valley is opening where the crust is being pulled apart, with volcanoes and "
        "earthquakes along its floor. Which statement covers that case?",
      choices=[
        "Divergent boundaries can result in seafloor spreading, rift valleys, volcanoes, "
        "and earthquakes",
        "Convergent boundaries can result in the creation of mountains, island arcs, "
        "earthquakes, and volcanoes",
        "Transform boundaries can result in earthquakes",
        "An earthquake occurs when stress overcomes a locked fault, releasing stored energy",
        "A record of plate boundaries can be used to locate hot spots and faults"],
      ans=0,
      why="Crust being pulled apart is a divergent boundary, and ERT-4.A.2 names rift "
          "valleys, volcanoes and earthquakes among what such a boundary can result in. "
          "The convergent list has no rift valley in it."),

 dict(q="Along one boundary the two plates slide past one another; earthquakes are frequent "
        "there, but no volcanoes and no rising mountains have been found. Which statement "
        "covers that case?",
      choices=[
        "Transform boundaries can result in earthquakes",
        "Convergent boundaries can result in the creation of mountains, island arcs, "
        "earthquakes, and volcanoes",
        "Divergent boundaries can result in seafloor spreading, rift valleys, volcanoes, "
        "and earthquakes",
        "An earthquake occurs when stress overcomes a locked fault, releasing stored energy",
        "A record of plate boundaries can be used to locate hot spots and faults"],
      ans=0,
      why="Plates sliding past one another meet at a transform boundary, and ERT-4.A.3 "
          "names earthquakes and nothing else for that type, which is exactly what the "
          "case reports. Both other boundary statements include volcanoes."),

 dict(q="Why is knowing the global distribution of plate boundaries especially useful for "
        "locating earthquakes in particular?",
      choices=[
        "The framework attributes earthquakes to convergent, divergent and transform "
        "boundaries alike, so every boundary is a place they can occur",
        "The framework attributes earthquakes to transform boundaries only, so only those "
        "stretches matter",
        "The framework attributes earthquakes to convergent boundaries only, so only those "
        "stretches matter",
        "The framework makes no connection between earthquakes and plate boundaries",
        "The framework states that earthquakes occur only away from plate boundaries"],
      ans=0,
      why="Earthquakes appear in all three of ERT-4.A.1, ERT-4.A.2 and ERT-4.A.3, and "
          "ERT-4.A.4 puts earthquakes among the things the global distribution of "
          "boundaries can be used to locate. No statement restricts them to one boundary "
          "type or places them away from boundaries."),

 dict(q="Which of the following does the framework NOT attribute to divergent boundaries?",
      choices=["The creation of island arcs", "Seafloor spreading", "Rift valleys",
               "Volcanoes", "Earthquakes"],
      ans=0,
      why="ERT-4.A.2 names seafloor spreading, rift valleys, volcanoes and earthquakes. "
          "Island arcs appear in ERT-4.A.1, among what convergent boundaries can result "
          "in, and in no other statement."),

 dict(q="Which of the following does the framework NOT attribute to convergent boundaries?",
      choices=["Rift valleys", "The creation of mountains", "Island arcs", "Volcanoes",
               "Earthquakes"],
      ans=0,
      why="ERT-4.A.1 names mountains, island arcs, earthquakes and volcanoes. Rift valleys "
          "appear in ERT-4.A.2, among what divergent boundaries can result in, and in no "
          "other statement."),

 dict(q="A student reasons that because transform boundaries produce earthquakes, they must "
        "produce volcanoes as well. What is wrong with that reasoning?",
      choices=[
        "The framework names only earthquakes for transform boundaries, and names volcanoes "
        "for the other two kinds of boundary",
        "Nothing is wrong, because the framework names volcanoes for transform boundaries "
        "as well",
        "The framework names no feature at all for transform boundaries",
        "The framework names volcanoes for transform boundaries only",
        "The framework names earthquakes for convergent boundaries only"],
      ans=0,
      why="ERT-4.A.3 is a single clause naming earthquakes, while ERT-4.A.1 and ERT-4.A.2 "
          "each name volcanoes. Sharing one feature with those statements does not carry "
          "the rest of their lists across."),

 dict(q="What does the framework's statement about how an earthquake happens add that the "
        "three boundary statements do not?",
      choices=[
        "A mechanism, in which stress overcomes a locked fault and stored energy is released",
        "A list of the features found at each kind of boundary",
        "The global distribution of the boundaries themselves",
        "The speed at which the plates move past one another",
        "The depth beneath the surface at which the shaking begins"],
      ans=0,
      why="ERT-4.A.1 to ERT-4.A.3 say which features a boundary type can result in, and "
          "ERT-4.A.5 says what happens for one earthquake to occur. Neither the speed of "
          "the plates nor the depth of an earthquake appears anywhere in the topic."),

 dict(q="Three boundaries were surveyed for the features found along them. Which record "
        "matches what the framework attributes to a convergent boundary?",
      table=_T_BOUNDARY,
      choices=[
        "The boundary where the plates move toward each other, which records mountains, "
        "volcanoes and earthquakes together",
        "The boundary where the plates move apart, which records no mountains",
        "The boundary where the plates slide past each other, which records neither "
        "mountains nor volcanoes",
        "All three boundaries equally, since each records earthquakes",
        "None of the three, since no boundary records every feature the framework names"],
      ans=0,
      why="Only one of the three records mountain ranges, and it is the one along which the "
          "plates move toward each other; it also records volcanoes and earthquakes. "
          "ERT-4.A.1 names mountains, island arcs, earthquakes and volcanoes as what a "
          "convergent boundary can result in."),

 dict(q="Using the same survey, which record matches what the framework attributes to a "
        "transform boundary?",
      table=_T_BOUNDARY,
      choices=[
        "The boundary where the plates slide past each other, which records earthquakes but "
        "no volcanoes and no mountains",
        "The boundary where the plates move toward each other, which records mountains as "
        "well",
        "The boundary where the plates move apart, which records volcanoes as well",
        "All three boundaries equally, since each records earthquakes",
        "None of the three, since the survey does not report volcanoes"],
      ans=0,
      why="Exactly one of the three records earthquakes with neither volcanoes nor mountain "
          "ranges beside them, and it is the boundary along which the plates slide past "
          "each other. ERT-4.A.3 names earthquakes and nothing further for a transform "
          "boundary."),

 dict(q="Along which of the surveyed boundaries were the most earthquakes recorded?",
      table=_T_BOUNDARY,
      choices=[
        "The boundary where the plates slide past each other",
        "The boundary where the plates move toward each other",
        "The boundary where the plates move apart",
        "All three recorded the same number of earthquakes",
        "None of the three recorded any earthquakes"],
      ans=0,
      why="The three counts differ and the largest belongs to the boundary along which the "
          "plates slide past each other. All three counts are above zero, which is "
          "consistent with ERT-4.A.1, ERT-4.A.2 and ERT-4.A.3 naming earthquakes for every "
          "boundary type."),

 dict(q="How many more earthquakes were recorded along the boundary where the plates slide "
        "past each other than along the boundary where they move apart?",
      table=_T_BOUNDARY,
      choices=["270 more", "150 more", "120 more", "790 more",
               "The survey does not allow that comparison"],
      ans=0,
      why="The two counts are 530 and 260, and 530 less 260 is 270. The rejected values are "
          "the differences between other pairs of rows and the sum of the two counts."),

 dict(q="Rock was dated at four points on a line running away from the crest of a "
        "mid-ocean ridge. What does the record establish?",
      table=_T_SPREAD,
      choices=[
        "The rock is older the farther it lies from the ridge crest",
        "The rock is younger the farther it lies from the ridge crest",
        "The rock is the same age at every distance from the ridge crest",
        "The rock is oldest at the ridge crest itself",
        "Distance from the crest and the age of the rock are unrelated in the record"],
      ans=0,
      why="The recorded age rises at every step as the distance from the crest rises, and "
          "the youngest rock lies at the crest. ERT-4.A.2 names seafloor spreading among "
          "what a divergent boundary can result in, and new seafloor forming at the crest "
          "and moving away is what that pattern of ages records."),

 dict(q="At what rate did the seafloor move away from that ridge crest, according to the "
        "same record?",
      table=_T_SPREAD,
      choices=[
        "About 20 kilometers per million years",
        "About 6 kilometers per million years",
        "About 120 kilometers per million years",
        "About 2 kilometers per million years",
        "A rate cannot be formed from the record"],
      ans=0,
      why="The farthest point lies 120 kilometers from the crest and its rock is 6 million "
          "years old, and 120 divided by 6 is 20. The rejected values are the two "
          "quantities themselves and the age at an intermediate point."),

 dict(q="Three segments of one fault were watched until each moved. What does the record "
        "establish about the energy an earthquake releases?",
      table=_T_QUAKE,
      choices=[
        "The energy released matched the stress that had been stored while the segment "
        "stayed locked",
        "The energy released bore no relation to the stress that had been stored",
        "The energy released was greatest where the least stress had been stored",
        "The same energy was released on all three segments",
        "The record reports the stress stored but no energy released"],
      ans=0,
      why="On every segment the energy released equals the stress stored, and the three "
          "amounts differ from one another. ERT-4.A.5 states that an earthquake occurs when "
          "stress overcomes a locked fault, releasing stored energy."),

 dict(q="Using the same three segments, which had stored the most stress before it moved?",
      table=_T_QUAKE,
      choices=[
        "The segment that had also stayed locked the longest",
        "The segment that had stayed locked for the shortest time",
        "The segment that had stayed locked for an intermediate time",
        "All three had stored the same amount of stress",
        "The record reports the energy released but not the stress stored"],
      ans=0,
      why="The largest stored stress and the longest time locked belong to the same "
          "segment, and both are unique in their columns. ERT-4.A.5 makes the stress that "
          "builds on a locked fault the thing that is eventually released."),

 dict(q="Features of three kinds were counted by their distance from the nearest mapped "
        "plate boundary. What does the record establish?",
      table=_T_LOCATE,
      choices=[
        "Every kind of feature is far more common near a boundary than away from one, so "
        "the boundaries locate them",
        "Every kind of feature is more common away from a boundary than near one",
        "The features are spread evenly with respect to the boundaries",
        "Only the earthquake epicenters are concentrated near the boundaries",
        "The record counts the features but not their distance from a boundary"],
      ans=0,
      why="For each of the three kinds the count near a boundary exceeds the count away "
          "from one by several times over. ERT-4.A.4 states that the global distribution of "
          "plate boundaries can be used to determine the location of volcanoes, island "
          "arcs, earthquakes, hot spots, and faults."),
]
