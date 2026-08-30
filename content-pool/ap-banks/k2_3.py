# AP COMPARATIVE GOVERNMENT AND POLITICS 2.3 Executive Systems
# CED effective Fall 2026, Unit 2 Political Institutions. Enduring understanding
# PAU-3; learning objective PAU-3.C (explain the structure, function, and change
# of executive leadership in course countries). Suggested skill 1.D.
#
# Essential knowledge relied on:
#   PAU-3.C.1  governments have executive institutions, including CHIEF EXECUTIVES
#              AND CABINETS, that FORMULATE, IMPLEMENT AND ENFORCE policy through
#              different methods and agencies
#   PAU-3.C.2  titles, powers, structure and functions vary across the six:
#     .a CHINA -- the president serves as commander in chief, chair of China's
#        Military Commission, and General Secretary of the Chinese Communist
#        party; the president nominates the PREMIER, who serves as HEAD OF
#        GOVERNMENT overseeing the civil service; changes in top leadership are
#        accomplished BEHIND CLOSED DOORS
#     .b IRAN -- the SUPREME LEADER sets the political agenda, serves as commander
#        in chief, and appoints top ministers, the Expediency Council, HALF of the
#        Guardian Council, and the head of the judiciary. The PRESIDENT is elected
#        for UP TO TWO 4-YEAR TERMS, oversees the civil service, and conducts
#        foreign policy
#     .c MEXICO -- the elected president is BOTH head of state and head of
#        government, commander in chief and leader of the bureaucracy, can approve
#        domestic legislation and lead foreign policy; RESTRICTED TO ONE TERM
#     .d NIGERIA -- the elected president is BOTH head of state and head of
#        government, chief executive, commander in chief, and head of civil
#        service, and can approve domestic legislation and conduct foreign policy
#     .e RUSSIA -- the PRIME MINISTER is head of government and oversees the civil
#        service; the elected PRESIDENT is head of state and commander in chief,
#        appoints top ministers, conducts foreign policy, and PRESIDES OVER THE
#        DUMA UNDER CERTAIN CONDITIONS
#     .f UNITED KINGDOM -- the MONARCH serves CEREMONIALLY as head of state and
#        FORMALLY appoints as prime minister the leader of the party or coalition
#        holding the largest number of seats in the Commons. The PRIME MINISTER can
#        call elections, sets the foreign policy agenda, and serves as DE FACTO
#        commander in chief and chief executive over the civil service
#
# TWO NUMBERS AND ONE HEDGE THE FRAMEWORK ACTUALLY PRINTS, and the ones it does
# not: Iran's president serves UP TO TWO 4-YEAR TERMS and Mexico's president is
# RESTRICTED TO ONE TERM. No term-limit figure is given for China, Nigeria, Russia
# or the United Kingdom, and no length is given for Mexico's single term, so no
# item asks for either (AP_COMP_GOV_CED.md note 7). The hedge is 'de facto' in the
# United Kingdom case, which item 28 keys.
#
# Half of the Guardian Council, not all of it (AP_COMP_GOV_CED.md note 8).
#
# Table cases are HYPOTHETICAL and labelled so; the term-limit table deliberately
# carries term LENGTHS the framework does not state for any country, which is why
# its rows are lettered cases rather than named countries.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("2.3", "Executive Systems", 2)

_T_EXEC = dict(
    headers=["Case (hypothetical)", "Head of state", "Head of government",
             "Who commands the armed forces"],
    rows=[["Case A", "an elected president", "the same elected president",
           "the elected president"],
          ["Case B", "a hereditary monarch, ceremonially",
           "the leader of the largest party in the elected chamber",
           "the head of government, in fact rather than in form"],
          ["Case C", "an elected president", "a prime minister who oversees the civil service",
           "the elected president"]])

