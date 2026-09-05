# AP WORLD HISTORY: MODERN 9.9 Continuity and Change in a Globalized World
# CED effective Fall 2026 (Course Framework V.1), Unit 9 Globalization,
# c. 1900 to the present. Reasoning process: Continuity and Change.
#
# THIS IS THE UNIT'S REASONING TOPIC, AND THE BANK IS WRITTEN AS ONE. The CED
# says of it: "The final topic in this unit focuses on the skill of argumentation
# and so provides an opportunity for your students to draw upon the key concepts
# and historical developments they have studied in this unit. Using evidence
# relevant to this unit's key concepts, students should practice the suggested
# skill for this topic." So every item below is an argument-evaluation item, not
# fact recall: each puts a claim, an argument or a body of evidence in front of
# the student and asks what would corroborate it, what would qualify it, what
# would refute it, or why one argument is better made than another.
#
# Learning Objective: Unit 9 Learning Objective I -- explain THE EXTENT TO WHICH
# science and technology brought change in the period from 1900 to the present.
# Suggested skill 6.D, corroborate, qualify, or modify an argument using diverse
# and alternative evidence in order to develop a complex argument, with the same
# four things such an argument might do that Topic 8.9 prints: nuance from
# multiple variables, connections within and across periods, the relative
# significance of a source's credibility and limitations, and why an argument is
# or is not effective.
#
# THE CED'S OWN SENTENCE FRAME IS THE SHAPE OF THIS TOPIC. Its sample activity
# for 9.9 gives students this frame to complete: "Science and technology led to
# profound changes like ______; however, this change did have limits, for example
# ______ remained constant." A claim of change, qualified by a continuity. That
# is what an argument about EXTENT is, and it is why so many items here ask what
# would limit or qualify a change claim rather than what would prove it.
#
# HOW THIS DIFFERS FROM 8.9, WHICH IS THE OTHER REASONING TOPIC IN THIS
# TERRITORY. 8.9's reasoning process is CAUSATION and its question is whether the
# Cold War's effects were similar across two hemispheres, so its items turn on
# corroborating and refuting causal claims. 9.9's reasoning process is CONTINUITY
# AND CHANGE and its question is the EXTENT of change, so its items turn on
# qualifying a change with a continuity, on telling a difference of degree from a
# difference of kind, and on matching the scope of a claim to the scope of its
# evidence. Neither module reuses the other's stems or its evidence.
#
# REVIEW: UNIT 9 KEY CONCEPTS, which the CED reprints on this page and which are
# the sentences the keys below rest on:
#   KC-6.1         Rapid advances in science and technology altered the
#                  understanding of the universe and the natural world and led to
#                  advances in communication, transportation, industry,
#                  agriculture, and medicine.
#   KC-6.1.I.A     New modes of communication and transportation reduced the
#                  problem of geographic distance.
#   KC-6.1.I.B     The Green Revolution and commercial agriculture increased
#                  productivity and sustained the earth's growing population as
#                  it spread chemically and genetically modified forms of
#                  agriculture.
#   KC-6.1.I.C     Medical innovations, including vaccines and antibiotics,
#                  increased the ability of humans to survive and live longer
#                  lives.
#   KC-6.1.I.D     Energy technologies raised productivity and increased the
#                  production of material goods.
#   KC-6.1.III.B   More effective forms of birth control gave women greater
#                  control over fertility and contributed to declining rates of
#                  fertility in much of the world.
#   KC-6.3.I       States responded in a variety of ways to the economic
#                  challenges of the 20th century.
#   KC-6.3.III.i   Rights-based discourses challenged old assumptions about race,
#                  class, gender, and religion.
#   KC-6.3.III.ii  In much of the world, access to education as well as
#                  participation in new political and professional roles became
#                  more inclusive in terms of race, class, gender, and religion.
#   KC-6.3.IV.i    Political and social changes of the 20th century led to changes
#                  in the arts and in the second half of the century, popular and
#                  consumer culture became more global.
#   KC-6.3.IV.ii   Arts, entertainment, and popular culture increasingly reflected
#                  the influence of a globalized society.
#   KC-6.3.IV.iii  Consumer culture became globalized and transcended national
#                  borders.
#
# THE THING THIS MODULE MUST NOT DO. Learning Objective I asks the EXTENT to
# which science and technology brought change. That is a question students are
# meant to argue, and the CED supplies no verdict on it. NO KEY HERE ANSWERS IT.
# Every item keys the reasoning move -- what qualifies a change claim, what a
# scope mismatch shows, what a source's limits are -- and leaves the historical
# judgement to the student. A bank that keyed "the change was profound" or "the
# change was limited" would mark one side of an open question wrong. The same
# refusal applies to the unit's live disputes: no key says whether modified
# agriculture, birth control, free-market policy or the globalization of culture
# was good or bad, and no key states a cause of climate change.
#
# SOURCES. Section I is stimulus-based and this bank cannot display an image, so
# every stimulus is TEXT and none is attributed to a real person or document.
# Historians' arguments quoted below are unattributed and illustrative; the item
# asks about the reasoning, never about who made it. TABLES are hypothetical,
# each states a whole and its parts, and every keyed conclusion is recomputed
# from the table alone. DATES are written "1900 to 2000", never with a hyphen.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("9.9", "Continuity and Change in a Globalized World", 9)

