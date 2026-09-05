# AP WORLD HISTORY: MODERN 8.8 End of the Cold War
# CED effective Fall 2026 (Course Framework V.1), Unit 8 Cold War and
# Decolonization, c. 1900 to the present. Thematic focus: Governance (GOV).
# Reasoning process: Causation.
#
# Learning Objective: Unit 8 Learning Objective J -- explain the causes of the
# end of the Cold War. Suggested skill 1.B, explain a historical concept,
# development, or process. That skill is the shape of this bank: the items ask a
# student to state what the process was and what stood in a causal relation to
# what, rather than to source a document; sourcing is 8.2's and 8.7's skill and
# 8.6's is claims and evidence.
#
# HISTORICAL DEVELOPMENT this topic prints -- ONE sentence, and the only sentence
# every key below rests on:
#   KC-6.2.IV.E  Advances in U.S. military and technological development, the
#                Soviet Union's costly and ultimately failed invasion of
#                Afghanistan, and public discontent and economic weakness in
#                communist countries led to the end of the Cold War and the
#                collapse of the Soviet Union.
# The CED prints NO illustrative examples on this page, so no item here turns on
# any, and none is invented to fill the space.
#
# THE SENTENCE HAS THREE CAUSES AND TWO OUTCOMES, and that structure is the whole
# topic. Causes: advances in United States military and technological
# development; the Soviet Union's costly and ultimately failed invasion of
# Afghanistan; public discontent and economic weakness in communist countries.
# Outcomes: the end of the Cold War, and the collapse of the Soviet Union. Items
# 6, 12, 18, 24 and 29 turn on the fact that the framework names THREE causes
# jointly rather than a single decisive one.
#
# CONTESTED GROUND, AND WHAT IS DELIBERATELY NOT KEYED. Why the Cold War ended
# is a live political argument, and the tempting keys are exactly the ones the
# framework does not license. NO key here says that any one of the three causes
# was decisive or outweighed the others; the sentence conjoins them and does not
# rank them. NO key names a head of government or attributes the outcome to a
# person: the CED names no individual on this page, and a bank that supplied one
# would be settling the dispute rather than teaching the course. NO key says
# that either side won, that either system was proved superior, or that the
# outcome was inevitable -- none of that is in the sentence. Items 21, 25 and 27
# exist precisely to mark those as claims the framework does not make.
#
# DATES. The CED gives no year for the end of the Cold War or for the collapse
# of the Soviet Union on this page, and it states generally that events and
# processes are not constrained by its given dates. No key here depends on a
# year. Spans in stems are written "1979 to 1989", never with a hyphen, and are
# stimulus detail rather than keyed content.
#
# DEDUPE NOTE. Topic 8.2 covers the ideological struggle and the emergence of
# the two superpowers; 8.3 covers alliances, nuclear proliferation and proxy
# wars as effects of the Cold War. This module stays on causation running toward
# the END of the Cold War, and those earlier developments appear here only where
# a distractor needs to name something the framework places elsewhere. Topic 9.4
# covers the free-market liberalization that the CED elsewhere describes as
# accelerated BY the end of the Cold War, which is the reverse direction and is
# kept out of the keys here.
#
# SOURCES. Section I is stimulus-based and this bank cannot display an image, so
# every stimulus is TEXT and none is attributed to a real person or document.
# TABLES are hypothetical, each states a whole and its parts, and every keyed
# conclusion is recomputed from the table alone.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("8.8", "End of the Cold War", 8)

_T_BUDGET = dict(
    headers=["Decade (hypothetical record of one state's military budget, index)",
             "Military budget (first decade = 100)",
             "Of that, spent on research and new technologies",
             "Of that, spent on existing forces"],
    rows=[["1960s", "100", "22", "78"],
          ["1970s", "140", "42", "98"],
          ["1980s", "200", "80", "120"]])

_T_INTERVENTION = dict(
    headers=["Year of a hypothetical foreign military intervention",
             "Annual cost (first year = 100)",
             "Of that, maintaining forces in the field",
             "Of that, supplying allied local forces"],
    rows=[["Year one", "100", "70", "30"],
          ["Year two", "145", "100", "45"],
          ["Year three", "190", "130", "60"],
          ["Year four", "230", "155", "75"]])

