# AP U.S. GOVERNMENT AND POLITICS 2.7 Presidential Communication -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# Learning objective 2.7.A: explain how communication technology has changed the
# president's relationship with the NATIONAL CONSTITUENCY and THE OTHER
# BRANCHES.
# Suggested skill for this topic (CED p. 67): 1.E, explain how political
# principles, institutions, processes, policies and behaviors apply to different
# scenarios in context.
#
# Essential knowledge relied on. ONE statement with two sub-items, which is the
# smallest content base of any topic in this unit:
#   EK 2.7.A.1 -- "The impact of presidential communication has increased with
#     advances in communication technology."
#     i.  "Modern technology, such as social media, allows for RAPID RESPONSES
#         to political issues."
#     ii. "Nationally broadcast State of the Union messages and the president's
#         BULLY PULPIT are tools for AGENDA SETTING that use the media to
#         influence public views about WHICH POLICIES ARE THE MOST IMPORTANT."
#
# HOW A THIRTY-ITEM MODULE ON ONE SENTENCE AVOIDS BEING ONE QUESTION THIRTY
# TIMES. The learning objective names TWO relationships -- the president and the
# national constituency, and the president and the other branches -- and the
# essential knowledge names TWO mechanisms -- rapid response and agenda setting.
# That is a two-by-two, and this module is built on it:
#
#     items 1-8    agenda setting toward the public (EK 2.7.A.1.ii)
#     items 9-14   rapid response toward the public (EK 2.7.A.1.i)
#     items 15-20  communication as leverage over the OTHER BRANCHES, which is
#                  the half of LO 2.7.A a bank usually forgets
#     items 21-26  the two data stimuli
#     items 27-30  limits, trade-offs and how the claim would be tested
#
# THE DEFINITION THAT CARRIES THE TOPIC: agenda setting is influence over WHICH
# POLICIES ARE SEEN AS MOST IMPORTANT -- not over what people believe about
# them, and not over what Congress enacts. EK 2.7.A.1.ii says so in those words.
# A president who changes what the country is arguing about has set the agenda
# even if he loses the argument, and items 3, 5 and 7 turn on exactly that.
#
# WHAT THIS MODULE DOES NOT DO: it names no living or recent president, no
# current platform beyond the CED's own "social media," and no contemporary
# controversy. The CED's illustrative example here is a 1981 address and is not
# required. Country-specific and person-specific claims date a bank and cannot
# be verified against the framework, which SOCIAL_BRIEF.md forbids.
#
# Documents the CED attaches to 2.7.A (p. 26-27): the Gettysburg Address.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: constitutional text and the Gettysburg
# Address (Bliss copy) are quoted verbatim. Both tables are labelled
# hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. The
# verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.7", "Presidential Communication", 2)

_REACH = ("In a hypothetical study, the table reports the share of adults who received a "
          "president's message through each channel, in three eras.")
_REACH_TABLE = dict(
    headers=["Channel", "Early era (%)", "Middle era (%)", "Recent era (%)"],
    rows=[["Printed newspaper account", "44", "21", "6"],
          ["Live radio or television broadcast", "9", "63", "28"],
          ["Recorded or streamed clip online", "0", "4", "51"],
          ["Direct message from the president's own account", "0", "0", "39"]])

_SALIENCE = ("In a hypothetical survey, respondents were asked to name the most important "
             "problem facing the country, in the week before and the week after a nationally "
             "broadcast presidential address devoted to infrastructure.")
_SALIENCE_TABLE = dict(
    headers=["Named as most important problem", "Week before (%)", "Week after (%)"],
    rows=[["Infrastructure", "6", "23"],
          ["The economy", "38", "31"],
          ["Health care", "24", "19"],
          ["Foreign affairs", "18", "14"],
          ["Other or no answer", "14", "13"]])

