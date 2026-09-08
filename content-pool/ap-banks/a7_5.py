# AP U.S. HISTORY 7.5 World War I: Military and Diplomacy
# (title copied from US_HISTORY_topics.json)
# Unit 7, Period 7: 1890 to 1945. Thematic focus: America in the World (WOR). Reasoning
# process: causation. Suggested skill 2.C, explain the significance of a source's point of
# view, purpose, historical situation, and/or audience, including how these might limit
# the use(s) of a source.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 7 Learning Objective F
#       Explain the causes and consequences of U.S. involvement in World War I.
#
#   KC-7.3.II    World War I and its aftermath intensified ongoing debates about the
#                nation's role in the world and how best to achieve national security and
#                pursue American interests.  (the concept the lettered points sit under)
#   KC-7.3.II.A  After initial neutrality in World War I, the nation entered the conflict,
#                departing from the U.S. foreign policy tradition of noninvolvement in
#                European affairs, in response to Woodrow Wilson's call for the defense of
#                humanitarian and democratic principles.
#   KC-7.3.II.B  Although the American Expeditionary Forces played a relatively limited
#                role in combat, the United States' entry helped to tip the balance of the
#                conflict in favor of the Allies.
#   KC-7.3.II.C  Despite Wilson's deep involvement in postwar negotiations, the U.S.
#                Senate refused to ratify the Treaty of Versailles or join the League
#                of Nations.
#
# THE TWO CONCESSIVE SENTENCES ARE THE WHOLE DIFFICULTY OF THIS TOPIC, and half of them
# is the commonest way to get it wrong:
#   * KC-7.3.II.B says the American Expeditionary Forces played a relatively limited role
#     in combat AND that the entry helped tip the balance in favour of the Allies. Keeping
#     either half alone -- a decisive army, or an entry that changed nothing -- misreports
#     the sentence in the two opposite directions a student is most likely to take.
#   * KC-7.3.II.C says Wilson was deeply involved in postwar negotiations AND that the
#     U.S. SENATE refused to ratify the Treaty of Versailles or join the League of
#     Nations. Again both halves are load-bearing, and the refusing body is the Senate.
#   Items 7, 8, 9, 13, 15, 27, 28, 29 and 30 turn on those pairs, and every anchor keyed
#   to one carries BOTH clauses.
#
# WHAT IS DELIBERATELY NOT KEYED. No battle, campaign, general, casualty figure, troop
# total, submarine, telegram or date of entry: the CED prints none of them on this page.
# Woodrow Wilson is named because KC-7.3.II.A and KC-7.3.II.C name him, and NOTHING IS
# QUOTED FROM HIM -- the framework reports a call for the defense of humanitarian and
# democratic principles and gives no words, so no words are invented here. The home front
# is topic 7.6 and interwar policy is topic 7.11; items 25 and 26 key those boundaries
# rather than crossing them.
#
# SOURCES. The bank cannot show images, so every stimulus is an explicitly hypothetical
# textual source or a table of explicitly illustrative data whose keyed conclusion is
# recoverable from the table alone. PROSE ONLY, no LaTeX, spans written with "to".
TOPIC = ("7.5", "World War I: Military and Diplomacy", 7)

_T_FORCES = dict(
    headers=["Allied combatant state (illustrative)",
             "Months recorded in the fighting",
             "Share of allied divisions in the final months (percent)"],
    rows=[["State M", "50", "38"],
          ["State N", "49", "22"],
          ["State P", "18", "40"]])

_T_PROPOSALS = dict(
    headers=["Postwar proposal in a hypothetical record",
             "Pursued by the head of government in the negotiations",
             "Approved by the legislature afterwards"],
    rows=[["Proposal 1", "Yes", "No"],
          ["Proposal 2", "Yes", "No"],
          ["Proposal 3", "No", "No"],
          ["Proposal 4", "Yes", "Yes"]])

