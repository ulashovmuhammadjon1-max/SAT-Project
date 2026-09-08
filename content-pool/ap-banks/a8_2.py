# AP U.S. HISTORY 8.2 The Cold War from 1945 to 1980  (title from US_HISTORY_topics.json)
# Unit 8, Period 8: 1945 to 1980. Thematic focus WOR, America in the World. Reasoning
# process: continuity and change. Suggested skill 2.C, explain the significance of a
# source's point of view, purpose, historical situation, and/or audience, including how
# these might limit the use or uses of a source.
#
# THE REQUIRED COURSE CONTENT OF THIS TOPIC, in the framework's own words. These four
# sentences and the Learning Objective are the only things the keys below rest on:
#
#   Unit 8 Learning Objective B
#       Explain the continuities and changes in Cold War policies from 1945 to 1980.
#
#   KC-8.1.I       United States policymakers engaged in a cold war with the authoritarian
#                  Soviet Union, seeking to limit the growth of Communist military power
#                  and ideological influence, create a free-market global economy, and
#                  build an international security system.
#   KC-8.1.I.A     As postwar tensions dissolved the wartime alliance between Western
#                  democracies and the Soviet Union, the United States developed a foreign
#                  policy based on collective security, international aid, and economic
#                  institutions that bolstered non-Communist nations.
#   KC-8.1.I.B.i   Concerned by expansionist Communist ideology and Soviet repression, the
#                  United States sought to contain communism through a variety of measures,
#                  including major military engagements in Korea.
#   KC-8.1.I.C     The Cold War fluctuated between periods of direct and indirect military
#                  confrontation and periods of mutual coexistence (or detente).
#
# WHAT IS DELIBERATELY NOT KEYED. This topic's page carries a long OPTIONAL SOURCES list
# naming real speeches, telegrams and interviews. The CED says of that list, in its own
# words, that the sources "are not required AP course content" and that "None of the AP
# Exam questions require students to have studied these specific sources." So nothing in
# this module keys a named document, a named policymaker or a named programme. Where a
# question needs a source it uses an explicitly hypothetical one, per HISTORY_BRIEF.md:
# inventing a line and attributing it to a real diplomat would be read by a student as
# fact, and would also be keying content the framework does not require.
#
# NOTATION. The CED prints "(or detente)" with an acute accent. The bank is ASCII only --
# es_check.style refuses a non-ASCII glyph, because a character that survives review and
# then renders wrong is exactly the defect this project has already shipped -- so the word
# is written here without the accent. Nothing turns on it: no key depends on the spelling,
# and the framework's own phrase "periods of mutual coexistence" is used throughout.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table=, and
# every figure in them is labelled hypothetical in the stem.
# PROSE ONLY: a span of years is written "1945 to 1980", never with a hyphen.
# FIVE choices (A-E). Invented sources are marked hypothetical.
TOPIC = ("8.2", "The Cold War from 1945 to 1980", 8)

_T_AID = dict(
    headers=["Category of assistance (hypothetical record)",
             "Amount recorded in 1948 (units)",
             "Amount recorded in 1958 (units)"],
    rows=[["Collective security commitments", "120", "260"],
          ["International aid", "300", "180"],
          ["Support for economic institutions", "90", "210"]])

_T_PHASES = dict(
    headers=["Stretch of years (hypothetical record)",
             "Character the record assigns to it"],
    rows=[["1948 to 1953", "Direct or indirect military confrontation"],
          ["1954 to 1958", "Mutual coexistence"],
          ["1959 to 1963", "Direct or indirect military confrontation"],
          ["1964 to 1968", "Mutual coexistence"]])

_T_ENGAGE = dict(
    headers=["Year (hypothetical record)",
             "Nations bound by recorded collective security agreements",
             "Nations receiving recorded international aid"],
    rows=[["1947", "5", "8"],
          ["1952", "14", "21"],
          ["1957", "22", "29"],
          ["1962", "27", "34"]])

