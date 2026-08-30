# AP COMPARATIVE GOVERNMENT AND POLITICS 2.4 Executive Term Limits
# CED effective Fall 2026, Unit 2 Political Institutions. Enduring understanding
# PAU-3; learning objective PAU-3.C. Suggested skill 5.A, Argumentation
# (articulate a defensible claim/thesis) -- which is why several items here ask
# which evidence would SUPPORT or WEAKEN a claim rather than what the framework
# says.
#
# Essential knowledge relied on:
#   PAU-3.C.3  executive term limits have ADVANTAGES AND DISADVANTAGES with regard
#              to promoting STABILITY and EFFECTIVE POLICIES in a country
#     .a ADVANTAGES: they check executive power and inhibit the emergence of
#        dictators and personality rule; help focus the officeholder on GOVERNING
#        RATHER THAN WINNING ELECTIONS; and provide opportunities for NEW LEADERS
#        with new ideas, policies or goals
#     .b DISADVANTAGES: they force good executives to leave office; allow
#        INSUFFICIENT TIME for an officeholder to achieve goals; IMPEDE POLICY
#        CONTINUITY; WEAKEN ACCOUNTABILITY; create a LAME-DUCK PERIOD; PREVENT THE
#        OFFICEHOLDER FROM BUILDING EXPERIENCE as chief executive; and can cause
#        POORLY DESIGNED POLICY
#
# The two term-limit facts the framework actually prints:
#   PAU-3.C.2b Iran's president is elected for UP TO TWO 4-YEAR TERMS
#   PAU-3.C.2c Mexico's president is RESTRICTED TO ONE TERM
# No figure is given for China, Nigeria, Russia or the United Kingdom. China's
# 2018 removal of presidential term limits appears ONLY in an optional sample
# instructional activity, not in any essential knowledge statement, so no item
# keys it; item 17 keys that fact about the framework instead
# (AP_COMP_GOV_CED.md note 7).
#
# 'Weaken accountability' is listed without explanation, so item 26 glosses it
# only as far as EK DEM-2.B.2 licenses -- accountability there rests on voters
# knowing whose record is on the ballot at the next election.
#
# Table figures are HYPOTHETICAL and labelled so, and the groups are lettered by
# rule rather than named, since the framework attaches no such data to any country.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("2.4", "Executive Term Limits", 2)

_T_TL = dict(
    headers=["Group of cases (hypothetical), by term-limit rule",
             "Mean years the chief executive held office",
             "Share of executives who left office at a scheduled date (percent)",
             "Major reversals of existing policy per decade"],
    rows=[["Cases with a two-term limit", "7.2", "94", "3.1"],
          ["Cases with a one-term limit", "5.0", "97", "4.4"],
          ["Cases with no term limit", "14.6", "61", "1.8"]])

_T_LAME = dict(
    headers=["Year of a chief executive's single permitted term (hypothetical)",
             "Executive-proposed bills passed", "Executive-proposed bills defeated"],
    rows=[["Year 1", "22", "3"],
          ["Year 2", "19", "5"],
          ["Year 3", "14", "9"],
          ["Year 4", "6", "17"]])

