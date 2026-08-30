# AP U.S. GOVERNMENT AND POLITICS 2.4 Roles and Powers of the President -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# Learning objective 2.4.A: explain how the president can implement a policy
# agenda.
# Suggested skill for this topic (CED p. 64): 3.B, DESCRIBE PATTERNS AND TRENDS
# IN DATA. This module carries nine data items across three tables, weighted to
# trend description rather than single-figure reading, because a trend is what
# skill 3.B asks for.
#
# Essential knowledge relied on:
#   EK 2.4.A.1 -- "Presidents use powers and perform functions of the office,
#     with support from the Vice-President, Cabinet, and Executive Office of the
#     President, to accomplish a policy agenda."
#   EK 2.4.A.2 -- "The powers of the president include both formal and informal
#     powers":
#     i.   VETOES and POCKET VETOES are FORMAL powers that check Congress, "but
#          vetoes can be overridden with a 2/3 vote while POCKET VETOES CANNOT
#          BE OVERRIDDEN with a 2/3 vote."
#     ii.  Foreign policy powers are both FORMAL (commander in chief, treaties)
#          and INFORMAL (executive agreements).
#     iii. BARGAINING AND PERSUASION are INFORMAL powers that enable the
#          president to secure congressional action.
#     iv.  EXECUTIVE ORDERS allow the president to manage the federal government
#          and are "implied by the president's vested executive power or by
#          power delegated by Congress."
#     v.   SIGNING STATEMENTS are INFORMAL powers that inform Congress and the
#          public of the president's interpretation of laws passed by Congress
#          and signed by the president.
#
# THE ONE FACT MOST BANKS GET WRONG, and the CED states it explicitly, so there
# is no room to hedge: A POCKET VETO CANNOT BE OVERRIDDEN. EK 2.4.A.2.i says so
# in the same sentence that says an ordinary veto can be. See AP_US_GOV_CED.md
# note 6. Items 5 to 8 and the data items at 24 and 25 all rest on that
# distinction, and no item in this module implies a pocket veto is subject to an
# override vote.
#
# THE FORMAL/INFORMAL SORT IS THE TOPIC'S SPINE, and it does not run along the
# lines a student expects. Both halves of the foreign policy pair are on the
# list: commander in chief and treaties are FORMAL, executive agreements are
# INFORMAL. Executive orders are on the list as a power implied by vested
# executive power or delegated by Congress rather than as a formal enumerated
# one. Items 9 to 16 test the sort itself rather than the definitions.
#
# Documents the CED attaches to 2.4.A (p. 26-27): the Emancipation Proclamation,
# Federalist No. 10, Federalist No. 51, Federalist No. 70, the Gettysburg
# Address.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: constitutional text and the Gettysburg
# Address (Bliss copy) are quoted verbatim; the Federalist No. 70 excerpt is the
# one the CED itself quotes at EK 2.6.A.1. All three tables are labelled
# hypothetical.
#
# NOTATION: the CED writes "2/3 vote." This module writes "two-thirds"
# everywhere, because mathfmt.convert would typeset the CED's own notation as a
# fraction on export. The verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.4", "Roles and Powers of the President", 2)

_VETO = ("In a hypothetical presidency, the table reports the use of the veto power across "
         "three periods of a single administration.")
_VETO_TABLE = dict(
    headers=["Period", "Regular vetoes", "Vetoes overridden", "Pocket vetoes"],
    rows=[["First two years", "4", "0", "1"],
          ["Middle two years", "17", "2", "6"],
          ["Final two years", "31", "9", "11"]])

_TOOLS = ("In a hypothetical study, the table reports how many times a president used each "
          "instrument in each of three years.")
_TOOLS_TABLE = dict(
    headers=["Instrument", "Year 1", "Year 2", "Year 3"],
    rows=[["Executive orders", "38", "44", "57"],
          ["Signing statements", "12", "19", "26"],
          ["Executive agreements", "165", "180", "203"],
          ["Treaties submitted to the Senate", "9", "7", "5"]])

