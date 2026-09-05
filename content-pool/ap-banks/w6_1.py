# AP WORLD HISTORY: MODERN 6.1 Rationales for Imperialism from 1750 to 1900
# CED effective Fall 2026, Unit 6 Consequences of Industrialization, c. 1750 to
# c. 1900. Thematic focus CDI, Cultural Developments and Interactions: "The
# development of ideas, beliefs, and religions illustrates how groups in society
# view themselves, and the interactions of societies and their beliefs often have
# political, social, and cultural implications."
#
# Unit 6 Learning Objective A: "Explain how ideologies contributed to the
# development of imperialism from 1750 to 1900."
# Suggested skill 4.B, explain how a specific historical development or process is
# situated within a broader historical context.
#
# The single historical development this topic prints, in the framework's own words:
#   KC-5.2.III  A range of cultural, religious, and racial ideologies were used to
#               justify imperialism, including Social Darwinism, nationalism, the
#               concept of the civilizing mission, and the desire to religiously
#               convert indigenous populations.
#
# Two neighbouring statements are cited where an item explicitly reaches across a
# topic boundary, and nowhere else:
#   KC-5.3.III.D  Increasing questions about political authority and growing
#                 nationalism contributed to anticolonial movements. (topic 6.3)
#   KC-5.2.I.A    Some states with existing colonies strengthened their control over
#                 those colonies and in some cases assumed direct control over
#                 colonies previously held by non-state entities. (topic 6.2)
#
# WHAT THIS BANK DOES NOT DO. The framework NAMES four ideologies and defines none
# of them, exactly as the Comparative Government framework names seven data
# resources without defining them (see k1_1.py). Items that turn on what an
# ideology asserts therefore rest on the plainest sense of the named term -- the
# sense the framework presupposes by asking students to explain how these
# ideologies contributed to imperialism -- and no item asks for a date, a person, a
# treaty or a statistic the CED does not print. Where an item needs a source, the
# source is UNATTRIBUTED and labelled as illustrative: inventing a quotation and
# hanging a real name on it would be read by a student as fact.
#
# TABLES are labelled hypothetical in the stem and every keyed conclusion is
# recomputable from the table alone, so no item asks a student to remember a number.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md. Dates are written "1750 to 1900"; a
# hyphen between numerals is banned by the notation gate in es_check.py.
TOPIC = ("6.1", "Rationales for 1750 to 1900", 6)

_T_PAMPHLETS = dict(
    headers=["Argument made in the pamphlet",
             "Pamphlets containing it, sample of 40 from the 1830s (hypothetical)",
             "Pamphlets containing it, sample of 40 from the 1890s (hypothetical)"],
    rows=[["A duty to bring law, schooling and medicine to the governed", "18", "26"],
          ["A call to convert the population to the writer's religion", "22", "12"],
          ["A claim that colonies raise the nation's standing among rivals", "9", "28"],
          ["A claim that peoples struggle and the stronger displace the weaker", "3", "19"]])

_T_APPEALS = dict(
    headers=["Purpose stated in the fundraising appeal",
             "Share of appeals mentioning it (hypothetical, percent)"],
    rows=[["Converting the population to the society's religion", "84"],
          ["Opening schools", "61"],
          ["Providing medical care", "47"],
          ["Assisting merchants", "12"],
          ["Supporting military garrisons", "5"]])