QUESTIONS = [

 dict(q="Unit 7's Learning Objective F, which this topic serves, asks students to explain "
        "what?",
      choices=[
        "The causes and consequences of U.S. involvement in World War I",
        "The effects of the Spanish-American War",
        "The causes and effects of international and internal migration patterns over time",
        "How and why U.S. participation in World War II transformed American society",
        "The similarities and differences in attitudes about the nation's proper role in the "
        "world"],
      ans=0,
      why="Unit 7 Learning Objective F reads 'Explain the causes and consequences of U.S. "
          "involvement in World War I', and KC-7.3.II.A, KC-7.3.II.B and KC-7.3.II.C are "
          "printed under it. The other four are the objectives of topics 7.3, 7.6, 7.12 and "
          "7.2, each printed on its own page."),

 dict(q="What does KC-7.3.II.A say the United States did BEFORE it entered the conflict?",
      choices=[
        "It was initially neutral",
        "It joined the fighting at the outbreak of the war",
        "It formed an alliance with the Allies in advance",
        "It offered to arbitrate the dispute and was refused",
        "It declared war and then withdrew"],
      ans=0,
      why="KC-7.3.II.A opens 'After initial neutrality in World War I, the nation entered the "
          "conflict', so neutrality comes first and entry follows. An immediate entry, a "
          "prior alliance, an arbitration and a withdrawal are none of them in the sentence."),

 dict(q="From what does KC-7.3.II.A say the entry into the conflict departed?",
      choices=[
        "The U.S. foreign policy tradition of noninvolvement in European affairs",
        "The U.S. foreign policy tradition of involvement in European affairs",
        "The tradition of territorial expansion in the Western Hemisphere",
        "The tradition of relying on international arbitration",
        "The framework names no tradition it departed from"],
      ans=0,
      why="KC-7.3.II.A states that the nation entered the conflict, departing from the U.S. "
          "foreign policy tradition of noninvolvement in European affairs. The second option "
          "reverses the tradition, and expansion in the Western Hemisphere belongs to "
          "KC-7.3.I rather than to this sentence."),

 dict(q="In response to what does KC-7.3.II.A say the nation entered the conflict?",
      choices=[
        "Woodrow Wilson's call for the defense of humanitarian and democratic principles",
        "A vote of the Senate rejecting continued neutrality",
        "A request from the League of Nations",
        "The perception that the western frontier was closed",
        "The suppression of a nationalist movement in the Philippines"],
      ans=0,
      why="KC-7.3.II.A states that the nation entered the conflict in response to Woodrow "
          "Wilson's call for the defense of humanitarian and democratic principles. The "
          "League of Nations appears in KC-7.3.II.C, after the war, the closed frontier in "
          "KC-7.3.I.A and the suppression in KC-7.3.I.C, and no Senate vote on neutrality is "
          "named anywhere on this page."),

 dict(q="A student places the entry into World War I before the period of neutrality. Which "
        "word in KC-7.3.II.A settles the order?",
      choices=[
        "AFTER, in the phrase 'After initial neutrality in World War I, the nation entered "
        "the conflict'",
        "DEPARTING, in the phrase about the tradition of noninvolvement",
        "RESPONSE, in the phrase about the call for humanitarian and democratic principles",
        "INITIAL, which the framework applies to the entry rather than to the neutrality",
        "No word in the sentence fixes the order of the two"],
      ans=0,
      why="KC-7.3.II.A opens with the word AFTER, which puts the initial neutrality before "
          "the entry into the conflict. 'Departing' describes what the entry broke with, "
          "'response' names what it answered, and 'initial' qualifies the neutrality rather "
          "than the entry, so none of those three fixes the sequence."),

 dict(q="What does the word DEPARTING establish in KC-7.3.II.A?",
      choices=[
        "That entry broke with an established U.S. practice rather than continuing it",
        "That entry continued an established U.S. practice",
        "That the United States left the conflict once it had entered",
        "That European states abandoned their own traditions",
        "That the tradition of noninvolvement began with the war"],
      ans=0,
      why="KC-7.3.II.A says the nation entered the conflict, DEPARTING FROM the U.S. foreign "
          "policy tradition of noninvolvement in European affairs, so the entry is a break "
          "with an existing tradition. It is not a continuation, not a departure from the "
          "war, and the tradition is described as already in place rather than as beginning "
          "then."),

 dict(q="What does KC-7.3.II.B say about the role the American Expeditionary Forces played in "
        "combat?",
      choices=[
        "That it was relatively limited",
        "That it was the decisive element in every theatre",
        "That it consisted of naval action alone",
        "That it began before the United States entered the conflict",
        "That the framework does not describe it"],
      ans=0,
      why="KC-7.3.II.B opens 'Although the American Expeditionary Forces played a relatively "
          "limited role in combat', which is the framework's own description. A decisive role "
          "in every theatre overstates it, and the sentence says nothing about naval action "
          "or about any activity before the entry KC-7.3.II.A describes."),

 dict(q="What does KC-7.3.II.B say the United States' entry helped to do?",
      choices=[
        "Tip the balance of the conflict in favor of the Allies",
        "End the fighting without further combat",
        "Bring the Central Powers into a negotiated alliance",
        "Establish the League of Nations during the fighting",
        "Restore the tradition of noninvolvement in European affairs"],
      ans=0,
      why="KC-7.3.II.B states that the United States' entry helped to tip the balance of the "
          "conflict in favor of the Allies. The League of Nations appears in KC-7.3.II.C as "
          "part of the postwar settlement, and the sentence describes neither an end without "
          "combat, nor an alliance with the Central Powers, nor a return to the tradition "
          "KC-7.3.II.A says the entry departed from."),

 dict(q="Which statement carries the whole of what KC-7.3.II.B asserts?",
      choices=[
        "The American Expeditionary Forces played a relatively limited role in combat, and "
        "the entry still helped tip the balance in favor of the Allies",
        "The American Expeditionary Forces played the decisive combat role, and the entry "
        "tipped the balance in favor of the Allies",
        "The American Expeditionary Forces played a relatively limited role in combat, and "
        "the entry therefore made little difference to the outcome",
        "The American Expeditionary Forces played a relatively limited role in combat, and "
        "the balance tipped against the Allies",
        "The framework declines to say what difference the entry made"],
      ans=0,
      why="KC-7.3.II.B is built on ALTHOUGH: a relatively limited role in combat on one side "
          "of it and an entry that helped tip the balance in favor of the Allies on the "
          "other. Keeping only the first half gives an entry that made little difference; "
          "keeping only the second gives a decisive army; and reversing the direction of the "
          "balance contradicts the sentence outright."),

 dict(q="A student asks which engagements KC-7.3.II.B credits the American Expeditionary "
        "Forces with. What is the answer?",
      choices=[
        "The sentence names no engagement and gives no figure for the forces involved",
        "It names one engagement on the western front",
        "It names the engagements but not the year",
        "It gives the number of troops but names no engagement",
        "It says the forces saw no combat at all"],
      ans=0,
      why="KC-7.3.II.B states that the American Expeditionary Forces played a relatively "
          "limited role in combat and that the entry helped tip the balance in favor of the "
          "Allies, and it names no battle, no commander, no date and no number. It also does "
          "not say the forces saw no combat, since a relatively limited role in combat is "
          "still a role in combat."),

 dict(q="What does KC-7.3.II.C say about Wilson and the postwar negotiations?",
      choices=[
        "That he was deeply involved in them",
        "That he took no part in them",
        "That he sent the Senate to conduct them",
        "That he withdrew from them before they concluded",
        "That the framework does not say who conducted them for the United States"],
      ans=0,
      why="KC-7.3.II.C opens 'Despite Wilson's deep involvement in postwar negotiations', so "
          "the framework states his involvement and then contrasts it with what followed at "
          "home. It does not describe an absence, a delegation to the Senate or a withdrawal."),

 dict(q="What does KC-7.3.II.C say the U.S. Senate refused to do?",
      choices=[
        "Ratify the Treaty of Versailles or join the League of Nations",
        "Ratify the Treaty of Versailles, while agreeing to join the League of Nations",
        "Join the League of Nations, while ratifying the Treaty of Versailles",
        "Fund the American Expeditionary Forces after the fighting ended",
        "Recognise the postwar negotiations as valid"],
      ans=0,
      why="KC-7.3.II.C states that the U.S. Senate refused to ratify the Treaty of Versailles "
          "OR join the League of Nations, so both refusals belong to the sentence. The second "
          "and third options each keep one refusal and reverse the other, and neither funding "
          "nor recognition of the negotiations appears in the sentence."),

 dict(q="Which statement carries the whole of what KC-7.3.II.C asserts?",
      choices=[
        "Wilson was deeply involved in the postwar negotiations, and the Senate still refused "
        "to ratify the treaty or join the League of Nations",
        "Wilson took little part in the postwar negotiations, and the Senate refused to "
        "ratify the treaty",
        "Wilson was deeply involved in the postwar negotiations, and the Senate accepted the "
        "results",
        "Wilson was deeply involved in the postwar negotiations, and no vote followed in the "
        "United States",
        "Wilson and the Senate agreed about the postwar settlement"],
      ans=0,
      why="KC-7.3.II.C is built on DESPITE: Wilson's deep involvement in postwar negotiations "
          "on one side and the U.S. Senate's refusal to ratify the Treaty of Versailles or "
          "join the League of Nations on the other. Reducing his involvement, or having the "
          "Senate accept, or reporting no decision at all, each loses one half of the "
          "contrast the sentence is built on."),

 dict(q="Which body does KC-7.3.II.C name as refusing the treaty and the League?",
      choices=[
        "The U.S. Senate",
        "The President",
        "The Supreme Court",
        "The House of Representatives",
        "A national referendum of voters"],
      ans=0,
      why="KC-7.3.II.C names the U.S. Senate as the body that refused to ratify the Treaty of "
          "Versailles or join the League of Nations, and it names Wilson on the other side of "
          "the contrast as deeply involved in the negotiations. The Court, the House and a "
          "referendum appear nowhere in the sentence."),

 dict(q="Which pairing correctly matches a framework sentence with what it contrasts?",
      choices=[
        "KC-7.3.II.B contrasts a limited combat role with a tipped balance, and KC-7.3.II.C "
        "contrasts deep involvement in negotiations with a refusal at home",
        "KC-7.3.II.B contrasts deep involvement in negotiations with a refusal at home, and "
        "KC-7.3.II.C contrasts a limited combat role with a tipped balance",
        "Both sentences contrast a limited combat role with a tipped balance",
        "Both sentences contrast deep involvement in negotiations with a refusal at home",
        "Neither sentence is built on a contrast"],
      ans=0,
      why="KC-7.3.II.B opens with ALTHOUGH and sets a relatively limited role in combat "
          "against an entry that helped tip the balance in favor of the Allies; KC-7.3.II.C "
          "opens with DESPITE and sets Wilson's deep involvement in postwar negotiations "
          "against the U.S. Senate's refusal. Exchanging the two puts each sentence's content "
          "under the other."),

 dict(q="What does KC-7.3.II, the key concept these three sentences sit under, state?",
      choices=[
        "That World War I and its aftermath intensified ongoing debates about the nation's "
        "role in the world and about national security and American interests",
        "That World War I settled the debates about the nation's role in the world",
        "That World War I began the debates about the nation's role in the world",
        "That the aftermath of the war left American foreign policy undiscussed",
        "That the debates concerned the domestic economy rather than the nation's role"],
      ans=0,
      why="KC-7.3.II states that World War I and its aftermath intensified ongoing debates "
          "about the nation's role in the world and how best to achieve national security and "
          "pursue American interests. The word 'ongoing' places those debates before the war, "
          "which KC-7.3.I already does, so neither a beginning nor a settlement matches the "
          "sentence."),

 dict(q="Unit 7's Learning Objective F asks for causes AND consequences. Which pair sorts two "
        "of the framework's statements correctly under those two headings?",
      choices=[
        "Wilson's call for the defense of humanitarian and democratic principles as a cause, "
        "and the Senate's refusal to ratify the treaty as a consequence of the war and its "
        "aftermath",
        "The Senate's refusal to ratify the treaty as a cause, and Wilson's call for the "
        "defense of humanitarian and democratic principles as a consequence",
        "Both as causes of U.S. involvement",
        "Both as consequences of U.S. involvement",
        "Neither, because the framework sorts nothing under either heading"],
      ans=0,
      why="KC-7.3.II.A gives Wilson's call as what the entry responded to, which places it "
          "among the causes Unit 7 Learning Objective F asks about, while KC-7.3.II.C's "
          "Senate refusal follows the war and the postwar negotiations. Reversing them puts a "
          "postwar vote before the entry it is supposed to have caused."),

 dict(q="This topic's suggested skill is printed on its own page. Which statement is it?",
      choices=[
        "Explain the significance of a source's point of view, purpose, historical situation, "
        "and audience, including how these might limit the uses of a source",
        "Explain the point of view, purpose, historical situation, and audience of a source",
        "Explain a historical concept, development, or process",
        "Use historical reasoning to explain relationships among pieces of historical evidence",
        "Explain how a specific historical development or process is situated within a "
        "broader historical context"],
      ans=0,
      why="The suggested skill printed on this topic page is 2.C, explain the significance of "
          "a source's point of view, purpose, historical situation, and audience, including "
          "how these might limit the uses of a source, and it is practised on Unit 7 Learning "
          "Objective F. Skill 2.B, the shorter statement, is printed on topics 7.3 and 7.14; "
          "the rest are skills 1.B, 6.C and 4.B."),

 dict(q="Which reasoning process does the CED print on this topic's page, and what in the "
        "required content calls for it?",
      choices=[
        "Causation, because the objective asks for the causes and consequences of U.S. "
        "involvement",
        "Comparison, because the objective asks students to set two attitudes side by side",
        "Continuity and change, because the objective follows one policy across the period",
        "Contextualization, because the objective previews the unit's key concepts",
        "Periodization, because the objective divides the war into phases"],
      ans=0,
      why="Causation is the reasoning process printed on this topic page and Unit 7 Learning "
          "Objective F asks for the causes and consequences of U.S. involvement in World War "
          "I, which is a causal question. Comparison is printed on topics 7.2, 7.4 and 7.11, "
          "and contextualization on topic 7.1."),

 dict(q="Which thematic focus does the CED print on this topic's page?",
      choices=[
        "America in the World, concerning interactions between empires, nations, and peoples",
        "Politics and Power, concerning debates about the role of government",
        "Social Structures, concerning social categories, roles, and practices",
        "Work, Exchange, and Technology, concerning markets, labor, and technology",
        "Migration and Settlement, concerning push and pull factors"],
      ans=0,
      why="The thematic focus printed on this topic page is America in the World, the "
          "diplomatic, economic, cultural, and military interactions between empires, "
          "nations, and peoples, which is where KC-7.3.II's debates about the nation's role "
          "in the world belong. The other four are printed on other pages of this unit."),

 dict(q="A hypothetical unattributed dispatch from an allied headquarters, invented for this "
        "question, records that a newly arrived army held a quiet sector while other armies "
        "fought the main actions. Which framework sentence does it most directly illustrate?",
      choices=[
        "KC-7.3.II.B's relatively limited role in combat",
        "KC-7.3.II.A's departure from the tradition of noninvolvement",
        "KC-7.3.II.C's refusal to ratify the Treaty of Versailles",
        "KC-7.3.II's intensified debates about national security",
        "KC-7.3.I.C's increase in involvement in Asia"],
      ans=0,
      why="KC-7.3.II.B states that the American Expeditionary Forces played a relatively "
          "limited role in combat, which is what a record of a quiet sector illustrates, "
          "while the same sentence's other half says the entry still helped tip the balance. "
          "The departure from tradition, the Senate's refusal, the debates and the increase "
          "in involvement in Asia are the subjects of the other sentences."),

 dict(q="A hypothetical unattributed letter, written by a member of a legislature to a "
        "constituent, argues that joining a new international body would tie the country to "
        "quarrels abroad. What does suggested skill 2.C ask a student to weigh about it?",
      choices=[
        "Whose point of view it expresses and to whom, and what that lets the letter show and "
        "not show",
        "Whether the framework judges the argument to have been correct",
        "How many members of the legislature agreed with it",
        "Which battles of the war preceded it",
        "How it compares with sources about the Progressive movement"],
      ans=0,
      why="Suggested skill 2.C asks for the significance of a source's point of view, "
          "purpose, historical situation, and audience, and how these might limit its uses, "
          "so one member's letter evidences an argument being made rather than the "
          "distribution of opinion. KC-7.3.II.C reports that the U.S. Senate refused to join "
          "the League of Nations without grading the arguments, and KC-7.3.II calls the "
          "surrounding debates intensified."),

 dict(q="Two hypothetical sources, both invented for this question, describe the same postwar "
        "negotiations: one is a summary prepared for a head of government, the other a "
        "hypothetical newspaper account written for readers at home. How does the difference "
        "in audience most reasonably bear on their use?",
      choices=[
        "Each was framed for the people who would read it, so what each includes and leaves "
        "out may differ even where the events are the same",
        "The two must agree in every particular, since they describe the same events",
        "Neither can be used, because sources written for different audiences conflict",
        "The summary must be the more reliable, because officials wrote it",
        "The audience of a source has no bearing on what it reports"],
      ans=0,
      why="Suggested skill 2.C asks a student to explain the significance of a source's "
          "audience and how it might limit the source's uses, and an audience matters only "
          "because it shapes what a source carries. KC-7.3.II.C supplies the events both "
          "hypothetical sources describe, Wilson's deep involvement in postwar negotiations "
          "and the Senate's refusal, and the framework ranks no kind of source above another."),

 dict(q="A hypothetical unattributed memoir claims that the American army won the war "
        "single-handed. Which framework sentence most directly qualifies that claim?",
      choices=[
        "KC-7.3.II.B, which calls the combat role relatively limited while crediting the "
        "entry with helping to tip the balance",
        "KC-7.3.II.A, which describes initial neutrality and a departure from tradition",
        "KC-7.3.II.C, which describes the Senate's refusal to ratify the treaty",
        "KC-7.3.II, which describes intensified debates about the nation's role",
        "Unit 7 Learning Objective F, which asks for causes and consequences"],
      ans=0,
      why="KC-7.3.II.B says the American Expeditionary Forces played a relatively limited "
          "role in combat and that the entry HELPED to tip the balance in favor of the "
          "Allies, so it qualifies a claim of single-handed victory in both of its halves. "
          "The other sentences concern the entry, the postwar refusal, the debates and the "
          "objective itself."),

 dict(q="Which statement belongs to the topic on the home front rather than to this topic?",
      choices=[
        "Official restrictions on freedom of speech grew during World War I as anxiety about "
        "radicalism increased",
        "After initial neutrality, the nation entered the conflict",
        "The American Expeditionary Forces played a relatively limited role in combat",
        "The U.S. Senate refused to ratify the Treaty of Versailles",
        "World War I and its aftermath intensified ongoing debates about the nation's role in "
        "the world"],
      ans=0,
      why="The growth of official restrictions on freedom of speech during the war is "
          "KC-7.2.I.C, printed on the home front topic that follows this one, while the other "
          "four statements are KC-7.3.II.A, KC-7.3.II.B, KC-7.3.II.C and KC-7.3.II, all "
          "printed on this page under Unit 7 Learning Objective F."),

 dict(q="Which statement belongs to the topic on interwar foreign policy rather than to this "
        "topic?",
      choices=[
        "In the years following World War I the United States pursued a unilateral foreign "
        "policy while maintaining isolationism",
        "The nation entered the conflict in response to a call for the defense of "
        "humanitarian and democratic principles",
        "The entry helped to tip the balance of the conflict in favor of the Allies",
        "The U.S. Senate refused to join the League of Nations",
        "Wilson was deeply involved in the postwar negotiations"],
      ans=0,
      why="The unilateral foreign policy of the years after the war is KC-7.3.II.D, printed "
          "on the interwar foreign policy topic later in this unit, while the other four "
          "statements come from KC-7.3.II.A, KC-7.3.II.B and KC-7.3.II.C on this page. Unit 7 "
          "Learning Objective F stops at the causes and consequences of the involvement "
          "itself."),

 dict(q="Using the table of illustrative allied combatants, which reading does the record "
        "support?",
      table=_T_FORCES,
      choices=[
        "The state recorded in the fighting for the fewest months records the largest share "
        "of allied divisions in the final months",
        "The state recorded in the fighting for the most months records the largest share of "
        "allied divisions in the final months",
        "The recorded shares rise as the recorded months rise",
        "No state is recorded in the fighting for fewer than twenty months",
        "Every state records the same share of allied divisions in the final months"],
      ans=0,
      why="Read from the table alone: one state records far the fewest months in the fighting "
          "and the largest share of divisions at the end, so the two columns do not run "
          "together. A short time in the fighting alongside real weight at the close is the "
          "shape of KC-7.3.II.B, which calls the American combat role relatively limited "
          "while crediting the entry with helping to tip the balance in favor of the Allies."),

 dict(q="Using the table of hypothetical postwar proposals, which reading matches "
        "KC-7.3.II.C?",
      table=_T_PROPOSALS,
      choices=[
        "Proposals pursued by the head of government in the negotiations were not all "
        "approved by the legislature afterwards",
        "Every proposal the head of government pursued was approved by the legislature",
        "The legislature approved every proposal put to it",
        "The legislature approved nothing in the record",
        "The head of government pursued every proposal in the record"],
      ans=0,
      why="Read from the table alone: three proposals are marked as pursued in the "
          "negotiations and only one of those is marked as approved afterwards, while one "
          "proposal was not pursued at all. A settlement pursued abroad and then refused at "
          "home is exactly the contrast KC-7.3.II.C draws between Wilson's deep involvement "
          "in postwar negotiations and the U.S. Senate's refusal."),

 dict(q="A student writes that KC-7.3.II.C shows Wilson refused the Treaty of Versailles. What "
        "has the student misread?",
      choices=[
        "The sentence gives Wilson deep involvement in the negotiations and gives the refusal "
        "to the U.S. Senate",
        "The sentence gives the refusal to Wilson and the negotiations to the Senate",
        "The sentence says the treaty was ratified",
        "The sentence says the United States joined the League of Nations",
        "The sentence places the negotiations before the war"],
      ans=0,
      why="KC-7.3.II.C states that despite Wilson's deep involvement in postwar negotiations, "
          "the U.S. Senate refused to ratify the Treaty of Versailles or join the League of "
          "Nations, so the involvement and the refusal belong to different actors. The "
          "sentence reports neither a ratification nor a membership, and the negotiations it "
          "names are postwar."),

 dict(q="Taken together, what do KC-7.3.II.A, KC-7.3.II.B and KC-7.3.II.C establish about U.S. "
        "involvement in World War I?",
      choices=[
        "The country broke with a tradition to enter, weighed in the outcome without carrying "
        "the main combat burden, and then declined the postwar settlement at home",
        "The country entered at the outbreak, carried the main combat burden, and ratified "
        "the postwar settlement",
        "The country stayed neutral throughout and took no part in the settlement",
        "The country entered late, made no difference to the outcome, and joined the League "
        "of Nations",
        "The country entered in support of an existing tradition of involvement in European "
        "affairs"],
      ans=0,
      why="KC-7.3.II.A has the nation enter after initial neutrality, departing from the "
          "tradition of noninvolvement in European affairs; KC-7.3.II.B has a relatively "
          "limited combat role and an entry that helped tip the balance in favor of the "
          "Allies; KC-7.3.II.C has the U.S. Senate refuse to ratify the Treaty of Versailles "
          "or join the League of Nations. Each of the other options reverses one of those "
          "three."),
]
