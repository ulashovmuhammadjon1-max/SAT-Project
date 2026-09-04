# AP ENVIRONMENTAL SCIENCE 8.15 Pathogens and Infectious Diseases
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding EIN-3. Learning objective EIN-3.D: explain human pathogens and their
# cycling through the environment. Suggested skill 2.B, explain relationships between
# different characteristics of environmental concepts, processes, or models represented
# visually, in theoretical and in applied contexts.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-3.D.1   Pathogens adapt to take advantage of new opportunities to infect and
#               spread through human populations.
#   EIN-3.D.2   Specific pathogens can occur in many environments regardless of the
#               appearance of sanitary conditions.
#   EIN-3.D.3   As equatorial-type climate zones spread north and south into what are
#               currently subtropical and temperate climate zones, pathogens, infectious
#               diseases, and any associated vectors are spreading into these areas where
#               the disease has not previously been known to occur.
#   EIN-3.D.4   Poverty-stricken, low-income areas often lack sanitary waste disposal and
#               have contaminated drinking water supplies, leading to havens and
#               opportunities for the spread of infectious diseases.
#   EIN-3.D.5   Plague is carried by organisms infected with the plague bacteria and is
#               transferred to humans via the bite of an infected organism or through
#               contact with contaminated fluids or tissues.
#   EIN-3.D.6   Tuberculosis is a bacterial infection that typically attacks the lungs,
#               spread by breathing in the bacteria from the bodily fluids of an infected
#               person.
#   EIN-3.D.7   Malaria is a parasitic disease caused by bites from infected mosquitoes,
#               most often found in sub-Saharan Africa.
#   EIN-3.D.8   West Nile virus is transmitted to humans via bites from infected
#               mosquitoes.
#   EIN-3.D.9   Severe acute respiratory syndrome (SARS) is a form of pneumonia,
#               transferred by inhaling or touching infected fluids.
#   EIN-3.D.10  Middle East Respiratory Syndrome (MERS) is a viral respiratory illness
#               that is transferred from animals to humans.
#   EIN-3.D.11  Zika is a virus caused by bites from infected mosquitoes and can be
#               transmitted through sexual contact.
#   EIN-3.D.12  Cholera is a bacterial disease that is contracted from infected water.
#
# ON SCOPE. Dysentery is keyed in 8.14 under EIN-3.C.2 and is NOT on this topic's list,
# so no key here attributes it to anything. Sewage treatment is keyed in 8.11. Nothing
# here restates either.
#
# ON THE FIGURES. Suggested skill 2.B concerns relationships represented visually and the
# bank carries no images, so every representation is a table and every keyed reading is
# recomputed in verify_e8_15.py from that table alone.
#
# NOT KEYED: no case count for a real outbreak, no incubation period, no treatment, no
# vaccine, and no cause for any disease the framework does not name a cause for. The
# framework states none of them.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.15", "Pathogens and Infectious Diseases", 8)

_T_SANITATION = dict(
    headers=["District", "Households with sanitary waste disposal (percent)",
             "Households whose drinking water is free of contamination (percent)",
             "Cholera cases per ten thousand people each year"],
    rows=[["District 1", "18", "22", "94"],
          ["District 2", "45", "51", "38"],
          ["District 3", "88", "91", "4.0"]])

_T_CLIMATE = dict(
    headers=["Climate band where cases were recorded",
             "Cases recorded in the earlier decade", "Cases recorded in the later decade"],
    rows=[["Equatorial band", "4200", "4600"],
          ["Subtropical band", "120", "1900"],
          ["Temperate band", "0", "430"]])

_T_APPEARANCE = dict(
    headers=["Site sampled", "Rating of how clean the site appears",
             "Percent of samples in which the pathogen was detected"],
    rows=[["Site 1", "looks clean and well kept", "41"],
          ["Site 2", "looks moderately kept", "46"],
          ["Site 3", "looks poorly kept", "52"]])

_T_MOSQUITO = dict(
    headers=["Area surveyed", "Infected mosquitoes caught per trap night",
             "New human cases of the mosquito borne disease each month"],
    rows=[["Area 1", "0.20", "3.0"],
          ["Area 2", "1.4", "19"],
          ["Area 3", "4.8", "71"],
          ["Area 4", "9.1", "142"]])