QUESTIONS = [
 dict(q="According to the course framework, the impact of presidential communication has",
   choices=[
     "increased with advances in communication technology",
     "decreased as the public has come to distrust the media",
     "remained constant since the founding",
     "been limited to the president's relationship with Congress",
     "depended entirely on whether the president's party controls Congress"], ans=0,
   why="EK 2.7.A.1 states this in exactly these words, and it is the claim the whole topic elaborates. The learning objective adds that the change runs both toward the public and toward the other branches."),

 dict(q="According to the course framework, the State of the Union message and the bully pulpit are tools for",
   choices=[
     "agenda setting, using the media to influence public views about which policies are most important",
     "vetoing legislation the president opposes",
     "issuing binding directives to executive agencies",
     "negotiating agreements with foreign governments",
     "confirming the president's nominees to the federal courts"], ans=0,
   why="EK 2.7.A.1.ii names both as tools for agenda setting and defines the effect as influencing public views about which policies are the most important. The other options name formal powers rather than communication."),

 dict(q="As the course framework defines it, agenda setting is influence over",
   choices=[
     "which policies the public sees as most important",
     "what the public believes about the merits of a policy",
     "how members of Congress vote on a bill",
     "which nominees the Senate confirms",
     "how federal agencies write their regulations"], ans=0,
   why="EK 2.7.A.1.ii's phrase is 'which policies are the most important,' which is about salience rather than persuasion. A president may set the agenda and still lose the argument about the policy."),

 dict(q="A president devotes a nationally broadcast address to a subject the public has not been discussing, and in the following weeks that subject is named far more often as the country's leading problem, although opinion on the president's proposal remains divided. What has the address accomplished?",
   choices=[
     "It has set the agenda, since it changed which issue the public treats as most important",
     "Nothing, since public opinion on the proposal did not move",
     "It has persuaded the public to support the president's position",
     "It has compelled Congress to act on the proposal",
     "It has exercised a formal power of the presidency"], ans=0,
   why="EK 2.7.A.1.ii defines the effect as influence over which policies are seen as most important, and that is precisely what changed. Divided opinion on the merits is consistent with successful agenda setting."),

 dict(q="Which of the following would be the best evidence that a presidential address succeeded at agenda setting as the course framework defines it?",
   choices=[
     "The share of the public naming the address's subject as the nation's most important problem rose sharply afterward",
     "A majority of the public came to agree with the president's proposal",
     "Congress passed the president's bill within a month",
     "The president's approval rating rose by several points",
     "News organizations reported that the speech was well delivered"], ans=0,
   why="Agenda setting is measured by salience, so the evidence must be a change in what the public names as most important. Agreement, enactment and approval are different outcomes, each of which can move without any change in the agenda."),

 dict(q="According to the course framework, what does modern technology such as social media allow a president to do?",
   choices=[
     "Respond rapidly to political issues",
     "Enact legislation without congressional approval",
     "Appoint officials without Senate confirmation",
     "Override a Supreme Court decision",
     "Extend a presidential term beyond its constitutional limit"], ans=0,
   why="EK 2.7.A.1.i says modern technology such as social media allows for rapid responses to political issues. The other four options describe powers no communication technology confers."),

 dict(q="What is the principal difference between the two tools EK 2.7.A.1 describes?",
   choices=[
     "One is a scheduled, formal address to a national audience; the other is an immediate response to events as they occur",
     "One is a formal constitutional power and the other is informal",
     "One is directed at Congress and the other at the courts",
     "One is available only in wartime and the other only in peacetime",
     "One requires the consent of the Senate and the other does not"], ans=0,
   why="EK 2.7.A.1.ii's State of the Union and bully pulpit are set-piece communication; EK 2.7.A.1.i's modern technology is about speed. Both are informal, and neither is directed at a single branch."),

 dict(q="Read the following excerpt.\n\n“He shall from time to time give to the Congress Information of the State of the Union, and recommend to their Consideration such Measures as he shall judge necessary and expedient.”\n—U.S. Constitution, Article II, Section 3\n\nHow has communication technology changed the practice this clause describes?",
   choices=[
     "A message addressed by the text to Congress now reaches a national audience directly, which makes it a tool for setting the public agenda",
     "The clause now requires the president to address the public rather than Congress",
     "The clause has been amended to require an annual televised address",
     "The president may now recommend measures only through the media",
     "Congress is now required to act on every measure the president recommends"], ans=0,
   why="The constitutional duty runs to Congress, and EK 2.7.A.1.ii's point is that broadcasting turns that message into an instrument aimed at the public as well. The text has not changed and imposes no duty on Congress to act."),

 dict(q="A president responds to a breaking political controversy within minutes through a direct online message, before news organizations have reported on it. Which claim from the course framework does this best illustrate?",
   choices=[
     "That modern technology allows for rapid responses to political issues",
     "That the State of the Union is a tool for agenda setting",
     "That the president's longest lasting influence lies in judicial appointments",
     "That executive orders allow the president to manage the federal government",
     "That Senate confirmation is a check on the appointment power"], ans=0,
   why="EK 2.7.A.1.i names rapid response as what modern technology such as social media enables, and speed is the defining feature of the scenario."),

 dict(q="What is the most significant change that direct communication from a president to the public introduces, compared with an era when the press was the only channel?",
   choices=[
     "The president can address the national constituency without an intermediary deciding what to report",
     "The president gains the power to prohibit news organizations from reporting",
     "The president is no longer subject to any check from Congress or the courts",
     "The press loses its constitutional protection once the president communicates directly",
     "The president is required to give equal time to opposing views"], ans=0,
   why="LO 2.7.A is about the president's relationship with the NATIONAL CONSTITUENCY, and the structural change is the removal of an editorial intermediary. Nothing about direct communication alters the First Amendment or the branches' powers."),

 dict(q="Which is the most important risk a president accepts by responding to events within minutes rather than after deliberation?",
   choices=[
     "A statement made before the facts are settled cannot be unsaid and may commit the administration to a position",
     "Rapid statements are not protected by the First Amendment",
     "Rapid statements require Senate confirmation before taking effect",
     "Rapid statements automatically become executive orders",
     "Rapid statements may be issued only when Congress is in session"], ans=0,
   why="EK 2.7.A.1.i identifies speed as what the technology enables, and speed's cost is acting on incomplete information. The remaining options describe legal consequences that communication does not carry."),

 dict(q="A president uses a series of short public messages over several weeks to keep attention on a single issue. Which pair of the framework's concepts does this combine?",
   choices=[
     "Rapid response, in the form of the messages, and agenda setting, in the sustained attention to one issue",
     "The veto and the pocket veto",
     "Executive orders and signing statements",
     "Treaties and executive agreements",
     "Impeachment and removal"], ans=0,
   why="EK 2.7.A.1.i supplies the speed and EK 2.7.A.1.ii the effect on what the public treats as important, and the scenario uses the first in service of the second."),

 dict(q="Which observation would most WEAKEN the claim that presidential communication has greater impact than it once did?",
   choices=[
     "The audience for any single presidential message is now split across many channels, so no message reaches the share of the public a broadcast address once did",
     "Presidents now speak publicly more often than they did a century ago",
     "More Americans own devices capable of receiving presidential messages",
     "Presidents now have staff dedicated to communication",
     "Presidential addresses are now archived and can be viewed later"], ans=0,
   why="EK 2.7.A.1's claim is about IMPACT, and audience fragmentation attacks impact directly while leaving the technology's reach intact. Frequency, device ownership and staffing all describe capacity rather than effect."),

 dict(q="Which of the following best describes how communication technology has changed the president's relationship with CONGRESS, as distinct from the public?",
   choices=[
     "A president who can mobilize public attention on an issue brings pressure to bear on members who must face those voters",
     "A president may now introduce legislation directly in either chamber",
     "A president may now vote in Congress on measures he has proposed",
     "A president may now compel a committee to report a bill",
     "A president may now address Congress only in writing"], ans=0,
   why="LO 2.7.A names the other branches as well as the national constituency, and the mechanism is indirect: attention among constituents becomes a legislator's problem. No communication technology gives a president a formal role in Congress."),

 dict(q="A president loses a legislative vote but the issue remains at the center of national debate for a year afterward. Which assessment is most consistent with the course framework?",
   choices=[
     "The president failed at legislating but succeeded at agenda setting, which the framework treats as a distinct effect",
     "The president failed at both, since agenda setting is measured by legislation enacted",
     "The president succeeded at both, since sustained debate is a form of enactment",
     "The framework does not distinguish between the two outcomes",
     "The president exercised a formal power that Congress overrode"], ans=0,
   why="EK 2.7.A.1.ii's effect is on which policies the public treats as most important, which is independent of whether a bill passes. Collapsing the two is the error the item is built to catch."),

 dict(q="How might a president's ability to speak directly to a national audience affect the JUDICIARY, if at all?",
   choices=[
     "Only indirectly, since courts decide cases on legal grounds and a president's public argument is not evidence before them",
     "Directly, since a president's public statements bind federal courts",
     "Directly, since courts must consider public opinion in every case",
     "Not at all, since presidents never comment publicly on litigation",
     "Directly, since a president may order a court to reconsider a decision"], ans=0,
   why="LO 2.7.A includes the other branches, and the honest answer for the judiciary is that the channel is indirect: public argument may shape the climate but is not a source of law. The direct options describe authority no president holds."),

 dict(q="Read the following excerpt.\n\n“Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.”\n—Abraham Lincoln, Gettysburg Address, 1863\n\nWhy is this address a useful example in a topic about presidential communication?",
   choices=[
     "It shows a president using a public occasion to define what the nation's central commitment is, which is agenda setting before broadcast technology existed",
     "It shows a president exercising a formal power granted by Article II",
     "It shows a president issuing a directive to the executive branch",
     "It shows a president responding rapidly to a political controversy",
     "It shows a president addressing Congress as required by the Constitution"], ans=0,
   why="The Address is a short public speech that reframed the war's meaning, which is influence over what the country treats as most important. EK 2.7.A.1's claim is that TECHNOLOGY increased that impact, not that it created the practice."),

 dict(q="A student writes that the bully pulpit is a power granted to the president by Article II. What is the correction?",
   choices=[
     "It is an informal instrument arising from the office's visibility, not a power the constitutional text confers",
     "It is a formal power, but one granted by statute rather than by Article II",
     "It is a power the Senate must confirm before each use",
     "It is a power shared with the Speaker of the House",
     "It is a power that expired with the adoption of the Twenty-Second Amendment"], ans=0,
   why="EK 2.7.A.1.ii lists the bully pulpit as a tool for agenda setting, and EK 2.4.A.2 places instruments of persuasion among the president's INFORMAL powers. No clause of Article II mentions it."),

 dict(q="Which scenario best illustrates a president using communication to affect the other branches rather than the public directly?",
   choices=[
     "A president publicizes the names of senators blocking a nominee, prompting constituents in those states to contact their offices",
     "A president issues an executive order reorganizing an agency",
     "A president vetoes a bill and returns it with objections",
     "A president signs a treaty submitted for Senate ratification",
     "A president appoints a judge to a district court"], ans=0,
   why="LO 2.7.A's second half is the relationship with the other branches, and the mechanism runs through the public back to the officeholder. The other four options are formal powers exercised without any communicative step."),

 dict(q="Which question would best distinguish agenda setting from persuasion in a study of presidential speeches?",
   choices=[
     "Did the share naming the topic as most important change, and did the share agreeing with the president's position change?",
     "Did the president's approval rating change after the speech?",
     "How many people watched the speech?",
     "How long did the speech last?",
     "How many times did the president mention Congress?"], ans=0,
   why="EK 2.7.A.1.ii defines the effect as salience, so distinguishing it from persuasion requires measuring both salience and agreement separately. Audience size and speech length measure neither."),

 dict(q=_REACH + " Which pattern is best supported by the data?",
   table=_REACH_TABLE,
   choices=[
     "The dominant channel changed in each era, and two channels that did not exist in the early era carry most of the recent audience",
     "The same channel was dominant in all three eras",
     "Printed newspaper accounts reached more adults in the recent era than in the early era",
     "Live broadcast reached its largest share in the recent era",
     "No channel reached more than half the public in any era"], ans=0,
   why="Newspapers lead the early era at 44, live broadcast the middle at 63, and streamed clips the recent at 51, with direct messages at 39. Newspapers fall from 44 to 6, live broadcast peaks in the middle era, and 63 exceeds half."),

 dict(q=_REACH + " Which claim from the course framework do these data most directly support?",
   table=_REACH_TABLE,
   choices=[
     "That advances in communication technology have changed how presidential messages reach the public",
     "That the State of the Union is required by the Constitution",
     "That vetoes can be overridden while pocket vetoes cannot",
     "That Senate confirmation is a check on the appointment power",
     "That the president's longest lasting influence lies in judicial appointments"], ans=0,
   why="EK 2.7.A.1 ties the impact of presidential communication to advances in technology, and a table in which two channels appear from nothing and one nearly disappears is that change measured."),

 dict(q=_REACH + " A student concludes from the data that presidents reach a larger share of the public now than ever before. Which limitation of the data most undercuts that conclusion?",
   table=_REACH_TABLE,
   choices=[
     "Respondents may have received a message through more than one channel, so the shares cannot simply be added to give total reach",
     "The table omits the recent era, so no comparison is possible",
     "The table reports only one channel, so no comparison across channels is possible",
     "The table covers a single era, so no trend can be observed",
     "The table gives no information about how any message was received"], ans=0,
   why="The recent column sums to 124 percent, which is only possible if channels overlap, so no total reach can be read off it. Four channels and three eras are plainly present."),

 dict(q=_SALIENCE + " Which conclusion is best supported by the data?",
   table=_SALIENCE_TABLE,
   choices=[
     "The address's subject rose by seventeen points while every other category fell",
     "Every category rose after the address",
     "The address's subject became the most frequently named problem",
     "The economy fell by more points than the address's subject rose",
     "The shares were unchanged from one week to the next"], ans=0,
   why="Infrastructure rises from 6 to 23 while the other four categories all fall. It remains behind the economy at 31, and the economy's fall of 7 points is smaller than infrastructure's rise of 17."),

 dict(q=_SALIENCE + " Which claim from the course framework do these data most directly illustrate?",
   table=_SALIENCE_TABLE,
   choices=[
     "That a nationally broadcast address is a tool for agenda setting, influencing which policies the public sees as most important",
     "That a nationally broadcast address persuades the public to support the president's proposal",
     "That modern technology allows for rapid responses to political issues",
     "That the president's communication compels Congress to act",
     "That the bully pulpit is a formal power under Article II"], ans=0,
   why="EK 2.7.A.1.ii's effect is on which policies are seen as most important, and the table measures exactly that. It reports nothing about whether anyone came to agree with the president or whether Congress acted."),

 dict(q=_SALIENCE + " A student concludes that the address CAUSED the change. Which limitation of the data most undercuts that conclusion?",
   table=_SALIENCE_TABLE,
   choices=[
     "Other events in the same week could have raised the subject's salience, and the table records no other variable",
     "The table omits the week after the address, so no comparison is possible",
     "The table reports counts rather than percentages, so no share can be computed",
     "The table covers a single category, so no comparison is possible",
     "The shares in each week do not sum to one hundred, so the table is invalid"], ans=0,
   why="A before-and-after comparison with no control cannot separate the address from anything else that happened that week. Both weeks, five categories and percentages summing to 100 are plainly present."),

 dict(q="A commentator argues that a president's ability to set the public agenda is a greater source of influence over policy than any formal power. Which counterargument is strongest?",
   choices=[
     "Agenda setting determines what is discussed but not what is enacted, and a bill still requires majorities in two chambers",
     "Agenda setting has no effect on public opinion of any kind",
     "Presidents cannot address the public without congressional approval",
     "Formal powers are exercised only in wartime",
     "The public pays no attention to presidential communication"], ans=0,
   why="EK 2.7.A.1.ii's effect is on salience, and the legislative process described in EK 2.2.A.3 still stands between salience and law. The other options deny facts the framework asserts."),

 dict(q="Why does the course framework treat the growth of presidential communication as part of a unit on INTERACTIONS AMONG BRANCHES rather than as a topic about the media alone?",
   choices=[
     "Because the president's ability to reach the public directly changes the president's leverage over Congress and the other branches",
     "Because the media are a fourth branch of government under the Constitution",
     "Because Congress regulates what the president may say",
     "Because the courts approve presidential addresses in advance",
     "Because communication technology is itself a formal power of the presidency"], ans=0,
   why="LO 2.7.A names the president's relationship with the other branches alongside the national constituency, which is why the topic belongs to a unit about interactions rather than to a unit about media."),

 dict(q="Which trade-off does a president face in using rapid, direct communication rather than a scheduled formal address?",
   choices=[
     "Speed and directness are gained, but the occasion's authority and the guaranteed national audience are given up",
     "Speed is gained and nothing is given up",
     "The president gains a formal power but loses an informal one",
     "The president gains Senate support but loses House support",
     "The president gains the ability to legislate but loses the veto"], ans=0,
   why="EK 2.7.A.1.i and EK 2.7.A.1.ii describe two instruments with different properties, and a set-piece address carries an audience and a solemnity that an immediate message does not. Neither instrument is a formal power."),

 dict(q="A researcher wants to test EK 2.7.A.1's claim that the impact of presidential communication has increased with technology. Which design would test it most directly?",
   choices=[
     "Compare, across eras, how much the public's ranking of the most important problem shifted after comparable presidential addresses",
     "Compare, across eras, how many words presidents used in their addresses",
     "Compare, across eras, how many presidents were re-elected",
     "Compare, across eras, how many executive orders presidents issued",
     "Compare, across eras, the size of the White House staff"], ans=0,
   why="The claim is about IMPACT, and EK 2.7.A.1.ii defines the relevant impact as influence on which policies are seen as most important, so the design must measure that shift across eras. Word counts, re-election and staffing measure other things."),
]
