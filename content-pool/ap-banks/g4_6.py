# AP HUMAN GEOGRAPHY 4.6 Internal Boundaries -- 30 questions
# CED Course Framework V.1, Unit 4. Enduring understanding IMP-4; learning
# objective IMP-4.B, "Explain the nature and function of international and
# internal boundaries."
#
# Essential knowledge for THIS topic -- one statement:
#   IMP-4.B.5  Voting districts, redistricting, and gerrymandering affect
#              election results at various scales.
#
# Three terms and one claim. The claim is the examinable part: internal
# boundaries CHANGE OUTCOMES. Where the lines are drawn decides how a fixed set
# of votes converts into a set of seats, which is why the same electorate can
# produce opposite results under two different maps. Items 9, 13, 18, 22, 26 and
# 29 rest on that, and items 26 and 29 prove it with tables rather than
# asserting it.
#
# The three terms, defined here because the CED defines none of them:
#   voting district  the area whose residents elect one representative; also
#                    called an electoral district or constituency
#   redistricting    redrawing those areas, usually after a census has shown
#                    that population has moved between them
#   gerrymandering   drawing them deliberately so as to advantage one party,
#                    candidate or group
#
# The two techniques of gerrymandering are standard course content rather than
# CED text, and are used throughout with these meanings:
#   packing   concentrating opposing voters into a few districts they win by
#             enormous margins, so their surplus votes elect nobody
#   cracking  splitting opposing voters across many districts so that they are
#             a minority in each and win none
# The two are opposites in method and identical in purpose, which is what items
# 6, 7, 8, 20 and 26 are built on.
#
# ONE FURTHER DISTINCTION, because students merge them: REDISTRICTING is drawing
# the lines and is done routinely and lawfully; GERRYMANDERING is drawing them
# for advantage. Every gerrymander is a redistricting and most redistricting is
# not a gerrymander. Item 3 asks for exactly that relationship.
#
# MALAPPORTIONMENT -- districts of very unequal population, so that a vote is
# worth more in one than in another -- is a separate defect from gerrymandering
# and can exist without it. Items 12, 21 and 27 keep them apart.
#
# THE ITEMS ARE ABOUT MECHANISM, NOT PARTISANSHIP. No question names a real
# party or asks which side benefits in any real country, because that is not a
# question a key could defend. Groups are named neutrally throughout.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("4.6", "Internal Boundaries", 4)

