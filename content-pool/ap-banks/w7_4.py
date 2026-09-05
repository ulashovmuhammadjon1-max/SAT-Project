# AP WORLD HISTORY: MODERN 7.4 Economy in the Interwar Period
# CED effective Fall 2026, Unit 7 Global Conflict, c. 1900 to the present.
# Thematic focus Economic Systems (ECN). Unit 7 Learning Objective D: explain
# how different governments responded to economic crisis after 1900. Reasoning
# process: comparison. Suggested skill 2.C, explain the significance of a
# source's point of view, purpose, historical situation, and/or audience,
# including how these might limit the use(s) of a source.
#
# THE HISTORICAL DEVELOPMENTS THIS TOPIC RESTS ON, in the framework's own words:
#   KC-6.3.I.B    Following World War I and the onset of the Great Depression,
#                 governments began to take a more active role in economic life.
#   KC-6.3.I.A.i  In the Soviet Union, the government controlled the national
#                 economy through the Five Year Plans, often implementing
#                 repressive policies, with negative repercussions for the
#                 population.
#
# ILLUSTRATIVE EXAMPLES the CED prints for government intervention in the
# economy: the New Deal; the fascist corporatist economy; governments with
# strong popular support in Brazil and Mexico. Those three phrases are the
# framework's own and are the only examples named here. Nothing is asserted
# about what any of them contained beyond the heading they are printed under,
# because the CED prints no such detail and an illustrative example is offered
# as an instance rather than as required content.
#
# WHAT IS DELIBERATELY NOT ASKED. No item keys to a date, an agency, a statute,
# a plan number, an output total or a leader's name. No item asks whether an
# intervention succeeded: KC-6.3.I.B states that governments became more active
# and does not evaluate the results, and KC-6.3.I.A.i states the Soviet case's
# repressive policies and negative repercussions without quantifying them.
#
# SOURCES. The suggested skill for this topic is about what a source's point of
# view, purpose, situation and audience do to its usefulness, so most stimuli
# here are sources. Every one is an explicitly unattributed illustrative source
# or a table of illustrative data whose keyed conclusion is recoverable from the
# table alone. Nothing is attributed to a real person or document.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md.
TOPIC = ("7.4", "Economy in the Interwar Period", 7)

_T_STATE_SHARE = dict(
    headers=["Country (illustrative)",
             "Government share of total investment, 1925 (percent)",
             "Government share of total investment, 1938 (percent)"],
    rows=[["Country R", "18", "54"],
          ["Country S", "9", "31"],
          ["Country T", "12", "26"]])

_T_PLAN = dict(
    headers=["Category of production (illustrative planned economy)",
             "Index at the start of the plan period",
             "Index at the end of the plan period"],
    rows=[["Heavy industry", "100", "290"],
          ["Transport equipment", "100", "210"],
          ["Consumer goods for households", "100", "115"]])