_T_INCOME = dict(
    headers=["Neighborhood", "Average household income (thousands of currency units)",
             "Households with sanitary waste disposal (percent)",
             "Infectious disease cases per thousand people each year"],
    rows=[["Neighborhood A", "4.0", "12", "88"],
          ["Neighborhood B", "16", "49", "41"],
          ["Neighborhood C", "60", "94", "9.0"]])

_T_TB = dict(
    headers=["Housing setting studied",
             "Hours per day people share unventilated indoor air",
             "Tuberculosis cases per thousand residents each year"],
    rows=[["Setting 1", "2.0", "1.0"],
          ["Setting 2", "6.0", "6.0"],
          ["Setting 3", "12", "17"],
          ["Setting 4", "18", "29"]])

QUESTIONS = [

 dict(q="What does the framework say pathogens do in relation to new opportunities?",
      choices=[
        "They adapt to take advantage of new opportunities to infect and spread through "
        "human populations",
        "They remain unchanged and cannot exploit any new opportunity",
        "They disappear whenever human populations change",
        "They can only spread in places where they first appeared",
        "They become harmless as soon as they encounter a new population"],
      ans=0,
      why="EIN-3.D.1 states that pathogens adapt to take advantage of new opportunities to "
          "infect and spread through human populations. Each rejected option denies that "
          "adaptation or the spread it allows."),

 dict(q="What does the framework say about where specific pathogens can occur?",
      choices=[
        "They can occur in many environments regardless of how sanitary the conditions "
        "appear",
        "They occur only in environments that appear visibly dirty",
        "They occur only in environments that appear visibly clean",
        "They occur only in tropical environments",
        "They occur only where a laboratory has released them"],
      ans=0,
      why="EIN-3.D.2 states that specific pathogens can occur in many environments "
          "regardless of the appearance of sanitary conditions, so appearance is not a "
          "reliable guide to whether a pathogen is present."),

 dict(q="What does the framework say happens as equatorial-type climate zones spread north "
        "and south?",
      choices=[
        "Pathogens, infectious diseases and any associated vectors spread into subtropical "
        "and temperate areas where the disease has not previously been known to occur",
        "Pathogens retreat toward the equator and disappear from higher latitudes",
        "Pathogens remain confined to the zones where they are found today",
        "Infectious diseases become impossible outside the tropics",
        "Vectors die out wherever the climate changes"],
      ans=0,
      why="EIN-3.D.3 states that as equatorial-type climate zones spread north and south "
          "into what are currently subtropical and temperate climate zones, pathogens, "
          "infectious diseases and any associated vectors are spreading into these areas "
          "where the disease has not previously been known to occur."),

 dict(q="Three districts of one city were compared.",
      table=_T_SANITATION,
      choices=[
        "The district with the least sanitary waste disposal and the most contaminated "
        "drinking water carries by far the most disease",
        "The district with the best sanitary waste disposal carries the most disease",
        "All three districts carry the same amount of disease",
        "Sanitation and disease are unrelated across these districts",
        "The district with the most contaminated water carries the least disease"],
      ans=0,
      why="Ranking the districts by either sanitation column gives the reverse of the order "
          "by case rate. EIN-3.D.4 states that areas lacking sanitary waste disposal and "
          "having contaminated drinking water become havens for the spread of infectious "
          "diseases, and EIN-3.D.12 makes cholera a disease contracted from infected "
          "water."),

 dict(q="What does the framework say about poverty-stricken, low-income areas?",
      choices=[
        "They often lack sanitary waste disposal and have contaminated drinking water, "
        "which creates havens and opportunities for infectious disease to spread",
        "They usually have the most reliable sanitary waste disposal of any area",
        "They are protected from infectious disease by their small populations",
        "They have contaminated water but no effect on the spread of disease",
        "They are the only places where any pathogen can survive"],
      ans=0,
      why="EIN-3.D.4 states that poverty-stricken, low-income areas often lack sanitary "
          "waste disposal and have contaminated drinking water supplies, leading to havens "
          "and opportunities for the spread of infectious diseases."),

 dict(q="How does the framework describe the transmission of plague to humans?",
      choices=[
        "By the bite of an infected organism, or through contact with contaminated fluids "
        "or tissues",
        "By breathing in bacteria from the bodily fluids of an infected person",
        "By drinking water that has been contaminated",
        "By bites from infected mosquitoes only",
        "By transfer from animals to humans through the air alone"],
      ans=0,
      why="EIN-3.D.5 states that plague is carried by organisms infected with the plague "
          "bacteria and is transferred to humans via the bite of an infected organism or "
          "through contact with contaminated fluids or tissues. The rejected routes belong "
          "to tuberculosis, cholera, the mosquito borne diseases and MERS."),

 dict(q="How does the framework describe tuberculosis?",
      choices=[
        "A bacterial infection that typically attacks the lungs, spread by breathing in "
        "the bacteria from the bodily fluids of an infected person",
        "A parasitic disease spread by the bites of infected mosquitoes",
        "A viral illness transferred from animals to humans",
        "A bacterial disease contracted from infected water",
        "A disease carried by organisms infected with the plague bacteria"],
      ans=0,
      why="EIN-3.D.6 states that tuberculosis is a bacterial infection that typically "
          "attacks the lungs and is spread by breathing in the bacteria from the bodily "
          "fluids of an infected person. The rejected descriptions belong to malaria, "
          "MERS, cholera and plague."),

 dict(q="Cases of one vector borne disease were recorded in three climate bands in two "
        "decades.",
      table=_T_CLIMATE,
      choices=[
        "The band that recorded no cases in the earlier decade recorded hundreds in the "
        "later one, and the middle band rose many times over",
        "Every band recorded fewer cases in the later decade than in the earlier one",
        "Only the equatorial band recorded any cases in either decade",
        "The temperate band recorded more cases in the earlier decade than in the later "
        "one",
        "The three bands recorded identical numbers in both decades"],
      ans=0,
      why="The temperate row moves from zero to hundreds and the subtropical row rises by "
          "more than tenfold, while the equatorial row changes little. EIN-3.D.3 states "
          "that pathogens, infectious diseases and associated vectors are spreading into "
          "subtropical and temperate areas where the disease has not previously been known "
          "to occur."),

 dict(q="How does the framework describe malaria?",
      choices=[
        "A parasitic disease caused by bites from infected mosquitoes, most often found in "
        "sub-Saharan Africa",
        "A bacterial disease contracted from infected water",
        "A viral respiratory illness transferred from animals to humans",
        "A bacterial infection of the lungs spread by breathing infected droplets",
        "A form of pneumonia transferred by inhaling or touching infected fluids"],
      ans=0,
      why="EIN-3.D.7 states that malaria is a parasitic disease caused by bites from "
          "infected mosquitoes and is most often found in sub-Saharan Africa. The rejected "
          "descriptions are cholera, MERS, tuberculosis and SARS."),

 dict(q="How is West Nile virus transmitted to humans, according to the framework?",
      choices=[
        "By bites from infected mosquitoes",
        "By drinking water that carries the virus",
        "By breathing air in a crowded indoor space",
        "By contact with the tissues of an infected rodent",
        "By eating food prepared by an infected person"],
      ans=0,
      why="EIN-3.D.8 states that West Nile virus is transmitted to humans via bites from "
          "infected mosquitoes. Water, air, animal tissues and food are the routes the "
          "framework gives for other diseases in this list."),

 dict(q="How does the framework describe severe acute respiratory syndrome?",
      choices=[
        "A form of pneumonia transferred by inhaling or touching infected fluids",
        "A parasitic disease transmitted by mosquito bites",
        "A bacterial disease contracted from infected water",
        "A disease carried by organisms infected with the plague bacteria",
        "A virus that can also be transmitted through sexual contact"],
      ans=0,
      why="EIN-3.D.9 states that severe acute respiratory syndrome is a form of pneumonia "
          "transferred by inhaling or touching infected fluids. The rejected descriptions "
          "belong to malaria, cholera, plague and Zika."),

 dict(q="Samples were taken at three sites that differ in how clean they look.",
      table=_T_APPEARANCE,
      choices=[
        "The pathogen was detected at broadly similar rates at all three sites, so how "
        "clean a site looks is a poor guide to whether the pathogen is present",
        "The pathogen was detected only at the site that looks poorly kept",
        "The pathogen was absent from the site that looks clean and well kept",
        "The pathogen was detected far more often at the site that looks clean",
        "The pathogen was detected in every sample at every site"],
      ans=0,
      why="The three detection percentages sit within a narrow band of one another even "
          "though the appearance ratings differ, and none is zero or complete. EIN-3.D.2 "
          "states that specific pathogens can occur in many environments regardless of the "
          "appearance of sanitary conditions."),

 dict(q="How does the framework describe Middle East Respiratory Syndrome?",
      choices=[
        "A viral respiratory illness that is transferred from animals to humans",
        "A bacterial infection of the lungs spread between people by breathing",
        "A parasitic disease carried by mosquitoes",
        "A bacterial disease contracted from infected water",
        "A disease transferred by the bite of an infected rodent"],
      ans=0,
      why="EIN-3.D.10 states that Middle East Respiratory Syndrome is a viral respiratory "
          "illness that is transferred from animals to humans. Tuberculosis, malaria, "
          "cholera and plague have different descriptions in the framework."),

 dict(q="What two routes of transmission does the framework give for Zika?",
      choices=[
        "Bites from infected mosquitoes, and transmission through sexual contact",
        "Drinking infected water, and contact with contaminated tissues",
        "Breathing infected droplets, and eating contaminated food",
        "Transfer from animals to humans, and bites from infected rodents",
        "Bites from infected mosquitoes only, with no second route"],
      ans=0,
      why="EIN-3.D.11 states that Zika is a virus caused by bites from infected mosquitoes "
          "and that it can be transmitted through sexual contact, so the framework gives "
          "two routes for this disease."),

 dict(q="How does the framework describe cholera?",
      choices=[
        "A bacterial disease that is contracted from infected water",
        "A viral illness transferred from animals to humans",
        "A parasitic disease carried by infected mosquitoes",
        "A bacterial infection of the lungs spread by breathing",
        "A form of pneumonia spread by touching infected fluids"],
      ans=0,
      why="EIN-3.D.12 states that cholera is a bacterial disease that is contracted from "
          "infected water. The rejected descriptions belong to MERS, malaria, tuberculosis "
          "and SARS."),

 dict(q="Trapping results and case counts were compared across four areas.",
      table=_T_MOSQUITO,
      choices=[
        "The areas that caught the most infected mosquitoes recorded the most new human "
        "cases",
        "The areas that caught the most infected mosquitoes recorded the fewest new cases",
        "All four areas recorded the same number of new cases",
        "The area catching the fewest infected mosquitoes recorded the most cases",
        "Mosquito catches and human cases are unrelated across these areas"],
      ans=0,
      why="Ranking the areas by infected mosquitoes caught gives the same order as ranking "
          "them by new human cases. The framework attributes malaria, West Nile virus and "
          "Zika to bites from infected mosquitoes in EIN-3.D.7, EIN-3.D.8 and EIN-3.D.11."),

 dict(q="Which set of diseases does the framework attribute to bites from infected "
        "mosquitoes?",
      choices=[
        "Malaria, West Nile virus and Zika",
        "Cholera, tuberculosis and plague",
        "Tuberculosis, SARS and MERS",
        "Cholera, malaria and SARS",
        "Plague, MERS and Zika"],
      ans=0,
      why="EIN-3.D.7 gives malaria, EIN-3.D.8 gives West Nile virus and EIN-3.D.11 gives "
          "Zika as caused by bites from infected mosquitoes. Cholera is waterborne, "
          "tuberculosis and SARS are spread from infected people, plague comes from an "
          "infected organism, and MERS comes from animals."),

 dict(q="Which disease does the framework describe as transferred from animals to humans?",
      choices=[
        "Middle East Respiratory Syndrome",
        "Cholera",
        "Tuberculosis",
        "Severe acute respiratory syndrome",
        "Zika"],
      ans=0,
      why="EIN-3.D.10 states that Middle East Respiratory Syndrome is a viral respiratory "
          "illness that is transferred from animals to humans. Cholera comes from infected "
          "water, tuberculosis and SARS from an infected person, and Zika from mosquitoes "
          "or sexual contact."),

 dict(q="Which mosquito borne disease does the framework also give a route of transmission "
        "that does not involve a vector?",
      choices=[
        "Zika, which can also be transmitted through sexual contact",
        "Malaria, which can also be contracted from infected water",
        "West Nile virus, which can also be transferred from animals to humans",
        "Malaria, which can also be spread by breathing infected droplets",
        "West Nile virus, which can also be spread by contact with contaminated tissues"],
      ans=0,
      why="EIN-3.D.11 gives Zika two routes, bites from infected mosquitoes and sexual "
          "contact. EIN-3.D.7 and EIN-3.D.8 give malaria and West Nile virus only the "
          "mosquito route."),

 dict(q="Three neighborhoods were compared on income, sanitation and disease.",
      table=_T_INCOME,
      choices=[
        "The neighborhood with the lowest income has the least sanitary waste disposal and "
        "the most infectious disease",
        "The neighborhood with the highest income has the most infectious disease",
        "All three neighborhoods carry the same amount of infectious disease",
        "Income and sanitary waste disposal run in opposite directions here",
        "The neighborhood with the least sanitary waste disposal has the least disease"],
      ans=0,
      why="Ranking the neighborhoods by income gives the same order as ranking them by "
          "sanitation coverage and the reverse of the order by disease. EIN-3.D.4 states "
          "that poverty-stricken, low-income areas often lack sanitary waste disposal, "
          "creating havens for the spread of infectious diseases."),

 dict(q="A community's only water source is contaminated and a bacterial illness spreads "
        "through it. Which disease on the framework's list is contracted this way?",
      choices=[
        "Cholera",
        "Malaria",
        "Tuberculosis",
        "West Nile virus",
        "Middle East Respiratory Syndrome"],
      ans=0,
      why="EIN-3.D.12 states that cholera is a bacterial disease contracted from infected "
          "water. Malaria and West Nile virus come from mosquitoes, tuberculosis from "
          "breathing infected droplets, and MERS from animals."),

 dict(q="A person handles the carcass of an animal that died of a bacterial infection and "
        "later becomes ill. Which framework statement covers that route?",
      choices=[
        "Plague can be transferred through contact with contaminated fluids or tissues",
        "Cholera is contracted from infected water",
        "Tuberculosis is spread by breathing in bacteria from an infected person",
        "West Nile virus is transmitted by bites from infected mosquitoes",
        "SARS is transferred by inhaling or touching infected fluids from a person"],
      ans=0,
      why="EIN-3.D.5 states that plague is transferred to humans via the bite of an "
          "infected organism or through contact with contaminated fluids or tissues, which "
          "covers handling an infected animal. The rejected statements name water, human "
          "droplets and mosquitoes."),

 dict(q="A health officer argues that a facility needs no testing because it looks clean. "
        "Which framework statement most directly challenges that reasoning?",
      choices=[
        "Specific pathogens can occur in many environments regardless of the appearance of "
        "sanitary conditions",
        "Pathogens adapt to take advantage of new opportunities to spread",
        "Poverty-stricken areas often lack sanitary waste disposal",
        "Equatorial climate zones are spreading toward the poles",
        "Cholera is a bacterial disease contracted from infected water"],
      ans=0,
      why="EIN-3.D.2 states that specific pathogens can occur in many environments "
          "regardless of the appearance of sanitary conditions, which is exactly the "
          "inference the officer is making from appearance."),

 dict(q="Housing settings differing in shared indoor air were compared.",
      table=_T_TB,
      choices=[
        "The more hours people share unventilated indoor air, the higher the tuberculosis "
        "rate in that setting",
        "The more hours people share unventilated indoor air, the lower the tuberculosis "
        "rate",
        "All four settings show the same tuberculosis rate",
        "The setting with the fewest shared hours shows the highest rate",
        "Shared indoor air and tuberculosis are unrelated across these settings"],
      ans=0,
      why="Ranking the settings by hours of shared unventilated air gives the same order "
          "as ranking them by case rate. EIN-3.D.6 states that tuberculosis is spread by "
          "breathing in the bacteria from the bodily fluids of an infected person."),

 dict(q="Which set of diseases does the framework describe in terms of the lungs or the "
        "respiratory system?",
      choices=[
        "Tuberculosis, severe acute respiratory syndrome and Middle East Respiratory "
        "Syndrome",
        "Cholera, malaria and Zika",
        "Plague, cholera and West Nile virus",
        "Malaria, Zika and West Nile virus",
        "Cholera, tuberculosis and Zika"],
      ans=0,
      why="EIN-3.D.6 calls tuberculosis a bacterial infection that typically attacks the "
          "lungs, EIN-3.D.9 calls SARS a form of pneumonia, and EIN-3.D.10 calls MERS a "
          "viral respiratory illness. The rejected sets mix in waterborne and mosquito "
          "borne diseases."),

 dict(q="A temperate region records its first locally acquired cases of a mosquito borne "
        "disease, along with the first established population of the mosquito that carries "
        "it. Which framework statement covers that?",
      choices=[
        "Pathogens, infectious diseases and their vectors are spreading into areas where "
        "the disease has not previously been known to occur as equatorial climate zones "
        "expand",
        "Specific pathogens occur regardless of the appearance of sanitary conditions",
        "Low-income areas lack sanitary waste disposal and contaminated water spreads "
        "disease",
        "Cholera is a bacterial disease contracted from infected water",
        "Plague is transferred by the bite of an infected organism"],
      ans=0,
      why="EIN-3.D.3 states that as equatorial-type climate zones spread north and south, "
          "pathogens, infectious diseases and any associated vectors are spreading into "
          "these areas where the disease has not previously been known to occur, which is "
          "the arrival of both disease and vector described in the stem."),

 dict(q="Why does the framework describe low-income areas as havens for the spread of "
        "infectious diseases?",
      choices=[
        "They often lack sanitary waste disposal and have contaminated drinking water, "
        "which gives pathogens opportunities to spread",
        "They contain more mosquitoes than any other kind of area",
        "Their residents are unable to recover from any infection",
        "They are the only places where bacteria can survive",
        "They receive more rainfall than higher income areas"],
      ans=0,
      why="EIN-3.D.4 attributes the havens and opportunities to the lack of sanitary waste "
          "disposal and to contaminated drinking water supplies rather than to any other "
          "feature of those areas."),

 dict(q="Which pairing of a disease with the framework's own route of transmission is "
        "correct?",
      choices=[
        "Tuberculosis, paired with breathing in bacteria from the bodily fluids of an "
        "infected person",
        "Cholera, paired with bites from infected mosquitoes",
        "Malaria, paired with contracting the disease from infected water",
        "Zika, paired with transfer from animals to humans",
        "Plague, paired with inhaling infected fluids from another person"],
      ans=0,
      why="EIN-3.D.6 gives tuberculosis its airborne route from an infected person, "
          "EIN-3.D.12 gives cholera water, EIN-3.D.7 gives malaria mosquitoes, EIN-3.D.11 "
          "gives Zika mosquitoes and sexual contact, and EIN-3.D.5 gives plague an "
          "infected organism. Each rejected pairing crosses two of those."),

 dict(q="Which of the following does the framework NOT state about pathogens in this "
        "topic?",
      choices=[
        "That a site which appears sanitary is reliably free of pathogens",
        "That pathogens adapt to take advantage of new opportunities to spread",
        "That vectors are spreading into areas where a disease was not previously known",
        "That contaminated drinking water supplies help infectious diseases spread",
        "That a pathogen can be transferred to humans from animals"],
      ans=0,
      why="EIN-3.D.2 states the opposite, that specific pathogens can occur in many "
          "environments regardless of the appearance of sanitary conditions. The four "
          "rejected options restate EIN-3.D.1, EIN-3.D.3, EIN-3.D.4 and EIN-3.D.10."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Pathogens adapt to new opportunities and occur regardless of how sanitary a place "
        "looks, they and their vectors are spreading as equatorial climate zones expand, "
        "poor sanitation and contaminated water give them havens, and the framework names "
        "specific diseases with specific routes through mosquitoes, water, air, animals "
        "and contact",
        "Pathogens occur only where conditions look unsanitary and never spread beyond "
        "their present range",
        "Every disease on the framework's list is spread by mosquitoes",
        "Sanitation and drinking water have no bearing on the spread of infectious disease",
        "Pathogens cannot be transferred between animals and humans in any case"],
      ans=0,
      why="Each clause of the keyed summary is one of EIN-3.D.1 through EIN-3.D.12. Every "
          "rejected summary denies the appearance statement, collapses every route into "
          "one, denies the role of sanitation, or denies animal to human transfer."),
]
