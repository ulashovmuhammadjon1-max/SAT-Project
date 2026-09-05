# AP WORLD HISTORY: MODERN 9.7 Resistance to Globalization After 1900
# CED effective Fall 2026 (Course Framework V.1), Unit 9 Globalization,
# c. 1900 to the present. Thematic focus: Cultural Developments and Interactions
# (CDI). Reasoning process: Causation.
#
# Learning Objective: Unit 9 Learning Objective G -- explain the VARIOUS responses
# to increasing globalization from 1900 to present. Suggested skill 2.C, explain
# the significance of a source's point of view, purpose, historical situation,
# and/or audience, including how these might limit the use(s) of a source.
#
# HISTORICAL DEVELOPMENT this topic prints -- ONE sentence, and the shortest in
# the unit:
#   KC-6.3.IV.iv  Responses to rising cultural and economic globalization took a
#                 variety of forms.
# ILLUSTRATIVE EXAMPLES the CED prints beside it, under "Responses to economic
# globalization": anti-IMF and anti-World Bank activism; the advent of locally
# developed social media, such as Weibo in China. There are only two, so exactly
# ONE item turns on them and its stem says the course prints them as such.
#
# WHAT THIS ONE SENTENCE ACTUALLY LICENSES, because thirty questions have to come
# out of it honestly and nothing may be added:
#   (a) that there WERE responses, and that what they responded to was
#       globalization that was RISING;
#   (b) that the globalization responded to was of TWO kinds, cultural AND
#       economic, and the sentence names both;
#   (c) that the responses took A VARIETY OF FORMS -- not one form, which is
#       the whole content of the word various in the Learning Objective too.
# Everything keyed below is one of those three, or is a matter of skill 2.C
# applied to a source produced by someone responding. Where an item needs to name
# what globalization consisted of, it cites the sentence in another topic that
# says so -- KC-6.3.IV.i, ii and iii for the cultural side and KC-6.3.I.D,
# KC-6.3.I.E and KC-6.3.II.B for the economic -- rather than inventing content
# for this page.
#
# THE WORD IS "RESPONSES", NOT "REJECTIONS", AND THIS IS THE TOPIC'S REAL
# SUBTLETY. The title says Resistance, but the framework's sentence says
# RESPONSES, and it says they took a VARIETY of forms. The CED's own second
# illustrative example is the advent of locally developed social media, which is
# a locally made alternative rather than a refusal of the medium. So a bank that
# keyed every response as a rejection would narrow the framework's own word.
# Items 5, 11, 19, 24 and 28 hold the variety open.
#
# WHAT IS DELIBERATELY NOT KEYED. Whether globalization should have been resisted,
# whether any response was justified, and whether any response succeeded are all
# live political arguments and the framework settles none of them. NO key here
# says a response was right or wrong, effective or futile, reasonable or
# unreasonable; NO key attributes a motive to anyone who responded; and NO key
# says any institution deserved or did not deserve the opposition it met. The
# framework says responses happened and varied; that is what is keyed.
#
# DEDUPE NOTE. Topic 8.7, Global Resistance to Established Power Structures After
# 1900, borders this one and is in the same territory, so the line is drawn
# explicitly: 8.7 is reactions to CONFLICT and to power structures in the age of
# the Cold War -- nonviolence, militarized states, violence against civilians --
# and none of that vocabulary appears here. This module is only about responses to
# GLOBALIZATION, cultural and economic. Topic 9.5's KC-6.3.II.C, movements
# protesting the INEQUALITY of the environmental and economic consequences of
# global integration, is a narrower and different sentence; it is cited here only
# where an item needs an example of one form a response took, and the protest
# items of 9.5 are not reused.
#
# SOURCES. Section I is stimulus-based and this bank cannot display an image, so
# every stimulus is TEXT and none is attributed to a real person or document.
# TABLES are hypothetical, each states a whole and its parts, and every keyed
# conclusion is recomputed from the table alone. DATES are written "1970 to
# 2000", never with a hyphen.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("9.7", "Resistance to Globalization After 1900", 9)

_T_FORMS = dict(
    headers=["Decade (hypothetical record of recorded responses to globalization)",
             "Responses recorded",
             "Of those, taking the form of public protest",
             "Of those, taking some other form"],
    rows=[["1970s", "30", "18", "12"],
          ["1990s", "85", "44", "41"],
          ["2010s", "160", "62", "98"]])