QUESTIONS = [
 dict(q="What does the framework say voting districts, redistricting, and gerrymandering do?", choices=[
   "They affect election results at various scales",
   "They determine which citizens may vote",
   "They set the boundaries between states",
   "They decide how many political parties may exist",
   "They have no measurable effect on outcomes"], ans=0,
   why="EK IMP-4.B.5 states that voting districts, redistricting and gerrymandering affect election results at various scales. The claim is about outcomes rather than about eligibility, and the phrase about scales is what places it in a geography course."),

 dict(q="A voting district is best defined as", choices=[
   "The area whose residents elect one representative",
   "The area in which a party has the most support",
   "The boundary between two countries",
   "The area a government administers directly",
   "The area within which people may campaign"], ans=0,
   why="EK IMP-4.B.5 names voting districts without defining them, and the standard definition is the geographic unit from which a representative is chosen. Because the unit is geographic, moving its boundary changes which voters are counted together."),

 dict(q="What is the relationship between redistricting and gerrymandering?", choices=[
   "Every gerrymander is a redistricting, but most redistricting is not a gerrymander",
   "The two words mean exactly the same thing",
   "Redistricting is illegal and gerrymandering is lawful",
   "Gerrymandering happens before redistricting",
   "Neither has any effect on election results"], ans=0,
   why="EK IMP-4.B.5 names both terms separately, which implies they are not identical. Redistricting is the routine act of redrawing lines after population shifts; gerrymandering is doing so with the intention of producing a particular result."),

 dict(q="Why is redistricting normally carried out after a census?", choices=[
   "Population moves between districts, so equal representation requires the lines to be adjusted to the new distribution",
   "Censuses are required to identify each voter's party",
   "The law requires a new map every year",
   "Districts wear out and must be replaced",
   "Census data are the only maps available"], ans=0,
   why="EK IMP-4.B.5 names redistricting as one of the three things affecting election results. A district that has gained or lost population relative to its neighbours no longer represents an equal number of people, and a count is what reveals the imbalance."),

 dict(q="Gerrymandering is best defined as", choices=[
   "Drawing voting district boundaries deliberately so as to advantage a particular party, candidate, or group",
   "Redrawing district boundaries after a census",
   "Preventing certain citizens from voting",
   "Counting votes incorrectly",
   "Holding an election at an unusual time"], ans=0,
   why="EK IMP-4.B.5 names gerrymandering alongside redistricting and voting districts as things affecting election results. The distinguishing feature is intent: the same act of drawing lines becomes a gerrymander when the purpose is advantage rather than equality."),

 dict(q="A map concentrates almost all of one group's supporters into two districts, which that group wins with more than 90 percent of the vote, while the group narrowly loses every other district. Which technique is this?", choices=[
   "Packing, since the group's supporters are concentrated so that their surplus votes elect nobody",
   "Cracking, since the group is spread thinly",
   "Malapportionment, since the districts differ in population",
   "Reapportionment, since seats have been reallocated",
   "No technique at all, since the group won two districts"], ans=0,
   why="Packing concentrates opposing voters into a small number of districts they win overwhelmingly, so the votes above the winning margin are wasted. EK IMP-4.B.5 makes gerrymandering a way of affecting election results, and this is one of its two standard methods."),

 dict(q="A map divides a group's supporters among six districts so that they form about 30 percent of the electorate in each and win none. Which technique is this?", choices=[
   "Cracking, since the group is split so that it is a minority everywhere",
   "Packing, since the group is concentrated",
   "Malapportionment, since the districts are unequal",
   "Redistricting without any partisan intent",
   "No technique, since 30 percent is a substantial share"], ans=0,
   why="Cracking splits a group across many districts so it is a majority in none, which converts a substantial minority into no seats at all. It is the opposite method from packing and serves exactly the same purpose."),

 dict(q="What do packing and cracking have in common?", choices=[
   "Both waste an opposing group's votes so that its share of seats falls below its share of the vote",
   "Both concentrate an opposing group into one district",
   "Both spread an opposing group across many districts",
   "Both increase the number of seats a group wins",
   "Both require districts of unequal population"], ans=0,
   why="The two techniques are opposite in method and identical in purpose. A vote cast for a losing candidate elects nobody and so does a vote cast for a winner far beyond the margin needed, and EK IMP-4.B.5's claim that gerrymandering affects results is exactly this arithmetic."),

 dict(q="A group wins 55 percent of the votes cast across a region but holds only 40 percent of its seats. What is the most likely explanation?", choices=[
   "The distribution of its supporters among the districts converts its votes into seats inefficiently, whether by design or not",
   "Some of its votes were not counted",
   "The region has too few districts",
   "The group's supporters did not vote",
   "Seats are allocated by population rather than by votes"], ans=0,
   why="EK IMP-4.B.5 states that voting districts and how they are drawn affect election results. A seat share below a vote share means the group's votes are concentrated where they are not needed or dispersed where they are not enough, which is what district geography determines."),

 dict(q="Which of the following would a geographer take as a warning sign of gerrymandering in a district map?", choices=[
   "Districts of extremely irregular shape that split towns and neighbourhoods without any geographic reason",
   "Districts of roughly equal population",
   "Districts that follow county boundaries",
   "Districts drawn by an independent commission",
   "Districts that are compact and contiguous"], ans=0,
   why="EK IMP-4.B.5 names gerrymandering as an influence on results, and shape is the most visible symptom because achieving a target outcome usually requires abandoning natural units. Compactness, contiguity and respect for existing boundaries are what a map drawn without a target tends to produce."),

 dict(q="Why does the framework say these processes affect election results 'at various scales'?", choices=[
   "District drawing operates for municipal wards, provincial constituencies, and national legislatures alike",
   "Because only national elections are affected",
   "Because only local elections are affected",
   "Because scale has no bearing on elections",
   "Because districts exist only in large countries"], ans=0,
   why="EK IMP-4.B.5 ends with the phrase 'at various scales', which generalizes the claim beyond national legislatures. A city council ward and a national constituency are drawn by the same kind of decision and are open to the same kinds of manipulation."),

 dict(q="One district contains 20,000 voters and another in the same legislature contains 140,000, and each elects one representative. What is this defect called, and how does it differ from gerrymandering?", choices=[
   "Malapportionment, which makes votes unequal in weight and can exist even where no map was drawn for advantage",
   "Gerrymandering, since the districts are unequal",
   "Cracking, since voters are divided",
   "Packing, since voters are concentrated",
   "No defect, since each district elects one representative"], ans=0,
   why="Unequal district populations make one voter's ballot worth seven of another's, which is a defect of size rather than of shape. It commonly arises from failing to redistrict as population moves, so it can exist with no intent to advantage anyone."),

 dict(q="Two different district maps are drawn for the same region using the same voter data, and they produce different numbers of seats for each group. What does this demonstrate?", choices=[
   "That the conversion of votes into seats depends on where the lines are drawn, not only on how people vote",
   "That some voters were counted twice",
   "That one of the two maps must be arithmetically wrong",
   "That the voters changed their minds",
   "That district maps cannot affect results"], ans=0,
   why="EK IMP-4.B.5 states that voting districts and redistricting affect election results, and holding the votes constant while varying the map is the cleanest possible demonstration. The difference in outcome can only come from the boundaries."),

 dict(q="An independent commission, rather than the legislature itself, is given the task of drawing district boundaries. What is the reasoning behind this arrangement?", choices=[
   "Legislators drawing the districts they are elected from have an interest in the outcome, which a body without that interest does not",
   "Commissions can draw maps faster",
   "Commissions are not required to use census data",
   "Legislators are not permitted to see maps",
   "Commissions can create more districts"], ans=0,
   why="EK IMP-4.B.5 makes gerrymandering a real influence on results, which is what creates the conflict of interest. The design response is to move the decision to a body whose members' seats do not depend on the map they draw."),

 dict(q="Which of the following is a legitimate criterion commonly used in drawing voting districts?", choices=[
   "Keeping districts compact, contiguous, and as far as possible respectful of existing communities and administrative units",
   "Ensuring one party wins a majority of districts",
   "Placing all of one group's supporters in a single district",
   "Making district populations as unequal as possible",
   "Drawing the districts before the census is taken"], ans=0,
   why="EK IMP-4.B.5's gerrymandering is defined against something, and the something is a set of neutral criteria. Compactness, contiguity, equal population and respect for existing communities are the standard tests, and none of them refers to how anyone votes."),

 dict(q="A region's population grows unevenly for thirty years and no redistricting is carried out. What is the consequence?", choices=[
   "Districts drift far apart in population, so voters in the fastest-growing districts become progressively under-represented",
   "The districts automatically adjust to the new population",
   "Elections cannot be held at all",
   "Every district gains an extra representative",
   "The consequence is confined to the largest district"], ans=0,
   why="EK IMP-4.B.5 names redistricting as one of the processes affecting results, and failing to do it is itself a decision with consequences. A district whose population has doubled still elects one member, so each of its voters holds half the influence of a voter in a district that did not grow."),

 dict(q="Which statement about the geography of a group's supporters is most accurate?", choices=[
   "A group whose supporters are heavily concentrated in a few areas can win fewer seats than a group with the same total votes spread more evenly",
   "Concentration always produces more seats",
   "Dispersal always produces more seats",
   "The spatial distribution of supporters has no effect on seats",
   "Only the total number of votes matters"], ans=0,
   why="Seats are won district by district, so votes beyond the margin needed in a safe district elect nobody. That is why a group's spatial distribution matters independently of its total support, and why concentration can be a disadvantage under this kind of system."),

 dict(q="An internal boundary is redrawn so that a fast-growing suburb is moved from one district to another. Which framework claim does this illustrate?", choices=[
   "That redistricting affects election results, since the same voters now help decide a different contest",
   "That internal boundaries have no political consequences",
   "That the suburb has left the country",
   "That the suburb's residents have lost the vote",
   "That international boundaries have changed"], ans=0,
   why="EK IMP-4.B.5 states that redistricting affects election results. Moving a bloc of voters from one district to another changes the balance in both districts at once, which is why the placement of a single suburb can be fought over."),

 dict(q="Which of the following is NOT one of the three things the framework names in this topic?", choices=[
   "Supranational organizations",
   "Voting districts",
   "Redistricting",
   "Gerrymandering",
   "Election results"], ans=0,
   why="EK IMP-4.B.5 names voting districts, redistricting and gerrymandering, and states that they affect election results. Supranational organizations belong to Topic 4.9's statement about challenges to sovereignty, not to this one about internal boundaries."),

 dict(q="A group with 45 percent of a region's votes is packed into districts where it wins 85 percent. What happens to the votes above the margin it needed?", choices=[
   "They elect no additional representative, so they are wasted in exactly the way packing is designed to achieve",
   "They are transferred to another district",
   "They elect a second representative in the same district",
   "They are added to the group's total in the next election",
   "They cause the district to be redrawn automatically"], ans=0,
   why="A district elects one representative regardless of the winning margin, so a vote beyond the threshold changes nothing. Packing works precisely because surplus votes are as wasted as losing ones, which EK IMP-4.B.5's claim about affected results depends on."),

 dict(q="A country requires that all districts be within a few percent of the same population but places no restriction on their shape. Which problem does this rule address, and which does it leave open?", choices=[
   "It addresses malapportionment but leaves gerrymandering by shape entirely available",
   "It addresses gerrymandering but leaves malapportionment available",
   "It addresses both problems completely",
   "It addresses neither problem",
   "It makes districts unnecessary"], ans=0,
   why="Equal population is a constraint on size and says nothing about which voters are placed together. A map can satisfy an equal-population rule exactly while pursuing any partisan target at all, which is why compactness rules are treated as a separate safeguard."),

 dict(q="Which is the strongest reason internal boundaries deserve as much attention from geographers as international ones?", choices=[
   "They determine how a population's preferences are converted into political power, which is one of the largest consequences a line can have",
   "They are longer in total than international boundaries",
   "They are more expensive to survey",
   "They are visible from the air",
   "They change more slowly than international boundaries"], ans=0,
   why="EK IMP-4.B.5 places these lines inside a learning objective that covers international AND internal boundaries, and it attaches an effect on election results to them. A line that decides who governs is doing political work of the same order as a state border."),

 dict(q="A map is drawn to create a district in which a previously under-represented minority forms a majority and can elect a representative of its choice. How should this be described?", choices=[
   "A deliberate use of district drawing whose purpose is representation rather than partisan advantage, which is why it is judged differently from a gerrymander",
   "A gerrymander identical in every respect to a partisan one",
   "Malapportionment",
   "Cracking",
   "An accident of the census"], ans=0,
   why="EK IMP-4.B.5 makes district drawing an influence on results without saying that every deliberate use of it is illegitimate. The purpose is what distinguishes the cases, and drawing to enable representation is a different purpose from drawing to entrench a party."),

 dict(q="Why can two experts examine the same district map and disagree about whether it is a gerrymander?", choices=[
   "Gerrymandering is defined by intent, and intent must be inferred from shape, outcome, and the process that produced the map",
   "Because maps cannot be measured",
   "Because election results are never published",
   "Because the term has no meaning",
   "Because district populations cannot be counted"], ans=0,
   why="EK IMP-4.B.5 names gerrymandering without supplying a test for it, and the distinguishing feature is purpose rather than any measurable property. A very irregular map can have an innocent explanation and a tidy one can have been drawn to a target."),

 dict(q="Which combination would produce the largest gap between a group's share of votes and its share of seats?", choices=[
   "A map that packs the group's strongest areas into a few districts and cracks the remainder across many",
   "A map with compact districts of equal population",
   "A map drawn by an independent commission",
   "A map following existing administrative units",
   "A map redrawn after every census"], ans=0,
   why="The two techniques are complementary rather than alternative: packing wastes surplus votes and cracking wastes losing ones, and applying both to the same group wastes as many of its votes as possible. EK IMP-4.B.5's claim that gerrymandering affects results is at its maximum here."),

 dict(q="Votes in five equally sized districts are recorded. Using the accompanying figures, how many seats does Group X win, and what share of the vote did it receive?",
   table=dict(headers=["District", "Votes for Group X", "Votes for Group Y"],
     rows=[["District 1", "9,500", "500"],
           ["District 2", "9,000", "1,000"],
           ["District 3", "4,000", "6,000"],
           ["District 4", "3,800", "6,200"],
           ["District 5", "3,700", "6,300"]]),
   choices=[
   "Two seats with 60 percent of the vote, since its supporters are concentrated in districts it wins overwhelmingly",
   "Three seats with 60 percent of the vote",
   "Two seats with 40 percent of the vote",
   "Five seats, since it has the most votes overall",
   "No seats, since it loses three districts"], ans=0,
   why="Group X takes 30,000 of the 50,000 votes cast, which is 60 percent, and wins the first two districts by more than nine to one while losing the other three narrowly. Sixty percent of the votes converting into forty percent of the seats is what packing produces."),

 dict(q="Registered voters are recorded for four districts, each of which elects one representative. Using the accompanying figures, how much more is a vote worth in the smallest district than in the largest?",
   table=dict(headers=["District", "Registered voters"],
     rows=[["District A", "20,000"],
           ["District B", "60,000"],
           ["District C", "100,000"],
           ["District D", "140,000"]]),
   choices=[
   "Seven times as much, since one representative is elected by 20,000 voters in one district and by 140,000 in the other",
   "Twice as much, since the districts differ in size",
   "Four times as much, since there are four districts",
   "The same, since each district elects one representative",
   "It cannot be compared, since the districts differ"], ans=0,
   why="Dividing the largest district by the smallest gives 140,000 over 20,000, so a ballot in the smallest carries seven times the weight in choosing a representative. This is malapportionment, a defect of unequal size rather than of shape, and it needs no partisan intent to arise."),

 dict(q="A group's share of the electorate is recorded district by district under two proposed maps covering the same equally sized districts. Using the accompanying figures, what do the two maps show?",
   table=dict(headers=["District", "Group A share under Map 1 (%)", "Group A share under Map 2 (%)"],
     rows=[["District 1", "30", "100"],
           ["District 2", "30", "12.5"],
           ["District 3", "30", "12.5"],
           ["District 4", "30", "12.5"],
           ["District 5", "30", "12.5"]]),
   choices=[
   "The same 30 percent of voters wins no seats under one map and one seat under the other, so the boundaries alone decide the outcome",
   "Group A wins more votes under Map 2 than under Map 1",
   "Group A wins three seats under Map 1",
   "The two maps produce identical results",
   "Group A wins no seats under either map"], ans=0,
   why="Both maps average to 30 percent across five equal districts, so the group's total support is identical, yet it is a minority in all five districts under one map and a unanimous majority in one district under the other. EK IMP-4.B.5's claim that districts affect results is exactly this."),

 dict(q="A legislature draws its own district boundaries and the governing party holds a comfortable majority. Which safeguard would most directly address the resulting conflict of interest?", choices=[
   "Transferring the drawing of boundaries to a body whose members do not stand for election in those districts",
   "Increasing the number of districts",
   "Holding elections more frequently",
   "Publishing the election results sooner",
   "Reducing the number of political parties"], ans=0,
   why="EK IMP-4.B.5 makes gerrymandering a real influence on election results, which means the people drawing the lines are choosing part of their own electorate. Removing the decision from those with a stake in it addresses the cause rather than the symptom."),

 dict(q="Which is the most defensible summary of this topic's essential knowledge?", choices=[
   "Where internal electoral lines are drawn converts a fixed set of votes into a set of seats, so the map is part of the result at every scale of election",
   "Internal boundaries are administrative details with no political consequences",
   "Only the number of votes cast determines an election result",
   "Gerrymandering occurs only in national elections",
   "District boundaries cannot be changed once drawn"], ans=0,
   why="EK IMP-4.B.5 states that voting districts, redistricting and gerrymandering affect election results at various scales, which is a claim about mechanism and about generality at once. Treating the map as part of the result rather than as its container is what the statement asks students to understand."),
]
