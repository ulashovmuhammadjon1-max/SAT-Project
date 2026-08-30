# AP HUMAN GEOGRAPHY 4.5 The Function of Political Boundaries -- 30 questions
# CED Course Framework V.1, Unit 4. Enduring understanding IMP-4, "Political
# boundaries and divisions of governance, between states and within them,
# reflect balances of power that have been negotiated or imposed." Learning
# objective IMP-4.B, "Explain the nature and function of international and
# internal boundaries."
#
# Essential knowledge for THIS topic (IMP-4.B.5 belongs to 4.6):
#   IMP-4.B.1  Boundaries are defined, delimited, demarcated, and administered
#              to establish limits of sovereignty, but they are often contested.
#   IMP-4.B.2  Political boundaries often coincide with cultural, national, or
#              economic divisions. However, some boundaries are created by
#              demilitarized zones or policy, such as the Berlin Conference.
#   IMP-4.B.3  Land and maritime boundaries and international agreements can
#              influence national or regional identity and encourage or
#              discourage international or internal interactions and disputes
#              over resources.
#   IMP-4.B.4  The United Nations Convention on the Law of the Sea defines the
#              rights and responsibilities of nations in the use of
#              international waters, established territorial seas, and
#              exclusive economic zones.
#
# TOPIC 4.4 (already built) classifies boundaries by ORIGIN -- antecedent,
# subsequent, superimposed, relict, geometric, consequent. This topic is about
# what a boundary DOES, which is a different question, and no item here asks a
# student to name a boundary type.
#
# IMP-4.B.1's four verbs are a sequence and the CED prints them in order:
#   defined      the boundary is set out in a legal document or treaty
#   delimited    it is drawn on a map
#   demarcated   it is physically marked on the ground with posts, fences, walls
#   administered it is managed and enforced -- customs, patrols, crossings
# The last clause of the same sentence is examinable too: boundaries are OFTEN
# CONTESTED, so completing all four steps does not settle a boundary.
#
# IMP-4.B.4 names the Law of the Sea convention. The zones it establishes are
# standard, uncontested course content and are used at that level only:
#   territorial sea      up to 12 nautical miles from the baseline; the coastal
#                        state has sovereignty here, subject to innocent passage
#   contiguous zone      to 24 nautical miles; limited enforcement powers
#   exclusive economic zone  to 200 nautical miles; the coastal state holds the
#                        rights to resources, NOT sovereignty over the water
#   high seas            beyond, open to all states
# The distinction between SOVEREIGNTY in the territorial sea and RESOURCE RIGHTS
# in the exclusive economic zone is the one students collapse, and items 12, 16,
# 20 and 28 turn on it.
#
# A terminology constraint the checker enforces: geo_check treats "exclusive
# economic zone" and "EEZ" as one construct, and likewise the convention's full
# name and its acronym, so no question offers both forms as separate options.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("4.5", "The Function of Political Boundaries", 4)

