# AP U.S. GOVERNMENT AND POLITICS 1.6 Principles of American Government -- 30 questions
# CED V.1 (c) 2026, Unit 1 Foundations of American Democracy.
# TWO learning objectives, which is unusual for a Unit 1 topic and is the reason
# this module is split the way it is:
#   LO 1.6.A -- explain the constitutional principles of separation of powers
#     and checks and balances.
#   LO 1.6.B -- explain the EFFECTS of separation of powers and checks and
#     balances for the U.S. political system.
#
# Essential knowledge relied on:
#   EK 1.6.A.1 -- "The specific and separate powers delegated to Congress, the
#     president, and the courts allow each branch to check and balance the power
#     of the other branches, ensuring no one branch becomes too powerful."
#   EK 1.6.A.2 -- "Federalist No. 51 explains how constitutional provisions of
#     separation of powers and checks and balances control potential abuses by
#     majorities."
#   EK 1.6.B.1 -- "Separation of powers and checks and balances creates multiple
#     access points for stakeholders and institutions to influence public
#     policy."
#   EK 1.6.B.2 -- legal actions against officials who abuse power: IMPEACHMENT,
#     in which "the House formally charges an official with abuse of power or
#     misconduct," and REMOVAL, "if the official is convicted in a Senate
#     impeachment trial."
#
# THE DISTINCTION THIS MODULE INSISTS ON, because students collapse it every
# year and the CED keeps it separate across two objectives: SEPARATION OF POWERS
# is the assignment of distinct powers to distinct branches; CHECKS AND BALANCES
# is one branch's power over ANOTHER branch's exercise of its own power. The
# veto is a check, not a separation; the fact that only Congress may legislate
# is a separation, not a check. Items 3 to 8 turn on exactly that line.
#
# AND THE ONE STUDENTS GET WRONG ON THE EXAM: impeachment is a CHARGE, not a
# removal. EK 1.6.B.2 is explicit -- the House charges, and removal follows only
# on conviction in a Senate trial. Items 17 to 20 are built on that sentence,
# and no item in this module says an official was "impeached and removed" as
# though the words were one act.
#
# Documents the CED attaches to 1.6.A (p. 26-27): Federalist No. 51,
# Federalist No. 70. 1.6.B: Federalist No. 51.
# Required cases the CED attaches to 1.6.A (p. 31-32): Marbury v. Madison,
# Engel v. Vitale, Gideon v. Wainwright, Wisconsin v. Yoder. To 1.6.B:
# Marbury v. Madison, Baker v. Carr.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: Federalist No. 51 and No. 70 are quoted
# verbatim; constitutional text is quoted verbatim. The impeachment table in
# items 24 to 26 is a labelled HYPOTHETICAL, because a running count of real
# federal impeachments would date the module and could not be verified here.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("1.6", "Principles of American Government", 1)

_CHECKS = ("The table lists five constitutional checks and identifies, for each, the branch "
           "that exercises it and the branch whose action it restrains.")
_CHECKS_TABLE = dict(
    headers=["Check", "Branch that exercises it", "Branch it restrains"],
    rows=[["Veto of a bill", "Executive", "Legislative"],
          ["Override of a veto", "Legislative", "Executive"],
          ["Confirmation of an appointment", "Legislative", "Executive"],
          ["Declaring an act unconstitutional", "Judicial", "Legislative"],
          ["Appointment of federal judges", "Executive", "Judicial"]])

_IMPEACH = ("In a hypothetical national legislature that follows the U.S. impeachment "
            "procedure, the table reports the outcome of every proceeding brought against "
            "a federal official over one decade.")
_IMPEACH_TABLE = dict(
    headers=["Type of official", "Charged by the lower chamber", "Convicted by the upper chamber"],
    rows=[["Chief executive", "2", "0"],
          ["Cabinet secretary", "3", "1"],
          ["Federal judge", "7", "5"],
          ["Independent agency head", "1", "0"]])