_APPROVAL = ("In a hypothetical study, the table reports a president's public approval rating "
             "and the share of the president's legislative proposals enacted by Congress in "
             "the same year.")
_APPROVAL_TABLE = dict(
    headers=["Year", "Approval rating (%)", "Proposals enacted (%)"],
    rows=[["Year 1", "63", "58"],
          ["Year 2", "54", "47"],
          ["Year 3", "41", "31"],
          ["Year 4", "36", "22"]])

QUESTIONS = [
 dict(q="According to the course framework, a president pursues a policy agenda with support from",
   choices=[
     "the Vice-President, the Cabinet, and the Executive Office of the President",
     "the Senate majority leader and the Speaker of the House",
     "the Supreme Court and the federal judiciary",
     "the state governors and the National Governors Association",
     "the chairs of the standing committees of Congress"], ans=0,
   why="EK 2.4.A.1 names exactly these three sources of support. The other options name officials in other branches or levels of government, who are not part of the executive establishment."),

 dict(q="According to the course framework, the powers of the president",
   choices=[
     "include both formal and informal powers",
     "consist entirely of powers written into Article II",
     "consist entirely of powers delegated by Congress",
     "are exercised only with the prior consent of the Senate",
     "may not be exercised without a supporting act of Congress"], ans=0,
   why="EK 2.4.A.2 states that the powers include both formal and informal powers, and the whole topic turns on sorting particular instruments into those two categories."),

 dict(q="A president signs an agreement with another country's head of government that takes effect without a Senate vote. According to the course framework, this instrument is",
   choices=[
     "an executive agreement, an informal foreign policy power",
     "a treaty, a formal foreign policy power",
     "an executive order, a power implied by the vested executive power",
     "a signing statement, an informal power of interpretation",
     "a pocket veto, a formal power to check Congress"], ans=0,
   why="EK 2.4.A.2.ii lists executive agreements among the INFORMAL foreign policy powers, in contrast to treaties, which the same statement lists as formal. The absence of Senate ratification is what distinguishes the two."),

 dict(q="Which pairing of a presidential foreign policy power with its category is correct under the course framework?",
   choices=[
     "Commander in chief, formal; executive agreements, informal",
     "Commander in chief, informal; treaties, informal",
     "Treaties, informal; executive agreements, formal",
     "Executive agreements, formal; signing statements, formal",
     "Treaties, formal; commander in chief, informal"], ans=0,
   why="EK 2.4.A.2.ii sorts commander in chief and treaties as formal and executive agreements as informal. Each other option miscategorizes at least one of the three."),

 dict(q="According to the course framework, what is the relationship between a veto and an override?",
   choices=[
     "A regular veto can be overridden by a two-thirds vote, but a pocket veto cannot be overridden",
     "Both a regular veto and a pocket veto can be overridden by a two-thirds vote",
     "Neither a regular veto nor a pocket veto can be overridden",
     "A pocket veto can be overridden by a two-thirds vote, but a regular veto cannot",
     "An override requires a simple majority in both chambers"], ans=0,
   why="EK 2.4.A.2.i states both halves in one sentence: vetoes can be overridden with a two-thirds vote while pocket vetoes cannot. This is the point the framework is most explicit about."),

 dict(q="Congress passes a bill and then adjourns; the president neither signs nor returns it, and the bill does not become law. What has happened, and what can Congress do about it?",
   choices=[
     "A pocket veto has occurred, and Congress cannot override it",
     "A pocket veto has occurred, and Congress may override it by a two-thirds vote",
     "A regular veto has occurred, and Congress may override it by a two-thirds vote",
     "The bill has become law without a signature, and no further action is needed",
     "The bill returns automatically to committee for a new markup"], ans=0,
   why="EK 2.4.A.2.i says pocket vetoes cannot be overridden with a two-thirds vote, and the pocket veto arises precisely when Congress has adjourned so the bill cannot be returned."),

 dict(q="Why is the pocket veto a more absolute check than the regular veto?",
   choices=[
     "The regular veto returns the bill to Congress, which may act on it again; the pocket veto leaves Congress no vote to take",
     "The pocket veto requires the approval of the Supreme Court, which rarely grants it",
     "The regular veto may be used only on revenue bills",
     "The pocket veto may be overridden only by a unanimous vote of both chambers",
     "The regular veto expires after ten days while the pocket veto is permanent for that Congress and all future ones"], ans=0,
   why="EK 2.4.A.2.i's asymmetry follows from procedure: a returned bill can be voted on again, and a bill that dies on adjournment cannot. The fourth option contradicts the framework's flat statement that pocket vetoes cannot be overridden."),

 dict(q="Both the regular veto and the pocket veto are classified by the course framework as",
   choices=[
     "formal powers that enable the president to check Congress",
     "informal tools of persuasion rather than powers of the office",
     "powers delegated to the president by statute",
     "powers exercised jointly with the Senate",
     "powers of foreign policy rather than of domestic policy"], ans=0,
   why="EK 2.4.A.2.i calls vetoes and pocket vetoes formal powers that enable the president to check Congress. Their difference lies in whether an override is possible, not in their category, and neither is a matter of persuasion."),

 dict(q="According to the course framework, executive orders",
   choices=[
     "allow the president to manage the federal government and are implied by the vested executive power or delegated by Congress",
     "are enumerated in Article II and require no source beyond the text",
     "must be approved by a majority of both chambers before taking effect",
     "may be issued only during a declared national emergency",
     "are the president's principal tool for negotiating with foreign governments"], ans=0,
   why="EK 2.4.A.2.iv gives both the function and the two sources in exactly these terms. The framework does not describe executive orders as enumerated, which is why the second option misstates their basis."),

 dict(q="A president directs every executive agency to publish its rulemaking schedule on a common website. Which presidential power is being used?",
   choices=[
     "An executive order, which allows the president to manage the federal government",
     "A signing statement, which conveys the president's interpretation of a law",
     "An executive agreement, which commits the United States to an understanding with another nation",
     "A pocket veto, which prevents a bill from becoming law",
     "Bargaining and persuasion, an informal power to secure congressional action"], ans=0,
   why="EK 2.4.A.2.iv describes executive orders as the instrument for managing the federal government, and a directive to agencies about their own procedures is exactly that."),

 dict(q="According to the course framework, a signing statement is",
   choices=[
     "an informal power that informs Congress and the public of the president's interpretation of a law the president has signed",
     "a formal power that prevents a bill from taking effect",
     "a document by which the president negotiates an agreement with a foreign government",
     "a directive requiring an agency to take a specified action",
     "the president's formal request that Congress take up a particular bill"], ans=0,
   why="EK 2.4.A.2.v defines the signing statement as an informal power that informs Congress and the public of the president's interpretation of laws passed by Congress and signed by the president."),

 dict(q="What distinguishes a signing statement from a veto?",
   choices=[
     "A signing statement accompanies a bill the president has signed into law; a veto prevents the bill from becoming law at all",
     "A signing statement prevents the bill from becoming law; a veto accompanies a bill the president has signed",
     "Both prevent a bill from becoming law, but only one may be overridden",
     "Both accompany a signed bill, but only one is formal",
     "A signing statement may be issued only after Congress overrides a veto"], ans=0,
   why="EK 2.4.A.2.v attaches the signing statement to laws 'passed by Congress AND SIGNED by the president,' while EK 2.4.A.2.i makes the veto an instrument for blocking a bill. The two operate on opposite outcomes."),

 dict(q="A president invites wavering members of Congress to the White House, offers support for their local priorities, and secures their votes for a bill. According to the course framework, which power is being exercised?",
   choices=[
     "Bargaining and persuasion, informal powers that enable the president to secure congressional action",
     "The veto, a formal power to check Congress",
     "An executive order, which manages the federal government",
     "A signing statement, which conveys an interpretation of a law",
     "The treaty power, a formal foreign policy power"], ans=0,
   why="EK 2.4.A.2.iii names bargaining and persuasion as informal powers that enable the president to secure congressional action, and the scenario is that description exactly."),

 dict(q="Which list contains ONLY informal presidential powers as the course framework classifies them?",
   choices=[
     "Executive agreements, bargaining and persuasion, signing statements",
     "Vetoes, treaties, executive agreements",
     "Commander in chief, signing statements, bargaining",
     "Pocket vetoes, executive agreements, persuasion",
     "Treaties, signing statements, executive orders"], ans=0,
   why="EK 2.4.A.2 classifies executive agreements (ii), bargaining and persuasion (iii) and signing statements (v) as informal. Vetoes, pocket vetoes, treaties and commander in chief are all formal."),

 dict(q="Which list contains ONLY formal presidential powers as the course framework classifies them?",
   choices=[
     "The veto, the pocket veto, the treaty power, and the role of commander in chief",
     "The veto, the executive agreement, and bargaining",
     "The treaty power, the signing statement, and persuasion",
     "The pocket veto, the signing statement, and the executive agreement",
     "Commander in chief, persuasion, and the executive agreement"], ans=0,
   why="EK 2.4.A.2.i names vetoes and pocket vetoes as formal and EK 2.4.A.2.ii names commander in chief and treaties as formal. Every other option mixes in at least one informal instrument."),

 dict(q="A president cannot persuade Congress to pass a measure and instead directs an agency to pursue the same objective through its existing statutory authority. Which trade-off does this illustrate?",
   choices=[
     "The president gains action without congressional agreement but is limited to what existing authority allows and can be reversed by a successor",
     "The president gains permanent authority that no later president may alter",
     "The president acquires the power to enact a statute without Congress",
     "The president must obtain Senate confirmation before the agency may act",
     "The president converts an informal power into a formal one"], ans=0,
   why="EK 2.4.A.2.iv grounds executive orders in vested or delegated authority, which is what bounds them, and an instrument resting on the president's own authority is available to the next president to undo."),

 dict(q="Read the following excerpt.\n\n“Every Bill which shall have passed the House of Representatives and the Senate, shall, before it become a Law, be presented to the President of the United States; If he approve he shall sign it, but if not he shall return it, with his Objections to that House in which it shall have originated.”\n—U.S. Constitution, Article I, Section 7\n\nWhich presidential power does this passage establish?",
   choices=[
     "The veto, which the course framework classifies as a formal power to check Congress",
     "The executive order, which allows the president to manage the federal government",
     "The signing statement, which conveys the president's interpretation of a law",
     "The executive agreement, an informal foreign policy power",
     "Bargaining and persuasion, informal powers to secure congressional action"], ans=0,
   why="The clause describes presentment and return with objections, which is the veto, and EK 2.4.A.2.i classifies it as a formal power that enables the president to check Congress."),

 dict(q="Read the following excerpt.\n\n“The President shall be Commander in Chief of the Army and Navy of the United States... he shall have Power, by and with the Advice and Consent of the Senate, to make Treaties, provided two thirds of the Senators present concur.”\n—U.S. Constitution, Article II, Section 2\n\nWhich statement about these two powers is accurate under the course framework?",
   choices=[
     "Both are formal foreign policy powers, and the treaty power alone requires Senate concurrence",
     "Both are informal foreign policy powers requiring no Senate action",
     "Both require Senate concurrence before the president may act",
     "The commander in chief power requires Senate concurrence and the treaty power does not",
     "Neither is a foreign policy power under the course framework"], ans=0,
   why="EK 2.4.A.2.ii lists commander in chief and treaties as the formal foreign policy powers, and the text conditions only the treaty power on the Senate's advice and consent."),

 dict(q="Read the following excerpt.\n\n“It is rather for us to be here dedicated to the great task remaining before us... that government of the people, by the people, for the people, shall not perish from the earth.”\n—Abraham Lincoln, Gettysburg Address, 1863\n\nA president quotes this passage in a nationally televised address urging Congress to act on a proposal. Which presidential power is being exercised?",
   choices=[
     "Persuasion, an informal power used to build support for the president's agenda",
     "The veto, a formal power to check Congress",
     "An executive order, which manages the federal government",
     "A signing statement, which interprets a law already signed",
     "The treaty power, a formal foreign policy power"], ans=0,
   why="EK 2.4.A.2.iii names persuasion among the informal powers that enable the president to secure congressional action, and a public appeal for legislative action is that power in use rather than any formal instrument."),

 dict(q="A president issues the Emancipation Proclamation as a wartime measure resting on the powers of the commander in chief rather than on a statute. Which claim about presidential power does the episode best illustrate?",
   choices=[
     "A formal power granted for one purpose can become the basis for far-reaching policy action",
     "The president may enact a statute when Congress declines to do so",
     "Executive agreements require the consent of two thirds of the Senate",
     "A signing statement may repeal a law the president has signed",
     "The pocket veto may be used at any time, whether or not Congress has adjourned"], ans=0,
   why="EK 2.4.A.2.ii names commander in chief as a formal power, and the Proclamation rests on it, which shows how broadly a formal grant may be read. The other options assert rules the framework contradicts."),

 dict(q=_VETO + " Which pattern is best supported by the data?",
   table=_VETO_TABLE,
   choices=[
     "Both regular and pocket vetoes rose across the three periods, and overrides rose with them",
     "Regular vetoes rose while pocket vetoes fell across the three periods",
     "Overrides fell as regular vetoes rose",
     "Pocket vetoes exceeded regular vetoes in every period",
     "No veto of any kind was overridden in any period"], ans=0,
   why="Regular vetoes run 4, 17 and 31; pocket vetoes run 1, 6 and 11; overrides run 0, 2 and 9. Regular vetoes exceed pocket vetoes in every period, and nine overrides occurred in the final period alone."),

 dict(q=_VETO + " In which period was the largest share of regular vetoes overridden, and what was that share?",
   table=_VETO_TABLE,
   choices=[
     "The final two years, when nine of thirty-one regular vetoes were overridden, or about twenty-nine percent",
     "The first two years, when none of four regular vetoes was overridden",
     "The middle two years, when two of seventeen regular vetoes were overridden, or about twelve percent",
     "The final two years, when nine of forty-two vetoes of all kinds were overridden",
     "It cannot be determined, because the table does not report the number of overrides"], ans=0,
   why="The three override shares are zero, about twelve percent and about twenty-nine percent, so the final period is the largest. Pocket vetoes must be excluded from the denominator, because EK 2.4.A.2.i says they cannot be overridden at all."),

 dict(q=_VETO + " A student computes the override rate by dividing overrides by the sum of regular and pocket vetoes. Why is that calculation wrong?",
   table=_VETO_TABLE,
   choices=[
     "Pocket vetoes cannot be overridden, so including them in the denominator counts vetoes that were never eligible",
     "Pocket vetoes are overridden more often than regular vetoes, so the combined rate understates the total",
     "The table reports overrides of pocket vetoes in a separate column that must be added in",
     "Overrides apply only to pocket vetoes, so regular vetoes must be excluded instead",
     "The calculation is correct, since both kinds of veto are subject to the same override procedure"], ans=0,
   why="EK 2.4.A.2.i states that pocket vetoes cannot be overridden with a two-thirds vote, so no pocket veto belongs in the denominator of an override rate. This is the framework's most explicit factual claim about the veto."),

 dict(q=_TOOLS + " Which pattern is best supported by the data?",
   table=_TOOLS_TABLE,
   choices=[
     "Three instruments rose across the three years while treaties submitted to the Senate fell",
     "All four instruments rose across the three years",
     "Executive agreements were used less often than treaties in every year",
     "Signing statements were the most frequently used instrument in every year",
     "Executive orders fell while signing statements rose"], ans=0,
   why="Executive orders, signing statements and executive agreements all rise, while treaties submitted fall from nine to five. Executive agreements are the largest row in the table by a wide margin."),

 dict(q=_TOOLS + " Which claim about presidential power do these data most directly support?",
   table=_TOOLS_TABLE,
   choices=[
     "The president relied increasingly on instruments that do not require a Senate vote",
     "The president relied increasingly on instruments requiring Senate ratification",
     "The president used only formal powers during these three years",
     "The president used only informal powers during these three years",
     "The president's use of the veto increased across the three years"], ans=0,
   why="Executive orders, signing statements and executive agreements all proceed without a Senate vote and all rise, while treaties, which require the concurrence of two thirds of senators present, fall. The table reports no vetoes at all."),

 dict(q=_TOOLS + " A commentator concludes from these data that presidential power expanded during these three years. Which limitation of the data most undercuts that conclusion?",
   table=_TOOLS_TABLE,
   choices=[
     "Counting instruments says nothing about their significance, and one treaty may matter more than fifty routine orders",
     "The table omits executive orders, so no comparison is possible",
     "The table reports a single year, so no trend can be observed",
     "The table reports percentages that do not sum to one hundred",
     "The table gives no information about whether any instrument was used"], ans=0,
   why="A frequency count treats every use as equivalent, which is the standard limitation of a tally of unweighted actions. The table plainly reports four instruments across three years as counts."),

 dict(q=_APPROVAL + " Which pattern is best supported by the data?",
   table=_APPROVAL_TABLE,
   choices=[
     "Approval and the share of proposals enacted both fell in every year, and the two series moved together",
     "Approval fell while the share of proposals enacted rose",
     "Approval rose while the share of proposals enacted fell",
     "Approval remained above half in every year",
     "The share of proposals enacted exceeded the approval rating in every year"], ans=0,
   why="Approval runs 63, 54, 41 and 36 while enactment runs 58, 47, 31 and 22, both falling every year. Approval falls below half in the third year, and enactment is below approval in every year."),

 dict(q=_APPROVAL + " Which claim from the course framework do these data most directly bear on?",
   table=_APPROVAL_TABLE,
   choices=[
     "That bargaining and persuasion are informal powers enabling the president to secure congressional action",
     "That vetoes can be overridden while pocket vetoes cannot",
     "That executive orders are implied by the vested executive power or delegated by Congress",
     "That signing statements convey the president's interpretation of a law",
     "That treaties require the concurrence of two thirds of the senators present"], ans=0,
   why="EK 2.4.A.2.iii makes persuasion an informal power for securing congressional action, and a president's standing with the public is the resource that power draws on. The other four statements concern instruments the table does not report."),

 dict(q=_APPROVAL + " A student concludes that falling approval caused the decline in enactments. Which limitation of the data most undercuts that conclusion?",
   table=_APPROVAL_TABLE,
   choices=[
     "The two series move together, but the table reports nothing about which party controlled Congress or what the proposals were",
     "The table omits the approval rating, so no comparison is possible",
     "The table covers a single year, so no trend can be seen",
     "The two series move in opposite directions, which rules out any relationship",
     "The table reports counts rather than percentages, so no rate can be computed"], ans=0,
   why="Two series falling together are equally consistent with a common cause such as a change in party control, which EK 2.3.A.3 identifies as affecting support for presidential initiatives. The table plainly reports four years of both series as percentages."),

 dict(q="A president's party loses control of both chambers at the midterm election. Which change in the president's use of power would the course framework lead you to expect?",
   choices=[
     "Greater reliance on executive orders and other instruments that do not require congressional agreement",
     "Greater reliance on treaties, since the Senate becomes more cooperative",
     "Abandonment of the veto, since Congress can override it by a simple majority",
     "Greater reliance on signing statements to prevent bills from becoming law",
     "Loss of the power to issue executive orders until control is regained"], ans=0,
   why="EK 2.5.A.3 says policy conflicts with the congressional agenda can lead the president to use executive orders and directives to the bureaucracy, and EK 2.4.A.2.iv grounds those orders in the president's own authority. A signing statement accompanies a bill the president has signed and cannot block one."),
]