QUESTIONS = [
 dict(q="According to the framework, what is the purpose for which boundaries are defined, delimited, demarcated, and administered?", choices=[
   "To establish the limits of sovereignty",
   "To mark the limits of a language region",
   "To divide land among private owners",
   "To record the physical geography of a region",
   "To determine which climate zone a place belongs to"], ans=0,
   why="EK IMP-4.B.1 states that boundaries are defined, delimited, demarcated and administered to establish limits of sovereignty. The four steps are procedural stages, and the purpose the sentence attaches to all of them is a statement about where one state's authority stops."),

 dict(q="A treaty sets out in words where a boundary shall run, cartographers then draw it on an agreed map, surveyors set concrete pillars along it, and customs posts open at the crossings. Which sequence of terms describes these four actions?", choices=[
   "Defined, delimited, demarcated, and administered",
   "Delimited, defined, administered, and demarcated",
   "Demarcated, administered, defined, and delimited",
   "Administered, demarcated, delimited, and defined",
   "Defined, demarcated, administered, and delimited"], ans=0,
   why="EK IMP-4.B.1 prints the four verbs in this order and the scenario matches them one by one: a legal text, a map, physical markers on the ground, and then day-to-day management. Getting the order right is what shows the terms are understood as stages rather than as synonyms."),

 dict(q="Two states have completed every stage of establishing their common boundary, yet each publishes maps showing a different line in one sector. What does this illustrate?", choices=[
   "That boundaries are often contested even after they have been formally established",
   "That the boundary was never defined",
   "That one of the two states does not exist",
   "That boundaries cannot be drawn on maps",
   "That the sector belongs to neither state"], ans=0,
   why="EK IMP-4.B.1 ends by noting that boundaries are often contested, and it places that clause after the four establishment steps rather than before them. Completing the procedure creates a line that can be argued about precisely, not one that everyone accepts."),

 dict(q="A boundary runs along the division between two language communities, with speakers of one language almost entirely on one side. Which framework statement covers this?", choices=[
   "That political boundaries often coincide with cultural, national, or economic divisions",
   "That boundaries are created only by demilitarized zones",
   "That boundaries establish maritime resource rights",
   "That boundaries are always contested",
   "That boundaries determine which language people speak"], ans=0,
   why="EK IMP-4.B.2 states that political boundaries often coincide with cultural, national or economic divisions. A line matching a language divide is the cultural case, and the word 'coincide' leaves open whether the line followed the division or the division followed the line."),

 dict(q="A strip of territory between two states is demilitarized by agreement, and the edges of that strip now function as the effective boundary between them. Which framework statement covers this?", choices=[
   "That some boundaries are created by demilitarized zones",
   "That boundaries always coincide with cultural divisions",
   "That boundaries establish exclusive economic zones",
   "That boundaries are always drawn by conferences",
   "That demilitarized zones are not boundaries at all"], ans=0,
   why="EK IMP-4.B.2 says that although boundaries often coincide with cultural, national or economic divisions, some are created by demilitarized zones or policy. The 'however' in that sentence introduces exactly this case, in which the line records a military settlement rather than a social division."),

 dict(q="The Berlin Conference is named in the framework as an example of what?", choices=[
   "A boundary created by policy rather than by an existing cultural, national, or economic division",
   "A boundary created by a demilitarized zone",
   "A maritime boundary agreement",
   "A boundary that follows a language divide",
   "An internal boundary within one state"], ans=0,
   why="EK IMP-4.B.2 names the Berlin Conference alongside demilitarized zones as an example of boundaries created by policy rather than by coincidence with an existing division. Lines agreed at a conference table by parties who did not live there are the paradigm of that category."),

 dict(q="Which of the following would be evidence that a boundary is being ADMINISTERED, in the framework's sense, rather than merely demarcated?", choices=[
   "Staffed crossing points, customs inspection, and patrols managing who and what passes",
   "Concrete pillars set along the line at intervals",
   "A treaty text describing where the line runs",
   "A published map showing the agreed line",
   "A survey establishing coordinates for the line"], ans=0,
   why="EK IMP-4.B.1 lists administration as the last of four stages, after the line has been defined, mapped and marked. Pillars, texts, maps and surveys establish where the boundary is; administration is the ongoing work of making it operate."),

 dict(q="A newly agreed boundary is never physically marked because the terrain it crosses is remote and mountainous. Which stage has not been completed?", choices=[
   "Demarcation, the physical marking of the line on the ground",
   "Definition, the setting out of the line in a legal document",
   "Delimitation, the drawing of the line on a map",
   "Administration, the management of crossings",
   "None; a boundary requires no physical marking"], ans=0,
   why="EK IMP-4.B.1 names demarcation as a distinct step from definition and delimitation. A line can be legally settled and accurately mapped while no one has ever placed a marker on it, and unmarked boundaries are among the most often disputed on the ground."),

 dict(q="How does the framework say boundaries and international agreements can affect the way people think about where they live?", choices=[
   "They can influence national or regional identity",
   "They determine which language people speak",
   "They fix a region's physical geography",
   "They have no effect on identity",
   "They determine a region's climate"], ans=0,
   why="EK IMP-4.B.3 states that land and maritime boundaries and international agreements can influence national or regional identity. A line that separates people from a neighbour and joins them to a capital becomes part of how they describe themselves over time."),

 dict(q="A new border regime requires visas and inspections where crossing had previously been unrestricted, and trade between the two sides falls sharply. Which framework claim does this illustrate?", choices=[
   "That boundaries can discourage international interactions",
   "That boundaries always encourage interaction",
   "That boundaries have no economic effects",
   "That boundaries determine national identity alone",
   "That boundaries can only be changed by war"], ans=0,
   why="EK IMP-4.B.3 says boundaries and international agreements can encourage OR discourage international and internal interactions. Which direction they work in depends on how the boundary is administered, which is why the same line can be a channel in one decade and a barrier in the next."),

 dict(q="Two states share a boundary that crosses an oil field, and each claims the whole deposit. Which framework claim does this illustrate?", choices=[
   "That boundaries and international agreements can produce disputes over resources",
   "That boundaries always coincide with economic divisions",
   "That boundaries cannot cross resource deposits",
   "That resource disputes are unrelated to boundaries",
   "That the boundary must be relocated automatically"], ans=0,
   why="EK IMP-4.B.3 names disputes over resources among the things boundaries and agreements can produce. A deposit that spans a line makes the exact position of the line worth money, which converts a cartographic question into a political one."),

 dict(q="Under the Law of the Sea convention, what does a coastal state hold in its exclusive economic zone?", choices=[
   "Rights to the resources of the water and seabed, without full sovereignty over the waters themselves",
   "Full sovereignty equivalent to its land territory",
   "No rights of any kind",
   "The right to exclude all foreign vessels for any reason",
   "Only the right to regulate scientific research"], ans=0,
   why="EK IMP-4.B.4 says the convention defines rights and responsibilities in international waters and established both territorial seas and exclusive economic zones. The distinction the two zones draw is between sovereignty close to shore and resource rights further out, which is why foreign vessels may still navigate the latter."),

 dict(q="Which of the following best describes what the Law of the Sea convention does, according to the framework?", choices=[
   "It defines the rights and responsibilities of nations in the use of international waters and establishes maritime zones",
   "It abolishes all maritime boundaries",
   "It grants every state an equal share of the ocean",
   "It applies only to landlocked states",
   "It governs the use of rivers within states"], ans=0,
   why="EK IMP-4.B.4 states that the convention defines the rights and responsibilities of nations in the use of international waters and established territorial seas and exclusive economic zones. It is a framework of rules rather than an allocation of equal shares."),

 dict(q="A state's maritime claim overlaps with a neighbour's because the two coasts are less than 400 nautical miles apart. What does this situation most directly require?", choices=[
   "A negotiated or adjudicated division of the overlapping area between the two states",
   "The automatic award of the whole area to the larger state",
   "The abandonment of both claims",
   "The conversion of the area into high seas",
   "The relocation of one state's coastline"], ans=0,
   why="EK IMP-4.B.4 makes the convention a framework of rights and responsibilities rather than a self-executing map, and EK IMP-4.B.1's contestation clause applies at sea as on land. Where full zones would overlap, the states must agree a line or submit the question to a tribunal."),

 dict(q="A boundary that once separated hostile states is opened, checkpoints removed, and cross-border commuting becomes routine. Which framework claim does this illustrate?", choices=[
   "That boundaries can encourage international interactions as well as discourage them",
   "That boundaries are always barriers",
   "That the boundary has ceased to exist",
   "That the two states have merged",
   "That boundaries have no effect on daily life"], ans=0,
   why="EK IMP-4.B.3 states that boundaries and agreements can encourage or discourage interaction, naming both directions. The line still marks the limit of each state's sovereignty; what changed is how it is administered, which is the fourth of EK IMP-4.B.1's stages."),

 dict(q="Which statement correctly distinguishes a coastal state's territorial sea from its exclusive economic zone?", choices=[
   "The territorial sea is subject to the coastal state's sovereignty while the exclusive economic zone confers resource rights over a much wider area",
   "The exclusive economic zone is subject to sovereignty and the territorial sea confers only resource rights",
   "Both confer identical rights over identical areas",
   "Neither is recognized by international agreement",
   "The territorial sea is wider than the exclusive economic zone"], ans=0,
   why="EK IMP-4.B.4 names both zones as things the convention established, and the difference between them is the kind of authority each carries. Sovereignty applies near the coast while the wider zone grants rights to fish, minerals and energy without closing the water to navigation."),

 dict(q="A state builds a fence along a boundary that had previously been marked only by occasional stone pillars. Which stage of the boundary process is being strengthened?", choices=[
   "Demarcation, since the physical marking on the ground is being made continuous",
   "Definition, since the legal text is being rewritten",
   "Delimitation, since the map is being redrawn",
   "Administration, since the fence replaces customs officers",
   "None, since a fence is not a boundary feature"], ans=0,
   why="EK IMP-4.B.1 names demarcation as the physical marking of a boundary on the ground, and a continuous fence is a more emphatic version of a line of pillars. The legal text and the map are unchanged, and a fence supplements rather than replaces the work of administration."),

 dict(q="Which of the following boundaries would be LEAST likely to coincide with a cultural or economic division?", choices=[
   "A line agreed at an international conference by powers with no population on either side of it",
   "A line negotiated between two neighbouring communities",
   "A line following the edge of a language region",
   "A line separating two long-established trading zones",
   "A line agreed between two states after centuries of contact"], ans=0,
   why="EK IMP-4.B.2 says boundaries often coincide with cultural, national or economic divisions but that some are created by policy instead. A line drawn by parties with no local knowledge or interest has no mechanism by which it could match a division on the ground."),

 dict(q="A landlocked state negotiates guaranteed access to a neighbour's port. Which framework claim does this agreement illustrate?", choices=[
   "That international agreements can encourage interactions that boundaries would otherwise discourage",
   "That landlocked states have no boundaries",
   "That the convention on the law of the sea does not apply to any state",
   "That boundaries cannot be crossed by agreement",
   "That the landlocked state has acquired a coastline"], ans=0,
   why="EK IMP-4.B.3 names international agreements alongside boundaries as things that can encourage or discourage interaction. Being enclosed by other states' territory is a barrier that only an agreement can overcome, which is the clearest case of the encouraging direction."),

 dict(q="Two states dispute a maritime area that both claim as part of their exclusive economic zone. What is actually at stake?", choices=[
   "The rights to fish stocks, seabed minerals, and energy deposits in the disputed area",
   "Sovereignty over the water in the same sense as over land territory",
   "The right to prohibit all foreign shipping from the area",
   "The physical extent of each state's coastline",
   "Nothing, since the area is high seas"], ans=0,
   why="EK IMP-4.B.4 establishes exclusive economic zones as a category of right rather than of sovereignty, and EK IMP-4.B.3 names disputes over resources as a consequence of maritime boundaries. What the two states are arguing over is who may take what from the area."),

 dict(q="A boundary drawn by an outside power decades ago is now defended by the state it created as essential to its identity. What does this show?", choices=[
   "That boundaries can influence national identity over time regardless of how they originated",
   "That the boundary was never imposed",
   "That identity determines where boundaries are drawn",
   "That imposed boundaries are always rejected",
   "That boundaries have no relationship to identity"], ans=0,
   why="EK IMP-4.B.3 says boundaries can influence national or regional identity, and it attaches no condition about their origin. A line that shaped who governs, who is schooled together and who trades with whom becomes the container within which an identity forms."),

 dict(q="An internal boundary between two provinces of one state is being contested by the provincial governments. Which framework statement applies?", choices=[
   "That boundaries, internal as well as international, are often contested",
   "That only international boundaries can be contested",
   "That internal boundaries are not established by any process",
   "That internal boundaries carry no consequences",
   "That the state has ceased to be sovereign"], ans=0,
   why="EK IMP-4.B's learning objective covers international AND internal boundaries, and EK IMP-4.B.1's contestation clause is not limited to either. Provincial lines decide revenue, representation and jurisdiction, which is enough to make them worth arguing over."),

 dict(q="Which pairing correctly matches a boundary function to an example?", choices=[
   "Discouraging internal interaction, matched to an internal boundary at which goods are inspected and taxed",
   "Encouraging international interaction, matched to a militarized frontier closed to all crossing",
   "Establishing limits of sovereignty, matched to a line marking a change of soil type",
   "Producing resource disputes, matched to a boundary through uninhabited desert with no known deposits",
   "Influencing identity, matched to a survey line never published or marked"], ans=0,
   why="EK IMP-4.B.3 names encouraging and discouraging internal as well as international interaction among the effects of boundaries. Inspection and taxation at an internal line raise the cost of moving goods within one state, which is the discouraging case."),

 dict(q="Why does the framework treat a boundary as something more than a line on a map?", choices=[
   "Because it is established through a legal and physical process and then administered, and it produces effects on identity, interaction, and resources",
   "Because lines on maps are always inaccurate",
   "Because boundaries are physical features of the Earth",
   "Because boundaries cannot be mapped",
   "Because maps are not used by geographers"], ans=0,
   why="EK IMP-4.B.1 supplies the process and EK IMP-4.B.3 supplies the consequences, which together make a boundary an institution rather than a graphic. Delimitation is only the second of four stages, and the effects the CED names all follow from the stages after it."),

 dict(q="Which of the following is the strongest reason a boundary through a densely settled region is harder to administer than one through an empty one?", choices=[
   "Far more people, goods, and daily journeys cross it, so every function of the boundary must operate at much greater volume",
   "Settled regions have more difficult terrain",
   "Empty regions cannot be surveyed",
   "Boundaries through settled regions cannot be defined",
   "Settled regions have no economic activity"], ans=0,
   why="EK IMP-4.B.1 makes administration the ongoing management of a boundary, and its burden scales with the traffic across it. A line through an empty desert may be legally identical and practically trivial, which is why demarcation and administration are separate stages."),

 dict(q="Four stages in establishing one boundary are recorded with the years they were completed. Using the accompanying record, which stage remains outstanding?",
   table=dict(headers=["Stage", "Year completed"],
     rows=[["Defined by treaty", "1904"],
           ["Delimited on an agreed map", "1907"],
           ["Demarcated with physical markers", "Not completed"],
           ["Administered with staffed crossings", "1912"]]),
   choices=[
   "Demarcation, which is the only stage the record shows as incomplete",
   "Definition, which was completed first",
   "Delimitation, which followed definition",
   "Administration, which was completed last",
   "None, since all four stages carry a year"], ans=0,
   why="EK IMP-4.B.1 lists four stages and the record marks exactly one of them as not completed, while the other three carry years. That a boundary can be administered without ever having been physically marked is what makes the four stages genuinely separate."),

 dict(q="Four boundary segments are recorded with what they coincide with and how they arose. Using the accompanying record, how many segments were created by policy rather than by an existing division?",
   table=dict(headers=["Segment", "Coincides with", "Origin"],
     rows=[["Segment 1", "A language divide", "Negotiated locally"],
           ["Segment 2", "Nothing on the ground", "Agreed at an international conference"],
           ["Segment 3", "A trading region's edge", "Negotiated locally"],
           ["Segment 4", "Nothing on the ground", "Fixed by an armistice line"]]),
   choices=[
   "Two segments, since two coincide with no division on the ground and arose from a conference and an armistice",
   "One segment, since only a conference creates a boundary by policy",
   "Three segments, since only one follows a language divide",
   "All four segments, since every boundary is a policy decision",
   "No segments, since all boundaries coincide with something"], ans=0,
   why="EK IMP-4.B.2 says boundaries often coincide with cultural, national or economic divisions but that some are created by demilitarized zones or policy. Exactly two of the four segments match nothing on the ground, and their origins are the two the statement names."),

 dict(q="Distances from a coastline are recorded for four points at sea. Using the accompanying figures and the zones the Law of the Sea convention established, in which zone does the coastal state hold resource rights but not sovereignty?",
   table=dict(headers=["Point", "Distance from baseline (nautical miles)"],
     rows=[["Point 1", "6"],
           ["Point 2", "10"],
           ["Point 3", "140"],
           ["Point 4", "320"]]),
   choices=[
   "Point 3, at 140 nautical miles, which lies beyond the territorial sea but within the exclusive economic zone",
   "Point 1, at 6 nautical miles, which lies within the territorial sea",
   "Point 2, at 10 nautical miles, which lies within the territorial sea",
   "Point 4, at 320 nautical miles, which lies on the high seas",
   "All four points, since the convention treats the whole sea alike"], ans=0,
   why="EK IMP-4.B.4 names territorial seas and exclusive economic zones as separate categories the convention established, and they differ in the kind of authority they carry. Only one of the four points lies past the 12-mile territorial sea and inside the 200-mile resource zone, which is where rights exist without sovereignty."),

 dict(q="A state's government argues that its boundaries should be redrawn to match the distribution of one ethnic group. Which two framework ideas does this argument engage?", choices=[
   "The claim that boundaries often coincide with cultural divisions, and the claim that they are often contested",
   "The four stages of establishing a boundary only",
   "The convention on the law of the sea only",
   "Neither idea, since ethnicity is not a geographic variable",
   "The claim that boundaries determine climate"], ans=0,
   why="EK IMP-4.B.2 makes coincidence with cultural divisions a common property of boundaries rather than a requirement, and EK IMP-4.B.1 records that boundaries are often contested. An argument that a line SHOULD match a distribution is a contest about the line conducted in the vocabulary of coincidence."),

 dict(q="Which is the most defensible summary of what political boundaries do, given all four of this topic's essential knowledge statements?", choices=[
   "They mark the limits of sovereignty through a legal and physical process, shape identity and interaction, allocate maritime rights, and remain frequently contested",
   "They only mark where one country stops and another begins",
   "They have no effects beyond administration",
   "They exist only at sea",
   "They are determined entirely by physical geography"], ans=0,
   why="EK IMP-4.B.1 supplies the process and the contestation, EK IMP-4.B.2 the coincidence with divisions, EK IMP-4.B.3 the effects on identity, interaction and resources, and EK IMP-4.B.4 the maritime allocation. A summary keeping all four is what the statements together assert."),
]
