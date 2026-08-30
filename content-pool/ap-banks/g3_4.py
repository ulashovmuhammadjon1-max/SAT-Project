# AP HUMAN GEOGRAPHY 3.4 Types of Diffusion -- 30 questions
# CED Course Framework V.1, Unit 3. Enduring understanding IMP-3, "The
# interaction of people contributes to the spread of cultural practices."
# Learning objective IMP-3.A, "Define the types of diffusion."
#
# Essential knowledge -- one statement, and it is the whole typology:
#   IMP-3.A.1  Relocation and expansion -- including contagious, hierarchical,
#              and stimulus expansion -- are types of diffusion.
#
# The sentence has a structure that a flat list would hide, and the structure is
# the examinable content:
#
#   DIFFUSION
#     |
#     +-- RELOCATION      the trait travels because PEOPLE travel; it leaves the
#     |                   hearth with them and may weaken or vanish there
#     |
#     +-- EXPANSION       the trait spreads outward while REMAINING at the
#          |              source, often strengthening there
#          |
#          +-- CONTAGIOUS    spread by direct contact, outward from the source
#          |                 more or less uniformly; strongly distance-dependent,
#          |                 so nearby places adopt before distant ones
#          |
#          +-- HIERARCHICAL  spread from larger or more influential places or
#          |                 people to smaller or less influential ones, SKIPPING
#          |                 the countryside in between; weakly distance-dependent
#          |
#          +-- STIMULUS      the specific trait does NOT take hold, but the
#                            underlying idea does and is adapted into a locally
#                            acceptable form
#
# The single test that separates relocation from every kind of expansion, and
# the reason items 2, 5, 9, 14 and 20 exist: does the trait REMAIN at the source
# after spreading? Expansion keeps it; relocation carries it away.
#
# The single test that separates contagious from hierarchical, and the reason
# items 6, 7, 16, 26 and 27 exist: does adoption follow DISTANCE or does it
# follow SIZE and RANK? Contagious spreads to the next place along; hierarchical
# jumps to the next big place and fills in later.
#
# Stimulus diffusion is the one students under-recognize, because nothing looks
# as though it has spread. What crossed was the idea; what appears at the
# destination is a local adaptation of it. Items 8, 13, 21, 25 and 30 test it.
#
# A note on terminology, enforced by the checker: this course treats
# "contagious" and "contagious expansion" as one name, and likewise for the
# other two subtypes, so no question offers both forms as separate options.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g3_4.py. FIVE choices (A-E).
TOPIC = ("3.4", "Types of Diffusion", 3)

