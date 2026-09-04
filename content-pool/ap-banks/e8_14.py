# AP ENVIRONMENTAL SCIENCE 8.14 Pollution and Human Health
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding EIN-3, pollutants can have both direct and indirect impacts on the health
# of organisms, including humans. Learning objective EIN-3.C: identify sources of human
# health issues that are linked to pollution. Suggested skill 4.C, describe an aspect of
# a research method, design, and/or measure used.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-3.C.1  It can be difficult to establish a cause and effect between pollutants and
#              human health issues because humans experience exposure to a variety of
#              chemicals and pollutants.
#   EIN-3.C.2  Dysentery is caused by untreated sewage in streams and rivers.
#   EIN-3.C.3  Mesothelioma is a type of cancer caused mainly by exposure to asbestos.
#   EIN-3.C.4  Respiratory problems and overall lung function can be impacted by elevated
#              levels of tropospheric ozone.
#
# THE OZONE SWAP. EIN-3.C.4 is about ELEVATED ozone in the TROPOSPHERE, near the ground.
# Topic 9.1 is about DEPLETED ozone in the STRATOSPHERE, whose health consequences the
# framework gives as skin cancer and cataracts (STB-4.A.3). Confusing the two is one of
# the most common errors in this course, so items 5, 14 and 24 invite exactly that
# confusion and their anchors in verify_e8_14.py carry BOTH clauses -- the direction of
# the change AND the layer -- so an anchor cannot match the swapped option.
#
# ON SCOPE. Topic 8.15 keys pathogens and the diseases EIN-3.D.1 to EIN-3.D.12 names;
# dysentery is not on that list and is keyed here under EIN-3.C.2. Topic 8.11 keys the
# stages of sewage treatment; nothing here restates them. Topic 7.2 keys photochemical
# smog; nothing here keys how tropospheric ozone forms, only what elevated levels of it
# do to the respiratory system.
#
# ON THE FIGURES. The bank carries no images, so every representation is a table and
# every keyed reading is recomputed in verify_e8_14.py from that table alone.
#
# NOT KEYED: no exposure limit, no incidence figure for a real place, no latency period,
# no other disease attributed to any of these pollutants. The framework states none.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.14", "Pollution and Human Health", 8)

_T_SEWAGE = dict(
    headers=["Village on the same river", "Is sewage treated before it enters the stream",
             "Dysentery cases per thousand people each year"],
    rows=[["Village 1", "no", "62"],
          ["Village 2", "no", "48"],
          ["Village 3", "yes", "5.0"],
          ["Village 4", "yes", "3.0"]])

_T_ASBESTOS = dict(
    headers=["Group of workers followed", "Years spent working with asbestos",
             "Mesothelioma cases per hundred thousand people"],
    rows=[["Group A", "0", "1.0"],
          ["Group B", "5.0", "18"],
          ["Group C", "20", "96"]])

_T_OZONE = dict(
    headers=["Day of the study",
             "Ozone measured near the ground (parts per billion)",
             "Hospital visits for breathing problems"],
    rows=[["Day 1", "25", "12"],
          ["Day 2", "48", "21"],
          ["Day 3", "76", "44"],
          ["Day 4", "102", "68"]])

_T_MULTI = dict(
    headers=["Group of people studied",
             "Number of different pollutants above background in their air and water",
             "Respiratory illnesses reported per hundred people"],
    rows=[["Group 1", "1", "8.0"],
          ["Group 2", "3", "14"],
          ["Group 3", "6", "23"]])

_T_LUNG = dict(
    headers=["Group of children tested",
             "Ozone near the ground on the days of testing (parts per billion)",
             "Average lung function score"],
    rows=[["Group 1", "20", "100"],
          ["Group 2", "55", "92"],
          ["Group 3", "95", "81"]])

_T_TIME = dict(
    headers=["Time relative to the opening of a sewage treatment plant",
             "Untreated sewage entering the river (millions of liters per day)",
             "Dysentery cases reported per thousand people"],
    rows=[["Three years before", "40", "58"],
          ["One year before", "38", "54"],
          ["Two years after", "6.0", "12"],
          ["Five years after", "2.0", "4.0"]])

