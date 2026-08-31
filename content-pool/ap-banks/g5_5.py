# AP HUMAN GEOGRAPHY 5.5 The Green Revolution -- 30 questions
# CED Course Framework V.1, Unit 5. Enduring understanding SPS-5, "Agriculture
# has changed over time because of cultural diffusion and advances in
# technology." Learning objective SPS-5.D, "Explain the consequences of the
# Green Revolution on food supply and the environment in the developing world."
#
# Essential knowledge -- two statements:
#   SPS-5.D.1  The Green Revolution was characterized in agriculture by the use
#              of high-yield seeds, increased use of chemicals, and mechanized
#              farming.
#   SPS-5.D.2  The Green Revolution had positive and negative consequences for
#              both human populations and the environment.
#
# SPS-5.D.2 IS A TWO-BY-TWO AND THE MODULE IS BUILT ON IT. The statement crosses
# two axes -- positive/negative and human/environmental -- and it asserts that
# all four cells are occupied:
#
#                     POSITIVE                     NEGATIVE
#   human      more food, cheaper food,     capital requirement favours larger
#              famine averted               farmers, debt, displaced labour
#   environment less pressure to clear      fertilizer runoff, pesticide load,
#              new land for the same        salinization and falling water
#              output                       tables, narrowed crop diversity
#
# An item keyed to only one cell would be teaching half the sentence, so items 6
# to 15 walk all four and items 16, 23 and 30 key directly against one-sided
# readings in either direction. This is the single most important property of the
# topic: a student who has learned only that the Green Revolution fed people, or
# only that it damaged the environment, has learned the wrong sentence.
#
# WHY THE THREE CHARACTERISTICS ARE A PACKAGE, which is the mechanism the CED
# does not spell out and item 5 asks for directly. A high-yield variety is bred
# to convert nutrients and water into grain rather than into straw. It therefore
# out-yields a traditional variety ONLY when the nutrients and the water are
# supplied, which is what the increased use of chemicals and the irrigation and
# machinery are for. The three parts of SPS-5.D.1 are not three separate
# improvements; they are one system, and that is also why adoption tracked the
# ability to buy inputs (items 9, 17, 22, 28).
#
# "IN THE DEVELOPING WORLD" is in the learning objective, not the essential
# knowledge, but it fixes where the topic applies and item 21 keys on it.
#
# SYNONYM CARE. `geo_check` treats {"monocropping", "monoculture"} as one
# construct and {"genetically modified organisms", "gmos"} as another; GMOs
# belong to Topic 5.11's EK IMP-5.B.1 and are kept out of this module's keys
# entirely, since the CED's characterization here is high-yield SEEDS from
# conventional breeding.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("5.5", "The Green Revolution", 5)