_T_SHORTAGES = dict(
    headers=["Country (hypothetical household survey, thousands of households)",
             "Households surveyed",
             "Of those, reporting shortages of basic goods in the past year",
             "Of those, reporting no such shortage"],
    rows=[["Country one", "400", "260", "140"],
          ["Country two", "300", "195", "105"],
          ["Country three", "250", "150", "100"]])

QUESTIONS = [

 dict(q="According to this course, which combination of developments led to the end of the Cold War and the collapse of the Soviet Union?",
   choices=[
     "Advances in United States military and technological development, the Soviet Union's costly and failed invasion of Afghanistan, and public discontent and economic weakness in communist countries",
     "A negotiated treaty of union between the two superpowers followed by their merger into a single state",
     "The defeat of both superpowers in a war fought between them directly",
     "The transfer of both superpowers' territories to the administration of an international organization",
     "The refusal of the newly independent states to trade with either superpower"],
   ans=0,
   why="KC-6.2.IV.E states that advances in U.S. military and technological development, the Soviet Union's costly and ultimately failed invasion of Afghanistan, and public discontent and economic weakness in communist countries led to the end of the Cold War and the collapse of the Soviet Union. Those three developments are the framework's causes and it names no others."),

 dict(q="A budget analysis written in the late 1980s observes that one superpower has been able to sustain a long programme of advanced weapons research while the other has found the same programme increasingly hard to match. The analysis bears most directly on which of the framework's causes?",
   choices=[
     "Advances in United States military and technological development",
     "The Soviet Union's costly and ultimately failed invasion of Afghanistan",
     "Public discontent in the communist countries of Europe",
     "The dissolution of overseas empires after World War II",
     "The migration of former colonial subjects to imperial metropoles"],
   ans=0,
   why="KC-6.2.IV.E names advances in U.S. military and technological development first among the three causes it gives for the end of the Cold War. A sustained programme of advanced weapons research that the other superpower struggles to match is that advance described in budgetary terms, and it is distinct from the two other causes the same sentence names."),

 dict(q="This course describes one superpower's intervention in Afghanistan in terms of two features. What are they?",
   choices=[
     "That it was costly, and that it ultimately failed",
     "That it was inexpensive, and that it achieved its objectives",
     "That it was brief, and that it was conducted jointly with the other superpower",
     "That it was authorized by an international organization and financed by it",
     "That it was confined to economic assistance and involved no military forces"],
   ans=0,
   why="KC-6.2.IV.E describes the Soviet Union's COSTLY and ULTIMATELY FAILED invasion of Afghanistan among the causes of the end of the Cold War. Both adjectives are the framework's own, and a cause that had been cheap or successful would not do the work the sentence assigns it."),

 dict(q="A hypothetical record divides one state's military budget into two parts in each decade. Which conclusion does the table alone support?",
   table=_T_BUDGET,
   choices=[
     "The budget rose in each decade recorded, and the portion going to research and new technologies rose as a share of it",
     "The budget fell in each decade after the first one recorded",
     "The portion going to research and new technologies fell as a share of the budget",
     "Spending on existing forces fell in each decade after the first one recorded",
     "Spending on research and new technologies exceeded spending on existing forces in every decade"],
   ans=0,
   why="KC-6.2.IV.E names advances in U.S. military and technological development among the causes of the end of the Cold War, and a rising research share of a rising budget is one form such an advance takes. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="An unattributed letter written in 1988 from a town in a communist country complains that basic goods have been unobtainable for months and that the writer no longer believes official promises of improvement. The letter is best used as evidence about which of the framework's causes?",
   choices=[
     "Public discontent and economic weakness in communist countries",
     "Advances in United States military and technological development",
     "The Soviet Union's costly and ultimately failed invasion of Afghanistan",
     "The formation of new military alliances during the Cold War",
     "The spread of a globalized consumer culture across national borders"],
   ans=0,
   why="KC-6.2.IV.E names public discontent and economic weakness in communist countries among the three causes of the end of the Cold War and the collapse of the Soviet Union. A complaint of unobtainable goods joined to a loss of confidence in official promises is both halves of that cause in one document."),

 dict(q="A student argues that this course attributes the end of the Cold War to a single decisive cause. What is the best correction?",
   choices=[
     "The framework names three causes acting together and does not rank one above the others",
     "The framework names one cause and treats the other developments of the period as irrelevant",
     "The framework names no causes at all and treats the outcome as unexplained",
     "The framework names two causes and explicitly rejects a third",
     "The framework names three causes and states that the first was decisive"],
   ans=0,
   why="KC-6.2.IV.E conjoins advances in U.S. military and technological development, the Soviet Union's costly and ultimately failed invasion of Afghanistan, and public discontent and economic weakness in communist countries as leading to the end of the Cold War and the collapse of the Soviet Union. The sentence gives three causes in one list and assigns no priority among them."),

 dict(q="According to this course, what were the two outcomes to which the causes named in this topic led?",
   choices=[
     "The end of the Cold War and the collapse of the Soviet Union",
     "The end of the Cold War and the dissolution of the overseas empires",
     "The collapse of the Soviet Union and the founding of the United Nations",
     "The partition of Europe and the beginning of the Cold War",
     "The independence of the colonies and the founding of new military alliances"],
   ans=0,
   why="KC-6.2.IV.E states that the three causes it names led to the end of the Cold War and the collapse of the Soviet Union. Those are the two outcomes the sentence gives, and the dissolution of empires, the founding of the United Nations and the beginning of the Cold War belong to other statements in this course."),

 dict(q="A hypothetical record divides the annual cost of a foreign military intervention into two parts. Which conclusion does the table alone support?",
   table=_T_INTERVENTION,
   choices=[
     "The annual cost rose in every year recorded, and the cost of maintaining forces in the field rose alongside it",
     "The annual cost fell in at least one of the years recorded",
     "The cost of maintaining forces in the field fell over the course of the record",
     "The cost of supplying allied local forces exceeded the cost of maintaining forces in the field in every year",
     "The annual cost in the last year recorded stood below its first-year level"],
   ans=0,
   why="KC-6.2.IV.E names the Soviet Union's COSTLY and ultimately failed invasion of Afghanistan among the causes of the end of the Cold War, and a cost rising year on year is what makes an intervention costly in the framework's sense. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="Which of the following does this course NOT name as a cause of the end of the Cold War?",
   choices=[
     "A direct war fought between the two superpowers on each other's territory",
     "Advances in United States military and technological development",
     "The Soviet Union's costly and ultimately failed invasion of Afghanistan",
     "Public discontent in communist countries",
     "Economic weakness in communist countries"],
   ans=0,
   why="KC-6.2.IV.E names three causes and a direct war between the superpowers is not among them; the framework nowhere states that the two fought each other directly. The other four are the three causes of that sentence, with public discontent and economic weakness listed separately because the sentence names both."),

 dict(q="A hypothetical economic report of the late 1980s describes a country in which industrial plant is obsolete, growth has stopped, and shortages of ordinary goods have become normal. According to this course, conditions of this kind contributed to",
   choices=[
     "the end of the Cold War and the collapse of the Soviet Union",
     "the beginning of the Cold War and the division of Europe into two blocs",
     "the dissolution of the overseas empires after World War II",
     "the redrawing of political boundaries in the former colonies",
     "the founding of new international organizations to keep the peace"],
   ans=0,
   why="KC-6.2.IV.E names economic weakness in communist countries among the causes that led to the end of the Cold War and the collapse of the Soviet Union. The framework places that weakness at the end of the confrontation rather than at its beginning, so the direction of the causal relation is what the key states."),

 dict(q="A historian writes that the war one superpower fought in Afghanistan mattered to the end of the Cold War not because of where it was fought but because of what it cost and how it ended. This reading is",
   choices=[
     "consistent with the framework, which names the invasion as costly and ultimately failed",
     "inconsistent with the framework, which names the invasion as inexpensive and successful",
     "inconsistent with the framework, which does not mention Afghanistan at all",
     "consistent with the framework, which names the invasion as the sole cause of the outcome",
     "inconsistent with the framework, which attributes the invasion to the other superpower"],
   ans=0,
   why="KC-6.2.IV.E describes the Soviet Union's costly and ultimately failed invasion of Afghanistan, which is exactly the pairing of expense and outcome the historian identifies. The framework does not make it the sole cause, so a reading that did would go beyond the sentence rather than restate it."),

 dict(q="How does this course's framework relate the three causes it names to one another?",
   choices=[
     "It lists them together as jointly leading to the same outcome, without ordering them by importance",
     "It presents each as sufficient on its own and the other two as unnecessary",
     "It presents the first as the cause of the other two",
     "It presents them as unrelated developments with separate outcomes",
     "It presents them as consequences of the end of the Cold War rather than as its causes"],
   ans=0,
   why="KC-6.2.IV.E joins advances in U.S. military and technological development, the Soviet Union's costly and ultimately failed invasion of Afghanistan, and public discontent and economic weakness in communist countries in a single list leading to one pair of outcomes. It neither ranks them, nor derives one from another, nor reverses cause and effect."),

 dict(q="A hypothetical household survey divides the households it records into two groups. Which conclusion does the table alone support?",
   table=_T_SHORTAGES,
   choices=[
     "In every country surveyed, more than half of the households reported shortages of basic goods",
     "In every country surveyed, fewer than half of the households reported such shortages",
     "No household surveyed in country three reported a shortage of basic goods",
     "Country three surveyed more households than country two surveyed",
     "The three countries surveyed the same number of households as one another"],
   ans=0,
   why="KC-6.2.IV.E names public discontent and economic weakness in communist countries among the causes of the end of the Cold War, and widespread shortages of basic goods are one measurable form of that weakness. The survey is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="Which statement correctly explains the direction of the causal relation this topic describes?",
   choices=[
     "The three developments named came first and the end of the Cold War followed from them",
     "The end of the Cold War came first and produced the three developments named",
     "The collapse of the Soviet Union preceded the invasion of Afghanistan and caused it",
     "The three developments and the end of the Cold War were simultaneous and unrelated",
     "The end of the Cold War caused the advances in United States military and technological development"],
   ans=0,
   why="KC-6.2.IV.E states that the three developments LED TO the end of the Cold War and the collapse of the Soviet Union, which fixes them as prior and the outcomes as their result. Every distractor reverses that order or denies the relation the sentence asserts."),

 dict(q="An unattributed factory newsletter published in a communist country in 1987 prints a series of workers' letters complaining about conditions and about the officials who manage them. Read against this course's framework, the newsletter is most useful as evidence of",
   choices=[
     "public discontent inside a communist country in the years before the Cold War ended",
     "the military and technological programmes of the United States in the same years",
     "the conduct of a foreign military intervention in Afghanistan",
     "the terms of a military alliance between communist states",
     "the growth of knowledge economies in some regions of the world"],
   ans=0,
   why="KC-6.2.IV.E names public discontent in communist countries among the causes of the end of the Cold War and the collapse of the Soviet Union. Workers' letters of complaint printed inside such a country are that discontent recorded from within, and they bear on none of the other causes the sentence names."),

 dict(q="Which explanation of the end of the Cold War would go beyond what this course's framework states?",
   choices=[
     "That the outcome proves one economic system to have been superior to the other",
     "That advances in United States military and technological development contributed to it",
     "That a costly and failed invasion of Afghanistan contributed to it",
     "That economic weakness in communist countries contributed to it",
     "That the Soviet Union collapsed as well as the confrontation ending"],
   ans=0,
   why="KC-6.2.IV.E names three causes and two outcomes and makes no judgement about the merits of either economic system, so a verdict on systemic superiority is a claim the framework does not supply. The other four restate parts of that sentence."),

 dict(q="A textbook chapter is to explain the end of the Cold War as a historical process. Which structure would follow this course's framework most closely?",
   choices=[
     "Set out three contributing developments and then the two outcomes they led to",
     "Set out one contributing development and dismiss all others as irrelevant",
     "Set out the outcomes first and present the three developments as their consequences",
     "Set out a chronology of battles fought directly between the two superpowers",
     "Set out the terms of a treaty in which the two superpowers agreed to merge"],
   ans=0,
   why="KC-6.2.IV.E has exactly that shape: three developments conjoined, leading to the end of the Cold War and the collapse of the Soviet Union. Skill 1.B asks a student to explain a historical development or process, and reproducing the framework's own causal structure is what that requires."),

 dict(q="Two students disagree. One says the end of the Cold War is explained by pressures inside the communist countries; the other says it is explained by pressures from outside them. How does this course's framework bear on the disagreement?",
   choices=[
     "It names causes of both kinds, so neither student has the whole of the framework's account",
     "It names only causes inside the communist countries, so the first student is entirely right",
     "It names only causes outside the communist countries, so the second student is entirely right",
     "It names no causes, so neither student can appeal to it",
     "It names causes of both kinds but states that the internal ones were decisive"],
   ans=0,
   why="KC-6.2.IV.E names public discontent and economic weakness in communist countries, which are internal, alongside advances in U.S. military and technological development and a failed invasion of Afghanistan, which reach the communist states from outside their own societies. The sentence supplies both kinds and ranks neither."),

 dict(q="An unattributed dispatch of 1986 reports that a foreign war entering its seventh year is consuming resources a government had expected to spend at home, and that its objectives remain out of reach. The dispatch describes a situation this course associates with",
   choices=[
     "a costly and ultimately failed invasion among the causes of the end of the Cold War",
     "the technological advances of the opposing superpower",
     "the ideological origins of the Cold War in the years after 1945",
     "the redrawing of political boundaries after a colonial withdrawal",
     "the strong role newly independent governments took in guiding economic life"],
   ans=0,
   why="KC-6.2.IV.E names the Soviet Union's costly and ultimately failed invasion of Afghanistan among the causes of the end of the Cold War. A long war consuming resources intended for domestic use while its objectives remain unmet is that pairing of cost and failure described without naming the country."),

 dict(q="Which of the following is a consequence, rather than a cause, in the relation this topic describes?",
   choices=[
     "The collapse of the Soviet Union",
     "Advances in United States military and technological development",
     "The Soviet Union's invasion of Afghanistan",
     "Public discontent in communist countries",
     "Economic weakness in communist countries"],
   ans=0,
   why="KC-6.2.IV.E places the collapse of the Soviet Union with the end of the Cold War on the outcome side of the sentence, and the other four on the cause side. Skill 1.B asks a student to explain a process, and distinguishing which term of a causal statement is which is the first requirement of doing so."),

 dict(q="A commentator writes that the end of the Cold War was bound to happen whatever any government did. What does this course's framework say about that claim?",
   choices=[
     "The framework explains the outcome by particular developments and asserts no inevitability",
     "The framework states that the outcome was inevitable from the beginning of the confrontation",
     "The framework states that the outcome was impossible to explain by any development",
     "The framework states that no government's actions had any bearing on the outcome",
     "The framework states that the outcome depended on a single government's decision"],
   ans=0,
   why="KC-6.2.IV.E gives three specific developments that led to the end of the Cold War and the collapse of the Soviet Union. An explanation by particular causes is not a claim of inevitability, and the framework nowhere states that the outcome was fixed in advance or that actions were irrelevant."),

 dict(q="Which pairing correctly matches one of the framework's causes to the kind of evidence that would bear on it?",
   choices=[
     "Economic weakness in communist countries, matched with records of production and of shortages of consumer goods",
     "Economic weakness in communist countries, matched with the design specifications of foreign aircraft",
     "Advances in United States military and technological development, matched with harvest returns from communist agriculture",
     "The invasion of Afghanistan, matched with the membership rolls of a colonial nationalist party",
     "Public discontent in communist countries, matched with treaties signed between empires before 1914"],
   ans=0,
   why="KC-6.2.IV.E names economic weakness in communist countries among the causes of the end of the Cold War, and production figures and shortages are the direct measures of such weakness. Each distractor attaches a cause to evidence bearing on a different cause or on a different topic entirely."),

 dict(q="Suppose a researcher finds that public discontent in a communist country rose sharply in the same years in which its economy weakened. How does this course's framework treat the two?",
   choices=[
     "As two conditions the framework names together among the causes of the end of the Cold War",
     "As two conditions the framework treats as unrelated to the end of the Cold War",
     "As a single condition that the framework names only once",
     "As consequences of the collapse of the Soviet Union rather than causes",
     "As conditions the framework locates in the United States rather than in communist countries"],
   ans=0,
   why="KC-6.2.IV.E names public discontent AND economic weakness in communist countries in one clause among the causes that led to the end of the Cold War and the collapse of the Soviet Union. The framework locates both inside the communist countries and places both before the outcome rather than after it."),

 dict(q="A seminar is asked which single development this course identifies as having ended the Cold War by itself. What is the correct response?",
   choices=[
     "The course identifies no such single development, naming three that led to the outcome together",
     "The course identifies the invasion of Afghanistan as having ended the Cold War by itself",
     "The course identifies United States technological advance as having ended it by itself",
     "The course identifies economic weakness as having ended it by itself",
     "The course identifies public discontent as having ended it by itself"],
   ans=0,
   why="KC-6.2.IV.E names three developments in one list leading to the end of the Cold War and the collapse of the Soviet Union, and assigns no priority among them. Answering with any one of the three would supply a ranking the framework withholds, which is the error this item is built to catch."),

 dict(q="Which claim about the end of the Cold War does this course's framework support?",
   choices=[
     "Developments inside communist countries and developments outside them both contributed to it",
     "Developments inside communist countries had no bearing on it",
     "Developments outside communist countries had no bearing on it",
     "It was brought about by a formal agreement dissolving both superpowers at once",
     "It was brought about by the intervention of an international organization"],
   ans=0,
   why="KC-6.2.IV.E names public discontent and economic weakness in communist countries alongside advances in U.S. military and technological development and the Soviet Union's failed invasion of Afghanistan. The list spans both the inside and the outside of the communist states, so the framework supports the conjunction and denies neither half."),

 dict(q="An examiner asks a student to explain the end of the Cold War as a process rather than as an event. Which answer best meets that request within this course?",
   choices=[
     "It was an outcome reached through several developments accumulating over years, not a single moment of decision",
     "It was a single announcement made on one day and requiring no prior developments",
     "It was a battle fought between the two superpowers and decided in a season",
     "It was a treaty negotiated in one meeting between the two superpowers",
     "It was a vote taken among the newly independent states of the world"],
   ans=0,
   why="KC-6.2.IV.E names a sustained programme of military and technological advance, a long and costly invasion, and accumulated public discontent and economic weakness, all of which are processes running over years rather than moments. Skill 1.B asks for the explanation of a development or process, which is what distinguishes the key from an account built around a single event."),

 dict(q="Which statement about the two superpowers is NOT supported by this course's account of the end of the Cold War?",
   choices=[
     "The confrontation ended because one superpower defeated the other in open war",
     "Advances in one superpower's military and technological development contributed to the outcome",
     "A costly and failed invasion undertaken by the other superpower contributed to the outcome",
     "Conditions inside the communist countries contributed to the outcome",
     "One of the two superpowers collapsed as a state"],
   ans=0,
   why="KC-6.2.IV.E names three causes and neither states nor implies a war fought between the superpowers, so a defeat in open war is the claim the framework does not support. The other four restate parts of that sentence, including its second outcome, the collapse of the Soviet Union."),

 dict(q="An unattributed planning memorandum of 1985 argues that its government cannot at the same time match a rival's new weapons programmes, sustain a war abroad, and supply its own population with the goods it expects. According to this course, the memorandum sets out",
   choices=[
     "the three pressures the framework names as leading to the end of the Cold War, seen from one side",
     "the causes of the beginning of the Cold War in the years after World War II",
     "the reasons empires dissolved in the decades after World War II",
     "the arguments for encouraging free-market economic policies late in the century",
     "the case for forming a new military alliance among neighbouring states"],
   ans=0,
   why="KC-6.2.IV.E names advances in U.S. military and technological development, a costly and ultimately failed invasion, and public discontent and economic weakness in communist countries as the causes of the end of the Cold War and the collapse of the Soviet Union. A memorandum listing all three as simultaneous burdens is that sentence stated as a problem of policy."),

 dict(q="Considered as a whole, why does this course's account of the end of the Cold War count as a multi-causal explanation?",
   choices=[
     "Because it names three distinct developments and attributes the outcome to them together",
     "Because it names one development and describes it in three different ways",
     "Because it names three outcomes and attributes them all to one development",
     "Because it names no developments and treats the outcome as unexplained",
     "Because it names three developments and states that only one of them mattered"],
   ans=0,
   why="KC-6.2.IV.E lists advances in U.S. military and technological development, the Soviet Union's costly and ultimately failed invasion of Afghanistan, and public discontent and economic weakness in communist countries, and says they led to the end of the Cold War and the collapse of the Soviet Union. Three distinct developments joined to one pair of outcomes is what makes the explanation multi-causal."),

 dict(q="Taking the topic as a whole, which single sentence best states what this course says about the end of the Cold War?",
   choices=[
     "One superpower's military and technological advance, the other's costly and failed war in Afghanistan, and discontent and economic weakness inside the communist countries together brought the confrontation to an end and the Soviet Union to collapse",
     "The confrontation ended when the two superpowers agreed to abolish themselves and merge their territories",
     "The confrontation ended for reasons the course does not identify, and the Soviet Union survived it intact",
     "The confrontation ended because the newly independent states refused to take either side",
     "The confrontation ended in a war fought between the two superpowers and won decisively by one of them"],
   ans=0,
   why="KC-6.2.IV.E is a single sentence naming those three causes and those two outcomes, and the key restates it without adding a ranking among the causes, a verdict on either system, or a person to credit. Each distractor contradicts the sentence or supplies a cause the framework does not name."),
]