QUESTIONS = [
 dict(q="What does the framework say about executive term limits overall?",
   choices=[
     "they have advantages and disadvantages with regard to promoting stability and effective policies",
     "they promote stability and effective policies with no offsetting costs",
     "they damage stability and effective policies with no offsetting benefits",
     "they have no bearing on stability or on the effectiveness of policy",
     "they exist only in presidential systems"], ans=0,
   why="EK PAU-3.C.3 states that executive term limits have advantages and disadvantages with regard to promoting stability and effective policies in a country, and then lists three of the first and seven of the second. A one-sided reading contradicts the statement in either direction."),
 dict(q="Which of the following does the framework list among the ADVANTAGES of executive term limits?",
   choices=[
     "they check executive power and inhibit the emergence of dictators and personality rule",
     "they force good executives to leave office",
     "they create a lame-duck period for the officeholder",
     "they impede policy continuity",
     "they weaken accountability"], ans=0,
   why="EK PAU-3.C.3.a lists checking executive power and inhibiting the emergence of dictators and personality rule among the advantages. Every rejected option is drawn from EK PAU-3.C.3.b, the disadvantages half of the same statement."),
 dict(q="The framework says term limits help focus an officeholder on",
   choices=[
     "governing rather than winning elections",
     "winning elections rather than governing",
     "building a personal following within the governing party",
     "negotiating with foreign governments rather than with the legislature",
     "expanding the powers of the office before leaving it"], ans=0,
   why="EK PAU-3.C.3.a states that term limits help to focus the officeholder on governing rather than winning elections. An executive who cannot stand again has no re-election campaign to conduct, which is the framework's reason for listing this as an advantage."),
 dict(q="Which advantage of term limits does the framework describe in terms of who comes next?",
   choices=[
     "they provide opportunities for new leaders with new ideas, policies or goals",
     "they guarantee that the next officeholder will come from the same party",
     "they allow the outgoing officeholder to choose a successor",
     "they ensure that the next officeholder will have served in the cabinet",
     "they require the legislature to elect the successor"], ans=0,
   why="EK PAU-3.C.3.a lists providing opportunities for new leaders with new ideas, policies or goals among the advantages of executive term limits. The framework says nothing about the successor's party, prior office, or method of selection under this heading."),
 dict(q="Which of the following does the framework list among the DISADVANTAGES of executive term limits?",
   choices=[
     "they force good executives to leave office",
     "they check executive power",
     "they inhibit the emergence of personality rule",
     "they help focus the officeholder on governing rather than winning elections",
     "they provide opportunities for new leaders with new ideas"], ans=0,
   why="EK PAU-3.C.3.b lists forcing good executives to leave office among the disadvantages. Every rejected option is drawn from EK PAU-3.C.3.a, the advantages half of the same statement."),
 dict(q="The framework's disadvantage concerning the time available to an officeholder is that term limits",
   choices=[
     "allow insufficient time for an officeholder to achieve goals",
     "allow so much time that officeholders lose urgency",
     "shorten the legislative session",
     "delay the date of the next election",
     "prevent an officeholder from taking office promptly"], ans=0,
   why="EK PAU-3.C.3.b lists allowing insufficient time for an officeholder to achieve goals among the disadvantages of term limits. The complaint is about the length of the tenure available, not about the parliamentary or electoral calendar."),
 dict(q="Which disadvantage does the framework state in terms of what happens to policy across administrations?",
   choices=[
     "term limits impede policy continuity",
     "term limits require every policy to be renewed annually",
     "term limits transfer policy making to the legislature",
     "term limits prevent the executive from proposing legislation",
     "term limits oblige each administration to keep its predecessor's policies"], ans=0,
   why="EK PAU-3.C.3.b lists impeding policy continuity among the disadvantages of term limits. A guaranteed change of officeholder means a guaranteed opportunity for a change of direction, which is the same fact EK PAU-3.C.3.a counts as an advantage when it speaks of new leaders with new ideas."),
 dict(q="Which of the framework's listed disadvantages concerns the relationship between the officeholder and the voters?",
   choices=[
     "term limits weaken accountability",
     "term limits reduce voter turnout to zero",
     "term limits transfer the conduct of elections to the courts",
     "term limits require voters to approve each policy separately",
     "term limits prevent voters from electing a legislature"], ans=0,
   why="EK PAU-3.C.3.b lists weakening accountability among the disadvantages of executive term limits, and EK DEM-2.B.2 grounds accountability in voters knowing whose record is on the ballot at the next election. An officeholder who cannot stand again is not on that ballot."),
 dict(q="The framework says term limits create a lame-duck period for the officeholder. Which situation best illustrates that disadvantage?",
   choices=[
     "In the final part of a term-limited executive's tenure, other actors discount the executive's demands because a successor is already certain",
     "An executive resigns after losing a confidence vote",
     "An executive is impeached by the legislature",
     "An executive calls an early election to strengthen a majority",
     "An executive appoints a new cabinet after a reshuffle"], ans=0,
   why="EK PAU-3.C.3.b lists creating a lame-duck period for the officeholder among the disadvantages of term limits. The period arises precisely because the executive's departure is scheduled rather than contingent, which the rejected options are not."),
 dict(q="Which disadvantage does the framework state in terms of what the officeholder is unable to accumulate?",
   choices=[
     "term limits prevent the officeholder from building experience as chief executive",
     "term limits prevent the officeholder from appointing a cabinet",
     "term limits prevent the officeholder from meeting foreign leaders",
     "term limits prevent the officeholder from proposing a budget",
     "term limits prevent the officeholder from addressing the legislature"], ans=0,
   why="EK PAU-3.C.3.b lists preventing the officeholder from building experience as chief executive among the disadvantages of term limits. The framework attaches no restriction on appointments, diplomacy, budgets or addresses to a term limit."),
 dict(q="Which further disadvantage of term limits does the framework name?",
   choices=[
     "they can cause poorly designed policy",
     "they can cause the legislature to be dissolved",
     "they can cause the judiciary to lose its independence",
     "they can cause a state to lose its international recognition",
     "they can cause a regime to become federal"], ans=0,
   why="EK PAU-3.C.3.b lists causing poorly designed policy among the disadvantages of term limits, alongside insufficient time to achieve goals and the loss of accumulated experience. The rejected options concern institutions the framework never connects to term limits."),
 dict(q="A list contains: checking executive power; forcing good executives from office; inhibiting personality rule; and impeding policy continuity. Which pair does the framework count as ADVANTAGES?",
   choices=[
     "checking executive power and inhibiting personality rule",
     "forcing good executives from office and impeding policy continuity",
     "checking executive power and impeding policy continuity",
     "inhibiting personality rule and forcing good executives from office",
     "none of the four, since the framework lists no advantages"], ans=0,
   why="EK PAU-3.C.3.a lists checking executive power and inhibiting the emergence of dictators and personality rule among the advantages, while EK PAU-3.C.3.b lists forcing good executives to leave office and impeding policy continuity among the disadvantages. The four items come two from each half of the statement."),
 dict(q="A second list contains: providing opportunities for new leaders; creating a lame-duck period; weakening accountability; and focusing the officeholder on governing rather than winning elections. Which pair does the framework count as DISADVANTAGES?",
   choices=[
     "creating a lame-duck period and weakening accountability",
     "providing opportunities for new leaders and focusing the officeholder on governing",
     "creating a lame-duck period and providing opportunities for new leaders",
     "weakening accountability and focusing the officeholder on governing",
     "none of the four, since the framework lists no disadvantages"], ans=0,
   why="EK PAU-3.C.3.b lists creating a lame-duck period and weakening accountability among the disadvantages, while EK PAU-3.C.3.a lists opportunities for new leaders and the focus on governing rather than winning elections among the advantages."),
 dict(q="Which course country's president does the framework describe as restricted to one term?",
   choices=[
     "Mexico",
     "Nigeria",
     "Russia",
     "China",
     "the United Kingdom"], ans=0,
   why="EK PAU-3.C.2.c states that Mexico's president is restricted to one term, in the same sentence that describes the office as head of state and head of government, commander in chief and leader of the bureaucracy. This is one of only two term-limit figures the framework prints."),
 dict(q="What does the framework say about the term of Iran's president?",
   choices=[
     "the president is elected for up to two four-year terms",
     "the president serves a single six-year term",
     "the president serves without a fixed term at the Supreme Leader's pleasure",
     "the president may serve any number of consecutive terms",
     "the president's term is set by the Guardian Council before each election"], ans=0,
   why="EK PAU-3.C.2.b states that Iran's president is elected for up to two 4-year terms, oversees the civil service and conducts foreign policy. This and Mexico's one-term restriction are the only term-limit figures in the framework."),
 dict(q="For which set of course countries does the framework state NO term limit for the chief executive?",
   choices=[
     "China, Nigeria, Russia and the United Kingdom",
     "Iran and Mexico",
     "Mexico and Nigeria",
     "all six course countries",
     "none of the six course countries"], ans=0,
   why="EK PAU-3.C.2.b and EK PAU-3.C.2.c give figures for Iran and Mexico respectively, and no essential knowledge statement gives one for the other four. Asserting a limit for any of those four would go beyond what the framework supports."),
 dict(q="A student proposes to answer an examination question by citing one course country's 2018 removal of presidential term limits. Why is that citation weak in this course?",
   choices=[
     "the framework mentions it only in an optional sample instructional activity, not in any essential knowledge statement",
     "the framework states that no country has ever removed a term limit",
     "the framework states that term limits cannot be removed once adopted",
     "the framework assigns that country a two-term limit instead",
     "the framework does not name that country as a course country"], ans=0,
   why="The removal appears in the Unit 2 sample instructional activities rather than in any essential knowledge statement, and the essential knowledge statements are what the course content is. EK PAU-3.C.2.a describes that country's executive without stating any term limit at all."),
 dict(q="Which evidence would most directly support a claim that executive term limits promote stability?",
   choices=[
     "In systems with term limits, executives leave office at scheduled dates far more often than they are removed by crisis or force",
     "In systems with term limits, executives serve longer on average",
     "In systems with term limits, more legislation is proposed each year",
     "In systems with term limits, cabinets are larger",
     "In systems with term limits, the legislature meets for more days"], ans=0,
   why="EK PAU-3.C.3 frames the whole question in terms of promoting stability and effective policies, and EK PAU-3.C.3.a attributes to term limits a check on executive power and the inhibition of dictators and personality rule. A scheduled, predictable departure is what those advantages amount to in observable terms."),
 dict(q="Which evidence would most directly support a claim that executive term limits harm effective policy?",
   choices=[
     "Long-term programmes are abandoned at each change of executive, and the incoming officeholder repeatedly reverses the predecessor's approach",
     "Executives with term limits appoint more ministers from outside the legislature",
     "Executives with term limits give more speeches in their final year",
     "Systems with term limits hold elections on fixed dates",
     "Systems with term limits have more political parties"], ans=0,
   why="EK PAU-3.C.3.b lists impeding policy continuity, insufficient time to achieve goals and poorly designed policy among the disadvantages, and repeated abandonment and reversal of programmes is the observable form those take. The rejected findings bear on none of the seven listed disadvantages."),
 dict(q="The table reports hypothetical figures for three groups of cases. Which row most directly supports the framework's claim that term limits check executive power and inhibit personality rule?",
   table=_T_TL,
   choices=[
     "the group with no term limit, whose executives hold office more than twice as long on average and least often leave at a scheduled date",
     "the group with a one-term limit, whose executives hold office for the shortest time",
     "the group with a two-term limit, whose executives most often leave at a scheduled date",
     "no row, since the table reports nothing about how long executives serve",
     "all three rows equally, since each reports a mean tenure"], ans=0,
   why="EK PAU-3.C.3.a attributes to term limits a check on executive power and the inhibition of dictators and personality rule, so the supporting evidence is the contrast case: where no limit applies, tenures run longest and scheduled departures are least common."),
 dict(q="Using the same table, which row most directly supports the framework's claim that term limits impede policy continuity?",
   table=_T_TL,
   choices=[
     "the group with a one-term limit, which records the most reversals of existing policy per decade",
     "the group with no term limit, which records the fewest reversals per decade",
     "the group with a two-term limit, whose executives serve longest on average",
     "no row, since the table reports nothing about policy",
     "all three rows equally, since each records some reversals"], ans=0,
   why="EK PAU-3.C.3.b lists impeding policy continuity among the disadvantages of term limits, so the supporting row is the one whose executives turn over fastest and whose policy reversals are most frequent. The row with no limit records the fewest reversals, which is the same claim seen from the other side."),
 dict(q="A student concludes from the same table that term limits are simply beneficial. Which objection combines the framework and the data most directly?",
   table=_T_TL,
   choices=[
     "The framework states that term limits have advantages and disadvantages, and the table shows the limited groups leading on scheduled departures while also recording more policy reversals",
     "The framework states that term limits have only disadvantages",
     "The table reports nothing about term-limit rules",
     "The table shows the group with no term limit leading on every measure",
     "The framework states that term limits apply in all six course countries"], ans=0,
   why="EK PAU-3.C.3 states that term limits have advantages AND disadvantages with regard to promoting stability and effective policies, and the table's columns point in opposite directions for the same rows. The data reproduce the framework's two-sidedness rather than settling it."),
 dict(q="The table reports hypothetical outcomes across the four years of a chief executive's single permitted term. Which pattern does it show, and which of the framework's points does that pattern illustrate?",
   table=_T_LAME,
   choices=[
     "Bills passed fall and bills defeated rise as the term proceeds, which illustrates the lame-duck period the framework lists as a disadvantage",
     "Bills passed rise and bills defeated fall as the term proceeds, which illustrates growing executive authority",
     "Bills passed and bills defeated are unchanged across the four years, which illustrates policy continuity",
     "Bills passed rise while bills defeated also rise, which illustrates an expanding legislative programme",
     "The table reports nothing about the fate of executive-proposed bills"], ans=0,
   why="EK PAU-3.C.3.b lists creating a lame-duck period for the officeholder among the disadvantages of term limits. Reading the two columns year by year, one falls at every step while the other rises at every step, which is that period appearing in data."),
 dict(q="According to the same table, the total number of bills the executive proposed across the four years is",
   table=_T_LAME,
   choices=[
     "95",
     "61",
     "34",
     "23",
     "48"], ans=0,
   why="Every proposed bill was either passed or defeated, so the total is the sum of both columns across all four years. The alternatives arise from adding only one of the two columns, from summing a single year, or from adding the two largest rows only."),
 dict(q="According to the same table, the share of the executive's proposed bills that passed in the final year of the term was closest to",
   table=_T_LAME,
   choices=[
     "26 percent",
     "74 percent",
     "88 percent",
     "61 percent",
     "39 percent"], ans=0,
   why="Dividing the bills passed in the final year by that year's total of passed and defeated bills gives the share. Each alternative is a real share drawn from the wrong cell or the wrong year: the complementary defeat share, the first year's passage share, and the third year's passage and defeat shares."),
 dict(q="Which restatement of the framework's disadvantage 'weaken accountability' stays within what the framework supports?",
   choices=[
     "an executive who cannot stand again is not on any future ballot, so voters have no further election at which to judge that record",
     "an executive who cannot stand again may ignore the law entirely",
     "an executive who cannot stand again loses the power to propose legislation",
     "an executive who cannot stand again must be removed by impeachment",
     "an executive who cannot stand again is no longer answerable to the courts"], ans=0,
   why="EK PAU-3.C.3.b lists weakening accountability without explaining the mechanism, and EK DEM-2.B.2 grounds accountability in voters knowing whose record is on the ballot at the next election. Immunity from law, loss of legislative initiative, forced impeachment and freedom from the courts are consequences the framework never attaches to a term limit."),
 dict(q="Which statement best captures the trade-off the framework describes?",
   choices=[
     "The same guaranteed turnover that checks executive power and brings new leaders forward also interrupts policy and denies an officeholder time and experience",
     "Term limits check executive power at no cost to policy",
     "Term limits interrupt policy without checking executive power",
     "Term limits affect neither executive power nor policy",
     "Term limits are recommended by the framework for every course country"], ans=0,
   why="EK PAU-3.C.3.a and EK PAU-3.C.3.b describe the same institutional feature, a scheduled and unavoidable change of officeholder, from opposite sides. The framework presents the trade-off rather than recommending a rule, and it attaches term-limit figures to only two of the six course countries."),
 dict(q="Which finding would most directly WEAKEN a claim that term limits inhibit the emergence of personality rule?",
   choices=[
     "In several term-limited systems the outgoing executive continued to direct policy from outside the office through a chosen successor",
     "In several term-limited systems executives left office on the scheduled date",
     "In several term-limited systems the legislature passed most executive bills",
     "In several term-limited systems turnout rose at the following election",
     "In several term-limited systems the cabinet was reshuffled before the term ended"], ans=0,
   why="EK PAU-3.C.3.a claims that term limits check executive power and inhibit the emergence of dictators and personality rule, so the finding that weakens it is one showing personal rule surviving the departure from office. Scheduled departures, legislative success, turnout and reshuffles are all consistent with the claim."),
 dict(q="An executive in the final year of a single permitted term finds that ministers, legislators and foreign counterparts increasingly deal with the presumed successor instead. Which of the framework's listed disadvantages does this illustrate?",
   choices=[
     "the lame-duck period created for the officeholder",
     "the forcing of good executives from office",
     "the prevention of the officeholder from building experience",
     "the causing of poorly designed policy",
     "the allowance of insufficient time to achieve goals"], ans=0,
   why="EK PAU-3.C.3.b lists creating a lame-duck period for the officeholder among the disadvantages, and the scenario describes exactly the loss of leverage that arises when a departure is scheduled. The other listed disadvantages concern who leaves, what the officeholder can accumulate, the quality of policy and the time available."),
 dict(q="Taking the framework's account of executive term limits together, which summary is most accurate?",
   choices=[
     "Term limits are presented as a trade-off with three named advantages and seven named disadvantages for stability and effective policy, and the framework attaches a term-limit figure to only two of the six course countries",
     "Term limits are presented as unambiguously good, and every course country has one",
     "Term limits are presented as unambiguously bad, and no course country has one",
     "Term limits are presented as irrelevant to stability and policy effectiveness",
     "Term limits are presented as a feature only of parliamentary systems"], ans=0,
   why="EK PAU-3.C.3 opens with advantages and disadvantages regarding stability and effective policies, EK PAU-3.C.3.a lists three of the first and EK PAU-3.C.3.b seven of the second, and EK PAU-3.C.2.b and EK PAU-3.C.2.c are the only statements attaching a figure to a country."),
]