QUESTIONS = [
 dict(q="By which three things does the framework characterize the Green Revolution in agriculture?", choices=[
   "High-yield seeds, increased use of chemicals, and mechanized farming",
   "Domestication of plants, domestication of animals, and settled villages",
   "Crop rotation, the seed drill, and enclosure of open fields",
   "Organic farming, community-supported agriculture, and fair trade",
   "High-yield seeds, reduced use of chemicals, and hand cultivation"], ans=0,
   why="EK SPS-5.D.1 names exactly these three characteristics. Crop rotation and the seed drill belong to the second agricultural revolution, and organic farming and fair trade are food-choice movements in EK IMP-5.B.2, so each of those describes a different part of the course."),

 dict(q="What makes a high-yield seed variety high-yielding?", choices=[
   "It has been bred to put more of the nutrients and water it receives into grain rather than into stem and leaf",
   "It needs no water or nutrients of any kind",
   "It produces seed that cannot be eaten",
   "It grows only in temperate climates",
   "It is the wild ancestor of a modern crop"], ans=0,
   why="EK SPS-5.D.1 names high-yield seeds as one of the Green Revolution's three characteristics. The gain comes from how the plant allocates what it takes up, which is why such a variety rewards heavy inputs and is unremarkable without them."),

 dict(q="Why does the framework name increased use of chemicals alongside high-yield seeds?", choices=[
   "A variety bred to convert nutrients into grain needs those nutrients supplied, and fertilizer is what supplies them",
   "Because chemicals replace the need for seed",
   "Because chemicals make land flatter",
   "Because high-yield seeds are themselves a chemical",
   "Because the framework lists the two as alternatives to each other"], ans=0,
   why="EK SPS-5.D.1 names both among the Green Revolution's characteristics, and they are complements rather than alternatives. A variety able to use more nitrogen produces more grain only when more nitrogen is actually applied."),

 dict(q="How does mechanized farming contribute to the package the framework describes?", choices=[
   "Machinery makes it possible to prepare, plant, irrigate and harvest a larger area on a tighter schedule, which the higher-yielding system requires",
   "Machinery increases the nutrient content of the soil",
   "Machinery removes the need for seed of any kind",
   "Machinery is unrelated to yields and appears on the list by accident",
   "Machinery reduces the total area a farm can work"], ans=0,
   why="EK SPS-5.D.1 names mechanized farming as one of the three characteristics. A system with more inputs, tighter timing and often more than one crop a year cannot be operated at the pace hand tools allow, so the three characteristics support one another."),

 dict(q="Why are the framework's three characteristics best understood as one package rather than as three independent improvements?", choices=[
   "The seed out-yields a traditional variety only when the water and nutrients it was bred to use are actually supplied, so adopting one part without the others gives little benefit",
   "Because all three were invented by the same person",
   "Because a farmer is legally required to adopt all three together",
   "Because each of the three works equally well on its own",
   "Because the three were adopted in three different regions"], ans=0,
   why="EK SPS-5.D.1 lists high-yield seeds, chemicals and mechanization together as the characterization of one thing. The seed is the component that makes the others worth buying and the others are what make the seed worth planting, which is why the package spread or failed to spread as a whole."),

 dict(q="Which is a POSITIVE consequence of the Green Revolution for human populations?", choices=[
   "Cereal output rose faster than population in several regions, so more people could be fed from the same land",
   "Fertilizer running off fields into rivers",
   "Water tables falling under heavily irrigated districts",
   "Farmers borrowing to buy inputs and falling into debt",
   "The narrowing of the range of crop varieties grown"], ans=0,
   why="EK SPS-5.D.2 states that the Green Revolution had positive and negative consequences for both human populations and the environment. Feeding a growing population from a land area that did not grow is the clearest of the positive human consequences, and the other four options are negative ones."),

 dict(q="Which is a POSITIVE environmental consequence of the Green Revolution?", choices=[
   "Producing more food on land already farmed reduced the pressure to clear additional forest and grassland",
   "Increased application of pesticides",
   "Salinization of irrigated soils",
   "Loss of traditional crop varieties",
   "Depletion of groundwater under irrigated districts"], ans=0,
   why="EK SPS-5.D.2 says the consequences were positive and negative for the environment as well as for people. Raising output per hectare means a given food requirement is met from a smaller area, which is an environmental gain set against the other four, which are costs."),

 dict(q="How did the Green Revolution affect food prices, and who benefited most directly from that effect?", choices=[
   "A larger supply lowered the real price of staple grain, which most directly benefited people who buy their food rather than growing it",
   "Prices rose sharply, which benefited urban consumers",
   "Prices were unaffected, since supply does not influence price",
   "Prices fell, which most benefited farmers selling grain",
   "Prices fell only for exported crops and not for staples"], ans=0,
   why="EK SPS-5.D.2 names positive consequences for human populations, and cheaper staple food is among the largest of them. A price fall is a gain to buyers and a squeeze on sellers, so the urban poor gain most directly while producers face lower returns per tonne."),

 dict(q="Why did the Green Revolution tend to widen the gap between larger and smaller farmers?", choices=[
   "The package had to be bought each season -- seed, fertilizer, water and machinery -- and farmers with capital or credit could buy it while others could not",
   "Because small farms have worse soil than large ones",
   "Because governments forbade small farmers from using new seed",
   "Because high-yield varieties will not grow on small plots",
   "Because larger farms are always closer to markets"], ans=0,
   why="EK SPS-5.D.2 names negative as well as positive consequences for human populations. The three characteristics of EK SPS-5.D.1 are all purchased inputs, so the ability to adopt tracked the ability to pay, and a technology that raises the income of those who can buy it widens the distance to those who cannot."),

 dict(q="A smallholder borrows to buy seed, fertilizer and pump irrigation, then loses the crop to a bad season. What negative consequence does this illustrate?", choices=[
   "Indebtedness, since the inputs must be paid for whether or not the harvest arrives",
   "Salinization, since irrigation was used",
   "A positive consequence, since the farmer adopted the new technology",
   "Genetic narrowing, since one variety was planted",
   "No consequence recognized by the framework"], ans=0,
   why="EK SPS-5.D.2 states that there were negative consequences for human populations. A system built on purchased inputs converts a bad season from a lean year into a debt, because the costs were incurred before the harvest failed."),

 dict(q="How did mechanization of Green Revolution farming affect rural employment?", choices=[
   "Machinery replaced tasks that had employed hired labour, so some rural workers lost work even as output rose",
   "Machinery increased the number of workers needed per hectare",
   "Machinery had no effect on rural employment anywhere",
   "Machinery employed only people who already owned land",
   "Machinery reduced output and therefore employment"], ans=0,
   why="EK SPS-5.D.1 names mechanized farming among the characteristics and EK SPS-5.D.2 names negative consequences for human populations. Ploughing, threshing and harvesting by machine displaces exactly the seasonal wage work that landless rural households depend on."),

 dict(q="Nitrogen fertilizer applied in excess of what a crop can take up reaches rivers and lakes. What is the environmental consequence?", choices=[
   "The added nutrients feed algal growth, whose decay strips oxygen from the water and kills aquatic life",
   "The nutrients make the water permanently safer to drink",
   "The nutrients evaporate without effect",
   "The nutrients raise the water level of the river",
   "There is no consequence, since fertilizer is used on land"], ans=0,
   why="EK SPS-5.D.2 names negative environmental consequences, and fertilizer runoff is the classic one. What is a nutrient in a field is also a nutrient in water, so the effect is not a poisoning but an over-feeding whose consequence is oxygen depletion."),

 dict(q="Why is heavy pesticide use listed among the negative environmental consequences?", choices=[
   "Pesticides kill organisms beyond the target pest and can persist in soil, water and food chains",
   "Pesticides raise crop yields and so cannot be negative",
   "Pesticides are applied only to non-agricultural land",
   "Pesticides prevent machinery from operating",
   "Pesticides make soil saline"], ans=0,
   why="EK SPS-5.D.1 names increased use of chemicals among the characteristics and EK SPS-5.D.2 names negative environmental consequences. A compound designed to kill one organism rarely distinguishes perfectly between species, which is why the effects extend past the field."),

 dict(q="Irrigating a dry district heavily over many years leads to salt accumulating in the topsoil. What is the mechanism?", choices=[
   "Irrigation water carries dissolved salts, and where evaporation exceeds drainage the water leaves and the salt stays behind",
   "Salt is added deliberately to raise yields",
   "Irrigation water is itself made of salt",
   "Machinery deposits salt as it works the ground",
   "High-yield seeds release salt into the soil"], ans=0,
   why="EK SPS-5.D.2 names negative environmental consequences, and salinization is among the most serious for irrigated agriculture. The salt was always dissolved in the water; what changes is that repeated evaporation concentrates it at the surface until the ground will no longer grow a crop."),

 dict(q="Why does the spread of a small number of high-yield varieties raise a risk that traditional mixed varieties did not?", choices=[
   "A large area planted with genetically similar plants can be damaged by a single pest or disease that all of them share a vulnerability to",
   "Because high-yield varieties cannot reproduce at all",
   "Because traditional varieties yield more in every case",
   "Because genetic similarity makes a crop immune to disease",
   "Because narrow diversity reduces the area that can be planted"], ans=0,
   why="EK SPS-5.D.2 names negative environmental consequences of the Green Revolution, and the loss of crop diversity is one of them. Diversity across a landscape acts as insurance, because a pathogen that defeats one variety meets a different defence in the next field."),

 dict(q="A student writes that the Green Revolution was simply a success. What does the framework's own wording require the student to add?", choices=[
   "That its consequences were positive AND negative, for human populations and for the environment alike",
   "That it had no consequences for the environment",
   "That its consequences were entirely negative",
   "That it affected only wealthy countries",
   "That the framework takes no position on its consequences"], ans=0,
   why="EK SPS-5.D.2 says in one sentence that the Green Revolution had positive and negative consequences for both human populations and the environment. A one-sided account is not a stronger version of the framework's claim but a different and weaker one."),

 dict(q="Why did the Green Revolution transform some regions and barely reach others?", choices=[
   "It required irrigation, credit and input supply chains, and regions without them could not run the package",
   "Because farmers in some regions had never heard of the new varieties",
   "Because the new varieties were legally restricted to a few countries",
   "Because some regions had no need for more food",
   "Because the framework says the revolution reached every region equally"], ans=0,
   why="EK SPS-5.D.1's three characteristics are all things that must be delivered and paid for, and EK SPS-5.D.2 records that consequences differed. Where water could not be controlled or inputs could not be bought and moved, the seed alone produced no revolution."),

 dict(q="How does the Green Revolution differ from the second agricultural revolution?", choices=[
   "It is a later, largely twentieth-century change centred on the developing world, built on bred seed varieties and purchased chemical inputs",
   "It is another name for the same set of changes",
   "It concerned only the domestication of new species",
   "It occurred entirely before the Industrial Revolution",
   "It reduced yields rather than raising them"], ans=0,
   why="EK SPS-5.C.1 describes the second agricultural revolution's technology and social impacts while EK SPS-5.D.1 characterizes the Green Revolution by high-yield seeds, chemicals and mechanization. Learning objective SPS-5.D locates the latter's consequences in the developing world, which is a further difference."),

 dict(q="A country doubles its cereal production and still has widespread hunger. What does this show?", choices=[
   "Producing food and being able to obtain it are different things, so a rise in national output does not by itself reach every household",
   "That the production figures must be false",
   "That hunger is unrelated to food supply in any way",
   "That the Green Revolution never occurred in that country",
   "That national output is the only thing that matters for hunger"], ans=0,
   why="EK SPS-5.D.2 names both positive and negative consequences for human populations, and the two can occur in the same country at once. Output is measured nationally while eating happens in a household, so purchasing power and distribution decide who benefits from an aggregate gain."),

 dict(q="At which scales must the Green Revolution's consequences be examined to see the whole picture?", choices=[
   "National output, regional adoption and the individual farm household, since the same change reads as a triumph, an unevenness and a debt at those three scales",
   "The global scale only, since food is traded internationally",
   "The household scale only, since farming is a family activity",
   "No scale, since consequences are not spatial",
   "The continental scale only, since climate zones cross borders"], ans=0,
   why="EK SPS-5.D.2 names consequences that are positive and negative at the same time, which is possible because they fall on different people in different places. Choosing one scale and stopping there is how a student comes away with only half of the statement."),

 dict(q="The framework's learning objective locates the Green Revolution's consequences in which part of the world?", choices=[
   "The developing world",
   "The polar regions",
   "Only countries that had already industrialized",
   "The Fertile Crescent and the Indus River Valley",
   "Countries with Mediterranean climates only"], ans=0,
   why="Learning objective SPS-5.D asks students to explain the consequences of the Green Revolution on food supply and the environment IN THE DEVELOPING WORLD. That location is part of what distinguishes it from the earlier agricultural revolutions of this unit."),

 dict(q="A farmer with two hectares and no access to credit continues to plant a traditional variety while neighbours with larger holdings adopt the new package. What is the most accurate description of the outcome?", choices=[
   "The technology is available in principle but not in practice for this household, so the gap between its income and its neighbours' widens",
   "The farmer will obtain the same yields as the adopters",
   "The framework predicts that small farms always adopt first",
   "The farmer has chosen a higher-yielding option",
   "There is no difference in outcome, since all farmers face the same weather"], ans=0,
   why="EK SPS-5.D.1's three characteristics are all purchased, and EK SPS-5.D.2 records negative as well as positive consequences for human populations. Availability and affordability are different conditions, and it is the second that determines who actually adopts."),

 dict(q="Is a large rise in yields sufficient evidence that the Green Revolution was beneficial in a district? What does the framework imply?", choices=[
   "No, because the framework requires the environmental costs and the distribution of the gains to be weighed alongside the yield figure",
   "Yes, because yield is the only measure the framework names",
   "No, because yields are impossible to measure accurately",
   "Yes, because the framework says all consequences were positive",
   "No, because the framework says yields did not actually rise"], ans=0,
   why="EK SPS-5.D.2 names consequences for human populations AND the environment, and both positive and negative. A yield figure speaks to one cell of that account, and the statement's structure is what makes the other three cells part of the question."),

 dict(q="Which change would most directly address the environmental costs the framework attributes to the Green Revolution while keeping its yield gains?", choices=[
   "Applying nutrients and water in the amounts and at the times the crop can actually use, rather than in excess",
   "Abandoning irrigation entirely in all districts",
   "Returning to the varieties grown before the revolution everywhere",
   "Increasing pesticide applications to protect the higher yields",
   "Planting a single variety across a still wider area"], ans=0,
   why="EK SPS-5.D.2 names both positive and negative consequences, which frames the problem as one of keeping the first while reducing the second. Runoff, salinization and falling water tables are consequences of applying more than the crop can take up, so matching the application to the uptake attacks the cost without surrendering the gain."),

 dict(q="How does the Green Revolution bear on Malthus's argument about population and food supply?", choices=[
   "It is a case of food output rising faster than population for a period, which is what Malthus's argument said could not be sustained",
   "It confirms Malthus's prediction exactly",
   "It has no bearing on any argument about population",
   "It shows that population always grows faster than food supply",
   "It shows that food supply cannot be increased by technology"], ans=0,
   why="EK SPS-5.D.2 names positive consequences for human populations, and the largest of them is that more people were fed than the earlier trend suggested could be. Whether the gain can be repeated indefinitely is exactly the open question, which is where the environmental costs re-enter the argument."),

 dict(q="Yields and fertilizer use in one country are recorded below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Measure", "Before the new varieties", "After the new varieties"],
     rows=[["Rice yield (tonnes per hectare)", "1.9", "4.6"],
           ["Wheat yield (tonnes per hectare)", "1.1", "3.2"],
           ["Fertilizer applied (kilograms per hectare)", "8", "92"],
           ["Area under cereals (million hectares)", "22", "22"]]),
   choices=[
   "Both cereal yields more than doubled while fertilizer application rose more than elevenfold on an unchanged area",
   "Yields rose because the area under cereals expanded",
   "Fertilizer use fell as yields rose",
   "Wheat yields rose while rice yields fell",
   "No change can be identified, since only four measures are given"], ans=0,
   why="Rice rises from 1.9 to 4.6 and wheat from 1.1 to 3.2 tonnes per hectare, both more than doubling, while fertilizer rises from 8 to 92 kilograms per hectare and the cereal area is identical in both columns. EK SPS-5.D.1 names high-yield seeds and increased chemical use together, and the record shows the two moving together on land already in cultivation."),

 dict(q="Irrigation and soil condition in one district are recorded below. Using the accompanying figures, what has occurred?",
   table=dict(headers=["Period", "Irrigated area (thousand hectares)", "Area with damaging salt accumulation (thousand hectares)"],
     rows=[["Earlier", "1,200", "50"],
           ["Later", "4,800", "900"]]),
   choices=[
   "Irrigated area quadrupled while salt-damaged area rose eighteenfold, so the damaged share of irrigated land rose from about 4 percent to about 19 percent",
   "Both areas grew at the same rate, so the damaged share was unchanged",
   "Salt-damaged area fell as irrigation expanded",
   "Irrigation expanded but no salt damage occurred",
   "The damaged share of irrigated land fell from 19 percent to 4 percent"], ans=0,
   why="Irrigated area rises from 1,200 to 4,800 thousand hectares, a factor of four, while damaged area rises from 50 to 900, a factor of eighteen, so the damaged share rises from about 4 to about 19 percent. EK SPS-5.D.2 names negative environmental consequences, and a cost growing faster than the practice producing it is what the record shows."),

 dict(q="Adoption of the new package by farm size is recorded below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Holding size", "Farms in the district", "Share adopting the full package (%)"],
     rows=[["Under 1 hectare", "4,100", "22"],
           ["1 to 4 hectares", "2,600", "48"],
           ["4 to 10 hectares", "900", "79"],
           ["Over 10 hectares", "300", "94"]]),
   choices=[
   "Adoption rises steadily with holding size, from 22 percent on the smallest farms to 94 percent on the largest",
   "Adoption falls as holding size rises",
   "Adoption is the same at every holding size",
   "The largest farms are the most numerous and therefore adopted most",
   "No pattern can be read, since the number of farms differs by size band"], ans=0,
   why="The adoption share rises at every step from 22 to 48 to 79 to 94 percent as holdings get larger, while the number of farms falls in the same direction, so the majority of farms are in the least-adopting band. EK SPS-5.D.2 names negative consequences for human populations, and a technology taken up in proportion to holding size is how a yield gain becomes a widening gap."),

 dict(q="What limitation should be stated when using a table of adoption rates by farm size to explain inequality?", choices=[
   "The record shows that adoption and holding size move together, but not whether capital, irrigation access or something else is what actually prevents adoption",
   "Adoption rates cannot be compared across farm sizes at all",
   "Percentages and counts can never appear in the same record",
   "A pattern in a table always establishes its own cause",
   "The framework forbids the use of quantitative evidence in this topic"], ans=0,
   why="EK SPS-5.D.2 names negative consequences for human populations without specifying a mechanism, so the mechanism has to be argued rather than read off. Holding size is correlated with credit, irrigation and market access all at once, which is why a size-banded table narrows the explanation without settling it."),

 dict(q="Which statement best captures what this topic's two essential knowledge statements assert together?", choices=[
   "A package of high-yield seeds, chemicals and machinery raised output substantially and brought both benefits and costs to people and to the environment",
   "A package of high-yield seeds, chemicals and machinery was beneficial in every respect",
   "The Green Revolution damaged the environment and produced no benefits",
   "The Green Revolution consisted of returning to traditional seed varieties",
   "The Green Revolution affected the environment but not human populations"], ans=0,
   why="EK SPS-5.D.1 supplies the three characteristics and EK SPS-5.D.2 supplies the two-sided account across both people and the environment. Each rejected summary drops one of the four cells the second statement asserts to be occupied."),
]