_T_TARGET = dict(
    headers=["Decade (hypothetical record of recorded responses, by what they addressed)",
             "Responses recorded",
             "Of those, addressed chiefly to economic globalization",
             "Of those, addressed chiefly to cultural globalization"],
    rows=[["1980s", "50", "34", "16"],
          ["1990s", "90", "58", "32"],
          ["2000s", "140", "82", "58"]])

_T_SERVICES = dict(
    headers=["Country (hypothetical survey of users of online services, millions)",
             "Users recorded",
             "Of those, using a locally developed service most often",
             "Of those, using a service developed abroad most often"],
    rows=[["Country one", "120", "96", "24"],
          ["Country two", "60", "21", "39"],
          ["Country three", "40", "8", "32"]])

QUESTIONS = [

 dict(q="According to this course, what can be said about the forms taken by responses to rising cultural and economic globalization?",
   choices=[
     "They took a variety of forms",
     "They took a single form everywhere they occurred",
     "They took no organized form at any point",
     "They took the same form as responses to earlier changes had taken",
     "They are not described by the framework in any terms"],
   ans=0,
   why="KC-6.3.IV.iv states that responses to rising cultural and economic globalization took A VARIETY OF FORMS. Variety is the framework's own word and it is the whole content of the sentence about form, which Unit 9 Learning Objective G repeats when it asks for the VARIOUS responses to increasing globalization."),

 dict(q="This course names two kinds of globalization to which responses were made. What are they?",
   choices=[
     "Cultural globalization and economic globalization",
     "Military globalization and diplomatic globalization",
     "Cultural globalization alone, with no economic dimension",
     "Economic globalization alone, with no cultural dimension",
     "Environmental globalization and demographic globalization"],
   ans=0,
   why="KC-6.3.IV.iv states that responses to rising CULTURAL AND ECONOMIC globalization took a variety of forms. Both adjectives are in the framework's sentence, so a key naming one of the two would report half of what it says."),

 dict(q="A hypothetical record divides the responses of each decade into two groups by the form they took. Which conclusion does the table alone support?",
   table=_T_FORMS,
   choices=[
     "Responses of both kinds are recorded in every decade, and the share taking the form of public protest falls across the record",
     "Every response recorded took the form of public protest",
     "No response recorded in the 1970s took the form of public protest",
     "The number of responses recorded fell in each decade after the first",
     "The share taking the form of public protest rose across the record"],
   ans=0,
   why="KC-6.3.IV.iv states that responses took A VARIETY of forms, and a record in which protest is one form among others, and a shrinking share of the whole, is that variety counted. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="An unattributed circular of 1999 calls on readers to attend a meeting outside the offices of an international lending body during its annual session. According to this course, the circular is an instance of",
   choices=[
     "one of the forms taken by responses to rising economic globalization",
     "one of the forms taken by responses to the redrawing of colonial boundaries",
     "one of the forms taken by responses to the emergence of new epidemic diseases",
     "one of the forms taken by nationalist movements seeking independence",
     "one of the forms taken by militaries responding to a proliferation of conflicts"],
   ans=0,
   why="KC-6.3.IV.iv states that responses to rising cultural and economic globalization took a variety of forms, and the CED prints anti-IMF and anti-World Bank activism among its illustrative examples of responses to economic globalization. The key identifies which development the circular belongs to and says nothing about whether the meeting was justified."),

 dict(q="A firm founded in 1998 builds an online service for readers in its own country, in its own language, at a time when comparable services made abroad are becoming available there. According to this course, this founding is best described as",
   choices=[
     "one of the varied forms a response to globalization could take, alongside protest",
     "not a response to globalization at all, since it built something rather than opposing something",
     "a response to globalization identical in form to a public protest",
     "a rejection of the technology on which such services depend",
     "a development the framework places before the twentieth century"],
   ans=0,
   why="KC-6.3.IV.iv states that responses to rising cultural and economic globalization took A VARIETY OF FORMS, and the CED prints the advent of locally developed social media among its illustrative examples of responses to economic globalization. A locally built alternative is one of the varied forms the sentence covers, which is why the framework's word is responses rather than rejections."),

 dict(q="A student writes that this course says every response to globalization took the form of street protest. What is the best correction?",
   choices=[
     "The framework says responses took a variety of forms, so protest was one form among others",
     "The framework says responses took no form that can be identified",
     "The framework says no responses to globalization occurred at all",
     "The framework says responses were confined to a single country",
     "The framework says protest was the only form and the student is correct"],
   ans=0,
   why="KC-6.3.IV.iv states that responses took A VARIETY of forms. Variety rules out a single form without denying that protest was among them, so the correction has to keep protest inside the range rather than removing it, which is what the key does."),

 dict(q="A hypothetical record divides the responses of each decade by what they chiefly addressed. Which conclusion does the table alone support?",
   table=_T_TARGET,
   choices=[
     "Responses of both kinds are recorded in every decade, and those addressed chiefly to economic globalization outnumber the others throughout",
     "Only responses addressed chiefly to economic globalization are recorded",
     "Only responses addressed chiefly to cultural globalization are recorded",
     "Responses addressed chiefly to cultural globalization outnumber the others in every decade",
     "The number of responses recorded fell in each decade after the first"],
   ans=0,
   why="KC-6.3.IV.iv names both cultural and economic globalization as what responses answered, and a record containing both in every decade is that pairing counted. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier; the framework asserts no real frequency for either kind."),

 dict(q="An unattributed newsletter of 1996 is written by an association whose members trade in imported goods, and it argues against a proposed restriction on such trade. What does this course's suggested skill direct a student to notice first?",
   choices=[
     "That the association's members stand to gain from the outcome it argues for, which bears on how the argument can be used",
     "That the newsletter was written in 1996, which places it outside the period the framework covers",
     "That the newsletter concerns trade, a subject on which no evidence survives",
     "That the newsletter is an association's publication, which makes it the only admissible source",
     "That the newsletter has more than one author, which makes it unusable"],
   ans=0,
   why="Skill 2.C asks for the significance of a source's point of view, purpose, historical situation and audience, including how these might limit its uses. Unit 9 Learning Objective G asks for the various responses to increasing globalization, and an association arguing for the outcome its members profit from is a response whose interest a historian has to weigh before using it as evidence of anything else."),

 dict(q="Two unattributed sources of 1994 respond to the same trade agreement, one by organizing a demonstration and one by founding a magazine to argue against it in print. Read together, the pair most directly supports which of this course's statements?",
   choices=[
     "That responses to rising globalization took a variety of forms",
     "That responses to rising globalization all took the same form",
     "That no responses to globalization were made in this period",
     "That responses to globalization were addressed only to its cultural side",
     "That responses to globalization ceased after the 1980s"],
   ans=0,
   why="KC-6.3.IV.iv states that responses to rising cultural and economic globalization took A VARIETY OF FORMS. A demonstration and a magazine answering the same agreement are two forms of one response, which is the variety the sentence asserts made visible in a single case."),

 dict(q="This course describes responses to a globalization it characterizes in a particular way. How?",
   choices=[
     "As rising during the period in which the responses were made",
     "As declining during the period in which the responses were made",
     "As unchanging throughout the twentieth century",
     "As confined to the years before 1900",
     "As a process the framework does not characterize at all"],
   ans=0,
   why="KC-6.3.IV.iv states that responses were to RISING cultural and economic globalization. The framework's adjective makes the globalization something that was increasing while the responses were made, and Unit 9 Learning Objective G repeats it in asking for responses to INCREASING globalization."),

 dict(q="A cultural association founded in 1985 sets out to record and publish songs from its own region, explaining that it does so because so much of what is now heard there comes from elsewhere. This course would treat the association as",
   choices=[
     "a response to rising cultural globalization, taking one of the varied forms such responses took",
     "a response to rising economic globalization rather than to its cultural side",
     "an instance of consumer culture transcending national borders",
     "an instance of political change leading to a change in the arts",
     "an instance of the widening of access to education in much of the world"],
   ans=0,
   why="KC-6.3.IV.iv states that responses to rising CULTURAL and economic globalization took a variety of forms. An association that begins recording local songs because so much heard locally now comes from elsewhere is answering the cultural side, and collecting and publishing is one of the varied forms rather than the only one."),

 dict(q="A hypothetical survey divides each country's recorded users of online services into two groups. Which conclusion does the table alone support?",
   table=_T_SERVICES,
   choices=[
     "Some users in every country surveyed most often use a locally developed service, but such services are the more common choice in only one of the three",
     "No user in any country surveyed most often uses a locally developed service",
     "Locally developed services are the more common choice in every country surveyed",
     "Country three records more users than country two records",
     "The three countries record the same number of users as one another"],
   ans=0,
   why="KC-6.3.IV.iv states that responses to rising cultural and economic globalization took a variety of forms, and the CED prints the advent of locally developed social media among its illustrative examples. A survey in which locally developed services prevail in one place and not in others is that variety measured, and the figures are hypothetical, with the key recomputed from the table alone in the verifier."),

 dict(q="This course prints two illustrative examples of responses to economic globalization. Which pair is the one the course prints?",
   choices=[
     "Anti-IMF and anti-World Bank activism, and the advent of locally developed social media",
     "Greenpeace and the Green Belt Movement in Kenya",
     "The World Trade Organization, NAFTA, and ASEAN",
     "Reggae, Bollywood, and World Cup soccer",
     "Shining Path and Al-Qaeda"],
   ans=0,
   why="The CED prints anti-IMF and anti-World Bank activism and the advent of locally developed social media, such as Weibo in China, beside KC-6.3.IV.iv as its illustrative examples of responses to economic globalization. The other lists are printed beside statements in Topics 9.5, 9.4, 9.6 and 8.7. The item asks which pair the course prints and says nothing about whether either response was justified."),

 dict(q="An unattributed government white paper of 2001 describes the protests outside a recent international economic conference as the work of a small and unrepresentative minority. Which consideration most limits the use of this source as evidence about how widely those views were held?",
   choices=[
     "It was issued by a government that was a party to the conference the protests were directed at",
     "It was published in 2001, and documents of this century cannot be used as evidence",
     "It describes protests, and protests leave no other trace in the record",
     "It is a white paper, and white papers contain no statements about opinion",
     "It concerns an international conference, and such conferences are not studied"],
   ans=0,
   why="Skill 2.C asks how a source's point of view, purpose and situation might limit its uses. KC-6.3.IV.iv establishes that responses to rising globalization occurred and varied, and a government party to the meeting being protested has an interest in how numerous the protesters are said to be, which is exactly the claim at issue."),

 dict(q="What relation does this course draw between globalization and the responses described in this topic?",
   choices=[
     "The responses were made to globalization as it rose, so globalization is what they answered",
     "The responses caused globalization to begin",
     "The responses and globalization are treated as unconnected developments",
     "The responses preceded globalization by several decades",
     "The framework states that no response was ever made to globalization"],
   ans=0,
   why="KC-6.3.IV.iv states that RESPONSES TO rising cultural and economic globalization took a variety of forms, which makes globalization the thing responded to and the responses what followed. The reasoning process the CED prints beside this topic is causation, and this is the direction the sentence fixes."),

 dict(q="An unattributed pamphlet of 1993 opposes a proposed agreement, and a second pamphlet of the same year, from a different organization, opposes the same agreement for entirely different reasons. What does this course's framework allow a student to conclude?",
   choices=[
     "That responses to globalization varied in their grounds as well as in their forms",
     "That one of the two organizations must have misunderstood the agreement",
     "That the two organizations were in fact a single body under two names",
     "That neither pamphlet can be evidence of a response to globalization",
     "That the framework recognizes only one possible ground of objection"],
   ans=0,
   why="KC-6.3.IV.iv states that responses to rising cultural and economic globalization took A VARIETY OF FORMS, and Unit 9 Learning Objective G asks for the VARIOUS responses. Two organizations opposing one agreement on different grounds is that variety, and nothing in the framework requires objections to share a reason."),

 dict(q="Which statement about responses to globalization is NOT supported by this course?",
   choices=[
     "Every response to globalization in this period took the same form as every other",
     "Responses were made to rising cultural globalization",
     "Responses were made to rising economic globalization",
     "Responses took a variety of forms",
     "The globalization responded to was rising during the period"],
   ans=0,
   why="KC-6.3.IV.iv states that responses took A VARIETY of forms, so a claim that every response took the same form reverses the framework's sentence. The item asks which statement is NOT supported, so the key is deliberately the false one; the other four restate the parts of that single sentence."),

 dict(q="An unattributed leaflet of 2003 is addressed to shoppers and asks them to consider where the goods on a particular shelf were made. Judged by this course's suggested skill, what does the leaflet's choice of audience tell a historian?",
   choices=[
     "That its authors sought to act on globalization through the decisions of ordinary consumers rather than through government",
     "That its authors had no view about globalization of any kind",
     "That its authors were employed by the shop in which it was distributed",
     "That its authors intended it for an audience of professional economists",
     "That leaflets addressed to shoppers cannot be used as historical evidence"],
   ans=0,
   why="Skill 2.C asks for the significance of a source's audience, and a leaflet addressed to shoppers at the shelf is aimed at the point where a consumer decides. KC-6.3.IV.iv states that responses to rising cultural and economic globalization took a variety of forms, and acting through consumers rather than through governments is one of those forms."),

 dict(q="Which of the following best explains why this course speaks of responses to globalization rather than only of resistance to it?",
   choices=[
     "Because the framework says responses took a variety of forms, and building a local alternative is a different form from refusing",
     "Because the framework says no one resisted globalization at any point",
     "Because the framework treats resistance and acceptance as the same thing",
     "Because the framework says globalization was welcomed everywhere it reached",
     "Because the framework confines responses to a single decade"],
   ans=0,
   why="KC-6.3.IV.iv's own noun is RESPONSES and its own claim is that they took A VARIETY of forms, and the CED's second illustrative example, the advent of locally developed social media, is a locally made alternative rather than a refusal. A bank that read every response as a rejection would narrow the framework's own word, which is what this item exists to prevent."),

 dict(q="A researcher wants to explain why organized responses to globalization appear in a particular country from the 1980s onward rather than earlier. Which line of inquiry does this course's framework make most relevant?",
   choices=[
     "When cultural and economic globalization began to rise in that country",
     "When the country's frontiers were first drawn on a map",
     "When the country's population reached its present size",
     "When the country's first university was founded",
     "When the country's climate last changed measurably"],
   ans=0,
   why="KC-6.3.IV.iv states that the responses were to RISING cultural and economic globalization, which makes the timing of that rise the framework's own explanation for when responses appear. The reasoning process the CED prints beside this topic is causation, and the other lines of inquiry bear on developments the framework treats elsewhere."),

 dict(q="Two accounts describe the same demonstration outside an economic summit: one written by an organizer for supporters, one written by a delegate for colleagues. How should a historian use the pair?",
   choices=[
     "Read each for the position it was written from, since neither was composed to give a neutral account",
     "Prefer the organizer's account, because participants understand their own actions best",
     "Prefer the delegate's account, because officials keep more careful records",
     "Discard both, because interested parties produce no usable evidence",
     "Combine them by averaging their estimates of the numbers present"],
   ans=0,
   why="Skill 2.C asks for the significance of a source's point of view, purpose and audience, which is a question to put to both accounts rather than a rule for ranking them. KC-6.3.IV.iv places responses to rising globalization inside a period in which the parties disagreed, so accounts from the two sides are expected to differ and the difference is itself evidence."),

 dict(q="An unattributed broadcasting authority's minute of 1990 proposes a quota for programmes made within the country. This course would situate the proposal within",
   choices=[
     "responses to rising cultural globalization, of which this is one of the varied forms",
     "responses to rising economic globalization, which the framework treats as unrelated to programming",
     "the political and social changes that led to changes in the arts",
     "the reduction of the problem of geographic distance by new communications",
     "the growth of knowledge economies in some regions of the world"],
   ans=0,
   why="KC-6.3.IV.iv states that responses to rising CULTURAL and economic globalization took a variety of forms, and KC-6.3.IV.ii records that arts, entertainment and popular culture increasingly reflected a globalized society. A quota for home-made programmes is a response to that cultural side, and a regulatory measure is one of the varied forms rather than the only one."),

 dict(q="A commentator writes that the framework's account of this topic tells us whether the responses it describes were justified. Is that correct?",
   choices=[
     "No, because the framework states that responses occurred and varied without judging any of them",
     "Yes, because the framework states that every response was justified",
     "Yes, because the framework states that no response was justified",
     "No, because the framework denies that any response occurred",
     "No, because the framework places all such responses before 1900"],
   ans=0,
   why="KC-6.3.IV.iv states only that responses to rising cultural and economic globalization took a variety of forms. It records their occurrence and their variety and passes no judgement on any of them, and Unit 9 Learning Objective G asks a student to explain the various responses rather than to rank them."),

 dict(q="Which set of developments would this course count as showing the variety of forms responses took?",
   choices=[
     "A public demonstration, a locally built alternative service, and a regulation restricting imports",
     "Three public demonstrations held in the same city in the same week",
     "Three separate accounts of one public demonstration",
     "Three governments signing the same trade agreement",
     "Three firms opening factories in the same country"],
   ans=0,
   why="KC-6.3.IV.iv states that responses took A VARIETY OF FORMS, so what shows the variety is a set of responses different in kind rather than a set of instances of one kind. The CED's own two illustrative examples, activism and the advent of locally developed social media, are themselves two different kinds, which is the pattern the key follows."),

 dict(q="An unattributed trade union bulletin of 1997 objects to a firm's decision to move production abroad. Which of this course's statements does the objection respond to?",
   choices=[
     "That industrial production and manufacturing were increasingly situated in Asia and Latin America",
     "That consumer culture became globalized and transcended national borders",
     "That access to education became more inclusive in much of the world",
     "That diseases associated with poverty persisted through the century",
     "That the redrawing of political boundaries created new states"],
   ans=0,
   why="KC-6.3.I.E states that in the late twentieth century industrial production and manufacturing were increasingly situated in Asia and Latin America, which is the economic development the bulletin is objecting to, and KC-6.3.IV.iv establishes that responses to rising economic globalization took a variety of forms. The key names what is being responded to, not whether the objection was sound."),

 dict(q="A historian argues that responses to globalization cannot be understood by studying protest alone. Which of this course's statements most directly supports that argument?",
   choices=[
     "That responses to rising cultural and economic globalization took a variety of forms",
     "That responses to rising globalization took a single characteristic form",
     "That no response to globalization was ever organized",
     "That responses were confined to the economic side of globalization",
     "That the framework identifies protest as the only response worth studying"],
   ans=0,
   why="KC-6.3.IV.iv states that responses took A VARIETY OF FORMS, which is precisely the claim that studying one form cannot exhaust the subject. Unit 9 Learning Objective G's word is VARIOUS, and the CED's second illustrative example is not a protest at all."),

 dict(q="An unattributed government statement of 1995 announces support for local film production, and an unattributed manifesto of the same year demands the closing of the country's markets to foreign goods. What do the two have in common within this course's framework?",
   choices=[
     "Both are responses to rising globalization, though they answer different sides of it and take different forms",
     "Both are responses to rising cultural globalization taking the same form",
     "Both are responses to rising economic globalization taking the same form",
     "Neither is treated by the framework as a response to globalization",
     "Both are treated by the framework as identical in aim and in method"],
   ans=0,
   why="KC-6.3.IV.iv states that responses to rising CULTURAL AND ECONOMIC globalization took A VARIETY of forms. Support for local film answers the cultural side and a demand to close markets the economic, and a subsidy and a manifesto are different forms, so the pair shows both halves of the framework's sentence at once."),

 dict(q="A researcher assembles a collection of sources produced by people responding to globalization and notices that almost all of them argue a case. What does this course's suggested skill make of that?",
   choices=[
     "That each was produced to persuade someone, which shapes what it can be used to establish",
     "That none of them can be used, since arguing a case disqualifies a source",
     "That all of them are equally reliable, since all argue in the same way",
     "That the collection proves the arguments they make are correct",
     "That sources arguing a case fall outside the period the framework covers"],
   ans=0,
   why="Skill 2.C asks for the significance of a source's purpose, including how it might limit the source's uses. KC-6.3.IV.iv establishes that responses to rising globalization took a variety of forms, and sources produced in the course of responding are made to persuade, which is a property to be reckoned with rather than a disqualification."),

 dict(q="Considered across this topic, what does this course establish about responses to globalization from 1900 to the present?",
   choices=[
     "That they were made, that what they answered was rising cultural and economic globalization, and that they took a variety of forms",
     "That they were made in a single form and against a single target",
     "That they were made only after globalization had ceased to rise",
     "That they were made only against the cultural side of globalization",
     "That the framework records no such responses at any point"],
   ans=0,
   why="KC-6.3.IV.iv is one sentence containing exactly three assertions: that there were responses, that they answered rising cultural and economic globalization, and that they took a variety of forms. The key states all three and each distractor removes or narrows one of them."),

 dict(q="Taking the topic as a whole, which single sentence best states what this course says about resistance to globalization?",
   choices=[
     "As cultural and economic globalization rose, people answered it in many different ways, from organized activism to building local alternatives of their own, and the framework records the variety without ranking the responses",
     "As globalization rose, people everywhere answered it in one identical way, and the framework ranks that way as the correct one",
     "Globalization rose without provoking any response of any kind anywhere in the world",
     "People responded only to the economic side of globalization and never to its cultural side",
     "The framework states which responses to globalization were justified and which were not"],
   ans=0,
   why="KC-6.3.IV.iv states that responses to rising cultural and economic globalization took a variety of forms, and the CED prints activism and the advent of locally developed social media as its two illustrative examples of exactly that variety. The key states the rise, the variety and the framework's silence on the merits, and each distractor contradicts one of those."),
]
