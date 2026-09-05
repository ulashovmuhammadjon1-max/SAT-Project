# AP WORLD HISTORY: MODERN 4.7 Changing Social Hierarchies from 1450 to 1750
# CED effective Fall 2024/2026, Unit 4 Transoceanic Interconnections, c. 1450 to
# c. 1750. Title copied verbatim from WORLD_HISTORY_topics.json.
#
# Unit 4: Learning Objective M -- explain how social categories, roles, and
# practices have been maintained or have changed over time.
# Suggested skill 3.D, explain how claims or evidence support, modify, or refute
# a source's argument. Reasoning process: continuity and change.
# Thematic focus: Social Interactions and Organization.
#
# Historical developments this module keys to, in the framework's own words:
#   KC-4.3.I.B    Many states, such as the Mughal and Ottoman empires, adopted
#                 practices to accommodate the ethnic and religious diversity of
#                 their subjects or to utilize the economic, political, and
#                 military contributions of different ethnic or religious groups.
#                 In other cases, states suppressed diversity or limited certain
#                 groups' roles in society, politics, or the economy.
#   KC-4.2.III.A  Imperial conquests and widening global economic opportunities
#                 contributed to the formation of new political and economic
#                 elites, including in China with the transition to the Qing
#                 Dynasty and in the Americas with the rise of the Casta system.
#   KC-4.2.III.B  The power of existing political and economic elites fluctuated
#                 as the elites confronted new challenges to their ability to
#                 affect the policies of the increasingly powerful monarchs and
#                 leaders.
#
# Illustrative examples printed beside the topic, under two headings:
#   Differential treatment of groups in society, politics, and the economy:
#     expulsion of Jews from Spain and Portugal, and the acceptance of Jews in
#     the Ottoman Empire; restrictive policies against Han Chinese in Qing China;
#     varying status of different classes of women within the Ottoman Empire.
#   Existing elites: Ottoman timars; Russian boyars; European nobility.
#
# WHAT THIS MODULE DELIBERATELY DOES NOT ASSERT. KC-4.3.I.B has TWO halves and
# the framework commits to neither as the rule: many states accommodated
# diversity or used the contributions of different groups, and in other cases
# states suppressed diversity or limited certain groups' roles. Nothing here
# keys either half as what states generally did, and two items exist to catch
# exactly that flattening. KC-4.2.III.B's verb is "FLUCTUATED", not rose and not
# fell, so no item keys a direction for the power of existing elites. The
# framework gives no dates, no ruler, and no account of how any of these
# practices worked.
#
# The Qing appears TWICE and deliberately so: at KC-4.2.III.A as a transition
# that formed a new political and economic elite, and in the illustrative
# examples as a state with restrictive policies against Han Chinese. Item 15 is
# built on that double rather than around it.
#
# Dates are written "1450 to 1750". Five choices A-E per HISTORY_BRIEF.md. Every
# stimulus is hypothetical or unattributed; no quotation is put in a real
# person's mouth.
TOPIC = ("4.7", "Changing Social Hierarchies from 1450 to 1750", 4)

_T_PRACTICES = dict(
    headers=["Practice in a hypothetical state's records", "What the record says it did"],
    rows=[["Practice 1", "Guaranteed a religious minority the use of its own courts"],
          ["Practice 2", "Recruited soldiers from several ethnic groups into the army"],
          ["Practice 3", "Barred one group from holding any office of state"],
          ["Practice 4", "Set the same harvest tax for every household alike"]])

_T_ELITES = dict(
    headers=["Elite group in a hypothetical survey", "How the survey describes it"],
    rows=[["An elite that rose after an imperial conquest", "Newly formed in this period"],
          ["An elite that rose with new global economic opportunities",
           "Newly formed in this period"],
          ["A landed nobility of long standing", "Long established before this period"],
          ["A body of hereditary provincial lords", "Long established before this period"]])

