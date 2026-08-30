# AP HUMAN GEOGRAPHY 2.11 Forced and Voluntary Migration -- 30 questions
# CED Course Framework V.1, Unit 2. Enduring understanding IMP-2; learning
# objective IMP-2.D, "Describe types of forced and voluntary migration."
#
# Essential knowledge, in full -- two statements, each a closed list:
#   IMP-2.D.1  Forced migrations include slavery and events that produce
#              refugees, internally displaced persons, and asylum seekers.
#   IMP-2.D.2  Types of voluntary migrations include transnational,
#              transhumance, internal, chain, step, guest worker, and
#              rural-to-urban.
#
# Because both statements are lists of NAMES, almost every key in this module is
# a classification: given a case, which term applies. The definitions below are
# the ones the module holds itself to, since the CED prints no definitions.
#
# FORCED (IMP-2.D.1):
#   slavery                      movement under coercion and ownership, with no
#                                element of choice at any stage
#   refugee                      has CROSSED AN INTERNATIONAL BORDER fleeing
#                                persecution, conflict or violence
#   internally displaced person  forced to flee for the same reasons but has
#                                NOT crossed a border, and so remains under the
#                                jurisdiction of the state they fled
#   asylum seeker                has crossed a border and APPLIED for protection
#                                but whose claim is not yet decided
#   The three are distinguished by exactly two questions -- was a border
#   crossed, and has a claim been decided -- and items 2, 3, 4, 8, 12, 22 and 26
#   turn on that pair.
#
# VOLUNTARY (IMP-2.D.2), all seven:
#   transnational    movement across international borders, often with
#                    continuing ties to and movement between both countries
#   transhumance     SEASONAL movement of herders with livestock between
#                    pastures, usually between lowland and highland. It is
#                    cyclical rather than one-way, which is why it is the one
#                    entry students misclassify most often; item 10 asks about
#                    that directly
#   internal         movement within one country's borders
#   chain            following relatives or people from the same community to a
#                    destination they have already established
#   step             a sequence of shorter moves up the settlement hierarchy
#                    rather than one long move
#   guest worker     temporary labour migration under a programme, with the
#                    right to remain tied to the work
#   rural-to-urban   countryside to city, the dominant internal flow of the
#                    industrializing and urbanizing world
#
# One honesty point the module makes explicit. The forced/voluntary line is a
# spectrum rather than a switch: a household leaving because drought has
# destroyed its livelihood is not coerced by anyone and is not freely choosing
# either. Item 25 tests that the line is a simplification, because presenting it
# as absolute would be teaching something false.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g2_11.py. FIVE choices (A-E).
TOPIC = ("2.11", "Forced and Voluntary Migration", 2)

