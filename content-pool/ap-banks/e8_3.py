# AP ENVIRONMENTAL SCIENCE 8.3 Endocrine Disruptors
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding STB-3. Learning objectives STB-3.C, describe endocrine disruptors, and
# STB-3.D, describe the effects of endocrine disruptors on ecosystems. Suggested skill
# 1.A, describe environmental concepts and processes.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-3.C.1  Endocrine disruptors are chemicals that can interfere with the endocrine
#              system of animals.
#   STB-3.D.1  Endocrine disruptors can lead to birth defects, developmental disorders,
#              and gender imbalances in fish and other species.
#
# WHAT IS PRESUPPOSED, STATED SO IT CAN BE CHECKED. The framework uses the term
# endocrine system without defining it and does not describe any mechanism of
# interference -- no receptor, no mimicry, no hormone named. So the only content
# presupposed anywhere in this module is that the endocrine system is an animal's
# hormone system and that to interfere with it is to disturb its normal working. No
# key states how a disruptor acts at the molecular level, because the framework does
# not.
#
# WHAT IS NOT KEYED. No chemical is named as an endocrine disruptor. The framework
# names none in this topic, and DDT and PCBs appear in STB-3.H.1 as persistent organic
# pollutants rather than as endocrine disruptors, so this module keeps them out. No
# concentration, dose or threshold is keyed either; every number belongs to the study
# in its own table and is recomputed in verify_e8_3.py.
#
# ON SCOPE. Persistence and fat solubility belong to 8.7, bioaccumulation to 8.8, and
# dose-response measurement to 8.12 and 8.13. This topic keys what an endocrine
# disruptor is and the three kinds of effect the framework lists.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.3", "Endocrine Disruptors", 8)

_T_SEXRATIO = dict(
    headers=["Sampling reach", "Position relative to the effluent outfall",
             "Male fish in the sample (percent)",
             "Fish with both male and female characteristics (percent)"],
    rows=[["Reach 1", "upstream", "49", "0"],
          ["Reach 2", "just downstream", "22", "31"],
          ["Reach 3", "far downstream", "41", "8"]])

_T_DEFORM = dict(
    headers=["Concentration of the test chemical in the tank (micrograms per liter)",
             "Embryos developing normally (percent)",
             "Embryos with visible developmental defects (percent)"],
    rows=[["0", "94", "6"],
          ["1", "81", "19"],
          ["10", "52", "48"],
          ["50", "23", "77"]])

_T_SPECIES = dict(
    headers=["Species sampled in the same contaminated wetland",
             "Individuals examined",
             "Individuals with developmental abnormalities (percent)"],
    rows=[["Fish species A", "200", "34"],
          ["Frog species B", "150", "28"],
          ["Turtle species C", "60", "17"],
          ["Fish species A at a reference wetland", "200", "4"]])

_T_TIMING = dict(
    headers=["Life stage during which the animals were exposed",
             "Adults showing reproductive abnormalities (percent)"],
    rows=[["Exposed as embryos only", "38"],
          ["Exposed as adults only", "9"],
          ["Never exposed", "3"]])

_T_HATCH = dict(
    headers=["Pond", "Chemical measured in the water (micrograms per liter)",
             "Eggs hatching successfully (percent)",
             "Hatchlings with limb or spine defects (percent)"],
    rows=[["Pond 1", "0.2", "88", "3"],
          ["Pond 2", "2.0", "71", "12"],
          ["Pond 3", "9.0", "44", "29"],
          ["Pond 4", "26.0", "21", "51"]])

_T_RECOVERY = dict(
    headers=["Year relative to the closure of the discharge",
             "Chemical in the river (micrograms per liter)",
             "Male fish in the sample (percent)"],
    rows=[["Two years before closure", "14", "24"],
          ["Year of closure", "11", "27"],
          ["Two years after closure", "3", "39"],
          ["Five years after closure", "1", "47"]])

