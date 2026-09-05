# AP WORLD HISTORY: MODERN 4.3 Columbian Exchange
# CED effective Fall 2024/2026, Unit 4 Transoceanic Interconnections, c. 1450 to
# c. 1750. Title copied verbatim from WORLD_HISTORY_topics.json.
#
# Unit 4: Learning Objective D -- explain the causes of the Columbian Exchange and
# its effects on the Eastern and Western Hemispheres.
# Suggested skill 3.B, identify the evidence used in a source to support an
# argument. Reasoning process: causation.
# Thematic focus: Humans and the Environment.
#
# Historical developments this module keys to, in the framework's own words:
#   KC-4.1.V     The new connections between the Eastern and Western Hemispheres
#                resulted in the exchange of new plants, animals, and diseases,
#                known as the Columbian Exchange.
#   KC-4.1.V.A   European colonization of the Americas led to the unintentional
#                transfer of disease vectors, including mosquitoes and rats, and
#                the spread of diseases that were endemic in the Eastern
#                Hemisphere, including smallpox, measles, and malaria. Some of
#                these diseases substantially reduced the indigenous populations,
#                with catastrophic effects in many areas.
#   KC-4.1.V.B   American foods became staple crops in various parts of Europe,
#                Asia, and Africa. Cash crops were grown primarily on plantations
#                with coerced labor and were exported mostly to Europe and the
#                Middle East.
#   KC-4.1.V.C   Afro-Eurasian fruit trees, grains, sugar, and domesticated
#                animals were brought by Europeans to the Americas, while other
#                foods were brought by African enslaved persons.
#   KC-4.1.V.D   Populations in Afro-Eurasia benefitted nutritionally from the
#                increased diversity of American food crops.
#
# Illustrative examples printed beside the topic, under two headings:
#   Domesticated animals: horses; pigs; cattle.
#   Foods brought by African enslaved persons: okra; rice.
#
# WHAT THIS MODULE DELIBERATELY DOES NOT ASSERT. The framework names no American
# crop at all -- not maize, not the potato -- so no item here names one either;
# where a stimulus needs the category it says "American food crops", which is the
# framework's own phrase. It gives no figure for the population loss, saying only
# that some of these diseases substantially reduced the indigenous populations
# with catastrophic effects in many areas, so nothing here keys a rate or a
# proportion. It does NOT say that any disease travelled from the Western
# Hemisphere to the Eastern; the direction it states runs the other way, and a
# question that keyed the reverse would be teaching the framework's silence as
# fact. And it calls the transfer of disease vectors UNINTENTIONAL, which is a
# distinction two items turn on.
#
# Dates are written "1450 to 1750". Five choices A-E per HISTORY_BRIEF.md. Every
# stimulus is hypothetical or unattributed; no quotation is put in a real
# person's mouth.
TOPIC = ("4.3", "Columbian Exchange", 4)

_T_CARGOES = dict(
    headers=["Cargo in a hypothetical shipping list", "Direction recorded for it"],
    rows=[["Fruit trees and grains", "Carried from Afro-Eurasia to the Americas"],
          ["Cattle, pigs, and horses", "Carried from Afro-Eurasia to the Americas"],
          ["Okra and rice", "Carried by African enslaved persons to the Americas"],
          ["American food crops", "Carried from the Americas to Afro-Eurasia"]])

_T_POPULATION = dict(
    headers=["Period of a hypothetical count",
             "Recorded population of one region (index, first period equals 100)"],
    rows=[["First period", "100"],
          ["Second period", "71"],
          ["Third period", "42"],
          ["Fourth period", "30"]])

_T_STAPLES = dict(
    headers=["Region in a hypothetical survey",
             "American food crops grown there as staples"],
    rows=[["A region of Europe", "3"],
          ["A region of Asia", "4"],
          ["A region of Africa", "2"],
          ["A region of the Americas", "6"]])