QUESTIONS = [
 dict(q="Which of the following does the framework list as a form of FORCED migration?",
   choices=[
     "Events that produce refugees, internally displaced people, and asylum seekers, together with slavery",
     "Transhumance and chain migration",
     "Guest worker programmes and step migration",
     "Rural-to-urban and internal migration",
     "Transnational migration and chain migration"],
   ans=0,
   why="EK IMP-2.D.1 names slavery and the events producing refugees, internally displaced persons and asylum seekers. Every other option is drawn from EK IMP-2.D.2's list of VOLUNTARY types, which is the distinction the learning objective asks students to make."),

 dict(q="A family flees armed conflict and crosses into a neighbouring country, where their claim for protection has been recognized. They are",
   choices=[
     "Refugees, since they crossed an international border and their status has been determined",
     "Internally displaced people, since they fled violence",
     "Asylum seekers, since they fled to another country",
     "Guest workers, since they are living abroad",
     "Transnational migrants, since they crossed a border"],
   ans=0,
   why="EK IMP-2.D.1 lists refugees separately from internally displaced persons and asylum seekers, and the two questions that separate them are whether a border was crossed and whether the claim has been decided. Here both answers are yes."),

 dict(q="A family flees the same conflict but remains inside their own country, sheltering in a camp two hundred kilometres from home. They are",
   choices=[
     "Internally displaced people, since they have not crossed an international border",
     "Refugees, since they fled violence",
     "Asylum seekers, since they are seeking safety",
     "Voluntary internal migrants, since they moved within one country",
     "Guest workers, since they may find work in the camp"],
   ans=0,
   why="EK IMP-2.D.1 lists internally displaced persons as a category distinct from refugees, and the border is the whole of the distinction. Distance moved is irrelevant, which is why a two-hundred-kilometre move inside a country is displacement and a five-kilometre move across a border is not."),

 dict(q="A person has crossed an international border, lodged a claim for protection, and is waiting for a decision. The correct term is",
   choices=[
     "Asylum seeker, since the claim has been made but not yet determined",
     "Refugee, since the border has been crossed",
     "Internally displaced person, since the case is unresolved",
     "Guest worker, since the person is awaiting permission to stay",
     "Chain migrant, since others have made the same journey"],
   ans=0,
   why="EK IMP-2.D.1 lists asylum seekers as a separate category from refugees, and what separates them is the decision rather than the journey. The same person may become a refugee if the claim succeeds or be required to leave if it fails."),

 dict(q="Which sequence correctly matches the three status terms to what distinguishes them?",
   choices=[
     "Internally displaced people have not crossed a border; asylum seekers have crossed and await a decision; refugees have crossed and been recognized",
     "Refugees have not crossed a border; asylum seekers have; internally displaced people are recognized",
     "All three terms mean the same thing in different countries",
     "The terms are distinguished by the distance each group has travelled",
     "The terms are distinguished by whether the migration was economic or political"],
   ans=0,
   why="EK IMP-2.D.1 lists all three, and only two questions separate them: was an international border crossed, and has the protection claim been decided. Distance and motive vary within each category and cannot do the work."),

 dict(q="The transatlantic slave trade forcibly moved millions of people across an ocean over three centuries. In the framework's terms, this is",
   choices=[
     "The clearest case of forced migration, since the people moved had no element of choice at any stage",
     "A form of guest worker migration",
     "A form of chain migration",
     "Voluntary transnational migration, since a border was crossed",
     "Step migration, since the journey had stages"],
   ans=0,
   why="EK IMP-2.D.1 names slavery explicitly among forced migrations. What makes a migration forced is the absence of choice rather than the distance or the direction, and no case is further from choice than movement under ownership."),

 dict(q="A worker from one country lives and works in another for a decade, sends money home monthly, visits annually, and holds property in both. This is best described as",
   choices=[
     "Transnational migration, since the migrant maintains active ties in and movement between both countries",
     "Forced migration, since economic need drove the move",
     "Transhumance, since the migrant moves back and forth",
     "Internal migration, since the migrant has two homes",
     "Step migration, since the migrant will eventually move again"],
   ans=0,
   why="EK IMP-2.D.2 lists transnational among the voluntary types, and its defining feature is that the migrant's life spans two countries rather than being transferred from one to the other. Remittances, visits and property in both places are exactly that pattern."),

 dict(q="Herders move their cattle from lowland winter pastures to highland summer pastures each year and return in the autumn. This is",
   choices=[
     "Transhumance, a seasonal and cyclical movement between pastures",
     "Chain migration, since the same families follow the same route",
     "Step migration, since the move occurs in stages",
     "Forced migration, since the animals must be fed",
     "Rural-to-urban migration, since the herders move to higher ground"],
   ans=0,
   why="EK IMP-2.D.2 lists transhumance among the voluntary types, and it is the only one that is cyclical rather than one-way. The herders return every year, which distinguishes it from every other entry on the list."),

 dict(q="Why is transhumance the entry on the voluntary list that students most often misclassify?",
   choices=[
     "Every other type describes a move to a new place of residence, while transhumance is a repeating seasonal cycle back to the same places",
     "Transhumance is the only type involving international borders",
     "Transhumance is the only type that is forced",
     "Transhumance always involves cities",
     "Transhumance is not really a form of migration"],
   ans=0,
   why="EK IMP-2.D.2 puts transhumance in the same list as chain, step and rural-to-urban migration, all of which relocate a household. Recognising that one member of a list has a different structure from the rest is the point of learning the list rather than reciting it."),

 dict(q="Families from one village have moved, over twenty years, to the same three streets of a distant city, each helped by relatives already there. This is",
   choices=[
     "Chain migration, since each move follows a path opened by earlier migrants from the same community",
     "Step migration, since the moves happened over twenty years",
     "Transhumance, since the families keep ties to the village",
     "Forced migration, since the village had few opportunities",
     "Guest worker migration, since the migrants work in the city"],
   ans=0,
   why="EK IMP-2.D.2 lists chain migration among the voluntary types, and the mechanism is information and support flowing back along an established route. The concentration into a few streets is the signature: a random set of movers would not cluster like that."),

 dict(q="A migrant moves from a village to a market town, then after five years to a provincial city, then to the capital. This is",
   choices=[
     "Step migration, a sequence of moves up the settlement hierarchy",
     "Chain migration, since each move follows the last",
     "Transhumance, since the migrant keeps moving",
     "Transnational migration, since three places are involved",
     "Forced migration, since the migrant did not stay"],
   ans=0,
   why="EK IMP-2.D.2 lists step migration separately from chain migration, and the two answer different questions: step is about the ROUTE, chain about WHO opened it. A hierarchy climbed in stages is the step pattern precisely."),

 dict(q="A country admits workers for fixed three-year contracts, tied to a named employer, with no route to permanent residence. Those workers are",
   choices=[
     "Guest workers, since their right to remain is tied to temporary employment",
     "Refugees, since they live in a country not their own",
     "Asylum seekers, since their status is temporary",
     "Internally displaced people, since they moved for work",
     "Transhumant migrants, since their stay is seasonal"],
   ans=0,
   why="EK IMP-2.D.2 lists guest worker migration among the voluntary types. The defining feature is the conditionality of the stay -- it lasts as long as the work does -- rather than the length of the contract or the distance travelled."),

 dict(q="A young woman leaves her family's farm for a factory job in a nearby city. This is best classified as",
   choices=[
     "Rural-to-urban migration, which is also a form of internal migration",
     "Transnational migration, since she leaves the family",
     "Forced migration, since the farm could not support her",
     "Transhumance, since she may return at harvest",
     "Guest worker migration, since she works in a factory"],
   ans=0,
   why="EK IMP-2.D.2 lists both internal and rural-to-urban migration, and this case satisfies both descriptions at once: the move stays inside one country and it runs from countryside to city. Naming the more specific of the two is the fuller answer."),

 dict(q="Which pair of terms from the voluntary list overlaps rather than excluding one another?",
   choices=[
     "Internal and rural-to-urban, since a countryside-to-city move within one country is both",
     "Transhumance and guest worker, since both are seasonal",
     "Chain and forced, since both involve communities",
     "Step and transnational, since both involve borders",
     "Guest worker and refugee, since both are temporary"],
   ans=0,
   why="EK IMP-2.D.2's list is not a partition: several of its entries describe different aspects of one move. Internal names where the move stays and rural-to-urban names what it runs between, so one migration can carry both labels honestly."),

 dict(q="What single question separates a refugee from an internally displaced person?",
   choices=[
     "Whether an international border was crossed",
     "Whether the person fled violence",
     "How far the person travelled",
     "Whether the person intends to return",
     "Whether the person found employment"],
   ans=0,
   why="EK IMP-2.D.1 lists the two categories separately, and both describe people forced to flee for the same reasons. The border is the only difference, and it matters because it changes which state and which body of law is responsible for them."),

 dict(q="Why does the distinction between a refugee and an internally displaced person have practical consequences?",
   choices=[
     "A refugee has left the jurisdiction of the state they fled and can seek international protection, while a displaced person remains under that state's authority",
     "Refugees travel further than displaced people in every case",
     "Displaced people are always more numerous",
     "Refugees are voluntary migrants and displaced people are not",
     "The distinction is only a matter of vocabulary"],
   ans=0,
   why="EK IMP-2.D.1 separates the two categories, and the reason the separation matters is legal and practical rather than descriptive. International protection is available across a border and largely unavailable inside the country of origin."),

 dict(q="A guest worker programme runs for thirty years, and many workers stay, bring families, and settle permanently. What does this illustrate?",
   choices=[
     "Temporary labour programmes frequently produce permanent settlement, because people build lives where they work",
     "Guest workers are legally refugees",
     "Guest worker migration is a form of forced migration",
     "Guest worker programmes never produce settlement",
     "The workers were engaged in transhumance"],
   ans=0,
   why="EK IMP-2.D.2's guest worker category is defined by the intended temporariness of the arrangement, which is a policy design rather than a prediction of behaviour. Long programmes produce marriages, children and communities that no contract term dissolves."),

 dict(q="Which of the following is NOT one of the voluntary types the framework lists?",
   choices=[
     "Displacement",
     "Chain migration",
     "Step migration",
     "Transhumance",
     "Guest worker migration"],
   ans=0,
   why="EK IMP-2.D.2's list contains transnational, transhumance, internal, chain, step, guest worker and rural-to-urban migration. Displacement belongs to EK IMP-2.D.1's forced category, which is exactly the confusion this item tests."),

 dict(q="A country's largest internal flow is from its interior provinces to its coastal manufacturing cities. Which two terms apply?",
   choices=[
     "Internal migration and rural-to-urban migration",
     "Transnational migration and chain migration",
     "Forced migration and step migration",
     "Transhumance and guest worker migration",
     "Asylum-seeking and chain migration"],
   ans=0,
   why="EK IMP-2.D.2 names both terms, and a flow that stays inside one country and runs from farming provinces to manufacturing cities satisfies each. Neither term excludes the other, which is why the fuller description uses both."),

 dict(q="Which observation would best support the claim that a particular migration stream is a CHAIN rather than an unconnected set of moves?",
   choices=[
     "Migrants from one origin community are heavily concentrated in a few destination neighbourhoods and most report a relative already there",
     "The migrants all left in the same year",
     "The migrants all work in the same industry",
     "The migrants travelled the same distance",
     "The migrants are all of working age"],
   ans=0,
   why="EK IMP-2.D.2's chain migration is defined by the link between earlier and later migrants, so the evidence must show that link operating. Spatial concentration at the destination plus prior contacts is exactly what an unconnected set of moves would not produce."),

 dict(q="A person fled persecution, crossed a border, was refused protection, and has appealed. What is the most accurate description of their current status?",
   choices=[
     "Still an asylum seeker, since no final decision has been reached on the claim",
     "A refugee, since they fled persecution",
     "An internally displaced person, since the claim was refused",
     "A guest worker, since they are permitted to remain during the appeal",
     "A voluntary migrant, since they chose to appeal"],
   ans=0,
   why="EK IMP-2.D.1 separates asylum seekers from refugees by whether the claim has been decided, and an appeal means it has not been decided finally. The reasons for flight do not by themselves confer the recognized status."),

 dict(q="Which of these best explains why the number of internally displaced people worldwide is usually larger than the number of refugees?",
   choices=[
     "Most people fleeing danger move as short a distance as they can and never leave their own country, and crossing a border requires means and permission",
     "There are more conflicts inside countries than between them, so no one crosses borders",
     "Refugees are undercounted while displaced people are counted twice",
     "Displaced people move further on average",
     "Border crossings are unrestricted almost everywhere"],
   ans=0,
   why="EK IMP-2.D.1 distinguishes the two by the border, and the border is a real barrier with costs, documents and controls attached. Distance decay applies to forced movement too: people stop as soon as they are safe, and safety is often found within their own country."),

 dict(q="A student writes that all migration is either entirely forced or entirely voluntary. What is the strongest correction?",
   choices=[
     "The two form a spectrum, and cases such as a household leaving because drought destroyed its livelihood sit between coercion and free choice",
     "All migration is in fact forced",
     "All migration is in fact voluntary",
     "The framework recognizes only forced migration",
     "The framework recognizes only voluntary migration"],
   ans=0,
   why="EK IMP-2.D.1 and EK IMP-2.D.2 list the two kinds separately, which is a classification rather than a claim that every case falls cleanly on one side. Environmental and economic collapse remove options without any person compelling the move, which is why the boundary is argued over."),

 dict(q="Which pairing correctly matches a case to its type?",
   choices=[
     "A family following cousins to a city where those cousins already live, matched to chain migration",
     "A herder's annual move to summer pasture, matched to step migration",
     "A person awaiting a decision on a protection claim, matched to refugee status",
     "A worker on a three-year employer-tied contract, matched to transhumance",
     "A household fleeing conflict without leaving its country, matched to refugee status"],
   ans=0,
   why="EK IMP-2.D.2 defines chain migration by the link to earlier migrants from the same community, which the case describes exactly. Each of the other pairings attaches a case to a term whose defining feature it does not have."),

 dict(q="Why does the framework treat 'events that produce refugees' rather than 'refugees' as the forced migration?",
   choices=[
     "The forced element lies in the conflict or persecution that removes the option of staying, not in the person's status afterward",
     "Refugees are not really migrants",
     "The status is granted after the migration and so cannot cause it",
     "The framework treats all statuses as voluntary",
     "The wording is accidental and carries no meaning"],
   ans=0,
   why="EK IMP-2.D.1's wording locates the coercion in the events rather than in the label. A status is assigned by a state after the fact, while what made the migration forced was the situation that left no alternative to leaving."),

 dict(q="Displacement figures for one conflict are shown. Using the table, what share of those displaced remained inside the country?",
   table=dict(
     headers=["Category", "People (thousands)"],
     rows=[
       ["Displaced within the country", "3,600"],
       ["Recognized as refugees abroad", "1,100"],
       ["Awaiting a decision on a claim abroad", "300"]]),
   choices=[
     "72 percent, since 3,600 of 5,000 thousand did not cross a border",
     "3,600 percent, since that is the number displaced internally",
     "50 percent, since roughly half of those displaced crossed a border",
     "28 percent, since 1,400 thousand went abroad",
     "The share cannot be calculated without knowing the country's population"],
   ans=0,
   why="Adding the three rows gives 5,000 thousand people, of whom 3,600 thousand did not cross a border, which is 72 percent. The two categories abroad total 1,400 thousand, or 28 percent, which is the complement rather than the answer."),

 dict(q="Migration into one city is broken down by origin and by whether the migrant had a relative already there. Using the table, which origin's flow shows the strongest evidence of chain migration?",
   table=dict(
     headers=["Origin district", "Migrants", "Had a relative already in the city"],
     rows=[
       ["District 1", "4,000", "1,200"],
       ["District 2", "900", "810"],
       ["District 3", "6,000", "2,400"],
       ["District 4", "2,000", "1,300"]]),
   choices=[
     "District 2, where 90 percent had a relative already in the city",
     "District 3, which sent the most migrants and the most with relatives",
     "District 1, where 30 percent had a relative already in the city",
     "District 4, where 65 percent had a relative already in the city",
     "District 3, because the largest flow must be the most connected"],
   ans=0,
   why="Shares are 30, 90, 40 and 65 percent, so the district sending the most migrants and the most with relatives in absolute terms is not the one whose flow is most strongly chained. Chain migration is a property of the mechanism, which is a rate rather than a count."),

 dict(q="A country's in-migrants are classified by type over three decades. Using the table, what has changed?",
   table=dict(
     headers=["Decade", "Guest workers", "Family members joining earlier migrants", "Asylum seekers"],
     rows=[
       ["1970s", "82,000", "9,000", "4,000"],
       ["1990s", "41,000", "68,000", "21,000"],
       ["2010s", "22,000", "94,000", "38,000"]]),
   choices=[
     "Labour recruitment fell by three quarters while family migration grew more than tenfold, which is the chain a guest worker programme sets up",
     "All three categories fell over the period",
     "Guest worker migration grew while family migration fell",
     "The total number of in-migrants fell over the period",
     "Asylum seekers were the largest category in every decade"],
   ans=0,
   why="Guest workers fall from 82,000 to 22,000, a reduction of 73 percent, while family arrivals rise from 9,000 to 94,000, a factor of more than ten, and the total rises from 95,000 to 154,000. Workers admitted temporarily who settle become the anchor for a chain the programme did not intend."),

 dict(q="Herd movements are recorded for one pastoral community. Using the table, which pattern do the records describe?",
   table=dict(
     headers=["Month", "Location of herds", "Elevation (m)"],
     rows=[
       ["January", "Valley floor", "400"],
       ["April", "Mid-slope pastures", "1,100"],
       ["July", "High summer pastures", "2,300"],
       ["October", "Mid-slope pastures", "1,100"],
       ["December", "Valley floor", "400"]]),
   choices=[
     "Transhumance, since the herds return to the same elevation they started from within a single year",
     "Step migration, since the herds move up the hierarchy in stages",
     "Chain migration, since the same families follow one another",
     "Rural-to-urban migration, since the herds leave the valley",
     "Forced migration, since the herds must follow the grass"],
   ans=0,
   why="Elevation rises from 400 to 2,300 metres and returns to 400 within the same year, which makes the movement cyclical rather than a relocation. That return is what separates transhumance from every other type on the voluntary list."),

 dict(q="Four migration streams are described by their characteristics. Using the table, which stream is the clearest case of step migration?",
   table=dict(
     headers=["Stream", "Number of separate moves", "Settlement size at each successive stop", "Crossed a border"],
     rows=[
       ["Stream W", "1", "Village to capital", "No"],
       ["Stream X", "4", "Village, town, small city, capital", "No"],
       ["Stream Y", "1", "Village to a foreign capital", "Yes"],
       ["Stream Z", "2", "Village to town, then back to village", "No"]]),
   choices=[
     "Stream X, whose four moves ascend the settlement hierarchy without a single long jump",
     "Stream W, which reaches the capital in one move",
     "Stream Y, which crosses an international border",
     "Stream Z, which involves two separate moves",
     "All four, since each involves at least one move"],
   ans=0,
   why="Only one stream records more than two moves and an ascending sequence of settlement sizes, which is what step migration means. A single long move is not step migration however far it goes, and a move out and back is a return rather than an ascent."),
]