QUESTIONS = [

 dict(q="How does the framework define an endocrine disruptor?",
      choices=[
        "A chemical that can interfere with the endocrine system of animals",
        "A chemical that dissolves the shells of aquatic organisms",
        "A chemical that removes oxygen from water",
        "A microorganism that causes disease in animals",
        "A physical condition of the water such as its temperature"],
      ans=0,
      why="The framework states that endocrine disruptors are chemicals that can "
          "interfere with the endocrine system of animals. Dissolving shells, removing "
          "oxygen, causing infection and altering a physical condition are effects of "
          "other agents described elsewhere in the course."),

 dict(q="Which effects does the framework attribute to endocrine disruptors?",
      choices=[
        "Birth defects, developmental disorders, and gender imbalances in fish and other "
        "species",
        "Immediate suffocation of adult animals within minutes of exposure",
        "Corrosion of shells and skeletons on contact",
        "Permanent hearing loss in aquatic mammals",
        "Increased growth and reproduction in every exposed species"],
      ans=0,
      why="Those three are exactly the effects the framework lists, and it applies them "
          "to fish and other species. Suffocation, corrosion and hearing loss belong to "
          "other pollutants, and the framework describes no benefit from exposure."),

 dict(q="Fish sampled above and below a discharge are compared.",
      table=_T_SEXRATIO,
      choices=[
        "The reach just downstream of the outfall has the smallest share of males and "
        "the largest share of fish with mixed characteristics",
        "The upstream reach has the smallest share of males",
        "The three reaches have identical shares of males",
        "Fish with mixed characteristics appear only upstream of the outfall",
        "The reach far downstream has the largest share of fish with mixed "
        "characteristics"],
      ans=0,
      why="The reach immediately below the outfall carries both the smallest male share "
          "and the largest share of fish with mixed characteristics, with the upstream "
          "reach near an even split and none of the mixed condition. Gender imbalance in "
          "fish is one of the effects the framework lists."),

 dict(q="Which of the following best describes what it means for a chemical to interfere "
        "with an animal's endocrine system?",
      choices=[
        "It disturbs the normal working of the animal's hormone system",
        "It blocks the animal's airway so that it cannot breathe",
        "It reduces the oxygen dissolved in the water around the animal",
        "It raises the temperature of the animal's habitat",
        "It changes the acidity of the water the animal lives in"],
      ans=0,
      why="The endocrine system is an animal's hormone system, so interference with it "
          "is a disturbance of that system's normal working. The rejected options "
          "describe asphyxiation, oxygen depletion, thermal pollution and acidification, "
          "which the framework treats separately."),

 dict(q="Results from a controlled exposure of developing embryos are shown.",
      table=_T_DEFORM,
      choices=[
        "The share of embryos with developmental defects rises with the concentration of "
        "the test chemical",
        "The share of embryos with developmental defects falls as the concentration rises",
        "Defects appear only in the tank with no chemical added",
        "The share developing normally rises with the concentration",
        "The concentration has no effect on either measurement"],
      ans=0,
      why="The defect column rises at every step as the concentration rises and the "
          "normal-development column falls in step with it. Developmental disorders are "
          "one of the effects the framework attributes to endocrine disruptors."),

 dict(q="Which of the following would be the most direct evidence that a chemical is "
        "acting as an endocrine disruptor in a wild population?",
      choices=[
        "A higher frequency of developmental abnormalities and altered sex ratios in "
        "animals exposed to it than in comparable animals that are not",
        "A higher total number of animals living in the exposed area",
        "A measurement showing the chemical is present in the water",
        "A record of how much of the chemical was manufactured last year",
        "A survey showing that residents dislike the smell of the water"],
      ans=0,
      why="The framework's effects are birth defects, developmental disorders and gender "
          "imbalances, so evidence for disruption is a difference in those outcomes "
          "between exposed and comparable unexposed animals. Presence alone, production "
          "figures and opinions do not show an effect."),

 dict(q="Animals of several kinds are sampled in one contaminated wetland.",
      table=_T_SPECIES,
      choices=[
        "Every species in the contaminated wetland shows a higher rate of abnormalities "
        "than the same fish species does at the reference wetland",
        "Only the fish species shows abnormalities in the contaminated wetland",
        "The reference wetland shows the highest rate of abnormalities",
        "The rates of abnormality are identical in all four rows",
        "The turtle species shows the highest rate of abnormalities"],
      ans=0,
      why="All three species sampled in the contaminated wetland carry abnormality rates "
          "several times the rate recorded for the same fish species at the reference "
          "site. The framework applies these effects to fish and other species alike."),

 dict(q="Why does the framework describe the effects of endocrine disruptors in fish and "
        "other species rather than in fish alone?",
      choices=[
        "The effects it names are attributed to fish and other species together",
        "Only fish have an endocrine system",
        "Fish are the only animals ever exposed to chemicals in water",
        "The effects appear in fish but never in amphibians or reptiles",
        "The framework restricts the term to species raised in laboratories"],
      ans=0,
      why="The framework's own wording is birth defects, developmental disorders, and "
          "gender imbalances in fish and other species, so the effects are not confined "
          "to fish. Nothing in it makes the endocrine system unique to fish."),

 dict(q="Results from an experiment varying the life stage at which animals were exposed "
        "are shown.",
      table=_T_TIMING,
      choices=[
        "Exposure during embryonic development produced far more reproductive "
        "abnormalities in adults than exposure during adulthood",
        "Exposure during adulthood produced the most abnormalities",
        "The never-exposed group produced the most abnormalities",
        "All three groups produced the same rate of abnormalities",
        "Exposure at any stage produced no abnormalities"],
      ans=0,
      why="The group exposed as embryos shows about four times the rate of the group "
          "exposed as adults and more than ten times the never-exposed rate. "
          "Developmental disorders and birth defects are among the effects the framework "
          "lists for endocrine disruptors."),

 dict(q="Measurements from four ponds are shown.",
      table=_T_HATCH,
      choices=[
        "As the measured chemical rises, hatching success falls and the share of "
        "hatchlings with defects rises",
        "As the measured chemical rises, hatching success rises",
        "The pond with the most chemical has the fewest hatchlings with defects",
        "Hatching success and defect rate are the same in all four ponds",
        "The chemical measurement is unrelated to both other columns"],
      ans=0,
      why="Ordering the ponds by the measured chemical puts hatching success in "
          "decreasing order and the defect share in increasing order. Birth defects are "
          "one of the effects the framework attributes to endocrine disruptors."),

 dict(q="A river is monitored before and after a discharge is closed.",
      table=_T_RECOVERY,
      choices=[
        "The chemical fell after the discharge closed and the share of male fish rose "
        "toward an even split",
        "The chemical rose after the discharge closed",
        "The share of male fish fell after the discharge closed",
        "Neither measurement changed after the discharge closed",
        "The share of male fish was highest before the discharge closed"],
      ans=0,
      why="The measured chemical falls at every step after closure while the male share "
          "rises at every step toward half the sample. Gender imbalance in fish is one "
          "of the effects the framework names, so its easing as exposure falls is "
          "consistent with that attribution."),

 dict(q="Which of the following is the best reason that an endocrine disruptor can harm "
        "a population without killing any individual outright?",
      choices=[
        "The effects the framework names concern development and reproduction rather "
        "than immediate survival",
        "The chemical is destroyed before it reaches any animal",
        "Endocrine disruptors act only on plants",
        "The chemical is only harmful at concentrations no ecosystem ever reaches",
        "Populations are unaffected by anything that does not kill adults"],
      ans=0,
      why="Birth defects, developmental disorders and gender imbalances are all effects "
          "on the production and development of young rather than on the survival of "
          "exposed adults, which is why a population can be affected without adult "
          "deaths."),

 dict(q="A study finds that a pond receiving runoff has an unusually small proportion of "
        "males among its frogs. Which framework effect does the observation most "
        "directly concern?",
      choices=[
        "Gender imbalance in a species exposed to an endocrine disruptor",
        "Intestinal blockage caused by litter",
        "Corrosion of human-made structures by acid deposition",
        "Reduced light infiltration caused by sediment",
        "Low dissolved oxygen caused by nutrient pollution"],
      ans=0,
      why="A skewed proportion of males is a gender imbalance, which the framework lists "
          "among the effects of endocrine disruptors in fish and other species. The "
          "other options are effects of litter, acid deposition, sediment and nutrients."),

 dict(q="Which comparison would make a study of an endocrine disruptor's effect on a "
        "stream population most convincing?",
      choices=[
        "Animals from the exposed reach compared with animals of the same species from a "
        "similar reach with no exposure, examined in the same way",
        "Animals from the exposed reach compared with animals of a different species from "
        "a distant region",
        "Animals from the exposed reach examined twice by two different observers",
        "Animals from the exposed reach compared with a description written many years "
        "earlier",
        "Animals from the exposed reach counted but not examined"],
      ans=0,
      why="Attributing an effect to the exposure requires a comparison group alike in "
          "species and setting but without the exposure, examined the same way. A "
          "different species, a repeated examination of one group, an old description "
          "and a count without examination cannot supply that."),

 dict(q="Why is the phrase interfere with the endocrine system more accurate than saying "
        "an endocrine disruptor poisons an animal outright?",
      choices=[
        "The framework describes disturbance of a body system leading to defects, "
        "developmental disorders and gender imbalance, rather than immediate lethality",
        "The framework says endocrine disruptors have no effects at all",
        "The framework says endocrine disruptors act only on the nervous system",
        "The framework says the effects appear only in adults",
        "The framework says endocrine disruptors are harmless below a stated dose"],
      ans=0,
      why="The two statements together give a chemical interfering with a body system "
          "and three developmental and reproductive outcomes, which is a different claim "
          "from immediate lethality. The framework states no dose threshold and confines "
          "the effects to no life stage."),

 dict(q="Which of the following observations in a wild population would NOT by itself "
        "indicate an endocrine disruptor is at work?",
      choices=[
        "A decline in the total number of animals following an unusually cold winter",
        "An unusually small proportion of males in successive samples",
        "A high frequency of visible developmental defects in young animals",
        "Individuals showing characteristics of both sexes",
        "A high rate of birth defects compared with an unexposed reference population"],
      ans=0,
      why="A decline after cold weather is a change in numbers with an evident "
          "alternative cause and is not among the framework's three effects. Skewed sex "
          "ratios, mixed characteristics and developmental or birth defects are exactly "
          "what it names."),

 dict(q="Which statement best describes what a student should be able to do with this "
        "topic?",
      choices=[
        "Describe what an endocrine disruptor is and describe the effects it can have on "
        "organisms in ecosystems",
        "Calculate the concentration at which any endocrine disruptor becomes harmful",
        "Name the chemical structures of the principal endocrine disruptors",
        "Explain the sequence of hormone reactions a disruptor alters",
        "Rank endocrine disruptors by the number of species they affect"],
      ans=0,
      why="The two learning objectives are to describe endocrine disruptors and to "
          "describe their effects on ecosystems. The framework supplies no harmful "
          "concentration, no chemical structures, no reaction sequence and no ranking."),

 dict(q="An investigator observes fish with both male and female characteristics "
        "downstream of a treatment plant. Which conclusion is best supported on its own?",
      choices=[
        "The observation is consistent with exposure to a chemical interfering with the "
        "fish's endocrine system, and comparison with an unexposed reach would test that",
        "The observation proves which chemical in the effluent is responsible",
        "The observation shows that the fish were killed by the effluent",
        "The observation shows that the effluent contains no chemicals at all",
        "The observation is unrelated to anything in the effluent under any circumstances"],
      ans=0,
      why="The condition observed is one of the framework's effects, so it is consistent "
          "with endocrine disruption, but a single downstream observation cannot "
          "identify the responsible chemical and does not concern mortality."),

 dict(q="Why can the same chemical concentration produce visible harm in developing "
        "young while adults of the same species appear normal?",
      choices=[
        "The framework's effects include birth defects and developmental disorders, which "
        "are outcomes of exposure during development",
        "Adults are never exposed to chemicals in the same water",
        "Chemicals cannot enter an adult animal at all",
        "Developing young are the only animals that have an endocrine system",
        "Adults convert the chemical into a nutrient"],
      ans=0,
      why="Birth defects and developmental disorders are effects on development itself, "
          "so they appear in animals exposed while developing. The framework does not "
          "confine the endocrine system to the young or make adults immune to exposure."),

 dict(q="A regulator asks what makes endocrine disruptors different from pollutants "
        "measured only by how much of them is lethal. Which answer is best supported?",
      choices=[
        "Their described effects are interference with a body system leading to "
        "developmental and reproductive outcomes, which can occur without death",
        "They are lethal at every concentration, so no measurement is needed",
        "They affect only the individuals directly exposed and never their offspring",
        "They act only on plants and so are not measured in animals",
        "They are harmless and are regulated for other reasons"],
      ans=0,
      why="The framework describes chemicals that interfere with the endocrine system "
          "and lists birth defects, developmental disorders and gender imbalances, which "
          "are outcomes reached without killing the exposed animal."),

 dict(q="Which of the following best explains why gender imbalance is included among the "
        "effects the framework lists?",
      choices=[
        "It is an outcome the framework attributes to interference with the endocrine "
        "system in fish and other species",
        "It is a direct measure of how much chemical is in the water",
        "It is a physical change in the habitat rather than in the animals",
        "It is a consequence of low dissolved oxygen",
        "It is a result of increased sediment reducing light"],
      ans=0,
      why="The framework's own list is birth defects, developmental disorders and gender "
          "imbalances in fish and other species. It is an outcome in the animals rather "
          "than a measurement of the water or an effect of oxygen or sediment."),

 dict(q="A laboratory finds that a chemical produces developmental defects in fish "
        "embryos at concentrations found in a nearby river. What further evidence would "
        "best link the laboratory result to the river population?",
      choices=[
        "A survey of the river population for the same defects, compared with a "
        "population from an unexposed river",
        "A repeat of the laboratory experiment with the same embryos",
        "A record of how long the laboratory experiment took",
        "A measurement of the river's width and depth",
        "A list of other chemicals manufactured in the region"],
      ans=0,
      why="Linking the laboratory finding to the wild population requires looking for the "
          "same effects in that population against a comparable unexposed one. Repeating "
          "the laboratory work, recording its duration, or measuring the channel does "
          "not test the population."),

 dict(q="Which of the following is described by the framework as a species-level "
        "consequence rather than an effect on one individual?",
      choices=[
        "A gender imbalance among the animals in an exposed population",
        "A single fish with a visible spinal deformity",
        "One embryo failing to develop normally",
        "One adult animal showing reduced growth",
        "A single hatchling with a missing limb"],
      ans=0,
      why="A gender imbalance is a property of a population's composition, while a "
          "deformity or a failure to develop is observed in an individual. The framework "
          "lists all of these outcomes, and only the imbalance is inherently about the "
          "group."),

 dict(q="Why is a reference site important in a field study of endocrine disruption?",
      choices=[
        "It shows what rate of defects and what sex ratio occur without the exposure, so "
        "the exposed site can be compared with it",
        "It doubles the number of animals available for the exposed site",
        "It removes the need to measure anything at the exposed site",
        "It guarantees that the exposed site will show an effect",
        "It measures the chemical rather than the animals"],
      ans=0,
      why="The framework's effects are rates and ratios that also occur, at some level, "
          "without exposure, so a comparison site is what makes an elevated rate "
          "meaningful. It does not supply animals to the exposed site or replace its "
          "measurements."),

 dict(q="An argument holds that because a chemical did not kill any fish in a test, it "
        "cannot be an endocrine disruptor. Which response is best supported?",
      choices=[
        "The framework's effects include birth defects, developmental disorders and "
        "gender imbalances, none of which requires the death of the exposed animal",
        "The framework defines an endocrine disruptor by the number of deaths it causes",
        "The framework says endocrine disruptors always kill within a short time",
        "The framework says a chemical must kill adults before it can affect embryos",
        "The framework treats survival as the only measure of harm"],
      ans=0,
      why="The framework defines endocrine disruptors by interference with the endocrine "
          "system and lists three developmental and reproductive effects, so survival is "
          "not the test of whether a chemical is one."),

 dict(q="Which additional measurement would most strengthen a claim that an effluent "
        "contains an endocrine disruptor affecting a fish population?",
      choices=[
        "The share of fish with mixed sexual characteristics at several distances "
        "downstream, compared with upstream",
        "The width of the river at the outfall",
        "The number of vehicles crossing the nearest bridge",
        "The temperature of the effluent as it leaves the pipe",
        "The number of fishing licenses sold in the county"],
      ans=0,
      why="Mixed characteristics are an instance of the gender imbalance the framework "
          "names, and a gradient with distance compared with upstream ties it to the "
          "outfall. Channel width, traffic, effluent temperature and license sales do "
          "not measure the effect."),

 dict(q="Which pairing of an observation with the framework's category of effect is "
        "correct?",
      choices=[
        "Hatchlings born with malformed limbs, birth defects",
        "Hatchlings born with malformed limbs, gender imbalance",
        "An unusually small share of males, birth defects",
        "Slower growth of adult plants, developmental disorders in animals",
        "Fewer insects in the water, gender imbalance"],
      ans=0,
      why="The framework lists birth defects, developmental disorders and gender "
          "imbalances, and malformed limbs at birth belong to the first of those. Each "
          "rejected pairing attaches an observation to the wrong category or to organisms "
          "the statement does not concern."),

 dict(q="Why does the framework place endocrine disruptors in a unit about pollution "
        "rather than in a unit about population growth?",
      choices=[
        "They are chemicals released into ecosystems whose interference with animals is "
        "the harm at issue",
        "They are a natural feature of every ecosystem",
        "They determine the carrying capacity of every habitat",
        "They are a measure of how many young a species produces in a good year",
        "They are physical rather than chemical agents"],
      ans=0,
      why="The framework defines them as chemicals that can interfere with the endocrine "
          "system of animals, which makes them pollutants acting on organisms. It "
          "attaches to them no role in setting carrying capacity or measuring "
          "reproduction in general."),

 dict(q="A team detects an endocrine-disrupting effect in one species in a wetland and "
        "asks whether other species are affected. Which framework statement most "
        "directly bears on that question?",
      choices=[
        "The effects are described for fish and other species, so more than one kind of "
        "animal can be affected",
        "The effects are described only for species raised in captivity",
        "The effects are described only for the species first tested",
        "The effects are described only for species that live on land",
        "The effects are described only for adult animals"],
      ans=0,
      why="The framework's wording, in fish and other species, is what makes the "
          "question worth asking, since it does not confine the effects to one kind of "
          "animal, one habitat or one life stage."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Chemicals that interfere with the endocrine system of animals can lead to birth "
        "defects, developmental disorders, and gender imbalances in fish and other "
        "species",
        "Chemicals that raise water temperature reduce the oxygen available to fish",
        "Chemicals that persist in the environment accumulate in fatty tissue and "
        "concentrate up the food chain",
        "Nutrient pollution causes algal blooms whose decay lowers dissolved oxygen",
        "Solid waste in water causes choking hazards and introduces toxic substances"],
      ans=0,
      why="The keyed summary states the framework's two sentences for this topic. The "
          "rejected summaries belong to thermal pollution, persistent organic pollutants "
          "and bioaccumulation, eutrophication, and litter, each of which is a different "
          "topic."),
]