_T_PETITIONS = dict(
    headers=["Period of a hypothetical council record",
             "Petitions from the existing elite that the monarch granted",
             "Petitions from the existing elite that the monarch refused"],
    rows=[["First period", "18", "6"],
          ["Second period", "11", "13"],
          ["Third period", "15", "9"],
          ["Fourth period", "7", "20"]])

QUESTIONS = [
 dict(
  q=("The framework says many states adopted practices with a particular aim. Which aim does it "
     "name first?"),
  choices=[
   "To accommodate the ethnic and religious diversity of their subjects",
   "To make every subject adopt a single language",
   "To move their subjects into newly conquered provinces",
   "To abolish the distinction between rulers and subjects",
   "To transfer their subjects to a neighbouring state"],
  ans=0,
  why=("KC-4.3.I.B says many states, such as the Mughal and Ottoman empires, adopted practices to "
       "accommodate the ethnic and religious diversity of their subjects. The framework records "
       "no policy of imposed language, forced migration, abolished distinction or transferred "
       "population in this statement.")),
 dict(
  q=("Besides accommodating diversity, what second aim does the framework give for the practices "
     "many states adopted?"),
  choices=[
   "To utilize the economic, political, and military contributions of different ethnic or religious groups",
   "To reduce the number of groups living within their borders",
   "To end all commercial contact with foreign merchants",
   "To transfer authority from the ruler to local assemblies",
   "To standardize religious practice across every province"],
  ans=0,
  why=("KC-4.3.I.B pairs accommodation with a second purpose: to utilize the economic, political, "
       "and military contributions of different ethnic or religious groups. Reduction of groups "
       "and standardized religion belong to the other half of the same sentence, about states "
       "that suppressed diversity.")),
 dict(
  q=("Which states does the framework name as examples of those that adopted practices to "
     "accommodate diversity or to use the contributions of different groups?"),
  choices=[
   "The Mughal and Ottoman empires",
   "The Manchu and Safavid empires",
   "The Portuguese and Spanish maritime empires",
   "The Asante and the Kingdom of the Kongo",
   "Ming China and Tokugawa Japan"],
  ans=0,
  why=("KC-4.3.I.B names the Mughal and Ottoman empires as its examples of states that adopted "
       "such practices. The other empires and states listed appear elsewhere in the framework, at "
       "KC-4.3.II.B, KC-4.3.II.C, KC-4.3.II.A.ii and KC-4.3.II.A.i, but not in this sentence.")),
 dict(
  q=("The framework adds a second case to its account of how states treated the groups within "
     "them. What does it say happened in those other cases?"),
  choices=[
   "States suppressed diversity or limited certain groups' roles in society, politics, or the economy",
   "States dissolved themselves into their constituent groups",
   "States granted every group an equal share of office",
   "States expelled their rulers and adopted assemblies",
   "States withdrew from contact with all other states"],
  ans=0,
  why=("KC-4.3.I.B closes by saying that in other cases states suppressed diversity or limited "
       "certain groups' roles in society, politics, or the economy. That is the second half of a "
       "single sentence whose first half describes accommodation, and neither half is offered as "
       "the general rule.")),
 dict(
  q=("A student asks whether the framework says states of this period accommodated diversity or "
     "suppressed it. What is the best answer from the text?"),
  choices=[
   "It records both: many states accommodated or used the contributions of different groups, and in other cases states suppressed diversity or limited certain groups' roles",
   "It records only accommodation, and no case of suppression",
   "It records only suppression, and no case of accommodation",
   "It records neither, since it says nothing about how states treated groups",
   "It records that every state did both at once, in equal measure"],
  ans=0,
  why=("KC-4.3.I.B holds both cases in one sentence and commits to neither as the rule: many "
       "states adopted practices to accommodate ethnic and religious diversity or to utilize the "
       "contributions of different groups, and in other cases states suppressed diversity or "
       "limited certain groups' roles. Choosing one half is the flattening this item exists to "
       "catch.")),
 dict(
  q=("What does the framework say contributed to the formation of new political and economic "
     "elites in this period?"),
  choices=[
   "Imperial conquests and widening global economic opportunities",
   "The collapse of long-distance trade",
   "A general fall in agricultural output",
   "The abolition of hereditary office everywhere",
   "The withdrawal of monarchs from public affairs"],
  ans=0,
  why=("KC-4.2.III.A says imperial conquests and widening global economic opportunities "
       "contributed to the formation of new political and economic elites. Each rejected option "
       "describes a contraction or a withdrawal that the framework nowhere records as producing "
       "new elites.")),
 dict(
  q=("Which two examples does the framework give of the formation of new political and economic "
     "elites?"),
  choices=[
   "China with the transition to the Qing Dynasty, and the Americas with the rise of the Casta system",
   "China with the transition to the Qing Dynasty, and Russia with the rise of the boyars",
   "The Ottoman Empire with the timar, and Europe with its nobility",
   "The Americas with the rise of the Casta system, and Europe with its nobility",
   "Spain and Portugal with the expulsion of Jews, and the Ottoman Empire with their acceptance"],
  ans=0,
  why=("KC-4.2.III.A names China with the transition to the Qing Dynasty and the Americas with "
       "the rise of the Casta system as its examples of new elites. The boyars, the timars and "
       "the European nobility are printed under the separate heading of EXISTING elites, which "
       "belongs to KC-4.2.III.B.")),
 dict(
  q=("What does the framework say happened to the power of existing political and economic elites "
     "in this period?"),
  choices=[
   "It fluctuated",
   "It rose steadily throughout the period",
   "It fell steadily throughout the period",
   "It remained exactly as it had been",
   "It passed entirely to the new elites"],
  ans=0,
  why=("KC-4.2.III.B says the power of existing political and economic elites fluctuated as the "
       "elites confronted new challenges. Fluctuation is the framework's own word, so a steady "
       "rise, a steady fall, no change at all and a complete transfer each assert a direction the "
       "sentence declines to give.")),
 dict(
  q=("According to the framework, what were existing elites confronting as their power "
     "fluctuated?"),
  choices=[
   "New challenges to their ability to affect the policies of increasingly powerful monarchs and leaders",
   "A refusal by monarchs to govern at all",
   "The disappearance of monarchy from every state",
   "An offer from monarchs to share power equally",
   "The loss of all their landholdings by decree"],
  ans=0,
  why=("KC-4.2.III.B says the power of existing elites fluctuated as they confronted new "
       "challenges to their ability to affect the policies of the increasingly powerful monarchs "
       "and leaders. The phrase increasingly powerful is the framework's own and rules out the "
       "readings in which monarchs weaken or withdraw.")),
 dict(
  q=("The framework's illustrative examples for this topic pair a treatment of one group in two "
     "different places. Which pairing is printed there?"),
  choices=[
   "The expulsion of Jews from Spain and Portugal, and the acceptance of Jews in the Ottoman Empire",
   "The acceptance of Jews in Spain and Portugal, and the expulsion of Jews from the Ottoman Empire",
   "The expulsion of Han Chinese from Qing China, and their acceptance in the Mughal Empire",
   "The expulsion of merchants from the Indian Ocean ports, and their acceptance in the Atlantic",
   "The expulsion of the boyars from Russia, and their acceptance in the Ottoman Empire"],
  ans=0,
  why=("The illustrative examples beside Unit 4: Learning Objective M print the expulsion of Jews "
       "from Spain and Portugal together with the acceptance of Jews in the Ottoman Empire, under "
       "the heading of differential treatment of groups in society, politics, and the economy. "
       "That pairing is what KC-4.3.I.B's two halves look like side by side, and reversing the "
       "two states inverts it.")),
 dict(
  q=("Against which group does the framework's illustrative list name restrictive policies in Qing "
     "China?"),
  choices=[
   "Han Chinese",
   "Gujarati merchants",
   "Russian boyars",
   "Ottoman timar holders",
   "Javanese merchants"],
  ans=0,
  why=("The illustrative examples for this topic name restrictive policies against Han Chinese in "
       "Qing China under the heading of differential treatment of groups, illustrating "
       "KC-4.3.I.B's second half. The merchants named belong to KC-4.3.II.A.iii's Indian Ocean "
       "networks and the boyars and timars to the separate heading of existing elites.")),
 dict(
  q=("One of the framework's illustrative examples of differential treatment concerns status "
     "within a single empire. Which example is it?"),
  choices=[
   "The varying status of different classes of women within the Ottoman Empire",
   "The equal status of every subject of the Mughal Empire",
   "The uniform status of merchants across the Indian Ocean",
   "The identical status of all elites in Qing China",
   "The equal status of every group in Spain and Portugal"],
  ans=0,
  why=("The illustrative examples print the varying status of different classes of women within "
       "the Ottoman Empire under the heading of differential treatment of groups in society, "
       "politics, and the economy, illustrating KC-4.3.I.B. Each rejected option asserts a "
       "uniformity the framework never claims for any state.")),
 dict(
  q=("Which groups are printed among the framework's illustrative examples of existing elites?"),
  choices=[
   "Ottoman timars, Russian boyars, and the European nobility",
   "The Casta system of the Americas and the Qing elite of China",
   "Gujarati, Javanese, and Omani merchants",
   "Maroon societies of the Caribbean and Brazil",
   "The Asante and the Kingdom of the Kongo"],
  ans=0,
  why=("The illustrative examples for this topic print Ottoman timars, Russian boyars and the "
       "European nobility under the heading of existing elites, which is what KC-4.2.III.B means "
       "by existing political and economic elites. The Casta system and the Qing transition are "
       "KC-4.2.III.A's NEW elites.")),
 dict(
  q=("A student is sorting the elites this topic names into those the framework calls new and "
     "those it calls existing. Which sorting follows the framework?"),
  choices=[
   "The Casta system among the new elites, and the Russian boyars among the existing elites",
   "The Russian boyars among the new elites, and the Casta system among the existing elites",
   "Both the Casta system and the Russian boyars among the new elites",
   "Both the Casta system and the Russian boyars among the existing elites",
   "Neither the Casta system nor the Russian boyars is named in this topic"],
  ans=0,
  why=("KC-4.2.III.A names the rise of the Casta system in the Americas among the new political "
       "and economic elites formed in this period, while the illustrative examples print Russian "
       "boyars under the heading of existing elites, which belongs to KC-4.2.III.B. The rejected "
       "sortings exchange the two or collapse them into one category.")),
 dict(
  q=("Qing China appears in two different places in the framework's account of this topic. Which "
     "statement describes both appearances correctly?"),
  choices=[
   "The transition to the Qing Dynasty is given as the formation of a new elite, and restrictive policies against Han Chinese are given as differential treatment of a group",
   "The transition to the Qing Dynasty is given as differential treatment of a group, and restrictive policies against Han Chinese as the formation of a new elite",
   "Both appearances concern the formation of new elites",
   "Both appearances concern the accommodation of diversity",
   "Qing China appears only once in the framework's account of this topic"],
  ans=0,
  why=("KC-4.2.III.A names China with the transition to the Qing Dynasty among the new political "
       "and economic elites, while the illustrative examples name restrictive policies against Han "
       "Chinese in Qing China under differential treatment of groups, illustrating KC-4.3.I.B's "
       "second half. Both are printed and they are different statements about the same state.")),
 dict(
  q=("Unit 4: Learning Objective M asks students to explain how something has been maintained or "
     "has changed over time. What?"),
  choices=[
   "Social categories, roles, and practices",
   "Maritime technology and navigational skill",
   "The circulation of silver through global markets",
   "The exchange of plants and animals between hemispheres",
   "The sponsorship of exploration by states"],
  ans=0,
  why=("Unit 4: Learning Objective M asks how social categories, roles, and practices have been "
       "maintained or have changed over time, which is why KC-4.3.I.B, KC-4.2.III.A and "
       "KC-4.2.III.B are printed beside it. The rejected options belong to Learning Objectives A, "
       "I, D and B of the same unit.")),
 dict(
  q=("Suggested skill 3.D asks how claims or evidence support, modify, or refute a source's "
     "argument. A hypothetical source argues that the states of this period were uniformly hostile "
     "to minorities. Which evidence would most directly modify that argument?"),
  choices=[
   "Evidence that some states adopted practices to accommodate the diversity of their subjects and to use their contributions",
   "Evidence that the source was written by an official",
   "Evidence that the source survives in several copies",
   "Evidence that the source uses figures as well as prose",
   "Evidence that the source is shorter than others of its kind"],
  ans=0,
  why=("KC-4.3.I.B says many states, such as the Mughal and Ottoman empires, adopted practices to "
       "accommodate ethnic and religious diversity or to utilize the contributions of different "
       "groups, while in other cases states suppressed diversity, so evidence of the first half "
       "modifies a claim of uniform hostility without simply refuting it. Authorship, copies, "
       "figures and length are features of the document rather than evidence about its claim.")),
 dict(
  q=("A hypothetical decree of the period grants a religious community the right to settle its own "
     "civil disputes before its own judges, and confirms its members in trades they already "
     "practise.\n\n"
     "Which part of the framework's account does the decree illustrate?"),
  choices=[
   "A practice adopted to accommodate the diversity of a state's subjects",
   "A practice by which a state suppressed diversity",
   "The formation of a new political and economic elite",
   "A fluctuation in the power of an existing elite",
   "A restrictive trade policy adopted against foreign merchants"],
  ans=0,
  why=("KC-4.3.I.B says many states adopted practices to accommodate the ethnic and religious "
       "diversity of their subjects or to utilize their contributions, and a grant of separate "
       "courts together with confirmed trades is such a practice. The rejected options are the "
       "second half of the same sentence, KC-4.2.III.A, KC-4.2.III.B and KC-4.3.II.A.i.")),
 dict(
  q=("A hypothetical register from a conquered province lists the families who have taken over the "
     "chief offices and the largest estates since the conquest, none of whom held either "
     "before.\n\n"
     "Which statement of the framework does the register illustrate?"),
  choices=[
   "That imperial conquests contributed to the formation of new political and economic elites",
   "That the power of existing elites fluctuated",
   "That states adopted practices to accommodate religious diversity",
   "That states suppressed diversity or limited certain groups' roles",
   "That enslaved persons challenged existing authorities through organized resistance"],
  ans=0,
  why=("KC-4.2.III.A says imperial conquests and widening global economic opportunities "
       "contributed to the formation of new political and economic elites, and a province whose "
       "offices and estates have passed to families that held neither before is that formation. "
       "The rejected options are KC-4.2.III.B, both halves of KC-4.3.I.B, and KC-5.3.III.C.")),
 dict(
  q=("Four practices recorded in a hypothetical state's papers appear in the table below.\n\n"
     "How do they fall against the framework's account of how states treated the groups within "
     "them?"),
  table=_T_PRACTICES,
  choices=[
   "Two accommodate diversity or use the contributions of different groups, one limits a group's role, and one does neither",
   "All four accommodate diversity or use the contributions of different groups",
   "All four limit the roles of particular groups",
   "Two limit the roles of particular groups and two do neither",
   "None of the four bears on the treatment of groups at all"],
  ans=0,
  why=("KC-4.3.I.B names both accommodating the ethnic and religious diversity of subjects or "
       "using the contributions of different groups, and suppressing diversity or limiting certain "
       "groups' roles. Separate courts and mixed recruitment are the first, a bar on office is the "
       "second, and a tax charged alike to every household distinguishes no group at all. The "
       "verifier recomputes how each row falls.")),
 dict(
  q=("A hypothetical survey of four elite groups appears in the table below.\n\n"
     "Which conclusion is best supported by the table?"),
  table=_T_ELITES,
  choices=[
   "Two of the groups are described as newly formed in this period and two as long established before it",
   "All four groups are described as newly formed in this period",
   "All four groups are described as long established before this period",
   "Three of the groups are described as newly formed and one as long established",
   "None of the groups is described as either newly formed or long established"],
  ans=0,
  why=("KC-4.2.III.A describes new political and economic elites formed through imperial conquests "
       "and widening global economic opportunities, while KC-4.2.III.B describes existing elites "
       "whose power fluctuated, and the survey holds two of each. The verifier recomputes the "
       "split.")),
 dict(
  q=("A hypothetical council record of the petitions an existing elite brought before its monarch "
     "appears in the table below.\n\n"
     "Which statement about the recorded figures is accurate?"),
  table=_T_PETITIONS,
  choices=[
   "The share of petitions granted falls, then rises, then falls again rather than moving in one direction",
   "The share of petitions granted rises in every period shown",
   "The share of petitions granted falls in every period shown",
   "The share of petitions granted is the same in every period shown",
   "Every petition brought by the elite was granted in every period"],
  ans=0,
  why=("KC-4.2.III.B says the power of existing political and economic elites fluctuated as they "
       "confronted new challenges to their ability to affect the policies of increasingly powerful "
       "monarchs, and a record that moves down, up and down again is what fluctuation looks like. "
       "The verifier recomputes the share granted in each period and confirms it is not "
       "monotonic.")),
 dict(
  q=("This topic's reasoning process is continuity and change. Which pairing of a continuity with "
     "a change does the framework support?"),
  choices=[
   "Existing elites persisted while their power fluctuated, and new political and economic elites were formed",
   "Existing elites disappeared, and no new elites were formed",
   "New elites were formed, and the framework records no existing elites at all",
   "Existing elites held constant power, and no new elites appeared",
   "Neither existing nor new elites are described by the framework for this period"],
  ans=0,
  why=("KC-4.2.III.B has existing political and economic elites confronting new challenges with "
       "their power fluctuating, which presupposes their persistence, and KC-4.2.III.A has new "
       "political and economic elites formed by imperial conquests and widening global economic "
       "opportunities. Each rejected pairing deletes one of those two statements.")),
 dict(
  q=("Which of the following claims about this topic would require evidence from outside the "
     "framework's own statements?"),
  choices=[
   "That accommodation of diversity was more common in this period than suppression of it",
   "That many states adopted practices to accommodate the diversity of their subjects",
   "That in other cases states suppressed diversity or limited certain groups' roles",
   "That imperial conquests contributed to the formation of new political and economic elites",
   "That the power of existing elites fluctuated"],
  ans=0,
  why=("The four rejected statements are KC-4.3.I.B, KC-4.2.III.A and KC-4.2.III.B almost "
       "verbatim. KC-4.3.I.B records both accommodation and suppression without saying which was "
       "commoner, so a comparison of their frequency would have to be defended from another "
       "source.")),
 dict(
  q=("A student writes that every state in this period suppressed the minorities within it. What "
     "is the most accurate correction from the framework?"),
  choices=[
   "Many states adopted practices to accommodate diversity or to use the contributions of different groups, though in other cases states did suppress it",
   "No state in the period limited any group's role in society or politics",
   "Every state accommodated diversity without exception",
   "The framework says nothing about how states treated the groups within them",
   "Suppression is recorded only for states outside Asia"],
  ans=0,
  why=("KC-4.3.I.B says many states, such as the Mughal and Ottoman empires, adopted practices to "
       "accommodate ethnic and religious diversity or to utilize the contributions of different "
       "groups, and that in other cases states suppressed diversity or limited certain groups' "
       "roles. A correction has to keep both halves, and each rejected option deletes one of "
       "them.")),
 dict(
  q=("A student writes that the old landed elites of this period lost their influence once and for "
     "all. How should the claim be assessed against the framework?"),
  choices=[
   "It overstates the framework, which says the power of existing elites fluctuated as they met new challenges",
   "It is supported, because the framework says existing elites lost all influence",
   "It is supported, because the framework says the new elites replaced the old entirely",
   "It is contradicted, because the framework says the power of existing elites only grew",
   "It is contradicted, because the framework says no challenge to the existing elites arose"],
  ans=0,
  why=("KC-4.2.III.B says the power of existing political and economic elites fluctuated as the "
       "elites confronted new challenges to their ability to affect the policies of the "
       "increasingly powerful monarchs and leaders. Fluctuation is neither a permanent loss nor a "
       "steady gain, so both the supporting and the flatly contradicting readings go beyond the "
       "sentence.")),
 dict(
  q=("The Social Interactions and Organization thematic focus is printed with this topic. Which of "
     "its statements does this topic's content bear on most directly?"),
  choices=[
   "That the process by which societies group their members, and the norms governing those groups, influence political, economic, and cultural institutions",
   "That the environment shapes human societies and populations shape their environments",
   "That governments obtain, retain, and exercise power in different ways",
   "That human adaptation and innovation have increased efficiency and security",
   "That societies are affected by the ways they produce and exchange goods"],
  ans=0,
  why=("The Social Interactions and Organization thematic focus printed with this topic says the "
       "process by which societies group their members and the norms that govern the interactions "
       "between those groups influence political, economic, and cultural institutions and "
       "organization, which is what KC-4.3.I.B, KC-4.2.III.A and KC-4.2.III.B describe. The "
       "rejected statements are the other four thematic focuses of the course.")),
 dict(
  q=("Which piece of evidence would best support the framework's claim that new economic elites "
     "formed as global economic opportunities widened?"),
  choices=[
   "Records showing families that made their fortunes in long-distance trade entering the highest ranks of a society",
   "Records of the rainfall in a single province over one year",
   "Records of the stone used to build a provincial fortress",
   "Records of the number of ships wrecked on one coast",
   "Records of the names of a monarch's household servants"],
  ans=0,
  why=("KC-4.2.III.A says imperial conquests and widening global economic opportunities "
       "contributed to the formation of new political and economic elites, so evidence for the "
       "economic half has to connect commercial wealth with a rise in social rank. Rainfall, "
       "building stone, wrecks and servants' names bear on none of it.")),
 dict(
  q=("What is the clearest difference between the two illustrative headings the framework prints "
     "beside this topic?"),
  choices=[
   "One collects instances of differential treatment of groups, the other collects elites that already existed",
   "One collects conflicts between states, the other conflicts within a ruling family",
   "One collects labor systems, the other trading networks",
   "One collects events before 1450, the other events after 1750",
   "The two headings collect the same material under different names"],
  ans=0,
  why=("The first heading, differential treatment of groups in society, politics, and the economy, "
       "illustrates KC-4.3.I.B, while the second, existing elites, illustrates KC-4.2.III.B's "
       "account of elites whose power fluctuated. Conflicts between states are KC-4.3.III.i and "
       "KC-4.3.III.ii, and labor systems and trading networks belong to other topics of this "
       "unit.")),
 dict(
  q=("A summary sentence for this topic is being drafted for students. Which version stays within "
     "what the framework asserts about the period 1450 to 1750?"),
  choices=[
   "Some states accommodated the diversity of their subjects or drew on the contributions of different groups while others suppressed it, imperial conquest and wider economic opportunity formed new elites such as the Qing and the Casta system, and the power of long-standing elites fluctuated as monarchs grew more powerful",
   "Every state of the period suppressed the groups within it, and no new elite was formed",
   "Every state of the period accommodated the groups within it, and existing elites steadily gained power",
   "New elites replaced existing elites everywhere, and no state limited any group's role",
   "The framework records no change in social categories, roles, or practices in this period"],
  ans=0,
  why=("The keyed sentence joins both halves of KC-4.3.I.B to KC-4.2.III.A's new elites and "
       "KC-4.2.III.B's fluctuating existing elites. Each rejected version flattens KC-4.3.I.B to "
       "one half, asserts a direction where the framework says fluctuated, or denies the change "
       "Unit 4: Learning Objective M asks students to explain.")),
]