_T_TERM = dict(
    headers=["Case (hypothetical)", "Maximum consecutive terms permitted for the chief executive",
             "Length of one term, in years", "Maximum consecutive years in office"],
    rows=[["Case D", "1", "6", "6"],
          ["Case E", "2", "4", "8"],
          ["Case F", "3", "5", "15"]])

QUESTIONS = [
 dict(q="According to the framework, what do executive institutions do?",
   choices=[
     "they formulate, implement and enforce policy through different methods and agencies",
     "they make law and hear appeals from lower courts",
     "they certify election results and register political parties",
     "they interpret the constitution and resolve disputes between levels of government",
     "they exist only in presidential systems"], ans=0,
   why="EK PAU-3.C.1 states that governments have executive institutions, including chief executives and cabinets, that formulate, implement and enforce policy through different methods and agencies. Lawmaking, adjudication and electoral administration are assigned elsewhere in the framework."),
 dict(q="Which combination of roles does the framework assign to China's president?",
   choices=[
     "commander in chief, chair of China's Military Commission, and General Secretary of the Chinese Communist party",
     "head of government overseeing the civil service, nominated by the premier",
     "ceremonial head of state who formally appoints the head of government",
     "head of state and head of government elected directly by voters to a single term",
     "an official who sets the political agenda and appoints the head of the judiciary"], ans=0,
   why="EK PAU-3.C.2.a assigns China's president the roles of commander in chief, chair of China's Military Commission and General Secretary of the Chinese Communist party. The rejected descriptions belong to the premier, to the United Kingdom's monarch, to Mexico's president and to Iran's Supreme Leader."),
 dict(q="Which combination of powers does the framework assign to Iran's Supreme Leader?",
   choices=[
     "setting the political agenda, serving as commander in chief, and appointing top ministers, the Expediency Council, half of the Guardian Council, and the head of the judiciary",
     "overseeing the civil service and conducting foreign policy after election to a four-year term",
     "approving domestic legislation as head of state and head of government",
     "formally appointing the leader of the largest party in the elected chamber",
     "presiding over the lower chamber of the legislature under certain conditions"], ans=0,
   why="EK PAU-3.C.2.b assigns exactly these powers to the Supreme Leader, and specifies HALF of the Guardian Council rather than all of it. The rejected descriptions belong to Iran's elected president, to Mexico's and Nigeria's presidents, to the United Kingdom's monarch and to Russia's president."),
 dict(q="One course country's chief executive is elected, serves as commander in chief and leader of the bureaucracy, may approve domestic legislation and lead foreign policy, and may not serve a second term. Whose office does the framework describe this way?",
   choices=[
     "Mexico's president",
     "Nigeria's president",
     "Russia's president",
     "Iran's president",
     "the United Kingdom's prime minister"], ans=0,
   why="EK PAU-3.C.2.c describes Mexico's elected president as commander in chief and leader of the bureaucracy, able to approve domestic legislation and lead foreign policy, and restricted to one term. That restriction is one of only two term-limit figures the framework prints, and it is what separates this office from the otherwise similar one described at EK PAU-3.C.2.d."),
 dict(q="The framework describes one chief executive as holding the roles of head of state, head of government, chief executive, commander in chief, and head of the civil service all at once. Whose office is this?",
   choices=[
     "Nigeria's president",
     "Russia's prime minister",
     "China's premier",
     "Iran's president",
     "the United Kingdom's monarch"], ans=0,
   why="EK PAU-3.C.2.d lists exactly these roles for Nigeria's elected president, adding that the officeholder can approve domestic legislation and conduct foreign policy. Each rejected office holds only some of the five under EK PAU-3.C.2.a, .b, .e and .f."),
 dict(q="How does the framework divide executive roles in Russia?",
   choices=[
     "the prime minister is head of government and oversees the civil service, while the elected president is head of state and commander in chief, appoints top ministers and conducts foreign policy",
     "the elected president is both head of state and head of government and oversees the civil service",
     "a ceremonial head of state appoints the head of government from the largest party",
     "the head of the judiciary appoints the head of government",
     "an unelected leader sets the political agenda and the elected president implements it"], ans=0,
   why="EK PAU-3.C.2.e divides the roles exactly this way. The split between a head of government running the administration and an elected head of state holding command and foreign policy is what EK PAU-3.A.3's semi-presidential definition leads one to expect."),
 dict(q="How does the framework describe the executive arrangement in the United Kingdom?",
   choices=[
     "the monarch serves ceremonially as head of state and formally appoints as prime minister the leader of the party or coalition holding the largest number of seats in the elected chamber",
     "the monarch chooses the prime minister from among the party leaders at the monarch's discretion",
     "the prime minister is elected directly by voters at a separate national election",
     "the prime minister is nominated by the head of state and approved by the legislature",
     "the head of state and head of government are the same elected person"], ans=0,
   why="EK PAU-3.C.2.f states that the monarch serves ceremonially as head of state and FORMALLY appoints as prime minister the leader of the party or coalition holding the largest number of seats in the House of Commons. The seat count decides the outcome, which is what makes the role ceremonial."),
 dict(q="Who does the framework identify as China's head of government, and how does that officeholder reach the post?",
   choices=[
     "the premier, nominated by the president",
     "the president, elected by the legislature",
     "the General Secretary of the party, chosen by a popular vote",
     "the chair of the Military Commission, appointed by the premier",
     "the head of the judiciary, appointed by the president"], ans=0,
   why="EK PAU-3.C.2.a states that China's president nominates the premier of the National People's Congress, who in turn serves as head of government overseeing the civil service. The president holds a different set of roles under the same statement."),
 dict(q="What does the framework say about how changes in China's top leadership are accomplished?",
   choices=[
     "behind closed doors",
     "by a national popular vote among competing candidates",
     "by a vote of the eight parties permitted to exist alongside the governing party",
     "by the head of the judiciary on the advice of the premier",
     "by a referendum requiring an absolute majority"], ans=0,
   why="EK PAU-3.C.2.a states that changes in top leadership are accomplished behind closed doors. EK PAU-1.D.1.a locates that regime's stability in the Communist Party's control, and a succession settled outside public institutions is a succession settled by the party."),
 dict(q="Which description of Iran's president is consistent with the framework?",
   choices=[
     "elected for up to two four-year terms, overseeing the civil service and conducting foreign policy",
     "appointed by the Supreme Leader and serving without a fixed term",
     "elected for a single term and serving as commander in chief",
     "nominated by the head of the judiciary and approved by the legislature",
     "serving as both head of state and head of government with no term limit"], ans=0,
   why="EK PAU-3.C.2.b states that Iran's president is elected for up to two 4-year terms, oversees the civil service, and conducts foreign policy. Command of the armed forces and the setting of the political agenda belong to the Supreme Leader under the same statement."),
 dict(q="How much of Iran's Guardian Council does the framework say the Supreme Leader appoints?",
   choices=[
     "half of it",
     "all of it",
     "none of it",
     "one member only",
     "as many members as the Majles approves"], ans=0,
   why="EK PAU-3.C.2.b states that the Supreme Leader appoints half of the Guardian Council, and EK PAU-3.G.1.b adds that the head of the judiciary can nominate the other half with approval by the Majles. The framework says half in both places."),
 dict(q="Which power does the framework assign to Russia's president in relation to the lower chamber of the legislature?",
   choices=[
     "presiding over it under certain conditions",
     "appointing all of its members",
     "dissolving it at any time without condition",
     "serving as its speaker for the duration of each session",
     "casting a vote in every division"], ans=0,
   why="EK PAU-3.C.2.e states that Russia's elected president presides over the Duma under certain conditions, alongside being head of state and commander in chief, appointing top ministers and conducting foreign policy. EK PAU-3.E.1.e describes the Duma as elected, so its members are not presidential appointees."),
 dict(q="Which combination of powers does the framework assign to the United Kingdom's prime minister?",
   choices=[
     "calling elections, setting the foreign policy agenda, and serving as de facto commander in chief and chief executive over the civil service",
     "formally appointing the head of state and dissolving the courts",
     "nominating half the members of an upper chamber and the head of the judiciary",
     "presiding over the elected chamber under certain conditions",
     "serving as head of state as well as head of government"], ans=0,
   why="EK PAU-3.C.2.f assigns the prime minister the power to call elections, the setting of the foreign policy agenda, and the roles of de facto commander in chief and chief executive over the civil service. The head of state remains the monarch under the same statement."),
 dict(q="What role does the framework assign to the United Kingdom's monarch?",
   choices=[
     "serving ceremonially as head of state",
     "serving as head of government and chief executive",
     "commanding the armed forces in fact as well as in form",
     "setting the foreign policy agenda",
     "calling general elections"], ans=0,
   why="EK PAU-3.C.2.f states that the monarch serves ceremonially as head of state and formally appoints the prime minister. Every rejected role is assigned by the same statement to the prime minister instead."),
 dict(q="Which comparison of who commands the armed forces is consistent with the framework?",
   choices=[
     "In Iran the Supreme Leader is commander in chief, whereas in Nigeria the elected president is",
     "In Iran the elected president is commander in chief, whereas in Nigeria the head of the judiciary is",
     "In both countries the head of government commands the armed forces without holding the office of head of state",
     "In neither country does the framework identify a commander in chief",
     "In both countries an unelected office commands the armed forces"], ans=0,
   why="EK PAU-3.C.2.b makes Iran's Supreme Leader commander in chief while EK PAU-3.C.2.d makes Nigeria's elected president commander in chief as well as head of state and head of government. The contrast is between an unelected and an elected holder of the same function."),
 dict(q="Which comparison of Mexico's and Nigeria's presidencies is consistent with the framework?",
   choices=[
     "Both are elected leaders serving as head of state and head of government, but the framework states a one-term restriction for only one of them",
     "Both are elected leaders restricted to a single term",
     "Neither serves as head of state",
     "One is elected and the other is appointed by the legislature",
     "Both share executive authority with a prime minister who oversees the civil service"], ans=0,
   why="EK PAU-3.C.2.c and EK PAU-3.C.2.d describe the two presidencies in almost identical terms, and only the first adds that the president is restricted to one term. The framework prints no term-limit figure for Nigeria, so asserting one would go beyond it."),
 dict(q="Which comparison of the executive arrangements in China and Russia is consistent with the framework?",
   choices=[
     "In both, a head of government oversees the civil service while a separate president holds command of the armed forces, but the framework has one nominated by the president and the other reaching office in a system with separate popular elections",
     "In both, the head of government is elected directly by voters",
     "In both, the president is both head of state and head of government",
     "In neither is there a head of government distinct from the president",
     "In both, the head of government is appointed by the head of the judiciary"], ans=0,
   why="EK PAU-3.C.2.a has China's president nominating a premier who serves as head of government overseeing the civil service, and EK PAU-3.C.2.e has Russia's prime minister as head of government overseeing the civil service alongside an elected president who is commander in chief. EK PAU-3.A.3 supplies Russia's separate popular elections."),
 dict(q="Which comparison of Iran's Supreme Leader and the United Kingdom's monarch is consistent with the framework?",
   choices=[
     "One holds an unelected office that sets the political agenda and commands the armed forces, while the other holds an unelected office that is ceremonial",
     "Both hold unelected offices that set the political agenda",
     "Both hold ceremonial offices with no policy role",
     "One is elected for up to two four-year terms and the other is hereditary",
     "Both appoint the head of the judiciary"], ans=0,
   why="EK PAU-3.C.2.b gives the Supreme Leader the political agenda, command in chief and a set of appointments, while EK PAU-3.C.2.f describes the monarch as serving ceremonially and appointing the prime minister only formally. Both offices are unelected, which is why the contrast has to be drawn on powers rather than on selection."),
 dict(q="In which pair of course countries does the framework describe an executive in which the same person is head of state and head of government?",
   choices=[
     "Mexico and Nigeria",
     "China and Russia",
     "Iran and the United Kingdom",
     "Russia and the United Kingdom",
     "China and Iran"], ans=0,
   why="EK PAU-3.C.2.c and EK PAU-3.C.2.d both describe an elected president who is both head of state and head of government. The rejected pairs each contain at least one country whose head of state and head of government are different officeholders under EK PAU-3.C.2.a, .b, .e and .f."),
 dict(q="The table describes three hypothetical executive arrangements. Which case matches the framework's description of Mexico's and Nigeria's executives?",
   table=_T_EXEC,
   choices=[
     "Case A, in which one elected president is head of state, head of government, and commander of the armed forces",
     "Case B, in which a ceremonial monarch is head of state",
     "Case C, in which a prime minister is head of government and an elected president commands the armed forces",
     "None of the three, since the framework describes no such arrangement",
     "All three equally, since each has a head of state and a head of government"], ans=0,
   why="EK PAU-3.C.2.c and EK PAU-3.C.2.d both describe an elected president who is head of state, head of government and commander in chief. Only one row of the table puts all three roles in the same elected officeholder."),
 dict(q="Using the same table, which case matches the framework's description of the United Kingdom's executive?",
   table=_T_EXEC,
   choices=[
     "Case B, in which a ceremonial hereditary head of state coexists with a head of government drawn from the largest party in the elected chamber and commanding the armed forces in fact rather than in form",
     "Case A, in which one elected president holds every executive role",
     "Case C, in which an elected president commands the armed forces",
     "None of the three, since the United Kingdom has no head of government",
     "All three, since each row names a head of government"], ans=0,
   why="EK PAU-3.C.2.f describes a ceremonial monarch as head of state, a prime minister drawn from the party or coalition with the largest number of Commons seats, and that prime minister as DE FACTO commander in chief. Only one row carries all three features, including the 'in fact rather than in form' qualification."),
 dict(q="Using the same table, which case matches the framework's description of Russia's executive?",
   table=_T_EXEC,
   choices=[
     "Case C, in which an elected president is head of state and commands the armed forces while a prime minister is head of government overseeing the civil service",
     "Case A, in which one elected president is also head of government",
     "Case B, in which a hereditary monarch is head of state",
     "None of the three, since Russia has no prime minister",
     "Both Case A and Case C, since each has an elected president"], ans=0,
   why="EK PAU-3.C.2.e has Russia's prime minister as head of government overseeing the civil service and the elected president as head of state and commander in chief. Only one row separates the two roles that way while keeping the head of state elected."),
 dict(q="The table reports three hypothetical term-limit arrangements. Which case is consistent with the framework's statement about the course country whose president is restricted to one term?",
   table=_T_TERM,
   choices=[
     "Case D, which permits one consecutive term",
     "Case E, which permits two consecutive terms",
     "Case F, which permits three consecutive terms",
     "None of the three, since the framework states no term limit for any country",
     "All three, since each states a maximum"], ans=0,
   why="EK PAU-3.C.2.c states that Mexico's president is restricted to one term, so the arrangement that matches is the one permitting a single consecutive term. The framework does print term limits, for two of the six countries, which is why the option denying that fails."),
 dict(q="Using the same table, which case is consistent with the framework's statement that one course country's president is elected for up to two four-year terms?",
   table=_T_TERM,
   choices=[
     "Case E, which permits two consecutive terms of four years each",
     "Case D, which permits one consecutive term",
     "Case F, which permits three consecutive terms",
     "None of the three, since no case states a term length",
     "Both Case D and Case E, since each permits at least one term"], ans=0,
   why="EK PAU-3.C.2.b states that Iran's president is elected for up to two 4-year terms, so both the number of terms and the length must match. Only one row carries both figures together, and every row in the table states a term length."),
 dict(q="According to the same table, which case reports the largest maximum number of consecutive years in office, and how does that figure arise?",
   table=_T_TERM,
   choices=[
     "Case F, at 15 years, which is its three permitted terms multiplied by its five-year term length",
     "Case E, at 8 years, which is the largest figure in the table",
     "Case D, at 6 years, since its single term is the longest",
     "Case F, at 5 years, since that is the length of one term",
     "The table does not report maximum consecutive years"], ans=0,
   why="Multiplying each case's permitted number of terms by its term length reproduces the final column, and the largest product is the answer. The alternatives quote a smaller row's product, a single term length, and a figure that is not the maximum."),
 dict(q="In one country the person who commands the armed forces and sets the political agenda is not elected to that office, while a separately elected official runs the civil service and conducts foreign policy. Which course country does the framework describe this way?",
   choices=[
     "Iran",
     "Mexico",
     "Nigeria",
     "the United Kingdom",
     "China"], ans=0,
   why="EK PAU-3.C.2.b gives Iran's unelected Supreme Leader the political agenda and command in chief while giving the elected president oversight of the civil service and the conduct of foreign policy. No other course country is described with that particular division."),
 dict(q="In a second country the head of government oversees the civil service after being nominated by a president who is also the governing party's General Secretary and chairs the military commission. Which course country does the framework describe this way?",
   choices=[
     "China",
     "Russia",
     "Iran",
     "Nigeria",
     "the United Kingdom"], ans=0,
   why="EK PAU-3.C.2.a describes China's president as commander in chief, chair of China's Military Commission and General Secretary of the Chinese Communist party, nominating the premier who serves as head of government overseeing the civil service. The party office is what distinguishes this from Russia's arrangement."),
 dict(q="The framework calls the United Kingdom's prime minister the DE FACTO commander in chief. The point of that qualification is that",
   choices=[
     "the formal position belongs to the head of state while the power is exercised by the head of government",
     "the prime minister commands the armed forces only during a declared emergency",
     "the prime minister has no role in defence policy at all",
     "the office of commander in chief does not exist in that country",
     "the prime minister commands the armed forces only with the legislature's consent"], ans=0,
   why="EK PAU-3.C.2.f describes the monarch as serving ceremonially as head of state and the prime minister as serving as de facto commander in chief and chief executive over the civil service. The phrase separates where the form of the office sits from where the power is exercised, the same distinction EK PAU-3.E.1.a and EK PAU-3.F.1.a draw for China."),
 dict(q="Which executive in the framework's account appoints the head of the judiciary?",
   choices=[
     "Iran's Supreme Leader",
     "Mexico's president, without any confirmation",
     "the United Kingdom's monarch",
     "China's premier",
     "Russia's prime minister"], ans=0,
   why="EK PAU-3.C.2.b states that the Supreme Leader appoints the head of the judiciary, and EK PAU-3.G.1.b repeats it. EK PAU-3.G.1.d has Mexico's Supreme Court magistrates nominated by the president and approved by the Senate, and EK PAU-3.G.1.h has Russia's judges nominated by the president and approved by the Federation Council."),
 dict(q="Taking the framework's account of the six executives together, which summary is most accurate?",
   choices=[
     "Executive institutions everywhere formulate, implement and enforce policy, but the titles, powers and division of roles differ across the six, with head of state and head of government sometimes fused and sometimes separate",
     "All six countries divide the roles of head of state and head of government between two officeholders",
     "All six countries fuse the roles of head of state and head of government in one officeholder",
     "The framework describes the executives of the six countries as institutionally identical",
     "Executive institutions in the six countries make law as well as enforcing it"], ans=0,
   why="EK PAU-3.C.1 supplies the common function and EK PAU-3.C.2 opens by stating that titles, powers, structure and functions vary across the six countries. EK PAU-3.C.2.c and .d fuse the two roles while EK PAU-3.C.2.a, .b, .e and .f separate them, so neither uniform claim survives."),
]
