# AP U.S. GOVERNMENT AND POLITICS 2.6 Expansion of Presidential Power -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# Learning objective 2.6.A: explain how presidents have interpreted and
# justified their use of formal and informal powers.
# Suggested skill for this topic (CED p. 66): 4.A, DESCRIBE THE ARGUMENT,
# PERSPECTIVE, EVIDENCE, AND REASONING PRESENTED IN THE SOURCE. So this module
# is weighted to source items: a third of it prints a passage and asks what the
# argument is, which is what 4.A tests.
#
# Essential knowledge relied on. Only three statements, and the first supplies
# its own quotation, which is unusual and worth using:
#   EK 2.6.A.1 -- "Federalist No. 70 offers justification for a single executive
#     by arguing a strong executive is 'essential to the protection of the
#     country against foreign attacks, to the steady administration of the laws,
#     to the protection of property, and to the security of liberty.'" That
#     four-part list is quoted BY THE CED ITSELF, so it is examinable text and
#     items 5 and 6 use it verbatim.
#   EK 2.6.A.2 -- "Passage of the Twenty-Second Amendment, which established
#     presidential term limits, demonstrates concern about the expansion of
#     presidential power."
#   EK 2.6.A.3 -- "Different perspectives on the presidential role, ranging from
#     a limited to a more expansive interpretation and use of power, continue to
#     be debated in the context of contemporary events."
#
# WHAT FEDERALIST NO. 70 ARGUES, AND WHAT IT DOES NOT. Hamilton's case is for a
# SINGLE executive against a PLURAL one -- a committee -- and for energy in that
# office. It is not a case against checks on the presidency, and reading it that
# way is the standard error. EK 2.6.A.1's own four-part list makes the point:
# the last item is "the security of liberty," which is a reason FOR the design
# rather than an exemption from it. Items 5 to 12 are written so a student who
# has flattened Hamilton into "the president should be unchecked" gets them
# wrong.
#
# THE TWENTY-SECOND AMENDMENT IS EVIDENCE OF CONCERN, WHICH IS A CLAIM ABOUT
# WHAT ITS PASSAGE SHOWS. EK 2.6.A.2 does not say term limits caused anything or
# that presidential power stopped expanding. It says the amendment's passage
# DEMONSTRATES CONCERN about expansion. Items 13 to 17 keep the claim at that
# strength, because the stronger version is false and easy to write.
#
# Documents the CED attaches to 2.6.A (p. 26-27): Federalist No. 10,
# Federalist No. 51, Federalist No. 70.
# Required cases the CED attaches to 2.6.A (p. 32-33): New York Times Co. v.
# United States.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: the Federalist No. 70 four-part list is
# the CED's own quotation; other Federalist No. 70 excerpts and the text of the
# Twenty-Second Amendment are quoted verbatim. William Howard Taft's and
# Theodore Roosevelt's writings are ILLUSTRATIVE EXAMPLES in the CED, not
# required documents, so their positions are DESCRIBED and never quoted, and no
# item requires a student to have read them.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. The
# verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.6", "Expansion of Presidential Power", 2)

_GROWTH = ("In a hypothetical study, the table reports the average number of times per year "
           "that presidents used each instrument, by era.")
_GROWTH_TABLE = dict(
    headers=["Era", "Executive orders per year", "Executive agreements per year", "Treaties ratified per year"],
    rows=[["Early republic", "2", "1", "4"],
          ["Late nineteenth century", "12", "6", "9"],
          ["Mid twentieth century", "48", "97", "8"],
          ["Recent decades", "41", "215", "3"]])

_VIEWS = ("In a hypothetical survey, respondents were asked whether the president should be "
          "able to act without congressional approval in each of four situations.")
_VIEWS_TABLE = dict(
    headers=["Situation", "Should be able to act alone (%)", "Should require Congress (%)"],
    rows=[["Responding to a sudden armed attack", "78", "22"],
          ["Committing troops to a long conflict", "24", "76"],
          ["Reorganizing an executive agency", "61", "39"],
          ["Creating a new federal program", "17", "83"]])