QUESTIONS = [
 dict(q="Which types of diffusion does the framework name?",
   choices=[
     "Relocation and expansion, with expansion including contagious, hierarchical, and stimulus",
     "Contagious and hierarchical only",
     "Relocation and contagious only",
     "Expansion and migration",
     "Hierarchical, stimulus, and migration"],
   ans=0,
   why="EK IMP-3.A.1 names relocation and expansion as the two types and lists contagious, hierarchical and stimulus as kinds of expansion. The nesting matters: the three subtypes are all ways a trait can spread while remaining at its source."),

 dict(q="What single test best distinguishes relocation diffusion from expansion diffusion?",
   choices=[
     "Whether the trait remains at its source after spreading, which expansion preserves and relocation does not require",
     "Whether the trait spreads quickly or slowly",
     "Whether the trait is religious or economic",
     "Whether the trait crosses an international border",
     "Whether the trait spreads to cities or to rural areas"],
   ans=0,
   why="EK IMP-3.A.1 separates the two types at the top level, and the difference is mechanism: expansion spreads outward from a source that keeps the trait, while relocation carries the trait away with the people who hold it."),

 dict(q="A religious practice appears in a distant country because a community of believers emigrated there, and it continues at the hearth as well. Which type of diffusion moved it to the new country?",
   choices=[
     "Relocation diffusion, since the practice travelled with the people who carried it",
     "Contagious diffusion, since the practice spread by contact",
     "Hierarchical diffusion, since believers moved to a city",
     "Stimulus diffusion, since the practice was adapted",
     "No diffusion occurred, since the practice already existed"],
   ans=0,
   why="EK IMP-3.A.1 names relocation among the types of diffusion, and the mechanism here is physical movement of the people holding the trait. That the practice also survives at the hearth does not make the transfer an expansion, since nothing spread outward from the source to reach the new country."),

 dict(q="A fashion spreads from person to person through daily contact, reaching neighbouring towns before distant ones and eventually covering a whole region. This is",
   choices=[
     "Contagious diffusion, since spread follows direct contact and therefore distance",
     "Hierarchical diffusion, since the fashion reached many places",
     "Relocation diffusion, since people carried the fashion",
     "Stimulus diffusion, since the fashion changed as it spread",
     "Not diffusion, since fashions change constantly"],
   ans=0,
   why="EK IMP-3.A.1 lists contagious among the kinds of expansion diffusion. Its signature is that adoption falls off with distance from the source, because the mechanism is contact and contact is more likely between nearby people."),

 dict(q="A practice appears first in a country's three largest cities, then in provincial cities, then in towns, and only later in the countryside between them. This is",
   choices=[
     "Hierarchical diffusion, since spread follows the size and rank of places rather than distance",
     "Contagious diffusion, since the practice eventually reached everywhere",
     "Relocation diffusion, since city dwellers travel",
     "Stimulus diffusion, since the practice was modified",
     "Not diffusion, since cities always differ from countryside"],
   ans=0,
   why="EK IMP-3.A.1 names hierarchical among the kinds of expansion diffusion, and its diagnostic is that intervening rural areas are skipped. Adoption ordered by settlement size rather than by proximity is what identifies it."),

 dict(q="Which observation would distinguish contagious from hierarchical diffusion in a set of adoption dates?",
   choices=[
     "Whether adoption date correlates better with distance from the source or with the size of the adopting settlement",
     "Whether the practice is old or new",
     "Whether the practice spread within one country",
     "Whether the practice is cultural or economic",
     "Whether more than one place adopted the practice"],
   ans=0,
   why="EK IMP-3.A.1 lists both as kinds of expansion, so the difference is which variable orders the adoptions. Contagious spread is distance-ordered and hierarchical spread is rank-ordered, and comparing the two correlations is exactly how a geographer tells them apart."),

 dict(q="A society encounters a neighbouring people's script but does not adopt it. Instead it uses the idea of writing to devise a script of its own suited to its own language. This is",
   choices=[
     "Stimulus diffusion, since the underlying idea spread while the specific trait did not",
     "Contagious diffusion, since the two peoples were in contact",
     "Relocation diffusion, since scribes travelled",
     "Hierarchical diffusion, since scripts start in cities",
     "Not diffusion, since a new script was invented"],
   ans=0,
   why="EK IMP-3.A.1 names stimulus among the kinds of expansion diffusion. What crossed was the principle rather than the artifact, and the local version exists because of the encounter, which is what makes it diffusion rather than independent invention."),

 dict(q="Which statement about expansion diffusion is correct?",
   choices=[
     "The trait remains at its source and often strengthens there while also appearing in new places",
     "The trait disappears from its source as it spreads",
     "The trait spreads only through the physical movement of people",
     "The trait spreads only within a single country",
     "The trait must be modified in order to spread"],
   ans=0,
   why="EK IMP-3.A.1 treats expansion as one of the two top-level types, and the source retaining the trait is what separates it from relocation. All three subtypes share that property, which is why the CED nests them beneath it."),

 dict(q="A restaurant chain opens first in the largest metropolitan areas of several countries, then in second-tier cities, and only much later in small towns. Which type of diffusion is this?",
   choices=[
     "Hierarchical diffusion operating through the urban system",
     "Contagious diffusion, since the chain expanded outward",
     "Relocation diffusion, since staff move between branches",
     "Stimulus diffusion, since menus are adapted locally",
     "Not diffusion, since business expansion is an economic process"],
   ans=0,
   why="EK IMP-3.A.1 lists hierarchical among the kinds of expansion diffusion, and an ordering by metropolitan rank across several countries is its clearest form. That the process is commercial does not exempt it: a chain is a practice spreading between places."),

 dict(q="A crop variety spreads because farmers who tried it tell their immediate neighbours, who tell theirs, and adoption moves outward in a widening ring. This is",
   choices=[
     "Contagious diffusion, since each adoption comes from contact with a nearby adopter",
     "Hierarchical diffusion, since large farms adopt first",
     "Relocation diffusion, since seed is carried",
     "Stimulus diffusion, since the variety is adapted",
     "Not diffusion, since farmers make independent decisions"],
   ans=0,
   why="EK IMP-3.A.1 lists contagious among the kinds of expansion. A widening ring is the geometric signature of contact-based spread, since each new adopter can only be reached by someone already nearby."),

 dict(q="Why is relocation diffusion the type most closely tied to Unit 2's migration material?",
   choices=[
     "Its mechanism is the physical movement of people, so any migration stream is a potential diffusion channel",
     "It is the only type that involves culture",
     "It is the only type that crosses borders",
     "It is the only type that can be mapped",
     "It is not connected to migration at all"],
   ans=0,
   why="EK IMP-3.A.1 defines relocation by movement rather than by contact, which makes migrants the carriers. Every chain, step and transnational stream from Unit 2 is therefore also a route along which practices travel."),

 dict(q="A ritual observed in one region is adopted in a distant region in a substantially altered form that fits local beliefs, after traders described it. Which type is this?",
   choices=[
     "Stimulus diffusion, since the idea travelled and was reworked rather than reproduced",
     "Relocation diffusion, since traders moved",
     "Contagious diffusion, since traders had contact",
     "Hierarchical diffusion, since traders reached cities",
     "Not diffusion, since the two versions differ"],
   ans=0,
   why="EK IMP-3.A.1 names stimulus among the kinds of expansion diffusion, and the diagnostic is that the specific trait failed to take while its principle did. That traders were the channel identifies the route, not the type."),

 dict(q="A practice that had spread from a hearth to many other places dies out at the hearth itself but continues elsewhere. What does this tell us about the original diffusion?",
   choices=[
     "Nothing decisive, since a trait can be lost at its source long after it spread by either relocation or expansion",
     "That the diffusion must have been relocation",
     "That the diffusion must have been expansion",
     "That no diffusion ever occurred",
     "That the practice was invented independently elsewhere"],
   ans=0,
   why="The distinction in EK IMP-3.A.1 concerns the mechanism at the time of spread, not the fate of the source afterward. A hearth can lose a trait for reasons entirely unrelated to how the trait travelled, so the later disappearance is not evidence about the type."),

 dict(q="Which of the following is the clearest case of relocation diffusion?",
   choices=[
     "A cuisine appearing in a city because immigrants from a particular region settled there and cooked what they knew",
     "A song becoming popular in nearby towns through radio play",
     "A technology adopted first in capitals and later in provincial cities",
     "A design principle reworked into an unrecognizable local form",
     "A word entering a language through contact between neighbouring villages"],
   ans=0,
   why="EK IMP-3.A.1 names relocation as the type in which the trait moves with people. The other four options describe spread through contact, through the urban hierarchy, through adaptation of an idea, and through proximity, which are the expansion kinds."),

 dict(q="A disease spreads through a population by direct transmission between people who are physically near one another. Which diffusion type does this most resemble, and why is the analogy useful?",
   choices=[
     "Contagious diffusion, since the same distance-dependent contact mechanism describes both a pathogen and a practice",
     "Hierarchical diffusion, since diseases start in cities",
     "Relocation diffusion, since infected people move",
     "Stimulus diffusion, since diseases mutate",
     "No diffusion type applies, since disease is biological"],
   ans=0,
   why="EK IMP-3.A.1's contagious subtype takes its name from exactly this analogy. What the two share is the mechanism -- transmission requires proximity -- and that shared mechanism produces the same distance-decaying spatial pattern."),

 dict(q="Which pattern of adoption dates would be strongest evidence for HIERARCHICAL rather than contagious diffusion?",
   choices=[
     "A distant metropolis adopting years before a small town twenty kilometres from the source",
     "Every settlement within fifty kilometres adopting before any settlement beyond it",
     "All settlements adopting in the same year",
     "Adoption spreading outward in a smooth ring",
     "Adoption occurring only where people migrated"],
   ans=0,
   why="EK IMP-3.A.1 lists both subtypes, and hierarchical spread is identified by skipping: a far but important place adopts before a near but small one. A smooth outward ring and a distance-ordered sequence are both the contagious signature instead."),

 dict(q="Why does hierarchical diffusion often leave the countryside between adopting cities unchanged for years?",
   choices=[
     "The channels carrying the trait connect large places to one another rather than connecting each place to its neighbours",
     "Rural people are unable to adopt new practices",
     "Rural areas have no contact with cities",
     "The trait is physically unable to travel over farmland",
     "Rural areas adopt first and cities follow"],
   ans=0,
   why="EK IMP-3.A.1's hierarchical subtype spreads along a network ordered by rank, and a network of that kind links nodes rather than filling space. The gaps are a property of the channel, not of the people living in them."),

 dict(q="A practice diffuses from a hearth by two mechanisms at once: it spreads to neighbouring districts by contact, and it also appears in distant capitals through elite networks. How should this be described?",
   choices=[
     "Both contagious and hierarchical expansion are operating, since a single trait can travel by more than one channel",
     "Only contagious diffusion is occurring",
     "Only hierarchical diffusion is occurring",
     "This is relocation diffusion",
     "This cannot be diffusion, since the mechanisms differ"],
   ans=0,
   why="EK IMP-3.A.1's subtypes describe channels rather than mutually exclusive events, and nothing prevents a trait from using two. Recognising a mixed case is more accurate than forcing it into one category and losing half the pattern."),

 dict(q="Which of the following would NOT be diffusion at all?",
   choices=[
     "Two isolated societies with no contact developing similar tools independently",
     "A practice carried to a new country by migrants",
     "A practice spreading between neighbouring villages through contact",
     "A practice appearing in large cities first",
     "An idea adopted in a locally altered form after an encounter"],
   ans=0,
   why="EK IMP-3.A.1's types all describe a trait or an idea travelling from somewhere to somewhere else. Independent invention produces similarity without transmission, and similarity alone is not evidence that anything spread."),

 dict(q="A student says stimulus diffusion is 'when a practice changes a little as it spreads'. What is the correction?",
   choices=[
     "In stimulus diffusion the specific practice is not adopted at all; only the underlying idea crosses and is remade locally",
     "Stimulus diffusion means the practice spreads without changing",
     "Stimulus diffusion is a kind of relocation diffusion",
     "Stimulus diffusion occurs only between cities",
     "The student's definition is correct"],
   ans=0,
   why="EK IMP-3.A.1 lists stimulus as a distinct kind of expansion rather than as ordinary spread with minor variation. What distinguishes it is that the original trait was rejected or was unusable, while the principle behind it was kept."),

 dict(q="Why does the framework place contagious, hierarchical, and stimulus UNDER expansion rather than beside relocation?",
   choices=[
     "All three describe ways a trait spreads outward from a source that retains it, which is what expansion means",
     "All three are faster than relocation",
     "All three occur only in cities",
     "All three involve migration",
     "The placement is arbitrary"],
   ans=0,
   why="EK IMP-3.A.1 writes 'expansion -- including contagious, hierarchical, and stimulus expansion', which subordinates the three. What they share is that the source keeps the trait, and they differ only in which channel carries it outward."),

 dict(q="A language spreads across an empire as administrators, soldiers, and settlers move into new provinces. Which type predominates?",
   choices=[
     "Relocation diffusion, since the language travels in the mouths of people who move",
     "Contagious diffusion, since neighbours hear it",
     "Hierarchical diffusion, since administration is centralized",
     "Stimulus diffusion, since local languages borrow words",
     "No diffusion, since the empire imposed the language"],
   ans=0,
   why="EK IMP-3.A.1 defines relocation by the physical movement of the people carrying the trait, and settlement and garrisoning are exactly that. Subsequent local adoption by contact is a second, later process rather than the one that brought the language."),

 dict(q="Which factor most strongly SLOWS contagious diffusion in particular?",
   choices=[
     "Physical or social barriers that reduce ordinary contact between adjacent populations",
     "The absence of large cities",
     "A lack of written records",
     "The trait being economic rather than cultural",
     "A long distance between two capital cities"],
   ans=0,
   why="EK IMP-3.A.1's contagious subtype spreads by direct contact, so whatever interrupts contact interrupts the spread. City size and the distance between capitals bear on hierarchical spread instead, which travels between nodes rather than across intervening ground."),

 dict(q="A trait spreads rapidly worldwide through the internet, reaching users in many countries within days regardless of distance. How is this best classified?",
   choices=[
     "Expansion diffusion in which the usual distance friction is largely removed, so hierarchical patterns by influence replace distance-ordered ones",
     "Relocation diffusion, since users are in different countries",
     "Contagious diffusion in its classic distance-dependent form",
     "Not diffusion, since no physical movement occurred",
     "Stimulus diffusion, since content is remixed"],
   ans=0,
   why="EK IMP-3.A.1's expansion types are defined by mechanism rather than by medium, and the source keeps the trait here. What changes online is that proximity stops governing contact, so the ordering falls to prominence and connection instead of to distance."),

 dict(q="Which of the following is the best example of stimulus diffusion?",
   choices=[
     "A society that cannot keep the animal a foreign practice requires adopting the practice's purpose in a form using a local animal",
     "A society adopting a foreign practice unchanged",
     "A society rejecting a foreign practice entirely",
     "A society exporting its own practice to a neighbour",
     "A society adopting a practice brought by immigrants"],
   ans=0,
   why="EK IMP-3.A.1 names stimulus among the kinds of expansion diffusion, and its structure is rejection of the specific plus retention of the principle. Unchanged adoption is ordinary expansion, complete rejection is no diffusion, and immigrant carriage is relocation."),

 dict(q="Adoption dates for a new practice are shown by settlement. Using the table, which type of diffusion do the data indicate?",
   table=dict(
     headers=["Settlement", "Population", "Distance from source (km)", "Year of adoption"],
     rows=[
       ["Metropolis A", "4,200,000", "620", "1"],
       ["City B", "800,000", "310", "2"],
       ["Town C", "40,000", "45", "5"],
       ["Village D", "1,800", "18", "8"]]),
   choices=[
     "Hierarchical diffusion, since the largest and most distant settlement adopted first and the smallest and nearest adopted last",
     "Contagious diffusion, since the nearest settlement adopted first",
     "Relocation diffusion, since people moved between the settlements",
     "Stimulus diffusion, since the practice was adapted",
     "No pattern, since the settlements differ in several ways"],
   ans=0,
   why="Adoption order runs exactly opposite to distance and exactly with population: 4.2 million at 620 kilometres adopts in year 1 and 1,800 people at 18 kilometres adopt in year 8. Ordering by rank rather than by proximity is the hierarchical signature."),

 dict(q="Adoption dates for a different practice are shown. Using the table, which type of diffusion do these data indicate?",
   table=dict(
     headers=["Settlement", "Population", "Distance from source (km)", "Year of adoption"],
     rows=[
       ["Village P", "900", "8", "1"],
       ["Town Q", "22,000", "35", "2"],
       ["Village R", "1,400", "70", "3"],
       ["City S", "600,000", "150", "5"]]),
   choices=[
     "Contagious diffusion, since adoption follows distance from the source regardless of settlement size",
     "Hierarchical diffusion, since the largest settlement adopted last",
     "Relocation diffusion, since the practice moved between places",
     "Stimulus diffusion, since the practice varies locally",
     "No pattern, since two of the settlements are villages"],
   ans=0,
   why="Adoption order matches distance exactly -- 8, 35, 70 and 150 kilometres in years 1, 2, 3 and 5 -- while population runs 900, 22,000, 1,400 and 600,000, which is no order at all. Distance ordering with size ignored is the contagious signature."),

 dict(q="A trait's presence at its hearth and at three destinations is recorded before and after diffusion. Using the table, which type is indicated?",
   table=dict(
     headers=["Place", "Practitioners before", "Practitioners after"],
     rows=[
       ["Hearth region", "40,000", "58,000"],
       ["Destination 1", "0", "12,000"],
       ["Destination 2", "0", "7,500"],
       ["Destination 3", "0", "3,200"]]),
   choices=[
     "Expansion diffusion, since the practice grew at its source while also appearing in three new places",
     "Relocation diffusion, since the practice appeared in new places",
     "Relocation diffusion, since practitioners must have moved",
     "Stimulus diffusion, since the numbers differ between destinations",
     "No diffusion, since the hearth still has practitioners"],
   ans=0,
   why="The hearth rises from 40,000 to 58,000 practitioners while three destinations go from zero to 22,700 between them. A source that gains rather than loses while the trait appears elsewhere is the definition of expansion rather than relocation."),

 dict(q="Migration and the appearance of a cuisine are recorded for four cities. Using the table, what do the data indicate?",
   table=dict(
     headers=["City", "Migrants from the hearth region", "Restaurants serving the cuisine"],
     rows=[
       ["City 1", "84,000", "112"],
       ["City 2", "31,000", "44"],
       ["City 3", "9,000", "13"],
       ["City 4", "600", "1"]]),
   choices=[
     "Relocation diffusion, since the number of restaurants tracks the number of migrants across all four cities",
     "Contagious diffusion, since restaurants are close together",
     "Hierarchical diffusion, since large cities have more restaurants",
     "Stimulus diffusion, since menus are adapted",
     "No relationship, since the two columns measure different things"],
   ans=0,
   why="Restaurants per thousand migrants are 1.33, 1.42, 1.44 and 1.67, so the count tracks the migrant population closely across a range of nearly 140 to 1. EK IMP-3.A.1's relocation type is diffusion carried by people who move, which is what a proportional relationship to migrant numbers shows."),

 dict(q="Four societies' responses to an encountered practice are recorded. Using the table, which society's response is stimulus diffusion?",
   table=dict(
     headers=["Society", "Adopted the practice as encountered", "Adopted the underlying idea in an altered form", "Rejected it entirely"],
     rows=[
       ["Society W", "Yes", "No", "No"],
       ["Society X", "No", "Yes", "No"],
       ["Society Y", "No", "No", "Yes"],
       ["Society Z", "Yes", "No", "No"]]),
   choices=[
     "Society X, the only one that took the idea while declining the specific practice",
     "Society W, which adopted the practice as encountered",
     "Society Y, which rejected the practice",
     "Society Z, which adopted the practice as encountered",
     "All four, since each responded to the same encounter"],
   ans=0,
   why="Exactly one row records adoption of the underlying idea in an altered form together with non-adoption of the practice as encountered, which is the structure of stimulus diffusion. Two societies took the practice unchanged, which is ordinary expansion, and one took nothing, which is no diffusion at all."),
]