QUESTIONS = [

 dict(q="Why does the framework say it can be difficult to establish cause and effect "
        "between pollutants and human health issues?",
      choices=[
        "Because humans experience exposure to a variety of chemicals and pollutants at "
        "the same time",
        "Because pollutants have no measurable effect on human health",
        "Because human health issues cannot be counted or recorded",
        "Because every pollutant produces exactly the same illness",
        "Because only one pollutant is ever present in a given place"],
      ans=0,
      why="EIN-3.C.1 states that it can be difficult to establish a cause and effect "
          "between pollutants and human health issues because humans experience exposure "
          "to a variety of chemicals and pollutants. Each rejected option denies that "
          "difficulty or its stated reason."),

 dict(q="What does the framework give as the cause of dysentery?",
      choices=[
        "Untreated sewage in streams and rivers",
        "Exposure to asbestos fibers in old buildings",
        "Elevated levels of ozone near the ground",
        "Heavy metals leaching from a landfill",
        "Excess nutrients from agricultural runoff"],
      ans=0,
      why="EIN-3.C.2 states that dysentery is caused by untreated sewage in streams and "
          "rivers. Asbestos and tropospheric ozone are the subjects of EIN-3.C.3 and "
          "EIN-3.C.4, and metals and nutrients belong to other topics of this unit."),

 dict(q="Four villages along one river were compared.",
      table=_T_SEWAGE,
      choices=[
        "The villages whose sewage is untreated report many times the dysentery of the "
        "villages whose sewage is treated",
        "The villages whose sewage is treated report more dysentery than the others",
        "All four villages report about the same amount of dysentery",
        "Only one village reports any dysentery at all",
        "Treatment of sewage makes no difference to the dysentery reported"],
      ans=0,
      why="Both untreated rows carry figures many times larger than either treated row. "
          "EIN-3.C.2 states that dysentery is caused by untreated sewage in streams and "
          "rivers."),

 dict(q="What does the framework give as the main cause of mesothelioma?",
      choices=[
        "Exposure to asbestos",
        "Drinking water contaminated with untreated sewage",
        "Breathing ozone that has built up near the ground",
        "Eating fish that carry a biomagnified pollutant",
        "Living near a landfill that releases methane"],
      ans=0,
      why="EIN-3.C.3 states that mesothelioma is a type of cancer caused mainly by "
          "exposure to asbestos. Sewage is EIN-3.C.2, tropospheric ozone is EIN-3.C.4, and "
          "biomagnification and landfill gas belong to other topics."),

 dict(q="Which health effects does the framework attach to ozone, and to ozone in which "
        "part of the atmosphere?",
      choices=[
        "Respiratory problems and overall lung function, from elevated levels of ozone in "
        "the troposphere near the ground",
        "Respiratory problems and overall lung function, from depleted ozone in the "
        "stratosphere high above the ground",
        "Skin cancer and cataracts, from elevated ozone near the ground",
        "Dysentery and intestinal illness, from ozone near the ground",
        "Mesothelioma, from ozone in the stratosphere"],
      ans=0,
      why="EIN-3.C.4 states that respiratory problems and overall lung function can be "
          "impacted by elevated levels of tropospheric ozone, which is ozone near the "
          "ground. Skin cancer and cataracts belong to STB-4.A.3, which concerns a "
          "decrease in stratospheric ozone, a different layer and the opposite direction "
          "of change."),

 dict(q="Three groups of workers with different histories were followed.",
      table=_T_ASBESTOS,
      choices=[
        "The longer a group worked with asbestos, the higher its rate of the cancer the "
        "framework links to asbestos",
        "The longer a group worked with asbestos, the lower its rate of that cancer",
        "All three groups show the same rate of that cancer",
        "The group with no asbestos work shows the highest rate of that cancer",
        "Years of asbestos work tell nothing about the rate in these data"],
      ans=0,
      why="Ranking the groups by years worked gives the same order as ranking them by the "
          "case rate, and the group with none is lowest. EIN-3.C.3 states that "
          "mesothelioma is a type of cancer caused mainly by exposure to asbestos."),

 dict(q="A study finds that people living near a busy industrial area have more illness "
        "than people elsewhere but cannot say which pollutant is responsible. Which "
        "framework statement describes that situation?",
      choices=[
        "Establishing cause and effect is difficult because humans are exposed to a "
        "variety of chemicals and pollutants",
        "Dysentery is caused by untreated sewage in streams and rivers",
        "Mesothelioma is a cancer caused mainly by exposure to asbestos",
        "Elevated tropospheric ozone can affect respiratory problems and lung function",
        "Pollutants have no relationship to human health"],
      ans=0,
      why="EIN-3.C.1 gives the simultaneous exposure of humans to a variety of chemicals "
          "and pollutants as the reason cause and effect is hard to establish, which is "
          "exactly the study's difficulty. The other statements each name one specific "
          "link."),

 dict(q="Which disease does the framework link to a specific mineral fiber rather than to "
        "a waterborne or airborne pollutant?",
      choices=[
        "Mesothelioma",
        "Dysentery",
        "A respiratory problem caused by ozone near the ground",
        "An intestinal illness caused by sewage in a river",
        "A reduction in overall lung function"],
      ans=0,
      why="EIN-3.C.3 attributes mesothelioma mainly to exposure to asbestos, which is a "
          "mineral fiber. EIN-3.C.2 attributes dysentery to untreated sewage in water and "
          "EIN-3.C.4 attributes respiratory effects to elevated tropospheric ozone."),

 dict(q="Ozone measured near the ground and hospital visits were recorded on four days.",
      table=_T_OZONE,
      choices=[
        "The days with the highest ozone near the ground carried the most hospital visits "
        "for breathing problems",
        "The days with the highest ozone near the ground carried the fewest such visits",
        "The number of visits was the same on all four days",
        "The day with the lowest ozone carried the most visits",
        "Ozone near the ground and breathing problems are unrelated in these data"],
      ans=0,
      why="Ranking the days by ozone measured near the ground gives the same order as "
          "ranking them by hospital visits. EIN-3.C.4 states that respiratory problems can "
          "be impacted by elevated levels of tropospheric ozone."),

 dict(q="Which measure would most directly capture the effect the framework attributes to "
        "elevated tropospheric ozone?",
      choices=[
        "A test of how well the lungs of exposed people are working",
        "A count of the number of vehicles registered in the city",
        "A survey of how many people have heard of ozone",
        "A measurement of the depth of the nearest river",
        "A record of the number of days it rained during the study"],
      ans=0,
      why="EIN-3.C.4 names respiratory problems and overall lung function as what elevated "
          "tropospheric ozone can affect, so a measure of lung function is the measure "
          "aligned with the claim. Vehicle counts, awareness, river depth and rainfall are "
          "not health measures."),

 dict(q="Why is a health study easier to interpret when the group studied is exposed to "
        "one pollutant well above background rather than to several?",
      choices=[
        "With one pollutant standing out, an observed health difference is less likely to "
        "belong to some other exposure",
        "With one pollutant standing out, the health difference must be larger",
        "With several pollutants present, no health difference can ever be measured",
        "With several pollutants present, the study needs fewer participants",
        "The number of pollutants has no bearing on how a study is interpreted"],
      ans=0,
      why="EIN-3.C.1 states that establishing cause and effect is difficult because humans "
          "experience exposure to a variety of chemicals and pollutants, so reducing the "
          "number of competing exposures is what makes an attribution more secure."),

 dict(q="Three groups of people were compared on their exposures and their illness rates.",
      table=_T_MULTI,
      choices=[
        "Illness rises with the number of pollutants present, so no single pollutant in "
        "the table can be identified as the cause",
        "The table identifies exactly which pollutant causes the illness",
        "Illness falls as the number of pollutants rises",
        "All three groups report the same illness rate",
        "The group exposed to the most pollutants reports the least illness"],
      ans=0,
      why="The table records only how many pollutants are elevated, not which, and the "
          "illness rate rises with that count. EIN-3.C.1 states that exposure to a variety "
          "of chemicals and pollutants is what makes cause and effect difficult to "
          "establish."),

 dict(q="A village draws its drinking water from a stream that receives sewage from "
        "upstream homes with no treatment. Which health outcome does the framework link "
        "most directly to that situation?",
      choices=[
        "Dysentery",
        "Mesothelioma",
        "A reduction in lung function from ozone",
        "Skin cancer from ultraviolet exposure",
        "A respiratory illness from asbestos fibers"],
      ans=0,
      why="EIN-3.C.2 states that dysentery is caused by untreated sewage in streams and "
          "rivers. Mesothelioma is asbestos under EIN-3.C.3, lung function is tropospheric "
          "ozone under EIN-3.C.4, and skin cancer belongs to STB-4.A.3."),

 dict(q="Which layer's ozone does this topic connect to human health, and in which "
        "direction?",
      choices=[
        "Tropospheric ozone near the ground, when its levels are elevated",
        "Stratospheric ozone high above the ground, when its levels are depleted",
        "Tropospheric ozone near the ground, when its levels are depleted",
        "Stratospheric ozone high above the ground, when its levels are elevated",
        "Ozone in any layer, in either direction, with the same consequences"],
      ans=0,
      why="EIN-3.C.4 concerns elevated levels of tropospheric ozone. STB-4.A.3 concerns a "
          "decrease in stratospheric ozone and attaches skin cancer and cataracts to it, "
          "so both the layer and the direction of the change differ between the two "
          "statements."),

 dict(q="Which pairing of a health issue with the pollutant the framework names is "
        "correct?",
      choices=[
        "Mesothelioma, paired with exposure to asbestos",
        "Mesothelioma, paired with untreated sewage in a river",
        "Dysentery, paired with elevated ozone near the ground",
        "Reduced lung function, paired with exposure to asbestos",
        "Dysentery, paired with exposure to asbestos"],
      ans=0,
      why="EIN-3.C.3 attributes mesothelioma mainly to asbestos, EIN-3.C.2 attributes "
          "dysentery to untreated sewage in streams and rivers, and EIN-3.C.4 attributes "
          "respiratory effects to elevated tropospheric ozone. Each rejected pairing "
          "crosses two of those."),

 dict(q="Lung function was measured in three groups of children on days with different "
        "ground level ozone.",
      table=_T_LUNG,
      choices=[
        "The group tested on the days with the most ozone near the ground had the lowest "
        "average lung function score",
        "The group tested on the days with the most ozone near the ground had the highest "
        "score",
        "All three groups recorded the same average score",
        "The group tested on the cleanest days had the lowest score",
        "Ozone near the ground and lung function are unrelated in these data"],
      ans=0,
      why="Ranking the groups by ozone measured near the ground gives the reverse of the "
          "order by lung function score. EIN-3.C.4 states that overall lung function can "
          "be impacted by elevated levels of tropospheric ozone."),

 dict(q="A researcher wants to attribute an illness to one pollutant. Which feature of a "
        "study design most directly addresses the difficulty the framework names?",
      choices=[
        "Recording every other pollutant the participants are exposed to so that those "
        "exposures can be accounted for",
        "Increasing the number of pages in the final report",
        "Choosing participants who live closest to the researcher's laboratory",
        "Measuring the illness only once, at the end of the study",
        "Reporting the results in a journal read by many scientists"],
      ans=0,
      why="EIN-3.C.1 names simultaneous exposure to a variety of chemicals and pollutants "
          "as the source of the difficulty, so measuring the other exposures is what a "
          "design can do about it. Report length, convenience sampling, a single "
          "measurement and readership do not."),

 dict(q="Which of the following does the framework NOT state in this topic?",
      choices=[
        "That a single pollutant can always be identified as the cause of an illness",
        "That dysentery is caused by untreated sewage in streams and rivers",
        "That mesothelioma is caused mainly by exposure to asbestos",
        "That elevated tropospheric ozone can affect respiratory problems and lung "
        "function",
        "That humans are exposed to a variety of chemicals and pollutants"],
      ans=0,
      why="EIN-3.C.1 states the opposite, that the variety of simultaneous exposures makes "
          "cause and effect difficult to establish. The four rejected options restate "
          "EIN-3.C.1 through EIN-3.C.4 correctly."),

 dict(q="A worker who spent decades installing insulation containing asbestos develops a "
        "cancer of the lining of the chest. Which framework statement bears on that case?",
      choices=[
        "Mesothelioma is a type of cancer caused mainly by exposure to asbestos",
        "Dysentery is caused by untreated sewage in streams and rivers",
        "Elevated tropospheric ozone can affect respiratory problems and lung function",
        "Humans experience exposure to a variety of chemicals and pollutants",
        "A decrease in stratospheric ozone increases the ultraviolet rays reaching the "
        "surface"],
      ans=0,
      why="EIN-3.C.3 attributes mesothelioma mainly to exposure to asbestos, which is the "
          "worker's history. The rejected statements concern sewage, ozone near the ground, "
          "the general difficulty of attribution, and the stratosphere."),

 dict(q="A river town's records were examined before and after a sewage treatment plant "
        "opened.",
      table=_T_TIME,
      choices=[
        "Both the untreated sewage entering the river and the dysentery cases fell sharply "
        "after the plant opened",
        "The untreated sewage fell but the dysentery cases rose after the plant opened",
        "Neither figure changed after the plant opened",
        "The untreated sewage rose after the plant opened",
        "The dysentery cases were highest in the years after the plant opened"],
      ans=0,
      why="Both columns are several times smaller in the rows after the opening than in "
          "the rows before it. EIN-3.C.2 states that dysentery is caused by untreated "
          "sewage in streams and rivers."),

 dict(q="Why does the framework say mesothelioma is caused mainly by asbestos rather than "
        "caused only by asbestos?",
      choices=[
        "The wording leaves room for the difficulty it also states, that people are "
        "exposed to many chemicals and pollutants at once",
        "The wording means asbestos has no role in the disease",
        "The wording means the disease is caused by every pollutant equally",
        "The wording means asbestos causes every kind of cancer",
        "The wording means the disease has no known cause"],
      ans=0,
      why="EIN-3.C.3 uses the word mainly, and EIN-3.C.1 states that establishing cause "
          "and effect is difficult because humans experience exposure to a variety of "
          "chemicals and pollutants, so the qualifier is consistent with the framework's "
          "own caution."),

 dict(q="Which study design would best support the framework's claim about ground level "
        "ozone and breathing?",
      choices=[
        "Measuring ozone near the ground and lung function in the same people across days "
        "with different ozone levels",
        "Measuring ozone near the ground once and asking people whether they feel healthy",
        "Measuring lung function once in people whose ozone exposure is unknown",
        "Counting the number of ozone stories published in the newspaper",
        "Measuring stratospheric ozone above the study area over several years"],
      ans=0,
      why="EIN-3.C.4 links elevated tropospheric ozone to respiratory problems and lung "
          "function, so both the ground level ozone and the lung measure must vary and be "
          "recorded together. Measuring the stratosphere tests a different statement "
          "entirely."),

 dict(q="Which evidence would most strengthen the claim that a community's illness comes "
        "from sewage in its river rather than from something else?",
      choices=[
        "Illness falls sharply in the community after the sewage entering the river is "
        "treated, with other conditions unchanged",
        "The community is located beside a river",
        "The river is wider downstream than upstream",
        "The community has grown in population over the same period",
        "The river carries more water in spring than in autumn"],
      ans=0,
      why="EIN-3.C.2 names untreated sewage in streams and rivers as the cause of "
          "dysentery, and EIN-3.C.1 warns that many exposures compete, so a change in the "
          "sewage with other conditions held steady is what isolates it. Location, channel "
          "width, population growth and seasonal flow do not."),

 dict(q="What does the word elevated do in the framework's statement about tropospheric "
        "ozone?",
      choices=[
        "It specifies that the respiratory effects follow from higher than usual amounts "
        "of ozone near the ground",
        "It specifies that the ozone in question sits high above the ground in the "
        "stratosphere",
        "It specifies that the effects follow from a shortage of ozone near the ground",
        "It specifies that the ozone is measured at a high altitude station",
        "It specifies that the effects are elevated rather than the ozone"],
      ans=0,
      why="EIN-3.C.4 attaches respiratory problems and lung function to elevated levels of "
          "tropospheric ozone, so the word describes how much ozone is present near the "
          "ground. STB-4.A.3 concerns a decrease in ozone in a different layer."),

 dict(q="Why is the link between asbestos and mesothelioma easier to establish than a link "
        "between general urban air pollution and illness?",
      choices=[
        "The framework attributes that cancer mainly to one exposure, while urban air "
        "carries the variety of chemicals and pollutants that makes attribution hard",
        "Urban air contains no pollutants at all",
        "Mesothelioma can be diagnosed without any medical examination",
        "Asbestos is the only pollutant that has any health effect",
        "The framework says urban air pollution has no health consequences"],
      ans=0,
      why="EIN-3.C.3 names asbestos as the main cause of mesothelioma while EIN-3.C.1 "
          "states that exposure to a variety of chemicals and pollutants is what makes "
          "cause and effect difficult, and urban air is the case with many exposures at "
          "once."),

 dict(q="Which action follows most directly from the framework's statement about "
        "dysentery?",
      choices=[
        "Treating sewage before it is allowed to enter streams and rivers",
        "Removing asbestos from older buildings",
        "Reducing the ozone that forms near the ground on hot days",
        "Restoring the ozone layer high in the atmosphere",
        "Capping a landfill to stop gas from escaping"],
      ans=0,
      why="EIN-3.C.2 states that dysentery is caused by untreated sewage in streams and "
          "rivers, so treating the sewage addresses the stated cause. The rejected actions "
          "address asbestos, ozone in either layer, and landfill gas."),

 dict(q="A study reports higher rates of several illnesses in a neighborhood with an "
        "incinerator, a highway and an old industrial site. What does the framework "
        "caution about such a result?",
      choices=[
        "The residents are exposed to a variety of chemicals and pollutants, so the "
        "illnesses cannot be assigned to one source from this result alone",
        "The result proves that the incinerator is responsible",
        "The result proves that none of the three sources is responsible",
        "The result cannot be reported because several sources are present",
        "The result shows that pollution has no effect on human health"],
      ans=0,
      why="EIN-3.C.1 states that it can be difficult to establish a cause and effect "
          "between pollutants and human health issues because humans experience exposure "
          "to a variety of chemicals and pollutants, which is precisely this "
          "neighborhood's situation."),

 dict(q="Which measure best matches the health outcome the framework names for elevated "
        "ozone near the ground?",
      choices=[
        "The share of a group reporting breathing difficulty together with a measured "
        "index of lung performance",
        "The share of a group reporting stomach illness",
        "The number of cancers of the lining of the chest recorded in a group",
        "The number of people who moved into the area during the study",
        "The concentration of a pollutant measured in a river"],
      ans=0,
      why="EIN-3.C.4 names respiratory problems and overall lung function, so a "
          "respiratory report combined with a lung measurement is the aligned measure. "
          "Stomach illness is EIN-3.C.2 and the chest lining cancer is EIN-3.C.3."),

 dict(q="Which of the following best describes what this topic asks a student to be able "
        "to do?",
      choices=[
        "Identify particular human health issues that the framework links to particular "
        "pollutants, while recognizing why such links are hard to establish in general",
        "Calculate the dose of a chemical that kills half of a population",
        "Describe the stages by which sewage is treated at a plant",
        "Explain how ozone is formed in the atmosphere",
        "List the components of a sanitary municipal landfill"],
      ans=0,
      why="Learning objective EIN-3.C is to identify sources of human health issues that "
          "are linked to pollution, and EIN-3.C.1 supplies the caution about attribution. "
          "The rejected options belong to topics 8.12, 8.11, unit 7 and 8.9."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Untreated sewage in streams and rivers causes dysentery, asbestos is the main "
        "cause of mesothelioma, and elevated ozone near the ground affects breathing and "
        "lung function, but attributing illness to one pollutant is difficult because "
        "people are exposed to many at once",
        "Every human illness can be traced to a single identified pollutant without "
        "difficulty",
        "Dysentery comes from asbestos and mesothelioma comes from sewage",
        "Ozone affects human health only when the ozone layer high in the atmosphere is "
        "depleted",
        "Pollutants have no established link to any human health issue"],
      ans=0,
      why="Each clause of the keyed summary is one of EIN-3.C.1 through EIN-3.C.4. Every "
          "rejected summary denies the stated difficulty, swaps two causes, moves the "
          "ozone effect to the wrong layer, or denies the links altogether."),
]