QUESTIONS = [
 dict(
  q=("The framework gives one name to the whole exchange this topic describes. What does it "
     "say the new connections between the Eastern and Western Hemispheres resulted in?"),
  choices=[
   "The exchange of new plants, animals, and diseases",
   "The exchange of coined money and precious stones alone",
   "The exchange of legal codes between empires",
   "The exchange of ambassadors between rulers",
   "The exchange of prisoners taken in war"],
  ans=0,
  why=("KC-4.1.V states that the new connections between the Eastern and Western Hemispheres "
       "resulted in the exchange of new plants, animals, and diseases, known as the Columbian "
       "Exchange. Coinage, legal codes, ambassadors and prisoners are named in no part of that "
       "sentence.")),
 dict(
  q=("According to the framework, what caused the exchange of new plants, animals, and diseases "
     "in this period?"),
  choices=[
   "The new connections between the Eastern and Western Hemispheres",
   "A change in the climate of the Atlantic",
   "The exhaustion of soils across Afro-Eurasia",
   "The collapse of trade within the Indian Ocean",
   "A decision taken jointly by the rulers of both hemispheres"],
  ans=0,
  why=("KC-4.1.V makes the new connections between the Eastern and Western Hemispheres the cause "
       "and the exchange of new plants, animals, and diseases the result, which is what Unit 4: "
       "Learning Objective D asks students to explain. The framework offers none of the other "
       "causes listed.")),
 dict(
  q=("The framework says European colonization of the Americas led to the transfer of disease "
     "vectors. Which vectors does it name?"),
  choices=[
   "Mosquitoes and rats",
   "Locusts and termites",
   "Horses and cattle",
   "Fruit flies and beetles",
   "Sheep and goats"],
  ans=0,
  why=("KC-4.1.V.A names mosquitoes and rats as the disease vectors unintentionally transferred "
       "by European colonization of the Americas. Horses and cattle appear in the illustrative "
       "examples as domesticated animals brought deliberately, which is a different transfer in "
       "the same statement's neighbourhood.")),
 dict(
  q=("Which diseases does the framework name as having spread in the course of European "
     "colonization of the Americas?"),
  choices=[
   "Smallpox, measles, and malaria",
   "Cholera, typhus, and tuberculosis",
   "Plague, leprosy, and rabies",
   "Influenza, scurvy, and dysentery",
   "Yellow fever, polio, and tetanus"],
  ans=0,
  why=("KC-4.1.V.A names smallpox, measles, and malaria among the diseases that were endemic in "
       "the Eastern Hemisphere and spread with European colonization. The framework names no "
       "other disease anywhere in this topic, so the remaining lists cannot be traced to it.")),
 dict(
  q=("In which hemisphere does the framework say the diseases that spread with European "
     "colonization of the Americas had been endemic?"),
  choices=[
   "The Eastern Hemisphere",
   "The Western Hemisphere",
   "Both hemispheres equally",
   "Neither hemisphere, since the framework says the diseases were new to both",
   "The framework does not say where any disease was endemic"],
  ans=0,
  why=("KC-4.1.V.A describes the spread of diseases that were endemic in the Eastern Hemisphere, "
       "including smallpox, measles, and malaria. Reversing that to the Western Hemisphere, or "
       "denying that the framework locates the diseases at all, misreports the sentence.")),
 dict(
  q=("What effect does the framework attribute to some of the diseases that spread with European "
     "colonization?"),
  choices=[
   "They substantially reduced the indigenous populations, with catastrophic effects in many areas",
   "They left population levels in the Americas unchanged",
   "They reduced European populations while sparing indigenous ones",
   "They spread widely but caused no recorded deaths",
   "They were confined to a single settlement"],
  ans=0,
  why=("KC-4.1.V.A says some of these diseases substantially reduced the indigenous populations, "
       "with catastrophic effects in many areas. Each rejected option denies either the "
       "reduction or the population it fell upon, which the framework states in the same "
       "sentence.")),
 dict(
  q=("The framework says American foods became staple crops in various parts of which regions?"),
  choices=[
   "Europe, Asia, and Africa",
   "Australia and the Pacific islands",
   "The Caribbean and the Andes alone",
   "Northern Europe alone",
   "Nowhere outside the Americas"],
  ans=0,
  why=("KC-4.1.V.B says American foods became staple crops in various parts of Europe, Asia, and "
       "Africa. Confining them to the Americas, or moving them to regions the sentence does not "
       "name, is a claim the framework does not make.")),
 dict(
  q=("How does the framework say cash crops were grown in this period?"),
  choices=[
   "Primarily on plantations with coerced labor",
   "Primarily on small holdings farmed by their owners",
   "Primarily in gardens attached to monasteries",
   "Primarily by wage labor hired for the season",
   "Primarily by herders moving between pastures"],
  ans=0,
  why=("KC-4.1.V.B states that cash crops were grown primarily on plantations with coerced "
       "labor. Owner-farmed holdings, monastic gardens, seasonal wage labor and herding are "
       "named nowhere in the sentence, and KC-4.2.II.C independently ties the plantation economy "
       "to a rising demand for enslaved labor.")),
 dict(
  q=("Where does the framework say the cash crops of this period were mostly exported?"),
  choices=[
   "To Europe and the Middle East",
   "To East Asia and the Pacific",
   "To the interior of Africa",
   "To the Andes and Mesoamerica",
   "Nowhere, since they were consumed where they were grown"],
  ans=0,
  why=("KC-4.1.V.B says cash crops were exported mostly to Europe and the Middle East. The "
       "remaining destinations appear in no part of that statement, and consumption at the point "
       "of growth is the opposite of what the word exported asserts.")),
 dict(
  q=("The framework lists what Europeans brought to the Americas. Which of the following is that "
     "list?"),
  choices=[
   "Fruit trees, grains, sugar, and domesticated animals",
   "Tools, ship designs, and charts of the winds",
   "Gunpowder, cannons, and armed trade",
   "Tribute collection, tax farming, and new tax-collection systems",
   "Mercantilist policies and joint-stock companies"],
  ans=0,
  why=("KC-4.1.V.C says Afro-Eurasian fruit trees, grains, sugar, and domesticated animals were "
       "brought by Europeans to the Americas. The rejected lists are KC-4.1.II.A, KC-4.3.II, "
       "KC-4.3.I.D and KC-4.1.IV.C, which concern technology, expansion, revenue and commercial "
       "policy rather than the exchange of living things.")),
 dict(
  q=("The framework distinguishes what Europeans carried to the Americas from what another group "
     "carried. Which group does it name, and what does it say they brought?"),
  choices=[
   "African enslaved persons, who brought other foods",
   "African enslaved persons, who brought domesticated animals",
   "Asian merchants, who brought fruit trees",
   "Indigenous American traders, who brought grains",
   "European missionaries, who brought sugar"],
  ans=0,
  why=("KC-4.1.V.C says Afro-Eurasian fruit trees, grains, sugar, and domesticated animals were "
       "brought by Europeans to the Americas, while other foods were brought by African enslaved "
       "persons, and the illustrative examples print okra and rice under that heading. The "
       "domesticated animals belong to the European half of the same sentence.")),
 dict(
  q=("Which populations does the framework say benefited nutritionally from the increased "
     "diversity of American food crops?"),
  choices=[
   "Populations in Afro-Eurasia",
   "Populations in the Americas alone",
   "Populations in the Caribbean alone",
   "No population, since the framework records no nutritional effect",
   "Only the populations that grew the crops for export"],
  ans=0,
  why=("KC-4.1.V.D states that populations in Afro-Eurasia benefitted nutritionally from the "
       "increased diversity of American food crops. The framework records the benefit for that "
       "side of the exchange and for no other, so both the denials and the narrower readings go "
       "beyond it.")),
 dict(
  q=("A student is setting out which way each part of the exchange moved. Which pairing follows "
     "the framework?"),
  choices=[
   "American foods became staples in Europe, Asia, and Africa, while Afro-Eurasian animals were brought to the Americas",
   "Afro-Eurasian foods became staples in the Americas, while American animals were brought to Europe, Asia, and Africa",
   "American animals were brought to Afro-Eurasia, while Afro-Eurasian foods stayed where they were",
   "Both foods and animals moved only from the Americas outward",
   "Both foods and animals moved only into the Americas"],
  ans=0,
  why=("KC-4.1.V.B has American foods becoming staple crops in various parts of Europe, Asia, and "
       "Africa, and KC-4.1.V.C has Afro-Eurasian fruit trees, grains, sugar, and domesticated "
       "animals brought by Europeans to the Americas. The rejected pairings reverse one or both "
       "of those directions, which is the easiest error in this topic to make and to miss.")),
 dict(
  q=("Which statement about disease in this period would a reader of the framework recognise as "
     "an error, even though every term in it appears in the topic?"),
  choices=[
   "The diseases that spread were endemic in the Western Hemisphere and were carried to the Eastern",
   "The diseases that spread were endemic in the Eastern Hemisphere and included smallpox and measles",
   "European colonization of the Americas transferred disease vectors unintentionally",
   "Mosquitoes and rats were among the vectors transferred",
   "Some of the diseases substantially reduced indigenous populations"],
  ans=0,
  why=("KC-4.1.V.A locates the diseases as endemic in the Eastern Hemisphere and describes their "
       "spread with European colonization of the Americas, so reversing the hemispheres is the "
       "error. The other four statements are that sentence almost verbatim, which is what makes "
       "the mistaken one hard to see.")),
 dict(
  q=("Which animals are printed among the framework's illustrative examples of the domesticated "
     "animals brought to the Americas?"),
  choices=[
   "Horses, pigs, and cattle",
   "Camels, yaks, and reindeer",
   "Llamas, alpacas, and guinea pigs",
   "Elephants, buffalo, and oxen",
   "Chickens, geese, and ducks"],
  ans=0,
  why=("The illustrative examples beside Unit 4: Learning Objective D print horses, pigs and "
       "cattle under the heading of domesticated animals, which are the animals KC-4.1.V.C says "
       "Europeans brought to the Americas. The framework names no other animal in this topic.")),
 dict(
  q=("Which foods are printed among the framework's illustrative examples of the foods brought by "
     "African enslaved persons?"),
  choices=[
   "Okra and rice",
   "Sugar and wheat",
   "Grapes and olives",
   "Apples and pears",
   "Barley and rye"],
  ans=0,
  why=("The illustrative examples for this topic print okra and rice under the heading of foods "
       "brought by African enslaved persons, which is the second half of KC-4.1.V.C. Sugar and "
       "grains belong to the first half of the same sentence, where they are brought by "
       "Europeans.")),
 dict(
  q=("A hypothetical account written a generation after the founding of a colony reports that the "
     "settlements of the surrounding district hold far fewer people than the oldest residents "
     "remember, and that sickness rather than warfare emptied them.\n\n"
     "Which statement of the framework does the account most directly illustrate?"),
  choices=[
   "That some of the diseases that spread substantially reduced the indigenous populations",
   "That American foods became staple crops in Europe, Asia, and Africa",
   "That cash crops were exported mostly to Europe and the Middle East",
   "That populations in Afro-Eurasia benefited nutritionally from American crops",
   "That Europeans brought fruit trees and grains to the Americas"],
  ans=0,
  why=("KC-4.1.V.A says some of these diseases substantially reduced the indigenous populations, "
       "with catastrophic effects in many areas, and a district emptied by sickness rather than "
       "war is that effect. The rejected options are KC-4.1.V.B, KC-4.1.V.D and KC-4.1.V.C, none "
       "of which concerns mortality.")),
 dict(
  q=("A hypothetical estate record kept in the Americas lists the livestock on the property and "
     "the orchards planted beside the house, and notes that neither was found in the district "
     "before the estate was founded.\n\n"
     "Which part of the exchange does the record document?"),
  choices=[
   "Afro-Eurasian animals and fruit trees brought to the Americas",
   "American food crops carried to Afro-Eurasia",
   "Disease vectors transferred unintentionally",
   "Cash crops exported to the Middle East",
   "The nutritional benefit felt by populations in Afro-Eurasia"],
  ans=0,
  why=("KC-4.1.V.C says Afro-Eurasian fruit trees, grains, sugar, and domesticated animals were "
       "brought by Europeans to the Americas, and livestock with orchards new to the district is "
       "that half of the exchange. The rejected options name the other direction of KC-4.1.V.B, "
       "the vectors of KC-4.1.V.A and the benefit of KC-4.1.V.D.")),
 dict(
  q=("A hypothetical shipping list records four cargoes and the direction each travelled, as "
     "shown in the table below.\n\n"
     "Which conclusion is best supported by the table alone?"),
  table=_T_CARGOES,
  choices=[
   "Three of the four cargoes were carried to the Americas and one was carried away from them",
   "All four cargoes were carried to the Americas",
   "All four cargoes were carried away from the Americas",
   "The cargoes were divided evenly between the two directions",
   "No cargo in the list crossed between the hemispheres at all"],
  ans=0,
  why=("KC-4.1.V.C has fruit trees, grains, sugar and domesticated animals brought to the "
       "Americas and other foods brought by African enslaved persons, while KC-4.1.V.B has "
       "American foods becoming staples elsewhere, so the exchange runs both ways with more "
       "listed here going west. The verifier recomputes the direction recorded in every row.")),
 dict(
  q=("A hypothetical count of one region's population across four periods appears in the table "
     "below.\n\n"
     "Which statement about the recorded figures is accurate?"),
  table=_T_POPULATION,
  choices=[
   "The recorded population falls in every period and ends below half its first-period level",
   "The recorded population rises in every period shown",
   "The recorded population falls and then returns to its first-period level",
   "The recorded population is unchanged across the four periods",
   "The recorded population ends above three quarters of its first-period level"],
  ans=0,
  why=("KC-4.1.V.A says some of the diseases that spread substantially reduced the indigenous "
       "populations, with catastrophic effects in many areas, and a count of this shape is what "
       "a substantial reduction looks like in a record. The verifier recomputes the direction of "
       "change at every step and the final level against the first.")),
 dict(
  q=("A hypothetical survey of four regions counts the American food crops grown as staples in "
     "each, as set out in the table below.\n\n"
     "Which conclusion is best supported by the table?"),
  table=_T_STAPLES,
  choices=[
   "American food crops are grown as staples in the surveyed regions of Europe, Asia, and Africa alike",
   "American food crops are grown as staples only in the surveyed region of Europe",
   "American food crops are grown as staples only in the surveyed region of the Americas",
   "American food crops are grown as staples in the surveyed region of Asia but in neither of the other two outside the Americas",
   "No region in the survey grows any American food crop as a staple"],
  ans=0,
  why=("KC-4.1.V.B says American foods became staple crops in various parts of Europe, Asia, and "
       "Africa, and every one of those three surveyed regions returns a count above zero. The "
       "verifier recomputes each region's count and confirms that no surveyed region outside the "
       "Americas is empty.")),
 dict(
  q=("Suggested skill 3.B asks a student to identify the evidence a source uses to support its "
     "argument. A source argues that the exchange of this period reached ordinary diets in "
     "Afro-Eurasia. Which evidence in that source would be doing the work?"),
  choices=[
   "Records of American food crops appearing among the staples of Afro-Eurasian households",
   "Records of the tonnage of silver shipped from the Americas",
   "Records of the number of ships built in one European port",
   "Records of the titles held by a colonial governor",
   "Records of the stone used to build a colonial church"],
  ans=0,
  why=("KC-4.1.V.B and KC-4.1.V.D are the framework's statements that American foods became "
       "staple crops elsewhere and that Afro-Eurasian populations benefitted nutritionally from "
       "them, so the evidence bearing on the argument is what people there were eating. Silver, "
       "shipbuilding, titles and building stone bear on other claims.")),
 dict(
  q=("Why does the framework describe the transfer of mosquitoes and rats as unintentional, when "
     "it describes the transfer of cattle and fruit trees differently?"),
  choices=[
   "Because the vectors travelled as a by-product of colonization while the animals and trees were brought deliberately",
   "Because the vectors were carried deliberately and the animals were not",
   "Because the framework says neither transfer actually occurred",
   "Because the vectors are said to have crossed before 1450 and the animals after",
   "Because the framework says the vectors were carried by African enslaved persons"],
  ans=0,
  why=("KC-4.1.V.A calls the transfer of disease vectors unintentional and ties it to European "
       "colonization, while KC-4.1.V.C says fruit trees, grains, sugar, and domesticated animals "
       "were brought by Europeans, which is an act rather than a by-product. The distinction is "
       "the framework's own wording and not an inference.")),
 dict(
  q=("Which of the following claims about this topic would require evidence from outside the "
     "framework's own statements?"),
  choices=[
   "That one named disease killed a larger share of a population than another did",
   "That the diseases that spread were endemic in the Eastern Hemisphere",
   "That American foods became staple crops in various parts of Europe, Asia, and Africa",
   "That cash crops were grown primarily on plantations with coerced labor",
   "That Afro-Eurasian populations benefited nutritionally from American food crops"],
  ans=0,
  why=("The four rejected statements are KC-4.1.V.A, KC-4.1.V.B and KC-4.1.V.D almost verbatim. "
       "The framework gives no figure and no comparison of mortality between diseases, saying "
       "only that some of them substantially reduced the indigenous populations, so a ranking "
       "would have to be defended from another source.")),
 dict(
  q=("The Humans and the Environment thematic focus is printed with this topic. Which statement "
     "of it does the Columbian Exchange illustrate?"),
  choices=[
   "That the environment shapes human societies and that populations in turn shape their environments",
   "That governments obtain, retain, and exercise power in different ways",
   "That societies group their members and govern the norms between those groups",
   "That the development of ideas and religions shows how groups view themselves",
   "That societies are affected by the ways they produce and exchange goods"],
  ans=0,
  why=("The Humans and the Environment thematic focus printed with this topic says the "
       "environment shapes human societies and that as populations grow and change these "
       "populations in turn shape their environments, which is what KC-4.1.V describes when "
       "plants, animals, and diseases move between hemispheres. The rejected statements are the "
       "other four thematic focuses of the course.")),
 dict(
  q=("A student writes that the Columbian Exchange carried goods in one direction only. What is "
     "the most accurate correction from the framework?"),
  choices=[
   "Plants and animals moved in both directions, and the framework describes an effect of each direction",
   "Only diseases moved, and no plant or animal crossed either way",
   "Only American crops moved, and nothing was carried to the Americas",
   "Only Afro-Eurasian animals moved, and nothing was carried out of the Americas",
   "Nothing moved between the hemispheres until after 1750"],
  ans=0,
  why=("KC-4.1.V.C has Afro-Eurasian fruit trees, grains, sugar, and animals brought to the "
       "Americas, KC-4.1.V.B has American foods becoming staples in Europe, Asia, and Africa, and "
       "KC-4.1.V.D records a nutritional benefit in Afro-Eurasia, so the framework describes "
       "effects on both sides. Each rejected correction deletes one of those statements.")),
 dict(
  q=("Which piece of evidence would best support the claim that the exchange of this period "
     "reshaped agriculture in the Americas as well as in Afro-Eurasia?"),
  choices=[
   "Records of Afro-Eurasian grains and livestock appearing on farms in the Americas",
   "Records of the number of clerks employed in a European treasury",
   "Records of the depth of a harbour on the African coast",
   "Records of the taxes levied on a caravan in Central Asia",
   "Records of the wages paid to a shipwright in a European port"],
  ans=0,
  why=("KC-4.1.V.C says Afro-Eurasian fruit trees, grains, sugar, and domesticated animals were "
       "brought by Europeans to the Americas, so evidence for a change in American agriculture "
       "has to show those things arriving there. Treasury clerks, harbour depths, caravan taxes "
       "and shipwrights' wages bear on none of it.")),
 dict(
  q=("How does this topic relate to the labor systems described elsewhere in the unit?"),
  choices=[
   "The framework says cash crops were grown primarily on plantations with coerced labor",
   "The framework says cash crops were grown without any labor system at all",
   "The framework says plantations disappeared as the exchange grew",
   "The framework says coerced labor was confined to the Eastern Hemisphere",
   "The framework says the exchange had no economic dimension"],
  ans=0,
  why=("KC-4.1.V.B states that cash crops were grown primarily on plantations with coerced labor "
       "and exported mostly to Europe and the Middle East, which is the point at which this topic "
       "meets KC-4.2.II.C on the growth of the plantation economy and its demand for enslaved "
       "labor. Each rejected option contradicts one of those two statements.")),
 dict(
  q=("An examiner asks what the framework treats as the two sides of the Columbian Exchange's "
     "effects. Which answer is best supported?"),
  choices=[
   "A catastrophic loss of indigenous population in the Americas, and a nutritional gain for populations in Afro-Eurasia",
   "A nutritional gain in the Americas, and a catastrophic loss of population in Afro-Eurasia",
   "A gain on both sides, with no population loss recorded anywhere",
   "A loss on both sides, with no nutritional gain recorded anywhere",
   "No recorded effect on either side of the exchange"],
  ans=0,
  why=("KC-4.1.V.A gives the substantial reduction of indigenous populations with catastrophic "
       "effects in many areas, and KC-4.1.V.D gives the nutritional benefit to populations in "
       "Afro-Eurasia. The second option exchanges those two effects between the hemispheres, "
       "which is the misreading this item is built to catch.")),
 dict(
  q=("A summary sentence for this topic is being drafted for students. Which version stays within "
     "what the framework asserts about the period 1450 to 1750?"),
  choices=[
   "New connections between the hemispheres carried plants, animals, and diseases both ways: Afro-Eurasian crops and animals reached the Americas, American foods became staples in Europe, Asia, and Africa and improved nutrition there, and diseases endemic in the Eastern Hemisphere substantially reduced indigenous populations",
   "New connections carried only trade goods, and neither plants nor animals nor diseases crossed between the hemispheres",
   "American foods reached the Americas from Europe, while Afro-Eurasian animals became staples in Asia and Africa",
   "Diseases endemic in the Americas reduced European populations, and no crop crossed in either direction",
   "The exchange left both hemispheres exactly as they had been before 1450"],
  ans=0,
  why=("The keyed sentence joins KC-4.1.V on the exchange of plants, animals, and diseases to "
       "KC-4.1.V.C, KC-4.1.V.B, KC-4.1.V.D and KC-4.1.V.A in turn. Each rejected version denies "
       "the exchange, reverses the direction of the crops and animals, reverses the hemisphere "
       "the diseases came from, or denies every effect the framework records.")),
]