QUESTIONS = [

 dict(q="Unit 8 Learning Objective B states what students should be able to explain about Cold "
        "War policies. What does the framework ask for?",
      choices=[
        "The continuities and changes in Cold War policies from 1945 to 1980",
        "The causes and effects of the Red Scare after World War II",
        "The various military and diplomatic responses to international developments over time",
        "The causes and effects of the Vietnam War",
        "The context for societal change from 1945 to 1980"],
      ans=0,
      why="Unit 8 Learning Objective B reads 'Explain the continuities and changes in Cold War "
          "policies from 1945 to 1980.' The rejected options are Learning Objectives C, H, I and "
          "A of the same unit, each printed beside a different topic, so each names a real task "
          "of the course but not the one this topic sets."),

 dict(q="KC-8.1.I says United States policymakers sought to limit the growth of something. Which "
        "two forms does the sentence name?",
      choices=[
        "Communist military power and ideological influence",
        "Communist military power and colonial territory",
        "Communist trade and cultural exchange",
        "Soviet population and industrial output",
        "Communist ideological influence considered on its own"],
      ans=0,
      why="KC-8.1.I states that policymakers sought 'to limit the growth of Communist military "
          "power and ideological influence', which pairs an armed capacity with a capacity to "
          "persuade. Colonial territory, trade, cultural exchange, population and industrial "
          "output are not what that clause names, and keeping only the ideological half drops "
          "the military one."),

 dict(q="KC-8.1.I.A opens by describing something that dissolved. What dissolved, and what "
        "dissolved it?",
      choices=[
        "The wartime alliance between Western democracies and the Soviet Union, dissolved by "
        "postwar tensions",
        "The wartime alliance between Western democracies and the Soviet Union, dissolved by a "
        "formal treaty of separation",
        "The alliance between the Soviet Union and its neighbours, dissolved by postwar tensions",
        "The economic institutions of the prewar world, dissolved by postwar tensions",
        "The alliance the Western democracies had made with one another, dissolved by postwar "
        "tensions"],
      ans=0,
      why="KC-8.1.I.A begins 'As postwar tensions dissolved the wartime alliance between Western "
          "democracies and the Soviet Union', so the alliance is the one that had joined the "
          "Western democracies TO the Soviet Union and the agent is tension rather than any "
          "formal act. Each rejected option keeps one of those two elements and alters the "
          "other."),

 dict(q="On what three things does KC-8.1.I.A say the United States based the foreign policy it "
        "developed?",
      choices=[
        "Collective security, international aid, and economic institutions that bolstered "
        "non-Communist nations",
        "Collective security, territorial annexation, and a withdrawal from European affairs",
        "International aid, general disarmament, and neutrality between the two blocs",
        "Economic institutions, colonial administration, and the suppression of foreign trade",
        "Collective security, international aid, and economic institutions that bolstered every "
        "nation equally"],
      ans=0,
      why="KC-8.1.I.A names a foreign policy 'based on collective security, international aid, "
          "and economic institutions that bolstered non-Communist nations'. The last option keeps "
          "all three headings and removes the qualification, which is the likeliest error here, "
          "since the framework's own wording ties the institutions to one side of the division."),

 dict(q="KC-8.1.I.B.i names two things that concerned the United States and led it to seek "
        "containment. Which pair does the framework give?",
      choices=[
        "Expansionist Communist ideology and Soviet repression",
        "Expansionist Communist ideology and a shortage of raw materials",
        "Soviet repression and the collapse of European colonial empires",
        "The growth of world trade and Soviet repression",
        "Expansionist Communist ideology taken by itself"],
      ans=0,
      why="KC-8.1.I.B.i opens 'Concerned by expansionist Communist ideology and Soviet "
          "repression', so the framework gives a doctrine and a practice together as the reason "
          "for containment. Raw materials, colonial collapse and world trade appear nowhere in "
          "the sentence, and reducing the pair to one term drops half of the stated concern."),

 dict(q="KC-8.1.I.B.i says the United States sought to contain communism through a variety of "
        "measures, INCLUDING major military engagements in Korea. What does that word establish?",
      choices=[
        "That the military engagements were one kind of measure among several the sentence groups "
        "together",
        "That military engagement was the only measure the United States employed",
        "That the framework places military engagement outside containment",
        "That containment began only once fighting had started",
        "That the measures the framework has in mind were all economic rather than military"],
      ans=0,
      why="KC-8.1.I.B.i says containment was sought 'through a variety of measures, including "
          "major military engagements in Korea', and a variety that INCLUDES something is not "
          "exhausted by it. The sentence therefore neither confines containment to fighting, nor "
          "excludes fighting from it, nor dates containment from the fighting's start."),

 dict(q="According to KC-8.1.I.C, what pattern did the Cold War follow?",
      choices=[
        "It fluctuated between periods of direct and indirect military confrontation and periods "
        "of mutual coexistence",
        "It moved once from confrontation to coexistence and stayed there",
        "It consisted of continuous direct military confrontation throughout",
        "It consisted of continuous mutual coexistence throughout",
        "It alternated between confrontation and formal alliance with the Soviet Union"],
      ans=0,
      why="KC-8.1.I.C states that the Cold War fluctuated between periods of direct and indirect "
          "military confrontation and periods of mutual coexistence. To fluctuate is to move back "
          "and forth, which rules out a single transition, an unvarying state of either kind, and "
          "a return to the alliance KC-8.1.I.A says postwar tensions had dissolved."),

 dict(q="Taking KC-8.1.I together with KC-8.1.I.C, which statement best captures a continuity "
        "and a change in Cold War policy across the period?",
      choices=[
        "The aim of limiting Communist power persisted, while the level of confrontation rose "
        "and fell",
        "The aim of limiting Communist power was abandoned, while the level of confrontation "
        "held steady",
        "Both the aim and the level of confrontation held steady throughout",
        "Both the aim and the level of confrontation were reversed at a single moment",
        "The framework describes neither the aim nor the level of confrontation"],
      ans=0,
      why="KC-8.1.I states the aims policymakers pursued in engaging in a cold war and reports no "
          "abandonment of them, while KC-8.1.I.C describes the Cold War fluctuating between "
          "confrontation and coexistence. That is a persisting purpose and a varying intensity, "
          "which is what Unit 8 Learning Objective B asks students to separate."),

 dict(q="KC-8.1.I.C distinguishes direct from indirect military confrontation. What does "
        "including both in one phrase tell a reader?",
      choices=[
        "That the framework counts confrontations conducted at a remove as well as those between "
        "the two powers themselves",
        "That only confrontations between the two powers themselves belong to the Cold War",
        "That indirect confrontation belongs among the periods of mutual coexistence",
        "That the two kinds of confrontation never occurred within the same period",
        "That the framework treats confrontation and coexistence as the same condition"],
      ans=0,
      why="KC-8.1.I.C groups 'direct and indirect military confrontation' on one side of its "
          "contrast and 'periods of mutual coexistence' on the other, so indirect confrontation "
          "counts as confrontation rather than as coexistence, and the pairing widens rather than "
          "narrows what the framework includes."),

 dict(q="The suggested skill printed beside this topic is 2.C. How does the framework state it?",
      choices=[
        "Explain the significance of a source's point of view, purpose, historical situation, "
        "and audience, including how these might limit the use or uses of a source",
        "Explain the point of view, purpose, historical situation, or audience of a source",
        "Compare the arguments or main ideas of two sources",
        "Identify patterns among or connections between historical developments and processes",
        "Explain a historical concept, development, or process"],
      ans=0,
      why="Skill 2.C is printed beside this topic as the skill students practise while meeting "
          "Unit 8 Learning Objective B, and it asks them to explain the significance of a "
          "source's point of view, purpose, historical situation, and audience, including how "
          "these might limit the use or uses of a source. Skill 2.B, the near neighbour, stops at "
          "explaining those features and does not reach their limiting effect; the others are "
          "skills 3.C, 5.A and 1.B."),

 dict(q="A hypothetical diplomatic dispatch of 1947, sent from an allied capital, argues that "
        "the wartime partnership with the Soviet Union has ended and that the United States must "
        "now build lasting commitments with other governments. Which sentence of this topic does "
        "it most directly illustrate?",
      choices=[
        "KC-8.1.I.A, on postwar tensions dissolving the wartime alliance and a foreign policy "
        "built on collective security",
        "KC-8.1.I.C, on the Cold War fluctuating between confrontation and mutual coexistence",
        "KC-8.1.I.B.i, on containment sought through a variety of measures including major "
        "military engagements",
        "KC-8.1.I, on the aim of creating a free-market global economy",
        "Unit 8 Learning Objective B, which states the span of years rather than a development"],
      ans=0,
      why="KC-8.1.I.A is the sentence that joins the dissolution of the wartime alliance to the "
          "development of a foreign policy based on collective security, international aid and "
          "economic institutions, which is exactly the pair of claims the dispatch makes. The "
          "other options name real content of the topic that the dispatch does not address."),

 dict(q="A hypothetical report on conditions in a foreign capital was written by an officer of "
        "the same government that was funding aid to that capital. Applying skill 2.C, which "
        "limitation follows most directly from the source's point of view?",
      choices=[
        "Its author had an interest in the aid programme appearing successful, so favourable "
        "findings need corroboration from elsewhere",
        "Its author was writing at the time described, which by itself makes the source useless",
        "Its author wrote in prose rather than in figures, which by itself makes the source "
        "unreliable",
        "It was written for a government, so nothing in it can be true",
        "It concerns a foreign capital, so it cannot bear on United States policy"],
      ans=0,
      why="KC-8.1.I.A makes international aid one basis of United States foreign policy, and "
          "skill 2.C asks how a source's point of view might limit its use. An author reporting "
          "on a programme his own government funds has a stake in the finding, which is a reason "
          "to seek corroboration rather than a reason to discard the source; being contemporary, "
          "being written in prose or being official are none of them grounds for dismissal."),

 dict(q="A hypothetical pamphlet printed in 1950 for readers abroad describes American "
        "prosperity and invites them to compare it with life under Communist rule. Applying "
        "skill 2.C, what does its purpose tell a reader about its use as evidence?",
      choices=[
        "It was made to persuade a foreign audience, so it is strong evidence of what the United "
        "States wished such audiences to believe and weak evidence of conditions themselves",
        "It was made to persuade a foreign audience, so it is strong evidence of conditions "
        "inside the United States",
        "It was made for foreign readers, so it tells a reader nothing about American aims",
        "Its purpose cannot be recovered from the pamphlet itself",
        "Its purpose makes it useful only for the history of printing"],
      ans=0,
      why="KC-8.1.I names limiting Communist ideological influence among the aims of policy, so a "
          "persuasive pamphlet aimed abroad is direct evidence of that aim. Skill 2.C asks how "
          "purpose limits use: a document written to persuade reports its makers' intentions "
          "reliably and the conditions it describes much less so, which is why the two halves of "
          "the key have to be held together."),

 dict(q="A hypothetical set of instructions circulated only among senior officials and a "
        "hypothetical public address given the same week make different arguments about the same "
        "policy. Applying skill 2.C, what does the difference in audience most reasonably "
        "suggest?",
      choices=[
        "Each was shaped for the people who would read or hear it, so the two must be weighed "
        "against each other rather than either taken as the whole policy",
        "The public address must be the truthful one, because it was delivered openly",
        "The confidential instructions must be the truthful one, because they were secret",
        "The difference in audience has no bearing on how either should be read",
        "Neither can be used as evidence about the policy"],
      ans=0,
      why="Skill 2.C makes audience one of the features whose significance a student must "
          "explain, and Unit 8 Learning Objective B asks for continuities and changes in policy, "
          "which no single document establishes. Treating either audience as automatically "
          "truthful substitutes a rule for the comparison the skill actually calls for."),

 dict(q="A hypothetical newspaper editorial written during a stretch of years the framework "
        "would place among periods of mutual coexistence urges patience with the Soviet Union. "
        "Applying skill 2.C, what does its historical situation most directly explain?",
      choices=[
        "That the argument belongs to a phase of the Cold War in which confrontation had eased, "
        "and need not represent the whole period",
        "That the argument represents United States policy across the entire span from 1945 to "
        "1980",
        "That the argument shows the Cold War had come to an end",
        "That the editorial's date is what makes it useless as evidence",
        "That the framework records no phases in which confrontation eased"],
      ans=0,
      why="KC-8.1.I.C states that the Cold War fluctuated between periods of confrontation and "
          "periods of mutual coexistence, so a source produced in one phase is evidence for that "
          "phase and not for the whole. Coexistence in the framework's sense is a phase of the "
          "Cold War rather than its end, and a date situates a source rather than disqualifying "
          "it."),

 dict(q="The table records hypothetical amounts of assistance under three headings ten years "
        "apart. Which conclusion does the table alone support?",
      table=_T_AID,
      choices=[
        "Two of the three recorded categories rise while the third falls, and the recorded total "
        "is larger in the later year",
        "Every recorded category is larger in the later year than in the earlier one",
        "Every recorded category is smaller in the later year than in the earlier one",
        "One recorded category falls to nothing by the later year",
        "The three categories are recorded at equal amounts in both years"],
      ans=0,
      why="KC-8.1.I.A names collective security, international aid, and economic institutions "
          "together as the bases of the foreign policy the United States developed, so a shifting "
          "mix among the three is a change in method rather than in purpose, which is the "
          "distinction Unit 8 Learning Objective B asks for. The figures are hypothetical and "
          "every reading offered is recomputed from the table alone in the verifier."),

 dict(q="Using the hypothetical record of successive stretches of years, which conclusion does "
        "the table alone support about the pattern it shows?",
      table=_T_PHASES,
      choices=[
        "The character assigned alternates from one stretch to the next rather than changing once "
        "and holding",
        "The record assigns the same character to every stretch",
        "The record moves from confrontation to coexistence once and then holds",
        "The record assigns three or more distinct characters across the stretches",
        "The record assigns no character to the earliest stretch"],
      ans=0,
      why="KC-8.1.I.C states that the Cold War fluctuated between periods of direct and indirect "
          "military confrontation and periods of mutual coexistence, and alternation is what "
          "fluctuation looks like when it is set out stretch by stretch. The stretches are "
          "hypothetical and the alternation, with the falsity of every rejected reading, is "
          "recomputed from the table alone."),

 dict(q="Using the hypothetical counts of nations, which statement does the record support?",
      table=_T_ENGAGE,
      choices=[
        "Both counts rise at every reading, and in every year recorded more nations receive aid "
        "than are bound by security agreements",
        "Both counts rise at every reading, and in every year recorded more nations are bound by "
        "security agreements than receive aid",
        "The count of nations bound by security agreements falls at least once",
        "The two counts are equal in every year recorded",
        "The count of nations receiving aid falls at least once"],
      ans=0,
      why="KC-8.1.I.A names collective security and international aid as two bases of the same "
          "foreign policy, so a record in which both widen together is evidence about that policy "
          "rather than about either instrument alone. The counts are hypothetical and both the "
          "direction of each column and the relation between them are recomputed from the table "
          "alone in the verifier."),

 dict(q="A hypothetical veteran's testimony, recorded decades after the fighting in Korea, "
        "describes his unit's experience. Which limitation does the source's historical situation "
        "most directly create?",
      choices=[
        "It was recorded long after the events, so memory and later knowledge may shape what it "
        "reports",
        "It concerns Korea, which the framework does not treat as part of containment",
        "It is testimony rather than a document, so it cannot serve as evidence at all",
        "It was given by a participant, so his account of his own unit is worthless",
        "It describes fighting, so it can bear on no question of policy"],
      ans=0,
      why="KC-8.1.I.B.i names major military engagements in Korea among the measures by which the "
          "United States sought to contain communism, so the subject is squarely within the "
          "topic and the second option is false. Skill 2.C locates the real limitation in the "
          "source's historical situation: an account given long afterwards is shaped by what has "
          "happened since, which is a reason to read it carefully rather than to discard it."),

 dict(q="Which of the following does KC-8.1.I.A NOT name as a basis of the foreign policy the "
        "United States developed?",
      choices=[
        "The annexation of territory from defeated states",
        "Collective security",
        "International aid",
        "Economic institutions that bolstered non-Communist nations",
        "A response to postwar tensions with the Soviet Union"],
      ans=0,
      why="KC-8.1.I.A names collective security, international aid, and economic institutions "
          "that bolstered non-Communist nations, and it opens with the postwar tensions that "
          "dissolved the wartime alliance. Annexation of territory appears nowhere in the "
          "sentence or anywhere else in this topic's required content."),

 dict(q="KC-8.1.I.B.i gives both a reason and a method. Which option pairs them as the framework "
        "does?",
      choices=[
        "Concern at expansionist Communist ideology and Soviet repression was the reason, and "
        "containment through a variety of measures was the method",
        "Containment through a variety of measures was the reason, and concern at expansionist "
        "Communist ideology was the method",
        "Concern at Soviet repression was the reason, and the building of a free-market global "
        "economy was the method",
        "The collapse of the wartime alliance was the reason, and mutual coexistence was the "
        "method",
        "Major military engagement was the reason, and Soviet repression was the method"],
      ans=0,
      why="KC-8.1.I.B.i reads 'Concerned by expansionist Communist ideology and Soviet "
          "repression, the United States sought to contain communism through a variety of "
          "measures', which puts the concern in the causal position and containment in the "
          "instrumental one. Exchanging them inverts the sentence, and the remaining options "
          "borrow terms from KC-8.1.I, KC-8.1.I.A and KC-8.1.I.C that the sentence does not pair."),

 dict(q="KC-8.1.I.A, KC-8.1.I.B.i and KC-8.1.I.C are printed beneath KC-8.1.I on this topic's "
        "page. What does that arrangement indicate?",
      choices=[
        "That each develops part of the engagement in a cold war that KC-8.1.I states in general "
        "terms",
        "That each contradicts the general statement printed above it",
        "That the three sub-points concern the years before 1945",
        "That KC-8.1.I summarises developments belonging to a different unit",
        "That the sub-points replace the general statement rather than developing it"],
      ans=0,
      why="KC-8.1.I states the engagement and its aims in general terms; KC-8.1.I.A supplies the "
          "policy that was built, KC-8.1.I.B.i the reason and method of containment, and "
          "KC-8.1.I.C the rhythm the confrontation took. Each is consistent with the sentence "
          "above it and adds detail to it, which is what a lettered sub-point in this framework "
          "does."),

 dict(q="A hypothetical memorandum from an association of exporters in 1949 urges the government "
        "to help rebuild markets abroad so that American goods will have buyers. Which of "
        "KC-8.1.I's stated aims does it most directly bear on?",
      choices=[
        "The aim of creating a free-market global economy",
        "The aim of limiting the growth of Communist military power",
        "The aim of building an international security system",
        "The aim of exposing suspected communists within the United States",
        "The aim of limiting the growth of Communist ideological influence"],
      ans=0,
      why="KC-8.1.I lists creating a free-market global economy among the things policymakers "
          "sought, and a request for help in rebuilding foreign markets is an argument for "
          "exactly that. Military power, an international security system and ideological "
          "influence are the sentence's other aims and are not what the memorandum addresses; "
          "exposing suspected communists at home belongs to KC-8.1.II.A and to topic 8.3."),

 dict(q="A hypothetical government circular of 1953 states that the administration's policy "
        "toward the Soviet Union has not changed. Why is that single source insufficient to "
        "establish the continuities Learning Objective B asks students to explain?",
      choices=[
        "A statement made in one year cannot by itself show what held across the whole span from "
        "1945 to 1980",
        "A government circular is never evidence of government policy",
        "The claim concerns the Soviet Union, which this topic does not discuss",
        "Continuity cannot be established from written sources at all",
        "The circular comes from inside the period, which disqualifies it"],
      ans=0,
      why="Unit 8 Learning Objective B asks for the continuities and changes in Cold War policies "
          "across 1945 to 1980, which is a claim about a span rather than about a moment, and "
          "skill 2.C makes a source's historical situation a limit on its use. The circular is "
          "relevant evidence about 1953 and about what the administration wished to assert; it is "
          "the reach of the claim, not the kind of document, that the single source cannot cover."),

 dict(q="Which statement about Cold War policy is NOT supported by this topic's required "
        "content?",
      choices=[
        "The United States pursued containment solely through military engagement",
        "The United States developed a foreign policy resting in part on international aid",
        "The Cold War included periods of mutual coexistence",
        "Postwar tensions dissolved the wartime alliance with the Soviet Union",
        "Policymakers sought to build an international security system"],
      ans=0,
      why="KC-8.1.I.B.i says containment was sought 'through a variety of measures, including "
          "major military engagements', which makes fighting one measure among several rather "
          "than the whole. The four rejected statements restate KC-8.1.I.A, KC-8.1.I.C, "
          "KC-8.1.I.A again and KC-8.1.I in nearly the framework's own words."),

 dict(q="A hypothetical revision guide summarises the Cold War as a steady increase in hostility "
        "from 1945 to 1980. Which sentence of this topic most directly qualifies that summary?",
      choices=[
        "KC-8.1.I.C, which describes fluctuation between confrontation and periods of mutual "
        "coexistence",
        "KC-8.1.I.A, which describes a foreign policy built on collective security and "
        "international aid",
        "KC-8.1.I.B.i, which describes containment sought through a variety of measures",
        "KC-8.1.I, which describes the engagement with the authoritarian Soviet Union",
        "Unit 8 Learning Objective B, which states the span of years the topic covers"],
      ans=0,
      why="A steady increase and a fluctuation are different shapes, and KC-8.1.I.C is the "
          "sentence that asserts the second: the Cold War moved between periods of direct and "
          "indirect military confrontation and periods of mutual coexistence. The other "
          "statements are compatible with either shape and so cannot by themselves correct the "
          "summary."),

 dict(q="KC-8.1.I.A says the economic institutions the United States helped build bolstered "
        "non-Communist nations. What does that qualification establish?",
      choices=[
        "That the support described was directed by the terms of the Cold War division rather "
        "than offered without regard to it",
        "That the institutions were open to every nation on equal terms",
        "That the institutions were military rather than economic in character",
        "That the institutions operated only inside the United States",
        "That the framework does not say whom the institutions supported"],
      ans=0,
      why="KC-8.1.I.A specifies that the institutions bolstered NON-COMMUNIST nations, which "
          "names the recipients by their side in the division KC-8.1.I describes. The sentence "
          "therefore does say whom they supported, calls them economic, and places them abroad as "
          "part of a foreign policy."),

 dict(q="A hypothetical agreement among several governments in 1949 provides that an attack on "
        "any one of them will be treated as an attack on all. Which element of KC-8.1.I.A does it "
        "illustrate?",
      choices=[
        "Collective security",
        "International aid",
        "Economic institutions that bolstered non-Communist nations",
        "Mutual coexistence between the two powers",
        "Containment pursued through major military engagement"],
      ans=0,
      why="KC-8.1.I.A names collective security as the first basis of the foreign policy the "
          "United States developed, and an undertaking to treat an attack on one as an attack on "
          "all is what that phrase describes. Aid and economic institutions are the sentence's "
          "other two bases, mutual coexistence belongs to KC-8.1.I.C, and military engagement is "
          "KC-8.1.I.B.i's example of a containment measure."),

 dict(q="A hypothetical dispatch of 1950 urges an immediate military response to a Communist "
        "advance, while a hypothetical dispatch of 1968 urges negotiation with the same "
        "adversary. Read together and set against this topic's content, what do they best "
        "illustrate?",
      choices=[
        "The fluctuation KC-8.1.I.C describes between confrontation and periods of mutual "
        "coexistence",
        "A change in the American aim of limiting Communist military power",
        "The dissolution of the wartime alliance described in KC-8.1.I.A",
        "The abandonment of collective security as a basis of policy",
        "A disagreement the framework says never arose"],
      ans=0,
      why="KC-8.1.I.C states that the Cold War fluctuated between periods of direct and indirect "
          "military confrontation and periods of mutual coexistence, and two sources eighteen "
          "years apart urging opposite courses are what that fluctuation looks like from inside. "
          "Nothing in the pair shows the aims of KC-8.1.I changing or collective security being "
          "given up, and the alliance had dissolved before either was written."),

 dict(q="Taken together, what do this topic's four required sentences establish about Cold War "
        "policy from 1945 to 1980?",
      choices=[
        "A steady set of aims pursued by several kinds of measure, at an intensity that rose and "
        "fell across the period",
        "A single aim pursued by a single measure at a constant intensity",
        "Aims that changed completely every few years and were pursued by no settled method",
        "A policy of neutrality between the two blocs, maintained without variation",
        "A policy the framework describes only in its economic aspects"],
      ans=0,
      why="KC-8.1.I gives the aims and reports no change in them, KC-8.1.I.A and KC-8.1.I.B.i "
          "give the several kinds of measure through which they were pursued, and KC-8.1.I.C "
          "gives the fluctuation in intensity. That combination of constant purpose and varying "
          "means and intensity is what Unit 8 Learning Objective B asks students to explain."),
]