QUESTIONS = [
 dict(q="According to the course framework, Federalist No. 70 offers a justification for",
   choices=[
     "a single executive",
     "a plural executive composed of several officers of equal rank",
     "the abolition of the veto power",
     "the election of the president by Congress",
     "a president who serves during good behavior rather than for a fixed term"], ans=0,
   why="EK 2.6.A.1 says Federalist No. 70 offers justification for a SINGLE executive. Hamilton's argument is directed against a plural executive, which is the second option."),

 dict(q="What is the central contrast Federalist No. 70 draws in arguing for the design of the executive?",
   choices=[
     "Between a single executive and an executive divided among several officers",
     "Between an executive chosen by the people and one chosen by Congress",
     "Between an executive with a veto and one without",
     "Between a president and a prime minister",
     "Between national and state executive authority"], ans=0,
   why="EK 2.6.A.1 frames the paper as a justification for a single executive, and the alternative Hamilton is arguing against is dividing the office among several holders."),

 dict(q="Read the following excerpt.\n\n“Energy in the executive is a leading character in the definition of good government. It is essential to the protection of the community against foreign attacks; it is not less essential to the steady administration of the laws.”\n—Alexander Hamilton, Federalist No. 70, 1788\n\nWhich statement best describes the argument in this passage?",
   choices=[
     "That an executive capable of acting decisively is part of what makes a government good, not a departure from good government",
     "That the executive should be free from any check by Congress or the courts",
     "That the executive should be divided among several officials to prevent haste",
     "That the legislature rather than the executive should administer the laws",
     "That the executive's principal duty is to defer to public opinion"], ans=0,
   why="Hamilton is defining good government to include executive energy rather than excusing the executive from restraint. The second and third options state, respectively, a claim he does not make and the position he is arguing against."),

 dict(q="Read the following excerpt.\n\n“Decision, activity, secrecy, and despatch will generally characterise the proceedings of one man in a much more eminent degree than the proceedings of any greater number.”\n—Alexander Hamilton, Federalist No. 70, 1788\n\nWhat evidence does Hamilton offer for his conclusion in this passage?",
   choices=[
     "A comparison of how one person and a group behave when a decision must be made",
     "A list of the enumerated powers granted to the president by Article II",
     "An account of the failures of the Articles of Confederation's executive",
     "A survey of the executives of the several states",
     "A prediction about how future presidents will interpret their powers"], ans=0,
   why="The sentence is a claim about the comparative behavior of one man and a larger number, which is a comparison rather than a citation of text or of history. Skill 4.A asks what evidence a source actually offers."),

 dict(q="The course framework quotes Federalist No. 70 as arguing that a strong executive is essential to four things. Which of the following is one of them?",
   choices=[
     "The security of liberty",
     "The supremacy of the legislature",
     "The independence of the judiciary",
     "The sovereignty of the states",
     "The regulation of interstate commerce"], ans=0,
   why="EK 2.6.A.1 quotes the four: protection against foreign attacks, the steady administration of the laws, the protection of property, and the security of liberty. The other options name goods the passage does not mention."),

 dict(q="Which of the following is NOT one of the four things the course framework quotes Federalist No. 70 as calling a strong executive essential to?",
   choices=[
     "The expansion of the president's authority over time",
     "The protection of the country against foreign attacks",
     "The steady administration of the laws",
     "The protection of property",
     "The security of liberty"], ans=0,
   why="EK 2.6.A.1's quoted list contains the other four. An argument that the office should GROW is precisely what Hamilton's four purposes do not say, and reading it in is the standard misuse of this paper."),

 dict(q="A president cites Federalist No. 70 to argue that Congress should not restrict his authority to direct military operations. What is the most accurate assessment of that use of the source?",
   choices=[
     "The paper supports an energetic single executive but does not argue that the executive should be exempt from congressional checks",
     "The paper directly holds that Congress may not regulate military operations",
     "The paper argues that the executive power should be shared with a council of state",
     "The paper concerns only the appointment power and is irrelevant to military authority",
     "The paper argues that the president's powers derive from Congress rather than from the Constitution"], ans=0,
   why="EK 2.6.A.1 describes the paper as a justification for a single executive, and its own four purposes include the security of liberty. Treating a defense of unity and energy as a defense of freedom from checks reads more into the source than it contains."),

 dict(q="Read the following excerpt.\n\n“A feeble Executive implies a feeble execution of the government. A feeble execution is but another phrase for a bad execution; and a government ill executed, whatever it may be in theory, must be, in practice, a bad government.”\n—Alexander Hamilton, Federalist No. 70, 1788\n\nWhat is the structure of the reasoning here?",
   choices=[
     "A chain of equivalences leading from a weak executive to a bad government",
     "An appeal to the authority of the state constitutions",
     "A comparison between the proposed Constitution and the Articles of Confederation",
     "A concession followed by a rebuttal",
     "An enumeration of the president's specific powers"], ans=0,
   why="The passage moves by restating each term as the next -- feeble executive, feeble execution, bad execution, bad government -- which is a chain rather than a comparison or a concession. Skill 4.A asks for the reasoning's shape."),

 dict(q="How does Federalist No. 51's account of checks and balances fit with Federalist No. 70's argument for an energetic executive?",
   choices=[
     "The two are complementary: the executive is made capable of acting, and the other branches are given the means to restrain it",
     "The two are contradictory, and the Constitution adopted only one of them",
     "Federalist No. 51 argues that the executive should be plural, which Federalist No. 70 rejects",
     "Federalist No. 70 argues that the branches should not check one another",
     "Both papers argue that the legislature should be the strongest branch"], ans=0,
   why="EK 1.6.A.2 credits Federalist No. 51 with explaining how separation of powers and checks and balances control abuses, and EK 2.6.A.1 credits Federalist No. 70 with justifying a single executive. Capacity and restraint are two halves of one design."),

 dict(q="A student writes that Federalist No. 70 predicted the modern expansion of presidential power. What is the most important qualification?",
   choices=[
     "The paper argues for the design of the office in 1788 and makes no claim about how far its powers would later grow",
     "The paper explicitly forecasts the growth of executive agreements and executive orders",
     "The paper argues that presidential power should shrink over time",
     "The paper was written after the Constitution was ratified and could not have predicted anything",
     "The paper concerns the judiciary rather than the executive"], ans=0,
   why="EK 2.6.A.1 describes the paper as a justification for a single executive, which is an argument about design. Reading a defense of unity as a forecast of later expansion confuses the argument with its consequences."),

 dict(q="According to the course framework, what does the passage of the Twenty-Second Amendment demonstrate?",
   choices=[
     "Concern about the expansion of presidential power",
     "That presidential power stopped expanding once term limits were adopted",
     "That the framers had intended term limits from the beginning",
     "That Congress may set the length of a presidential term by statute",
     "That the president may be removed by a vote of the states"], ans=0,
   why="EK 2.6.A.2 says the amendment's passage 'demonstrates concern about the expansion of presidential power.' It is a claim about what the passage shows, not a claim that the expansion stopped."),

 dict(q="Read the following excerpt.\n\n“No person shall be elected to the office of the President more than twice, and no person who has held the office of President, or acted as President, for more than two years of a term to which some other person was elected President shall be elected to the office of the President more than once.”\n—U.S. Constitution, Twenty-Second Amendment\n\nWhich statement about this provision is accurate?",
   choices=[
     "It limits how many times a person may be elected president, and treats a partial term of more than two years as one of those times",
     "It limits the total number of years any person may serve as president to four",
     "It applies only to a president who has served two full terms",
     "It permits unlimited re-election so long as the terms are not consecutive",
     "It authorizes Congress to remove a president who has served too long"], ans=0,
   why="The amendment's second clause is what makes a long partial term count, which is why the answer must mention it. Nothing in the text gives Congress a removal power or permits nonconsecutive unlimited service."),

 dict(q="Why does the course framework treat a constitutional amendment as evidence about presidential power rather than merely as a procedural rule?",
   choices=[
     "Amending the Constitution requires broad supermajorities, so the effort itself indicates widespread concern",
     "Amendments take effect only when the president signs them",
     "Amendments may be adopted by a simple majority of Congress when the presidency is at issue",
     "Amendments are proposed by the Supreme Court in response to executive overreach",
     "Amendments are the only way Congress can check the president"], ans=0,
   why="EK 1.5.A.2's thresholds -- two-thirds to propose and three-fourths to ratify -- mean an amendment records agreement far beyond a passing majority, which is why EK 2.6.A.2 can read the amendment as evidence of concern."),

 dict(q="A commentator argues that the Twenty-Second Amendment failed to arrest the growth of presidential power. Is that consistent with the course framework?",
   choices=[
     "Yes, because the framework claims only that the amendment's passage demonstrates concern, not that it reversed the trend",
     "No, because the framework claims that the amendment ended the expansion of presidential power",
     "No, because the framework says nothing about the Twenty-Second Amendment",
     "Yes, because the framework says the amendment was never ratified",
     "No, because the framework treats the amendment as an expansion of presidential power"], ans=0,
   why="EK 2.6.A.2 states only that the amendment's passage demonstrates concern about expansion, so a claim about whether it worked neither confirms nor contradicts the framework."),

 dict(q="Which piece of evidence would best support the claim that concern about presidential power has been a recurring theme rather than a single episode?",
   choices=[
     "Congress and the courts have repeatedly acted to constrain executive action across different eras and under presidents of both parties",
     "A single amendment limiting presidential terms was adopted in the twentieth century",
     "Presidents have issued more executive orders in recent decades than in the nineteenth century",
     "The Executive Office of the President employs more staff than it once did",
     "Presidents deliver an annual address to Congress"], ans=0,
   why="A claim about recurrence needs evidence spread across time and across administrations of both parties. A single amendment, larger staffs and more orders each describe one episode or the growth itself rather than recurring resistance to it."),

 dict(q="According to the course framework, perspectives on the presidential role",
   choices=[
     "range from a limited to a more expansive interpretation and use of power, and continue to be debated in the context of contemporary events",
     "have converged on a single interpretation accepted by both parties",
     "were settled by the Twenty-Second Amendment",
     "are set by the Supreme Court and are not open to debate",
     "concern only foreign policy and not domestic policy"], ans=0,
   why="EK 2.6.A.3 states the range and says the debate continues in the context of contemporary events, which is why the framework treats this as an ongoing argument rather than a settled question."),

 dict(q="A president argues that the office may take any action not forbidden by the Constitution or by statute. Where does that view fall on the range the course framework describes?",
   choices=[
     "At the expansive end, since it treats silence in the law as permission",
     "At the limited end, since it acknowledges that statutes bind the president",
     "Outside the range entirely, since the framework describes only foreign policy views",
     "At the limited end, since it requires a constitutional provision for every action",
     "Outside the range, since no president has ever held such a view"], ans=0,
   why="EK 2.6.A.3's range runs from limited to expansive, and a view that reads legal silence as authorization sits at the expansive end. The fourth option describes the opposite view, which requires an affirmative grant."),

 dict(q="A president argues that the office may act only where the Constitution or a statute affirmatively grants authority. Where does that view fall on the range the course framework describes?",
   choices=[
     "At the limited end, since it requires an affirmative grant for every action",
     "At the expansive end, since it lets the president act whenever a statute is silent",
     "Outside the range, since the framework describes only informal powers",
     "At the expansive end, since it relies on the vested executive power",
     "Outside the range, since it describes the powers of Congress rather than the president"], ans=0,
   why="EK 2.6.A.3's limited end is a reading that confines the office to what has been granted, which is exactly the view described. The second option states the expansive view, its opposite."),

 dict(q="In New York Times Co. v. United States (1971), the Supreme Court bolstered freedom of the press, establishing a heavy presumption against prior restraint even in cases involving national security. How does the case bear on the expansion of presidential power?",
   choices=[
     "It set a judicial limit on an executive claim of authority justified by national security",
     "It expanded the president's authority over the press during wartime",
     "It held that the president may restrain publication whenever secrecy is claimed",
     "It concerned only state governments and not the executive branch",
     "It held that the press may be regulated by Congress but not by the president"], ans=0,
   why="The CED states the holding as a heavy presumption against prior restraint even in national security cases, and the restraint sought there came from the executive. The case is thus a check on an expansive executive claim."),

 dict(q="Which pair best illustrates the two directions of change in presidential power that the course framework describes?",
   choices=[
     "Growing use of executive agreements and executive orders, alongside the Twenty-Second Amendment and judicial limits on executive claims",
     "Growing use of executive agreements, alongside the growth of the Executive Office of the President",
     "The Twenty-Second Amendment, alongside the requirement that revenue bills originate in the House",
     "The Senate's confirmation power, alongside the House's power of impeachment",
     "The president's veto, alongside the president's power to grant pardons"], ans=0,
   why="EK 2.6.A.3's range implies movement in both directions, so the pair must include an instrument of expansion and an instrument of constraint. The second option names two expansions and the last two names only presidential or congressional powers."),

 dict(q=_GROWTH + " Which pattern is best supported by the data?",
   table=_GROWTH_TABLE,
   choices=[
     "Executive agreements grew far more than any other instrument, while treaties ratified per year fell below their early republic level",
     "All three instruments grew steadily across the four eras",
     "Treaties ratified per year grew faster than executive agreements",
     "Executive orders were the most used instrument in every era",
     "Executive agreements were used less often than treaties in every era"], ans=0,
   why="Executive agreements run 1, 6, 97 and 215 while treaties run 4, 9, 8 and 3, ending below the early figure. Executive orders fall from 48 to 41 in the last era, and agreements overtake treaties in the two most recent eras, so they are not always fewer."),

 dict(q=_GROWTH + " Which claim about presidential power do these data most directly support?",
   table=_GROWTH_TABLE,
   choices=[
     "Presidents came to rely on an instrument that requires no Senate vote in place of one that does",
     "Presidents came to rely on instruments requiring Senate ratification",
     "Presidents abandoned the use of executive orders",
     "Congress prohibited the use of executive agreements",
     "The Twenty-Second Amendment reduced the use of all three instruments"], ans=0,
   why="EK 2.4.A.2.ii makes executive agreements informal and treaties formal with Senate concurrence, and the table shows one rising as the other falls. Executive orders remain in the dozens per year in both recent eras."),

 dict(q=_GROWTH + " A student concludes from these data that presidential power is now greater than at any time in history. Which limitation of the data most undercuts that conclusion?",
   table=_GROWTH_TABLE,
   choices=[
     "Counting instruments measures activity, not authority, and says nothing about what constrains the president",
     "The table omits executive agreements, so no comparison is possible",
     "The table covers a single era, so no trend can be observed",
     "The table reports percentages that do not sum to one hundred",
     "The table gives no information about the number of treaties ratified"], ans=0,
   why="A tally of actions cannot show whether the actions were more consequential or less checked, and EK 2.6.A.3's debate is precisely about authority. All three instruments and four eras are plainly in the table."),

 dict(q=_VIEWS + " Which conclusion is best supported by the data?",
   table=_VIEWS_TABLE,
   choices=[
     "Support for unilateral presidential action varies sharply by situation, from seventeen percent to seventy-eight percent",
     "A majority favors unilateral presidential action in every situation",
     "A majority opposes unilateral presidential action in every situation",
     "Support is roughly the same across all four situations",
     "Support is highest for creating a new federal program"], ans=0,
   why="The four figures for acting alone are 78, 24, 61 and 17, a spread of sixty-one points. Majorities favor acting alone in two situations and oppose it in the other two."),

 dict(q=_VIEWS + " Which generalization about the two situations where a majority favors unilateral action is best supported?",
   table=_VIEWS_TABLE,
   choices=[
     "Both involve either an emergency or the internal management of the executive branch, rather than the creation of new policy",
     "Both involve the commitment of military force over a long period",
     "Both involve the creation of new federal programs",
     "Both involve actions requiring the appropriation of new money",
     "Both involve powers the Constitution assigns to Congress"], ans=0,
   why="The two majorities are responding to a sudden armed attack and reorganizing an agency, which are an emergency and an internal management action; the two situations that draw opposition both create new commitments."),

 dict(q=_VIEWS + " Which claim from the course framework do these data most directly illustrate?",
   table=_VIEWS_TABLE,
   choices=[
     "That perspectives on the presidential role range from limited to expansive and continue to be debated",
     "That the Twenty-Second Amendment demonstrates concern about the expansion of presidential power",
     "That Federalist No. 70 justifies a single executive",
     "That Senate confirmation is a check on the appointment power",
     "That vetoes can be overridden while pocket vetoes cannot"], ans=0,
   why="EK 2.6.A.3 describes an ongoing debate across a range of views, and a survey in which the same public takes the expansive side on two questions and the limited side on two others is that debate measured."),

 dict(q="A scholar argues that the growth of presidential power is best explained by Congress rather than by presidents. Which evidence would most support that argument?",
   choices=[
     "Congress has repeatedly enacted statutes delegating broad discretion to the executive branch",
     "Presidents have issued more executive orders in recent decades",
     "The Executive Office of the President has grown in size",
     "Presidents have used the bully pulpit to build public support",
     "Federalist No. 70 argued for an energetic single executive"], ans=0,
   why="EK 2.4.A.2.iv grounds executive orders partly in power delegated by Congress, so evidence that Congress handed over discretion locates the cause in the legislature. The other options describe executive activity or an eighteenth-century argument."),

 dict(q="Which question would best test the framework's claim that debate over the presidential role continues in the context of contemporary events?",
   choices=[
     "When a president takes a contested action, do the arguments made for and against it track the limited and expansive interpretations the framework describes?",
     "How many executive orders has the current president issued?",
     "How large is the Executive Office of the President?",
     "How often does the president address the nation?",
     "How many treaties has the Senate ratified in the past decade?"], ans=0,
   why="EK 2.6.A.3's claim is about the CONTENT OF THE DEBATE, so the test has to examine the arguments made about particular contested actions rather than counting presidential activity."),

 dict(q="A president justifies an action by pointing to a statute's silence, and a senator responds by pointing to the same silence. What does the exchange best illustrate?",
   choices=[
     "The limited and expansive interpretations of presidential power reaching opposite conclusions from the same fact",
     "A disagreement about what the statute says",
     "A dispute over which chamber should consider the matter",
     "The Supreme Court's exclusive authority to interpret statutes",
     "The Twenty-Second Amendment's limit on presidential terms"], ans=0,
   why="EK 2.6.A.3's two ends differ on what silence means: permission on the expansive reading, absence of authority on the limited one. Both speakers agree about the text and disagree about its significance."),

 dict(q="Which statement best summarizes what the course framework says about presidential power in this topic?",
   choices=[
     "Presidents have justified their use of formal and informal powers by interpretation, and how far those powers reach remains contested",
     "The scope of presidential power was fixed by Article II and has not changed",
     "Presidential power has grown steadily with no institutional resistance",
     "Presidential power is determined entirely by the Supreme Court",
     "Presidential power was settled by Federalist No. 70 at the founding"], ans=0,
   why="LO 2.6.A asks how presidents have INTERPRETED AND JUSTIFIED their use of powers, and EK 2.6.A.3 says the resulting debate continues. The other options each deny either the interpretation or the continuing dispute."),
]