QUESTIONS = [
 dict(q="According to the course framework, the specific and separate powers delegated to Congress, the president and the courts allow each branch to",
   choices=[
     "check and balance the power of the other branches, ensuring no one branch becomes too powerful",
     "exercise the powers of the other branches whenever necessary",
     "operate independently, with no authority over the actions of the others",
     "delegate its own powers to the branch best suited to exercise them",
     "overrule the decisions of the state governments within its own sphere"], ans=0,
   why="EK 1.6.A.1 states this in exactly these words. The third option describes separation of powers alone, without the checks that the same sentence says the separate powers make possible."),

 dict(q="Which of the following is an example of SEPARATION of powers rather than of checks and balances?",
   choices=[
     "Only Congress may enact a statute; neither the president nor the courts may do so",
     "The president may veto a bill passed by both houses of Congress",
     "The Senate must confirm the president's nominees to the federal courts",
     "Congress may override a veto by a two-thirds vote in both chambers",
     "The Supreme Court may declare an act of Congress unconstitutional"], ans=0,
   why="Separation of powers assigns a distinct function to a distinct branch; a check is one branch's authority over another branch's exercise of its own power. Vetoes, confirmations, overrides and judicial review are all the second kind."),

 dict(q="Which of the following is an example of a CHECK on one branch by another rather than of separation of powers?",
   choices=[
     "The Senate may refuse to confirm a presidential nominee",
     "Federal judges decide cases and controversies arising under federal law",
     "Congress has the power to lay and collect taxes",
     "The president is commander in chief of the armed forces",
     "Each house of Congress determines the rules of its own proceedings"], ans=0,
   why="Refusing confirmation is one branch acting on another branch's decision, which is the defining shape of a check. The other four describe powers each branch exercises within its own sphere, which is separation."),

 dict(q="A president signs a bill into law, an agency writes rules to carry it out, and a federal court later holds that one of those rules exceeds what the statute authorized. Which combination of principles does this sequence illustrate?",
   choices=[
     "Separation of powers, because three distinct institutions perform distinct functions, and checks and balances, because the court restrains the agency",
     "Federalism alone, because the national government acted at every stage",
     "Checks and balances alone, because no branch acted within its own sphere",
     "Popular sovereignty alone, because the president had been elected",
     "Separation of powers alone, because no institution restrained another"], ans=0,
   why="Both principles appear because the sequence contains both shapes: distinct functions performed by distinct institutions, and a judicial ruling that restrains an executive action. The fifth option ignores the judicial holding at the end."),

 dict(q="Read the following excerpt.\n\n“The great security against a gradual concentration of the several powers in the same department, consists in giving to those who administer each department the necessary constitutional means and personal motives to resist encroachments of the others.”\n—James Madison, Federalist No. 51, 1788\n\nMadison's design depends on which assumption about officeholders?",
   choices=[
     "That they will defend the powers of their own office out of self-interest, whatever their personal virtue",
     "That they will subordinate their own interests to the public good once in office",
     "That they will be selected for their unusual honesty and restraint",
     "That they will rarely disagree with officeholders in the other branches",
     "That they will be removable at will by the branch they most often oppose"], ans=0,
   why="The sentence pairs constitutional means with personal motives, which is a design that works because officeholders are ambitious rather than despite it. Assuming public-spiritedness is precisely the assumption Madison declines to make."),

 dict(q="Read the following excerpt.\n\n“In republican government, the legislative authority necessarily predominates. The remedy for this inconveniency is to divide the legislature into different branches; and to render them, by different modes of election and different principles of action, as little connected with each other as the nature of their common functions and their common dependence on the society will admit.”\n—James Madison, Federalist No. 51, 1788\n\nWhich feature of the Constitution follows most directly from this reasoning?",
   choices=[
     "A bicameral Congress whose chambers are elected differently and for different terms",
     "A president chosen by electors rather than by Congress",
     "Federal judges who hold office during good behavior",
     "The reservation of unenumerated powers to the states",
     "A single national capital in which all three branches sit"], ans=0,
   why="Madison identifies the legislature as the branch most likely to predominate and prescribes dividing it, which is bicameralism with different modes of election and different terms. The other options address the executive, the judiciary and federalism rather than the legislature's internal division."),

 dict(q="Read the following excerpt.\n\n“It is of great importance in a republic not only to guard the society against the oppression of its rulers, but to guard one part of the society against the injustice of the other part.”\n—James Madison, Federalist No. 51, 1788\n\nThis sentence identifies which danger in addition to the danger of overreaching officials?",
   choices=[
     "The danger that a majority of citizens will act unjustly toward a minority",
     "The danger that foreign powers will interfere in domestic elections",
     "The danger that the states will refuse to enforce national law",
     "The danger that officeholders will refuse to leave office after an election",
     "The danger that the judiciary will decide cases too slowly"], ans=0,
   why="EK 1.6.A.2 states that Federalist No. 51 explains how separation of powers and checks and balances control potential abuses BY MAJORITIES, and this sentence is where Madison names that second danger."),

 dict(q="Read the following excerpt.\n\n“Energy in the executive is a leading character in the definition of good government. It is essential to the protection of the community against foreign attacks; it is not less essential to the steady administration of the laws.”\n—Alexander Hamilton, Federalist No. 70, 1788\n\nHamilton's argument is best understood as a claim that",
   choices=[
     "a government divided into branches still requires an executive capable of acting decisively",
     "the executive should be free of any check by the legislature or the courts",
     "executive power should be shared among several officials of equal rank",
     "the executive should be chosen directly by the people to guarantee its energy",
     "the legislature rather than the executive should administer the laws"], ans=0,
   why="Federalist No. 70 argues for a single, energetic executive as a component of good government, not for an unchecked one; Hamilton's own argument against a plural executive is why the third option is the position he rejects."),

 dict(q="A senator argues that a proposed statute giving an executive agency final authority to decide disputes about its own regulations, with no review by any court, would violate a constitutional principle. Which principle is the senator invoking?",
   choices=[
     "Checks and balances, because it would leave one branch's exercise of power unreviewable by another",
     "Federalism, because the agency operates at the national level",
     "Popular sovereignty, because agency heads are not elected",
     "Republicanism, because the people act through representatives",
     "Limited government, because agencies should not exist at all"], ans=0,
   why="The objection is to the ABSENCE of review by another branch, which is the defining feature of a check. That agency heads are unelected is a separate observation and does not turn on which branch may review the decision."),

 dict(q="In Marbury v. Madison (1803), the Supreme Court established the principle of judicial review, empowering the Court to declare an act of the legislative or executive branch unconstitutional. This holding is best described as",
   choices=[
     "the Court's most important check on the other two branches",
     "an example of separation of powers with no element of a check",
     "a limitation on the Court's own authority over the other branches",
     "a grant of power to Congress to review the constitutionality of its own acts",
     "a rule that applies only to the actions of state governments"], ans=0,
   why="The CED states the Marbury holding as empowering the Court to declare an act of the legislative or executive branch unconstitutional, which is by definition one branch acting on another's exercise of power. The third option reverses the direction of the holding."),

 dict(q="A non-required case: a federal court holds that an executive order directing an agency to spend funds Congress never appropriated is invalid. Which required case supplies the principle the court is applying?",
   choices=[
     "Marbury v. Madison (1803), which established that courts may declare an act of the legislative or executive branch unconstitutional",
     "Baker v. Carr (1962), which held that redistricting does not raise political questions",
     "Engel v. Vitale (1962), which held that school sponsorship of religious activities violates the Establishment Clause",
     "Gideon v. Wainwright (1963), which extended the right to an attorney to felony defendants in state courts",
     "Wisconsin v. Yoder (1972), which held that compelling Amish students to attend school past the eighth grade violates the Free Exercise Clause"], ans=0,
   why="A court invalidating an executive action is exercising judicial review, which the CED attributes to Marbury. The other four holdings concern districting, religion in schools, counsel for the accused and compulsory schooling."),

 dict(q="In Engel v. Vitale (1962), the Supreme Court held that school sponsorship of religious activities violates the Establishment Clause of the First Amendment. A student cites the case as an illustration of checks and balances. Which reasoning best supports that use?",
   choices=[
     "A court set aside a policy adopted by elected officials, which is one branch restraining another's exercise of power",
     "A court adopted a new school policy of its own, which is one branch performing another's function",
     "Congress overrode a decision of the Supreme Court, which is a legislative check on the judiciary",
     "The president refused to enforce the decision, which is an executive check on the judiciary",
     "The states amended the Constitution in response, which is a check by the state governments"], ans=0,
   why="The check is the judicial invalidation of a policy made elsewhere. The second option misdescribes the holding, since a court striking a policy down does not thereby write one, and the last three describe events that did not occur in this case."),

 dict(q="Which of the following best explains why the framers gave the Senate a role in appointments and treaties rather than leaving both entirely to the president?",
   choices=[
     "To subject the executive's most consequential decisions to review by a body it does not control",
     "To make the Senate the branch that selects nominees for federal office",
     "To ensure that the president could not be removed from office by the courts",
     "To transfer the conduct of foreign relations from the executive to the legislature",
     "To give the states a direct vote on every executive decision"], ans=0,
   why="Advice and consent is a check: the president decides and another branch reviews. It does not make the Senate the nominating body or the conductor of foreign relations, which is what the second and fourth options claim."),

 dict(q="A president announces that an agency will stop enforcing a statute the president considers unwise. Which check is most directly available to Congress in response?",
   choices=[
     "Withholding or conditioning the appropriations the agency needs to operate",
     "Declaring the president's decision unconstitutional by a majority vote",
     "Ordering the Supreme Court to hear the case immediately",
     "Removing the president from office by a vote of the House alone",
     "Appointing a new head of the agency without the president's involvement"], ans=0,
   why="The power of the purse is Congress's most direct instrument against an executive that will not act, and it operates through the ordinary legislative process. Removal requires conviction in a Senate trial after a House charge, per EK 1.6.B.2, not a House vote alone."),

 dict(q="According to the course framework, one effect of separation of powers and checks and balances is that they",
   choices=[
     "create multiple access points for stakeholders and institutions to influence public policy",
     "guarantee that policy will be made quickly once a majority has formed",
     "prevent interest groups from participating in the policymaking process",
     "concentrate influence over policy in the branch with the most direct electoral mandate",
     "eliminate disagreement between the branches over the meaning of a statute"], ans=0,
   why="EK 1.6.B.1 states this effect in exactly these words. Multiplying the institutions that must agree multiplies the places where an outside actor can press its case, which is the opposite of the third option."),

 dict(q="An advocacy organization fails to persuade the House to include its provision in a bill, then persuades several senators to add it in committee, and later urges an agency to interpret the provision broadly in its rules. This sequence best illustrates which effect of the constitutional structure?",
   choices=[
     "That dividing authority creates multiple access points at which an outside interest may try again",
     "That the House and Senate are constitutionally required to consult outside organizations",
     "That interest groups exercise formal constitutional powers of their own",
     "That an organization defeated in one chamber may not raise the same proposal elsewhere",
     "That agencies are prohibited from interpreting statutes they administer"], ans=0,
   why="EK 1.6.B.1 names the multiple access points that the division of authority creates, and this is a group using three of them in turn. Nothing in the sequence gives the organization a constitutional power or requires anyone to listen to it."),

 dict(q="According to the course framework, impeachment is the process by which",
   choices=[
     "the House formally charges an official with abuse of power or misconduct",
     "the Senate convicts an official and removes that official from office",
     "the Supreme Court declares an official's actions unconstitutional",
     "the president dismisses an appointed official for misconduct",
     "the voters recall an elected official before the end of a term"], ans=0,
   why="EK 1.6.B.2 defines impeachment as the House formally charging an official, and defines removal separately as conviction in a Senate impeachment trial. Collapsing the two is the most common error on this topic."),

 dict(q="An official is impeached by the House and the Senate then votes to acquit. What is the official's status?",
   choices=[
     "The official remains in office, because removal requires conviction in the Senate trial",
     "The official is removed from office, because impeachment by the House is itself a removal",
     "The official is suspended until the next general election",
     "The official must be tried again by the House before the matter is closed",
     "The official is removed unless the president objects"], ans=0,
   why="EK 1.6.B.2 makes removal conditional on conviction in a Senate impeachment trial, so an acquittal leaves the charge without effect on tenure. The second option is the impeached-equals-removed error."),

 dict(q="Which statement about impeachment and removal is accurate under the constitutional design the course framework describes?",
   choices=[
     "The two chambers of Congress perform different roles, one charging and the other trying",
     "Both chambers must vote to charge, and the courts then conduct the trial",
     "The Supreme Court presides over every impeachment and casts the deciding vote",
     "The president may pardon an official after a conviction in an impeachment trial",
     "An official may be charged only after a criminal conviction in an ordinary court"], ans=0,
   why="EK 1.6.B.2 assigns the charge to the House and the trial to the Senate, which is itself an internal division of a single check. Impeachment is a political process and does not require a prior criminal conviction."),

 dict(q="Why is impeachment best understood as an application of checks and balances rather than of separation of powers?",
   choices=[
     "It gives one branch authority over whether officials of another branch remain in office",
     "It assigns the legislative function exclusively to Congress",
     "It divides Congress into two chambers with different terms",
     "It reserves to the states the powers not delegated to the national government",
     "It allows each branch to determine the rules of its own proceedings"], ans=0,
   why="A check is one branch acting on another, and impeachment reaches executive and judicial officers rather than Congress's own members' offices. The other options describe separation, bicameralism, federalism and internal self-governance."),

 dict(q=_CHECKS + " Which conclusion is best supported by the table?",
   table=_CHECKS_TABLE,
   choices=[
     "Every branch appears in the table both as a branch that exercises a check and as a branch that is restrained by one",
     "The executive branch appears only as a branch that is restrained",
     "The judicial branch exercises more of the listed checks than either other branch",
     "No listed check runs from the legislative branch to the executive",
     "Each listed check is exercised by a different branch from every other"], ans=0,
   why="Reading the two branch columns, each of the three branches appears at least once in each, which is what makes the arrangement mutual rather than a hierarchy. The legislature restrains the executive twice, through the override and through confirmation."),

 dict(q=_CHECKS + " A student says the table proves the three branches are exactly equal in power. What is the most important limitation of that inference?",
   table=_CHECKS_TABLE,
   choices=[
     "Counting checks says nothing about how often each is used or how much each one accomplishes",
     "The table omits the judicial branch entirely, so no comparison is possible",
     "The table reports opinions about the branches rather than constitutional provisions",
     "The table lists every check the Constitution contains, so nothing further can be said",
     "The table gives numerical scores that cannot be compared across branches"], ans=0,
   why="A list of five checks is a catalogue of formal authority, and formal authority is not the same as effective power; a check rarely used constrains less than one used constantly. The table plainly does include the judiciary and contains no numbers."),

 dict(q=_CHECKS + " Which check listed in the table restrains the branch that is otherwise least accountable to the voters?",
   table=_CHECKS_TABLE,
   choices=[
     "Appointment of federal judges, which restrains the judicial branch",
     "Veto of a bill, which restrains the legislative branch",
     "Override of a veto, which restrains the executive branch",
     "Confirmation of an appointment, which restrains the executive branch",
     "Declaring an act unconstitutional, which restrains the legislative branch"], ans=0,
   why="Federal judges are appointed rather than elected and hold office during good behavior, so the judiciary is the branch furthest from the electorate, and the appointment row is the only listed check that runs to it."),

 dict(q=_IMPEACH + " Which conclusion is best supported by the data?",
   table=_IMPEACH_TABLE,
   choices=[
     "Federal judges account for both the most charges and the most convictions of any category",
     "Every official charged was also convicted",
     "No category shows a conviction",
     "Chief executives were convicted more often than cabinet secretaries",
     "The number of convictions equals the number of charges in every category"], ans=0,
   why="The judge row carries 7 charges and 5 convictions, each the largest figure in its column. Thirteen officials were charged and six convicted, so charges and convictions are equal in no category."),

 dict(q=_IMPEACH + " Which conclusion about the constitutional design is best supported by the pattern in the data?",
   table=_IMPEACH_TABLE,
   choices=[
     "Charging an official is a lower bar than removing one, since fewer than half of those charged were convicted",
     "Charging and removing an official are effectively the same act",
     "The upper chamber convicts whenever the lower chamber charges",
     "Only the chief executive can be charged under this procedure",
     "Conviction requires no vote of the upper chamber at all"], ans=0,
   why="Six convictions out of thirteen charges is under half, which is the arithmetic form of EK 1.6.B.2's two-stage design: the House charges and removal follows only on conviction in a Senate trial."),

 dict(q=_IMPEACH + " A commentator concludes from the data that the removal power is ineffective. Which limitation of the data most undercuts that conclusion?",
   table=_IMPEACH_TABLE,
   choices=[
     "The table counts only proceedings that were brought, and cannot show officials who resigned or changed course under the threat of one",
     "The table omits the upper chamber, so no conviction can be counted",
     "The table covers a single year and so is too short to interpret",
     "The table reports percentages that do not sum to one hundred",
     "The table includes officials of only one type, so no comparison is possible"], ans=0,
   why="A count of completed proceedings misses the deterrent effect entirely, which is the standard limitation of any table of enforcement actions. The table plainly covers a decade, four types of official and two chambers, and contains no percentages."),

 dict(q="A commentator argues that checks and balances make the American system inefficient and that efficiency should be the primary goal of institutional design. Which response draws most directly on Federalist No. 51?",
   choices=[
     "The design accepts delay as the price of preventing any single interest, majority or officeholder from acting without restraint",
     "The design was intended to produce faster decisions than a parliamentary system",
     "Efficiency was the framers' primary goal, and any delay is a defect in execution",
     "The framers expected the branches to cooperate rather than to check one another",
     "The framers gave the executive the power to act without legislative approval"], ans=0,
   why="EK 1.6.A.2 states that Federalist No. 51 explains how these provisions control potential abuses by majorities, so obstruction is the mechanism rather than a side effect. Madison's design assumes conflict between the branches, not cooperation."),

 dict(q="In Baker v. Carr (1962), the Supreme Court held that redistricting did not raise political questions, allowing federal courts to hear cases challenging redistricting plans. Which effect of the separation of powers does the decision best illustrate?",
   choices=[
     "It opened an additional access point, allowing a claim that had failed in the legislature to be pressed in court",
     "It transferred the drawing of district lines from the states to Congress",
     "It removed the courts from any role in disputes about representation",
     "It required that every districting plan be approved by the president",
     "It established that federal courts may decide only questions Congress refers to them"], ans=0,
   why="EK 1.6.B.1 names the multiple access points the structure creates, and a holding that a class of claim is justiciable adds one. The CED's statement of the holding concerns whether courts may hear such cases, not who draws the lines."),

 dict(q="Which scenario best illustrates EK 1.6.B.1's claim that the structure creates multiple access points, rather than illustrating checks and balances between the branches?",
   choices=[
     "A coalition of state governments, an industry association and a public interest group each press the same policy on Congress, the relevant agency and the courts in turn",
     "The president vetoes a bill and Congress fails to override the veto",
     "The Senate rejects a nominee to a federal court",
     "The Supreme Court holds a federal statute unconstitutional",
     "The House charges an official and the Senate acquits"], ans=0,
   why="Access points are about OUTSIDE actors finding places to press a claim, which is EK 1.6.B.1; the other four are institutions restraining one another, which is EK 1.6.A.1. Keeping the two objectives distinct is the point of the item."),

 dict(q="Which question would best test whether the checks and balances described in the course framework are operating as intended in a given period?",
   choices=[
     "Are the branches in fact using their formal powers against one another, or has one branch's actions gone unreviewed?",
     "Are the three branches located in the same city?",
     "Does the Constitution list more powers for one branch than for another?",
     "Have the branches avoided all public disagreement?",
     "Does each branch employ approximately the same number of officials?"], ans=0,
   why="EK 1.6.A.1 ties the design to the result that no one branch becomes too powerful, so the test is whether the checks are actually exercised. An absence of public disagreement would be evidence against the design working, not for it."),
]