QUESTIONS = [
 dict(q="An unattributed pamphlet published in an imperial capital during this period argues: 'The peoples of the earth are locked in a contest for survival. Those nations that do not expand will in time be displaced by those that do, and no sentiment can suspend that law.' Which of the ideologies the course framework names as a justification for imperialism does this argument most directly express?",
   choices=[
     "Social Darwinism, which transfers a struggle among species onto a struggle among peoples",
     "The concept of the civilizing mission, which promises improvement to the governed",
     "Nationalism, which measures a country by loyalty to its own language and traditions",
     "The desire to convert indigenous populations to the writer's religion",
     "A demand for the free movement of goods across borders without tariffs"], ans=0,
   why="KC-5.2.III names Social Darwinism among the cultural, religious and racial ideologies used to justify imperialism. The passage offers no benefit to the governed, no religious purpose and no tariff argument; it presents expansion as a law of survival among peoples, which is the Social Darwinist move."),
 dict(q="An illustrative colonial administrator's report from the period states: 'We hold this territory in trust. Our courts, our roads and our schools will in time raise its people to a condition in which they may govern themselves.' The rationale offered here is best identified as",
   choices=[
     "the concept of the civilizing mission",
     "Social Darwinism",
     "the desire to convert the population to a new religion",
     "national rivalry with a neighbouring empire",
     "the search for a market able to absorb surplus manufactures"], ans=0,
   why="KC-5.2.III names the concept of the civilizing mission among the justifications for imperialism. The report justifies rule by a claimed improvement of the governed and by their eventual fitness to govern themselves, and it says nothing about survival of the strong, about religion, about a rival or about markets."),
 dict(q="A newspaper editorial of the period, quoted here without attribution, tells its readers: 'Every great power is measured by the extent of its possessions. A country that acquires nothing will not be counted in the first rank of nations.' The editorial appeals most directly to",
   choices=[
     "nationalism, by making empire a measure of the nation's standing",
     "the civilizing mission, by promising benefits to the governed",
     "Social Darwinism, by describing peoples as biologically ranked",
     "religious conversion, by describing a duty to spread a faith",
     "a theory of free trade, by describing tariffs as an obstacle to wealth"], ans=0,
   why="KC-5.2.III names nationalism among the ideologies used to justify imperialism. The editorial's argument is entirely about the nation's rank among other nations and offers nothing about the governed, about biology, about faith or about tariffs."),
 dict(q="An unattributed missionary society circular of the period appeals for funds so that 'the Gospel may be carried to peoples who have never heard it, and their souls gathered in.' The rationale for expansion offered in this circular is",
   choices=[
     "the desire to religiously convert indigenous populations",
     "the concept of the civilizing mission understood as secular schooling",
     "Social Darwinism understood as a contest among races",
     "nationalism understood as competition for prestige among states",
     "an economic argument about the cost of maintaining a colony"], ans=0,
   why="KC-5.2.III names the desire to religiously convert indigenous populations among the justifications for imperialism. The circular asks for money for preaching and conversion, not for schools, not for a contest among races, not for national standing and not on grounds of cost."),
 dict(q="Two illustrative sources justify the same colonial administration. The first says the governed are 'children who will one day come of age'; the second says they are 'a stock that must inevitably give way'. Which feature of the second source best shows that it draws on Social Darwinism rather than on the civilizing mission?",
   choices=[
     "It presents the decline of the governed as a natural outcome rather than as a condition that instruction could change",
     "It presents the governed as capable of improvement, whereas the first source denies that they are",
     "It appeals to a religious duty, whereas the first source appeals to a secular one",
     "It was written for readers in the colony, whereas the first was written for readers at home",
     "It concerns a territory acquired by treaty, whereas the first concerns one acquired by war"], ans=0,
   why="KC-5.2.III lists Social Darwinism and the civilizing mission as separate ideologies. The civilizing mission holds that the governed can be raised by instruction; a Social Darwinist argument treats their displacement as the natural working out of a struggle, which is what 'must inevitably give way' asserts. The two clauses of the key have to be read together: it is the contrast between inevitability and improvability that separates them, not either idea alone."),
 dict(q="Text 1, an illustrative official memorandum, describes colonial rule as 'a tutelage that must end when its work is done'. Text 2, an illustrative pamphlet of the same decade, describes the same rule as 'the permanent ascendancy of a fitter people'. The clearest difference between the two justifications is that",
   choices=[
     "Text 1 treats the difference between the two societies as temporary while Text 2 treats it as permanent",
     "Text 1 treats the difference between the two societies as permanent while Text 2 treats it as temporary",
     "Text 1 appeals to religion while Text 2 appeals to national prestige",
     "Text 1 concerns a settler colony while Text 2 concerns a trading post",
     "Text 1 was intended for readers in the colony and Text 2 for readers abroad"], ans=0,
   why="KC-5.2.III names both the civilizing mission and Social Darwinism as justifications in use in this period. A tutelage that ends when its work is done is a temporary difference; a permanent ascendancy of the fitter is not. Both clauses of the key are needed, because the reversed statement is offered as a choice and is false."),
 dict(q="The course framework names several ideologies used to justify imperialism from 1750 to 1900. What do the named ideologies have in common as the framework presents them?",
   choices=[
     "Each supplied a reason offered in public for imperial rule",
     "Each was first formulated by colonized populations and later adopted by imperial states",
     "Each was an economic doctrine about the cost of acquiring territory",
     "Each was formally adopted as law by the states that expanded",
     "Each was abandoned by its supporters before the end of the period"], ans=0,
   why="KC-5.2.III's own verb is that these ideologies were 'used to justify' imperialism, which is what the key says and what the four other options do not. The framework does not describe them as colonial in origin, as economic doctrines, as statutes, or as abandoned."),
 dict(q="An illustrative speech to a parliamentary audience argues that acquiring a new territory will 'raise our name among the powers and at the same time lift its inhabitants from ignorance'. The speech joins together",
   choices=[
     "an appeal to the nation's standing and a claimed duty to improve the governed",
     "an appeal to religious conversion and a claim about racial fitness",
     "an appeal to racial fitness and a claim about the cost of administration",
     "an appeal to free trade and a claimed duty to improve the governed",
     "an appeal to the nation's standing and a claim that the territory is uninhabited"], ans=0,
   why="KC-5.2.III names nationalism and the concept of the civilizing mission among the justifications for imperialism, and this speech carries one clause of each: standing among the powers, and the lifting of the inhabitants. Nothing in it concerns religion, racial fitness, tariffs or an empty territory."),
 dict(q="Which of the following is NOT among the ideologies the course framework names as having been used to justify imperialism in this period?",
   choices=[
     "A doctrine calling for the free movement of goods across borders without tariffs",
     "Social Darwinism",
     "Nationalism",
     "The concept of the civilizing mission",
     "The desire to religiously convert indigenous populations"], ans=0,
   why="KC-5.2.III names exactly four: Social Darwinism, nationalism, the concept of the civilizing mission, and the desire to religiously convert indigenous populations. A tariff doctrine is not on that list, and the framework treats economic factors in the separate topics on the global economy and on economic imperialism."),
 dict(q="An unattributed report by a colonial official describes local religious practice as 'superstition that our missions will in time replace'. The passage is best used as evidence of",
   choices=[
     "the use of religious conversion as a justification for imperial rule",
     "the use of Social Darwinism as a justification for imperial rule",
     "an economic argument for the extraction of raw materials",
     "the growth of anticolonial movements within the territory",
     "the transfer of a colony from a company to a government"], ans=0,
   why="KC-5.2.III names the desire to religiously convert indigenous populations among the ideologies used to justify imperialism, and the passage justifies the imperial presence by the replacement of local practice with the missions' religion. It reports nothing about struggle among peoples, about raw materials, about resistance or about administrative transfer."),
 dict(q="Reading an illustrative editorial that warns 'the loss of this territory would be a humiliation before our rivals', a student should identify the argument as an appeal to",
   choices=[
     "national prestige in competition with other states",
     "a religious obligation owed to the inhabitants",
     "the biological ranking of human populations",
     "the improvement of the governed through schooling",
     "the price of the commodities the territory produces"], ans=0,
   why="KC-5.2.III names nationalism among the justifications for imperialism. The editorial's stated stake is the nation's humiliation before rivals, which is a claim about standing among states, and it makes no religious, biological, educational or commercial claim."),
 dict(q="A student asks why the ideologies in this topic are described as rationales for imperialism rather than as its causes. The best answer is that the framework",
   choices=[
     "says these ideologies were used to justify imperialism, which is a claim about the arguments offered rather than about everything that moved states to expand",
     "denies that ideas had any bearing on imperial expansion during this period",
     "treats these ideologies as the only reason states acquired territory in this period",
     "places all four ideologies after 1900 and so outside the period of expansion",
     "presents these ideologies as arguments made by colonized populations against expansion"], ans=0,
   why="KC-5.2.III's wording is that a range of ideologies 'were used to justify imperialism'. That is a statement about the justifications offered, and the unit treats economic and environmental factors separately in the topics on the global economy, economic imperialism and migration. The framework neither denies that ideas mattered nor makes them the sole cause."),
 dict(q="The table below reports a hypothetical study of two samples of forty imperial pamphlets each, one from the 1830s and one from the 1890s. Which conclusion is supported by the data as given?",
   choices=[
     "The claim about the nation's standing appears in more of the later pamphlets than of the earlier ones",
     "The call for religious conversion appears in more of the later pamphlets than of the earlier ones",
     "Every argument listed appears more often in the later sample than in the earlier one",
     "The claim about struggle among peoples is the most common argument in the earlier sample",
     "The duty to bring law, schooling and medicine disappears from the later sample"], ans=0,
   table=_T_PAMPHLETS,
   why="Read from the table alone: the standing argument rises from 9 pamphlets to 28. Religious conversion falls from 22 to 12, so not every argument rises; struggle is the least common argument in the earlier sample at 3; and the duty argument is present in 26 of the later pamphlets. Only the keyed statement survives the numbers."),
 dict(q="Using the same hypothetical pamphlet study, which argument shows the largest increase in the number of pamphlets containing it between the two samples?",
   choices=[
     "The claim that colonies raise the nation's standing among rivals",
     "The claim that peoples struggle and the stronger displace the weaker",
     "The duty to bring law, schooling and medicine to the governed",
     "The call to convert the population to the writer's religion",
     "All four arguments increase by the same number of pamphlets"], ans=0,
   table=_T_PAMPHLETS,
   why="The increases recompute from the table as 19 for the standing argument, 16 for the struggle argument and 8 for the duty argument, while the conversion argument falls by 10. The largest increase is therefore the standing argument, and the four increases are plainly not equal."),
 dict(q="A researcher holding the hypothetical pamphlet study wishes to know how readers reacted to these arguments. Which of the following can the table NOT establish?",
   choices=[
     "Whether readers were persuaded by the arguments the pamphlets made",
     "Whether the standing argument appears in more of the later pamphlets than of the earlier ones",
     "Whether the conversion argument appears in fewer of the later pamphlets than of the earlier ones",
     "Whether the struggle argument is the least common argument in the earlier sample",
     "Whether the duty argument appears in more than half of the later sample"], ans=0,
   table=_T_PAMPHLETS,
   why="The table counts the arguments a pamphlet contains and nothing else. Each of the four rejected statements is a count that can be read off the table, while the effect of an argument on the people who read it is not recorded anywhere in it and cannot be inferred from a tally of what was printed."),
 dict(q="An illustrative colonial governor's dispatch justifies a new administration by promising 'order, law and instruction' and says nothing about faith, race or rivalry. Which of the framework's named justifications does the dispatch rely on?",
   choices=[
     "The concept of the civilizing mission alone",
     "Social Darwinism alone",
     "Religious conversion alone",
     "Nationalism alone",
     "The civilizing mission joined to religious conversion"], ans=0,
   why="KC-5.2.III separates the four justifications, and this dispatch carries the marks of only one of them: a promised improvement of the governed through order, law and instruction. Silence about faith rules out conversion, silence about race rules out Social Darwinism, and silence about rivals rules out an appeal to national standing."),
 dict(q="Which feature of an imperial argument best distinguishes an appeal to the civilizing mission from an appeal to national prestige?",
   choices=[
     "The civilizing mission justifies rule by a benefit claimed for the governed, while an appeal to prestige justifies it by a gain claimed for the governing nation",
     "The civilizing mission justifies rule by a gain claimed for the governing nation, while an appeal to prestige justifies it by a benefit claimed for the governed",
     "The civilizing mission is always expressed in religious language and an appeal to prestige never is",
     "The civilizing mission was used only in Africa and an appeal to prestige only in Asia",
     "The civilizing mission was used before 1850 and an appeal to prestige only afterwards"], ans=0,
   why="KC-5.2.III lists the civilizing mission and nationalism as separate ideologies used to justify imperialism. The distinction is in whom the claimed benefit belongs to, and the reversed version of that sentence is offered as a distractor and is false. The framework attaches no region and no date within the period to either, and its dates are in any case approximate."),
 dict(q="An illustrative annual report of a mission society describes its stations as places where 'the word is preached, the sick are treated and the young are taught'. The report shows two of the framework's named ideologies working together, namely",
   choices=[
     "religious conversion together with the concept of the civilizing mission",
     "religious conversion together with Social Darwinism",
     "Social Darwinism together with an appeal to the nation's standing",
     "an appeal to the nation's standing together with the concept of the civilizing mission",
     "an appeal to free trade together with religious conversion"], ans=0,
   why="KC-5.2.III names both the desire to religiously convert indigenous populations and the concept of the civilizing mission. Preaching answers to the first; treating the sick and teaching the young are the improvement of the governed that answers to the second. Nothing in the report concerns struggle among peoples, national standing or tariffs."),
 dict(q="A student writes that the ideologies in this topic belong to the twentieth century and had no part in the expansion the unit describes. The most accurate correction is that the framework",
   choices=[
     "places the use of these justifications within the period from 1750 to 1900, the period this unit covers",
     "places these justifications only in the decades after the unit's period closes",
     "denies that any justification was offered in public for imperial expansion",
     "treats these justifications as the private opinions of a few writers with no public use",
     "restricts these justifications to a single empire in a single region"], ans=0,
   why="KC-5.2.III appears under Unit 6, whose stated span is c. 1750 to c. 1900, and its claim is that these ideologies were used to justify imperialism in that period. The framework does not confine them to one empire, one region or one set of private opinions, and it says nothing that would move their use out of the period entirely."),
 dict(q="The thematic focus of this topic states that the interactions of societies and their beliefs often have political, social and cultural implications. Applied to the ideologies in this topic, that statement means that",
   choices=[
     "what a society believed about other peoples shaped how it governed them",
     "beliefs about other peoples were held privately and left administration untouched",
     "political arrangements in this period were settled entirely by military strength",
     "cultural beliefs are of interest to historians only where they were written down by governments",
     "religion is the only kind of belief with political consequences"], ans=0,
   why="The Cultural Developments and Interactions focus states that the development of ideas and beliefs illustrates how groups view themselves and that the interaction of societies and their beliefs has political, social and cultural implications. KC-5.2.III is that statement in operation: beliefs about other peoples supplied the justification for ruling them."),
 dict(q="An illustrative settler newspaper argues that the district's original inhabitants are 'a vanishing remnant whose lands will pass by nature to those who can use them'. This argument is an application of",
   choices=[
     "Social Darwinism to a question of land",
     "the civilizing mission to a question of land",
     "religious conversion to a question of land",
     "anticolonial nationalism to a question of land",
     "an argument about the price of agricultural exports"], ans=0,
   why="KC-5.2.III names Social Darwinism among the ideologies used to justify imperialism. The passage presents dispossession as a natural passing rather than as an improvement offered to the inhabitants, a conversion, an argument against empire or a claim about prices."),
 dict(q="Nationalism appears in this unit both as a justification for imperial expansion and as a contributor to movements against imperial rule. The best statement of that double role is that",
   choices=[
     "the same ideology was used to justify empire and, in other hands, to oppose it",
     "the ideology changed its meaning entirely at a fixed date in the middle of the period",
     "the framework treats the two uses as belonging to different centuries",
     "the framework treats anticolonial movements as having no ideological content at all",
     "nationalism was used only by colonizing states and never by colonized populations"], ans=0,
   why="KC-5.2.III names nationalism among the ideologies used to justify imperialism, while KC-5.3.III.D states that growing nationalism contributed to anticolonial movements. Both statements sit in the same unit and the same period, so the framework has one ideology serving two opposite purposes rather than changing meaning on a date."),
 dict(q="The table below reports a hypothetical survey of fundraising appeals issued by mission societies during this period. Which conclusion is supported by the data as given?",
   choices=[
     "Conversion is named in a larger share of the appeals than any other purpose listed",
     "Support for military garrisons is named in a larger share of the appeals than schooling",
     "Assisting merchants is named in more than half of the appeals",
     "Medical care is named in a larger share of the appeals than conversion",
     "Every purpose listed is named in at least a quarter of the appeals"], ans=0,
   table=_T_APPEALS,
   why="Read from the table alone: conversion at 84 percent is the largest of the five shares. Garrisons at 5 percent fall below schooling at 61; assisting merchants at 12 percent is not a majority; medical care at 47 percent is below conversion; and two of the five purposes fall below a quarter."),
 dict(q="Using the same hypothetical survey of mission appeals, a student concludes that the societies were interested only in trade. The strongest objection to that conclusion is that",
   choices=[
     "assisting merchants is the second least often named purpose in the survey",
     "the survey does not record how much money each appeal raised",
     "the survey covers appeals rather than the sermons preached at the stations",
     "the survey gives shares rather than counts of appeals",
     "the survey does not name the countries in which the societies worked"], ans=0,
   table=_T_APPEALS,
   why="The objection has to come from the data the student is using, and the table answers the claim directly: assisting merchants is named in 12 percent of appeals, above only garrisons at 5 percent and far below conversion, schooling and medical care. The other four statements are true of the survey but leave the student's claim untouched."),
 dict(q="A historian argues that appeals to racial struggle were aimed mainly at educated readers at home rather than at officials serving in the colonies. Which additional evidence would most directly test that argument?",
   choices=[
     "A comparison of the arguments used in material addressed to readers at home with those used in material addressed to serving officials",
     "A count of the total number of pamphlets published in the period",
     "A list of the territories acquired by each state during the period",
     "The biographies of the authors of the pamphlets that survive",
     "The sales figures of newspapers in the imperial capital"], ans=0,
   why="The argument is a claim about which audience received which argument, so the evidence that tests it must compare material by audience. A total count, a list of acquisitions, biographies and circulation figures each measure something the claim does not assert, and none of them separates the two audiences the historian names."),
 dict(q="Learning objective A asks students to explain how ideologies contributed to the development of imperialism. Which statement best describes the contribution the framework attributes to them?",
   choices=[
     "They made expansion appear legitimate to the publics and governments that authorized it",
     "They supplied the machinery and capital that made expansion physically possible",
     "They determined the borders drawn between neighbouring colonies",
     "They obliged states to relinquish territories they already held",
     "They were the only factor at work in the expansion of empires in this period"], ans=0,
   why="KC-5.2.III says these ideologies were used to justify imperialism, and a justification works on the people who authorize and accept a policy. Machinery and capital, boundary drawing and the giving up of territory are not claims the framework attaches to these ideologies, and it does not present them as the sole factor."),
 dict(q="Which pair of statements about an imperial pamphlet can be settled by reading the pamphlet itself, and which cannot?",
   choices=[
     "What arguments the pamphlet offered in public can be settled by reading it; whether its author sincerely believed them cannot",
     "Whether its author sincerely believed the arguments can be settled by reading it; what arguments it offered cannot",
     "Neither what it argued nor how it was distributed can be settled by reading it",
     "Both what it argued and how many readers it persuaded can be settled by reading it",
     "What arguments it offered can be settled only by consulting government records"], ans=0,
   why="A text is direct evidence of the argument it makes and is not evidence of the state of mind behind it or of its effect on readers. Confusing the argument made with the motive held is the error the reversed option commits, and it is the reason the framework describes these ideologies as justifications that were used rather than as feelings that were held."),
 dict(q="Why does the framework place the ideologies that justified imperialism under the theme of cultural developments and interactions rather than under governance or economics?",
   choices=[
     "Because they are sets of beliefs a society held about itself and about other peoples",
     "Because they were enacted as statutes by imperial legislatures",
     "Because they concern the prices at which colonial commodities were exchanged",
     "Because they describe the administrative institutions through which colonies were run",
     "Because they were produced by colonized populations rather than by imperial ones"], ans=0,
   why="The Cultural Developments and Interactions focus is defined as the development of ideas, beliefs and religions and how groups in society view themselves and others. Social Darwinism, nationalism, the civilizing mission and the desire to convert are all beliefs of that kind; statutes, prices and administrative institutions belong to the governance and economics themes the unit treats elsewhere."),
 dict(q="An illustrative account written by a serving official describes the transfer of a territory from a trading company to the government of the same state, and defends the change as bringing 'settled principles of justice' to the population. This account is best used as evidence about",
   choices=[
     "a change in who exercised colonial control, defended in the language of improvement",
     "a change in who exercised colonial control, defended in the language of racial struggle",
     "the end of colonial control over the territory in question",
     "a migration of workers into the territory in question",
     "the price paid for the territory's exports in the imperial market"], ans=0,
   why="KC-5.2.I.A states that some states assumed direct control over colonies previously held by non-state entities, which is the change the account describes; KC-5.2.III supplies the language of improvement in which the writer defends it. The account reports no end of control, no migration and no prices, and it makes no claim about struggle among peoples."),
 dict(q="A student argues that one ideology alone accounts for the justification of imperialism across this whole period. The framework's own statement of the topic corrects this by",
   choices=[
     "describing a range of ideologies used to justify imperialism rather than a single one",
     "identifying religious conversion as the only justification actually used",
     "identifying Social Darwinism as the only justification actually used",
     "denying that any of these ideologies was used before the middle of the nineteenth century",
     "confining every justification to a single empire and a single continent"], ans=0,
   why="KC-5.2.III opens by describing a range of cultural, religious and racial ideologies and then lists four of them, so the framework's claim is plural on its face. It singles out none of the four, dates none of them within the period, and confines none of them to one empire or one continent."),
]