_T_ELECTRICITY = dict(
    headers=["Region (hypothetical household survey, thousands of households)",
             "Households surveyed",
             "Of those, connected to an electricity supply",
             "Of those, not connected"],
    rows=[["Region one", "1,000", "960", "40"],
          ["Region two", "800", "480", "320"],
          ["Region three", "600", "180", "420"]])

_T_DEATHS = dict(
    headers=["Period (hypothetical record of one population, thousands of deaths recorded)",
             "Deaths recorded",
             "Of those, of persons under 5 years of age",
             "Of those, of persons 5 years of age and over"],
    rows=[["1920", "200", "90", "110"],
          ["1960", "150", "45", "105"],
          ["2000", "120", "12", "108"]])

_T_TELEPHONES = dict(
    headers=["Period (hypothetical record of one country's households, thousands)",
             "Households recorded",
             "Of those, with a telephone of any kind",
             "Of those, with none"],
    rows=[["1960", "4,000", "400", "3,600"],
          ["1980", "5,000", "2,000", "3,000"],
          ["2000", "6,000", "5,100", "900"]])

QUESTIONS = [

 dict(q="A historian argues that science and technology transformed human life completely in the twentieth century. Which kind of evidence would most directly qualify that argument without overturning it?",
   choices=[
     "Evidence of a region in which one of the century's technologies had still not arrived",
     "Evidence of a further region in which the same technology had arrived",
     "Evidence that the technology was invented earlier than the argument states",
     "Evidence that the historian has written about other centuries as well",
     "Evidence that the argument has been made by other historians too"],
   ans=0,
   why="Unit 9 Learning Objective I asks for the EXTENT to which science and technology brought change, and skill 6.D asks a student to qualify or modify an argument using alternative evidence. KC-6.1 records advances in communication, transportation, industry, agriculture and medicine without asserting that they reached everywhere, so a region the technology had not reached limits the claim's scope rather than denying the advance."),

 dict(q="The framework's own sentence frame for this topic asks a student to complete: science and technology led to profound changes like blank; however, this change did have limits, for example blank remained constant. What kind of argument does that frame produce?",
   choices=[
     "A claim of change qualified by a continuity, which is what a claim about extent requires",
     "A claim of change supported by further examples of the same change",
     "A claim that nothing changed, supported by examples of continuity",
     "A chronology of inventions with no claim attached",
     "A ranking of technologies from most to least important"],
   ans=0,
   why="Unit 9 Learning Objective I asks for the extent to which science and technology brought change, and skill 6.D asks for an argument that qualifies and complicates. The frame the CED prints in its sample activity for this topic pairs a profound change with something that remained constant, which is a claim about extent rather than a claim about occurrence."),

 dict(q="A hypothetical household survey divides each region's households into two groups. Which conclusion does the table alone support?",
   table=_T_ELECTRICITY,
   choices=[
     "Connected households are recorded in every region, but the share connected differs greatly between the three",
     "No household in the third region is recorded as connected",
     "Every household in every region is recorded as connected",
     "The share connected is the same in all three regions",
     "The third region surveyed more households than the second"],
   ans=0,
   why="KC-6.1.I.D records that energy technologies raised productivity and increased the production of material goods, and Unit 9 Learning Objective I asks for the EXTENT of the change technology brought. A survey in which a technology is present everywhere but unevenly gives a student material for both halves of an argument about extent rather than settling it, and the figures are hypothetical, with the key recomputed from the table alone in the verifier."),

 dict(q="Two students argue about the same claim. The first writes that a technology changed everything about how people worked. The second writes that it changed some tasks greatly, others hardly at all, and gives an example of each. Whose argument better meets the standard this topic sets?",
   choices=[
     "The second, because a claim about extent requires the limits of the change to be shown as well as the change",
     "The first, because a stronger claim is always a better argument",
     "The first, because giving examples of limits weakens any argument",
     "Neither, because arguments about technology cannot be assessed",
     "Both equally, because both mention the same technology"],
   ans=0,
   why="Unit 9 Learning Objective I asks for the EXTENT to which science and technology brought change, and skill 6.D names explaining how or why an argument is or is not effective as one of the moves a complex argument makes. An argument that shows where a change reached and where it did not is an argument about extent; one that asserts totality is not."),

 dict(q="A researcher wants to argue that the twentieth century's technological change was uneven rather than uniform. Which body of evidence would most directly corroborate that argument?",
   choices=[
     "Measurements of the same technology's spread in several regions, showing markedly different levels",
     "Measurements of one technology's spread in one region over one decade",
     "A list of the century's inventions in the order they were made",
     "The biographies of the people who made those inventions",
     "The number of scientific journals founded during the century"],
   ans=0,
   why="KC-6.1 records that rapid advances in science and technology led to advances in communication, transportation, industry, agriculture, and medicine, and skill 6.D asks a student to corroborate an argument with diverse evidence. A claim about unevenness is a comparative claim and needs measurements from more than one place, which a single region or a list of inventions cannot supply."),

 dict(q="An unattributed textbook chapter of 1995 states that medicine lengthened human life in the twentieth century and stops there. Judged by this topic's standard, what does the chapter leave out?",
   choices=[
     "Any indication of how far and where that lengthening reached, which is what a claim about extent requires",
     "Any statement that medicine changed at all during the century",
     "Any mention of the century in which the change occurred",
     "Any reference to a source of any kind",
     "Any claim that could be argued about by a student"],
   ans=0,
   why="KC-6.1.I.C states that medical innovations, including vaccines and antibiotics, increased the ability of humans to survive and live longer lives, which the chapter reports correctly. Unit 9 Learning Objective I asks for the EXTENT of such change, so what is missing is the reach and the limits rather than the fact."),

 dict(q="A hypothetical record divides the deaths of one population into two groups in each period. Which conclusion does the table alone support?",
   table=_T_DEATHS,
   choices=[
     "The number of deaths recorded fell in each period, and the share of them of persons under 5 fell in each period as well",
     "The number of deaths recorded rose in each period after the first",
     "The share of deaths of persons under 5 rose across the record",
     "No death of a person under 5 is recorded in the last period",
     "Deaths of persons 5 and over fell in each period recorded"],
   ans=0,
   why="KC-6.1.I.C states that medical innovations increased the ability of humans to survive and live longer lives, and a falling share of deaths among the youngest is one measure a student could use in an argument about how far that reached. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier; the framework supplies no verdict on the extent of the change."),

 dict(q="An argument holds that because a technology existed by 1970, its effects were felt everywhere by 1970. What is wrong with the inference?",
   choices=[
     "The existence of a technology does not establish that it had reached or been adopted everywhere",
     "The existence of a technology in 1970 cannot be established by any evidence",
     "Technologies of the twentieth century are not treated by this course",
     "A technology's effects can never be studied historically",
     "The inference is sound and nothing is wrong with it"],
   ans=0,
   why="KC-6.1 records that advances in science and technology led to advances in communication, transportation, industry, agriculture, and medicine without asserting that any of them reached everywhere at once. Unit 9 Learning Objective I asks for the EXTENT of the change, so the gap between a technology existing and its being in use is exactly the question the argument assumes away."),

 dict(q="A student assembles evidence on communication, agriculture, medicine and energy to support one claim about the century. Which of skill 6.D's moves is the student making?",
   choices=[
     "Explaining nuance by analyzing multiple variables",
     "Explaining the relative significance of a source's credibility",
     "Explaining a connection between one period and another",
     "Explaining a definition of a historical term",
     "Explaining a quantity recomputed from a table"],
   ans=0,
   why="Skill 6.D names explaining nuance of an issue by analyzing multiple variables as one of the four moves a complex argument makes, and KC-6.1 names communication, transportation, industry, agriculture, and medicine as the fields in which advances occurred. Assembling four of those fields under one claim is that move rather than any of the other three."),

 dict(q="A hypothetical record divides one country's households into two groups in each period. Which conclusion does the table alone support?",
   table=_T_TELEPHONES,
   choices=[
     "The share of households with a telephone rose in each period and was a large majority by the last",
     "The share of households with a telephone fell across the record",
     "No household is recorded with a telephone in the first period",
     "A majority of households had a telephone in every period recorded",
     "The number of households recorded fell across the record"],
   ans=0,
   why="KC-6.1.I.A states that new modes of communication reduced the problem of geographic distance, and the spread of a household technology is one measure of how far that reached. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier; how much change this represents is what a student is asked to argue."),

 dict(q="Two claims are set side by side. The first is that agricultural technology fed a growing population. The second is that the methods it spread were themselves a change in how farming was done. How does this course's framework bear on the pair?",
   choices=[
     "It supports both, since the same sentence states the yields and the spread of modified methods",
     "It supports the first and denies the second",
     "It supports the second and denies the first",
     "It denies both and states that agriculture was unchanged",
     "It is silent on agriculture in this period"],
   ans=0,
   why="KC-6.1.I.B states that the Green Revolution and commercial agriculture increased productivity and sustained the earth's growing population AS IT SPREAD chemically and genetically modified forms of agriculture. Both claims are halves of that single sentence, and the framework asserts them together without judging whether the methods were good."),

 dict(q="A historian argues that the century's most important change was in the fields where the framework records advances. Which observation would most directly complicate that argument?",
   choices=[
     "That the framework also records changes in social categories and in culture that were not technological",
     "That the framework records advances in communication as well as in medicine",
     "That the framework places the advances in the twentieth century",
     "That other historians have written about technology as well",
     "That technology is a subject that can be studied historically"],
   ans=0,
   why="KC-6.1 records the technological advances, but KC-6.3.III.i and KC-6.3.III.ii record rights-based challenges to old assumptions and a widening of access, and KC-6.3.IV.i to iii record changes in the arts and in culture. Skill 6.D asks a student to qualify an argument using alternative evidence, and the non-technological changes the unit also records are that evidence."),

 dict(q="An unattributed pamphlet of 1998 argues that the world of its day was unrecognizable to someone born in 1900. Which consideration would most usefully qualify the pamphlet's argument?",
   choices=[
     "Identifying what a person born in 1900 would still recognize, and saying why",
     "Identifying further things that person would not recognize",
     "Establishing the exact year in which the pamphlet was written",
     "Establishing how many copies of the pamphlet were printed",
     "Establishing whether the pamphlet's author was born before 1900"],
   ans=0,
   why="Unit 9 Learning Objective I asks for the EXTENT of the change science and technology brought, and the CED's own sentence frame for this topic pairs a profound change with something that remained constant. Skill 6.D asks a student to qualify an argument using alternative evidence, and what remained recognizable is that evidence; more instances of the same change would only restate the claim."),

 dict(q="A researcher finds that a technology spread quickly in one country and slowly in a neighbouring one. Which use of that finding best fits this topic's reasoning?",
   choices=[
     "Using the difference to say something about how far and how evenly the change reached",
     "Discarding the slower country as an exception that spoils the pattern",
     "Reporting only the faster country, since it shows the technology working",
     "Concluding that the technology did not exist in either country",
     "Concluding that no comparison between the two countries is possible"],
   ans=0,
   why="Unit 9 Learning Objective I asks for the extent to which science and technology brought change, and skill 6.D asks a student to develop a complex argument using diverse and ALTERNATIVE evidence. A difference between two neighbours is evidence about evenness, and discarding the inconvenient case is the failure the skill is written against."),

 dict(q="An unattributed report of 1985 written by a company that manufactures a technology concludes that the technology has transformed the region it sells into. What is the most significant limitation of this source for that conclusion?",
   choices=[
     "It is the manufacturer's own assessment of what its product has done",
     "It was written in 1985, which places it outside the period this course covers",
     "It concerns a region, and regions are too large to be studied",
     "It is a report, and reports contain no assessments of any kind",
     "It was written by a company, which makes it the only reliable source"],
   ans=0,
   why="Skill 6.D names explaining the relative historical significance of a source's credibility and limitations as one of the moves a complex argument makes. KC-6.1 records that advances in science and technology led to advances across several fields, and a manufacturer assessing its own product's effect has an interest in the answer, which is what limits the use of the source."),

 dict(q="Which statement about this unit's material would this course's framework treat as still open rather than settled?",
   choices=[
     "How far science and technology changed the world between 1900 and the present",
     "Whether new modes of communication reduced the problem of geographic distance",
     "Whether medical innovations increased the ability of humans to live longer lives",
     "Whether energy technologies raised productivity and the production of goods",
     "Whether consumer culture became globalized during the century"],
   ans=0,
   why="KC-6.1.I.A, KC-6.1.I.C, KC-6.1.I.D and KC-6.3.IV.iii each state a development as course content, while Unit 9 Learning Objective I asks students to explain THE EXTENT TO WHICH science and technology brought change. The framework supplies the developments and leaves the measure of their reach to be argued, which is the distinction this item is built on."),

 dict(q="A student argues that because access to education became more inclusive, every old assumption about who should be educated had disappeared by the end of the century. What is the best correction?",
   choices=[
     "The framework says access became more inclusive in much of the world, which is a change of degree rather than a disappearance",
     "The framework says access became less inclusive over the century",
     "The framework says no assumptions about education were ever challenged",
     "The framework says access changed only in the last decade of the century",
     "The framework says education is not a subject it treats"],
   ans=0,
   why="KC-6.3.III.ii states that IN MUCH OF THE WORLD access to education and participation in new political and professional roles became more inclusive in terms of race, class, gender, and religion. Unit 9 Learning Objective I asks for the extent of change, and the framework's qualifier makes this a change of degree, which is precisely what the student's inference oversteps."),

 dict(q="Two unattributed accounts of a village describe it in 1930 and in 1990. A student notes the differences and stops. What does this topic's skill ask the student to do next?",
   choices=[
     "Note what the two accounts show to have stayed the same, and build a claim about extent from both",
     "Find a third account of the same village from an intermediate year",
     "Establish which of the two accounts is longer",
     "Determine whether either account was published",
     "Abandon the comparison, since two accounts cannot be compared"],
   ans=0,
   why="The reasoning process the CED prints beside this topic is continuity and change, and Unit 9 Learning Objective I asks for the extent of the change science and technology brought. Skill 6.D asks a student to develop a complex argument, and the CED's own sentence frame for this topic requires both a change and something that remained constant, so the continuities are the missing half."),

 dict(q="Which of the following would count as an argument about extent rather than about occurrence?",
   choices=[
     "A claim that a technology changed a great deal in some places and little in others, with evidence for both",
     "A claim that a technology was invented during the twentieth century",
     "A claim that a technology was used somewhere in the twentieth century",
     "A claim that a technology has been described by historians",
     "A claim that a technology had a name by which people knew it"],
   ans=0,
   why="Unit 9 Learning Objective I asks for THE EXTENT TO WHICH science and technology brought change, which is a question of how much and how widely rather than whether at all. KC-6.1 already settles the occurrence by recording the advances, so an argument that adds anything must be about their reach, which is what skill 6.D's complex argument requires."),

 dict(q="A historian connects the falling rates of fertility recorded in much of the world to the spread of a technology, and then notes that the fall was not recorded everywhere. Which of skill 6.D's moves is this?",
   choices=[
     "Qualifying a claim using alternative evidence, so that the argument states its own limits",
     "Establishing the credibility of a single source against another",
     "Defining a historical term so that it can be used consistently",
     "Recomputing a published figure from the data behind it",
     "Listing the events of a period in the order they occurred"],
   ans=0,
   why="KC-6.1.III.B states that more effective forms of birth control gave women greater control over fertility and contributed to declining rates of fertility IN MUCH OF THE WORLD, which is a claim with a qualifier already in it. Skill 6.D names qualifying an argument using diverse and alternative evidence, and a historian who states both the pattern and its limit is making exactly that move."),

 dict(q="An argument claims that the century's technological changes made every society more alike. Which evidence from this unit would most directly complicate it?",
   choices=[
     "That states responded in a variety of ways to the economic challenges of the century",
     "That advances occurred in communication, transportation and medicine",
     "That the century's advances were rapid rather than gradual",
     "That the advances altered the understanding of the natural world",
     "That the advances have been written about by historians since"],
   ans=0,
   why="KC-6.3.I states that states responded IN A VARIETY OF WAYS to the economic challenges of the twentieth century, which is difference persisting alongside a common set of technologies. Skill 6.D asks a student to complicate an argument with alternative evidence, and the framework's own word variety is that evidence."),

 dict(q="A seminar is asked what makes an argument about this unit complex rather than simple. Which answer is best?",
   choices=[
     "That it states how far a change reached, supports that with evidence from more than one field or place, and explains what it did not reach",
     "That it states a change and supports it with as many examples of that change as possible",
     "That it lists every development of the century in chronological order",
     "That it selects the single most striking development and describes it fully",
     "That it avoids any claim that could be disputed by another student"],
   ans=0,
   why="Skill 6.D asks a student to corroborate, qualify, or modify an argument using diverse and alternative evidence IN ORDER TO DEVELOP A COMPLEX ARGUMENT, and Unit 9 Learning Objective I asks specifically for extent. Reach, breadth of evidence and an explained limit are the three parts of that; repetition, chronology and a single case each fail one."),

 dict(q="A student writes that popular culture became global and that this proves the whole world became culturally identical. Which consideration most directly checks that inference?",
   choices=[
     "That the framework says popular culture became more global, which is not the same as saying it became uniform",
     "That the framework says popular culture did not change during the century",
     "That the framework says popular culture became less global over time",
     "That the framework says culture is not a subject it treats",
     "That the framework says only consumer culture changed and popular culture did not"],
   ans=0,
   why="KC-6.3.IV.i states that in the second half of the century popular and consumer culture became MORE GLOBAL, and KC-6.3.IV.ii that arts, entertainment, and popular culture increasingly reflected the influence of a globalized society. More global is a comparative, and Unit 9 Learning Objective I's question about extent is exactly what the student's leap to uniformity skips."),

 dict(q="A researcher has two sources about the same technological change: a government statistical series and the recollections of people who lived through it. Which use of the pair best fits this topic's reasoning?",
   choices=[
     "Use the series for the scale of the change and the recollections for what it meant to those it reached",
     "Use the statistical series alone, since numbers are always more reliable than memory",
     "Use the recollections alone, since those present understand a change best",
     "Discard both, since a statistical series and a memory cannot be compared",
     "Average the two and report the result as a single finding"],
   ans=0,
   why="Skill 6.D asks for diverse and alternative evidence and for an explanation of the relative significance of a source's credibility and limitations. KC-6.1 records advances across several fields whose scale a series can measure and whose meaning it cannot, so the two sources answer different parts of one question about extent."),

 dict(q="Which pairing correctly matches a claim about this unit to the evidence that would test it?",
   choices=[
     "A claim about how widely a medical advance reached, tested against records of who received it and where",
     "A claim about how widely a medical advance reached, tested against the date the advance was first described",
     "A claim about the spread of a communications technology, tested against harvest returns",
     "A claim about agricultural productivity, tested against the number of films released",
     "A claim about energy technologies, tested against the membership of international organizations"],
   ans=0,
   why="KC-6.1.I.C states that medical innovations increased the ability of humans to survive and live longer lives, and a claim about how widely that reached is a claim about coverage, which records of recipients test directly. Skill 6.D asks for evidence relevant to the argument, and each distractor pairs a claim with material bearing on nothing in it."),

 dict(q="An unattributed lecture of 2001 argues that the twentieth century's changes were greater than those of any earlier century. Judged by this topic's standard, what does the argument most obviously need?",
   choices=[
     "Evidence about the earlier centuries as well, since the claim is comparative",
     "Evidence about a further development of the twentieth century",
     "Evidence about who first proposed the comparison",
     "Evidence about how long the lecture lasted",
     "Evidence about the audience the lecture addressed"],
   ans=0,
   why="Skill 6.D asks a student to explain how or why an argument is or is not effective, and Unit 9 Learning Objective I asks for the extent of change, which invites comparison. A claim that one century's change exceeded another's cannot be supported from one side alone, however much evidence is added to that side."),

 dict(q="A student's essay claims that science and technology changed the world and supports it entirely with examples drawn from a single city. What is the most accurate assessment?",
   choices=[
     "The claim is far wider than the evidence gathered to support it",
     "The evidence is far wider than the claim it is asked to support",
     "The claim and the evidence are matched in scope",
     "The essay cannot be assessed, since claims about the world are never arguable",
     "The evidence is unusable, since evidence from one city has no value"],
   ans=0,
   why="Unit 9 Learning Objective I asks for the extent to which science and technology brought change from 1900 to the present, which makes the scope of a claim and the scope of its evidence the thing at issue. Skill 6.D asks a student to explain why an argument is or is not effective, and evidence narrower than the claim it supports is the standard reason a sound-sounding argument fails."),

 dict(q="How does the reasoning process printed beside this topic differ from the one printed beside the final topic of the preceding unit?",
   choices=[
     "This topic's process is continuity and change, where the preceding unit's final topic is causation",
     "This topic's process is causation, where the preceding unit's final topic is continuity and change",
     "Both topics print the same reasoning process",
     "Neither topic prints a reasoning process at all",
     "This topic's process is comparison and the other's is contextualization"],
   ans=0,
   why="The CED prints continuity and change as the reasoning process for this topic, under Unit 9 Learning Objective I, and causation for Topic 8.9 under Unit 8 Learning Objective K. Both share skill 6.D, so what distinguishes the arguments they ask for is the process: how far something changed against what brought something about."),

 dict(q="Considered as a whole, why does this unit's material lend itself to an argument about extent rather than to a simple claim of transformation?",
   choices=[
     "Because the framework's own statements carry qualifiers, recording change in much of the world, in some regions, and in a variety of ways",
     "Because the framework records no changes of any kind during the century",
     "Because the framework states that every change reached every place equally",
     "Because the framework treats the century as too recent to be argued about",
     "Because the framework supplies a verdict on how much changed and how much did not"],
   ans=0,
   why="KC-6.3.III.ii says in much of the world, KC-6.3.I says in a variety of ways, KC-6.1.III.B says in much of the world again, and KC-6.3.I.E in Topic 9.4 says in some regions. Qualifiers of that kind are what make the reach of a change a question rather than a given, and Unit 9 Learning Objective I asks a student to argue it."),

 dict(q="Taking this topic as a whole, what does it ask a student to be able to do with the unit's material?",
   choices=[
     "Argue how far science and technology changed the period, support that with evidence from more than one field, and say what the change did not reach",
     "Recall the date of every technological advance in the unit and place them in order",
     "Decide which of the century's technologies was the most beneficial and defend that verdict",
     "Summarize each topic of the unit in turn without connecting any of them",
     "Identify the single technology from which every other development followed"],
   ans=0,
   why="Unit 9 Learning Objective I asks a student to explain the extent to which science and technology brought change from 1900 to the present, and skill 6.D asks for an argument corroborated, qualified or modified with diverse and alternative evidence. Extent, breadth of evidence and an explained limit are the three parts of that; a chronology, a verdict on benefit and a single cause are none of them."),
]