QUESTIONS = [
 dict(q="What change in the relationship between governments and their economies does the framework place after the First World War and the onset of the Great Depression?",
   choices=[
     "Governments began to take a more active role in economic life",
     "Governments began to withdraw from economic life and leave it to private decision",
     "Governments abolished private property everywhere outside the Soviet Union",
     "Governments agreed among themselves to fix a single world price for grain",
     "Governments transferred responsibility for the economy to the League of Nations"], ans=0,
   why="KC-6.3.I.B states that following World War I and the onset of the Great Depression, governments began to take a more active role in economic life. That is the change the framework names, and it is the opposite of a withdrawal."),
 dict(q="A student writes that governments were pushed out of economic life by the crises of the interwar years. Using the framework, the best correction is that the crises are followed by",
   choices=[
     "an increase in the economic role governments took, not a decrease",
     "a decrease in the economic role governments took, not an increase",
     "no change at all in what governments did about their economies",
     "the transfer of economic decisions to private banks in every state",
     "the end of all trade between states until the crises had passed"], ans=0,
   why="KC-6.3.I.B has governments beginning to take a more active role in economic life following the war and the onset of the depression. The direction of that sentence is what the student has reversed."),
 dict(q="How does the framework describe the Soviet government's management of its economy in this period?",
   choices=[
     "It controlled the national economy through the Five Year Plans, often with repressive policies and negative consequences for the population",
     "It left the national economy to private owners while regulating prices only",
     "It controlled the national economy through the Five Year Plans, with no consequences for the population that the framework records",
     "It abandoned central planning in favour of an open market in agricultural goods",
     "It managed the economy jointly with the governments of neighbouring states"], ans=0,
   why="KC-6.3.I.A.i states that in the Soviet Union the government controlled the national economy through the Five Year Plans, often implementing repressive policies, with negative repercussions for the population. The repression and the consequences are part of the sentence, not an addition to it."),
 dict(q="Which set of cases does the CED print as illustrative examples of government intervention in the economy?",
   choices=[
     "The New Deal, the fascist corporatist economy, and governments with strong popular support in Brazil and Mexico",
     "The League of Nations mandates, the Indian National Congress, and West African strikes",
     "The alliance system, intensified nationalism, and imperialist expansion",
     "Political propaganda, art, media, and intensified forms of nationalism",
     "The Armenian, Cambodian, and Rwandan cases"], ans=0,
   why="The illustrative examples the CED prints beside KC-6.3.I.B, this topic's required content, are the New Deal, the fascist corporatist economy, and governments with strong popular support in Brazil and Mexico. The other lists are the illustrative examples or historical developments of topics 7.5, 7.2, 7.3 and 7.8."),
 dict(q="Two governments both respond to the same economic crisis, one by directing investment through a national plan and the other by funding public employment while leaving most firms in private hands. On the framework's account, the best comparison is that",
   choices=[
     "both took a more active role in economic life, and they differed in how far that role went",
     "only the first took a more active role, since the second left firms in private hands",
     "only the second took a more active role, since planning is not a form of intervention",
     "neither took a more active role, because both were responding to a crisis",
     "the two responses are indistinguishable in the framework's terms"], ans=0,
   why="KC-6.3.I.B states the shared development, that governments began to take a more active role in economic life, while KC-6.3.I.A.i marks out the Soviet case as control of the whole national economy. The comparison the reasoning process asks for is a shared direction with different extents."),
 dict(q="An unattributed government pamphlet from the 1930s describes a public works programme as having restored dignity to the nation's workers and asks readers to support the government at the coming election. Which limitation on its use is most significant?",
   choices=[
     "Its purpose is to win support, so it cannot be taken as a neutral report of the programme's results",
     "It was produced during the period it describes, which makes it unusable as evidence",
     "It concerns employment rather than industry, so it says nothing about the economy",
     "It was printed rather than broadcast, so its audience cannot be identified",
     "It names a government, and no source naming a government can be used"], ans=0,
   why="Suggested skill 2.C asks students to explain how a source's purpose and audience limit its uses. A pamphlet soliciting electoral support is evidence of the government's own account of its intervention, which KC-6.3.I.B describes, and not evidence that the intervention worked."),
 dict(q="The table below reports illustrative figures for the share of total investment directed by government in three countries. Which conclusion is best supported by the data as given?",
   table=_T_STATE_SHARE,
   choices=[
     "The government share rose in all three countries, and rose by the most percentage points in Country R",
     "The government share rose in all three countries, and rose by the most percentage points in Country T",
     "The government share fell in at least one of the three countries",
     "The three countries had equal government shares at the later date",
     "The government share was unchanged in every country between the two dates"], ans=0,
   why="Read from the table alone: each country's later share exceeds its earlier one, and subtracting the earlier from the later shows one country with the largest rise. This is the more active role in economic life that KC-6.3.I.B places after the war and the onset of the depression."),
 dict(q="The table below reports illustrative output indexes for three categories of production in a planned economy over one plan period. Which conclusion is best supported?",
   table=_T_PLAN,
   choices=[
     "Output rose in every category, but by far the least in goods produced for households",
     "Output rose in every category, but by far the least in heavy industry",
     "Output fell in every category over the plan period",
     "The three categories grew by the same amount over the plan period",
     "Only goods produced for households rose over the plan period"], ans=0,
   why="Read from the table alone: every category ends above its starting index, and the smallest increase by a wide margin is in household goods. KC-6.3.I.A.i states that Soviet control of the national economy through the Five Year Plans carried negative repercussions for the population, and a plan that raises industrial output far faster than household supply is what that looks like in data."),
 dict(q="The CED lists the fascist corporatist economy beside the New Deal under the same heading. What does that placement indicate?",
   choices=[
     "Both are offered as examples of government intervention in the economy",
     "Both are offered as examples of alliance systems formed before a war",
     "Both are offered as examples of colonial administration",
     "Both are offered as examples of military mobilization strategies",
     "Both are offered as examples of mass atrocities after 1900"], ans=0,
   why="The illustrative examples for KC-6.3.I.B appear under the heading government intervention in the economy, and the New Deal and the fascist corporatist economy are both printed there. The heading is what the placement asserts; the framework says nothing here about what either contained."),
 dict(q="The CED describes the governments of Brazil and Mexico in this connection with which phrase?",
   choices=[
     "Governments with strong popular support",
     "Governments installed by foreign intervention",
     "Governments ruling without any organised support",
     "Governments formed by the League of Nations",
     "Governments established by treaty settlement"], ans=0,
   why="The illustrative examples printed for KC-6.3.I.B name governments with strong popular support in Brazil and Mexico as instances of government intervention in the economy. That is the framework's own wording, and it makes no claim about foreign intervention or treaty origins."),
 dict(q="What does the framework state about the effects of Soviet economic control on the population?",
   choices=[
     "It records negative repercussions for the population",
     "It records improvements in living standards for the population",
     "It records no effect on the population in either direction",
     "It records effects on neighbouring populations but not on the Soviet population",
     "It records that the population itself directed the plans"], ans=0,
   why="KC-6.3.I.A.i states that the Soviet government controlled the national economy through the Five Year Plans, often implementing repressive policies, with negative repercussions for the population. The framework asserts the direction of the effect without quantifying it."),
 dict(q="Which phrase does the framework attach to the methods by which the Soviet government carried out its control of the economy?",
   choices=[
     "Often implementing repressive policies",
     "Relying on voluntary participation by enterprises",
     "Deferring to elected regional assemblies",
     "Leaving the pace of change to individual farmers",
     "Following the recommendations of foreign advisers"], ans=0,
   why="KC-6.3.I.A.i says the Soviet government controlled the national economy through the Five Year Plans, often implementing repressive policies. The phrase is part of the framework's own description of the method."),
 dict(q="A historian compares three interwar governments that all increased their economic role. Which conclusion follows from the framework?",
   choices=[
     "A more active economic role was taken by governments of very different political character",
     "A more active economic role was taken only by governments of one political character",
     "A more active economic role was taken only where the population had no vote",
     "A more active economic role was taken only in states that had lost the war",
     "A more active economic role was taken only in states without colonies"], ans=0,
   why="KC-6.3.I.B states the development in general terms, and the illustrative examples the CED prints for it span the New Deal, the fascist corporatist economy, and governments with strong popular support in Brazil and Mexico. The intervention crosses political types rather than marking one out."),
 dict(q="An unattributed radio address from the early 1930s tells listeners that when private enterprise cannot put people to work, the state must do it instead. The argument is best situated in which development?",
   choices=[
     "The move by governments towards a more active role in economic life after the onset of the Great Depression",
     "The formation of alliances between states before the First World War",
     "The mobilization of colonial populations for the purpose of waging war",
     "The transfer of former colonies under a system of mandates",
     "The collapse of the older land-based empires and the revolution that followed"], ans=0,
   why="KC-6.3.I.B places the move to a more active government role after World War I and the onset of the Great Depression. An argument that the state must employ people when private enterprise cannot is that move stated as a principle."),
 dict(q="A source praising a state's economic plan was published by a press that the same state controls. What does this most affect?",
   choices=[
     "The weight the source can carry as independent evidence about the plan's effects",
     "Whether the source can be dated to the period it describes",
     "Whether the source concerns economics at all",
     "Whether the plan existed in the first place",
     "Whether the source names the country it discusses"], ans=0,
   why="Suggested skill 2.C asks how a source's point of view and purpose limit its uses. KC-6.3.I.A.i records that Soviet economic control was often carried out through repressive policies, and a press controlled by the same government is not positioned to report the repercussions the framework names."),
 dict(q="Which of the following is NOT among the illustrative examples the CED prints for government intervention in the economy?",
   choices=[
     "The system of League of Nations mandates",
     "The New Deal",
     "The fascist corporatist economy",
     "A government with strong popular support in Brazil",
     "A government with strong popular support in Mexico"], ans=0,
   why="The illustrative examples for KC-6.3.I.B are the New Deal, the fascist corporatist economy, and governments with strong popular support in Brazil and Mexico. The system of League of Nations mandates is printed for KC-6.2.I.B in topic 7.5, under territorial gains, and concerns colonies rather than economic intervention."),
 dict(q="In the framework, the Great Depression appears both in this topic and among the causes of the Second World War. What is the difference in the role it plays?",
   choices=[
     "Here it is the crisis governments responded to, and there it is one of the causes of the later war",
     "Here it is a cause of the later war, and there it is the crisis governments responded to",
     "In both places it is described as a consequence of the peace settlement alone",
     "In both places it is described as a strategy of wartime mobilization",
     "It appears in only one of the two places and not the other"], ans=0,
   why="KC-6.3.I.B places the onset of the Great Depression among the conditions after which governments took a more active economic role, while KC-6.2.IV.B.ii names the global economic crisis engendered by the Great Depression among the causes of World War II. The same development carries the two roles, and the anchor fixes which belongs where."),
 dict(q="Which research question follows most directly from this topic's learning objective?",
   choices=[
     "How did different governments respond to economic crisis after 1900",
     "Which composers were most popular in the interwar years",
     "How many kilometres of railway existed in each state in 1900",
     "Which generals held command during the interwar years",
     "How did the climate of the northern hemisphere change after 1900"], ans=0,
   why="Unit 7 Learning Objective D asks students to explain how different governments responded to economic crisis after 1900, and the word different is what makes the topic a comparison. The other questions ask about matters the objective does not name."),
 dict(q="Why does the framework's statement about government activity in the economy count as a change rather than a continuity?",
   choices=[
     "Because governments are described as beginning to take a role more active than the one they had held before",
     "Because governments are described as having always directed their economies in the same way",
     "Because governments are described as abolishing their economies",
     "Because the statement concerns only states that did not exist before the war",
     "Because the statement concerns only the years after 1945"], ans=0,
   why="KC-6.3.I.B says governments BEGAN to take a more active role in economic life following the war and the onset of the depression. A beginning marks a departure from what came before, which is what makes it a change."),
 dict(q="An unattributed factory newspaper from a planned economy reports that a workshop exceeded its target and that its workers have pledged to exceed the next one. What is the most defensible use of this source?",
   choices=[
     "As evidence of how the plan was presented to workers, rather than of how much was produced",
     "As an accurate measurement of the workshop's output",
     "As proof that the population supported the plan",
     "As a record of the government's private deliberations",
     "As evidence about production in countries other than this one"], ans=0,
   why="Suggested skill 2.C asks what a source's purpose and audience allow it to show. KC-6.3.I.A.i notes that control of the economy was often accompanied by repressive policies, which is exactly the circumstance in which a workplace publication reports targets met; the source documents the presentation rather than the production."),
 dict(q="A government facing mass unemployment begins to set prices, direct credit to selected industries, and employ workers directly. The framework would treat these measures as",
   choices=[
     "instances of the more active economic role governments took after the onset of the depression",
     "instances of governments withdrawing from economic life",
     "instances of wartime mobilization for the purpose of waging war",
     "instances of imperialist expansion in search of resources",
     "instances of the peace settlement that followed the First World War"], ans=0,
   why="KC-6.3.I.B states that following World War I and the onset of the Great Depression governments began to take a more active role in economic life. Setting prices, directing credit and employing workers are that role in practice."),
 dict(q="What distinguishes the Soviet case from the other interwar interventions the CED names?",
   choices=[
     "The framework describes the government as controlling the national economy as a whole",
     "The framework describes the government as leaving the national economy untouched",
     "The framework describes the government as intervening only in agriculture",
     "The framework describes the government as acting only after 1945",
     "The framework describes the government as following a plan drawn up abroad"], ans=0,
   why="KC-6.3.I.A.i says the Soviet government controlled the national economy through the Five Year Plans, which is a statement about the whole economy, while KC-6.3.I.B says only that governments generally took a more active role. The difference is one of extent and it is in the framework's wording."),
 dict(q="A student wants to argue that responses to the economic crisis differed in political character as well as in method. Which evidence base would serve that argument best?",
   choices=[
     "Comparable records of intervention from states with different political systems",
     "The full text of a single government's own account of its programme",
     "A list of the crops grown in each state before the crisis",
     "The published memoirs of one finance minister",
     "The tonnage of shipping registered in each state"], ans=0,
   why="Unit 7 Learning Objective D asks how DIFFERENT governments responded, and the CED's illustrative examples span political systems as unlike as the New Deal and the fascist corporatist economy. An argument about difference needs comparable material from more than one system."),
 dict(q="Which statement about the framework's treatment of interwar economic policy is accurate?",
   choices=[
     "It states a general development and offers particular cases as illustrations of it",
     "It states particular cases and offers no general development at all",
     "It states a general development and forbids the use of particular cases",
     "It evaluates each particular case as a success or a failure",
     "It confines itself to the economies of states that had colonies"], ans=0,
   why="KC-6.3.I.B states the general development that governments began to take a more active role in economic life, and the CED prints the New Deal, the fascist corporatist economy and governments with strong popular support in Brazil and Mexico as illustrative examples beside it. The framework does not rate any of them."),
 dict(q="An unattributed opposition newspaper in an interwar state accuses the government of ruining the economy through its new controls. How should a historian treat this source?",
   choices=[
     "As evidence of the controls' existence and of one contemporary reaction to them, not as a settled verdict",
     "As a neutral assessment of the controls' economic effects",
     "As proof that the controls were never actually introduced",
     "As evidence about a different country's economic policy",
     "As a source whose point of view makes it useless for any purpose"], ans=0,
   why="Suggested skill 2.C asks students to weigh a source's point of view rather than to accept or discard it. The complaint confirms that the more active government role KC-6.3.I.B describes was under way, and it reports a reaction whose author has an interest in the verdict."),
 dict(q="Why does this topic's reasoning process, comparison, suit the material the framework supplies?",
   choices=[
     "Because several governments faced the same crisis and the framework records different responses to it",
     "Because the framework records only one government's response and no others",
     "Because the framework denies that any government responded to the crisis",
     "Because the framework treats every response as identical in method and character",
     "Because the framework confines the crisis to a single country"], ans=0,
   why="KC-6.3.I.B states a development common to governments generally, KC-6.3.I.A.i marks out the Soviet case, and the CED prints further illustrative examples. A shared crisis with differing responses is what a comparison is made of."),
 dict(q="A government publishes output totals showing rapid growth while private letters from the same period describe shortages of ordinary goods. What is the best way to use both kinds of source?",
   choices=[
     "Treat them as reporting different aspects, since totals may rise while household supply does not",
     "Discard the letters, since official totals are always more reliable",
     "Discard the totals, since any government source is worthless",
     "Conclude that one of the two sources must have been forged",
     "Conclude that no economic change took place at all"], ans=0,
   why="KC-6.3.I.A.i states that control of the national economy through the Five Year Plans carried negative repercussions for the population, so rising aggregate output and household shortage are not in contradiction. Suggested skill 2.C asks what each source's situation allows it to show."),
 dict(q="Which pairing correctly matches a statement in the framework with the case it is made about?",
   choices=[
     "Control of the national economy through Five Year Plans, made about the Soviet Union",
     "Control of the national economy through Five Year Plans, made about every state in the period",
     "A more active role in economic life, made about the Soviet Union alone",
     "Repressive policies with negative repercussions, made about governments with strong popular support",
     "Government intervention in the economy, made about states that avoided the depression"], ans=0,
   why="KC-6.3.I.A.i attaches the Five Year Plans and their repercussions to the Soviet Union specifically, while KC-6.3.I.B states the more active role as a general development. Attaching either statement to the wrong scope is the error the distractors make."),
 dict(q="A claim that interwar governments everywhere adopted the same economic programme would be best answered with which observation?",
   choices=[
     "The framework's own illustrative cases include programmes of very different kinds",
     "The framework states that no government adopted any economic programme",
     "The framework states that all programmes were drawn up by the same body",
     "The framework confines its account to one country",
     "The framework treats economic policy as unchanged since the nineteenth century"], ans=0,
   why="The CED prints the New Deal, the fascist corporatist economy, and governments with strong popular support in Brazil and Mexico as illustrative examples of the development KC-6.3.I.B states. A shared direction is asserted; a shared programme is not."),
 dict(q="What is the most accurate summary of the framework's position on the interwar economy?",
   choices=[
     "A crisis followed by a general increase in government activity, with the Soviet case marked out as control of the whole economy",
     "A crisis followed by a general withdrawal of government from economic activity",
     "A period of stability in which no government changed its economic role",
     "A period in which only the Soviet government responded to the crisis at all",
     "A period in which economic policy was set by agreement among the powers"], ans=0,
   why="KC-6.3.I.B gives the general movement towards a more active role after the war and the onset of the depression, and KC-6.3.I.A.i gives the Soviet case as control of the national economy through the Five Year Plans. The summary has to carry both, which is why the anchor names both."),
]
